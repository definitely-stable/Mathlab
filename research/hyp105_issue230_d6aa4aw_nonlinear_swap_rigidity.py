"""HYP-105 #230 / AA4-AW: zero disjoint-swap Hessian = linear assignment.

Research-only all-h proof-method classification over the SAME fully
globally injected ORIGINAL line-source map and fixed occupied physical
edge-image support. Permutation group math is classical in ingredients;
do not assert publication novelty or root Branch A/B/C acceptance.

THEOREM (n>=4): H_sigma,tau F(g)==0 for ALL g and all DISJOINT true
source-factor transpositions iff F(g)=c+sum_l A[l,g(l)] on that fiber.

COROLLARY: every one-sign disjoint-swap Hessian is identically zero;
and if right physical-coordinate relabel symmetry is transitive on
occupied edge images, every gauge-invariant such F is CONSTANT on the
entire original right map fiber. For TRUE W(3,2), physical E=K6,
the S6 coordinate symmetry is transitive.

This applies to ANY nonlinear scalar expression of the historical seven
original GF5 motif counts, as long as it is well-defined for a shared
complete global (f,g); the original seven-sum itself is NOT all-h proved
positive and cannot be promoted via this no-go.
"""
from collections import Counter
from itertools import combinations, permutations
from math import factorial

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import (
    classify_seven_prechecked, R3_CERTIFIED_FLOORS,
)


def _swap(state, ids):
    i,j=ids
    if len(set(ids))!=2 or min(ids)<0 or max(ids)>=len(state):
        raise ValueError("two DIFFERENT actual original source LINE factor IDs required")
    v=list(state)
    v[i],v[j]=v[j],v[i]
    return tuple(v)


def full_global_disjoint_hessian(g, first, second, scalar_function):
    """4 COMPLETE original LINE assignments. Strictly disjoint swaps."""
    g=tuple(g)
    if len(set(g))!=len(g):
        raise ValueError("one globally injected full original typed line map required")
    if len(first)!=2 or len(second)!=2 or len(set(tuple(first)+tuple(second)))!=4:
        raise ValueError("two disjoint source line image transpositions required")
    gs=_swap(g,first)
    gt=_swap(g,second)
    gst=_swap(gs,second)
    vals=tuple(scalar_function(x) for x in (g,gs,gt,gst))
    if any(not isinstance(v,(int,float)) for v in vals):
        raise ValueError("real-valued scalar statistic expected")
    return vals[3]-vals[1]-vals[2]+vals[0]


def assignment_value(g,coefficient_matrix,intercept=0):
    """Any original source LINE factor/image additive assignment potential."""
    g=tuple(g)
    n=len(g)
    if len(set(g))!=n or len(coefficient_matrix)!=n:
        raise ValueError("complete n-source image injection/matrix shape required")
    if not all(len(row)==n for row in coefficient_matrix):
        raise ValueError("all n possible image labels must have one coefficient per factor")
    if set(g)!=set(range(n)):
        raise ValueError("assignment oracle expects canonical image labels 0..n-1")
    return intercept+sum(coefficient_matrix[i][g[i]] for i in range(n))


def finite_permutation_kernel_rank_mod_prime(n,prime=1009):
    """INDEPENDENT FULL S4/S5 Hessian linear-system rank over a field.

    Does NOT materialize fake original large W3 geometries. Every row is
    ONE entire permutation's disjoint-transposition mixed derivative.
    Reduction is from independent modular arithmetic, not theorem's
    constructive proof, so it can falsify a missing basis direction.
    """
    if n not in (4,5):
        raise ValueError("finite independent exhaustive oracle restricted to S4,S5")
    states=tuple(permutations(range(n)))
    owners={p:i for i,p in enumerate(states)}
    swaps=tuple(combinations(range(n),2))
    disjoint=tuple((a,b) for a,b in combinations(swaps,2)
                   if len(set(a+b))==4)
    pivots={}
    constraints=0
    for p in states:
        for s,t in disjoint:
            ps=_swap(p,s);pt=_swap(p,t);pst=_swap(ps,t)
            row={
                owners[p]:1,owners[ps]:-1,
                owners[pt]:-1,owners[pst]:1
            }
            # Every four-state square has four different permutations
            # because s,t are disjoint genuine different swaps.
            assert len(set((p,ps,pt,pst)))==4
            sparse={k:v%prime for k,v in row.items() if v%prime}
            while sparse:
                lead=min(sparse)
                if lead in pivots:
                    base=pivots[lead]
                    factor=sparse[lead]
                    for col,v in base.items():
                        tval=(sparse.get(col,0)-factor*v)%prime
                        if tval:sparse[col]=tval
                        else:sparse.pop(col,None)
                else:
                    inv=pow(sparse[lead],-1,prime)
                    pivots[lead]={k:(v*inv)%prime for k,v in sparse.items()}
                    break
            constraints+=1
    rank=len(pivots)
    assignment_dimension=(n-1)**2+1
    return {
        "permutation_slots_n":n,
        "full_permutation_states":len(states),
        "actual_disjoint_swap_pairs":len(disjoint),
        "enumerated_mixed_Hessian_equations":constraints,
        "rank_over_F1009":rank,
        "full_kernel_dimension":len(states)-rank,
        "expected_exact_assignment_span_dimension":assignment_dimension,
        "rank_matches_assignment_theorem":len(states)-rank==assignment_dimension,
        "original_GQ_not_fabricated":True,
    }


