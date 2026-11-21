"""GIO-001.1: uniform flag-deletion resilience and disjoint motif packing.

The all-order argument is in docs/research/GIO-001-RESILIENCE.md.
Exact rational ledgers instantiate only FORMAL choices of existential graph
constants, not published numeric constants. Finite genuine W32/W34
censuses are adversarial falsifiers, never an asymptotic proof.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, product
from math import isqrt
import argparse
import json
import random
from pathlib import Path

from hyp105_low_publication_partition_referee import model
from hyp105_aa4_branch_a_integrated_referee import (
    actual_edges, canonical_cycle, historical_bbo, physical_d6,
    source_d6, source_bbo_inverse, source_first_bbo_w32, factor_first_d6,
)

SCHEMA = "mathlab.gio001.resilience.v1"
CAP = Q(1,32)


def ceil(x):
    x=Q(x)
    return -(-x.numerator//x.denominator)


def ceil_sqrt(x):
    n=ceil(x)
    if n<0:
        raise ValueError("nonnegative squared budget required")
    r=isqrt(n)
    return r+(r*r<n)


def root_ledger(C0=Q(1),c0=Q(1)):
    """Fixed order CAP -> external C0,c0 -> R,T -> CORE -> rho -> h0.
    This arithmetic certifies implications for any admissible external
    constants; the supplied default numbers are hypothetical only.
    """
    if type(C0) is not Q or type(c0) is not Q or C0<1 or not 0<c0<=1:
        raise ValueError("exact rational existential constants required")
    u=Q(1,2**32);t=Q(1,2**16)
    v=(1+u)*(1+u*u);nu=(1+u)*v
    M=(1+u*u)*(1+Q(23,16)*t)
    A=2*v+Q(23,4)*t**3+4*t**6
    assert 2*v<Q(10,7)**2 and 4*nu<Q(17,4)
    assert 8*(nu+M)<17 and 24*(nu+M)<49
    assert 16*(1+u*u)*(1+2*t)+16*v*t+16*u*u+4*u*nu<17
    assert 32*(1+u)*nu*v*(t+(1+u)*(Q(10,7)+t**3))<46

    # HEAVY: E_T >= s^4/8, deletions cost at most two edges per flag,
    # so surviving distinct owners >= s^4/32.
    ell=Q(1,16)-CAP
    assert ell==Q(1,32)
    independent=ell**2/(ell+4*M)
    # One coherent cut pair: /4. One heavy endpoint color: /2.
    # Real balanced top-r subgraph: / (2 A).
    density=independent/(16*A)
    R=ceil(1/density)
    assert R==ceil(512*A*(1+128*M))
    T=ceil(Q(17,2)*R**3*C0**3)
    assert Q(17,2)*R**3*C0**3<=T

    K=10
    c=Q(7,8)-CAP-4*M/(K+1)
    w=(4*c)**3/A**2
    assert c>0 and w>0
    delta=min(c0/R**6,w/4)
    assert 0<delta<=1
    q2=4**2*(K+1)**2
    q3=4**3*(K+1)**3
    L6=1+ceil(36*nu*T*T)
    L4=q2*q2*ceil_sqrt(nu*L6)+17*T
    E=q3*ceil_sqrt(17*L6)
    B=ceil_sqrt(46*(K+1)*T)
    D=4*ceil_sqrt(B*T*L4)

    # Reserve four equal error budgets of w/8; deletion charge is
    # order s^6, so choose the actual rho AFTER all moment constants.
    budget=w/8
    rho=min(CAP,budget**2/(12*q3*q3*L6))
    assert 0<rho<=CAP and 12*rho*q3*q3*L6<=budget**2
    s0=max(2**32,ceil(49*T/budget),ceil((E/budget)**2),
           ceil((D/budget)**8))
    h0=(s0-1).bit_length()
    ss=1<<h0
    assert 49*T<=budget*ss
    assert E*E<=budget*budget*ss
    assert D**8<=budget**8*ss
    assert delta<=w/4 and delta<=c0/R**6
    packing_count=(rho*ss**4//6)+1
    assert 6*(packing_count-1)<=rho*ss**4
    assert 6*packing_count>rho*ss**4
    # Historical single-sign minimum for every accepted BBo, and
    # alternating D6 sign. This is NOT the sum-of-events R3 weight.
    p=Q(5175,51**6)
    return dict(FORMAL_ONLY=True,external_numeric_constants_unknown=True,
        C0=str(C0),c0=str(c0),rho_cap=str(CAP),rho=str(rho),delta=str(delta),
        R=R,T=str(T),K=K,core_coefficient=str(c),walk_coefficient=str(w),
        q2=q2,q3=q3,L6=str(L6),L4=str(L4),E=str(E),B=str(B),D=str(D),
        error_budget_each=str(budget),total_error_fraction="1/2",
        sufficient_h0=h0,packing_at_formal_h0=str(packing_count),
        independent_collision_probability_lower=str(p),
        independent_collision_tail_exponent_per_witness=str(p/8),
        endpoint_deleted_projection_union_coefficient=12,
        root_proved_by_finite_experiments=False,
        new_ASET_exponent=False)


def deletion_set(m,Z):
    Z=tuple(Z)
    n=len(m["flags"])
    if (len(set(Z))!=len(Z) or
            any(type(i) is not int or i<0 or i>=n for i in Z)):
        raise ValueError("distinct genuine original flag IDs required")
    return frozenset(Z)


def validate_asymptotic_budget(h,deleted_count,ledger):
    """Pure integer/rational guard; no gigantic geometry construction."""
    if type(h) is not int or h<ledger["sufficient_h0"]:
        raise ValueError("outside sufficient dyadic threshold")
    if type(deleted_count) is not int or deleted_count<0:
        raise ValueError("nonnegative integer deletion count required")
    s=1<<h
    if deleted_count>Q(ledger["rho"])*s**4:
        raise ValueError("deletion exceeds proved budget")
    return s


def pencils(m):
    by_p=defaultdict(set);by_l=defaultdict(set)
    for p,l in m["flags"]:
        by_p[p].add(l);by_l[l].add(p)
    return by_p,by_l


def anchor_ids(m,q,r):
    p,l=m["projection"][q,r]
    lookup=m["flag_to_id"]
    return lookup[q,l],lookup[p,l],lookup[p,r]


def anchor_damage(m,Z):
    """Two independent exact descriptions of the union of deleted anchors."""
    Z=deletion_set(m,Z)
    by_p,by_l=pencils(m)
    direct={(q,r) for q,r in m["projection"]
            if Z.intersection(anchor_ids(m,q,r))}
    incident=set(m["flags"])
    union=set()
    s=m["s"]
    for i in Z:
        a,b=m["flags"][i]
        left={(a,r) for p in by_l[b]-{a} for r in by_p[p]-{b}}
        middle={(q,r) for q in by_l[b]-{a} for r in by_p[a]-{b}}
        right={(q,b) for l in by_p[a]-{b} for q in by_l[l]-{a}}
        assert len(left)==len(middle)==len(right)==s*s
        assert not (left&middle or left&right or middle&right)
        assert not ((left|middle|right)&incident)
        union.update(left|middle|right)
    assert direct==union
    # Reconstruct all four real ordered physical endpoint orientations.
    oriented=set()
    for q,r in union:
        f=m["f"][q];g=m["g"][r]
        for x,y in product(f,g):
            oriented.add(((x,y),(next(v for v in f if v!=x),
                                 next(v for v in g if v!=y))))
    assert len(oriented)==4*len(union)<=12*s*s*len(Z)
    return direct,oriented


def original_corner_index(m,A):
    """Index source-owner corners, without building any physical adjacency."""
    index=defaultdict(set)
    for i in A:
        p,l=m["flags"][i]
        for corner in product(m["f"][p],m["g"][l]):
            index[corner].add(i)
    return index


def opposite(m,i,u):
    p,l=m["flags"][i]
    x,y=u
    f=m["f"][p];g=m["g"][l]
    assert x in f and y in g
    return next(a for a in f if a!=x),next(b for b in g if b!=y)


def source_first_d6(m,A):
    """Walk original owner IDs and forced opposite rectangle corners.

    Unlike physical rainbow DFS this traverses a source-corner incidence
    index and canonicalizes by minimum ORIGINAL owner and its neighbors.
    No calls to actual_edges or physical_d6.
    """
    index=original_corner_index(m,A)
    out={}
    for start in sorted(A):
        p,l=m["flags"][start]
        for corner in product(m["f"][p],m["g"][l]):
            def rec(ids,corners):
                v=opposite(m,ids[-1],corners[-1])
                if len(ids)==6:
                    if v==corner and ids[1]<ids[-1]:
                        key=tuple(sorted(ids))
                        assert key not in out
                        cyc=canonical_cycle(corners)
                        assert source_d6(m,key)==cyc
                        out[key]=cyc
                    return
                if any(v[0]==a or v[1]==b for a,b in corners):
                    return
                for j in index[v]:
                    if j>start and j not in ids:
                        rec(ids+(j,),corners+(v,))
            rec((start,),(corner,))
    return out


def six_from_path(m,path,residual,A):
    """Physical-path side of the proof, full projection then available anchors."""
    if len(set(residual))!=3 or not set(residual)<=A:
        return None
    x=[v[0] for v in path];y=[v[1] for v in path]
    if len(set(x))!=4 or len(set(y))!=4:
        return None
    q=m["point_by_pair"].get(tuple(sorted((x[0],x[-1]))))
    r=m["line_by_pair"].get(tuple(sorted((y[0],y[-1]))))
    if q is None or r is None or (q,r) not in m["projection"]:
        return None
    p,l=m["projection"][q,r]
    anchors=anchor_ids(m,q,r)
    if not set(anchors)<=A:
        return None
    if set(x)&set(m["f"][p]) or set(y)&set(m["g"][l]):
        return None
    ids=tuple(sorted(anchors+tuple(residual)))
    assert len(set(ids))==6
    assert historical_bbo(m,ids)
    return ids


def physical_bbo(m,A,C=None):
    """Only residual three-walk owners must be in C; all six must be in A."""
    C=A if C is None else C
    if not C<=A:
        raise ValueError("paired CORE must be a subset of available owners")
    adj,own=actual_edges(m,C)
    out=defaultdict(set)
    for u in adj:
        for v in adj[u]:
            for w in adj[v]:
                for z in adj[w]:
                    path=(u,v,w,z)
                    res=tuple(own[tuple(sorted((a,b)))]
                              for a,b in zip(path,path[1:]))
                    key=six_from_path(m,path,res,A)
                    if key is not None:
                        out[key].add(path)
    for k,paths in out.items():
        assert len(paths)==2 and next(iter(paths))[::-1] in paths
        assert source_bbo_inverse(m,k)==paths
    return dict(out)


def source_first_bbo(m,A,C=None):
    """Independent middle-OWNER join of two source rectangle intersections.

    The middle source label forces its two opposite joining corners.
    No physical walk enumeration or physical-side classifier is called.
    Restore the full six-ID classification using original factor supports
    and the source-only inverse from the integrated theorem.
    """
    C=A if C is None else C
    if not C<=A:
        raise ValueError("paired CORE must be available")
    index=original_corner_index(m,C)
    out={}
    for j in sorted(C):
        p,l=m["flags"][j]
        for u in product(m["f"][p],m["g"][l]):
            v=opposite(m,j,u)
            if v<=u:
                continue
            for i in index[u]-{j}:
                a=opposite(m,i,u)
                for k in index[v]-{i,j}:
                    b=opposite(m,k,v)
                    if len({a[0],u[0],v[0],b[0]})!=4 or len({a[1],u[1],v[1],b[1]})!=4:
                        continue
                    q=m["point_by_pair"].get(tuple(sorted((a[0],b[0]))))
                    r=m["line_by_pair"].get(tuple(sorted((a[1],b[1]))))
                    if q is None or r is None or (q,r) not in m["projection"]:
                        continue
                    ids=tuple(sorted(anchor_ids(m,q,r)+(i,j,k)))
                    if len(set(ids))!=6 or not set(ids)<=A or not historical_bbo(m,ids):
                        continue
                    paths=source_bbo_inverse(m,ids)
                    if not paths:
                        continue
                    # Both typed residual orders must align. The genuine
                    # middle-owner join supplies one of these two orders.
                    assert (a,u,v,b) in paths and len(paths)==2
                    assert ids not in out
                    out[ids]=paths
    return out


def dual_model(m):
    flags=tuple((l,p) for p,l in m["flags"])
    return dict(m,flags=flags,f=m["g"],g=m["f"],
        projection={(r,q):(l,p) for (q,r),(p,l) in m["projection"].items()},
        point_by_pair=m["line_by_pair"],line_by_pair=m["point_by_pair"],
        flag_to_id={z:i for i,z in enumerate(flags)})


def masks(m,B):
    n=len(m["flags"])
    p,l=m["flags"][0]
    star_p={i for i,(q,r) in enumerate(m["flags"]) if q==p}
    star_l={i for i,(q,r) in enumerate(m["flags"]) if r==l}
    disjoint=next(i for i,(q,r) in enumerate(m["flags"]) if q!=p and r!=l)
    adj,own=actual_edges(m,range(n))
    owner_score=Counter()
    for (u,v),i in own.items():
        owner_score[i]+=len(adj[u])+len(adj[v])
    ranked=sorted(range(n),key=lambda i:(-owner_score[i],i))
    out={"empty":set(),"singleton":{0},"point_star":star_p,
         "line_star":star_l,"mixed_star_union":star_p|star_l,
         "disconnected_pair":{0,disjoint},
         "map_dependent":set(ranked[:max(1,n//12)]),
         "seeded_mask":set(random.Random(230+17*m["s"]).sample(range(n),max(1,n//10))),
         "delete_all_diagnostic":set(range(n))}
    if B:
        ids=next(iter(B))
        fs=[m["flags"][i] for i in ids]
        rp=next(p for p,n in Counter(p for p,l in fs).items() if n==2)
        rl=next(l for l,n in Counter(l for p,l in fs).items() if n==2)
        out["middle_anchor_only"]={m["flag_to_id"][rp,rl]}
    return {k:frozenset(z) for k,z in out.items()}


def greedy_pack(motifs,initial_deleted=()):
    """Deterministic coefficient-blind, finite packing of actual six-ID sets."""
    used=set(initial_deleted);ret=[]
    for k in sorted(motifs):
        if len(k)!=6 or len(set(k))!=6:
            raise ValueError("six distinct original flags required")
        if used.isdisjoint(k):
            ret.append(k);used.update(k)
    return tuple(ret)


@lru_cache(maxsize=6)
def finite_case(s,scheme):
    m=model(s,scheme,"full")
    full=frozenset(range(len(m["flags"])))
    d=source_first_d6(m,full)
    b=source_first_bbo(m,full)
    assert d==physical_d6(m,full)
    assert b==physical_bbo(m,full)
    if s==2:
        assert d==factor_first_d6(m)
        assert b==source_first_bbo_w32(m)
    assert set(d).isdisjoint(b)
    ret=[]
    for name,Z in masks(m,b).items():
        A=full-Z
        damage,oriented=anchor_damage(m,Z)
        # Independent full-source family filter is exact: removing flags
        # cannot alter the labels, historical class or unique full projection.
        expected_d={k:v for k,v in d.items() if set(k)<=A}
        expected_b={k:v for k,v in b.items() if set(k)<=A}
        pd=physical_d6(m,A)
        pb=physical_bbo(m,A)
        assert pd==expected_d and pb==expected_b
        assert all(set(k)<=A for k in {*pd,*pb})
        if name=="middle_anchor_only":
            lost=[k for k in b if set(k)&Z]
            assert lost and all(k not in pb for k in lost)
        # Test FULL available anchors distinct from a smaller actual CORE.
        C=frozenset(i for i in A if i%2==0)
        pc=physical_bbo(m,A,C)
        sc=source_first_bbo(m,A,C)
        assert pc==sc
        for k in pc:
            assert k in pb
        packed=greedy_pack(set(pd)|set(pb))
        assert len({i for k in packed for i in k})==6*len(packed)
        assert all(set(k)<=A for k in packed)
        ret.append(dict(mask=name,deleted=len(Z),surviving=len(A),
            damaged_projections=len(damage),damaged_ordered_endpoints=len(oriented),
            deletion_endpoint_bound=12*s*s*len(Z),D6=len(pd),
            produced_BBo=len(pb),smaller_core_produced_BBo=len(pc),
            greedy_disjoint_witnesses=len(packed),independent_exact_sets_agree=True))
    dm=dual_model(m)
    assert set(source_first_d6(dm,full))==set(d)
    assert set(source_first_bbo(dm,full))==set(b)
    # One mixed mask checked under complete duality (same original IDs).
    Z=masks(m,b)["mixed_star_union"]
    a0,_=anchor_damage(m,Z);a1,_=anchor_damage(dm,Z)
    assert {(r,q) for q,r in a0}==a1
    return dict(s=s,scheme=scheme,original_flags=len(full),
        full_D6=len(d),full_produced_BBo=len(b),duality_verified=True,masks=ret)


def certificate():
    ledgers=[root_ledger(c,d) for c,d in ((Q(1),Q(1)),(Q(2),Q(1,5)),(Q(7,3),Q(1,17)))]
    cases=[finite_case(s,scheme) for s,scheme in
            ((2,"lex"),(2,"reverse"),(2,"correlated"),(4,"lex"),(4,"correlated"))]
    assert all(x["duality_verified"] for x in cases)
    return dict(schema=SCHEMA,foundation_issue=230,issue=791,
        foundation_commit="a49e1de8a46b6afbeb668c4413647fd4eeb63d8a",
        claim="RESILIENCE_AND_PACKING_PROOF_CANDIDATE",
        formal_ledgers=ledgers,finite_cases=cases,
        finite_checks_not_all_order_proof=True,
        general_ASET_exponent=False,external_peer_review_received=False)


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--out",default="gio-resilience-certificate.json")
    args=p.parse_args()
    result=certificate()
    Path(args.out).write_text(json.dumps(result,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print("GIO_RESILIENCE_CERTIFICATE="+json.dumps(result,sort_keys=True))
