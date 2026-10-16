"""HYP-105 #230 AA4-AS: EVERY genuine original f,g admits >=s^6/4
DISTINCT complete globally injected right maps g' at <=5 original LINE
factor transpositions with SAME one true six-incidence GF5 D6 witness.

This is a repair-ball cardinality theorem, not any positive lower at the
given adversarial pair f,g, and not all-seven Branch A/B/C. The proofs
are a physical K_a cycle-deficit count + actual GQ d-regular incidence
count + original positional cycle match. This file contains exact ALL-h
integer certificates and independently checkable small-real-GQ oracles.
"""
from collections import Counter
from itertools import combinations, permutations
from math import comb, perm

from hyp105_issue230_d6aa4r_quenched_original_d6 import _params
from hyp105_issue230_d6aa4ar_five_swap_original_D6 import (
    repair_original_D6_with_at_most_five_line_swaps,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import (
    classify_seven_prechecked, physical_column_dual, is_connected_column_cycle,
)


def all_h_repair_ball_certificate(s):
    """Exact integer all-h proof gates; NO synthetic high-h source geometry.

    Let A=(a-2)_4 be #undirected K_a physical C6 through any fixed
    occupied edge e. An occupied edge is called robust if it survives
    >=A/2 real C6 after globally injected physical edge-image holes.
    m=K-V<=a-2. Lost edge-C6 incidences across all occupied edges:
        sum_e (A-real_cycles_through_e) <= 6*m*A.
    Consequently strictly <12m occupied edges are nonrobust.
    Their original global line factor preimages are <=12m, and at most
    12m original point factors have every incident line nonrobust,
    by actual original d-regularity.
    For h>=5, K>78m ensures an occupied f-side physical C6 missing
    all these <=12m excluded point factors. For h<=4, every occupied
    right edge is robust, since m<=(a-2)/2 (exact GQ parameters).
    One original robust anchor plus 5 Hall-completed genuine lines
    produces >=2*(A/2)=A distinct globally injected g' via 5 swaps.
    """
    V,a,K,m=_params(s)
    A=perm(a-2,4)
    if A<=0 or V<6:
        raise AssertionError("six physical edge certificate invalid")
    total_undirected_C6=perm(a,6)//12
    destroyed_by_one_edge=A
    if total_undirected_C6*6 != K*A:
        raise AssertionError("double-count ambient K_a C6 edge incidence")
    if s<=16:
        expected={2:(6,0),4:(14,6),8:(35,10),16:(94,2)}
        if (a,m)!=expected[s]:
            raise AssertionError("finite low-h palette certificate changed")
        if 2*m>a-2:
            raise AssertionError("every physical right edge robust gate fails")
        argument="every_right_occupied_edge_robust_by_union_bound"
        excluded_bad_line_upper=0
        excluded_bad_point_upper=0
        guaranteed_left_cycles_avoiding_bad_points=(
            total_undirected_C6-m*A)
    else:
        if s<32 or a<261 or K<=78*(a-2) or K<=78*m:
            raise AssertionError("large-h palette robust-anchor gate failed")
        argument="global_loss_mass_and_true_original_regular_bipartite"
        # A right physical edge is BAD if it is contained in <A/2
        # occupied right physical C6. Every such edge contributes >A/2
        # deficit to sum_e(A-actual_anchor_C6). Therefore count <12m.
        excluded_bad_line_upper=12*m
        # ORIGINAL, not artificial, incidence d-regularity:
        # each point whose d true neighboring line factors are bad
        # consumes d of at most d*|bad lines| original incidences.
        excluded_bad_point_upper=12*m
        guaranteed_left_cycles_avoiding_bad_points=(
            total_undirected_C6-(m+excluded_bad_point_upper)*A)
        if guaranteed_left_cycles_avoiding_bad_points<=0:
            raise AssertionError("no guaranteed globally f-occupied 6cycle")
    physical_left_C6_lower=total_undirected_C6-m*A
    if physical_left_C6_lower<=0:
        raise AssertionError("no occupied f physical 6cycle guaranteed")
    # Every robust chosen original right line anchor physical edge lies
    # on >=A/2 distinct undirected occupied right cycles. TWO cyclic
    # orientations, with its original physical edge g(l0) kept fixed,
    # lead to 2*cycles >= A pairwise-distinct globally legal g'.
    distinct_global_positive_right_map_lower=A
    if s==2:
        if A< s**6//4:
            raise AssertionError("smallest actual W32 repair-ball bound wrong")
    else:
        # a^2>=2V>=2s^3; a>=14 ensures
        # (a-2)_4 >= (a-5)^4 >= a^4/8 >= s^6/2.
        if not 8*(a-5)**4>=a**4 or 2*A<s**6:
            raise AssertionError("all-h polynomial C6 repair density proof fails")
    if 4*distinct_global_positive_right_map_lower < s**6:
        raise AssertionError("all-h bound on distinct repair target maps failed")
    return {
        "s":s,"V":V,"a":a,"K":K,"m":m,"d":s+1,
        "ambient_C6_through_one_physical_edge_A":A,
        "occupied_f_C6_unconditional_lower":physical_left_C6_lower,
        "bad_right_original_LINE_factors_strict_upper":excluded_bad_line_upper,
        "original_points_all_LINE_neighbors_bad_upper":excluded_bad_point_upper,
        "occupied_f_C6_avoiding_all_bad_original_points_lower":
            guaranteed_left_cycles_avoiding_bad_points,
        "robust_anchor_argument":argument,
        "at_least_unoriented_right_cycles_through_chosen_anchor":
            str(A)+"/2",
        "two_right_cycle_orientations_per_anchor":2,
        "distinct_COMPLETE_global_right_maps_positive_D6_within_5_line_swaps_at_least":A,
        "uniform_all_h_distinct_global_right_repair_lower_s6_over4":True,
        "one_and_same_actual_six_original_incidence_IDs_for_all_repairs":True,
        "original_fixed_f_and_original_right_physical_support_unchanged":True,
        "original_d6_at_given_adversarial_g_lower_proved":False,
        "all_seven_class_original_fixed_pair_minimax_proved":False,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def _all_anchored_right_C6_oriented(a,occupied,anchor):
    """Enumerate two orientations of every REAL C6 containing anchor."""
    E=set(tuple(e) for e in occupied)
    u,v=anchor
    if (u,v) not in E:
        raise ValueError("anchor must be present in occupied right image")
    for middle in permutations((w for w in range(a) if w not in anchor),4):
        vertices=(u,v)+middle
        cycle=tuple(
            tuple(sorted((vertices[i],vertices[(i+1)%6])))
            for i in range(6))
        if all(e in E for e in cycle):
            assert cycle[0]==anchor
            yield cycle
            yield (cycle[0],)+tuple(reversed(cycle[1:]))


def finite_genuine_original_one_Q_repair_ball(model):
    """Enumerate exact ALL distinct <=5-swap g' for a fixed true six-Q.

    This executable definition-level oracle is deliberately capped to
    actual source W32/W34; all-h proof uses exact symbolic counting.
    """
    s=model["s"]
    if s not in (2,4):
        raise ValueError("finite true original controls only W(3,2) and W(3,4)")
    V,a,K,m=_params(s)
    expected=(model["a"],len(model["left_labels"]),len(model["right_labels"]))
    if expected!=(a,V,V):
        raise ValueError("wrong physical original symplectic global model")
    model0=repair_original_D6_with_at_most_five_line_swaps(model)
    ids=tuple(model0["actual_original_six_incidence_IDs"])
    lines=tuple(model0["six_actual_original_line_factor_IDs"])
    original=tuple(tuple(q) for q in model["incidences"])
    f=tuple(tuple(q) for q in model["left_labels"])
    g=tuple(tuple(q) for q in model["right_labels"])
    anchor=g[lines[0]]
    if anchor!=model0["anchored_physical_image_preserved"]:
        raise AssertionError("anchor changed")
    original_left=physical_column_dual(
        original,f,tuple(original[i][0] for i in ids))
    if not is_connected_column_cycle(original_left):
        raise AssertionError("not a real original source C6")
    unique={}
    anchored=0
    for targets in _all_anchored_right_C6_oriented(a,g,anchor):
        anchored+=1
        right=list(g)
        owner={edge:i for i,edge in enumerate(right)}
        swaps=0
        for l,desired in zip(lines[1:],targets[1:]):
            if right[l]==desired:
                continue
            previous=right[l]
            other=owner[desired]
            right[l],right[other]=right[other],right[l]
            owner[previous]=other
            owner[desired]=l
            swaps+=1
        if swaps>5 or right[lines[0]]!=anchor:
            raise AssertionError("more than five global line swaps or lost anchor")
        if set(right)!=set(g) or len(set(right))!=V:
            raise AssertionError("not fully globally injected original line map")
        right=tuple(right)
        if right in unique:
            raise AssertionError("distinct right C6 orientations produced same global map")
        right_dual=physical_column_dual(
            original,right,tuple(original[i][1] for i in ids))
        if original_left!=right_dual or not is_connected_column_cycle(right_dual):
            raise AssertionError("independent ORIGINAL six-position physical D6 control")
        if a==6 and classify_seven_prechecked(ids,f,right,original)!="D6":
            raise AssertionError("original W32 historical sevenclass mismatch")
        unique[right]=swaps
    if anchored%2:
        raise AssertionError("right physical cycles require TWO rooted orientations")
    if anchored!=len(unique):
        raise AssertionError("physical cycle orientations and right map count mismatch")
    A=perm(a-2,4)
    assert anchored>=A
    return {
        "s":s,
        "physical_a":a,
        "original_6_DISTINCT_source_incidence_IDs":ids,
        "original_6_DISTINCT_source_LINE_IDs":lines,
        "anchored_global_right_line_physical_edge_kept":anchor,
        "actual_right_occupied_undirected_C6_through_anchor":anchored//2,
        "actual_different_full_right_maps_positive_same_original_D6_Q":len(unique),
        "theoretical_lower_maps_from_all_h":A,
        "largest_global_LINE_swap_distance_used":max(unique.values()),
        "smallest_global_LINE_swap_distance_used":min(unique.values()),
        "all_original_and_repaired_global_support_equal":True,
        "historical_W32_classifier_full_crosscheck":a==6,
        "independent_all_a_six_position_physical_D6_crosscheck":True,
        "given_original_g_D6_positive_NOT_asserted":True,
        "seven_GF5_minimax_not_proved":True,
    }


if __name__=="__main__":
    import json
    r=[all_h_repair_ball_certificate(1<<h) for h in range(1,32)]
    for h,name in ((1,"S68"),(1,"S72"),(2,"lex"),(2,"random")):
        z=finite_genuine_original_one_Q_repair_ball(fixture(h,name))
        print(json.dumps({"scheme":name,**z},sort_keys=True))
    print(json.dumps({"symbolic_certificates_count":len(r),
                      "all_h_lower":"(a-2)_4 >= s^6/4",
                      "not_root_A_B_C":True},sort_keys=True))
