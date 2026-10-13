"""HYP-105 #230 D6-V: coupled ORIGINAL sixset star NO-GO and exact cluster dual.

ALL h>=1 theorem:
For any collection C of distinct six-incidence ORIGINAL GQ W(3,2^h)
subsets, if the union of ORIGINAL POINT factors or the union of ORIGINAL
LINE factors has cardinality <=a-1, where K_a is the physical pair
alphabet, there exist simultaneously globally injective left and right
assignments for which ALL members of C have ZERO accepted seven-GF5
positive contribution, both unweighted and selected nonnegative weights.

The construction assigns every original factor of the small-union side
a distinct pair (0,k) from the physical star K_(1,a-1) and extends to a
full typed injection; coordinate 0 then occurs SIX times in every sixset
on that side. In particular every collection of at most floor((a-1)/6)
sixsets has zero joint minimum, with cluster-size obstruction
Omega(s^(3/2)) since a=(sqrt(2)+o(1))s^(3/2).

Also provide an exact coupled-cluster certificate for independent full
nonnegative truth tables: disjoint covers by blocks of up to k FACTORS;
sum of block minima is a valid global lower bound. The finite ORIGINAL
W32 application is conditioned on fixed f and 12 right originals and
uses D6-T's exact complete incidence-position-aware right cylinders.
It NEVER proves Branch A/B or full GF5 R3 bounds.
"""
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb
import json

from hyp105_issue230_proof_audit import parameters
from hyp105_issue230_d6u_proper_scope_nogo import (
    original_sixset_forest_scope, physical_two_regular,
)
from hyp105_issue230_d6t_assignment_dual_certificate import (
    complete_true_original_W32_three_factor_tables, local_factor_objective,
)
from hyp105_issue230_projection import fixture


def star_zero_family(s, original_sixsets):
    """Exact globally injective original maps zeroing a family of sixsets.

    Inputs MUST be bona fide original W(3,s) incidences, verified against
    the true geometry by the caller. The local forest oracle checks
    distinctness, typed-factor scope and forbidden short cycles.
    Full ORIGINAL typed injections are emitted for independent checking.
    """
    par = parameters(s)
    V, a, K = par["V"], par["a"], par["K"]
    if not isinstance(original_sixsets, (list, tuple)) or not original_sixsets:
        raise ValueError("nonempty ORIGINAL six-incidence family required")
    family = []
    points, lines = set(), set()
    for q in original_sixsets:
        if not isinstance(q, (tuple, list)):
            raise ValueError("six ORIGINAL incidence positions required")
        q = tuple(tuple(x) for x in q)
        L, R = original_sixset_forest_scope(q)
        if any(x >= V for x in L) or any(y >= V for y in R):
            raise ValueError("ORIGINAL GQ factor out of range")
        family.append(q)
        points.update(L)
        lines.update(R)
    if len(points) > a - 1 and len(lines) > a - 1:
        raise ValueError("star certificate unavailable: both factor unions exceed a-1")
    side = "left" if len(points) <= a - 1 else "right"
    side_union = sorted(points if side == "left" else lines)
    all_pairs = tuple(combinations(range(a), 2))
    if len(all_pairs) != K or K < V:
        raise AssertionError("physical pair alphabet incomplete")
    star_pairs = tuple((0, j) for j in range(1, a))
    assigned = dict(zip(side_union, star_pairs))
    used = set(assigned.values())
    remainder = (e for e in all_pairs if e not in used)
    target = []
    for i in range(V):
        target.append(assigned[i] if i in assigned else next(remainder))
    other = tuple(all_pairs[:V])
    f, g = (tuple(target), other) if side == "left" else (other, tuple(target))
    if len(set(f)) != V or len(set(g)) != V:
        raise AssertionError("global two-sided injection violated")
    for q in family:
        P = tuple(p for p, _ in q)
        R = tuple(r for _, r in q)
        if physical_two_regular(P, f) and physical_two_regular(R, g):
            raise AssertionError("ORIGINAL Q positive GF5 still possible")
        failed = P if side == "left" else R
        labels = f if side == "left" else g
        deg_zero = sum(0 in labels[v] for v in failed)
        if deg_zero != 6:
            raise AssertionError("star must have six appearances of center 0")
    return {
        "s": s, "a": a, "V": V, "K": K, "star_side": side,
        "original_sixsets_count": len(family),
        "union_original_points": len(points),
        "union_original_lines": len(lines),
        "star_distinct_original_sites": len(side_union),
        "all_seven_GF5_contributions_zero": True,
        "selected_nonnegative_GF5_numerator_zero": True,
        "complete_left_injection": f,
        "complete_right_injection": g,
    }


