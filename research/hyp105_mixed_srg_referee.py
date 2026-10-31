"""AA4-MIXSRG: independent exact original W(3,s) blocker-energy referee.

New ALL-h analytic identity (valid for EVERY legal complete globally injected
point map f, with true source W(3,s) and its self-dual original lines):
  C_P**2 = (s*s-1)*I - 2*C_P + (s+1)*J,
  sum_x || C_P 1_{S_x} ||²
    = 2*(s*s-1)*V + (s+1)*sum_x |S_x|²
      - 4*sum_x #{unordered collinear source-point pairs in S_x}.
where S_x={p:x in f(p)}. It gives a more precise nonnegative
subtractive correction to the first mixed blocker Cauchy factor
than the #672 spectral norm bound (14). It does not by itself change
the asymptotic exponent or settle root Branch A independently.

Finite W32/W34 checks on actual original incidence flags compute both
duals, FULL R and CORE R0, source collinearity, the exact mixed K_pu,
a direct blocked-triple enumeration, and actual 2walk completions,
without invoking #672's precomputed finite_source_certificate.
No synthetic incidence hosts or probabilistic map completions.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_full_physical_degree_tail import genuine_source, physical, conflict_graph
from hyp105_physical_degree_energy import minimal_alphabet, _verify_typed_injections


def exact_allh_first_mixed_factor_envelopes(s):
    """Strictly sharper uniform ALL-h first mixed-factor bound than #672.

    Proof for every s>=2 (indeed all integers): the trial alphabet
    t=s²+2 has choose(t,2)-V=(s²+1)*s*(s-2)/2>=0.
    Therefore minimal a<=s²+2 and d*(a-1)<=d*(s²+1)=V.

    Old #672: A_f<=4*d²*(V+s²*(a-1)).
    New SRG: A_f<=4*V*(s²-1+d*(a-1))-8*E_f.
    Difference old-minus-new-uniform:
      4*d*(2*V-d*(a-1)) >=4*d*V>0.
    This uniformly improves the exact finite bound for EVERY embedding;
    exponent of the asymptotic blocking error is not changed.
    """
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("s must be dyadic >=2")
    V=(s+1)*(s*s+1)
    d=s+1
    a=minimal_alphabet(V)
    if a>s*s+2:
        raise AssertionError("minimal K_a all-h algebraic trial violated")
    old=4*d*d*(V+s*s*(a-1))
    new=4*V*(s*s-1+d*(a-1))
    gap=4*d*(2*V-d*(a-1))
    if old-new!=gap or gap<4*d*V:
        raise AssertionError("exact all-h SRG universal strict improvement failed")
    return {
        "s":s,"V":V,"a":a,
        "older_672_first_square_uniform":old,
        "new_allh_SRG_first_square_uniform":new,
        "strict_improvement_integer":gap,
        "minimum_proven_strict_improvement":4*d*V,
        "allh_algebraic_proof_not_extrapolation":True,
    }


def exact_source_star_collinearity_energy(s, source_flags, source_pair_labels):
    """Independent finite source oracle for the ALL-h exact SRG identity.

    Supports any s from a true regular W(3,s) incidence host. This
    routine checks every strongly-regular common-neighbor count,
    rather than trusting the W32/W34 instance's source provenance.
    No graph-adjacency matrix multiplication is needed.
    """
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("dyadic s>=2 required")
    V=(s+1)*(s*s+1)
    d=s+1
    if len(source_pair_labels)!=V or len(set(map(tuple,source_pair_labels)))!=V:
        raise ValueError("complete globally injected source pair map required")
    a=minimal_alphabet(V)
    if any(len(z)!=2 or not 0<=z[0]<z[1]<a for z in source_pair_labels):
        raise ValueError("invalid original source pair coordinates")
    pencils=[set() for _ in range(V)]
    lines=[set() for _ in range(V)]
    for p,ell in source_flags:
        pencils[p].add(ell)
        lines[ell].add(p)
    if len(source_flags)!=V*d or any(len(z)!=d for z in pencils+lines):
        raise ValueError("not a (s+1)-regular true original source incidence")
    C=[set().union(*(lines[ell] for ell in pencils[p]))-{p}
       for p in range(V)]
    if any(len(z)!=s*d for z in C):
        raise AssertionError("original W3 point-collinearity degree broken")
    # Explicitly independent rowwise C² strongly-regular identity:
    # any collinear distinct p,q have s-1 common neighbors,
    # any noncollinear distinct p,q have s+1.
    if any(len(C[p]&C[q])!=(s-1 if q in C[p] else s+1)
           for p in range(V) for q in range(p+1,V)):
        raise AssertionError("W3 original strongly regular common-neighbor law false")
    if any(len(C[p])!=s*d for p in range(V)):
        raise AssertionError("C_P diagonal square entry wrong")
    S=[set() for _ in range(a)]
    for p,(x,y) in enumerate(source_pair_labels):
        S[x].add(p);S[y].add(p)
    square_by_C=sum(sum(len(C[p]&S[x])**2 for p in range(V))
                    for x in range(a))
    adjacent_in_stars=sum(
        sum(q in C[p] for p,q in combinations(sorted(points),2))
        for points in S)
    sizes=sum(len(points)**2 for points in S)
    closed=2*(s*s-1)*V+d*sizes-4*adjacent_in_stars
    if square_by_C!=closed:
        raise AssertionError("exact W3 SRG identity/source physical star collision incorrect")
    if sum(map(len,S))!=2*V or any(len(points)>a-1 for points in S):
        raise AssertionError("global source point injection star bound broken")
    envelopes=exact_allh_first_mixed_factor_envelopes(s)
    if 2*square_by_C>envelopes["new_allh_SRG_first_square_uniform"]:
        raise AssertionError("exact source SRG squared energy exceeds improved uniform bound")
    return {
        "s":s,"V":V,"a":a,
        "original_source_neighbors":tuple(map(frozenset,C)),
        "original_coordinate_stars":tuple(map(frozenset,S)),
        "coordinate_star_square_sum":sizes,
        "original_collinear_source_pair_collisions_in_coordinate_stars":
            adjacent_in_stars,
        "exact_source_star_srg_energy":square_by_C,
        "exact_source_star_srg_closed_form":closed,
        "allh_uniform_strict_improvement_over_672":envelopes["strict_improvement_integer"],
        "all_h_identity_abstract_proved_not_by_extrapolation":True,
    }


def exact_mixed_blocker_referee(power, f, g, core_ids=None, *, dual=False):
    """Full independent finite exact mixed blocker vs actual blocked triples.

    In dual mode swap ORIGINAL point/line incidence types AND physical
    first/second coordinate types, retaining the SAME original flags.
    Each physical edge still has its ORIGINAL incidence owner.
    """
    if type(power) is not int or power not in (1,2):
        raise ValueError("genuine source finite oracle supports h=1,2 only")
    s,V,source=genuine_source(power)
    a=minimal_alphabet(V)
    f=tuple(map(tuple,f));g=tuple(map(tuple,g))
    _verify_typed_injections(a,V,f,g)
    flags=tuple((ell,p) for p,ell in source) if dual else source
    if dual:f,g=g,f
    ids=tuple(range(len(flags))) if core_ids is None else tuple(core_ids)
    if (len(set(ids))!=len(ids) or
            any(type(i) is not int or not 0<=i<len(flags) for i in ids)):
        raise ValueError("distinct legal genuine ORIGINAL core flag IDs required")
    ids=tuple(sorted(ids))
    graph,prov=physical(ids,flags,f,g)
    degrees={v:len(ns) for v,ns in graph.items()}
    Delta=max(degrees.values(),default=0)
    conflict,mf,mg=conflict_graph(ids,flags,f,g)
    K=max((len(x) for x in conflict.values()),default=0)
    star=exact_source_star_collinearity_energy(s,flags,f)
    S=star["original_coordinate_stars"]
    C=star["original_source_neighbors"]
    Cstars=[[len(C[p]&S[x]) for p in range(V)] for x in range(a)]
    R=[[0]*a for _ in range(V)]
    R0=[[0]*a for _ in range(V)]
    for i,(p,ell) in enumerate(flags):
        for y in g[ell]:
            R[p][y]+=1
            if i in ids:R0[p][y]+=1
    # No delegation to older finite_source_certificate or its fixture.
    Kpu=[[sum(R[p][y]*R0[u][y] for y in range(a)) for u in range(V)]
         for p in range(V)]
    F1=F2=Phi=Ksum=0
    for u,(x,k) in enumerate(f):
        for x,k in ((x,k),(k,x)):
            for p in S[k]:
                A=Cstars[x][p]
                B=Kpu[p][u]
                F1+=A*A
                F2+=B*B
                Phi+=A*B
                Ksum+=B
    if Phi*Phi>F1*F2:
        raise AssertionError("mixed Cauchy squared bound failed")
    if F1>2*star["exact_source_star_srg_energy"]:
        raise AssertionError("mixed first square exceeds EXACT SRG energy")
    full_graph,_=physical(range(len(flags)),flags,f,g)
    degree_product=sum(len(full_graph.get(v,()))*len(graph.get(v,()))
                       for v in set(full_graph)|set(graph))
    if Ksum!=degree_product:
        raise AssertionError("full/core exact mixed physical degree contraction false")
    Kmax=2*(s+1)*(K+1)
    if max((max(row) for row in Kpu),default=0)>Kmax:
        raise AssertionError("true source/core pencil conflict cap false")
    if F2>Kmax*Ksum or Ksum>4*len(flags)*Delta:
        raise AssertionError("mixed second square source/core degree inequality false")
    # Genuine ORIGINAL projection (q,r): unique q--ell--p--r.
    pencils=[set() for _ in range(V)]
    through=[set() for _ in range(V)]
    for p,ell in flags:
        pencils[p].add(ell);through[ell].add(p)
    collinear=C
    projections={}
    for q in range(V):
        for r in range(V):
            if r in pencils[q]:continue
            candidate=collinear[q]&through[r]
            if len(candidate)!=1:
                raise AssertionError("original GQ unique nonincident endpoint projection false")
            projections[q,r]=next(iter(candidate))
    finv={frozenset(edge):p for p,edge in enumerate(f)}
    ginv={frozenset(edge):ell for ell,edge in enumerate(g)}
    triples=set()
    # Independent explicit physical oriented first-core-edge enumeration
    # and every possible physical endpoint label. We do NOT use Phi to
    # generate candidate triples.
    for v0,ns in graph.items():
        x,y=v0
        for v1 in ns:
            k=v1[0]
            for z in range(a):
                q=finv.get(frozenset((x,z)))
                if q is None:continue
                for w in range(a):
                    r=ginv.get(frozenset((y,w)))
                    if r is None:continue
                    p=projections.get((q,r))
                    if p is not None and k in f[p]:
                        triples.add((v0,v1,(z,w)))
    if len(triples)>Phi:
        raise AssertionError("actual blocked triple not covered by mixed source contraction")
    # Independent adjacency expansion A0² and physical weighted blocker
    # completion (v0,v1,v2,v3) for all triples.
    A2={}
    for v,ns in graph.items():
        row=Counter()
        for u in ns:
            row.update(graph[u])
        A2[v]=row
    trace4=sum(c*c for row in A2.values() for c in row.values())
    weighted_completions=sum(A2.get(v1,{}).get(v3,0)
                              for v0,v1,v3 in triples)
    if weighted_completions**2>len(triples)*Delta*trace4:
        raise AssertionError("blocked triple completion Cauchy fourth-moment transfer false")
    if weighted_completions**2>Phi*Delta*trace4:
        raise AssertionError("source mixed triple bound to fourth-moment transfer false")
    return {
        "s":s,"V":V,"a":a,"dual_original_line_side":dual,
        "original_core_flags":len(ids),
        "original_core_conflict_cap":K,
        "max_physical_core_degree":Delta,
        "srg_coordinate_star_energy":star["exact_source_star_srg_energy"],
        "srg_collinear_coordinate_star_pair_subtraction":
            4*star["original_collinear_source_pair_collisions_in_coordinate_stars"],
        "mixed_first_square_exact":F1,
        "mixed_second_square_exact":F2,
        "mixed_phi_exact":Phi,
        "mixed_sumK_equals_full_core_degree_product":Ksum,
        "source_pointwise_K_cap":Kmax,
        "independent_original_projection_blocked_triples":len(triples),
        "blocked_first_internal_coordinate_weighted_2walk_completions":
            weighted_completions,
        "physical_core_trace4":trace4,
        "all_checks_passed":True,
        "no_all_h_computational_proof":True,
    }
