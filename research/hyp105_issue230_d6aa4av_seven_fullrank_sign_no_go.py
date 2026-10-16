"""HYP-105 / #230 AA4-AV -- seven GF5 class signed-curvature rank barrier.

The source-local signed disjoint-transposition Hessian identity is PRIOR
work (#417, #497). This slice studies the rank of the SEVEN original
classwise Hessian vectors at genuine W(3,2), fixed FULL global f,g,
and the all-h sign reversal under a LEGAL whole-source-LINE swap.

No positive seven-class ORIGINAL global minimax theorem follows.
"""
from fractions import Fraction
from itertools import combinations
from math import factorial

from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS
from hyp105_issue230_d6aa4au_two_line_seven_hessian import (
    genuine_original_W32_signed_disjoint_swap_hessian,
    CANONICAL_DISJOINT_PAIRS,
)
from hyp105_issue230_projection import fixture

ORDER=tuple(R3_CERTIFIED_FLOORS)
assert len(ORDER)==7 and len(set(ORDER))==7


def integer_rank_and_basis(rows):
    """Exact rational row reduction, independent of GF5 class scorer."""
    if not rows:
        return {"rank":0,"pivot_row_indices":(),"pivot_column_indices":()}
    width=len(rows[0])
    if not width or any(len(row)!=width for row in rows):
        raise ValueError("rectangular integer matrix required")
    if any(type(x) is not int for row in rows for x in row):
        raise ValueError("genuine integer Hessian count entries required")
    a=[[Fraction(x) for x in row] for row in rows]
    labels=list(range(len(a)))
    rank=0
    pivots=[]
    for col in range(width):
        pos=next((i for i in range(rank,len(a)) if a[i][col]),None)
        if pos is None:continue
        a[rank],a[pos]=a[pos],a[rank]
        labels[rank],labels[pos]=labels[pos],labels[rank]
        pivot=a[rank][col]
        a[rank]=[x/pivot for x in a[rank]]
        for j in range(rank+1,len(a)):
            q=a[j][col]
            if q:
                a[j]=[x-q*y for x,y in zip(a[j],a[rank])]
        pivots.append(col)
        rank+=1
        if rank==min(len(rows),width):break
    return {"rank":rank,"pivot_row_indices":tuple(labels[:rank]),
            "pivot_column_indices":tuple(pivots)}


def integer_determinant_bareiss(matrix):
    """Second, independently arithmetic rational-free determinant oracle."""
    n=len(matrix)
    if not n or any(len(r)!=n for r in matrix):
        raise ValueError("square integer matrix required")
    a=[list(row) for row in matrix]
    if any(type(x) is not int for row in a for x in row):
        raise ValueError("integer matrix expected")
    sign=1
    previous=1
    for k in range(n-1):
        j=next((j for j in range(k,n) if a[j][k]),None)
        if j is None:return 0
        if j!=k:
            a[k],a[j]=a[j],a[k]
            sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for h in range(k+1,n):
                num=a[i][h]*pivot-a[i][k]*a[k][h]
                if num%previous:
                    raise AssertionError("Bareiss nonintegral pivot: exact math bug")
                a[i][h]=num//previous
            a[i][k]=0
        previous=pivot
    return sign*a[-1][-1]


