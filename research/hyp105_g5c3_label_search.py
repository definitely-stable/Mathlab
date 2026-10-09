"""HYP-105 G5-C3-A: bounded, reproducible pair-label search, GF5 unit submodel.

Exact finite optimization over bijective K6-edge assignments to W(3,2)
vertices. Mathematical results are a gauge-symmetry lemma and finite
certificates; no m->infinity exponent, optimum or global ASET theorem.
"""
from collections import defaultdict
from itertools import combinations
from random import Random
import argparse
import json

from hyp105_g5c2_density import (
    collision_spectrum, conditional_expectation_extract, optimize_first_moment,
    validate_cleaned
)
from test_hyp105_g5b_graph_realization import (
    canonical_pair_embedding, quadrangle_w32
)

PAIRS = tuple(combinations(range(6), 2))
W32_EDGES = quadrangle_w32()[1]
LABEL_COUNT = 15
COLUMN_COUNT = len(W32_EDGES)
IDENTITY = tuple(range(LABEL_COUNT))


def check_bijection(perm):
    if len(perm) != LABEL_COUNT or set(perm) != set(IDENTITY):
        raise ValueError("expected a bijection onto the 15 K6 edge labels")


def supports_for_labels(left, right):
    """Produce fixed graph-edge-order GF5 all-one 4-support coordinate tuples."""
    check_bijection(left)
    check_bijection(right)
    edge_ids = tuple((left[i], right[j]) for i, j in W32_EDGES)
    return canonical_pair_embedding(edge_ids, 15, 15, 6, 6)


def vectors_for_labels(left, right):
    return tuple(
        tuple(int(i in support) for i in range(12))
        for support in supports_for_labels(left, right)
    )


def fast_minimal_conflicts(left, right):
    """Independent base-five digit encoding of <=3 column sums.

    The GF5 field sums equal integer sums because every unit column
    contributes at most one, and at most three columns are selected.
    This implementation differs from C2's direct vector-sum census.
    """
    supports = supports_for_labels(left, right)
    powers = tuple(5 ** k for k in range(12))
    encoded = tuple(sum(powers[c] for c in col) for col in supports)
    pair_buckets = defaultdict(list)
    for i, j in combinations(range(COLUMN_COUNT), 2):
        pair_buckets[encoded[i] + encoded[j]].append((1 << i) | (1 << j))
    t4 = set()
    for bucket in pair_buckets.values():
        for a, b in combinations(bucket, 2):
            if a & b:
                raise AssertionError("duplicate single-column signature")
            t4.add(a | b)

    triple_buckets = defaultdict(list)
    for i, j, k in combinations(range(COLUMN_COUNT), 3):
        triple_buckets[encoded[i] + encoded[j] + encoded[k]].append(
            (1 << i) | (1 << j) | (1 << k))
    t6_all = set()
    for bucket in triple_buckets.values():
        for a, b in combinations(bucket, 2):
            if not (a & b):
                t6_all.add(a | b)
    minimal6 = {edge for edge in t6_all if not any(
        edge & four == four for four in t4)}
    return tuple(sorted(t4)), tuple(sorted(minimal6))


def trade_score(c4, c6, four_weight=16):
    """Finite heuristic objective, NOT a proven exponent proxy."""
    if four_weight <= 0:
        raise ValueError("positive four-support penalty required")
    return four_weight * len(c4) + len(c6)


def apply_swap(perm, a, b):
    if not (0 <= a < LABEL_COUNT and 0 <= b < LABEL_COUNT):
        raise ValueError("vertex indices outside 15")
    result = list(perm)
    result[a], result[b] = result[b], result[a]
    return tuple(result)


def induced_pair_relabeling(coordinate_perm):
    """Action of S6 on all 15 K6-edge labels."""
    if len(coordinate_perm) != 6 or set(coordinate_perm) != set(range(6)):
        raise ValueError("coordinate relabel must permute all six positions")
    pair_to_id = {pair: i for i, pair in enumerate(PAIRS)}
    return tuple(pair_to_id[tuple(sorted(
        (coordinate_perm[a], coordinate_perm[b]))) ] for a, b in PAIRS)


def compose_image(label_bijection, induced):
    """Map each vertex pair label through a coordinate permutation."""
    check_bijection(label_bijection)
    check_bijection(induced)
    return tuple(induced[i] for i in label_bijection)


def seeded_labels(seed):
    """Deterministic independent shuffle of both 15-edge palettes."""
    if seed is None:
        return IDENTITY, IDENTITY
    rng = Random(seed)
    l, r = list(IDENTITY), list(IDENTITY)
    rng.shuffle(l)
    rng.shuffle(r)
    return tuple(l), tuple(r)


