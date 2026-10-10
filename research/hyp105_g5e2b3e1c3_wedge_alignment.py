"""HYP-105 B3.2-E1-C3: all-h GQ distinguished right-pair physical-alignment theorem.

For genuine W(3,s) original incidences and arbitrary injective correlated
physical pair labels f,g, nearly all left-B original six-incidence mass
has its UNIQUE doubled-original-point pair of right lines mapped to two
PHYSICALLY DISJOINT coordinate pairs. This is a source-target-interface
RESTRICTION, not a positive six-hyperedge overlap theorem.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import json

from hyp105_g5e2b3e1b1a_one_sided import gq_parameters
from hyp105_g5e2b3e1c0_weighted_overlap import (
    GQ_weighted_BA_right_sixset_spread,
    source_weighted_BA_hypergraph,
)
from hyp105_g5e2b3e1a_fixed_leading import (
    selected_left_six, validated_small_model,
)


def max_occupied_physical_adjacency(a, occupied_pairs):
    """Sharp edge-adjacency max among V-edge subgraphs of K_a.

    If t=C(a,2)-V missing edges and t<a, the maximum is attained
    by missing t edges of one star. Missing graph M has degrees r_x.
    Actual adjacent occupied pairs:
      C(a,2)*(a-2) - 2*t*(a-2) + sum_x C(r_x,2).
    Since two missing edges meet in at most one endpoint, the sum
    is at most C(t,2). A star attains equality for every t<=a-1.
    """
    if type(a) is not int or a<6 or type(occupied_pairs) is not int:
        raise ValueError("a and occupied_pairs must be legal integers")
    K=comb(a,2)
    if not 6<=occupied_pairs<=K:
        raise ValueError("occupied pair count out of range")
    t=K-occupied_pairs
    if t>=a:
        raise ValueError("sharp missing-star bound assumes t<a")
    all_adjacent=K*(a-2)
    cap=all_adjacent-2*t*(a-2)+comb(t,2)
    if not 0<=cap<=all_adjacent:
        raise AssertionError("invalid occupied physical line-graph cap")
    return {
        "a":a,"K":K,"occupied":occupied_pairs,"missing":t,
        "full_physical_adjacent_pair_count":all_adjacent,
        "max_occupied_physical_adjacent_pair_count":cap,
        "star_of_missing_physical_pairs_attains_cap":True,
    }


def actual_occupied_physical_adjacency(a, missing_physical_pairs):
    """Exact original coordinate incidence count, independent oracle."""
    if type(a) is not int or a<6:
        raise ValueError("invalid physical coordinate count")
    edges=set(combinations(range(a),2))
    missing=tuple(missing_physical_pairs)
    if len(missing)!=len(set(missing)) or any(e not in edges for e in missing):
        raise ValueError("missing physical labels must be distinct K_a pairs")
    occupied=edges.difference(missing)
    r=Counter(v for edge in missing for v in edge)
    count=sum(comb(a-1-r[x],2) for x in range(a))
    direct=sum(bool(set(e)&set(f)) for e,f in combinations(sorted(occupied),2))
    if count!=direct:
        raise AssertionError("occupied line-graph degree formula false")
    return count


def universal_wedge_alignment(s):
    """Uniform over ALL legal left/right GQ pair embeddings f,g, all h.

    A genuine B-left source sixset has ONE repeated ORIGINAL left point.
    Its two chosen ORIGINAL lines {u,v} concur there, uniquely by GQ.
    For each particular pair {u,v}, its number of possible source lifts
    is bounded by 3*C(a-2,4)*Delta**4: choose the four other physical
    coordinates; one of three physical 4-cycles; one original neighbor
    right line independently for each singleton original left point.
    Rejecting repeated original RIGHT lines can only reduce the count.

    Under right injection g, physically-adjacent images of concurrent
    original lines form a SUBSET of the physically adjacent occupied
    K_a pair labels. This latter count is at most its exact star-deletion
    extremal cap. Therefore the total source mass with physically
    adjacent distinguished right pair is bounded by cap_witness*cap_adj.
    """
    p=gq_parameters(s)
    spread=GQ_weighted_BA_right_sixset_spread(s)
    v,a,K,d=p["V"],p["a"],p["K"],p["Delta"]
    k=s*(s+1)
    E=v*k//2
    if v*k%2:
        raise AssertionError("invalid GQ line-concurrence graph")
    physical=max_occupied_physical_adjacency(a,v)
    original_concurrent_physical_adjacent_cap=min(
        E,physical["max_occupied_physical_adjacent_pair_count"])
    per_concurrent_pair_source_cap=3*comb(a-2,4)*d**4
    total_mass_lower=spread["source_BA_weighted_mass_lower"]
    adjacent_mass_cap=(original_concurrent_physical_adjacent_cap
                       *per_concurrent_pair_source_cap)
    nonadjacent_witness_mass_lower=max(0,total_mass_lower-adjacent_mass_cap)
    # A physical target sixset containing two physically disjoint
    # K_a edges has qD completions. This is only a TWO-LABEL target
    # completion with the other four original right source vertices
    # unconstrained. It is *NOT* a lower bound on U_B/A.
    disjoint_pair_target_codegree=14*comb(a-4,2)
    return {
        "s":s,"V":v,"a":a,"K":K,"Delta":d,
        "original_concurrent_pair_count":E,
        "missing_physical_pair_labels":K-v,
        "occupied_physical_adjacency_upper":
            physical["max_occupied_physical_adjacent_pair_count"],
        "concurrent_pairs_mapped_physically_adjacent_upper":
            original_concurrent_physical_adjacent_cap,
        "source_mass_lower":total_mass_lower,
        "source_witness_multiplicity_each_pair_upper":
            per_concurrent_pair_source_cap,
        "physically_adjacent_distinguished_pair_source_mass_upper":
            adjacent_mass_cap,
        "physically_disjoint_distinguished_pair_source_mass_lower":
            nonadjacent_witness_mass_lower,
        "source_mass_disjoint_fraction_lower":
            (Fraction(nonadjacent_witness_mass_lower,total_mass_lower)
             if total_mass_lower else Fraction(0)),
        "all_K_a_target_completions_of_a_disjoint_pair":
            disjoint_pair_target_codegree,
        "partial_target_pair_completion_lower":
            disjoint_pair_target_codegree*nonadjacent_witness_mass_lower,
        "exact_asymptotic_source_disjoint_witness_mass":
            "(1/4-O(s**(-1/2)))*s**15",
        "positive_all_correlated_sixset_overlap_proved":False,
        "all_seven_motifs_omega_s6_proved":False,
    }


def original_W32_distinguished_right_pair_source(model):
    """Actual original-incidence, not a graph of physical coordinates.

    Enumerate each accepted B-left original six-incidence set ONCE.
    Keep six distinct ORIGINAL right line factors and recover its
    unique repeated ORIGINAL point and its two chosen original lines.
    This oracle is distinct from a physical right target scan.
    """
    _,_,original,_=validated_small_model(model)
    weights=Counter()
    right_sixset_mass=Counter()
    seen=0
    for ids,kind in selected_left_six(model):
        if kind!="B":
            continue
        seen+=1
        pts=Counter(original[i][0] for i in ids)
        doubled=[p for p,m in pts.items() if m==2]
        if len(doubled)!=1 or sorted(pts.values())!=[1,1,1,1,2]:
            raise AssertionError("B-original-factor profile lost")
        right=tuple(original[i][1] for i in ids)
        if len(set(right))!=6:
            continue
        pair=frozenset(original[i][1] for i in ids
                       if original[i][0]==doubled[0])
        if len(pair)!=2:
            raise AssertionError("two different original concurrent right lines required")
        weights[pair]+=1
        right_sixset_mass[frozenset(right)]+=1
    if seen!=10935 or sum(weights.values())!=5000:
        raise AssertionError("W32 B original mass changed")
    return weights,right_sixset_mass


def finite_W32_distinguished_pair_report(model, *, right_labels=None):
    weights,source=original_W32_distinguished_right_pair_source(model)
    if source!=source_weighted_BA_hypergraph(model):
        raise AssertionError("weighted source and unique witness census differ")
    labels=tuple(right_labels if right_labels is not None
                 else model["right_labels"])
    allowed=set(combinations(range(6),2))
    if len(labels)!=15 or len(set(labels))!=15 or set(labels)!=allowed:
        raise ValueError("W32 right-label map must be K6 bijection")
    adjacent=0
    disjoint=0
    for pair,w in weights.items():
        i,j=sorted(pair)
        if set(labels[i]) & set(labels[j]):
            adjacent+=w
        else:
            disjoint+=w
    if adjacent+disjoint!=5000:
        raise AssertionError("distinguished source mass not conserved")
    cert=universal_wedge_alignment(2)
    if adjacent>cert["physically_adjacent_distinguished_pair_source_mass_upper"]:
        raise AssertionError("universal witness alignment cap falsified")
    return {
        "scheme":model.get("scheme","W32"),
        "original_source_mass":adjacent+disjoint,
        "distinct_original_concurrent_witness_pairs":len(weights),
        "physically_adjacent_witness_mass":adjacent,
        "physically_disjoint_witness_mass":disjoint,
        "two_label_target_completion_count":
            adjacent*7+disjoint*14,
        "actual_complete_BA_six_target_lower_claim":False,
    }


def report():
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    data={}
    for s in (2,4,8,16,32,64,128,256):
        d=universal_wedge_alignment(s)
        data[str(s)]={k:str(v) if isinstance(v,Fraction) else v
                      for k,v in d.items()}
    for label in ("lex","reverse-line"):
        data["W32_"+label]=finite_W32_distinguished_pair_report(
            pair_labeled_symplectic(1,label))
    return data


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True,default=str))
