"""HYP-105 / #230 AA4-Y-SRC — exact ORIGINAL A/C,C/A triple-pencil GQ count.

All h>=1, s=2^h: three distinct actual source LINES each selected
twice on six distinct original point-line incidence IDs, with all SIX
actual original POINT IDs distinct. The center-line triples fall into
exactly four immutable GQ categories: zero pair intersections, exactly
one, exactly two, three concurrent at ONE original point. A 'triangle'
of three pairwise meetings at THREE different original points would
be a forbidden ORIGINAL six-cycle (girth eight), and never occurs.

Counts and collision-corrected per-triple two-neighbor choices are
polynomial in V=(s+1)(s²+1), d=s+1, independent of any physical f,g.
Pair with AA4-W exact A,C physical pattern probabilities under TWO
independent COMPLETE global typed injections f,g (shared across Q)
to obtain an exact ALL-h original positive seven-GF5 C/A EXPECTATION.

NO every-f,g deterministic lower, no all-h root hypothesis accepted.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_issue230_projection import fixture, ProjectionClosure
from hyp105_issue230_d6aa4w_full_seven_quenched_kernel import (
    all_h_full_seven_one_global_map_transfer_probabilities,
)
from hyp105_issue230_d6aa4x_exact_source_forest_capacities import (
    checked_gq_parameters, all_h_two_closed_source_forest_expectations,
)


KINDS=("disjoint","one_meeting","two_meetings","concurrent")


def all_h_true_original_triple_pencil_capacity(s):
    """ALL-h exact A/C = three disjoint ORIGINAL two-edge line-pencil paths.

    Host W(3,s) has no C4, no C6 in original point-line incidence graph;
    intersection point of each two source lines is unique or absent.
    """
    V,d,N=checked_gq_parameters(s)
    Q=comb(d,2)
    R=d-1
    line_pairs_meeting=V*Q
    concurrent_line_triples=V*comb(d,3)
    two_pair_meetings=V*comb(d,2)*R**2
    one_pair_meeting=line_pairs_meeting*(V-2)-2*two_pair_meetings-3*concurrent_line_triples
    zero_pair_meeting=comb(V,3)-one_pair_meeting-two_pair_meetings-concurrent_line_triples
    # Three line centers, choose unordered 2-neighbor source POINT
    # sets per center, imposing pairwise disjoint actual original points.
    #
    # One shared source point between two distinct lines:
    # violation count = (d-1)^2*C(d,2).
    # Two shared points centered on same third line (distinct):
    # violating both events = (d-1)^2.
    # All three source lines concurrent at one point:
    # 3 intersecting-pair collision events, pairwise AND triple
    # all count (d-1)^3; IE correction +2*(d-1)^3.
    disjoint_Q=Q**3
    one_Q=disjoint_Q-R**2*Q
    two_Q=disjoint_Q-2*R**2*Q+R**2
    concurrent_Q=disjoint_Q-3*R**2*Q+2*R**3
    groups={
        "disjoint":zero_pair_meeting,
        "one_meeting":one_pair_meeting,
        "two_meetings":two_pair_meetings,
        "concurrent":concurrent_line_triples,
    }
    possibilities={
        "disjoint":disjoint_Q,
        "one_meeting":one_Q,
        "two_meetings":two_Q,
        "concurrent":concurrent_Q,
    }
    if sum(groups.values())!=comb(V,3) or any(v<0 for v in groups.values()):
        raise AssertionError("all real original source line triples must occupy four GQ cells")
    if any(v<0 or v>Q**3 for v in possibilities.values()):
        raise AssertionError("source line triple 2-subsets invalid")
    total=sum(groups[k]*possibilities[k] for k in KINDS)
    if total<=0:
        raise AssertionError("source original A/C six-flag capacity must be positive")
    return {
        "s":s,"V":V,"d":d,"N_original_flag_IDs":N,
        "original_line_pair_meetings":line_pairs_meeting,
        "three_source_line_center_triple_type_counts":groups,
        "pairwise_disjoint_two_original_points_per_source_line_choices":possibilities,
        "source_original_A/C_six_incidence_Q":total,
        "source_original_C/A_by_true_GQ_duality":total,
        "forbidden_three_pairwise_distinct_meeting_triangle":True,
        "girth8_no_original_6cycle_used":True,
        "no_global_physical_maps_used_for_source_count":True,
    }


def full_global_uniform_AC_CA_selected_GF5(s):
    """Both full globally injected typed maps uniform, INDEPENDENT by type.

    Per ORIGINAL Q probability point-side physical A and line-side C is
    pA*pC, and same for dual source C/A. Across different actual Q,
    each of the TWO maps is globally shared; no per-Q independence.
    """
    z=all_h_true_original_triple_pencil_capacity(s)
    p=all_h_full_seven_one_global_map_transfer_probabilities(s)
    pa=p["A_any_connected_or_disconnected_physical_2factor"]
    pc=p["C_three_source_repeats_physical_matching"]
    mean=2*z["source_original_A/C_six_incidence_Q"]*pa*pc
    x=all_h_two_closed_source_forest_expectations(s)
    return {
        "s":s,"V":z["V"],"a":p["a"],
        "source_original_U_A/C":z["source_original_A/C_six_incidence_Q"],
        "source_original_U_C/A":z["source_original_C/A_by_true_GQ_duality"],
        "pA":pa,"pC":pc,
        "two_UNIFORM_complete_global_maps_expected_selected_C/A":mean,
        "prior_X_two_tag_selected_expected":x["expected_two_tag_total"],
        "three_positive_original_selected_tags_expected":mean+x["expected_two_tag_total"],
        "true_original_third_tag_new_mean_PROVED":True,
        "all_h_source_triple_pencil_counts_PROVED":True,
        "leading_source_U_AC_over_s15":Fraction(1,48),
        "leading_AC_CA_expected_GF5_tag_over_s6":Fraction(70,3),
        "leading_three_selected_tag_expected_over_s6":Fraction(160,3),
        "does_NOT_imply_adversarial_infimum":True,
    }


def _strict_actual_source_line_neighborhoods(model):
    """TRUE ORIGINAL GQ fixture validation, not mere regularity/no C4."""
    G=ProjectionClosure(model)
    adj=[set() for _ in range(G.v)]
    for point,line in G.edges:
        adj[line].add(point)
    if any(len(q)!=G.delta for q in adj):
        raise AssertionError("real source GQ line degree lost")
    return G,adj


def independent_real_original_line_triple_census(model,*,max_weighted_trials=0):
    """Finite TRUE real original line triples, source-only independent oracle.

    For every distinct triple of actual original line IDs, directly
    intersect actual original point-neighbor sets. Count four GQ triple
    classes. Optionally independently brute-force the six-distinct
    original point selection count for the first N source line triples.
    No physical projection is used after TRUE GQ validation.
    """
    G,lines=_strict_actual_source_line_neighborhoods(model)
    hist=Counter()
    points_choices=Counter()
    checked=0
    witnesses={}
    for IDs in combinations(range(G.v),3):
        L=[lines[i] for i in IDs]
        meets=[L[0]&L[1],L[0]&L[2],L[1]&L[2]]
        if any(len(t)>1 for t in meets):
            raise AssertionError("original GQ forbids two original lines meeting at >1 point")
        pairs=sum(bool(k) for k in meets)
        concurrent=pairs==3 and len(set().union(*meets))==1
        if pairs==3 and not concurrent:
            raise AssertionError("actual GQ line triangle gives original incidence six-cycle")
        if pairs>3:
            raise AssertionError("invalid GQ center triple")
        tag={0:"disjoint",1:"one_meeting",2:"two_meetings"}.get(
            pairs,"concurrent")
        hist[tag]+=1
        if tag not in witnesses:witnesses[tag]=tuple(IDs)
        if max_weighted_trials and checked<max_weighted_trials:
            direct=0
            for a in combinations(L[0],2):
                for b in combinations(L[1],2):
                    if set(a)&set(b):continue
                    for c in combinations(L[2],2):
                        if len(set(a+b+c))==6:direct+=1
            points_choices[(tag,direct)]+=1
            checked+=1
    ref=all_h_true_original_triple_pencil_capacity(G.s)
    if dict(hist)!=ref["three_source_line_center_triple_type_counts"]:
        raise AssertionError("independent complete actual source line-triple GQ census differs")
    for (tag,count),n in points_choices.items():
        if count!=ref["pairwise_disjoint_two_original_points_per_source_line_choices"][tag]:
            raise AssertionError("ACTUAL original three pencils direct local overlap count changed")
    return {
        "s":G.s,"number_actual_source_line_triples":comb(G.v,3),
        "actual_original_line_triple_cell_counts":dict(hist),
        "actual_original_source_witness_per_class":witnesses,
        "independently_bruteforced_source_point_pair_choices":{
            f"{k[0]}:{k[1]}":v for k,v in sorted(points_choices.items())},
        "direct_source_local_triples_checked":checked,
        "source_closed_all_h_formula_matches_true_GQ":True,
    }


def real_original_W32_bruteforce_all_three_pencils(model):
    """Independently directly enumerate ALL actual original source A/C six-Q.

    W32 has 15 lines and 3 incident original points/line, so 455 triples
    and <=27 neighbor-two selections per triple; exhaustively check all.
    For bigger GQ full source 6-Q enumeration is not claimed.
    """
    G,adj=_strict_actual_source_line_neighborhoods(model)
    if G.s!=2:
        raise ValueError("complete brute original three pencils only W(3,2)")
    total=0
    by_type=Counter()
    for IDs in combinations(range(G.v),3):
        L=[adj[i] for i in IDs]
        meet=sum(bool(L[i]&L[j]) for i,j in ((0,1),(0,2),(1,2)))
        tag={0:"disjoint",1:"one_meeting",2:"two_meetings"}.get(
            meet,"concurrent")
        for a in combinations(L[0],2):
            for b in combinations(L[1],2):
                for c in combinations(L[2],2):
                    if len(set(a+b+c))==6:
                        total+=1
                        by_type[tag]+=1
    ref=all_h_true_original_triple_pencil_capacity(2)
    if total!=ref["source_original_A/C_six_incidence_Q"]:
        raise AssertionError("all original W32 3-pencil six-incidence exhaustive census disagreement")
    expected={
        k:ref["three_source_line_center_triple_type_counts"][k]*
          ref["pairwise_disjoint_two_original_points_per_source_line_choices"][k]
        for k in KINDS}
    if dict(by_type)!=expected:
        raise AssertionError("whole original A/C triple intersection stratification changed")
    return {
        "s":2,"actual_original_A/C_sixset_count":total,
        "exhaustive_original_three_line_center_classes":dict(by_type),
        "independent_genuine_original_A/C_source_sixset_count":total,
    }


def report(s_values=(2,4,8,16,32)):
    out={}
    for s in s_values:
        src=all_h_true_original_triple_pencil_capacity(s)
        e=full_global_uniform_AC_CA_selected_GF5(s)
        q=e["two_UNIFORM_complete_global_maps_expected_selected_C/A"]
        t=e["three_positive_original_selected_tags_expected"]
        out[str(s)]={
            "s":s,
            "source_original_AC_CA":src["source_original_A/C_six_incidence_Q"],
            "line_triple_types":src["three_source_line_center_triple_type_counts"],
            "exact_selected_C_A_expected_fraction":f"{q.numerator}/{q.denominator}",
            "combined_three_tags_fraction":f"{t.numerator}/{t.denominator}",
        }
    return {"slice":"HYP105-ISSUE230-D6-AA4-Y-SRC-TRIPLE-PENCIL",
            "results":out,"root_A":"OPEN","root_B":"OPEN"}


if __name__=="__main__":
    import argparse,json
    p=argparse.ArgumentParser()
    p.add_argument("--real-source",action="store_true")
    args=p.parse_args()
    z=report()
    if args.real_source:
        z["real_source_W32_W34"]= {
            str(1<<h):independent_real_original_line_triple_census(
                fixture(h,"lex"),max_weighted_trials=20)
            for h in (1,2)
        }
        z["real_source_W32_A_C_sixsets"] = real_original_W32_bruteforce_all_three_pencils(fixture(1,"lex"))
    print(json.dumps(z,indent=2,sort_keys=True))
