"""AA4-BN genuine original three-swap refutation controls and exact all-h proof."""
import unittest
from collections import Counter
from itertools import combinations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import zero_split_original_W32
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bn_three_swap_original_cherry import (
    original_BN_all_h_three_swap_certificate,
    original_root_physical_good_C4_index,
    original_fixed_pair_three_swap_cherry_repair,
    missing_endpoint_degrees,
)
from hyp105_issue230_d6aa4bm_four_swap_root_BA_repair import (
    original_fixed_pair_repair_cherry_four_swaps,
)
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6aa4q_two_sided_seven_join import independent_joint_classify


def independent_C4_good_source_points(model,side,root):
    """Source physical C4 by independent 4-vertex/3-unoriented-cycle DFS."""
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    images=(f,g)[side]
    allowed={v for v in range(a) if v not in images[root]}
    edge_owner={edge:i for i,edge in enumerate(images)}
    good=set()
    for verts in combinations(sorted(allowed),4):
        u,v,w,z=verts
        for cycle in (
            ((u,v),(v,w),(w,z),(z,u)),
            ((u,v),(v,z),(z,w),(w,u)),
            ((u,w),(w,v),(v,z),(z,u)),
        ):
            pair=tuple(tuple(sorted(e)) for e in cycle)
            if len(set(pair))==4 and all(e in edge_owner for e in pair):
                good.update(edge_owner[e] for e in pair)
    return good


def independent_bad_opposite_line_count(model,side,root):
    """Literal ORIGINAL GQ factor adjacency, not physical fourflag oracle."""
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    usable=independent_C4_good_source_points(model,side,root)
    other=(byL,byP)[side]
    bad=set()
    for fac,actual_ids in enumerate(other):
        if all(inc[j][side] not in usable for j in actual_ids):
            bad.add(fac)
    return bad


def replay_three_swaps_and_all_real_injections(before,steps,immutable):
    owners=[tuple(before)]
    now=list(before)
    for left,right in steps:
        now[left],now[right]=now[right],now[left]
        assert len(set(now))==len(now)
        for pin in immutable:assert now[pin]==before[pin]
        assert set(now)==set(before)
        owners.append(tuple(now))
    return owners


def independent_three_target_swap_minimum():
    """Abstract target-specific bound, NOT global historical GF5 optimality."""
    init=tuple(range(8))
    desired=(5,6,7)
    # Exactly three target edges start EXTERNAL to source indices 2,3,4;
    # one global transposition can add at most one of those outside
    # target edges to the selected source-factor set.
    frontier={init}
    if any(tuple(q[i] for i in (2,3,4))==desired for q in frontier):
        return 0
    for depth in (1,2):
        nextf=set()
        for q in frontier:
            for i,j in combinations(range(2,8),2):
                z=list(q)
                z[i],z[j]=z[j],z[i]
                nextf.add(tuple(z))
        if any(tuple(q[i] for i in (2,3,4))==desired for q in nextf):
            return depth
        frontier=nextf
    return None


