"""HYP-105 #230 D6-R: exact *disjoint* transposition Hessian of all seven ORIGINAL GF5 sectors.

For ANY finite original W(3,2**h) and globally injective fixed f,g,
take two DISJOINT transpositions sigma=(u,v), tau=(w,z) of ORIGINAL
right-line physical pair labels. Let I_sigma be ORIGINAL incidence
cylinders containing u or v; let I_tau similarly. The EXACT mixed
difference ("discrete Hessian") of seven-positive counts is

 H_{sigma,tau} S(g) = S(g^{sigma tau})-S(g^sigma)-S(g^tau)+S(g)
   = sum_{c in I_sigma intersect I_tau} m_f(c)*
       (chi_c(g^{sigma tau})-chi_c(g^sigma)-chi_c(g^tau)+chi_c(g)).

This uses the incidence-POSITION cylinders of D6-P, including aligned
D6 and the B/B overlap. It is not valid for overlapping swaps with
this intersection-only boundary. No physical right-edge injection is
broken by swapping two ORIGINAL right IDs.

Consequently Delta_{sigma tau} S = Delta_sigma S + Delta_tau S + H.
Every indicator is 0 or 1; |H|<=2*sum_{c in both}m_f(c).
For the positive selected GF5 necessary lower NUMERATOR, each cylinder
takes one of its class weights or zero, so
  |H_GF5| <= 2*51750*sum_{c in both}m_f(c).
These are exact all-h signed curvature identities and deterministic
worst-case bounds, not the all-g Omega(s**6) root theorem. They
explain why two strict one-swap local minima can nevertheless have
an improving disjoint two-swap composition (if observed), and give a
necessary negative-curvature threshold to escape one-swap minima.

Executable true-ORIGINAL finite oracle is W(3,2) only; the targeted
S68/S72 two-swap probe has an EXPLICIT subset-of-105-pairs scope and
does not claim all two-swaps, 3-cycles, global optimality or W34 S.
"""
from collections import Counter
from itertools import combinations
import json

from hyp105_issue230_d6p_seven_cylinder_swap_audit import (
    SEVEN_CLASSES, swapped_labels, compile_original_W32_cylinders,
    cylinder_seven_class, cylinder_census, exact_seven_cylinder_swap,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, seven_census,
)


MAX_GF5_WEIGHT = max(R3_CERTIFIED_FLOORS.values())
assert MAX_GF5_WEIGHT == 51750


def _validate_disjoint_pairs(right_labels,first,second):
    if (len(first)!=2 or len(second)!=2 or
            len(set(first))!=2 or len(set(second))!=2 or
            len(set(first)|set(second))!=4):
        raise ValueError("requires two transpositions on FOUR distinct ORIGINAL right lines")
    if any(type(i) is not int or i<0 or i>=len(right_labels)
           for i in (*first,*second)):
        raise ValueError("invalid ORIGINAL right line in disjoint transposition")
    return tuple(sorted(first)),tuple(sorted(second))


def _accepted_tag_value(tag):
    return int(tag is not None)


def _weighted_tag_value(tag):
    return R3_CERTIFIED_FLOORS[tag] if tag is not None else 0


