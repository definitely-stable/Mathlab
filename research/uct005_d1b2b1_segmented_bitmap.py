#!/usr/bin/env python3
"""D1-B2-B1: physical allocation bitmap changed in page-sized segments.

Extends the *conditional* two-reader authenticated COW reference without
changing its node/root commitments or PIN/GC service. The public segmented
allocation bitmap is ADVISORY and is not a cryptographic proof.

P-byte pages and B=8*P bits; node and epoch segments have distinct namespaces.
SET reads/rewrites only the segments it actually changes, with one complete
page per distinct touched segment, not a free dictionary index or global
re-serialization. GC still performs a fully priced scan, then rewrites only
segments whose bits change. Fixed slot page IDs are never reused.
"""
from __future__ import annotations

import json
from math import ceil

from uct005_d1b2b_page_cow import Abort, PageCowTree, _ceil


class SegmentedPageCowTree(PageCowTree):
    """Page-image COW comparator under an ideal, separately paid anchor.

    node_bitmap_segments and epoch_bitmap_segments are remote untrusted page
    images at deterministic addresses (namespace, segment_number), not
    cached trusted indexes. Python dictionaries simulate sparse slots only.
    """

    def __init__(self, bits, page_bytes=64):
        self.node_bitmap_segments: dict[int, bytes] = {}
        self.epoch_bitmap_segments: dict[int, bytes] = {}
        self._new_nodes: list[int] = []
        self._set_index: int | None = None
        self._bitmap_read_cache: dict[tuple[str, int], bytes] = {}
        super().__init__(bits, page_bytes)

    @property
    def bits_per_segment(self) -> int:
        return 8 * self.P

    @property
    def bitmap_pages(self) -> int:
        # Count persisted full page-images, including segments that became
        # all zero after GC and stay allocated at their public address.
        # Derive complete physical highwater from separately priced metadata;
        # Python dictionary occupancy cannot make a missing page "free".
        node_issued = self.next_id - 1
        epoch_issued = self.epoch + 1
        return (_ceil(node_issued, self.bits_per_segment)
                + _ceil(epoch_issued, self.bits_per_segment))

    def _alloc(self, raw: bytes, phase: str):
        node_id, digest = super()._alloc(raw, phase)
        self._new_nodes.append(node_id)
        return node_id, digest

    def _segment(self, namespace: str, bit_index: int) -> tuple[str, int, int]:
        if namespace not in ("node", "epoch") or not 0 <= bit_index < 2**64:
            raise ValueError("segment address outside public grammar")
        segment_id, local_bit = divmod(bit_index, self.bits_per_segment)
        return namespace, segment_id, local_bit

    def _pages(self, namespace: str):
        return (self.node_bitmap_segments if namespace == "node"
                else self.epoch_bitmap_segments)

    def _max_index(self, namespace: str) -> int:
        # This is a charged trusted highwater, not an untrusted directory scan.
        return self.next_id - 2 if namespace == "node" else self.epoch

    def _get_page(self, namespace: str, segment: int, phase: str) -> bytes:
        """Charge page fetch *even for an unallocated all-zero segment*."""
        if namespace not in ("node", "epoch") or segment < 0:
            raise Abort("bad segment locator")
        pages = self._pages(namespace)
        start = segment * self.bits_per_segment
        issued_max = self._max_index(namespace)
        self.ledger[f"{phase}_bitmap_page_reads"] += 1
        self.ledger[f"{phase}_bitmap_request_bytes"] += 1 + 8
        self.ledger[f"{phase}_bitmap_response_bytes"] += self.P
        if segment not in pages and start <= issued_max:
            raise Abort("missing previously issued bitmap page")
        raw = pages.get(segment, bytes(self.P))
        if not isinstance(raw, bytes) or len(raw) != self.P:
            raise Abort("missing, malformed or truncated bitmap segment")
        # Reserved future bits and byte padding cannot be set.
        maximum = issued_max
        if start > maximum:
            if any(raw):
                raise Abort("nonzero future allocation bitmap segment")
        elif maximum < start + self.bits_per_segment - 1:
            first_unused = maximum - start + 1
            if any((raw[i // 8] >> (i % 8)) & 1
                   for i in range(first_unused, self.bits_per_segment)):
                raise Abort("reserved bitmap bits nonzero")
        return raw

    def _path_nodes(self, index: int) -> int:
        if not 0 <= index < self.n:
            raise ValueError("invalid path index")
        lo, hi, depth = 0, self.n, 1
        while hi - lo > 1:
            middle = (lo + hi) // 2
            if index < middle:
                hi = middle
            else:
                lo = middle
            depth += 1
        return depth

    def _read_bitmap(self, phase: str):
        """Override predecessor's O(n/P) global bitmap scan on SET."""
        self._bitmap_read_cache = {}
        if phase == "set":
            if self._set_index is None:
                raise AssertionError("SET path must be declared")
            path_len = self._path_nodes(self._set_index)
            # Monotone node IDs are allocated contiguously; the root epoch
            # also gets exactly one new occupancy bit.
            planned = {("node", self._segment("node", i - 1)[1])
                       for i in range(self.next_id, self.next_id + path_len)}
            planned.add(("epoch", self._segment("epoch", self.epoch + 1)[1]))
            for kind, segment in sorted(planned):
                self._bitmap_read_cache[(kind, segment)] = self._get_page(
                    kind, segment, phase)
            self.ledger["set_bitmap_projected_node_count"] += path_len
        elif phase == "gc":
            # Collector reads all allocated bitmap segment pages. No free
            # reachability index; parent's GC charges node/root highwater.
            for kind in ("node", "epoch"):
                # Scan all issued segment addresses. Missing remote pages
                # must charge an attempted read and ABORT, not disappear
                # from Python dict iteration and undercount GC costs.
                high = self._max_index(kind)
                for segment in range(high // self.bits_per_segment + 1):
                    self._bitmap_read_cache[(kind, segment)] = self._get_page(
                        kind, segment, phase)
        else:
            raise ValueError("unknown bitmap read phase")
        return self._bitmap_read_cache

    def set(self, index: int, bit: int) -> int:
        self._set_index = index
        try:
            return super().set(index, bit)
        finally:
            self._set_index = None
            self._bitmap_read_cache = {}

    def _write_changed(self, phase: str,
                       changes: dict[tuple[str, int], bytes]):
        for (kind, segment), image in sorted(changes.items()):
            if not isinstance(image, bytes) or len(image) != self.P:
                raise AssertionError("nonconserving bitmap page writer")
            self._pages(kind)[segment] = image
            self.ledger[f"{phase}_bitmap_page_writes"] += 1
            self.ledger[f"{phase}_bitmap_upload_bytes"] += self.P
            # The sparse simulator does not silently identify a page as an
            # on-disk block write. These are page-image API calls only.
            if phase in ("setup", "set"):
                self.ledger[f"{phase}_remote_upload_bytes"] += self.P
        self.ledger["peak_remote_pages"] = max(
            self.ledger["peak_remote_pages"], self.remote_pages)

    def _write_bitmap(self, phase: str):
        if phase in ("setup", "set"):
            # Node IDs produced during this SET were logged by _alloc; no
            # scan over historical COW nodes occurs on the update path.
            bits = [("node", node_id - 1) for node_id in self._new_nodes]
            bits.append(("epoch", self.epoch))
            staged = {}
            for kind, index in bits:
                _, segment, bit = self._segment(kind, index)
                key = kind, segment
                if key not in staged:
                    if phase == "set":
                        if key not in self._bitmap_read_cache:
                            raise AssertionError("unpriced target segment")
                        staged[key] = bytearray(self._bitmap_read_cache[key])
                    else:
                        staged[key] = bytearray(bytes(self.P))
                j, shift = divmod(bit, 8)
                if (staged[key][j] >> shift) & 1:
                    raise Abort("allocator ID reuse or false occupied bit")
                staged[key][j] |= 1 << shift
            self._write_changed(phase, {k: bytes(v) for k, v in staged.items()})
            self._new_nodes.clear()
            self._bitmap_read_cache = {}
        elif phase == "gc":
            # Parent GC has already authenticated all retained roots and
            # physically examined issued slots. Occupancy is reconstructed
            # from that verified page-image state, not blindly trusted as
            # a certificate of reachability.
            modified = {}
            for kind, pages in (("node", self.node_bitmap_segments),
                                ("epoch", self.epoch_bitmap_segments)):
                for segment, old in sorted(pages.items()):
                    if not isinstance(old, bytes) or len(old) != self.P:
                        raise Abort("malformed bitmap at collection")
                    expected = bytearray(self.P)
                    start = segment * self.bits_per_segment
                    issued = self._max_index(kind)
                    for offset in range(self.bits_per_segment):
                        index = start + offset
                        if index > issued:
                            break
                        present = ((index + 1) in self.nodes if kind == "node"
                                   else index in self.roots)
                        if present:
                            expected[offset // 8] |= 1 << (offset % 8)
                        self.ledger["gc_bitmap_bits_examined"] += 1
                    if old != bytes(expected):
                        modified[kind, segment] = bytes(expected)
            self._write_changed("gc", modified)
            self._bitmap_read_cache = {}
        else:
            raise ValueError("unknown bitmap write phase")

    def segment_matches_storage(self) -> bool:
        """Independent finite audit; intentionally O(all issued page bits)."""
        for kind, pages in (("node", self.node_bitmap_segments),
                            ("epoch", self.epoch_bitmap_segments)):
            expected_count = _ceil(self._max_index(kind) + 1,
                                   self.bits_per_segment)
            if set(pages) != set(range(expected_count)):
                return False
            for segment, raw in pages.items():
                if not isinstance(raw, bytes) or len(raw) != self.P:
                    return False
                for i in range(self.bits_per_segment):
                    index = segment * self.bits_per_segment + i
                    actual = ((index + 1) in self.nodes if kind == "node"
                              else index in self.roots)
                    if bool((raw[i // 8] >> (i % 8)) & 1) != actual:
                        return False
        return True


def report():
    original = PageCowTree((0, 1, 0, 1, 1), page_bytes=2)
    segmented = SegmentedPageCowTree((0, 1, 0, 1, 1), page_bytes=2)
    for machine in (original, segmented):
        machine.pin_current(0)
        machine.set(0, 1)
        machine.set(1, 1)  # identical no-op, independent epoch
        machine.pin_current(1)
        machine.set(4, 0)
        if (machine.query(0, 0, 5, as_of=0) != 1
                or machine.query(1, 0, 5, as_of=2) != 0
                or machine.query(0, 0, 5) != 1):
            raise AssertionError("parity history mismatch")
        machine.gc()
        if not set(machine.roots) == {0, 2, 3}:
            raise AssertionError("PIN/GC mismatch")
    return {
        "classification":"SEGMENTED_PHYSICAL_BITMAP_SAME_F1_UPPER_NO_NOVEL_LOWER_BOUND",
        "n":segmented.n,"P":segmented.P,
        "global_SET_bitmap_page_writes":original.ledger["set_bitmap_page_writes"],
        "segmented_SET_bitmap_page_writes":segmented.ledger["set_bitmap_page_writes"],
        "global_GC_bitmap_page_writes":original.ledger["gc_bitmap_page_writes"],
        "segmented_GC_bitmap_page_writes":segmented.ledger["gc_bitmap_page_writes"],
        "segmented_live_bitmap_pages":segmented.bitmap_pages,
        "segmented_matches_storage":segmented.segment_matches_storage(),
        "proof_of_joint_lower_bound":False,
        "root_novelty":"OPEN_UNPROVED",
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2))
