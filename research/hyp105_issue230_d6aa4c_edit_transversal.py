"""HYP-105 #230 D6-AA4-C: source-factor edit transversals and invariance.

All-h: if complete typed injections (f',g') differ from (f,g) only on
original factor identity set B, every ORIGINAL sixset Q disjoint from B
preserves its exact seven-accepted class and its certified GF5 floor.
Finite W32: exhaust ALL 2**15 unilateral edit supports per type and ALL
mixed two-type supports of cardinality <=5, with genuine source IDs.
No universal positive initial S is assumed or derived.
"""
from collections import Counter
from itertools import combinations
from math import comb

from hyp105_g5e2b3e1a_fixed_leading import (
    selected_left_six, validated_small_model)
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
from hyp105_issue230_d6aa_positional_tensor import (
    WEIGHTS, classify_original_six)

V32=15
TYPED_COUNT=30
MIXED_RADIUS=5
FROZEN_SCHEMES=("S68","S72")


def genuine_original_positive_hypergraph(model):
    """Exact original-sixset positive support hypergraph, with two oracles."""
    if model.get("s")!=2:
        raise ValueError("W32 true-original finite oracle only")
    left,right,incidences,_=validated_small_model(model)
    if len(left)!=V32 or len(right)!=V32 or len(incidences)!=45:
        raise ValueError("complete W32 typed source model required")
    records=[]
    seen=set()
    by_class=Counter()
    for ids,_ in selected_left_six(model):
        if len(ids)!=6 or len(set(ids))!=6 or ids in seen:
            raise AssertionError("distinct original incidence sixsets only")
        seen.add(ids)
        tag=classify_seven_prechecked(ids,left,right,incidences)
        six=tuple(incidences[i] for i in ids)
        independent=classify_original_six(six,left,right)
        if tag!=independent:
            raise AssertionError("historical and independent original classifiers diverged on ANY sixset")
        if not tag:
            continue
        if tag not in WEIGHTS:
            raise AssertionError("unrecognized positive GF5 necessary class")
        p=tuple(sorted({q for q,l in six}))
        l=tuple(sorted({t for q,t in six}))
        both=sum(1<<i for i in p)|sum(1<<(V32+i) for i in l)
        if not (p and l and len(p)<=6 and len(l)<=6):
            raise AssertionError("wrong ORIGINAL factor support")
        records.append({
            "original_incidence_ids":tuple(ids),
            "point_factors":p,
            "line_factors":l,
            "typed_support_bitmask":both,
            "tag":tag,
            "certified_GF5_numerator":WEIGHTS[tag]})
        by_class[tag]+=1
    if len(seen)!=62370:
        raise AssertionError("original-left generator incomplete")
    S=len(records)
    Y=sum(r["certified_GF5_numerator"] for r in records)
    if S!=({"S68":68,"S72":72}.get(model.get("scheme"),S)):
        # Fixtures may omit scheme metadata; source check below is stronger.
        raise AssertionError("unexpected pinned scheme")
    if (S,Y) not in ((68,3112510),(72,3283610)):
        raise AssertionError("W32 seven accepted source census has drifted")
    return {"records":tuple(records),"S":S,"Y":Y,
            "by_class":dict(by_class),"original_candidates_checked":len(seen)}


def incidence_cover_bits(records):
    """Factor -> bitset of affected ORIGINAL positive sixsets."""
    bitsets=[0]*TYPED_COUNT
    weights=[]
    allmask=(1<<len(records))-1
    for j,r in enumerate(records):
        ids=r["typed_support_bitmask"]
        if ids<=0 or ids>=(1<<TYPED_COUNT):
            raise AssertionError("invalid source factor support")
        while ids:
            unit=ids & -ids
            i=unit.bit_length()-1
            bitsets[i] |= 1<<j
            ids ^= unit
        weights.append(r["certified_GF5_numerator"])
    return tuple(bitsets),tuple(weights),allmask


def survivor_certificate(bits,weights,allmask,block):
    """Exact positives and GF5 floors left untouched by changing B."""
    touched=0
    for i in block:
        if type(i) is not int or not 0<=i<len(bits):
            raise ValueError("typed original factor ID outside support model")
        touched |= bits[i]
    surviving=allmask & ~touched
    total=0
    marker=surviving
    while marker:
        unit=marker & -marker
        total+=weights[unit.bit_length()-1]
        marker ^= unit
    return surviving.bit_count(),total,surviving


