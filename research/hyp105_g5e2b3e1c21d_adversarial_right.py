"""C21-D: EXACT real W(3,2) one-global-right D6 zero witness.

FINITE restricted obstruction only: one COMPLETE original W32 left f and
one COMPLETE original W32 right g attain D6(f,g)=0 although C21's
one-common-uniform-right D6 mean is positive. The seven-class sum for this
SAME fixed (f,g) is 146 > 0: NOT a seven-family counterexample and NOT
an all-h family. Every counted witness is six DISTINCT original incidence
IDs of the TRUE 45-edge classical symplectic W(3,2), not an abstract trade.

Two independent routes:
(1) Direct enumerate 60 physical left C6 * 3^6 true incidences, count
    strict equal-position physical right dual cycles with bit-intersections.
(2) Complete historical left-2factor source and seven-family classifier,
    including non-D6 accepted B/A, A/B, C/A, C/B and B/B classes.

The global right permutation below was found via deterministic bounded
permutation search. Its correctness is certified exhaustively by the two
independent oracles, not by trusting a heuristic search, external solver,
or assumption that a random mean bounds a minimum.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb

from hyp105_g5e2b3e1c20_global_left_c6 import canonical_simple_six_cycles

# Original right line ID -> index in ordered K6 PAIRS.
W32_LEX_RIGHT_ZERO_D6 = (
    4, 13, 2, 9, 14, 3, 6, 0, 8, 1, 11, 5, 7, 12, 10
)
W32_SEVEN_EXPECTED = {
    "D6": 0,
    "B-left/A-right": 60,
    "A-left/B-right": 66,
    "C/A": 5,
    "C/B": 0,
    "B/B-overlap": 9,
    "B/B-disjoint": 6,
}
W32_EXPECTED_GF5_NECESSARY_NUMERATOR = 6698010


def genuine_global_W32_model(right_permutation=W32_LEX_RIGHT_ZERO_D6):
    """ONE complete legal left/right ORIGINAL physical pair injection."""
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    from hyp105_g5e2b3e1a_fixed_leading import PAIRS
    from hyp105_g5e2b3e1c14_domain_certificates import _filled_model

    p = tuple(right_permutation)
    if (len(p) != 15 or any(type(i) is not int for i in p)
            or set(p) != set(range(15))):
        raise ValueError("right permutation must be a full bijection of 15 original lines")
    baseline = pair_labeled_symplectic(1, "lex")
    m = _filled_model(baseline, dict(enumerate(range(15))),
                      dict(enumerate(p)))
    if (m["left_labels"] != tuple(PAIRS)
            or m["right_labels"] != tuple(PAIRS[i] for i in p)
            or len(m["incidences"]) != 45):
        raise AssertionError("not a true original W32 complete global map")
    return m


def direct_original_C6_D6_oracle(
        model, *, max_original_sixsets=43740):
    """Independent C20 physical C6 -> original incidences -> right D6.

    Does not call historical selected_left_six or seven_census.
    Uses ordered source physical edges and pairwise column overlaps,
    not the B0 physical_column_dual graph classifier.
    """
    from hyp105_g5e2b3e1a_fixed_leading import PAIRS, validated_small_model
    left, right, incidence, by_point = validated_small_model(model)
    if left != tuple(PAIRS):
        raise ValueError("direct C21-D oracle requires frozen original lex left map")
    if (type(max_original_sixsets) is not int
            or max_original_sixsets < 60*3**6):
        raise ValueError("exact original C6 sixset budget below exhaustive census")
    cycles = tuple(canonical_simple_six_cycles(PAIRS, 6))
    if len(cycles) != 60:
        raise AssertionError("physical K6 missing source C6")
    original_of_phys = {p:i for i,p in enumerate(left)}
    all_lifts = 0
    original_right_distinct = 0
    accepted_D6 = 0
    per_cycle_distinct = []
    for cycle in cycles:
        pts = tuple(original_of_phys[physical] for physical in cycle)
        if len(set(pts)) != 6:
            raise AssertionError("same original left point reused")
        lhs = frozenset((i, j) for i, j in combinations(range(6), 2)
                        if bool(set(cycle[i]) & set(cycle[j])))
        if len(lhs) != 6:
            raise AssertionError("physical left source not a C6")
        current_distinct = 0
        for ids in product(*(by_point[p] for p in pts)):
            all_lifts += 1
            if all_lifts > max_original_sixsets:
                raise ValueError("complete original C6 census budget exceeded")
            orig_right = tuple(incidence[i][1] for i in ids)
            if len(set(orig_right)) != 6:
                continue
            current_distinct += 1
            right_edges = tuple(right[line] for line in orig_right)
            rhs = frozenset((i,j) for i,j in combinations(range(6), 2)
                            if bool(set(right_edges[i]) & set(right_edges[j])))
            if rhs == lhs:
                accepted_D6 += 1
        per_cycle_distinct.append(current_distinct)
        original_right_distinct += current_distinct
    if all_lifts != 43740 or len(per_cycle_distinct) != 60:
        raise AssertionError("incomplete real W32 left C6 source")
    return {
        "original_incidence_universe": len(incidence),
        "global_original_left_points": len(left),
        "global_original_right_lines": len(right),
        "physical_left_C6": len(cycles),
        "true_original_left_C6_sixsets": all_lifts,
        "true_original_right_distinct_left_C6_sixsets": original_right_distinct,
        "per_physical_left_C6_right_distinct_counts": tuple(per_cycle_distinct),
        "independent_direct_strict_D6": accepted_D6,
        "not_full_seven_class_census": True,
    }



def exact_global_right_swap_neighborhood():
    """ALL 105 complete right maps at transposition distance 1 from D6 zero.

    One shared global right map per swap; source ORIGINAL f stays frozen.
    The direct method uses ONLY physical left C6 and TRUE ORIGINAL GQ
    incidence choices; no seven_census or original-to-physical symmetry.
    All 105 scores are integer exact, with no Monte Carlo sampling.
    """
    from hyp105_g5e2b3e1a_fixed_leading import PAIRS, validated_small_model

    m = genuine_global_W32_model()
    left, right, incidence, by_point = validated_small_model(m)
    physical_cycles = tuple(canonical_simple_six_cycles(PAIRS, 6))
    source = []
    pair_positions = tuple(combinations(range(6), 2))
    inverse = {e:i for i,e in enumerate(left)}
    for cycle in physical_cycles:
        pts = tuple(inverse[e] for e in cycle)
        target_pattern = tuple(bool(set(cycle[i]) & set(cycle[j]))
                               for i,j in pair_positions)
        for ids in product(*(by_point[p] for p in pts)):
            lines = tuple(incidence[i][1] for i in ids)
            if len(set(lines)) == 6:
                source.append((target_pattern, lines))
    if len(source) != 18716:
        raise AssertionError("GQ right-distinct original source lost")
    physical_bits = tuple((1<<a)|(1<<b) for a,b in PAIRS)
    baseline = W32_LEX_RIGHT_ZERO_D6
    scores = Counter()
    examples = {}
    for i,j in combinations(range(15), 2):
        global_g = list(baseline)
        global_g[i], global_g[j] = global_g[j], global_g[i]
        # One common globally swapped g: right adjacency is computed ONCE
        # for original right-line pair IDs and used across EVERY original J.
        edge_mask = tuple(physical_bits[p] for p in global_g)
        adjacency = tuple(tuple(bool(edge_mask[x] & edge_mask[y])
                                for y in range(15)) for x in range(15))
        value = 0
        for target, lines in source:
            if all(adjacency[lines[u]][lines[v]] == expected
                   for (u,v), expected in zip(pair_positions,target)):
                value += 1
        scores[value] += 1
        examples.setdefault(value, (i,j))
    if sum(scores.values()) != comb(15, 2):
        raise AssertionError("not every one-swap global right map enumerated")
    return {
        "scope": "ONE_FIXED_TRUE_ORIGINAL_W32_LEFT_AND_105_FULL_RIGHT_MAPS",
        "shared_original_right_source": len(source),
        "one_global_right_transposition_neighbors": comb(15,2),
        "D6_histogram": dict(sorted(scores.items())),
        "zero_D6_right_swap_neighbors": scores[0],
        "lexicographically_first_swap_by_D6": {
            score: list(swap) for score,swap in sorted(examples.items())},
        "not_global_right_full_15_factorial_minimum_enumeration": True,
        "not_all_h_or_all_seven_no_go": True,
    }


def genuine_W32_C21D_certificate(right_permutation=W32_LEX_RIGHT_ZERO_D6):
    """Finite unrestricted right zero witness; full seven-class fallback audit."""
    from hyp105_g5e2b3e1b0_seven_signature import (
        R3_CERTIFIED_FLOORS, seven_census)
    from hyp105_g5e2b3e1c0_weighted_overlap import (
        source_weighted_BA_hypergraph, exact_BA_overlap,
        simple_six_2factor_targets)

    m = genuine_global_W32_model(right_permutation)
    direct = direct_original_C6_D6_oracle(m)
    census = seven_census(m, independent_checks=False)
    counts = census["seven_class_motif_counts"]
    if counts["D6"] != direct["independent_direct_strict_D6"]:
        raise AssertionError("original Hamilton C6 D6 and full seven census disagree")
    expected_right_distinct = direct["true_original_right_distinct_left_C6_sixsets"]
    uniform_mean = Fraction(expected_right_distinct, 5005)
    if uniform_mean <= 0:
        raise AssertionError("C21 positive one-common random g mean lost")
    weights = source_weighted_BA_hypergraph(m)
    independent_BA = exact_BA_overlap(
        weights, m["right_labels"],
        target=simple_six_2factor_targets(6))
    if independent_BA != counts["B-left/A-right"]:
        raise AssertionError("independent weighted B/A right-overlap census disagrees")
    if sum(counts.values()) != census["S_seven"]:
        raise AssertionError("seven-family actual full map sum inconsistent")
    numerator = sum(R3_CERTIFIED_FLOORS[k] * counts[k]
                    for k in R3_CERTIFIED_FLOORS)
    if numerator != census["GF5_seven_lower_numerator"]:
        raise AssertionError("seven-class necessary full map weights inconsistent")
    # Hard expected finite oracle: the exact zero target is a CERTIFIED
    # witness for a restricted s=2 conclusion, not a fit to all-h.
    is_zero_witness = tuple(right_permutation) == W32_LEX_RIGHT_ZERO_D6
    if is_zero_witness:
        if (direct["true_original_right_distinct_left_C6_sixsets"] != 18716
                or direct["independent_direct_strict_D6"] != 0
                or counts != W32_SEVEN_EXPECTED
                or numerator != W32_EXPECTED_GF5_NECESSARY_NUMERATOR
                or census["S_seven"] != 146):
            raise AssertionError("genuine original W32 zero-D6 global right witness invalid")
    return {
        "scope": "GENUINE_W32_ONE_FULL_GLOBAL_LEFT_AND_RIGHT",
        "right_permutation_original_line_to_K6_lex_pair": list(right_permutation),
        "right_permutation_is_one_complete_global_bijection": True,
        "direct_C6_original_right_D6": direct,
        "actual_true_original_seven_family_counts": dict(counts),
        "actual_seven_total": census["S_seven"],
        "independent_weighted_B_left_A_right": independent_BA,
        "actual_GF5_seven_necessary_numerator": numerator,
        "common_random_right_D6_exact_mean_for_this_f": str(uniform_mean),
        "restricted_s2_fixed_f_min_over_all_right_g_exactly_zero":
            is_zero_witness,
        "no_all_h_counterexample_family_proved": True,
        "no_all_g_seven_S_zero_or_GF5_R3_upper": True,
    }


if __name__ == "__main__":
    import json
    print(json.dumps({
        "adversarial_global_right": genuine_W32_C21D_certificate(),
        "lex_baseline": genuine_W32_C21D_certificate(tuple(range(15))),
        "all_105_true_global_right_single_swaps":
            exact_global_right_swap_neighborhood(),
    }, sort_keys=True, indent=2))
