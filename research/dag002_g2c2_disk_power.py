"""DAG-002 C2-B2: real-file Felsner + SEA power anchor reachability index.

Fully paid application-page and directory reads for all PREVIOUS VERTEX
DATA and published family manifest. Same immutable source parent codec as
the disk lazy and bitmap comparator. Explicitly NOT a production persistence,
bounded-RSS, trusted-storage or block-device lower-bound implementation.

References: SEA 2025 §3.2.2, Felsner 1994 up-growing chain partition.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import struct

from dag002_g2c2_file_store import FilePageStore
from dag002_g2c2_disk_reach import encode_parents
from dag002_g2b2_power_anchors import Label, highest_crossed_power
from dag002_g2b2c_paid_ledger import encode_label, decode_label

_MAGIC = b"D2POWR02"
_HEAD = struct.Struct("<8sIIIII")
_VERSION = 1


def parse_label(data: bytes) -> tuple[int, int, int, int, int]:
    chain, anchor, _ = decode_label(data)
    _, _, rank, power, lp, _ = struct.unpack_from("<IiIIiH", data)
    return chain, anchor, rank, power, lp


def encode_state(n: int, horizon: int, base: int,
                 heads: list[int], groups: list[list[int]]) -> bytes:
    values = [_HEAD.pack(_MAGIC, _VERSION, horizon, base, n, len(groups)),
              struct.pack("<I", len(heads))]
    for level, group in enumerate(groups, 1):
        if len(group) > level:
            raise ValueError("Felsner capacity exceeded")
        values.append(struct.pack("<I", len(group)))
        for cid in group:
            if not 0 <= cid < len(heads):
                raise ValueError("invalid chain in family")
            values.append(struct.pack("<II", cid, heads[cid]))
    return b"".join(values)


def decode_state(data: bytes, horizon: int,
                 base: int) -> tuple[int, list[int], list[list[int]]]:
    if len(data) < _HEAD.size + 4:
        raise ValueError("truncated manifest")
    magic, version, persisted_horizon, persisted_base, n, k = _HEAD.unpack_from(data)
    if (magic, version, persisted_horizon, persisted_base) != (
            _MAGIC, _VERSION, horizon, base):
        raise ValueError("wrong Power manifest version or parameters")
    if n > horizon or k > n:
        raise ValueError("invalid manifest node/family count")
    total_chains, = struct.unpack_from("<I", data, _HEAD.size)
    if total_chains > n:
        raise ValueError("too many chains")
    offset = _HEAD.size + 4
    heads = [-1] * total_chains
    groups: list[list[int]] = []
    seen: set[int] = set()
    for level in range(1, k+1):
        if offset+4 > len(data):
            raise ValueError("truncated family")
        count, = struct.unpack_from("<I", data, offset)
        offset += 4
        if count > level or offset + 8*count > len(data):
            raise ValueError("invalid family size")
        group = []
        for _ in range(count):
            cid, vertex = struct.unpack_from("<II", data, offset)
            offset += 8
            if cid >= total_chains or cid in seen or vertex >= n:
                raise ValueError("invalid duplicate chain or top")
            seen.add(cid)
            heads[cid] = vertex
            group.append(cid)
        groups.append(group)
    if offset != len(data) or seen != set(range(total_chains)):
        raise ValueError("trailing or missing family entries")
    return n, heads, groups


@dataclass(frozen=True)
class Update:
    vertex: int
    chain: int
    level: int
    anchor: int
    logical_page_requests: int
    file_directory_pread_pages: int
    file_payload_pread_pages: int
    modeled_scratch_bytes: int


class DiskPowerIndex:
    def __init__(self, root: str | Path, horizon: int = 64,
                 page_bytes: int = 64, base: int = 2,
                 cache_pages: int = 0, scratch_cap_bytes: int = 32768):
        if not 1 <= horizon <= 4096 or base < 2 or scratch_cap_bytes < 1:
            raise ValueError("invalid horizon, base or scratch cap")
        self.store = FilePageStore(root, page_bytes, cache_pages)
        self.horizon, self.base = horizon, base
        self.scratch_cap_bytes = scratch_cap_bytes
        self.bitmap_bytes = (horizon+7)//8

    def state(self) -> tuple[int, list[int], list[list[int]]]:
        if not self.store.exists("manifest"):
            return 0, [], []
        return decode_state(self.store.read("manifest"),
                            self.horizon, self.base)

    def _support(self, vertex: int) -> int:
        image = self.store.read(f"support:{vertex}")
        if len(image) != self.bitmap_bytes:
            raise ValueError("bad serialized ancestry support")
        return int.from_bytes(image, "little")

    def _label(self, vertex: int) -> tuple[int, int, int, int, int]:
        return parse_label(self.store.read(f"label:{vertex}"))

    def append(self, parents: tuple[int, ...]) -> Update:
        before = self.store.report()
        n, heads, groups = self.state()
        if n >= self.horizon or parents != tuple(sorted(set(parents))):
            raise ValueError("noncanonical parents or horizon")
        if any(p < 0 or p >= n for p in parents):
            raise ValueError("parent must precede new sink")
        scratch = (12*(n+1) + 3*self.bitmap_bytes + 4*len(parents)
                   + 8*(n+1) + 256)
        if scratch > self.scratch_cap_bytes:
            raise MemoryError("modeled logical scratch cap exceeded")

        ancestors = 1 << n
        for p in parents:
            ancestors |= self._support(p)
        rank = ancestors.bit_count()
        best_parent, prev_rank = -1, 0
        for p in parents:
            _, _, r, _, _ = self._label(p)
            if r > prev_rank or (r == prev_rank and
                                 (best_parent < 0 or p < best_parent)):
                best_parent, prev_rank = p, r
        power = highest_crossed_power(prev_rank, rank, self.base)
        anchor = best_parent
        while anchor >= 0:
            _, successor, _, prev_power, _ = self._label(anchor)
            if prev_power >= power:
                break
            anchor = successor

        level = 1
        while True:
            if level > len(groups):
                groups.append([])
            group = groups[level-1]
            eligible = [cid for cid in group if
                        ancestors & (1 << heads[cid])]
            if eligible or len(group) < level:
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
            old_prev = groups[level-2][:]
            old_current = groups[level-1][:]
            groups[level-2] = [cid for cid in old_current
                               if cid != selected]
            groups[level-1] = old_prev + [selected]

        restricted = ancestors & ~(
            self._support(anchor) if anchor >= 0 else 0)
        tops: dict[int, int] = {selected: n}
        for old in range(n):
            if restricted & (1 << old):
                chain, _, _, _, _ = self._label(old)
                tops[chain] = max(tops.get(chain, -1), old)
        label = Label(selected, anchor, tuple(sorted(tops.items())),
                      rank, power, best_parent)

        # No transactional durability is claimed: manifest-last only orders
        # userspace system calls, without fsync or atomic directory roots.
        self.store.write(f"parents:{n}", encode_parents(parents),
                         immutable=True)
        self.store.write(f"support:{n}",
                         ancestors.to_bytes(self.bitmap_bytes, "little"),
                         immutable=True)
        self.store.write(f"label:{n}", encode_label(label),
                         immutable=True)
        self.store.write("manifest",
                         encode_state(n+1, self.horizon, self.base, heads,
                                      groups),
                         immutable=False)
        after = self.store.report()
        return Update(n, selected, level, anchor,
                      after["logical_page_requests"] -
                      before["logical_page_requests"],
                      after["os_pread_directory_pages"] -
                      before["os_pread_directory_pages"],
                      after["os_pread_payload_pages"] -
                      before["os_pread_payload_pages"],
                      scratch)

    def query(self, source: int, target: int) -> tuple[bool, int]:
        before = self.store.read_requests
        n, _, _ = self.state()
        if not (0 <= source < n and 0 <= target < n):
            raise ValueError("unknown published vertex")
        if source == target:
            return True, self.store.read_requests-before
        if source > target:
            return False, self.store.read_requests-before
        chain, _, _, _, _ = self._label(source)
        at = target
        while at >= 0:
            _, next_anchor, tops = decode_label(
                self.store.read(f"label:{at}"))
            if chain in tops:
                return source <= tops[chain], self.store.read_requests-before
            at = next_anchor
        return False, self.store.read_requests-before

    def report(self) -> dict:
        n, heads, groups = self.state()
        return {
            "method": "FELSNER_POWER",
            "vertices": n,
            "chains": len(heads),
            "groups": len(groups),
            "input_incidence_bits": n*(n-1)//2,
            "charged_all_historical_support_reads": True,
            "directory_lookup_paid": True,
            "model_scratch_cap_bytes": self.scratch_cap_bytes,
            "process_rss_bounded": False,
            "kernel_cache_bounded": False,
            "crash_durable": False,
            "physical_ssd_io_measured": False,
            "novel_theorem_proven": False,
            **self.store.report(),
        }

    def close(self) -> None:
        self.store.close()

    def __enter__(self) -> "DiskPowerIndex":
        return self

    def __exit__(self, *_args) -> None:
        self.close()
