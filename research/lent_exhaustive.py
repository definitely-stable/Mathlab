#!/usr/bin/env python3
"""Exact finite oracles for the LENT-001 / ASET research family.

G0 keeps its original q={2,3} frozen grid. G1A adds independent checks for:
- exact subset-sum injectivity (ASET);
- bounded signed {-1,0,1} relations with separate side bounds;
- arbitrary-coefficient small-column linear dependence.

All G1A arithmetic is deliberately restricted to prime fields q in {2,3,5}.
The implementation is brute-force by design and only targets tiny evidence grids.
"""

from __future__ import annotations

import json
from itertools import combinations, product
from pathlib import Path
from typing import Iterable, Sequence

from lent_exact import finite_bound_holds, hamming_ball, input_count


Vector = tuple[int, ...]
SignedRelationWitness = tuple[tuple[int, ...], tuple[int, ...]]
LinearDependencyWitness = tuple[tuple[int, ...], tuple[int, ...]]
G1A_PRIMES = (2, 3, 5)
PRIME_ORACLE_FIELDS = (2, 3, 5, 7)


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


def linear_combination(
    columns: Sequence[Vector],
    indices: Sequence[int],
    coefficients: Sequence[int],
    q: int,
) -> Vector:
    if len(indices) != len(coefficients):
        raise ValueError("indices and coefficients must have the same length")
    if not columns:
        return ()
    m = len(columns[0])
    return tuple(
        sum(
            coefficient * columns[index][coordinate]
            for index, coefficient in zip(indices, coefficients)
        )
        % q
        for coordinate in range(m)
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


def signed_relation_witness(
    columns: Sequence[Vector], q: int, d: int
) -> SignedRelationWitness | None:
    """Find a nonzero signed relation with <=d positive and <=d negative terms.

    This implementation is intentionally independent from collision_witness.
    Positive and negative supports are disjoint, matching the relation obtained
    after cancelling the intersection of two colliding sets.
    """
    if not columns or d <= 0:
        return None

    m = len(columns[0])
    zero = (0,) * m
    universe = tuple(range(len(columns)))
    max_positive = min(d, len(columns))

    for positive_size in range(max_positive + 1):
        for positive in combinations(universe, positive_size):
            positive_set = set(positive)
            remaining = tuple(index for index in universe if index not in positive_set)
            max_negative = min(d, len(remaining))

            for negative_size in range(max_negative + 1):
                if positive_size == 0 and negative_size == 0:
                    continue

                for negative in combinations(remaining, negative_size):
                    state = tuple(
                        (
                            sum(columns[index][coordinate] for index in positive)
                            - sum(columns[index][coordinate] for index in negative)
                        )
                        % q
                        for coordinate in range(m)
                    )
                    if state == zero:
                        return positive, negative

    return None


def linear_dependency_witness(
    columns: Sequence[Vector], q: int, max_size: int
) -> LinearDependencyWitness | None:
    """Find an arbitrary-coefficient dependency among <=max_size columns.

    G1A deliberately supports prime fields q in {2,3,5}; non-prime prime powers
    require a real finite-field representation and are outside this oracle.
    """
    if q not in G1A_PRIMES:
        raise ValueError(f"G1A linear oracle supports only q in {G1A_PRIMES}")
    if not columns or max_size <= 0:
        return None

    zero = (0,) * len(columns[0])
    for size in range(1, min(max_size, len(columns)) + 1):
        for indices in combinations(range(len(columns)), size):
            for coefficients in product(range(1, q), repeat=size):
                if linear_combination(columns, indices, coefficients, q) == zero:
                    return indices, coefficients
    return None


def has_small_gf2_dependency(columns: Sequence[Vector], max_size: int) -> bool:
    """True iff a nonempty subset of <=max_size binary columns sums to zero."""
    return linear_dependency_witness(columns, 2, max_size) is not None


def enumerate_case(q: int, m: int, d: int, w: int, max_v: int) -> dict:
    """Run the unchanged G0 exhaustive contract."""
    if q not in (2, 3):
        raise ValueError("G0 exhaustive oracle is frozen to q=2 or q=3")
    candidates = sparse_nonzero_vectors(q, m, w)
    by_v: list[dict[str, int]] = []

    for v in range(1, max_v + 1):
        exact_families = 0
        for columns in combinations(candidates, v):
            exact = is_exact_family(columns, q, d)

            if q == 2:
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


def _serialize_columns(columns: Sequence[Vector]) -> list[list[int]]:
    return [list(column) for column in columns]


def _serialize_linear_dependency(
    witness: LinearDependencyWitness,
) -> dict[str, list[int]]:
    indices, coefficients = witness
    return {
        "indices": list(indices),
        "coefficients": list(coefficients),
    }


def enumerate_g1a_case(q: int, m: int, d: int, w: int, max_v: int) -> dict:
    """Exhaustively compare ASET, signed and full-linear properties."""
    if q not in G1A_PRIMES:
        raise ValueError(f"G1A exhaustive oracle supports only q in {G1A_PRIMES}")

    candidates = sparse_nonzero_vectors(q, m, w)
    by_v: list[dict[str, object]] = []

    for v in range(1, max_v + 1):
        total_families = 0
        aset_exact_families = 0
        signed_relation_free_families = 0
        full_linear_independent_families = 0
        aset_not_full_linear_families = 0
        first_separation: dict[str, object] | None = None

        for columns in combinations(candidates, v):
            total_families += 1

            aset_exact = is_exact_family(columns, q, d)
            signed_witness = signed_relation_witness(columns, q, d)
            signed_free = signed_witness is None

            if aset_exact != signed_free:
                raise AssertionError(
                    "ASET/signed-relation equivalence failed: "
                    f"q={q} m={m} d={d} w={w} V={v} columns={columns}"
                )

            full_dependency = linear_dependency_witness(columns, q, 2 * d)
            full_linear_independent = full_dependency is None

            if full_linear_independent and not aset_exact:
                raise AssertionError(
                    "full small-column independence must imply ASET exactness"
                )

            if q == 2 and aset_exact != full_linear_independent:
                raise AssertionError(
                    "q=2 ASET/full-linear equivalence failed"
                )

            if aset_exact:
                aset_exact_families += 1
                signed_relation_free_families += 1
                if not finite_bound_holds(v, q, m, d, w):
                    raise AssertionError(
                        "counterexample to finite bound in G1A grid: "
                        f"q={q} m={m} d={d} w={w} V={v}"
                    )

            if full_linear_independent:
                full_linear_independent_families += 1

            if aset_exact and not full_linear_independent:
                aset_not_full_linear_families += 1
                if first_separation is None:
                    assert full_dependency is not None
                    first_separation = {
                        "columns": _serialize_columns(columns),
                        "dependency": _serialize_linear_dependency(full_dependency),
                    }

        by_v.append(
            {
                "v": v,
                "total_families": total_families,
                "aset_exact_families": aset_exact_families,
                "signed_relation_free_families": signed_relation_free_families,
                "full_linear_independent_families": full_linear_independent_families,
                "aset_not_full_linear_families": aset_not_full_linear_families,
                "first_aset_not_full_linear_witness": first_separation,
            }
        )

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


def load_g1a_protocol() -> dict:
    path = Path(__file__).with_name("lent-001") / "g1a-protocol.json"
    return json.loads(path.read_text(encoding="utf-8"))


def run_frozen_grid() -> list[dict]:
    protocol = load_protocol()
    results = [enumerate_case(**case) for case in protocol["exhaustive_cases"]]
    print(json.dumps(results, indent=2, sort_keys=True))
    print("EXHAUSTIVE_PASS")
    return results


def _verify_pinned_separation(q: int) -> None:
    columns: tuple[Vector, ...] = ((1,), (2,))
    d = 1

    if not is_exact_family(columns, q, d):
        raise AssertionError(f"pinned q={q} ASET family must be exact")
    if signed_relation_witness(columns, q, d) is not None:
        raise AssertionError(f"pinned q={q} family must have no legal signed relation")
    if linear_dependency_witness(columns, q, 2 * d) is None:
        raise AssertionError(f"pinned q={q} family must be linearly dependent")


def run_g1a_grid() -> list[dict]:
    protocol = load_g1a_protocol()
    results = [
        enumerate_g1a_case(**case)
        for case in protocol["oracle_cases"]
    ]

    if not any(result["q"] == 2 for result in results):
        raise AssertionError("G1A grid must include q=2 equivalence coverage")

    print(json.dumps(results, indent=2, sort_keys=True))
    print("G1A_SIGNED_EQUIV_PASS")
    print("G1A_Q2_EQUIV_PASS")

    _verify_pinned_separation(3)
    print("G1A_Q3_SEPARATION_PASS")

    _verify_pinned_separation(5)
    print("G1A_Q5_SEPARATION_PASS")

    print("G1A_ORACLE_PASS")
    return results


if __name__ == "__main__":
    run_frozen_grid()
    run_g1a_grid()
