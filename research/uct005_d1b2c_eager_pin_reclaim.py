#!/usr/bin/env python3
"""UCT-005 D1-B2-C: paid eager PIN-aware version reclaim reference upper.

This is an alternative to the byte-conserving PAGE-001 full-manifest-scan
collector, NOT a novel information lower bound or actual crash-safe storage.
Serial honest author, two offline readers, trusted linearizable PIN/anchor
authority and honest remote page-deletion API are explicit assumptions.
"""
from __future__ import annotations

import itertools
import json
from math import ceil

from uct005_d1b0_f1_reference import SnapshotF1Reference, Abort, validate_contract


class EagerPinReclaim(SnapshotF1Reference):
    """Immutable PAGE-001 slots, reclaim when trusted authority releases a root.

    The PIN authority is already serialized with SET/PIN/UNPIN. It scans every
    independently trusted 41-byte PIN record (page reads/CPU charged) before
    deleting a superseded epoch. A remote DROP_PAGE command is charged per
    page with its full 8-byte page address. This is a logical remote page
    delete API, not NAND erasure or crash-safe filesystem hole punching.

    No PIN of an arbitrary old epoch is supported: only PIN_CURRENT.
    Thus an unpinned historical version cannot become newly pinned later.
    """

    def _authority_reclaim(self, candidate: int) -> int:
        self.ledger["eager_authority_latest_root_reads"] += 1
        self.ledger["eager_authority_latest_root_bytes_read"] += self.ROOT_BYTES
        pinned = False
        pin_record_pages = self._pages(self.PIN_RECORD_BYTES)
        for _, pinned_epoch in self.pin_registry:
            self.ledger["eager_authority_pin_record_reads"] += 1
            self.ledger["eager_authority_pin_record_page_reads"] += pin_record_pages
            self.ledger["eager_authority_pin_record_bytes_read"] += self.PIN_RECORD_BYTES
            self.ledger["eager_authority_pin_comparisons"] += 1
            if pinned_epoch == candidate:
                pinned = True
        if candidate == self.epoch or pinned:
            self.ledger["eager_retention_decisions"] += 1
            return 0
        # No remote "does this slot exist?" lookup: the trusted serialized
        # transition determines the obsolete epoch. Issue addressed deletion
        # operations unconditionally (idempotent even if a malicious server
        # already discarded a slot). The simulator's sparse dictionary is
        # not consulted to decide the paid remote operation.
        pages = self._pages_per_snapshot()
        start = self._slot_start_page(candidate)
        if start + pages > (1 << 64):
            raise OverflowError("8-byte page-address delete API overflows")
        for index in range(start, start + pages):
            self.ledger["eager_remote_drop_page_calls"] += 1
            self.ledger["eager_remote_drop_page_request_bytes"] += 8
            self.ledger["eager_remote_drop_page_address_checks"] += 1
        self.remote.pop(candidate, None)
        self.remote_manifests.pop(candidate, None)
        self.ledger["gc_logical_pages_freed"] += pages
        self.ledger["eager_retired_epochs"] += 1
        return pages

    def set(self, i: int, value: int) -> int:
        prior = self.epoch
        # The publication followed by reclaim is serialized under the
        # ideal PIN authority, including the race with PIN_CURRENT.
        now = super().set(i, value)
        self._authority_reclaim(prior)
        self._assert_live_epoch_invariant()
        return now

    def unpin(self, reader: int, epoch: int) -> None:
        super().unpin(reader, epoch)
        self._authority_reclaim(epoch)
        self._assert_live_epoch_invariant()

    def gc(self) -> int:
        # All obsolete epochs were synchronously retired by SET or UNPIN.
        self.ledger["eager_explicit_gc_calls"] += 1
        self._assert_live_epoch_invariant()
        return 0

    def _assert_live_epoch_invariant(self) -> None:
        expected = {self.epoch} | {e for _, e in self.pin_registry}
        if set(self.remote) != expected or set(self.remote_manifests) != expected:
            raise AssertionError("retired unpinned or protected pinned page slot")


def _assert_same_answers(a, b, known_versions, pins):
    n = a.n
    if a.epoch != b.epoch or a.epoch != len(known_versions) - 1:
        raise AssertionError("epoch disagreement")
    if a.writer_bits != b.writer_bits:
        raise AssertionError("writer-state disagreement")
    for left in range(n):
        for right in range(left + 1, n + 1):
            expected = sum(known_versions[-1][left:right]) & 1
            for reader in (0, 1):
                if a.latest(reader, left, right) != expected:
                    raise AssertionError("eager latest incorrect")
                if b.latest(reader, left, right) != expected:
                    raise AssertionError("scan latest incorrect")
            for reader, ep in pins:
                older = sum(known_versions[ep][left:right]) & 1
                if a.as_of(reader, ep, left, right) != older:
                    raise AssertionError("eager PIN incorrect")
                if b.as_of(reader, ep, left, right) != older:
                    raise AssertionError("scan PIN incorrect")


