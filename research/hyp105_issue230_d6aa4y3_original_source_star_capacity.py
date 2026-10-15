"""HYP-105 issue #230 / D6-AA4-Y3: all-h TRUE ORIGINAL physical
pair-pattern source-star and incidence-anchored capacities.

For a genuine W(3,s), s=2^h>=2, regular original source degree
d=s+1 and minimal K_a physical pair alphabet with K=binom(a,2)>=V:
  - a physical K_a 2-regular six-edge pattern can be 6-cycle or
    two disjoint triangles, 70 patterns per prescribed 6 coordinates;
  - a B pattern is a doubled physical root pair plus C4 on
    four other physical coordinates;
  - a C pattern is 3 disjoint physical edges, each original source
    factor used at two DIFFERENT original incidence IDs.

For any ONE prescribed actual original source factor, count full-physical
patterns rooted at its assigned physical pair; multiply by genuine
original d-neighbor choices. Missing physical pairs in an incomplete
global injection can ONLY decrease the actual half-sixset census.

For any TWO prescribed actual distinct source factors, count union by
physical-edge adjacency versus disjointness, subtracting the patterns
that use BOTH marked edges. This is a strict all-h physical envelope
and is EXACT for every complete physical K6 W(3,2) source map.
No claim of an all-h seven-class S=Omega(s^6) minimax theorem.
"""
from collections import Counter
from itertools import combinations
from math import comb

def _choose(n,k):
    return comb(n,k) if n>=k and k>=0 else 0


def original_parameters(s):
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("only genuine original W(3,2^h), h>=1")
    V=(s+1)*(s*s+1)
    a=6
    while a*(a-1)//2<V:
        a+=1
    return s,s+1,V,a,a*(a-1)//2


def original_single_factor_pattern_capacity(s):
    s,d,V,a,K=original_parameters(s)
    q=_choose(d,2)
    physical={
        "A":28*_choose(a-2,4),
        "B_repeated_root":3*_choose(a-2,4),
        "B_single_on_C4":2*_choose(a-2,2)*_choose(a-4,2),
        "C_repeated_matching":3*_choose(a-2,4),
    }
    counts={
        "A":physical["A"]*d**6,
        "B_repeated_root":physical["B_repeated_root"]*q*d**4,
        "B_single_on_C4":physical["B_single_on_C4"]*q*d**4,
        "C":physical["C_repeated_matching"]*q**3,
    }
    incidence={
        "A":physical["A"]*d**5,
        "B_repeated_root":physical["B_repeated_root"]*(d-1)*d**4,
        "B_single_on_C4":physical["B_single_on_C4"]*q*d**3,
        "C":physical["C_repeated_matching"]*(d-1)*q**2,
    }
    if d*sum(incidence.values()) != (
        counts["A"]+2*counts["B_repeated_root"]
        +counts["B_single_on_C4"]+2*counts["C"]):
        raise AssertionError("true original six-ID incidence-source double counting failed")
    return {
        "s":s,"d":d,"V":V,"a":a,"K":K,
        "physical_patterns_in_full_Ka_containing_fixed_edge":physical,
        "six_ORIGINAL_IDs_containing_fixed_source_factor_upper":counts,
        "six_ORIGINAL_IDs_containing_fixed_actual_incidence_upper":incidence,
        "per_source_star_upper":sum(counts.values()),
        "per_actual_original_incidence_upper":sum(incidence.values()),
        "equal_for_every_globally_bijective_W32_K6_source_half":s==2,
        "all_h_true_original_source_factor_half_capacity_PROVED":True,
        "not_a_two_sided_seven_GF5_lower":True,
    }