def exact_disjoint_right_swap_hessian(compiled,right_labels,first,second,
                                      marginal_first=None,marginal_second=None):
    """Exact all-seven finite ORIGINAL disjoint-swap mixed curvature.

    Prior singleton deltas, if supplied, MUST originate from same
    compiled f and right_labels. Independent tests cross-check that.
    """
    first,second=_validate_disjoint_pairs(right_labels,first,second)
    index=compiled["by_original_line"]
    first_hit=set(index.get(first[0],()))
    first_hit.update(index.get(first[1],()))
    second_hit=set(index.get(second[0],()))
    second_hit.update(index.get(second[1],()))
    both=first_hit.intersection(second_hit)
    if marginal_first is None:
        marginal_first=exact_seven_cylinder_swap(
            compiled,right_labels,*first)
    if marginal_second is None:
        marginal_second=exact_seven_cylinder_swap(
            compiled,right_labels,*second)
    if (tuple(marginal_first["swap_original_lines"])!=first or
            tuple(marginal_second["swap_original_lines"])!=second):
        raise ValueError("incorrect cached marginal right swaps")
    g1=swapped_labels(right_labels,*first)
    g2=swapped_labels(right_labels,*second)
    g12=swapped_labels(g1,*second)  # disjoint => commutes
    if g12!=swapped_labels(g2,*first):
        raise AssertionError("disjoint right transpositions MUST commute")
    curvature_by_class=Counter()
    curvature=0
    weighted_curvature=0
    mass=0
    for cylinder in both:
        w=compiled["cylinders"][cylinder]
        tags=(
            cylinder_seven_class(cylinder,right_labels),
            cylinder_seven_class(cylinder,g1),
            cylinder_seven_class(cylinder,g2),
            cylinder_seven_class(cylinder,g12),
        )
        signs=(1,-1,-1,1)
        for tag,sign in zip(tags,signs):
            if tag is not None:
                curvature_by_class[tag]+=sign*w
        curvature+=w*sum(sign*_accepted_tag_value(tag)
                         for sign,tag in zip(signs,tags))
        weighted_curvature+=w*sum(sign*_weighted_tag_value(tag)
                                  for sign,tag in zip(signs,tags))
        mass+=w
    if (sum(curvature_by_class.values())!=curvature or
            sum(curvature_by_class[k]*R3_CERTIFIED_FLOORS[k]
                for k in SEVEN_CLASSES)!=weighted_curvature):
        raise AssertionError("seven-class Hessian GF5 conservation violated")
    bound=2*mass
    if abs(curvature)>bound or abs(weighted_curvature)>MAX_GF5_WEIGHT*bound:
        raise AssertionError("exact all-h right-cylinder Hessian support bound violated")
    delta_class={
        k:(marginal_first["delta_by_seven_class"][k]+
           marginal_second["delta_by_seven_class"][k]+curvature_by_class[k])
        for k in SEVEN_CLASSES
    }
    combined=marginal_first["delta_S_seven"]+marginal_second[
        "delta_S_seven"]+curvature
    combined_weighted=(
        marginal_first["delta_GF5_selected_lower_numerator"]+
        marginal_second["delta_GF5_selected_lower_numerator"]+
        weighted_curvature
    )
    if (combined!=sum(delta_class.values()) or
            combined_weighted!=sum(
                delta_class[k]*R3_CERTIFIED_FLOORS[k] for k in SEVEN_CLASSES)):
        raise AssertionError("two-swap marginal plus Hessian identity violated")
    return {
        "first_swap":list(first),
        "second_swap":list(second),
        "moved_original_right_factors":list(sorted(set(first)|set(second))),
        "joint_boundary_unique_original_cylinders":len(both),
        "joint_boundary_original_sixsets_weight":mass,
        "deterministic_absolute_Hessian_S_upper":bound,
        "deterministic_absolute_Hessian_GF5_upper":MAX_GF5_WEIGHT*bound,
        "singleton_delta_S_first":marginal_first["delta_S_seven"],
        "singleton_delta_S_second":marginal_second["delta_S_seven"],
        "Hessian_by_all_seven_positive_classes":{
            k:curvature_by_class[k] for k in SEVEN_CLASSES},
        "Hessian_S":curvature,
        "Hessian_GF5_selected_lower_numerator":weighted_curvature,
        "two_disjoint_swaps_delta_by_seven_class":delta_class,
        "two_disjoint_swaps_delta_S":combined,
        "two_disjoint_swaps_delta_GF5_selected_lower_numerator":combined_weighted,
        "genuine_complete_right_injection_preserved":True,
        "negative_Hessian_needed_to_escape_two_strict_single_swaps":
            (combined<0 and
             marginal_first["delta_S_seven"]>0 and
             marginal_second["delta_S_seven"]>0),
        "root_all_h_lower_proved":False,
    }


