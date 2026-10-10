"""HYP-105 B3.1-B2-B: complete leading (6,6) repeated-factor forests.

A: six distinct factor endpoints -> simple column-dual 2-factor.
B: one repeated endpoint -> one double edge plus a C4.
C: three repeated endpoints -> three disjoint double edges.

All are colored column-dual coordinate graphs, NOT factor incidence graphs.
Classifies the 50,700 remaining named, unsigned 3v3 signed templates
after accepted complete A/A (#214) and A/B (#218). The 11,032
subleading necessary forest types remain OPEN. No all-h fixed-map upper.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations
from math import comb
import json

from hyp105_g5e2b3b1_critical_flows import (
    SIGNS, two_factors, exact_nowherezero_signed_flow,
)
from hyp105_g5e2b3b1b_five_six_flows import exact_dual_GF5_six_flow
from hyp105_g5e2b1_energy import single_signed_trade_mitm

C_PAIRS = ((0, 1), (2, 3), (4, 5))
C_GRAPH = tuple(sorted(edge for pair in C_PAIRS for edge in (pair, pair)))
B_CHERRY = (0, 1)
ALL_MASK = (1 << 6) - 1
EXPECTED_NAMED = {
    "C/A": 21000, "C/B": 10800,
    "B/B-overlap": 10800, "B/B-disjoint": 8100,
}
# Independent small Python finite-certificate reproduction, full 51-palette:
# (orbit representatives, fixed-left named mass, exact flow sum, min, max).
EXPECTED_GF5 = {
    "C/A": (31, 700, 4243968, 4332, 8319),
    "C/B": (12, 360, 2084184, 4905, 6786),
    "B/B-overlap": (17, 240, 1287120, 5175, 5535),
    "B/B-disjoint": (21, 180, 1116160, 4501, 8310),
}


def normalize(edges):
    return tuple(sorted(tuple(sorted(edge)) for edge in edges))


def b_graphs(pair):
    """Three four-cycles on four remaining columns, plus double pair."""
    pair = tuple(sorted(pair))
    remaining = tuple(i for i in range(6) if i not in pair)
    answer = []
    for cycle in combinations(tuple(combinations(remaining, 2)), 4):
        degrees = Counter(v for edge in cycle for v in edge)
        if len(degrees) == 4 and all(degrees[v] == 2 for v in remaining):
            answer.append(normalize((pair, pair) + cycle))
    if len(answer) != 3 or len(set(answer)) != 3:
        raise AssertionError("exact C4-on-four enumeration broken")
    return tuple(sorted(answer))


B_GRAPH = b_graphs(B_CHERRY)[0]


def relabel_graph(edges, perm):
    return normalize((perm[u], perm[v]) for u, v in edges)


def relabel_sign(mask, perm):
    image = sum(1 << perm[i] for i in range(6) if mask & (1 << i))
    return image if image & 1 else ALL_MASK ^ image


@lru_cache(maxsize=2)
def automorphisms(left):
    group = tuple(p for p in permutations(range(6))
                  if relabel_graph(left, p) == left)
    expected = 48 if left == C_GRAPH else 16
    if len(group) != expected:
        raise AssertionError("parallel-edge stabilizer mismatch")
    return group


def cases(kind):
    """Fixed left graph, right graph, sign, raw multiplicity.

    Named forest and physical-C4 placement multipliers are applied only
    after orbit sums, never in the GF5 flow coefficient of a six-set.
    """
    if kind == "C/A":
        left = C_GRAPH
        rights = two_factors()
        multiplier = 30  # 15 C partitions, two color orientations
    elif kind == "C/B":
        left = C_GRAPH
        rights = tuple(graph for pair in combinations(range(6), 2)
                       if pair not in C_PAIRS for graph in b_graphs(pair))
        multiplier = 30
    elif kind.startswith("B/B-"):
        left = B_GRAPH
        intersect = kind == "B/B-overlap"
        rights = tuple(graph for pair in combinations(range(6), 2)
                       if pair != B_CHERRY
                       and (bool(set(pair) & set(B_CHERRY)) == intersect)
                       for graph in b_graphs(pair))
        multiplier = 45  # 15 left cherry pairs, three left C4s
    elif kind == "B/A-regression":
        left, rights, multiplier = B_GRAPH, two_factors(), 1
    else:
        raise ValueError("unknown leading forest type")
    return left, rights, multiplier


def signed_orbits(kind):
    left, rights, multiplier = cases(kind)
    group = automorphisms(left)
    orbit_mass = Counter()
    for right in rights:
        for signs in SIGNS:
            key = min((relabel_graph(right, p), relabel_sign(signs, p))
                      for p in group)
            orbit_mass[key] += 1
    if sum(orbit_mass.values()) != len(rights) * len(SIGNS):
        raise AssertionError("signed orbit mass not conserved")
    if kind in EXPECTED_NAMED and multiplier * sum(orbit_mass.values()) != EXPECTED_NAMED[kind]:
        raise AssertionError("expected named forest signed cases changed")
    return left, tuple(sorted(orbit_mass.items())), multiplier


def supports(left, right):
    """Convert 12 physical coordinates into six DISTINCT 2+2 supports."""
    column = [[] for _ in range(6)]
    for block, edges in enumerate((left, right)):
        if len(edges) != 6:
            raise AssertionError("six physical coordinates per color required")
        for j, (u, v) in enumerate(edges):
            if not 0 <= u < v < 6:
                raise AssertionError("bad column-dual edge")
            column[u].append(6 * block + j)
            column[v].append(6 * block + j)
    result = tuple(tuple(sorted(s)) for s in column)
    if len(set(result)) != 6 or any(len(s) != 4 or len(set(s)) != 4 for s in result):
        raise AssertionError("duplicate columns or invalid split support4")
    return result


@lru_cache(maxsize=1)
def report():
    rows = []
    numerator = 0
    named_total = 0
    for kind in EXPECTED_NAMED:
        left, orbits, multiplier = signed_orbits(kind)
        positive = zero = 0
        minimum = None
        maximum = 0
        fixed_sum = 0
        zero_examples = []
        witness = None
        for ((right, mask), mass) in orbits:
            signs = tuple(1 if mask & (1 << i) else -1 for i in range(6))
            support = supports(left, right)
            value = exact_dual_GF5_six_flow(support, signs, dimension=12)
            if not 0 <= value <= 51 ** 6:
                raise AssertionError("invalid full-palette GF5 flow")
            positive += mass if value else 0
            zero += mass if value == 0 else 0
            if value == 0 and len(zero_examples) < 3:
                zero_examples.append((right, mask, mass))
            if witness is None:
                witness = (left, right, mask, value)
            fixed_sum += mass * value
            minimum = value if minimum is None else min(minimum, value)
            maximum = max(maximum, value)
        if positive + zero != sum(mass for _, mass in orbits):
            raise AssertionError("positivity completeness failed")
        row = {
            "class": kind, "orbits": len(orbits),
            "fixed_left_signed_cases": positive + zero,
            "all_named_signed_cases": multiplier * (positive + zero),
            "positive_named_cases": multiplier * positive,
            "zero_named_cases": multiplier * zero,
            "minimum_GF5_flow": minimum, "maximum_GF5_flow": maximum,
            "sum_flow_fixed_left": fixed_sum,
            "all_named_flow_sum": multiplier * fixed_sum,
            "zero_examples": zero_examples,
            "witness": witness,
        }
        if ((row["orbits"], row["fixed_left_signed_cases"],
             row["sum_flow_fixed_left"], row["minimum_GF5_flow"],
             row["maximum_GF5_flow"]) != EXPECTED_GF5[kind]
                or row["zero_named_cases"]):
            raise AssertionError("pinned independent GF5 all-positive certificate changed")
        rows.append(row)
        named_total += row["all_named_signed_cases"]
        numerator += row["all_named_flow_sum"]
    if named_total != 50700 or numerator != 297992160:
        raise AssertionError("failed exact 50,700 leading signed GF5 certificate")
    by_kind = {row["class"]: row for row in rows}
    cb_sum = by_kind["C/B"]["sum_flow_fixed_left"]
    overlap_sum = by_kind["B/B-overlap"]["sum_flow_fixed_left"]
    disjoint_sum = by_kind["B/B-disjoint"]["sum_flow_fixed_left"]
    if cb_sum % 12 or (3 * overlap_sum) % 8 or (3 * disjoint_sum) % 6:
        raise AssertionError("per-factor-forest coefficient violates symmetry")
    # Exactly one abstract factor six-set is counted in each M-class;
    # never multiply the symbolic expected R3 identity by 15 or 30.
    per_forest = {
        "C/A": by_kind["C/A"]["sum_flow_fixed_left"],
        "C/B": cb_sum // 12,
        "B/B-overlap": 3 * overlap_sum // 8,
        "B/B-disjoint": 3 * disjoint_sum // 6,
    }
    if per_forest != {"C/A": 4243968, "C/B": 173682,
                      "B/B-overlap": 482670, "B/B-disjoint": 558080}:
        raise AssertionError("per-original-factor forest coefficients changed")
    return {
        "all_new_signed_templates_positive": True,
        "all_new_named_GF5_weight_sum": 297992160,
        "per_original_factor_forest_signed_GF5_coefficients": per_forest,
        "random_expected_class_identity": {
            "C/A": "M_CA*S_CA*(a)_6^2/[8*51^6*(K)_3*(K)_6]",
            "C/B": "M_CB*S_CB*(a)_6^2/[16*51^6*(K)_3*(K)_5]",
            "B/B": "(M_cap*S_cap+M_disj*S_disj)*(a)_6^2/"
                   "[4*51^6*(K)_5^2]",
        },
        "completed_named_cases": named_total,
        "all_leading_named_cases_including_accepted": 162700,
        "all_leading_factor_partition_shapes": 631,
        "new_flow_weighted_signed_sum": numerator,
        "by_class": rows,
        "subleading_forest_shapes_open": 11032,
        "all_h_fixed_label_R3_upper": False,
        "improved_ASET_exponent": False,
    }


def independent_checks():
    """Independent E0 inclusion-exclusion + GF5 full 51^3 MITM checks."""
    checked = []
    for kind in EXPECTED_NAMED:
        left, orbits, _ = signed_orbits(kind)
        samples = [orbits[0][0], orbits[len(orbits)//2][0], orbits[-1][0]]
        for right, mask in samples:
            ss = supports(left, right)
            signs = tuple(1 if mask & (1 << i) else -1 for i in range(6))
            dual = exact_dual_GF5_six_flow(ss, signs, dimension=12)
            flow = exact_nowherezero_signed_flow(left, right, mask)
            if dual != flow:
                raise AssertionError("independent GF5 Fourier/IE disagreement")
            checked.append((kind, dual))
        right, mask = samples[0]
        signs = tuple(1 if mask & (1 << i) else -1 for i in range(6))
        mitm = single_signed_trade_mitm(supports(left, right), signs, 12)
        if mitm["weighted_flow_count"] != checked[-3][1]:
            raise AssertionError("independent full-palette GF5 MITM disagrees")
    return {"independent_ie_cross_checks": len(checked),
            "independent_full_51_palette_mitm": len(EXPECTED_NAMED)}


def regression():
    left, orbits, _ = signed_orbits("B/A-regression")
    total = 0
    for (right, mask), mass in orbits:
        signs = tuple(1 if mask & (1 << i) else -1 for i in range(6))
        total += mass * exact_dual_GF5_six_flow(supports(left, right), signs, dimension=12)
    if total != 3902064:
        raise AssertionError("PR #218 fixed-left-cherry exact GF5 coefficient mismatch")
    return total


if __name__ == "__main__":
    print(json.dumps({"census": report(), "independent": independent_checks(),
                      "prior_cherry_regression": regression()},
                     indent=2, sort_keys=True))
