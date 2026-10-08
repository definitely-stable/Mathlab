#!/usr/bin/env python3
"""HYP-001/002: constructive lower-bound witnesses; falsification-first.

No numerical search here establishes a general theorem or scientific novelty.
GF(q) in verification refers exclusively to *prime* q.
"""
from __future__ import annotations

import json
from itertools import combinations, product

from lent_exhaustive import is_exact_family

Vector = tuple[int, ...]
Block = tuple[int, ...]


def block_incidence_columns(
    coordinate_count: int, blocks: list[Block], field_prime: int
) -> list[Vector]:
    if field_prime not in (2, 3, 5, 7):
        raise ValueError("prime field must be 2, 3, 5 or 7")
    if coordinate_count <= 0:
        raise ValueError("coordinate_count must be positive")
    if len(set(blocks)) != len(blocks):
        raise ValueError("blocks must be distinct")
    result: list[Vector] = []
    for block in blocks:
        if not block or tuple(sorted(set(block))) != block:
            raise ValueError("blocks must be sorted, nonempty, with distinct positions")
        if block[0] < 0 or block[-1] >= coordinate_count:
            raise ValueError("block coordinate out of range")
        vector = [0] * coordinate_count
        for point in block:
            vector[point] = 1
        result.append(tuple(vector))
    return result


def projective_plane_points(prime: int) -> tuple[Vector, ...]:
    """Canonical nonzero projective triples over prime F_p."""
    if prime not in (2, 3, 5, 7):
        raise ValueError("prime must be 2, 3, 5 or 7")
    normalized: set[Vector] = set()
    for v in product(range(prime), repeat=3):
        if v == (0, 0, 0):
            continue
        first = next(x for x in v if x)
        inv = pow(first, -1, prime)
        normalized.add(tuple((x * inv) % prime for x in v))
    return tuple(sorted(normalized))


def projective_incidence_blocks(prime: int) -> tuple[int, list[Block]]:
    """Bipartite point-line incidence for PG(2,prime), each edge a pair."""
    points = projective_plane_points(prime)
    n = len(points)
    blocks = [
        (i, n + j)
        for i, point in enumerate(points)
        for j, line in enumerate(points)
        if sum(x * y for x, y in zip(point, line)) % prime == 0
    ]
    assert n == prime * prime + prime + 1
    assert len(blocks) == n * (prime + 1)
    return 2 * n, blocks


def is_c4_free_bipartite(blocks: list[Block], left_size: int) -> bool:
    """Detect any pair of left points having two common right neighbors."""
    neighbors: dict[int, set[int]] = {}
    for a, b in blocks:
        if not (0 <= a < left_size <= b):
            raise ValueError("expected bipartite edges ordered left/right")
        neighbors.setdefault(a, set()).add(b)
    seen: set[tuple[int, int]] = set()
    for rights in neighbors.values():
        for right_pair in combinations(sorted(rights), 2):
            if right_pair in seen:
                return False
            seen.add(right_pair)
    return True


def affine_sts_blocks(rank: int) -> tuple[int, list[Block]]:
    """Lines in F_3^rank: distinct x,y,z with x+y+z=0 mod 3."""
    if not 1 <= rank <= 4:
        raise ValueError("rank must be between 1 and 4")
    points = tuple(product(range(3), repeat=rank))
    index = {point: i for i, point in enumerate(points)}
    blocks: list[Block] = []
    for i, j in combinations(range(len(points)), 2):
        z = tuple((-a - b) % 3 for a, b in zip(points[i], points[j]))
        k = index[z]
        if k <= j:
            continue
        blocks.append((i, j, k))
    m = len(points)
    assert len(blocks) == m * (m - 1) // 6
    return m, blocks


def fano_sts_blocks() -> tuple[int, list[Block]]:
    """One explicit STS(7), using cyclic translates of the (0,1,3) difference set."""
    return 7, sorted(
        tuple(sorted(((i + v) % 7 for v in (0, 1, 3))))
        for i in range(7)
    )


def is_linear_three_uniform(blocks: list[Block]) -> bool:
    """Every block has three points and every pair occurs in <=1 block."""
    seen_pairs: set[tuple[int, int]] = set()
    for block in blocks:
        if len(block) != 3 or tuple(sorted(set(block))) != block:
            return False
        for pair in combinations(block, 2):
            if pair in seen_pairs:
                return False
            seen_pairs.add(pair)
    return True


def verify_construction(
    m: int, blocks: list[Block], q: int, support: int
) -> dict[str, int | bool]:
    if any(len(block) != support for block in blocks):
        raise ValueError("incorrect support")
    columns = block_incidence_columns(m, blocks, q)
    return {
        "q": q,
        "m": m,
        "w": support,
        "d": 2,
        "V": len(blocks),
        "aset_exact": is_exact_family(columns, q, 2),
    }


def run_hypothesis_construction_evidence() -> None:
    # The graph is C4-free. Every two-edge sum is identifiable in odd
    # characteristic, including the overlapping/disjoint distinction.
    pair_cases = []
    for order in (2, 3):
        m, edges = projective_incidence_blocks(order)
        assert is_c4_free_bipartite(edges, m // 2)
        for q in (3, 5, 7):
            case = verify_construction(m, edges, q, support=2)
            assert case["aset_exact"]
            pair_cases.append(case)

    triple_cases = []
    for factory in (fano_sts_blocks, lambda: affine_sts_blocks(2)):
        m, triples = factory()
        assert is_linear_three_uniform(triples)
        for q in (3, 5, 7):
            case = verify_construction(m, triples, q, support=3)
            assert case["aset_exact"]
            triple_cases.append(case)

    # Two different pairs of blocks of a linear hypergraph are identifiable
    # over odd q; characteristic 2 is deliberately outside the theorem.
    pasch = [(0, 1, 2), (0, 3, 4), (1, 3, 5), (2, 4, 5)]
    assert is_linear_three_uniform(pasch)
    assert not verify_construction(6, pasch, 2, support=3)["aset_exact"]
    assert verify_construction(6, pasch, 3, support=3)["aset_exact"]

    c4 = [(0, 2), (0, 3), (1, 2), (1, 3)]
    assert not is_c4_free_bipartite(c4, 2)
    assert not verify_construction(4, c4, 3, support=2)["aset_exact"]

    print("HYP001_PROJECTIVE_CONSTRUCTION_PASS")
    print("HYP002_STEINER_CONSTRUCTION_PASS")
    print("HYP_ODD_CHARACTERISTIC_BOUNDARY_PASS")
    print("HYP_FALSIFICATION_CASES_PASS")
    print("HYP_LOCALITY_PHASE_A_PASS")
    print(json.dumps(
        {"HYP001": pair_cases, "HYP002": triple_cases},
        indent=2, sort_keys=True,
    ))


if __name__ == "__main__":
    run_hypothesis_construction_evidence()
