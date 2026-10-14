"""HYP-105 #230 D6-AA4-H: exact rational capacity dual + ORIGINAL source profiles.

The all-h Lagrangian inequality is valid for genuine complete typed injections.
Finite candidate-universe calculations certify ONLY the precisely enumerated
candidate set. True W32 whole-seven sixset results are frozen-outside finite
fibers, not a universal W(3,s) proof. No asserted standard SA/SOS solution.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_issue230_d6aa4g_overlap_capacity import (
    complete_fixed_image_states, analytical_X_Y_capacity_checks,
)


def exact_one_cut_lagrangian(rows):
    """Exact max_{lambda>=0} min_i (cost_i+lambda*violation_i).

    Each row describes a candidate in an EXPLICIT finite universe U,
    with nonnegative rational cost and a rational signed globally-valid
    upper-cut violation g_i (valid real complete assignments obey g<=0).
    For a genuine-original theorem U MUST contain all actual assignments
    whose minimum is claimed. A pseudo row is never automatically real.
    """
    if not rows or len(rows)>100000:
        raise ValueError("nonempty explicitly bounded finite candidate universe required")
    data=[]
    for name,cost,violation in rows:
        if not isinstance(name,str) or not name or any(name==n for n,_,_ in data):
            raise ValueError("candidate names must be nonempty and unique")
        c,g=Fraction(cost),Fraction(violation)
        if c<0:
            raise ValueError("negative source-motif cost")
        data.append((name,c,g))
    if all(g>0 for _,_,g in data):
        raise ValueError("no feasible real candidate: dual is unbounded")
    prices={Fraction(0)}
    for i,(_,ci,gi) in enumerate(data):
        for _,cj,gj in data[:i]:
            if gi!=gj:
                crossing=Fraction(cj-ci,gi-gj)
                if crossing>=0:
                    prices.add(crossing)
    def evaluate(lam):
        scored=[(c+lam*g,name) for name,c,g in data]
        val=min(v for v,_ in scored)
        active=tuple(n for v,n in scored if v==val)
        return val,active
    optimum=None
    for lam in sorted(prices):
        val,active=evaluate(lam)
        if optimum is None or val>optimum[0]:
            optimum=(val,lam,active)
    value,price,active=optimum
    # Independent feasibility and a constructive audit of exact rational
    # support: the lower affine envelope achieves its maximum at a
    # nonnegative endpoint or at one of ALL nonnegative intersections.
    if any(c+price*g<value for _,c,g in data):
        raise AssertionError("claimed rational capacity dual bound false")
    return {
        "candidate_universe_size":len(data),
        "unconstrained_candidate_cost_floor":str(min(c for _,c,_ in data)),
        "optimal_one_cut_dual_lower":str(value),
        "nonnegative_exact_cut_multiplier":str(price),
        "active_candidates":active,
        "all_affine_breakpoints_enumerated":len(prices),
        "only_valid_for_this_explicit_candidate_universe":True,
    }


def toy_capacity_source_coupling(s):
    """D6-X/Y obstruction + exact dual pricing on a clearly synthetic 2-row model.

    The feasible row cost 1 is a SYNTHETIC control, NOT an actual GF5
    positive count. The pseudo row cost 0 comes from an ASSUMED surrogate
    objective; no implied source-GQ feasibility or global R3 statement.
    """
    z=analytical_X_Y_capacity_checks(s)
    if s<4 or not z["D6Y_selected_two_site_gap"]>0:
        raise ValueError("toy requires s>=4 and positive missing-edge gap")
    gap=z["D6Y_selected_two_site_gap"]
    image=exact_one_cut_lagrangian((
        ("SYNTHETIC_feasible_control_cost_one",1,0),
        ("D6Y_unextendible_zero_surrogate",0,gap),
    ))
    star=-Fraction(z["D6X_star_pseudo_column_lift_slack"])
    if star<=0:
        raise AssertionError("D6-X star-pseudo lifted capacity regression drift")
    lifted=exact_one_cut_lagrangian((
        ("SYNTHETIC_feasible_control_cost_one",1,0),
        ("D6X_unextendible_zero_surrogate",0,star),
    ))
    if (Fraction(image["optimal_one_cut_dual_lower"])!=1
        or Fraction(image["nonnegative_exact_cut_multiplier"])!=Fraction(1,gap)
        or Fraction(lifted["optimal_one_cut_dual_lower"])!=1
        or Fraction(lifted["nonnegative_exact_cut_multiplier"])!=1/star):
        raise AssertionError("capacity cannot falsify synthetic zero surrogate")
    return {
        "s":s,"true_physical_adjacency_upper":z[
            "all_real_images_max_adjacent_pairs"],
        "D6Y_false_expected_adjacency":z["D6Y_selected_two_site_pseudo_adjacent_pairs"],
        "D6Y_valid_cut_violation":gap,
        "D6X_lifted_capacity_violation":str(star),
        "image_cut_dual":image,"lifted_column_cut_dual":lifted,
        "all_GF5_objectives_in_toys_are_synthetic":True,
        "neither_pseudo_claimed_global_or_standard_SA_feasible":True,
        "no_universal_source_GQ_lower":True,
    }


def greedy_original_profile_cover(profile_rows):
    """Sparse genuine-profile cover of EVERY complete tested source state.

    profile_rows: unique tuple(profile, positive-state mask) pairs.
    This is a verifiable CONSTRUCTIVE cover, never called minimum-cardinality.
    """
    rows=tuple((tuple(p),int(mask)) for p,mask in profile_rows)
    if not rows or any(not p or m<=0 for p,m in rows):
        raise ValueError("nonempty ORIGINAL positive source profiles required")
    if len(set(p for p,_ in rows))!=len(rows):
        raise ValueError("duplicate original profile")
    n=max(mask.bit_length() for _,mask in rows)
    if not 1<=n<=24 or any(mask>=1<<n for _,mask in rows):
        raise ValueError("unsupported exhaustive state count")
    full=(1<<n)-1
    if not any(mask & full for _,mask in rows):
        raise AssertionError("no accepted original positive witnesses")
    uncovered=full
    chosen=[]
    while uncovered:
        ranked=sorted((-(m&uncovered).bit_count(),p,m) for p,m in rows)
        gainneg,profile,mask=ranked[0]
        if gainneg==0:
            raise AssertionError("some genuine complete source state has no positive Q")
        chosen.append((profile,mask))
        uncovered &= ~mask
        if len(chosen)>n:
            raise AssertionError("greedy cover failed at most-one-new-state bound")
    union=0
    for _,mask in chosen:
        union |= mask
    if union!=full:
        raise AssertionError("source-profile cover misses complete global assignment")
    return {
        "complete_states_covered":n,
        "active_original_source_profiles":len(rows),
        "greedy_profiles_used":len(chosen),
        "greedy_selected_original_line_multisets":tuple(p for p,_ in chosen),
        "selected_original_profile_24bit_masks":tuple(mask for _,mask in chosen),
        "independently_verified_cover_mask":full,
        "minimum_size_NOT_claimed":True,
    }


def _original_w32_line_profile_fiber(scheme):
    """One globally shared g for ALL true-original six-incidence Q in each state."""
    from hyp105_issue230_projection import fixture
    from hyp105_g5e2b3e1b0_seven_signature import (
        R3_CERTIFIED_FLOORS,seven_census)
    from hyp105_issue230_d6aa4c_edit_transversal import (
        genuine_original_positive_hypergraph, incidence_cover_bits)
    from hyp105_issue230_d6aa4d_mixed_transversal_fibers import (
        finite_source_support_partition)
    if scheme not in ("S68","S72"):
        raise ValueError("pinned genuine ORIGINAL W32 only")
    model=fixture(1,scheme)
    records=genuine_original_positive_hypergraph(model)["records"]
    bits,weights,mask=incidence_cover_bits(records)
    partition=finite_source_support_partition(bits,weights,mask)
    if partition["number_transversal_blocks"]!={"S68":53,"S72":119}[scheme]:
        raise AssertionError("AA4D exact size-four source transversal baseline drift")
    block=next((b for b in partition["transversal_original_factor_blocks"]
                if len(b)==4 and all(i>=15 for i in b)),None)
    if block is None:
        raise AssertionError("no genuine original four-LINE transversal")
    original_incidence=tuple(tuple(x) for x in model["incidences"])
    if len(original_incidence)!=45:
        raise AssertionError("original W32 GQ 45 source incidences missing")
    fixed_left=tuple(tuple(x) for x in model["left_labels"])
    fixed_right=tuple(tuple(x) for x in model["right_labels"])
    original_line_ids=tuple(i-15 for i in block)
    baseline=tuple(fixed_right[i] for i in original_line_ids)
    states=complete_fixed_image_states(("L",)*4,baseline)
    if len(states)!=24:
        raise AssertionError("24 complete ORIGINAL line four-factor states missing")
    full=[]
    all_Q=set()
    for state in states:
        right=list(fixed_right)
        for i,edge in zip(original_line_ids,state):
            right[i]=edge
        census=seven_census({**model,"left_labels":fixed_left,
                            "right_labels":tuple(right)},
                           independent_checks=False,witness_sets=True)
        if census["S_seven"]!=len(census["sets"]):
            raise AssertionError("real ORIGINAL six-incidence classification inconsistent")
        if census["GF5_seven_lower_numerator"]!=sum(
             R3_CERTIFIED_FLOORS[tag] for tag in census["sets"].values()):
            raise AssertionError("real ORIGINAL GF5 51-column numerator inconsistent")
        full.append(census)
        all_Q.update(census["sets"])
    if full[0]["S_seven"]!={"S68":68,"S72":72}[scheme]:
        raise AssertionError("baseline map must be the genuine pinned source scheme")
    profile_counts=defaultdict(lambda:[0]*24)
    profile_weights=defaultdict(lambda:[0]*24)
    profile_sets=defaultdict(set)
    for Q in sorted(all_Q):
        if len(Q)!=6 or len(set(Q))!=6:
            raise AssertionError("not six original DISTINCT incidence IDs")
        profile=tuple(sorted(original_incidence[i][1] for i in Q))
        if len(profile)!=6:
            raise AssertionError("unfaithful ORIGINAL repeated line multiplicity")
        touched=tuple(j for j,i in enumerate(original_line_ids)
                      if i in profile)
        by_projection={}
        for k,(state,census) in enumerate(zip(states,full)):
            tag=census["sets"].get(Q)
            key=tuple(state[j] for j in touched)
            if key in by_projection and by_projection[key]!=tag:
                raise AssertionError("ORIGINAL GF5 Q class depends on unmentioned source factor")
            by_projection[key]=tag
            if tag is not None:
                profile_counts[profile][k]+=1
                profile_weights[profile][k]+=R3_CERTIFIED_FLOORS[tag]
                profile_sets[profile].add(Q)
    reconstructed=tuple(sum(row[k] for row in profile_counts.values())
                        for k in range(24))
    true_costs=tuple(c["S_seven"] for c in full)
    if reconstructed!=true_costs:
        raise AssertionError("per-ORIGINAL-profile sixset count did not reconstruct")
    weighted=tuple(sum(row[k] for row in profile_weights.values())
                   for k in range(24))
    if weighted!=tuple(c["GF5_seven_lower_numerator"] for c in full):
        raise AssertionError("ORIGINAL sixset profile GF5 numerator recomposition failed")
    profile_independent=sum(min(x) for x in profile_counts.values())
    weighted_independent=sum(min(x) for x in profile_weights.values())
    active_masks=tuple(sorted((profile,sum(
        1<<k for k,n in enumerate(row) if n>0))
        for profile,row in profile_counts.items()))
    cover=greedy_original_profile_cover(active_masks)
    if cover["complete_states_covered"]!=24:
        raise AssertionError("false coherent 24-state original source profile cover")
    for k in range(24):
        if sum(int(profile_counts[p][k]>0)
               for p in cover["greedy_selected_original_line_multisets"])<1:
            raise AssertionError("sparse ORIGINAL profile proof did not cover real map")
    lower_expected={"S68":68,"S72":68}[scheme]
    if min(true_costs)!=lower_expected:
        raise AssertionError("AA4G hosted coherent source four-line minimum drift")
    if not 0<=profile_independent<=lower_expected:
        raise AssertionError("original-profile independent relaxation unsound")
    # W32 V=K=15: EVERY true typed global image is the FULL K6.
    # Its physical adjacency sum is EXACTLY 6*C(5,2)=60; no scalar
    # global missing-edge IMAGE bound can penalize an abstract relaxed
    # profile-state assigned this exact full-image scalar observable.
    bound=analytical_X_Y_capacity_checks(2)
    if not (bound["K"]==bound["V"]==15 and bound["m"]==0 and
            bound["all_real_images_max_adjacent_pairs"]==60):
        raise AssertionError("true W32 physical image not complete K6")
    rows=[("ORIGINAL_real_state_%02d"%i,score,0)
          for i,score in enumerate(true_costs)]
    rows.append(("ABSTRACT_independent_profile_relaxation",
                 profile_independent,0))
    scalar=exact_one_cut_lagrangian(rows)
    if Fraction(scalar["optimal_one_cut_dual_lower"])!=profile_independent:
        raise AssertionError("zero-slack W32 image-only dual spuriously closes source gap")
    return {
        "scheme":scheme,"source_factor_type":"ORIGINAL_LINE",
        "four_original_factor_ids":block,
        "complete_global_typed_injection_states":24,
        "original_Q_candidates_evaluated_per_complete_state":62370,
        "distinct_original_Q_positive_in_any_state":len(all_Q),
        "active_original_six_incidence_line_profiles":len(profile_counts),
        "sum_independent_original_profile_minima":profile_independent,
        "sum_independent_original_profile_GF5_numerator_minima":weighted_independent,
        "minimum_exact_complete_global_S":min(true_costs),
        "minimum_exact_complete_global_GF5_numerator":min(weighted),
        "complete_all_24_true_original_S_scores":true_costs,
        "complete_all_24_true_GF5_numerator_scores":weighted,
        "greedy_original_line_profile_cover":cover,
        "W32_full_physical_image_adjacent_pairs":60,
        "scalar_image_capacity_dual_inability_to_close_relaxation_gap":scalar,
        "no_claim_about_multivariate_ORIGINAL_source_capacity_joint_LP":True,
        "no_all_W32_or_all_h_universal_positive_result":True,
    }


def report(scheme=None):
    out={
        "slice":"HYP105-ISSUE230-D6-AA4-H-SOURCE-CAPACITY-DUAL",
        "all_h_weak_dual_only_for_valid_complete_coverage":True,
        "toy_s4":toy_capacity_source_coupling(4),
        "root_A":"OPEN","root_B":"OPEN",
        "full_GF5_R3_proved":False,
        "ASET_exponent_proved":False,
        "independent_mathematical_peer_review":"OPEN",
    }
    if scheme is not None:
        out["true_original_W32"]= _original_w32_line_profile_fiber(scheme)
    return out


if __name__=="__main__":
    import argparse,json
    p=argparse.ArgumentParser()
    p.add_argument("--scheme",choices=("S68","S72"))
    args=p.parse_args()
    print(json.dumps(report(args.scheme),indent=2,sort_keys=True))
