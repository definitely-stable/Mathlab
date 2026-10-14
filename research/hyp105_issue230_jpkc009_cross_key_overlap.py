"""JPKC-009: fixed-ORIGINAL-triple Hall capacities and CROSS-KEY anchor coupling.

ALL-h J30–J33 are exactly scoped combinatorial statements; counts use
ONE true globally injected f,g and original W(3,s) incidence.
This does NOT prove original positive GF5 S=Omega(s^6) or an all-h
cross-anchor positivity lower bound. Draft research-only.
"""
from collections import Counter,defaultdict
from itertools import combinations,product
from math import comb
import argparse
import json

from hyp105_issue230_projection import ProjectionClosure,fixture
from hyp105_issue230_jpkc002_path_collision_taxonomy import _path_fibers
from hyp105_issue230_jpkc005_alternate_three_completion import _bad_seed_paths
from hyp105_issue230_jpkc006_source_topology_sharp_charge import _other_source_completion
from hyp105_issue230_jpkc007_completion_deficit_ledger import _stratified_indices
from hyp105_issue230_jpkc008_source_hall_coherence import (
    _demand,hall_certificate,source_key_original_anchor,
    _P4_endpoint_pair,all_h_original_3matching_capacity,
)


def point_triple_matching_capacity(ctx,points,*,check_direct=False):
    """J31 ALL-h number of ORIGINAL disjoint-line SDR for 3 source points.

    GQ unique common source line between any two distinct collinear
    original points. A three-point ORIGINAL GQ triangle either lies
    on a SINGLE common line or is forbidden by incidence girth >=8.

    For d=s+1:
        C(P) = d^3 - d*c(P) + 2*t(P).
    """
    P=tuple(sorted(points))
    if (len(P)!=3 or len(set(P))!=3
            or any(type(p)!=int or not 0<=p<ctx.v for p in P)):
        raise ValueError("three distinct in-range ORIGINAL source points required")
    adjacent=sum(bool(ctx.point_lines[i]&ctx.point_lines[j])
                 for i,j in combinations(P,2))
    triple=int(bool(ctx.point_lines[P[0]] & ctx.point_lines[P[1]]
                    & ctx.point_lines[P[2]]))
    if adjacent==3 and not triple:
        raise AssertionError("GQ original point collinearity triangle violates girth 8")
    d=ctx.delta
    cap=d**3-d*adjacent+2*triple
    if cap<0 or cap>d**3:
        raise AssertionError("J31 impossible ORIGINAL point-triple SDR capacity")
    if check_direct:
        candidates=[ctx.point_lines[p] for p in P]
        count=sum(len(set(lines))==3 for lines in product(*candidates))
        if count!=cap:
            raise AssertionError("J31 direct GQ line-SDR enumeration != exact capacity")
        # Unique source 3x3 matching by J25: each line triple counted once.
        # Distinct SDR witnesses imply distinct unordered L source triples.
        result=set(tuple(sorted(lines)) for lines in product(*candidates)
                   if len(set(lines))==3)
        if len(result)!=cap:
            raise AssertionError("J31 source triple line-SDR reused an ORIGINAL key")
    return {"P":P,"collinear_point_pairs":adjacent,
            "single_common_original_line":triple,
            "unique_original_line_triples_satisfying_Hall":cap,
            "J31_exact_capacity":True}


def line_triple_matching_capacity(ctx,lines,*,check_direct=False):
    """J31 dual EXACT point-triple matching source capacity."""
    L=tuple(sorted(lines))
    if (len(L)!=3 or len(set(L))!=3
            or any(type(l)!=int or not 0<=l<ctx.v for l in L)):
        raise ValueError("three distinct in-range ORIGINAL source lines required")
    concurrent=sum(bool(ctx.lines[i]&ctx.lines[j])
                   for i,j in combinations(L,2))
    triple=int(bool(ctx.lines[L[0]] & ctx.lines[L[1]] & ctx.lines[L[2]]))
    if concurrent==3 and not triple:
        raise AssertionError("GQ original line concurrency triangle violates girth 8")
    d=ctx.delta
    cap=d**3-d*concurrent+2*triple
    if cap<0 or cap>d**3:
        raise AssertionError("J31 impossible ORIGINAL line-triple SDR capacity")
    if check_direct:
        candidates=[ctx.lines[l] for l in L]
        result=[ps for ps in product(*candidates) if len(set(ps))==3]
        if len(result)!=cap or len(set(tuple(sorted(ps)) for ps in result))!=cap:
            raise AssertionError("J31 direct dual original point matching capacity mismatch")
    return {"L":L,"concurrent_line_pairs":concurrent,
            "single_common_original_point":triple,
            "unique_original_point_triples_satisfying_Hall":cap,
            "J31_exact_dual_capacity":True}


