"""JPKC-005: alternate ORIGINAL 3-incidence completion of ONE proper P3 seed.

Fully exhaustive true ORIGINAL W(3,2) seven-positive sixsets and all
endpoint-bad seeds; W(3,4) performs only honest structural/unblocked
closure checks, NOT a complete seven-family sixset census.

All-h J14 cap 320 and conditional extension-isolation consequence in
companion note. No root A/B proof, no ASET exponent.
"""
from collections import Counter, defaultdict
from itertools import combinations
import argparse
import json

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_issue230_jpkc002_path_collision_taxonomy import (
    _path_fibers, _edge_incidence_map, BLOCKED,
)
from hyp105_issue230_jpkc004_original_sixset_transport import (
    _degrees, _two_regular,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census, classify_seven_prechecked,
    physical_column_dual, is_connected_column_cycle,
)

ALL_CLASSES=("D6","B-left/A-right","A-left/B-right","C/A","C/B",
             "B/B-overlap","B/B-disjoint")
SEED_REACHABLE=("D6","B-left/A-right","A-left/B-right",
                "B/B-overlap","B/B-disjoint")
MAX_SEEDS_PER_ORIGINAL_SIXSET=320
MAX_PHYSICAL_REALIZATIONS_PER_ORIGINAL_THREE_SEED=16


def _general_half_type(ctx,ids,side):
    """The original incidence POSITION multiplier, no hardcoded K6 palette."""
    factors=tuple(ctx.edges[i][side] for i in ids)
    freq=tuple(sorted(Counter(factors).values(),reverse=True))
    symbol_degrees=_degrees(ctx,ids,side)
    if not _two_regular(symbol_degrees):
        return None
    return {(1,1,1,1,1,1):"A",
            (2,1,1,1,1):"B",
            (2,2,2):"C"}.get(freq)


def general_seven_original(ctx,ids):
    """Exact STRUCTURAL seven-family acceptance on genuine original sixsets.

    This lifts the W32 classifier's incidence-pattern rules to ANY
    physical alphabet size but does NOT imply a complete all-h enumeration
    or independently re-prove every GF5 flow weight.
    """
    ids=tuple(sorted(ids))
    if len(ids)!=6 or len(set(ids))!=6 or ids[0]<0 or ids[-1]>=len(ctx.edges):
        raise ValueError("six distinct original incidence IDs required")
    lt=_general_half_type(ctx,ids,0)
    rt=_general_half_type(ctx,ids,1)
    if lt is None or rt is None:
        return None
    if (lt,rt)==("B","A"):
        return "B-left/A-right"
    if (lt,rt)==("A","B"):
        return "A-left/B-right"
    if lt==rt=="A":
        left=physical_column_dual(ctx.edges,ctx.f,tuple(ctx.edges[i][0] for i in ids))
        right=physical_column_dual(ctx.edges,ctx.g,tuple(ctx.edges[i][1] for i in ids))
        return "D6" if left==right and is_connected_column_cycle(left) else None
    if {lt,rt}=={"C","A"}:
        return "C/A"
    if {lt,rt}=={"C","B"}:
        return "C/B"
    if lt==rt=="B":
        pts=tuple(ctx.edges[i][0] for i in ids)
        lns=tuple(ctx.edges[i][1] for i in ids)
        lp=next(p for p,n in Counter(pts).items() if n==2)
        rp=next(r for r,n in Counter(lns).items() if n==2)
        L={j for j,p in enumerate(pts) if p==lp}
        R={j for j,r in enumerate(lns) if r==rp}
        intersection=len(L & R)
        if intersection not in (0,1):
            raise AssertionError("two distinct incidence IDs cannot duplicate both original factors")
        return "B/B-overlap" if intersection else "B/B-disjoint"
    return None


def _other_gq_anchor(ctx,triple):
    """Recover an alternative true ORIGINAL q--ell--p--r from a 3-ID set."""
    incidences=[ctx.edges[i] for i in triple]
    for p,l in incidences:
        for q,first_l in incidences:
            if first_l!=l or q==p:
                continue
            for second_p,r in incidences:
                if second_p!=p or r==l:
                    continue
                if len({(q,l),(p,l),(p,r)})!=3:
                    continue
                if ctx.projection.get((q,r))==(p,l):
                    return (q,r)
    return None


