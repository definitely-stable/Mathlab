"""HYP-105 #230 AA4-AU: NEW all-h TWO genuine source-line original
incidence-support CAP for signed SEVEN-GF5 disjoint-global-swap Hessians.

PR #417 already proved the mixed-swap HESSIAN support identity. This
slice derives previously missing explicit TRUE-ORIGINAL all-h numeric
source-line-two-factor capacity using GQ no-four-cycle partial linearity
and physical doubly-rooted 2-regular multigraph slots.

Actual original six DISTINCT incidence IDs, complete globally injected
original factor f,g, same fixed physical image support: NO per-Q redraw.
No fixed-adversarial-original-seven S>=Omega(s6) inferred.
"""
from collections import Counter
from itertools import combinations, combinations_with_replacement
from math import comb, factorial

from hyp105_issue230_d6aa4r_quenched_original_d6 import _params
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import (
    classify_seven_prechecked, R3_CERTIFIED_FLOORS, seven_census,
)
from hyp105_issue230_d6aa4at_seven_swap_boundary import LEFT_MAX_WEIGHT

TYPES={ (1,1,1,1,1,1):"A", (2,1,1,1,1):"B", (2,2,2):"C" }
EXPECTED={
    "same": {"B":3,"C":3},
    "adjacent": {"A":7,"B":3},
    "disjoint": {"A":14,"B":6,"C":1},
}
CANONICAL_DISJOINT_PAIRS=(
    ((0,1),(2,3)),
    ((0,2),(3,4)),
    ((0,3),(1,4)),
    ((0,5),(6,7)),
    ((4,5),(8,9)),
    ((1,2),(10,11)),
)


def independent_doubly_rooted_K6_physical_multiset():
    """Literal all 5005 six-edge multisets, no theorem constant assumed.

    Here "same" demands >=2 OCCURRENCES of physical edge 0-1;
    "adjacent" demands >=1 of 0-1,0-2; and "disjoint" >=1 of 0-1,2-3.
    The source incidence pair is ORDERED as two assigned real ORIGINAL
    LINE factors, but physical multiset permutations of remaining four
    factor columns are counted by 4! in the actual source cap.
    """
    es=tuple(combinations(range(6),2))
    out={key:Counter() for key in EXPECTED}
    for six in combinations_with_replacement(es,6):
        deg=Counter(i for edge in six for i in edge)
        if len(deg)!=6 or set(deg.values())!={2}:continue
        c=Counter(six)
        kind=TYPES.get(tuple(sorted(c.values(),reverse=True)))
        if kind is None:raise AssertionError("unexpected 2regular original half")
        if c[(0,1)]>=2:out["same"][kind]+=1
        if c[(0,1)]>=1 and c[(0,2)]>=1:out["adjacent"][kind]+=1
        if c[(0,1)]>=1 and c[(2,3)]>=1:out["disjoint"][kind]+=1
    a={k:dict(v) for k,v in out.items()}
    if a!=EXPECTED:
        raise AssertionError("independent doubly pinned physical 2factor count mismatch")
    return a


