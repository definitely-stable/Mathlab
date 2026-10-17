"""AA4-BM actual W32/W34 original source and ≤4 global swap repair falsifiers."""
import unittest
from collections import Counter
from itertools import combinations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import zero_split_original_W32
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bk_each_cherry_BA import genuine_original_root_BA_source_pool
from hyp105_issue230_d6aa4bl_two_pin_conditional_BA import (
    every_fixed_original_g_good_root_pin_majority,
)
from hyp105_issue230_d6aa4bm_four_swap_root_BA_repair import (
    missing_endpoint_degrees,
    find_genuine_source_root_C4_sixflags,
    find_target_C6_with_two_original_pinned_edges,
    original_fixed_pair_repair_cherry_four_swaps,
    original_genuine_root_pin_majority_four_swap_cert,
    four_external_donors_swap_lower_bound,
)
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6aa4q_two_sided_seven_join import independent_joint_classify


def separate_original_flag_physical_degree2(Q,inc,labels,side):
    deg=Counter(u for j in Q for u in labels[inc[j][side]])
    return len(deg)==6 and set(deg.values())=={2}


def independently_replay_global_source_swaps(initial,steps):
    """Independent immutable-permutation trace, not production owner map."""
    img=tuple(initial)
    hist=[img]
    for left,right in steps:
        z=list(img)
        z[left],z[right]=z[right],z[left]
        img=tuple(z)
        hist.append(img)
    return tuple(hist)


def exact_target_specific_bfs_three_swaps_no_match():
    """Independent 10-label permutation BFS with two immutable roots.

    Four specific desired target images are initially on four
    EXTERNAL labels, so count all 2- and 3-step possibilities.
    Not a claimed GF5 global optimal bound.
    """
    init=tuple(range(10))
    visited={init}
    frontier={init}
    def done(x):
        return x[2:6]==(6,7,8,9)
    for depth in range(4):
        if any(done(x) for x in frontier):
            return depth
        if depth==3:break
        nxt=set()
        for x in frontier:
            for i,j in combinations(range(2,10),2):
                y=list(x)
                y[i],y[j]=y[j],y[i]
                z=tuple(y)
                if z not in visited:nxt.add(z)
        visited|=nxt
        frontier=nxt
    return None


