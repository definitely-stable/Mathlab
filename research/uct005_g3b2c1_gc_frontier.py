#!/usr/bin/env python3
"""UCT-005 G3-B2-C1: immutable page liveness, paid GC and novelty falsifiers.

Restricted layout simulator: NOT measured OS I/O or real crash durability.
The trusted monotone epoch/root is a separately paid external primitive.
"""
from dataclasses import dataclass
from uct005_g3b2c0_pages import (
    ColdLRU, FrozenPages, TreePageLedger, _all_nodes, _frontier_nodes,
    _path_nodes, novelty_falsifiers,
)
from uct005_g3b2b_range_tree import Reader, checked_query


@dataclass(frozen=True)
class ReclaimCost:
    latest_epoch: int
    pinned_epochs: tuple
    allocated_page_ids: int
    resident_before: int
    live_after: int
    pages_freed: int
    bytes_capacity_recovered: int
    root_mark_page_reads: int
    metadata_page_reads: int
    metadata_page_writes: int
    remote_read_bytes: int
    remote_write_bytes: int
    trim_commands: int
    ram_budget_bytes: int
    anchor_publications: int
    trusted_checkpoint_bytes: int


def _ceildiv(a, b):
    return (a + b - 1) // b


class EpochGcModel:
    """COW pages and explicit latest-only versus pinned historical roots.

    Page IDs use the exact previous C0 allocation model. Python objects
    remain allocated but only resident page IDs can be read. Stop-the-world
    sweep scans reachable roots and accounts one metadata bitmap bit per
    allocated page address, including pre-existing holes. Each sweep reads
    AND writes whole metadata page images even if nothing can be freed.
    A TRIM is charged as a separate logical command (not a guarantee of
    SSD physical reclamation). No hidden free liveness/retention guarantee.
    """
    def __init__(self, bits, layout=FrozenPages()):
        if layout.ram_pages < 1:
            raise ValueError("GC requires a paid RAM page for marking")
        self.ledger = TreePageLedger(bits, layout)
        self.resident = set(range(self.ledger.next_page))
        self.pins = set()
        self.history = []

    @property
    def latest(self):
        return self.ledger.writer.anchor.epoch

    def _reachable(self, epoch):
        if type(epoch) is not int or not 0 <= epoch <= self.latest:
            raise ValueError("epoch out of range")
        pages = {self.ledger.epoch_directory[epoch]}
        pages.update(self.ledger.addresses[id(node)]
                     for node in _all_nodes(self.ledger.writer.roots[epoch]))
        return pages

    def pin_asof(self, epoch):
        """Caller must already hold an authenticated historical root."""
        need = self._reachable(epoch)
        if not need <= self.resident:
            raise ValueError("historical pages already reclaimed")
        self.pins.add(epoch)

    def release_asof(self, epoch):
        if epoch not in self.pins:
            raise ValueError("not pinned")
        self.pins.remove(epoch)

    def set(self, index, bit):
        root = self.ledger.writer.roots[-1]
        need = {self.ledger.epoch_directory[-1]}
        need.update(self.ledger.addresses[id(node)]
                    for node in _path_nodes(root, self.ledger.writer.n, index))
        if not need <= self.resident:
            raise ValueError("current data already missing")
        previous = self.ledger.next_page
        result = self.ledger.update(index, bit)
        self.resident.update(range(previous, self.ledger.next_page))
        return result

    def _readable(self, epoch, left, right):
        root = self.ledger.writer.roots[epoch]
        need = {self.ledger.epoch_directory[epoch]}
        need.update(self.ledger.addresses[id(node)]
                    for node in _frontier_nodes(
                        root, 0, self.ledger.writer.n - 1, left, right))
        if not need <= self.resident:
            raise ValueError("requested pages already reclaimed")

    def current_query(self, left, right):
        self._readable(self.latest, left, right)
        return self.ledger.query(self.latest, left, right)

    def historical_query(self, epoch, left, right):
        if epoch not in self.pins:
            raise ValueError("historical AS_OF epoch must be pinned")
        self._readable(epoch, left, right)
        response, reads = self.ledger.writer.serve(epoch, left, right)
        # Historical anchor is a previously obtained independent attestation;
        # do NOT confuse historical AS_OF with latest F1 freshness.
        historical_anchor = self.ledger.writer.epochs[epoch]
        return checked_query(
            Reader(self.ledger.writer.epochs[0]), self.ledger.writer.n,
            left, right, response, reads, historical_anchor,
        )

    def sweep(self, expected_epoch):
        """Stop-the-world: reject concurrent anchor change; paid cold mark."""
        if type(expected_epoch) is not int or expected_epoch != self.latest:
            raise ValueError("stale mark-phase epoch")
        keep = self._reachable(self.latest)
        for epoch in self.pins:
            keep.update(self._reachable(epoch))
        if not keep <= self.resident:
            raise ValueError("live page missing; cannot reclaim safely")
        cache = ColdLRU(self.ledger.layout.ram_pages)
        for epoch in sorted(self.pins | {self.latest}):
            cache.touch(self.ledger.epoch_directory[epoch])
            for node in _all_nodes(self.ledger.writer.roots[epoch]):
                cache.touch(self.ledger.addresses[id(node)])
        before = len(self.resident)
        garbage = self.resident - keep
        payload_bits = 8 * self.ledger.layout.payload_bytes
        metadata = _ceildiv(self.ledger.next_page, payload_bits)
        self.resident.difference_update(garbage)
        p = self.ledger.layout.page_bytes
        charge = ReclaimCost(
            latest_epoch=self.latest, pinned_epochs=tuple(sorted(self.pins)),
            allocated_page_ids=self.ledger.next_page,
            resident_before=before, live_after=len(self.resident),
            pages_freed=len(garbage), bytes_capacity_recovered=len(garbage)*p,
            root_mark_page_reads=cache.faults,
            metadata_page_reads=metadata, metadata_page_writes=metadata,
            remote_read_bytes=(cache.faults+metadata)*p,
            remote_write_bytes=metadata*p, trim_commands=len(garbage),
            ram_budget_bytes=self.ledger.layout.ram_pages*p,
            anchor_publications=0, trusted_checkpoint_bytes=40,
        )
        self.history.append(charge)
        return charge


def typed_candidate_gate(n=4096, layout=FrozenPages()):
    """Finite explicit falsifiers; NOT a theorem about all possible protocols."""
    if type(n) is not int or n < 16:
        raise ValueError("n must be an integer >=16")
    base = novelty_falsifiers(n, layout)
    log_bound = (n-1).bit_length()
    product = (base["tree_physical_page_writes"] *
               base["full_range_tree_query_page_reads"])
    service = EpochGcModel((0,) * n, layout)
    service.set(0, 1)
    gc = service.sweep(service.latest)
    return {
        "n": n, "s_trusted_bytes": 40,
        "server_ram_cap_bytes": layout.ram_pages*layout.page_bytes,
        "wrong_all_query_bound": {
            "claimed_min_product": log_bound,
            "observed_full_range_product": product,
            "rejected": product < log_bound,
        },
        "zero_cost_gc_rejected": {
            "pages_freed": gc.pages_freed,
            "mark_read_bytes": gc.remote_read_bytes,
            "bitmap_write_bytes": gc.remote_write_bytes,
            "rejected": gc.remote_read_bytes > 0 and gc.remote_write_bytes > 0,
        },
        "status": "EXPLICIT_FALSE_CANDIDATES_NOT_ORIGINAL_LOWER_BOUND",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(typed_candidate_gate(), sort_keys=True, indent=2))