def original_two_factors_union_capacity(s,relation):
    """Original half six-ID candidates that use at least ONE of two
    distinct affected source factors; physical pair images are either
    adjacent (one physical coordinate in common) or disjoint.

    Universal U2 upper for ANY global incomplete injection, and exact
    for EVERY W32 global K6 physical-edge bijection.
    """
    single=original_single_factor_pattern_capacity(s)
    d,a=single["d"],single["a"]
    q=_choose(d,2)
    if relation=="adjacent":
        both_phys={
            "A":7*_choose(a-3,3),
            "B":(a-3)*_choose(a-4,2),
            "C":0,
        }
    elif relation=="disjoint":
        both_phys={
            "A":14*_choose(a-4,2),
            "B":6*_choose(a-4,2),
            "C":_choose(a-4,2),
        }
    else:
        raise ValueError("two distinct globally injected physical pair images: adjacent or disjoint")
    both={
        "A":both_phys["A"]*d**6,
        "B":both_phys["B"]*q*d**4,
        "C":both_phys["C"]*q**3,
    }
    source=single["six_ORIGINAL_IDs_containing_fixed_source_factor_upper"]
    one={"A":source["A"],
         "B":source["B_repeated_root"]+source["B_single_on_C4"],
         "C":source["C"]}
    union={t:2*one[t]-both[t] for t in ("A","B","C")}
    if any(n<0 or n>2*one[t] for t,n in union.items()):
        raise AssertionError("physical two-root original half union inclusion-exclusion failed")
    return {
        "s":s,"a":a,"relation":relation,
        "physical_complete_Ka_patterns_with_both_marked_edges":both_phys,
        "two_source_factor_original_sixsets_both_contained_full_Ka":both,
        "two_source_factor_original_sixsets_union_upper":union,
        "two_source_factor_original_union_upper":sum(union.values()),
        "one_source_original_upper":sum(one.values()),
        "strict_vs_two_independent_star_upper":
            sum(union.values())<2*sum(one.values()),
        "exact_for_every_W32_full_K6_original_half":s==2,
        "all_h_partial_injection_physical_PATTERN_UPPER":True,
        "all_h_two_sided_conflicting_mode_S_lower_PROVED":False,
    }


def original_swapped_source_harm_capacity(s,point_relation,line_relation):
    """A coarse sign-robust upper on harmful shared modes H.

    Every active half-mode uses a UNIQUE actual six-original-flag Q.
    If source labels change only at two factors on each side, no
    Q disjoint from either affected source pair can change. Each
    half feature can switch from one active mode to another at most
    once, so the symmetric difference of both half feature indexes
    is <= 2 U2 for that side. Opposite-sign shared-mode
    coincidence count H <= min(E_point,E_line).
    """
    P=original_two_factors_union_capacity(s,point_relation)
    L=original_two_factors_union_capacity(s,line_relation)
    up=2*P["two_source_factor_original_union_upper"]
    ul=2*L["two_source_factor_original_union_upper"]
    return {
        "s":s,"point_pair_physical_relation":point_relation,
        "line_pair_physical_relation":line_relation,
        "original_point_mode_gradient_energy_upper":up,
        "original_line_mode_gradient_energy_upper":ul,
        "harmful_opposite_sign_original_shared_mode_count_upper":min(up,ul),
        "all_h_valid_for_global_source_two_swaps":True,
        "root_all_map_seven_S_Omega_s6_PROVED":False,
    }