def _seed_is_physical_P4(ctx,vertices):
    if len(vertices)!=4 or len(set(vertices))!=4:
        return False
    a=ctx.a
    return len({u//a for u in vertices})==4 and len({u%a for u in vertices})==4


def _canonical(ctx,q,r):
    p,l=ctx.projection[q,r]
    return frozenset((ctx.edge_id[q,l],ctx.edge_id[p,l],ctx.edge_id[p,r]))


def _physical_seed_counts_by_Q(ctx,fibers,accepted):
    """Independent actual-physical witness multiplicity falsifier for J14."""
    seed_index=defaultdict(list)
    for (_, _),paths in fibers.items():
        for b,c,tag,ids in paths:
            if tag=="coordinate_repeat":
                continue
            if len(set(ids))!=3:
                raise AssertionError("proper physical three-path repeats ORIGINAL incidence")
            seed_index[tuple(sorted(ids))].append((b,c))
    cardinalities=Counter()
    for Q in accepted:
        total=0
        for trip in combinations(Q,3):
            total+=len(seed_index.get(trip,()))
        cardinalities[Q]=total
        if total>MAX_SEEDS_PER_ORIGINAL_SIXSET:
            raise AssertionError("J14 20*8*2 structural source sixset P3 seed cap violated")
    return cardinalities


def _bad_seed_paths(ctx,fibers):
    """Unique physical ORIENTED endpoints plus original incidence triple.

    Each eligible path preserves its exact source 3 incidence IDs.
    """
    for (u,v),paths in fibers.items():
        q=ctx.fi.get(tuple(sorted((u//ctx.a,v//ctx.a))))
        r=ctx.gi.get(tuple(sorted((u%ctx.a,v%ctx.a))))
        if q is None or r is None or (q,r) not in ctx.projection:
            continue
        p,l=ctx.projection[q,r]
        bad_left=bool(set(ctx.f[q])&set(ctx.f[p]))
        bad_right=bool(set(ctx.g[r])&set(ctx.g[l]))
        if not (bad_left or bad_right):
            continue
        for b,c,tag,ids in paths:
            if tag not in BLOCKED:
                continue
            if not _seed_is_physical_P4(ctx,(u,b,c,v)):
                raise AssertionError("endpoint-bad physical P3 has repeated coordinate")
            if len(set(ids))!=3:
                raise AssertionError("original proper path repeated an incidence")
            yield (u,b,c,v),tuple(sorted(ids)),(q,r)


def alternate_completion_certificate(model,*,max_paths=2_000_000,
                                     max_accepted_sixsets=10_000,
                                     exact_W32=True,
                                     include_examples=False):
    ctx=ProjectionClosure(model)
    if exact_W32 and ctx.s!=2:
        raise ValueError("full original seven-family sixset completion index is W32-only")
    if type(max_accepted_sixsets)!=int or max_accepted_sixsets<1:
        raise ValueError("positive full sixset-completion index budget required")
    _,fibers,_=_path_fibers(ctx,max_paths)
    seeds=list(_bad_seed_paths(ctx,fibers))
    E=len(seeds)
    histogram=Counter()
    per_class=Counter()
    canonical_overlap=Counter()
    alternate_anchor=Counter()
    selected_seed_support=Counter()
    examples={}

    if exact_W32:
        actual=seven_census(model,independent_checks=False,witness_sets=True)
        accepted=actual["sets"]
        if len(accepted)>max_accepted_sixsets:
            raise ValueError("complete ORIGINAL seven-family sixset completion index budget exceeded")
        index=defaultdict(list)
        for Q,tag in accepted.items():
            if general_seven_original(ctx,Q)!=tag:
                raise AssertionError("general-h ORIGINAL structural seven classifier differs from W32")
            for trip in combinations(Q,3):
                index[trip].append((Q,tag))
        Qcounts=_physical_seed_counts_by_Q(ctx,fibers,accepted)
        max_mult=max(Qcounts.values(),default=0)
    else:
        accepted={}
        index={}
        max_mult=None

    physical_seed_by_triple=Counter()
    completion_hits=0
    accepted_extension_paths=0
    second_gq_anchor_hits=0
    seen_seed_triples=set()
    for path,T,(q,r) in seeds:
        seen_seed_triples.add(T)
        physical_seed_by_triple[T]+=1
        canon=_canonical(ctx,q,r)
        options=index.get(T,()) if exact_W32 else ()
        histogram[len(options)]+=1
        if options:
            accepted_extension_paths+=1
            for Q,tag in options:
                completion_hits+=1
                if tag not in SEED_REACHABLE:
                    raise AssertionError("J15 source proper P3 seed cannot extend to any C type")
                U=frozenset(Q)-frozenset(T)
                if len(U)!=3:
                    raise AssertionError("original alternate completion must add THREE distinct incidence IDs")
                if U==canon:
                    raise AssertionError("J9 endpoint-bad canonical GQ closure falsely selected")
                second=_other_gq_anchor(ctx,U)
                # J17 all-h: an ORIGINAL GQ length-three path
                # completing a physical coordinate-proper P4 to
                # a selected two-sided 2-regular Q must be the UNIQUE
                # original endpoint (q,r) projection. Because our
                # endpoint is BAD, canonical completion is forbidden.
                if second is not None:
                    if second!=(q,r) or U!=canon:
                        raise AssertionError(
                            "J17: noncanonical original GQ three-walk falsely "
                            "converted a source P3 to a positive sixset")
                    raise AssertionError(
                        "J9/J17: canonical endpoint-bad original GQ completion "
                        "cannot produce a positive selected sixset")
                second_gq_anchor_hits+=int(second is not None)
                alternate_anchor["second_true_original_GQ_walk" if second else
                                 "not_three_incidence_GQ_walk"]+=1
                canonical_overlap[len(U&canon)]+=1
                per_class[tag]+=1
                if include_examples and tag not in examples:
                    examples[tag]={
                        "seed_original_ids":T,
                        "seed_graph_vertices":path,
                        "first_original_GQ_anchor":(q,r),
                        "original_canonical_incidence_ids":tuple(sorted(canon)),
                        "alternate_completion_original_ids":tuple(sorted(U)),
                        "second_original_GQ_anchor":second,
                        "six_original_ids":Q,
                    }
    if any(n>MAX_PHYSICAL_REALIZATIONS_PER_ORIGINAL_THREE_SEED
           for n in physical_seed_by_triple.values()):
        raise AssertionError("J14 2^3*2 physical three-seed realized more than 16 paths")
    if completion_hits!=sum(per_class.values()) or sum(histogram.values())!=E:
        raise AssertionError("original alternate completion accounting inconsistent")
    if exact_W32:
        if accepted_extension_paths>E or completion_hits>MAX_SEEDS_PER_ORIGINAL_SIXSET*len(accepted):
            raise AssertionError("J14 uniform 320S accepted-seed witness bound violated")
        if sum(Qcounts.values())<completion_hits:
            raise AssertionError("endpoint-bad seed witness exceeds ALL physical paths contained in selected Q")
        if sum(canonical_overlap.values())!=completion_hits:
            raise AssertionError("original canonical/alternate completion edit record incomplete")
        if sum(alternate_anchor.values())!=completion_hits:
            raise AssertionError("second ORIGINAL GQ anchor classification incomplete")
        if histogram[0]!=E-accepted_extension_paths:
            raise AssertionError("positive seed completion coverage mismatch")
        if any(k>2 for k in canonical_overlap):
            raise AssertionError("J9 endpoint-bad canonical completion distance must be >=1")
    # A single original 3-incidence triple has at most 2^3 graph-diagonal
    # choices and each undirected physical P4 at most 2 orientations.
    out={
        "s":ctx.s,"a":ctx.a,"source_scope":"TRUE ORIGINAL GQ complete f,g",
        "endpoint_bad_oriented_proper_P3":E,
        "unique_original_three_incidence_seeds":len(seen_seed_triples),
        "maximum_realized_physical_P3_per_original_three_seed":
            max(physical_seed_by_triple.values(),default=0),
        "J14_universal_path_seeds_per_accepted_original_sixset":320,
        "J14_universal_physical_path_realizations_per_source_triple":16,
        "J15_all_h_C_left_or_right_forbidden_from_proper_P3_seed":True,
        "J17_all_h_only_canonical_original_GQ_three_walk_if_positive":True,
        "J9_endpoint_bad_canonical_completion_excluded":True,
        "all_h_universal_seven_lower_PROVED_A":False,
        "all_h_counterexample_B_constructed":False,
        "full_seven_enumeration_executed":bool(exact_W32),
    }
    if exact_W32:
        out.update({
            "W32_true_original_S":actual["S_seven"],
            "accepted_seed_completion_pairs":completion_hits,
            "endpoint_bad_physical_seeds_with_accepted_alternate_completion":
                accepted_extension_paths,
            "endpoint_bad_physical_seeds_without_accepted_completion":
                E-accepted_extension_paths,
            "J14_witness_320S_verified":completion_hits<=320*actual["S_seven"],
            "observed_max_physical_P3_seed_hits_per_accepted_Q":max_mult,
            "accepted_extension_by_true_original_seven_class":
                {t:per_class[t] for t in ALL_CLASSES},
            "J17_noncanonical_second_GQ_anchor_positive_completions":second_gq_anchor_hits,
            "completion_options_per_oriented_physical_seed":
                dict(sorted(histogram.items())),
            "alternate_three_incidence_completion_GQ_walk_types":
                dict(alternate_anchor),
            "alternate_completion_intersection_with_canonical_three":
                dict(sorted(canonical_overlap.items())),
        })
    if include_examples:
        out["actual_original_completion_examples"]=examples
    return out


def _honest_W34_structural_stress(model):
    """Same true-original W34 point/line assignments; no full seven Q index."""
    ctx=ProjectionClosure(model)
    _,fibers,_=_path_fibers(ctx,2_000_000)
    unblocked_checked=0
    classes=Counter()
    for (u,v),paths in fibers.items():
        q=ctx.fi.get(tuple(sorted((u//ctx.a,v//ctx.a))))
        r=ctx.gi.get(tuple(sorted((u%ctx.a,v%ctx.a))))
        if q is None or r is None or (q,r) not in ctx.projection:
            continue
        canonical=_canonical(ctx,q,r)
        for b,c,status,ids in paths:
            if status!="unblocked":
                continue
            Q=tuple(sorted(set(ids)|canonical))
            if len(Q)!=6:
                raise AssertionError("unblocked PR394 closure is not a six ORIGINAL incidence set")
            tag=general_seven_original(ctx,Q)
            if tag!="B/B-overlap":
                raise AssertionError("all-h original sixset GQ closure motif mismatch")
            classes[tag]+=1
            unblocked_checked+=1
    answer=alternate_completion_certificate(
        model,exact_W32=False)
    if unblocked_checked==0:
        raise AssertionError("true original W34 fixture has no unblocked GQ witness")
    answer["unblocked_original_sixset_structural_crosscheck"]=unblocked_checked
    answer["unblocked_Q_classes"]=dict(classes)
    answer["full_W34_seven_census_PROVED"]=False
    return answer


def report(*,spread=False):
    out=[]
    for scheme in ("lex","reverse","S68","S72"):
        out.append({"scheme":scheme,**alternate_completion_certificate(
            fixture(1,scheme))})
    for scheme in ("lex","random"):
        out.append({"scheme":scheme,**_honest_W34_structural_stress(fixture(2,scheme))})
    if spread:
        from hyp105_issue230_jpkc_spread_adversary import spread_adversary_model
        model,cert=spread_adversary_model(2)
        out.append({"scheme":"D4-true-original-symplectic-spread",
                    "original_Mf":cert["M_f_original_exact"],
                    **_honest_W34_structural_stress(model)})
    return {
        "all_h_J14_320_seed_multiplicity_proved_in_docs":True,
        "all_h_J15_proper_seed_no_C_accepted_class":True,
        "root_A_PROVED":False,
        "no_false_full_W34_GF5_enumeration":True,
        "records":out,
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--spread",action="store_true")
    args=parser.parse_args()
    print(json.dumps(report(spread=args.spread),sort_keys=True,indent=2))
