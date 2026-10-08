#!/usr/bin/env python3
"""Exact G2A extremal search for odd-characteristic ASET.

Phase A is deliberately specialized to d=2 and tiny prime fields q in {3,5,7}.
The search is deterministic and exact: branch-and-bound prunes only when the
number of remaining candidates cannot beat the incumbent.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Sequence

from lent_exact import hamming_ball, input_count
from lent_exhaustive import (
    Vector,
    is_exact_family,
    linear_dependency_witness,
    sparse_nonzero_vectors,
)


def add_vector(a: Vector, b: Vector, q: int) -> Vector:
    return tuple((x + y) % q for x, y in zip(a, b))


def lent_upper_v(q: int, m: int, d: int, w: int) -> int:
    """Largest V not excluded by the finite Hamming-ball count."""
    capacity = hamming_ball(q, m, d * w)
    v = 0
    while input_count(v + 1, d) <= capacity:
        v += 1
    return v


def _can_add_d2(
    selected: Sequence[Vector],
    states: set[Vector],
    candidate: Vector,
    q: int,
) -> bool:
    """Exact incremental legality check for d=2.

    states contains 0, all selected singletons, and all selected pair sums.
    Adding c is legal iff c and every a+c are new states.
    """
    if candidate in states:
        return False

    for column in selected:
        if add_vector(column, candidate, q) in states:
            return False

    return True


def _states_after_add_d2(
    selected: Sequence[Vector],
    states: set[Vector],
    candidate: Vector,
    q: int,
) -> set[Vector]:
    result = set(states)
    result.add(candidate)
    for column in selected:
        result.add(add_vector(column, candidate, q))
    return result


def max_aset_d2(q: int, m: int, w: int) -> dict[str, object]:
    """Compute A_q^set(m,w,2) exactly by exhaustive branch-and-bound."""
    candidates = sparse_nonzero_vectors(q, m, w)
    zero = (0,) * m

    best: list[Vector] = []
    nodes = 0

    def search(index: int, selected: list[Vector], states: set[Vector]) -> None:
        nonlocal best, nodes
        nodes += 1

        # Safe exact upper bound: even taking every remaining candidate cannot
        # improve the incumbent.
        if len(selected) + (len(candidates) - index) <= len(best):
            return

        if len(selected) > len(best):
            best = list(selected)

        if index >= len(candidates):
            return

        candidate = candidates[index]

        if _can_add_d2(selected, states, candidate, q):
            next_states = _states_after_add_d2(
                selected,
                states,
                candidate,
                q,
            )
            selected.append(candidate)
            search(index + 1, selected, next_states)
            selected.pop()

        search(index + 1, selected, states)

    search(0, [], {zero})

    if not is_exact_family(best, q, 2):
        raise AssertionError("extremal ASET witness failed independent oracle")

    return {
        "q": q,
        "m": m,
        "d": 2,
        "w": w,
        "candidate_columns": len(candidates),
        "max_v": len(best),
        "witness": [list(column) for column in best],
        "search_nodes": nodes,
        "lent_upper_v": lent_upper_v(q, m, 2, w),
    }


def max_full_linear_d2(q: int, m: int, w: int) -> dict[str, object]:
    """Exact stronger baseline: no dependency among <=4 columns."""
    candidates = sparse_nonzero_vectors(q, m, w)

    best: list[Vector] = []
    nodes = 0

    def search(index: int, selected: list[Vector]) -> None:
        nonlocal best, nodes
        nodes += 1

        if len(selected) + (len(candidates) - index) <= len(best):
            return

        if len(selected) > len(best):
            best = list(selected)

        if index >= len(candidates):
            return

        candidate = candidates[index]
        trial = selected + [candidate]

        if linear_dependency_witness(trial, q, 4) is None:
            selected.append(candidate)
            search(index + 1, selected)
            selected.pop()

        search(index + 1, selected)

    search(0, [])

    if linear_dependency_witness(best, q, 4) is not None:
        raise AssertionError("linear-baseline witness is dependent")

    return {
        "q": q,
        "m": m,
        "d": 2,
        "w": w,
        "candidate_columns": len(candidates),
        "max_v": len(best),
        "witness": [list(column) for column in best],
        "search_nodes": nodes,
    }


def max_local_w1_d2(q: int) -> dict[str, object]:
    """Exact one-coordinate value A_q^set(1,1,2)."""
    return max_aset_d2(q, 1, 1)


def construct_w1_product_witness(q: int, m: int) -> list[Vector]:
    """Repeat an exact one-coordinate witness on disjoint coordinates."""
    local = max_local_w1_d2(q)["witness"]
    result: list[Vector] = []

    for coordinate in range(m):
        for scalar_list in local:
            scalar = scalar_list[0]
            column = [0] * m
            column[coordinate] = scalar
            result.append(tuple(column))

    if not is_exact_family(result, q, 2):
        raise AssertionError("w=1 product witness failed")

    return result


def verify_w1_formula(q: int, m: int, expected_local: int) -> dict[str, object]:
    """Verify the constructive side of A_q^set(m,1,2)=m*A_q^set(1,1,2).

    The matching upper bound is proved in the G2A proof note by coordinate
    decomposition. CI checks the exact local value and the product witness.
    """
    local = max_local_w1_d2(q)
    if local["max_v"] != expected_local:
        raise AssertionError(
            f"unexpected local w=1 maximum for q={q}: {local['max_v']}"
        )

    witness = construct_w1_product_witness(q, m)
    expected = m * expected_local
    if len(witness) != expected:
        raise AssertionError("w=1 product size mismatch")

    return {
        "q": q,
        "m": m,
        "d": 2,
        "w": 1,
        "local_max": expected_local,
        "max_v_by_proof": expected,
        "witness": [list(column) for column in witness],
        "lent_upper_v": lent_upper_v(q, m, 2, 1),
    }


def load_g2a_protocol() -> dict:
    path = Path(__file__).with_name("lent-001") / "g2a-protocol.json"
    return json.loads(path.read_text(encoding="utf-8"))


def run_g2a() -> dict[str, object]:
    protocol = load_g2a_protocol()

    exact_results: list[dict[str, object]] = []
    for case in protocol["exact_cases"]:
        aset = max_aset_d2(case["q"], case["m"], case["w"])
        linear = max_full_linear_d2(case["q"], case["m"], case["w"])

        if aset["max_v"] != case["expected_aset_max"]:
            raise AssertionError(
                f"ASET maximum mismatch for {case}: {aset['max_v']}"
            )
        if linear["max_v"] != case["expected_linear_max"]:
            raise AssertionError(
                f"linear maximum mismatch for {case}: {linear['max_v']}"
            )
        if aset["lent_upper_v"] != case["expected_lent_upper"]:
            raise AssertionError(
                f"LENT upper mismatch for {case}: {aset['lent_upper_v']}"
            )
        if linear["max_v"] > aset["max_v"]:
            raise AssertionError("stronger linear baseline exceeded ASET")

        exact_results.append({"aset": aset, "linear": linear})

    print("G2A_ASET_EXACT_PASS")
    print("G2A_LINEAR_BASELINE_PASS")

    w1_results = [
        verify_w1_formula(
            case["q"],
            case["m"],
            case["expected_local_max"],
        )
        for case in protocol["w1_cases"]
    ]
    print("G2A_W1_PASS")

    for result in exact_results:
        if not is_exact_family(
            [tuple(column) for column in result["aset"]["witness"]],
            result["aset"]["q"],
            2,
        ):
            raise AssertionError("persisted ASET witness failed")
    print("G2A_WITNESS_PASS")

    payload = {
        "exact_results": exact_results,
        "w1_results": w1_results,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    print("G2A_PHASE_A_PASS")
    return payload


if __name__ == "__main__":
    run_g2a()
