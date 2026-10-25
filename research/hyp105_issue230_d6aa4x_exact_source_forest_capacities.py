"""HYP-105 issue #230 AA4-X: exact ALL-h genuine ORIGINAL source forests.

Two source-only, true W(3,s) exact closed formulas (all s=2^h>=2):
  U_B/C = U_C/B = P4_point_center * admissible_disjoint_line_P2,
  U_B/B-overlap = P3_point_to_line * m3(G - four P3 vertices).
Six different ACTUAL original incidence IDs, no physical image maps needed.
These are actual GQ forest populations, NOT joint physical GF5 certificates.

G is the original bipartite d=s+1 regular incidence graph on 2V
vertices, N=V*d edges, girth >= 8. For P3 deletion the residual
degree histogram and edge-degree mixing are universal from girth 8;
a 3-matching count is given by an exact line-graph inclusion-exclusion.
"""
from fractions import Fraction
from math import comb
from collections import Counter

from hyp105_issue230_projection import fixture,ProjectionClosure
from hyp105_issue230_d6aa4w_full_seven_quenched_kernel import (
    all_h_full_seven_one_global_map_transfer_probabilities,
)

def checked_gq_parameters(s):
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("genuine ORIGINAL W(3,2^h) requires h>=1")
    V=(s+1)*(s*s+1)
    d=s+1
    return V,d,V*d


def all_h_BC_two_source_path_population(s):
    """EXACT all-h source forest: P4 (point endpoints) plus disjoint P2 (line root).

    Source point B: one repeated original point (P4 internal point).
    Source line C: three repeated original lines (2 internal P4 lines,
    one internal disjoint P2 line). All original incidence edges differ.
    Girth 8 forbids extra short original paths with repeated vertices.
    """
    V,d,N=checked_gq_parameters(s)
    # Physical-free number of un-oriented four-edge point→point paths.
    P4=V*d*(d-1)**3//2
    # Delete three original POINT vertices and two original LINE vertices
    # along one P4; any remaining original line intersects deleted points
    # in at most one point (else ORIGINAL 4-/6-cycle). Remaining lines:
    # 3d-4 have degree d-1, V-3d+2 retain degree d.
    line_affected=3*d-4
    line_unaffected=V-3*d+2
    if min(line_affected,line_unaffected)<0 or (V*d*(d-1)**3)%2:
        raise AssertionError("true original point-ended GQ P4 counts invalid")
    P2_remaining=(line_affected*comb(d-1,2)
                  +line_unaffected*comb(d,2))
    count=P4*P2_remaining
    return {
        "s":s,"V":V,"d":d,"N_original_incidences":N,
        "root_original_point_ended_P4_count":P4,
        "P4_deleted_point_count":3,"P4_deleted_line_count":2,
        "remaining_original_lines_with_one_removed_point":line_affected,
        "remaining_original_lines_with_no_removed_points":line_unaffected,
        "disjoint_original_line_centered_P2_per_root_P4":P2_remaining,
        "source_original_B/C_count":count,
        "source_original_C/B_by_true_GQ_duality":count,
        "girth_eight_all_h_original_source_theorem":True,
        "physical_global_maps_NOT_USED":True,
    }