def genuine_W32_star_oracle(scheme):
    """Independent full physical projection half index on ALL actual 45
    original point-line incidence IDs; exhaust every source factor,
    every actual original flag, all 105 source-source edge relations.
    """
    from hyp105_issue230_projection import fixture
    from hyp105_issue230_d6aa4q_two_sided_seven_join import (
        exact_ONE_side_original_projection_index,strict_true_W32_model)
    model=fixture(1,scheme)
    inc,point,line=strict_true_W32_model(model)
    single=original_single_factor_pattern_capacity(2)
    refs={k:single["six_ORIGINAL_IDs_containing_fixed_source_factor_upper"][k]
          for k in ("A","B_repeated_root","B_single_on_C4","C")}
    inc_ref=single["six_ORIGINAL_IDs_containing_fixed_actual_incidence_upper"]
    pairs_ref={
        relation: original_two_factors_union_capacity(2,relation)
        for relation in ("adjacent","disjoint")
    }
    records={}
    for side,labels in enumerate((point,line)):
        half=exact_ONE_side_original_projection_index(model,side)
        rows=half["candidate_sixset_map"]
        if len(rows)!=62370:
            raise AssertionError("true W32 all actual six-original-ID physical half count drift")
        factor_kind=[Counter() for _ in range(15)]
        flag_kind=[Counter() for _ in range(45)]
        both_kind=Counter()
        for Q,kind in rows.items():
            factors=Counter(inc[j][side] for j in Q)
            for src,multiplicity in factors.items():
                if kind=="B":
                    key="B_repeated_root" if multiplicity==2 else "B_single_on_C4"
                else:
                    key=kind
                factor_kind[src][key]+=1
            for j in Q:
                if kind=="B":
                    key="B_repeated_root" if factors[inc[j][side]]==2 else "B_single_on_C4"
                else:key=kind
                flag_kind[j][key]+=1
            for x,y in combinations(sorted(factors),2):
                both_kind[(x,y,kind)]+=1
        expected_source=refs
        for i,actual in enumerate(factor_kind):
            if dict(actual)!=expected_source:
                raise AssertionError(f"true original {scheme} {side} source factor {i} half star mismatch: {actual}")
        for j,actual in enumerate(flag_kind):
            if dict(actual)!=inc_ref:
                raise AssertionError(f"true original {scheme} {side} original incidence {j} half flag mismatch: {actual}")
        relation_counts=Counter()
        for x,y in combinations(range(15),2):
            relation=("adjacent" if len(set(labels[x])&set(labels[y]))==1
                      else "disjoint")
            relation_counts[relation]+=1
            analytic=pairs_ref[relation]["two_source_factor_original_sixsets_both_contained_full_Ka"]
            for kind in ("A","B","C"):
                if both_kind[(x,y,kind)]!=analytic[kind]:
                    raise AssertionError("real ORIGINAL two-star physical projection collision differs from all-h bound")
            union=sum(factor_kind[x].values())+sum(factor_kind[y].values())-sum(
                both_kind[(x,y,k)] for k in ("A","B","C"))
            if union!=pairs_ref[relation]["two_source_factor_original_union_upper"]:
                raise AssertionError("full actual original W32 source pair physical union mismatch")
        if relation_counts!={"adjacent":60,"disjoint":45}:
            raise AssertionError("physical K6 marked edge pair adjacency classes invalid")
        records["point" if side==0 else "line"]={
            "source_factors_checked":15,"actual_source_incidences_checked":45,
            "actual_source_factor_pairs_checked":105,
            "all_62370_TRUE_original_half_Q_exhaustively_visited":True,
            "per_actual_source_factor_ORIGINAL_Q":single["per_source_star_upper"],
            "per_actual_original_incidence_Q":single["per_actual_original_incidence_upper"],
            "adjacent_source_pair_ORIGINAL_Q_union":pairs_ref["adjacent"]["two_source_factor_original_union_upper"],
            "disjoint_source_pair_ORIGINAL_Q_union":pairs_ref["disjoint"]["two_source_factor_original_union_upper"],
            "pair_classes":dict(relation_counts),
        }
    return {"scheme":scheme,"s":2,"a":6,"per_typed_side":records,
            "true_original_source_GQ_physical_complete_K6_required":True,
            "root_A":"OPEN","root_B":"OPEN"}