def _injection_tuples(m, r):
    return tuple(permutations(range(m), r))


def _validate_exact_factors(factors, nL, mL, nR, mR, *, max_rows=50000):
    if any(type(x) is not int or x < 0 for x in (nL, mL, nR, mR)):
        raise ValueError("nonnegative integer variable and image sizes required")
    if mL < nL or mR < nR:
        raise ValueError("cannot inject more original sites than physical images")
    if not isinstance(factors, (tuple, list)) or not factors or len(factors)>12:
        raise ValueError("1..12 complete ORIGINAL factor tables required")
    budget=0
    for factor in factors:
        if not isinstance(factor, dict) or set(factor)!={"L","R","costs"}:
            raise ValueError("exact factor needs L/R/costs")
        L,R=factor["L"],factor["R"]
        if (not isinstance(L,(tuple,list)) or not isinstance(R,(tuple,list))
                or any(type(x) is not int or not 0<=x<nL for x in L)
                or any(type(x) is not int or not 0<=x<nR for x in R)
                or len(set(L))!=len(L) or len(set(R))!=len(R)
                or len(L)>6 or len(R)>6 or len(L)+len(R)>12):
            raise ValueError("invalid typed ORIGINAL factor scope")
        domain={(x,y) for x in _injection_tuples(mL,len(L))
                        for y in _injection_tuples(mR,len(R))}
        budget+=len(domain)
        if budget>max_rows:
            raise ValueError("complete coupled-factor domain budget exceeded")
        costs=factor["costs"]
        if (not isinstance(costs,dict) or set(costs)!=domain
                or any(type(v) is not int or v<0 for v in costs.values())):
            raise ValueError("missing, extra, non-injective, negative or noninteger row")
    return budget


def exact_cluster_min(factors, indices, mL, mR, *, max_states=50000):
    """Minimum of SUM of factors on their common ORIGINAL variable union.

    Every locally injective union tuple is jointly extendible to global
    two-sided injections if each side's physical alphabet is >=V.
    """
    if not indices or len(set(indices))!=len(indices):
        raise ValueError("nonempty distinct cluster factor indices required")
    if any(type(i) is not int or not 0<=i<len(factors) for i in indices):
        raise ValueError("unknown cluster factor")
    L=tuple(sorted({v for i in indices for v in factors[i]["L"]}))
    R=tuple(sorted({v for i in indices for v in factors[i]["R"]}))
    states=1
    for m,k in ((mL,len(L)),(mR,len(R))):
        if m<k:
            raise ValueError("not enough images for union scope")
        states*=comb(m,k)*__import__("math").factorial(k)
    if states>max_states:
        raise ValueError("joint cluster truth table state budget exceeded")
    best=None
    argmin=None
    for la,ra in product(_injection_tuples(mL,len(L)), _injection_tuples(mR,len(R))):
        left=dict(zip(L,la))
        right=dict(zip(R,ra))
        val=sum(factors[i]["costs"][(
            tuple(left[t] for t in factors[i]["L"]),
            tuple(right[t] for t in factors[i]["R"]))] for i in indices)
        if best is None or val<best:
            best=val
            argmin=(la,ra)
    if best is None:
        raise AssertionError("cluster has no injective assignment")
    return best, (L, R, argmin)


