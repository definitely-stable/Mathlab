#!/usr/bin/env python3
"""Exact finite arithmetic for LENT-001.

Standard library only.  This module intentionally contains no floating-point
entropy approximations; G0 is the finite counting layer.
"""

from __future__ import annotations

from itertools import product
from math import comb


def input_count(v: int, d: int) -> int:
    if v < 0 or d < 0:
        raise ValueError("v and d must be nonnegative")
    return sum(comb(v, i) for i in range(min(v, d) + 1))


def hamming_ball(q: int, m: int, radius: int) -> int:
    if q < 2:
        raise ValueError("q must be at least 2")
    if m < 0 or radius < 0:
        raise ValueError("m and radius must be nonnegative")
    return sum(
        comb(m, j) * (q - 1) ** j
        for j in range(min(m, radius) + 1)
    )


def direct_hamming_ball_count(q: int, m: int, radius: int) -> int:
    """Directly enumerate q-ary vectors; tiny-regression use only."""
    if q < 2:
        raise ValueError("q must be at least 2")
    if m < 0 or radius < 0:
        raise ValueError("m and radius must be nonnegative")
    count = 0
    for vector in product(range(q), repeat=m):
        if sum(x != 0 for x in vector) <= radius:
            count += 1
    return count


def finite_bound_holds(v: int, q: int, m: int, d: int, w: int) -> bool:
    """Numerical form of LENT-A for parameters known to admit an exact family."""
    if w < 0:
        raise ValueError("w must be nonnegative")
    return input_count(v, d) <= hamming_ball(q, m, d * w)


def self_check() -> None:
    # Formula-vs-direct cardinality checks.  These test the machine arithmetic,
    # not existence of a sketch family.
    for q in (2, 3):
        for m in range(0, 6):
            for radius in range(0, m + 2):
                exact = hamming_ball(q, m, radius)
                direct = direct_hamming_ball_count(q, m, radius)
                if exact != direct:
                    raise AssertionError(
                        f"Hamming-ball mismatch q={q} m={m} r={radius}: "
                        f"{exact} != {direct}"
                    )

    # Fixed regressions.
    assert input_count(5, 2) == 16
    assert input_count(3, 99) == 8
    assert hamming_ball(2, 4, 2) == 11
    assert hamming_ball(3, 2, 1) == 5
    print("EXACT_ARITHMETIC_PASS")


if __name__ == "__main__":
    self_check()
