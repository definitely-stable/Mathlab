"""HYP-105 #230 / AA4-AI: sharp *original pencil* root-pair badness.

New ALL-f ALL-g pre-Hall occupied two-triangle physical mass lower
P_triangle >= s^14/256 for ALL powers of two s >= 16 (not AG's
previous s>=2**19). SAME original W(3,s) complete global typed maps,
same INDEXED rooted physical first-C4 and occupied other-side
two-triangle completions, no original four-rook Hall positivity claimed.

Key original GQ line incidence improvement:
Every real original line intersects exactly d(d-1) other lines,
not V-1. At most (a-1) globally injected original line factors
can have a physical pair incident with a prescribed hot coordinate.
Thus original root/pair count touching hot physical coordinates is
<= H*(a-1)*d*(d-1), H<=floor(32m/a)<=32, instead of the AG bound
H*(a-1)*(V-1). The remaining original root/pairs have disjoint
globally physical pairs whose 4 endpoints all have hole-degree<a/16.

Proof for s>=128: a<=1.5 s**1.5; bad/N <=27/(8sqrt(s))
+96/s**1.5 <1/2. The small powers 16,32,64 are independently
integer-certified; 16,32 still have good fraction>1/4 and their
actual slack exceeds final s14/256. For s>=128, C4>=a4/128
and occupied two-triangle completions >=a2/4 per good rootpair
imply (N/2)*(a4/128)*(a2/4)>=s14/256 because
N>=s5/2 and a2>=2s3.

CRITICAL: P_triangle counts PRE-HALL PHYSICAL CANDIDATES. For genuine
original Hall-positive accepted original six-Q T_triangle,
T_triangle <= P_triangle, and T_triangle may vanish at an individual
original rootpair. No all-map positive true-GF5 S theorem.
"""
from collections import Counter
from itertools import combinations
from math import comb
from hyp105_issue230_d6aa4ag_deterministic_triangle_hall import (
    minimal_alphabet, independent_common_neighbors, occupied_two_triangles,
)
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import _valid_original_model
from hyp105_issue230_d6aa4af_rootpair_robust_quench import (
    occupied_root_C4_source_factors,
)


def improved_all_h_original_line_pencil_preHall(s):
    """Pure integer original-GQ all-h theorem, no simulated f,g."""
    V,a,m=minimal_alphabet(s)
    d=s+1
    N=V*comb(d,2)
    hot_upper=(32*m)//a
    adjacent_upper=a*comb(a-1,2)
    # ORIGINAL GQ: each original line touches d actual original points
    # and d-1 other original lines through each -> exactly d(d-1).
    hot_touch_upper=hot_upper*(a-1)*d*(d-1)
    bad_upper=adjacent_upper+hot_touch_upper
    good_floor=max(0,N-bad_upper)
    C4_floor=max(0,3*comb(a-2,4)-m*(a-4)*(a-5))
    triangle_floor=(a*a+3)//4  # integer ceil(a^2/4)
    prehall_lower=good_floor*C4_floor*triangle_floor
    exact_exception={(16,94,2): (594184,402132,0,192052),
                     (32,261,105): (17859600,8787870,3294720,5777010),
                     (64,731,510): (553914400,194508135,66809600,292596665)}
    if s>=16:
        assert 4*C4_floor>=0
        # For a>=22: n=a-2, m<=n:
        # C4>=n(n-2)(n-3)(n-9)/8>=a**4/128.
        assert 128*C4_floor>=a**4
        assert 2*V<=a*a
        if s>=128:
            assert 4*a*a<=9*s**3
            # Original-line pencil bound, not a codegree relaxation:
            assert 2*bad_upper<=N
            assert 4*triangle_floor>=a*a
        else:
            key=(s,a,m)
            if key not in exact_exception:
                raise AssertionError("all small true GQ orders 16/32/64 explicitly frozen")
            n_exact,adj_exact,hot_exact,good_exact=exact_exception[key]
            assert (N,adjacent_upper,hot_touch_upper,good_floor)==(
                n_exact,adj_exact,hot_exact,good_exact)
            assert good_floor>0
        assert 256*prehall_lower>=s**14
    return {
        "s":s,"V":V,"d":d,"a":a,"K":comb(a,2),
        "missing_physical_pair_images":m,
        "actual_original_root_two_lines_indexed_N":N,
        "hot_physical_coordinate_upper":hot_upper,
        "adjacent_pinned_physical_pairs_upper":adjacent_upper,
        "NEW_genuine_GQ_line_pencil_hot_touch_upper":hot_touch_upper,
        "total_original_bad_rootpairs_upper":bad_upper,
        "safe_original_rootpairs_lower":good_floor,
        "universal_occupied_point_C4_per_root_lower":C4_floor,
        "occupied_opposite_two_triangles_per_safe_pair_lower":triangle_floor,
        "indexed_original_global_preHall_physical_mass_lower":prehall_lower,
        "exact_s14_over_256_PROVED_for_all_h_ge4":s>=16,
        "first_valid_order_with_constant_1_over_256":16,
        "AG_previous_first_valid_order":2**19,
        "improved_bad_original_pair_dependency":
            "at most (a-1)*d*(d-1) rooted line pairs per hot physical vertex",
        "single_same_global_f_g_and_true_source_GQ_required":True,
        "original_four_rook_Hall_positive_lower_PROVED":False,
        "issue230_universal_seven_GF5_lower_PROVED":False,
    }


