"""HYP-105 #230 D6-AA4-D: exhaust globally coherent two-typed 4-factor fibers.

All-h exact mixed ORIGINAL-factor block completion identity, with both
physical type images independently injective. Exact W32-only zero-feasibility
gate over EVERY size-four typed-source transversal of fixed S68/S72.
Nontransversal edit supports retain old Q by AA4-C. No global all-f,g
Omega theorem or full GF5 R3 is claimed.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb, factorial

from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, seven_census)
from hyp105_g5e2b3e1a_fixed_leading import validated_small_model
from hyp105_issue230_d6p_seven_cylinder_swap_audit import (
    compile_original_W32_cylinders, cylinder_census)
from hyp105_issue230_d6aa4b_coherent_block_fiber import assign_block
from hyp105_issue230_d6aa4c_edit_transversal import (
    V32, TYPED_COUNT, genuine_original_positive_hypergraph,
    incidence_cover_bits, survivor_certificate)

BUDGET_MIXED_BLOCKS=comb(TYPED_COUNT,4)
SOURCES=("S68","S72")


def finite_source_support_partition(bits,weights,allmask,*,size=4):
    """Inspect ALL C(30,4) typed source blocks; no sampled subsets.

    Return all and only exact transversals as ORIGINAL source factor IDs.
    Each nontransversal B has a rigorously retained original-Q witness,
    independent of edited physical label choices.
    """
    if len(bits)!=TYPED_COUNT or len(weights) not in (68,72):
        raise ValueError("actual ORIGINAL W32 seven-Q support required")
    blocks=[]
    strata=Counter()
    min_other_survivors=len(weights)+1
    min_other_weight=sum(weights)+1
    min_other_block=None
    n=0
    for block in combinations(range(TYPED_COUNT),size):
        n+=1
        retained,weighted,_=survivor_certificate(bits,weights,allmask,block)
        p=sum(i<V32 for i in block)
        strata[p]+=1
        if retained==0:
            if weighted:
                raise AssertionError("zero retained Q cannot carry positive weight")
            blocks.append(block)
        else:
            if retained<min_other_survivors:
                min_other_survivors=retained
                min_other_block=block
            min_other_weight=min(min_other_weight,weighted)
    if n!=comb(TYPED_COUNT,size) or n!=BUDGET_MIXED_BLOCKS:
        raise AssertionError("incomplete source edit-block partition")
    if sum(strata.values())!=n or not blocks:
        raise AssertionError("bad source support strata")
    return {
        "source_blocks_checked":n,
        "transversal_original_factor_blocks":tuple(blocks),
        "number_transversal_blocks":len(blocks),
        "nontransversal_blocks":n-len(blocks),
        "minimum_unchanged_old_S_on_nontransversal_blocks":min_other_survivors,
        "minimum_unchanged_old_GF5_on_nontransversal_blocks":min_other_weight,
        "example_nontransversal_worst_support":min_other_block,
        "all_blocks_by_number_original_point_factors":dict(strata),
    }


def block_legal_completions(base_left,base_right,block):
    """All  bP! bL! legal W32 globally injective mixed completions.

    Unlike independent per-Q cost minimization, each ORIGINAL factor's
    label is shared across ALL ORIGINAL incidence positions and sixsets.
    """
    block=tuple(sorted(block))
    if len(block)!=4 or len(set(block))!=4 or any(
        type(i) is not int or i<0 or i>=TYPED_COUNT for i in block
    ):
        raise ValueError("four distinct typed ORIGINAL factor IDs needed")
    base_left=tuple(tuple(x) for x in base_left)
    base_right=tuple(tuple(x) for x in base_right)
    if len(base_left)!=V32 or len(base_right)!=V32 or (
        len(set(base_left))!=V32 or len(set(base_right))!=V32
    ):
        raise ValueError("W32 globally bijective typed pair assignments required")
    bp=tuple(i for i in block if i<V32)
    bl=tuple(i-V32 for i in block if i>=V32)
    p_edges=tuple(base_left[i] for i in bp)
    l_edges=tuple(base_right[i] for i in bl)
    for left_order in permutations(p_edges):
        left=assign_block(base_left,bp,left_order)
        if set(left)!=set(base_left):
            raise AssertionError("W32 physical point pair image lost")
        for right_order in permutations(l_edges):
            right=assign_block(base_right,bl,right_order)
            if set(right)!=set(base_right):
                raise AssertionError("W32 physical line pair image lost")
            yield left,right


def coherent_mixed_transversal_census(model,blocks,*,expected_blocks):
    """Exhaust BOTH type injections for every actual four-factor transversal.

    Baseline six-incidence original host is never changed. The complete
    left generator is recompiled for each legal left assignment. The
    ORIGINAL right-cylinder model then counts all accepted GF5 classes
    for every legal right assignment with exact original Q multiplicity.
    """
    left,right,edges,_=validated_small_model(model)
    if model["s"]!=2 or len(left)!=V32 or len(edges)!=45:
        raise ValueError("true ORIGINAL W32 only")
    blocks=tuple(blocks)
    if len(blocks)!=expected_blocks or len(set(blocks))!=len(blocks):
        raise AssertionError("missing/duplicate size-four source transversals")

    by_split=defaultdict(lambda: {"blocks":0,"completions":0,"zero_S_completions":0,
                                   "min_S":None,"min_GF5":None})
    minS=None
    minGF5=None
    worst=None
    total=0
    zero=0
    positive=0
    min_by_block=[]
    original_baseline=None
    independent_spotchecks=[]
    spotcheck_quota_per_split=2

    for block in blocks:
        bp=tuple(i for i in block if i<V32)
        bl=tuple(i-V32 for i in block if i>=V32)
        p=len(bp)
        g=by_split[p]
        g["blocks"]+=1
        expected=factorial(p)*factorial(4-p)
        local_min=None
        local_min_weight=None
        local_zero=0
        count=0
        previous_left=None
        compiled=None
        for current_left,current_right in block_legal_completions(left,right,block):
            if current_left!=previous_left:
                m=dict(model)
                m["left_labels"]=current_left
                compiled=compile_original_W32_cylinders(m)
                previous_left=current_left
            current=cylinder_census(compiled,current_right)
            score=current["S_seven"]
            weight=current["GF5_seven_lower_numerator"]
            if score!=sum(current["seven_class_motif_counts"].values()):
                raise AssertionError("seven GF5 class mass not conserved")
            if weight!=sum(current["seven_class_motif_counts"][k]*w
                           for k,w in R3_CERTIFIED_FLOORS.items()):
                raise AssertionError("GF5 floor numerator drift")
            if current_left==left and current_right==right:
                baseline=(score,weight)
                if original_baseline is None:
                    original_baseline=baseline
                elif original_baseline!=baseline:
                    raise AssertionError("baseline globally injected source drift")
            local_min=score if local_min is None else min(local_min,score)
            local_min_weight=(weight if local_min_weight is None
                              else min(local_min_weight,weight))
            total+=1
            count+=1
            g["completions"]+=1
            if score==0:
                zero+=1
                local_zero+=1
                g["zero_S_completions"]+=1
            else:
                positive+=1
            if g["min_S"] is None or score<g["min_S"]:
                g["min_S"]=score
            if g["min_GF5"] is None or weight<g["min_GF5"]:
                g["min_GF5"]=weight
            if minS is None or score<minS:
                minS=score
                worst={"source_block":block,
                       "reassigned_original_point_labels":
                           tuple(current_left[i] for i in bp),
                       "reassigned_original_line_labels":
                           tuple(current_right[i] for i in bl),
                       "S_seven":score,"GF5_floor_numerator":weight}
            minGF5=weight if minGF5 is None else min(minGF5,weight)

            # Strict independent ORIGINAL classifier on a representative
            # global completion from each mixed/one-sided split.
            if (len([x for x in independent_spotchecks if x["point_block_size"]==p])
                    < spotcheck_quota_per_split):
                independent=seven_census(
                    {**model,"left_labels":current_left,"right_labels":current_right},
                    independent_checks=False)
                if independent["S_seven"]!=score or (
                    independent["GF5_seven_lower_numerator"]!=weight
                ) or independent["seven_class_motif_counts"]!=current["seven_class_motif_counts"]:
                    raise AssertionError("independent true ORIGINAL GF5 census disagrees")
                independent_spotchecks.append({
                    "point_block_size":p,
                    "source_block":block,
                    "S":score,
                    "GF5_floor_numerator":weight})
        if count!=expected:
            raise AssertionError("not every globally injective completion was checked")
        min_by_block.append({"original_typed_factor_block":block,
                             "original_point_factors":bp,
                             "original_line_factors":bl,
                             "globally_legal_completions":count,
                             "minimum_S_seven":local_min,
                             "minimum_GF5_floor_numerator":local_min_weight,
                             "zero_S_completions":local_zero})
    if total!=zero+positive or len(min_by_block)!=len(blocks):
        raise AssertionError("incomplete typed source transversal exhaustion")
    if original_baseline is None:
        raise AssertionError("baseline assignment missing from coherent fibers")
    if len(independent_spotchecks)!=2*len(by_split):
        raise AssertionError("independent spotcheck coverage incomplete")

    return {
        "original_source_transversal_blocks":len(blocks),
        "globally_injective_two_typed_completions_checked":total,
        "positive_S_completions":positive,
        "zero_S_completions":zero,
        "minimum_S_in_all_transversal_fibers":minS,
        "minimum_GF5_floor_numerator_in_all_transversal_fibers":minGF5,
        "baseline":original_baseline,
        "example_global_minimum_completion":worst,
        "by_point_factor_split":{str(k):v for k,v in sorted(by_split.items())},
        "all_block_minima":min_by_block,
        "independent_full_original_classification_checks":independent_spotchecks,
    }


def report_one(scheme):
    from hyp105_issue230_projection import fixture
    if scheme not in SOURCES:
        raise ValueError("recognized ORIGINAL W32 scheme required")
    model=fixture(1,scheme)
    source=genuine_original_positive_hypergraph(model)
    bits,weights,allmask=incidence_cover_bits(source["records"])
    partition=finite_source_support_partition(bits,weights,allmask)
    expected={"S68":53,"S72":119}[scheme]
    if partition["number_transversal_blocks"]!=expected:
        raise AssertionError("exact AA4C source transversal cardinality drift")
    physical=coherent_mixed_transversal_census(
        model,partition["transversal_original_factor_blocks"],
        expected_blocks=expected)
    baseline={"S68":(68,3112510),"S72":(72,3283610)}[scheme]
    if physical["baseline"]!=baseline:
        raise AssertionError("genuine ORIGINAL baseline S/Y regression drift")
    source_survival_floor=partition[
        "minimum_unchanged_old_S_on_nontransversal_blocks"]
    # Every 4-factor edit support is EITHER a transversal (all globally
    # legal completions checked) OR retains at least source_survival_floor
    # previously positive Q, independent of the physical completion.
    radius_four_bound=min(source_survival_floor,
        physical["minimum_S_in_all_transversal_fibers"])
    if radius_four_bound<0:
        raise AssertionError("negative exact global injection support gate")
    return {
        "scheme":scheme,
        "scope":"all ORIGINAL W32 global injections agreeing outside <=4 typed original factors of THIS fixed f,g",
        "base_seven_S":source["S"],
        "base_GF5_floor_numerator":source["Y"],
        "source_support_partition":partition,
        "globally_consistent_transversal_fibers":physical,
        "uniform_all_legal_typed_edits_radius_at_most_four_S_floor":radius_four_bound,
        "positive_for_every_radius_four_edit":radius_four_bound>0,
        "not_arbitrary_starting_f_g":True,
        "not_all_h":True,
    }


def report(scheme=None):
    if scheme is None:
        sources=SOURCES
    elif scheme in SOURCES:
        sources=(scheme,)
    else:
        raise ValueError("unknown W32 scheme")
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-D-TWO-TYPE-FOUR-FACTOR-GLOBAL-FIBER",
        "all_h_conditional_global_completion_identity":True,
        "all_h_frozen_outside_original_block":True,
        "source_geometry_fixed":True,
        "W32":tuple(report_one(s) for s in sources),
        "Branch_A":"OPEN","Branch_B":"OPEN",
        "all_h_universal_S_lower":False,
        "full_GF5_R3":False,
    }


if __name__=="__main__":
    import argparse
    import json
    parser=argparse.ArgumentParser()
    parser.add_argument("--scheme",choices=SOURCES)
    x=parser.parse_args()
    print(json.dumps(report(x.scheme),indent=2,sort_keys=True))
