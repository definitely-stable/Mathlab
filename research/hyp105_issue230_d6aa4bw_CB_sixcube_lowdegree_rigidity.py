"""AA4-BW: uniform original GQ C/B degree-3 approximation on SIX swaps.

True original W(3,2^h), h>=1, SAME six distinct source incidence IDs
on both sides, ANY globally injected and arbitrarily correlated full
typed physical source point f and LINE g factor edge maps.

For six disjoint complete ORIGINAL LINE image-swap packets, all 64
full global map states share occupied right support. C/B score F(x)
has Fourier-Walsh degree <=5 and its degree>=4 tail is pointwise bounded
for every x by
    E_s=15/2*[960+96d+192(2d-1)(d-1)] + 6*480.
More sharply:  E_f = 1/2 * sum_{|T|=4} H4(f,T)
                       + 1/2 * sum_{|T|=5} H5(f,T),
where H4/H5 count actual source-C/B sixflag Q touching every selected
packet with three pairwise physically disjoint original POINT images.
Both bounds are independent of g and hold at every Boolean vertex.

This is an O(s^2) uniform remainder, versus natural s^6 scale.
It does NOT imply S_original(f,g)>=cs^6; no root Branch A/B/C.
"""
from fractions import Fraction
from itertools import combinations
from math import comb
from collections import Counter

