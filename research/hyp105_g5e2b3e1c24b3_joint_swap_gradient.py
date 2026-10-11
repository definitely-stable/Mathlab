"""HYP-105 C24-B3: exact finite joint-seven penalty frontier and exchange gate.

Only genuine original W(3,2) global f,g and complete coherent ORIGINAL
right-line permutations. Mathematical all-h exchange lemma holds for every
finite original GQ source, but numerical envelopes are ONLY 105 neighbors.
"""
from collections import Counter
from fractions import Fraction

from hyp105_g5e2b3e1c24b_three_collision import (
    W32_LEFT_H45, W32_RIGHT_H45_ZERO)
from hyp105_g5e2b3e1c24b2_joint_seven import (
    TAGS, GF5_WEIGHTS, compile_left, full_permutation,
    full_left_score, right_first_independent, right_swap_105,
)

def legal_transpose(global_g, i, j):
    """ONE common original-right bijection, swapping exactly two line images."""
    g = list(full_permutation(global_g))
    if (type(i) is not int or type(j) is not int or
            i == j or not 0 <= i < 15 or not 0 <= j < 15):
        raise ValueError("two distinct ORIGINAL right lines required")
    g[i], g[j] = g[j], g[i]
    return tuple(g)


def exact_joint_seven_swap_signature(reference, changed):
    """Seven fixed-family integer deltas; no motif can migrate between tags."""
    if set(reference["seven_counts"]) != set(TAGS) or set(changed["seven_counts"]) != set(TAGS):
        raise ValueError("complete seven-class original source counts required")
    diff = tuple(changed["seven_counts"][k] - reference["seven_counts"][k]
                 for k in TAGS)
    dS = changed["S_seven"] - reference["S_seven"]
    dQ = changed["Q7_necessary_numerator"] - reference["Q7_necessary_numerator"]
    dC = changed["right_C_accepted"] - reference["right_C_accepted"]
    if dS != sum(diff) or dQ != sum(w * d for w, d in zip(GF5_WEIGHTS, diff)):
        raise AssertionError("one-global-g fixed seven-class exchange conservation failed")
    return {"delta_seven": dict(zip(TAGS, diff)), "delta_S": dS,
            "delta_Q7": dQ, "delta_original_right_C": dC,
            "cross_class_compensation": bool(any(x < 0 for x in diff) and
                                             any(x > 0 for x in diff))}


def exact_finite_penalty_frontier(rows):
    """Exact lower envelope min(S + lambda * original-right-C), lambda>=0.

    Returns a simple two-phase certificate ONLY when source rows satisfy
    the witnessed two-point dominance conditions. Does not extrapolate.
    """
    rows = tuple(rows)
    if not rows:
        raise ValueError("nonempty coherent right permutation scores required")
    if any(type(x["S_seven"]) is not int or type(x["right_C_accepted"]) is not int
           or x["S_seven"] < 0 or x["right_C_accepted"] < 0 for x in rows):
        raise ValueError("invalid nonnegative exact integer seven/C scores")
    zeros = [x for x in rows if x["right_C_accepted"] == 0]
    positives = [x for x in rows if x["right_C_accepted"] > 0]
    if not zeros or not positives:
        raise ValueError("both C=0 and C>0 global-map witnesses required")
    z = min(zeros, key=lambda x: (x["S_seven"], x["swap"]))
    p = min(positives, key=lambda x: (x["S_seven"], x["right_C_accepted"], x["swap"]))
    if p["right_C_accepted"] != 1 or p["S_seven"] >= z["S_seven"]:
        raise ValueError("two-phase closed envelope preconditions do not hold")
    switch = z["S_seven"] - p["S_seven"]
    if switch <= 0:
        raise AssertionError("zero-C witness must cost more S")
    for weight in (Fraction(0), Fraction(1, 2), Fraction(3), Fraction(switch),
                   Fraction(switch + 1), Fraction(10 * switch)):
        direct = min(Fraction(x["S_seven"]) + weight * x["right_C_accepted"]
                     for x in rows)
        expected = min(Fraction(z["S_seven"]),
                       Fraction(p["S_seven"]) + weight)
        if direct != expected:
            raise AssertionError("two-point penalty envelope incorrectly inferred")
    return {"zero_C_witness_swap": z["swap"],
            "zero_C_min_S": z["S_seven"], "positive_C_witness_swap": p["swap"],
            "positive_C_min_S": p["S_seven"],
            "positive_C_at_best": p["right_C_accepted"],
            "switch_weight_lambda": switch,
            "for_every_nonnegative_lambda_exact": True,
            "below_switch": "positive-C-one witness",
            "above_switch": "zero-C witness",
            "tie_at_switch": True,
            "no_global_15_factorial_or_all_h_claim": True}