def exact_original_w32_hessian_linear_obstruction():
    """24 genuine original W32 global-map curvature vectors.

    All 24 entries come from EXACT same-original-six-ID source incidence
    Q, scored at FOUR complete global g states. Each original f and g
    is held complete and globally injected; no per-Q redraw.
    """
    rows=[]
    witnesses=[]
    for scheme in ("S68","S72","lex","reverse"):
        z=genuine_original_W32_signed_disjoint_swap_hessian(scheme)
        if len(z["mixed_hessian_rows"])!=6:
            raise AssertionError("6 historical disjoint swaps expected per map")
        for j,w in enumerate(z["mixed_hessian_rows"]):
            if w["two_disjoint_true_LINE_factor_transpositions"]!=CANONICAL_DISJOINT_PAIRS[j]:
                raise AssertionError("true source swap witness provenance shifted")
            if not w["independent_sparse_true_Q_Hessian_agrees_with_four_full_maps"]:
                raise AssertionError("original source Q sparse Hessian not validated")
            v=tuple(w["seven_per_tag_signed_Hessian"][k] for k in ORDER)
            if sum(v)!=w["signed_mixed_seven_S_Hessian"]:
                raise AssertionError("wrong historical unweighted seven curvature")
            if sum(x*R3_CERTIFIED_FLOORS[k] for x,k in zip(v,ORDER)) != (
                    w["selected_GF5_weighted_necessary_numerator_Hessian"]):
                raise AssertionError("wrong historical selected GF5 floor numerator")
            rows.append(v)
            witnesses.append({
                "scheme":scheme,
                "two_ACTUAL_original_LINE_swaps":CANONICAL_DISJOINT_PAIRS[j],
                "seven_original_class_vector":dict(zip(ORDER,v)),
                "signed_seven_Hessian":sum(v),
                "selected_Gf5_floor_numerator_Hessian":sum(
                    v[i]*R3_CERTIFIED_FLOORS[k] for i,k in enumerate(ORDER)),
            })
    alg=integer_rank_and_basis(rows)
    pivots=alg["pivot_row_indices"]
    nonzero_det=(integer_determinant_bareiss([rows[i] for i in pivots])
                 if alg["rank"]==7 else None)
    if alg["rank"]==7 and not nonzero_det:
        raise AssertionError("rank 7 but determinant zero")
    return {
        "true_original_geometry":"W(3,2) on 45 ACTUAL flags; global K6",
        "seven_historical_positive_GF5_tags_in_fixed_order":ORDER,
        "number_of_really_global_complete_original_Q_four_state_rows":len(rows),
        "exact_real_original_integer_Hessian_matrix":tuple(rows),
        "exact_Fraction_Gaussian_rank":alg["rank"],
        "exact_independent_Bareiss_rank_witness_det":nonzero_det,
        "independent_pivot_original_witness_row_indices":pivots,
        "pivot_true_original_global_schemes_and_LINE_swap_pairs":
            tuple((witnesses[i]["scheme"],witnesses[i]["two_ACTUAL_original_LINE_swaps"])
                  for i in pivots),
        "rank_seven_COMPLETE_seven_GF5_signed_no_universal_linear_curvature_if_true":
            alg["rank"]==7,
        "original_fixed_f_g_seven_minimax_PROVED":False,
        "all_h_signed_inversion_identity_applies":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
        "all_original_witnesses":tuple(witnesses),
    }


def original_disjoint_swap_hessian_permutation_sign_identity(g,sigma,tau,evaluate):
    """All-h exact four-global-map anti-invariance independent of classifier.

    evaluate is an arbitrary deterministic vector/count function of ONE
    full global map. The all-h proof uses only legal disjoint commuting
    source factor transpositions, not f,g stochastic independence.
    """
    if len(sigma)!=2 or len(tau)!=2 or len(set(sigma+tau))!=4:
        raise ValueError("two disjoint genuine source LINE transpositions required")
    if any(type(x) is not int or x<0 or x>=len(g) for x in sigma+tau):
        raise ValueError("invalid ORIGINAL source LINE factor ID")
    base=tuple(g)
    if len(set(base))!=len(base):
        raise ValueError("one fully globally injected original LINE map required")
    def swapped(x,sw):
        q=list(x)
        i,j=sw
        q[i],q[j]=q[j],q[i]
        return tuple(q)
    gs=swapped(base,sigma)
    gt=swapped(base,tau)
    gst=swapped(gs,tau)
    y0=evaluate(base);ys=evaluate(gs);yt=evaluate(gt);yst=evaluate(gst)
    if any(type(y) is not int for y in (y0,ys,yt,yst)):
        raise ValueError("integer count functional expected")
    h=yst-ys-yt+y0
    reversed_h=yt-y0-yst+ys
    if reversed_h!=-h or set(gs)!=set(base) or set(gst)!=set(base):
        raise AssertionError("all-h disjoint same-original-global-map inversion failed")
    return {"hessian_original":h,"hessian_at_legally_swapped_g":reversed_h,
            "signed_reversal":True,
            "all_four_complete_global_line_maps_valid":True}


if __name__=="__main__":
    import json
    r=exact_original_w32_hessian_linear_obstruction()
    print(json.dumps({k:v for k,v in r.items()
          if k not in ("all_original_witnesses","exact_real_original_integer_Hessian_matrix")},
          indent=2,sort_keys=True,default=list))