class AA4BMOriginalFourSwapRootRepair(unittest.TestCase):
    def test_01_all_h_fully_fixed_f_g_majority_source_cherry_four_swap_math(self):
        for h in tuple(range(5,36))+(40,48,64,80):
            s=1<<h
            z=original_genuine_root_pin_majority_four_swap_cert(s)
            self.assertGreater(z["fraction_true_original_cherries_with_regular_two_pinned_images_lower"],0.75)
            self.assertEqual(z["allowed_source_LINE_image_transpositions_max"],4)
            self.assertTrue(z["six_real_original_source_incidence_IDs_immutable"])
            self.assertTrue(z["unmodified_arbitrary_full_original_f_g_positive_NOT_PROVED"])
            self.assertTrue(z["one_repaired_map_simultaneously_for_all_roots_NOT_PROVED"])
            self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")

    def test_02_five_real_original_W32_complete_full_map_root_repair_and_historic(self):
        mods=[("dual_zero",zero_split_original_W32())]+[
            (n,fixture(1,n)) for n in ("lex","reverse","S68","S72")]
        for name,model in mods:
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            repaired=0
            pos_changed=0
            for side,by in ((0,byP),(1,byL)):
                for p in range(V):
                    for root in combinations(by[p],2):
                        source=find_genuine_source_root_C4_sixflags(model,side,p,root)
                        if source is None:continue
                        z=original_fixed_pair_repair_cherry_four_swaps(
                            model,side,p,root,require_regular=False)
                        self.assertIsNotNone(z)
                        self.assertLessEqual(z["number_global_source_FACTOR_swaps"],4)
                        self.assertEqual(set(z["original_global_opposite_map_before"]),
                                         set(z["original_global_opposite_map_after"]))
                        self.assertEqual(z["same_six_REAL_original_incidence_IDs"],source)
                        pins=tuple(inc[j][1-side] for j in root)
                        for src in pins:
                            self.assertEqual(z["original_global_opposite_map_before"][src],
                                             z["original_global_opposite_map_after"][src])
                        replay=independently_replay_global_source_swaps(
                            z["original_global_opposite_map_before"],
                            z["exact_original_source_line_swap_transpositions"])
                        self.assertEqual(replay[-1],z["original_global_opposite_map_after"])
                        for intermediate in replay:
                            self.assertEqual(len(set(intermediate)),V)
                            self.assertEqual(set(intermediate),set(z["original_global_opposite_map_before"]))
                            for src in pins:
                                self.assertEqual(intermediate[src],
                                                 z["original_global_opposite_map_before"][src])
                        target_model=z["repaired_full_true_original_model"]
                        self.assertEqual(tuple(target_model["left_labels" if side==0 else "right_labels"]),
                                         tuple(model["left_labels" if side==0 else "right_labels"]))
                        q=source
                        self.assertTrue(separate_original_flag_physical_degree2(
                            q,inc,target_model["left_labels"],0))
                        self.assertTrue(separate_original_flag_physical_degree2(
                            q,inc,target_model["right_labels"],1))
                        self.assertEqual(
                            z["accepted_historical_seven_GF5_tag"],
                            "B-left/A-right" if side==0 else "A-left/B-right")
                        if z["number_global_source_FACTOR_swaps"]:
                            pos_changed+=1
                        if repaired<5:
                            # INDEPENDENT original W32 7-class oracle enumerates
                            # all six-source-flag motifs, not just physical 2regularity.
                            historical=seven_census(target_model,independent_checks=False,witness_sets=True)
                            self.assertEqual(
                                historical["sets"][frozenset(q)],
                                z["accepted_historical_seven_GF5_tag"])
                        repaired+=1
            self.assertGreaterEqual(repaired,20)
            self.assertGreater(pos_changed,0)
            print("AA4BM_W32",name,"repaired ACTUAL original source roots",repaired,
                  "positive swap paths",pos_changed)

    def test_03_real_original_W34_nononto_K14_lex_and_random_both_typed(self):
        total=0
        for name in ("lex","random"):
            model=fixture(2,name)
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            self.assertEqual((s,V,a),(4,85,14))
            for side,by in ((0,byP),(1,byL)):
                checked=0
                for p in (0,7,37,84):
                    for root in combinations(by[p],2):
                        z=original_fixed_pair_repair_cherry_four_swaps(
                            model,side,p,root,require_regular=False)
                        if z is None:continue
                        after=z["repaired_full_true_original_model"]
                        q=z["same_six_REAL_original_incidence_IDs"]
                        expected="B-left/A-right" if side==0 else "A-left/B-right"
                        self.assertEqual(
                            independent_joint_classify(
                                q,"B" if side==0 else "A",
                                "A" if side==0 else "B",
                                inc,after["left_labels"],after["right_labels"]),
                            expected)
                        self.assertEqual(tuple(after["left_labels" if side==0 else "right_labels"]),
                                         tuple(model["left_labels" if side==0 else "right_labels"]))
                        self.assertLessEqual(len(z["exact_original_source_line_swap_transpositions"]),4)
                        checked+=1
                self.assertGreater(checked,0)
                total+=checked
        self.assertGreater(total,10)

    def test_04_independent_true_original_W32_gauge_and_two_root_pins(self):
        model=fixture(1,"lex")
        s,V,a,inc,f,g,byP,byL=_original_source(model)
        roots=((0,tuple(byP[0][:2])),(4,tuple(byP[4][:2])))
        for p,flags in roots:
            original=original_fixed_pair_repair_cherry_four_swaps(model,0,p,flags,require_regular=False)
            rotated=dict(model,
                left_labels=tuple(tuple(sorted(((u+2)%6 for u in e))) for e in model["left_labels"]),
                right_labels=tuple(tuple(sorted(((5-u)%6 for u in e))) for e in model["right_labels"]))
            target=original_fixed_pair_repair_cherry_four_swaps(rotated,0,p,flags,require_regular=False)
            self.assertEqual(original["accepted_historical_seven_GF5_tag"],
                             target["accepted_historical_seven_GF5_tag"])
            self.assertEqual(original["same_six_REAL_original_incidence_IDs"],
                             target["same_six_REAL_original_incidence_IDs"])
            self.assertLessEqual(target["number_global_source_FACTOR_swaps"],4)

    def test_05_abstract_target_four_swap_lower_bound_not_GF5_optimality(self):
        z=four_external_donors_swap_lower_bound()
        self.assertEqual(z["source_transposition_lower_for_THIS_SPECIFIC_TARGET"],4)
        self.assertFalse(z["claim_all_GF5_BA_targets_need_four_swaps"])
        self.assertTrue(z["not_a_true_W3_source_fixture"])
        self.assertIsNone(exact_target_specific_bfs_three_swaps_no_match())

    def test_06_invalid_true_root_original_physical_images_and_scope_reject(self):
        model=fixture(1,"lex")
        s,V,a,inc,f,g,byP,byL=_original_source(model)
        for bad in ((byP[0][0],)*2,(99,byP[0][1]),(True,byP[0][1])):
            with self.assertRaises(ValueError):
                original_fixed_pair_repair_cherry_four_swaps(
                    model,0,0,bad,require_regular=False)
        for bad in (2,True,-1):
            with self.assertRaises(ValueError):
                original_fixed_pair_repair_cherry_four_swaps(
                    model,bad,0,byP[0][:2],require_regular=False)
        for invalid in (2,4,8,16,33,48,True):
            with self.assertRaises(ValueError):
                original_genuine_root_pin_majority_four_swap_cert(invalid)
        for bad in (dict(model,left_labels=((0,1),)*15),
                    dict(model,right_labels=((0,1),)*15),
                    dict(model,incidences=model["incidences"][:-1])):
            with self.assertRaises(ValueError):
                original_fixed_pair_repair_cherry_four_swaps(
                    bad,0,0,byP[0][:2],require_regular=False)

if __name__=="__main__":
    unittest.main()
