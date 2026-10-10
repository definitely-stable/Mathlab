"""UCT-005 D1-B2-F2: independent full-page crash-prefix ordering oracle.

This is a *separate* finite state-machine model of two addressed bitmap slots,
NOT real filesystem crash safety. The only durable assumptions are atomic
complete page images, order-preserving durable writes and a separately atomic,
monotone trusted (generation, digest) publication. No server availability,
cryptographic SHA security theorem, or real power-loss guarantee is inferred.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
from math import ceil

from uct005_d1b2d_remote_pin_bitmap import RemotePinBitmapF1

DOMAIN = RemotePinBitmapF1._DOMAIN


class RecoveryAbort(RuntimeError):
    """No fallback to the other bitmap slot on an absent/bad trusted page."""


def digest(generation: int, payload: bytes) -> bytes:
    if type(generation) is not int or not 0 <= generation < (1 << 64):
        raise ValueError("invalid trusted bitmap generation")
    return hashlib.sha256(DOMAIN + generation.to_bytes(8, "big") + payload).digest()


def framed_pages(payload: bytes, P: int) -> dict[int, bytes]:
    if type(P) is not int or P < 1 or not payload:
        raise ValueError("positive P and nonempty payload required")
    return {j: payload[j * P:(j + 1) * P].ljust(P, b"\0")
            for j in range(ceil(len(payload) / P))}


@dataclass(frozen=True)
class Recovery:
    trusted_generation: int
    bitmap: bytes
    page_attempts: int
    page_reads: int
    request_bytes: int
    response_bytes: int
    hash_input_bytes: int


def recover(slots: dict[int, dict[int, bytes]], generation: int,
            expected_digest: bytes, B: int, P: int) -> Recovery:
    """Read *only* the slot authorized by the trusted generation.

    The 8-byte page address per read is charged even on missing pages. Every
    successful page reply is a complete P-byte transfer. The digest covers
    the unpadded bitmap only; nonzero padding is rejected before acceptance.
    """
    if type(B) is not int or B < 1 or type(P) is not int or P < 1:
        raise ValueError("invalid bitmap/page dimensions")
    if type(expected_digest) is not bytes or len(expected_digest) != 32:
        raise ValueError("trusted digest must be 32 bytes")
    if type(generation) is not int or not 0 <= generation < (1 << 64):
        raise ValueError("invalid generation")
    slot = slots.get(generation & 1, {})
    pages = ceil(B / P)
    hashed = hashlib.sha256(DOMAIN + generation.to_bytes(8, "big"))
    attempts = replies = 0
    data = bytearray()
    for j in range(pages):
        attempts += 1
        frame = slot.get(j)
        if type(frame) is not bytes or len(frame) != P:
            raise RecoveryAbort("trusted active bitmap page missing or truncated")
        replies += 1
        take = min(P, B - j * P)
        if any(frame[take:]):
            raise RecoveryAbort("noncanonical last-page padding")
        data.extend(frame[:take])
        hashed.update(frame[:take])
    if hashed.digest() != expected_digest:
        raise RecoveryAbort("active bitmap violates trusted digest/generation")
    return Recovery(generation, bytes(data), attempts, replies, 8 * attempts,
                    P * replies, len(DOMAIN) + 8 + B)


def crash_prefix(C: int, P: int, reader: int, epoch: int, prefix: int,
                 *, order: str = "canonical",
                 tamper: str | None = None) -> dict:
    """Simulate prefixes of stage-writes -> anchor-publish -> retire-old.

    Canonical trace has M stage writes, one trusted anchor publication,
    then M old-slot DROP_PAGE operations: 2M+1 operations, 2M+2 cuts.
    Alternative order=publish-first/retire-first are intentional negative
    schedules. Attacks modify one page after the crash cut and before
    recovery; no untrusted slot fallback is available.
    """
    if (type(C) is not int or not 2 <= C <= 65536
            or type(P) is not int or P < 1
            or reader not in (0, 1) or type(reader) is not int
            or type(epoch) is not int or not 0 <= epoch < C):
        raise ValueError("invalid finite PIN capacity/reader/epoch/page")
    B = ceil(2 * C / 8)
    M = ceil(B / P)
    if type(prefix) is not int or not 0 <= prefix <= 2 * M + 1:
        raise ValueError("crash prefix outside paid transition schedule")
    if order not in ("canonical", "publish-first", "retire-first"):
        raise ValueError("unrecognized schedule")
    if tamper not in (None, "active-flip", "active-missing", "active-padding"):
        raise ValueError("unrecognized adversary")
    old = bytes(B)
    edited = bytearray(old)
    index = 2 * epoch + reader
    edited[index >> 3] |= (1 << (index & 7))
    new = bytes(edited)
    old_frames, new_frames = framed_pages(old, P), framed_pages(new, P)
    slots = {0: dict(old_frames), 1: {}}
    generation, commitment = 0, digest(0, old)
    writes = publications = drops = 0

    actions = [("stage", j) for j in range(M)] + [("publish", 0)] + [
        ("retire", j) for j in range(M)]
    if order == "publish-first":
        actions = [actions[M]] + actions[:M] + actions[M + 1:]
    elif order == "retire-first":
        actions = [actions[M + 1]] + actions[:M + 1] + actions[M + 2:]

    for action, page in actions[:prefix]:
        if action == "stage":
            slots[1][page] = new_frames[page]
            writes += 1
        elif action == "publish":
            generation, commitment = 1, digest(1, new)
            publications += 1
        else:
            slots[0].pop(page, None)
            drops += 1

    if tamper is not None:
        active = slots[generation & 1]
        last = M - 1
        if tamper == "active-missing":
            active.pop(0, None)
        elif tamper == "active-flip":
            if 0 in active:
                page = bytearray(active[0])
                page[0] ^= 1
                active[0] = bytes(page)
        else:
            if M * P == B:
                raise ValueError("padding attack needs a padded final page")
            if last in active:
                page = bytearray(active[last])
                page[-1] = 1
                active[last] = bytes(page)

    try:
        result = recover(slots, generation, commitment, B, P)
        accepted = True
    except RecoveryAbort:
        result = None
        accepted = False
    return {
        "C": C, "P": P, "B": B, "M": M,
        "prefix": prefix, "order": order, "tamper": tamper,
        "accepted": accepted,
        "trusted_generation": generation,
        "recovered_bitmap": result.bitmap if result is not None else None,
        "expected_bitmap": old if generation == 0 else new,
        "stage_page_writes": writes,
        "trusted_root_publications": publications,
        "old_slot_drop_calls": drops,
        "stage_upload_bytes": P * writes,
        "retirement_address_bytes": 8 * drops,
        "recovery_page_reads": result.page_reads if result else None,
        "recovery_request_bytes": result.request_bytes if result else None,
        "recovery_response_bytes": result.response_bytes if result else None,
        "root_novelty": "OPEN_UNPROVED",
        "real_powerloss_safety_proved": False,
    }


def all_canonical_cuts(C: int, P: int, reader: int = 0,
                       epoch: int = 0) -> dict:
    M = ceil(ceil(2 * C / 8) / P)
    results = [crash_prefix(C, P, reader, epoch, k)
               for k in range(2 * M + 2)]
    if not all(x["accepted"] and
               x["recovered_bitmap"] == x["expected_bitmap"]
               for x in results):
        raise AssertionError("valid ordered crash prefix failed recovery")
    if any(x["trusted_generation"] != (int(x["prefix"] > M))
           for x in results):
        raise AssertionError("trusted commit ordering broken")
    return {
        "capacity": C, "page_bytes": P, "bitmap_pages": M,
        "distinct_crash_cuts": len(results),
        "every_canonical_cut_recovers_exact_trusted_bitmap": True,
        "root_novelty": "OPEN_UNPROVED",
        "real_powerloss_safety_proved": False,
    }


if __name__ == "__main__":
    import json
    print(json.dumps({
        "ordered": [all_canonical_cuts(c, p)
                    for c, p in ((8, 1), (17, 2), (257, 64))],
        "bad_publish_first": crash_prefix(8, 1, 0, 0, 1,
                                          order="publish-first")["accepted"],
        "bad_retire_first": crash_prefix(8, 1, 0, 0, 1,
                                         order="retire-first")["accepted"],
        "root_novelty": "OPEN_UNPROVED",
    }, indent=2, sort_keys=True))
