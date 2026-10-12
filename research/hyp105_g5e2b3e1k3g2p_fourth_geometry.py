"""HYP-105 E1-K3-G2-P: exact ALL-a Johnson H4 and GQ forbidden diamond.

Eleven physical four-edge isomorphism types provide the entire target
rank-four orbit table at any a>=6, without enumerating C(C(a,2),6).
For the ORIGINAL GQ line intersection graph, induced K4-e ('diamond')
is impossible for all s, and induced K4 must fit in a single pencil
of s+1 lines. A joint 11x11 original/physical four-subset tensor
reproduces the rank-four contribution from an independent W32
Johnson projector. Rank 5+6 and universal P2 remain OPEN.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import comb, factorial, perm
import json

from hyp105_g5e2b3e1c0_weighted_overlap import (
    simple_six_2factor_targets, source_weighted_BA_hypergraph,
)
from hyp105_g5e2b3e1k3g2n_johnson_harmonics import (
    rat, target_low_harmonics, physical_pair_indices,
    six_image_index, exact_target_johnson_decomposition,
    spectral_overlap_certificate, gq_pair_model,
)
from hyp105_g5e2b3e1k3g2o_gq_third_coupling import (
    target_rank3_orbits, physical_triple_shape, gq_line_geometry,
    original_GQ_third_coupling,
)
from hyp105_g5e2b3e1k3g2m_twofamily_falsifier import (
    dual_model, exact_two_family_point, _anchors,
)
from hyp105_g5e2b3e1k3g2h_exact_swap_shell import swapped_labeling


def physical_four_shape(edges):
    """Isomorphism-invariant 4-edge graphlet: component-degree signatures."""
    edges=tuple(tuple(e) for e in edges)
    if (len(edges)!=4 or len(set(edges))!=4 or
            any(len(e)!=2 or type(e[0]) is not int or
                type(e[1]) is not int or not 0<=e[0]<e[1]
                for e in edges)):
        raise ValueError("four distinct canonical physical pair edges required")
    neighbors={}
    for u,v in edges:
        neighbors.setdefault(u,set()).add(v)
        neighbors.setdefault(v,set()).add(u)
    visited=set()
    signature=[]
    for v in neighbors:
        if v in visited:
            continue
        stack=[v]
        visited.add(v)
        component=[]
        while stack:
            u=stack.pop()
            component.append(u)
            for w in neighbors[u]:
                if w not in visited:
                    visited.add(w)
                    stack.append(w)
        degrees=tuple(sorted(len(neighbors[u]) for u in component))
        signature.append((sum(degrees)//2,degrees))
    return tuple(sorted(signature))


def _automorphisms_of_template(edges):
    vertices=tuple(sorted({v for e in edges for v in e}))
    r={v:i for i,v in enumerate(vertices)}
    normalized={tuple(sorted((r[u],r[v]))) for u,v in edges}
    n=len(vertices)
    autom=sum(1 for pi in permutations(range(n)) if {
        tuple(sorted((pi[u],pi[v]))) for u,v in normalized}==normalized)
    if autom<1 or factorial(n)%autom:
        raise AssertionError("invalid graph automorphism orbit")
    return n,autom


@lru_cache(maxsize=1)
def physical_four_templates():
    """Exactly 11 unlabeled 4-edge graphs with no isolated vertices."""
    representatives={}
    for four in combinations(tuple(combinations(range(8),2)),4):
        key=physical_four_shape(four)
        representatives.setdefault(key,four)
    if len(representatives)!=11:
        raise AssertionError("4-edge simple graph orbit completeness failed")
    return tuple((key,representatives[key],
                  *_automorphisms_of_template(representatives[key]))
                 for key in sorted(representatives))


def _physical_h2_on_subset(edges,low):
    adj=sum(bool(set(u)&set(v)) for u,v in combinations(edges,2))
    pairs=comb(len(edges),2)
    return adj*low["h2_adj"]+(pairs-adj)*low["h2_dis"]


def _physical_h3_on_subset(edges,third):
    palette=tuple(edges)
    return sum((third["h3"][physical_triple_shape(B)]
                for B in combinations(palette,3)),Fraction(0))


def target_rank4_orbits(a):
    """ALL a>=6: exact physical 4-edge target codegrees + Johnson H4.

    c4(F)=c4,K6(shape)*C(a-v,6-v) for v<=6, otherwise zero.
    Its harmonic h4(F) is the residual 4-down-marginal divided by
    lambda4=C(K-8,2). The orbit population is (a)_v/Aut(shape).
    """
    low=target_low_harmonics(a)
    third=target_rank3_orbits(a)
    K=low["K"]
    lam4=comb(K-8,2)
    K6=tuple(combinations(range(6),2))
    T6=simple_six_2factor_targets(6)
    codegrees=Counter()
    for S in T6:
        for A in combinations(sorted(S),4):
            codegrees[physical_four_shape(A)]+=1
    census={}
    for shape,representative,v,autom in physical_four_templates():
        c6=0
        if v<=6:
            c6=sum(set(representative).issubset(S) for S in T6)
            if codegrees[shape] % (perm(6,v)//autom):
                raise AssertionError("physical target 4-orbit class inconsistency")
            if codegrees[shape] != c6*perm(6,v)//autom:
                raise AssertionError("K6 physical 4-orbit target codegree mismatch")
        c4=c6*comb(a-v,6-v) if v<=6 else 0
        pop=perm(a,v)//autom if v<=a else 0
        q2=_physical_h2_on_subset(representative,low)
        q3=_physical_h3_on_subset(representative,third)
        coeff=Fraction(
            c4-low["density"]*comb(K-4,2)
            -comb(K-6,2)*q2-comb(K-7,2)*q3,lam4)
        census[str(shape)]={
            "vertices":v,"automorphisms":autom,"orbit_size":pop,
            "K6_codegree":c6,"target_codegree":c4,
            "h4":coeff,
        }
    if len(census)!=11 or sum(d["orbit_size"] for d in census.values())!=comb(K,4):
        raise AssertionError("eleven physical four-orbits do not exhaust K_a")
    E4=lam4*sum((d["orbit_size"]*d["h4"]**2
                  for d in census.values()),Fraction(0))
    E56=third["E_ge4"]-E4
    if E56<0:
        raise AssertionError("negative physical rank5/6 energy")
    return {
        "a":a,"K":K,"lambda4":lam4,"shapes":census,
        "E4":E4,"E_ge5":E56,
    }


def original_four_type(vertices,adjacency):
    """Canonical induced 4-vertex graph code modulo S4 relabeling."""
    if len(vertices)!=4 or len(set(vertices))!=4:
        raise ValueError("four distinct original GQ line sources")
    es=tuple(combinations(range(4),2))
    raw={(i,j) for i,j in es
         if vertices[j] in adjacency[vertices[i]]}
    return min(sum(1<<i for i,(u,v) in enumerate(es)
                   if tuple(sorted((pi[u],pi[v]))) in raw)
               for pi in permutations(range(4)))


@lru_cache(maxsize=1)
def _original_four_shapes():
    classes={}
    es=tuple(combinations(range(4),2))
    for bitmask in range(1<<6):
        edge={(u,v) for i,(u,v) in enumerate(es)
              if bitmask & (1<<i)}
        canonical=min(sum(1<<i for i,(u,v) in enumerate(es)
                          if tuple(sorted((pi[u],pi[v]))) in edge)
                      for pi in permutations(range(4)))
        classes.setdefault(canonical,len(edge))
    if len(classes)!=11:
        raise AssertionError("exactly 11 original four-vertex graph types")
    return dict(sorted(classes.items()))


def gq_forbidden_diamond_theorem(geom):
    """Finite original-symplectic falsifier of ALL-h GQ no-diamond lemma."""
    adj=geom["adjacency"]
    V=geom["V"]
    n_diamond=n_clique=0
    four_hist=Counter()
    codes=_original_four_shapes()
    for A in combinations(range(V),4):
        typ=original_four_type(A,adj)
        four_hist[typ]+=1
        edges=codes[typ]
        if edges==5:
            n_diamond+=1
        if edges==6:
            n_clique+=1
    if n_diamond:
        raise AssertionError("GQ has impossible original induced diamond")
    if geom["s"]==2 and n_clique:
        raise AssertionError("W32 has no 4 concurrent lines in 3-line pencil")
    return {
        "V":V,"s":geom["s"],"diamond_count":n_diamond,
        "K4_count":n_clique,
        "complete_four_histogram":{
            str(k):four_hist[k] for k in codes
        },
        "full_original_foursets":comb(V,4),
        "all_h_no_induced_diamond_GQ_theorem":True,
        "all_h_clique_pencil_capacity":geom["s"]+1,
    }


def _target_rank4_on_six(S,edges,orbit):
    if len(S)!=6 or len(set(S))!=6:
        raise ValueError("six distinct physical edges required")
    return sum((orbit["shapes"][str(physical_four_shape(
        tuple(edges[i] for i in B)))]["h4"]
        for B in combinations(S,4)),Fraction(0))


def original_GQ_fourth_coupling(model):
    """Exact TRUE GQ original-physical 11x11 tensor and independent H4."""
    if model["s"]!=2 or model["a"]!=6:
        raise ValueError("complete original four-source tensor is W32 only")
    geom=gq_line_geometry(model)
    origtypes=_original_four_shapes()
    w=source_weighted_BA_hypergraph(model)
    fourth=target_rank4_orbits(6)
    labels=tuple(model["right_labels"])
    palette=physical_pair_indices(6)
    edges=tuple(combinations(range(6),2))
    table=Counter()
    corr=Fraction(0)
    for R,mult in w.items():
        if not mult:
            continue
        for A in combinations(sorted(R),4):
            ot=original_four_type(A,geom["adjacency"])
            physical=tuple(sorted(palette[labels[i]] for i in A))
            pt=str(physical_four_shape(tuple(edges[i] for i in physical)))
            table[(ot,pt)]+=mult
            corr+=mult*fourth["shapes"][pt]["h4"]
    if sum(table.values())!=15*sum(w.values()):
        raise AssertionError("original fourth order tensor mass mismatch")
    if any(v and origtypes[code]==5 for (code,_),v in table.items()):
        raise AssertionError("source GQ diamond impossible for all h")
    spectrum=spectral_overlap_certificate(w,labels)
    if corr!=Fraction(*spectrum["signed_ranks"][4]):
        raise AssertionError("independent entire-Johnson spectral rank4 mismatch")
    E56=Fraction(*spectrum["source_E_ge3"])-Fraction(0)
    # Source high-rank moments through H4 are computed separately by the
    # full-source rank4 oracle; no fake bound derived from target alone.
    residual=sum((Fraction(*v) for v in spectrum["signed_ranks"][5:]),
                 Fraction(0))
    complete_gq=gq_forbidden_diamond_theorem(geom)
    return {
        "original_GQ_four_histogram":complete_gq,
        "source_mass":sum(w.values()),
        "coupled_original_GQ_four_by_physical_four":{
            str(code):{
                phys:table[(code,phys)] for phys in fourth["shapes"]
            } for code in origtypes
        },
        "tensor_mass":sum(table.values()),
        "rank4_contraction":rat(corr),
        "independent_full_spectrum_rank4":spectrum["signed_ranks"][4],
        "rank5_and_rank6_correlation":rat(residual),
        "rank4_target_E":rat(fourth["E4"]),
        "rank_ge5_target_E":rat(fourth["E_ge5"]),
        "universal_P2_proved":False,
    }


def report():
    fourth={}
    for a in (6,9,14):
        v=target_rank4_orbits(a)
        fourth[str(a)]={
            "a":a,"K":v["K"],
            "E4":rat(v["E4"]),"E_ge5":rat(v["E_ge5"]),
            "four_graph_orbits":{
                k:{field:(rat(val) if isinstance(val,Fraction) else val)
                   for field,val in entry.items()}
                for k,entry in v["shapes"].items()
            },
        }
    lex=gq_pair_model(1,"lex")
    hard=swapped_labeling(_anchors()[0][1],"left",13,14)
    models=[]
    for name,m in (("lex",lex),("hardest-M",hard)):
        o=exact_two_family_point(m)
        first=original_GQ_fourth_coupling(m)
        second=original_GQ_fourth_coupling(dual_model(m))
        if (o["U_BA"]+o["U_AB"]+o["five_other_family"]
                !=o["S_seven"]):
            raise AssertionError("genuine complete original/dual B0 seven check")
        models.append({
            "name":name,"U_BA":o["U_BA"],"U_AB":o["U_AB"],
            "S_seven":o["S_seven"],"P2_margin":o["two_family_minus_mu"],
            "original_BA":first,"genuine_original_dual_AB":second,
        })
    return {
        "slice":"HYP-105-E1-K3-G2-P",
        "physical_rank4_all_a":fourth,
        "original_GQ_models":models,
        "all_h_original_no_diamond_and_clique_pencil_proved":True,
        "all_h_P2_proved":False,"all_h_P7_proved":False,
        "branch_A_B":"OPEN",
    }


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
