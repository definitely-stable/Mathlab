"""Hosted only: true ORIGINAL W(3,2) joint S=P2+R+mu cylinder certificate.

One globally coherent partial right injection, ten pinned original lines of
g68, five remaining lines, 5!=120 entire completions. No 15! and no
independent original motif maps. The joint support relaxation proves a
pointwise lower on S for EVERY one of those 120 full consistent completions.
"""
from fractions import Fraction
from itertools import combinations,permutations
import json

from hyp105_g5e2b3e1c24_right_c_certificate import K6_PAIRS
from hyp105_g5e2b3e1c24b_three_collision import W32_LEFT_H45
from hyp105_g5e2b3e1c24b6_mixed_curvature_s68 import W32_RIGHT_S68
from hyp105_g5e2b3e1c24b2_joint_seven import (
    BITS,compile_left,full_left_score,right_first_independent,accepted,
)
from hyp105_g5e2b3e1c24b5_two_swap_escape import (
    compile_right_pullback_fibers,template_pullback_score,
)
from hyp105_g5e2b3e1c24b8d_two_line_influence import compiled_matrix
from hyp105_g5e2b3e1c24b8e_pair_harmonic_residual import (
    exact_pair_projection,evaluate_projection,
)
from hyp105_g5e2b3e1c24b8h_joint_source_cylinder import (
    joint_cylinder_certificate,
)


def report():
    left=tuple(W32_LEFT_H45)
    right=tuple(W32_RIGHT_S68)
    src=compile_left(left)
    original_records=tuple(
        (tuple(sorted(set(rec[1]))),rec[3],rec)
        for rec in src["records"])
    if (sum(weight for _,weight,_ in original_records)!=src["static_eligible"]
            or src["static_eligible"]!=53907):
        raise AssertionError("original W32 seven-family multiplicity lost")

    # The payload exact original support must be all/right incidences read
    # by the existing seven-score acceptance oracle, including D6 signature.
    for support,weight,rec in original_records:
        if (support!=tuple(sorted(set(rec[1]))) or
                len(rec[1])!=6 or rec[3]!=weight):
            raise AssertionError("source support contract is incomplete")
    pinned={i:right[i] for i in range(10)}
    free=tuple(range(10,15))
    available=tuple(e for e in range(15) if e not in pinned.values())

    def original_source_accept(rec,assignment):
        masks=[0]*15
        for l in set(rec[1]):
            if l not in assignment:
                raise AssertionError("attempted incomplete original record support")
            masks[l]=BITS[assignment[l]]
        return accepted(rec,masks)

    certificate=joint_cylinder_certificate(
        original_records,pinned,15,15,original_source_accept,
        max_union_support=3,include_exact=True,
        max_group_states=6000,max_record_evaluations=25000000)
    if certificate["whole_completion_states_evaluated"]!=120:
        raise AssertionError("exact coherent five-line completion orbit incomplete")
    if certificate["exact_cylinder_minimum"]>68:
        raise AssertionError("true g68 must lie in the frozen partial cylinder")

    # SECOND exact scorer does NOT minimize independently at a source:
    # it globally inverts all 130 physical two-factor templates on EVERY full g.
    fibers=compile_right_pullback_fibers(src)
    all_states=[]
    for remainder in permutations(available):
        whole=tuple(pinned.get(i,remainder[i-10]) for i in range(15))
        all_states.append((template_pullback_score(fibers,whole)["S_seven"],whole))
    if len(all_states)!=120 or len(set(g for _,g in all_states))!=120:
        raise AssertionError("not all globally coherent original g completions")
    minimum,chosen=min(all_states)
    if minimum!=certificate["exact_cylinder_minimum"]:
        raise AssertionError("independent entire-score cylinder minimum disagrees")
    if full_left_score(src,chosen)["S_seven"]!=minimum:
        raise AssertionError("independent original left-first minimum disagrees")
    if right_first_independent(left,chosen)["S_seven"]!=minimum:
        raise AssertionError("original RIGHT-FIRST 62370-sixset minimum disagrees")
    if full_left_score(src,right)["S_seven"]!=68 or right_first_independent(left,right)["S_seven"]!=68:
        raise AssertionError("original score-68 reference changed")

    matrix=compiled_matrix(src,6,15)
    if matrix["mean"]!=Fraction(870476,5005) or any(matrix["row_sums"].values()):
        raise AssertionError("B8-D original W32 mean/row identities lost")
    mu=matrix["mean"]
    projection=exact_pair_projection(matrix["matrix"],6,15)
    pairs=[]
    for score,whole in all_states:
        p=evaluate_projection(projection,tuple(K6_PAIRS[x] for x in whole),6)
        residual=Fraction(score)-mu-p
        pairs.append((p,residual,score,whole))
    if Fraction(min(score for score,_ in all_states))-mu != min(
            p+r for p,r,_,_ in pairs):
        raise AssertionError("exact joint P2+R reconstruction failed")
    if evaluate_projection(projection,tuple(K6_PAIRS[x] for x in right),6)!=Fraction(-6875243,60060):
        raise AssertionError("B8-E g68 exact pair projection lost")

    min_p=min(p for p,_,_,_ in pairs)
    min_r=min(r for _,r,_,_ in pairs)
    min_joint=Fraction(minimum)-mu
    if min_p+min_r>min_joint:
        raise AssertionError("separate minima cannot exceed true coupled minimum")
    independent_floor=certificate["supportwise_pointwise_seven_lower"]
    coupled_floor=certificate["coupled_pointwise_seven_lower"]
    if not 0<=independent_floor<=coupled_floor<=minimum:
        raise AssertionError("valid original seven-score cylinder floors lost")
    return {
        "slice":"HYP-105-C24-B8-H",
        "exact_parent_B8G_HEAD":"4e28b85298fd7ddca1d3e7339e471a00ea60fc19",
        "genuine_original_W32_left_eligible_sources":src["static_eligible"],
        "genuine_original_W32_left_compiled_records":len(original_records),
        "pinned_original_right_lines":len(pinned),
        "remaining_original_right_lines":len(free),
        "entire_global_right_completions":len(all_states),
        "frozen_original_g68_score":68,
        "independent_sourcewise_all_completions_score_lower":independent_floor,
        "coupled_source_groups_all_completions_score_lower":coupled_floor,
        "exact_cylinder_seven_score_min":minimum,
        "exact_cylinder_min_global_right":list(chosen),
        "true_original_right_first_min_verified":True,
        "exact_mean":str(mu),
        "joint_pointwise_P2_plus_R_lower_via_support_groups":
            str(Fraction(coupled_floor)-mu),
        "exact_min_joint_P2_plus_R_over_cylinder":str(min_joint),
        "separately_minimized_P2_plus_residual_over_cylinder":str(min_p+min_r),
        "correlation_slack_joint_minus_separately_minimized":
            str(min_joint-min_p-min_r),
        "separate_P2_min_over_cylinder":str(min_p),
        "separate_nonlinear_R_min_over_cylinder":str(min_r),
        "independent_completion_states_evaluated":
            certificate["independent_completion_states_evaluated"],
        "coupled_completion_states_evaluated":
            certificate["coupled_completion_states_evaluated"],
        "coupled_support_group_count":certificate["coupled_support_groups"],
        "max_coupled_support":certificate["max_coupled_group_support"],
        "original_source_evaluation_count":certificate["weighted_source_acceptance_evaluations"],
        "NOT_global_all_15_factorial_or_min_S":True,
        "NOT_all_h_positive_omega_s6_R3_ASET":True,
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