def coupled_partition_certificate(factors, nL, mL, nR, mR, *,
                                  max_cluster_size=2, max_rows=50000):
    """Verified monotone nonnegative block-minimum cover lower certificate.

    All local tables FULLY validated and factor indices partitioned.
    The partition minimizes no costs independently per Q; it minimizes
    each CLUSTER joint cost, and maximizes the sum over partitions.
    This is a restricted exact packing bound, NOT Sherali-Adams.
    """
    totalrows=_validate_exact_factors(
        factors,nL,mL,nR,mR,max_rows=max_rows)
    if (type(max_cluster_size) is not int or
            not 1<=max_cluster_size<=min(4,len(factors))):
        raise ValueError("cluster size must be 1..min(4, factor count)")
    n=len(factors)
    @lru_cache(None)
    def block(tup):
        return exact_cluster_min(factors,tup,mL,mR)[0]
    @lru_cache(None)
    def optimum(mask):
        if not mask:
            return 0,()
        pivot=(mask & -mask).bit_length()-1
        remaining=[j for j in range(pivot+1,n) if mask & (1<<j)]
        chosen=None
        for k in range(min(max_cluster_size-1,len(remaining))+1):
            for others in combinations(remaining,k):
                group=(pivot,)+others
                used=sum(1<<j for j in group)
                rest,path=optimum(mask^used)
                candidate=(block(group)+rest,(group,)+path)
                if chosen is None or candidate[0]>chosen[0]:
                    chosen=candidate
        return chosen
    lower,partition=optimum((1<<n)-1)
    if sorted(i for c in partition for i in c)!=list(range(n)):
        raise AssertionError("not a disjoint original-factor partition")
    independent=sum(block((i,)) for i in range(n))
    if lower<independent:
        raise AssertionError("coupling weaker than singleton partition")
    return {
        "complete_truth_rows_verified":totalrows,
        "factors_verified":n,
        "maximum_factors_per_joint_cluster":max_cluster_size,
        "exact_singleton_minima_sum":independent,
        "exact_coupled_cluster_lower":lower,
        "strict_gain_over_singletons":lower-independent,
        "partition":[list(c) for c in partition],
        "local_cluster_joint_minima":[block(c) for c in partition],
        "scope":"EXACT_NONNEGATIVE_FINITE_CLUSTER_PARTITION_BOUND",
        "general_Sherali_Adams_claim":False,
    }


def frozen_original_W32_coupling_report():
    result=[]
    for scheme,T in (("S68",(3,11,12)),("S72",(1,7,9))):
        model=fixture(1,scheme)
        triple,labels,images,compiled,S,Y=(
            complete_true_original_W32_three_factor_tables(model,T))
        if compiled["original_left_sixsets"]!=62370:
            raise AssertionError("not the full ORIGINAL W32 left-selected sixset census")
        cells={}
        for objective,fs in (("S_seven",S),("GF5_selected_numerator",Y)):
            lows={}
            for order in (1,2,3):
                lows[order]=coupled_partition_certificate(
                    fs,0,0,len(triple),3,max_cluster_size=order)
            full=min(local_factor_objective(fs,triple,phi)
                     for phi in permutations(range(3)))
            if (not lows[1]["exact_coupled_cluster_lower"] <=
                    lows[2]["exact_coupled_cluster_lower"] <=
                    lows[3]["exact_coupled_cluster_lower"] <= full):
                raise AssertionError("monotonic jointly certified cluster lower violated")
            cells[objective]={
                "exact_full_three_permutation_min":full,
                "orders":{str(k):v for k,v in lows.items()},
                "all_right_outside_triple_frozen":True,
            }
        if cells["S_seven"]["exact_full_three_permutation_min"]!=68:
            raise AssertionError("frozen REAL W32 seven-S suborbit min drift")
        result.append({
            "scheme":scheme,"original_right_triple":list(triple),
            "true_original_left_sixsets":compiled["original_left_sixsets"],
            "right_permutations":6,"objectives":cells,
        })
    return result


def report():
    p=[]
    for h in range(1,7):
        x=parameters(2**h)
        p.append({"s":x["s"],"a":x["a"],"V":x["V"],
                  "guaranteed_zero_cluster_max_sixsets":(x["a"]-1)//6,
                  "first_unruled_out_cluster_size":(x["a"]-1)//6+1})
    return {
        "slice":"HYP105-ISSUE230-D6V-COUPLED-STAR-CLUSTER-BOUND",
        "theorem":"ALL-H-STAR-ZERO-FOR-SMALL-UNIONS-BOTH-SIDES",
        "all_h_any_t_le_floor_a_minus_one_over_six_joint_min":"ZERO",
        "unconditional_local_block_size_required_asymptotic":"OMEGA(s^(3/2))",
        "method_NO_GO":"UNCONDITIONED-INDEPENDENT-CLUSTER-MINIMA-WITH-BOUNDED-SIXSET-BLOCKS",
        "actual_global_min_positive_proved":False,
        "general_Sherali_Adams_no_go":False,
        "Branch_A":"OPEN","Branch_B":"OPEN",
        "parameters":p,
        "W32_conditioned":frozen_original_W32_coupling_report(),
    }


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True))
