"""HYP-105 C16: true two-sided original GQ sixset coupling.

Restricted exact finite W(3,2)/K6 certificate. Unlike C14/C15, left
physical 2-factor membership is recomputed for EVERY genuine residual
left permutation: a canonical filler may never define a variable-left
witness universe. Sixsets absent for a full left map contribute ZERO.
No all-h obstruction, full R3 claim, or scalable full-permutation search.
"""
from collections import defaultdict
from itertools import permutations
from math import factorial

from hyp105_g5e2b3e1a_fixed_leading import PAIRS, selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, classify_seven_prechecked,
)
from hyp105_g5e2b3e1c14_domain_certificates import (
    _filled_model, _original_W32, _pins,
)


def two_sided_source_certificate(
        model, left_pins, right_pins, *,
        max_free_left=3, max_free_right=3,
        max_joint_maps=36, max_motif_evaluations=2500000):
    """Exact sound bounds on every common full original (f,g) descendant.

    For a fixed ORIGINAL six-incidence set J, define chi_J(f,g)=1 iff
    J is selected by the TRUE completed physical-left 2factor enumerator
    AND the accepted seven-family classifier succeeds on the SAME full
    right map. Otherwise chi_J=0. Let w_J be its nonnegative GF5 necessary
    numerator, zero when not selected. Each true full score equals the
    sum over distinct ORIGINAL J, not physical orbits or signed events.

    Partition by (Mleft(J), Mright(J)), the exact touched currently
    unpinned ORIGINAL points and lines. For EACH common full map, all
    groups contribute disjointly. Consequently:
      C15 shared-right eligible-left bound
      <= C16 base + sum_(Mleft nonempty,Mright) min_(f,g) group
      <= sum_Mleft min_(f,g) all groups with this Mleft
      <= min_f sum_Mleft min_g all groups with this Mleft
      <= min_(f,g) sum_J chi_J(f,g)
      <= S_seven(f,g) for EVERY legal descendant.
    The last min is EXACT within this bounded full completion box; it
    is not a scalable new asymptotic obstruction. All statements also
    hold for w_J separately; optimizing S and GF5 may yield DIFFERENT
    maps. Signature group minima need not share an attainable map.

    A sixset that ceases to be left-eligible under a specific completion
    contributes zero (never a false positive from a filler). All source
    sets over ALL left completions are used, with a hard total budget.
    The hierarchy is monotone under legal additional pins: completion
    domains shrink, projected signatures merge, and impossible sixsets
    contribute zero throughout the restricted domain.
    """
    f = _pins(left_pins, "C16 original left pins")
    g = _pins(right_pins, "C16 original right pins")
    _original_W32(model)
    budgets = (max_free_left, max_free_right, max_joint_maps,
               max_motif_evaluations)
    if any(type(v) is not int or v < 0 for v in budgets[:2]) or any(
            type(v) is not int or v < 1 for v in budgets[2:]):
        raise ValueError("invalid two-sided exact budgets")
    unknown_l = tuple(i for i in range(15) if i not in f)
    unknown_r = tuple(i for i in range(15) if i not in g)
    unused_l = tuple(i for i in range(15) if i not in f.values())
    unused_r = tuple(i for i in range(15) if i not in g.values())
    n_l, n_r = factorial(len(unknown_l)), factorial(len(unknown_r))
    n = n_l * n_r
    evaluations = 62370 * n
    if (len(unknown_l) > max_free_left
            or len(unknown_r) > max_free_right
            or n > max_joint_maps
            or evaluations > max_motif_evaluations):
        raise ValueError("two-sided exact source/census cap exceeded")
    left_tails = tuple(permutations(unused_l))
    right_tails = tuple(permutations(unused_r))
    if len(left_tails) != n_l or len(right_tails) != n_r:
        raise AssertionError("incomplete actual residual permutation domain")
    inc = model["incidences"]
    # No arbitrary fake source-to-physical edge action: these are genuine
    # completed ORIGINAL point/line -> occupied physical K6 pair-edge maps.
    rights = []
    for tail in right_tails:
        full_g = {**g, **dict(zip(unknown_r, tail))}
        rights.append(tuple(PAIRS[full_g[i]] for i in range(15)))
    cells = {}  # (named ORIGINAL missing-left, missing-right) -> [S[], GF5[]]
    original_union = set()
    eligible_by_left = []
    counts = [[0] * n, [0] * n]
    for l_index, left_tail in enumerate(left_tails):
        full_f = {**f, **dict(zip(unknown_l, left_tail))}
        full = _filled_model(model, full_f, g)
        left = full["left_labels"]
        seen = set()
        eligible = 0
        for six, _ in selected_left_six(full):
            if six in seen:
                raise AssertionError("duplicate ORIGINAL six-incidence set")
            seen.add(six)
            original_union.add(six)
            ml = tuple(sorted({inc[e][0] for e in six if inc[e][0] not in f}))
            mr = tuple(sorted({inc[e][1] for e in six if inc[e][1] not in g}))
            eligible += int(not ml)
            key = (ml, mr)
            if key not in cells:
                cells[key] = [[0] * n, [0] * n]
            bucket = cells[key]
            for r_index, right in enumerate(rights):
                j = l_index * n_r + r_index
                tag = classify_seven_prechecked(six, left, right, inc)
                if tag is not None:
                    bucket[0][j] += 1
                    weight = R3_CERTIFIED_FLOORS[tag]
                    bucket[1][j] += weight
                    counts[0][j] += 1
                    counts[1][j] += weight
        if len(seen) != 62370:
            raise AssertionError("incomplete left physical 2-factor census")
        eligible_by_left.append(eligible)
    if len(set(eligible_by_left)) != 1:
        raise AssertionError("all-left-pinned source depends on left filler")
    left_groups = {}
    base = [[0] * n, [0] * n]
    for (ml, mr), two_scores in cells.items():
        if ml not in left_groups:
            left_groups[ml] = [[0] * n, [0] * n]
        for q in (0, 1):
            target = left_groups[ml][q]
            for j, value in enumerate(two_scores[q]):
                target[j] += value
                if not ml:
                    base[q][j] += value
    if () not in left_groups:
        raise AssertionError("missing frozen-left source group")
    for q in (0, 1):
        for l in range(1, n_l):
            if base[q][l*n_r:(l+1)*n_r] != base[q][:n_r]:
                raise AssertionError("frozen-left contributions vary by left tail")
        if any(sum(group[q][j] for group in left_groups.values())
               != counts[q][j] for j in range(n)):
            raise AssertionError("disjoint signature grouping double counted")
    scores = []
    for q in (0, 1):
        c15 = min(base[q][:n_r])
        pair = c15 + sum(min(values[q]) for (ml, _), values in cells.items()
                         if ml)
        left_group = sum(min(values[q]) for values in left_groups.values())
        one_left = min(
            sum(min(values[q][l*n_r:(l+1)*n_r])
                for values in left_groups.values())
            for l in range(n_l))
        joint = min(counts[q])
        if not (0 <= c15 <= pair <= left_group <= one_left <= joint):
            raise AssertionError("invalid two-sided joint lower hierarchy")
        scores.append((c15, pair, left_group, one_left, joint))
    return {
        "scope": "TRUE_ORIGINAL_W32_FULL_K6_BOTH_SIDES",
        "actual_original_left_completions": n_l,
        "actual_original_right_completions": n_r,
        "actual_joint_completions": n,
        "all_source_templates_per_left_completion": 62370,
        "left_pinned_candidates_per_left_completion": eligible_by_left[0],
        "distinct_original_sixsets_in_union": len(original_union),
        "two_sided_original_signature_count": len(cells),
        "left_original_signature_count": len(left_groups),
        "actual_motif_classifications": evaluations,
        "C15_eligible_one_right_lower_S": scores[0][0],
        "C16_two_sided_signature_lower_S": scores[0][1],
        "C16_one_left_signature_group_lower_S": scores[0][2],
        "C16_shared_left_groupwise_right_lower_S": scores[0][3],
        "C16_exact_joint_box_lower_S": scores[0][4],
        "C15_eligible_one_right_lower_GF5_numerator": scores[1][0],
        "C16_two_sided_signature_lower_GF5_numerator": scores[1][1],
        "C16_one_left_signature_group_lower_GF5_numerator": scores[1][2],
        "C16_shared_left_groupwise_right_lower_GF5_numerator": scores[1][3],
        "C16_exact_joint_box_lower_GF5_numerator": scores[1][4],
        "S_by_every_actual_joint_completion": tuple(counts[0]),
        "GF5_by_every_actual_joint_completion": tuple(counts[1]),
        "not_full_GF5_R3_or_global_15_factorial_squared": True,
        "no_universal_all_h_lower_proved": True,
    }


def genuine_W32_C16_report():
    """One bounded 3!^2 true original GQ box, NOT a general search."""
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    from hyp105_g5e2b3e1c14_domain_certificates import (
        independent_exact_completion_audit,
    )
    m = pair_labeled_symplectic(1, "reverse-line")
    f = {i: PAIRS.index(m["left_labels"][i]) for i in range(12)}
    g = {i: PAIRS.index(m["right_labels"][i]) for i in range(12)}
    cert = two_sided_source_certificate(m, f, g)
    independent = independent_exact_completion_audit(
        m, f, g, max_full_maps=36)
    if (cert["C15_eligible_one_right_lower_S"] != 12
            or cert["C15_eligible_one_right_lower_GF5_numerator"] != 513393
            or cert["C16_exact_joint_box_lower_S"]
            != independent["true_minimum_S_seven_in_box"] != 148
            or cert["C16_exact_joint_box_lower_GF5_numerator"]
            != independent["true_minimum_GF5_floor_numerator_in_box"]
            != 6676842):
        raise AssertionError("C16 two-sided source differs from true W32 audit")
    return cert


if __name__ == "__main__":
    import json
    print(json.dumps(genuine_W32_C16_report(), indent=2, sort_keys=True))
