"""AA4-MIXBOOK: exact ALL-h defect formula for the #672 mixed blocker.

For every true W(3,s), arbitrary COMPLETE globally injected correlated
source point/line maps f,g, and arbitrary retained ORIGINAL incidence-ID
core I (no probabilistic assumptions), the source book sum Phi from
#672's mixed full/core inequality has an EXACT decomposition

    Phi = B_blocked_original_triples + Psi_incident_original_books.

Phi enumerates original book witnesses (i=(u,L) IN I, oriented f(u),
oriented g(L), source p, q collinear p, original r through p), with
coordinate compatibility:
    p in S_k, q in S_x, y in g(r).
Psi counts exactly the witnesses where q is incident with r.
All other witnesses have q NOT incident with r; by the generalized
quadrangle axiom their original nonincident q-r projection has unique
point p, which was already chosen. Source-pair maps are globally
injective, so each surviving book has a UNIQUE physical triple
(v0=(x,y),v1=(k,t),v3=(z,w)) and conversely. Hence equality, not just
the inequality B<=Phi of #672.

The original anchor flag (p,r) belongs to the FULL source and need not
be retained in I. This source-first combinatorial identity holds for
every h without asserting an improved uniform exponent or the global
Branch A theorem.

A genuine W32/W34 finite oracle evaluates both the direct source book
partition and a FULLY INDEPENDENT physical-first source projection
triple census, in point/line-dual orientations and arbitrary original
cores. No old pinned certificate is used for evaluation.
"""
from collections import Counter
from itertools import combinations

from hyp105_full_physical_degree_tail import genuine_source, physical
from hyp105_physical_degree_energy import minimal_alphabet, _verify_typed_injections


def _true_source_data(power, f, g, core_ids, dual):
    if type(power) is not int or power not in (1,2):
        raise ValueError("independent true source finite oracle permits h=1,2")
    s,V,actual_flags=genuine_source(power)
    a=minimal_alphabet(V)
    f=tuple(map(tuple,f));g=tuple(map(tuple,g))
    _verify_typed_injections(a,V,f,g)
    flags=(tuple((ell,p) for p,ell in actual_flags) if dual
           else tuple(actual_flags))
    if dual:f,g=g,f
    ids=(tuple(range(len(flags))) if core_ids is None else tuple(core_ids))
    if (len(set(ids))!=len(ids) or
            any(type(i) is not int or not 0<=i<len(flags) for i in ids)):
        raise ValueError("unique genuine original core flag IDs required")
    pencils=[set() for _ in range(V)]
    onlines=[set() for _ in range(V)]
    for p,ell in flags:
        pencils[p].add(ell)
        onlines[ell].add(p)
    if any(len(z)!=s+1 for z in pencils+onlines):
        raise AssertionError("not regular original W(3,s) point-line incidence")
    collinear=[set().union(*(onlines[ell] for ell in pencils[p]))-{p}
               for p in range(V)]
    if any(len(z)!=s*(s+1) for z in collinear):
        raise AssertionError("original source GQ collinearity degree invalid")
    return s,V,a,flags,f,g,tuple(sorted(ids)),pencils,onlines,collinear


