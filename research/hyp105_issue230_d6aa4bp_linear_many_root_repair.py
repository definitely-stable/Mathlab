"""AA4-BP: one common original full map repairs LINEARLY MANY genuine roots.

Every complete original correlated f,g, dyadic s>=32, and ANY
2<=k<=floor((s+1)/6) distinct BL-regular same-type true W(3,s)
source cherry roots: ONE new complete opposite map repairs ALL k
six-distinct-original-flag B/A (or A/B dual) motifs in <=4k
whole ORIGINAL opposite-factor image transpositions, with EVERY
root pin unaltered throughout. This does not prove positive motifs
on the UNCHANGED input g or root issue #230 Branch A/B/C.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations

from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import _params
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bl_two_pin_conditional_BA import (
    every_fixed_original_g_good_root_pin_majority,
)
from hyp105_issue230_d6aa4bm_four_swap_root_BA_repair import (
    missing_endpoint_degrees,
)
from hyp105_issue230_d6aa4bo_simultaneous_cherry_repair import (
    genuine_root_Q_avoiding_opposite_ids,
)
from hyp105_issue230_d6aa4bn_multi_root_swap_compatibility import (
    candidate_from_target,
    original_multi_cherry_candidate_minimum,
)


def linear_many_root_all_h_certificate(s, k=None):
    """Exact all-dyadic arithmetic, no fake high-order W3 enumeration.

    k is the simultaneous-root size to be certified, or None for the
    maximum guaranteed size. The pin count <=2k, prior free genuine
    opposite source IDs <=4(k-1), and within-Q used IDs <=3 imply
    d=s+1>6k-1. The physical six-cycle forbidden edge cap is
    2(k-1)+6(k-1)=8(k-1)<(a-4)/2.
    """
    if type(s) is not int or s<32 or s&(s-1):
        raise ValueError("genuine dyadic W3 s>=32 only")
    V,a,alphabet_size,missing=_params(s)
    d=s+1
    max_source=d//6
    max_physical=(a+11)//16
    max_roots=min(max_source,max_physical)
    if k is None:
        k=max_roots
    if type(k) is not int or not 2<=k<=max_roots:
        raise ValueError("two or more roots, <= exact joint source/target bound")
    forbidden=8*(k-1)
    source_banned=2*k+4*(k-1)+3
    if not d>source_banned or not 2*forbidden<a-4:
        raise AssertionError("actual original source degree or physical C6 bound failed")
    # For s>=32, minimal alphabet satisfies a>8s: a(a-1)/2
    # >=V>s^3 implies a>sqrt(2*s^3)>=8s.
    if not a>8*s or not max_physical>=max_source:
        raise AssertionError("claimed all-h original source bottleneck not justified")
    adjacent=Fraction((a-4)*(a-5)*(a-3),2)-forbidden*(a-4)*(a-5)
    disjoint=Fraction((a-4)*(a-5),2)-forbidden*(a-5)
    if not adjacent>0 or not disjoint>0:
        raise AssertionError("rooted physical C6 survives all prior targets and protected pins")
    majority=every_fixed_original_g_good_root_pin_majority(s)
    N=majority["number_true_original_point_cherries"]
    G=majority["number_true_original_cherries_with_regular_two_pinned_images_lower"]
    if not 4*G>3*N or not G>=k:
        raise AssertionError("true original all-fixed-map BL-majority does not supply k roots")
    return {
        "s":s,"V":V,"a":a,"physical_missing_edge_count":missing,
        "original_opposite_degree":d,"simultaneous_roots_k":k,
        "max_guaranteed_roots":max_roots,
        "max_from_original_GQ_source_degree":max_source,
        "max_from_physical_six_cycle_avoidance":max_physical,
        "source_banned_original_opposite_ids_worst":source_banned,
        "physical_forbidden_edges_worst":forbidden,
        "physical_adjacent_pin_C6_survivor_lower":adjacent,
        "physical_disjoint_pin_C6_survivor_lower":disjoint,
        "max_protected_true_original_opposite_factor_ids":2*k,
        "max_changed_free_true_original_factor_ids":4*k,
        "max_original_whole_factor_image_swaps":4*k,
        "number_true_original_cherries":N,
        "guaranteed_pin_regular_original_cherries":G,
        "ANY_k_DISTINCT_regular_root_subset_one_common_new_map":True,
        "number_of_original_good_k_subsets_lower_symbolic":"binomial(G,k)",
        "number_of_total_original_k_subsets_symbolic":"binomial(N,k)",
        "distinct_accepted_original_six_incidence_motifs_lower_on_NEW_map":k,
        "a_single_new_map_for_ALL_good_roots_NOT_PROVED":True,
        "unchanged_input_pair_GF5_positive_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def occupied_two_pin_C6_avoiding_many(E,a,pin1,pin2,forbidden):
    """Finite constructive physical C6 avoiding arbitrary other images.

    This is not an exhaustive count and is used only on finite genuine
    low-h original fixtures. The all-h existence is a separate proof.
    """
    if type(a) is not int or a<6:
        raise ValueError("at least six physical vertices")
    try:
        occupied={tuple(sorted(e)) for e in E}
        p1=tuple(sorted(pin1))
        p2=tuple(sorted(pin2))
        F={tuple(sorted(e)) for e in forbidden}
    except TypeError:
        raise ValueError("bad physical occupied pairs") from None
    if p1==p2 or p1 not in occupied or p2 not in occupied or {p1,p2}&F:
        raise ValueError("different occupied physical pin pairs must remain allowed")
    if any(len(e)!=2 or e[0]==e[1] or e[0]<0 or e[1]>=a for e in occupied|F):
        raise ValueError("invalid physical edge support")
    if len(F)>len(occupied)-2:
        raise ValueError("more exclusions than available unpinned occupied edges")
    def edge(u,v):
        return (u,v) if u<v else (v,u)
    common=set(p1)&set(p2)
    if len(common)==1:
        v=next(iter(common))
        u=next(x for x in p1 if x!=v)
        w=next(x for x in p2 if x!=v)
        remaining=[x for x in range(a) if x not in (u,v,w)]
        for x,y,z in permutations(remaining,3):
            target=(p1,p2,edge(w,x),edge(x,y),edge(y,z),edge(z,u))
            if len(set(target))==6 and set(target)<=occupied and not set(target)&F:
                return tuple(sorted(target))
    elif len(common)==0:
        for u,v in (p1,p1[::-1]):
            for w,x in (p2,p2[::-1]):
                remaining=[z for z in range(a) if z not in (u,v,w,x)]
                for y,z in permutations(remaining,2):
                    target=(p1,edge(v,y),edge(y,w),p2,edge(x,z),edge(z,u))
                    if len(set(target))==6 and set(target)<=occupied and not set(target)&F:
                        return tuple(sorted(target))
    else:
        raise AssertionError("two distinct physical edges cannot share both vertices")
    return None


def simultaneous_many_original_cherries(model,side,cherries,*,require_regular=True):
    """Construct an identical FULL global image map for k true source roots.

    High-h mathematical guarantee: all dyadic s>=32, 2<=k<=floor(d/6),
    each original cherry BL-local physically pin regular. Small genuine
    W32/W34 models are independent finite falsifiers, not an all-h proof.
    """
    if type(side) is not int or side not in (0,1):
        raise ValueError("typed original source side 0 POINT / 1 LINE")
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    roots=(byP,byL)[side]
    other=(g,f)[side]
    cherries=tuple(cherries)
    if len(cherries)<2:
        raise ValueError("at least TWO true original cherries")
    maxk=linear_many_root_all_h_certificate(s)["max_guaranteed_roots"] if s>=32 else None
    if s>=32 and len(cherries)>maxk and require_regular:
        raise ValueError("too many roots for certified all-h linear-many guarantee")
    selected=[]
    seen=set()
    allpins=set()
    for entry in cherries:
        try:
            p,rawflags=entry
            flags=tuple(rawflags)
        except (ValueError,TypeError):
            raise ValueError("each root requires an original source factor and exactly two flags") from None
        if type(p) is not int or p<0 or p>=V:
            raise ValueError("bad TRUE ORIGINAL root source factor ID")
        if len(flags)!=2 or len(set(flags))!=2 or any(
            type(j) is not int or j not in roots[p] for j in flags
        ):
            raise ValueError("two distinct ACTUAL original incidence IDs through this source root required")
        key=(p,frozenset(flags))
        if key in seen:
            raise ValueError("duplicate original source cherry root")
        seen.add(key)
        pins={inc[j][1-side] for j in flags}
        if len(pins)!=2:
            raise AssertionError("genuine source opposite root factor pins not distinct")
        selected.append((p,flags,pins))
        allpins.update(pins)
    physical_holes=missing_endpoint_degrees(other,a)
    t=(a-4)//8
    regular=all(max(physical_holes[u] for src in pins for u in other[src])<=t
                for _,_,pins in selected)
    if require_regular and s>=32 and not regular:
        raise ValueError("a selected true original source cherry fails physical BL-LOCAL")
    targets=[]
    constructed=[]
    used_free=set()
    protected_images={other[i] for i in allpins}
    for ordinal,(p,flags,pins) in enumerate(selected):
        Q=genuine_root_Q_avoiding_opposite_ids(
            model,side,p,flags,(allpins|used_free)-pins)
        if Q is None:
            if s>=32 and require_regular:
                raise AssertionError("original source-C4 true sixflag Hall all-h lower contradicted")
            return None
        free={inc[j][1-side] for j in Q}-pins
        if len(free)!=4 or free & (allpins|used_free):
            raise AssertionError("genuine source LINE factors collide across repaired roots")
        own_images={other[i] for i in pins}
        excluded=(protected_images-own_images)|set().union(*targets) if targets else protected_images-own_images
        if own_images&excluded:
            raise AssertionError("current true opposite pinned image was mistakenly forbidden")
        if s>=32 and require_regular and len(excluded)>8*(len(selected)-1):
            raise AssertionError("all-h physically forbidden image cap violated")
        target=occupied_two_pin_C6_avoiding_many(
            other,a,other[inc[flags[0]][1-side]],
            other[inc[flags[1]][1-side]],excluded)
        if target is None:
            if s>=32 and require_regular:
                raise AssertionError("true physical rooted six-cycle with foreign exclusions absent")
            return None
        free_target=set(target)-own_images
        if len(free_target)!=4 or free_target&protected_images:
            raise AssertionError("free target physical edges touch protected original image")
        if any(free_target&(set(T)-{other[i] for i in ownpins})
               for T,(_,_,ownpins) in zip(targets,selected[:ordinal])):
            raise AssertionError("distinct rooted C6 free target edge images collide")
        constructed.append(candidate_from_target(model,side,p,flags,Q,target))
        targets.append(target)
        used_free.update(free)
    witness=original_multi_cherry_candidate_minimum(model,side,constructed)
    if witness["exact_minimum_image_transpositions"]>4*len(cherries):
        raise AssertionError("one whole-map matching exceeded available four factor images per root")
    Qs=tuple(z["Q"] for z in witness["actual_true_original_cherry_certificates"])
    if len(set(Qs))!=len(cherries):
        raise AssertionError("original source incidence Q repeated across distinct roots")
    witness.update({
        "all_selected_actual_original_cherries":tuple((p,flags) for p,flags,_ in selected),
        "all_protected_TRUE_original_opposite_factor_IDs":tuple(sorted(allpins)),
        "all_input_true_original_pin_physical_images":tuple(other[i] for i in sorted(allpins)),
        "number_concurrently_accepted_distinct_original_GF5_sixsets":len(Qs),
        "whole_original_factor_image_swap_bound":4*len(cherries),
        "all_h_proved_if_dyadic_s>=32_k<=floor_d_over6_and_every_BL_regular":
            s>=32 and regular and len(cherries)<=((s+1)//6),
        "every_intermediate_full_global_map_same_support_and_ALL_root_pins":True,
        "each_given_original_cherry_k_subfamily_repair_map_may_differ":True,
        "UNCHANGED_original_pair_selected_seven_GF5_lower_NOT_PROVED":True,
    })
    return witness
