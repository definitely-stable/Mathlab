"""HYP-105 B3.2-E1-B1-B: exact correlated right pair-label transposition.

A W(3,2), finite-only, first-order label-exchange landscape. For any
left map fixed and right K6-pair bijection, every swap of two right
ORIGINAL factor line -> physical pair assignments is scored exactly
against all accepted seven GF5-positive original six-incidence families.
The swap delta is supported ONLY on original sixsets containing either
of the swapped right factor vertices. This elementary cancellation
identity makes full 105-neighbor exact scan tractable.

Crucial: this is NOT a full 51-pattern R3 minimizer, not an all-h
counterexample, and a better finite W32 right permutation cannot refute
a uniform asymptotic Omega(s^6) statement. Physical coordinate-symbol
relabelings are gauge and cannot improve an invariant objective.
"""
from collections import Counter
from itertools import combinations
from math import comb
import json

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1a_fixed_leading import (
    selected_left_six, validated_small_model,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, GF5_DENOM,
    classify_seven_prechecked, seven_census, exact_seven_weighted_GF5,
)

def all_h_two_right_line_influence_bound(s):
    """Proved all-label absolute one-swap seven-family influence, all h.

    In full physical K_a, c=(70,45,15) A/B/C left templates
    on six physical symbols, F_k=c_k*C(a,6). Each template uses
    exactly six ORIGINAL incidence columns, though B/C repeat pair
    labels. Let lambda=(Delta^6,C(Delta,2)Delta^4,C(Delta,2)^3).
    Complete K_a edge transitivity implies for any fixed LEFT
    physical pair e, exactly 6*F_k/K TOTAL template COLUMN
    multiplicity at e, hence a fixed ORIGINAL incidence (p,l)
    appears in at most 6*sum F_k*lambda_k/(K*Delta)
    qualifying left original sixsets (full K_a upper).
    A right factor line l has Delta incident original columns.
    By union bound two changed line factors u,v touch at most
    12*L_full/K original left sixsets, with L_full=sum F*lambda.
    Thus |S(f,g')-S(f,g)| <= floor(12*L_full/K)
    for arbitrary correlated maps and any GQ(s,s) right-label swap.
    The selected weighted GF5 MINIMUM-floor numerator changes by
    at most 51750 times that count (nonnegative per-set weight).
    This bound is Theta(s^12), too large to prove Omega(s^6).
    """
    if (not isinstance(s,int) or isinstance(s,bool)
            or s<2 or s&(s-1)):
        raise ValueError("s=2^h with h>=1 required")
    V=(s+1)*(s*s+1)
    Delta=s+1
    a=6
    while comb(a,2)<V:
        a+=1
    K=comb(a,2)
    c6=comb(a,6)
    full={"A":70*c6*Delta**6,
          "B":45*c6*comb(Delta,2)*Delta**4,
          "C":15*c6*comb(Delta,2)**3}
    L=sum(full.values())
    upper=min(L,(12*L)//K)
    return {
        "s":s,"V":V,"Delta":Delta,"a":a,"K":K,
        "full_left_A_B_C":full,
        "full_left_sixset_upper":L,
        "max_affected_sixsets_for_one_right_pair_assignment_swap":upper,
        "max_absolute_S_change":upper,
        "max_absolute_GF5_seven_floor_numerator_change":
            max(R3_CERTIFIED_FLOORS.values())*upper,
        "leading_affected_bound_over_s12":"151/12+o(1)",
        "uniform_over_all_injections":True,
        "all_h_two_sided_omega_s6_proved":False,
    }


def swap_line_pair_labels(model, line_a, line_b):
    """Swap two original right factor-vertex pair assignments, never columns."""
    _,left,right,edges_dummy = (None,None,None,None)
    left,right,edges,_=validated_small_model(model)
    if (not isinstance(line_a,int) or not isinstance(line_b,int)
            or isinstance(line_a,bool) or isinstance(line_b,bool)
            or not 0<=line_a<len(right) or not 0<=line_b<len(right)
            or line_a==line_b):
        raise ValueError("two different valid right original factor IDs required")
    other=list(right)
    other[line_a],other[line_b]=other[line_b],other[line_a]
    a=model["a"]
    supports=tuple(tuple(sorted(
        tuple(left[p])+tuple(a+c for c in other[l])
    )) for p,l in edges)
    changed=dict(model)
    changed["right_labels"]=tuple(other)
    changed["supports"]=supports
    changed["scheme"]=f'{model.get("scheme","fixed")}:rightsweep({line_a},{line_b})'
    return changed


def exact_swap_deltas(model, *, audit_full_candidates=True):
    """All 105 right factor-pair label transpositions with exact integer delta.

    Snapshot base original-sixset tags; on swapping RIGHT factor labels
    i,j, only sixsets whose original RIGHT factor list contains i or j
    can change. The rest have exactly unchanged right pair labels.
    We compute the full class-weighted necessary GF5 R3 numerator too,
    but rank swaps primarily by TOTAL seven-class sixsets S.
    """
    left,right,edges,_=validated_small_model(model)
    if len(right)!=15:
        raise ValueError("complete doily K6 right injection required")
    sixsets=tuple(ids for ids,_ in selected_left_six(model))
    if len(sixsets)!=62370 or len(set(sixsets))!=62370:
        raise AssertionError("complete E1A 62370 source changed")
    prior=tuple(classify_seven_prechecked(ids,left,right,edges)
                for ids in sixsets)
    incidence_by_line=[set() for _ in right]
    for idx,ids in enumerate(sixsets):
        for ln in set(edges[eid][1] for eid in ids):
            incidence_by_line[ln].add(idx)
    start=Counter(x for x in prior if x is not None)
    base_S=sum(start.values())
    base_weight=sum(start[k]*R3_CERTIFIED_FLOORS[k] for k in start)
    swap_bound=all_h_two_right_line_influence_bound(2)
    swaps=[]
    labels=list(right)
    for i,j in combinations(range(len(right)),2):
        touched=sorted(incidence_by_line[i]|incidence_by_line[j])
        labels[i],labels[j]=labels[j],labels[i]
        old=Counter()
        new=Counter()
        for index in touched:
            before=prior[index]
            after=classify_seven_prechecked(sixsets[index],left,labels,edges)
            if before is not None:
                old[before]+=1
            if after is not None:
                new[after]+=1
        labels[i],labels[j]=labels[j],labels[i]
        deltaS=sum(new.values())-sum(old.values())
        deltaGF5=sum((new[k]-old[k])*w for k,w in R3_CERTIFIED_FLOORS.items())
        if (abs(deltaS)>swap_bound["max_absolute_S_change"] or
                abs(deltaGF5)>
                swap_bound["max_absolute_GF5_seven_floor_numerator_change"]):
            raise AssertionError("proved all-h one-swap influence bound violated")
        swaps.append({
            "swap":(i,j),"affected_sixsets":len(touched),
            "new_S":base_S+deltaS,
            "new_GF5_R3_floor_numerator":base_weight+deltaGF5,
            "delta_S":deltaS,
            "delta_GF5_floor_numerator":deltaGF5,
        })
    if len(swaps)!=105:
        raise AssertionError("not all two right-label transpositions tested")
    baseline=seven_census(model,independent_checks=False)
    if (baseline["S_seven"]!=base_S or
            baseline["GF5_seven_lower_numerator"]!=base_weight):
        raise AssertionError("incremental baseline disagrees with exact oracle")
    if audit_full_candidates:
        best=min(swaps,key=lambda d: (
            d["new_S"],d["new_GF5_R3_floor_numerator"],d["swap"]))
        proposed=swap_line_pair_labels(model,*best["swap"])
        verified=seven_census(proposed,independent_checks=True)
        if (verified["S_seven"]!=best["new_S"] or
                verified["GF5_seven_lower_numerator"]!=
                best["new_GF5_R3_floor_numerator"]):
            raise AssertionError("incremental best delta differs from full seven oracle")
        independent={
            "best_swap":best["swap"],
            "full_recount_S":verified["S_seven"],
            "full_recount_GF5_floor_numerator":
                verified["GF5_seven_lower_numerator"],
            "full_recount_Q4":verified["Q4"],
        }
    else:
        independent=None
    return {
        "base_S":base_S,
        "base_GF5_R3_floor_numerator":base_weight,
        "base_class_counts":dict(start),
        "candidate_left_sixsets":len(sixsets),
        "universal_all_h_single_swap_influence":swap_bound,
        "all_105_swaps":swaps,
        "best":min(swaps,key=lambda d:(
            d["new_S"],d["new_GF5_R3_floor_numerator"],d["swap"])),
        "exact_independent_best_verification":independent,
        "each_swap_exact":True,
        "full_R3_minimization":False,
        "universal_asymptotic_counterexample":False,
    }


def report():
    model=pair_labeled_symplectic(1,"reverse-line")
    landscape=exact_swap_deltas(model)
    best=landscape["best"]
    changed=swap_line_pair_labels(model,*best["swap"])
    full=seven_census(changed,independent_checks=True)
    weighted=exact_seven_weighted_GF5(changed,max_signed_events=5000)
    if weighted["seven_class_original_sixsets"]!=full["S_seven"]:
        raise AssertionError("selected exact GF5 event count mismatch")
    return {
        "scope":"W(3,2) finite all-105 right factor-label swap landscape",
        "initial_S":landscape["base_S"],
        "initial_GF5_minimum_numerator":
            landscape["base_GF5_R3_floor_numerator"],
        "best_swap":best["swap"],
        "new_S":best["new_S"],
        "new_GF5_minimum_numerator":best["new_GF5_R3_floor_numerator"],
        "new_Q4":full["Q4"],
        "new_seven_class_counts":full["seven_class_motif_counts"],
        "new_exact_selected_10sign_GF5_R3_numerator":
            weighted["exact_selected_GF5_R3_numerator"],
        "new_exact_selected_10sign_GF5_R3_denominator":GF5_DENOM,
        "tested_swaps":len(landscape["all_105_swaps"]),
        "best_independent_full_six_census":True,
        "one_swap_local_optimum_certified":False,
        "full_R3_certified":False,
        "all_h_obstruction_refuted":False,
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
