#!/usr/bin/env python3
"""G2B-B1 exact one-exchange neighborhood audit of frozen q5 witness.

This checks only the immediate combinatorial neighborhood of ONE known
10-column family. Even if all 12,800 possibilities fail, it does NOT
establish that an unrelated 11-column family is impossible.
"""
from __future__ import annotations

from itertools import combinations

from lent_exhaustive import is_exact_family, sparse_nonzero_vectors

FROZEN_Q5_TEN = (
    (0, 1, 1), (0, 1, 2), (0, 1, 3), (0, 3, 1),
    (1, 0, 2), (1, 3, 0), (2, 0, 4), (2, 4, 0),
    (3, 0, 0), (4, 0, 0),
)


def verify_frozen_local_exchange() -> dict[str, int | bool]:
    family = FROZEN_Q5_TEN
    universe = tuple(sparse_nonzero_vectors(5, 3, 2))
    universe_set = set(universe)
    if not set(family) <= universe_set or not is_exact_family(family, 5, 2):
        raise AssertionError("frozen 10-column q5 witness not valid")
    immediate = tuple(c for c in universe if c not in family)
    direct_checks = 0
    for new in immediate:
        direct_checks += 1
        if is_exact_family((*family, new), 5, 2):
            raise AssertionError("found 11-column extension; optimum is 11!")

    swap_checks = 0
    for removed in family:
        remaining = tuple(c for c in family if c != removed)
        candidates = tuple(c for c in universe if c not in remaining)
        for a, b in combinations(candidates, 2):
            swap_checks += 1
            if is_exact_family((*remaining, a, b), 5, 2):
                raise AssertionError("found exact 11-column witness after 1 swap")
    return {
        "universe": len(universe),
        "frozen_witness_size": len(family),
        "direct_add_checks": direct_checks,
        "one_delete_two_add_checks": swap_checks,
        "one_exchange_exhausted": True,
        "global_maximum_still_unknown": True,
    }


def run_g2bb_local_gate() -> None:
    result = verify_frozen_local_exchange()
    if not (result["direct_add_checks"] == 50
            and result["one_delete_two_add_checks"] == 12_750):
        raise AssertionError("local neighborhood coverage changed")
    print("G2BB_FROZEN_WITNESS_LOCAL_MAXIMALITY_PASS")
    print("G2BB_LOCAL_NEIGHBORHOOD_NON_GLOBAL_PASS")
    print("G2BB_LOCAL_EXCHANGE", result)


if __name__ == "__main__":
    run_g2bb_local_gate()
