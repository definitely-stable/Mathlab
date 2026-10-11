"""DAG-002 G2-B2-C1: page-read-backed Felsner+power *reference updater*.

Unlike C0's PowerAnchorIndex, ALL historical ancestor bits, labels and
chain-family metadata used by append() are obtained via PageImageStore.read.
No prior graph/F_i objects persist in this updater. Backend page images are
RAM-hosted simulator storage, not a filesystem; the explicit budget limits
MODELED LOGICAL SCRATCH ONLY, not process RSS or OS cache. Directory lookups,
page allocation, WAL, fsync and crash consistency are not priced.
"""
from __future__ import annotations

import json
import struct
from dataclasses import dataclass

from dag002_g2b2_power_anchors import highest_crossed_power, Label
from dag002_g2b2c_paid_ledger import (
    PageImageStore, encode_label, decode_label, encode_parents,
)
from dag002_g2b2_felsner import source_dfs


def _label_fields(payload: bytes) -> tuple[int, int, int, int, int]:
    chain, anchor, _ = decode_label(payload)  # validates size & duplicate IDs
    _, _, rank, power, lp, _ = struct.unpack_from("<IiIIiH", payload)
    return chain, anchor, rank, power, lp


def _manifest_encode(n: int, heads: list[int], groups: list[list[int]]) -> bytes:
    pieces = [struct.pack("<III", n, len(heads), len(groups))]
    for group in groups:
        pieces.append(struct.pack("<I", len(group)))
        for cid in group:
            pieces.append(struct.pack("<II", cid, heads[cid]))
    return b"".join(pieces)


def _manifest_decode(payload: bytes) -> tuple[int, list[int], list[list[int]]]:
    if len(payload) < 12:
        raise ValueError("short persistent manifest")
    n, num_chains, num_groups = struct.unpack_from("<III", payload)
    if num_chains > n or num_groups > n or n > 4096:
        raise ValueError("invalid manifest dimensions")
    heads = [-1] * num_chains
    groups: list[list[int]] = []
    cursor = 12
    seen: set[int] = set()
    for level in range(1, num_groups + 1):
        if cursor + 4 > len(payload):
            raise ValueError("truncated family count")
        count, = struct.unpack_from("<I", payload, cursor)
        cursor += 4
        if count > level or cursor + 8 * count > len(payload):
            raise ValueError("invalid family length")
        group = []
        for _ in range(count):
            cid, head = struct.unpack_from("<II", payload, cursor)
            cursor += 8
            if cid >= num_chains or cid in seen or head >= n:
                raise ValueError("duplicate/invalid chain or head")
            seen.add(cid)
            heads[cid] = head
            group.append(cid)
        groups.append(group)
    if cursor != len(payload) or seen != set(range(num_chains)):
        raise ValueError("manifest unreferenced data or missing chain")
    return n, heads, groups


@dataclass(frozen=True)
class ChargedStep:
    vertex: int
    chain: int
    level: int
    anchor: int
    read_pages: int
    write_pages: int
    modeled_scratch_bound: int
    parent_input_bits: int


