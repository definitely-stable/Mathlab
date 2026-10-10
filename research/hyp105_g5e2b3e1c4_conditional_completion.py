"""HYP-105 B3.2-E1-C4 — conditional original-four-line completion.

Exact ALL-h model-equivalent formula for each legal f,g; finite W(3,2)
independent incidence oracle; pair-frozen random-bijection first/second
moments; exact conditional L2 sufficient certificate. No all-g bound.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import json

from hyp105_g5e2b3e1a_fixed_leading import (
    _two_factors_K6, selected_left_six, validated_small_model,
)
from hyp105_g5e2b3e1c0_weighted_overlap import (
    physical_target_two_point_design, source_weighted_BA_hypergraph,
)


def _choose(n,r):
    return comb(n,r) if 0 <= r <= n else 0


def _physical_pair(x,a):
    if (not isinstance(x,tuple) or len(x)!=2 or
        any(type(y) is not int or not 0<=y<a for y in x) or
        x[0]>=x[1]):
        raise ValueError("pair labels must be sorted, distinct physical coordinates")
    return x


def occupied_target_residuals(a, occupied_labels, distinguished_pair):
    """Exact four-label completions in ACTUALLY OCCUPIED physical labels.

    Implements 70 simple degree-two templates on each six-physical-vertex
    superset of the two fixed edge labels. No T_a materialization.
    This executable oracle is finite; theorem itself has no a upper limit.
    """
    if type(a) is not int or a<6 or a>40:
        raise ValueError("finite residual oracle requires 6<=a<=40")
    occupied=tuple(_physical_pair(x,a) for x in occupied_labels)
    if len(set(occupied)) != len(occupied) or len(occupied)<6:
        raise ValueError("occupied physical labels must be injective and >=6")
    anchor=tuple(_physical_pair(x,a) for x in distinguished_pair)
    if len(anchor)!=2 or len(set(anchor))!=2 or any(x not in occupied for x in anchor):
        raise ValueError("two distinct occupied distinguished physical pair labels required")
    anchor_set=frozenset(anchor)
    vertices=set(v for e in anchor for v in e)
    available=tuple(v for v in range(a) if v not in vertices)
    if len(vertices)>6:
        raise AssertionError("anchor has >4 physical vertices")
    completions=set()
    for other in combinations(available,6-len(vertices)):
        six=tuple(sorted(vertices.union(other)))
        for template in _two_factors_K6():
            target=frozenset(tuple(sorted((six[u],six[v])))
                             for u,v in template)
            if anchor_set <= target and target <= set(occupied):
                rest=target-anchor_set
                if len(rest)!=4:
                    raise AssertionError("not a four-physical-label completion")
                completions.add(rest)
    expected=physical_target_two_point_design(a)
    full_codegree=(expected["pair_codegree_adjacent_physical_labels"]
                   if set(anchor[0])&set(anchor[1]) else
                   expected["pair_codegree_disjoint_physical_labels"])
    if len(completions)>full_codegree:
        raise AssertionError("occupied 2factor count exceeds all-K_a codegree")
    return frozenset(completions),full_codegree



def occupied_disjoint_triangle_completion_lower(a,occupied_labels,anchor_pair):
    """Constructive, exact physically occupied two-triangle 2-factor family.

    For two PHYSICALLY DISJOINT occupied edges ab,cd let X consist of
    physical x outside {a,b,c,d} with ax,bx occupied, and Y consist of
    y with cy,dy occupied. Every x∈X,y∈Y,x!=y gives the distinct
    2factor triangles abx and cdy. This counts a true subfamily of
    q_F, not arbitrary four-original-line compatibility.
    """
    if type(a) is not int or a<6:
        raise ValueError("physical alphabet must be >=6")
    F=frozenset(_physical_pair(e,a) for e in occupied_labels)
    if len(F)!=len(tuple(occupied_labels)) or len(F)<6:
        raise ValueError("physical occupied labels must be injective")
    pair=tuple(_physical_pair(e,a) for e in anchor_pair)
    if len(pair)!=2 or len(set(pair))!=2 or any(e not in F for e in pair):
        raise ValueError("anchor must be two distinct occupied labels")
    if set(pair[0])&set(pair[1]):
        raise ValueError("triangle subfamily bound requires disjoint anchor edges")
    (p,q),(r,s)=pair
    used=set((p,q,r,s))
    outside=set(range(a))-used
    edge=lambda x,y:tuple(sorted((x,y)))
    X={x for x in outside if edge(p,x) in F and edge(q,x) in F}
    Y={y for y in outside if edge(r,y) in F and edge(s,y) in F}
    count=len(X)*len(Y)-len(X&Y)
    if count<0:
        raise AssertionError("negative available two-triangle completions")
    t=comb(a,2)-len(F)
    L=max(0,a-4-t)
    universal=max(0,L*(L-1))
    if count<universal:
        raise AssertionError("universal occupied two-triangle lower falsified")
    return {
        "a":a,"occupied_labels":len(F),"missing_labels":t,
        "first_triangle_extra_vertices":len(X),
        "second_triangle_extra_vertices":len(Y),
        "two_triangle_occupied_completion_count":count,
        "uniform_missing_budget_lower":universal,
        "not_actual_GQ_four_line_completion":True,
    }


def all_h_pairwise_random_benchmark_lower(s):
    """Asymmetric C3 anchored mass × occupied physical triangles / C(V-2,4).

    A sum of DIFFERENT per-P frozen-pair random-bijection means.
    It is NOT the expectation under ONE shared uniform right labeling,
    NOT a bound for fixed adversarial g, and NOT R3.
    If along a sequence t<= (1-eta)*a for fixed eta>0, this lower
    is Omega_eta(s^6), by the separately proved C3 mass estimate.
    """
    from hyp105_g5e2b3e1c3_wedge_alignment import universal_wedge_alignment
    p=universal_wedge_alignment(s)
    a,V,t=p["a"],p["V"],p["missing_physical_pair_labels"]
    L=max(0,a-4-t)
    per_disjoint=max(0,L*(L-1))
    conditional_N=comb(V-2,4)
    mdis=p["physically_disjoint_distinguished_pair_source_mass_lower"]
    bound=Fraction(mdis*per_disjoint,conditional_N)
    return {
        "s":s,"a":a,"V":V,"physical_missing_t":t,
        "all_disjoint_anchors_occupied_completion_lower":per_disjoint,
        "all_correlated_disjoint_original_witness_mass_lower":mdis,
        "pairwise_frozen_bijection_benchmark_lower":bound,
        "bound_is_global_deterministic_BA_overlap":False,
        "asymptotic_if_t_le_(1-eta)a":
            "Omega_eta(s^6) for every fixed eta>0, only for benchmark",
    }


def original_W32_conditional_source(model):
    """Unique original doubled-point P and four OTHER original right lines.

    Uses original incidence IDs, never physical target co-degrees.
    Grouped tensor b_f(P,H), not only aggregate m_f(R).
    """
    _,_,edges,_=validated_small_model(model)
    tensor={}
    candidates=0
    total=0
    for ids,kind in selected_left_six(model):
        if kind!="B":
            continue
        candidates+=1
        points=Counter(edges[i][0] for i in ids)
        doubled=[p for p,m in points.items() if m==2]
        if len(doubled)!=1 or tuple(sorted(points.values()))!=(1,1,1,1,2):
            raise AssertionError("wrong original B-left profile")
        right=[edges[i][1] for i in ids]
        if len(set(right))!=6:
            continue
        pair=frozenset(edges[i][1] for i in ids if edges[i][0]==doubled[0])
        other=frozenset(right)-pair
        if len(pair)!=2 or len(other)!=4:
            raise AssertionError("nonunique original GQ doubled pair")
        tensor.setdefault(pair,Counter())[other]+=1
        total+=1
    if candidates!=10935 or total!=5000:
        raise AssertionError("actual W32 original B-left census changed")
    recombined=Counter()
    for P,rows in tensor.items():
        for H,w in rows.items():
            recombined[P|H]+=w
    if recombined!=source_weighted_BA_hypergraph(model):
        raise AssertionError("sixset GQ source disagrees with conditional tensor")
    return tensor


def _checked_tensor(tensor,V):
    if type(V) is not int or V<6 or not hasattr(tensor,"items"):
        raise ValueError("invalid number of original right factors or tensor")
    for P,rows in tensor.items():
        if len(P)!=2 or len(set(P))!=2 or any(type(i) is not int or i<0 or i>=V for i in P):
            raise ValueError("invalid original right-line pair")
        if not hasattr(rows,"items"):
            raise ValueError("four-line conditional rows must be a mapping")
        for H,w in rows.items():
            if (len(H)!=4 or len(set(H))!=4 or P&set(H) or
                any(type(i) is not int or not 0<=i<V for i in H) or
                type(w) is not int or w<0):
                raise ValueError("invalid original four-line conditional source")


def pair_frozen_moment_certificate(rows, original_vertices, target_completions,
                                   *, retain_overlap_counts=False):
    """Exact first and second moment for random bijection of other V-2 labels.

    The distinguished original pair's two physical images AND the whole
    physical image F remain fixed. We independently randomize the
    remaining V-2 original line labels, uniformly over their occupied
    V-2 physical labels. This is a diagnostic distribution; NOT the
    adversarial fixed g, nor one joint randomization for all P.
    """
    V=original_vertices
    N=_choose(V-2,4)
    if N==0: raise ValueError("need >=6 original line vertices")
    w=sum(rows.values())
    q=len(target_completions)
    h2=sum(x*x for x in rows.values())
    centered_source=Fraction(h2)-Fraction(w*w,N)
    centered_target=Fraction(q)-Fraction(q*q,N)
    if centered_source<0 or centered_target<0:
        raise AssertionError("negative centered mass")
    mean=Fraction(w*q,N)
    error_square_bound=centered_source*centered_target
    source_overlap=Counter()
    for H,x in rows.items():
        for J,y in rows.items():
            source_overlap[len(H&J)]+=x*y
    target_overlap=Counter()
    for A in target_completions:
        for B in target_completions:
            target_overlap[len(A&B)]+=1
    second=Fraction(0)
    for j in range(5):
        denom=N*comb(4,j)*_choose(V-6,4-j)
        sn=source_overlap[j]
        tn=target_overlap[j]
        if not denom:
            if sn or tn:
                raise AssertionError("impossible overlap type has positive mass")
            continue
        second+=Fraction(sn*tn,denom)
    variance=second-mean*mean
    if variance<0:
        raise AssertionError("negative conditional variance")
    result={
        "source_mass":w,"occupied_fourset_target_count":q,
        "conditional_random_mean":mean,
        "conditional_random_second_moment":second,
        "conditional_random_variance":variance,
        "source_centered_L2_squared":centered_source,
        "target_centered_L2_squared":centered_target,
        "deterministic_error_squared_upper":error_square_bound,
        "deterministic_positive_overlap_sufficient":
            mean>0 and mean*mean>error_square_bound,
        "not_an_all_right_lower":True,
    }
    if retain_overlap_counts:
        result["ordered_source_pair_overlap_mass"]=tuple(source_overlap[j] for j in range(5))
        result["ordered_target_completion_pair_overlap_count"]=tuple(target_overlap[j] for j in range(5))
    return result


def evaluate_conditional_tensor(tensor, right_labels, *, a=6,
                                include_random_second_moments=False):
    """Exact fixed-g overlap, completed vs uncompleted original wedges.

    The per-P random mean is a DIAGNOSTIC, not the expectation of
    U(f,g) under one common permutation fixing all distinguished P.
    """
    if type(a) is not int or not 6<=a<=40:
        raise ValueError("finite C4 oracle restricts 6<=a<=40")
    labels=tuple(_physical_pair(e,a) for e in right_labels)
    if len(set(labels))!=len(labels):
        raise ValueError("not an injective physical right map")
    _checked_tensor(tensor,len(labels))
    occupied=frozenset(labels)
    by_pair={}
    actual=0
    total=0
    relaxed=0
    total_mean=Fraction(0)
    positive_but_zero=[]
    for pair,rows in tensor.items():
        phys_pair=tuple(labels[i] for i in sorted(pair))
        comp,full=occupied_target_residuals(a,occupied,phys_pair)
        actual_pair=sum(w for H,w in rows.items()
                        if frozenset(labels[i] for i in H) in comp)
        mass=sum(rows.values())
        m=Fraction(mass*len(comp),_choose(len(labels)-2,4))
        actual+=actual_pair
        total+=mass
        relaxed+=mass*len(comp)
        total_mean+=m
        if mass and comp and not actual_pair:
            positive_but_zero.append(tuple(sorted(pair)))
        output={
            "mass":mass, "full_target_two_label_codegree":full,
            "occupied_target_two_label_codegree":len(comp),
            "actual_six_edge_completions":actual_pair,
            "conditional_uniform_four_label_mean":m,
            "exact_conditional_discrepancy":Fraction(actual_pair)-m,
        }
        if include_random_second_moments:
            output.update(pair_frozen_moment_certificate(rows,len(labels),comp))
        by_pair[tuple(sorted(pair))]=output
    assert actual==sum(x["actual_six_edge_completions"] for x in by_pair.values())
    assert total_mean+sum(x["exact_conditional_discrepancy"] for x in by_pair.values())==actual
    return {
        "source_mass":total,
        "original_distinguished_pairs":len(by_pair),
        "actual_complete_six_edge_BA_overlap":actual,
        "relaxed_occupied_two_label_completion_weight":relaxed,
        "pairwise_conditioned_benchmarks_sum":total_mean,
        "pairwise_conditioned_discrepancy_sum":Fraction(actual)-total_mean,
        "pairs_with_available_completion_but_zero_actual":tuple(positive_but_zero),
        "pairs":by_pair,
        "fixed_g_identity_exact":True,
        "universal_s6_lower_proved":False,
        "not_a_joint_randomization":True,
    }


def finite_W32_report():
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    result={}
    for scheme in ("lex","reverse-line"):
        model=pair_labeled_symplectic(1,scheme)
        data=evaluate_conditional_tensor(original_W32_conditional_source(model),
                                         model["right_labels"],a=6)
        result[scheme]={
            "total_original_BA_mass":data["source_mass"],
            "actual_overlap":data["actual_complete_six_edge_BA_overlap"],
            "relaxed_occupied_completions":data["relaxed_occupied_two_label_completion_weight"],
            "conditional_uniform_benchmark":str(data["pairwise_conditioned_benchmarks_sum"]),
            "conditional_discrepancy":str(data["pairwise_conditioned_discrepancy_sum"]),
            "positive_completion_zero_actual_witness_count":
                 len(data["pairs_with_available_completion_but_zero_actual"]),
            "not_all_g_omega_s6":True,
        }
    return result


if __name__=="__main__":
    print(json.dumps(finite_W32_report(),sort_keys=True,indent=2,default=str))
