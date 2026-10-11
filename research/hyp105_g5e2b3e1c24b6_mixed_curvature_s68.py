"""HYP-105 C24-B6: exact S68 next-sphere and all-h joint-exposure curvature bound.

The all-h lemma concerns only ORIGINAL distinct six-incidence source J with a
static left/original endpoint tag, and ONE globally complete physical-right
bijection g. The W32 numerical census fixes C24-B5's concrete f and g68.
Neither is a universal positive seven-family lower or a global 15! minimum.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb

from hyp105_g5e2b3e1c24b_three_collision import W32_LEFT_H45
from hyp105_g5e2b3e1c24b2_joint_seven import (
    TAGS, compile_left, full_left_score, full_permutation, right_first_independent)
from hyp105_g5e2b3e1c24b3_joint_swap_gradient import legal_transpose
from hyp105_g5e2b3e1c24b5_two_swap_escape import (
    ALL_SWAPS, N_RIGHT, N_DISTANCE_TWO, N_DOUBLE_TRANSPOSITIONS,
    N_THREE_CYCLES, N_SWAPS, compile_right_pullback_fibers,
    template_pullback_score, independent_disjoint_original_source_curvature,
)

# HEAD C24-B5 verified true original W32 two-disjoint-swap endpoint.
W32_RIGHT_S68 = (12, 9, 11, 4, 1, 6, 0, 13, 5, 14, 3, 7, 2, 10, 8)
W32_S68_VECTOR = (0, 44, 21, 0, 0, 2, 1)


def choose_nonnegative(n, k):
    if type(n) is not int or type(k) is not int:
        raise ValueError("combinatorial arguments must be integers")
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


def both_touch_disjoint_swap_pair_count(n, r):
    """Number of UNORDERED disjoint transposition pairs A,B touching H.

    |H|=r original right lines out of n. Inclusion-exclusion for ordered
    disjoint pairs, then /2 because the pair A,B is unordered:

    [C(n,2)C(n-2,2) - 2 C(n-r,2)C(n-2,2)
      + C(n-r,2)C(n-r-2,2)]/2.

    Exact for every 0 <= r <= n, n>=4, independent of f,g and GF5.
    """
    if (type(n) is not int or type(r) is not int or
            n < 4 or not 0 <= r <= n):
        raise ValueError("valid original right universe n>=4 and support 0<=r<=n required")
    total = choose_nonnegative(n, 2)*choose_nonnegative(n-2, 2)
    miss = choose_nonnegative(n-r, 2)*choose_nonnegative(n-2, 2)
    both_miss = (choose_nonnegative(n-r, 2)*
                 choose_nonnegative(n-r-2, 2))
    numerator = total - 2*miss + both_miss
    if numerator < 0 or numerator % 2:
        raise AssertionError("joint-exposure pair counting lost integrality")
    return numerator // 2


def exact_all_disjoint_joint_exposure(source):
    """All-h structural bound specialized to the genuine compressed W32 source.

    For disjoint right swaps A and B and a static original sixset J, the
    mixed contribution X_J(gAB)-X_J(gA)-X_J(gB)+X_J(g) is ZERO unless J
    touches both A and B, and its absolute value <=2. Thus

       |kappa_AB| <= 2 M_AB,
       SUM_{unordered disjoint A,B}|kappa_AB|
          <= 2 SUM_{distinct original J} K(n, |H(J)|),

    where M_AB is the ORIGINAL candidate-sixset count jointly touching A,B,
    K is both_touch_disjoint_swap_pair_count, and multiplicities from
    compressed original records are expanded arithmetically.
    The upper may be nonsharp; it provides NO positive S lower bound.
    """
    if source["left_source_size"] != 62370 or len(source["by_line"]) != N_RIGHT:
        raise ValueError("true original W32 fixed-left source is required")
    support_hist = Counter()
    total_j = total_pair_exposure = 0
    for tag, lines, signature, weight in source["records"]:
        if tag not in TAGS or type(weight) is not int or weight <= 0:
            raise ValueError("invalid original static candidate source")
        r = len(set(lines))
        if not 1 <= r <= 6:
            raise AssertionError("original sixset support out of range")
        support_hist[r] += weight
        total_j += weight
        total_pair_exposure += weight * both_touch_disjoint_swap_pair_count(N_RIGHT, r)
    if total_j != source["static_eligible"]:
        raise AssertionError("weighted source multiplicity mismatch")
    if total_pair_exposure < 0:
        raise AssertionError("negative true original joint exposure")
    return {
        "n_original_right": N_RIGHT,
        "original_candidate_sixsets": total_j,
        "original_right_support_histogram": dict(sorted(support_hist.items())),
        "unordered_disjoint_pairs": 3 * comb(N_RIGHT, 4),
        "sum_jointly_touched_original_sources_over_all_pairs": total_pair_exposure,
        "sum_absolute_mixed_curvature_upper": 2 * total_pair_exposure,
        "bound_proved_all_h": True,
        "does_not_imply_positive_seven_minimum": True,
    }


def exact_next_ball_from_s68():
    """All 105+5005 complete global original-right maps around genuine S68.

    Fast reference is the independently source-validated 130-template
    pullback scorer from C24-B5. Key endpoint maps are checked against the
    entire original 51k left signatures and separate 62,370 right-first
    original six-incidence census. No per-sixset independent map choices.
    """
    source = compile_left(W32_LEFT_H45)
    fibers = compile_right_pullback_fibers(source)
    start = full_permutation(W32_RIGHT_S68)
    base = template_pullback_score(fibers, start)
    if (base["S_seven"] != 68 or
            tuple(base["seven_counts"][t] for t in TAGS) != W32_S68_VECTOR or
            base["Q7_necessary_numerator"] != 3112510 or
            base["right_C_accepted"] != 0 or
            base != full_left_score(source, start)):
        raise AssertionError("C24-B5 true GQ S68 original global witness lost")

    first, first_perm = {}, {}
    for pair in ALL_SWAPS:
        target = legal_transpose(start, *pair)
        first_perm[pair] = target
        first[pair] = template_pullback_score(fibers, target)
    if len(first) != N_SWAPS:
        raise AssertionError("incomplete 105 original first swaps")
    first_min = min(ALL_SWAPS, key=lambda a: (first[a]["S_seven"], a))

    states, decomps, kind = {}, defaultdict(list), {}
    for a in ALL_SWAPS:
        after_a = first_perm[a]
        for b in ALL_SWAPS:
            if a == b:
                continue
            g = legal_transpose(after_a, *b)
            this_kind = "three_cycle" if len(set(a) & set(b)) == 1 else "disjoint"
            if g in kind and kind[g] != this_kind:
                raise AssertionError("same endpoint has conflicting cycle type")
            kind[g] = this_kind
            decomps[g].append((a, b))
            if g not in states:
                states[g] = template_pullback_score(fibers, g)

    if (len(states) != N_DISTANCE_TWO or len(kind) != N_DISTANCE_TWO or
            len([v for v in kind.values() if v == "three_cycle"]) != N_THREE_CYCLES or
            len([v for v in kind.values() if v == "disjoint"]) != N_DOUBLE_TRANSPOSITIONS or
            sum(map(len, decomps.values())) != N_SWAPS*(N_SWAPS-1)):
        raise AssertionError("radius-two quotient incomplete")
    if any(len(paths) != (3 if kind[g] == "three_cycle" else 2)
           for g, paths in decomps.items()):
        raise AssertionError("incorrect ordered double-swap path multiplicity")

    best = min(states, key=lambda g: (states[g]["S_seven"], g))
    best_score = states[best]["S_seven"]
    best_paths = decomps[best]
    pick_path = lambda p: (max(base["S_seven"], first[p[0]]["S_seven"],
                                 best_score), p)
    path = min(best_paths, key=pick_path)

    # ALL disjoint double swaps, each exactly once. Negative curvature may
    # occur without any improvement: record both quantities separately.
    # Independently group ORIGINAL candidate sixsets by their original
    # right-line SUPPORT, preserving each compressed row's true multiplicity.
    # This differs from the K(n,r) formula: it counts actual joint exposures
    # pair by pair, making an exhaustive finite falsifier of the all-h bound.
    support_multiplicity = Counter()
    for rec in source["records"]:
        mask = 0
        for line in set(rec[1]):
            mask |= 1 << line
        support_multiplicity[mask] += rec[3]
    if sum(support_multiplicity.values()) != source["static_eligible"]:
        raise AssertionError("original line support compression lost sixset multiplicities")
    support_fibers = tuple(support_multiplicity.items())
    disjoint_curvatures = Counter()
    most_negative = None
    actual_abs_sum = 0
    exact_sum_joint_exposure = 0
    smallest_pointwise_slack = None
    improves_disjoint = improves_three_cycle = 0
    for g, row in states.items():
        if row["S_seven"] < 68:
            if kind[g] == "disjoint":
                improves_disjoint += 1
            else:
                improves_three_cycle += 1
        if kind[g] != "disjoint":
            continue
        a, b = decomps[g][0]
        kappa = (row["S_seven"] - first[a]["S_seven"] -
                 first[b]["S_seven"] + base["S_seven"])
        disjoint_curvatures[kappa] += 1
        actual_abs_sum += abs(kappa)
        amask = (1 << a[0]) | (1 << a[1])
        bmask = (1 << b[0]) | (1 << b[1])
        jointly_touched = sum(weight for mask, weight in support_fibers
                              if mask & amask and mask & bmask)
        exact_sum_joint_exposure += jointly_touched
        slack = 2*jointly_touched - abs(kappa)
        if slack < 0:
            raise AssertionError("pointwise original source support cap violated")
        if smallest_pointwise_slack is None or slack < smallest_pointwise_slack:
            smallest_pointwise_slack = slack
        record = (kappa, a, b, g)
        if most_negative is None or record < most_negative:
            most_negative = record
    if sum(disjoint_curvatures.values()) != N_DOUBLE_TRANSPOSITIONS:
        raise AssertionError("missing disjoint mixed curvatures")
    exposure = exact_all_disjoint_joint_exposure(source)
    if exact_sum_joint_exposure != exposure["sum_jointly_touched_original_sources_over_all_pairs"]:
        raise AssertionError("K(n,r) source exposure != independent enumeration of all 4095 swap pairs")
    if actual_abs_sum > exposure["sum_absolute_mixed_curvature_upper"]:
        raise AssertionError("all-h signed curvature support bound falsified")

    def full_independent_check(g):
        row = states[g]
        left = full_left_score(source, g)
        right = right_first_independent(W32_LEFT_H45, g)
        if left != row or any(right[k] != row[k] for k in
                             ("seven_counts", "S_seven", "Q7_necessary_numerator",
                              "right_C_accepted")):
            raise AssertionError("true original LEFT/RIGHT independent sixset mismatch")
        return True

    # Independent full original source check for best-of-two, best-of-one,
    # max radius-two score and each cycle type representative.
    representative = {best, max(states, key=lambda g:(states[g]["S_seven"],g)),
                      next(g for g in states if kind[g] == "disjoint"),
                      next(g for g in states if kind[g] == "three_cycle")}
    # Independently recount EVERY tied exact distance-two minimum, not just
    # the lexical winner. This is a finite ORIGINAL right-first falsifier.
    representative.update(g for g, row in states.items()
                          if row["S_seven"] == best_score)
    for g in representative:
        full_independent_check(g)
    one_check = full_left_score(source, first_perm[first_min])
    if one_check != first[first_min]:
        raise AssertionError("best one-swap full original source mismatch")
    best_right = right_first_independent(W32_LEFT_H45, first_perm[first_min])
    if best_right["seven_counts"] != first[first_min]["seven_counts"]:
        raise AssertionError("best first swap right-first mismatch")

    kappa, ka, kb, kg = most_negative
    source_curvature = independent_disjoint_original_source_curvature(
        source, start, ka, kb)
    if source_curvature["mixed_curvature"] != kappa:
        raise AssertionError("most negative true joint original source curvature wrong")
    touched = source_curvature["jointly_touched_original_sixsets"]
    if abs(kappa) > 2*touched:
        raise AssertionError("pointwise original joint source support bound violated")
    if not (smallest_pointwise_slack is not None and smallest_pointwise_slack >= 0):
        raise AssertionError("all 4095 pointwise source support caps not checked")

    best_curvature = None
    if kind[best] == "disjoint":
        a, b = path
        source_best = independent_disjoint_original_source_curvature(
            source, start, a, b)
        formula = (best_score - first[a]["S_seven"] -
                   first[b]["S_seven"] + base["S_seven"])
        if source_best["mixed_curvature"] != formula:
            raise AssertionError("best mixed curvature disagrees with genuine original sources")
        best_curvature = source_best

    improvements = sorted((row["S_seven"], g) for g,row in states.items()
                          if row["S_seven"] < 68)
    minima = min(base["S_seven"], first[first_min]["S_seven"], best_score)

    # Independently reconstructed true W(3,2) 62,370-sixset baseline and
    # full 105+5005 endpoints. Pin the finite S68 RADIUS-TWO optimum; a
    # later code or source drift must fail closed instead of silently
    # changing the accepted scientific witness.
    if (first[first_min]["S_seven"] != 75 or first_min != (8, 9)
            or sum(row["S_seven"] < 68 for row in first.values()) != 0
            or best_score != 69 or minima != 68
            or improvements or improves_three_cycle or improves_disjoint
            or sum(1 for row in states.values() if row["S_seven"] == 69) != 2
            or best != (2,9,11,4,10,6,0,13,5,14,3,7,12,1,8)
            or tuple(states[best]["seven_counts"][t] for t in TAGS)
               != (0,41,25,0,0,2,1)
            or states[best]["Q7_necessary_numerator"] != 3158110
            or states[best]["right_C_accepted"] != 0
            or path != ((4,13),(0,12))
            or first[path[0]]["S_seven"] != 78
            or kappa != -65 or (ka,kb) != ((0,12),(4,11))
            or actual_abs_sum != 40989
            or exact_sum_joint_exposure != 77873220
            or smallest_pointwise_slack != 33604
            or len(support_fibers) != 7468):
        raise AssertionError("independent original W32 exact S68 radius-two witness changed")
    return {
        "base_S":68, "base_global_right":start,
        "original_sixsets":source["left_source_size"],
        "static_eligible_original_sources":source["static_eligible"],
        "physical_K6_templates":len(fibers["templates"]),
        "original_right_multiset_fibers":fibers["right_fibers"],
        "first_neighborhood_count":N_SWAPS,
        "first_minimum_S":first[first_min]["S_seven"],
        "first_minimum_swap":first_min,
        "first_strict_improving_count":sum(r["S_seven"]<68 for r in first.values()),
        "first_stationary":all(r["S_seven"]>=68 for r in first.values()),
        "distance_two_distinct_states":len(states),
        "distance_two_ordered_paths":sum(map(len,decomps.values())),
        "distance_two_three_cycles":N_THREE_CYCLES,
        "distance_two_disjoint_double_transpositions":N_DOUBLE_TRANSPOSITIONS,
        "distance_two_minimum_S":best_score,
        "inclusive_radius_two_minimum_S":minima,
        "distance_two_strict_improving_count":len(improvements),
        "improving_three_cycles":improves_three_cycle,
        "improving_disjoint_double_transpositions":improves_disjoint,
        "best_two_global_right":best,
        "best_two_original_seven_vector":states[best]["seven_counts"],
        "best_two_original_right_C":states[best]["right_C_accepted"],
        "best_two_Q7_necessary_numerator":states[best]["Q7_necessary_numerator"],
        "best_two_cycle_type":kind[best],
        "best_two_ordered_path":path,
        "best_two_path_first_S":first[path[0]]["S_seven"],
        "best_two_path_barrier_over_base":max(
            68, first[path[0]]["S_seven"], best_score)-68,
        "best_two_source_curvature":best_curvature,
        "most_negative_disjoint_curvature":kappa,
        "most_negative_disjoint_pair":(ka,kb),
        "most_negative_joint_source":source_curvature,
        "disjoint_curvature_negative_count":sum(v for k,v in disjoint_curvatures.items() if k<0),
        "disjoint_curvature_minimum":min(disjoint_curvatures),
        "sum_abs_disjoint_curvature":actual_abs_sum,
        "all_4095_individual_support_caps_verified":True,
        "smallest_individual_two_M_minus_abs_kappa":smallest_pointwise_slack,
        "independently_enumerated_joint_exposure_all_disjoint_pairs":exact_sum_joint_exposure,
        "original_support_mask_fiber_count":len(support_fibers),
        "all_h_joint_exposure_certificate":exposure,
        "exact_original_left_and_right_falsifiers":True,
        "no_full_right_15_factorial_minimum_claim":True,
        "no_all_h_seven_lower_or_full_GF5_R3_claim":True,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(exact_next_ball_from_s68(), sort_keys=True, indent=2))
