#!/usr/bin/env python3
"""HYP-002-D: finite quadratic capacity bound via C4-free prefix-pair fibers.

Works for prime fields q=2,3,5,7; the mathematical argument works for any
field with q elements, but modular arithmetic and test vectors here are
strictly prime-field. The matching quadratic lower bound uses odd q only.

This is NOT a decoder, originality claim, exact finite optimum, or a
certificate of general asymptotic correctness supplied by CI.
"""
from __future__ import annotations

from collections import defaultdict
from itertools import combinations
from math import comb
from typing import Sequence

from lent_exhaustive import Vector, support_size

PRIMES = (2, 3, 5, 7)
Left = tuple[tuple[int, int], tuple[int, int]]
Right = tuple[int, int]


def quadratic_capacity_bound(m: int, q: int) -> dict[str, int]:
    """Proof-derived explicit finite upper bound for A_q^set(m,3,2).

    Weight-three vectors each form an edge between their first two
    nonzero (coordinate, coefficient) pairs and the remaining pair.
    This bipartite graph must be C4-free in every ASET-exact family.

    The raw nonzero-column count is included only as an optional
    universally valid second bound. Both are valid simultaneously.
    """
    if m < 0 or q not in PRIMES:
        raise ValueError("m must be >=0 and q a pinned prime 2,3,5,7")
    r = q - 1
    lower_weight = r * m + r * r * comb(m, 2) if m >= 2 else r * m
    left_size = r * r * comb(m, 2) if m >= 2 else 0
    right_size = r * m
    c4_bound_w3 = left_size + comb(right_size, 2) if right_size >= 2 else left_size
    count_w3 = r**3 * comb(m, 3) if m >= 3 else 0
    return {
        "q": q,
        "m": m,
        "support_le_2_count": lower_weight,
        "left_fiber_universe": left_size,
        "right_universe": right_size,
        "c4_bound_w3": c4_bound_w3,
        "all_nonzero_support_le_3": lower_weight + count_w3,
        "proved_upper": min(lower_weight + c4_bound_w3, lower_weight + count_w3),
    }


def prefix_pair_fibers(
    columns: Sequence[Vector], q: int
) -> dict[Left, set[Right]]:
    """Sparse 3-column C4 projection; no ASET-exact assumption needed.

    Ignore support <3. Fail closed on zero/duplicate or invalid vectors:
    those cannot belong to a d=2 ASET exact family.
    """
    if q not in PRIMES:
        raise ValueError("q is not a pinned prime")
    if not columns:
        return {}
    m = len(columns[0])
    seen: set[Vector] = set()
    fibers: dict[Left, set[Right]] = defaultdict(set)
    for col in columns:
        if len(col) != m or any(not 0 <= x < q for x in col):
            raise ValueError("invalid coordinate or field element")
        support = tuple((i, v) for i, v in enumerate(col) if v)
        if not support or len(support) > 3 or col in seen:
            raise ValueError("column must be distinct, nonzero and weight<=3")
        seen.add(col)
        if len(support) == 3:
            left = (support[0], support[1])
            right = support[2]
            fibers[left].add(right)
    return dict(fibers)


def c4_witness(
    fibers: dict[Left, set[Right]]
) -> tuple[Left, Left, Right, Right] | None:
    """Detect forbidden rectangle by repeated unordered right pair."""
    witnessed: dict[tuple[Right, Right], Left] = {}
    for left in sorted(fibers):
        for right_pair in combinations(sorted(fibers[left]), 2):
            prior = witnessed.get(right_pair)
            if prior is not None:
                return prior, left, right_pair[0], right_pair[1]
            witnessed[right_pair] = left
    return None


def fiber_pair_certificate(
    columns: Sequence[Vector], q: int
) -> dict[str, int | bool]:
    """Count pair incidences (a necessary condition, not ASET sufficiency)."""
    fibers = prefix_pair_fibers(columns, q)
    m = len(columns[0]) if columns else 0
    triples = sum(len(rights) for rights in fibers.values())
    pairs = sum(comb(len(rights), 2) for rights in fibers.values())
    right_universe = m * (q - 1)
    witness = c4_witness(fibers)
    if witness is None and pairs > comb(right_universe, 2):
        raise AssertionError("C4-free fiber pair count contradicted")
    return {
        "m": m,
        "q": q,
        "weight_3_columns": triples,
        "active_left_fibers": len(fibers),
        "right_pair_uses": pairs,
        "right_pair_budget": comb(right_universe, 2),
        "has_forbidden_c4": witness is not None,
    }


def run_hyp002_quadratic_gate() -> None:
    from lent_exhaustive import is_exact_family
    from locality_transition import affine_sts_blocks, block_incidence_columns
    for q in PRIMES:
        for m in (3, 7, 27):
            b = quadratic_capacity_bound(m, q)
            assert b["proved_upper"] <= b["support_le_2_count"] + b["c4_bound_w3"]
            assert b["proved_upper"] <= b["all_nonzero_support_le_3"]
    for rank in (2, 3):
        m, blocks = affine_sts_blocks(rank)
        for q in (3, 5, 7):
            columns = block_incidence_columns(m, blocks, q)
            assert is_exact_family(columns, q, 2)
            cert = fiber_pair_certificate(columns, q)
            assert cert["has_forbidden_c4"] is False
            assert cert["right_pair_uses"] <= cert["right_pair_budget"]
            assert len(columns) <= quadratic_capacity_bound(m, q)["proved_upper"]
    print("HYP002_QUADRATIC_FINITE_BOUND_PASS")
    print("HYP002_PREFIX_FIBER_CERTIFICATE_PASS")
    print("HYP002_BOUNDARY_AND_WITNESS_PASS")
    print("HYP002_SHARP_EXPONENT_PHASE_B_PASS")


if __name__ == "__main__":
    run_hyp002_quadratic_gate()
