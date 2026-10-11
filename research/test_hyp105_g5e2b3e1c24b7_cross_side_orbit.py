"""HYP-105 C24-B7: all-h common-universe joint support and typed W32 maps.

Lightweight tests only; FULL 11236-cell audit is deliberately an explicit
hosted Contract/Research step to prevent hidden 105x105 broad-unit repeats.
"""
from itertools import combinations
from math import comb
import unittest

from hyp105_g5e2b3e1c24_right_c_certificate import original_W32
from hyp105_g5e2b3e1c24b_three_collision import W32_LEFT_H45
from hyp105_g5e2b3e1c24b2_joint_seven import (
    TAGS, compile_left, full_left_score, right_first_independent)
from hyp105_g5e2b3e1c24b3_joint_swap_gradient import legal_transpose
from hyp105_g5e2b3e1c24b5_two_swap_escape import (
    compile_right_pullback_fibers, template_pullback_score)
from hyp105_g5e2b3e1c24b6_mixed_curvature_s68 import W32_RIGHT_S68
from hyp105_g5e2b3e1c24b7_cross_side_orbit import (
    PAIRS, all_h_original_gq_cross_touch_bound, binom_or_zero,
    exact_cross_touch_universe_count, original_w32_point_line_cross_overlap)


class OriginalW32MixedSideTest(unittest.TestCase):
    def test_independent_unrestricted_incidence_k_subset_exact_counts(self):
        # Independent direct finite subsets, not the same inclusion-exclusion
        # arithmetic as the production all-h support oracle.
        for E in (6, 7, 8):
            U=set(range(E))
            for left in combinations(range(E), 2):
                L=set(left)
                for right in combinations(range(E), 3):
                    R=set(right)
                    overlap=len(L & R)
                    for k in (1,2,3,4,6):
                        direct=sum(bool(L&set(j)) and bool(R&set(j))
                                   for j in combinations(range(E), k))
                        self.assertEqual(
                            exact_cross_touch_universe_count(
                                E,len(L),len(R),overlap,k),
                            direct,(E,left,right,k))
        for x in ((4,3,3,0,3),(8,2,3,4,6),(8,-1,3,0,6),
                  (8,2,3,1,-1),(True,2,3,1,6)):
            with self.assertRaises(ValueError):
                exact_cross_touch_universe_count(*x)

    def test_true_gq_all_h_source_bound_scope(self):
        for s in (2,4,8):
            v=(s+1)*(s*s+1)
            e=v*(s+1)
            d=2*(s+1)
            values=[]
            for c in range(4):
                row=all_h_original_gq_cross_touch_bound(s,c)
                self.assertEqual(row["original_point_and_line_count"],v)
                self.assertEqual(row["original_incidence_count"],e)
                self.assertEqual(row["point_swap_incident_edges"],d)
                self.assertEqual(row["line_swap_incident_edges"],d)
                self.assertEqual(
                    row["original_distinct_sixset_joint_touch_upper"],
                    comb(e,6)-2*comb(e-d,6)+comb(e-2*d+c,6))
                self.assertTrue(row["does_not_prove_asymptotic_Os6_or_positivity"])
                values.append(row["absolute_signed_cross_curvature_upper"])
            self.assertEqual(values,sorted(values))
        for s,c in ((3,0),(1,0),(2,4),(2,-1),(2,1.0),(True,0)):
            with self.assertRaises(ValueError):
                all_h_original_gq_cross_touch_bound(s,c)

    def test_true_original_W32_overlap_has_no_incidence_four_cycle(self):
        _,lines,_=original_W32()
        self.assertEqual(len(lines),15)
        histogram={}
        for a in PAIRS:
            for b in PAIRS:
                c=original_w32_point_line_cross_overlap(a,b,lines)
                histogram[c]=histogram.get(c,0)+1
                self.assertTrue(0<=c<=3)
        self.assertEqual(sum(histogram.values()),11025)
        self.assertEqual(set(histogram),set(range(4)))
        with self.assertRaises(ValueError):
            original_w32_point_line_cross_overlap((1,0),(2,3),lines)

    def test_different_left_maps_recompile_original_eligible_source(self):
        f0=tuple(W32_LEFT_H45)
        g0=W32_RIGHT_S68
        source=compile_left(f0)
        base=full_left_score(source,g0)
        self.assertEqual(base["S_seven"],68)
        for a,b in (((0,1),(2,3)),((4,14),(0,12))):
            fa=legal_transpose(f0,*a)
            gb=legal_transpose(g0,*b)
            src=compile_left(fa)
            self.assertEqual(src["left_source_size"],62370)
            self.assertNotEqual(src["f"],source["f"])
            fibers=compile_right_pullback_fibers(src)
            left=template_pullback_score(fibers,g0)
            joint=template_pullback_score(fibers,gb)
            self.assertEqual(left,full_left_score(src,g0))
            self.assertEqual(joint,full_left_score(src,gb))
            independent=right_first_independent(fa,gb)
            self.assertEqual(joint["S_seven"],independent["S_seven"])
            self.assertEqual(joint["seven_counts"],independent["seven_counts"])
            self.assertEqual(joint["right_C_accepted"],independent["right_C_accepted"])
            right=full_left_score(source,gb)
            mixed=(joint["S_seven"]-left["S_seven"]-
                   right["S_seven"]+base["S_seven"])
            _,lines,_=original_W32()
            c=original_w32_point_line_cross_overlap(a,b,lines)
            bound=all_h_original_gq_cross_touch_bound(2,c)
            self.assertLessEqual(abs(mixed),
                                 bound["absolute_signed_cross_curvature_upper"])


if __name__=="__main__":
    unittest.main()
