"""HYP-105 C21-A/B: GLOBAL-LEFT C6 -> right-distinct source -> random D6.

This is an all-h theorem for every ONE fixed, complete, globally compatible
left mapping f and every fixed occupied right physical pair alphabet F_R.
A SINGLE uniform random bijection g of all original right GQ lines onto
F_R is used. This is NOT a pointwise all-g lower, a GF5 R3 theorem, or
a proof of issue #230's universal Omega(s^6) seven-family minimum.

For a fixed left physical C6, each of its six distinct ORIGINAL GQ
points has Delta=s+1 ORIGINAL incident lines. For a pair of distinct GQ
points, at most ONE line can be incident to both. A union bound on the
15 possible pair collisions leaves at least Delta^6-15*Delta^4 choices
of six DISTINCT ORIGINAL right lines; Hall's theorem gives at least
one choice also when this bound is nonpositive (regular bipartite GQ).

If the six chosen original lines are distinct, the images of those six
lines under ONE uniform full bijection g form a uniformly random ordered
six-tuple of distinct occupied right physical pair edges. Each simple
physical right C6 offers precisely |Aut(C6)|=12 compatible ordered
assignments, so for a given ORIGINAL incidence sixset J with left dual
C6, P_g[J has the strictly aligned D6 class] = 12*C6(F_R)/(V)_6.

Thus E_g D6(f,g) = N_leftC6_rightDistinct(f)*12*C6(F_R)/(V)_6
                 >= L(s)*max(1,Delta^6-15Delta^4)*12*L(s)/(V)_6
                 = Omega(s^6).
This is a MEAN over one shared g, not a fixed adversarial g minimum.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, perm

from hyp105_g5e2b3e1c20_global_left_c6 import (
    all_h_global_left_c6_lower,
    canonical_simple_six_cycles,
)


def _gq_right_distinct_floor(s):
    """Per six DISTINCT original GQ points; elementary collision/Hall."""
    d = s + 1
    collision_union = d**6 - comb(6, 2)*d**4
    return max(1, collision_union)


def all_h_global_random_right_D6_transfer(s):
    """Exact rational ALL-h floor for one COMMON uniformly random g.

    The right and left occupied alphabets may differ but both have V
    physical pair edges of the same minimal K_a; L(s) is uniform in F.
    s=2 uses the regular-bipartite Hall existence bound (>=1 SDR).
    """
    left = all_h_global_left_c6_lower(s)
    v, d = left["original_GQ_points"], s + 1
    c6 = left["certified_remaining_physical_six_cycles"]
    favorable = _gq_right_distinct_floor(s)
    ordered = perm(v, 6)
    if ordered <= 0 or not (0 < 12*c6 <= ordered):
        raise AssertionError("invalid D6 six-label probability bound")
    p = Fraction(12*c6, ordered)
    source = c6*favorable
    expectation = source*p
    if expectation <= 0:
        raise AssertionError("uniform random right transfer lost positivity")
    return {
        "s": s, "V": v, "Delta": d,
        "all_h_GQ_at_most_one_common_line_per_distinct_point_pair": True,
        "left_physical_C6_uniform_floor": c6,
        "right_physical_C6_uniform_floor": c6,
        "right_distinct_original_line_lifts_per_left_C6_floor": favorable,
        "right_distinct_collision_union_bound": d**6-15*d**4,
        "hall_regular_bipartite_rescue": d**6-15*d**4 <= 0,
        "certified_leftC6_rightDistinct_original_sixsets": source,
        "one_common_uniform_random_right_D6_probability_floor": str(p),
        "one_common_uniform_random_right_D6_expectation_floor": str(expectation),
        "right_physical_C6_compatible_ordered_maps_each": 12,
        "asymptotic_uniform_mean_growth": "(16/3-o(1))*s^6",
        "not_fixed_adversarial_g_lower": True,
        "not_full_seven_class_or_GF5_R3_lower": True,
    }


def _line_sdr_dp(point_line_neighbors):
    """Independent Hall/SDR exact oracle: bitset DP, no incidence products."""
    dp = {0: 1}
    for neighbors in point_line_neighbors:
        nxt = {}
        for mask, count in dp.items():
            for line in neighbors:
                bit = 1 << line
                if not mask & bit:
                    key = mask | bit
                    nxt[key] = nxt.get(key, 0) + count
        dp = nxt
    return sum(dp.values())


def _cycle_dual(cycle):
    """Unlabeled cycle on six ORIGINAL incidence column positions."""
    if len(cycle) != 6:
        raise ValueError("six physical edges required")
    result = frozenset((i, j) for i, j in combinations(range(6), 2)
                       if set(cycle[i]) & set(cycle[j]))
    if len(result) != 6 or any(
        sum(i in e for e in result) != 2 for i in range(6)
    ):
        raise ValueError("expected a simple physical C6")
    return result


def exact_K6_D6_compatible_right_orderings():
    """Independent physical isomorphism count, never assume factor 12."""
    from hyp105_g5e2b3e1a_fixed_leading import PAIRS
    cycles = tuple(canonical_simple_six_cycles(PAIRS, 6))
    if len(cycles) != 60:
        raise AssertionError("K6 C6 source missing")
    left_dual = _cycle_dual(cycles[0])
    matches = 0
    for target in cycles:
        for ordered in permutations(target):
            matches += int(_cycle_dual(ordered) == left_dual)
    if matches != 12*len(cycles):
        raise AssertionError("D6 automorphism multiplicity is not 12")
    return {"right_C6": len(cycles),
            "compatible_ordered_right_edge_six_tuples": matches,
            "ordered_right_edge_tuples": perm(15, 6),
            "right_D6_probability_exact": str(Fraction(matches, perm(15, 6)))}


def genuine_W32_C21_report(*, max_sixset_evaluations=200000):
    """Four genuine global left maps, ONE actual global right map in each.

    Independent SDR DP and incidence-product enumeration must agree for
    EVERY left physical C6, not just their grand totals. Actual fixed-g
    D6 acceptance is checked with historical seven-class classifier.
    """
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    from hyp105_g5e2b3e1a_fixed_leading import PAIRS
    from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
    from hyp105_g5e2b3e1c14_domain_certificates import _filled_model

    if type(max_sixset_evaluations) is not int or max_sixset_evaluations < 1:
        raise ValueError("invalid exact original sixset evaluation cap")
    cycles = tuple(canonical_simple_six_cycles(PAIRS, 6))
    # Four genuine complete global left injections; 60*3^6 per model.
    required = 4*len(cycles)*3**6
    if required > max_sixset_evaluations:
        raise ValueError("exact C21 original incidence census cap exceeded")
    cases = []
    for scheme in ("lex", "reverse-line"):
        baseline = pair_labeled_symplectic(1, scheme)
        for relabel in ("original", "swap-original-0-13"):
            if relabel == "original":
                m = baseline
            else:
                original = tuple(PAIRS.index(e) for e in baseline["left_labels"])
                changed = dict(enumerate(original))
                changed[0], changed[13] = changed[13], changed[0]
                m = _filled_model(baseline, changed, {})
            incidence = tuple(m["incidences"])
            if len(incidence) != 45:
                raise AssertionError("not genuine W(3,2) 45-incidence host")
            inverse = {e: i for i, e in enumerate(m["left_labels"])}
            if len(inverse) != 15:
                raise AssertionError("global original left mapping not bijective")
            by_point = [[] for _ in range(15)]
            line_neighbors = [set() for _ in range(15)]
            for eid, (p, line) in enumerate(incidence):
                by_point[p].append(eid)
                line_neighbors[p].add(line)
            if any(len(x) != 3 for x in by_point):
                raise AssertionError("true GQ point has wrong degree")
            distinct_right_total = 0
            observed_fixed_g_D6 = 0
            all_lifts = 0
            classes = Counter()
            cycle_sdr_hist = Counter()
            for physical_cycle in cycles:
                points = tuple(inverse[e] for e in physical_cycle)
                if len(set(points)) != 6:
                    raise AssertionError("physical cycle reuses original point")
                neighbors = tuple(tuple(sorted(line_neighbors[p])) for p in points)
                dp_distinct = _line_sdr_dp(neighbors)
                enumeration_distinct = 0
                for choices in product(*(by_point[p] for p in points)):
                    ids = tuple(sorted(choices))
                    lines = [incidence[i][1] for i in ids]
                    all_lifts += 1
                    if len(set(lines)) != 6:
                        continue
                    enumeration_distinct += 1
                    tag = classify_seven_prechecked(
                        ids, m["left_labels"], m["right_labels"], incidence)
                    if tag not in (None, "D6"):
                        raise AssertionError("six distinct right lines cannot be B/C")
                    if tag == "D6":
                        observed_fixed_g_D6 += 1
                        classes[tag] += 1
                if enumeration_distinct != dp_distinct or dp_distinct < 1:
                    raise AssertionError("independent genuine GQ SDR or Hall gate false")
                distinct_right_total += dp_distinct
                cycle_sdr_hist[dp_distinct] += 1
            if all_lifts != 43740 or sum(cycle_sdr_hist.values()) != 60:
                raise AssertionError("C20 left Hamilton lift census lost")
            expected = Fraction(distinct_right_total, 5005)
            cases.append({
                "scheme": scheme,
                "global_original_left_relabel": relabel,
                "true_original_left_C6_sixsets": all_lifts,
                "right_distinct_original_line_sixsets": distinct_right_total,
                "per_left_cycle_SDR_histogram": dict(sorted(cycle_sdr_hist.items())),
                "independently_verified_SDR_dynamic_program": True,
                "true_actual_one_fixed_global_right_D6": observed_fixed_g_D6,
                "one_shared_uniform_random_global_right_D6_exact_mean": str(expected),
                "finite_adversarial_minimum_not_proved": True,
            })
    return {
        "scope": "TRUE_ORIGINAL_W32_GLOBAL_LEFT_C6_AND_GLOBAL_RIGHT_D6",
        "independent_physical_D6_orderings": exact_K6_D6_compatible_right_orderings(),
        "all_h_s2_necessary_mean_floor": all_h_global_random_right_D6_transfer(2),
        "four_true_global_original_GQ_left_mappings": cases,
        "not_an_all_g_minimum": True,
    }


if __name__ == "__main__":
    import json
    print(json.dumps({
        "all_h": [all_h_global_random_right_D6_transfer(s)
                  for s in (2, 4, 8, 16, 32, 64, 128)],
        "W32": genuine_W32_C21_report(),
    }, indent=2, sort_keys=True))