def global_triple_capacity_identity(ctx,*,full_brute=False):
    """J32 exact global collinear pair-count identity = independent J29."""
    V,d=ctx.v,ctx.delta
    collinear_pairs=V*comb(d,2)
    collinear_triples=V*comb(d,3)
    summed=comb(V,3)*d**3-d*collinear_pairs*(V-2)+2*collinear_triples
    prior=all_h_original_3matching_capacity(ctx)
    if summed!=prior["original_three_edge_matchings_exact_formula"]:
        raise AssertionError("J32 two INDEPENDENT global 3matching formulas disagree")
    histogram=Counter()
    if full_brute:
        if V>85:
            raise ValueError("J32 brute verification capped at true ORIGINAL V<=85")
        explicit=0
        for P in combinations(range(V),3):
            row=point_triple_matching_capacity(ctx,P)
            explicit+=row["unique_original_line_triples_satisfying_Hall"]
            histogram[(row["collinear_point_pairs"],
                       row["single_common_original_line"])]+=1
        if explicit!=summed:
            raise AssertionError("J32 complete original source-point-triple sum disagrees")
        if sum(histogram.values())!=comb(V,3):
            raise AssertionError("J32 original point-triple topology distribution incomplete")
    return {
        "V":V,"d":d,
        "original_collinear_point_pair_count":collinear_pairs,
        "original_common_line_point_triples":collinear_triples,
        "source_matching_capacity_from_point_triples":summed,
        "source_matching_capacity_independent_linegraph_J29":
            prior["original_three_edge_matchings_exact_formula"],
        "complete_original_triple_sum_checked":bool(full_brute),
        "point_triple_type_distribution":{
            str(k):v for k,v in sorted(histogram.items())} if full_brute else None,
        "J32_exact_global_source_capacity_identity":True,
    }


