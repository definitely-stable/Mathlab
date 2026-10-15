"""HYP-105 / issue #230 / D6-AA4-Y5
Universal EXACT original repeated-B source root-pair forest matching identity
for historical B-left/A-right and A-left/B-right cells.

For a realized physical B pattern with original doubled source p and
fixed TWO DISTINCT actual original flags (p,l1),(p,l2), four other
point source factors q1..q4, the number of ACTUAL original six-flag Q
with six DISTINCT opposite LINE source factors is the exact injection
permanent of N(qi)\\{l1,l2}. A source GQ has pairwise source-neighbor
intersection <=1 and no other qi on both distinct lines through p.
An explicit integer partition-lattice Möbius formula, an ALL-h lower
and upper for every realized original B physical pattern follow.

CRUCIAL: this is an exact SOURCE-FOREST B/A or A/B POTENTIAL and not
the accepted historical GF5 B/A count until the OPPOSITE side also
has a physically 2-regular A projection under ONE GLOBAL opposite map.
Finite true W(3,2) tests retain and report that missing physical gate.
No all-h universal S>=c*s^6 root result is claimed.
"""
from collections import Counter
from itertools import combinations, product
from math import comb, factorial
import argparse
import json

from hyp105_issue230_d6aa4y3_original_source_star_capacity import original_parameters


def _partitions(items):
    """Each set partition of at most four ACTUAL source positions once."""
    items=tuple(items)
    if not items:
        yield ()
        return
    first=items[0]
    for tail in _partitions(items[1:]):
        yield ((first,),)+tail
        for j in range(len(tail)):
            new=list(tail)
            new[j]=(first,)+new[j]
            yield tuple(new)


def original_four_source_injective_matching(neighbors):
    """Exact number of injective assignments of 4 distinct opposite
    source IDs to 4 given different original point/line factors.

    Rook/partition-lattice Möbius identity:
    sum_pi (-1)^(4-|pi|) prod_(block in pi)(|block|-1)!
                         * |intersect_(i in block) N_i|.
    Valid for any actual original incidence graph and any finite sets.
    """
    if len(neighbors)!=4:
        raise ValueError("four ORIGINAL singly used physical C4 source factors needed")
    items=tuple(frozenset(v) for v in neighbors)
    result=0
    for pi in _partitions(range(4)):
        term=1
        for block in pi:
            intersection=set(items[block[0]])
            for idx in block[1:]:
                intersection.intersection_update(items[idx])
            term*=(-1)**(len(block)-1)*factorial(len(block)-1)*len(intersection)
        result+=term
    if not 0<=result<=__import__("math").prod(len(z) for z in items):
        raise AssertionError("exact ORIGINAL source permanent outside admissible range")
    return result


def original_BA_root_pair_universal_bounds(s):
    s,d,V,a,K=original_parameters(s)
    physical_c4=3*comb(a-2,4)
    raw=physical_c4*d**4
    greedy=1
    for j in range(4):
        greedy*=max(0,d-1-j)
    bonferroni=max(0,(d-1)**4-6*d*d)
    floor=max(greedy,bonferroni)
    return {
        "s":s,"d":d,"V":V,"a":a,"K":K,
        "fixed_original_B_root_two_distinct_flags":True,
        "physical_Ka_C4_candidates_per_prescribed_root_edge":physical_c4,
        "max_true_original_B_A_source_forest_six_Q_per_root_flag_pair":
            raw,
        "per_REALIZED_root_C4_pattern_distinct_opposite_A_source_lower":floor,
        "per_REALIZED_root_C4_pattern_distinct_opposite_A_source_upper":d**4,
        "Greedy_distinct_original_opposite_source_lower":greedy,
        "GQ_no_4cycle_pair_collision_Bonferroni_lower":bonferroni,
        "positive_per_REALIZED_B_C4_for_s_ge_4":s>=4 and floor>0,
        "all_h_exact_source_BA_A_B_forest_permanent_PROVED":True,
        "historical_GF5_opposite_physical_A_also_needed":True,
        "root_all_h_seven_S_omega_s6_PROVED":False,
    }


def _canonical_edge(a,b):
    return (a,b) if a<b else (b,a)


