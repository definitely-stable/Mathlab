"""HYP-105 #230 D6-AA4-B: shared-factor coherent completion-fiber certificate.

Exact all-h conditional fiber theorem: freeze f and all right original line
labels outside a block B. Permute/reinject ONE COMMON physical assignment on B
across EVERY distinct-original-incidence sixset, respecting global capacity.
min(sum_Q w_Q) >= sum_Q min(w_Q), possibly strictly.
The W(3,2) executable fixes four original lines and enumerates all 4!=24
complete, genuine, globally injective right pair maps in that fiber.
No all-h unconditioned obstruction or full R3 is asserted.
"""
from collections import Counter, defaultdict
from itertools import permutations
from math import factorial

from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS
from hyp105_g5e2b3e1a_fixed_leading import validated_small_model
from hyp105_issue230_d6p_seven_cylinder_swap_audit import (
    compile_original_W32_cylinders, cylinder_seven_class,
    cylinder_census,
)

SEVEN=tuple(R3_CERTIFIED_FLOORS)


def validate_block(labels, block, *, size=4):
    if len(block)!=size or len(set(block))!=size or any(
        type(v) is not int or not 0<=v<len(labels) for v in block
    ):
        raise ValueError("exact distinct original line block required")
    if len(set(labels))!=len(labels):
        raise ValueError("g must globally inject original right lines")
    return tuple(sorted(block))


def assign_block(labels, block, ordered_edges):
    """One shared globally injective completion, never per-Q assignments."""
    block=validate_block(labels,block,size=len(block))
    if len(ordered_edges)!=len(block):
        raise ValueError("incomplete right injection fiber assignment")
    frozen={labels[i] for i in range(len(labels)) if i not in block}
    if len(set(ordered_edges))!=len(block) or any(e in frozen for e in ordered_edges):
        raise ValueError("global injection / occupied physical column violated")
    current=list(labels)
    for original_line,edge in zip(block,ordered_edges):
        current[original_line]=edge
    if len(set(current))!=len(current):
        raise AssertionError("global right pair capacity broken")
    return tuple(current)


