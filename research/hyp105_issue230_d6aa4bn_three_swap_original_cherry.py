"""AA4-BN: <=3 original source FACTOR image swaps, not 4, for good roots.

NEW genuine original W(3,s), ALL dyadic h>=22; EVERY already fixed
fully globally injected correlated f,g; EVERY original point cherry
with TWO opposite line physical pin endpoints locally regular as in
AA4-BL: one HISTORICALLY GF5-positive rooted B/A sixflag is reachable
after <=3 WHOLE original LINE image transpositions, preserving BOTH
root source LINE factor pins, the physical right support, the entire
original f, and all SIX genuine original source incidence IDs.

KEY NEW GQ partial-linearity + physical C4 lemma:
bad original POINT factor count <=10(a-1) outside rooted physical C4s.
A TRUE original LINE factor with all d points bad consumes binom(d,2)
UNIQUE ORIGINAL point pairs, hence <=binom(10(a-1),2)/binom(d,2)
bad original source LINE factors <=400s. For h>=22 this is
<(a-4)/4. In each AA4-BL pinned physical C6 family, excluding all
physical pair edges assigned to bad source LINE factors still leaves a
pinned C6. One of its 4 non-pinned right edges is the CURRENT image
of a source LINE that lies on a GOOD source-side physical C4. Include
the corresponding genuine incidence as a third pinned true source
flag. Then repair only THREE remaining real original source LINE
factor images by full globally legal transpositions.

A LOCAL-REPAIR theorem only. Do NOT assert positive motifs on original
unchanged fully fixed g, one repair for all roots, or Branch A/B/C.
"""
from collections import Counter
from itertools import combinations,permutations

from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import _params
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bj_cherry_hall_defect import _full_four_patterns
from hyp105_issue230_d6aa4bm_four_swap_root_BA_repair import (
    _edge,_root_flags,missing_endpoint_degrees,
)
from hyp105_issue230_d6aa4q_two_sided_seven_join import independent_joint_classify
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked


