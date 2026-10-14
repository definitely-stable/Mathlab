"""HYP-105 #230 D6-AA4-J: exact ORIGINAL source-pair -> true GF5 Q transfer gate.

All-h combinatorial incidence budget and conditional multiplicity-amplification
lemma. Exact genuine W32 original positional seven-census falsification.
No assumed charge from SOURCE pair to positive Q; quantify uncovered pairs.
No universal seven-GF5 lower bound; Branch A/B OPEN.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_issue230_d6aa4i_original_spectral_coordinate import (
    geometry, all_h_source_disjoint_theorem, one_type_spectral_certificate,
)


def _ceil(q):
    q=Fraction(q)
    return -((-q.numerator)//q.denominator)


def conditional_charge_formula(s, multiplicity_per_pair):
    """Honest sufficient ALL-h transfer, NOT an asserted GF5 hypothesis.

    If EVERY original collinear physically-disjoint pair has at least
    multiplicity_per_pair genuine positive ORIGINAL sixsets Q containing
    both source factors, then S>=ceil(multiplicity*D/15). Each six-incidence
    Q has at most 6 distinct source point factors (or line factors), so
    it contains <=C(6,2)=15 source pairs. The necessary gap in AA4-I is
    establishing an all-h lower multiplicity growing linearly with s,
    not relabeling pair counts as sixset counts.
    """
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("s must be 2^h >=2")
    b=Fraction(multiplicity_per_pair)
    if b<0:
        raise ValueError("nonnegative lower multiplicity hypothesis required")
    base=all_h_source_disjoint_theorem(s)
    d=base["uniform_forced_physically_disjoint_collinear_lower"]
    lower=_ceil(Fraction(max(d,0))*b/15)
    return {
        "s":s,"conditional_per_original_pair_positive_Q_minimum":str(b),
        "all_h_source_pair_disjoint_lower":d,
        "all_h_conditional_positive_original_Q_lower":lower,
        "maximum_original_same_type_source_pairs_per_sixset":15,
        "conditionally_valid_if_each_eligible_pair_has_its_Q_multiplicity":True,
        "required_per_pair_growth_for_Omega_s6":"Omega(s)",
        "hypothesis_established_for_all_labels":False,
        "seven_GF5_all_h_positive_bound_proved":False,
    }


def _eligible_pairs(g,labels,source_type):
    z=one_type_spectral_certificate(g,labels,source_type=source_type)
    ns=g["source_point_neighbors" if source_type=="P" else "source_line_neighbors"]
    labels=tuple(tuple(x) for x in labels)
    pairs=frozenset((p,q) for p in range(g["V"]) for q in ns[p]
                    if p<q and not set(labels[p]).intersection(labels[q]))
    if len(pairs)!=z["original_collinear_physically_disjoint"]:
        raise AssertionError("SOURCE pair spectral oracle mismatched independently rebuilt pairs")
    return pairs,z


def charge_original_sixsets(g,model,accepted,*,source_type):
    """Count REAL ORIGINAL Q supporting every forced-disjoint source pair.

    Distinguish weak pair appearance (both distinct ORIGINAL factors occur
    anywhere among Q's six incidences) and strictly same-pencil appearance
    (two Q incidences use both pair factors and their unique common
    ORIGINAL line/point). The latter cannot be inferred from the former.
    NO physical-P3 gating: include ALL genuine accepted seven-GF5 Q.
    """
    from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS
    if source_type not in ("P","L"):
        raise ValueError("true ORIGINAL source type P or L required")
    incumbents=g["original_incidences"]
    accepted=dict(accepted)
    if any(not isinstance(Q,tuple) or len(Q)!=6 or len(set(Q))!=6
           or any(type(i) is not int or not 0<=i<len(incumbents) for i in Q)
           or tag not in R3_CERTIFIED_FLOORS for Q,tag in accepted.items()):
        raise ValueError("every cost must be one accepted true ORIGINAL six-incidence Q")
    labels=model["left_labels" if source_type=="P" else "right_labels"]
    eligible,spectral=_eligible_pairs(g,labels,source_type)
    weak=Counter()
    strict=Counter()
    charges_by_GF5=Counter()
    strict_by_GF5=Counter()
    maximum_per_Q=0
    maximum_same_pencil_per_Q=0
    pairfree_Q=0
    strict_pairfree_Q=0
    for Q,tag in accepted.items():
        endpoints=tuple(incumbents[i] for i in Q)
        position=0 if source_type=="P" else 1
        other=1-position
        by_factor=defaultdict(set)
        for p,l in endpoints:
            x=(p,l)
            by_factor[x[position]].add(x[other])
        touched=set()
        strict_touched=set()
        for u,v in combinations(sorted(by_factor),2):
            pair=(u,v)
            if pair in eligible:
                touched.add(pair)
                if by_factor[u]&by_factor[v]:
                    strict_touched.add(pair)
        if not strict_touched.issubset(touched):
            raise AssertionError("strict pencil source-pair charge not also weak Q charge")
        maximum_per_Q=max(maximum_per_Q,len(touched))
        maximum_same_pencil_per_Q=max(maximum_same_pencil_per_Q,len(strict_touched))
        pairfree_Q+=not touched
        strict_pairfree_Q+=not strict_touched
        for pair in touched:
            weak[pair]+=1
            charges_by_GF5[tag]+=1
        for pair in strict_touched:
            strict[pair]+=1
            strict_by_GF5[tag]+=1
    if maximum_per_Q>15 or maximum_same_pencil_per_Q>15:
        raise AssertionError("true six-incidence Q has >15 same-type source pairs")
    uncovered=tuple(sorted(eligible-set(weak)))
    strict_uncovered=tuple(sorted(eligible-set(strict)))
    D=len(eligible)
    S=len(accepted)
    W=sum(weak.values())
    T=sum(strict.values())
    if len(weak)+len(uncovered)!=D or len(strict)+len(strict_uncovered)!=D:
        raise AssertionError("actual ORIGINAL pair-to-Q coverage partition broken")
    if W!=sum(charges_by_GF5.values()) or T!=sum(strict_by_GF5.values()):
        raise AssertionError("seven-GF5 class charge decomposition lost source pairs")
    if W>15*S or T>W:
        raise AssertionError("unconditional six-incidence pair charge capacity violated")
    # Independent direct pair-major oracle over true ORIGINAL positive Q.
    # It neither uses positive class labels except membership nor the
    # Q-major implementation's by_factor aggregation.
    pair_major=Counter()
    pencil_major=Counter()
    for pair in sorted(eligible):
        for Q in accepted:
            selected=[incumbents[i] for i in Q]
            u,v=pair
            ix=0 if source_type=="P" else 1
            jx=1-ix
            au=[edge[jx] for edge in selected if edge[ix]==u]
            av=[edge[jx] for edge in selected if edge[ix]==v]
            if au and av:
                pair_major[pair]+=1
                if set(au)&set(av):
                    pencil_major[pair]+=1
    if pair_major!=weak or pencil_major!=strict:
        raise AssertionError("independent pair-major ORIGINAL six-incidence oracle disagrees")
    return {
        "source_type":source_type,
        "original_gq_collinear_physically_disjoint_pair_count":D,
        "original_seven_positive_sixsets":S,
        "original_pairs_covered_by_any_positive_sixset":len(weak),
        "original_pairs_not_covered_by_any_positive_sixset":len(uncovered),
        "original_pairs_covered_by_same_pencil_positive_sixset":len(strict),
        "original_pairs_not_covered_by_same_pencil_positive_sixset":len(strict_uncovered),
        "sample_uncovered_source_pair_ids":uncovered[:12],
        "sample_strict_uncovered_source_pair_ids":strict_uncovered[:12],
        "all_genuine_original_pair_to_positive_Q_weak_charges":W,
        "all_genuine_original_pair_to_positive_Q_same_pencil_charges":T,
        "maximum_physically_disjoint_source_pair_charges_in_one_Q":maximum_per_Q,
        "maximum_same_pencil_pair_charges_in_one_Q":maximum_same_pencil_per_Q,
        "original_positive_Q_without_any_eligible_source_pair":pairfree_Q,
        "original_positive_Q_without_any_same_pencil_eligible_source_pair":strict_pairfree_Q,
        "sharp_unconditional_capacity_15_Q_lower_from_weak_charges":
            _ceil(Fraction(W,15)),
        "sharp_unconditional_capacity_15_Q_lower_from_covered_pairs":
            _ceil(Fraction(len(weak),15)),
        "minimum_actual_positive_Q_multiplicity_per_eligible_pair":
            min((weak.get(pair,0) for pair in eligible),default=0),
        "minimum_actual_same_pencil_Q_multiplicity_per_eligible_pair":
            min((strict.get(pair,0) for pair in eligible),default=0),
        "exact_weak_charges_by_seven_GF5_class":
            dict(sorted(charges_by_GF5.items())),
        "exact_same_pencil_charges_by_seven_GF5_class":
            dict(sorted(strict_by_GF5.items())),
        "independent_pair_major_original_incidence_oracle":"PASS",
        "complete_seven_GF5_original_Q_not_P3_filtered":True,
        "no_all_h_pair_to_GF5_transfer_established":True,
        "spectral_pair_count_reproduced":spectral[
            "original_collinear_physically_disjoint"],
    }


def genuine_original_W32_pair_to_Q_audit(scheme):
    """Full historical ORIGINAL 24-state W32 GF5 and two-sided Q charge."""
    from hyp105_issue230_projection import fixture
    from hyp105_g5e2b3e1b0_seven_signature import (
        seven_census,R3_CERTIFIED_FLOORS)
    from hyp105_issue230_d6aa4c_edit_transversal import (
        genuine_original_positive_hypergraph,incidence_cover_bits)
    from hyp105_issue230_d6aa4d_mixed_transversal_fibers import (
        finite_source_support_partition)
    from hyp105_issue230_d6aa4g_overlap_capacity import (
        complete_fixed_image_states)
    if scheme not in ("S68","S72"):
        raise ValueError("only pinned true ORIGINAL W32 S68/S72")
    model=fixture(1,scheme)
    g=geometry(2,model["incidences"])
    rows=genuine_original_positive_hypergraph(model)["records"]
    bits,weights,full_mask=incidence_cover_bits(rows)
    partition=finite_source_support_partition(bits,weights,full_mask)
    if partition["number_transversal_blocks"]!={"S68":53,"S72":119}[scheme]:
        raise AssertionError("genuine original source transversals drift")
    block=next((tuple(q) for q in partition["transversal_original_factor_blocks"]
                if len(q)==4 and all(0<=i<15 for i in q)),None)
    if block is None:
        raise AssertionError("no genuine four-point source transversal")
    baseline=tuple(tuple(model["left_labels"][p]) for p in block)
    states=complete_fixed_image_states(("P",)*4,baseline)
    if len(states)!=24:
        raise AssertionError("missing globally coherent K6 source four-factor fiber")
    fixed_right=tuple(tuple(x) for x in model["right_labels"])
    all_results=[]
    for state in states:
        left=list(tuple(tuple(x) for x in model["left_labels"]))
        for p,lab in zip(block,state):
            left[p]=lab
        x={**model,"left_labels":tuple(left),"right_labels":fixed_right}
        full=seven_census(x,independent_checks=False,witness_sets=True)
        actual=full["sets"]
        if full["S_seven"]!=len(actual) or full["GF5_seven_lower_numerator"]!=sum(
                R3_CERTIFIED_FLOORS[t] for t in actual.values()):
            raise AssertionError("actual true ORIGINAL six-Q GF5 classifier mass drift")
        P=charge_original_sixsets(g,x,actual,source_type="P")
        L=charge_original_sixsets(g,x,actual,source_type="L")
        if (P["original_seven_positive_sixsets"]!=full["S_seven"]
           or L["original_seven_positive_sixsets"]!=full["S_seven"]):
            raise AssertionError("original same-GF5-Q disjoint source pair split")
        all_results.append((full,P,L))
    if all_results[0][0]["S_seven"]!={"S68":68,"S72":72}[scheme]:
        raise AssertionError("baseline is not pinned original full S")
    min_S=min(r[0]["S_seven"] for r in all_results)
    if min_S!={"S68":68,"S72":72}[scheme]:
        raise AssertionError("AA4-I true-source four-point minimum regression")
    summarized={}
    for typ in ("P","L"):
        tmp=[r[1 if typ=="P" else 2] for r in all_results]
        measures=("original_gq_collinear_physically_disjoint_pair_count",
            "original_pairs_not_covered_by_any_positive_sixset",
            "original_pairs_not_covered_by_same_pencil_positive_sixset",
            "all_genuine_original_pair_to_positive_Q_weak_charges",
            "all_genuine_original_pair_to_positive_Q_same_pencil_charges",
            "minimum_actual_positive_Q_multiplicity_per_eligible_pair",
            "minimum_actual_same_pencil_Q_multiplicity_per_eligible_pair",
            "original_positive_Q_without_any_eligible_source_pair")
        summarized[typ]={
            "per_complete_state":tuple(tmp),
            "ranges":{name:{"min":min(r[name] for r in tmp),
                             "max":max(r[name] for r in tmp)}
                      for name in measures},
            "all_24_original_sixset_pair_charge_oracles":"PASS",
            "all_true_source_pair_occupancy_independent_of_physical_P3":True,
        }
    return {
        "scheme":scheme,"original_source_four_point_block":block,
        "complete_true_global_injective_assignments":24,
        "historical_original_sixset_candidates_per_complete_map":62370,
        "minimum_original_seven_positive_Q":min_S,
        "maximum_source_pair_Q_multiplicity_per_Q_all_h":15,
        "original_point_and_line_pair_charge":summarized,
        "branch_A":"OPEN","branch_B":"OPEN",
        "finite_pair_to_GF5_transfer_only":True,
    }


def report(scheme=None):
    result={
        "slice":"HYP105-ISSUE230-D6-AA4-J-ORIGINAL-SOURCE-PAIR-GF5-CHARGE",
        "all_h_s5_original_source_pair_spectral_bound":True,
        "all_h_exact_pair_to_positive_sixset_capacity":15,
        "conditional_all_h_linear_per_pair_multiplicity_yields_s6":
            conditional_charge_formula(4,4),
        "all_h_GF5_positive_lower_proven":False,
        "root_A":"OPEN","root_B":"OPEN","full_R3_proven":False,
        "ASET_exponent_proven":False,
    }
    if scheme:
        result["true_original_W32"]=genuine_original_W32_pair_to_Q_audit(scheme)
    return result


if __name__=="__main__":
    import argparse,json
    p=argparse.ArgumentParser()
    p.add_argument("--scheme",choices=("S68","S72"))
    args=p.parse_args()
    print(json.dumps(report(args.scheme),indent=2,sort_keys=True))
