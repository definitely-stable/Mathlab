"""AA4-BX: weighted TWO historical original source POINT-C GF5 classes cubic.

Original symplectic W(3,2^h), h>=1, arbitrary fully fixed, globally
injected, potentially correlated physical pair-labeling f and g.
Fix six DISJOINT genuine original LINE source factor-image swap pairs.
On all 64 full globally injected right-map states simultaneously:

    W_C = 43320 S_C/A + 49050 S_C/B
    ||W_C - WalshProjection_<=3 W_C||_infinity <= E_s = O(s^5)=o(s^6).

This COMBINES the GQ fourth C/A source-point anchor bound proved
independently in sibling #595, genuine fourth C/B source line-transversal
bound #594, genuine fifth C/A/C/B #593, and genuine sixth C/A and C/B
#591. Unlike prior #596 (C/B ONLY), it covers BOTH weighted source
POINT C classes and gives a true f-only support refinement at W32.

The 4th weighted POINT C signed coefficient can take OPPOSITE signs
on authentic W32 lex and S72 under the SAME six LINE swap packets.
No universal positivity on ORIGINAL UNCHANGED f,g follows.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import _params
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    validate_disjoint_factor_swaps,apply_disjoint_factor_swaps,
)
from hyp105_issue230_d6aa4br_all_seven_signed_source_flux import (
    immutable_original_sixflag_class,
)
from hyp105_issue230_d6aa4bw_CB_sixcube_lowdegree_rigidity import (
    original_CB_sixcube_uniform_certificate,
    original_CB_sixcube_fixed_f_source_tail,
    _fwt_integer,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS,classify_seven_prechecked,
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six


def weighted_POINT_C_all_h_certificate(s):
    """Source W3 analytical fixed-label theorem, NOT simulated high-h."""
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("requires genuine symplectic W(3,2^h), h>=1")
    V,a,_,_=_params(s)
    if V<12:raise ValueError("need twelve distinct genuine source LINE factors")
    d=s+1
    # Sibling #595: four authentic source LINE packets, mark 4
    # genuine flag anchors, true source point profile 2+1+1 or 2+2.
    source_CA4=96*d*d*(d-1)**2 + 48*(V-2)*comb(d,2)
    # Parent #593 GQ: fifth 5 singleton anchors in point source C/A.
    source_CA5=480*d*(d-1)
    # Parent #591: sixth 3 true paired source-point intersections.
    source_CA6=960
    cb=original_CB_sixcube_uniform_certificate(s)
    CA_error=Fraction(15*source_CA4+6*source_CA5+source_CA6,2)
    CB_error=cb["all_h_uniform_degree_gt3_absolute_remainder_cap"]
    w_CA=R3_CERTIFIED_FLOORS["C/A"]
    w_CB=R3_CERTIFIED_FLOORS["C/B"]
    if (w_CA,w_CB)!=(43320,49050):
        raise AssertionError("original accepted necessary 51-column GF5 risk weights drifted")
    E=w_CA*CA_error+w_CB*CB_error
    return {
        "s":s,"h":s.bit_length()-1,"V":V,"a":a,"d":d,
        "genuine_original_LINE_source_packet_pairs":6,
        "FULL_globally_injected_right_map_cube_vertices":64,
        "historical_selected_weight_C_A":w_CA,
        "historical_selected_weight_C_B":w_CB,
        "SOURCE_point_C_original_class_C_A_fourth_upper":source_CA4,
        "SOURCE_point_C_original_class_C_A_fifth_upper":source_CA5,
        "SOURCE_point_C_original_class_C_A_sixth_upper":source_CA6,
        "SOURCE_point_C_original_class_C_B_fourth_upper":
            cb["max_fourth_true_original_C_B_sixflag_source_cap"],
        "SOURCE_point_C_original_class_C_B_fifth_upper":960,
        "SOURCE_point_C_original_class_C_B_sixth_upper":0,
        "uniform_CA_cubic_remainder":CA_error,
        "uniform_CB_cubic_remainder":CB_error,
        "uniform_WEIGHTED_point_C_cubic_remainder":E,
        "normalized_by_s6_exact":E/Fraction(s**6),
        "weighted_C_cubic_remainder_o_s6_proved_by_degree5":True,
        "weight_combination_is_NOT_all_seven_classes":True,
        "unchanged_original_full_f_g_positive_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def _sixcube_original_CA_source_geometry_W32(model,packets,all_left_six_Q):
    """FINITE true W32 fixed-f physically eligible C/A original Q counts.

    This is a deliberately separate, simple 62370-flag census, not the
    sibling #595 four-packet true GQ anchor enumerator (which works for
    W32/W34), used only for independent finite original corroboration.
    Never infer large-h physical H4/H5/H6 counts from this W32 scan.
    """
    s,V,a,inc,f,g,_,_=_original_source(model)
    if (s,V,a)!=(2,15,6):raise ValueError("actual original W32 only")
    p=validate_disjoint_factor_swaps(V,packets)
    if len(p)!=6:raise ValueError("six source LINE swap packets required")
    Qs=tuple(Q for Q in all_left_six_Q
             if immutable_original_sixflag_class(Q,inc)=="C/A")
    lines=[frozenset(inc[j][1] for j in Q) for Q in Qs]
    H4={};H5={};H6={}
    for n,dest in ((4,H4),(5,H5),(6,H6)):
        for T in combinations(range(6),n):
            dest[T]=sum(all(not ls.isdisjoint(p[i]) for i in T)
                        for ls in lines)
    error=Fraction(sum(H4.values())+sum(H5.values())+sum(H6.values()),2)
    return {
        "finite_true_original_W32_physical_LEFT_C_A_sixflag_sets":len(Qs),
        "four_packet_true_source_C_A_physical_f_counts":H4,
        "five_packet_true_source_C_A_physical_f_counts":H5,
        "six_packet_true_source_C_A_physical_f_counts":H6,
        "g_INDEPENDENT_refined_original_W32_C_A_cubic_error":error,
        "true_W32_only_not_fabricated_higher_GQ":True,
    }


def historical_W32_POINT_C_two_class_sixcube(model,packets):
    """C/A+C/B original fixed-pair 64-map real GF5 and signed Walsh cube."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("historical SIXTY-FOUR full original maps W32 only")
    pairs=validate_disjoint_factor_swaps(V,packets)
    if len(pairs)!=6:raise ValueError("need six disjoint genuine source LINE pairs")
    universe=tuple(Q for Q,_ in selected_left_six(model))
    classes=tuple((Q,immutable_original_sixflag_class(Q,inc))
                  for Q in universe)
    Qs={c:tuple(Q for Q,k in classes if k==c) for c in ("C/A","C/B")}
    weights={c:R3_CERTIFIED_FLOORS[c] for c in Qs}
    counts={c:[] for c in Qs}
    for mask in range(64):
        right=apply_disjoint_factor_swaps(g,pairs,tuple(
            j for j in range(6) if mask>>j&1))
        for c,original_Qs in Qs.items():
            counts[c].append(sum(classify_seven_prechecked(Q,f,right,inc)==c
                                 for Q in original_Qs))
    coeffs={c:tuple(Fraction(v,64)
                    for v in _fwt_integer(counts[c])) for c in Qs}
    total=tuple(sum(weights[c]*counts[c][x] for c in Qs) for x in range(64))
    weighted_hat={k:Fraction(v,64) for k,v in
                  enumerate(_fwt_integer(total))}
    # Exact orthogonal projection of the SAME weighted source-class
    # historical gf5 score, not a fitted sample polynomial.
    projection=tuple(sum(
        (-1 if (x&T).bit_count()%2 else 1)*weighted_hat[T]
        for T in range(64) if T.bit_count()<=3) for x in range(64))
    residual=tuple(Fraction(total[x])-projection[x] for x in range(64))
    CA_geometry=_sixcube_original_CA_source_geometry_W32(
        model,pairs,universe)
    CB_geometry=original_CB_sixcube_fixed_f_source_tail(model,pairs)
    f_error=(weights["C/A"]*CA_geometry[
        "g_INDEPENDENT_refined_original_W32_C_A_cubic_error"]+
             weights["C/B"]*CB_geometry[
        "fixed_f_uniform_all_64_complete_g_SWAP_maps_tail_cap"])
    bound=weighted_POINT_C_all_h_certificate(s)
    if not f_error<=bound["uniform_WEIGHTED_point_C_cubic_remainder"]:
        raise AssertionError("g-independent original weighted point C refinement exceeds all-h")
    for x in range(64):
        if abs(residual[x])>f_error:
            raise AssertionError("all-original historical two-class weighted cubic remainder")
    for T in range(64):
        n=T.bit_count()
        if weighted_hat[T]!=sum(weights[c]*coeffs[c][T] for c in Qs):
            raise AssertionError("true-original weighted C source Walsh nonlinearity bug")
        if n==6 and coeffs["C/B"][T]!=0:
            raise AssertionError("six packet right original LINE B class cannot contribute")
        if n>=4:
            ids=tuple(i for i in range(6) if T>>i&1)
            CA_count=(CA_geometry[
                {4:"four_packet_true_source_C_A_physical_f_counts",
                 5:"five_packet_true_source_C_A_physical_f_counts",
                 6:"six_packet_true_source_C_A_physical_f_counts"}[n]][ids])
            CB_count=(CB_geometry[
                {4:"fourth_source_C_B_left_physical_eligible_by_T",
                 5:"fifth_source_C_B_left_physical_eligible_by_T"}[n]][ids]
                      if n<6 else 0)
            if abs(coeffs["C/A"][T])>Fraction(CA_count,2):
                raise AssertionError("physical f-only CA Fourier certificate")
            if abs(coeffs["C/B"][T])>Fraction(CB_count,2):
                raise AssertionError("physical f-only CB Fourier certificate")
    return {
        "s":s,"V":V,"a":a,
        "original_SOURCE_incidence_flags_are_same_across_all_64_maps":True,
        "64_globally_injected_original_right_maps":64,
        "historical_GF5_C_A_and_C_B_counts":{c:tuple(v) for c,v in counts.items()},
        "original_selected_necessary_GF5_weighted_POINT_C_values":total,
        "exact_original_class_Walsh":coeffs,
        "exact_original_WEIGHTED_point_C_Walsh":weighted_hat,
        "exact_degree3_weighted_projection":projection,
        "exact_weighted_point_C_high_order_tail":residual,
        "max_actual_weighted_tail":max(abs(x) for x in residual),
        "initial_unchanged_weighted_POINT_C_score":total[0],
        "original_POINT_C_WEIGHTED_zero_mode":weighted_hat[0],
        "four_packet_point_C_weighted_signed_coefficient":weighted_hat[15],
        "given_original_f_source_only_CA":CA_geometry,
        "given_original_f_source_only_CB":CB_geometry,
        "g_independent_original_f_refined_WEIGHTED_error":f_error,
        "all_h_uniform_WEIGHTED_point_C_error":
            bound["uniform_WEIGHTED_point_C_cubic_remainder"],
        "no_original_center_positive_lower_from_this":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