def bounded_descent(initial_left, initial_right, *, seed, rounds=6,
                    probes_per_round=12, four_weight=16):
    """Deterministic best-improvement across sampled valid label swaps.

    All operations are finite and bounded. No claim of local optimality
    against all swaps, or optimality across all possible label permutations.
    """
    check_bijection(initial_left)
    check_bijection(initial_right)
    if rounds < 0 or probes_per_round < 0:
        raise ValueError("negative search budget")
    rng = Random(seed)
    left, right = initial_left, initial_right
    four, six = fast_minimal_conflicts(left, right)
    before = (len(four), len(six))
    initial_score = trade_score(four, six, four_weight)
    score = initial_score
    accepted = []
    evaluations = 1
    for step in range(rounds):
        seen = set()
        candidates = []
        for _ in range(probes_per_round):
            half = rng.randrange(2)
            i, j = sorted(rng.sample(range(LABEL_COUNT), 2))
            key = (half, i, j)
            if key in seen:
                continue
            seen.add(key)
            a = apply_swap(left, i, j) if half == 0 else left
            b = apply_swap(right, i, j) if half == 1 else right
            c4, c6 = fast_minimal_conflicts(a, b)
            evaluations += 1
            new_score = trade_score(c4, c6, four_weight)
            candidates.append((new_score, len(c4), len(c6), key, a, b))
        better = [row for row in candidates if row[0] < score]
        if not better:
            continue
        choice = min(better, key=lambda row: row[:4])
        score, _, _, key, left, right = choice
        accepted.append((step, key, score))
    four, six = fast_minimal_conflicts(left, right)
    if score != trade_score(four, six, four_weight):
        raise AssertionError("search score mismatch")
    return {
        "start": before, "finish": (len(four), len(six)),
        "objective_start": initial_score, "objective_finish": score,
        "left_labels": left, "right_labels": right,
        "accepted": tuple(accepted), "evaluations": evaluations,
        "four_weight": four_weight
    }


def certified_result(left, right):
    """Validate optimized finite family using INDEPENDENT C2 oracle."""
    columns = vectors_for_labels(left, right)
    direct4, direct6 = collision_spectrum(columns)
    encoded4, encoded6 = fast_minimal_conflicts(left, right)
    if (direct4, direct6) != (encoded4, encoded6):
        raise AssertionError("independent exact trade census mismatch")
    hyperedges = direct4 + direct6
    p, bound = optimize_first_moment(COLUMN_COUNT, hyperedges)
    selected, cleaned, certified, score = conditional_expectation_extract(
        COLUMN_COUNT, hyperedges, p)
    if certified != bound or score < certified:
        raise AssertionError("rational conditional expectation certificate")
    if not validate_cleaned(columns, cleaned, hyperedges):
        raise AssertionError("actual all-subset GF5 sums collided")
    return {
        "T4": len(direct4), "T6": len(direct6),
        "extracted_aset": cleaned.bit_count(),
        "grid_p": str(p), "fractional_lower": str(bound),
        "column_ids": [i for i in range(COLUMN_COUNT) if cleaned >> i & 1],
        "selected_before_clean": selected.bit_count()
    }


def report(seed=1, rounds=6, probes=12):
    l0, r0 = seeded_labels(seed)
    descent = bounded_descent(l0, r0, seed=20261009 + seed,
                              rounds=rounds, probes_per_round=probes)
    result = certified_result(descent["left_labels"],
                              descent["right_labels"])
    return {
        "model": "W(3,2)/GF5/unit-exact4/2+2 split; m=12",
        "seed": seed, "rounds": rounds, "probes_per_round": probes,
        "before": list(descent["start"]),
        "after": [result["T4"], result["T6"]],
        "before_objective": descent["objective_start"],
        "after_objective": descent["objective_finish"],
        "accepted_swap_count": len(descent["accepted"]),
        "evaluations": descent["evaluations"],
        "left_labels": list(descent["left_labels"]),
        "right_labels": list(descent["right_labels"]),
        "actual_aset_subfamily": result,
        "quantifier": "one finite m=12 instance, no uniform-in-m theorem",
        "no_exponent_improvement": True
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--rounds", type=int, default=6)
    parser.add_argument("--probes", type=int, default=12)
    args = parser.parse_args()
    print(json.dumps(report(args.seed, args.rounds, args.probes),
                     ensure_ascii=False, sort_keys=True, indent=2))
