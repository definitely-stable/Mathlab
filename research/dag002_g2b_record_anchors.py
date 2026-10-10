"""SEA 2025 Section 3.2.1 record-based anchors on first-compatible chains.

Research-only page-image cost simulator. NOT Felsner's online chain algorithm,
device I/O measurements, or the full SEA 2025 index implementation.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json


@dataclass(frozen=True)
class Record:
    chain: int
    anchor: int
    restricted: tuple[tuple[int, int], ...]


@dataclass(frozen=True)
class Cost:
    parent_input_bits: int
    update_page_reads: int
    update_page_writes: int
    update_address_bytes: int
    label_pages: int
    manifest_pages: int
    max_anchor_depth: int
    workspace_bytes_bound: int


class IndexedDAG:
    def __init__(self, page_bytes: int = 16, horizon: int = 256,
                 depth_cap: int | None = None, seed: int = 73):
        if page_bytes < 8 or horizon < 1 or (depth_cap is not None and depth_cap < 1):
            raise ValueError("invalid page size, horizon or depth cap")
        self.page_bytes, self.horizon = page_bytes, horizon
        self.d = max(1, ((horizon + 1).bit_length() + 7) // 8)
        self.depth_cap, self.seed = depth_cap, seed
        self.records: list[Record] = []
        self.parents: list[tuple[int, ...]] = []  # oracle only, never queried
        self.heads: list[int] = []
        self.update_log: list[Cost] = []
        self.total_label_pages = 0

    def score(self, vertex: int) -> int:
        # Reproducible pseudorandom scores, not truly independent random variables.
        digest = hashlib.blake2b(
            f'{self.seed}:{vertex}'.encode(), digest_size=16).digest()
        return int.from_bytes(digest, 'big')

    def record_bytes(self, rec: Record) -> int:
        return 2 * self.d + 2 + 2 * self.d * len(rec.restricted)

    def pages(self, size: int) -> int:
        return (size + self.page_bytes - 1) // self.page_bytes

    def manifest_pages(self, chains: int | None = None) -> int:
        count = len(self.heads) if chains is None else chains
        return self.pages(4 + self.d * count)

    def append(self, parent_ids: tuple[int, ...]) -> Cost:
        v = len(self.records)
        if v >= self.horizon:
            raise ValueError("horizon exceeded")
        if parent_ids != tuple(sorted(set(parent_ids))):
            raise ValueError("parents must be sorted and unique")
        if any(not 0 <= p < v for p in parent_ids):
            raise ValueError("parent must be an old vertex")
        reads = self.manifest_pages()
        seen: set[int] = set()
        max_buffer = 4 + self.d * len(self.heads)

        def load(i: int) -> Record:
            nonlocal reads, max_buffer
            if i not in seen:
                seen.add(i)
                size = self.record_bytes(self.records[i])
                reads += self.pages(size)
                max_buffer = max(max_buffer, size)
            return self.records[i]

        cache: dict[int, dict[int, int]] = {}

        def top_map(i: int) -> dict[int, int]:
            if i in cache:
                return cache[i]
            rec = load(i)
            value = top_map(rec.anchor).copy() if rec.anchor >= 0 else {}
            for c, node in rec.restricted:
                value[c] = max(value.get(c, -1), node)
            cache[i] = value
            return value

        full: dict[int, int] = {}
        for p in parent_ids:
            for c, t in top_map(p).items():
                full[c] = max(full.get(c, -1), t)
        chain = next((c for c, head in enumerate(self.heads)
                      if full.get(c, -1) >= head), len(self.heads))
        if chain == len(self.heads):
            self.heads.append(v)
        else:
            self.heads[chain] = v
        full[chain] = v

        candidates: set[int] = set()
        for p in parent_ids:
            curr = p
            while curr >= 0:
                rec = load(curr)
                if self.score(curr) > self.score(v):
                    candidates.add(curr)
                curr = rec.anchor

        def restrict(a: int) -> tuple[tuple[int, int], ...]:
            old = top_map(a) if a >= 0 else {}
            return tuple(sorted((c, t) for c, t in full.items()
                                if t > old.get(c, -1)))

        chosen = -1
        restricted = restrict(-1)
        best = (len(restricted), 0, -1)
        for a in sorted(candidates):
            depth, curr = 0, a
            while curr >= 0:
                depth += 1
                curr = load(curr).anchor
            if self.depth_cap is not None and depth >= self.depth_cap:
                continue
            target = restrict(a)
            ranking = (len(target), depth, a)
            if ranking < best:
                chosen, restricted, best = a, target, ranking

        rec = Record(chain, chosen, restricted)
        self.records.append(rec)
        self.parents.append(parent_ids)
        label_pages = self.pages(self.record_bytes(rec))
        self.total_label_pages += label_pages
        manifest_pages = self.manifest_pages()
        writes = label_pages + manifest_pages
        workspace = self.record_bytes(rec) + 4 + self.d * len(self.heads) + max_buffer
        cost = Cost(v, reads, writes,
                    (reads + writes) * (1 + 2 * self.d),
                    label_pages, manifest_pages, self.anchor_depth(v), workspace)
        self.update_log.append(cost)
        return cost

    def anchor_depth(self, i: int) -> int:
        depth = 0
        while i >= 0:
            depth += 1
            i = self.records[i].anchor
        return depth

    def query(self, source: int, target: int) -> tuple[bool, int]:
        n = len(self.records)
        if not (0 <= source < n and 0 <= target < n):
            raise ValueError("invalid query")
        if source == target:
            return True, 0
        if source > target:
            return False, 0
        src = self.records[source]
        reads = self.pages(self.record_bytes(src))
        chain = src.chain
        curr = target
        while curr >= 0:
            rec = self.records[curr]
            reads += self.pages(self.record_bytes(rec))
            tops = dict(rec.restricted)
            if chain in tops:
                return source <= tops[chain], reads
            curr = rec.anchor
        return False, reads

    def report(self) -> dict:
        return {
            "vertices": len(self.records),
            "chains": len(self.heads),
            "label_pages": self.total_label_pages,
            "current_manifest_pages": self.manifest_pages(),
            "total_update_page_reads": sum(c.update_page_reads for c in self.update_log),
            "total_update_page_writes": sum(c.update_page_writes for c in self.update_log),
            "max_anchor_depth": max((c.max_anchor_depth for c in self.update_log), default=0),
        }


def source_reach(parents: tuple[tuple[int, ...], ...], u: int, v: int) -> bool:
    pending, seen = [v], set()
    while pending:
        node = pending.pop()
        if node == u:
            return True
        if node not in seen:
            seen.add(node)
            pending.extend(parents[node])
    return False


def fan_in_comparison() -> dict:
    parents = [() for _ in range(32)] + [tuple(range(32))]
    parents.extend((v - 1,) for v in range(33, 160))
    results = {}
    for name, cap in (("no_anchor", 1), ("record_anchor_D3", 3)):
        db = IndexedDAG(page_bytes=16, horizon=160, depth_cap=cap)
        for p in parents:
            db.append(p)
        for u in (0, 1, 31, 32, 100, 159):
            for v in (31, 32, 100, 159):
                assert db.query(u, v)[0] == source_reach(tuple(parents), u, v)
        results[name] = {
            **db.report(),
            "sample_query_pages": sum(db.query(u, 159)[1]
                                      for u in (0, 31, 32, 159)),
        }
    return results


def demo() -> dict:
    scenarios = {
        "chain": [()] + [(i - 1,) for i in range(1, 160)],
        "antichain": [() for _ in range(160)],
        "diamond": [(), (), (0, 1), (0, 1, 2)],
    }
    result = {}
    for name, parents in scenarios.items():
        db = IndexedDAG(page_bytes=16, horizon=160, depth_cap=8)
        for p in parents:
            db.append(p)
        for target in range(len(parents)):
            for source in range(len(parents)):
                assert db.query(source, target)[0] == source_reach(
                    tuple(parents), source, target)
        result[name] = db.report()
    return {**result, "fan_in_32": fan_in_comparison()}


if __name__ == "__main__":
    print(json.dumps(demo(), sort_keys=True))
