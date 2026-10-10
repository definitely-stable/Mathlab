#!/usr/bin/env python3
"""UCT-005 D1-B2-E: exactly scoped PIN information gate and paid F1 budget audit.

Finite deterministic full-audit counting is CLASSICAL. The two conditional
computational F1 comparators are not a novel joint lower bound. This file
cannot prove physical SSD costs, crash safety or SHA256 collision resistance.
"""
from __future__ import annotations

import itertools
import json

from uct005_d1b0_f1_reference import Abort, validate_contract
from uct005_d1b2c_eager_pin_reclaim import EagerPinReclaim
from uct005_d1b2d_remote_pin_bitmap import RemotePinBitmapF1


STATUS = "DERIVED_CLASSICAL_FULL_AUDIT_BOUND_AND_CONDITIONAL_F1_BUDGET"
ROOT_STATUS = "OPEN_UNPROVED"
UNKNOWN_RESOURCE_AXES = (
    "transient_trusted_scratch_peak_bytes",
    "transport_retry_and_authentication_bytes",
    "physical_crash_recovery_page_writes",
    "underlying_ssd_ftl_write_amplification",
    "security_assumption_uniform_asymptotics",
    "program_and_preprocessing_advice_bits",
)


def projection_signature(word: tuple[int, ...], trusted_bits: int,
                         remote_reply_bits: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """A tight *fixed bit-projection* construction for one COMPLETE audit."""
    if (trusted_bits < 0 or remote_reply_bits < 0
            or any(v not in (0, 1) for v in word)):
        raise ValueError("nonnegative budgets and binary word required")
    return (word[:trusted_bits],
            word[trusted_bits:trusted_bits + remote_reply_bits])


def complete_audit_gate(horizon: int, trusted_bits: int,
                        remote_reply_bits: int) -> dict:
    """Classical H <= s+b for exact full H-bit output, not individual queries.

    Response includes ALL remote data/status/timing channels capable of
    conveying state. The honest server must actually answer; ABORT-only
    protocols cannot fake exact full-audit correctness.
    """
    if not 0 <= horizon <= 10 or trusted_bits < 0 or remote_reply_bits < 0:
        raise ValueError("finite 0..10 horizon and nonnegative budgets required")
    seen: dict[tuple[tuple[int, ...], tuple[int, ...]], tuple[int, ...]] = {}
    collision = None
    for bits in itertools.product((0, 1), repeat=horizon):
        signature = projection_signature(bits, trusted_bits, remote_reply_bits)
        previous = seen.setdefault(signature, bits)
        if previous != bits and collision is None:
            collision = (previous, bits)
    expected = 1 << min(horizon, trusted_bits + remote_reply_bits)
    if len(seen) != expected:
        raise AssertionError("finite signature count contradicts direct counting")
    unique = len(seen) == (1 << horizon)
    if unique != (trusted_bits + remote_reply_bits >= horizon):
        raise AssertionError("tight classical bound misclassified")
    return {
        "horizon": horizon,
        "trusted_bits": trusted_bits,
        "complete_remote_reply_bits": remote_reply_bits,
        "membership_vectors": 1 << horizon,
        "distinct_state_transcripts": len(seen),
        "injective_full_audit": unique,
        "distinct_collision_witness": (
            {"a": list(collision[0]), "b": list(collision[1])}
            if collision is not None else None
        ),
        "necessary_classical_bound": "H <= s + b (full-vector exact audit only)",
        "novelty": "CLASSICAL_PIGEONHOLE",
    }


def independent_member_lookup_countermodel(horizon: int) -> dict:
    """Honest, unauthenticated remote bit-addressing refutes a false transfer.

    Single query returns PIN(epoch), not ALL H membership bits; thus q=1
    suffices at trusted membership state 0 even when H is arbitrarily larger
    than one. NOT a malicious-server authenticated F1 implementation.
    """
    if not 2 <= horizon <= 10:
        raise ValueError("countermodel requires 2..10 epochs")
    queries = 0
    for word in itertools.product((0, 1), repeat=horizon):
        for epoch in range(horizon):
            # One direct-indexed bit is the sole reply, with an input-supplied
            # query epoch. No other history is read.
            remote_reply = word[epoch]
            if remote_reply != int(epoch in {e for e, b in enumerate(word) if b}):
                raise AssertionError("direct-index oracle incorrect")
            queries += 1
    return {
        "horizon": horizon, "trusted_membership_bits": 0,
        "remote_bits_read_per_single_epoch_query": 1,
        "all_exact_queries_checked": queries,
        "refutes": "H <= s + b for a SINGLE membership query",
        "scope": "HONEST_UNAUTHENTICATED_SINGLE_QUERY_NOT_F1",
    }


def persistent_budget_filter(modeled_trusted_bits: dict[str, int],
                             cap_bits: int) -> dict[str, bool]:
    if type(cap_bits) is not int or cap_bits < 0:
        raise ValueError("persistent trusted-state cap must be nonnegative integer")
    if (not modeled_trusted_bits or any(
            not isinstance(k, str) or type(v) is not int or v < 0
            for k, v in modeled_trusted_bits.items())):
        raise ValueError("all candidate peak trust bits must be explicit integers")
    return {name: bits <= cap_bits for name, bits in modeled_trusted_bits.items()}


def identical_f1_budget_witness(bits: tuple[int, ...], page_bytes: int,
                                epoch_capacity: int = 8,
                                cap_bits: int | None = None) -> dict:
    validate_contract()
    if (not bits or any(type(x) is not int or x not in (0, 1) for x in bits)
            or type(page_bytes) is not int or page_bytes < 1
            or type(epoch_capacity) is not int or epoch_capacity < 4):
        raise ValueError("nonempty GF2 bits, positive page, capacity >=4 required")
    first = RemotePinBitmapF1(bits, page_bytes, epoch_capacity)
    second = EagerPinReclaim(bits, page_bytes)
    models = {"R_AUTH_REMOTE_BITMAP": first, "E_TRUSTED_PIN_ENTRIES": second}
    truth = [tuple(bits)]
    trust_peaks = {name: candidate.trusted_bits for name, candidate in models.items()}
    def note_peaks():
        for key, candidate in models.items():
            trust_peaks[key] = max(trust_peaks[key], candidate.trusted_bits)

    for model in models.values():
        assert model.pin_current(0) == 0
    note_peaks()
    operations = [
        (0, bits[0] ^ 1),
        (min(1, len(bits)-1), None),   # explicit epoch-2 NO-OP
        (len(bits)-1, "flip"),
    ]
    for j, (pos, next_bit) in enumerate(operations):
        old = list(truth[-1])
        bit = old[pos] if next_bit is None else (
            old[pos] ^ 1 if next_bit == "flip" else next_bit)
        old[pos] = bit
        truth.append(tuple(old))
        for model in models.values():
            if model.set(pos, bit) != j + 1:
                raise AssertionError("F1 epoch mismatch")
        note_peaks()
        if j == 1:
            for model in models.values():
                if model.pin_current(1) != 2:
                    raise AssertionError("second PIN not bound to epoch2")
            note_peaks()
    if truth[1] != truth[2]:
        raise AssertionError("no-op must preserve the word")
    for model in models.values():
        if model.epoch != 3 or set(model.remote) != {0, 2, 3}:
            raise AssertionError("different PIN-retained history semantics")

    pinned_checkpoint = {name: model.trusted_bits for name, model in models.items()}
    saved_remote_pages = {name: model.remote_pages for name, model in models.items()}
    for left in range(len(bits)):
        for right in range(left + 1, len(bits) + 1):
            for model in models.values():
                current = sum(truth[3][left:right]) & 1
                historic0 = sum(truth[0][left:right]) & 1
                historic2 = sum(truth[2][left:right]) & 1
                if (model.latest(0, left, right) != current
                        or model.latest(1, left, right) != current
                        or model.as_of(0, 0, left, right) != historic0
                        or model.as_of(1, 2, left, right) != historic2):
                    raise AssertionError("snapshot/query semantics mismatch")

    for reader, epoch in ((0, 0), (1, 2)):
        for model in models.values():
            model.unpin(reader, epoch)
        note_peaks()
    for model in models.values():
        if model.gc() != 0 or set(model.remote) != {3}:
            raise AssertionError("latest-only page retention failure")
        try:
            model.as_of(0, 0, 0, len(bits))
        except Abort:
            pass
        else:
            raise AssertionError("old unpinned PIN token unexpectedly accepted")

    L = ((len(bits) + 7) // 8 + page_bytes - 1) // page_bytes + (
        48 + page_bytes - 1) // page_bytes
    bitmap_pages = ((2 * epoch_capacity + 7) // 8 + page_bytes - 1) // page_bytes
    if saved_remote_pages != {
        "R_AUTH_REMOTE_BITMAP": 3 * L + bitmap_pages,
        "E_TRUSTED_PIN_ENTRIES": 3 * L,
    }:
        raise AssertionError("reference byte-to-page layout disagrees")

    known = {
        "R_AUTH_REMOTE_BITMAP": {
            "persistent_trusted_peak_bits": trust_peaks["R_AUTH_REMOTE_BITMAP"],
            "trusted_bits_with_two_active_pins": pinned_checkpoint["R_AUTH_REMOTE_BITMAP"],
            "remote_pages_with_three_live_versions": saved_remote_pages["R_AUTH_REMOTE_BITMAP"],
            "remote_page_peak": first.ledger["peak_remote_pages"],
            "snapshot_set_full_page_writes": first.ledger["set_full_page_writes"],
            "remote_bitmap_page_read_attempts": first.ledger["bitmap_remote_page_read_attempts"],
            "remote_bitmap_page_writes": first.ledger["bitmap_remote_page_writes"],
            "remote_bitmap_verifier_hashed_bytes": first.ledger["bitmap_verifier_hashed_bytes"],
            "remote_bitmap_author_hashed_bytes": first.ledger["bitmap_author_hash_input_bytes"],
            "trusted_bitmap_root_publications": first.ledger["bitmap_trusted_root_publications"],
            "remote_delete_page_calls": first.ledger["bitmap_remote_drop_page_calls"],
            "remote_delete_request_bytes": first.ledger["bitmap_remote_drop_request_bytes"],
        },
        "E_TRUSTED_PIN_ENTRIES": {
            "persistent_trusted_peak_bits": trust_peaks["E_TRUSTED_PIN_ENTRIES"],
            "trusted_bits_with_two_active_pins": pinned_checkpoint["E_TRUSTED_PIN_ENTRIES"],
            "remote_pages_with_three_live_versions": saved_remote_pages["E_TRUSTED_PIN_ENTRIES"],
            "remote_page_peak": second.ledger["peak_remote_pages"],
            "snapshot_set_full_page_writes": second.ledger["set_full_page_writes"],
            "trusted_authority_pin_record_page_reads": second.ledger["eager_authority_pin_record_page_reads"],
            "trusted_authority_pin_record_bytes_read": second.ledger["eager_authority_pin_record_bytes_read"],
            "trusted_authority_pin_record_comparisons": second.ledger["eager_authority_pin_comparisons"],
            "remote_delete_page_calls": second.ledger["eager_remote_drop_page_calls"],
            "remote_delete_request_bytes": second.ledger["eager_remote_drop_page_request_bytes"],
        },
    }
    eligible = (persistent_budget_filter(trust_peaks, cap_bits)
                if cap_bits is not None else None)
    return {
        "status": STATUS, "n": len(bits), "P": page_bytes,
        "epoch_capacity": epoch_capacity,
        "epoch_count": 3, "reader_pin_epochs": [0, 2],
        "noop_epochs": [2],
        "page001_snapshot_full_pages": L,
        "remote_bitmap_full_pages": bitmap_pages,
        "known_axes_by_candidate": known,
        "unknown_unpriced_axes": list(UNKNOWN_RESOURCE_AXES),
        "modeled_persistent_trust_budget_bits": cap_bits,
        "within_modeled_persistent_trust_budget": eligible,
        "total_trusted_state_includes_both_reader_roots": True,
        "full_pareto_judgment": "FORBIDDEN_MISSING_RESOURCE_AND_SECURITY_AXES",
        "root_novelty": ROOT_STATUS,
    }


def report() -> dict:
    samples = [identical_f1_budget_witness(tuple(i & 1 for i in range(n)), p,
                                           8, 1600)
               for n, p in ((1, 1), (8, 2), (33, 2), (65, 64))]
    return {
        "classification": STATUS,
        "full_audit_examples": [
            complete_audit_gate(6, 1, 4),
            complete_audit_gate(6, 2, 4),
            complete_audit_gate(6, 6, 0)],
        "single_membership_falsifier": independent_member_lookup_countermodel(6),
        "F1_cases": samples,
        "new_joint_lower_bound_proved": False,
        "root_novelty": ROOT_STATUS,
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True))