def exact_exchange_neighborhood(source, global_g):
    """All 105 complete coherent global right transpositions, seven-vector deltas."""
    g = full_permutation(global_g)
    raw = right_swap_105(source, g)
    baseline = raw["baseline"]
    entries = []
    for trial in raw["swaps"]:
        sign = exact_joint_seven_swap_signature(baseline, trial)
        entries.append({**trial, "exchange": sign})
    if len(entries) != 105:
        raise AssertionError("incomplete global transposition 105-graph")
    improving = tuple(e for e in entries if e["exchange"]["delta_S"] < 0)
    return {
        "global_right": g, "baseline": baseline,
        "entries": entries,
        "min_S": raw["min_S"],
        "C_histogram": raw["C_histogram"],
        "strict_S_improving_global_neighbors": len(improving),
        "one_swap_local_minimum_S": not improving,
        "sum_joint_exchange_delta_by_tag": {
            k: sum(e["exchange"]["delta_seven"][k] for e in entries)
            for k in TAGS},
        "sum_delta_S": sum(e["exchange"]["delta_S"] for e in entries),
        "sum_delta_Q7": sum(e["exchange"]["delta_Q7"] for e in entries),
        "simultaneous_positive_negative_class_tradeoffs": sum(
            e["exchange"]["cross_class_compensation"] for e in entries),
    }


def verified_two_step_finite_descent():
    """Two exact 105-neighborhood audits. Not a global minimum search."""
    source = compile_left(W32_LEFT_H45)
    initial = exact_exchange_neighborhood(source, W32_RIGHT_H45_ZERO)
    first = initial["min_S"]
    if first["swap"] != (6, 14) or first["S_seven"] != 129:
        raise AssertionError("C24-B2 frozen first global S improvement invalid")
    improved_g = legal_transpose(W32_RIGHT_H45_ZERO, *first["swap"])
    independent = right_first_independent(W32_LEFT_H45, improved_g)
    if (independent["seven_counts"] != first["seven_counts"] or
            independent["right_C_accepted"] != first["right_C_accepted"]):
        raise AssertionError("first step independent full 62370 right census failed")
    next_step = exact_exchange_neighborhood(source, improved_g)
    if next_step["baseline"]["S_seven"] != 129:
        raise AssertionError("first step not the second neighborhood baseline")
    possible = next_step["min_S"]
    # Every legal one-swap neighbor may be worse if g is already a
    # strict local minimum; compare before applying a candidate move.
    # The min over exactly 105 swaps can exceed current S if the first-step
    # map is already a strict 1-swap local minimum; no action is then taken.
    take_move = possible["S_seven"] < 129
    second_g = legal_transpose(improved_g, *possible["swap"]) if take_move else improved_g
    second_score = possible if take_move else next_step["baseline"]
    if take_move:
        second_independent = right_first_independent(W32_LEFT_H45, second_g)
        if second_independent["seven_counts"] != second_score["seven_counts"]:
            raise AssertionError("second global step independent right census failed")
    return {
        "source_original_left_2factors": source["left_source_size"],
        "first_initial_S": initial["baseline"]["S_seven"],
        "first_best_neighbor": first,
        "initial_penalty_frontier": exact_finite_penalty_frontier(initial["entries"]),
        "initial_seven_signed_exchange_sum": initial["sum_joint_exchange_delta_by_tag"],
        "initial_class_antagonistic_neighbors":
            initial["simultaneous_positive_negative_class_tradeoffs"],
        "after_first_full_right_perm": improved_g,
        "after_first_S": next_step["baseline"]["S_seven"],
        "after_first_one_swap_S_stationary": next_step["one_swap_local_minimum_S"],
        "after_first_strict_improving_neighbors":
            next_step["strict_S_improving_global_neighbors"],
        "second_move_taken": take_move,
        "second_best_or_stationary_S": second_score["S_seven"],
        "second_full_right_perm": second_g,
        "only_two_exact_neighborhoods_not_global_minimum": True,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(verified_two_step_finite_descent(), indent=2, sort_keys=True))
