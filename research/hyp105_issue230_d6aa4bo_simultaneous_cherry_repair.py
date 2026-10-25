"""AA4-BO: two genuinely distinct cherry roots repaired on ONE full original map.

For s=2^h>=32, arbitrary already fixed correlated globally injected typed
source maps f,g, and any TWO actual same-type original cherry roots whose
opposite images satisfy AA4-BL local pin regularity, exists ONE g' fixing the
union of (at most four) original pinned opposite factors and accepting a
distinct six-ORIGINAL-incidence Q for EACH root within <=8 whole-image swaps.

Root-dependent g' is NOT the original fixed g. No original seven-GF5
minimax statement. Purely geometric all-h certificate does not instantiate
fake high-order generalized quadrangles.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bj_cherry_hall_defect import _full_four_patterns
from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import _params
from hyp105_issue230_d6aa4bl_two_pin_conditional_BA import (
    every_fixed_original_g_good_root_pin_majority,
)
from hyp105_issue230_d6aa4bm_four_swap_root_BA_repair import (
    missing_endpoint_degrees,
)
from hyp105_issue230_d6aa4bn_multi_root_swap_compatibility import (
    original_multi_cherry_candidate_minimum,
    candidate_from_target,
)


def two_pin_cycle_survivor_certificate(s, foreign_forbidden_edges=6):
    """ALL-h integer-proof bound, not enumeration of a fictional W(3,s).

    BL proves at least half of ONE fixed rooted orientation survives
    physical holes, for both types of pin adjacency. Removing t distinct
    arbitrary other occupied edges costs at most
      adjacent: t (a-4)(a-5)
      disjoint: t (a-5).
    """
    if type(s) is not int or s < 32 or s & (s-1):
        raise ValueError("all-h BO theorem needs genuine dyadic s>=32")
    if type(foreign_forbidden_edges) is not int or not 0<=foreign_forbidden_edges<=6:
        raise ValueError("BO excludes at most six foreign physical pair edges")
    V,a,K,m=_params(s)
    t=foreign_forbidden_edges
    adj=Fraction((a-3)*(a-4)*(a-5),2)-t*(a-4)*(a-5)
    disj=Fraction((a-4)*(a-5),2)-t*(a-5)
    if not adj>0 or not disj>0:
        raise AssertionError("BL cycle half-bound does not survive six arbitrary forbiddens")
    d=s+1
    # Four free ORIGINAL source line-factor choices per root.  The second
    # must avoid all <=4 root pins and four first-root other line IDs
    # and at most 3 previously chosen line IDs.  d>=33 makes it possible.
    if d<=11:
        raise AssertionError("original GQ greedy distinct-line Hall source bound fails")
    r=every_fixed_original_g_good_root_pin_majority(s)
    N=r["number_true_original_point_cherries"]
    G=r["number_true_original_cherries_with_regular_two_pinned_images_lower"]
    if not (4*G>3*N and N>4):
        raise AssertionError("BL source-root pin regularity majority missing")
    pairs_lower=comb(G,2)
    pairs_total=comb(N,2)
    if not 2*pairs_lower>pairs_total:
        raise AssertionError(">half original cherry pairs certified simultaneously repairable")
    return {
        "s":s, "a":a, "V":V, "m":m, "d":d,
        "max_other_occupied_edge_exclusions":t,
        "adjacent_pins_physical_C6_survivors_lower":adj,
        "disjoint_pins_physical_C6_survivors_lower":disj,
        "max_protected_actual_original_opposite_factors":4,
        "max_combined_other_original_source_factors":8,
        "max_whole_original_factor_image_transpositions":8,
        "total_true_original_cherries":N,
        "pin_regular_original_cherries_lower":G,
        "simultaneously_repairable_DISTINCT_true_original_root_pairs_lower":pairs_lower,
        "all_distinct_true_original_root_pairs":pairs_total,
        "simultaneously_repairable_pair_fraction_lower":Fraction(pairs_lower,pairs_total),
        "strict_more_than_half_true_original_root_pairs":True,
        "one_COMMON_new_gprime_for_EACH_selected_two_roots_not_all_roots":True,
        "original_input_g_positive_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def occupied_two_pin_C6_avoiding(E,a,pin1,pin2,forbidden):
    """Finite independent physical cycle witness, not a stochastic image draw.

    Only invoked on genuine small symplectic W32/W34 in tests; asymptotic
    existence proven by the mathematical AA4-BO cycle-removal bound.
    """
    E={tuple(sorted(e)) for e in E}
    p1,p2=tuple(sorted(pin1)),tuple(sorted(pin2))
    F={tuple(sorted(e)) for e in forbidden}
    if p1==p2 or not {p1,p2}<=E or F&{p1,p2}:
        raise ValueError("different occupied root pins must be allowed")
    if len(F)>6:
        raise ValueError("at most six foreign physical pair edges can be excluded")
    def edge(u,v):
        return (u,v) if u<v else (v,u)
    common=set(p1)&set(p2)
    if len(common)==1:
        v=next(iter(common))
        u=next(t for t in p1 if t!=v)
        w=next(t for t in p2 if t!=v)
        others=[t for t in range(a) if t not in (u,v,w)]
        for x,y,z in permutations(others,3):
            cycle=(p1,p2,edge(w,x),edge(x,y),edge(y,z),edge(z,u))
            if len(set(cycle))==6 and set(cycle)<=E and not set(cycle)&F:
                return tuple(sorted(cycle))
    elif not common:
        for u,v in (p1,p1[::-1]):
            for w,x in (p2,p2[::-1]):
                others=[t for t in range(a) if t not in (u,v,w,x)]
                for y,z in permutations(others,2):
                    cycle=(p1,edge(v,y),edge(y,w),p2,edge(x,z),edge(z,u))
                    if len(set(cycle))==6 and set(cycle)<=E and not set(cycle)&F:
                        return tuple(sorted(cycle))
    else:
        raise AssertionError("two different physical pair edges cannot share both endpoints")
    return None


def genuine_root_Q_avoiding_opposite_ids(model,side,p,flags,forbidden):
    """True original W3 root B/C4 plus four REAL different opposite IDs.

    For h>=5 each source factor has d>=33 opposite incidence choices:
    exclude <=4 joint pins + <=4 prior Q free IDs + <=3 greedy used IDs.
    """
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    if type(side) is not int or side not in (0,1):
        raise ValueError("typed original source side required")
    roots=(byP,byL)[side]
    if type(p) is not int or p<0 or p>=V:
        raise ValueError("actual original source factor invalid")
    flags=tuple(flags)
    if len(flags)!=2 or len(set(flags))!=2 or any(
        type(j) is not int or j not in roots[p] for j in flags):
        raise ValueError("two distinct genuine incidence flags through root required")
    given={inc[j][1-side] for j in flags}
    if len(given)!=2:
        raise AssertionError("original root source opposite ids are not different")
    banned=set(forbidden)|given
    first=(f,g)[side]
    inv={edge:i for i,edge in enumerate(first)}
    if len(inv)!=V:
        raise ValueError("complete original typed source map must be injective")
    others=tuple(v for v in range(a) if v not in first[p])
    for four in combinations(others,4):
        _,_,patterns=_full_four_patterns(four,set(inv))
        for kind,edges in patterns:
            if kind!="C4":
                continue
            factors=tuple(inv[e] for e in edges)
            if len(set(factors))!=4 or p in factors:
                raise AssertionError("non-original 4-point factor source C4")
            used=set(banned)
            new=[]
            for src in factors:
                avail=next((j for j in roots[src] if inc[j][1-side] not in used),None)
                if avail is None:
                    break
                new.append(avail)
                used.add(inc[avail][1-side])
            if len(new)==4:
                Q=tuple(sorted(flags+tuple(new)))
                if len(set(Q))!=6 or len({inc[j][1-side] for j in Q})!=6:
                    raise AssertionError("genuine original six distinct source incidences/opposite factors")
                degrees=Counter(z for j in Q for z in first[inc[j][side]])
                if len(degrees)!=6 or set(degrees.values())!={2}:
                    raise AssertionError("original fixed first side not B/C4")
                return Q
    return None


def simultaneous_two_original_cherries(model,side,root1,root2,*,require_regular=True):
    """One REAL common full globally injected map accepts two real original Q.

    Both original cherries must be of same typed source side. For h>=5
    and both individually BL-regular, ALL-h proof guarantees success.
    At small h return None (no extrapolation from finite W32/W34).
    """
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    if type(side) is not int or side not in (0,1):
        raise ValueError("original typed side must be 0 or 1")
    roots=(byP,byL)[side]
    pairs=[]
    allpins=set()
    other=(g,f)[side]
    for entry in (root1,root2):
        try: p,flags=entry
        except (TypeError,ValueError):
            raise ValueError("each root must have factor ID and two actual incidence IDs") from None
        if type(p) is not int or not 0<=p<V:
            raise ValueError("actual original source root out of range")
        flags=tuple(flags)
        if len(flags)!=2 or len(set(flags))!=2 or any(
            type(j) is not int or j not in roots[p] for j in flags):
            raise ValueError("both actual original flags must share their claimed root")
        pins={inc[j][1-side] for j in flags}
        if len(pins)!=2:
            raise AssertionError("source factor root opposite neighbor uniqueness fails")
        pairs.append((p,flags,pins))
        allpins|=pins
    if (pairs[0][0],frozenset(pairs[0][1]))==(pairs[1][0],frozenset(pairs[1][1])):
        raise ValueError("two DISTINCT original source cherries required")
    missing=missing_endpoint_degrees(other,a)
    t=(a-4)//8
    regular=all(max(missing[u] for src in pins for u in other[src])<=t
                for _,_,pins in pairs)
    if require_regular and s>=32 and not regular:
        raise ValueError("at least one actual original cherry fails BL-LOCAL")
    constructed=[]
    used_free=set()
    previous_target=set()
    for index,(p,flags,pins) in enumerate(pairs):
        Q=genuine_root_Q_avoiding_opposite_ids(model,side,p,flags,
                  (allpins|used_free)-pins)
        if Q is None:
            if require_regular and s>=32:
                raise AssertionError("true ORIGINAL sixflag root C4/Hall source construction missing")
            return None
        free={inc[j][1-side] for j in Q}-pins
        if len(free)!=4 or free & (allpins|used_free):
            raise AssertionError("opposite actual source factor disjointness across roots failed")
        ownimages={other[src] for src in pins}
        if index==0:
            excluded={other[src] for src in allpins-pins}
        else:
            excluded=previous_target-ownimages
        if len(excluded)>6 or excluded & ownimages:
            raise AssertionError("two-root forbidden physical edge budget exceeded")
        target=occupied_two_pin_C6_avoiding(other,a,
                    other[inc[flags[0]][1-side]],
                    other[inc[flags[1]][1-side]],excluded)
        if target is None:
            if require_regular and s>=32:
                raise AssertionError("BL-LOCAL and 6-foreign-edge C6 lower contradicted")
            return None
        candidate=candidate_from_target(model,side,p,flags,Q,target)
        constructed.append(candidate)
        previous_target.update(target)
        used_free.update(free)
    result=original_multi_cherry_candidate_minimum(model,side,constructed)
    if result["exact_minimum_image_transpositions"]>8:
        raise AssertionError("two four-source-per-root constraint union needs >8 transpositions")
    if len(result["accepted_original_seven_GF5_tags"])!=2:
        raise AssertionError("one globally completed map does not accept two true original Q")
    result["both_original_cherries"]=((pairs[0][0],pairs[0][1]),(pairs[1][0],pairs[1][1]))
    result["all_original_opposite_pin_ids"]=tuple(sorted(allpins))
    result["all_input_original_pin_images"]=tuple(other[i] for i in sorted(allpins))
    result["actual_Qs_are_distinct"]=constructed[0]["Q"]!=constructed[1]["Q"]
    result["same_original_source_incidence_Q_ids_not_resampled"]=True
    result["all_h_certified_if_h>=5_and_each_BL_pin_regular"]=s>=32 and regular
    result["this_witness_gprime_may_depend_on_the_chosen_root_PAIR"]=True
    result["original_unmodified_f_g_lower_NOT_PROVED"]=True
    return result
