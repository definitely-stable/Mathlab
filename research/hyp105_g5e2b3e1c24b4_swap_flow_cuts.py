"""HYP-105 C24-B4: exact all-h swap flow/cut identities and genuine W32 third neighborhood.

Theorems concern the original, globally shared complete right bijection.
Finite W32 evidence fixes ONE left f and inspects exactly 105 third-neighborhood
right maps. Neither a global W32 minimum nor an all-h positive bound follows.
"""
from collections import Counter
from itertools import combinations

from hyp105_g5e2b3e1c24b_three_collision import W32_LEFT_H45
from hyp105_g5e2b3e1c24b2_joint_seven import (
    TAGS, GF5_WEIGHTS, accepted, compile_left, full_left_score,
    right_first_independent, right_masks,
)
from hyp105_g5e2b3e1c24b3_joint_swap_gradient import (
    exact_exchange_neighborhood, legal_transpose,
)

# True original right GQ line -> occupied physical K6 edge index after exactly
# (6,14) then (12,13) from the C24-B1 complete global right map.
W32_RIGHT_AFTER_TWO_SWAPS = (12, 10, 5, 2, 8, 14, 11, 7, 0, 6, 3, 13, 4, 9, 1)


def swap_flow_certificate(source, g, i, j):
    """Exact original sixset gain/loss accounting on one genuine global swap.

    For arbitrary original sources this definition is all-h: a given sixset
    contributes to exactly one STATIC left+original-endpoint family; right
    transpositions alter only the acceptance predicate of touched sixsets.
    Here the executable specializes the definition to true W(3,2).
    """
    new = legal_transpose(g, i, j)
    old_masks, new_masks = right_masks(g), right_masks(new)
    gain, loss = Counter(), Counter()
    gain_c = loss_c = 0
    affected_original = 0
    for rid in source["by_line"][i] | source["by_line"][j]:
        record = source["records"][rid]
        before = accepted(record, old_masks)
        after = accepted(record, new_masks)
        amount = record[3]
        affected_original += amount
        if before == after:
            continue
        if after:
            gain[record[0]] += amount
            if len(set(record[1])) == 3:
                gain_c += amount
        else:
            loss[record[0]] += amount
            if len(set(record[1])) == 3:
                loss_c += amount
    gvec = {tag: gain[tag] for tag in TAGS}
    lvec = {tag: loss[tag] for tag in TAGS}
    dvec = {tag: gvec[tag] - lvec[tag] for tag in TAGS}
    gsum, lsum = sum(gvec.values()), sum(lvec.values())
    return {
        "swap": (i, j),
        "affected_original_sixsets": affected_original,
        "gain_by_tag": gvec, "loss_by_tag": lvec, "delta_by_tag": dvec,
        "gain": gsum, "loss": lsum, "delta_S": gsum - lsum,
        "delta_Q7_necessary": sum(GF5_WEIGHTS[k] * dvec[tag]
                                  for k, tag in enumerate(TAGS)),
        "original_right_C_gain": gain_c,
        "original_right_C_loss": loss_c,
        "original_right_C_delta": gain_c - loss_c,
        "strictly_improving_iff_loss_gt_gain": (lsum > gsum),
    }