def _physical_root_C4_source_patterns(labels,root):
    """INDEPENDENT of AA4-Q's physical C4 iterator. Each fixed B root
    physical edge has exactly three possible physical C4 complements
    in full physical K6, even though the source labels are ONE global
    bijection rather than independently redrawn per original Q.
    """
    physical=tuple(labels)
    inverse={tuple(e):i for i,e in enumerate(physical)}
    if len(inverse)!=15:
        raise ValueError("full original physical K6 source injection only")
    marked=physical[root]
    other=tuple(x for x in range(6) if x not in marked)
    if len(other)!=4:
        raise ValueError("physical root edge must have two different vertices")
    xs=other
    omitted=(((xs[0],xs[1]),(xs[2],xs[3])),
             ((xs[0],xs[2]),(xs[1],xs[3])),
             ((xs[0],xs[3]),(xs[1],xs[2])))
    patterns=[]
    all_edges={_canonical_edge(a,b) for a,b in combinations(xs,2)}
    for two_disjoint_edges in omitted:
        excluded={_canonical_edge(a,b) for a,b in two_disjoint_edges}
        phys=tuple(sorted(all_edges-excluded))
        if len(phys)!=4 or any(e not in inverse for e in phys):
            raise AssertionError("genuine W32 complete source physical B C4 missing")
        sources=tuple(inverse[e] for e in phys)
        if root in sources or len(set(sources))!=4:
            raise AssertionError("genuine original B pattern repeats non-root factor")
        patterns.append(sources)
    if len(set(patterns))!=3:
        raise AssertionError("three distinct physical C4 source patterns expected")
    return patterns


def _brute_four_choices(sets):
    """Independent literal ORIGINAL opposite incidence 4-rook oracle.
    W32 only (d=3), not used for the all-h symbolic formula."""
    return sum(len(set(choice))==4 for choice in product(*sets))


def _source_cell_bucket(Q,inc,side):
    mult=Counter(inc[j][side] for j in Q)
    if sorted(mult.values())!=[1,1,1,1,2]:
        raise AssertionError("only genuine physical B half source shape")
    root=next(q for q,m in mult.items() if m==2)
    pinned=tuple(sorted(j for j in Q if inc[j][side]==root))
    return root,pinned


