"""JPKC-008: exact ORIGINAL 3x3 Hall matching and globally shared source demand.

All-h J25–J27 structural statements have independent proofs in the companion
note. One coherent globally injective f,g serves ALL source demands.
No Root A/B theorem; a Hall-feasible A/A is NOT automatically a positive D6.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb
import argparse
import json

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_issue230_jpkc002_path_collision_taxonomy import _path_fibers
from hyp105_issue230_jpkc005_alternate_three_completion import (
    _bad_seed_paths,general_seven_original,
)
from hyp105_issue230_jpkc006_source_topology_sharp_charge import (
    _a_sides,_path_source,_other_source_completion,
)
from hyp105_issue230_jpkc007_completion_deficit_ledger import (
    _source_matching_stages,_stratified_indices,
)

def hall_certificate(ctx,points,lines,*,crosscheck_permutations=True):
    """All 7 Hall subsets; full source 3x3 incidence induced graph.

    Deficiency = max_A(|A|-|N(A)|), including the empty set (zero).
    The exact number of source incidence perfect matchings is 0 or 1
    because a genuine original GQ incidence graph has girth >=8.
    """
    P=tuple(sorted(points))
    L=tuple(sorted(lines))
    if len(P)!=3 or len(set(P))!=3 or len(L)!=3 or len(set(L))!=3:
        raise ValueError("Hall source demand requires distinct ORIGINAL 3 points and 3 lines")
    if any(x not in range(ctx.v) for x in P+L):
        raise ValueError("Hall source demand has out-of-range ORIGINAL factor")
    masks=tuple(sum(1<<j for j,l in enumerate(L) if (p,l) in ctx.edge_id)
                for p in P)
    deficiency=0
    obstructing=[]
    for size in (1,2,3):
        for inds in combinations(range(3),size):
            union=0
            for i in inds:
                union|=masks[i]
            gap=size-union.bit_count()
            if gap>0:
                obstructing.append((tuple(P[i] for i in inds),union.bit_count(),gap))
            deficiency=max(deficiency,gap)
    witness=None
    match_count=0
    if crosscheck_permutations or deficiency==0:
        for perm in permutations(L):
            if all((p,l) in ctx.edge_id for p,l in zip(P,perm)):
                match_count+=1
                witness=tuple(ctx.edge_id[(p,l)] for p,l in zip(P,perm))
    if match_count>1:
        raise AssertionError("J25 genuine GQ 3x3 source matching is not unique")
    if crosscheck_permutations and (match_count==1)!=(deficiency==0):
        raise AssertionError("J26 Hall deficiency and actual ORIGINAL matching disagree")
    if deficiency==0 and match_count!=1:
        raise AssertionError("J26 Hall satisfied but no true original perfect matching")
    if deficiency>0 and match_count:
        raise AssertionError("J26 Hall-deficient but ORIGINAL matching found")
    return {
        "P":P,"L":L,"row_incidence_masks":masks,
        "deficiency":deficiency,
        "hall_feasible":deficiency==0,
        "unique_original_matching_ids":witness,
        "matched_incidence_permutations":match_count,
        "witness_minimal_hall_gap":
            min(obstructing,key=lambda x:(len(x[0]),-x[2]))
            if obstructing else None,
    }


def _P4_endpoint_pair(labels,source_triple):
    """Recover uniquely BOTH degree-one endpoints from 3 physical Ka pair edges."""
    degrees=Counter()
    for source in source_triple:
        degrees.update(labels[source])
    if sorted(degrees.values())!=[1,1,2,2]:
        raise AssertionError(
            "J28 each physical A-half source triple must be a simple 3-edge P4")
    endpoints=tuple(sorted(z for z,degree in degrees.items() if degree==1))
    if len(endpoints)!=2:
        raise AssertionError("J28 A-half source endpoints not uniquely determined")
    return endpoints


def source_key_original_anchor(ctx,P,L):
    """J28 ALL h: the pair of A-half SOURCE triples fixes original (q,r)."""
    q=ctx.fi.get(_P4_endpoint_pair(ctx.f,P))
    r=ctx.gi.get(_P4_endpoint_pair(ctx.g,L))
    if q is None or r is None or (q,r) not in ctx.projection:
        raise AssertionError("J28 genuine original A-half key lacks a unique nonincident GQ anchor")
    return q,r


def _demand(ctx,path):
    """Exact complete source-point and source-line A-half candidate product."""
    src=set(_path_source(ctx,path))
    left=_a_sides(ctx,path,0)
    right=_a_sides(ctx,path,1)
    for p3 in left:
        for l3 in right:
            P=tuple(sorted(p3))
            L=tuple(sorted(l3))
            if len(set(P))!=3 or len(set(L))!=3:
                raise AssertionError("A-side physically valid source triple duplicated factor")
            yield P,L,src


def hall_coherence_certificate(model,*,limit_seeds=None,exact_W32=True,
                               max_paths=2_000_000,
                               max_source_demand_pairs=1_000_000,
                               record_examples=False):
    """All actual selected seeds for each fixed legal globally complete map.

    No fictitious independently optimized source adjacency matrix:
    every identical source-key (P,L) has ONE globally fixed matching.
    """
    ctx=ProjectionClosure(model)
    if exact_W32 and ctx.s!=2:
        raise ValueError("full ORIGINAL seven-family scope is W32 only")
    if type(max_source_demand_pairs) is not int or max_source_demand_pairs<1:
        raise ValueError("positive original source demand pair budget required")
    _,fibers,_=_path_fibers(ctx,max_paths)
    seeds=list(_bad_seed_paths(ctx,fibers))
    chosen=[seeds[i] for i in _stratified_indices(
        len(seeds),len(seeds) if limit_seeds is None else limit_seeds)]
    demand_cache={}
    demand_multiplicity=Counter()
    demand_anchors=defaultdict(set)
    per_seed=Counter()
    totals=Counter()
    hall_gaps=Counter()
    sample={}
    covered=0

    for path,T,anchor in chosen:
        source=set(T)
        positives=0
        expected,_=_source_matching_stages(ctx,path)
        stage=Counter()
        for P,L,_ in _demand(ctx,path):
            key=(P,L)
            recovered=source_key_original_anchor(ctx,P,L)
            if recovered!=anchor:
                raise AssertionError(
                    "J28 original source A-half pair key demanded by a different GQ anchor")
            if key not in demand_cache:
                demand_cache[key]=hall_certificate(ctx,P,L)
            c=demand_cache[key]
            demand_multiplicity[key]+=1
            demand_anchors[key].add(anchor)
            stage["source_triple_pairs"]+=1
            if stage["source_triple_pairs"]+totals["source_triple_pairs"]>max_source_demand_pairs:
                raise ValueError("complete true original Hall demand pair budget exceeded")
            if not c["hall_feasible"]:
                stage["hall_deficient_pairs"]+=1
                hall_gaps[c["deficiency"]]+=1
                if record_examples and "hall" not in sample:
                    sample["hall"]={"seed":path,"anchor":anchor,
                                    "source_P":P,"source_L":L,
                                    "hall_witness":c["witness_minimal_hall_gap"]}
                continue
            stage["hall_feasible_pairs"]+=1
            ids=c["unique_original_matching_ids"]
            if ids is None or len(set(ids))!=3 or set(ids)&source:
                raise AssertionError("J25 legal unique matching repeats ORIGINAL source")
            Q=tuple(sorted(source|set(ids)))
            selected=(general_seven_original(ctx,Q)=="D6")
            if selected:
                stage["aligned_D6"]+=1
                positives+=1
            else:
                stage["nonaligned_AA"]+=1
            if record_examples and selected and "positive" not in sample:
                sample["positive"]={"seed":path,"anchor":anchor,
                                    "source_P":P,"source_L":L,"Q":Q}
        if stage["source_triple_pairs"]!=sum(stage[k] for k in (
            "hall_deficient_pairs","hall_feasible_pairs")):
            raise AssertionError("J27 total 3x3 source-pair Hall telescope failed")
        if stage["hall_feasible_pairs"]!=stage["aligned_D6"]+stage["nonaligned_AA"]:
            raise AssertionError("J27 Hall-feasible positional dual split failed")
        if stage["source_triple_pairs"]*6!=expected["raw_matching_bijections"]:
            raise AssertionError("J27 independent JPKC007 original 6LR source budget mismatch")
        if 6*stage["source_triple_pairs"]-stage["hall_feasible_pairs"]!=expected[
                "missing_original_incidence_matching"]:
            raise AssertionError("J27 old six-permutation missing original incidence ledger disagrees")
        if stage["nonaligned_AA"]!=expected["nonaligned_AA_original_duals"]:
            raise AssertionError("J27 independently counted true original nonaligned A/A mismatch")
        if stage["aligned_D6"]!=expected["source_positive_D6"]:
            raise AssertionError("J27 independently counted true original D6 mismatch")
        actual=_other_source_completion(ctx,path,T,anchor)
        if positives!=sum(v=="D6" for v in actual.values()):
            raise AssertionError("J27 actual ORIGINAL D6 transfer disagrees with JPKC006")
        covered+=int(positives>0)
        for field,n in stage.items():
            totals[field]+=n
        per_seed[positives]+=1
    if totals["source_triple_pairs"]!=sum(demand_multiplicity.values()):
        raise AssertionError("J27 global demand aggregation lost source-pair requests")
    unique_feasible=sum(c["hall_feasible"] for c in demand_cache.values())
    weighted_feasible=sum(demand_multiplicity[k] for k,c in demand_cache.items()
                          if c["hall_feasible"])
    if weighted_feasible!=totals["hall_feasible_pairs"]:
        raise AssertionError("J27 shared true ORIGINAL point-line source assignments diverged")
    if totals["source_triple_pairs"]!=totals["hall_deficient_pairs"]+weighted_feasible:
        raise AssertionError("J27 globally shared Hall source capacity identity failed")
    if sum(per_seed.values())!=len(chosen):
        raise AssertionError("J27 true original physical seed count mismatch")
    # Genuine global sharing: a 3x3 factor pair has one fixed status and
    # (when feasible) one fixed 3-incidence matching for ALL seed/anchor demands.
    repeat=sum(v-1 for v in demand_multiplicity.values())
    across=sum(len(demand_anchors[k])>1 for k in demand_cache)
    if across:
        raise AssertionError(
            "J28 exact globally shared source A-half key cannot cross ORIGINAL GQ anchors")
    result={
        "s":ctx.s,"a":ctx.a,
        "full_true_original_endpoint_bad_P3_population":len(seeds),
        "actual_endpoint_bad_P3_examined":len(chosen),
        "complete_endpoint_bad_census":len(chosen)==len(seeds),
        "J25_all_h_girth8_unique_3x3_matching":True,
        "J26_all_h_Hall_3subset_exact":True,
        "J27_all_h_source_matched_D6_telescope":True,
        "J27_global_original_factor_key_shared_across_all_seeds":True,
        "J28_all_h_A_half_source_key_unique_GQ_anchor":True,
        "J28_cross_original_anchor_sharing_is_impossible":True,
        "original_source_demand_pair_budget":totals["source_triple_pairs"],
        "globally_distinct_original_3x3_factor_pair_keys":len(demand_cache),
        "source_demands_repeated_over_different_physical_P3":repeat,
        "keys_demanded_by_multiple_original_GQ_anchors":across,
        "unique_Hall_feasible_original_factor_pairs":unique_feasible,
        "total_Hall_feasible_source_demand_occurrences":weighted_feasible,
        "true_ORIGINAL_source_pair_Hall_deficiency_histogram":
            {str(k):v for k,v in sorted(hall_gaps.items())},
        "source_matching_deficit":{k:totals[k] for k in (
            "source_triple_pairs","hall_deficient_pairs","hall_feasible_pairs",
            "nonaligned_AA","aligned_D6")},
        "seeds_with_true_positive_original_D6":covered,
        "actual_D6_extension_multiplicity_per_seed":
            {str(k):v for k,v in sorted(per_seed.items())},
        "no_all_h_source_matching_existence_lower_PROVED":True,
        "root_A_proved":False,"root_B_constructed":False,
        "full_W34_original_seven_GF5_census":False,
        "J29_global_original_3matching_capacity":
            all_h_original_3matching_capacity(ctx),
    }
    if record_examples:
        result["actual_original_examples"]=sample
    return result


def all_h_original_3matching_capacity(ctx):
    """J29 closed count of original 3edge matchings in regular bipartite GQ.

    Original line graph has N vertices, degree 2*(d-1),
    N*(d-1) edges and 2*V*choose(d,3) triangles (only original
    source point/line stars). Independent triples there correspond
    exactly to size-three incidence matchings.
    """
    V=ctx.v
    d=ctx.delta
    N=len(ctx.edges)
    if N!=V*d:
        raise AssertionError("J29 true GQ original incidence regularity violated")
    adjacent_original_incidence_pairs=N*(d-1)
    conflict_wedges=N*comb(2*(d-1),2)
    conflict_triangles=2*V*comb(d,3)
    result=(comb(N,3)-adjacent_original_incidence_pairs*(N-2)
            +conflict_wedges-conflict_triangles)
    if result<0 or result>comb(V,3)**2:
        raise AssertionError("J29 exact original matching capacity out of range")
    return {
        "original_three_edge_matchings_exact_formula":result,
        "source_triple_pair_choices":comb(V,3)**2,
        "source_incidence_edges":N,
        "source_incidence_degree":d,
        "line_graph_adjacent_pairs":adjacent_original_incidence_pairs,
        "line_graph_wedges":conflict_wedges,
        "line_graph_triangles":conflict_triangles,
        "J29_all_h_exact_matching_capacity":True,
    }


def all_W32_factor_triples_hall_theorem(model,*,max_checks=300000):
    """All C(15,3)^2 ORIGINAL 3x3 induced pairs, not random/local fixture."""
    ctx=ProjectionClosure(model)
    if ctx.s!=2:
        raise ValueError("full ORIGINAL source factor Hall validation W32 only")
    total=comb(ctx.v,3)**2
    if total>max_checks:
        raise ValueError("complete W32 factor triple grid budget exceeded")
    hist=Counter()
    for P in combinations(range(ctx.v),3):
        for L in combinations(range(ctx.v),3):
            h=hall_certificate(ctx,P,L,crosscheck_permutations=True)
            hist[h["deficiency"]]+=1
            if h["matched_incidence_permutations"]>1:
                raise AssertionError("original GQ forbidden alternating cycle appeared")
    if sum(hist.values())!=total:
        raise AssertionError("full original point/line factor triple grid incomplete")
    capacity=all_h_original_3matching_capacity(ctx)
    if hist[0]!=capacity["original_three_edge_matchings_exact_formula"]:
        raise AssertionError(
            "J29 exhaustive TRUE GQ Hall-feasible source pairs do not match "
            "independent 3-edge matching line-graph closed formula")
    return {"entire_original_3x3_source_factor_grid":total,
            **capacity,
            "all_h_unique_original_perfect_matching_verified":True,
            "true_GQ_hall_deficiency_histogram":dict(sorted(hist.items()))}


def report(*,w34_seeds=8):
    rows=[]
    for name in ("lex","reverse","S68","S72"):
        rows.append({"scheme":name,**hall_coherence_certificate(fixture(1,name))})
    for name in ("lex","random"):
        rows.append({"scheme":name,**hall_coherence_certificate(
            fixture(2,name),limit_seeds=w34_seeds,exact_W32=False)})
    from hyp105_issue230_jpkc_spread_adversary import spread_adversary_model
    model,cert=spread_adversary_model(2)
    rows.append({"scheme":"D4-true-original-symplectic-spread",
                 "M_f_true_original":cert["M_f_original_exact"],
                 **hall_coherence_certificate(
                     model,limit_seeds=w34_seeds,exact_W32=False)})
    return {
        "all_h_J25_J26_J27_true_original_Hall_source_coherence":True,
        "no_root_A_or_B":True,
        "rows":rows,
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--w34-seeds",type=int,default=8)
    args=parser.parse_args()
    print(json.dumps(report(w34_seeds=args.w34_seeds),indent=2,sort_keys=True))
