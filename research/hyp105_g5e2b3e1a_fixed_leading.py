"""HYP-105 B3.2-E1-A: exhaustive W(3,2) fixed-label leading six motifs.

For the complete 15-by-15 pair-label bijections K6, enumerate the 62,370
candidate six-incidence sets with LEFT coordinate projection 6-vertex
2-regular (A / B / C) WITHOUT scanning binom(45,6).
Then independently test the RIGHT 6-coordinate 2-regular projection and
classify the accepted strictly-positive C/A, C/B, and B/B sectors.

This is an exact finite structural census, NOT the exact full R3. Each
counted six-set has ten positive GF5 3v3 signed events by accepted #214,
#218, #224. The fixed-map R3 lower only charges proved class-specific
minimum GF5 full-51-palette weights. Does NOT prove all-h Omega(s^6),
does NOT bound entire R3 above, and never claims asymptotic extrapolation.
"""
from collections import Counter
from itertools import combinations, product
from fractions import Fraction
import json

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3b2_coincident_cycles import check_input
from hyp105_g5e2b3b1b_five_six_flows import exact_dual_GF5_six_flow

PAIRS=tuple(combinations(range(6),2))
GF5_DENOM=51**6
MIN_GF5={"C/A":4332, "C/B":4905, "B/B-overlap":5175,
         "B/B-disjoint":4501}
CASES=("C/A","C/B","B/B-overlap","B/B-disjoint")


def _half_projection_kind(incidences, labels):
    """Structural half classifier: exactly six touched physical symbols."""
    endpoints=tuple(incidences)
    freq=Counter(endpoints)
    prof=tuple(sorted(freq.values(),reverse=True))
    if prof==(1,)*6:
        kind="A"
    elif prof==(2,1,1,1,1):
        kind="B"
    elif prof==(2,2,2):
        kind="C"
    else:
        return None
    deg=[0]*6
    for endpoint in endpoints:
        u,v=labels[endpoint]
        deg[u]+=1
        deg[v]+=1
    return kind if deg==[2]*6 else None


def _four_cycles_on_four(vertices):
    edges=tuple(combinations(sorted(vertices),2))
    choices=[]
    for graph in combinations(edges,4):
        degree=Counter(u for edge in graph for u in edge)
        if all(sum(v in edge for edge in graph)==2 for v in vertices):
            choices.append(tuple(sorted(graph)))
    if len(choices)!=3:
        raise AssertionError("four physical vertices must have three C4s")
    return tuple(sorted(choices))


def _perfect_matchings(vertices):
    if not vertices:
        yield ()
        return
    root=vertices[0]
    for index in range(1,len(vertices)):
        partner=vertices[index]
        for other in _perfect_matchings(vertices[1:index]+vertices[index+1:]):
            yield ((root,partner),)+other


def _two_factors_K6():
    out=[]
    for graph in combinations(PAIRS,6):
        degree=[0]*6
        for a,b in graph:
            degree[a]+=1;degree[b]+=1
        if degree==[2]*6:
            out.append(graph)
    if len(out)!=70:
        raise AssertionError("K6 has exactly 70 simple six-edge 2-factors")
    return tuple(out)


def validated_small_model(model):
    a,left,right,edges=check_input(model)
    if (a!=6 or len(left)!=15 or len(right)!=15 or
            len(edges)!=45 or model.get("s")!=2 or
            set(left)!=set(PAIRS) or set(right)!=set(PAIRS)):
        raise ValueError("E1-A exact census supports only W(3,2) K6 bijections")
    by_point=[[] for _ in left]
    for i,(p,l) in enumerate(edges):
        by_point[p].append(i)
    if sorted(map(len,by_point))!=[3]*15:
        raise ValueError("expected 15 three-regular factor points")
    return left,right,edges,tuple(tuple(ids) for ids in by_point)


def selected_left_six(model):
    """Exactly once each of 51,030 A + 10,935 B + 405 C candidates.

    These are selected six ORIGINAL incidence IDs; no signed coefficients
    and no multiplicity based on physical-coordinate automorphisms.
    """
    left,_,_,by_point=validated_small_model(model)
    invert={pair:i for i,pair in enumerate(left)}
    if len(invert)!=15:
        raise AssertionError("not bijective")
    for cycle in _two_factors_K6():
        ids=tuple(invert[e] for e in cycle)
        for selection in product(*(by_point[p] for p in ids)):
            yield tuple(sorted(selection)),"A"
    for pair in PAIRS:
        p=invert[pair]
        remaining=tuple(v for v in range(6) if v not in pair)
        for square in _four_cycles_on_four(remaining):
            others=tuple(invert[e] for e in square)
            for twice in combinations(by_point[p],2):
                for singles in product(*(by_point[q] for q in others)):
                    yield tuple(sorted(twice+singles)),"B"
    matchings=tuple(_perfect_matchings(tuple(range(6))))
    if len(matchings)!=15:
        raise AssertionError("six vertices have 15 perfect matchings")
    for matching in matchings:
        points=tuple(invert[edge] for edge in matching)
        for pairs in product(*(tuple(combinations(by_point[p],2))
                               for p in points)):
            yield tuple(sorted(x for pair in pairs for x in pair)),"C"