def genuine_W32_rooted_BA_forest(scheme):
    """For true ORIGINAL W32 independently validate EVERY 45 root-flag
    pair cohort on BOTH point and line physical B halves against
    (a) exact GQ rook-polynomial formula, (b) independent literal
    10,935 original six-Q B half enumeration, and (c) the physical
    A projection of the opposite complete globally injected map.
    """
    from hyp105_issue230_projection import fixture
    from hyp105_issue230_d6aa4q_two_sided_seven_join import (
        strict_true_W32_model,exact_ONE_side_original_projection_index,
        exact_two_sided_original_seven_join)
    model=fixture(1,scheme)
    inc,left,right=strict_true_W32_model(model)
    actual_source_edges=(left,right)
    all_index=[exact_ONE_side_original_projection_index(model,side)[
        "candidate_sixset_map"] for side in (0,1)]
    history=exact_two_sided_original_seven_join(model,independent_history=True)
    results={}
    for side in (0,1):
        labels=actual_source_edges[side]
        index=all_index[side]
        other_index=all_index[1-side]
        bysource=[[] for _ in range(15)]
        neighbors=[set() for _ in range(15)]
        for j,e in enumerate(inc):
            bysource[e[side]].append(j)
            neighbors[e[side]].add(e[1-side])
        if any(len(a)!=3 for a in bysource):
            raise AssertionError("genuine original W32 B root must have 3 distinct flags")
        groups={}
        for root in range(15):
            for pinned in combinations(bysource[root],2):
                excluded={inc[j][1-side] for j in pinned}
                if len(excluded)!=2:
                    raise AssertionError("two original B root flags must have DISTINCT opposite source endpoints")
                predicted=0
                bypattern=[]
                for sources in _physical_root_C4_source_patterns(labels,root):
                    allowed=tuple(neighbors[q]-excluded for q in sources)
                    if any(len(v)<2 for v in allowed):
                        raise AssertionError("source GQ 4-cycle forbids other point on both pinned lines")
                    for q,r in combinations(sources,2):
                        if len(neighbors[q]&neighbors[r])>1:
                            raise AssertionError("genuine original GQ point/line source girth four")
                    exact=original_four_source_injective_matching(allowed)
                    brute=_brute_four_choices(allowed)
                    if exact!=brute:
                        raise AssertionError("independent actual original source rook/matching direct-oracle disagreement")
                    predicted+=exact
                    bypattern.append(exact)
                groups[root,tuple(pinned)]={
                    "root":root,"actual_root_incidence_IDs":tuple(pinned),
                    "realized_source_B_C4_patterns":3,
                    "source_forests_predicted_by_exact_partition_permanent":predicted,
                    "per_C4_actual_source_forest_counts":bypattern,
                    "physical_B_raw_actual_original_six_Q":3*3**4,
                    "source_A_shape_rejected_due_opposite_endpoint_collision":3*3**4-predicted,
                    "source_forests_seen_by_independent_actual_Q":0,
                    "fully_accepted_GF5_with_opposite_physical_A":0,
                }
        if len(groups)!=45:
            raise AssertionError("exact 15 x C(3,2) rooted source flag cohorts absent")
        b_seen=0
        for Q,kind in index.items():
            if kind!="B":continue
            b_seen+=1
            key=_source_cell_bucket(Q,inc,side)
            found=groups[key]
            if len({inc[j][1-side] for j in Q})==6:
                found["source_forests_seen_by_independent_actual_Q"]+=1
                if other_index.get(Q)=="A":
                    found["fully_accepted_GF5_with_opposite_physical_A"]+=1
        if b_seen!=10935:
            raise AssertionError("genuine W32 original B half count !=10935")
        for record in groups.values():
            if record["source_forests_predicted_by_exact_partition_permanent"]!=(
                    record["source_forests_seen_by_independent_actual_Q"]):
                raise AssertionError(
                    "true original B/A forest exact rook count disagrees with distinct ORIGINAL six-ID half census")
            if not 0<=record["fully_accepted_GF5_with_opposite_physical_A"]<=(
                    record["source_forests_seen_by_independent_actual_Q"])<=243:
                raise AssertionError("original true six-ID physical GF5 BA filter hierarchy false")
        tag="B-left/A-right" if side==0 else "A-left/B-right"
        accepted=sum(z["fully_accepted_GF5_with_opposite_physical_A"]
                     for z in groups.values())
        if accepted!=history["accepted_seven_GF5_original_Q_by_tag"][tag]:
            raise AssertionError("independent ORIGINAL full historical 51palette B/A GF5 count disagrees")
        forests=sum(z["source_forests_seen_by_independent_actual_Q"] for z in groups.values())
        raw=10935
        lost_source=raw-forests
        lost_physical=forests-accepted
        if raw!=lost_source+lost_physical+accepted:
            raise AssertionError("genuine original B/A double-source/physical rejection budget incorrect")
        sorted_by_accepted=sorted(groups.values(),
            key=lambda z:(-z["fully_accepted_GF5_with_opposite_physical_A"],
                          z["root"],z["actual_root_incidence_IDs"]))
        sorted_by_forests=sorted(groups.values(),
            key=lambda z:(-z["source_forests_seen_by_independent_actual_Q"],
                          z["root"],z["actual_root_incidence_IDs"]))
        results[tag]={
            "typed_original_B_side":"point" if side==0 else "line",
            "real_original_root_factors":15,
            "root_fixed_two_distinct_flag_pairs":45,
            "physical_B_C4_patterns_per_root_pair":3,
            "physical_B_candidate_original_six_IDs":raw,
            "true_source_BA_forest_potential_six_IDs":forests,
            "true_source_opposite_A_failures":lost_source,
            "true_source_BA_forest_opposite_physical_A_failures":lost_physical,
            "historical_positive_GF5_accepted_BA_six_IDs":accepted,
            "cohorts_with_positive_source_BA_forests":
                sum(z["source_forests_seen_by_independent_actual_Q"]>0
                    for z in groups.values()),
            "cohorts_with_positive_historical_GF5":
                sum(z["fully_accepted_GF5_with_opposite_physical_A"]>0
                    for z in groups.values()),
            "source_forest_maximum_per_root_two_actual_flags":
                max(z["source_forests_seen_by_independent_actual_Q"] for z in groups.values()),
            "source_forest_minimum_per_root_two_actual_flags":
                min(z["source_forests_seen_by_independent_actual_Q"] for z in groups.values()),
            "top_source_forest_cohorts":sorted_by_forests[:5],
            "top_actual_positive_GF5_cohorts":sorted_by_accepted[:5],
            "all_45_true_original_root_flag_pairs_independently_brute_checked":True,
            "all_10935_original_B_half_Q_checked":True,
            "original_BA_rooted_51palette_historical_GF5_crosscheck":"PASS",
        }
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-Y5-TRUE-ORIGINAL-BA-ROOT-PAIR-FOREST",
        "scheme":scheme,
        "true_original_GQ_W32_incidence_flags":45,
        "all_h_mathematical_exact_partition_permanent_for_realized_B_patterns":True,
        "genuine_complete_GLOBAL_point_line_maps_not_independent_per_Q":True,
        "six_original_incidence_IDs_not_physical_pseudo_forests":True,
        "per_historical_GF5_BA_tag":results,
        "root_A":"OPEN","root_B":"OPEN","root_C":"OPEN",
    }


def report():
    rows=[original_BA_root_pair_universal_bounds(1<<h) for h in range(1,15)]
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-Y5-ALL-H-ROOT-PAIR-FOREST-MATCHING",
        "all_h_exact_BA_source_forest_injective_4_neighbor_matching_PROVED":True,
        "all_h_GQ_pencil_no_4cycle_root_two_flag_lower_PROVED":True,
        "all_h_opposite_physical_A_acceptance_NOT_GUARANTEED":True,
        "per_order":rows,"root_A":"OPEN","root_B":"OPEN","root_C":"OPEN",
    }


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--scheme",choices=("S68","S72","lex","reverse"))
    a=p.parse_args()
    obj=genuine_W32_rooted_BA_forest(a.scheme) if a.scheme else report()
    print(json.dumps(obj,indent=2,sort_keys=True))
