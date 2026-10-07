#!/usr/bin/env python3
"""Tiny exhaustive injectivity oracle for LENT-001.

The frozen CI grid uses q=2 or q=3, so coordinate addition modulo q is field
addition.  Enumeration is deliberately small and exact.
"""

from __future__ import annotations

import json
from itertools import combinations, product
from pathlib import Path
from typing import Iterable, Sequence

from lent_exact import finite_bound_holds, hamming_ball, input_count


Vector = tuple[int, ...]


def support_size(vector: Sequence[int]) -> int:
    return sum(x != 0 for x in vector)


def sparse_nonzero_vectors(q: int, m: int, w: int) -> list[Vector]:
    return [
        tuple(vector)
        for vector in product(range(q), repeat=m)
        if any(vector) and support_size(vector) <= w
    ]


def subset_sum(columns: Sequence[Vector], indices: Iterable[int], q: int) -> Vector:
    if not columns:
        return ()
    m = len(columns[0])
    return tuple(
        sum(columns[i][j] for i in indices) % q
        for j in range(m)
    )


def collision_witness(
    columns: Sequence[Vector], q: int, d: int
) -> tuple[tuple[int, ...], tuple[int, ...], Vector] | None:
    if not columns:
        return None
    seen: dict[Vector, tuple[int, ...]] = {(0,) * len(columns[0]): ()}
    for size in range(1, min(d, len(columns)) + 1):
        for indices in combinations(range(len(columns)), size):
            state = subset_sum(columns, indices, q)
            prior = seen.get(state)
            if prior is not None:
                return prior, indices, state
            seen[state] = indices
    return None


def is_exact_family(columns: Sequence[Vector], q: int, d: int) -> bool:
    return collision_witness(columns, q, d) is None


def has_small_gf2_dependency(columns: Sequence[Vector], max_size: int) -> bool:
    """True iff a nonempty subset of <= max_size binary columns sums to zero."""
    if not columns:
        return False
    zero = (0,) * len(columns[0])
    for size in range(1, min(max_size, len(columns)) + 1):
        for indices in combinations(range(len(columns)), size):
            if subset_sum(columns, indices, 2) == zero:
                return True
    return False


def enumerate_case(q: int, m: int, d: int, w: int, max_v: int) -> dict:
    if q not in (2, 3):
        raise ValueError("G0 exhaustive oracle is frozen to q=2 or q=3")
    candidates = sparse_nonzero_vectors(q, m, w)
    by_v: list[dict[str, int]] = []

    for v in range(1, max_v + 1):
        exact_families = 0
        for columns in combinations(candidates, v):
            exact = is_exact_family(columns, q, d)

            if q == 2:
                # Frozen equivalence check: exact set injectivity up to d iff
                # there is no nonempty GF(2) dependency of size <= 2d.
                dependency = has_small_gf2_dependency(columns, 2 * d)
                if exact == dependency:
                    raise AssertionError(
                        "binary injectivity/dependency equivalence failed"
                    )

            if not exact:
                continue

            exact_families += 1
            if not finite_bound_holds(v, q, m, d, w):
                raise AssertionError(
                    "counterexample to finite bound: "
                    f"q={q} m={m} d={d} w={w} V={v}"
                )

        by_v.append({"v": v, "exact_families": exact_families})

    return {
        "q": q,
        "m": m,
        "d": d,
        "w": w,
        "max_v": max_v,
        "candidate_columns": len(candidates),
        "input_count_at_max_v": input_count(max_v, d),
        "hamming_ball_bound": hamming_ball(q, m, d * w),
        "by_v": by_v,
    }


def load_protocol() -> dict:
    path = Path(__file__).with_name("lent-001") / "protocol.json"
    return json.loads(path.read_text(encoding="utf-8"))


def run_frozen_grid() -> list[dict]:
    protocol = load_protocol()
    results = [enumerate_case(**case) for case in protocol["exhaustive_cases"]]
    print(json.dumps(results, indent=2, sort_keys=True))
    print("EXHAUSTIVE_PASS")
    return results


if __name__ == "__main__":
    run_frozen_grid()