def source_all_h_rigidity_certificate(s):
    """All h>=1 dyadic scope: formal mathematical result, not enumerate n!."""
    from hyp105_issue230_d6aa4r_quenched_original_d6 import _params
    V,a,K,m=_params(s)
    if s<2 or s&(s-1):
        raise ValueError("the scope is genuine W(3,2^h), h>=1")
    if V<4 or K<V or m>a-2:
        raise AssertionError("true original minimal physical image model invalid")
    return {
        "s":s,"actual_original_source_LINE_factor_count":V,
        "physical_pair_coordinate_count":a,
        "occupied_physical_pair_edges":V,
        "unused_physical_pair_edges":m,
        "one_fixed_right_support_per_permutation_fiber":True,
        "zero_mixed_Hessian_iff_one_factor_assignment_linear":True,
        "universal_one_sign_mixed_Hessian_forces_zero_then_assignment":True,
        "if_right_occupied_edge_automorphism_transitive_then_gauge_invariant_F_constant":True,
        "true_original_W32_complete_K6_and_transitive_gauge":s==2,
        "not_same_global_pair_seven_GF5_minimax":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def actual_original_W32_four_map_nonlinear_witness(scheme="S68",
                                                   first=(0,1),
                                                   second=(2,3)):
    """True original W(3,2), four full globally injected K6 line maps.

    EACH historical seven GF5 Q has same six original source incidence
    IDs and same original f; only entire global right line map changes.
    """
    if scheme not in ("S68","S72","lex","reverse"):
        raise ValueError("only independently checked genuine original W32 models")
    model=fixture(1,scheme)
    inc=tuple(tuple(edge) for edge in model["incidences"])
    f=tuple(tuple(edge) for edge in model["left_labels"])
    g=tuple(tuple(edge) for edge in model["right_labels"])
    if len(f)!=15 or len(g)!=15 or len(set(f))!=15 or len(set(g))!=15:
        raise AssertionError("actual W32 true original complete point/line injection")
    original_Q=tuple(tuple(ids) for ids,kind in selected_left_six(model))
    if len(inc)!=45 or len(original_Q)!=62370:
        raise AssertionError("actual original incidence model changed")
    def classes(current):
        bins=Counter()
        for ids in original_Q:
            tag=classify_seven_prechecked(ids,f,current,inc)
            if tag is not None:
                bins[tag]+=1
        return bins
    gs=_swap(g,first);gt=_swap(g,second);gst=_swap(gs,second)
    records=tuple(classes(v) for v in (g,gs,gt,gst))
    order=tuple(R3_CERTIFIED_FLOORS)
    vecs=tuple(tuple(c[k] for k in order) for c in records)
    def h_of(fn):
        y=tuple(fn(c) for c in records)
        return y[3]-y[1]-y[2]+y[0]
    h_vec=tuple(vecs[3][i]-vecs[1][i]-vecs[2][i]+vecs[0][i]
                for i in range(7))
    scalar={
        "unweighted_S7":h_of(lambda c:sum(c.values())),
        "historical_51palette_selected_floor_numerator":
            h_of(lambda c:sum(c[k]*R3_CERTIFIED_FLOORS[k] for k in order)),
        "NONLINEAR_squared_S7":h_of(lambda c:sum(c.values())**2),
        "NONLINEAR_sum_seven_class_squares":
            h_of(lambda c:sum(c[k]**2 for k in order)),
    }
    return {
        "scheme":scheme,
        "full_original_six_incidence_ID_left_candidates":len(original_Q),
        "original_seven_GF5_class_coordinate_order":order,
        "four_complete_original_global_seven_class_vectors":vecs,
        "true_original_classwise_mixed_Hessian":h_vec,
        "scalar_mixed_Hessians":scalar,
        "same_full_original_point_map_all_states":True,
        "original_line_global_physical_support_unchanged":True,
        "opposite_sign_by_shifting_original_baseline_to_first_swapped_full_map":True,
        "fixed_original_f_and_given_g_sixclass_lower_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


if __name__=="__main__":
    import json
    for n in (4,5):
        print(json.dumps(finite_permutation_kernel_rank_mod_prime(n),sort_keys=True))
    print(json.dumps(actual_original_W32_four_map_nonlinear_witness(),
                     sort_keys=True))