class AA4BNTrueOriginalThreeSwapRoot(unittest.TestCase):
    def test_01_all_h_genuine_original_pair_unique_line_badness_and_positive_cycle(self):
        for h in tuple(range(22,37))+(40,48,64,80):
            z=original_BN_all_h_three_swap_certificate(1<<h)
            self.assertEqual(z["h"],h)
            self.assertLess(4*z["genuine_original_line_factors_all_of_whose_d_points_bad_upper"],
                            z["a"]-4)
            self.assertLessEqual(z["genuine_original_line_factors_all_of_whose_d_points_bad_upper"],
                                 400*z["s"])
            self.assertGreater(z["root_pin_6cycle_with_NO_BAD_line_images_adjacent_twice_lower"],0)
            self.assertGreater(z["root_pin_6cycle_with_NO_BAD_line_images_disjoint_twice_lower"],0)
            self.assertEqual(z["original_source_LINE_image_swap_upper"],3)
            self.assertTrue(z["genuine_original_source_point_PAIR_uniqueness_REQUIRED"])
            self.assertTrue(z["unchanged_fixed_f_g_positive_not_proved"])
            self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")

    def test_02_true_original_W32_five_global_maps_all_cherries_source_comparison(self):
        mods=[("dual_zero",zero_split_original_W32())]+[
            (name,fixture(1,name)) for name in ("lex","reverse","S68","S72")]
        successes=Counter()
        candidates=Counter()
        three_swap_counts=Counter()
        for name,model in mods:
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            for side,by in ((0,byP),(1,byL)):
                for p in range(V):
                    self.assertEqual(
                        set(original_root_physical_good_C4_index(model,side,p)),
                        independent_C4_good_source_points(model,side,p))
                    for root in combinations(by[p],2):
                        candidates[(name,side)]+=1
                        z=original_fixed_pair_three_swap_cherry_repair(
                            model,side,p,root,require_h22_regular=False)
                        if z is None:
                            # Finite s=2 outside h>=22: allowed to fail,
                            # while the true original ≤4-swap parent DOES
                            # provide an independent corrected witness.
                            baseline=original_fixed_pair_repair_cherry_four_swaps(
                                model,side,p,root,require_regular=False)
                            self.assertIsNotNone(baseline)
                            continue
                        successes[(name,side)]+=1
                        if z["number_transpositions"]==3:
                            three_swap_counts[(name,side)]+=1
                        before=z["complete_opposite_original_map_before"]
                        after=z["complete_opposite_original_map_after"]
                        self.assertEqual(set(before),set(after))
                        immutable=set(z["original_source_three_pinned_opposite_factors"])
                        hist=replay_three_swaps_and_all_real_injections(
                            before,z["swaps_of_REAL_original_FACTOR_images"],immutable)
                        self.assertEqual(hist[-1],after)
                        self.assertLessEqual(len(hist)-1,3)
                        self.assertEqual(len(immutable),3)
                        self.assertTrue(set(root)<=set(z["true_original_six_incidence_flag_IDs"]))
                        cls="B-left/A-right" if side==0 else "A-left/B-right"
                        self.assertEqual(z["historical_genuine_GF5_accepted_seven_class"],cls)
                        if p==0 and successes[(name,side)]==1:
                            # Older independent W32 historical census on
                            # FULL completed original f,g, not a fake six-edge
                            # physical support classifier.
                            h7=seven_census(z["repaired_full_original_model"],
                                            independent_checks=False,witness_sets=True)
                            self.assertEqual(h7["sets"][z["true_original_six_incidence_flag_IDs"]],
                                             cls)
            self.assertGreater(sum(v for (label,side),v in successes.items()
                                   if label==name),10)
            print("AA4BN_W32",name,
                  "root_successes",{side:successes[(name,side)] for side in (0,1)},
                  "root_candidates",{side:candidates[(name,side)] for side in (0,1)},
                  "exact_three_swaps",{side:three_swap_counts[(name,side)] for side in (0,1)})

    def test_03_true_original_W34_nonto_K14_both_typed_and_gauge(self):
        total=0
        for name in ("lex","random"):
            model=fixture(2,name)
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            self.assertEqual((s,V,a),(4,85,14))
            for side,by in ((0,byP),(1,byL)):
                for p in (0,7,19,37,84):
                    good=set(original_root_physical_good_C4_index(model,side,p))
                    self.assertEqual(good,independent_C4_good_source_points(model,side,p))
                    actual_bad=independent_bad_opposite_line_count(model,side,p)
                    self.assertLessEqual(len(actual_bad),
                                         (V-len(good))*(V-len(good)-1)//(s*(s+1))
                                         if V-len(good)>=2 else 0)
                    for root in combinations(by[p],2):
                        z=original_fixed_pair_three_swap_cherry_repair(
                            model,side,p,root,require_h22_regular=False)
                        if z is None:continue
                        after=z["repaired_full_original_model"]
                        cls="B-left/A-right" if side==0 else "A-left/B-right"
                        Q=z["true_original_six_incidence_flag_IDs"]
                        independent=independent_joint_classify(
                            Q,"B" if side==0 else "A","A" if side==0 else "B",
                            inc,after["left_labels"],after["right_labels"])
                        self.assertEqual(independent,cls)
                        original=(g,f)[side]
                        fixed=z["original_source_three_pinned_opposite_factors"]
                        hist=replay_three_swaps_and_all_real_injections(
                            original,z["swaps_of_REAL_original_FACTOR_images"],fixed)
                        self.assertEqual(hist[-1],z["complete_opposite_original_map_after"])
                        self.assertLessEqual(len(hist)-1,3)
                        total+=1
        self.assertGreater(total,5)

    def test_04_true_original_GQ_bad_line_pair_packing_W32_and_W34(self):
        for model in (fixture(1,"lex"),fixture(1,"S68"),
                      fixture(2,"lex"),fixture(2,"random")):
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            for side in (0,1):
                for p in (0,V//2,V-1):
                    good=independent_C4_good_source_points(model,side,p)
                    bad_count=V-len(good)
                    nonextendible=independent_bad_opposite_line_count(model,side,p)
                    self.assertLessEqual(
                        len(nonextendible)*s*(s+1),bad_count*(bad_count-1))
                    # Strong primitive needed by the proof: any two
                    # actual original source points share <=1 original
                    # source line (or dual line pair shares <=1 point).
                    opp=(1-side)
                    neighbors=[set() for _ in range(V)]
                    for x,y in inc:
                        vals=(x,y)
                        neighbors[vals[side]].add(vals[opp])
                    for x,y in combinations(range(min(V,40)),2):
                        self.assertLessEqual(len(neighbors[x]&neighbors[y]),1)

    def test_05_three_external_owner_target_specific_lower_not_GF5_optimality(self):
        self.assertIsNone(independent_three_target_swap_minimum())
        # Exact three swaps achieve the prescribed source-three-image
        # destination while pin0,pin1,extra-pin are untouched.
        arr=list(range(8))
        for u,v in ((2,5),(3,6),(4,7)):arr[u],arr[v]=arr[v],arr[u]
        self.assertEqual(tuple(arr[i] for i in (2,3,4)),(5,6,7))
        self.assertEqual(arr[:2],[0,1])

    def test_06_fake_genuine_original_and_invalid_source_id_rejection(self):
        for invalid in (0,2,4,32,2**21,2**22+1,True,-1):
            with self.assertRaises(ValueError):
                original_BN_all_h_three_swap_certificate(invalid)
        model=fixture(1,"lex")
        _,V,a,inc,f,g,byP,byL=_original_source(model)
        for invalid_side in (2,-1,True):
            with self.assertRaises(ValueError):
                original_fixed_pair_three_swap_cherry_repair(
                    model,invalid_side,0,byP[0][:2],require_h22_regular=False)
        for flags in ((byP[0][0],)*2,(-1,byP[0][1]),(True,byP[0][0])):
            with self.assertRaises(ValueError):
                original_fixed_pair_three_swap_cherry_repair(
                    model,0,0,flags,require_h22_regular=False)
        for bad in (dict(model,left_labels=((0,1),)*15),
                    dict(model,right_labels=((0,1),)*15),
                    dict(model,incidences=model["incidences"][:-1])):
            with self.assertRaises(ValueError):
                original_fixed_pair_three_swap_cherry_repair(
                    bad,0,0,byP[0][:2],require_h22_regular=False)

if __name__=="__main__":
    unittest.main()
