"""AA4-BP: k arbitrary genuine original BL-regular source cherries, ONE map.

NEW: for genuine W(3,2^h), every h>=5, every already FULLY FIXED
possibly correlated complete original point f / LINE g pair images,
EVERY collection of k DISTINCT original source-POINT cherry roots
that each satisfy AA4-BL local right occupied-support pin regularity,
for any 1<=k<=k_*=min(floor(s/8),floor((a-4)/16)),
ONE common repaired FULL original LINE map g' exists with <=4k
whole source LINE factor-image transpositions, preserving the UNION
of all root source LINE factor pins at EACH step, unchanged f and right
occupied pair-edge support, and accepting k DIFFERENT true-original
six-incidence positive historical B/A motifs, all on SAME g'.

Typed source LINE / opposite original POINT map dual follows by GQ
self-duality. Candidate-level consistency / shortest Cayley metric was
already proved in parent #580. The two-root k=2 case was already proved
in immediate parent #583. THIS slice proves the growing k~s/8
uniform simultaneous actual-source-root selection and compatibility.

No inference to accepted original sixflags on ORIGINAL UNCHANGED f,g.
No fictitious large-h source GQ is generated.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import comb

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
    original_multi_cherry_candidate_minimum,
    candidate_from_target,
)


def k_root_uniform_all_h_certificate(s, k=None):
    """Proof-domain integer/Fraction certificate, no artificial W3 source.

    Input k is the number of arbitrarily prescribed DISTINCT original
    BL-regular source cherry roots. The eligible source-root set is
    deterministic for each given full g; there are >3/4 of all roots,
    but NOT >3/4 of k-sets for k>=2.
    """
    if type(s) is not int or s<32 or s&(s-1):
        raise ValueError("genuine original dyadic s>=32 required")
    V,a,K,m=_params(s)
    d=s+1
    capacity=min(s//8,(a-4)//16)
    if type(k) is not int or k<1 or k>capacity:
        raise ValueError("k must be positive and <= the certified simultaneous capacity")
    foreign_max=6*k-6
    adj=Fraction((a-3)*(a-4)*(a-5),2)-foreign_max*(a-4)*(a-5)
    disj=Fraction((a-4)*(a-5),2)-foreign_max*(a-5)
    banned_line_source_ids=2*k+4*(k-1)+3
    if not (adj>0 and disj>0 and banned_line_source_ids<d):
        raise AssertionError("uniform k original source Hall or pinned physical C6 bound fails")
    majority=every_fixed_original_g_good_root_pin_majority(s)
    G=majority["number_true_original_cherries_with_regular_two_pinned_images_lower"]
    N=majority["number_true_original_point_cherries"]
    if G<k or not 4*G>3*N:
        raise AssertionError("true original k-root eligible pin-regular mass too small")
    return {
        "s":s,"h":s.bit_length()-1,"a":a,"V":V,"m":m,"d":d,
        "chosen_k_distinct_true_original_cherry_roots":k,
        "max_certified_k_distinct_original_roots":capacity,
        "max_other_real_root_pins_or_prior_free_images_to_avoid":foreign_max,
        "max_forbidden_real_original_opposite_SOURCE_line_ids_per_new_flag":
            banned_line_source_ids,
        "adjacent_pinned_physical_sixcycle_survivor_lower":adj,
        "disjoint_pinned_physical_sixcycle_survivor_lower":disj,
        "max_union_of_genuine_original_root_line_pins":2*k,
        "max_new_true_original_line_factors":4*k,
        "max_whole_original_line_image_transpositions_one_COMMON_map":4*k,
        "distinct_true_original_source_sixflag_BA_motifs_in_one_map_lower":k,
        "all_genuine_point_cherries":N,
        "guaranteed_physically_regular_original_point_cherries":G,
        "every_k_subset_of_regular_original_roots_has_one_own_COMMON_repair":True,
        "number_repairable_k_subsets_exact_symbolic":f"binom({G},{k})",
        "fraction_all_distinct_original_k_subsets_symbolic":
            f"binom({G},{k})/binom({N},{k})",
        "fraction_lower_bounded_symbolically":
            f"(({G}-{k}+1)/{N})**{k}",
        "a_SINGLE_gprime_for_ALL_good_roots_NOT_PROVED":True,
        "original_UNMODIFIED_full_f_g_GF5_positive_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def _edge(u,v):
    return (u,v) if u<v else (v,u)


def _physical_pinned_sixcycle_avoiding_many(E,a,p1,p2,forbidden):
    """Finite exhaustive canonical physical C6 witness, unbounded F length.

    This extends #583's <=6-forbidden primitive to up to 6k-6
    occupied physical edges. All forbidden images are physical
    edges of OTHER true-original source root pins or earlier
    free assignments, never the current genuine root pins.
    """
    E={tuple(sorted(edge)) for edge in E}
    p1,p2=tuple(sorted(p1)),tuple(sorted(p2))
    F={tuple(sorted(edge)) for edge in forbidden}
    if p1==p2 or not {p1,p2}<=E or {p1,p2}&F:
        raise ValueError("two distinct ACTUAL occupied original root factor edges must be unblocked")
    if any(not all(type(u) is int and 0<=u<a for u in e) or len(e)!=2 or e[0]==e[1]
           for e in E|F):
        raise ValueError("physical unordered edge coordinates out of range")
    common=set(p1)&set(p2)
    if len(common)==1:
        mid=next(iter(common))
        u=next(x for x in p1 if x!=mid)
        w=next(x for x in p2 if x!=mid)
        remain=tuple(x for x in range(a) if x not in (u,mid,w))
        for x,y,z in permutations(remain,3):
            edges=(p1,p2,_edge(w,x),_edge(x,y),_edge(y,z),_edge(z,u))
            if len(set(edges))==6 and all(e in E and e not in F for e in edges):
                return tuple(sorted(edges))
    elif len(common)==0:
        for u,v in (p1,p1[::-1]):
            for w,x in (p2,p2[::-1]):
                remain=tuple(t for t in range(a) if t not in (u,v,w,x))
                for y,z in permutations(remain,2):
                    edges=(p1,p2,_edge(v,y),_edge(y,w),_edge(x,z),_edge(z,u))
                    if len(set(edges))==6 and all(e in E and e not in F for e in edges):
                        return tuple(sorted(edges))
    else:
        raise AssertionError("two different physical pair-edges cannot share BOTH endpoints")
    return None


def simultaneous_k_original_cherries(model,side,selected_roots,
                                     *,require_all_h_regular=True):
    """Construct one full source map respecting ALL pinned actual factors.

    selected_roots: sequence of (ACTUAL ORIGINAL source factor ID,
        (original incidence flag ID1, original incidence flag ID2)).
    For h>=5 with k<=capacity and BL-regular roots guaranteed.
    For genuine W32/W34 small h only direct finite opportunistic test.
    """
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    if type(side) is not int or side not in (0,1):
        raise ValueError("only original POINT=0 or LINE=1 typed roots")
    by=(byP,byL)[side]
    chosen=tuple(selected_roots)
    if not chosen:
        raise ValueError("at least one genuine source root required")
    normal=[]
    allpins=set()
    identities=set()
    for item in chosen:
        try:
            p,flags=item
            flags=tuple(flags)
        except (TypeError,ValueError):
            raise ValueError("root must have actual source factor and two actual flag IDs") from None
        if type(p) is not int or not 0<=p<V or len(flags)!=2 or len(set(flags))!=2 or any(
            type(t) is not int or t not in by[p] for t in flags
        ):
            raise ValueError("distinct TRUE original incidence flags through each real source root")
        key=(p,frozenset(flags))
        if key in identities:
            raise ValueError("selected original cherry roots must be DISTINCT")
        identities.add(key)
        pins={inc[j][1-side] for j in flags}
        if len(pins)!=2:
            raise AssertionError("genuine original source 2flag root opposite IDs must differ")
        normal.append((p,flags,pins))
        allpins.update(pins)
    k=len(normal)
    if require_all_h_regular and s>=32:
        k_root_uniform_all_h_certificate(s,k)
    other=(g,f)[side]
    missing=missing_endpoint_degrees(other,a)
    cap=(a-4)//8
    regular=all(max(missing[u] for src in pins for u in other[src])<=cap
                for _,_,pins in normal)
    if require_all_h_regular and s>=32 and not regular:
        raise ValueError("one or more selected original source cherries lack BL-LOCAL")
    allphysicalpins={other[i] for i in allpins}
    used_free_factors=set()
    used_free_edges=set()
    candidates=[]
    for pos,(p,flags,pins) in enumerate(normal):
        # Preserve source factor pins of all k REAL roots, and the
        # disjoint previously selected extra ORIGINAL LINE factor IDs.
        Q=genuine_root_Q_avoiding_opposite_ids(
            model,side,p,flags,(allpins|used_free_factors)-pins)
        if Q is None:
            if require_all_h_regular and s>=32:
                raise AssertionError("all-h genuine source Q C4/d distinct opposite factor Hall failed")
            return None
        ownfree={inc[j][1-side] for j in Q}-pins
        if len(ownfree)!=4 or ownfree&(allpins|used_free_factors):
            raise AssertionError("different real source root Q free original factor collision")
        pinimages={other[src] for src in pins}
        forbidden=(allphysicalpins-pinimages)|used_free_edges
        # The physical edge reserve is <=(2k-2)+4(pos)<=6k-6.
        if len(forbidden)>6*k-6 or forbidden & pinimages:
            raise AssertionError("all-h cross-root physical forbidden-edge budget false")
        cycle=_physical_pinned_sixcycle_avoiding_many(
            other,a,other[inc[flags[0]][1-side]],other[inc[flags[1]][1-side]],
            forbidden)
        if cycle is None:
            if require_all_h_regular and s>=32:
                raise AssertionError("all-h BL pin-regular physical C6 survives all prior k targets")
            return None
        freeedges=set(cycle)-pinimages
        if len(freeedges)!=4 or freeedges&used_free_edges or freeedges&allphysicalpins:
            raise AssertionError("k rooted physical C6 forbidden IMAGE overlap")
        candidates.append(candidate_from_target(model,side,p,flags,Q,cycle))
        used_free_factors.update(ownfree)
        used_free_edges.update(freeedges)
    if len(used_free_factors)!=4*k or len(used_free_edges)!=4*k:
        raise AssertionError("k different original Q extras / physical target extras incorrectly counted")
    # Exact shortest global source image completion and INDEPENDENT
    # true source original sixGF5 classification delegated to #580.
    repaired=original_multi_cherry_candidate_minimum(model,side,candidates)
    if repaired["exact_minimum_image_transpositions"]>4*k:
        raise AssertionError("one common original full global map exceeded 4k image swaps")
    after=repaired["repaired_original_complete_model"]
    Qs=tuple(tuple(c["Q"]) for c in candidates)
    if len(set(Qs))!=k:
        raise AssertionError("k DISTINCT original source cherry roots must give k different Q")
    if any(after["right_labels" if side==0 else "left_labels"][i]!=other[i]
           for i in allpins):
        raise AssertionError("some actual original root physical factor image pin changed")
    return {
        **repaired,
        "original_root_side":side,
        "original_k_distinct_cherry_roots":tuple((p,flags) for p,flags,_ in normal),
        "actual_k_distinct_true_original_Qs":Qs,
        "all_original_ROOT_PIN_source_factor_IDs":tuple(sorted(allpins)),
        "all_free_original_source_factor_IDs":tuple(sorted(used_free_factors)),
        "all_distinct_occupied_free_physical_images":tuple(sorted(used_free_edges)),
        "one_and_same_common_global_repaired_source_map_for_ALL_k":True,
        "same_input_complete_original_map_is_NOT_guaranteed_positive":True,
        "h_ge5_uniform_arbitrary_roots_guarantee":s>=32 and regular and
             k<=min(s//8,(a-4)//16),
        "root_230":"OPEN_WITH_FORMAL_BLOCKER"}