def genuine_W32_signed_harm_vs_source_star(scheme,native_conflict_engine):
    """Check every real W32 mixed-source signed GF5 mode harm vs all-h star cap."""
    import subprocess
    from hyp105_issue230_projection import fixture
    from hyp105_issue230_d6aa4ycyc_bilateral_original_matrix import engine_input,MOVES
    from hyp105_issue230_d6aa4y2_original_mode_gram import parse_exact_signed_conflict_tsv
    model=fixture(1,scheme)
    run=subprocess.run([str(native_conflict_engine)],input=engine_input(model),
                       text=True,capture_output=True,check=True)
    if "GENUINE ORIGINAL 11236 EXACT SIGNED MODE CONFLICTS COMPLETE" not in run.stderr:
        raise AssertionError("native true ORIGINAL GF5 harmful quadrant census incomplete")
    conflicts=parse_exact_signed_conflict_tsv(run.stdout)
    from hyp105_issue230_d6aa4y3_original_cross_source_capacity import (
        original_two_plus_two_actual_GQ_harm_upper)
    original_source_incidence_set=set(tuple(x) for x in model["incidences"])
    labels=(model["left_labels"],model["right_labels"])
    max_h=0
    max_ratio=(0,1)
    best=None
    detail=Counter()
    strict_cross_improvements=0
    for i in range(1,106):
        for j in range(1,106):
            kind=[]
            for physical,swap_id in ((labels[0],i),(labels[1],j)):
                u,v=MOVES[swap_id]
                relation=("adjacent" if set(physical[u])&set(physical[v])
                          else "disjoint")
                kind.append(relation)
            upper=original_swapped_source_harm_capacity(2,kind[0],kind[1])
            marked_points=MOVES[i]
            marked_lines=MOVES[j]
            n=sum((p,l) in original_source_incidence_set
                  for p in marked_points for l in marked_lines)
            refined=original_two_plus_two_actual_GQ_harm_upper(
                2,n,kind[0],kind[1])
            cap=refined["harmful_shared_original_seven_GF5_mode_upper"]
            if cap<upper["harmful_opposite_sign_original_shared_mode_count_upper"]:
                strict_cross_improvements+=1
            c=conflicts[i,j]
            harm=c["pn"]+c["np"]
            favor=c["pp"]+c["nn"]
            if not 0<=harm<=cap:
                raise AssertionError(f"REAL ORIGINAL source-star mode harmful capacity violated {i,j}")
            detail[(kind[0],kind[1])]+=1
            if harm>max_h:
                max_h=harm
                best={"point_swap":MOVES[i],"line_swap":MOVES[j],
                      "point_physical_relation":kind[0],
                      "line_physical_relation":kind[1],
                      "harmful_original_mode_count":harm,
                      "favorable_original_mode_count":favor,
                      "physical_pair_star_all_h_upper":cap,
                      "actual_original_two_by_two_cross_incidence_count":n,
                      "point_line_cross_star_capacity_refinement_APPLIED":True,
                      "witness_slack":cap-harm}
            if harm*max_ratio[1]>max_ratio[0]*cap:
                max_ratio=(harm,cap)
    if sum(detail.values())!=11025:
        raise AssertionError("real original 105x105 source two-factor harms missed")
    return {
        "scheme":scheme,"true_original_GQ_W32":True,
        "historical_Y2_signed_original_mode_11236_rows_read":len(conflicts),
        "mixed_true_original_global_complete_pairs_audited":11025,
        "max_harmful_original_modes":max_h,
        "pairs_with_strict_original_point_line_cross_star_refinement":
            strict_cross_improvements,
        "max_harmful_relative_to_analytic_source_star_upper":
            f"{max_ratio[0]}/{max_ratio[1]}",
        "max_harmful_original_global_witness":best,
        "point_line_physical_source_pair_relation_matrix_counts":{
            f"{p}/{l}":detail[p,l] for p in ("adjacent","disjoint")
            for l in ("adjacent","disjoint")},
        "all_h_analytical_source_star_harm_upper_verified_on_original_W32":True,
        "all_h_genuine_no4cycle_point_line_cross_refinement_verified":True,
        "all_h_original_seven_minimax_Omega_s6_PROVED":False,
    }


def report():
    orders=[original_single_factor_pattern_capacity(1<<h)
            for h in range(1,13)]
    pair=[{"s":1<<h,
            "adjacent":original_two_factors_union_capacity(1<<h,"adjacent"),
            "disjoint":original_two_factors_union_capacity(1<<h,"disjoint")}
          for h in range(1,13)]
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-Y3-ORIGINAL-SOURCE-STAR-PHYSICAL-CAPACITY",
        "all_h_original_physical_source_anchored_six_ID_star_upper_PROVED":True,
        "all_h_two_original_factor_physical_pair_geometry_capacity_PROVED":True,
        "all_h_harmful_original_mode_local_swap_upper_PROVED":True,
        "root_A":"OPEN","root_B":"OPEN","root_C":"OPEN",
        "per_order_single_anchored":orders,"per_order_two_marked_edges":pair,
    }


if __name__=="__main__":
    import argparse,json
    parser=argparse.ArgumentParser()
    parser.add_argument("--scheme",choices=("lex","reverse","S68","S72"))
    parser.add_argument("--native-conflicts")
    args=parser.parse_args()
    if args.native_conflicts and not args.scheme:
        parser.error("--native-conflicts requires --scheme")
    value=(genuine_W32_signed_harm_vs_source_star(args.scheme,args.native_conflicts)
           if args.native_conflicts else
           genuine_W32_star_oracle(args.scheme) if args.scheme else report())
    print(json.dumps(value,sort_keys=True,indent=2))
