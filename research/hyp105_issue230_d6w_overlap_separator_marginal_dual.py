"""HYP-105 issue #230 D6-W: exact overlap-separator marginal dual.

ALL-h SOUND SUFFICIENT dual (given complete truthful ORIGINAL sixset tables):
reparameterize nonnegative local factors F_c on typed ORIGINAL point/line
physical labels by finite signed integer separator functions h_(c,S),
|S|<=2, whose sum over factors sharing the EXACT SAME typed separator
is identically zero on every locally injective assignment. Then
    sum F_c(f,g) = sum G_c(f,g) >= sum_c min G_c
for EVERY pair of complete globally injective f and g. Signed shifted
factors are allowed. No independence between f,g or original Q factors.

This is a restricted feasible dual of overlap-consistent local marginal
relaxation. It proves no positive all-h root lower unless such messages
are explicitly constructed for all original Q and verified.

Finite true ORIGINAL W(3,2): f and 12 right lines FROZEN, only 3
ORIGINAL right factors permute the SAME 3 occupied physical pairs.
Add a zero-cost full-three-site anchor factor; pair separator (0,1)
uniquely determines the third edge in a 3-to-3 bijection. Transfer
all seven-GF5 incidence-position-aware cylinder group costs to that
anchor using separators of size 0,1,2. Exact rational/integer dual
equals the min of all six complete global right-triple permutations.
This is NOT an ALL-f,g or all-h lower and the full-three anchor does
NOT imply a generic 2-site Sherali-Adams exactness result.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product
import json

from hyp105_issue230_d6v_coupled_star_cluster import (
    _validate_exact_factors, coupled_partition_certificate,
)
from hyp105_issue230_d6t_assignment_dual_certificate import (
    complete_true_original_W32_three_factor_tables, local_factor_objective,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census


def _scope(factor):
    return tuple(("L",z) for z in factor["L"])+tuple(("R",z) for z in factor["R"])


def _canonical_separator(sep, nL, nR):
    if not isinstance(sep, (tuple,list)):
        raise ValueError("typed ORIGINAL separator must be ordered")
    sep=tuple(sep)
    if (any(not isinstance(s,(tuple,list)) or len(s)!=2
            or s[0] not in ("L","R")
            or type(s[1]) is not int
            or not 0<=s[1]<(nL if s[0]=="L" else nR)
            for s in sep)):
        raise ValueError("invalid typed ORIGINAL separator site")
    canonical=tuple(sorted(sep,key=lambda s:(s[0]!="L",s[1])))
    if len(set(map(tuple,sep)))!=len(sep) or tuple(map(tuple,sep))!=canonical:
        raise ValueError("separator must be distinct, canonical L/R ordered")
    return canonical


def _separator_domain(sep,mL,mR):
    kL=sum(tag=="L" for tag,_ in sep)
    kR=len(sep)-kL
    return tuple(a+b for a,b in product(
        permutations(range(mL),kL),permutations(range(mR),kR)))


def _projection(local_scope,local_row,separator):
    L,R=local_scope
    la,ra=local_row
    images={("L",v):la[j] for j,v in enumerate(L)}
    images.update({("R",v):ra[j] for j,v in enumerate(R)})
    return tuple(images[v] for v in separator)


def verified_separator_reparam_dual(factors,nL,mL,nR,mR,messages,
                                    *,max_separator_size=2,
                                    max_truth_rows=50000):
    """Exact integer dual with fail-closed row coverage and cancellation.

    Message = {'factor':int, 'separator':(('L',id),('R',id),...),
               'values':{physical-image-tuple: signed exact int}}.
    A signed shift is ADDED to its factor. Conservation is checked for
    EVERY possible separator assignment, including the empty tuple.
    No solver optimality claim: returns the lower bound of THESE messages.
    """
    rows=_validate_exact_factors(factors,nL,mL,nR,mR,
                                 max_rows=max_truth_rows)
    if type(max_separator_size) is not int or not 0<=max_separator_size<=2:
        raise ValueError("separator rank must be 0..2")
    if not isinstance(messages,(list,tuple)) or len(messages)>200:
        raise ValueError("bounded list of explicit signed dual messages required")
    shifts=[[] for _ in factors]
    balances=defaultdict(int)
    count=0
    for msg in messages:
        if not isinstance(msg,dict) or set(msg)!={"factor","separator","values"}:
            raise ValueError("message requires exactly factor/separator/values")
        idx=msg["factor"]
        if type(idx) is not int or not 0<=idx<len(factors):
            raise ValueError("unknown original local factor index")
        sep=_canonical_separator(msg["separator"],nL,nR)
        if len(sep)>max_separator_size or not set(sep)<=set(_scope(factors[idx])):
            raise ValueError("separator not contained in ORIGINAL factor scope")
        domain=_separator_domain(sep,mL,mR)
        values=msg["values"]
        if (not isinstance(values,dict) or set(values)!=set(domain)
                or any(type(v) is not int for v in values.values())):
            raise ValueError("message must specify EVERY legal image tuple as signed int")
        for key in domain:
            balances[(sep,key)]+=values[key]
        shifts[idx].append((sep,values))
        count+=len(domain)
    if any(v!=0 for v in balances.values()):
        raise ValueError("separator marginal messages fail exact pointwise cancellation")
    minima=[]
    argmins=[]
    for i,factor in enumerate(factors):
        best=None
        chosen=None
        for row,cost in factor["costs"].items():
            shifted=cost+sum(vals[_projection((factor["L"],factor["R"]),row,sep)]
                             for sep,vals in shifts[i])
            if best is None or shifted<best:
                best,chosen=shifted,row
        if best is None:
            raise AssertionError("validated factor lacks full truth table")
        minima.append(best)
        argmins.append(chosen)
    return {
        "theorem":"ALL-H-SOUND-OVERLAP-CONSISTENT-TYPED-SEPARATOR-DUAL",
        "factor_count":len(factors),
        "truth_rows_verified":rows,
        "signed_message_rows_verified":count,
        "signed_messages_verified":len(messages),
        "separator_rank":max((len(m["separator"]) for m in messages),default=0),
        "all_separators_cancel_identically":True,
        "globally_injective_two_typed_sides":"RESTRICTION-TO-COMPLETE-LOCAL-TABLES",
        "shifted_factor_minima":minima,
        "exact_integer_lower":sum(minima),
        "exact_integer_argmin_rows":argmins,
        "global_root_positive_PROVED_A":False,
    }


def check_local_marginal_consistency(factors,nL,mL,nR,mR,
                                     distributions,rank):
    """Exact finite *primal* marginal falsifier, not an optimized LP.

    Full factors may have different distributions; they must agree on
    EVERY shared typed ORIGINAL separator of size <=rank, including
    per-side local injection. Results are exact Fractions.
    """
    _validate_exact_factors(factors,nL,mL,nR,mR)
    if type(rank) is not int or not 1<=rank<=2:
        raise ValueError("marginal rank must be 1 or 2")
    if not isinstance(distributions,(list,tuple)) or len(distributions)!=len(factors):
        raise ValueError("one complete probability table per local factor")
    mass=[]
    for factor,distribution in zip(factors,distributions):
        if not isinstance(distribution,dict) or set(distribution)!=set(factor["costs"]):
            raise ValueError("probability table must contain every local injection")
        if any(type(v) not in (int,Fraction) or v<0
               for v in distribution.values()):
            raise ValueError("exact nonnegative integer/Fraction probabilities only")
        row={a:Fraction(v) for a,v in distribution.items()}
        if sum(row.values())!=1:
            raise ValueError("every local marginal distribution must sum to one")
        mass.append(row)
    inspected=0
    for i in range(len(factors)):
        for j in range(i+1,len(factors)):
            common=tuple(v for v in _scope(factors[i])
                         if v in set(_scope(factors[j])))
            for level in range(1,min(rank,len(common))+1):
                for sep in combinations(common,level):
                    counts=[]
                    for idx in (i,j):
                        d=defaultdict(Fraction)
                        for row,pr in mass[idx].items():
                            d[_projection((factors[idx]["L"],factors[idx]["R"]),
                                          row,sep)]+=pr
                        counts.append(d)
                    if counts[0]!=counts[1]:
                        return {
                            "consistent":False,
                            "rank":rank,
                            "first_conflict_factor_pair":[i,j],
                            "first_conflict_typed_separator":[list(z) for z in sep],
                            "separators_verified_before_conflict":inspected,
                        }
                    inspected+=1
    return {
        "consistent":True,"rank":rank,
        "separators_verified":inspected,
        "objective_expectation":str(sum(
            Fraction(cost)*p for factor,dist in zip(factors,mass)
            for row,cost in factor["costs"].items() for p in (dist[row],))),
    }


def saturated_triple_anchor_certificate(factors):
    """Exact 3-to-3 right injection conditional certificate, rank <=2.

    Original (already renumbered to 0,1,2) factors may have any subset
    U of right sites and NO left sites. Add a ZERO-COST 3-site region.
    Pair (R0,R1) uniquely determines R2, so every original cost
    transfers by messages on U (if |U|<=2) or (R0,R1) (if |U|=3).
    Full original 3-site tables and all injected rows are preserved.
    """
    if not isinstance(factors,(tuple,list)) or not factors:
        raise ValueError("at least one locally supported factor")
    _validate_exact_factors(factors,0,0,3,3)
    if any(f["L"] or not set(f["R"]) <= {0,1,2} for f in factors):
        raise ValueError("finite rank-two anchor is right-only saturated triple")
    anchor={"L":(),"R":(0,1,2),
            "costs":{((),p):0 for p in permutations(range(3))}}
    augmented=list(factors)+[anchor]
    anchor_idx=len(factors)
    messages=[]
    for i,f in enumerate(factors):
        original=tuple(f["R"])
        selected=original if len(original)<=2 else (0,1)
        separator=tuple(("R",v) for v in selected)
        rows={}
        for pin in permutations(range(3),len(selected)):
            mapping=dict(zip(selected,pin))
            if len(original)==3:
                # Exactly ONE remaining physical label among E=(0,1,2).
                other=tuple(set((0,1,2))-set(pin))
                if len(other)!=1:
                    raise AssertionError("3-to-3 saturated injection uniqueness false")
                mapping[2]=other[0]
            key=((),tuple(mapping[t] for t in original))
            if key not in f["costs"]:
                raise AssertionError("ORIGINAL cylinder lookup missing")
            rows[pin]=f["costs"][key]
        messages.append({"factor":i,"separator":separator,
                         "values":{k:-v for k,v in rows.items()}})
        messages.append({"factor":anchor_idx,"separator":separator,
                         "values":dict(rows)})
    dual=verified_separator_reparam_dual(
        augmented,0,0,3,3,messages,max_separator_size=2)
    exact=min(sum(f["costs"][((),tuple(p[t] for t in f["R"]))]
                  for f in factors) for p in permutations(range(3)))
    if dual["exact_integer_lower"]!=exact:
        raise AssertionError("separator-to-zero-anchor transfer did not close finite primal")
    if dual["shifted_factor_minima"][:-1]!=[0]*len(factors):
        raise AssertionError("not every ORIGINAL conditioned factor shifted to zero")
    dual["exact_six_permutation_primal_min"]=exact
    dual["zero_cost_full_three_site_anchor_explicit"]=True
    dual["anchor_covers_entire_conditional_original_triple"]=True
    dual["general_rank_two_Sherali_Adams_exactness_claim"]=False
    dual["true_global_original_f_g_root"]="NOT-COMPUTED"
    return dual,messages,augmented


def frozen_true_original_W32_report():
    rows=[]
    for scheme,T in (("S68",(3,11,12)),("S72",(1,7,9))):
        model=fixture(1,scheme)
        triple,labels,images,compiled,fs,fw=(
            complete_true_original_W32_three_factor_tables(model,T))
        assert compiled["original_left_sixsets"]==62370
        original=seven_census(model,independent_checks=False)
        results={}
        for name,source,expect in (
            ("S_seven",fs,original["S_seven"]),
            ("GF5_selected_numerator",fw,original["GF5_seven_lower_numerator"])):
            # ORIGINAL line IDs stay in the input and source census.
            # Only the tiny local solver axes are mapped to 0,1,2.
            indexed=[{**f,"R":tuple(triple.index(v) for v in f["R"])}
                     for f in source]
            cert,msg,aug=saturated_triple_anchor_certificate(indexed)
            baseline=local_factor_objective(source,triple,(0,1,2))
            if baseline!=expect:
                raise AssertionError("independent true-ORIGINAL source census drift")
            partition=coupled_partition_certificate(
                indexed,0,0,3,3,max_cluster_size=3)
            if cert["exact_integer_lower"] < partition["exact_coupled_cluster_lower"]:
                raise AssertionError("exact separator anchor weaker than 3-factor certificate")
            results[name]={
                "source_true_ORIGINAL_baseline":baseline,
                "global_conditional_exact_primal":cert["exact_six_permutation_primal_min"],
                "verified_pair_separator_integer_dual":cert["exact_integer_lower"],
                "D6V_max_three_factor_cluster_lower":partition["exact_coupled_cluster_lower"],
                "gap_closed_beyond_D6V":cert["exact_integer_lower"]-partition["exact_coupled_cluster_lower"],
                "separator_rank":cert["separator_rank"],
                "source_original_factor_groups":len(source),
                "signed_messages_verified":cert["signed_messages_verified"],
                "zero_cost_full_three_site_anchor_explicit":True,
                "globally_injective_source_left_and_right":True,
                "frozen_left_and_other_twelve_right_originals":True,
            }
        rows.append({
            "scheme":scheme,"original_right_triple":list(triple),
            "true_original_left_sixsets":compiled["original_left_sixsets"],
            "right_permutations_exhaustive":6,
            "objectives":results,
        })
    return rows


def report():
    return {
        "slice":"HYP105-ISSUE230-D6W-OVERLAP-SEPARATOR-MARGINAL-DUAL",
        "all_h_verified_sound_if_complete_ORIGINAL_truth_tables":
            "EXACT-SIGNED-TYPED-SEPARATOR-DUAL",
        "all_h_root_complete_truth_tables":"NOT-ENUMERATED",
        "finite_W32_only_saturated_triple_pair_separator_rank":2,
        "full_three_site_zero_cost_anchor":"EXPLICIT-REQUIRED",
        "generic_Sherali_Adams_rank_two_exactness":False,
        "original_global_min_PROVED_A":False,
        "infinite_counterexample_PROVED_B":False,
        "Branch_A":"OPEN","Branch_B":"OPEN",
        "W32_conditioned":frozen_true_original_W32_report(),
    }


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True))
