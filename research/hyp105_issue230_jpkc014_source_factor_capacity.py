"""HYP-105 JPKC-014: ORIGINAL right-source factor choice and capacity transfer.

J47: all-h conditional single-factor choice-star: source profiles with
      support intersecting moving ORIGINAL factor block B in EXACTLY {r}
      are independent of other moving factor images; for every legal
      r-image one such profile can force q_r true positive ORIGINAL Q.
J48: independent anchors r in B charge DISJOINT true ORIGINAL sixsets;
      S>=sum_r q_r (no artificial /6). For arbitrary overlapping
      sources, exact incidence multiplicity gives S>=ceil(total/d).
J49: W32 true 24-map finite source cylinder portfolios, exact original
      six-incidence Q-set equality, actual incidence IDs and capacities.

Root A/B remain OPEN. Original right factor labels shared for ALL Q;
no improper P3 predicate, no W34 full census or ASET exponent.
"""
from collections import Counter, defaultdict
from itertools import permutations
from math import ceil
import argparse
import json

from hyp105_issue230_projection import fixture
from hyp105_issue230_jpkc010_mixed_positive_transfer import FIBERS
from hyp105_issue230_jpkc012_incidence_tensor import (
    compile_incidence_tensor, contract_incidence_tensor,
)
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_jpkc014_choice_matching_bound import (
    exact_injective_choice_star_lower,
)


def incidence_capacity_certificate(anchor_witnesses, original_incidences,
                                   *, disjoint_block=None):
    """J48 finite exact source-incidence charging with no Q duplicates.

    Each anchor r selects a SET of TRUE six original incidence-ID subsets.
    Every Q assigned to r must use r as one of its ORIGINAL source
    right-line factors. If disjoint_block is set, each assigned Q must
    intersect the set of moving source factors in EXACTLY {r};
    distinct anchors then cannot share any ORIGINAL Q.

    General case: a Q can be selected for at most the number of distinct
    active anchors in its actual ORIGINAL right factor support. This is
    a valid all-h incidence cap, not a property inferred from W32 data.
    """
    try:
        incidences=tuple(tuple(x) for x in original_incidences)
    except TypeError as e:
        raise ValueError("complete ORIGINAL incidence pairs required") from e
    if not incidences or any(len(x)!=2 or any(type(t)!=int or t<0 for t in x)
                             for x in incidences) or len(set(incidences))!=len(incidences):
        raise ValueError("distinct nonnegative ORIGINAL incidence endpoints required")
    if not isinstance(anchor_witnesses,dict):
        raise ValueError("ORIGINAL source anchor-to-Q witness map required")
    moving=None
    if disjoint_block is not None:
        moving=tuple(disjoint_block)
        if len(set(moving))!=len(moving) or any(type(x)!=int or x<0 for x in moving):
            raise ValueError("distinct ORIGINAL moving right line block required")
    charge=defaultdict(set)
    total=0
    for r,qs in anchor_witnesses.items():
        if type(r)!=int or r<0 or (moving is not None and r not in moving):
            raise ValueError("valid original right line anchor required")
        if not isinstance(qs,(tuple,list,set,frozenset)):
            raise ValueError("original incidence sixset collection required")
        for raw_Q in qs:
            if not isinstance(raw_Q,(tuple,list)) or len(raw_Q)!=6 or any(
                    type(i)!=int or i<0 or i>=len(incidences) for i in raw_Q):
                raise ValueError("six actual ORIGINAL incidence IDs required")
            Q=tuple(sorted(raw_Q))
            if len(set(Q))!=6:
                raise ValueError("six distinct ORIGINAL incidence IDs required")
            support={incidences[i][1] for i in Q}
            if r not in support:
                raise AssertionError("anchor not in true ORIGINAL sixset source support")
            if moving is not None and support.intersection(moving)!={r}:
                raise AssertionError("single-factor source block cylinder was violated")
            if Q in charge[r]:
                raise AssertionError("duplicate ORIGINAL Q within one source-anchor charge")
            charge[r].add(Q)
            total+=1
    inverted=defaultdict(set)
    for r,Qs in charge.items():
        for Q in Qs:
            inverted[Q].add(r)
    max_charge=max((len(v) for v in inverted.values()),default=0)
    if moving is not None and max_charge>1:
        raise AssertionError("disjoint one-block-factor ORIGINAL Q was charged twice")
    if max_charge>6:
        raise AssertionError("one genuine ORIGINAL six-incidence Q has >6 line anchors")
    lower=ceil(total/max_charge) if max_charge else 0
    if len(inverted)<lower:
        raise AssertionError("source-incidence overlap capacity floor failed")
    if moving is not None and len(inverted)!=total:
        raise AssertionError("single-factor original Q charges were not disjoint")
    return {
        "source_anchor_count":len(anchor_witnesses),
        "total_anchor_original_Q_charges":total,
        "distinct_original_incidence_sixsets":len(inverted),
        "max_actual_anchor_multiplicity_of_an_original_Q":max_charge,
        "exact_original_incidence_capacity_lower_bound":lower,
        "single_moving_source_factor_disjoint_charge_verified":
            moving is not None,
        "all_h_incidence_support_cap_at_most_six":True,
    }


