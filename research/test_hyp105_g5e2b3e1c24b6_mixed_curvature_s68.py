"""HYP-105 C24-B6: fast exact support arithmetic and genuine original W32 tests.

The exhaustive new 5005-state scan lives in the explicit Contract/Research
report command, not duplicated inside broad unittest discovery.
"""
from itertools import combinations
from math import comb
import unittest

from hyp105_g5e2b3e1c24b_three_collision import W32_LEFT_H45
from hyp105_g5e2b3e1c24b2_joint_seven import (
    TAGS, compile_left, full_left_score, right_first_independent)
from hyp105_g5e2b3e1c24b3_joint_swap_gradient import legal_transpose
from hyp105_g5e2b3e1c24b5_two_swap_escape import (
    compile_right_pullback_fibers, template_pullback_score,
    independent_disjoint_original_source_curvature)
from hyp105_g5e2b3e1c24b6_mixed_curvature_s68 import (
    W32_RIGHT_S68, W32_S68_VECTOR, both_touch_disjoint_swap_pair_count,
    exact_all_disjoint_joint_exposure, choose_nonnegative)


class TrueOriginalW32B6Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = compile_left(W32_LEFT_H45)
        cls.fibers = compile_right_pullback_fibers(cls.source)

    def test_exhaustive_small_n_joint_touch_pair_count(self):
        for n in (4, 5, 6):
            edges = tuple(combinations(range(n), 2))
            for r in range(n+1):
                H = set(range(r))
                direct = sum(1 for a,b in combinations(edges, 2)
                             if set(a).isdisjoint(b) and set(a)&H and set(b)&H)
                self.assertEqual(both_touch_disjoint_swap_pair_count(n,r),direct,
                                 (n,r))
        self.assertEqual(both_touch_disjoint_swap_pair_count(15,0),0)
        self.assertEqual(both_touch_disjoint_swap_pair_count(15,1),0)
        self.assertEqual(both_touch_disjoint_swap_pair_count(15,15),
                         3*comb(15,4))
        for args in ((3,2),(4,-1),(4,5),(True,1),(4,1.5)):
            with self.assertRaises(ValueError):
                both_touch_disjoint_swap_pair_count(*args)
        self.assertEqual(choose_nonnegative(2,3),0)
        self.assertEqual(choose_nonnegative(-1,2),0)

    def test_original_source_exposure_conservation(self):
        r = exact_all_disjoint_joint_exposure(self.source)
        self.assertEqual(r["n_original_right"],15)
        self.assertEqual(r["original_candidate_sixsets"],53907)
        self.assertEqual(r["unordered_disjoint_pairs"],4095)
        self.assertEqual(sum(r["original_right_support_histogram"].values()),
                         r["original_candidate_sixsets"])
        self.assertEqual(r["sum_absolute_mixed_curvature_upper"],
                         2*r["sum_jointly_touched_original_sources_over_all_pairs"])
        self.assertTrue(r["bound_proved_all_h"])
        self.assertTrue(r["does_not_imply_positive_seven_minimum"])
        with self.assertRaises(ValueError):
            exact_all_disjoint_joint_exposure({"left_source_size":1,"by_line":[]})

    def test_frozen_b5_s68_complete_global_right(self):
        g = W32_RIGHT_S68
        row = template_pullback_score(self.fibers, g)
        self.assertEqual(row["S_seven"],68)
        self.assertEqual(tuple(row["seven_counts"][t] for t in TAGS),
                         W32_S68_VECTOR)
        self.assertEqual(row["Q7_necessary_numerator"],3112510)
        self.assertEqual(row["right_C_accepted"],0)
        self.assertEqual(row,full_left_score(self.source,g))
        right = right_first_independent(W32_LEFT_H45,g)
        self.assertEqual(right["seven_counts"],row["seven_counts"])

    def test_genuine_source_curvature_not_only_total_four_scores(self):
        g=W32_RIGHT_S68
        a,b=(4,14),(3,12)
        for x,y in ((a,b),(b,a)):
            q=independent_disjoint_original_source_curvature(
                self.source,g,x,y)
            self.assertEqual(q["mixed_curvature"],
                             sum(q["mixed_curvature_by_tag"].values()))
            self.assertLessEqual(abs(q["mixed_curvature"]),
                                 2*q["jointly_touched_original_sixsets"])
            ga=legal_transpose(g,*x)
            gb=legal_transpose(g,*y)
            gab=legal_transpose(ga,*y)
            self.assertEqual(q["mixed_curvature"],
                 full_left_score(self.source,gab)["S_seven"]
                 -full_left_score(self.source,ga)["S_seven"]
                 -full_left_score(self.source,gb)["S_seven"]
                 +full_left_score(self.source,g)["S_seven"])
        with self.assertRaises(ValueError):
            independent_disjoint_original_source_curvature(
                self.source,g,(4,14),(4,12))


if __name__ == "__main__":
    unittest.main()
