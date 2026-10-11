"""Hosted only: actual W(3,2) original sixset score vs certified star lower.

No 15! enumeration, no fabricated finite minimum, and no residual uniform bound.
"""
from fractions import Fraction
from itertools import combinations
import json

from hyp105_g5e2b3e1c24_right_c_certificate import K6_PAIRS
from hyp105_g5e2b3e1c24b_three_collision import W32_LEFT_H45
from hyp105_g5e2b3e1c24b6_mixed_curvature_s68 import W32_RIGHT_S68
from hyp105_g5e2b3e1c24b2_joint_seven import (
    compile_left,full_left_score,right_first_independent,
)
from hyp105_g5e2b3e1c24b8d_two_line_influence import compiled_matrix
from hyp105_g5e2b3e1c24b8e_pair_harmonic_residual import (
    exact_pair_projection,evaluate_projection,
)
from hyp105_g5e2b3e1c24b8f_signed_star_gate import (
    evaluate_full_star_form,star_dual_lower_certificate,conditional_residual_gate,
)


def report():
    f=tuple(W32_LEFT_H45)
    g=tuple(W32_RIGHT_S68)
    source=compile_left(f)
    I_data=compiled_matrix(source,6,15)
    I=I_data["matrix"]
    mu=I_data["mean"]
    if mu!=Fraction(870476,5005) or any(I_data["row_sums"].values()):
        raise AssertionError("B8-D W32 exact original influence or mean drift")
    score=full_left_score(source,g)["S_seven"]
    independently=right_first_independent(f,g)["S_seven"]
    if score!=68 or independently!=68:
        raise AssertionError("g68 actual W32 seven-source right-first oracle drift")
    projection=exact_pair_projection(I,6,15)
    if projection["projected_variance"]!=Fraction(329290770373,450900450):
        raise AssertionError("B8-E exact W32 L2 variance drift")
    edges=tuple(K6_PAIRS[i] for i in g)
    stars=evaluate_full_star_form(I,edges,6)
    independent_p=evaluate_projection(projection,edges,6)
    if stars["pair_projection"]!=independent_p or independent_p!=Fraction(-6875243,60060):
        raise AssertionError("independent star / Johnson projection vs g68 mismatch")
    residual=Fraction(score)-mu-independent_p
    if residual!=Fraction(73373,8580):
        raise AssertionError("true original W32 nonlinear residual drift")

    cert=star_dual_lower_certificate(I,6,sweeps=4)
    # Different direct all-3003-subsets formula, independent of reduced-array
    # coordinate implementation. This is NOT enumeration of global g.
    dual=cert["dual_y"]
    all_costs=[]
    for subset in combinations(range(15),5):
        cost=sum((I[i,j] for i,j in combinations(subset,2)),Fraction(0))
        all_costs.append(cost-sum((dual[i] for i in subset),Fraction(0)))
    independently_rebuilt=2*sum(dual,Fraction(0))+6*min(all_costs)
    if independently_rebuilt!=cert["certified_lower_T"]:
        raise AssertionError("star dual not independently reconstructed")
    if cert["certified_lower_T"]>stars["signed_T"]:
        raise AssertionError("valid full g68 violates global star relaxation")
    threshold=conditional_residual_gate(mu,cert["certified_lower_pair_projection"])

    return {
        "slice":"HYP-105-C24-B8-F",
        "parent_PR":361,
        "original_W32_right_first_seven_score":score,
        "original_left_source_eligible":source["static_eligible"],
        "right_global_injection":list(g),
        "mean":str(mu),
        "pair_projection_at_g68":str(independent_p),
        "star_signed_T_at_g68":str(stars["signed_T"]),
        "nonlinear_residual_at_g68":str(residual),
        "exact_signed_star_subsets_tested":cert["star_subset_count"],
        "naive_global_T_lower":str(cert["naive_lower_T"]),
        "optimized_dual_global_T_lower":str(cert["certified_lower_T"]),
        "optimized_dual_global_pair_projection_lower":str(
            cert["certified_lower_pair_projection"]),
        "certified_gap_to_actual_g68_projection":str(
            independent_p-cert["certified_lower_pair_projection"]),
        "dual_sweep_history":[str(x) for x in cert["dual_sweep_history"]],
        "required_all_g_residual_lower_for_strict_positive_score":str(
            threshold["residual_lower_needed_for_strict_positive"]),
        "conditional_gate_only_no_global_residual_certificate":True,
        "not_global_min_T_or_min_S":True,
        "not_branch_A_B_full_R3_ASET":True,
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
