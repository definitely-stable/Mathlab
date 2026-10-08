#!/usr/bin/env python3
"""G2B exact d=2 ASET forbidden-hypergraph oracle and bounded search.

The hyperedges come ONLY from collisions of admissible subset sums (size <=2).
In particular a+b+c=0 by itself is not a forbidden triple for d=2.
All arithmetic here uses prime fields q in {3,5,7}, not arbitrary GF(q).
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
from typing import Sequence

from lent_exhaustive import Vector, is_exact_family, sparse_nonzero_vectors
from lent_extremal import lent_upper_v


@dataclass(frozen=True)
class ForbiddenHypergraph:
    q: int
    m: int
    w: int
    columns: tuple[Vector, ...]
    edges: tuple[int, ...]  # vertex masks; an edge cannot be wholly selected


def build_forbidden_hypergraph(q: int, m: int, w: int) -> ForbiddenHypergraph:
    """Exact minimal forbidden edges, derived from actual subset collisions.

    Each pair of distinct subsets A,B of size at most two with equal sums
    yields the forbidden edge A symmetric-difference B. Common elements
    cancel, so selecting the edge already reproduces the collision.
    """
    if q not in (3, 5, 7) or m < 1 or not 1 <= w < m + 1:
        raise ValueError("G2B supports prime q=3,5,7 and 1<=w<=m")
    columns = tuple(sparse_nonzero_vectors(q, m, w))
    buckets: dict[Vector, list[int]] = defaultdict(list)
    buckets[(0,) * m].append(0)
    for i, vector in enumerate(columns):
        buckets[vector].append(1 << i)
    for i, j in combinations(range(len(columns)), 2):
        state = tuple((a + b) % q for a, b in zip(columns[i], columns[j]))
        buckets[state].append((1 << i) | (1 << j))

    raw_edges: set[int] = set()
    for same_sum_subsets in buckets.values():
        for left, right in combinations(same_sum_subsets, 2):
            edge = left ^ right  # cancel the common subset
            if not 2 <= edge.bit_count() <= 4:
                raise AssertionError("unexpected forbidden edge size")
            raw_edges.add(edge)

    # Discard redundant supersets; their smaller forbidden edges suffice.
    pairs = {edge for edge in raw_edges if edge.bit_count() == 2}
    triples = {edge for edge in raw_edges if edge.bit_count() == 3}
    minimal: list[int] = []
    for edge in sorted(raw_edges, key=lambda v: (v.bit_count(), v)):
        if edge.bit_count() > 2 and any((p & edge) == p for p in pairs):
            continue
        if edge.bit_count() > 3 and any((t & edge) == t for t in triples):
            continue
        minimal.append(edge)
    return ForbiddenHypergraph(q, m, w, columns, tuple(minimal))


def independent(mask: int, edges: Sequence[int]) -> bool:
    """True exactly when the chosen vertices contain no forbidden edge."""
    if mask < 0:
        raise ValueError("mask must be nonnegative")
    return all((mask & edge) != edge for edge in edges)


def verify_independent_oracle(graph: ForbiddenHypergraph, mask: int) -> bool:
    """Use the pre-existing, independently written subset-sum oracle."""
    if mask >> len(graph.columns):
        raise ValueError("mask contains vertices outside the graph")
    selected = [
        column for i, column in enumerate(graph.columns) if mask & (1 << i)
    ]
    return is_exact_family(selected, graph.q, 2)


def solve_exact_or_certified_interval(
    graph: ForbiddenHypergraph, max_nodes: int
) -> dict[str, object]:
    """Deterministic include/exclude B&B, preserving a rigorous upper bound.

    If the node budget is exhausted, the upper bound covers every unresolved
    search subtree. No heuristic cutoff is ever represented as exact.
    Only sound size pruning and logically forced exclusions are used.
    """
    if max_nodes < 1:
        raise ValueError("max_nodes must be positive")
    n = len(graph.columns)
    incident: list[list[int]] = [[] for _ in range(n)]
    for edge in graph.edges:
        rest = edge
        while rest:
            bit = rest & -rest
            incident[bit.bit_length() - 1].append(edge)
            rest ^= bit
    order = sorted(range(n), key=lambda i: (-len(incident[i]), i))
    global_upper = lent_upper_v(graph.q, graph.m, 2, graph.w)
    pending: list[tuple[int, int]] = [(0, (1 << n) - 1)]
    nodes = 0
    best_mask = 0
    best_size = 0

    while pending and nodes < max_nodes:
        chosen, available = pending.pop()
        nodes += 1
        size = chosen.bit_count()
        if size > best_size:
            best_size, best_mask = size, chosen
        if size + available.bit_count() <= best_size or best_size == global_upper:
            continue

        vertex = next(i for i in order if available & (1 << i))
        bit = 1 << vertex
        remaining = available ^ bit
        # Both branches are exhaustive. The exclude branch runs second.
        pending.append((chosen, remaining))

        included = chosen | bit
        forbidden = 0
        valid = True
        for edge in incident[vertex]:
            # Any previously excluded vertex makes this edge irrelevant.
            if edge & ~(included | remaining):
                continue
            still_available = edge & remaining
            if not still_available:
                valid = False
                break
            if still_available.bit_count() == 1:
                # All other vertices of this edge are included. The final
                # vertex is now provably impossible and may be removed.
                forbidden |= still_available
        if valid:
            pending.append((included, remaining & ~forbidden))

    upper = max(
        best_size,
        max(
            (
                min(global_upper, chosen.bit_count() + available.bit_count())
                for chosen, available in pending
            ),
            default=best_size,
        ),
    )
    if not independent(best_mask, graph.edges):
        raise AssertionError("solver returned forbidden-edge witness")
    if not verify_independent_oracle(graph, best_mask):
        raise AssertionError("solver witness failed independent ASET oracle")
    return {
        "q": graph.q,
        "m": graph.m,
        "w": graph.w,
        "d": 2,
        "candidates": n,
        "minimal_edges": len(graph.edges),
        "search_nodes": nodes,
        "search_exhausted": not pending,
        "exact": upper == best_size,
        "lower": best_size,
        "upper": upper,
        "witness": [
            list(column)
            for i, column in enumerate(graph.columns)
            if best_mask & (1 << i)
        ],
    }


def run_g2b_phase_a() -> None:
    q3 = solve_exact_or_certified_interval(
        build_forbidden_hypergraph(3, 4, 2), max_nodes=300_000
    )
    if not (q3["exact"] and q3["lower"] == q3["upper"] == 7):
        raise AssertionError("G2B q=3 sparse exact target did not close")
    print("G2B_HYPERGRAPH_ORACLE_PASS")
    print("G2B_Q3_SPARSE_PASS")

    q5 = solve_exact_or_certified_interval(
        build_forbidden_hypergraph(5, 3, 2), max_nodes=25_000
    )
    if not (9 <= q5["lower"] <= q5["upper"] <= 15):
        raise AssertionError("G2B q=5 certified interval unexpected")
    print("G2B_Q5_CERTIFICATE_PASS")
    print("G2B_WITNESS_PASS")
    print("G2B_PHASE_A_PASS")
    print("G2B_Q3_RESULT", q3)
    print("G2B_Q5_RESULT", q5)


if __name__ == "__main__":
    run_g2b_phase_a()