def exact_residual_three_matching_formula(V,d):
    """Any deleted ORIGINAL P3 (point-line-point-line) in a d-regular GQ.

    Delete its four different actual original source vertices, all
    edges incident to them, then count residual 3-matchings without
    enumerating original 6-incidence sixsets.

    A=4d-6 affected residual vertices of degree d-1; all other
    U=2(V-2d+1) vertices degree d. No affected/affected residual edge:
    its two deleted-neighbor paths plus the original P3 would yield
    a 3..6 original incidence cycle, against girth 8.
    """
    if type(V) is not int or type(d) is not int or d<3 or V<2*d-1:
        raise ValueError("original GQ parameter bounds violated")
    e=V*d-4*d+3
    A=4*d-6
    U=2*(V-2*d+1)
    if A+U!=2*V-4:
        raise AssertionError("P3 residual original vertex count changed")
    if A*(d-1)+U*d!=2*e:
        raise AssertionError("P3 residual original incidence handshake invalid")
    mixed=A*(d-1)
    high=e-mixed
    if high<0:
        raise AssertionError("all high-degree original residual edge count invalid")
    # In the LINE GRAPH L(G'), matchings of three original edges are
    # independent triples. Its adjacency-edge count:
    adjacent_pairs=A*comb(d-1,2)+U*comb(d,2)
    # Each residual original incidence edge gives a vertex of L(G') of
    # degree (deg(source point)+deg(source line)-2).
    # No mixed 'low-low' endpoint source edge, by source GQ girth8.
    wedges=(mixed*comb(2*d-3,2)
            +high*comb(2*d-2,2))
    # All triangles of L(G') are triples of original edges incident to
    # one common ORIGINAL vertex; G' is bipartite (no graph triangles).
    triangles=A*comb(d-1,3)+U*comb(d,3)
    matching3=(comb(e,3)
               -adjacent_pairs*(e-2)
               +wedges-triangles)
    if matching3<=0:
        raise AssertionError("a genuine original GQ should retain 3-matchings")
    return {
        "residual_original_incidence_edges":e,
        "residual_low_degree_vertices":A,
        "residual_high_degree_vertices":U,
        "residual_low_high_edges":mixed,
        "residual_high_high_edges":high,
        "line_graph_adjacent_edge_pairs":adjacent_pairs,
        "line_graph_two_edge_wedges":wedges,
        "line_graph_triangles":triangles,
        "actual_disjoint_original_three_edge_matchings":matching3,
    }


def all_h_BB_overlap_path_matching_population(s):
    """Exact source B/B-overlap = 3-edge path + THREE disjoint 1-edge paths.

    A distinguished genuine original P3 contains the sole repeated
    original point and the sole repeated original line that share one
    of the SIX selected original incidence ID edges. Its complement
    in the sixset consists of three pairwise vertex-disjoint original
    incidence edges outside the original P3 vertices.
    """
    V,d,N=checked_gq_parameters(s)
    P3=V*d*(d-1)**2
    rem=exact_residual_three_matching_formula(V,d)
    count=P3*rem["actual_disjoint_original_three_edge_matchings"]
    return {
        "s":s,"V":V,"d":d,"N_original_incidences":N,
        "root_original_point_to_line_P3_count":P3,
        **rem,
        "source_original_B/B-overlap_count":count,
        "source_original_B/B-overlap_by_true_GQ_duality":count,
        "original_3edge_path_plus_3isolated_incidence_edges_PROVED":True,
        "all_h_closed_form_and_true_source_girth_PROVED":True,
        "physical_global_maps_NOT_USED":True,
    }


def all_h_two_closed_source_forest_expectations(s):
    """Use verified AA4-W physical one-global-map kernels AFTER true source count.

    Genuine independently uniform COMPLETE f and g, SHARED over every Q.
    This is an EXACT both-random all-h first moment, NOT a worst-case min.
    """
    bc=all_h_BC_two_source_path_population(s)
    bb=all_h_BB_overlap_path_matching_population(s)
    probabilities=all_h_full_seven_one_global_map_transfer_probabilities(s)
    pB=probabilities["B_same_source_repeated_plus_physical_C4"]
    pC=probabilities["C_three_source_repeats_physical_matching"]
    EC_B=2*bc["source_original_B/C_count"]*pB*pC
    EBB=bb["source_original_B/B-overlap_count"]*pB*pB
    if not EC_B>0 or not EBB>0:
        raise AssertionError("positive source-complete global-ensemble classes lost")
    return {
        "s":s,"V":bc["V"],"d":bc["d"],"physical_a":probabilities["a"],
        "source_U_BC_and_CB":bc["source_original_B/C_count"],
        "source_U_BB_overlap":bb["source_original_B/B-overlap_count"],
        "pB":pB,"pC":pC,
        "expected_TRUE_original_selected_C/B_both_uniform_full_maps":EC_B,
        "expected_TRUE_original_selected_B/B-overlap_both_uniform_full_maps":EBB,
        "expected_two_tag_total":EC_B+EBB,
        "conditional_vs_adversarial_all_f_g_lower_PROVED":False,
        "all_h_true_original_source_counts_PROVED":True,
        "leading_asymptotic_U_BC_over_s12":Fraction(1,4),
        "leading_asymptotic_U_BB_overlap_over_s18":Fraction(1,6),
        "leading_asymptotic_s6_pB":12,
        "leading_asymptotic_pC":1,
        "leading_asymptotic_EXPECTED_C_B_over_s6":6,
        "leading_asymptotic_EXPECTED_BB_overlap_over_s6":24,
        "leading_asymptotic_two_tag_EXPECTED_over_s6":30,
    }