def original_BN_all_h_three_swap_certificate(s):
    """Formal all-h big-integer scope; NOT a fake high-s symplectic GQ."""
    if type(s) is not int or s<2**22 or s&(s-1):
        raise ValueError("certified 3-swap theorem requires dyadic h>=22")
    V,a,K,m=_params(s)
    d=s+1
    n=a-2
    # Missing physical point-side edges INSIDE the root complement:
    # at most m of them. At most eight complement-coordinate vertices
    # have missing degree >=(n-3)/4 for all a>=261.
    bad_vertex_bound=(8*m)//(n-3)
    if bad_vertex_bound>8:
        raise AssertionError("at most 8 high-missing-degree root complement coordinates")
    # + 2 pinned physical endpoints, each original factor pair-edge
    # image involving one of <=10 bad physical coordinates is bad.
    b=(2+bad_vertex_bound)*(a-1)
    bad_line_bound=b*(b-1)//(d*(d-1))
    if a*a>4*s**3 or bad_line_bound>400*s:
        raise AssertionError("root physical bad points or original GQ pair-incidence bound")
    if 4*bad_line_bound>=a-4:
        raise AssertionError("too many bad genuine opposite LINE source factors for pinned C6 repair")
    # Original AA4-BL gives >= HALF the clean-pinned-C6 constructed
    # families. Deleting an additional bad source-LINE edge damages
    # at most (a-4)(a-5) cycles if the pins are adjacent; at most
    # (a-5) cycles if their physical edges are disjoint.
    adjacent_numer=(a-3)*(a-4)*(a-5)-2*bad_line_bound*(a-4)*(a-5)
    disjoint_numer=(a-4)*(a-5)-2*bad_line_bound*(a-5)
    if adjacent_numer<=0 or disjoint_numer<=0:
        raise AssertionError("all-h 3-swap pinned 6cycle survivor not positive")
    if 400*s*4>=a-4:
        raise AssertionError("uniform analytic 400s <(a-4)/4 fails")
    return {
        "s":s,"h":s.bit_length()-1,"V":V,"a":a,"m":m,"d":d,
        "max_root_complement_physical_high_missing_vertices":bad_vertex_bound,
        "all_source_point_factors_not_usable_in_any_root_disjoint_physical_C4_max":b,
        "genuine_original_line_factors_all_of_whose_d_points_bad_upper":bad_line_bound,
        "simple_algebraic_original_BAD_LINE_limit":400*s,
        "strict_bad_line_support_lt_a_minus4_over4":True,
        "root_pin_6cycle_with_NO_BAD_line_images_adjacent_twice_lower":adjacent_numer,
        "root_pin_6cycle_with_NO_BAD_line_images_disjoint_twice_lower":disjoint_numer,
        "original_source_LINE_image_swap_upper":3,
        "two_source_PIN_line_images_plus_ONE_more_actual_SOURCE_LINE_image_unchanged":True,
        "for_EVERY_f_g_and_EVERY_aa4bl_regular_true_source_cherry":True,
        "genuine_original_source_point_PAIR_uniqueness_REQUIRED":True,
        "one_repaired_map_for_all_regular_original_roots_NOT_PROVED":True,
        "unchanged_fixed_f_g_positive_not_proved":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def original_root_physical_good_C4_index(model,side,p):
    """TRUE source C4 index for complete given f or dual g, no right changes."""
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    if type(side) is not int or side not in (0,1):
        raise ValueError("real original source side must be 0=POINT or 1=LINE")
    if type(p) is not int or not 0<=p<V:
        raise ValueError("real original source factor ID invalid")
    first=(f,g)[side]
    inv={e:i for i,e in enumerate(first)}
    root=set(first[p])
    usable=[v for v in range(a) if v not in root]
    ret={}
    for four in combinations(usable,4):
        _,_,patterns=_full_four_patterns(four,set(inv))
        for kind,edges in patterns:
            if kind!="C4":continue
            factors=tuple(sorted(inv[e] for e in edges))
            if len(set(factors))!=4 or p in factors:
                raise AssertionError("physical C4 inverted true source injection invalid")
            for factor in factors:ret.setdefault(factor,factors)
    return ret


def _rooted_cycle_candidates(occupied,a,e1,e2):
    """Two AAA4-BL rooted cycle families, explicitly six distinct edges."""
    E=set(occupied)
    if e1 not in E or e2 not in E or e1==e2:
        raise ValueError("two different original root physical images must be occupied")
    common=set(e1)&set(e2)
    seen=set()
    if len(common)==1:
        middle=next(iter(common))
        u=next(v for v in e1 if v!=middle)
        w=next(v for v in e2 if v!=middle)
        rest=tuple(v for v in range(a) if v not in (u,middle,w))
        for x,y,z in permutations(rest,3):
            edges=tuple(sorted((e1,e2,_edge(w,x),_edge(x,y),_edge(y,z),_edge(z,u))))
            if len(set(edges))==6 and all(t in E for t in edges) and edges not in seen:
                seen.add(edges)
                yield edges
    elif len(common)==0:
        for u,v in (e1,e1[::-1]):
            for w,x in (e2,e2[::-1]):
                rest=tuple(t for t in range(a) if t not in (u,v,w,x))
                for y,z in permutations(rest,2):
                    edges=tuple(sorted((e1,e2,_edge(v,y),_edge(y,w),_edge(x,z),_edge(z,u))))
                    if len(set(edges))==6 and all(t in E for t in edges) and edges not in seen:
                        seen.add(edges)
                        yield edges
    else:
        raise AssertionError("two distinct physical graph edges cannot share both endpoints")


def _find_true_source_Q_with_locked_extra_line(inc,by_first,first_root_flags,
                                               first_four_source_factors,
                                               selected_point_source,selected_LINE):
    """Greedy true incidence completion; recurse for small W32/W34 oracles."""
    chosen=(tuple(first_root_flags)+
            (next((j for j in by_first[selected_point_source]
                   if inc[j][1 if inc[j][0]==selected_point_source else 0]==selected_LINE),-1),))
    # Caller passes explicit source side in the reconstruction below;
    # this helper is kept unused to avoid guessing dual incidence type.
    raise AssertionError("use the side-explicit source selection in repair")


def original_fixed_pair_three_swap_cherry_repair(model,side,p,flags,
                                                *,require_h22_regular=True):
    """Construct ≤3 source factor image swaps with THREE original LINE pins.

    For h>=22 and a physical AA4-BL regular root existence is PROVED.
    For genuine W32/W34, search is a finite falsifier only and may
    return None if this stronger three-swap witness doesn't exist.
    """
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    if type(side) is not int or side not in (0,1):
        raise ValueError("source side must be exactly POINT0 or LINE1")
    by=(byP,byL)[side]
    flags=_root_flags(inc,by,side,p,flags)
    first=(f,g)[side]
    second=(g,f)[side]
    pins=tuple(inc[j][1-side] for j in flags)
    if pins[0]==pins[1]:
        raise AssertionError("genuine original flag IDs at common source factor must have distinct opposite factors")
    e1,e2=(second[x] for x in pins)
    miss=missing_endpoint_degrees(second,a)
    regular=max(miss[v] for v in set(e1+e2))<=(a-4)//8
    certified=s>=2**22 and regular and require_h22_regular
    if require_h22_regular and s>=2**22 and not regular:
        raise ValueError("physical original root pair fails local missing-degree hypothesis")

    firstgood=original_root_physical_good_C4_index(model,side,p)
    # SOURCE-LINE -> (a real source POINT neighbor appearing on a
    # physical original C4, and its physical four source factor IDs).
    by_opp=(byL,byP)[side]
    usable={}
    for opp in range(V):
        if opp in pins:continue
        for qid in by_opp[opp]:
            q=inc[qid][side]
            if q in firstgood:
                usable[opp]=(q,firstgood[q],qid)
                break
    owner={edge:i for i,edge in enumerate(second)}
    if len(owner)!=V:
        raise AssertionError("globally injected original source right physical pair support required")

    for target in _rooted_cycle_candidates(second,a,e1,e2):
        free_t=tuple(e for e in target if e not in (e1,e2))
        if len(free_t)!=4:raise AssertionError("rooted C6 four free physical edges")
        for fixed_edge in free_t:
            already_good_line=owner[fixed_edge]
            if already_good_line not in usable:continue
            chosen_point,four_sources,flagid=usable[already_good_line]
            # Build real source six-incidence ID Q, with 3 EXACT source
            # line IDs already pinned (two root plus this one current
            # right-edge image). Greedily complete other 3 original
            # point source factors using actual source GQ neighbors.
            used=set(pins)|{already_good_line}
            selected=[*flags,flagid]
            other_points=[q for q in four_sources if q!=chosen_point]
            if len(other_points)!=3:
                raise AssertionError("actual original point C4 needs exactly three other source factors")
            def extend(k):
                if k==len(other_points):return tuple(sorted(selected))
                q=other_points[k]
                for j in by[q]:
                    oid=inc[j][1-side]
                    if oid in used:continue
                    used.add(oid)
                    selected.append(j)
                    result=extend(k+1)
                    if result is not None:return result
                    selected.pop()
                    used.remove(oid)
                return None
            Q=extend(0)
            if Q is None:continue
            if len(Q)!=6 or len(set(Q))!=6 or not set(flags)<set(Q):
                raise AssertionError("real original six-ID source invariant")
            fixed_orig={*pins,already_good_line}
            selected_opp={inc[j][1-side] for j in Q}
            remaining=tuple(sorted(selected_opp-fixed_orig))
            desired=tuple(sorted(set(free_t)-{fixed_edge}))
            if len(remaining)!=3 or len(desired)!=3:
                raise AssertionError("three true original unpinned source factor IDs/target edges required")
            updated=list(second)
            where={edge:factor for factor,edge in enumerate(updated)}
            swaps=[]
            for src,dst in zip(remaining,desired):
                if updated[src]==dst:continue
                donor=where[dst]
                if donor in fixed_orig:
                    raise AssertionError("three genuine original source factor images must stay pinned")
                old=updated[src]
                updated[src],updated[donor]=updated[donor],updated[src]
                where[dst]=src
                where[old]=donor
                swaps.append((src,donor))
            if len(swaps)>3 or len(set(updated))!=V or set(updated)!=set(second):
                raise AssertionError("broken source global image injection / <=3 swap distance")
            if any(updated[src]!=second[src] for src in fixed_orig):
                raise AssertionError("changed original pinned source line image")
            rebuilt=dict(model)
            rebuilt["right_labels" if side==0 else "left_labels"]=tuple(updated)
            profiles=[]
            for typ,images in ((0,rebuilt["left_labels"]),(1,rebuilt["right_labels"])):
                counts=Counter()
                for j in Q:
                    counts.update(images[inc[j][typ]])
                if len(counts)!=6 or set(counts.values())!={2}:
                    raise AssertionError("true ORIGINAL sixflags fail physical 2regularity after swap")
                sizes=tuple(sorted(Counter(inc[j][typ] for j in Q).values()))
                profiles.append({(1,1,1,1,1,1):"A",(1,1,1,1,2):"B",
                                 (2,2,2):"C"}.get(sizes))
            tag=independent_joint_classify(
                Q,profiles[0],profiles[1],inc,
                rebuilt["left_labels"],rebuilt["right_labels"])
            want="B-left/A-right" if side==0 else "A-left/B-right"
            if tag!=want:
                raise AssertionError("incorrect true-original sevenGF5 B/A class")
            if s==2:
                historical=classify_seven_prechecked(Q,rebuilt["left_labels"],
                                                      rebuilt["right_labels"],inc)
                if historical!=tag:
                    raise AssertionError("historical TRUE W32 original GF5 class oracle disagrees")
            return {
                "s":s,"V":V,"a":a,"side":side,"original_root_source_factor":p,
                "original_root_two_actual_incidence_flag_IDs":flags,
                "true_original_six_incidence_flag_IDs":Q,
                "original_source_third_LINE_factor_already_correct":already_good_line,
                "original_source_three_pinned_opposite_factors":tuple(sorted(fixed_orig)),
                "same_physical_original_C6_target":target,
                "swaps_of_REAL_original_FACTOR_images":tuple(swaps),
                "number_transpositions":len(swaps),
                "complete_opposite_original_map_before":tuple(second),
                "complete_opposite_original_map_after":tuple(updated),
                "repaired_full_original_model":rebuilt,
                "historical_genuine_GF5_accepted_seven_class":tag,
                "good_original_line_source_factors_count":len(usable),
                "physical_root_pin_regular":regular,
                "covered_by_all_h_three_swap_theorem":certified,
                "unmodified_original_f_g_motif_lower_NOT_PROVED":True,
                "one_global_repair_for_all_cherries_NOT_PROVED":True,
                "root_230":"OPEN_WITH_FORMAL_BLOCKER"}
    if certified:
        raise AssertionError("proved all-h good-root right pinned C6 cannot have all four free physical edges from bad source LINE factors")
    return None