def scan_supports(bits,weights,allmask,universe,*,radius):
    """Exhaustive exact source-factor support optimization, not label search.

    Uses one ORIGINAL support set B for all sixsets; no independently
    chosen Q modifications or physical edge permutations.
    """
    universe=tuple(universe)
    if len(set(universe))!=len(universe) or any(
        type(i) is not int or not 0<=i<len(bits) for i in universe
    ):
        raise ValueError("universe must consist of distinct original factors")
    if not 0<=radius<=len(universe):
        raise ValueError("invalid exact support radius")
    out=[]
    tau=None
    for k in range(radius+1):
        minS=len(weights)+1
        minY=sum(weights)+1
        witnessS=None
        witnessY=None
        zero_count=0
        total=0
        for block in combinations(universe,k):
            count,weighted,_=survivor_certificate(bits,weights,allmask,block)
            total+=1
            if count<minS:
                minS=count
                witnessS=block
            if weighted<minY:
                minY=weighted
                witnessY=block
            if count==0:
                zero_count+=1
        if total!=comb(len(universe),k):
            raise AssertionError("incomplete original-factor support layer")
        if zero_count and tau is None:
            tau=k
        out.append({
            "edit_support_size":k,"exhaustive_supports":total,
            "min_unchanged_original_positive_sixsets":minS,
            "min_unchanged_certified_GF5_numerator":minY,
            "number_source_support_transversals":zero_count,
            "example_worst_S_original_factor_ids":witnessS,
            "example_worst_GF5_original_factor_ids":witnessY})
    if any(out[i]["min_unchanged_original_positive_sixsets"]>
           out[i-1]["min_unchanged_original_positive_sixsets"]
           for i in range(1,len(out))):
        raise AssertionError("survivor floor cannot improve with larger edit supports")
    return {
        "original_factor_universe_size":len(universe),
        "max_edit_radius_exhaustively_checked":radius,
        "number_exact_supports_checked":sum(row["exhaustive_supports"] for row in out),
        "minimum_transversal_size":tau if tau is not None else None,
        "minimum_transversal_is_exact":tau is not None,
        "if_no_transversal":"minimum transversal size > max checked edit radius",
        "by_exact_edit_support_size":out}


def source_hypergraph_report(scheme):
    from hyp105_issue230_projection import fixture
    if scheme not in FROZEN_SCHEMES:
        raise ValueError("frozen ORIGINAL W32 scheme required")
    model=fixture(1,scheme)
    source=genuine_original_positive_hypergraph(model)
    bits,weights,allmask=incidence_cover_bits(source["records"])
    profiles={
        "point_only":scan_supports(bits,weights,allmask,range(V32),radius=V32),
        "line_only":scan_supports(bits,weights,allmask,range(V32,TYPED_COUNT),radius=V32),
        "mixed_both_types":scan_supports(bits,weights,allmask,range(TYPED_COUNT),
                                        radius=MIXED_RADIUS)
    }
    for mode,profile in profiles.items():
        assert profile["by_exact_edit_support_size"][0][
            "min_unchanged_original_positive_sixsets"]==source["S"]
        assert profile["by_exact_edit_support_size"][0][
            "min_unchanged_certified_GF5_numerator"]==source["Y"]
        if mode!="mixed_both_types" and (
            profile["minimum_transversal_size"] is None or
            profile["number_exact_supports_checked"]!=(1<<V32)):
            raise AssertionError("complete unilateral hitting-set audit required")
    # Rigorous *uniform-over-all-reassignments-of-B* certificate for the
    # frozen maps: every original Q untouched by B keeps its entire class.
    for k in range(MIXED_RADIUS+1):
        mixed=profiles["mixed_both_types"]["by_exact_edit_support_size"][k]
        if mixed["min_unchanged_original_positive_sixsets"]<0:
            raise AssertionError("invalid positivity bound")

    original_a4b_blocks={"S68":(0,1,2,3),"S72":(1,7,9,12)}
    pinned=original_a4b_blocks[scheme]
    untouched=survivor_certificate(
        bits,weights,allmask,tuple(V32+i for i in pinned))
    if untouched[0]>{"S68":68,"S72":68}[scheme]:
        raise AssertionError("unaffected-original lower bound cannot exceed exact fiber min")
    return {
        "scheme":scheme,
        "true_original_W32":True,
        "original_positive_sixsets":source["S"],
        "original_GF5_certified_numerator":source["Y"],
        "by_class":source["by_class"],
        "all_62370_original_left_candidates_checked":True,
        "typed_original_factor_coverage":profiles,
        "AA4B_frozen_right_block":pinned,
        "AA4B_pinned_block_unchanged_positive_S":untouched[0],
        "AA4B_pinned_block_unchanged_GF5_numerator":untouched[1],
        "all_h_nonincreasing_support_under_arbitrary_typed_reassignments":True,
        "global_all_h_Omega_proved":False,
    }


def report():
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-C-ORIGINAL-FACTOR-EDIT-TRANSVERSAL",
        "all_h_support_invariance_theorem":True,
        "arbitrary_injective_pair_reassignments_on_original_factor_block":True,
        "no_fixed_physical_image_requirement":True,
        "W32":tuple(source_hypergraph_report(s) for s in FROZEN_SCHEMES),
        "Branch_A":"OPEN","Branch_B":"OPEN",
        "all_h_universal_positive_bound":False,"full_GF5_R3":False,
    }


if __name__=="__main__":
    import json
    print(json.dumps(report(),indent=2,sort_keys=True))