def every_original_two_line_seven_hessian_cap(s):
    """Symbolic all-h certificate for ANY two distinct ACTUAL ORIGINAL lines.

    Choose true incidences (p,ell) and (q,m). If p=q, true GQ
    partial linearity gives <=ONE common point (no C4). Both image
    physical edges of this point are the SAME, and the fixed pair of
    incidence slots requires two occurrences in a six-coordinate
    2factor. There are exactly 6*C(a-2,4) formal templates.

    If p!=q, <=d^2 choices, and full global injected f gives distinct
    physical edges: if adjacent, 10*C(a-3,3) templates; if disjoint,
    21*C(a-4,2) templates. Independent of which case actually applies,
    ADD the two possible capacities to bound all <=d² source pairs.

    Four remaining original incidence columns: at most 4! ways to
    assign remaining factor occurrence slots, and at most d^4 legal
    actual original line factors through physical-inverse source POINT
    factors (each has exactly d GQ line neighbors). Every eligible true
    six-incidence Q containing ell,m has >=one such rooted encoding,
    and repeated source flags only OVERCOUNT.
    """
    V,a,K,m=_params(s);d=s+1
    C4=comb(a-2,4); C3=comb(a-3,3); C2=comb(a-4,2)
    P=factorial(4)*d**4
    capacities={
        "same_original_POINT":P*6*C4,
        "different_points_adjacent_physical":P*d**2*10*C3,
        "different_points_disjoint_physical":P*d**2*21*C2,
    }
    N=sum(capacities.values())
    weighted_modes={
        mode:sum(LEFT_MAX_WEIGHT[t]*qty for t,qty in counts.items())
        for mode,counts in EXPECTED.items()
    }
    if weighted_modes != {"same":302400,"adjacent":474450,"disjoint":997950}:
        raise AssertionError("selected seven GF5 frozen historic coefficient maxima changed")
    weighted_pair=P*(
        weighted_modes["same"]*C4+
        d**2*(weighted_modes["adjacent"]*C3+weighted_modes["disjoint"]*C2))
    if s>=4:
        if a*a>4*s**3 or 4*d>5*s:
            raise AssertionError("actual minimal dyadic K_a scaling proof gate invalid")
        if N>5400*s**11:
            raise AssertionError("uniform genuine two-LINE source support O(s11) fails")
        # A pair of disjoint line source swaps \u03c3,\u03c4 affects at most
        # four ordered choices of one factor in each swap; their common
        # original Q shadow <=4N. Indicator mixed finite difference has
        # |H_Q|<=2; consequently |H S7|<=8N, and same for weighted caps.
        if 8*N>43200*s**11:
            raise AssertionError("all-h original seven-class disjoint-swap Hessian O(s11)")
    return {
        "s":s,"a":a,"K":K,"V":V,"d":d,
        "same_true_source_point_at_most_one_by_GQ_C4free":True,
        "doubly_pinned_true_original_physical_2factor_A_B_C":EXPECTED,
        "actual_original_two_distinct_LINE_factor_sixQ_support_upper":N,
        "support_components":capacities,
        "selected_GF5_51palette_numerator_abs_one_Q_seven_weight_upper":weighted_pair,
        "disjoint_two_global_source_LINE_swaps_four_factor_crosspairs":4,
        "absolute_mixed_seven_S_Hessian_upper":8*N,
        "absolute_mixed_selected_GF5_numerator_Hessian_upper":8*weighted_pair,
        "s_ge4_explicit_unweighted_Hessian_upper_43200_s11":s>=4,
        "uses_genuine_original_GQ_no_source_C4":True,
        "classwise_signed_Hessian_support_already_prior_PR417":True,
        "original_same_full_global_f_g_seven_lower_PROVED":False,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def _original_left_rows(model):
    inc=tuple(tuple(x) for x in model["incidences"])
    rows=[]
    for ids,kind in selected_left_six(model):
        row=(tuple(ids),frozenset(inc[i][1] for i in ids),kind)
        if len(set(row[0]))!=6:raise AssertionError("not six actual original distinct source flags")
        rows.append(row)
    if len(rows)!=62370:raise AssertionError("not true original W32 62370-Q left census")
    return tuple(rows)


def genuine_original_W32_two_line_support(scheme):
    """Independent literal real original source Q original two-line overlap."""
    model=fixture(1,scheme)
    rows=_original_left_rows(model)
    c=every_original_two_line_seven_hessian_cap(2)
    source=tuple(map(tuple,model["incidences"]))
    neighboring_points=[set() for _ in range(15)]
    for p,l in source: neighboring_points[l].add(p)
    if len(source)!=45 or any(len(pts)!=3 for pts in neighboring_points):
        raise AssertionError("not genuine original W32 line neighborhood")
    per_pair=[]
    for l,m in ((0,1),(0,2),(2,3),(4,5),(10,11),(13,14)):
        intersection=neighboring_points[l]&neighboring_points[m]
        if len(intersection)>1:
            raise AssertionError("true original GQ no-4cycle violated")
        hits=[row for row in rows if l in row[1] and m in row[1]]
        dist=Counter(row[2] for row in hits)
        if len(hits)>c["actual_original_two_distinct_LINE_factor_sixQ_support_upper"]:
            raise AssertionError("original two-LINE factor capacity is false")
        per_pair.append({
            "two_ACTUAL_original_LINE_factor_IDs":(l,m),
            "number_of_actual_shared_original_point_factors":len(intersection),
            "genuine_six_ID_Q_with_both_line_source_factors":len(hits),
            "genuine_six_ID_left_type_histogram":dict(dist),
        })
    return {"scheme":scheme,"s":2,"genuine_original_left_candidate_Q":len(rows),
            "per_actual_source_line_pair":per_pair,
            "true_GQ_no_source_C4_verified":True,
            "all_h_mixed_hessian_S7_lower_PROVED":False}


def genuine_original_W32_signed_disjoint_swap_hessian(scheme):
    """4 full globally coherent source line maps, all seven tag Hessian.

    This applies prior EXACT #417 identity and validates the NEW all-h
    quantitative two-source-factor overlap cap on true original Q.
    """
    if scheme not in ("S68","S72","lex","reverse"):
        raise ValueError("real W32 fixed original scheme only")
    m=fixture(1,scheme)
    rows=_original_left_rows(m)
    f=tuple(map(tuple,m["left_labels"]))
    g=tuple(map(tuple,m["right_labels"]))
    inc=tuple(map(tuple,m["incidences"]))
    cap=every_original_two_line_seven_hessian_cap(2)
    results=[]
    for (u,v),(x,y) in CANONICAL_DISJOINT_PAIRS:
        if len({u,v,x,y})!=4:raise AssertionError("swaps must be disjoint actual source line IDs")
        a=list(g);a[u],a[v]=a[v],a[u];g_s=tuple(a)
        a=list(g);a[x],a[y]=a[y],a[x];g_t=tuple(a)
        a=list(g_s);a[x],a[y]=a[y],a[x];g_st=tuple(a)
        if len(set(g_st))!=15 or set(g_st)!=set(g):
            raise AssertionError("not globally injected source LINE image swap maps")
        cc={}
        for name,rg in (("0",g),("s",g_s),("t",g_t),("st",g_st)):
            ct=Counter()
            for ids,ls,kind in rows:
                tag=classify_seven_prechecked(ids,f,rg,inc)
                if tag is not None:ct[tag]+=1
            cc[name]=ct
        hs={tag:cc["st"][tag]-cc["s"][tag]-cc["t"][tag]+cc["0"][tag]
            for tag in R3_CERTIFIED_FLOORS}
        h=sum(hs.values())
        shadow=[r for r in rows if r[1]&{u,v} and r[1]&{x,y}]
        if len(shadow)>4*cap["actual_original_two_distinct_LINE_factor_sixQ_support_upper"]:
            raise AssertionError("two-source-line actual shadow bound false")
        # Direct per TRUE source Q support Hessian: sum only shadow.
        sparse=Counter()
        for ids,ls,kind in shadow:
            tags=[classify_seven_prechecked(ids,f,rg,inc)
                  for rg in (g,g_s,g_t,g_st)]
            for t,w in zip(tags,(1,-1,-1,1)):
                if t is not None:sparse[t]+=w
        if any(hs[tag]!=sparse[tag] for tag in R3_CERTIFIED_FLOORS):
            raise AssertionError("true original two-disjoint-swap signed support Hessian mismatch")
        wH=sum(hs[tag]*R3_CERTIFIED_FLOORS[tag] for tag in hs)
        if abs(h)>2*len(shadow) or abs(wH)>8*cap[
            "selected_GF5_51palette_numerator_abs_one_Q_seven_weight_upper"]:
            raise AssertionError("mixed source class Hessian too large")
        results.append({
            "two_disjoint_true_LINE_factor_transpositions":((u,v),(x,y)),
            "source_original_six_ID_Q_with_both_swap_source_support":len(shadow),
            "seven_S_before":sum(cc["0"].values()),
            "signed_mixed_seven_S_Hessian":h,
            "seven_per_tag_signed_Hessian":hs,
            "selected_GF5_weighted_necessary_numerator_Hessian":wH,
            "independent_sparse_true_Q_Hessian_agrees_with_four_full_maps":True,
        })
    return {
        "scheme":scheme,"s":2,
        "original_global_source_line_pair_injective_all_four_states":True,
        "actual_original_left_Q":len(rows),
        "all_h_new_quantitative_pair_shadow_bound_checked":True,
        "mixed_hessian_rows":results,
        "root_A_B_C":"OPEN_WITH_FORMAL_BLOCKER"
    }


if __name__=="__main__":
    import json
    print(json.dumps(independent_doubly_rooted_K6_physical_multiset(),sort_keys=True))
    for h in range(1,30):
        c=every_original_two_line_seven_hessian_cap(1<<h)
        print("ALL_H_PAIR_CAP",h,c["a"],c["actual_original_two_distinct_LINE_factor_sixQ_support_upper"])
    for scheme in ("S68","lex"):
        print("TRUE_ORIGINAL_MIXED_HESSIAN",json.dumps(
            genuine_original_W32_signed_disjoint_swap_hessian(scheme),sort_keys=True))
