"""DAG-002 G2-B2-B: SEA 2025 power-anchor selection on Felsner online chains.

Exact Section 3.2.2 definitions with inclusive source rank and a positive
integer multiple x*B**pi. The source Lemma 9 has an apparent length/base-case
convention mismatch: this reference asserts the restricted-set inequality,
but does NOT promote the printed anchor-depth inequality to a verified proof.

Updater uses Felsner's *unpriced* full ancestor oracle; query uses only
published immutable restricted top labels and anchor pointers.
"""
from __future__ import annotations

from dataclasses import dataclass
import json

from dag002_g2b2_felsner import FelsnerUpGrowing, source_dfs


def highest_crossed_power(low: int, high: int, base: int) -> int:
    """Largest pi for which low < x*base**pi <= high, integer x >= 1."""
    if base < 2 or not (0 <= low < high):
        raise ValueError("base>=2 and strictly increasing ranks required")
    step = 1
    pi = 0
    while step * base <= high:
        step *= base
        pi += 1
    while high // step == low // step:
        step //= base
        pi -= 1
    return pi


@dataclass(frozen=True)
class Label:
    chain: int
    anchor: int
    restricted: tuple[tuple[int, int], ...]
    rank: int
    power: int
    lp: int


class PowerAnchorIndex:
    def __init__(self, base: int = 2):
        if base < 2:
            raise ValueError("base B must be >=2")
        self.base = base
        self.partition = FelsnerUpGrowing()
        self.labels: list[Label] = []
        self.parent_commands: list[tuple[int, ...]] = []
        self.query_label_reads: int = 0

    def append(self, parents: tuple[int, ...]) -> Label:
        v = len(self.labels)
        if parents != tuple(sorted(set(parents))):
            raise ValueError("parents must be unique sorted old IDs")
        if any(p < 0 or p >= v for p in parents):
            raise ValueError("parents must be old vertices")
        bitmap = (1 << v)
        for p in parents:
            bitmap |= self.partition.anc[p]
        rank = bitmap.bit_count()
        largest_parent = max(parents, key=lambda p: (
            self.labels[p].rank, -p), default=-1)
        prev_rank = self.labels[largest_parent].rank if largest_parent >= 0 else 0
        power = highest_crossed_power(prev_rank, rank, self.base)

        a = largest_parent
        while a >= 0 and self.labels[a].power < power:
            a = self.labels[a].anchor

        step = self.partition.append(parents)
        assert bitmap == self.partition.anc[v], "independent bitmap construction"
        restricted_bitmap = bitmap & ~(
            self.partition.anc[a] if a >= 0 else 0)
        restricted = tuple(
            (cid, max(node for node in chain
                      if restricted_bitmap & (1 << node)))
            for cid, chain in enumerate(self.partition.chains)
            if any(restricted_bitmap & (1 << node) for node in chain)
        )
        label = Label(step.chain, a, restricted, rank, power, largest_parent)
        self.labels.append(label)
        self.parent_commands.append(parents)
        return label

    def query(self, source: int, target: int) -> tuple[bool, int]:
        n = len(self.labels)
        if not (0 <= source < n and 0 <= target < n):
            raise ValueError("invalid query")
        if source == target:
            return True, 0
        if source > target:
            return False, 0
        wanted = self.labels[source].chain
        curr = target
        reads = 0
        while curr >= 0:
            rec = self.labels[curr]
            reads += 1
            for chain, top in rec.restricted:
                if chain == wanted:
                    self.query_label_reads += reads
                    return source <= top, reads
            curr = rec.anchor
        self.query_label_reads += reads
        return False, reads

    def anchor_depth(self, vertex: int) -> int:
        depth = 0
        while vertex >= 0:
            depth += 1
            vertex = self.labels[vertex].anchor
        return depth

    def restricted_ancestor_count(self, v: int) -> int:
        a = self.labels[v].anchor
        return (self.partition.anc[v] &
                ~(self.partition.anc[a] if a >= 0 else 0)).bit_count()

    def source_lemma_checks(self) -> list[str]:
        errors: list[str] = []
        for v, label in enumerate(self.labels):
            count = self.restricted_ancestor_count(v)
            if count > self.base ** (label.power + 1):
                errors.append(f"restricted count at v={v} exceeds B^(pi+1)")
            if label.anchor >= 0 and not (
                self.partition.anc[v] & (1 << label.anchor)):
                errors.append("anchor is not an ancestor")
            if label.lp >= 0 and label.lp not in self.parent_commands[v]:
                errors.append("lp not a parent")
            if label.anchor >= 0 and self.labels[label.anchor].rank >= label.rank:
                errors.append("anchor must precede vertex")
            if self.labels[v].chain != self.partition.assignment[v]:
                errors.append("chain assignment mismatch")
        return errors

    def report(self) -> dict:
        return {
            "base": self.base,
            "vertices": len(self.labels),
            "chains": len(self.partition.chains),
            "total_restricted_top_pairs":
                sum(len(x.restricted) for x in self.labels),
            "max_anchor_depth":
                max((self.anchor_depth(i) for i in range(len(self.labels))),
                    default=0),
            "source_lemma_errors": self.source_lemma_checks(),
            "oracle_bits_unpriced": len(self.labels) ** 2,
            "source_depth_convention": "UNRESOLVED_LENGTH_VS_ZERO_BASE_CASE",
            "claim": "EXACT_FINITE_SOURCE_RESTRICTED_BOUND; NO_NEW_THEOREM",
        }


def five_vertex_power_census() -> dict:
    pairs = [(u, v) for v in range(5) for u in range(v)]
    traces = 0
    queries = 0
    for mask in range(1 << len(pairs)):
        parents = tuple(
            tuple(u for bit, (u, t) in enumerate(pairs)
                  if t == v and mask & (1 << bit))
            for v in range(5))
        for b in (2, 3, 4):
            index = PowerAnchorIndex(b)
            old_records: tuple[Label, ...] = ()
            for v, p in enumerate(parents):
                index.append(p)
                assert tuple(index.labels[:-1]) == old_records
                old_records = tuple(index.labels)
                assert not index.partition.invariant_errors()
                assert not index.source_lemma_checks(), (mask, b, v)
                for u in range(v + 1):
                    for t in range(v + 1):
                        assert index.query(u, t)[0] == source_dfs(parents, u, t), (
                            mask, b, u, t)
                        queries += 1
            traces += 1
    return {
        "traces": traces,
        "queries": queries,
        "status": "CLASSICAL_SEA_POWER_ANCHOR_EXACT_FINITE_CHECK",
        "source_depth_convention": "UNRESOLVED",
    }


if __name__ == "__main__":
    print(json.dumps(five_vertex_power_census(), sort_keys=True))