def exact_source_book_partition(power,f,g,core_ids=None,*,dual=False):
    """Direct ORIGINAL source witness partition Phi=B+Psi (all-h theorem).

    Compute ALL witnesses without constructing physical edges or paths.
    Bad witnesses have q INCIDENT with r. Good ones uniquely map to
    blocked triples via K_a global pair injections. Check their
    unique source-projection p and source flag provenance.
    """
    (s,V,a,flags,f,g,ids,pencils,onlines,C)=_true_source_data(
        power,f,g,core_ids,dual)
    S=[set() for _ in range(a)]
    for p,uv in enumerate(f):
        for x in uv:S[x].add(p)
    phi_books=incident_books=0
    triples={}
    good_by_original_flag=Counter()
    bad_by_original_flag=Counter()
    for i in ids:
        u,L=flags[i]
        for x,k in (f[u],f[u][::-1]):
            for y,t in (g[L],g[L][::-1]):
                for p in S[k]:
                    for q in C[p]&S[x]:
                        for r in pencils[p]:
                            if y not in g[r]:
                                continue
                            phi_books+=1
                            if r in pencils[q]:
                                incident_books+=1
                                bad_by_original_flag[i]+=1
                                continue
                            if C[q]&onlines[r]!={p}:
                                raise AssertionError(
                                    "nonincident ORIGINAL GQ projection is not unique p")
                            z=next(v for v in f[q] if v!=x)
                            w=next(v for v in g[r] if v!=y)
                            physical_triple=((x,y),(k,t),(z,w))
                            if physical_triple in triples:
                                raise AssertionError(
                                    "two ORIGINAL source book witnesses map to one physical triple")
                            triples[physical_triple]=(i,p,q,r)
                            good_by_original_flag[i]+=1
    if phi_books!=len(triples)+incident_books:
        raise AssertionError("original source book incidence-defect partition broken")
    return {
        "s":s,"V":V,"a":a,"dual_original_line_side":dual,
        "core_original_flag_count":len(ids),
        "source_original_book_phi":phi_books,
        "incident_original_book_defect_psi":incident_books,
        "source_exact_blocked_triple_B":len(triples),
        "source_good_triples":triples,
        "good_books_per_core_original_ID":dict(good_by_original_flag),
        "incident_books_per_core_original_ID":dict(bad_by_original_flag),
        "identity_Phi_equals_B_plus_Psi":True,
        "anchor_source_flags_are_from_full_original_W3":True,
        "no_all_h_conclusion_inferred_from_finite_census":True,
    }


def independent_physical_first_blocked_triples(power,f,g,core_ids=None,*,dual=False):
    """Independent PHYSICAL-first full-core triple set, original GQ decoder.

    No source-book iteration, no K_pu, Phi, or formula Psi is used.
    The physical complete retained graph is built from true original
    incidence ID diagonals. Endpoints decode true original q,r.
    """
    (s,V,a,flags,f,g,ids,pencils,onlines,C)=_true_source_data(
        power,f,g,core_ids,dual)
    graph,owner=physical(ids,flags,f,g)
    finv={frozenset(z):i for i,z in enumerate(f)}
    ginv={frozenset(z):i for i,z in enumerate(g)}
    projection={}
    for q in range(V):
        for r in range(V):
            if r in pencils[q]:continue
            matches=C[q]&onlines[r]
            if len(matches)!=1:
                raise AssertionError("original GQ projection not unique")
            projection[q,r]=next(iter(matches))
    triples={}
    for v0,ns in graph.items():
        x,y=v0
        for v1 in ns:
            k,t=v1
            i=owner[tuple(sorted((v0,v1)))]
            for z in range(a):
                if z==x:continue
                q=finv.get(frozenset((x,z)))
                if q is None:continue
                for w in range(a):
                    if w==y:continue
                    r=ginv.get(frozenset((y,w)))
                    if r is None:continue
                    p=projection.get((q,r))
                    if p is None or k not in f[p]:continue
                    triple=(v0,v1,(z,w))
                    if triple in triples:
                        raise AssertionError("physical edge and endpoint provenance duplicated")
                    triples[triple]=(i,p,q,r)
    return {
        "s":s,"dual_original_line_side":dual,
        "core_original_flag_count":len(ids),
        "physical_exact_blocked_triple_B":len(triples),
        "physical_triples":triples,
        "source_projection_extracted_without_mixed_Phi":True,
    }


def independent_original_book_phi_tensor(power,f,g,core_ids=None,*,dual=False):
    """Third route: original R/R0 and Cstar tensor, *without* books or graph."""
    s,V,a,flags,f,g,ids,pencils,onlines,C=_true_source_data(
        power,f,g,core_ids,dual)
    I=set(ids)
    S=[set() for _ in range(a)]
    for p,pair in enumerate(f):
        for x in pair:S[x].add(p)
    R=[[0]*a for _ in range(V)]
    R0=[[0]*a for _ in range(V)]
    for i,(p,ell) in enumerate(flags):
        for y in g[ell]:
            R[p][y]+=1
            if i in I:R0[p][y]+=1
    Kpu=[[sum(R[p][y]*R0[u][y] for y in range(a))
          for u in range(V)] for p in range(V)]
    Phi=0
    for u,pair in enumerate(f):
        for x,k in (pair,pair[::-1]):
            for p in S[k]:
                Phi+=len(C[p]&S[x])*Kpu[p][u]
    return Phi