def single_factor_choice_certificate(scheme, *, states=None,
                                     independent_seven_Q=True,
                                     max_profiles=6000):
    """J49 exact W32 finite injection choice stars and Q-set charging.

    Use the DIRECT original tensor and ONE global g per state. Only source
    multisets with supp(m) intersecting moving block exactly in {r}
    may be used as a single-factor r-choice. Every allowed original
    physical image e of r must have a positive ORIGINAL source profile
    independent of the other block factor images. Choose the largest
    guaranteed true original Q count per image; on ties use lexicographic
    source multiset. No zero-value choice is declared a complete star.
    """
    if scheme not in FIBERS:
        raise ValueError("true pinned W32 S68/S72 source fiber required")
    if states is not None and (type(states)!=int or not 1<=states<=24):
        raise ValueError("states must be integer 1..24")
    if type(max_profiles)!=int or max_profiles<1:
        raise ValueError("positive ORIGINAL source profile budget required")
    if states is not None:
        # Partial prefixes cannot establish four-image source choices:
        # require complete 24 states for the star certificate itself.
        raise ValueError("complete original image choice requires all 24 legal states")
    original=fixture(1,scheme)
    compiled=compile_incidence_tensor(original)
    edges=tuple(tuple(x) for x in original["incidences"])
    labels=tuple(tuple(x) for x in original["right_labels"])
    block=tuple(FIBERS[scheme])
    images=tuple(labels[r] for r in block)
    if len(block)!=4 or len(set(block))!=4 or len(set(images))!=4:
        raise AssertionError("not a true globally legal four-original-factor block")
    choices=tuple(permutations(images))
    if len(choices)!=24:
        raise AssertionError("expected complete 4!=24 globally injective original fiber")
    all_profile_vectors=defaultdict(dict)
    true_sevens={}
    totals=[]
    for index,order in enumerate(choices):
        g=list(labels)
        for r,e in zip(block,order):
            g[r]=e
        if len(set(g))!=len(g):
            raise AssertionError("not one globally shared original right factor map")
        result=contract_incidence_tensor(compiled,tuple(g),
                                         record_profile_values=True)
        if independent_seven_Q:
            model=dict(original)
            model["right_labels"]=tuple(g)
            census=seven_census(model,independent_checks=False,witness_sets=True)
            if (result["complete_W32_true_original_S"]!=census["S_seven"] or
                    result["original_seven_classes"]!=census["seven_class_motif_counts"]):
                raise AssertionError("independent complete seven GF5 original census differs")
            by_profile=defaultdict(set)
            for Q in census["sets"]:
                m=tuple(sorted(edges[i][1] for i in Q))
                by_profile[m].add(Q)
            if {m:len(q) for m,q in by_profile.items()}!=dict(
                    result["profile_score_by_original_right_multiset"]):
                raise AssertionError("independent ORIGINAL incidence Q source profile sets differ")
            true_sevens[index]=by_profile
        for m,v in result["profile_score_by_original_right_multiset"].items():
            if type(v)!=int or v<=0:
                raise AssertionError("nonpositive true ORIGINAL source profile stored as positive")
            all_profile_vectors[m][index]=v
        totals.append(result["complete_W32_true_original_S"])
    if len(all_profile_vectors)>max_profiles:
        raise ValueError("original source profile census budget exceeded")
    N=24
    active={}
    local_restrictions=0
    source_factor_intersections=Counter()
    for m,by_state in all_profile_vectors.items():
        block_support=tuple(r for r in block if r in m)
        source_factor_intersections[len(block_support)]+=1
        if len(block_support)!=1:
            continue
        r=block_support[0]
        e_to_value={}
        for i,order in enumerate(choices):
            e=order[block.index(r)]
            value=by_state.get(i,0)
            if e in e_to_value and e_to_value[e]!=value:
                raise AssertionError("J47 local ORIGINAL line factor source cylinder violated")
            e_to_value[e]=value
            local_restrictions+=1
        if set(e_to_value)!=set(images):
            raise AssertionError("missing image of a legal original right line")
        active[m]=(r,e_to_value)

    stars={}
    portfolios={}
    for r in block:
        candidates={e:[] for e in images}
        for m,(owner,score_map) in active.items():
            if owner!=r:
                continue
            for e in images:
                if score_map[e]>0:
                    candidates[e].append((score_map[e],m))
        if any(not candidates[e] for e in images):
            continue
        best={}
        for e in images:
            q=max(score for score,_ in candidates[e])
            chosen=min(m for score,m in candidates[e] if score==q)
            best[e]={"original_source_line_multiset":chosen,
                     "number_of_true_positive_original_Q":q}
        guaranteed=min(best[e]["number_of_true_positive_original_Q"]
                       for e in images)
        if guaranteed<1:
            raise AssertionError("original factor complete star has no positive guarantee")
        stars[r]=guaranteed
        portfolios[r]=best

    selected_by_state={}
    exact_disjoint_caps=[]
    for i,order in enumerate(choices):
        charged={}
        for r in stars:
            e=order[block.index(r)]
            m=portfolios[r][e]["original_source_line_multiset"]
            q=portfolios[r][e]["number_of_true_positive_original_Q"]
            if all_profile_vectors[m].get(i,0)!=q:
                raise AssertionError("source factor witness changed under other global assignments")
            if independent_seven_Q:
                Qs=true_sevens[i].get(m,set())
                if len(Qs)!=q:
                    raise AssertionError("J48 source witness profile TRUE ORIGINAL Q-set drift")
                charged[r]=tuple(sorted(Qs))
        if independent_seven_Q:
            capacity=incidence_capacity_certificate(
                charged,edges,disjoint_block=block)
            if capacity["total_anchor_original_Q_charges"] < sum(stars.values()):
                raise AssertionError("single-factor star charge below declared all-state floor")
            if capacity["distinct_original_incidence_sixsets"]>totals[i]:
                raise AssertionError("J48 disjoint chosen true original sixsets exceed global seven S")
            exact_disjoint_caps.append(capacity)
        selected_by_state[i]=sum(portfolios[r][order[block.index(r)]][
            "number_of_true_positive_original_Q"] for r in stars)
        if selected_by_state[i]>totals[i]:
            raise AssertionError("J48 source-factor block-disjoint charge exceeds true full S")
    guaranteed_lower=sum(stars.values())
    q_matrix={
        r:{e:portfolios[r][e]["number_of_true_positive_original_Q"]
           for e in images}
        for r in stars}
    matching=exact_injective_choice_star_lower(q_matrix,images)
    if (matching["sum_of_independent_original_source_star_row_minima"]
            !=guaranteed_lower):
        raise AssertionError("J50 row minima do not equal genuine source stars")
    if (matching["exact_injective_min_original_Q_lower"]
            !=min(selected_by_state.values())):
        raise AssertionError("J50 independent dynamic matching optimum differs from 24 full global injections")
    if any(v<guaranteed_lower for v in selected_by_state.values()):
        raise AssertionError("J48 globally consistent source line stars violate disjoint lower bound")
    if any(v>totals[i] for i,v in selected_by_state.items()):
        raise AssertionError("J48 finite original incidence charge overcounts")
    one_line_value_masks={}
    for r,table in portfolios.items():
        masks={}
        for e in images:
            mask=sum(1<<i for i,order in enumerate(choices)
                     if order[block.index(r)]==e)
            if mask.bit_count()!=6:
                raise AssertionError("original one-factor image has not exactly six completions")
            masks[str(e)]=mask
        if sum(masks.values())!=(1<<N)-1 or any(
                x&y for i,x in enumerate(masks.values())
                for j,y in enumerate(masks.values()) if i<j):
            raise AssertionError("source one-factor value partition not disjoint/full")
        one_line_value_masks[r]=masks

    return {
        "scheme":scheme,
        "complete_24_state_true_original_injection_fiber":True,
        "one_fixed_original_left_map_and_one_global_right_map_per_state":True,
        "full_original_seven_S_min":min(totals),
        "total_active_positive_original_line_profiles":len(all_profile_vectors),
        "profiles_intersection_size_with_moving_original_block":
            dict(sorted(source_factor_intersections.items())),
        "single_factor_original_profile_local_cylinder_checks":local_restrictions,
        "J47_single_factor_original_image_stars":
            {r:{"min_true_original_Q_per_legal_image":stars[r],
                "per_original_physical_image_witnesses":[{
                    "image":e,**portfolios[r][e]}
                    for e in sorted(images)],
                "four_image_positive_state_partition_masks":one_line_value_masks[r]}
             for r in stars},
        "J48_distinct_original_block_line_stars":len(stars),
        "J48_all_h_conditional_block_disjoint_original_Q_lower":
            guaranteed_lower,
        "J48_finite_exact_min_selected_true_original_Q_by_state":
            min(selected_by_state.values()),
        "J50_exact_injective_original_source_star_matching":matching,
        "J48_independent_true_original_Q_set_capacity_checked":
            bool(independent_seven_Q),
        "J48_disjoint_Q_charge_summaries":(
            {"min_original_sixsets":min(x["distinct_original_incidence_sixsets"]
                                        for x in exact_disjoint_caps),
             "max_actual_multiplicity":max(
                 x["max_actual_anchor_multiplicity_of_an_original_Q"]
                 for x in exact_disjoint_caps)}
            if exact_disjoint_caps else None),
        "J49_true_original_incidence_census_reverified_every_state":
            bool(independent_seven_Q),
        "all_h_universal_star_existence_proved":False,
        "all_h_S_omega_six_proved":False,
        "root_A_proved":False,"root_B_constructed":False,
    }


def report():
    return {"slice":"JPKC-014",
            "results":[single_factor_choice_certificate(scheme)
                       for scheme in ("S68","S72")],
            "scope":"complete genuine ORIGINAL W32 4-line right factor fibers",
            "universal_all_h_S_lower_proved":False}


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--scheme",choices=tuple(FIBERS))
    args=parser.parse_args()
    result=(single_factor_choice_certificate(args.scheme) if args.scheme
            else report())
    print(json.dumps(result,indent=2,sort_keys=True))
