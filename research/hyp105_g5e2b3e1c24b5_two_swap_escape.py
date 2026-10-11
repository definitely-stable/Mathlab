"""HYP-105 C24-B5: exact W32 transposition-distance-two ball.

For the TRUE original W(3,2) point/line GQ, fix one common complete left f
and the globally coherent right S=72 1-swap strict local optimum of C24-B4.

Enumerate 105*104 ordered distinct double swaps; quotient by identical
resulting global right permutations (910 directed 3-cycles and 4095 disjoint
double transpositions = 5005 distinct distance-two states). Compute each
score by a new 130-template right-first *pullback* fiber oracle rather than
reusing left-first 105-neighborhood incremental deltas.

Finite original-GQ evidence only. NOT a 15! global right minimum or all-h
lower bound; Q7 is a necessary GF5 numerator, not the entire GF5 R3.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb

from hyp105_g5e2b3e1c24b_three_collision import W32_LEFT_H45
from hyp105_g5e2b3e1c24b2_joint_seven import (
    TAGS, GF5_WEIGHTS, accepted, compile_left, full_permutation,
    full_left_score, physical_templates, right_first_independent, right_masks,
    result,
)
from hyp105_g5e2b3e1c24b3_joint_swap_gradient import legal_transpose
from hyp105_g5e2b3e1c24b4_swap_flow_cuts import (
    certified_explicit_five_swap_witness,
)

N_RIGHT = 15
N_SWAPS = comb(N_RIGHT, 2)
N_THREE_CYCLES = 2 * comb(N_RIGHT, 3)
N_DOUBLE_TRANSPOSITIONS = 3 * comb(N_RIGHT, 4)
N_DISTANCE_TWO = N_THREE_CYCLES + N_DOUBLE_TRANSPOSITIONS
ALL_SWAPS = tuple(combinations(range(N_RIGHT), 2))


def compile_right_pullback_fibers(source):
    """Aggregate ORIGINAL sixsets by right multiset and fixed static family.

    The inverse image of any physical right K6 two-factor multiset under a
    *globally common right permutation* is a unique original-right multiset.
    Non-D6 family counts can therefore be directly summed. D6 needs its
    original six-position LEFT dual checked against the actual RIGHT dual.

    Integer source multiplicities are preserved. No sampling or per-J
    map choice. This is independent of left-first sparse swap deltas.
    """
    if source["left_source_size"] != 62370 or len(source["by_line"]) != N_RIGHT:
        raise ValueError("genuine original W32 source required")
    ordinary, d6 = defaultdict(Counter), defaultdict(list)
    total = 0
    for record in source["records"]:
        tag, lines, sig, amount = record
        if tag not in TAGS or len(lines) != 6 or type(amount) is not int or amount <= 0:
            raise ValueError("invalid original sixset fiber")
        key = tuple(sorted(lines))
        if tag == "D6":
            if sig is None:
                raise ValueError("D6 original static left dual required")
            d6[key].append(record)
        else:
            ordinary[key][tag] += amount
        total += amount
    if total != source["static_eligible"]:
        raise AssertionError("compressed original multiplicities lost")
    templates = physical_templates()
    if len(templates) != 130 or len(set(templates)) != 130:
        raise AssertionError("exact physical K6 130-template contract changed")
    return {"ordinary": dict(ordinary), "D6": dict(d6),
            "templates": templates, "original_eligible": total,
            "right_fibers": len(set(ordinary) | set(d6))}


def template_pullback_score(fibers, global_g):
    """Exact full seven-vector via 130 K6 right two-factor inverse images.

    Each physically accepted right source has exactly one right physical
    multiset of six edges, among the 130 templates. The original global
    right injection gives a bijection of multisets, so enumeration neither
    duplicates nor loses an ORIGINAL six-incidence set. D6's ordered-column
    dual condition is checked on the exact original candidate records.
    """
    g = full_permutation(global_g)
    inv = [0] * N_RIGHT
    for original_line, physical_index in enumerate(g):
        inv[physical_index] = original_line
    masks = right_masks(g)
    counts = Counter()
    original_right_c = 0
    for pattern in fibers["templates"]:
        key = tuple(sorted(inv[edge] for edge in pattern))
        ordinary = fibers["ordinary"].get(key)
        if ordinary:
            counts.update(ordinary)
            if len(set(key)) == 3:
                original_right_c += sum(ordinary.values())
        for record in fibers["D6"].get(key, ()):
            if accepted(record, masks):
                counts["D6"] += record[3]
    return result(counts, original_right_c)


def disjoint_swap_curvature(score0, score_a, score_b, score_ab):
    """Exact discrete mixed derivative for DISJOINT swap pairs only.

    Curvature < -(Delta_A + Delta_B) iff AB improves the baseline.
    Overlapping swaps are order-dependent; never use symmetric curvature
    without a commutativity proof.
    """
    for x in (score0, score_a, score_b, score_ab):
        if type(x) is not int or x < 0:
            raise ValueError("nonnegative integer exact scores required")
    da, db = score_a - score0, score_b - score0
    kappa = score_ab - score_a - score_b + score0
    return {"delta_first": da, "delta_second_independent": db,
            "mixed_curvature": kappa,
            "escape_iff_curvature_below_negative_first_sum":
                (score_ab < score0) == (kappa < -(da + db)),
            "escapes": score_ab < score0}


def audit_two_swap_ball(source=None, *, verify_right_first=True):
    """Exhaust the ENTIRE transposition-distance <=2 ball at frozen W32 S72.

    Complexity: 130 physical templates for each of exactly 5005 unique
    distance-two maps, plus 105 one-swap states. No exhaustive 15! claim.
    """
    if source is None:
        source = compile_left(W32_LEFT_H45)
    certificate = certified_explicit_five_swap_witness(source)
    g0 = full_permutation(certificate["final_original_right_perm"])
    fibers = compile_right_pullback_fibers(source)
    initial = template_pullback_score(fibers, g0)
    if (initial["S_seven"] != 72 or initial != full_left_score(source, g0)
            or initial["seven_counts"] != certificate["final_seven_counts"]):
        raise AssertionError("source/template baseline disagreement at original S72")
    first = {}
    g_after_first = {}
    for pair in ALL_SWAPS:
        p = legal_transpose(g0, *pair)
        g_after_first[pair] = p
        first[pair] = template_pullback_score(fibers, p)
    if len(first) != 105 or min(x["S_seven"] for x in first.values()) != 74:
        raise AssertionError("C24-B4 original strict 1-swap W32 bound changed")
    if any(x["S_seven"] <= 72 for x in first.values()):
        raise AssertionError("the 72 witness is not strict 1-swap stationary")

    # Each pair of DIFFERENT right transpositions composes either a 3-cycle
    # (one common original line) or two disjoint 2-cycles (four lines).
    # Each 3-cycle admits EXACTLY 3 ordered two-swap decompositions;
    # each double transposition admits EXACTLY 2 (commuting) decompositions.
    by_state = {}
    representations = defaultdict(list)
    kinds = {}
    for a in ALL_SWAPS:
        p = g_after_first[a]
        for b in ALL_SWAPS:
            if b == a:
                continue  # identity at distance 0; outside EXACT distance 2
            target = legal_transpose(p, *b)
            kind = "three_cycle" if len(set(a) & set(b)) == 1 else "disjoint"
            previous = kinds.setdefault(target, kind)
            if previous != kind:
                raise AssertionError("same right map has two different distance-two cycle types")
            representations[target].append((a, b))
            if target not in by_state:
                by_state[target] = template_pullback_score(fibers, target)
    if (len(by_state) != N_DISTANCE_TWO or
            sum(kind == "three_cycle" for kind in kinds.values()) != N_THREE_CYCLES or
            sum(kind == "disjoint" for kind in kinds.values()) != N_DOUBLE_TRANSPOSITIONS or
            sum(len(paths) for paths in representations.values()) != N_SWAPS * (N_SWAPS - 1)):
        raise AssertionError("complete and distinct two-swap original right orbit count failed")
    for g, paths in representations.items():
        if len(paths) != (3 if kinds[g] == "three_cycle" else 2):
            raise AssertionError("distance-two ordered decomposition multiplicity wrong")

    score_hist = Counter(row["S_seven"] for row in by_state.values())
    improving = [g for g, row in by_state.items() if row["S_seven"] < 72]
    best = min(by_state, key=lambda key: (by_state[key]["S_seven"], key))
    best_row = by_state[best]
    best_paths = representations[best]
    choose_path = lambda p: (max(72, first[p[0]]["S_seven"],
                                   best_row["S_seven"]), p[0], p[1])
    best_path = min(best_paths, key=choose_path)
    first_at_best = first[best_path[0]]["S_seven"]
    best_peak = max(first_at_best, best_row["S_seven"], 72)
    best_is_escape = best_row["S_seven"] < 72

    # Correctness firewall: direct independent LEFT full 51k+ source for
    # baseline, deterministic disjoint and overlapping samples, and minimum;
    # independently built RIGHT-FIRST full 62,370 source for best target.
    representatives = [best]
    representatives.extend(next(g for g, k in kinds.items() if k == kind)
                           for kind in ("three_cycle", "disjoint"))
    representatives.append(max(by_state, key=lambda k: (by_state[k]["S_seven"], k)))
    representatives.append(min(by_state))
    for g in set(representatives):
        if full_left_score(source, g) != by_state[g]:
            raise AssertionError("template pullback != full 51k original LEFT source")
    independent_best = right_first_independent(W32_LEFT_H45, best)
    if any(independent_best[k] != best_row[k] for k in
           ("seven_counts", "S_seven", "Q7_necessary_numerator", "right_C_accepted")):
        raise AssertionError("best distance-two witness fails independent RIGHT-FIRST census")
    if verify_right_first:
        independent_start = right_first_independent(W32_LEFT_H45, g0)
        if independent_start["seven_counts"] != initial["seven_counts"]:
            raise AssertionError("initial original RIGHT-FIRST witness changed")

    # Hosted C24-B5 Contract witnessed an exact COMPLETE 5005-state
    # ORIGINAL W32 finite two-swap escape. Freeze the published result;
    # deviations fail closed on subsequent HEADs.
    if (best_row["S_seven"] != 68 or len(improving) != 2
            or score_hist.get(68) != 2
            or kinds[best] != "disjoint"
            or best_path != ((4, 14), (3, 12))
            or first_at_best != 82
            or best_peak != 82
            or best_row["Q7_necessary_numerator"] != 3112510
            or tuple(best_row["seven_counts"][t] for t in TAGS)
               != (0, 44, 21, 0, 0, 2, 1)
            or best_row["right_C_accepted"] != 0
            or best != (12, 9, 11, 4, 1, 6, 0, 13, 5, 14, 3, 7, 2, 10, 8)):
        raise AssertionError("hosted C24-B5 exact W32 5005-map escape certificate changed")

    best_curvature = None
    if kinds[best] == "disjoint":
        a, b = best_path
        best_curvature = disjoint_swap_curvature(
            72, first[a]["S_seven"], first[b]["S_seven"], best_row["S_seven"])
    else:
        # 3-cycles compose noncommutatively: only ordered path deltas.
        best_curvature = {"noncommuting": True, "no_symmetric_disjoint_hessian_claim": True}

    return {
        "original_source_size": source["left_source_size"],
        "static_eligible": fibers["original_eligible"],
        "source_right_multiset_fibers": fibers["right_fibers"],
        "physical_K6_2factor_templates": len(fibers["templates"]),
        "base_S": 72, "base_perm": g0, "base_vector": initial["seven_counts"],
        "first_neighbors": N_SWAPS, "min_one_swap_S": min(x["S_seven"] for x in first.values()),
        "one_swap_strictly_stationary": True,
        "ordered_distinct_double_swaps": N_SWAPS * (N_SWAPS - 1),
        "unique_distance_two_states": len(by_state),
        "three_cycles": N_THREE_CYCLES,
        "disjoint_double_transpositions": N_DOUBLE_TRANSPOSITIONS,
        "min_distance_two_S": best_row["S_seven"],
        "min_ball_radius_two_S": min(72, best_row["S_seven"]),
        "strictly_better_distance_two_maps": len(improving),
        "distance_two_score_histogram": dict(sorted(score_hist.items())),
        "best_distance_two_perm": best,
        "best_distance_two_vector": best_row["seven_counts"],
        "best_distance_two_right_C": best_row["right_C_accepted"],
        "best_distance_two_Q7_necessary": best_row["Q7_necessary_numerator"],
        "best_kind": kinds[best],
        "best_path": best_path,
        "best_path_first_S": first_at_best,
        "best_path_peak_S": best_peak,
        "best_path_minimum_barrier_above_72": best_peak - 72,
        "best_curvature": best_curvature,
        "strict_two_swap_escape_exists": best_is_escape,
        "radius_two_local_minimum": not best_is_escape,
        "independent_left_right_original_oracles": True,
        "not_all_15_factorial_or_all_left_f": True,
        "not_all_h_positive_bound_or_total_GF5_R3": True,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(audit_two_swap_ball(), indent=2, sort_keys=True))
