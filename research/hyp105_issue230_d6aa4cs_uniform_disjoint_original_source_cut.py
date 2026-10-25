"""HYP-105 #230 AA4-CS: all-h original physically disjoint 3path cut theorem.

Previously #617 proved many true original NONINCIDENT point-to-line
3paths in every half-coordinate cut, but #618 needs the source middle
POINT q and LINE l0 to have disjoint physical pair-images from their
respective endpoints before any B/B-overlap 3x3-permanent can occur.

NEW exact all-h obstruction elimination: under ANY arbitrary correlated
COMPLETE globally injected typed original f,g, at most 2(a-2)s*|P_X|
paths violate f(p)∩f(q)=empty, and at most 2(a-2)s*|L_Y| paths violate
g(l)∩g(l0)=empty. No independence, no per-Q redraw, no synthetic flags.
Hence from h>=14, for EVERY two halfalphabet cuts, at least
T_good >= |P_X|*|L_Y|/2 >= V^2/128 > s^6/128
source P3 paths satisfy BOTH physical disjointness conditions.
This does NOT force occupied C4 completions or a true 3x3 permanent=1,
and does NOT prove the root historical seven-motif lower S_s.
"""
from itertools import combinations
from math import comb, isqrt

from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original


def _minimal_a(V):
    if type(V) is not int or V<1:
        raise ValueError("positive integer true original factor count required")
    a=(1+isqrt(1+8*V))//2
    while comb(a,2)<V:a+=1
    while a>2 and comb(a-1,2)>=V:a-=1
    return a


def dyadic_all_h_disjoint_macro_arithmetic(h):
    """Exact integer arithmetic, with SYMBOLIC h>=14 proof in AA4-CS note.

    Regression across many finite h is not the proof of the all-h lemma.
    """
    if type(h) is not int or h<1:
        raise ValueError("integer dyadic h>=1 required")
    s=1<<h
    V=(s+1)*(s*s+1)
    a=_minimal_a(V)
    k=a//2
    H=comb(a,2)-V
    m=comb(k,2)-H
    d=s+1
    c=2*(a-2)*s
    threshold=2*d+4*c
    if not (0<=H<=a-2 and comb(a-1,2)<V<=comb(a,2)):
        raise AssertionError("minimal global physical K_a alphabet invalid")
    from_h14=h>=14
    if from_h14:
        if not (m>=V//8 and 8*m>=V and m>=threshold):
            raise AssertionError("uniform true-original physical disjoint source P3 cut gate failed")
        if not (2*(a-2)**2<= 9*V and 4*(a-2)**2 < 9*s**3):
            # First inequality need not be sharp; second is the all-h
            # simple bound a-2 < 3/2 * s^(3/2).
            raise AssertionError("symbolic a-2 bound violated")
        if m*m//2*128 < V*V:
            raise AssertionError("half-square physical anchor guaranteed lower falsified")
    return {
        "h":h,"s":s,"V":V,"a":a,"k":k,"H":H,"m":m,
        "d":d,"c_per_cut_factor":c,
        "sufficient_threshold_m_ge_2d_plus_4c":threshold,
        "margin":m-threshold,
        "uniform_half_cut_disjoint_gate_h_ge_14":from_h14,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def original_disjoint_3path_cut_certificate(model,X=None,Y=None):
    """Direct genuine ORIGINAL GQ 3paths under SAME full injected f,g.

    Returns actual cut T and disjoint survivor A, and independent
    upper bounds for each failure from original GQ girth and globally
    injected physical image incidence. No all-h threshold imposed on
    small original s (W32, W34, W38 can have ZERO survivors).
    """
    s,V,a,f,g,point_lines,line_points=_validated_original(model)
    k=a//2
    X=tuple(range(k)) if X is None else tuple(X)
    Y=tuple(range(a-k,a)) if Y is None else tuple(Y)
    for C in (X,Y):
        if len(C)!=k or len(set(C))!=k or any(
                type(v) is not int or not 0<=v<a for v in C):
            raise ValueError("two exact original halfalphabet physical coordinate cuts required")
    fx,gy=set(X),set(Y)
    P=tuple(p for p in range(V) if set(f[p])<=fx)
    L=tuple(l for l in range(V) if set(g[l])<=gy)
    source_path_T=0
    f_bad=0
    g_bad=0
    both_bad=0
    good=0
    direct_incidence_count=0
    for p in P:
        for l in L:
            if l in point_lines[p]:
                direct_incidence_count+=1
                continue
            source_path_T+=1
            mids=[(q,l0) for l0 in point_lines[p]
                  for q in line_points[l0]
                  if q!=p and l in point_lines[q]]
            if len(mids)!=1:
                raise AssertionError("actual W(3,s) source GQ unique nonincident threepath violated")
            q,l0=mids[0]
            left_blocked=not set(f[p]).isdisjoint(f[q])
            right_blocked=not set(g[l]).isdisjoint(g[l0])
            f_bad+=left_blocked
            g_bad+=right_blocked
            both_bad+=left_blocked and right_blocked
            good+=not left_blocked and not right_blocked
    x,y=len(P),len(L)
    c=2*(a-2)*s
    m=comb(k,2)-(comb(a,2)-V)
    e=direct_incidence_count
    if source_path_T!=x*y-e or good+f_bad+g_bad-both_bad!=source_path_T:
        raise AssertionError("true original P3 dual physical-disjoint partition incomplete")
    if f_bad>c*x or g_bad>c*y:
        raise AssertionError("uniform one-sided original point-line disjointness obstruction cap violated")
    if e>(s+1)*min(x,y) or x<m or y<m:
        raise AssertionError("true original minimal-pair complete injection/degree bound violated")
    base_lower=x*y-(s+1)*min(x,y)-c*(x+y)
    if good<base_lower or good<source_path_T-f_bad-g_bad:
        raise AssertionError("physical-disjoint original GQ 3path lower certificate failed")
    theorem=dyadic_all_h_disjoint_macro_arithmetic(s.bit_length()-1)
    if s>=2**14:
        if good*2<x*y or good*128<V*V or good*128<=s**6:
            raise AssertionError("original all-h uniform eta-half disjoint source path gate invalid")
    return {
        "s":s,"V":V,"a":a,"physical_cut_X":X,"physical_cut_Y":Y,
        "original_SOURCE_P_X":P,"original_SOURCE_L_Y":L,
        "x":x,"y":y,"actual_original_nonincident_source_3paths_T":source_path_T,
        "true_original_incidence_edges_between_cuts":e,
        "left_physical_disjointness_blocked_paths":f_bad,
        "right_physical_disjointness_blocked_paths":g_bad,
        "both_disjointness_blocked_paths":both_bad,
        "both_physically_disjoint_source_3paths":good,
        "uniform_left_block_upper":c*x,
        "uniform_right_block_upper":c*y,
        "bounded_union_lower":source_path_T-c*(x+y),
        "actual_xy_source_degree_lower":base_lower,
        "cut_min_source_factors_m":m,
        "uniform_half_cut_disjoint_gate_h_ge_14":s>=2**14,
        "all_h_source_original_sixflag_GF5_acceptance_UNPROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