def cross_key_certificate(model,*,limit_seeds=None,max_paths=2_000_000,
                          max_keys=1_000_000,check_direct=True,
                          full_global_source_triples=False):
    """J33 exact source demand graph and distinct-key cross-ORIGINAL-anchor overlaps.

    Vertices: true ORIGINAL point triples P (left), ORIGINAL line triples L
    (right). A TRUE physical P3 contributes demanded edges (P,L). A fixed
    edge can be repeated only WITHIN one ORIGINAL (q,r) anchor (J28).
    A fixed left P can connect to DIFFERENT right anchors r; a fixed
    right L can connect to DIFFERENT left anchors q.

    Every demand uses the SAME globally injected physical labels f,g.
    """
    ctx=ProjectionClosure(model)
    if type(max_keys)!=int or max_keys<1:
        raise ValueError("positive cross-source demand key budget required")
    _,fibers,_=_path_fibers(ctx,max_paths)
    seeds=list(_bad_seed_paths(ctx,fibers))
    if not seeds:
        raise ValueError("true source map has zero endpoint-bad proper P3 seeds")
    indices=_stratified_indices(len(seeds),
        len(seeds) if limit_seeds is None else limit_seeds)
    chosen=[seeds[i] for i in indices]
    key_weight=Counter()
    edge_anchor={}
    source_left_anchor={}
    source_right_anchor={}
    left_neighbors=defaultdict(set)
    right_neighbors=defaultdict(set)
    matched_left=defaultdict(set)
    matched_right=defaultdict(set)
    selected_left=defaultdict(set)
    selected_right=defaultdict(set)
    hall_cache={}
    totals=Counter()

    for path,T,(q,r) in chosen:
        direct_D6=0
        for P,L,_ in _demand(ctx,path):
            key=(P,L)
            if key not in key_weight and len(key_weight)>=max_keys:
                raise ValueError("complete cross-source distinct key budget exceeded")
            if key not in edge_anchor:
                anchor=source_key_original_anchor(ctx,P,L)
                if anchor!=(q,r):
                    raise AssertionError("J28 exact source key recovered a different original anchor")
                edge_anchor[key]=anchor
            if edge_anchor[key]!=(q,r):
                raise AssertionError("J28 same source key demanded by different original GQ anchors")
            if P not in source_left_anchor:
                source_left_anchor[P]=q
            if source_left_anchor[P]!=q:
                raise AssertionError("J30 source left triple fixes its original point endpoint q")
            if L not in source_right_anchor:
                source_right_anchor[L]=r
            if source_right_anchor[L]!=r:
                raise AssertionError("J30 source right triple fixes its original line endpoint r")

            if key not in hall_cache:
                hall_cache[key]=hall_certificate(ctx,P,L)
            hall=hall_cache[key]
            key_weight[key]+=1
            left_neighbors[P].add(L)
            right_neighbors[L].add(P)
            totals["original_source_pair_demand_occurrences"]+=1
            if hall["hall_feasible"]:
                totals["original_Hall_feasible_occurrences"]+=1
                matched_left[P].add(L)
                matched_right[L].add(P)
                matched_ids=hall["unique_original_matching_ids"]
                Q=tuple(sorted((*T,*matched_ids)))
                if len(set(Q))!=6:
                    raise AssertionError("true original source matched D6 reused an incidence")
                from hyp105_issue230_jpkc005_alternate_three_completion import general_seven_original
                if general_seven_original(ctx,Q)=="D6":
                    totals["original_selected_D6_occurrences"]+=1
                    selected_left[P].add(L)
                    selected_right[L].add(P)
                    direct_D6+=1
                else:
                    totals["original_AA_nonaligned_occurrences"]+=1
            else:
                totals["original_Hall_deficient_occurrences"]+=1
        predicted=_other_source_completion(ctx,path,T,(q,r))
        if direct_D6!=sum(tag=="D6" for tag in predicted.values()):
            raise AssertionError("J33 exact original source D6 witness differs from independent oracle")

    left_capacity={}
    right_capacity={}
    for P in left_neighbors:
        calc=point_triple_matching_capacity(ctx,P,check_direct=check_direct)
        left_capacity[P]=calc["unique_original_line_triples_satisfying_Hall"]
        if len(matched_left[P])>left_capacity[P]:
            raise AssertionError("J31 source P node exceeds EXACT ORIGINAL Hall matching capacity")
    for L in right_neighbors:
        calc=line_triple_matching_capacity(ctx,L,check_direct=check_direct)
        right_capacity[L]=calc["unique_original_point_triples_satisfying_Hall"]
        if len(matched_right[L])>right_capacity[L]:
            raise AssertionError("J31 source L node exceeds EXACT DUAL Hall matching capacity")

    def overlap_by_side(neighbors,side):
        # Count unordered distinct demanded source EDGES meeting at a vertex,
        # but whose opposite factor endpoints belong to DIFFERENT GQ anchors.
        # Uses unique (P,L) keys, not repeated physical path multiplicity.
        within=across=0
        vertices_shared=0
        opposite=source_right_anchor if side=="left" else source_left_anchor
        max_anchor_degree=0
        for fixed,others in neighbors.items():
            by_anchor=Counter(opposite[k] for k in others)
            a=len(others)
            possible=comb(a,2)
            w=sum(comb(z,2) for z in by_anchor.values())
            across+=possible-w
            within+=w
            vertices_shared+=int(len(by_anchor)>1)
            max_anchor_degree=max(max_anchor_degree,len(by_anchor))
        return {"distinct_key_pairs_same_source_triple_same_original_anchor":within,
                "distinct_key_pairs_same_source_triple_DIFFERENT_original_anchors":across,
                "source_triples_joining_at_least_two_different_anchors":vertices_shared,
                "max_different_anchors_at_one_source_triple":max_anchor_degree}

    left=overlap_by_side(left_neighbors,"left")
    right=overlap_by_side(right_neighbors,"right")
    left_hall=overlap_by_side(matched_left,"left")
    right_hall=overlap_by_side(matched_right,"right")
    left_d6=overlap_by_side(selected_left,"left")
    right_d6=overlap_by_side(selected_right,"right")
    for all_row,hall_row,selected_row in (
        (left,left_hall,left_d6),(right,right_hall,right_d6)):
        for suffix in ("distinct_key_pairs_same_source_triple_DIFFERENT_original_anchors",
                       "distinct_key_pairs_same_source_triple_same_original_anchor"):
            if not 0<=selected_row[suffix]<=hall_row[suffix]<=all_row[suffix]:
                raise AssertionError(
                    "J34 ORIGINAL source graph D6 ⊆ Hall ⊆ all demand cross-anchor coupling broken")
    raw=len(key_weight)
    if sum(len(z) for z in left_neighbors.values())!=raw:
        raise AssertionError("J33 left source demand graph edge mismatch")
    if sum(len(z) for z in right_neighbors.values())!=raw:
        raise AssertionError("J33 right source demand graph edge mismatch")
    if totals["original_source_pair_demand_occurrences"]!=sum(key_weight.values()):
        raise AssertionError("J33 repeated original source-key demand mismatch")
    if totals["original_Hall_feasible_occurrences"]!=(
        totals["original_selected_D6_occurrences"]+
        totals["original_AA_nonaligned_occurrences"]):
        raise AssertionError("J33 true original Hall/selected D6 positional telescope failed")
    if sum(len(z) for z in matched_left.values())!=sum(
            len(z) for z in matched_right.values()):
        raise AssertionError("J33 Hall-feasible unique matching edge graph mismatch")
    global_capacity=global_triple_capacity_identity(
        ctx,full_brute=full_global_source_triples)
    if len(hall_cache)!=raw:
        raise AssertionError("J33 global original Hall matching source-key cache drift")
    return {
        "s":ctx.s,"a":ctx.a,
        "complete_globally_injective_original_f_g":True,
        "full_true_endpoint_bad_P3_population":len(seeds),
        "exact_endpoint_bad_physical_P3_examined":len(chosen),
        "complete_original_endpoint_bad_seed_census":len(chosen)==len(seeds),
        "distinct_original_source_left_point_triples":len(left_neighbors),
        "distinct_original_source_right_line_triples":len(right_neighbors),
        "distinct_original_bipartite_source_demand_edges":raw,
        "repeated_source_edge_demand_occurrences":sum(key_weight.values())-raw,
        "original_Hall_feasible_distinct_source_edges":sum(hall["hall_feasible"] for hall in hall_cache.values()),
        "all_h_J30_unique_one_sided_source_triple_anchor":True,
        "all_h_J31_exact_left_and_dual_Hall_star_capacity":True,
        "all_h_J32_global_capacity_equals_J29":True,
        "all_h_J33_cross_key_demand_graph_double_count_exact":True,
        "left_point_triple_source_overlap":left,
        "right_line_triple_source_overlap":right,
        "left_Hall_feasible_source_overlap":left_hall,
        "right_Hall_feasible_source_overlap":right_hall,
        "left_actual_GF5_D6_source_overlap":left_d6,
        "right_actual_GF5_D6_source_overlap":right_d6,
        "J34_exact_nested_Hall_vs_positive_overlap_certified":True,
        "original_demand_stage":dict(sorted(totals.items())),
        "source_triple_Hall_capacity_observed_max_left":max(left_capacity.values(),default=0),
        "source_triple_Hall_capacity_observed_max_right":max(right_capacity.values(),default=0),
        "complete_source_triple_star_capacity_checked":bool(check_direct),
        "global_original_source_Hall_capacity":global_capacity,
        "does_not_prove_cross_anchor_positive_extension":True,
        "root_A_proved":False,"root_B_constructed":False,
    }


def report(*,w34_seeds=8):
    rows=[]
    for scheme in ("lex","reverse","S68","S72"):
        rows.append({"scheme":scheme,**cross_key_certificate(
            fixture(1,scheme),full_global_source_triples=True)})
    for scheme in ("lex","random"):
        rows.append({"scheme":scheme,**cross_key_certificate(
            fixture(2,scheme),limit_seeds=w34_seeds)})
    from hyp105_issue230_jpkc_spread_adversary import spread_adversary_model
    model,proof=spread_adversary_model(2)
    rows.append({"scheme":"D4-true-original-symplectic-spread",
                "original_M_f":proof["M_f_original_exact"],
                **cross_key_certificate(model,limit_seeds=w34_seeds)})
    return {
       "research_scope":"cross-key original point/line triple coupling with exact Hall star capacities",
       "all_h_J30_J31_J32_J33_exact_and_restricted":True,
       "does_NOT_prove_root_A_or_B":True,
       "records":rows,
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--w34-seeds",type=int,default=8)
    args=parser.parse_args()
    print(json.dumps(report(w34_seeds=args.w34_seeds),indent=2,sort_keys=True))
