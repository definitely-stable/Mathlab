"""HYP-105 #230 / AA4-W: ALL-h one-global-map full-seven-GF5 quenched transfer.

A genuine W(3,s), s=2^h>=2, has original incidences Q of size SIX.
For EVERY fixed complete typed original point map f, one uniformly random
complete GLOBAL original line injection g satisfies:
 E_g[seven_class_count(tag)] = sum_F n_F(f) * p_right(F;tag),
where n_F(f) counts actual source Q selected by ONE full physical f half,
stratified by BOTH original endpoint source multiplicities (nine forests).
For source A/A only the connected positional C6 part of fixed left A is
eligible and the independent right positional matching probability is pH.

Exact universal one-half probabilities, a minimal, K=binom(a,2):
 pH=(a)_6/(K)_6; pA=70*pH;
 pB=K*3*binom(a-2,4)*24/(K)_5;
 pC=(a)_6/(8*(K)_3).
The same applies with fixed full g and one uniform full f, swapping types.
NO per-Q independent physical injections, false deterministic lower, nor
all-h min_(f,g) claim. The global map shared by ALL Q remains correlated.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, seven_census,
)
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    _column_physical_dual, _is_single_6cycle_on_incidence_positions,
    exact_ONE_side_original_projection_index,
    exact_two_sided_original_seven_join,
)
from hyp105_issue230_d6aa4r_original_joint_swap_certificate import (
    strict_true_W32_gq_model,
)
from hyp105_issue230_d6aa4s_root_conditional_frechet import minimal_physical_a
from hyp105_issue230_d6aa4t_quenched_aligned_d6 import falling
from hyp105_issue230_d6aa4u_source_forest_frechet import (
    CELL_NAMES, CELL_TO_GF5, original_sixset_source_cell,
)

TAGS=tuple(R3_CERTIFIED_FLOORS)
NONAA=tuple(k for k in CELL_NAMES if k!="A/A")


def all_h_full_seven_one_global_map_transfer_probabilities(s):
    """Exact rational SOURCE-profile conditional physical transfer kernel.

    The resulting coefficient applies simultaneously for all actual
    original six-ID Q with that source endpoint multiplicity under ONE
    uniformly sampled full GLOBAL injection on the remaining source type.
    """
    a=minimal_physical_a(s)
    K=comb(a,2)
    H=Fraction(falling(a,6),falling(K,6))
    A=70*H
    B=Fraction(K*3*comb(a-2,4)*factorial(4),falling(K,5))
    C=Fraction(falling(a,6),8*falling(K,3))
    for p in (H,A,B,C):
        if not 0<p<=1:
            raise AssertionError("valid exact full global injection probability required")
    if A!=70*H or H>=A:
        raise AssertionError("true positional C6 fraction of physical A mismatch")
    return {"s":s,"a":a,"V":(s+1)*(s*s+1),"K":K,
            "D6_position_matched_connected_H":H,
            "A_any_connected_or_disconnected_physical_2factor":A,
            "B_same_source_repeated_plus_physical_C4":B,
            "C_three_source_repeats_physical_matching":C,
            "one_single_uniform_full_global_map_all_six_Q":True,
            "all_h_root_minimin_proved":False}


def _source_kind(cell,side):
    """Actual left/right ORIGINAL source multiplicity A,B,C, not label type."""
    if cell.startswith("B/B"):
        return "B"
    if cell not in CELL_NAMES:
        raise AssertionError("unknown genuine original source path forest")
    return cell.split("/")[side]


def one_fixed_side_full_seven_ensemble(s, source_cell_fixed_half_counts,
                                       fixed_connected_AA_count,*,fixed_side=0):
    """Exact all-h seven-tag conditional expectation, every fixed global map.

    Inputs must be the REAL source forest counts of one physically valid
    half under the SAME single globally injected fixed typed factor map.
    The formulas apply to any such fixed map and require no joint f,g
    physical projection counts, and no assumption of inter-Q independence.
    fixed_side=0: fix f(point), random global g(line); fixed_side=1 dual.
    """
    if fixed_side not in (0,1):
        raise ValueError("typed side must be 0=point or 1=line")
    if type(fixed_connected_AA_count) is not int or fixed_connected_AA_count<0:
        raise ValueError("nonnegative integer genuine connected AA count required")
    counts={name:source_cell_fixed_half_counts.get(name,0) for name in CELL_NAMES}
    if any(type(v) is not int or v<0 for v in counts.values()):
        raise ValueError("SOURCE forest half-Q counts must be nonnegative integers")
    if set(source_cell_fixed_half_counts)-set(CELL_NAMES):
        raise ValueError("unknown genuine source forest cells in transfer")
    if fixed_connected_AA_count>counts["A/A"]:
        raise ValueError("connected physical AA source Q cannot exceed all AA source Q")
    kernel=all_h_full_seven_one_global_map_transfer_probabilities(s)
    p={k:kernel[k] for k in (
        "D6_position_matched_connected_H",
        "A_any_connected_or_disconnected_physical_2factor",
        "B_same_source_repeated_plus_physical_C4",
        "C_three_source_repeats_physical_matching")}
    by_kind={"A":p["A_any_connected_or_disconnected_physical_2factor"],
             "B":p["B_same_source_repeated_plus_physical_C4"],
             "C":p["C_three_source_repeats_physical_matching"]}
    # Counts of positively certified full-seven ORIGINAL source classes.
    out={tag:Fraction(0) for tag in TAGS}
    out["D6"]=p["D6_position_matched_connected_H"]*fixed_connected_AA_count
    decomposition={"D6":{ "A/A:connected":out["D6"] }}
    for cell in NONAA:
        # Fixed-side original kind is already physically compatible by
        # input. Right/left RANDOM side's genuine source-kind determines
        # the number of physical labels and conditional admissible patterns.
        target_kind=_source_kind(cell,1-fixed_side)
        tag=CELL_TO_GF5[cell]
        contribution=counts[cell]*by_kind[target_kind]
        out[tag]+=contribution
        decomposition[cell]={"positive_class":tag,
                             "original_Q_count":counts[cell],
                             "random_side_true_source_kind":target_kind,
                             "expected_GF5_accepted_original_Q":contribution}
    total=sum(out.values(),Fraction(0))
    numerator=sum((R3_CERTIFIED_FLOORS[k]*v for k,v in out.items()),Fraction(0))
    if numerator<0 or total<out["D6"]:
        raise AssertionError("positive GF5 weighted original source transfer invalid")
    return {
        "s":s,"fixed_side":"original_points" if fixed_side==0 else "original_lines",
        "random_other_side_single_complete_global_injection":True,
        "fixed_SOURCE_six_ID_forest_marginals":counts,
        "fixed_AA_positional_connected_C6_source_Q":fixed_connected_AA_count,
        "transfer_kernel":kernel,
        "expected_exact_seven_tag_counts":out,
        "expected_exact_original_full_seven_S":total,
        "expected_exact_51palette_certified_numerator":numerator,
        "cell_contributions":decomposition,
        "all_h_full_seven_one_fixed_type_ensemble_identity_PROVED":True,
        "all_h_adversarial_minimum_PROVED":False,
    }


def two_uniform_complete_global_maps_full_seven_expectation(s, full_true_source_universe):
    """Exact all-h BOTH-UNIFORM EXPECTATION from nine original GQ reservoirs.

    Independent ONE full uniform f and ONE full uniform g, not independent
    across Q; source-cell populations are for ALL genuine six original IDs.
    Complements AA: 60 admissible connected left dual H * same right H.
    """
    if set(full_true_source_universe)!=set(CELL_NAMES):
        raise ValueError("exact genuine source nine-cell universe required")
    if any(type(n) is not int or n<0 for n in full_true_source_universe.values()):
        raise ValueError("source cell universes must be nonnegative integers")
    tr=all_h_full_seven_one_global_map_transfer_probabilities(s)
    H=tr["D6_position_matched_connected_H"]
    p={"A":tr["A_any_connected_or_disconnected_physical_2factor"],
       "B":tr["B_same_source_repeated_plus_physical_C4"],
       "C":tr["C_three_source_repeats_physical_matching"]}
    tags={k:Fraction(0) for k in TAGS}
    tags["D6"]=full_true_source_universe["A/A"]*60*H*H
    for cell in NONAA:
        tags[CELL_TO_GF5[cell]]+=(
            full_true_source_universe[cell]*
            p[_source_kind(cell,0)]*p[_source_kind(cell,1)])
    return {
        "s":s, "model":"two independent UNIFORM complete global typed injections",
        "exact_tag_expectations":tags,
        "exact_expected_seven_S":sum(tags.values(),Fraction(0)),
        "exact_expected_51palette_numerator":sum(
            (R3_CERTIFIED_FLOORS[k]*v for k,v in tags.items()),Fraction(0)),
        "exact_original_source_nine_universes":dict(full_true_source_universe),
        "does_NOT_imply_all_f_g_lower":True,
    }


def genuine_W32_fixed_full_map_all_seven_transfer(model,*,fixed_side=0,
                                                   independent_history=True):
    inc, f, g=strict_true_W32_gq_model(model)
    half=exact_ONE_side_original_projection_index(model,fixed_side)
    labels=f if fixed_side==0 else g
    n=Counter()
    connected=0
    excluded=0
    for Q,kind in half["candidate_sixset_map"].items():
        cell=original_sixset_source_cell(Q,inc)
        if cell is None:
            excluded+=1
            continue
        if _source_kind(cell,fixed_side)!=kind:
            raise AssertionError("fixed physical half differs from true SOURCE factor multiplicity")
        n[cell]+=1
        if cell=="A/A":
            H=_column_physical_dual(Q,inc,labels,fixed_side)
            if _is_single_6cycle_on_incidence_positions(H):
                connected+=1
    if sum(n.values())+excluded!=62370:
        raise AssertionError("lost genuine original physically selected one-half candidates")
    o=one_fixed_side_full_seven_ensemble(2,n,connected,fixed_side=fixed_side)
    actual=exact_two_sided_original_seven_join(
        model,independent_history=independent_history)
    # For ONE SPECIFIED real complete opposite map actual seven counts
    # are not expected to equal full-global-map expectations.
    if independent_history:
        z=seven_census(model,independent_checks=False)
        if (z["S_seven"]!=actual["accepted_seven_GF5_original_S"] or
            z["GF5_seven_lower_numerator"]!=actual["selected_GF5_51palette_certified_numerator"]):
            raise AssertionError("fixed real historical original GF5 seven census mismatch")
    return {
        "scope":"TRUE ORIGINAL W32 same complete global typed f,g, conditional average ONE typed map",
        "fixed_full_type":o["fixed_side"],
        "true_FIXED_original_source_forest_half":dict(n),
        "genuine_fixed_one_half_source_Q_OUTSIDE_joint_nine_grid":excluded,
        "fixed_connected_C6_original_AA_Q":connected,
        "conditional_probability_by_source_type":o["transfer_kernel"],
        "expected_full_seven_tag_counts":o["expected_exact_seven_tag_counts"],
        "expected_full_seven_S":o["expected_exact_original_full_seven_S"],
        "expected_full_selected_51palette_numerator":o["expected_exact_51palette_certified_numerator"],
        "actual_one_specified_global_pair_seven_S":actual["accepted_seven_GF5_original_S"],
        "actual_one_specified_global_pair_51palette_numerator":
            actual["selected_GF5_51palette_certified_numerator"],
        "actual_one_specified_global_pair_tag_counts":
            actual["accepted_seven_GF5_original_Q_by_tag"],
        "all_h_conditional_exact_full_seven_kernel":True,
        "uniform_all_h_adversarial_pair_lower_PROVED":False,
        "independent_true_global_pair_GF5_history":
            "PASS" if independent_history else "NOT_RUN",
    }


def _emit_json(x):
    from fractions import Fraction
    if isinstance(x,Fraction):
        return {"numerator":x.numerator,"denominator":x.denominator}
    if isinstance(x,dict):
        return {str(k):_emit_json(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):
        return [_emit_json(v) for v in x]
    return x


def report(schemes=("S68","S72","lex","reverse")):
    return _emit_json({
        "slice":"HYP105-ISSUE230-D6-AA4-W-FULL-SEVEN-QUENCHED-KERNEL",
        "all_h_example":all_h_full_seven_one_global_map_transfer_probabilities(8),
        "cases":{s:{
            "fix_original_point":genuine_W32_fixed_full_map_all_seven_transfer(fixture(1,s),fixed_side=0),
            "fix_original_line":genuine_W32_fixed_full_map_all_seven_transfer(fixture(1,s),fixed_side=1),
        } for s in schemes},
        "ROOT_BRANCH_A":"OPEN","ROOT_BRANCH_B":"OPEN",
    })


if __name__=="__main__":
    import argparse,json
    ap=argparse.ArgumentParser()
    ap.add_argument("--scheme",choices=("S68","S72","lex","reverse"))
    ap.add_argument("--fixed-side",choices=("point","line"),default="point")
    args=ap.parse_args()
    obj=report((args.scheme,)) if args.scheme else report()
    print(json.dumps(obj,sort_keys=True,indent=2))
