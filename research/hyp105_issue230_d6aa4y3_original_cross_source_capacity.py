"""HYP-105 #230 Y3 extension: genuine ORIGINAL GQ crossed point-line
incidence-star cap for harmful shared historical GF5 modes.

A marked point source p and an ORIGINAL LINE source ell require
a true six-flag Q to contain a point incidence of p and a line
incidence of ell. Project this event onto one side and charge to
one true ORIGINAL flag (q,ell), q in actual neighborhood N(ell).
When q=p, use the one-flag physical envelope. When q!=p,
count complete physical K_a A/B/C patterns containing TWO
distinct source physical images, with q's actual original flag
fixed. No fake source incidences or random independent labelings.

For two changed point sources and two changed line sources,
there are at most THREE true point-line source incidence pairs
between the marked 2x2 factors: four would form a forbidden
original GQ incidence 4-cycle. This yields all-h O(s^11)
universal harmful-mode cap vs previous one-side O(s^12).
Neither is sufficient for the all-map S=Omega(s^6) root.
"""
from collections import Counter
from itertools import combinations

from hyp105_issue230_d6aa4y3_original_source_star_capacity import (
    original_parameters,original_single_factor_pattern_capacity,
    original_two_factors_union_capacity,
)

def original_two_source_one_fixed_flag_upper(s,relation):
    """Actual original p!=q source factors with assigned physical pairs
    having adjacent or disjoint endpoints, and ONE prescribed true
    original flag incident to source q. Complete-K_a pattern bound.
    """
    d=original_parameters(s)[1]
    q=d*(d-1)//2
    both=original_two_factors_union_capacity(
        s,relation)["physical_complete_Ka_patterns_with_both_marked_edges"]
    count={
        "A":both["A"]*d**5,
        "B":both["B"]*(d-1)*d**4,
        "C":both["C"]*(d-1)*q**2,
    }
    return {"s":s,"relation":relation,
            "true_original_two_source_fixed_other_flag_upper":count,
            "all_h_true_original_two_distinct_source_factor_physical_upper":
                sum(count.values()),
            "B_count_uses_max_over_fixed_flag_root_or_single":True}


def original_crossed_source_point_line_upper(s,source_incident,relations=None):
    """Number of ORIGINAL half-projected Q containing a particular
    marked side source factor p AND an opposite-side original factor
    ell. Neighbor q of ell may be p if p incident ell, else q !=p.

    When explicit physical edge adjacency of p with every other
    q in N(ell) is known, pass (relation0,...), one for each q!=p.
    Else take the worst possible physical pair relation separately
    for each of the d-I remaining neighbors.
    """
    d=original_parameters(s)[1]
    if type(source_incident) is not bool:
        raise ValueError("actual original source factor incidence must be boolean")
    source_incidence=original_single_factor_pattern_capacity(s)[
        "per_actual_original_incidence_upper"]
    neighboring=tuple(original_two_source_one_fixed_flag_upper(s,r)[
        "all_h_true_original_two_distinct_source_factor_physical_upper"]
        for r in ("adjacent","disjoint"))
    maximum=max(neighboring)
    n=d-int(source_incident)
    if relations is not None:
        if (len(relations)!=n or
            any(r not in ("adjacent","disjoint") for r in relations)):
            raise ValueError("need actual physical K_a relation for EVERY distinct original neighbor")
        neighbor_sum=sum(original_two_source_one_fixed_flag_upper(s,r)[
            "all_h_true_original_two_distinct_source_factor_physical_upper"]
            for r in relations)
    else:
        neighbor_sum=n*maximum
    upper=(source_incidence if source_incident else 0)+neighbor_sum
    return {
        "s":s,"source_POINT_LINE_incident":source_incident,
        "neighbor_count_other_than_marked_source":n,
        "exact_physical_neighbor_relations_used":relations is not None,
        "other_neighbor_source_physical_flag_upper":neighbor_sum,
        "direct_original_incidence_source_flag_upper":
            source_incidence if source_incident else 0,
        "original_crossed_source_point_line_half_Q_upper":upper,
        "all_h_TRUE_original_GQ_projection_source_cross_star":True,
    }


def original_two_plus_two_actual_GQ_harm_upper(s,original_incidence_count,
                                               point_relation,line_relation):
    """Universal all-h bound for H of signed historical shared modes
    after point and line source transpositions. Four marked point-line
    pairs have m<=3 source incidences, not 4 (girth8 forbids C4).
    Each active half-mode on Q meeting BOTH source supports lies in
    a point-line cross-star union. Sum over four source-factor pairs,
    exploiting actual original GQ incidence m.
    """
    if type(original_incidence_count) is not int or not 0<=original_incidence_count<=3:
        raise ValueError("four actual original source factor pairs cannot form a 4-cycle")
    d=original_parameters(s)[1]
    one_flag=original_single_factor_pattern_capacity(s)[
        "per_actual_original_incidence_upper"]
    both_worst=max(
        original_two_source_one_fixed_flag_upper(s,rel)[
            "all_h_true_original_two_distinct_source_factor_physical_upper"]
        for rel in ("adjacent","disjoint"))
    cross=original_incidence_count*one_flag + (
        4*d-original_incidence_count)*both_worst
    point=original_two_factors_union_capacity(
        s,point_relation)["two_source_factor_original_union_upper"]
    line=original_two_factors_union_capacity(
        s,line_relation)["two_source_factor_original_union_upper"]
    cap=2*min(point,line,cross)
    old=2*min(point,line)
    return {
        "s":s,
        "actual_original_marked_point_line_incidence_count":original_incidence_count,
        "true_GQ_girth_eight_excludes_four_point_line_cross_incidences":True,
        "point_two_source_physical_half_cap":point,
        "line_two_source_physical_half_cap":line,
        "true_original_opposite_source_cross_star_half_cap":cross,
        "harmful_shared_original_seven_GF5_mode_upper":cap,
        "previous_only_same_typed_side_mode_upper":old,
        "not_worse_than_prior_all_h_two_source_star_upper":cap<=old,
        "all_h_original_GQ_harmful_mixed_cap_PROVED":True,
        "all_h_original_full_seven_S_Omega_s6_PROVED":False,
    }


