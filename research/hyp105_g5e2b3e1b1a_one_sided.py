"""HYP-105 B3.2-E1-B1A: all-label, all-h one-sided six-motif mass.

A NEW restricted theorem: each injective mapping of V left factor
vertices to edges of K_a, for ANY Delta-regular bipartite factor graph,
gives Theta(s^15) distinct original six-incidence subsets whose LEFT
physical projection is leafless on exactly six coordinates. It makes no
claim that the RIGHT physical projection also passes, nor a lower on
R3 or S_seven. The missing right transfer is exactly the #230 blocker.

Proof: classify physically 2-regular graphs on six labeled physical
coordinate vertices as A (simple 2-factor), B (one double physical edge
and simple C4 elsewhere), C (three double physical edges of a matching).
For K_a images, their physical templates number 70/45/15 * C(a,6).
Each template occupies 6/5/3 distinct pair labels. The omitted t
physical pair labels destroy at most k*t/K of each total by edge
transitivity and the union bound. Every physical A/B/C template lifts
to Delta^6 / C(Delta,2)*Delta^4 / C(Delta,2)^3 DISTINCT unordered
original six-incidence sets. Multiplicity is exact: original degree
Delta and injectivity of left factor pair-label map suffice.

As s=2^h grows, a~sqrt(2)s^(3/2), V~s^3, Delta~s,
and L_left(s;f)=(151/144+o(1))s^15 UNIFORMLY over left injections.
No Ω(s^6) for two-sided S follows.
"""
from fractions import Fraction
from itertools import combinations
from math import comb
import json


COEFFICIENTS = {
    "A": Fraction(7, 9),
    "B": Fraction(1, 4),
    "C": Fraction(1, 48),
}
TOTAL_LIMIT = sum(COEFFICIENTS.values(), Fraction())
assert TOTAL_LIMIT == Fraction(151, 144)


def _positive_int(n, name):
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise ValueError(f"{name} must be a positive integer")


def _choose(n, k):
    return comb(n, k) if n >= k >= 0 else 0


def gq_parameters(s):
    _positive_int(s, "s")
    if s < 2 or (s & (s-1)):
        raise ValueError("W(3,s) certificate frozen for s=2^h, h>=1")
    V=(s+1)*(s*s+1)
    degree=s+1
    a=2
    while _choose(a,2)<V:
        a+=1
    K=_choose(a,2)
    missing=K-V
    if not 0<=missing<a:
        raise AssertionError("minimal coordinate alphabet violated")
    return {"s":s,"V":V,"Delta":degree,"a":a,
            "K":K,"missing":missing}


def template_counts(a, occupied_pairs):
    """Exact full-K_a counts and omitted-edge union bounds, all integers.

    Each distinct physical subgraph is enumerated once, on six physical
    symbols; no ordering of original columns or double-edge incidence
    choices is present at this stage.
    """
    _positive_int(a, "a")
    if a<6:
        raise ValueError("six physical symbols needed")
    K=_choose(a,2)
    if not isinstance(occupied_pairs,int) or isinstance(occupied_pairs,bool):
        raise ValueError("occupied_pairs must be an integer")
    if not 0<=occupied_pairs<=K:
        raise ValueError("occupied physical pair label count invalid")
    omitted=K-occupied_pairs
    count=_choose(a,6)
    totals={"A":70*count,"B":45*count,"C":15*count}
    edges_used={"A":6,"B":5,"C":3}
    affected={}
    lower={}
    for kind,total in totals.items():
        touched=total*edges_used[kind]
        if touched%K:
            raise AssertionError("edge-transitive physical pattern orbit broken")
        per_missing=touched//K
        affected[kind]=per_missing
        lower[kind]=max(0,total-omitted*per_missing)
    return {"full":totals,"lower":lower,
            "per_missing_edge":affected,"edges_per_motif":edges_used,
            "missing":omitted,"K":K,
            "all_injection_images_covered":True}


