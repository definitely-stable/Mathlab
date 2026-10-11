"""B8-C explicitly budgeted genuine ORIGINAL W(3,2) conditional-mean oracle.

Runs ONLY in dedicated GitHub-hosted Contract, not default unittest
discover. Cross-check compressed ORIGINAL source multiplicities against
independent 62,370 sixsets enumerated under ONE fixed complete left f.
No 11,236-state mixed orbit, no enumeration of 15! right maps.
"""
from collections import Counter
from fractions import Fraction
import json

from hyp105_g5e2b3e1c24_right_c_certificate import K6_PAIRS
from hyp105_g5e2b3e1c24b_three_collision import W32_LEFT_H45
from hyp105_g5e2b3e1c24b6_mixed_curvature_s68 import W32_RIGHT_S68
from hyp105_g5e2b3e1c24b2_joint_seven import (
    TAGS, compile_left, full_left_score, right_first_independent,
)
from hyp105_g5e2b3e1c24b8a_physical_tensor import source_profile
from hyp105_g5e2b3e1c24b8a_w32_tensor_witness import (
    independently_enumerate_left_original_sixsets,
)
from hyp105_g5e2b3e1c24b8b_signed_physical_balance import PROFILE_C
from hyp105_g5e2b3e1c24b8c_conditional_discrepancy import (
    right_mean_from_compiled_left,
    right_mean_from_independent_sixsets,
    exact_centered_discrepancy,
    two_edge_orbit_certificate,
)


def renumber_one_physical_right_coordinate(global_g, vertex_a, vertex_b):
    """A physical S6 coordinate relabeling acting on RIGHT maps ONLY."""
    physical={e:i for i,e in enumerate(K6_PAIRS)}
    x=[]
    for idx in global_g:
        e=K6_PAIRS[idx]
        new=tuple(sorted(vertex_b if t==vertex_a else
                         vertex_a if t==vertex_b else t for t in e))
        x.append(physical[new])
    if set(x)!=set(range(15)):
        raise AssertionError("coordinate permutation lost complete global injection")
    return tuple(x)


def report():
    f0,g0=tuple(W32_LEFT_H45),tuple(W32_RIGHT_S68)
    src=compile_left(f0)
    comp=right_mean_from_compiled_left(src,6)
    original=independently_enumerate_left_original_sixsets(f0)
    if len(original)!=62370:
        raise AssertionError("genuine ORIGINAL W32 fixed-left source changed")
    f_map={p+1:K6_PAIRS[e] for p,e in enumerate(f0)}
    direct=right_mean_from_independent_sixsets(original,f_map,6)
    if (direct["conditional_right_mean"] != comp["conditional_right_mean"]
            or direct["by_tag_expected"] != comp["by_tag_expected"]
            or direct["by_tag_population"] != comp["by_tag_population"]
            or direct["source_candidates_examined"]!=62370):
        raise AssertionError("independent original uncompressed W32 mean disagrees with source fibers")
    s0=full_left_score(src,g0)
    if s0["S_seven"]!=68 or right_first_independent(f0,g0)["S_seven"]!=68:
        raise AssertionError("frozen original W32 S68 genuine complete g changed")
    discrepancy=exact_centered_discrepancy(comp["conditional_right_mean"],68)
    right_invariant=[]
    for a,b in ((0,1),(0,4),(2,5)):
        modified=renumber_one_physical_right_coordinate(g0,a,b)
        new=full_left_score(src,modified)
        if new!=s0:
            raise AssertionError("independent RIGHT-only physical S6 action changed seven-vector")
        right_invariant.append((a,b))
    # Only explicit right-C profile sources, to check the hard-zero
    # adjacency obstruction in a TRUE ORIGINAL finite GQ source.
    witness=None
    for six in sorted(original):
        t=source_profile(six)
        rp=tuple(sorted(Counter(l for _,l in six).values(),reverse=True))
        if t is not None and rp==PROFILE_C:
            lines=sorted({l for _,l in six})
            candidate=two_edge_orbit_certificate(
                six,f_map,6,lines[0],lines[1])
            if (candidate["two_adjacent_pins_mean"]!=0
                    or candidate["two_disjoint_pins_mean"]<=0):
                raise AssertionError("physical three-double-edge C matching obstruction invalid")
            witness={"original_sixset":six,"right_line_pair":lines[:2],
                     "tag":t,"two_orbit":candidate}
            break
    if witness is None:
        raise AssertionError("genuine original W32 contains no certified static right C motif")
    return {
        "slice":"HYP-105-C24-B8-C",
        "left_global_complete_permutation":f0,
        "right_global_complete_S68_permutation":g0,
        "original_left_candidate_sixsets":len(original),
        "original_static_seven_tag_eligible":src["static_eligible"],
        "by_tag_population":comp["by_tag_population"],
        "by_tag_expected_str":{t:str(comp["by_tag_expected"][t]) for t in TAGS},
        "conditional_right_uniform_global_mean_exact":str(comp["conditional_right_mean"]),
        "conditional_right_uniform_global_mean_decimal":float(comp["conditional_right_mean"]),
        "one_valid_original_global_right_score":s0["S_seven"],
        "exact_signed_mean_minus_S68":str(discrepancy["signed_mean_minus_score"]),
        "observed_S68_is_below_conditional_mean":discrepancy["below_mean"],
        "independent_uncompressed_62370_original_sources_confirmed":True,
        "RIGHT_ONLY_coordinate_orbit_invariant_transpositions":right_invariant,
        "genuine_original_W32_right_C_two_edge_hard_zero": {
            "original_sixset":witness["original_sixset"],
            "right_line_pair":witness["right_line_pair"],"tag":witness["tag"],
            "adjacent_conditional_right_mean":str(witness["two_orbit"]["two_adjacent_pins_mean"]),
            "disjoint_conditional_right_mean":str(witness["two_orbit"]["two_disjoint_pins_mean"]),
            "unconditional_right_mean":str(witness["two_orbit"]["unconditional_mean"]),
        },
        "no_global_right_minimum_all_h_positive_lower_or_R3_ASET_claim":True,
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
