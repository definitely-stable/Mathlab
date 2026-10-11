"""C24-B8-A: explicit genuine W(3,2) independent four-map tensor witness.

Explicit hosted Contract only: DOES NOT run in default unittest discovery.
Enumerates the UNION of newly LEFT-eligible ORIGINAL sixsets under f and f^A.
No full 11236-cell orbit or new scientific lower-bound claim.
"""
from collections import Counter
from itertools import combinations, combinations_with_replacement, product
import json

from hyp105_g5e2b3e1c24_right_c_certificate import K6_PAIRS, original_W32
from hyp105_g5e2b3e1c24b_three_collision import W32_LEFT_H45
from hyp105_g5e2b3e1c24b6_mixed_curvature_s68 import W32_RIGHT_S68
from hyp105_g5e2b3e1c24b2_joint_seven import (
    compile_left, full_left_score, right_first_independent, full_permutation,
)
from hyp105_g5e2b3e1c24b3_joint_swap_gradient import legal_transpose
from hyp105_g5e2b3e1c24b7_cross_side_orbit import (
    all_h_original_gq_cross_touch_bound, original_w32_point_line_cross_overlap,
)
from hyp105_g5e2b3e1c24b8a_physical_tensor import audit_rectangle


def independently_enumerate_left_original_sixsets(f):
    """Independent physical K6 2-factor -> original distinct GQ sixset path.

    No use of B2 compressed source, B5 pullback fibers, or B7 result cache.
    """
    f = full_permutation(f)
    _, lines, _ = original_W32()
    inv = {edge: idx+1 for idx, edge in enumerate(f)}
    by_point = {p:tuple(l for l,line in enumerate(lines) if p in line)
                for p in range(1,16)}
    if len(inv) != 15 or any(len(x) != 3 for x in by_point.values()):
        raise AssertionError("invalid original W(3,2) incidence or left global injection")
    seen = set()
    template_count = 0
    for edges in combinations_with_replacement(range(15),6):
        degrees = Counter(v for edge in edges for v in K6_PAIRS[edge])
        if len(degrees) != 6 or any(d != 2 for d in degrees.values()):
            continue
        template_count += 1
        groups = tuple(sorted((inv[e], mult) for e,mult in Counter(edges).items()))
        for picked in product(*(combinations(by_point[p], n) for p,n in groups)):
            six = tuple(sorted((p,l) for (p,_),ls in zip(groups,picked) for l in ls))
            if six in seen:
                raise AssertionError("duplicate original sixset")
            seen.add(six)
    if template_count != 130 or len(seen) != 62370:
        raise AssertionError("wrong independent K6 physical 2-factor or true-GQ sixset count")
    return seen


def permutation_to_edges(f, *, left):
    return {(i+1 if left else i):K6_PAIRS[k] for i,k in enumerate(f)}


def report_one_typed_rectangle(a,b,expected,*,right_first):
    f0, g0 = full_permutation(W32_LEFT_H45), full_permutation(W32_RIGHT_S68)
    fa, gb = legal_transpose(f0,*a), legal_transpose(g0,*b)
    # Two separate physical original-source enumerations; NEVER reuse the
    # f0-only set after a left point swap. Contains all potential contributors.
    source0 = independently_enumerate_left_original_sixsets(f0)
    sourcea = independently_enumerate_left_original_sixsets(fa)
    union = source0 | sourcea
    if len(source0) != 62370 or len(sourcea) != 62370:
        raise AssertionError("unrecompiled original source")
    maps = (permutation_to_edges(f0,left=True),permutation_to_edges(fa,left=True),
            permutation_to_edges(g0,left=False),permutation_to_edges(gb,left=False))
    tensor = audit_rectangle(union,*maps)
    legacy = (
        full_left_score(compile_left(f0),g0)["S_seven"],
        full_left_score(compile_left(fa),g0)["S_seven"],
        full_left_score(compile_left(f0),gb)["S_seven"],
        full_left_score(compile_left(fa),gb)["S_seven"],
    )
    exact = tuple(tensor[k] for k in ("S_00","S_10","S_01","S_11"))
    if exact != legacy or tensor["mixed_curvature"] != expected:
        raise AssertionError("original W32 independent tensor vs left-first witness differs")
    if right_first:
        separate = right_first_independent(fa,gb)
        if separate["S_seven"] != tensor["S_11"]:
            raise AssertionError("independent original RIGHT-FIRST sixset witness differs")
    _, lines, _ = original_W32()
    cross = original_w32_point_line_cross_overlap(a,b,lines)
    cap_old = all_h_original_gq_cross_touch_bound(2,cross)["absolute_signed_cross_curvature_upper"]
    if tensor["sharp_sourcewise_physical_cap"] > cap_old:
        raise AssertionError("physical jointly changing bound worse than unrestricted universe")
    return {"left_swap":a,"right_swap":b, "old_f_left_candidates":len(source0),
            "new_f_left_candidates":len(sourcea),
            "common_universe_union":len(union),
            "distinct_candidates_newly_introduced_by_left_swap":len(sourcea-source0),
            "four_scores":exact, "mixed":tensor["mixed_curvature"],
            "signed_by_seven_tag":tensor["mixed_by_tag"],
            "physical_joint_cap":tensor["sharp_sourcewise_physical_cap"],
            "unrestricted_original_joint_touch_cap":cap_old,
            "independent_legacy_four_scores_equal":True,
            "independent_right_first":right_first,
            "exact_all_h_identity_instance_only":True}


def report():
    # Frozen authentic B7 certified typed four-corner discrepancy.
    positive_first_gradients = report_one_typed_rectangle(
        (3,8),(0,14),-54,right_first=True)
    if positive_first_gradients["four_scores"] != (68,95,97,70):
        raise AssertionError("genuine B7 negative mixed source-rectangle drift")
    # The most negative typed curvature in the entire prior B7 rectangle.
    strongest_negative = report_one_typed_rectangle(
        (4,14),(4,11),-70,right_first=False)
    return {"slice":"HYP-105-C24-B8-A",
            "positive_first_gradients_but_negative_curvature":positive_first_gradients,
            "most_negative_previous_B7_curvature":strongest_negative,
            "proof_scope":"exact_all_h_boolean_cycle_tensor; finite_original_W32_oracles",
            "no_global_optimum_or_R3_or_ASET_bound":True}


if __name__ == "__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