def exercise(initial: tuple[int, ...], page_bytes: int) -> dict:
    validate_contract()
    if not initial or any(type(bit) is not int or bit not in (0, 1)
                          for bit in initial):
        raise ValueError("nonempty exact binary initial word required")
    if page_bytes < 1:
        raise ValueError("positive complete page size required")
    eager = EagerPinReclaim(initial, page_bytes)
    scan = SnapshotF1Reference(initial, page_bytes)
    versions = [tuple(initial)]
    pins = set()

    assert eager.pin_current(0) == scan.pin_current(0) == 0
    pins.add((0, 0))
    # Three SETs with the middle write a mandatory no-op. Two offline
    # readers retain independent roots from epochs 0 and 2.
    ops = ((0, initial[0] ^ 1),
           (0, initial[0] ^ 1),
           (len(initial) - 1, None))
    for j, (pos, value) in enumerate(ops):
        old = list(versions[-1])
        new_bit = old[pos] ^ 1 if value is None else value
        new = old.copy()
        new[pos] = new_bit
        a_ep = eager.set(pos, new_bit)
        b_ep = scan.set(pos, new_bit)
        assert a_ep == b_ep == j + 1
        versions.append(tuple(new))
        if j == 1:
            assert eager.pin_current(1) == scan.pin_current(1) == 2
            pins.add((1, 2))
    _assert_same_answers(eager, scan, versions, pins)
    full_before_gc = scan.remote_pages
    freed_scan = scan.gc()
    if set(scan.remote) != {0, 2, 3} or set(eager.remote) != {0, 2, 3}:
        raise AssertionError("PIN-protected epoch set inconsistent")
    peak_eager = eager.ledger["peak_remote_pages"]
    peak_scan = scan.ledger["peak_remote_pages"]
    _assert_same_answers(eager, scan, versions, pins)

    for reader, ep in ((0, 0), (1, 2)):
        eager.unpin(reader, ep)
        scan.unpin(reader, ep)
        pins.remove((reader, ep))
        _assert_same_answers(eager, scan, versions, pins)
        scan.gc()
    assert eager.gc() == 0
    assert set(eager.remote) == set(scan.remote) == {3}
    if eager.remote_pages != scan.remote_pages:
        raise AssertionError("final latest-only footprint inconsistent")
    L = eager._pages_per_snapshot()
    return {
        "status": "RESTRICTED_SAME_F1_UPPER_COMPARISON_NOT_NEW_THEOREM",
        "n": len(initial),
        "page_bytes": page_bytes,
        "page_slot_bytes": L * page_bytes,
        "page_slot_full_pages": L,
        "manifest_bytes": eager.MANIFEST_BYTES,
        "epochs": eager.epoch,
        "independent_pins": 2,
        "no_op_set_epochs": 1,
        "eager_peak_pages": peak_eager,
        "scan_peak_pages": peak_scan,
        "eager_remote_slot_reads_for_gc": eager.ledger["gc_directory_page_reads"],
        "scan_remote_slot_reads_for_gc": scan.ledger["gc_directory_page_reads"],
        "eager_remote_page_delete_calls": eager.ledger["eager_remote_drop_page_calls"],
        "eager_remote_delete_request_bytes": eager.ledger["eager_remote_drop_page_request_bytes"],
        "eager_trusted_pin_record_page_reads": eager.ledger["eager_authority_pin_record_page_reads"],
        "eager_trusted_root_bytes_read": eager.ledger["eager_authority_latest_root_bytes_read"],
        "eager_pin_record_reads": eager.ledger["eager_authority_pin_record_reads"],
        "eager_logical_reclaimed_pages": eager.ledger["gc_logical_pages_freed"],
        "scan_logical_reclaimed_pages": scan.ledger["gc_logical_pages_freed"],
        "scan_initial_gc_freed_pages": freed_scan,
        "scan_before_first_gc_pages": full_before_gc,
        "same_data_write_pages": (
            eager.ledger["set_full_page_writes"] ==
            scan.ledger["set_full_page_writes"]),
        "same_latest_and_historical_answers": True,
        "root_status": "OPEN_UNPROVED",
        "pareto_verdict": "UNDECIDABLE_WITHOUT_FULL_TRUSTED_CPU_AND_DELETE_API_COSTS",
    }


def report():
    return {
        "classification": "CLASSICAL_EAGER_RECLAIM_VS_SCAN_REFERENCE_UPPER_ONLY",
        "cases": [exercise(tuple(i & 1 for i in range(n)), p)
                  for n, p in ((1, 1), (2, 2), (8, 8), (33, 2), (65, 64))],
        "F1_security": "ideal trusted serialized PIN authority assumed",
        "real_filesystem_durability": False,
        "root_novelty": "OPEN_UNPROVED",
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True))
