"""GitHub-hosted original W32 proof-tree construction AND independent replay.

Bounded scope: original LEFT f0 fixed and ten actual original-right images of
g68 fixed. The 120 remaining entire global K6-edge completions are covered
without a missing or duplicated physical edge. An unpinned K6 15! conclusion
would be FALSE: it is explicitly NOT attempted.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations,permutations
from pathlib import Path
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
from hyp105_g5e2b3e1c24b8i_global_cover_replay import (
    build_cover,replay_cover,
)


def report(output_path=None):
    f=tuple(W32_LEFT_H45)
    g68=tuple(W32_RIGHT_S68)
    source=compile_left(f)
    original=tuple((tuple(sorted(set(row[1]))),row[3],row)
                   for row in source["records"])
    if (source["static_eligible"]!=53907 or
            sum(w for _,w,_ in original)!=53907):
        raise AssertionError("genuine original sixset multiplicity drift")
    for support,w,row in original:
        if support!=tuple(sorted(set(row[1]))) or w!=row[3]:
            raise AssertionError("original support mismatch")
    pins={i:g68[i] for i in range(10)}
    order=tuple(range(10,15))
    fibers=compile_right_pullback_fibers(source)

    def _complete(assignment):
        if set(assignment)!=set(range(15)) or len(set(assignment.values()))!=15:
            raise AssertionError("score oracle received non-global original map")
        return tuple(assignment[i] for i in range(15))

    def fast_score(assignment):
        return template_pullback_score(fibers,_complete(assignment))["S_seven"]

    def independent_original_score(assignment):
        return full_left_score(source,_complete(assignment))["S_seven"]

    def original_eval(row,assignment):
        masks=[0]*15
        for line in set(row[1]):
            if line not in assignment:
                raise AssertionError("incomplete original source support")
            masks[line]=BITS[assignment[line]]
        return accepted(row,masks)

    floors={}
    def original_coupled_floor(assignment):
        if assignment!=pins:
            raise ValueError("this witness only authorizes root source floor")
        key=tuple(sorted(assignment.items()))
        if key not in floors:
            floors[key]=joint_cylinder_certificate(
                original,assignment,15,15,original_eval,
                max_union_support=3,include_exact=False,
                max_group_states=6000,max_record_evaluations=25000000)
        return floors[key]["coupled_pointwise_seven_lower"]

    exact_tree=build_cover(15,15,pins,order,fast_score,
                           max_nodes=400,max_leaves=130)
    exact_replay=replay_cover(exact_tree,independent_original_score,
                              max_nodes=400,max_leaves=130)
    if (exact_replay["whole_global_injection_leaf_count"]!=120 or
            exact_replay["has_pruned_subtrees"] or
            exact_replay["exact_cylinder_minimum"] is None):
        raise AssertionError("original W32 full pinned cylinder proof incomplete")
    minimum=exact_replay["exact_cylinder_minimum"]
    threshold_tree=build_cover(
        15,15,pins,order,fast_score,threshold=1,
        floor=original_coupled_floor,floor_max_depth=0,
        max_nodes=400,max_leaves=130)
    threshold_replay=replay_cover(
        threshold_tree,independent_original_score,
        floor=original_coupled_floor,max_nodes=400,max_leaves=130)
    if threshold_replay["certified_cylinder_score_lower"]>minimum:
        raise AssertionError("joint threshold proof exceeded independently exact minimum")
    if threshold_replay["positive_threshold_proven"]!=(minimum>=1):
        raise AssertionError("threshold proof does not match exact cylinder minimum")
    base=independent_original_score(dict(enumerate(g68)))
    if base!=68 or right_first_independent(f,g68)["S_seven"]!=68:
        raise AssertionError("baseline original right-first score drift")

    # Find the exact minimizer from a THIRD method: a full coherent permutation
    # over the five currently unused physical K6 edges. The verifier above
    # already rescored every entire leaf by original-left source enumeration.
    available=tuple(e for e in range(15) if e not in pins.values())
    candidates=[]
    for rest in permutations(available,5):
        whole=tuple(pins[i] if i in pins else rest[i-10] for i in range(15))
        candidates.append((template_pullback_score(fibers,whole)["S_seven"],whole))
    chosen_score,chosen=min(candidates)
    if (len(candidates)!=120 or chosen_score!=minimum or
            right_first_independent(f,chosen)["S_seven"]!=minimum):
        raise AssertionError("independent exact global cylinder minimum/original oracle drift")

    matrix=compiled_matrix(source,6,15)
    mu=matrix["mean"]
    projection=exact_pair_projection(matrix["matrix"],6,15)
    p68=evaluate_projection(projection,tuple(K6_PAIRS[e] for e in g68),6)
    if mu!=Fraction(870476,5005) or p68!=Fraction(-6875243,60060):
        raise AssertionError("genuine original B8-E rational projection drift")
    residual=Fraction(68)-mu-p68
    if residual!=Fraction(73373,8580):
        raise AssertionError("genuine original nonlinear residual drift")
    joint_lower=Fraction(minimum)-mu
    if joint_lower != min(
            Fraction(score)-mu for score,_ in candidates):
        raise AssertionError("W32 exact joint P2+R score reconstruction changed")

    proof={"schema":"hyp105.c24b8i.hosted-w32-proof.v1",
           "exact_tree":exact_tree,
           "threshold_tree":threshold_tree}
    encoded=json.dumps(proof,sort_keys=True,separators=(",",":")).encode("utf-8")
    if output_path is not None:
        path=Path(output_path)
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(encoded+b"\n")
    return {
        "slice":"HYP-105-C24-B8-I",
        "exact_parent_B8H_head":"68285a146e6987276e6938261926e4743fe0ffbe",
        "original_W32_left_eligible_original_sixsets":source["static_eligible"],
        "frozen_original_right_lines":len(pins),
        "free_original_right_lines":len(order),
        "whole_global_right_completions_verified":120,
        "exact_cylinder_minimum_S":minimum,
        "exact_cylinder_minimizer":list(chosen),
        "score_at_original_g68":68,
        "source_bucket_joint_floor_at_root":original_coupled_floor(pins),
        "proof_tree_exact_nodes":exact_replay["node_count"],
        "proof_tree_exact_leaves":exact_replay["whole_global_injection_leaf_count"],
        "threshold_tree_nodes":threshold_replay["node_count"],
        "threshold_tree_pruned_subtrees":threshold_replay["pruned_subtree_count"],
        "threshold_one_positive_floor_certified":threshold_replay["positive_threshold_proven"],
        "verified_global_branch_coverage":True,
        "independent_full_left_sixset_replay_each_leaf":True,
        "independent_right_first_original_minimizer":True,
        "mean":str(mu),
        "g68_P2":str(p68),
        "g68_nonlinear_R":str(residual),
        "joint_exact_cylinder_P2_plus_R_lower":str(joint_lower),
        "canonical_proof_bundle_sha256":sha256(encoded).hexdigest(),
        "NO_global_15_factorial_or_all_f_h_omega_s6_claim":True,
    }


if __name__=="__main__":
    print(json.dumps(report("artifacts/hyp105-c24b8i-w32-proof.json"),
                     indent=2,sort_keys=True))
