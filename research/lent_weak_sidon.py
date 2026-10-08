#!/usr/bin/env python3
"""G2B-B: rigorous weak-Sidon upper bound for prime-field d=2 ASET.

The bound is a known classical weak-Sidon result (Roth & Seroussi 1996,
Lemma 5); it is NOT novel and does not exploit sparse support w.

Distinct pairs from S={0} union the ASET columns have distinct sums.
For odd-order abelian G, |S|(|S|-3)+1 <= |G|, hence |columns| <= s-1,
where s is the largest integer satisfying that inequality.

All arithmetic is integer exact. The checker is independent of the
G2B forbidden-hypergraph builder/search.
"""
from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import comb, isqrt

from lent_exhaustive import Vector, is_exact_family


def weak_sidon_max_size(odd_group_order: int) -> int:
    """Best integer s allowed by s*(s-3)+1 <= |G|.

    Lemma holds for odd-order finite abelian groups. For degenerate s<=2
    the inequality is loose but still a sound upper bound. Never use
    for groups of even order here.
    """
    if (type(odd_group_order) is not int or odd_group_order < 3
            or odd_group_order % 2 == 0):
        raise ValueError("odd_group_order must be an odd integer >=3")
    estimate = (3 + isqrt(4 * odd_group_order + 5)) // 2
    if estimate * (estimate - 3) + 1 > odd_group_order:
        raise AssertionError("integer bound unexpectedly rounded upward")
    if (estimate + 1) * (estimate - 2) + 1 <= odd_group_order:
        raise AssertionError("integer bound unexpectedly rounded downward")
    return estimate


def weak_sidon_upper_v(q: int, m: int) -> int:
    """A_q^set(m,w,2) <= bound for every support w, odd prime q."""
    if type(q) is not int or q not in (3, 5, 7, 11):
        raise ValueError("only pinned odd prime fields 3,5,7,11")
    if type(m) is not int or m < 1:
        raise ValueError("m must be >=1")
    return max(0, weak_sidon_max_size(q ** m) - 1)


def is_weak_sidon_with_zero(columns: list[Vector], q: int) -> bool:
    """Independent exact finite pair-sum test for {0} union columns."""
    if q not in (3, 5, 7, 11):
        raise ValueError("q must be a pinned odd prime")
    if not columns:
        return True
    m = len(columns[0])
    if (m < 1 or any(len(x) != m for x in columns)
            or any(any(type(v) is not int or not 0 <= v < q for v in x)
                   for x in columns)):
        raise ValueError("non-field coordinate")
    s = [(0,) * m, *columns]
    if len(set(s)) != len(s):
        return False
    seen: set[Vector] = set()
    for a, b in combinations(s, 2):
        total = tuple((x + y) % q for x, y in zip(a, b))
        if total in seen:
            return False
        seen.add(total)
    return True


def difference_multiplicities(points: list[Vector], q: int) -> Counter[Vector]:
    """Full independent ordered-difference multiset, q prime."""
    if not points:
        return Counter()
    m = len(points[0])
    if any(len(x) != m for x in points):
        raise ValueError("mixed dimensions")
    return Counter(
        tuple((x - y) % q for x, y in zip(a, b))
        for a in points for b in points if a != b
    )


def weak_sidon_difference_certificate(
    columns: list[Vector], q: int
) -> dict[str, int | bool]:
    """Verify known lemma's double-representation accounting on input.

    This is an arithmetic witness check, not a universal theorem proof:
    for every weak-Sidon S of odd group order, at most |S| 3-term
    arithmetic progressions have a designated middle, hence at most
    2|S| duplicate ordered-difference representation pairs.
    """
    if not is_weak_sidon_with_zero(columns, q):
        raise ValueError("columns+zero do not form weak Sidon set")
    m = len(columns[0]) if columns else 1
    points = [(0,) * m, *columns]
    n = q ** m
    s = len(points)
    frequencies = difference_multiplicities(points, q)
    duplicate_excess = sum(count - 1 for count in frequencies.values())
    colliding_pair_count = sum(comb(count, 2) for count in frequencies.values())
    # A midpoint c determines the unordered two distinct endpoints
    # a,b (if present) by a+b=2c; weakness ensures uniqueness.
    centered_progressions = 0
    for center in points:
        endpoint_pairs = [
            (a, b) for a, b in combinations(points, 2)
            if a != center and b != center
            and all((x + y - 2 * z) % q == 0
                    for x, y, z in zip(a, b, center))
        ]
        if len(endpoint_pairs) > 1:
            raise AssertionError("weak Sidon midpoint uniqueness failed")
        centered_progressions += len(endpoint_pairs)
    if colliding_pair_count > 2 * centered_progressions:
        raise AssertionError("difference collisions cannot exceed twice AP")
    if duplicate_excess > colliding_pair_count:
        raise AssertionError("duplicate excess counting invariant")
    if s * (s - 1) != sum(frequencies.values()):
        raise AssertionError("ordered difference count")
    if s * (s - 1) > n - 1 + 2 * s:
        raise AssertionError("known group-order lemma contradicted")
    return {
        "q": q, "m": m, "group_size": n,
        "weak_sidon_points": s,
        "aset_columns": len(columns),
        "represented_nonzero_differences": len(frequencies),
        "ordered_differences": s * (s - 1),
        "duplicate_excess": duplicate_excess,
        "colliding_difference_pairs": colliding_pair_count,
        "centered_progressions": centered_progressions,
        "two_s_ap_budget": 2 * s,
        "weak_sidon_bound_v": weak_sidon_upper_v(q, m),
        "is_exact_aset": is_exact_family(columns, q, 2),
    }


def run_g2bb_sidon_gate() -> None:
    # Frozen original G2B-A independently tested 10-column witness.
    witness = [
        (0, 1, 1), (0, 1, 2), (0, 1, 3), (0, 3, 1),
        (1, 0, 2), (1, 3, 0), (2, 0, 4), (2, 4, 0),
        (3, 0, 0), (4, 0, 0),
    ]
    report = weak_sidon_difference_certificate(witness, 5)
    if not report["is_exact_aset"]:
        raise AssertionError("G2B-A witness regressed")
    if not (len(witness) == 10 and weak_sidon_upper_v(5, 3) == 11):
        raise AssertionError("GF5 target 10<=A<=11 is not established")
    if not (12 * 9 + 1 <= 125 < 13 * 10 + 1):
        raise AssertionError("GF5 weak-Sidon integer threshold")
    print("G2BB_WEAK_SIDON_MAPPING_PASS")
    print("G2BB_ODD_GROUP_BOUND_PASS")
    print("G2BB_GF5_INTERVAL_10_11_PASS")
    print("G2BB_INDEPENDENT_WITNESS_PASS")
    print("G2BB_SIDON_PHASE_A_PASS")
    print("G2BB_DIFFERENCE_CERTIFICATE", report)


if __name__ == "__main__":
    run_g2bb_sidon_gate()
