"""AA4-BO: MANY distinct <=3-swap original B/A repairs, ONE SAME original Q.

Genuine W(3,2^h), h>=22, EVERY already fully fixed arbitrary
correlated original point/LINE injections f,g, and EVERY actual original
point-source cherry whose two right pinned edge endpoints satisfy
AA4-BL local physical missing-degree condition:
There exists ONE genuine SIX-DISTINCT original incidence Q through that
root, and ONE additional real original LINE factor ell from Q whose
current global right physical image is already correctly placed, such
that at least ceil((a-5)/4) DIFFERENT complete right source-factor
maps g' in the <=3 WHOLE-original-LINE-image transposition ball of
the GIVEN g preserve f, occupied right physical support and all THREE
actual original line factor image pins and accept THAT SAME Q as
historically positive B/A. Root-dependent Q and g' permitted.
Typed POINT/LINE dual holds. NOT a result about unmodified g.

Novelty beyond #578 (>=many radius FOUR maps for selected root)
and parent #581 (one radius THREE map) is the SAME-Q, SAME-THREE-PINS,
>=Omega(a)=Omega(s^(3/2)) DISTINCT radius THREE repaired maps.

Proof: From #581 TRUE GQ source POINT-pair packing, <=Bbad genuine
opposite LINE factor images are unusable for the fixed source root.
After removing all these from AA4-BL's pinned C6 families, retain
R_adj >= (a-4)(a-5)((a-3)/2-Bbad), or
R_disj >= (a-5)((a-4)/2-Bbad) distinct occupied C6. Each has
exactly FOUR free right physical edges. Their union is contained in
U_adj <= a(a-3)/2 possible physical pair edges, or
U_disj <= 4(a-4). Thus by incidence pigeonhole some current GOOD
original right LINE image t lies on >=ceil(4R/U) different such
C6. This is >=ceil((a-5)/4) for h>=22. Keep its current SOURCE
LINE factor and true incidence Q fixed and repair the other 3 actual
source LINE image positions; distinct C6 edge sets => distinct
full globally injected repaired g'. No per-Q independent random map.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations
from math import ceil

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bn_three_swap_original_cherry import (
    original_BN_all_h_three_swap_certificate,
    original_root_physical_good_C4_index,
    _rooted_cycle_candidates,
)
from hyp105_issue230_d6aa4bm_four_swap_root_BA_repair import (
    _root_flags,missing_endpoint_degrees,
)
from hyp105_issue230_d6aa4q_two_sided_seven_join import independent_joint_classify
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked


def _ceil_fraction(z):
    return (z.numerator+z.denominator-1)//z.denominator


def all_h_shared_original_Q_three_swap_multiplicity(s):
    """Exact all-h certificate; no high-h artificial GQ graph materialized."""
    z=original_BN_all_h_three_swap_certificate(s)
    a=z["a"]
    B=z["genuine_original_line_factors_all_of_whose_d_points_bad_upper"]
    adjacent_R=Fraction((a-3)*(a-4)*(a-5),2)-B*(a-4)*(a-5)
    disjoint_R=Fraction((a-4)*(a-5),2)-B*(a-5)
    # For a fixed ordered pair of pinned e1,e2, the canonical adjacent
    # 6cycle free edges are w-x,x-y,y-z,z-u: 2(a-3)
    # root-to-free plus C(a-3,2) free-to-free physical edges.
    adjacent_U=a*(a-3)//2
    # The canonical disjoint-pin 6cycles only use four categories of
    # physical free edge, each incident to one of four pinned vertices:
    # at most 4(a-4) possible distinct occupied edge positions.
    disjoint_U=4*(a-4)
    adj_count=_ceil_fraction(4*adjacent_R/adjacent_U)
    dis_count=_ceil_fraction(4*disjoint_R/disjoint_U)
    target=(a-5+3)//4
    if not (adjacent_R>0 and disjoint_R>0 and
            adj_count>=target and dis_count>=target):
        raise AssertionError("shared Q 3swap multiplicity count does not reach ceil((a-5)/4)")
    return {
        **z,
        "minimum_distinct_C6_targets_surviving_bad_original_line_images_adjacent":
            adjacent_R,
        "minimum_distinct_C6_targets_surviving_bad_original_line_images_disjoint":
            disjoint_R,
        "max_possible_nonroot_target_edges_adjacent":adjacent_U,
        "max_possible_nonroot_target_edges_disjoint":disjoint_U,
        "incidence_pigeonhole_same_one_good_original_LINE_image_adjacent":
            adj_count,
        "incidence_pigeonhole_same_one_good_original_LINE_image_disjoint":
            dis_count,
        "uniform_same_Q_same_three_LINE_pins_distinct_global_three_swap_maps_lower":
            target,
        "true_original_source_six_ID_Q_common_to_ALL_repaired_maps":True,
        "all_three_source_LINE_factor_images_unchanged_in_ALL_repaired_maps":True,
        "one_fixed_f_and_same_right_occupied_support":True,
        "all_original_point_cherries_covered_by_same_single_Q_NOT_PROVED":True,
        "unmodified_original_f_g_positive_lower_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def _genuine_same_Q_at_good_right_owner(inc,by_source,by_opposite,
                                        side,point_source_root,root_flag_ids,
                                        original_good_physical_C4,
                                        fixed_line_owner):
    """Choose ONE true original Q containing three pinned source LINE IDs.

    Keeps actual original root flags, plus a new incidence on owner
    of a candidate right C6 free edge. Remaining three chosen from
    actual original source neighbors; all opposite factors distinct.
    """
    chosen_point,four_points,flagid=original_good_physical_C4[fixed_line_owner]
    ids=list(root_flag_ids)+[flagid]
    root_opp={inc[j][1-side] for j in root_flag_ids}
    used=root_opp|{fixed_line_owner}
    if len(used)!=3 or inc[flagid][side]!=chosen_point or inc[flagid][1-side]!=fixed_line_owner:
        raise AssertionError("wrong third actual original factor pin or six-ID root")
    for q in (v for v in four_points if v!=chosen_point):
        found=None
        for j in by_source[q]:
            v=inc[j][1-side]
            if v not in used:
                found=j
                break
        if found is None:
            return None
        ids.append(found)
        used.add(inc[found][1-side])
    Q=tuple(sorted(ids))
    if len(Q)!=6 or len(set(Q))!=6 or len(used)!=6:
        raise AssertionError("REAL original six source incidence flags / six actual opposite IDs")
    return Q


def enumerate_same_Q_three_swap_repairs(model,side,p,root_flags,
                                        *,min_target_count=1,verify=True):
    """Finite true-W32/W34 exhaustive certificate with root-dependent ONE Q.

    Returns ORIGINAL source sixflag set Q and complete global repaired
    opposite maps, all within <=3 swaps from ONE GIVEN opposite map,
    all sharing the SAME three untouched real source factor IDs.
    Does NOT claim h>=22 from finite original W32/W34.
    """
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    if type(side) is not int or side not in (0,1):
        raise ValueError("typed genuine original source side must be POINT0 or LINE1")
    if type(p) is not int or not 0<=p<V:
        raise ValueError("true original source factor ID")
    by=(byP,byL)[side]
    root_flags=_root_flags(inc,by,side,p,tuple(root_flags))
    source=(f,g)[side]
    opposite=(g,f)[side]
    root_opp=tuple(inc[j][1-side] for j in root_flags)
    e1,e2=tuple(opposite[j] for j in root_opp)
    owner={edge:i for i,edge in enumerate(opposite)}
    good_index=original_root_physical_good_C4_index(model,side,p)
    opposite_by=(byL,byP)[side]
    good_line={}
    for line_id,actual_flags in enumerate(opposite_by):
        if line_id in root_opp:continue
        for j in actual_flags:
            point_id=inc[j][side]
            if point_id in good_index:
                good_line[line_id]=(point_id,good_index[point_id],j)
                break
    candidates=defaultdict(set)
    all_physical_targets=set()
    for c6 in _rooted_cycle_candidates(opposite,a,e1,e2):
        if c6 in all_physical_targets:
            raise AssertionError("rooted C6 family contains non-unique target")
        all_physical_targets.add(c6)
        free=tuple(edge for edge in c6 if edge not in (e1,e2))
        if len(free)!=4:raise AssertionError("rooted original 6cycle has four unpinned edges")
        for edge in free:
            line_id=owner[edge]
            if line_id in good_line:
                candidates[line_id].add(c6)
    if not candidates:
        return None
    # Maximize number of distinct right 6cycle targets for the same
    # TRUE original source factor ell and same resulting genuine Q.
    best_line=min(candidates,key=lambda key:(-len(candidates[key]),key))
    Q=_genuine_same_Q_at_good_right_owner(
        inc,by,opposite_by,side,p,root_flags,good_line,best_line)
    if Q is None:return None
    third_edge=opposite[best_line]
    immutable=frozenset(root_opp+(best_line,))
    source_line_ids=frozenset(inc[j][1-side] for j in Q)
    remaining=tuple(sorted(source_line_ids-immutable))
    if len(remaining)!=3:raise AssertionError("three source factors need movable images")
    expected="B-left/A-right" if side==0 else "A-left/B-right"
    maps=[]
    witness_paths=[]
    for target in sorted(candidates[best_line]):
        free=tuple(sorted(set(target)-{e1,e2,third_edge}))
        if len(free)!=3:raise AssertionError("target must contain all THREE fixed original source LINE images")
        original=tuple(opposite)
        current=list(opposite)
        where={edge:j for j,edge in enumerate(current)}
        swaps=[]
        for source_id,dest in zip(remaining,free):
            if current[source_id]==dest:continue
            donor=where[dest]
            if donor in immutable:raise AssertionError("a pinned source factor was about to donate")
            old=current[source_id]
            current[source_id],current[donor]=current[donor],current[source_id]
            where[dest]=source_id
            where[old]=donor
            swaps.append((source_id,donor))
        after=tuple(current)
        if (len(swaps)>3 or len(set(after))!=V or set(after)!=set(original)
            or any(after[k]!=original[k] for k in immutable)):
            raise AssertionError("not a pin-preserving whole-original-factor three-swap complete map")
        if verify:
            rebuilt=dict(model)
            rebuilt["right_labels" if side==0 else "left_labels"]=after
            histories=[]
            for typ,images in ((0,rebuilt["left_labels"]),(1,rebuilt["right_labels"])):
                degrees=Counter(v for j in Q for v in images[inc[j][typ]])
                if len(degrees)!=6 or set(degrees.values())!={2}:
                    raise AssertionError("true original Q not physically 2regular on both sides")
                multiplicities=tuple(sorted(Counter(inc[j][typ] for j in Q).values()))
                histories.append({(1,1,1,1,1,1):"A",
                                  (1,1,1,1,2):"B",
                                  (2,2,2):"C"}.get(multiplicities))
            tag=independent_joint_classify(
                Q,histories[0],histories[1],inc,
                rebuilt["left_labels"],rebuilt["right_labels"])
            if tag!=expected:
                raise AssertionError("historically GF5 accepted true original SAME Q classification fails")
            if s==2:
                historical=classify_seven_prechecked(
                    Q,rebuilt["left_labels"],rebuilt["right_labels"],inc)
                if historical!=expected:
                    raise AssertionError("independent W32 historical original sevenGF5 tag disagrees")
        maps.append(after)
        witness_paths.append(tuple(swaps))
    if len(set(maps))!=len(maps) or len(maps)<min_target_count:
        raise AssertionError("different physical target C6 must give distinct complete repaired source maps")
    return {
        "s":s,"V":V,"a":a,"original_root_side":side,"original_root_factor":p,
        "root_two_real_original_incidence_IDs":root_flags,
        "SAME_six_actual_original_incidence_IDs_Q_for_every_map":Q,
        "three_unmodified_real_original_opposite_source_factor_IDs":
            tuple(sorted(immutable)),
        "third_opposite_source_factor_ID_already_correct":best_line,
        "original_complete_opposite_global_map":tuple(opposite),
        "different_COMPLETE_repaired_original_opposite_global_maps":tuple(maps),
        "all_distinct_physical_occupied_root_C6_targets":tuple(sorted(candidates[best_line])),
        "each_complete_repair_swaps":tuple(witness_paths),
        "distinct_GLOBAL_repaired_maps_with_SAME_Q_AND_three_pins":len(maps),
        "best_one_good_line_target_incidence":len(candidates[best_line]),
        "all_original_physical_root_C6_targets":len(all_physical_targets),
        "certified_h22_by_prior_pin_regular":
            s>=2**22 and max(missing_endpoint_degree for missing_endpoint_degree in
                           (sum((min(u,v),max(u,v)) not in owner for v in range(a) if u!=v)
                            for u in set(e1+e2)))<=(a-4)//8,
        "original_f_g_UNCHANGED_positive_NOT_PROVED":True,
        "one_map_simultaneously_for_all_roots_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
