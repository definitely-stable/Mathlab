"""HYP-105 #230 AA4-AT: all-h seven-GF5 GLOBAL 5-swap boundary theorem.

NEW exact rooted physical 6-edge 2-factor counts (28,18,6) and
class-resolved source-line fiber upper, including GF5 necessary floor
weighted changes; signed multi-swap original-fiber support identity was
known for single swaps (#493), do not rebrand it as new.

IMPORTANT: bound is O(s^12), much too large to turn positive repaired
D6 witnesses into an Omega(s^6) lower at adversarial ORIGINAL f,g.
"""
from collections import Counter
from itertools import combinations, combinations_with_replacement
from math import comb, factorial, perm

from hyp105_issue230_d6aa4r_quenched_original_d6 import _params
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ar_five_swap_original_D6 import (
    repair_original_D6_with_at_most_five_line_swaps,
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import (
    classify_seven_prechecked, R3_CERTIFIED_FLOORS, seven_census,
)

LEFT_TAG_TYPES = {
    "D6": "A",
    "A-left/B-right": "A",
    "B-left/A-right": "B",
    "B/B-overlap": "B",
    "B/B-disjoint": "B",
    "C/A": "C",
    "C/B": "C",
}
assert set(LEFT_TAG_TYPES) == set(R3_CERTIFIED_FLOORS)
EXACT_ROOTED_EXPECTED = {"A":28, "B":18, "C":6}
LEFT_MAX_WEIGHT = {
    t:max(R3_CERTIFIED_FLOORS[k] for k,side in LEFT_TAG_TYPES.items() if side==t)
    for t in ("A","B","C")
}


def rooted_k6_2regular_multigraph_oracle():
    """Independently enumerate ALL 130 physical K6 2-regular edge MULTISETS.

    The root physical edge e=(0,1) is counted WITH multiplicity. These
    represent A (six different source point factors), B (one source
    point factor twice), C (three doubled source point factors).
    Physical disconnected two-triangles included in A upper intentionally.
    """
    E=tuple(combinations(range(6),2))
    patterns=Counter()
    rooted=Counter()
    for six in combinations_with_replacement(E,6):
        degrees=Counter(v for edge in six for v in edge)
        if len(degrees)!=6 or set(degrees.values())!={2}:
            continue
        multiplicities=Counter(six)
        profile=tuple(sorted(multiplicities.values(),reverse=True))
        kind={
            (1,1,1,1,1,1):"A",
            (2,1,1,1,1):"B",
            (2,2,2):"C",
        }.get(profile)
        if kind is None:
            raise AssertionError("physical 2-factor has unexpected multiplicity")
        patterns[kind]+=1
        rooted[kind]+=multiplicities[(0,1)]
    if patterns!={"A":70,"B":45,"C":15}:
        raise AssertionError("physical six-coordinate rooted patterns changed")
    if rooted!=EXACT_ROOTED_EXPECTED:
        raise AssertionError("fixed physical edge rooted 2-factor count changed")
    return {"all_K6_physical_two_factors_by_profile":dict(patterns),
            "fixed_edge_rooted_occurrence_count_by_profile":dict(rooted),
            "total_multigraphs":sum(patterns.values()),
            "total_rooted_occurrences":sum(rooted.values())}


def all_h_seven_original_line_fiber_bound(s, affected_lines=10):
    """Every fixed original \ell fiber of eligible seven-family Q:
       5!*(28+18+6)*d^6*binom(a-2,4).

    Choose real incidence (p,\ell) (<=d choices). Complete six physical
    coordinates containing global f(p) (<=(a-2 choose 4)). Enumerate
    exactly 28/18/6 physical 2-regular six-edge multisets rooted at
    that physical edge, with root multiplicity counted. Assign the
    other five incidences to the five physical factor edge occurrences
    in <=5! ways; each physical edge has at most ONE original point
    preimage under ONE f, each actual original point admits <=d
    original incident line factors. Invalid real incidence combinations
    and duplicated ORIGINAL incidence IDs only reduce the count.
    """
    if type(affected_lines) is not int or not 0<=affected_lines<=10:
        raise ValueError("at most ten distinct original line factors affected by five swaps")
    V,a,K,m=_params(s)
    d=s+1
    t=min(affected_lines,V)
    C=comb(a-2,4)
    per_line_by_type={typ:factorial(5)*n*d**6*C
                      for typ,n in EXACT_ROOTED_EXPECTED.items()}
    per_line=sum(per_line_by_type.values())
    abs_seven_change=t*per_line
    weighted_by_type={typ:per_line_by_type[typ]*LEFT_MAX_WEIGHT[typ]
                      for typ in ("A","B","C")}
    max_weighted_abs_change=t*sum(weighted_by_type.values())
    if sum(EXACT_ROOTED_EXPECTED.values())!=52:
        raise AssertionError("physical template root 52 invalid")
    if per_line !=6240*d**6*C:
        raise AssertionError("literal left original line capacity identity changed")
    if sum(weighted_by_type.values())!=300312000*d**6*C:
        raise AssertionError("GF5 lower numerator class-resolved cap changed")
    if s>=4:
        # For dyadic s>=4, a^2<=4s^3 follows from physical-minimality
        # and V=s^3+s^2+s+1; d<=5s/4. Hence for TEN lines
        # 62400*d^6*binom(a-2,4)
        # <=62400*(5s/4)^6*(2s^(3/2))^4/24
        # =(5078125/32)*s^12 <160000*s^12.
        if a*a>4*s**3 or d*4>5*s:
            raise AssertionError("minimal true dyadic physical alphabet estimates fail")
        if 10*per_line>160000*s**12:
            raise AssertionError("all-h rooted original seven swap cut O(s12) certificate failed")
    return {
        "s":s,"V":V,"a":a,"K":K,"d":d,
        "number_of_distinct_affected_original_line_factor_IDs":t,
        "true_original_line_incident_flag_choices":d,
        "fixed_original_incidence_sixcoordinate_extensions":C,
        "exact_rooted_physical_multiset_counts":dict(EXACT_ROOTED_EXPECTED),
        "source_line_fiber_cap_by_left_A_B_C":per_line_by_type,
        "total_left_2regular_original_Q_cap_per_original_line":per_line,
        "all_seven_tag_change_abs_bound_for_at_most_t_changed_lines":abs_seven_change,
        "weighted_51palette_GF5_necessary_floor_numerator_change_abs_bound":
            max_weighted_abs_change,
        "maximum_weighted_per_line_by_left_type":weighted_by_type,
        "exact_5swap_bound_on_distinct_lines":10,
        "theorem_new_bound_is_O_s12_not_lower_s6":True,
        "d6_positive_repair_DOES_NOT_PROMOTE_to_original_g":True,
        "original_seven_minimax_proved":False,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def _all_original_left_candidates(model):
    inc=tuple(tuple(x) for x in model["incidences"])
    rows=[]
    for ids,kind in selected_left_six(model):
        ids=tuple(ids)
        lines=frozenset(inc[i][1] for i in ids)
        if len(set(ids))!=6:
            raise AssertionError("not six distinct actual original incidence IDs")
        rows.append((ids,lines,kind))
    if len(rows)!=62370:
        raise AssertionError("not actual W32 62370 original source sixsets")
    return tuple(rows)


def genuine_original_W32_five_swap_seven_boundary(scheme):
    """Full true ORIGINAL 62370 Q seven-tag census and INDEPENDENT sparse
    telescope per each real source line swap, with exact signed GF5 floor.

    Source provenance is genuine W32 only; does not hallucinate W34
    seven-tag physical K6 historical scorer compatibility.
    """
    if scheme not in ("S68","S72","lex","reverse"):
        raise ValueError("known actual original W32 fixed globally injected schemes only")
    model=fixture(1,scheme)
    rows=_all_original_left_candidates(model)
    inc=tuple(tuple(x) for x in model["incidences"])
    f=tuple(tuple(x) for x in model["left_labels"])
    g=tuple(tuple(x) for x in model["right_labels"])
    proof=repair_original_D6_with_at_most_five_line_swaps(model)
    swap_list=tuple(tuple(p) for p in proof["swap_list_of_TRUE_original_LINE_factor_labels"])
    actual_changed_lines=frozenset(x for uv in swap_list for x in uv)
    bound=all_h_seven_original_line_fiber_bound(2,len(actual_changed_lines))
    boundary=tuple(row for row in rows if row[1]&actual_changed_lines)
    if len(boundary)>bound["all_seven_tag_change_abs_bound_for_at_most_t_changed_lines"]:
        raise AssertionError("rooted physical original line-bound falsified")

    def score(right,chosen):
        tags={}
        c=Counter()
        for ids,_,_ in chosen:
            tag=classify_seven_prechecked(ids,f,right,inc)
            if tag is not None:
                tags[ids]=tag
                c[tag]+=1
        return c,tags

    old_count,old_tags=score(g,rows)
    final_g=tuple(proof["right_global_full_injection_after"])
    final_count,final_tags=score(final_g,rows)
    direct_change=Counter({tag:final_count[tag]-old_count[tag]
                           for tag in R3_CERTIFIED_FLOORS})
    direct_weighted=sum(direct_change[tag]*R3_CERTIFIED_FLOORS[tag]
                        for tag in R3_CERTIFIED_FLOORS)
    # Original Q outside *all* altered line IDs cannot change membership
    # or historical GF5 tag under one unchanged physical point map f.
    for ids,lines,kind in rows:
        if not lines&actual_changed_lines:
            if old_tags.get(ids)!=final_tags.get(ids):
                raise AssertionError("seven-GF5 tag changed outside true original source-line cut")

    sparse_signed=Counter()
    sparse_weight=0
    step_change=[]
    working=list(g)
    for u,v in swap_list:
        before=tuple(working)
        working[u],working[v]=working[v],working[u]
        after=tuple(working)
        nearby=tuple(row for row in rows if row[1]&{u,v})
        c_before,_=score(before,nearby)
        c_after,_=score(after,nearby)
        delta={tag:c_after[tag]-c_before[tag]
               for tag in R3_CERTIFIED_FLOORS}
        for tag,n in delta.items():
            sparse_signed[tag]+=n
        q=sum(delta[tag]*R3_CERTIFIED_FLOORS[tag] for tag in delta)
        sparse_weight+=q
        step_change.append({
            "two_TRUE_original_line_factor_IDs":(u,v),
            "true_original_left_2regular_sixsets_touched":len(nearby),
            "signed_seven_delta_total":sum(delta.values()),
            "signed_selected_GF5_floor_numerator_delta":q,
            "per_seven_class_signed_delta":delta,
        })
    if tuple(working)!=final_g or any(sparse_signed[tag]!=direct_change[tag]
                                      for tag in R3_CERTIFIED_FLOORS):
        raise AssertionError("exact ORIGINAL per-swap sparse telescoping != full direct census")
    if sparse_weight!=direct_weighted:
        raise AssertionError("selected historical GF5 floor numerator mischarged")
    independent_before=seven_census(model,independent_checks=False)
    modified=dict(model,right_labels=final_g)
    independent_after=seven_census(modified,independent_checks=False)
    if (independent_before["S_seven"]!=sum(old_count.values())
        or independent_after["S_seven"]!=sum(final_count.values())
        or independent_before["GF5_seven_lower_numerator"]!=
        sum(old_count[k]*R3_CERTIFIED_FLOORS[k] for k in old_count)
        or independent_after["GF5_seven_lower_numerator"]!=
        sum(final_count[k]*R3_CERTIFIED_FLOORS[k] for k in final_count)):
        raise AssertionError("original all-seven complete census disagrees with independent scorer")
    gained=sum(ids not in old_tags for ids in final_tags)
    lost=sum(ids not in final_tags for ids in old_tags)
    switched=sum(ids in final_tags and old_tags[ids]!=final_tags[ids]
                 for ids in old_tags)
    if gained-lost!=sum(direct_change.values()):
        raise AssertionError("original seven-family gain/loss count mismatch")
    if abs(sum(direct_change.values()))>len(boundary):
        raise AssertionError("direct change bigger than original line cut")
    if abs(direct_weighted)>bound[
       "weighted_51palette_GF5_necessary_floor_numerator_change_abs_bound"]:
        raise AssertionError("original weighted change outside physical bound")
    return {
        "scheme":scheme,
        "s":2,
        "total_original_six_ID_left_2regular_candidates":len(rows),
        "number_of_distinct_actual_source_line_labels_ever_swapped":len(actual_changed_lines),
        "five_swap_global_original_line_steps":len(swap_list),
        "actual_source_line_cut_candidate_Q":len(boundary),
        "original_seven_S_before":sum(old_count.values()),
        "repaired_seven_S_after":sum(final_count.values()),
        "original_seven_S_signed_change":sum(direct_change.values()),
        "original_7class_before":dict(old_count),
        "repaired_7class_after":dict(final_count),
        "per_seven_class_signed_change":dict(direct_change),
        "original_selected_GF5_floor_numerator_signed_change":direct_weighted,
        "accepted_original_six_ID_Q_gained":gained,
        "accepted_original_six_ID_Q_lost":lost,
        "accepted_original_six_ID_Q_switched_seven_tag":switched,
        "each_swap_true_original_source_line_sparse_details":step_change,
        "independent_complete_original_census_compared":True,
        "original_adversarial_g_D6_may_be_zero":True,
        "repaired_Q_true_original_D6_verified":True,
        "this_bound_PROVES_root_A_B_C":False,
    }


if __name__=="__main__":
    import json
    print(json.dumps({"exact_physical_patterns":rooted_k6_2regular_multigraph_oracle(),
                      "all_h": [all_h_seven_original_line_fiber_bound(1<<h)
                                for h in range(1,16)]},
                     sort_keys=True,default=str))
    for scheme in ("S68","S72","lex","reverse"):
        x=genuine_original_W32_five_swap_seven_boundary(scheme)
        print("ORIGINAL_FIVE_SWAP_SEVEN_BOUNDARY",
              json.dumps(x,sort_keys=True,default=str))
