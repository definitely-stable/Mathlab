"""HYP-105 C24-B7: TRUE original W32 mixed LEFT/RIGHT global 105x105 orbit.

Crucial gate: a LEFT transposition changes the ORIGINAL left-eligible source
sixsets, including previously ineligible original J. Never reuse the frozen
f0 62,370-sixset source when computing f^A. Recompile from 130 physical
left templates for EACH complete left bijection f^A, then evaluate the
entire global right neighborhood on those new original sixsets.

For all s=2^h, the original unrestricted six-incidence universe is COMMON
to every f,g, permitting a correct two-sided mixed-indicator support lemma.
The resulting binomial support upper bound is deliberately marked nonsharp.
"""
from collections import Counter
from itertools import combinations
from math import comb

from hyp105_g5e2b3e1c24_right_c_certificate import original_W32
from hyp105_g5e2b3e1c24b_three_collision import W32_LEFT_H45
from hyp105_g5e2b3e1c24b2_joint_seven import (
    TAGS, GF5_WEIGHTS, compile_left, full_left_score, full_permutation,
    right_first_independent,
)
from hyp105_g5e2b3e1c24b3_joint_swap_gradient import legal_transpose
from hyp105_g5e2b3e1c24b5_two_swap_escape import (
    compile_right_pullback_fibers, template_pullback_score,
)
from hyp105_g5e2b3e1c24b6_mixed_curvature_s68 import (
    W32_RIGHT_S68, W32_S68_VECTOR,
)

# W32_LEFT_H45 is a single COMPLETE original-point-to-physical-K6-edge
# permutation, not per-sixset label remapping. Original points are 1..15,
# original lines are indexed 0..14.
PAIRS = tuple(combinations(range(15), 2))
assert len(PAIRS) == 105


def binom_or_zero(n, k):
    if type(n) is not int or type(k) is not int:
        raise ValueError("integer binomial arguments required")
    return comb(n, k) if 0 <= k <= n else 0


def exact_cross_touch_universe_count(E, left_degree, right_degree, overlap, k=6):
    """Exact number of k-subsets touching BOTH designated incidence sets.

    With U an ORIGINAL incidence-edge universe |U|=E, sets L,R each of
    cardinality left_degree/right_degree, |L ∩ R|=overlap, a fixed source
    J subset of U touches both iff J∩L !=∅ and J∩R !=∅. Inclusion-exclusion:

    M = C(E,k)-C(E-|L|,k)-C(E-|R|,k)
                       +C(E-|L|-|R|+overlap,k).

    Original sixset universe is independent of f,g. No assertion that the
    k-subsets counted here are physical 2-factor eligible or accepted GF5:
    this is a potentially very LOOSE absolute mixed-curvature upper.
    """
    if (any(type(x) is not int for x in
            (E, left_degree, right_degree, overlap, k))
            or E < 0 or k < 0 or not 0 <= left_degree <= E
            or not 0 <= right_degree <= E
            or not 0 <= overlap <= min(left_degree, right_degree)
            or left_degree + right_degree - overlap > E):
        raise ValueError("consistent original incidence-set parameters required")
    count = (binom_or_zero(E, k)
             - binom_or_zero(E-left_degree, k)
             - binom_or_zero(E-right_degree, k)
             + binom_or_zero(E-left_degree-right_degree+overlap, k))
    if count < 0 or count > binom_or_zero(E,k):
        raise AssertionError("inclusion-exclusion count out of bounds")
    return count


def all_h_original_gq_cross_touch_bound(s, overlap):
    """All-h source universe cross-support certificate, NOT positive S bound.

    W(3,s): V=(s+1)(s^2+1) points and lines; each has degree s+1,
    E=V(s+1) original incidence edges. Swapping TWO original points
    touches exactly d=2(s+1) incidence edges; swapping TWO original lines
    similarly touches d. Their edge-set overlap is c in {0,1,2,3},
    since an incidence K_2,2 is a forbidden girth-four configuration.
    Every original six-incidence J has mixed |kappa_J| <= 2, and only J
    meeting BOTH support sets can contribute: |kappa_LR| <= 2 M.
    """
    if (type(s) is not int or s < 2 or s & (s-1)
            or type(overlap) is not int or not 0 <= overlap <= 3):
        raise ValueError("s=2^h>=2 and legal original GQ cross overlap 0..3")
    v = (s+1)*(s*s+1)
    e = (s+1)*v
    d = 2*(s+1)
    m = exact_cross_touch_universe_count(e,d,d,overlap,6)
    return {"s":s, "original_point_and_line_count":v,
            "original_incidence_count":e, "point_swap_incident_edges":d,
            "line_swap_incident_edges":d, "cross_original_overlap":overlap,
            "original_distinct_sixset_joint_touch_upper":m,
            "absolute_signed_cross_curvature_upper":2*m,
            "all_h_exact_support_cancellation":True,
            "does_not_prove_asymptotic_Os6_or_positivity":True}


