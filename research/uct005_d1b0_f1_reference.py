#!/usr/bin/env python3
"""UCT-005 D1-B0: fully charged *reference snapshot* and PIN/GC negative oracle.

NOT a production authenticated storage implementation or a lower bound.
SHA-256 binding and a serialized, separately trusted anchor+PIN authority
are assumptions. Page counts are complete reference API images, not SSD I/O.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path


SCHEMA = Path(__file__).resolve().parents[1] / "docs/research/UCT-005-G3-B2-D1B0-F1-MODEL.json"
REQUIRED_COSTS = frozenset({
    "s", "S", "U_r", "U_w", "U_delta", "Q_r", "B_pi", "C_author",
    "C_reader", "G", "V", "A", "T", "M", "GC_r", "GC_w", "GC_free",
    "F", "n", "H", "lambda", "epsilon", "P",
})


def validate_contract() -> dict:
    spec = json.loads(SCHEMA.read_text(encoding="utf-8"))
    if spec["schema"] != "mathlab.uct005.d1b0.f1.v1":
        raise ValueError("unrecognized F1 contract")
    if spec["root_novelty"] != "OPEN_UNPROVED":
        raise ValueError("root was falsely promoted")
    if REQUIRED_COSTS != frozenset(spec["coordinates"]):
        raise ValueError("missing or free cost axis")
    for name, item in spec["coordinates"].items():
        if not item.get("unit") or not (item.get("scope") or item.get("domain")):
            raise ValueError(f"undefined cost: {name}")
    if not spec["set"]["noop_creates_epoch"] or not spec["anchor"]["charged"]:
        raise ValueError("free epoch or anchor")
    if not spec["reader"]["latest_anchor_read"].startswith("mandatory"):
        raise ValueError("latest freshness can be silently assumed")
    if not spec["pin_gc"]["races"].startswith("serialize"):
        raise ValueError("pin/GC race unmodeled")
    if spec["d1_b1_status"] != "FULL_TEXT_THEOREM_TRANSFER_PENDING":
        raise ValueError("abstract-only source verification promoted")
    return spec


class Abort(RuntimeError):
    """An unsafe or withheld answer must not be accepted."""


class SnapshotF1Reference:
    """Single honest writer, two offline readers, ideal linearizable authority.

    The writer's n trusted bits, authority's latest root, each reader's PIN,
    and the duplicated authoritative PIN registry are all separately counted.
    Full immutable packed snapshots are an intentionally expensive upper
    comparator, not a cost-optimal data structure.
    """

    DIGEST_BYTES = 32
    ROOT_BYTES = 8 + DIGEST_BYTES

    def __init__(self, bits: tuple[int, ...], page_bytes: int = 64):
        if not bits or any(bit not in (0, 1) for bit in bits) or page_bytes < 1:
            raise ValueError("nonempty binary bits and positive complete page size")
        self.n = len(bits)
        self.page_bytes = page_bytes
        self.writer_bits = list(bits)  # n trusted writer bits; not free
        self.epoch = 0
        self.remote: dict[int, bytes] = {}
        self.readers: dict[int, dict[int, bytes]] = {0: {}, 1: {}}
        self.pin_registry: set[tuple[int, int]] = set()
        self.ledger = Counter()
        self.latest_root = self._digest(0, self._image())
        self.remote[0] = self._image()
        self.ledger["setup_full_page_writes"] += self._pages_per_snapshot()
        self.ledger["setup_anchor_publications"] += 1
        self.ledger["setup_anchor_bytes"] += self.ROOT_BYTES
        self.ledger["peak_remote_pages"] = self.remote_pages

    def _image(self) -> bytes:
        packed = bytearray((self.n + 7) // 8)
        for i, bit in enumerate(self.writer_bits):
            packed[i >> 3] |= bit << (i & 7)
        return bytes(packed)

    def _digest(self, epoch: int, image: bytes) -> bytes:
        return hashlib.sha256(
            b"mathlab.F1.snapshot.v1\0"
            + epoch.to_bytes(8, "big")
            + self.n.to_bytes(8, "big")
            + image
        ).digest()

    def _pages_per_snapshot(self) -> int:
        # ceil(data/P) + one entire full-page epoch/manifest entry
        return (len(self._image()) + self.page_bytes - 1) // self.page_bytes + 1

    @property
    def remote_pages(self) -> int:
        return len(self.remote) * self._pages_per_snapshot()

    @property
    def retained_pinned_pages(self) -> int:
        epochs = {epoch for _, epoch in self.pin_registry if epoch != self.epoch}
        return len(epochs) * self._pages_per_snapshot()

    @property
    def trusted_bits(self) -> int:
        # Writer + authoritative latest root + each reader PIN copy +
        # separately trusted authoritative PIN registry. All distinct.
        return self.n + 8 * self.ROOT_BYTES * (
            1 + sum(len(pins) for pins in self.readers.values())
            + len(self.pin_registry)
        )

    def _read_anchor(self) -> tuple[int, bytes]:
        self.ledger["anchor_read_calls"] += 1
        self.ledger["anchor_read_request_bytes"] += 1
        self.ledger["anchor_read_response_bytes"] += self.ROOT_BYTES
        return self.epoch, self.latest_root

    def set(self, i: int, value: int) -> int:
        if not 0 <= i < self.n or value not in (0, 1):
            raise ValueError("invalid SET")
        delta = int(self.writer_bits[i] != value)
        self.writer_bits[i] = value
        self.epoch += 1  # no-op also creates an epoch
        image = self._image()
        self.remote[self.epoch] = image  # complete immutable snapshot image
        self.latest_root = self._digest(self.epoch, image)
        self.ledger["set_changed_logical_bits"] += delta
        self.ledger["set_full_page_reads"] += 0  # author holds n trusted bits
        self.ledger["set_full_page_writes"] += self._pages_per_snapshot()
        self.ledger["anchor_publications"] += 1
        self.ledger["anchor_publication_bytes"] += self.ROOT_BYTES
        self.ledger["author_hash_input_bytes"] += len(image) + 16
        self.ledger["peak_remote_pages"] = max(
            self.ledger["peak_remote_pages"], self.remote_pages
        )
        return self.epoch

    def pin_current(self, reader: int) -> int:
        if reader not in self.readers:
            raise ValueError("unknown reader")
        epoch, root = self._read_anchor()
        # Ideal atomic PIN acquisition and GC exclusion at this boundary.
        self.readers[reader][epoch] = root
        self.pin_registry.add((reader, epoch))
        self.ledger["pin_registry_writes"] += 1
        self.ledger["pin_registry_bytes"] += self.ROOT_BYTES
        return epoch

    def unpin(self, reader: int, epoch: int) -> None:
        if reader not in self.readers or epoch not in self.readers[reader]:
            raise ValueError("UNPIN without active token")
        del self.readers[reader][epoch]
        self.pin_registry.remove((reader, epoch))
        self.ledger["pin_registry_revocations"] += 1
        self.ledger["pin_registry_bytes"] += self.ROOT_BYTES

    def gc(self) -> int:
        # One serialized collector. Scan explicitly charged version directory.
        self.ledger["gc_directory_page_reads"] += (
            len(self.remote) * 8 + self.page_bytes - 1
        ) // self.page_bytes
        retained = {self.epoch} | {epoch for _, epoch in self.pin_registry}
        deleted = [e for e in self.remote if e not in retained]
        for e in deleted:
            del self.remote[e]
        freed = len(deleted) * self._pages_per_snapshot()
        self.ledger["gc_logical_pages_freed"] += freed
        self.ledger["gc_manifest_page_writes"] += len(deleted)
        return freed

    def _verify(self, epoch: int, expected_root: bytes, left: int, right: int,
                presented: bytes | None = None,
                presented_epoch: int | None = None) -> int:
        if not 0 <= left < right <= self.n:
            raise ValueError("invalid half-open range")
        actual_epoch = epoch if presented_epoch is None else presented_epoch
        image = self.remote.get(actual_epoch) if presented is None else presented
        if image is None:
            raise Abort("withheld or reclaimed snapshot")
        self.ledger["query_full_page_reads"] += self._pages_per_snapshot()
        self.ledger["query_remote_payload_bytes"] += 8 + len(image)
        self.ledger["verifier_hash_input_bytes"] += 16 + len(image)
        if len(image) != (self.n + 7) // 8:
            raise Abort("malformed length")
        if (actual_epoch != epoch
                or self._digest(actual_epoch, image) != expected_root):
            raise Abort("stale/tampered snapshot")
        return sum((image[i >> 3] >> (i & 7)) & 1
                   for i in range(left, right)) & 1

    def latest(self, reader: int, left: int, right: int,
               presented: bytes | None = None,
               presented_epoch: int | None = None) -> int:
        if reader not in self.readers:
            raise ValueError("unknown reader")
        epoch, root = self._read_anchor()  # mandatory even if reader pinned
        return self._verify(epoch, root, left, right, presented, presented_epoch)

    def as_of(self, reader: int, epoch: int, left: int, right: int,
              presented: bytes | None = None,
              presented_epoch: int | None = None) -> int:
        if reader not in self.readers or epoch not in self.readers[reader]:
            raise Abort("no independently trusted historical PIN")
        return self._verify(epoch, self.readers[reader][epoch],
                            left, right, presented, presented_epoch)


def report() -> dict:
    validate_contract()
    demo = SnapshotF1Reference((0, 1, 1, 0), page_bytes=2)
    p = demo.pin_current(0)
    demo.set(0, 1)
    demo.pin_current(1)
    a = demo.as_of(0, p, 0, 4)
    b = demo.latest(1, 0, 4)
    demo.gc()
    return {
        "classification": "FINITE_IDEAL_ANCHOR_UPPER_AND_NEGATIVE_ORACLE",
        "as_of_initial_parity": a,
        "latest_parity": b,
        "charged_ledger": dict(demo.ledger),
        "trusted_bits": demo.trusted_bits,
        "retained_pinned_pages": demo.retained_pinned_pages,
        "root_novelty": "OPEN_UNPROVED",
        "real_ssd_or_crypto_proof": False,
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2))