from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import _params
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bv_fourth_GQ_CB_transversals import (
    fourth_GQ_C_B_source_certificate,
    fourth_original_C_B_true_GQ_geometry,
)
from hyp105_issue230_d6aa4bu_fifth_order_GQ_C_profiles import (
    fifth_order_original_GQ_C_certificate,
    original_five_packet_C_B_geometry,
)
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    validate_disjoint_factor_swaps,apply_disjoint_factor_swaps,
)
from hyp105_issue230_d6aa4br_all_seven_signed_source_flux import (
    immutable_original_sixflag_class,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    classify_seven_prechecked,
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six


def original_CB_sixcube_uniform_certificate(s):
    """Fully analytic all-h, including W32, no fake high-h source graph."""
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("original genuine symplectic GQ order s=2^h, h>=1 required")
    V,a,_,_=_params(s)
    if V<12:raise ValueError("six disjoint whole original LINE factor image swaps need 12")
    d=s+1
    four=fourth_GQ_C_B_source_certificate(s)
    five=fifth_order_original_GQ_C_certificate(s)
    c4=four["max_fourth_source_C_B_original_Q"]
    c5=five["max_actual_original_C_B_Q_touching_ALL_five_packets"]
    if c5!=960 or c4!=960+96*d+192*(2*d-1)*(d-1):
        raise AssertionError("exact pinned GQ original C/B order4/5 source hierarchy")
    error=Fraction(comb(6,4)*c4+comb(6,5)*c5,2)
    return {
        "s":s,"h":s.bit_length()-1,"a":a,"V":V,"d":d,
        "number_original_LINE_image_swap_packets":6,
        "number_GLOBALLY_injected_complete_map_cube_vertices":64,
        "max_fourth_true_original_C_B_sixflag_source_cap":c4,
        "max_fifth_true_original_C_B_sixflag_source_cap":c5,
        "number_fourth_packet_subsets":comb(6,4),
        "number_fifth_packet_subsets":comb(6,5),
        "original_C_B_sixth_order_Walsh_exactly_zero":True,
        "all_h_uniform_degree_gt3_absolute_remainder_cap":error,
        "degree3_original_CB_polynomial_approximates_EVERY_64_vertex":True,
        "relative_to_six_scale_exact":error/Fraction(s**6),
        "uniform_o_s6_analytic_since_degree2_in_s":True,
        "source_GQ_GIVEN_f_refinement_from_PHYSICAL_C_profile":True,
        "S_original_UNMODIFIED_positive_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def original_CB_sixcube_fixed_f_source_tail(model,packets):
    """Computable true-original geometry+unchanged-f remainder upper.

    Deliberately independent of right g (except strict input geometry
    validation), every genuine SIX-SOURCE-ID Q counted only ONCE.
    The physical f-image of three source POINTs must be pairwise
    disjoint: necessary for historical original left C.
    """
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    p=validate_disjoint_factor_swaps(V,packets)
    if len(p)!=6:
        raise ValueError("six DISJOINT ORIGINAL source LINE packets expected")
    summed4=0;summed5=0
    counts4={};counts5={}
    for ids in combinations(range(6),4):
        H=fourth_original_C_B_true_GQ_geometry(model,tuple(p[i] for i in ids))
        n=H["physically_LEFT_C_eligible_count"]
        counts4[ids]=n
        summed4+=n
    for ids in combinations(range(6),5):
        H=original_five_packet_C_B_geometry(model,tuple(p[i] for i in ids))
        n=H["number_FIXED_LEFT_physical_eligible_C_B"]
        counts5[ids]=n
        summed5+=n
    exact=Fraction(summed4+summed5,2)
    cap=original_CB_sixcube_uniform_certificate(s)[
        "all_h_uniform_degree_gt3_absolute_remainder_cap"]
    if exact>cap:
        raise AssertionError("fixed genuine source f-refined Walsh tail greater than analytic all-h cap")
    return {
        "s":s,"a":a,"original_six_source_LINE_packets":p,
        "fourth_source_C_B_left_physical_eligible_by_T":counts4,
        "fifth_source_C_B_left_physical_eligible_by_T":counts5,
        "sum_eligible_fourth_true_source_sixQ":summed4,
        "sum_eligible_fifth_true_source_sixQ":summed5,
        "fixed_f_uniform_all_64_complete_g_SWAP_maps_tail_cap":exact,
        "all_h_universal_tail_cap":cap,
        "independent_of_original_g_ASSIGNMENT":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def _fwt_integer(values):
    """Unnormalized classic Walsh Hadamard transformation, exact ints."""
    z=list(values)
    n=len(z)
    if n<=0 or n&(n-1):
        raise ValueError("non-empty two-power cube length required")
    stride=1
    while stride<n:
        for i in range(0,n,2*stride):
            for j in range(stride):
                u=z[i+j];v=z[i+j+stride]
                z[i+j]=u+v;z[i+j+stride]=u-v
        stride*=2
    return tuple(z)


def original_true_W32_CB_sixcube_polynomial(model,packets):
    """Actual W32: enumerate SIXTY-FOUR complete globally injected maps.

    Use each SAME genuine original six-incidence Q on the same source.
    All class values are exact historical positive GF5 right B counts.
    """
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("finite all-64 global source C/B historical W32 oracle only")
    p=validate_disjoint_factor_swaps(V,packets)
    if len(p)!=6:
        raise ValueError("exactly six disjoint original LINE source swaps")
    # Crucially f is unchanged for ALL vertices; each actual source Q
    # and its POINT/LINE original IDs are unchanged at each vertex.
    Qs=tuple(Q for Q,_ in selected_left_six(model)
             if immutable_original_sixflag_class(Q,inc)=="C/B")
    states=tuple(apply_disjoint_factor_swaps(g,p,tuple(
        i for i in range(6) if mask>>i&1)) for mask in range(64))
    values=[]
    for line_images in states:
        values.append(sum(1 for Q in Qs if
            classify_seven_prechecked(Q,f,line_images,inc)=="C/B"))
    numerators=_fwt_integer(values)
    hat={mask:Fraction(v,64) for mask,v in enumerate(numerators)}
    low=tuple(sum(((-1 if (mask&index).bit_count()%2 else 1)*
                    hat[index]) for index in range(64)
                  if index.bit_count()<=3)
              for mask in range(64))
    residual=tuple(Fraction(values[mask])-low[mask] for mask in range(64))
    source=original_CB_sixcube_fixed_f_source_tail(model,p)
    allh=original_CB_sixcube_uniform_certificate(s)
    for i,numerator in enumerate(numerators):
        degree=i.bit_count()
        if degree==6 and numerator!=0:
            raise AssertionError("genuine source LINE type B only five distinct factors")
        if degree==4 and abs(hat[i])>Fraction(
              source["fourth_source_C_B_left_physical_eligible_by_T"][
                tuple(j for j in range(6) if i>>j&1)],2):
            raise AssertionError("genuine GQ fourth C/B fixed-f Fourier support exceeded")
        if degree==5 and abs(hat[i])>Fraction(
              source["fifth_source_C_B_left_physical_eligible_by_T"][
                tuple(j for j in range(6) if i>>j&1)],2):
            raise AssertionError("genuine GQ fifth C/B fixed-f Fourier support exceeded")
    if max(abs(v) for v in residual)>source[
        "fixed_f_uniform_all_64_complete_g_SWAP_maps_tail_cap"]:
        raise AssertionError("six-cube original C/B degree3 source-f error")
    if max(abs(v) for v in residual)>allh[
        "all_h_uniform_degree_gt3_absolute_remainder_cap"]:
        raise AssertionError("original C/B all-h error")
    return {
        "s":s,"V":V,"a":a,"six_source_LINE_packets":p,
        "64_complete_GLOBAL_original_LINE_maps_on_same_support":64,
        "original_six_source_incidence_C_B_left_eligible_sets":len(Qs),
        "historical_C_B_acceptance_at_each_complete_map":tuple(values),
        "exact_fourier_coefficients":hat,
        "exact_degree3_projection_at_all_complete_maps":low,
        "exact_degree4_and_5_tail_at_all_complete_maps":residual,
        "max_actual_tail_absolute":max(abs(v) for v in residual),
        "source_geometry_fixed_f_certificate":source,
        "all_h_uniform_source_bound":allh[
            "all_h_uniform_degree_gt3_absolute_remainder_cap"],
        "zero_mode_original_C_B_average":hat[0],
        "unchanged_initial_original_C_B_score":values[0],
        "unchanged_map_SEVEN_class_positive_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
