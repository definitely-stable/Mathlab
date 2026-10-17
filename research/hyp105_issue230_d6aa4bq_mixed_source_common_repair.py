"""AA4-BQ: ONE common corrected PAIR (f',g') for MIXED original roots.

REAL original W(3,2^h); arbitrary completely fixed correlated globally
injected typed point f / LINE g physical maps; any k distinct source
cherries of EITHER source type, all opposite-pin BL regular. For
2<=k<=min(floor((s-4)/8), floor((a-4)/20)), there exist one f',g'
with total at most 4k whole original SOURCE factor image transpositions,
with original root opposite factor images and all already selected
B-side source factors unchanged. The same final pair simultaneously
accepts k different true six-ID historical GF5 B/A and/or A/B.

NEW compared to #583/#585/#586 same-typed k-root repairs: source
B-side factors must be frozen AGAINST opposite-type physical map edits.
Both original typed maps change, but no SIX original incidence IDs do.

This does NOT guarantee ANY motif on the original unchanged f,g.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import _params
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bj_cherry_hall_defect import _full_four_patterns
from hyp105_issue230_d6aa4bl_two_pin_conditional_BA import every_fixed_original_g_good_root_pin_majority
from hyp105_issue230_d6aa4bm_four_swap_root_BA_repair import _root_flags,missing_endpoint_degrees
from hyp105_issue230_d6aa4bp_k_root_common_repair import _physical_pinned_sixcycle_avoiding_many
from hyp105_issue230_d6aa4bn_multi_root_swap_compatibility import (
    original_multi_cherry_candidate_minimum,candidate_from_target,
)
from hyp105_issue230_d6aa4q_two_sided_seven_join import independent_joint_classify


def mixed_k_all_h_certificate(s,k=None,k_point=None,k_line=None):
    """Analytic source + target budgets. No fabricated large original GQ."""
    if type(s) is not int or s<32 or s&(s-1):
        raise ValueError("actual original theorem requires dyadic s>=32")
    V,a,K,m=_params(s); d=s+1
    cap=min((s-4)//8,(a-4)//20)
    if k is None:
        k=cap
    if type(k) is not int or not 2<=k<=cap:
        raise ValueError("mixed theorem requires 2<=k<=certified capacity")
    if (k_point is None) != (k_line is None):
        raise ValueError("both counts or neither")
    if k_point is None:
        k_point=1;k_line=k-1
    if (type(k_point) is not int or type(k_line) is not int or
        k_point<1 or k_line<1 or k_point+k_line!=k):
        raise ValueError("at least one of BOTH genuine root types required")
    Fpoint=5*k_point+2*k_line
    Fline=5*k_line+2*k_point
    # Each free 4-neighbor choice may exclude ALL globally protected
    # opposite-side IDs, up to 4(k_type-1) earlier free IDs of THAT type
    # plus the previous three chosen at the current root.
    src_point=Fpoint+4*(k_line-1)+3
    src_line=Fline+4*(k_point-1)+3
    # At root i, forbid every other protected opposite factor's already
    # occupied physical pair-edge image plus <=4(k_type-1) prior target
    # edges of that type. Source-B physical factor images of the
    # OPPOSITE root type are protected for the entire repair.
    omit_point=Fpoint-2+4*(k_line-1)
    omit_line=Fline-2+4*(k_point-1)
    adj_point=Fraction((a-3)*(a-4)*(a-5),2)-omit_point*(a-4)*(a-5)
    dis_point=Fraction((a-4)*(a-5),2)-omit_point*(a-5)
    adj_line=Fraction((a-3)*(a-4)*(a-5),2)-omit_line*(a-4)*(a-5)
    dis_line=Fraction((a-4)*(a-5),2)-omit_line*(a-5)
    if not (src_point<d and src_line<d and
            adj_point>0 and dis_point>0 and
            adj_line>0 and dis_line>0):
        raise AssertionError("mixed-type original source Hall / physical cycle bound fails")
    G=every_fixed_original_g_good_root_pin_majority(s)
    return {
        "s":s,"h":s.bit_length()-1,"V":V,"a":a,"m":m,"d":d,
        "number_original_point_source_cherries":k_point,
        "number_original_LINE_source_cherries":k_line,
        "total_mixed_original_cherries":k,
        "maximum_guaranteed_mixed_k":cap,
        "frozen_ORIGINAL_point_source_factor_upper":Fpoint,
        "frozen_ORIGINAL_LINE_source_factor_upper":Fline,
        "source_REAL_POINT_neighbor_banned_upper":src_point,
        "source_REAL_LINE_neighbor_banned_upper":src_line,
        "physical_left_extra_forbidden_occupied_pairs_upper":omit_point,
        "physical_right_extra_forbidden_occupied_pairs_upper":omit_line,
        "physical_left_adjacent_C6_survivor_lower":adj_point,
        "physical_left_disjoint_C6_survivor_lower":dis_point,
        "physical_right_adjacent_C6_survivor_lower":adj_line,
        "physical_right_disjoint_C6_survivor_lower":dis_line,
        "max_whole_original_POINT_factor_image_transpositions":4*k_line,
        "max_whole_original_LINE_factor_image_transpositions":4*k_point,
        "max_total_original_factor_image_transpositions":4*k,
        "B_side_original_factor_images_preserved_across_OPPOSITE_side_repairs":True,
        "every_mixed_set_of_both_pin_regular_true_source_types_has_one_common_pair":True,
        "unchanged_fixed_original_f_g_sevenGF5_lower_NOT_PROVED":True,
        "one_corrected_pair_for_ALL_regular_original_roots_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def _original_root_B_C4_skeleton(model,side,root,flags):
    """Root type B chosen on its EXISTING original fixed physical factor map."""
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    by=(byP,byL)[side]
    flags=_root_flags(inc,by,side,root,tuple(flags))
    images=(f,g)[side]
    inverse={e:i for i,e in enumerate(images)}
    for vertices in combinations(tuple(v for v in range(a) if v not in images[root]),4):
        _,_,patterns=_full_four_patterns(vertices,set(inverse))
        for kind,edges in patterns:
            if kind!="C4":continue
            other=tuple(inverse[e] for e in edges)
            if len(set(other))!=4 or root in other:
                raise AssertionError("original source factor C4 inversion not authentic")
            return {
                "type":side,"root":root,"flags":flags,
                "root_opposite_pins":tuple(inc[j][1-side] for j in flags),
                "fixed_B_source_factors":frozenset((root,)+other),
                "other_original_B_factors":other,
            }
    return None


def simultaneous_mixed_original_cherries(model,roots,*,require_all_h_regular=True):
    """Construct ONE full point+LINE image map accepting BOTH original classes.

    roots iterable (side=0/1, actual original source B factor root,
        pair of TRUE actual original source incidence IDs).
    With s>=32 and eligible mixed k guaranteed by theorem. W32/W34
    finite oracles run with require_all_h_regular=False and may fail.
    """
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    roots=tuple(roots)
    if len(roots)<2 or {v[0] for v in roots if isinstance(v,tuple) and len(v)==3}!={0,1}:
        raise ValueError("mixed source-root collection must contain BOTH original types")
    seen=set();skeletons=[]
    for entry in roots:
        try: side,p,flags=entry
        except (TypeError,ValueError):
            raise ValueError("root is (source-type, actual source factor ID, actual two flag IDs)") from None
        if type(side) is not int or side not in (0,1):
            raise ValueError("genuine original typed root 0=POINT,1=LINE")
        if type(p) is not int or p<0 or p>=V:
            raise ValueError("genuine original root factor ID")
        root=_original_root_B_C4_skeleton(model,side,p,flags)
        key=(side,p,frozenset(root["flags"]))
        if key in seen:raise ValueError("actual original cherry repeats")
        seen.add(key)
        if root is None:
            if require_all_h_regular and s>=32:
                raise AssertionError("true original source B C4 must exist for every root")
            return None
        skeletons.append(root)
    kp=sum(x["type"]==0 for x in skeletons)
    kl=len(skeletons)-kp
    if require_all_h_regular and s>=32:
        mixed_k_all_h_certificate(s,len(roots),kp,kl)
    frozen=[
        set().union(*(x["fixed_B_source_factors"] for x in skeletons if x["type"]==0)),
        set().union(*(x["fixed_B_source_factors"] for x in skeletons if x["type"]==1)),
    ]
    # Each original ROOT opposite source factor has its image pinned,
    # even if shared between roots or appearing as another root's B
    # source factor (consistency is retained automatically).
    for x in skeletons:
        frozen[1-x["type"]].update(x["root_opposite_pins"])
    preimages=(tuple(f),tuple(g))
    missing=[missing_endpoint_degrees(preimages[i],a) for i in (0,1)]
    t=(a-4)//8
    eligible=all(max(missing[1-x["type"]][coord]
                      for source in x["root_opposite_pins"]
                      for coord in preimages[1-x["type"]][source])<=t
                 for x in skeletons)
    if require_all_h_regular and s>=32 and not eligible:
        raise ValueError("at least one original root lacks opposite-image BL-regularity")
    used_free_src=(set(),set())
    used_free_target=(set(),set())
    candidates_by_side=([],[])
    actual_Qs=[]
    for x in skeletons:
        side=x["type"];opp=1-side
        root=x["root"];flags=x["flags"]
        by=(byP,byL)[side]
        used=set(frozen[opp])|used_free_src[opp]
        extra=[]
        for q in x["other_original_B_factors"]:
            j=next((j for j in by[q] if inc[j][opp] not in used),None)
            if j is None:
                if require_all_h_regular and s>=32:
                    raise AssertionError("genuine source GQ d=s+1 mixed protected distinct-neighbor Hall failed")
                return None
            extra.append(j)
            used.add(inc[j][opp])
        Q=tuple(sorted((*flags,*extra)))
        if len(Q)!=6 or len(set(Q))!=6 or len({inc[j][opp] for j in Q})!=6:
            raise AssertionError("six true original incidence flag IDs and distinct A source factors")
        free={inc[j][opp] for j in extra}
        if len(free)!=4 or free&frozen[opp] or free&used_free_src[opp]:
            raise AssertionError("mixed roots source opposite factor-ID collision")
        used_free_src[opp].update(free)
        opposite=preimages[opp]
        pinimages={opposite[src] for src in x["root_opposite_pins"]}
        forbidden=({opposite[id] for id in frozen[opp]}-pinimages)|used_free_target[opp]
        if len(forbidden)>len(frozen[opp])-2+4*(kp if side==1 else kl):
            raise AssertionError("mixed source right-target physical forbid budget")
        target=_physical_pinned_sixcycle_avoiding_many(
            opposite,a,opposite[x["root_opposite_pins"][0]],
            opposite[x["root_opposite_pins"][1]],forbidden)
        if target is None:
            if require_all_h_regular and s>=32:
                raise AssertionError("BL right occupied C6 survival under BOTH-type B-factor pins failed")
            return None
        free_target=set(target)-pinimages
        if (len(free_target)!=4 or free_target&used_free_target[opp] or
            free_target&{opposite[id] for id in frozen[opp]}):
            raise AssertionError("mixed right physical occupied target collision with B-side freeze")
        used_free_target[opp].update(free_target)
        cand=candidate_from_target(model,side,root,flags,Q,target)
        candidates_by_side[side].append(cand)
        actual_Qs.append((side,Q))
    corrected=[tuple(f),tuple(g)]
    source_swaps=((),())
    shortests=[]
    for side,subset in enumerate(candidates_by_side):
        if not subset:continue
        result=original_multi_cherry_candidate_minimum(model,side,subset)
        opp=1-side
        corrected[opp]=result["final_full_global_map"]
        source_swaps=tuple(
            result["actual_shortest_global_transpositions"] if i==opp else source_swaps[i]
            for i in range(2))
        shortests.append(result["exact_minimum_image_transpositions"])
        if any(corrected[opp][j]!=preimages[opp][j] for j in frozen[opp]):
            raise AssertionError("B-source physical image factor changed under opposite type repair")
    after=dict(model,left_labels=corrected[0],right_labels=corrected[1])
    tags=[]
    for side,Q in actual_Qs:
        tag=independent_joint_classify(
            Q,"B" if side==0 else "A","A" if side==0 else "B",
            inc,after["left_labels"],after["right_labels"])
        wanted="B-left/A-right" if side==0 else "A-left/B-right"
        if tag!=wanted:
            raise AssertionError("same FINAL joint physical pair fails true-original GF5 B/A or A/B")
        tags.append(tag)
    if len(set(q for _,q in actual_Qs))!=len(actual_Qs):
        raise AssertionError("mixed distinct true original sixflag Q identities collide")
    total=sum(len(p) for p in source_swaps)
    if total>4*len(skeletons):
        raise AssertionError("mixed two-type total source factor swap budget exceeded")
    return {
        "s":s,"V":V,"a":a,"source_mixed_root_count":len(skeletons),
        "number_original_POINT_source_cherries":kp,
        "number_original_LINE_source_cherries":kl,
        "actual_mixed_source_sixflag_Q_with_original_type":tuple(actual_Qs),
        "accepted_historical_original_seven_GF5_tags_ON_ONE_PAIR":tuple(tags),
        "initial_full_original_maps":preimages,
        "final_full_original_maps":tuple(corrected),
        "one_joint_repaired_full_original_model":after,
        "full_original_POINT_source_swaps":source_swaps[0],
        "full_original_LINE_source_swaps":source_swaps[1],
        "total_whole_original_factor_image_transpositions":total,
        "protected_true_original_factor_IDs_by_type":
            (tuple(sorted(frozen[0])),tuple(sorted(frozen[1]))),
        "all_original_B_source_factors_unchanged_on_B_side":True,
        "one_COMMON_final_f_prime_g_prime_for_both_original_GF5_BA_and_AB":True,
        "all_h_mixed_theorem_applies":s>=32 and eligible and
          len(skeletons)<=min((s-4)//8,(a-4)//20),
        "original_unmodified_fixed_f_g_sevenGF5_positive_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