def left_six_mass(s):
    """Integer L_left bounds for EVERY physical-pair factor injection."""
    p=gq_parameters(s)
    template=template_counts(p["a"],p["V"])
    d=p["Delta"]
    lifts={"A":d**6,
           "B":_choose(d,2)*d**4,
           "C":_choose(d,2)**3}
    lower={k:template["lower"][k]*lifts[k] for k in lifts}
    upper={k:template["full"][k]*lifts[k] for k in lifts}
    return {
        **p,
        "factor_graph":"any simple Delta-regular bipartite factor host",
        "left_original_sixsets_lower":lower,
        "left_original_sixsets_upper":upper,
        "total_left_lower":sum(lower.values()),
        "total_left_upper":sum(upper.values()),
        "physical_pattern_bounds":template,
        "lift_multiplicities":lifts,
        "normalized_asymptotic_limit":"151/144",
        "same_label_seven_family_lower":False,
        "strict_GQ_GF5_R3_exponent":False,
    }


def _patterns_on_six(a):
    """Slow but independent K6 local structural reference; a<=14 only."""
    all_local=tuple(combinations(range(6),2))
    A=[]
    B=[]
    C=[]
    for chosen in combinations(all_local,6):
        degree=[0]*6
        for u,v in chosen:
            degree[u]+=1
            degree[v]+=1
        if degree==[2]*6:
            A.append(tuple(chosen))
    for repeat in all_local:
        rem=set(range(6))-set(repeat)
        local=tuple(combinations(sorted(rem),2))
        for cycle in combinations(local,4):
            counts=[sum(x in edge for edge in cycle) for x in rem]
            if counts==[2]*4:
                B.append((repeat,)+tuple(cycle))
    for triple in combinations(all_local,3):
        if len({x for edge in triple for x in edge})==6:
            C.append(tuple(triple))
    if tuple(map(len,(A,B,C)))!=(70,45,15):
        raise AssertionError("independent physical six-symbol census")
    return {"A":tuple(A),"B":tuple(B),"C":tuple(C)}


def exact_physical_counts(a, pair_edges, *, max_a=14):
    """Deliberately slow independent exact missing-pair graph oracle.

    This scans all C(a,6)*(70+45+15) patterns, NOT original incidence
    sixsets. Refuses expensive dimensions instead of sampling or silent
    truncation. The B template has a repeated pair but set membership
    uses its five distinct physical edges, as required.
    """
    _positive_int(a,"a")
    if a<6 or a>max_a:
        raise ValueError("explicit exact pattern oracle resource bound")
    legal=set(combinations(range(a),2))
    try:
        edge_list=tuple(pair_edges)
        pairs=set(edge_list)
    except TypeError as exc:
        raise ValueError("physical graph pair iterator invalid") from exc
    if len(pairs)!=len(edge_list):
        raise ValueError("physical pair labels must be injective")
    if not pairs<=legal:
        raise ValueError("invalid unordered physical pair edges")
    patterns=_patterns_on_six(a)
    result={"A":0,"B":0,"C":0}
    for vertices in combinations(range(a),6):
        for kind, templates in patterns.items():
            for pattern in templates:
                physical=tuple(tuple(sorted((vertices[u],vertices[v])))
                               for u,v in pattern)
                if all(e in pairs for e in physical):
                    result[kind]+=1
    return result


def report():
    cases=[]
    for s in (2,4,8,16,32,64,128):
        b=left_six_mass(s)
        cases.append({
            "s":s,"a":b["a"],"K":b["K"],"missing":b["missing"],
            "left_lower":b["total_left_lower"],
            "left_upper":b["total_left_upper"],
            "normalized_lower":str(Fraction(b["total_left_lower"],s**15)),
            "normalized_upper":str(Fraction(b["total_left_upper"],s**15)),
        })
    return {
        "theorem":"universal one-sided original six-incidence physical-2-regular mass",
        "exact_W32_A_B_C":{"A":51030,"B":10935,"C":405},
        "uniform_leading_A":str(COEFFICIENTS["A"]),
        "uniform_leading_B":str(COEFFICIENTS["B"]),
        "uniform_leading_C":str(COEFFICIENTS["C"]),
        "uniform_leading_total":str(TOTAL_LIMIT),
        "all_h_quantifiers":True,
        "two_sided_motif_Omega_s6":False,
        "need_right_projection_transfer_rate":"Omega(s^-9)",
        "actual_full_GF5_R3_bound":False,
        "checks":cases,
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