def coherent_fiber(compiled, labels, block):
    """Exactly all b! completions in the fixed-image W32 fiber.

    Only genuine W32: V=K=15, all K6 physical pairs are occupied.
    No lookup in the historical original-sixset classifier is made.
    A class is attributed once per ORIGINAL sixset, never per signed event.
    """
    labels=tuple(tuple(x) for x in labels)
    block=validate_block(labels,block)
    if len(labels)!=15 or len(set(labels))!=15 or compiled["a"]!=6:
        raise ValueError("W32 complete K6 bijection fiber only")
    if compiled["original_lines"]!=15 or compiled["original_left_sixsets"]!=62370:
        raise ValueError("complete original W32 cylinder oracle required")
    edges=tuple(labels[i] for i in block)
    orders=tuple(permutations(edges))
    if len(orders)!=factorial(len(block)) or orders[0]!=edges:
        raise AssertionError("incomplete canonical right injection fiber")
    fiber_labels=tuple(assign_block(labels,block,p) for p in orders)
    if any(set(y)!=set(labels) for y in fiber_labels):
        raise AssertionError("physical image must stay fixed on W32")

    fixed=Counter()
    variable=[]
    count_affected=0
    for sig,m in compiled["cylinders"].items():
        if set(sig[1]).isdisjoint(block):
            tag=cylinder_seven_class(sig,labels)
            if tag is not None:
                fixed[tag]+=m
        else:
            count_affected+=m
            states=tuple(cylinder_seven_class(sig,y) for y in fiber_labels)
            variable.append((sig,m,states))
    if count_affected<=0 or count_affected>=compiled["original_left_sixsets"]:
        raise AssertionError("expected nontrivial original line fiber boundary")

    affected=[Counter() for _ in orders]
    independent_local_min_count=0
    independent_local_min_weight=0
    forced_individual_cylinders=0
    weighted_multiplicity=0
    masks=[]
    for sig,m,states in variable:
        vals=tuple(int(tag is not None) for tag in states)
        wvals=tuple(R3_CERTIFIED_FLOORS.get(tag,0) for tag in states)
        independent_local_min_count+=m*min(vals)
        independent_local_min_weight+=m*min(wvals)
        forced_individual_cylinders+=int(all(vals))
        weighted_multiplicity+=m
        mask=sum((1<<i) for i,positive in enumerate(vals) if positive)
        if mask:
            masks.append((mask,sig,m))
        for i,tag in enumerate(states):
            if tag is not None:
                affected[i][tag]+=m

    full=[]
    for order,c in zip(orders,affected):
        total=fixed+c
        full.append({
            "physical_original_line_image":tuple(tuple(x) for x in order),
            "S_seven":sum(total.values()),
            "GF5_floor_numerator":sum(total[k]*w for k,w in R3_CERTIFIED_FLOORS.items()),
            "affected_S":sum(c.values()),
            "affected_GF5_floor_numerator":sum(c[k]*w for k,w in R3_CERTIFIED_FLOORS.items()),
            "by_class":{name:total[name] for name in SEVEN},
        })
    base=cylinder_census(compiled,labels)
    if full[0]["S_seven"]!=base["S_seven"] or full[0]["GF5_floor_numerator"]!=base["GF5_seven_lower_numerator"]:
        raise AssertionError("frozen ORIGINAL cylinder baseline drift")

    minimum_aff_count=min(row["affected_S"] for row in full)
    minimum_aff_weight=min(row["affected_GF5_floor_numerator"] for row in full)
    gap=minimum_aff_count-independent_local_min_count
    wgap=minimum_aff_weight-independent_local_min_weight
    if min(gap,wgap)<0:
        raise AssertionError("coherent block completion cannot beat independent minima")

    # Greedy exact set-cover certificate for the statement that every one
    # of the 24 globally legal completions forces at least one POSITIVE Q
    # incident to this block. It is NOT an optimal/minimum-cardinality cover.
    remaining=(1<<len(orders))-1
    picked=[]
    available=masks.copy()
    while remaining and available:
        chosen=max(available,key=lambda row:(
            (row[0]&remaining).bit_count(),row[2],
            tuple(-v for v in row[1][1])))
        coverage=chosen[0]&remaining
        if not coverage:
            break
        picked.append({"sixset_right_cylinder_signature":repr(chosen[1]),
                       "original_sixset_multiplicity":chosen[2],
                       "completion_mask":chosen[0],
                       "new_completions_covered":coverage.bit_count()})
        remaining &= ~chosen[0]
        available.remove(chosen)
    if (minimum_aff_count>0)!=(remaining==0):
        raise AssertionError("fiber positivity and exact cover do not agree")

    minS=min(row["S_seven"] for row in full)
    minW=min(row["GF5_floor_numerator"] for row in full)
    return {
        "scope":"original W(3,2), pinned left and 11/15 right factors",
        "block_original_line_ids":block,
        "complete_global_injection_completions":len(orders),
        "unaffected_original_sixsets":compiled["original_left_sixsets"]-count_affected,
        "affected_original_sixsets":count_affected,
        "frozen_left_original_sixsets":compiled["original_left_sixsets"],
        "number_affected_positional_cylinders":len(variable),
        "number_individually_forced_positive_cylinders":forced_individual_cylinders,
        "number_affected_positive_original_sixsets_base":full[0]["affected_S"],
        "baseline_seven_count":base["S_seven"],
        "baseline_GF5_floor_numerator":base["GF5_seven_lower_numerator"],
        "min_global_fiber_S":minS,"min_global_fiber_GF5_floor_numerator":minW,
        "min_affected_coherent_S":minimum_aff_count,
        "min_affected_coherent_GF5_floor_numerator":minimum_aff_weight,
        "sum_affected_independent_cylinder_min_S":independent_local_min_count,
        "sum_affected_independent_cylinder_min_GF5":independent_local_min_weight,
        "exact_coherence_gap_S":gap,
        "exact_coherence_gap_GF5_numerator":wgap,
        "source_cylinder_cover":picked,
        "source_cylinder_cover_count":len(picked),
        "source_cylinder_cover_complete":remaining==0,
        "all_24_exact_global_completion_results":full,
        "all_h_claim":"conditional min/sum inequality with complete globally injective block fibers",
        "not_global_all_h_omega":True,"not_full_R3":True,
        "Branch_A":"OPEN","Branch_B":"OPEN",
    }


def report():
    from hyp105_issue230_projection import fixture
    rows=[]
    for scheme,block in (("S68",(0,1,2,3)),("S72",(1,7,9,12))):
        model=fixture(1,scheme)
        left,right,E,_=validated_small_model(model)
        compiled=compile_original_W32_cylinders(model)
        out=coherent_fiber(compiled,right,block)
        out["scheme"]=scheme
        if out["baseline_seven_count"]!={"S68":68,"S72":72}[scheme]:
            raise AssertionError("finite original GF5 necessary baseline drift")
        rows.append(out)
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-B-COHERENT-RIGHT-FOUR-FACTOR-FIBER",
        "exact_conditional_all_h_identity":True,
        "global_injectivity_enforced_at_every_completion":True,
        "cross_sixset_original_factor_reuse_enforced":True,
        "pinned_W32_fibers":rows,
        "all_h_global_S_lower_proved":False,
        "full_GF5_R3_computed":False,
        "Branch_A":"OPEN","Branch_B":"OPEN",
    }


if __name__=="__main__":
    import json
    print(json.dumps(report(),indent=2,sort_keys=True))