class BilledPowerUpdater:
    """A complete *abstract page-transfer* updater; NOT a physical/RAM theorem."""
    def __init__(self, horizon: int = 64, page_bytes: int = 64,
                 base: int = 2, modeled_scratch_cap: int = 16384,
                 store: PageImageStore | None = None):
        if not 1 <= horizon <= 4096 or base < 2 or modeled_scratch_cap < 1:
            raise ValueError("invalid horizon/base/scratch cap")
        if store is not None and store.page_bytes != page_bytes:
            raise ValueError("page size changed over restart")
        self.horizon = horizon
        self.base = base
        self.modeled_scratch_cap = modeled_scratch_cap
        self.store = store if store is not None else PageImageStore(page_bytes)
        self.bitset_bytes = (horizon + 7) // 8
        self.steps: list[ChargedStep] = []  # diagnostic only, not updater input
        self.query_pages = 0

    def _state(self) -> tuple[int, list[int], list[list[int]], int]:
        if "manifest" not in self.store.images:
            return 0, [], [], 0
        image = self.store.read("manifest")
        n, heads, groups = _manifest_decode(image)
        return n, heads, groups, len(image)

    def _support(self, node: int) -> int:
        data = self.store.read(f"support:{node}")
        if len(data) != self.bitset_bytes:
            raise ValueError("invalid stored support bitmap")
        return int.from_bytes(data, "little")

    def _label(self, node: int) -> tuple[int, int, int, int, int]:
        return _label_fields(self.store.read(f"label:{node}"))

    def append(self, parents: tuple[int, ...]) -> ChargedStep:
        read_start, write_start = self.store.read_pages, self.store.write_pages
        n, heads, groups, manifest_len = self._state()
        if n >= self.horizon or parents != tuple(sorted(set(parents))):
            raise ValueError("invalid APPEND_SINK command or horizon exhausted")
        if any(not 0 <= p < n for p in parents):
            raise ValueError("non-old parent")
        # Conservative model-specific logical byte-buffer upper bound.
        # It deliberately excludes Python interpreter/RSS, backing store and
        # allocator/directory; cannot be called an actual RAM cap.
        upper_manifest = 12 + 12 * (n + 1)
        scratch = (max(manifest_len, upper_manifest)
                   + 3 * self.bitset_bytes + 2 + 4 * len(parents)
                   + 22 + 8 * (n + 1) + 64)
        if scratch > self.modeled_scratch_cap:
            raise MemoryError("modeled logical scratch budget exceeded")

        # No cached ancestor arrays: every old ancestor bitset is read through
        # the same physical-page-image abstraction as the other comparators.
        ancestor_bits = 1 << n
        for p in parents:
            ancestor_bits |= self._support(p)
        rank = ancestor_bits.bit_count()

        best_parent, parent_rank = -1, 0
        for p in parents:
            _, _, r, _, _ = self._label(p)
            if r > parent_rank or (r == parent_rank and
                                   (best_parent < 0 or p < best_parent)):
                best_parent, parent_rank = p, r
        power = highest_crossed_power(parent_rank, rank, self.base)

        # Obtain every predecessor/anchor instruction by PAID label read.
        anchor = best_parent
        while anchor >= 0:
            _, next_anchor, _, prev_power, _ = self._label(anchor)
            if prev_power >= power:
                break
            anchor = next_anchor

        # Felsner's first viable family; chain tops come from the PAID
        # serialized manifest, not a retained Python partition oracle.
        level = 1
        while True:
            if level > len(groups):
                groups.append([])
            current = groups[level - 1]
            eligible = [c for c in current if
                        ancestor_bits & (1 << heads[c])]
            if eligible or len(current) < level:
                break
            level += 1
        if eligible:
            selected = min(eligible)
            heads[selected] = n
        else:
            selected = len(heads)
            heads.append(n)
        if level == 1:
            if not eligible:
                groups[0].append(selected)
        else:
            prev, curr = groups[level - 2][:], groups[level - 1][:]
            groups[level - 2] = [c for c in curr if c != selected]
            groups[level - 1] = prev + [selected]

        # Build restricted chain top labels using PAID prior label reads and
        # a PAID anchor support read. No hidden predecessor edge/chain table.
        restricted = ancestor_bits & ~(
            self._support(anchor) if anchor >= 0 else 0)
        tops: dict[int, int] = {selected: n}
        for vertex in range(n):
            if restricted & (1 << vertex):
                c, _, _, _, _ = self._label(vertex)
                tops[c] = max(tops.get(c, -1), vertex)
        label = Label(selected, anchor, tuple(sorted(tops.items())),
                      rank, power, best_parent)
        # Write immutable support/label/parent records first and publish
        # the mutable manifest last. There is no crash-safe atomic root here.
        self.store.write(f"parents:{n}", encode_parents(parents), immutable=True)
        self.store.write(f"support:{n}",
                         ancestor_bits.to_bytes(self.bitset_bytes, "little"),
                         immutable=True)
        self.store.write(f"label:{n}", encode_label(label), immutable=True)
        self.store.write("manifest", _manifest_encode(n + 1, heads, groups),
                         immutable=False)
        step = ChargedStep(n, selected, level, anchor,
                           self.store.read_pages - read_start,
                           self.store.write_pages - write_start,
                           scratch, n)
        self.steps.append(step)
        return step

    def query(self, source: int, target: int) -> tuple[bool, int]:
        start = self.store.read_pages
        n, _, _, _ = self._state()
        if not (0 <= source < n and 0 <= target < n):
            raise ValueError("invalid vertex ID")
        if source == target:
            return True, self.store.read_pages - start
        if source > target:
            return False, self.store.read_pages - start
        chain, _, _, _, _ = self._label(source)
        at = target
        while at >= 0:
            data = self.store.read(f"label:{at}")
            _, nxt, tops = decode_label(data)
            if chain in tops:
                return source <= tops[chain], self.store.read_pages - start
            at = nxt
        return False, self.store.read_pages - start

    def report(self) -> dict:
        s = self.store
        n, heads, groups, _ = self._state()
        labels = sum(len(v) for k, v in s.images.items()
                     if k.startswith("label:"))
        support = sum(len(v) for k, v in s.images.items()
                      if k.startswith("support:"))
        return {
            "vertices": n,
            "chains": len(heads),
            "family_count": len(groups),
            "label_bytes": labels,
            "support_bytes": support,
            "parent_input_bits": n * (n - 1) // 2,
            "page_reads": s.read_pages,
            "page_writes": s.write_pages,
            "read_address_bytes": s.read_address_bytes,
            "write_address_bytes": s.write_address_bytes,
            "live_padded_bytes": s.size_report()["live_padded_bytes"],
            "max_modeled_logical_scratch":
                max((x.modeled_scratch_bound for x in self.steps), default=0),
            "cap_on_actual_process_rss": False,
            "all_previous_graph_reads_through_page_api": True,
            "backing_store_in_process_memory": True,
            "directory_allocator_crash_cost_charged": False,
            "novelty": "CLASSICAL_LOGICAL_PAGE_REFERENCE; NO_LOWER_BOUND",
        }


def census_four() -> dict:
    pairs = [(u, v) for v in range(4) for u in range(v)]
    checked, query_cases = 0, 0
    for mask in range(1 << len(pairs)):
        trace = tuple(
            tuple(u for i, (u, dest) in enumerate(pairs)
                  if dest == v and mask & (1 << i))
            for v in range(4))
        for page in (16, 64):
            db = BilledPowerUpdater(4, page)
            for v, ps in enumerate(trace):
                db.append(ps)
                for u in range(v + 1):
                    for t in range(v + 1):
                        got, pages = db.query(u, t)
                        assert got == source_dfs(trace, u, t), (mask, page, u, t)
                        assert pages >= 1  # manifest publication read
                        query_cases += 1
            assert db.report()["all_previous_graph_reads_through_page_api"]
            checked += 1
    return {
        "traces": checked,
        "query_instances": query_cases,
        "result": "FINITE_PAID_PAGE_REFERENCE_PASS; NO_DEVICE_IO_CLAIM",
    }


if __name__ == "__main__":
    print(json.dumps(census_four(), sort_keys=True))