def original_true_rootpair_physical_safety_census(
    model, *, side=0, probe_good_pairs=6, probe_C4_root=True,
    independent_physical_triangle_check=True,
):
    """Literal finite genuine W32/W34/W38 check on ONE COMPLETE global f/g.

    No fake independent per-original-Q edge labels. Enumerates the
    real source GQ root+two-original-flags index, not all K_a edge
    pairs, and classifies actual pinned opposite physical adjacency,
    missing-physical-coordinate hot status, and safe completions.
    The analytic all-h certificate is NOT proved by these finite runs.
    """
    V,a,_=_valid_original_model(model)
    if type(side) is not int or side not in (0,1):
        raise ValueError("point B side=0 or line B side=1")
    if type(probe_good_pairs) is not int or probe_good_pairs<0 or probe_good_pairs>40:
        raise ValueError("bounded positive/zero finite safe pair probes 0..40")
    s=model["s"];d=s+1
    inc=tuple(tuple(e) for e in model["incidences"])
    B=tuple(tuple(e) for e in model["left_labels" if side==0 else "right_labels"])
    A=tuple(tuple(e) for e in model["right_labels" if side==0 else "left_labels"])
    E=frozenset(A)
    missing=frozenset(combinations(range(a),2))-E
    miss_degree=Counter(x for e in missing for x in e)
    hot=frozenset(x for x in range(a) if 16*miss_degree[x]>=a)
    byroot=[[] for _ in range(V)]
    for i,e in enumerate(inc):bysource=e[side];byroot[bysource].append(i)
    if any(len(x)!=d for x in byroot):
        raise AssertionError("not a regular TRUE ORIGINAL source GQ incidence graph")
    actual=Counter()
    probes=[]
    first_safe_root=None
    for root,flag_ids in enumerate(byroot):
        for two_flags in combinations(flag_ids,2):
            opposite=tuple(inc[i][1-side] for i in two_flags)
            e0,e1=A[opposite[0]],A[opposite[1]]
            actual["all_true_original_root_line_pairs"]+=1
            adjacent=bool(set(e0)&set(e1))
            touching_hot=bool(set(e0+e1)&hot)
            if adjacent:actual["physically_adjacent"]+=1
            if touching_hot:actual["touching_hot"]+=1
            if adjacent or touching_hot:
                actual["actual_bad_union"]+=1
                continue
            actual["genuinely_good_safe_original_rootpairs"]+=1
            if first_safe_root is None:first_safe_root=root
            if len(probes)<probe_good_pairs:
                n=independent_common_neighbors(E,e0,e1,a)
                if independent_physical_triangle_check:
                    literal=occupied_two_triangles(E,e0,e1,a)
                    if n!=len(literal):
                        raise AssertionError("physical actual 2-triangles disagree with unrelated direct enumeration")
                if a>=32 and n<((a*a+3)//4):
                    raise AssertionError("true original safe pair physical occupancy bound failed")
                probes.append({
                    "true_original_B_root":root,
                    "two_actual_original_incidence_ids":two_flags,
                    "two_global_opposite_physical_edges":(e0,e1),
                    "occupied_two_triangles_literal":n,
                    "universal_safe_two_triangle_floor":
                        (a*a+3)//4 if a>=32 else None,
                })
    analytic=improved_all_h_original_line_pencil_preHall(s)
    if actual["all_true_original_root_line_pairs"]!=analytic[
            "actual_original_root_two_lines_indexed_N"]:
        raise AssertionError("true original root two original flags count mismatch")
    if (actual["physically_adjacent"]>
            analytic["adjacent_pinned_physical_pairs_upper"] or
            actual["touching_hot"]>
            analytic["NEW_genuine_GQ_line_pencil_hot_touch_upper"] or
            len(hot)>analytic["hot_physical_coordinate_upper"]):
        raise AssertionError("new true-GQ source-line-pencil global incidence upper falsified")
    if actual["genuinely_good_safe_original_rootpairs"]<analytic[
            "safe_original_rootpairs_lower"]:
        raise AssertionError("true original safe rootpairs below global pencil lower")
    occupied_C4=None
    if probe_C4_root:
        root=first_safe_root if first_safe_root is not None else 0
        occupied_C4=len(occupied_root_C4_source_factors(model,side=side,root=root))
        if occupied_C4<analytic["universal_occupied_point_C4_per_root_lower"]:
            raise AssertionError("source physical global B-C4 complement occupancy violated")
    return {
        "s":s,"scheme_side":side,"V":V,"a":a,
        "missing_global_physical_edges":len(missing),
        "actual_high_missing_degree_physical_coordinates":tuple(sorted(hot)),
        "actual_true_original_rootpairs":dict(actual),
        "old_all_pairs_global_analytic_bad_bound":(
            analytic["adjacent_pinned_physical_pairs_upper"]+
            analytic["hot_physical_coordinate_upper"]*(a-1)*(V-1)),
        "NEW_all_pairs_true_line_pencil_bad_bound":
            analytic["total_original_bad_rootpairs_upper"],
        "independently_enumerated_safe_rootpair_triangle_probes":probes,
        "one_complete_B_global_image_C4_count":occupied_C4,
        "uniform_all_map_s14_over_256_PROVED_by_analytic_not_finite":
            analytic["exact_s14_over_256_PROVED_for_all_h_ge4"],
        "actual_source_GQ_incidences_and_single_global_typed_maps_used":True,
        "all_map_source_Hall_positive_lower_NOT_PROVED":True,
    }


if __name__=="__main__":
    import argparse,json
    from hyp105_issue230_projection import fixture
    p=argparse.ArgumentParser()
    p.add_argument("--scheme",choices=("lex","random"),default="lex")
    p.add_argument("--power",type=int,choices=(2,3),default=2)
    q=p.parse_args()
    print(json.dumps({
        "all_h":[improved_all_h_original_line_pencil_preHall(1<<h)
                 for h in range(1,19)],
        "finite":[original_true_rootpair_physical_safety_census(
                  fixture(q.power,q.scheme),side=j)
                  for j in (0,1)],
    },indent=2,sort_keys=True))
