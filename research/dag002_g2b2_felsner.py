"""DAG-002 G2-B2-A: Felsner up-growing online chain partition, not a new theorem.

Original strategy: Bosek et al., On-line Chain Partitions of Orders:
A Survey, Theorem 3.5 (Felsner 1994 / Agarwal-Garg presentation).
Each incoming DAG node is maximal. Families F_i hold <=i chains with
pairwise incomparable chain tops. Assignment to a vertex is immutable.

This is a finite *mathematical* comparator with a fully materialized
ancestor-bitset oracle. Access to this oracle and the F_i manifest is
NOT a priced cell-probe, page-I/O, RAM-bounded, or authenticated model.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
import json


@dataclass(frozen=True)
class Step:
    vertex: int
    level: int
    chain: int
    created: bool
    parent_input_bits: int
    heads_examined: int


class FelsnerUpGrowing:
    def __init__(self) -> None:
        self.parents: list[tuple[int, ...]] = []
        self.anc: list[int] = []
        self.chains: list[list[int]] = []
        self.heads: list[int] = []
        self.families: list[list[int]] = []
        self.assignment: list[int] = []
        self.steps: list[Step] = []

    def append(self, parents: tuple[int, ...]) -> Step:
        v = len(self.parents)
        if parents != tuple(sorted(set(parents))):
            raise ValueError("parents must be sorted and unique")
        if any(p < 0 or p >= v for p in parents):
            raise ValueError("APPEND_SINK parents must already exist")

        # Source reachability oracle, exposed rather than treated as free I/O:
        # old immutable ancestor bitsets are explicitly retained in memory.
        ancestors = (1 << v)
        for p in parents:
            ancestors |= self.anc[p]
        heads_examined = 0
        j = 1
        while True:
            if j > len(self.families):
                self.families.append([])
            group = self.families[j - 1]
            eligible = []
            for cid in group:
                heads_examined += 1
                if (ancestors >> self.heads[cid]) & 1:
                    eligible.append(cid)
            if eligible or len(group) < j:
                break
            j += 1

        if eligible:
            selected = min(eligible)  # deterministic free choice in theorem
            self.chains[selected].append(v)
            self.heads[selected] = v
            created = False
        else:
            selected = len(self.chains)
            self.chains.append([v])
            self.heads.append(v)
            created = True

        if j == 1:
            if created:
                self.families[0].append(selected)
        else:
            # Exact Theorem 3.5 exchange:
            # F_(j-1)'= F_j - {selected}, F_j'=F_(j-1) union {selected}.
            previous = self.families[j - 2][:]
            current = self.families[j - 1][:]
            if created:
                current.append(selected)
            self.families[j - 2] = [cid for cid in current if cid != selected]
            self.families[j - 1] = previous + [selected]

        self.parents.append(parents)
        self.anc.append(ancestors)
        self.assignment.append(selected)
        result = Step(v, j, selected, created, v, heads_examined)
        self.steps.append(result)
        return result

    def reaches(self, source: int, target: int) -> bool:
        """Mathematical oracle only, NOT a costed index query."""
        if not (0 <= source < len(self.anc) and
                0 <= target < len(self.anc)):
            raise ValueError("invalid vertex ID")
        return bool(self.anc[target] & (1 << source))

    def invariant_errors(self) -> list[str]:
        n = len(self.parents)
        errors: list[str] = []
        grouped = [c for family in self.families for c in family]
        if sorted(grouped) != list(range(len(self.chains))):
            errors.append("F_i not a disjoint chain partition")
        if len(self.assignment) != n or len(self.anc) != n:
            errors.append("incomplete vertex records")
        for level, group in enumerate(self.families, 1):
            if len(group) > level:
                errors.append("family capacity exceeded")
            for a, b in combinations(group, 2):
                x, y = self.heads[a], self.heads[b]
                if self.reaches(x, y) or self.reaches(y, x):
                    errors.append("family tops are comparable")
        for cid, chain in enumerate(self.chains):
            if self.heads[cid] != chain[-1]:
                errors.append("chain top mismatch")
            for a, b in zip(chain, chain[1:]):
                if not self.reaches(a, b):
                    errors.append("chain is not ordered by reachability")
        for v, cid in enumerate(self.assignment):
            if v not in self.chains[cid]:
                errors.append("old vertex changed its chain")
        return errors

    def report(self) -> dict:
        return {
            "vertices": len(self.parents),
            "chains": len(self.chains),
            "family_sizes": [len(f) for f in self.families],
            "total_updater_heads_examined": sum(s.heads_examined for s in self.steps),
            "parent_input_bits": sum(s.parent_input_bits for s in self.steps),
            "unpriced_ancestor_oracle_bits": len(self.anc) ** 2,
            "invariant_errors": self.invariant_errors(),
            "proof_status": "CLASSICAL_FELSNER_BOUND; FINITE_ORACLE_ONLY",
        }


def source_dfs(parents: tuple[tuple[int, ...], ...],
               u: int, v: int) -> bool:
    pending = [v]
    seen: set[int] = set()
    while pending:
        node = pending.pop()
        if node == u:
            return True
        if node not in seen:
            seen.add(node)
            pending.extend(parents[node])
    return False


def exact_width(anc: list[int]) -> int:
    """Brute force Dilworth antichain size; tiny independent test oracle."""
    n = len(anc)
    if n > 9:
        raise ValueError("tiny exact-width reference is limited to n<=9")
    best = 0
    for mask in range(1 << n):
        k = mask.bit_count()
        if k <= best:
            continue
        vertices = [v for v in range(n) if mask & (1 << v)]
        if all(not (anc[y] & (1 << x)) for x, y in combinations(vertices, 2)):
            best = k
    return best


def five_vertex_census() -> dict:
    pairs = [(u, v) for v in range(5) for u in range(v)]
    checked = 0
    max_chains, max_width = 0, 0
    for edge_mask in range(1 << len(pairs)):
        parents = tuple(
            tuple(u for i, (u, t) in enumerate(pairs)
                  if t == v and edge_mask & (1 << i))
            for v in range(5))
        db = FelsnerUpGrowing()
        for v, p in enumerate(parents):
            db.append(p)
            assert not db.invariant_errors(), (edge_mask, v, db.report())
            w = exact_width(db.anc)
            assert len(db.chains) <= w * (w + 1) // 2, (edge_mask, v, w)
            assert all(db.reaches(u, t) == source_dfs(parents, u, t)
                       for t in range(v + 1) for u in range(v + 1))
            max_chains = max(max_chains, len(db.chains))
            max_width = max(max_width, w)
        checked += 1
    return {"graphs": checked, "prefixes": checked * 5,
            "max_chains": max_chains, "max_width": max_width,
            "status": "EXACT_CLASSICAL_FELSNER_FINITE_GATE_PASS"}


if __name__ == "__main__":
    print(json.dumps(five_vertex_census(), sort_keys=True))
