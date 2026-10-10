"""HYP-105 B3.2-E1-C5: one COMMON right-label bijection moments.

Corrects C4's pair-frozen conditional-probability non-composability.
A single physical occupied right-label set F is fixed. ONE uniform
bijection Pi:L_s -> F randomizes ALL original right vertices together,
not separately per distinguished original concurrence pair.
C0 source mass and C5 occupied target form a permutation intersection.
Their full first and second moments are EXACT via seven intersection
types of SIX-original-right-line sets, with finite rational witnesses.

These are permutation-AVERAGED results. NO lower bound for fixed
adversarial correlated g follows without extra uniform mixing.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import json

from hyp105_g5e2b3e1a_fixed_leading import _two_factors_K6
from hyp105_g5e2b3e1b1a_one_sided import gq_parameters
from hyp105_g5e2b3e1c0_weighted_overlap import (
    GQ_weighted_BA_right_sixset_spread, source_weighted_BA_hypergraph,
)


def validate_weighted_sixsets(weights,V):
    if type(V) is not int or V<6 or not hasattr(weights,"items"):
        raise ValueError("requires at least six original right vertices and mapping")
    out={}
    for R,w in weights.items():
        try:
            s=frozenset(R)
        except TypeError as exc:
            raise ValueError("invalid right sixset") from exc
        if (len(s)!=6 or any(type(i) is not int or i<0 or i>=V for i in s)
                or type(w) is not int or w<0 or s in out):
            raise ValueError("invalid original right sixset or multiplicity")
        if w:
            out[s]=w
    return out


def sixset_intersection_spectrum(weights,V):
    """Exact ordered weighted R,S intersection spectrum S_0..S_6.

    Avoid quadratic O(support^2) comparison. For k=0..6 compute
    A_k=sum_{Q subset [V],|Q|=k} d(Q)^2,
    d(Q)=sum_{R superseteq Q}m(R).
    Then A_k=sum_{j=k}^6 C(j,k)*S_j.
    Binomial invert S_j=sum_{k=j}^6 (-1)^(k-j)*C(k,j)*A_k.
    Complete exact integer result; no float, approximation, or sampling.
    """
    w=validate_weighted_sixsets(weights,V)
    marg=[Counter() for _ in range(7)]
    for R,value in w.items():
        order=sorted(R)
        for k in range(7):
            for Q in combinations(order,k):
                marg[k][Q]+=value
    binomial_moments=tuple(sum(v*v for v in d.values()) for d in marg)
    overlap=tuple(
        sum((-1)**(k-j)*comb(k,j)*binomial_moments[k]
            for k in range(j,7)) for j in range(7)
    )
    mass=sum(w.values())
    if any(x<0 for x in overlap) or sum(overlap)!=mass*mass:
        raise AssertionError("nonnegative ordered-intersection spectrum failed")
    if sum(overlap[j]*comb(j,k) for j in range(7)) != binomial_moments[k]:
        raise AssertionError("binomial inversion moment identity failed")
    return {
        "V":V,"mass":mass,"support":len(w),
        "binomial_squared_marginal_moments":binomial_moments,
        "ordered_pair_overlap_spectrum":overlap,
        "full_original_endpoint_indexing":True,
    }


def _pair(e,a):
    if (not isinstance(e,tuple) or len(e)!=2
            or any(type(x) is not int or x<0 or x>=a for x in e)
            or e[0]>=e[1]):
        raise ValueError("sorted distinct physical pair edge required")
    return e


def physical_occupied_target(a,occupied):
    """Finite exact T(F) all six-edge simple two-factors in occupied K_a.

    Efficient enumerate all 70 unlabeled K6 templates on every six
    physical coordinate subset. Conservative finite cap a<=9.
    General theorem and union bound do NOT require this enumeration.
    """
    if type(a) is not int or not 6<=a<=9:
        raise ValueError("finite target exact enumeration only 6<=a<=9")
    E=tuple(_pair(e,a) for e in occupied)
    if len(E)<6 or len(E)!=len(set(E)):
        raise ValueError("physical occupied labels must be injective")
    indices={e:i for i,e in enumerate(E)}
    target=set()
    for six in combinations(range(a),6):
        for template in _two_factors_K6():
            edges=tuple(tuple(sorted((six[i],six[j]))) for i,j in template)
            if all(e in indices for e in edges):
                target.add(frozenset(indices[e] for e in edges))
    if len(target)>70*comb(a,6):
        raise AssertionError("target physical T(F) exceeds full K_a")
    return frozenset(target)


def occupied_target_uniform_floor(s):
    """All-h right image F of size V: almost ALL full physical targets survive.

    Every missing physical edge label appears in exactly
    D=28*C(a-2,4) physical T_a sixsets. Therefore missing t labels
    destroy AT MOST t*D target 2factors by the union bound.
    Since t=K-V<a for the MINIMAL a, the removed fraction
    <=12*t/(a*(a-1)) = O(1/a), UNIFORMLY over every occupied F.

    The C0 GQ source mass lower gives a positive fixed-IMAGE random
    mean = Omega(s^6), not a fixed-permutation/all-g lower.
    """
    p=gq_parameters(s)
    v,a,K=p["V"],p["a"],p["K"]
    t=K-v
    spread=GQ_weighted_BA_right_sixset_spread(s)
    total=70*comb(a,6)
    each=28*comb(a-2,4)
    minimum=max(0,total-t*each)
    removed_fraction_upper=Fraction(t*each,total)
    assert removed_fraction_upper==Fraction(12*t,a*(a-1))
    mean=Fraction(spread["source_BA_weighted_mass_lower"]*minimum,comb(v,6))
    return {
        "s":s,"V":v,"a":a,"K":K,"missing_physical_labels":t,
        "target_full_Ka_count":total,
        "target_each_physical_edge_degree":each,
        "occupied_target_count_lower":minimum,
        "destroyed_target_fraction_upper_union":removed_fraction_upper,
        "GQ_original_BA_source_mass_lower":spread["source_BA_weighted_mass_lower"],
        "one_common_right_bijection_mean_lower":mean,
        "asymptotic_common_bijection_mean_lower":"(140-o(1))*s**6",
        "uniform_all_f_and_occupied_F":True,
        "not_fixed_adversarial_g_lower":True,
        "not_seven_family_lower":True,
    }


def common_bijection_moments(source,physical_target,V, *,
                              retain_spectra=False):
    """Exact E[U], E[U^2] for ONE shared Pi of all V original right vertices.

    Target sixsets are indexed by occupied physical edge labels 0..V-1,
    NOT physical coordinate vertices. Same injective physical image F
    is frozen, but its association with original right factors varies.
    Source includes original genuine incidence sixsets with multiplicity.

    For any ordered original (R,S) of overlap j, its images under Pi
    are uniform on D_j=C(V,6)*C(6,j)*C(V-6,6-j) ordered target
    sixset pairs of overlap j. Summing target C_j gives E[U^2].
    """
    source=validate_weighted_sixsets(source,V)
    T=validate_weighted_sixsets({R:1 for R in physical_target},V)
    if len(T)!=len(physical_target):
        raise ValueError("duplicate target sixsets")
    left=sixset_intersection_spectrum(source,V)
    right=sixset_intersection_spectrum(T,V)
    n=comb(V,6)
    mass=left["mass"]
    size=right["mass"]
    mean=Fraction(mass*size,n)
    second=Fraction(0)
    valid=[]
    for j in range(7):
        denom=n*comb(6,j)*comb(V-6,6-j) if 0<=6-j<=V-6 else 0
        sj=left["ordered_pair_overlap_spectrum"][j]
        tj=right["ordered_pair_overlap_spectrum"][j]
        if not denom:
            if sj or tj:
                raise AssertionError("impossible sixset overlap has nonzero mass")
            continue
        second+=Fraction(sj*tj,denom)
        valid.append(j)
    variance=second-mean*mean
    if variance<0:
        raise AssertionError("negative common-bijection variance")
    if not mass and (mean or second):
        raise AssertionError("zero original source has nonzero moment")
    support_lower=mean*mean/second if second>0 else Fraction(0)
    zero_prob_upper=min(Fraction(1), variance/(mean*mean)) if mean>0 else Fraction(1)
    result={
        "V":V,"source_mass":mass,"source_support":left["support"],
        "physically_occupied_target_size":size,
        "one_common_right_bijection_mean":mean,
        "one_common_right_bijection_second_moment":second,
        "one_common_right_bijection_variance":variance,
        "one_common_right_bijection_positive_probability_lower":
            support_lower,
        "one_common_right_bijection_zero_probability_Chebyshev_upper":
            zero_prob_upper,
        "valid_overlap_j":tuple(valid),
        "one_global_permutation_not_separate_P_conditionals":True,
        "all_correlated_fixed_g_lower_proved":False,
        "source_original_distinct_six_incidences_only":True,
    }
    if retain_spectra:
        result["source_ordered_overlap_spectrum"]=left["ordered_pair_overlap_spectrum"]
        result["target_ordered_overlap_spectrum"]=right["ordered_pair_overlap_spectrum"]
        result["source_binomial_squared_marginals"]=left["binomial_squared_marginal_moments"]
        result["target_binomial_squared_marginals"]=right["binomial_squared_marginal_moments"]
    return result


def fixed_map_overlap(source,physical_target,original_to_occupied):
    """Count actual weighted ORIGINAL sixsets for one FIXED original-right g."""
    m=tuple(original_to_occupied)
    V=len(m)
    if set(m)!=set(range(V)):
        raise ValueError("bijective original-right to occupied-edge indexing required")
    source=validate_weighted_sixsets(source,V)
    T=set(physical_target)
    return sum(w for R,w in source.items()
               if frozenset(m[i] for i in R) in T)


def genuine_W32_common_permutation_report():
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    output={}
    F=tuple(combinations(range(6),2))
    T=physical_occupied_target(6,F)
    lookup={p:i for i,p in enumerate(F)}
    for scheme in ("lex","reverse-line"):
        model=pair_labeled_symplectic(1,scheme)
        source=source_weighted_BA_hypergraph(model)
        g=tuple(lookup[e] for e in model["right_labels"])
        actual=fixed_map_overlap(source,T,g)
        moments=common_bijection_moments(source,T,15)
        output[scheme]={
            "genuine_fixed_right_BA":actual,
            "single_shared_random_right_mean":
                str(moments["one_common_right_bijection_mean"]),
            "single_shared_random_right_variance":
                str(moments["one_common_right_bijection_variance"]),
            "single_shared_random_positive_prob_lower":
                str(moments["one_common_right_bijection_positive_probability_lower"]),
            "same_source_marginal_moments_not_fixed_g_lower":True,
        }
    return output


def report():
    return {
        "all_h_minimal_alphabet_occupied_floor":{
            str(s):{k:str(v) if isinstance(v,Fraction) else v
                    for k,v in occupied_target_uniform_floor(s).items()}
            for s in (2,4,8,16,32,64,128)},
        "genuine_W32":genuine_W32_common_permutation_report(),
        "seven_family_omega_s6":False,
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True,default=str))
