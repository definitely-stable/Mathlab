"""HYP-105 issue #230 / D6-AA4-L: honest source-pair charge energy frontier.

(1) All-h rigorous existence and counting of ORIGINAL 6-flag sets with
    NO same-type source-collinear pairs for s=2^h>=16.
(2) Real ORIGINAL W(3,8) FULL globally injected positive GF5 D6 sixset
    whose point AND line source-pair charge are BOTH ZERO.
(3) Exact ORIGINAL W32 24-state pair-Q incidence matrix first/second
    moments and independently checked Gram trace energy; quantile gates.
These facts do NOT prove or disprove uniform I_P+I_L=Omega(s^6).
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import factorial
import random

from hyp105_issue230_d6aa4i_original_spectral_coordinate import (
    geometry,all_h_source_disjoint_theorem)
from hyp105_issue230_d6aa4j_source_pair_gf5_charge import (
    _eligible_pairs,_ceil)
from hyp105_issue230_d6aa4k_projection_aware_charge import (
    true_original_projection_charge,six_incidence_projection_capacity)


def separated_original_flag_count_theorem(s):
    """ALL-h guaranteed count of source-separated ORIGINAL 6-flag sets.

    Closed GQ collinearity neighborhoods have size 1+s(s+1) for
    BOTH original points and original lines. After j flags, the
    forbidden original flags are a union of point and line stars;
    at most 2*j*(1+s(s+1))*(s+1). At s>=16, V>10*(k+1).
    Every next flag has a noncollinear point and nonconcurrent line.
    """
    if type(s) is not int or s<16 or s & (s-1):
        raise ValueError("proved greedy six-separated flags for 2^h>=16 only")
    v=(s+1)*(s*s+1)
    k=s*(s+1)
    sizes=tuple((s+1)*(v-2*j*(k+1)) for j in range(6))
    if min(sizes)<=0 or v<=10*(k+1):
        raise AssertionError("all-h greedy original-GQ count positivity failed")
    ordered=1
    for x in sizes:ordered*=x
    lower_unordered=(ordered+factorial(6)-1)//factorial(6)
    return {
        "s":s,"V":v,"original_incidence_count":v*(s+1),
        "original_closed_collinear_source_neighborhood":k+1,
        "conservative_valid_next_original_flag_counts":sizes,
        "guaranteed_distinct_ordered_six_original_flags":ordered,
        "guaranteed_distinct_unordered_six_flag_sets":lower_unordered,
        "all_six_source_points_pairwise_NONCOLLINEAR":True,
        "all_six_source_lines_pairwise_NONCONCURRENT":True,
        "all_h_s_ge_16_source_separated_six_flag_existence_PROVED":True,
        "counts_source_sixsets_individually_realizable_not_same_f_g":True,
        "seven_GF5_all_h_total_charge_bound_NOT_proved":True,
    }


def _true_source_geometry_incidence_lists(model):
    s=model["s"]
    v=len(model["left_labels"])
    if v!=(s+1)*(s*s+1):
        raise AssertionError("real original generalized quadrangle V mismatch")
    inc=tuple(tuple(x) for x in model["incidences"])
    if len(inc)!=v*(s+1) or len(set(inc))!=len(inc):
        raise AssertionError("original incidence host has wrong count or duplicates")
    lines=[set() for _ in range(v)]
    points=[set() for _ in range(v)]
    for p,l in inc:
        if not 0<=p<v or not 0<=l<v:
            raise AssertionError("ORIGINAL source incidence endpoints out of range")
        lines[l].add(p)
        points[p].add(l)
    if any(len(q)!=s+1 for q in (*points,*lines)):
        raise AssertionError("original point/line regularity fails")
    nearP=[set() for _ in range(v)]
    nearL=[set() for _ in range(v)]
    for row,graph in ((lines,nearP),(points,nearL)):
        for members in row:
            for t in members:graph[t].update(members-{t})
    if any(len(x)!=s*(s+1) for x in (*nearP,*nearL)):
        raise AssertionError("genuine source GQ collinearity graph degrees fail")
    return inc,nearP,nearL


def _select_six_original_separated_flags(model):
    """Deterministic greedy REAL original W38 six-flag witnesses.

    For s=8 the all-h crude counting does NOT guarantee existence,
    so this is a separately verified FINITE construction, not a
    claimed all-h s=8 theorem.
    """
    inc,adjP,adjL=_true_source_geometry_incidence_lists(model)
    for seed in range(64):
        indices=list(range(len(inc)))
        if seed:
            random.Random(230000+seed).shuffle(indices)
        flags=[]
        for q in indices:
            p,l=inc[q]
            if all(p!=u and p not in adjP[u] and
                   l!=v and l not in adjL[v] for u,v in flags):
                flags.append((p,l))
                if len(flags)==6:
                    result=tuple(flags)
                    if any(u==v or v in adjP[u]
                           for (u,_),(v,_) in combinations(result,2)):
                        raise AssertionError("chosen original source points are collinear")
                    if any(u==v or v in adjL[u]
                           for (_,u),(_,v) in combinations(result,2)):
                        raise AssertionError("chosen original source lines are concurrent")
                    return result,seed
    raise AssertionError("finite original W38 six-separated-flag construction failed")


def genuine_original_W38_zero_charge_positive_D6():
    """Construct one REAL accepted GF5 D6 Q charging ZERO source pairs.

    Both maps are FULL global typed pair injections over all 585 source
    points and all 585 original lines; Q has 6 distinct original
    incidence IDs, both half-projections simple C6 and same dual.
    """
    from hyp105_issue230_projection import fixture
    from hyp105_g5e2b3e1b0_seven_signature import (
        classify_seven_prechecked,R3_CERTIFIED_FLOORS)
    model=fixture(3,"lex")
    inc,adjP,adjL=_true_source_geometry_incidence_lists(model)
    selected,seed=_select_six_original_separated_flags(model)
    v=len(model["left_labels"])
    a=model["a"]
    if (model["s"],v,len(inc))!=(8,585,5265):
        raise AssertionError("not real original W(3,8)")
    edge_indices={e:i for i,e in enumerate(inc)}
    Q=tuple(sorted(edge_indices[pair] for pair in selected))
    cyc=tuple(tuple(sorted((i,(i+1)%6))) for i in range(6))
    physical=tuple(combinations(range(a),2))
    if len(physical)<v or len(set(cyc))!=6:
        raise AssertionError("cannot construct full global original physical injections")
    def complete_type(slot):
        assigned={edge[slot]:cyc[j] for j,edge in enumerate(selected)}
        if len(assigned)!=6:
            raise AssertionError("not six distinct true source factors")
        remain=(e for e in physical if e not in set(cyc))
        it=iter(remain)
        labels=tuple(assigned[i] if i in assigned else next(it)
                     for i in range(v))
        if len(set(labels))!=v:
            raise AssertionError("not one full typed-injective globally coherent map")
        return labels
    left,right=complete_type(0),complete_type(1)
    tag=classify_seven_prechecked(Q,left,right,inc)
    if tag!="D6":
        raise AssertionError("true ORIGINAL sixset not historical GF5 positive D6")
    for slot,labels in ((0,left),(1,right)):
        shape=six_incidence_projection_capacity(
            tuple(inc[i][slot] for i in Q),labels,a)
        if shape["true_original_source_projection_kind"]!="A" or shape[
            "ALL_physically_disjoint_original_factor_pairs"]!=9:
            raise AssertionError("real selected sixset not exact physical C6")
    points=tuple(p for p,l in selected)
    lines=tuple(l for p,l in selected)
    if any(p in adjP[q] for p,q in combinations(points,2)) or any(
       l in adjL[q] for l,q in combinations(lines,2)):
        raise AssertionError("positive GF5 ORIGINAL D6 cannot have eligible source-collinear pair")
    # Independently verify real original GQ typed source collinearity
    # over ALL 9+9 physically disjoint source pairs: ZERO are eligible.
    def pair_charge(ids,labels,neighbors):
        phys=nonzero=0
        for u,w in combinations(ids,2):
            if not(set(labels[u])&set(labels[w])):
                phys+=1
                nonzero+=w in neighbors[u]
        return phys,nonzero
    pphys,pcharge=pair_charge(points,left,adjP)
    lphys,lcharge=pair_charge(lines,right,adjL)
    if (pphys,pcharge,lphys,lcharge)!=(9,0,9,0):
        raise AssertionError("source-pair zero-charge construction incorrect")
    return {
        "s":8,"V":585,"K":len(physical),"a":a,
        "true_original_incidence_count":len(inc),
        "chosen_original_six_incidence_IDs":Q,
        "chosen_original_six_source_points":points,
        "chosen_original_six_source_lines":lines,
        "greedy_seed":seed,
        "complete_GLOBAL_point_and_line_injections_verified":True,
        "genuine_historical_GF5_class":"D6",
        "certified_selected_GF5_Q_numerator":R3_CERTIFIED_FLOORS[tag],
        "actual_physically_disjoint_point_pairs_in_Q":pphys,
        "actual_physically_disjoint_line_pairs_in_Q":lphys,
        "actual_ELIGIBLE_source_collinear_point_pairs_in_Q":pcharge,
        "actual_ELIGIBLE_source_concurrent_line_pairs_in_Q":lcharge,
        "positive_original_GF5_Q_with_zero_joint_charge_PROVED":True,
        "entire_real_W38_positive_sixset_census_NOT_executed":True,
        "does_not_construct_global_I_zero_family":True,
    }


def threshold_average_charge(degrees,threshold):
    """Finite degree-gated conditional transfer without a per-pair floor."""
    ds=tuple(int(d) for d in degrees)
    if not ds or any(type(d) is not int or d<0 for d in degrees):
        raise ValueError("complete nonnegative genuine original pair degrees required")
    if type(threshold) is not int or threshold<1:
        raise ValueError("positive integer charge threshold required")
    D=len(ds)
    active=sum(d>=threshold for d in ds)
    I=sum(ds)
    floor=_ceil(Fraction(active*threshold,9))
    if I<active*threshold or floor>_ceil(Fraction(I,9)):
        raise AssertionError("source degree threshold lower certificate invalid")
    return {
        "original_source_pair_count":D,
        "threshold":threshold,
        "pairs_with_at_least_threshold_positive_Q":active,
        "fraction_pairs_above_threshold":str(Fraction(active,D)),
        "total_actual_charge":I,
        "valid_S_lower_from_actual_threshold":floor,
        "global_large_s_positive_fraction_hypothesis_NOT_proved":True,
    }


def original_pair_energy(g,model,accepted,source_type):
    """Exact positive-Q/source-disjoint-collinear pair bipartite energy.

    T_{pair,Q}=1 iff Q has both ORIGINAL source factor identities,
    source pair is ORIGINAL collinear/concurrent and physical labels
    of the two factors are disjoint. All 7 actual accepted GF5 Q
    retained, no physical-proper-P3 filter or artificial independent Q.
    """
    if source_type not in ("P","L"):
        raise ValueError("P or L ORIGINAL source type required")
    from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS
    Qs=dict(accepted)
    if any(len(Q)!=6 or len(set(Q))!=6 or
           any(not isinstance(i,int) or i<0 or i>=len(g["original_incidences"])
               for i in Q) or tag not in R3_CERTIFIED_FLOORS
           for Q,tag in Qs.items()):
        raise ValueError("true accepted ORIGINAL six-incidence Q and GF5 tag required")
    labels=model["left_labels" if source_type=="P" else "right_labels"]
    eligible,_=_eligible_pairs(g,labels,source_type)
    ix=0 if source_type=="P" else 1
    orig=g["original_incidences"]
    supports=[]
    deg=Counter()
    for Q in sorted(Qs):
        sources={orig[j][ix] for j in Q}
        covered=frozenset(pair for pair in eligible
                          if pair[0] in sources and pair[1] in sources)
        supports.append(covered)
        deg.update(covered)
        if len(covered)>9:
            raise AssertionError("real ORIGINAL positive GF5 sixset exceeds 9 source pair cap")
    D=len(eligible)
    I=sum(deg.values())
    E=sum(deg[p]**2 for p in eligible)
    q_major=sum(len(sup) for sup in supports)
    if I!=q_major or E<0 or I>9*len(Qs):
        raise AssertionError("ORIGINAL source pair/Q marginal identity wrong")
    # Independent Gram computation of sum_Q,Q' |supp(Q) intersect supp(Q')|.
    # Can be fully evaluated since real W32 S<=O(10^2) in tested fiber.
    Gram=sum(len(a&b) for a in supports for b in supports)
    if Gram!=E:
        raise AssertionError("true original source-pair-to-Q squared energy NOT conserved")
    if I*I>D*E:
        raise AssertionError("actual ORIGINAL source-pair-Q Gram/Cauchy invalid")
    degrees=tuple(deg.get(p,0) for p in sorted(eligible))
    thresholds={str(q):threshold_average_charge(degrees,q)
                for q in (1,2,4,8,16,32)}
    # Independent verification of every computed degree from actual
    # ORIGINAL six-incidence endpoints: no participation solely by tag.
    for pair in sorted(eligible):
        manual=sum(
            pair[0] in {orig[k][ix] for k in Q} and
            pair[1] in {orig[k][ix] for k in Q}
            for Q in Qs
        )
        if manual!=deg.get(pair,0):
            raise AssertionError("independent pair-major actual ORIGINAL Q charge failed")
    return {
        "source_type":source_type,"true_source_eligible_pairs":D,
        "actual_accepted_original_seven_GF5_Q":len(Qs),
        "true_total_pair_Q_charge":I,
        "source_pair_positive_Q_degree_first_moment":I,
        "source_pair_positive_Q_degree_second_moment":E,
        "independent_ORIGINAL_Q_major_Gram":Gram,
        "exact_zero_charge_source_pair_count":D-len(deg),
        "minimum_eligible_pair_positive_Q_degree":min(degrees) if degrees else 0,
        "maximum_eligible_pair_positive_Q_degree":max(degrees) if degrees else 0,
        "true_positive_Q_with_no_eligible_source_pair":sum(not s for s in supports),
        "threshold_certificates":thresholds,
        "gram_energy_identity_independent_verified":True,
        "cauchy_energy_inequality_verified":True,
        "full_original_pair_major_audit":"PASS",
        "all_h_charge_lower_from_first_second_moments_PROVED":False,
    }


def genuine_original_W32_charge_energy_fiber(scheme):
    """Both types, all actual 24 frozen-outside globally injected source maps."""
    from hyp105_issue230_projection import fixture
    from hyp105_g5e2b3e1b0_seven_signature import seven_census
    from hyp105_issue230_d6aa4c_edit_transversal import (
        genuine_original_positive_hypergraph,incidence_cover_bits)
    from hyp105_issue230_d6aa4d_mixed_transversal_fibers import (
        finite_source_support_partition)
    from hyp105_issue230_d6aa4g_overlap_capacity import (
        complete_fixed_image_states)
    if scheme not in ("S68","S72"):
        raise ValueError("actual pinned ORIGINAL W32 S68/S72 only")
    model=fixture(1,scheme)
    g=geometry(2,model["incidences"])
    records=genuine_original_positive_hypergraph(model)["records"]
    bits,weights,allmask=incidence_cover_bits(records)
    part=finite_source_support_partition(bits,weights,allmask)
    if part["number_transversal_blocks"]!={"S68":53,"S72":119}[scheme]:
        raise AssertionError("true ORIGINAL W32 four-factor transversal count drift")
    block=next((tuple(q) for q in part["transversal_original_factor_blocks"]
                if len(q)==4 and all(p<15 for p in q)),None)
    if block is None:
        raise AssertionError("no genuine W32 four-point original source hitting block")
    initial=tuple(tuple(model["left_labels"][p]) for p in block)
    states=complete_fixed_image_states(("P",)*4,initial)
    right=tuple(tuple(x) for x in model["right_labels"])
    reports=[]
    for st in states:
        left=list(tuple(tuple(x) for x in model["left_labels"]))
        for p,e in zip(block,st):left[p]=e
        current={**model,"left_labels":tuple(left),"right_labels":right}
        census=seven_census(current,independent_checks=False,witness_sets=True)
        if len(census["sets"])!=census["S_seven"]:
            raise AssertionError("historical ORIGINAL positive GF5 seven-Q total drift")
        P=original_pair_energy(g,current,census["sets"],"P")
        L=original_pair_energy(g,current,census["sets"],"L")
        q_charge=true_original_projection_charge(g,current,census["sets"])
        if (P["true_total_pair_Q_charge"],L["true_total_pair_Q_charge"])!=(
                q_charge["source_P_charge"],q_charge["source_L_charge"]):
            raise AssertionError("AA4-K class-sensitive independently computed ORIGINAL Q charge disagrees")
        reports.append({
            "original_seven_S":census["S_seven"],
            "original_selected_GF5_numerator":census["GF5_seven_lower_numerator"],
            "source_P":P,"source_L":L,
            "joint_actual_I":P["true_total_pair_Q_charge"]+L["true_total_pair_Q_charge"],
            "joint_projection_aware_S_lower":
                _ceil(Fraction(P["true_total_pair_Q_charge"]+
                               L["true_total_pair_Q_charge"],18)),
        })
    if len(reports)!=24 or reports[0]["original_seven_S"]!={"S68":68,"S72":72}[scheme]:
        raise AssertionError("original W32 complete fiber construction changed")
    fields=("original_seven_S","joint_actual_I","joint_projection_aware_S_lower")
    ranges={f:{"min":min(r[f] for r in reports),
               "max":max(r[f] for r in reports)} for f in fields}
    for typ in ("P","L"):
        for fld in ("source_pair_positive_Q_degree_first_moment",
                    "source_pair_positive_Q_degree_second_moment",
                    "exact_zero_charge_source_pair_count",
                    "minimum_eligible_pair_positive_Q_degree",
                    "maximum_eligible_pair_positive_Q_degree",
                    "true_positive_Q_with_no_eligible_source_pair"):
            key=typ+"_"+fld
            ranges[key]={"min":min(r["source_"+typ][fld] for r in reports),
                         "max":max(r["source_"+typ][fld] for r in reports)}
    return {
        "scheme":scheme,"true_original_source_four_point_block":block,
        "genuine_globally_injected_complete_maps":24,
        "full_true_ORIGINAL_Q_candidates_per_map":62370,
        "all_24_state_charge_energy":reports,
        "full_state_ranges":ranges,
        "independent_original_pair_Q_Gram_moment_oracle":"PASS",
        "all_h_positive_total_I_theorem_PROVED":False,
        "root_Branch_A":"OPEN","root_Branch_B":"OPEN",
    }


def report(scheme=None):
    x={
        "slice":"HYP105-ISSUE230-D6-AA4-L-ORIGINAL-PAIR-ENERGY-OBSTRUCTION",
        "all_h_s_ge_16_original_source_separated_flag_count_theorem":
            tuple(separated_original_flag_count_theorem(2**h)
                  for h in range(4,9)),
        "actual_original_W38_positive_D6_with_ZERO_P_AND_L_charge":
            genuine_original_W38_zero_charge_positive_D6(),
        "all_h_valid_conditional_degree_fraction_logic":True,
        "source_pair_charge_Gram_exact_second_moment":True,
        "total_I_Omega_s6_PROVED":False,
        "root_A":"OPEN","root_B":"OPEN",
        "full_GF5_R3_PROVED":False,"ASET_exponent_PROVED":False,
    }
    if scheme is not None:
        x["true_original_W32"]=genuine_original_W32_charge_energy_fiber(scheme)
    return x


if __name__=="__main__":
    import argparse,json
    p=argparse.ArgumentParser()
    p.add_argument("--scheme",choices=("S68","S72"))
    x=p.parse_args()
    print(json.dumps(report(x.scheme),indent=2,sort_keys=True))
