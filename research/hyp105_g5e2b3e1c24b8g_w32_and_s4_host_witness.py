"""B8-G hosted original W32 f0/g68 and independent all-h s=4 Gram falsifier.

Actual original seven-score only for W32. The s=4 physical feature Z_01 is a
SYNTHETIC score for checking the all-h pair projection, not a real W(3,4)
six-motif census. Never extrapolate fixed-left W32 measurements to s>2.
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
    exact_pair_projection,evaluate_projection,exact_gram_entry,
    exact_pair_gram_parameters,
)
from hyp105_g5e2b3e1c24b8f_signed_star_gate import (
    star_dual_lower_certificate,
)
from hyp105_g5e2b3e1c24b8g_host_slack_pair_degree import (
    minimal_host_capacity,certified_pair_degree_lower,
    evaluate_global_projection,residual_separation_gate,
)


def report():
    f,g=tuple(W32_LEFT_H45),tuple(W32_RIGHT_S68)
    source=compile_left(f)
    table=compiled_matrix(source,6,15)
    mu=table["mean"]
    if mu!=Fraction(870476,5005) or any(table["row_sums"].values()):
        raise AssertionError("genuine W32 prior exact original matrix/mean drift")
    score=full_left_score(source,g)["S_seven"]
    if score!=68 or right_first_independent(f,g)["S_seven"]!=score:
        raise AssertionError("original left/right W32 six-incidence oracles disagree")
    proj=exact_pair_projection(table["matrix"],6,15)
    cert=certified_pair_degree_lower(proj["coefficients"],6,15)
    image=tuple(K6_PAIRS[e] for e in g)
    ev=evaluate_global_projection(proj["coefficients"],image,6)
    expected=evaluate_projection(proj,image,6)
    if ev["centered_projection"]!=expected or expected!=Fraction(-6875243,60060):
        raise AssertionError("B8-E exact W32 projection changed")
    if cert["certified_global_projection_lower"]>expected:
        raise AssertionError("actual original right g violates all-g capacity certificate")
    if cert["host"]["unused_physical_edges"]!=0 or cert["host"]["occupied_adjacency_total_min"]!=60:
        raise AssertionError("full W32 physical host adjacency must be constant at 60")
    star=star_dual_lower_certificate(table["matrix"],6,sweeps=4)
    star_bound=star["certified_lower_pair_projection"]
    residual=Fraction(score)-mu-expected
    if residual!=Fraction(73373,8580) or star_bound!=Fraction(-558274,3003):
        raise AssertionError("B8-F original nonlinear residual/star dual drift")
    gate=residual_separation_gate(mu,cert["certified_global_projection_lower"],residual)
    if not gate["separated_positive_gate_ruled_out_by_witness"]:
        raise AssertionError("W32 B8-G separated residual gate unexpectedly claimed closed")

    # Host-slack ALL-h exact law independent of true W(3,4) original source
    # census: use an invariant synthetic score Z_{0,1} on s=4 n=85 lines.
    s=4
    n=(s+1)*(s*s+1)
    a=14
    par=minimal_host_capacity(a,n)
    if (n!=85 or par["m"]!=91 or par["unused_physical_edges"]!=6 or
            par["occupied_row_degree_min"]!=18 or
            par["occupied_row_degree_max"]!=24 or
            par["occupied_adjacency_total_min"]!=948 or
            par["occupied_adjacency_total_max"]!=963):
        raise AssertionError("actual all-h minimal host/edge deletion law mismatch")
    params=exact_pair_gram_parameters(a,n)
    v=params["variance"]
    pair=(0,1)
    I={p:exact_gram_entry(a,n,p,pair)/v
       for p in combinations(range(n),2)}
    synthetic_proj=exact_pair_projection(I,a,n)
    if (params["rank"]!=n*(n-1)//2 or
            synthetic_proj["projected_variance"]!=v or
            synthetic_proj["coefficients"][pair]!=1 or
            any(value for k,value in synthetic_proj["coefficients"].items() if k!=pair)):
        raise AssertionError("all-h exact synthetic Z01 pair-projection invariant failed")
    synthetic_cert=certified_pair_degree_lower(
        synthetic_proj["coefficients"],a,n,max_exact_candidates=2000)
    actual_edges=tuple(combinations(range(a),2))[:n]
    synthetic_ev=evaluate_global_projection(
        synthetic_proj["coefficients"],actual_edges,a)
    if (synthetic_ev["centered_projection"]!=
            evaluate_projection(synthetic_proj,actual_edges,a)
            or synthetic_cert["certified_global_projection_lower"]!=Fraction(-4,15)
            or synthetic_ev["occupied_adjacency_count"]!=960 or
            not synthetic_cert["complete_piecewise_linear_dual_scan"]):
        raise AssertionError("s=4 exact minimal-host synthetic lower/oracle failed")
    return {
        "slice":"HYP-105-C24-B8-G",
        "genuine_W32_original_right_first_score":score,
        "genuine_W32_source_eligible":source["static_eligible"],
        "genuine_W32_mu":str(mu),
        "genuine_W32_P2_g68":str(expected),
        "genuine_W32_R_g68":str(residual),
        "genuine_W32_B8G_all_g_row_degree_P_lower":
            str(cert["certified_global_projection_lower"]),
        "genuine_W32_B8F_all_g_signed_star_P_lower":str(star_bound),
        "genuine_W32_B8G_selected_dual_price":str(cert["selected_adjacency_price"]),
        "genuine_W32_B8G_uniform_residual_gate_required":str(
            gate["residual_uniform_lower_must_exceed"]),
        "genuine_W32_gate_ruled_out_by_valid_R_witness":True,
        "synthetic_s4_not_original_GQ_seven_score":True,
        "synthetic_s4_n_lines":n,
        "synthetic_s4_host_K_a":a,
        "synthetic_s4_unused_physical_edges":par["unused_physical_edges"],
        "synthetic_s4_sharp_adjacency_min":par["occupied_adjacency_total_min"],
        "synthetic_s4_sharp_adjacency_max":par["occupied_adjacency_total_max"],
        "synthetic_s4_pair_projection_exact_rational_lower":
            str(synthetic_cert["certified_global_projection_lower"]),
        "synthetic_s4_complete_1D_breakpoint_dual_checked":
            synthetic_cert["complete_piecewise_linear_dual_scan"],
        "no_all_h_six_motif_or_original_S_minimum_claim":True,
        "no_branch_A_B_R3_or_ASET_claim":True,
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