def classify_six(model, indices):
    """One exact original 6-incidence set; None for all other patterns."""
    left,right,edges,_=validated_small_model(model)
    ids=tuple(sorted(indices))
    if len(ids)!=6 or len(set(ids))!=6 or ids[0]<0 or ids[-1]>=len(edges):
        raise ValueError("six DISTINCT actual incidence-column IDs required")
    pts=tuple(edges[i][0] for i in ids)
    lns=tuple(edges[i][1] for i in ids)
    lkind=_half_projection_kind(pts,left)
    rkind=_half_projection_kind(lns,right)
    if not lkind or not rkind:
        return None
    if {lkind,rkind}=={"A","C"}:
        return "C/A"
    if {lkind,rkind}=={"B","C"}:
        return "C/B"
    if lkind==rkind=="B":
        lp=next(p for p,n in Counter(pts).items() if n==2)
        rp=next(p for p,n in Counter(lns).items() if n==2)
        L={j for j,p in enumerate(pts) if p==lp}
        R={j for j,p in enumerate(lns) if p==rp}
        intersection=len(L&R)
        if intersection not in (0,1):
            raise AssertionError("two distinct GQ factor incidences duplicated")
        return "B/B-overlap" if intersection else "B/B-disjoint"
    return None


def finite_census(model, *, collect_sets=False):
    """Complete finite counts and the proven per-label R3 lower numerator."""
    validated_small_model(model)
    counts=Counter()
    types=Counter()
    witnesses={}
    included={} if collect_sets else None
    seen=set()
    for ids,expected_left in selected_left_six(model):
        if ids in seen:
            raise AssertionError("physical projection enumerator repeats a 6-set")
        seen.add(ids)
        p=tuple(model["incidences"][i][0] for i in ids)
        actual_left=_half_projection_kind(p,model["left_labels"])
        if actual_left!=expected_left:
            raise AssertionError("left physical 2-factor generator invalid")
        types[expected_left]+=1
        tag=classify_six(model,ids)
        if tag is not None:
            counts[tag]+=1
            witnesses.setdefault(tag,ids)
            if included is not None:
                included[ids]=tag
    if len(seen)!=62370 or types!=Counter({"A":51030,"B":10935,"C":405}):
        raise AssertionError("A/B/C exhaustive left-degree2 candidate counts changed")
    r3_floor=sum(10*MIN_GF5[tag]*counts[tag] for tag in CASES)
    if r3_floor<0:
        raise AssertionError("negative full GF5 risk impossible")
    return {
        "candidate_left_2factor_sets":len(seen),
        "candidate_counts_by_left_type":dict(types),
        "new_motif_counts":dict((name,counts[name]) for name in CASES),
        "new_total_original_six_sets":sum(counts.values()),
        "all_ten_balanced_signs_positive_per_counted_set":True,
        "GF5_exact_restricted_R3_lower_numerator":r3_floor,
        "GF5_exact_restricted_R3_lower":Fraction(r3_floor,GF5_DENOM),
        "witnesses":witnesses,
        "sets":included,
        "not_full_R3":True,
        "all_h_fixed_label_Omega_s6":False,
        "new_ASET_power":False,
    }


def exact_witness_GF5(model, ids):
    """Independent 782-dual Fourier oracle, ten full-palette signs."""
    tag=classify_six(model,ids)
    if tag not in MIN_GF5:
        raise ValueError("selected witness is not in a new positive class")
    from hyp105_g5e2b3b1_critical_flows import SIGNS
    weights=[]
    for mask in SIGNS:
        signs=tuple(1 if mask&(1<<i) else -1 for i in range(6))
        weights.append(exact_dual_GF5_six_flow(
            tuple(model["supports"][i] for i in sorted(ids)),
            signs,dimension=12))
    if len(weights)!=10 or min(weights)<MIN_GF5[tag]:
        raise AssertionError("exact full GF5 flow below accepted class minimum")
    return {"class":tag,"min":min(weights),"max":max(weights),
            "sum":sum(weights),"GF5_positive_signed_events":len(weights)}


def report():
    data=[]
    for scheme in ("lex","reverse-line"):
        model=pair_labeled_symplectic(1,scheme)
        x=finite_census(model)
        evidence={tag:exact_witness_GF5(model,ids)
                  for tag,ids in x["witnesses"].items()}
        data.append({
            "scheme":scheme,
            "candidate_left_2factor_sets":x["candidate_left_2factor_sets"],
            "left_types":x["candidate_counts_by_left_type"],
            "new_motifs":x["new_motif_counts"],
            "new_total":x["new_total_original_six_sets"],
            "fixed_R3_lower_GF5_numerator":
                x["GF5_exact_restricted_R3_lower_numerator"],
            "fixed_R3_lower_GF5_denominator":GF5_DENOM,
            "full_GF5_witnesses":evidence,
        })
    return {"scope":"complete W(3,2) six-coordinate NEW leading 4 sectors only",
            "cases":data, "GF5_full_palette":51, "all_h_exponent":False,
            "fixed_R3_upper":False, "new_aset_exponent":False}


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
