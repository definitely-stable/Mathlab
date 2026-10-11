"""C24-B1: exact triple-collision correction under one coherent global right g.

All-h identity; finite W(3,2) H=45 witness and abstract Pasch limitation.
"""
from collections import Counter
from itertools import combinations, combinations_with_replacement, product
from hyp105_g5e2b3e1c24_right_c_certificate import (
    K6_PAIRS, original_W32, degree_two_on_six_coordinates,
    checked_global_right_map, right_C_pair_weights,
)

W32_LEFT_H45 = (13, 4, 2, 14, 0, 11, 1, 7, 10, 6, 9, 5, 12, 3, 8)
W32_RIGHT_H45_ZERO = (12, 10, 5, 2, 8, 14, 1, 7, 0, 6, 3, 13, 9, 4, 11)
PASCH_A = ((0, 1, 2), (0, 3, 4), (1, 3, 5), (2, 4, 5))
PASCH_B = ((0, 1, 3), (0, 2, 4), (1, 2, 5), (3, 4, 5))
PASCH_EDGES_K6 = (5, 7, 3, 11, 12, 0)


def right_C_source_with_left_f(perm):
    """Enumerate three ORIGINAL GQ lines, two DISTINCT incidences each."""
    if (len(perm) != 15 or any(type(x) is not int for x in perm)
            or set(perm) != set(range(15))):
        raise ValueError("one complete ORIGINAL left K6 bijection required")
    _, lines, _ = original_W32()
    occupied = tuple(K6_PAIRS[i] for i in perm)
    triples = Counter()
    for ids in combinations(range(15), 3):
        for picked in product(*(combinations(lines[j], 2) for j in ids)):
            if degree_two_on_six_coordinates(occupied[p - 1]
                                             for group in picked for p in group):
                triples[ids] += 1
    return triples


def independent_left_first_source(perm):
    """Physical edge 2factors -> distinct ORIGINAL point incidences.

    Independent of right-first compiler: all 62,370 genuine sixsets checked.
    """
    if (len(perm) != 15 or any(type(x) is not int for x in perm)
            or set(perm) != set(range(15))):
        raise ValueError("complete original left permutation required")
    _, lines, _ = original_W32()
    inverse = {edge: idx + 1 for idx, edge in enumerate(perm)}
    originals = {p: tuple(j for j, line in enumerate(lines) if p in line)
                 for p in range(1, 16)}
    counts = Counter()
    all_left = 0
    for physical_ids in combinations_with_replacement(range(15), 6):
        if not degree_two_on_six_coordinates(K6_PAIRS[e] for e in physical_ids):
            continue
        multiplicities = Counter(physical_ids)
        original_ids = sorted((inverse[e], n) for e, n in multiplicities.items())
        picks = [tuple(combinations(originals[p], n)) for p, n in original_ids]
        for pick in product(*picks):
            all_left += 1
            original_right = Counter(l for group in pick for l in group)
            if tuple(sorted(original_right.values())) == (2, 2, 2):
                counts[tuple(sorted(original_right))] += 1
    return all_left, counts


def exact_collision_decomposition(triples, right_perm, physical_edges):
    """Exact inclusion-exclusion from 0/1/2/3 pair conflicts in each triple."""
    assigned = checked_global_right_map(right_perm, physical_edges)
    V = len(assigned)
    H = first = correction_two = correction_three = accepted = 0
    histogram = Counter()
    for tri, mult in triples.items():
        if (len(tri) != 3 or len(set(tri)) != 3 or
            any(type(i) is not int or not 0 <= i < V for i in tri) or
            type(mult) is not int or mult <= 0):
            raise ValueError("invalid original right triple source")
        H += mult
        k = sum(bool(set(assigned[i]) & set(assigned[j]))
                for i, j in combinations(tri, 2))
        first += mult * k
        histogram[k] += mult
        if k == 0:
            accepted += mult
        elif k == 2:
            correction_two += mult
        elif k == 3:
            correction_three += 2 * mult
    correction = correction_two + correction_three
    if H - first + correction != accepted:
        raise AssertionError("exact inclusion-exclusion identity failed")
    return {"H_C": H, "first_order_star_conflicts": first,
            "two_conflict_correction": correction_two,
            "three_conflict_correction": correction_three,
            "total_correction": correction,
            "accepted_right_C": accepted,
            "conflict_multiplicity_histogram": dict(sorted(histogram.items()))}


def pasch_pair_tensor_limitation():
    """Two different three-uniform families with IDENTICAL pair tensors."""
    A = {t: 1 for t in PASCH_A}
    B = {t: 1 for t in PASCH_B}
    if right_C_pair_weights(A, 6) != right_C_pair_weights(B, 6):
        raise AssertionError("Pasch pair-count trade invalid")
    occupied = tuple(K6_PAIRS[i] for i in PASCH_EDGES_K6)
    a = exact_collision_decomposition(A, range(6), occupied)
    b = exact_collision_decomposition(B, range(6), occupied)
    if ((a["accepted_right_C"], b["accepted_right_C"]) != (0, 1)
            or a["first_order_star_conflicts"] != b["first_order_star_conflicts"]):
        raise AssertionError("Pasch third-order witness lost")
    return {"same_pair_tensor": True,
            "Pasch_A_accepted": a["accepted_right_C"],
            "Pasch_B_accepted": b["accepted_right_C"],
            "shared_first_order_conflict": a["first_order_star_conflicts"],
            "different_triple_corrections": (a["total_correction"],
                                             b["total_correction"]),
            "abstract_trade_not_GQ_all_h_counterexample": True}


def original_W32_B1_report():
    f, g = W32_LEFT_H45, W32_RIGHT_H45_ZERO
    triples = right_C_source_with_left_f(f)
    total, oracle = independent_left_first_source(f)
    if triples != oracle or total != 62370:
        raise AssertionError("independent original source enumeration mismatch")
    if (sum(triples.values()), len(triples)) != (45, 40):
        raise AssertionError("H45 exact original witness lost")
    W = right_C_pair_weights(triples, 15)
    collision = exact_collision_decomposition(triples, g, K6_PAIRS)
    if collision["accepted_right_C"] != 0:
        raise AssertionError("right-C global zero witness invalid")
    return {"original_s": 2, "true_original_incidence_host": 45,
            "left_sixsets": total,
            "left_global_permutation": f, "right_global_permutation": g,
            "right_C_original_source_H": sum(triples.values()),
            "nonzero_original_right_triples": len(triples),
            "pair_weight_sum": sum(sum(row) for row in W) // 2,
            "pair_weight_max": max(max(row) for row in W),
            "exact_collision_identity": collision,
            "pasch_pair_only_no_go": pasch_pair_tensor_limitation(),
            "no_total_seven_or_asymptotic_counterexample": True}


if __name__ == "__main__":
    import json
    print(json.dumps(original_W32_B1_report(), indent=2, sort_keys=True))
