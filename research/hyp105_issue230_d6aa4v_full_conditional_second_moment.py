"""HYP-105 #230 / AA4-V: exact quenched second moment of genuine original D6.

Parent #487 supplies the all-overlap TWO-event line-cycle gluing probability.
This module contracts the ENTIRE ordered pair matrix for any explicitly
provided family of true six-incidence candidates sharing ONE fixed full
point map f and ONE uniformly random complete global line map g.

All six-line cycles supplied by a caller must originate from genuine ORIGINAL
six-distinct-incidence Q with six different original point/line factors and a
fixed-f connected left physical C6. The W32 adapter enforces that condition.
No independent event assumption; no all-f,g minimum theorem is claimed.
"""
from collections import Counter
from fractions import Fraction
from math import perm

from hyp105_issue230_d6aa4r_quenched_original_d6 import _params
from hyp105_issue230_d6aa4ucyc_shared_line_gluing import (
    _orientations, canonical_two_source_C6_gluing,
    exact_two_D6_gluing_kernel,
    _actual_original_Q_line_cycle,
)
from hyp105_issue230_d6aa4tcyc_fixed_f_d6_pair import (
    genuine_W32_fixed_f_original_connected_left_Q,
)


def canonical_single_original_line_cycle(cycle):
    """D6 edge positions can rotate/reverse, never permute arbitrarily."""
    return min(_orientations(tuple(cycle)))


def exact_D6_full_family_second_moment(s, source_line_cycles):
    """ALL-h mathematical formula for ANY explicitly supplied event family.

    Counting repeated cyclic line events is essential: DIFFERENT original Q
    can yield the very SAME event under global g; multiplicities are retained.
    The supplied family is COMPLETE iff caller supplied all eligible Q_f.
    Complexity O(u^2*144) canonical work, u distinct source-line cycles;
    gluing/color kernels memoized by relative tau.
    """
    V, a, K, missing = _params(s)
    if source_line_cycles is None:
        raise ValueError("explicit actual-original source-line cycles required")
    counts = Counter(canonical_single_original_line_cycle(c)
                     for c in source_line_cycles)
    n = sum(counts.values())
    p = Fraction(perm(a, 6), perm(K, 6))
    if n == 0:
        return {
            "s": s, "a": a, "K": K, "N_original_Q_events": 0,
            "N_distinct_source_line_cycle_events": 0,
            "single_event_probability": str(p),
            "E_D6": "0", "E_D6_squared": "0",
            "Var_D6": "0", "Paley_Zygmund_P_D6_positive_lower": "0",
            "ordered_pair_overlap_counts": {i: 0 for i in range(7)},
            "zero_joint_ordered_event_pairs": 0,
            "pair_gluing_types": 0,
            "global_minimax_six_motif_PROVED": False,
        }

    events = sorted(counts)
    by_gluing = Counter()
    overlap = Counter()
    for i, first in enumerate(events):
        for j in range(i, len(events)):
            second = events[j]
            factor = counts[first] * counts[second] * (1 if i == j else 2)
            gluing = canonical_two_source_C6_gluing(first, second)
            by_gluing[gluing] += factor
            overlap[sum(x < 6 for x in gluing)] += factor

    if sum(overlap.values()) != n*n:
        raise AssertionError("every ORDERED pair of genuine events must be counted")
    second = Fraction()
    zero = 0
    for tau, multiplicity in by_gluing.items():
        joint = Fraction(exact_two_D6_gluing_kernel(
            s, tuple(range(6)), tau)["joint_probability_one_complete_GLOBAL_g"])
        second += multiplicity*joint
        if joint == 0:
            zero += multiplicity
    expectation = n*p
    variance = second-expectation*expectation
    if variance < 0 or second < expectation*expectation:
        raise AssertionError("negative exact variance: pair kernel/model bug")
    positive = expectation*expectation/second  # exact Cauchy/Paley-Zygmund
    if not 0 < positive <= 1:
        raise AssertionError("invalid exact positive-probability lower bound")
    return {
        "s": s, "a": a, "K": K,
        "N_original_Q_events": n,
        "N_distinct_source_line_cycle_events": len(events),
        "single_event_probability": str(p),
        "E_D6": str(expectation),
        "E_D6_squared": str(second),
        "Var_D6": str(variance),
        "Paley_Zygmund_P_D6_positive_lower": str(positive),
        "ordered_pair_overlap_counts": {i: overlap[i] for i in range(7)},
        "zero_joint_ordered_event_pairs": zero,
        "pair_gluing_types": len(by_gluing),
        "same_ONE_uniform_complete_global_g": True,
        "all_original_source_line_overlaps_r0_to_r6_included": True,
        "complete_21000_plus_W32_family_not_claimed_unless_provided": True,
        "full_original_W32_pair_census_CI_verified": False,
        "global_minimax_six_motif_PROVED": False,
        "root_230": "OPEN_WITH_FORMAL_BLOCKER",
    }


def true_original_W32_subfamily_exact_moment(scheme, count=8):
    """Real W32 proof-fixture, independent of model labels on the right.

    Bounded regression subfamily; call the full function with ALL 21186
    true Q to obtain the full W32 answer (expensive; NOT done by CI).
    """
    if type(count) is not int or count < 1:
        raise ValueError("positive integer original Q subfamily count required")
    model, all_q = genuine_W32_fixed_f_original_connected_left_Q(scheme)
    selected = tuple(sorted(all_q)[:count])
    if len(selected) != count:
        raise ValueError("requested more real source Q than available")
    cycles = [_actual_original_Q_line_cycle(model, q) for q in selected]
    answer = exact_D6_full_family_second_moment(2, cycles)
    answer["scheme"] = scheme
    answer["actual_original_six_incidence_IDs"] = selected
    answer["subfamily_Q_count_not_full_W32"] = count
    answer["full_W32_left_C6_candidate_count_from_parent"] = len(all_q)
    if len(all_q) != 21186:
        raise AssertionError("authentic original W32 source enumeration drift")
    return answer


if __name__ == "__main__":
    import argparse
    import json
    parser = argparse.ArgumentParser()
    parser.add_argument("--scheme", choices=("S68", "S72"), default="S68")
    parser.add_argument("--count", type=int, default=8)
    args = parser.parse_args()
    print(json.dumps(true_original_W32_subfamily_exact_moment(
        args.scheme, args.count), sort_keys=True, indent=2))
