"""JPKC-006: sharp all-h source-P3 charging, non-GQ U topology and exact targeted extensions.

J18–J21 analytical statements are proved in the companion note. The W32
tests check EVERY true ORIGINAL endpoint-bad P3 seed and its accepted
source-sixsets against a separate exhaustive 62,370-candidate oracle.

W34 uses targeted, COMPLETE-per-selected-seed construction without claiming
a full seven-family W34 census. No Root A/B, R3, or ASET proof.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
import argparse
import json

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_issue230_jpkc002_path_collision_taxonomy import _path_fibers
from hyp105_issue230_jpkc005_alternate_three_completion import (
    general_seven_original, _bad_seed_paths, _canonical,
    _other_gq_anchor,
)
from hyp105_g5e2b3e1b0_seven_signature import seven_census

CLASSES=("D6","B-left/A-right","A-left/B-right",
         "B/B-overlap","B/B-disjoint","C/A","C/B")
NON_GQ_TARGETS=("D6","B-left/A-right","A-left/B-right")
SOURCE_U_TOPOLOGIES=("matching_3K2","point_wedge_plus_edge",
                     "line_wedge_plus_edge","GQ_P4","other")
J18_SHARP_SOURCE_TRIPLE_REALIZATIONS=4
J19_SELECTED_SOURCE_SIXSET_CAP=24
J19_CLASS_CAPS={
    "D6":24, "B-left/A-right":16, "A-left/B-right":16,
    "B/B-overlap":16, "B/B-disjoint":16,
    "C/A":0,"C/B":0,
}
# Endpoint-bad seeds cannot belong to B/B by all-h J17, so cap for
# eligible endpoint-bad witness Q is 24, with non-D6 <=16.


def _signature(ctx,ids):
    """Unordered true ORIGINAL bipartite incidence source graph of triple U."""
    if len(ids)!=3 or len(set(ids))!=3:
        raise ValueError("three DISTINCT ORIGINAL incidence IDs required")
    pl=[ctx.edges[i] for i in ids]
    pd=Counter(p for p,_ in pl)
    ld=Counter(l for _,l in pl)
    ptype=tuple(sorted(pd.values(),reverse=True))
    ltype=tuple(sorted(ld.values(),reverse=True))
    if ptype==(1,1,1) and ltype==(1,1,1):
        return "matching_3K2"
    if ptype==(2,1) and ltype==(1,1,1):
        return "point_wedge_plus_edge"
    if ptype==(1,1,1) and ltype==(2,1):
        return "line_wedge_plus_edge"
    if ptype==(2,1) and ltype==(2,1):
        q=next(p for p,n in pd.items() if n==1)
        r=next(l for l,n in ld.items() if n==1)
        p=next(p for p,n in pd.items() if n==2)
        ell=next(l for l,n in ld.items() if n==2)
        if set(pl)!={(q,ell),(p,ell),(p,r)}:
            raise AssertionError("simple bipartite 2+2 three-edge source is forced P4")
        if ctx.projection.get((q,r))!=(p,ell):
            raise AssertionError("nonincident ORIGINAL GQ P4 violates unique projection")
        return "GQ_P4"
    return "other"


def _a_sides(ctx,path,side):
    """All physical C6-completing triples for a fixed projected P4.

    A 3-edge P4 has four distinct symbols z0,z1,z2,z3.
    Its C6 completion is z3--z4--z5--z0, with z4,z5 BOTH outside P4.
    These are exact, not sampled, candidates of physical A-type halves.
    """
    a=ctx.a
    positions=[v//a if side==0 else v%a for v in path]
    if len(set(positions))!=4:
        raise AssertionError("physical original P3 must be coordinate-proper")
    inv=ctx.fi if side==0 else ctx.gi
    unused=sorted(set(range(a))-set(positions))
    source=set(ctx.edges[i][side] for i in _path_source(ctx,path))
    results=[]
    for z4,z5 in permutations(unused,2):
        pairlist=(
            tuple(sorted((positions[3],z4))),
            tuple(sorted((z4,z5))),
            tuple(sorted((z5,positions[0]))),
        )
        ids=tuple(inv.get(pair) for pair in pairlist)
        if any(k is None for k in ids) or len(set(ids))!=3 or source.intersection(ids):
            continue
        results.append(ids)
    return tuple(results)


def _path_source(ctx,path):
    """Definition-level independent ORIGINAL ID lookup for a grid path."""
    index=ctx.edge_id
    a=ctx.a
    ans=[]
    for u,v in zip(path,path[1:]):
        x1,y1=divmod(u,a)
        x2,y2=divmod(v,a)
        point=ctx.fi.get(tuple(sorted((x1,x2))))
        line=ctx.gi.get(tuple(sorted((y1,y2))))
        if point is None or line is None or (point,line) not in index:
            raise AssertionError("non-original graph edge in physical P3")
        ans.append(index[(point,line)])
    if len(set(ans))!=3:
        raise AssertionError("physical P3 repeats original incidence source")
    return tuple(ans)


def _a_b_wedges(ctx,path,T,q,r,left_A):
    """Enumerate exact A/B or B/A source triples from physical A-completion.

    left_A=True: left has A six-cycle, right has B=C4+C2:
    one extra original line r once, another ell' twice. The 3
    candidate left point factors form a P4 on the three extra edges.
    Reverse dual if left_A=False.
    """
    side=0 if left_A else 1
    center=r if left_A else q
    seed_coords={v%ctx.a if left_A else v//ctx.a for v in path}
    single=ctx.point_lines if left_A else ctx.lines
    # For left_A, three original points p_i, of which 1 incident
    # with r and other 2 lie on the repeated ORIGINAL line ell'.
    # For right_A, three original lines l_i, of which 1 is
    # incident with q and other 2 pass through the repeated point p'.
    common=ctx.point_lines if left_A else ctx.lines
    chosen=[]
    for factors in _a_sides(ctx,path,side):
        for index in range(3):
            only=factors[index]
            others=[factors[j] for j in range(3) if j!=index]
            if left_A:
                # factor is an ORIGINAL point; center is ORIGINAL line r
                if (only,center) not in ctx.edge_id:
                    continue
                shared=ctx.point_lines[others[0]]&ctx.point_lines[others[1]]
                if len(shared)>1:
                    raise AssertionError("original partial linearity on two points")
                if not shared:
                    continue
                repeat=next(iter(shared))
                if set(ctx.g[repeat])&seed_coords:
                    continue
                U=(ctx.edge_id[(only,center)],
                   ctx.edge_id[(others[0],repeat)],
                   ctx.edge_id[(others[1],repeat)])
            else:
                # factor is an ORIGINAL line; center is ORIGINAL point q
                if (center,only) not in ctx.edge_id:
                    continue
                shared=ctx.lines[others[0]]&ctx.lines[others[1]]
                if len(shared)>1:
                    raise AssertionError("original partial linearity on two lines")
                if not shared:
                    continue
                repeat=next(iter(shared))
                if set(ctx.f[repeat])&seed_coords:
                    continue
                U=(ctx.edge_id[(center,only)],
                   ctx.edge_id[(repeat,others[0])],
                   ctx.edge_id[(repeat,others[1])])
            if len(set(U))==3 and not set(U)&set(T):
                chosen.append(tuple(sorted(U)))
    return set(chosen)


def _a_a_matches(ctx,path,T):
    """Complete C6/C6 physical A/A candidates from two P4 complements."""
    left=_a_sides(ctx,path,0)
    right=_a_sides(ctx,path,1)
    found=set()
    for ps in left:
        for ls in right:
            for assignment in permutations(ls):
                U=[]
                for p,l in zip(ps,assignment):
                    k=ctx.edge_id.get((p,l))
                    if k is None:
                        break
                    U.append(k)
                if len(U)!=3 or len(set(U))!=3 or set(U)&set(T):
                    continue
                found.add(tuple(sorted(U)))
    return found


def _other_source_completion(ctx,path,T,qr):
    """EXACT per-physical-P3 source candidates in all reachable classes.

    Only three possible positive classes survive J15/J17/J20:
    D6, B-left/A-right, A-left/B-right. Neither seven_census
    nor a global S-proxy is queried.
    """
    q,r=qr
    T=tuple(sorted(T))
    if T!=tuple(sorted(_path_source(ctx,path))):
        raise AssertionError("provided source triple is NOT physical P3")
    outputs={}
    sets=[
        ("D6",_a_a_matches(ctx,path,T)),
        ("B-left/A-right",_a_b_wedges(ctx,path,T,q,r,left_A=False)),
        ("A-left/B-right",_a_b_wedges(ctx,path,T,q,r,left_A=True)),
    ]
    for expected,candidates in sets:
        for U in candidates:
            Q=tuple(sorted(T+U))
            if len(set(Q))!=6:
                raise AssertionError("positive source complement repeated incidence")
            actual=general_seven_original(ctx,Q)
            if expected=="D6" and actual is None:
                # A/A physical degree-2 candidates can have DIFFERENT
                # left/right six-column cycles. Only matched connected
                # ORIGINAL column duals are genuinely D6 selected.
                continue
            if actual!=expected:
                raise AssertionError(
                    "original topology completion generated a false seven class: "
                    +repr((expected,actual,T,U)))
            if _signature(ctx,U)== "GQ_P4":
                raise AssertionError("J17 true GQ second closure unexpectedly positive")
            if U==tuple(sorted(_canonical(ctx,q,r))):
                raise AssertionError("J9 bad canonical completion falsely positive")
            if Q in outputs and outputs[Q]!=expected:
                raise AssertionError("one ORIGINAL sixset assigned two seven classes")
            outputs[Q]=expected
    return outputs


def _local_three_source_paths(ctx,source):
    """Independent exact enumeration of BOTH physical diagonals / source edge.

    Unlike the global graph adjacency oracle this builds only source edges
    from the three incidence IDs and tests all edge orderings, without
    K2 or seven-family code.
    """
    a=ctx.a
    edges=[]
    for eid in source:
        p,l=ctx.edges[eid]
        x0,x1=ctx.f[p]
        y0,y1=ctx.g[l]
        edges.append(((x0*a+y0,x1*a+y1),
                      (x0*a+y1,x1*a+y0)))
    witnesses=set()
    for perm in permutations(range(3)):
        for choice in product((0,1),repeat=3):
            seq=[edges[perm[i]][choice[i]] for i in range(3)]
            e1,e2,e3=(set(s) for s in seq)
            j1=e1&e2
            j2=e2&e3
            if len(j1)!=1 or len(j2)!=1 or j1==j2:
                continue
            path=(next(iter(e1-j1)),next(iter(j1)),next(iter(j2)),next(iter(e3-j2)))
            if len(set(path))!=4:
                continue
            if (len({x//a for x in path})==4
                    and len({x%a for x in path})==4):
                witnesses.add(path)
    if len(witnesses)>J18_SHARP_SOURCE_TRIPLE_REALIZATIONS:
        raise AssertionError("J18 <=4 proper ORIGINAL path realizations per 3source failed")
    return witnesses


def sharp_charge_certificate(model,*,limit_endpoint_seeds=None,
                             exact_W32=True,max_paths=2_000_000,
                             max_accepted=20_000,record_examples=False):
    ctx=ProjectionClosure(model)
    if exact_W32 and ctx.s!=2:
        raise ValueError("full ORIGINAL seven-family Q charge check is W32 only")
    if limit_endpoint_seeds is not None and (
            type(limit_endpoint_seeds)!=int or limit_endpoint_seeds<1):
        raise ValueError("positive selected endpoint-bad physical seed limit required")
    _,fibers,_=_path_fibers(ctx,max_paths)
    seeds=list(_bad_seed_paths(ctx,fibers))
    if limit_endpoint_seeds is None:
        selected=seeds
    else:
        # Deterministic SOURCE-genuine prefix of physically ordered seeds.
        # Partial W34 results are never claimed as a full E census.
        selected=seeds[:limit_endpoint_seeds]
    source_triples=defaultdict(set)
    alternate=Counter()
    class_hits=Counter()
    topology=Counter()
    coverage=0
    examples={}
    physical_per_source=defaultdict(set)
    by_Q=Counter()
    witness_pairs=set()
    for path,T,qr in selected:
        physical_per_source[T].add(path)
        if T not in source_triples:
            source_triples[T]=_local_three_source_paths(ctx,T)
        if path not in source_triples[T]:
            raise AssertionError("independently enumerated true ORIGINAL seed not found")
        found=_other_source_completion(ctx,path,T,qr)
        coverage+=bool(found)
        for Q,tag in found.items():
            if tag not in ("D6","B-left/A-right","A-left/B-right"):
                raise AssertionError("J20 impossible endpoint-bad positive class")
            U=tuple(sorted(set(Q)-set(T)))
            t=_signature(ctx,U)
            expected={
                "D6":"matching_3K2",
                "B-left/A-right":"point_wedge_plus_edge",
                "A-left/B-right":"line_wedge_plus_edge",
            }[tag]
            if t!=expected:
                raise AssertionError("J20 non-GQ ORIGINAL U source topology violates class")
            if (path,Q) in witness_pairs:
                raise AssertionError("duplicate original (seed,Q) accepted completion")
            witness_pairs.add((path,Q))
            topology[t]+=1
            by_Q[Q]+=1
            class_hits[tag]+=1
            if record_examples and tag not in examples:
                examples[tag]={"physical_seed":path,"original_source_T":T,
                               "completion_U":U,"Q":Q,"source_topology":t,
                               "first_original_anchor":qr}
    if max(map(len,source_triples.values()),default=0)>4:
        raise AssertionError("J18 source triple four-direction cap violated")
    if max(by_Q.values(),default=0)>J19_SELECTED_SOURCE_SIXSET_CAP:
        raise AssertionError("J19 accepted sixset maximum 24 proper seeds violated")
    if len(witness_pairs)!=sum(class_hits.values()):
        raise AssertionError("source-positive physical seed-to-Q charge mismatch")
    if exact_W32:
        census=seven_census(model,independent_checks=False,witness_sets=True)
        if len(census["sets"])>max_accepted:
            raise ValueError("full W32 accepted-Q index budget exceeded")
        idx=defaultdict(set)
        for Q,tag in census["sets"].items():
            for t in combinations(Q,3):
                idx[t].add((Q,tag))
        indexed=0
        for path,T,qr in selected:
            expected=dict(idx.get(T,()))
            if _other_source_completion(ctx,path,T,qr)!=expected:
                raise AssertionError(
                    "independent ORIGINAL A/B/A/A physical completion mismatches "
                    "FULL 62,370-candidate W32 exact seven-family index")
            indexed+=len(expected)
        if indexed!=len(witness_pairs):
            raise AssertionError("complete W32 accepted Q witness count mismatched")
        for Q,tag in census["sets"].items():
            c=0
            for t in combinations(Q,3):
                c+=len(_local_three_source_paths(ctx,t))
            if c>J19_CLASS_CAPS[tag]:
                raise AssertionError("J19 class-specific 24/16 original sixset charge failed")
        if sum(class_hits.values())>J19_SELECTED_SOURCE_SIXSET_CAP*census["S_seven"]:
            raise AssertionError("new 24S globally coherent bound violated")
    return {
        "scope":"exact per seed ORIGINAL non-GQ alternate extension, NOT an image proxy",
        "s":ctx.s,"a":ctx.a,
        "full_endpoint_bad_population":len(seeds),
        "endpoint_bad_physical_seeds_examined":len(selected),
        "complete_endpoint_bad_coverage":len(selected)==len(seeds),
        "seeds_with_true_original_positive_alternates":coverage,
        "accepted_seed_sixset_pairs":len(witness_pairs),
        "selected_class_positive_source_hits":{tag:class_hits[tag] for tag in CLASSES},
        "U_source_topology":{k:topology[k] for k in SOURCE_U_TOPOLOGIES},
        "max_realized_complete_source_three_seed":
            max((len(v) for v in source_triples.values()),default=0),
        "max_physical_P3_per_accepted_Q_in_sample":max(by_Q.values(),default=0),
        "J18_all_h_4_source_triple_cap_verified":True,
        "J19_all_h_24_selected_sixset_cap_verified":True,
        "J20_all_h_only_matching_or_wedge_nonGQ_complements":True,
        "full_W32_independent_accepted_Q_oracle_compared":bool(exact_W32),
        "no_full_W34_Q_census":not exact_W32,
        "Root_A_proved":False,
        "Root_B_constructed":False,
        **({"actual_original_examples":examples} if record_examples else {}),
    }


def report(*,w34_sample=32,spread=True):
    records=[]
    for name in ("lex","reverse","S68","S72"):
        records.append({"scheme":name,**sharp_charge_certificate(fixture(1,name))})
    for name in ("lex","random"):
        records.append({"scheme":name,**sharp_charge_certificate(
            fixture(2,name),limit_endpoint_seeds=w34_sample,exact_W32=False)})
    if spread:
        from hyp105_issue230_jpkc_spread_adversary import spread_adversary_model
        m,cert=spread_adversary_model(2)
        records.append({"scheme":"D4-true-original-symplectic-spread",
                        "original_Mf":cert["M_f_original_exact"],
                        **sharp_charge_certificate(
                            m,limit_endpoint_seeds=w34_sample,exact_W32=False)})
    return {
        "J18_all_h_4_instead_of_16":True,
        "J19_selected_sixset_24_instead_of_320":True,
        "J20_nonGQ_matching_wedge_exact_type":True,
        "no_root_A_B_result":True,
        "records":records,
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--w34-sample",type=int,default=32)
    parser.add_argument("--no-spread",action="store_true")
    args=parser.parse_args()
    print(json.dumps(report(w34_sample=args.w34_sample,spread=not args.no_spread),
                     indent=2,sort_keys=True))