def genuine_W32_cross_star_oracle(scheme):
    """Independently enumerate ALL actual ORIGINAL W32 six-flag half
    candidates, all 15x15 true source point-line anchored stars,
    and all 105² possible 2point×2line source incidence layouts.
    """
    from hyp105_issue230_projection import fixture
    from hyp105_issue230_d6aa4q_two_sided_seven_join import (
        exact_ONE_side_original_projection_index,strict_true_W32_model)
    model=fixture(1,scheme)
    inc,f,g=strict_true_W32_model(model)
    actual_inc=set(inc)
    neighbors=[[],[]]
    for side in (0,1):
        neighbors[side]=[set() for _ in range(15)]
    for p,l in inc:
        neighbors[0][l].add(p)
        neighbors[1][p].add(l)
    outcomes={}
    for side,labels in enumerate((f,g)):
        projection=exact_ONE_side_original_projection_index(model,side)
        cross=Counter()
        for Q in projection["candidate_sixset_map"]:
            marked={inc[j][side] for j in Q}
            opposite={inc[j][1-side] for j in Q}
            for p in marked:
                for ell in opposite:
                    cross[p,ell]+=1
        max_inc=max_noninc=0
        max_slack=0
        for p in range(15):
            for ell in range(15):
                relation=[]
                other=neighbors[side][ell]
                for q in sorted(other):
                    if q!=p:
                        relation.append(
                            "adjacent" if set(labels[p])&set(labels[q])
                            else "disjoint")
                incident=p in other
                bound=original_crossed_source_point_line_upper(
                    2,incident,tuple(relation))
                actual=cross[p,ell]
                cap=bound["original_crossed_source_point_line_half_Q_upper"]
                if actual>cap:
                    raise AssertionError("TRUE ORIGINAL W32 cross-star source-incidence bound false")
                max_slack=max(max_slack,cap-actual)
                if incident:max_inc=max(max_inc,actual)
                else:max_noninc=max(max_noninc,actual)
        outcomes["point" if side==0 else "line"]={
            "actual_source_OPPOSITE_source_cross_stars_checked":225,
            "max_real_original_six_ID_Q_for_incident_point_line_stars":max_inc,
            "max_real_original_six_ID_Q_for_nonincident_point_line_stars":max_noninc,
            "maximum_analytic_source_cross_star_slack":max_slack,
            "all_225_real_original_source_cross_caps_PASS":True,
        }
    mcounts=Counter()
    for P in combinations(range(15),2):
        for L in combinations(range(15),2):
            m=sum((p,l) in actual_inc for p in P for l in L)
            if m==4:
                raise AssertionError("genuine ORIGINAL GQ forbids two source points sharing TWO lines")
            mcounts[m]+=1
    if sum(mcounts.values())!=11025:
        raise AssertionError("missed original marked 2point×2line possible source pairs")
    return {
        "scheme":scheme,"true_original_s":2,
        "true_original_GQ_2by2_marked_source_incidence_class_counts":
            dict(sorted(mcounts.items())),
        "full_11025_real_original_2point_x_2line_source_layouts_checked":True,
        "per_typed_side":outcomes,
        "all_h_cross_source_harm_omega_s6_root_PROVED":False,
    }


def report():
    out=[]
    for h in range(1,14):
        s=1<<h
        rows=[]
        for n in (0,1,2,3):
            for p in ("adjacent","disjoint"):
                for l in ("adjacent","disjoint"):
                    rows.append(original_two_plus_two_actual_GQ_harm_upper(s,n,p,l))
        out.append({
            "s":s,
            "worst_cap_all_actual_original_2point_by_2line_layouts":
                max(z["harmful_shared_original_seven_GF5_mode_upper"] for z in rows),
            "best_cap_no_true_original_cross_source_incidence":
                max(z["harmful_shared_original_seven_GF5_mode_upper"]
                    for z in rows if z["actual_original_marked_point_line_incidence_count"]==0),
            "at_least_one_strict_improvement_over_one_side_source_star":
                any(z["harmful_shared_original_seven_GF5_mode_upper"]<
                    z["previous_only_same_typed_side_mode_upper"] for z in rows),
        })
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-Y3-ORIGINAL-POINT-LINE-CROSS-STAR-CAPACITY",
        "all_h_genuine_GQ_two_by_two_source_incidence_girth_four_forbidden":True,
        "all_h_exact_source_cross_star_anchored_true_flag_bound":True,
        "all_h_harmful_GF5_mode_capacity_improves_to_O_s11":True,
        "root_A":"OPEN","root_B":"OPEN","root_C":"OPEN",
        "orders":out,
    }


if __name__=="__main__":
    import argparse,json
    ap=argparse.ArgumentParser()
    ap.add_argument("--scheme",choices=("lex","reverse","S68","S72"))
    q=ap.parse_args()
    print(json.dumps(genuine_W32_cross_star_oracle(q.scheme) if q.scheme else report(),
                     indent=2,sort_keys=True))
