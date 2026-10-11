"""DAG-002 G2-B2-C0: COMMON byte/page ledger, not a full priced updater.

Three source-equivalent APPEND_SINK variants on one immutable page format:
(1) cold lazy parents, (2) exact ancestor bitmap, (3) Felsner + SEA power anchors.
Stores immutable on-page images and a mutable manifest, charging every
write and every *implemented* query read. Its power-index construction still
invokes an UNPRICED full-ancestry computation and family bookkeeping:
the source of this debt is NOT disguised as zero physical cost.

No physical file, SSD, fsync, concurrency, persistent allocator or timing
claim. References: SEA 2025 §3 and DAG-002 issues #322/#326.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import ceil
import json
import struct

from dag002_g2b2_power_anchors import PowerAnchorIndex
from dag002_g2b2_felsner import source_dfs


def u32(x: int) -> bytes:
    if x < 0 or x >= 2**32:
        raise ValueError("nonnegative u32 expected")
    return struct.pack("<I", x)


class PageImageStore:
    """A deterministic page-image store: each keyed image starts a fresh page.

    Per-key block padding is charged. Updates to the manifest write a new
    image and retire its prior image logically; old media blocks are NOT
    counted as reclaimed, physical GC is out of scope.
    """
    def __init__(self, page_bytes: int = 64):
        if page_bytes < 16:
            raise ValueError("page must hold at least 16 bytes")
        self.page_bytes = page_bytes
        self.images: dict[str, bytes] = {}
        self.immutable: set[str] = set()
        self.read_pages = 0
        self.write_pages = 0
        self.read_address_bytes = 0
        self.write_address_bytes = 0
        self.read_payload_bytes = 0
        self.write_payload_bytes = 0

    def pages(self, data: bytes) -> int:
        return max(1, ceil(len(data) / self.page_bytes))

    def write(self, key: str, payload: bytes, immutable: bool = True) -> int:
        if key in self.immutable:
            raise ValueError("cannot modify an immutable key")
        if not isinstance(payload, bytes):
            raise TypeError("payload must be immutable bytes")
        if immutable:
            self.immutable.add(key)
        count = self.pages(payload)
        self.write_pages += count
        self.write_address_bytes += 8 * count
        self.write_payload_bytes += self.page_bytes * count
        self.images[key] = payload
        return count

    def read(self, key: str) -> bytes:
        payload = self.images[key]
        count = self.pages(payload)
        self.read_pages += count
        self.read_address_bytes += 8 * count
        self.read_payload_bytes += self.page_bytes * count
        return payload

    def size_report(self) -> dict:
        logical = sum(len(v) for v in self.images.values())
        padded = sum(self.page_bytes * self.pages(v)
                     for v in self.images.values())
        return {
            "logical_bytes": logical,
            "live_padded_bytes": padded,
            "read_pages": self.read_pages,
            "write_pages": self.write_pages,
            "read_address_bytes": self.read_address_bytes,
            "write_address_bytes": self.write_address_bytes,
            "read_payload_bytes": self.read_payload_bytes,
            "write_payload_bytes": self.write_payload_bytes,
        }


def encode_parents(parents: tuple[int, ...]) -> bytes:
    if len(parents) > 65535:
        raise ValueError("too many parents")
    return struct.pack("<H", len(parents)) + b"".join(u32(p) for p in parents)


def decode_parents(payload: bytes) -> tuple[int, ...]:
    if len(payload) < 2:
        raise ValueError("short parents")
    count, = struct.unpack("<H", payload[:2])
    if len(payload) != 2 + count * 4:
        raise ValueError("invalid parent record length")
    return tuple(struct.unpack_from("<I", payload, 2 + 4 * j)[0]
                 for j in range(count))


def encode_label(label) -> bytes:
    # chain:u32, anchor:i32, rank:u32, power:u32, lp:i32, pairs:u16
    if len(label.restricted) > 65535:
        raise ValueError("too many pairs")
    header = struct.pack("<IiIIiH", label.chain, label.anchor,
                         label.rank, label.power, label.lp,
                         len(label.restricted))
    return header + b"".join(struct.pack("<II", c, top)
                             for c, top in label.restricted)


def decode_label(payload: bytes) -> tuple[int, int, dict[int, int]]:
    if len(payload) < 22:
        raise ValueError("short label")
    chain, anchor, rank, power, lp, count = struct.unpack("<IiIIiH", payload[:22])
    if len(payload) != 22 + 8 * count:
        raise ValueError("invalid label")
    tops: dict[int, int] = {}
    for i in range(count):
        c, top = struct.unpack_from("<II", payload, 22 + 8*i)
        if c in tops:
            raise ValueError("duplicate chain in restricted top")
        tops[c] = top
    return chain, anchor, tops


def encode_manifest(index: PowerAnchorIndex) -> bytes:
    part = index.partition
    data = [u32(len(part.families)), u32(len(part.chains))]
    for family in part.families:
        data.append(u32(len(family)))
        for cid in family:
            data.extend((u32(cid), u32(part.heads[cid])))
    return b"".join(data)


class CommonLedger:
    MODES = ("lazy", "bitmap", "felsner_power")

    def __init__(self, mode: str, horizon: int, page_bytes: int = 64, base: int = 2):
        if mode not in self.MODES or not (1 <= horizon <= 4096):
            raise ValueError("invalid mode/horizon")
        self.mode = mode
        self.horizon = horizon
        self.store = PageImageStore(page_bytes)
        self.parents: list[tuple[int, ...]] = []  # reference ONLY, query never uses
        self.power = PowerAnchorIndex(base) if mode == "felsner_power" else None
        self.bitset_bytes = (horizon + 7) // 8
        self.parent_input_bits = 0
        self.support_bits_stored = 0
        self.unpriced_update_oracle = mode == "felsner_power"

    def append(self, parents: tuple[int, ...]) -> None:
        n = len(self.parents)
        if n >= self.horizon:
            raise ValueError("horizon exceeded")
        if parents != tuple(sorted(set(parents))) or any(p < 0 or p >= n
                                                        for p in parents):
            raise ValueError("APPEND_SINK requires sorted unique old parents")
        self.parent_input_bits += n
        self.store.write(f"parents:{n}", encode_parents(parents), immutable=True)
        if self.mode == "lazy":
            pass
        elif self.mode == "bitmap":
            bits = (1 << n)
            for p in parents:
                bits |= int.from_bytes(self.store.read(f"bitmap:{p}"), "little")
            self.store.write(f"bitmap:{n}",
                             bits.to_bytes(self.bitset_bytes, "little"),
                             immutable=True)
        else:
            assert self.power is not None
            label = self.power.append(parents)
            # This writes the support oracle but does NOT pretend that reads
            # performed internally by PowerAnchorIndex were billed.
            anc = self.power.partition.anc[n]
            self.store.write(f"support:{n}",
                             anc.to_bytes(self.bitset_bytes, "little"),
                             immutable=True)
            self.support_bits_stored += self.horizon
            self.store.write(f"label:{n}", encode_label(label),
                             immutable=True)
            self.store.write("manifest", encode_manifest(self.power),
                             immutable=False)
        self.parents.append(parents)

    def query(self, source: int, target: int) -> tuple[bool, int]:
        n = len(self.parents)
        if not (0 <= source < n and 0 <= target < n):
            raise ValueError("invalid query")
        before = self.store.read_pages
        if source == target:
            return True, 0
        if source > target:
            return False, 0
        if self.mode == "bitmap":
            bits = int.from_bytes(self.store.read(f"bitmap:{target}"), "little")
            result = bool(bits & (1 << source))
        elif self.mode == "lazy":
            stack = [target]
            seen: set[int] = set()
            result = False
            while stack:
                v = stack.pop()
                if v == source:
                    result = True
                    break
                if v not in seen:
                    seen.add(v)
                    stack.extend(decode_parents(self.store.read(f"parents:{v}")))
        else:
            chain = decode_label(self.store.read(f"label:{source}"))[0]
            at = target
            result = False
            while at >= 0:
                _, at_next, tops = decode_label(
                    self.store.read(f"label:{at}"))
                if chain in tops:
                    result = source <= tops[chain]
                    break
                at = at_next
        return result, self.store.read_pages - before

    def report(self) -> dict:
        s = self.store
        parent_bytes = sum(len(v) for k, v in s.images.items()
                           if k.startswith("parents:"))
        support_bytes = sum(len(v) for k, v in s.images.items()
                            if k.startswith("support:"))
        label_bytes = sum(len(v) for k, v in s.images.items()
                          if k.startswith("label:") or
                          k.startswith("bitmap:"))
        manifest_bytes = len(s.images.get("manifest", b""))
        return {
            "mode": self.mode,
            "vertices": len(self.parents),
            "page_bytes": s.page_bytes,
            "source_parent_bytes": parent_bytes,
            "index_label_bytes": label_bytes,
            "auxiliary_support_bytes": support_bytes,
            "mutable_manifest_bytes": manifest_bytes,
            "total_live_logical_bytes":
                parent_bytes + support_bytes + label_bytes + manifest_bytes,
            "live_padded_bytes": s.size_report()["live_padded_bytes"],
            "update_write_pages_charged": s.write_pages,
            "update_read_pages_charged": s.read_pages,
            "parent_input_bits": self.parent_input_bits,
            "unpriced_update_ancestor_oracle": self.unpriced_update_oracle,
            "claims_physical_device_io": False,
            "verdict": "INCOMPLETE_COMPARATOR_IF_UNPRICED_ORACLE"
                      if self.unpriced_update_oracle else
                      "FULLY_BILLED_ABSTRACT_PAGE_IMAGES",
        }


def run_case(parents: tuple[tuple[int, ...], ...],
             page_bytes: int = 64) -> dict:
    rows = {}
    for mode in CommonLedger.MODES:
        db = CommonLedger(mode, len(parents), page_bytes)
        query_pages = 0
        for v, p in enumerate(parents):
            db.append(p)
            for source in range(v + 1):
                for target in range(v + 1):
                    got, pages = db.query(source, target)
                    expected = source_dfs(parents, source, target)
                    assert got == expected, (mode, v, source, target)
                    query_pages += pages
        rows[mode] = {**db.report(), "total_query_read_pages": query_pages}
    return rows


def demo() -> dict:
    chain = ((),) + tuple((i-1,) for i in range(1, 64))
    antichain = tuple(() for _ in range(64))
    fanin = tuple(() for _ in range(16)) + (tuple(range(16)),)
    fanin += tuple((i - 1,) for i in range(17, 64))
    return {
        "chain": run_case(chain),
        "antichain": run_case(antichain),
        "fanin": run_case(fanin),
        "scientific_status":
            "EXACT_BYTE_IMAGES; POWER_UPDATER_HAS_UNPRICED_ORACLE",
    }


if __name__ == "__main__":
    print(json.dumps(demo(), sort_keys=True))
