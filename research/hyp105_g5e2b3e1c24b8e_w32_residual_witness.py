"""B8-E GitHub-hosted only: genuine W32 nonlinear pair-feature residual witness.

One compressed exact B8-D 105-pair tensor and a separate original right-first
full sixset score at ONE coherent complete global g68. No 15! search.
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
    exact_pair_projection,exact_residual_witness,evaluate_projection,
)


def report():
    f=tuple(W32_LEFT_H45)
    g=tuple(W32_RIGHT_S68)
    source=compile_left(f)
    matrix=compiled_matrix(source,6,15)
    mu=matrix["mean"]
    if mu!=Fraction(870476,5005) or any(matrix["row_sums"].values()):
        raise AssertionError("B8-D original W32 exact covariance certificate changed")
    oracle=right_first_independent(f,g)
    direct=full_left_score(source,g)
    if oracle["S_seven"]!=68 or direct["S_seven"]!=68:
        raise AssertionError("independent genuine original global W32 g68 score failed")

    projection=exact_pair_projection(matrix["matrix"],6,15)
    par=projection["params"]
    if (par["rank"]!=90 or par["eigenvalues"]!=(0,0,Fraction(2,7))
            or not projection["exact_orthogonality_all_pair_features"]):
        raise AssertionError("all-h pair Johnson spectrum W32 specialization failed")
    for pair,influence in matrix["matrix"].items():
        if projection["coefficients"][pair]!=Fraction(6,7)*influence:
            raise AssertionError("W32 full-bijection gamma=6I/7 lost")

    image_edges=tuple(K6_PAIRS[e] for e in g)
    witnessed=exact_residual_witness(projection,mu,68,image_edges,6)
    # Explicit independent arithmetic evaluation of pair-coefficient contraction.
    p=Fraction(4,7)
    by_pair=sum((Fraction(6,7)*matrix["matrix"][(i,j)]
                 *(int(bool(set(image_edges[i])&set(image_edges[j])))-p)
                 for i,j in combinations(range(15),2)),Fraction(0))
    if witnessed["pair_linear_projection_at_g"]!=by_pair:
        raise AssertionError("independent 105-pair contraction mismatch")
    selected_g=g
    if witnessed["nonlinear_pair_feature_residual_at_g"]==0:
        # A zero for this PARTICULAR global g does not prove that all R vanish.
        # Try only 105 globally coherent single right transpositions, never
        # independently change an original sixset or sample an incomplete g.
        for i,j in combinations(range(15),2):
            other=list(g)
            other[i],other[j]=other[j],other[i]
            alt=tuple(other)
            scored=full_left_score(source,alt)["S_seven"]
            candidate=exact_residual_witness(
                projection,mu,scored,tuple(K6_PAIRS[e] for e in alt),6)
            if candidate["actual_seven_score_not_pair_linear"]:
                witnessed=candidate
                selected_g=alt
                break
    if not witnessed["actual_seven_score_not_pair_linear"]:
        raise AssertionError("no valid genuine W32 nonlinear residual certificate found")

    # Orthogonality is an exact algebraic statement for all g, even though
    # one observed residual does NOT supply the full residual distribution.
    return {
        "slice":"HYP-105-C24-B8-E",
        "exact_parent_B8D_head":"5e13aa08f4a1322e6255139aa14c68457a895823",
        "original_seven_left_eligible_sources":source["static_eligible"],
        "complete_right_global_witness":list(selected_g),
        "baseline_g68_checked_by_independent_right_first":True,
        "n_lines":15, "host_coordinates":6,
        "pair_features":105,
        "gram_rank":par["rank"],
        "gram_nonzero_eigenvalue":str(par["eigenvalues"][2]),
        "pair_linear_projection_variance_exact":str(projection["projected_variance"]),
        "mean_exact":str(mu),
        "observed_seven_score":witnessed["score"],
        "pair_projection_at_valid_g":str(witnessed["pair_linear_projection_at_g"]),
        "nonlinear_residual_at_valid_g":str(
            witnessed["nonlinear_pair_feature_residual_at_g"]),
        "certified_residual_Linf_lower":str(
            witnessed["certified_residual_infinity_norm_floor"]),
        "orthogonal_residual_to_each_pair_in_L2":True,
        "no_residual_variance_or_uniform_minimum_claim":True,
        "no_branch_A_B_full_R3_or_ASET_claim":True,
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
