#!/usr/bin/env python3
"""G2B-B2: sound anchored SAT encoding for exact q5,m3,w2,d2 ASET.

The generation is dependency-free. External solvers are discovery tools;
only G1A independently verified SAT witnesses or independently checked
full UNSAT proofs may close A_5^set(3,2,2).

The anchor x_(0,1,1)=1 is valid ONLY for the specific target k=11:
at most two support-one columns per coordinate axis, so any 11-set
has a support-two element and the GF(5) coordinate-monomial group
acts transitively on all support-two nonzero columns.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import permutations, product
import json
from typing import Iterable, Sequence

from lent_exhaustive import Vector, is_exact_family
from lent_hypergraph import ForbiddenHypergraph, build_forbidden_hypergraph, independent

TARGET_Q, TARGET_M, TARGET_W, TARGET_K = 5, 3, 2, 11
ANCHOR: Vector = (0, 1, 1)


def field_action(vector: Vector, permutation: tuple[int, ...],
                 scales: tuple[int, ...], q: int) -> Vector:
    """Output coordinate permutation[i] is scale*input[i] (nonzero scale).

    Supports and all subset-sum equalities are preserved by linear
    monomial (invertible) actions. Translation is NOT an allowed action.
    """
    m = len(vector)
    if (len(permutation) != m or tuple(sorted(permutation)) != tuple(range(m))
            or len(scales) != m or any(type(s) is not int or not 0 < s < q
                                      for s in scales)):
        raise ValueError("invalid permutation or nonzero coordinate scalings")
    result = [0] * m
    for i, val in enumerate(vector):
        result[permutation[i]] = (scales[permutation[i]] * val) % q
    return tuple(result)


def all_actions(q: int, m: int):
    for permutation in permutations(range(m)):
        for scales in product(range(1, q), repeat=m):
            yield permutation, scales


def canonical_anchor_family(family: Sequence[Vector]) -> tuple[Vector, ...]:
    """Return isomorphic family including (0,1,1), or reject missing support2.

    Deterministically choose the lexicographically least transformed family
    whose selected columns contain anchor. Never assume this theorem for
    smaller cardinality or other fields; only a witness-normalizer.
    """
    if len(set(family)) != len(family) or any(
            len(v) != 3 or any(type(t) is not int or t not in range(5)
                               for t in v)
            or not 1 <= sum(x != 0 for x in v) <= 2 for v in family):
        raise ValueError("invalid distinct nonzero support<=2 GF5 family")
    if not any(sum(x != 0 for x in v) == 2 for v in family):
        raise ValueError("family contains no support-two column")
    choices = [
        tuple(sorted(field_action(v, p, s, 5) for v in family))
        for p, s in all_actions(5, 3)
        if ANCHOR in (field_action(v, p, s, 5) for v in family)
    ]
    if not choices:
        raise AssertionError("support-two orbit has no canonical anchor")
    return min(choices)


def anchor_index(graph: ForbiddenHypergraph) -> int:
    if (graph.q, graph.m, graph.w) != (5, 3, 2):
        raise ValueError("anchor proof is pinned to (q,m,w)=(5,3,2)")
    return graph.columns.index(ANCHOR)


def formula_source_hash(graph: ForbiddenHypergraph) -> str:
    """Canonical columns + forbidden masks SHA, pinned to enumeration."""
    model = {
        "q": graph.q, "m": graph.m, "w": graph.w, "d": 2,
        "columns": [list(v) for v in graph.columns],
        "minimal_edges": [str(e) for e in graph.edges],
    }
    return sha256((json.dumps(model, sort_keys=True,
                               separators=(",", ":")) + "\n").encode()).hexdigest()


@dataclass
class Formula:
    clauses: list[tuple[int, ...]]
    var_count: int
    candidate_count: int
    target: int
    anchor: int | None
    # (number of considered original columns, min target threshold) -> var
    wires: dict[tuple[int, int], int]

    def dimacs(self) -> str:
        lines = [f"p cnf {self.var_count} {len(self.clauses)}"]
        lines.extend(" ".join(map(str, clause)) + " 0" for clause in self.clauses)
        return "\n".join(lines) + "\n"

    def assignment_for(self, chosen: Iterable[int]) -> dict[int, bool]:
        """Canonical extension of original decisions to all DP variables."""
        selected = set(chosen)
        if any(type(i) is not int or not 0 <= i < self.candidate_count
               for i in selected):
            raise ValueError("selected index out of range")
        truth = {i + 1: i in selected for i in range(self.candidate_count)}
        count = 0
        for i in range(1, self.candidate_count + 1):
            count += int(i - 1 in selected)
            for k in range(1, min(i, self.target) + 1):
                truth[self.wires[(i, k)]] = count >= k
        return truth

    def satisfied_by(self, assignment: dict[int, bool]) -> bool:
        if set(assignment) != set(range(1, self.var_count + 1)):
            raise ValueError("must assign every CNF variable")
        return all(any(assignment[abs(lit)] == (lit > 0)
                       for lit in clause) for clause in self.clauses)


def _neg(lit: int | bool) -> int | bool:
    if type(lit) is bool:
        return not lit
    return -lit


def build_atleast_cnf(graph: ForbiddenHypergraph, target: int,
                      anchored: bool = False) -> Formula:
    """Exact Tseitin equivalence to DP prefix-at-least threshold.

    t_(i,k) <-> t_(i-1,k) OR (x_i AND t_(i-1,k-1)).
    Each gate is encoded in both directions, so no spurious SAT state
    can claim cardinality k. For fixed x there is a unique extension.
    """
    n = len(graph.columns)
    if type(target) is not int or not 1 <= target <= n:
        raise ValueError("invalid target cardinality")
    anchor = anchor_index(graph) if anchored else None
    clauses: list[tuple[int, ...]] = []
    def add_clause(*lits: int | bool) -> None:
        # Constants are reduced *before* integer sort (bool subclasses int).
        if any(type(l) is bool and l is True for l in lits):
            return
        vals = {int(l) for l in lits if type(l) is not bool}
        if any(-x in vals for x in vals):
            return
        clauses.append(tuple(sorted(vals, key=lambda v: (abs(v), v < 0))))

    for edge in graph.edges:
        members = [i + 1 for i in range(n) if edge & (1 << i)]
        add_clause(*(-i for i in members))
    if anchor is not None:
        add_clause(anchor + 1)

    wires: dict[tuple[int, int], int] = {}
    next_var = n
    for i in range(1, n + 1):
        x = i
        for k in range(1, min(i, target) + 1):
            next_var += 1
            y = next_var
            wires[(i, k)] = y
            old = wires.get((i-1, k), False)
            lower: int | bool = True if k == 1 else wires.get((i-1, k-1), False)
            # y <-> (old OR (x AND lower)).
            add_clause(_neg(old), y)
            add_clause(_neg(x), _neg(lower), y)
            add_clause(_neg(y), old, x)
            add_clause(_neg(y), old, lower)
    add_clause(wires[(n, target)])
    return Formula(clauses, next_var, n, target, anchor, wires)


def verify_11_witness(indices: Iterable[int], graph: ForbiddenHypergraph) -> list[Vector]:
    """Check witness using G1A sum oracle, not the forbidden hypergraph."""
    chosen = sorted(set(indices))
    if len(chosen) != 11 or any(type(i) is not int or not 0 <= i < len(graph.columns)
                                for i in chosen):
        raise ValueError("must select 11 distinct in-range indices")
    columns = [graph.columns[i] for i in chosen]
    if ANCHOR not in columns:
        raise ValueError("unanchored SAT model not part of frozen proof")
    if not is_exact_family(columns, graph.q, 2):
        raise AssertionError("SAT output FAILED independent ASET oracle")
    return columns


def run_foundation() -> None:
    g = build_forbidden_hypergraph(5, 3, 2)
    f = build_atleast_cnf(g, 11, anchored=True)
    assert len(g.columns) == 60 and len(g.edges) == 9990
    assert f.anchor == g.columns.index(ANCHOR)
    assert f.var_count > 60 and len(f.clauses) > 9990
    assert not f.satisfied_by(f.assignment_for(()))
    assert not f.satisfied_by(f.assignment_for((f.anchor,)))
    print("G2BB2_SYMMETRY_ANCHOR_FOUNDATION_PASS")
    print("G2BB2_CARDINALITY_GATE_FOUNDATION_PASS")
    print("G2BB2_MODEL",
          json.dumps({"candidate_count":len(g.columns),
                      "minimal_edges":len(g.edges), "anchor_index":f.anchor,
                      "cnf_variables":f.var_count, "cnf_clauses":len(f.clauses),
                      "source_sha256":formula_source_hash(g),
                      "dimacs_sha256":sha256(f.dimacs().encode()).hexdigest()},
                     sort_keys=True))


if __name__ == "__main__":
    run_foundation()
