"""C24-B8-B: 2 exact TRUE original W32 signed physical fiber reports.

Dedicated GitHub-hosted contract only. No full B7 11236-cell repeat.
The 2 left-swap source populations are enumerated independently and UNIONED.
"""
from itertools import combinations
from collections import Counter
import json

from hyp105_g5e2b3e1c24_right_c_certificate import original_W32
from hyp105_g5e2b3e1c24b_three_collision import W32_LEFT_H45
from hyp105_g5e2b3e1c24b6_mixed_curvature_s68 import W32_RIGHT_S68
from hyp105_g5e2b3e1c24b2_joint_seven import (
    compile_left, full_left_score, right_first_independent,
)
from hyp105_g5e2b3e1c24b3_joint_swap_gradient import legal_transpose
from hyp105_g5e2b3e1c24b7_cross_side_orbit import (
    all_h_original_gq_cross_touch_bound, original_w32_point_line_cross_overlap,
)
from hyp105_g5e2b3e1c24b8a_w32_tensor_witness import (
    independently_enumerate_left_original_sixsets, permutation_to_edges,
)
from hyp105_g5e2b3e1c24b8b_signed_physical_balance import (
    exact_signed_fiber_census, swap_orientation_sign_identity,
    original_source_annealed_probability,
)


def signed_true_W32_rectangle(left_swap,right_swap,frozen_four,frozen_kappa):
    f0,g0=tuple(W32_LEFT_H45),tuple(W32_RIGHT_S68)
    fa=legal_transpose(f0,*left_swap)
    gb=legal_transpose(g0,*right_swap)
    sources0=independently_enumerate_left_original_sixsets(f0)
    sources1=independently_enumerate_left_original_sixsets(fa)
    union=sources0 | sources1
    if (len(sources0)!=62370 or len(sources1)!=62370 or
            len(union)!=98982 or len(sources1-sources0)!=36612):
        raise AssertionError("two authentic differently compiled W32 original sources required")
    mappings=(permutation_to_edges(f0,left=True),permutation_to_edges(fa,left=True),
              permutation_to_edges(g0,left=False),permutation_to_edges(gb,left=False))
    signed=exact_signed_fiber_census(union,*mappings)
    expected=(
        full_left_score(compile_left(f0),g0)["S_seven"],
        full_left_score(compile_left(fa),g0)["S_seven"],
        full_left_score(compile_left(f0),gb)["S_seven"],
        full_left_score(compile_left(fa),gb)["S_seven"],
    )
    if (signed["four_scores"]!=expected or expected!=frozen_four or
            signed["kappa"]!=frozen_kappa):
        raise AssertionError("signed matched physical fibers mismatch independent B2 source")
    separate=right_first_independent(fa,gb)
    if separate["S_seven"]!=expected[3]:
        raise AssertionError("independent original RIGHT-FIRST result disagrees")
    flip=swap_orientation_sign_identity(f0,fa,g0,gb,expected)
    _,lines,_=original_W32()
    overlap=original_w32_point_line_cross_overlap(left_swap,right_swap,lines)
    raw_cap=all_h_original_gq_cross_touch_bound(2,overlap)["absolute_signed_cross_curvature_upper"]
    if not (abs(frozen_kappa)<=signed["exact_signed_absolute_bound"]<=
            signed["physical_change_cap"]<=raw_cap):
        raise AssertionError("sourcewise signed cancellation / exposure hierarchy violation")
    # Exact global coherent move criterion: single-side costs + mixed change.
    left_delta,right_delta=expected[1]-expected[0],expected[2]-expected[0]
    signed_descent_surplus=(signed["negative_matched"]-signed["positive_matched"]
                            -left_delta-right_delta)
    if signed_descent_surplus != expected[0]-expected[3]:
        raise AssertionError("mixed signed escape threshold not exact")
    # In this known B7 local optimum neither typed rectangle improves S68.
    if signed_descent_surplus>=0:
        raise AssertionError("W32 witness contradicts strict typed local minimum")
    return {
        "left_swap":left_swap, "right_swap":right_swap,
        "source_union":len(union),"new_original_sixsets_after_left_swap":len(sources1-sources0),
        "four_complete_map_scores":expected,
        "signed_curvature":signed["kappa"],
        "signed_positive_matched":signed["positive_matched"],
        "signed_negative_matched":signed["negative_matched"],
        "signed_cancellation":signed["net_cancellation"],
        "exact_matched_absolute_bound":signed["absolute_matched"],
        "actual_physical_change_cap":signed["physical_change_cap"],
        "B7_unrestricted_source_touch_bound":raw_cap,
        "separate_original_seven_tag_signed_breakdown":signed["by_tag"],
        "single_left_score_increase":left_delta,
        "single_right_score_increase":right_delta,
        "descent_surplus_after_sign_balanced_curvature":signed_descent_surplus,
        "left_right_sign_orientation_involution": {
            "left_reversed":flip["left_reversed"],
            "right_reversed":flip["right_reversed"],
            "both_reversed":flip["both_reversed"]},
        "independent_left_and_RIGHT_FIRST_oracles_agree":True,
        "no_all_h_positive_lower_or_production_claim":True,
    }


def report():
    x=signed_true_W32_rectangle((3,8),(0,14),(68,95,97,70),-54)
    y=signed_true_W32_rectangle((4,14),(4,11),(68,107,127,96),-70)
    # The exact random injection mean is an independent all-h formula,
    # NOT an estimate from these two optimized particular global maps.
    _,lines,_=original_W32()
    source=tuple((p,l) for l,line in enumerate(lines) for p in line)
    one=tuple(sorted(source)[:6])
    return {"slice":"HYP-105-C24-B8-B",
            "signed_w32_first":x,"signed_w32_second":y,
            "one_fixed_original_source_uniform_mean":str(
                original_source_annealed_probability(one,6)),
            "status":"RESTRICTED_EXACT_SIGNED_IDENTITIES_AND_FINITE_W32_ORACLES",
            "root_230_open":True}


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