def finite_targeted_W32_disjoint_double_swap_report(*,top_k=12):
    """Targeted, honest 2-swap subset from ALL 105 singleton deltas.

    Exactly 2 orientations of each overlapping pair are excluded: only
    two disjoint swaps are evaluated. The top_k singleton moves are
    chosen by (Delta S, original IDs) deterministically, independent of
    second-order results. This is NOT all 3-cycle/2-swap permutations.
    """
    if type(top_k) is not int or top_k<4 or top_k>105:
        raise ValueError("top_k requires 4..105 (explicit subset scope)")
    cases=[]
    for scheme in ("S68","S72"):
        model=fixture(1,scheme)
        compiled=compile_original_W32_cylinders(model)
        g=model["right_labels"]
        before=cylinder_census(compiled,g)
        real=seven_census(model,independent_checks=False)
        if before["S_seven"]!=real["S_seven"]:
            raise AssertionError("genuine ORIGINAL W32 baseline seven census mismatch")
        moves=[exact_seven_cylinder_swap(compiled,g,u,v)
               for u,v in combinations(range(len(g)),2)]
        if len(moves)!=105:
            raise AssertionError("all original W32 singleton transpositions lost")
        if not all(m["delta_S_seven"]>0 for m in moves):
            raise AssertionError("S68/S72 strict one-swap local minimum changed")
        rank=sorted(moves,key=lambda r:(
            r["delta_S_seven"],r["swap_original_lines"]))
        selected=rank[:top_k]
        pairs=[(x,y) for x,y in combinations(selected,2)
               if set(x["swap_original_lines"]).isdisjoint(
                   y["swap_original_lines"])]
        if not pairs:
            raise AssertionError("no genuine disjoint candidate swaps")
        outcomes=[exact_disjoint_right_swap_hessian(
            compiled,g,x["swap_original_lines"],y["swap_original_lines"],
            x,y) for x,y in pairs]
        best=min(outcomes,key=lambda row:(
            row["two_disjoint_swaps_delta_S"],
            row["first_swap"],row["second_swap"]))
        worst=max(outcomes,key=lambda row:(
            row["two_disjoint_swaps_delta_S"],
            row["first_swap"],row["second_swap"]))
        if any(result["negative_Hessian_needed_to_escape_two_strict_single_swaps"]
               != (result["two_disjoint_swaps_delta_S"]<0)
               for result in outcomes):
            raise AssertionError("strict singleton minimum mixed escape curvature wrong")
        weighted_escapes=sum(
            r["two_disjoint_swaps_delta_GF5_selected_lower_numerator"]<0
            for r in outcomes)
        cases.append({
            "scheme":scheme,
            "baseline_original_seven_S":before["S_seven"],
            "baseline_original_GF5_seven_floor_num":before[
                "GF5_seven_lower_numerator"],
            "full_105_single_swap_min_delta_S":rank[0]["delta_S_seven"],
            "all_105_singleton_swaps_strictly_worsen_S":True,
            "top_k_single_swap_ranked_moves":top_k,
            "targeted_disjoint_two_swap_pairs_scanned":len(pairs),
            "targeted_two_swap_improving_S":sum(
                r["two_disjoint_swaps_delta_S"]<0 for r in outcomes),
            "targeted_two_swap_equal_S":sum(
                r["two_disjoint_swaps_delta_S"]==0 for r in outcomes),
            "targeted_two_swap_worsening_S":sum(
                r["two_disjoint_swaps_delta_S"]>0 for r in outcomes),
            "targeted_two_swap_improving_GF5_floor":weighted_escapes,
            "targeted_negative_Hessian_pairs":sum(
                r["Hessian_S"]<0 for r in outcomes),
            "targeted_positive_Hessian_pairs":sum(
                r["Hessian_S"]>0 for r in outcomes),
            "min_targeted_Hessian_S":min(
                r["Hessian_S"] for r in outcomes),
            "max_targeted_Hessian_S":max(
                r["Hessian_S"] for r in outcomes),
            "best_targeted_two_swap":best,
            "worst_targeted_two_swap":worst,
            "all_disjoint_two_swaps_covered":False,
            "overlapping_3cycles_covered":False,
            "global_optimality_proved":False,
        })
    return {
        "slice":"HYP105-ISSUE230-D6R-EXACT-DISJOINT-SWAP-HESSIAN",
        "theorem":"ALL-H-EXACT-DISJOINT-ORIGINAL-CYLINDER-HESSIAN",
        "fin_W32_f_g_original_complete_injections":True,
        "all_h_local_hessian_intersection_support_identity":True,
        "all_h_abs_curvature_upper_from_original_cylinder_intersection":True,
        "two_swap_search_scope":"TOP-K-FIRST-SWAPS-ONLY-DISJOINT-PAIRS",
        "full_W34_W38_original_seven_S":"NOT-CLAIMED",
        "Branch_A":"OPEN","Branch_B":"OPEN",
        "rows":cases,
    }


if __name__=="__main__":
    print(json.dumps(finite_targeted_W32_disjoint_double_swap_report(),
                     sort_keys=True,indent=2))