def _independent_true_gq_source_graph(model):
    """Independent actual finite REAL GQ geometry gate, not a physical oracle."""
    # The pre-existing full ORIGINAL GQ checker enforces unique projection
    # for every nonincident original point-line pair; here physical maps
    # are checked but never used in the counted source-only quantities.
    valid=ProjectionClosure(model)
    V=valid.v;d=valid.delta
    lines=[set() for _ in range(V)]
    points=[set() for _ in range(V)]
    for p,l in valid.edges:
        lines[l].add(p);points[p].add(l)
    if any(len(q)!=d for q in lines+points):
        raise AssertionError("true original regularity lost")
    return V,d,tuple(valid.edges),points,lines


def independent_actual_source_path_four_after_deletion(model, *,limit=24):
    """Sample actual original point→point P4 and independently enumerate ALL surviving P2.

    Works for real W32 and W34 without enumerating O(N^6) original sixsets.
    """
    V,d,inc,points,lines=_independent_true_gq_source_graph(model)
    samples=0
    observed=Counter()
    witness=[]
    for p0 in range(V):
        for l1 in sorted(points[p0]):
            for p2 in sorted(lines[l1]-{p0}):
                for l3 in sorted(points[p2]-{l1}):
                    for p4 in sorted(lines[l3]-{p2,p0}):
                        if p4==p0:raise AssertionError("genuine original P4 cannot fold")
                        deleted_P={p0,p2,p4}
                        deleted_L={l1,l3}
                        actual=sum(
                            comb(len(lines[l]-deleted_P),2)
                            for l in range(V) if l not in deleted_L)
                        observed[actual]+=1
                        if len(witness)<3:witness.append((p0,l1,p2,l3,p4,actual))
                        samples+=1
                        if samples>=limit:
                            expect=all_h_BC_two_source_path_population(d-1)
                            if set(observed)!={expect["disjoint_original_line_centered_P2_per_root_P4"]}:
                                raise AssertionError("actual real original P4→P2 disjoint count disagrees")
                            return {"s":d-1,"sampled_oriented_actual_original_P4":samples,
                                    "actual_P2_per_P4_histogram":dict(observed),
                                    "three_true_source_P4_witnesses":witness}
    raise AssertionError("insufficient real original P4 source paths")