def signed_swap_cut_certificate(entries, n):
    """Recover EVERY signed swap gradient from singleton/pair cut sums.

    Let d_ij=S(g^ij)-S(g). For U subset of original right lines, define
    C(U)=sum_(i in U, j outside U) d_ij. Then exactly
    2*d_ij = C({i})+C({j})-C({i,j}).
    Here pair cuts refer to sums of *individual transposition* gradients,
    NOT to a new simultaneous block permutation. No positivity is implied.
    """
    if type(n) is not int or not 3 <= n <= 15:
        raise ValueError("finite cut audit requires 3 <= n <= 15")
    edge = {}
    for row in entries:
        pair = tuple(row["swap"])
        if (len(pair) != 2 or not all(type(x) is int for x in pair)
                or not 0 <= pair[0] < pair[1] < n or pair in edge):
            raise ValueError("distinct sorted original-right swap edges required")
        delta = row["exchange"]["delta_S"]
        if type(delta) is not int:
            raise ValueError("exact integer exchange deltas required")
        edge[pair] = delta
    if set(edge) != set(combinations(range(n), 2)):
        raise ValueError("complete transposition graph required")

    def cut_of(mask):
        return sum(d for (i, j), d in edge.items()
                   if bool(mask & (1 << i)) != bool(mask & (1 << j)))

    single = tuple(cut_of(1 << i) for i in range(n))
    pair_cut = {(i, j): cut_of((1 << i) | (1 << j))
                for i, j in combinations(range(n), 2)}
    recovered = {(i, j): single[i] + single[j] - pair_cut[i, j]
                 for i, j in edge}
    if any(v % 2 or v // 2 != edge[k] for k, v in recovered.items()):
        raise AssertionError("signed swap gradients not recovered from cuts")
    violating = tuple(pair for pair in edge
                      if pair_cut[pair] > single[pair[0]] + single[pair[1]])
    improving = tuple(pair for pair, d in edge.items() if d < 0)
    if violating != improving:
        raise AssertionError("all-h pair-cut stationarity reconstruction failed")
    # All nontrivial cuts up to complementary symmetry; pin line n-1 OUT.
    # This is finite W32 diagnostic, not a polynomial all-h algorithm.
    minimum = None
    negative_cuts = 0
    for mask in range(1, 1 << (n - 1)):
        v = cut_of(mask)
        if minimum is None or v < minimum:
            minimum = v
        if v < 0:
            negative_cuts += 1
    return {
        "edges": len(edge),
        "sum_delta": sum(edge.values()),
        "minimum_singleton_cut": min(single),
        "min_nontrivial_signed_cut": minimum,
        "negative_cut_count_unoriented": negative_cuts,
        "strict_improving_edges": len(improving),
        "pair_cut_inequality_violations": len(violating),
        "one_swap_stationary": not violating,
        "all_edge_gradients_recovered_exactly": True,
        "all_singleton_cuts_nonnegative": min(single) >= 0,
        "negative_pair_does_not_require_negative_cut": True,
    }


def genuine_w32_third_neighborhood():
    """Third *complete* original-right 105-neighborhood; no global claim."""
    source = compile_left(W32_LEFT_H45)
    g = W32_RIGHT_AFTER_TWO_SWAPS
    neighborhood = exact_exchange_neighborhood(source, g)
    baseline = neighborhood["baseline"]
    if baseline["S_seven"] != 111 or len(neighborhood["entries"]) != 105:
        raise AssertionError("C24-B3 genuine original W32 two-swap witness changed")
    reference = right_first_independent(W32_LEFT_H45, g)
    if any(reference[k] != baseline[k] for k in
           ("S_seven", "seven_counts", "Q7_necessary_numerator", "right_C_accepted")):
        raise AssertionError("independent full right-first ORIGINAL census disagrees")
    candidate = neighborhood["min_S"]
    take = candidate["S_seven"] < baseline["S_seven"]
    next_g = legal_transpose(g, *candidate["swap"]) if take else g
    next_row = candidate if take else baseline
    independent_next = right_first_independent(W32_LEFT_H45, next_g)
    if any(independent_next[k] != next_row[k] for k in
           ("S_seven", "seven_counts", "Q7_necessary_numerator", "right_C_accepted")):
        raise AssertionError("third-step independent 62,370-source census disagrees")
    flow = swap_flow_certificate(source, g, *candidate["swap"])
    if (flow["delta_S"] != candidate["S_seven"] - baseline["S_seven"]
            or any(flow["delta_by_tag"][tag] !=
                   candidate["seven_counts"][tag] - baseline["seven_counts"][tag]
                   for tag in TAGS)
            or flow["delta_Q7_necessary"] !=
               candidate["Q7_necessary_numerator"] - baseline["Q7_necessary_numerator"]
            or flow["original_right_C_delta"] !=
               candidate["right_C_accepted"] - baseline["right_C_accepted"]):
        raise AssertionError("independent source gain/loss conservation failed")
    cuts = signed_swap_cut_certificate(neighborhood["entries"], 15)
    if cuts["strict_improving_edges"] != neighborhood["strict_S_improving_global_neighbors"]:
        raise AssertionError("signed-cut and exchange-neighborhood sign mismatch")
    if take != flow["strictly_improving_iff_loss_gt_gain"]:
        raise AssertionError("strict gain/loss criterion lost")
    return {
        "original_source_size": source["left_source_size"],
        "source_static_eligible": source["static_eligible"],
        "two_swap_original_right": g,
        "two_swap_seven_vector": baseline["seven_counts"],
        "two_swap_S": baseline["S_seven"],
        "two_swap_Q7_necessary": baseline["Q7_necessary_numerator"],
        "two_swap_original_right_C": baseline["right_C_accepted"],
        "third_neighborhood_size": len(neighborhood["entries"]),
        "third_strictly_improving_neighbors": neighborhood["strict_S_improving_global_neighbors"],
        "third_best_swap": candidate["swap"],
        "third_best_neighbor_S": candidate["S_seven"],
        "third_best_neighbor_seven_vector": candidate["seven_counts"],
        "third_move_taken": take,
        "after_optional_third_S": next_row["S_seven"],
        "after_optional_third_Q7_necessary": next_row["Q7_necessary_numerator"],
        "after_optional_third_original_right": next_g,
        "after_two_swaps_stationary": neighborhood["one_swap_local_minimum_S"],
        "best_neighbor_flow": flow,
        "swap_cut_certificate": cuts,
        "independent_right_first_census": True,
        "scope": "FINITE W32, ONE fixed left f, exactly third 105-right-swap neighborhood",
        "all_h_positive_lower_proved": False,
        "full_GF5_R3_upper_proved": False,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(genuine_w32_third_neighborhood(), indent=2, sort_keys=True))