def original_w32_point_line_cross_overlap(point_pair, line_pair, lines):
    """Actual c=|incidences incident to both original point/line pairs|."""
    if (len(point_pair)!=2 or len(line_pair)!=2
            or not 0 <= point_pair[0]<point_pair[1]<15
            or not 0 <= line_pair[0]<line_pair[1]<15):
        raise ValueError("sorted original W32 typed line/point transpositions required")
    return sum((p+1) in lines[l] for p in point_pair for l in line_pair)


def audit_true_w32_cross_global_orbit():
    """Exhaust EXACT 105 left + 105 right + 11025 simultaneous L/R swaps.

    Each of 105 complete LEFT global swaps changes physical eligibility;
    compile its own ORIGINAL 62,370 left physical-template source. For each,
    independently use B5 physical RIGHT 130-template pullback of the NEW
    source to evaluate 105 shared complete right maps. This is an exact
    11236-cell two-sided local rectangle, NOT all (15!)^2 maps.
    """
    f0,g0=full_permutation(W32_LEFT_H45),full_permutation(W32_RIGHT_S68)
    source0=compile_left(f0)
    fibers0=compile_right_pullback_fibers(source0)
    base=template_pullback_score(fibers0,g0)
    if (base["S_seven"]!=68
            or tuple(base["seven_counts"][t] for t in TAGS)!=W32_S68_VECTOR
            or base["Q7_necessary_numerator"]!=3112510
            or base["right_C_accepted"]!=0
            or base!=full_left_score(source0,g0)):
        raise AssertionError("true original W32 C24-B6 S68 base changed")
    right_perms={b:legal_transpose(g0,*b) for b in PAIRS}
    right_rows={b:template_pullback_score(fibers0,g) for b,g in right_perms.items()}
    if min(r["S_seven"] for r in right_rows.values())!=75:
        raise AssertionError("B6 exact single right neighborhood changed")
    right_min=min(PAIRS,key=lambda b:(right_rows[b]["S_seven"],b))

    _,lines,_=original_W32()
    if (len(lines)!=15 or any(len(line)!=3 for line in lines)):
        raise AssertionError("original W32 45-incidence, 15-line GQ changed")
    # All 105*105 mixed cells are grouped by genuinely shared ORIGINAL
    # complete f,g. Caution: source0 is NOT reused after changing f.
    left_rows={}
    cross_best=None
    cross_min_Q7=None
    cross_score_hist=Counter()
    cross_negative_kappa=0
    cross_strict_improve=0
    cross_mixed_min=None
    overlap_hist=Counter()
    total_analytic_joint_universe=0
    eligible_hist=Counter()
    correct_cross_cells=0
    for a in PAIRS:
        fa=legal_transpose(f0,*a)
        source=compile_left(fa)
        if source["left_source_size"]!=62370:
            raise AssertionError("recompiled LEFT GQ ORIGINAL 62370-source changed")
        fibers=compile_right_pullback_fibers(source)
        eligible_hist[source["static_eligible"]]+=1
        left_row=template_pullback_score(fibers,g0)
        left_rows[a]=left_row
        if a in ((0,1),(4,14),(8,9)):
            if left_row!=full_left_score(source,g0):
                raise AssertionError("recompiled left physical template oracle fails")
        for b in PAIRS:
            gb=right_perms[b]
            row=template_pullback_score(fibers,gb)
            score=row["S_seven"]
            kappa=score-left_row["S_seven"]-right_rows[b]["S_seven"]+68
            c=original_w32_point_line_cross_overlap(a,b,lines)
            overlap_hist[c]+=1
            exposure=all_h_original_gq_cross_touch_bound(2,c)
            if abs(kappa)>exposure["absolute_signed_cross_curvature_upper"]:
                raise AssertionError("all-h shared original sixset cross bound violated")
            total_analytic_joint_universe+=exposure["original_distinct_sixset_joint_touch_upper"]
            cross_score_hist[score]+=1
            correct_cross_cells+=1
            if kappa<0:
                cross_negative_kappa+=1
            if cross_mixed_min is None or (kappa,a,b)<cross_mixed_min:
                cross_mixed_min=(kappa,a,b)
            if score<68:
                cross_strict_improve+=1
            item=(score,a,b)
            if cross_best is None or item<cross_best[:3]:
                cross_best=(score,a,b,fa,gb,row,kappa,left_row["S_seven"],
                            right_rows[b]["S_seven"],c)
            weighted=(row["Q7_necessary_numerator"],score,a,b)
            if cross_min_Q7 is None or weighted<cross_min_Q7:
                cross_min_Q7=weighted

    left_min=min(PAIRS,key=lambda a:(left_rows[a]["S_seven"],a))
    if (len(left_rows)!=105 or correct_cross_cells!=11025
            or sum(overlap_hist.values())!=11025
            or sum(cross_score_hist.values())!=11025
            or max(overlap_hist)>3
            or min(overlap_hist)<0
            or len(PAIRS)+len(PAIRS)+correct_cross_cells+1 != 11236):
        raise AssertionError("two-sided exact finite transposition rectangle incomplete")

    def separate_original_right_first(f,g,row):
        # INDEPENDENT original incidence-right-first 62370 ORIGINAL sixsets;
        # not the 130 physical template classifier reused to find minima.
        source=compile_left(f)
        independent=right_first_independent(f,g)
        left=full_left_score(source,g)
        if left!=row or any(independent[k]!=row[k] for k in
                ("S_seven","seven_counts","right_C_accepted",
                 "Q7_necessary_numerator")):
            raise AssertionError("independent source LEFT/RIGHT original W32 mismatch")

    a=left_min
    separate_original_right_first(legal_transpose(f0,*a),g0,left_rows[a])
    bestscore,besta,bestb,bestf,bestg,bestrow,bestk,firstL,firstR,cross_c=cross_best
    separate_original_right_first(bestf,bestg,bestrow)
    if (bestrow["S_seven"]!=bestscore
            or bestk!=bestscore-firstL-firstR+68):
        raise AssertionError("mixed global f,g aggregate identity failed")

    bestL=left_rows[a]["S_seven"]
    return {
        "original_gq_source_per_left":62370,
        "physical_K6_right_2factor_templates":130,
        "frozen_base_S":68,
        "left_global_swaps":105,"right_global_swaps":105,
        "simultaneous_left_right_swap_cells":11025,
        "whole_typed_radius_one_rectangle_cells":11236,
        "left_static_eligible_source_count_histogram":dict(sorted(eligible_hist.items())),
        "right_only_min_S":right_rows[right_min]["S_seven"],
        "right_only_best_swap":right_min,
        "left_only_min_S":bestL,
        "left_only_best_swap":left_min,
        "left_only_strict_improvements":sum(x["S_seven"]<68 for x in left_rows.values()),
        "cross_min_S":bestscore,
        "cross_best_left_swap":besta,
        "cross_best_right_swap":bestb,
        "cross_best_complete_left":bestf,
        "cross_best_complete_right":bestg,
        "cross_best_seven_vector":bestrow["seven_counts"],
        "cross_best_original_right_C":bestrow["right_C_accepted"],
        "cross_best_necessary_GF5_Q7":bestrow["Q7_necessary_numerator"],
        "cross_best_first_left_S":firstL,
        "cross_best_first_right_S":firstR,
        "cross_best_mixed_delta":bestk,
        "cross_best_original_incidence_overlap":cross_c,
        "cross_strict_improving_cells":cross_strict_improve,
        "cross_negative_signed_mixed_curvature_cells":cross_negative_kappa,
        "cross_min_signed_mixed_curvature":cross_mixed_min[0],
        "cross_min_signed_mixed_pair":(cross_mixed_min[1],cross_mixed_min[2]),
        "cross_score_histogram":dict(sorted(cross_score_hist.items())),
        "cross_min_necessary_Q7":cross_min_Q7[0],
        "cross_min_necessary_Q7_S":cross_min_Q7[1],
        "typed_point_line_original_overlap_histogram":dict(sorted(overlap_hist.items())),
        "sum_exact_original_sixset_joint_touch_universe_across_11025_cells":
            total_analytic_joint_universe,
        "independent_original_right_first_best_cross_and_best_left":True,
        "recompiled_all_105_different_left_sources":True,
        "all_h_cross_support_bound_is_loose_and_not_positive_S_lower":True,
        "no_global_15factorial_squared_or_all_h_positivity":True,
    }


if __name__=="__main__":
    import json
    print(json.dumps(audit_true_w32_cross_global_orbit(),sort_keys=True,indent=2))