def independent_actual_P3_deletion_three_matching(model, *,max_root_samples=4,
                                                  brute_force_when_small=True):
    """Cross-check actual ORIGINAL residual graph degree and m3 root invariants.

    Real W32 additionally enumerates ALL C(residual 36,3) ORIGINAL
    triples of source flag IDs, checking six-source-vertex disjointness.
    For W34 the direct degree/edge connectivity check avoids huge O(N^3).
    """
    V,d,inc,points,lines=_independent_true_gq_source_graph(model)
    expected=all_h_BB_overlap_path_matching_population(d-1)
    expected_m3=expected["actual_disjoint_original_three_edge_matchings"]
    samples=[]
    for p0 in range(V):
        for l1 in sorted(points[p0]):
            for p2 in sorted(lines[l1]-{p0}):
                for l3 in sorted(points[p2]-{l1}):
                    cutP={p0,p2};cutL={l1,l3}
                    residual=[(p,l) for p,l in inc if p not in cutP and l not in cutL]
                    dp=Counter(p for p,l in residual)
                    dl=Counter(l for p,l in residual)
                    low=sum(x==d-1 for x in dp.values())+sum(x==d-1 for x in dl.values())
                    high=sum(x==d for x in dp.values())+sum(x==d for x in dl.values())
                    if len(residual)!=expected["residual_original_incidence_edges"]:
                        raise AssertionError("actual original P3 residual edge capacity invalid")
                    if low!=expected["residual_low_degree_vertices"] or high!=expected["residual_high_degree_vertices"]:
                        raise AssertionError("actual GQ P3 residual local degree population invalid")
                    mixed=sum((dp[p]!=d) != (dl[l]!=d) for p,l in residual)
                    if mixed!=expected["residual_low_high_edges"]:
                        raise AssertionError("actual residual source edge-degree joint wrong")
                    if any(dp[p]!=d and dl[l]!=d for p,l in residual):
                        raise AssertionError("actual original P3 two affected neighbors create short cycle")
                    m3=None
                    if brute_force_when_small and d==3:
                        m3=0
                        for a,b,c in __import__("itertools").combinations(residual,3):
                            if len({a[0],b[0],c[0]})==3 and len({a[1],b[1],c[1]})==3:
                                m3+=1
                        if m3!=expected_m3:
                            raise AssertionError("independent exhaustive ORIGINAL 3-matchings disagree")
                    samples.append({"source_path":(p0,l1,p2,l3),
                                    "residual_edges":len(residual),
                                    "degree_low":low,"degree_high":high,
                                    "mixed_original_edges":mixed,
                                    "direct_enumerated_matchings":m3})
                    if len(samples)>=max_root_samples:
                        return {"s":d-1,"sampled_actual_original_P3":samples,
                                "all_h_exact_residual_m3":expected_m3,
                                "crosscheck_result":"PASS"}
    raise AssertionError("no genuine original P3 witnesses")


def report(s_values=(2,4,8,16,32)):
    result=[]
    for s in s_values:
        z=all_h_two_closed_source_forest_expectations(s)
        eC=z["expected_TRUE_original_selected_C/B_both_uniform_full_maps"]
        eB=z["expected_TRUE_original_selected_B/B-overlap_both_uniform_full_maps"]
        result.append({**{k:v for k,v in z.items()
                          if k not in ("pB","pC",
                                       "expected_TRUE_original_selected_C/B_both_uniform_full_maps",
                                       "expected_TRUE_original_selected_B/B-overlap_both_uniform_full_maps",
                                       "expected_two_tag_total")},
                       "expected_C_B_fraction":f"{eC.numerator}/{eC.denominator}",
                       "expected_BB_overlap_fraction":f"{eB.numerator}/{eB.denominator}"})
    return {"slice":"HYP105-ISSUE230-D6-AA4-X-EXACT-ORIGINAL-FOREST-CAPACITIES",
            "all_h":result,"root_A":"OPEN","root_B":"OPEN"}


if __name__=="__main__":
    import argparse,json
    p=argparse.ArgumentParser()
    p.add_argument("--check-real-gq",action="store_true")
    opts=p.parse_args()
    out=report()
    if opts.check_real_gq:
        out["real_source_GQ_samples"]={}
        for power in (1,2):
            model=fixture(power,"lex")
            out["real_source_GQ_samples"][str(1<<power)]={
                "P4":independent_actual_source_path_four_after_deletion(model,limit=18),
                "P3":independent_actual_P3_deletion_three_matching(model,max_root_samples=3),
            }
    print(json.dumps(out,indent=2,sort_keys=True))
