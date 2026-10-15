"""Independent genuine original D6 shared source LINE cycle-gluing tests."""
import unittest
from itertools import combinations, permutations
from fractions import Fraction
from math import perm

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
from hyp105_issue230_d6aa4ucyc_shared_line_gluing import (
    canonical_two_source_C6_gluing,
    exact_second_cycle_coordinate_color_coefficients,
    exact_two_D6_gluing_kernel,
    brute_given_first_SIX_physical_right_color_assignments,
    genuine_W32_anchored_FULL_shared_line_D6_kernel,
    independent_W32_TWO_real_D6_global_right_completion,
    _actual_original_Q_line_cycle,
)


class TrueOriginalSharedLineCycleGluingTests(unittest.TestCase):
    def test_001_exact_falling_factorial_kernels_vs_independent_6color_brute(self):
        examples=(
            (6,7,8,9,10,11),   # r0, original T-CYC
            (0,6,7,8,9,10),    # r1
            (0,1,6,7,8,9),     # r2 with nonadjacent color requirement
            (0,6,3,7,8,9),    # r2 possible
            (0,2,6,7,8,9),    # r2 impossible for any a
            (0,1,2,6,7,8),    # r3
            (0,1,2,3,4,5),    # same r6 cycle, equal event
            (0,1,2,3,5,4),    # r6 changed physical right cycle, mutually exclusive
        )
        for second in examples:
            kind=canonical_two_source_C6_gluing(tuple(range(6)),second)
            z=exact_second_cycle_coordinate_color_coefficients(kind)
            brute=brute_given_first_SIX_physical_right_color_assignments(kind)
            self.assertEqual(z[0],brute)
            self.assertEqual(len(z),7)
            self.assertTrue(all(type(x) is int and x>=0 for x in z))
            exact=exact_two_D6_gluing_kernel(2,tuple(range(6)),second)
            r=sum(x<6 for x in kind)
            self.assertEqual(exact["source_line_shared_count"],r)
            self.assertEqual(Fraction(exact["joint_probability_one_complete_GLOBAL_g"]),
                             Fraction(perm(6,6)*brute,perm(15,12-r)))
            self.assertTrue(exact["same_one_global_source_line_label_map"])
            self.assertFalse(exact["full_conditional_second_moment_PROVED"])

    def test_002_original_line_cyclic_GLUE_not_just_overlap_count(self):
        positive=exact_two_D6_gluing_kernel(2,(0,1,2,3,4,5),(0,6,3,7,8,9))
        impossible=exact_two_D6_gluing_kernel(2,(0,1,2,3,4,5),(0,2,6,7,8,9))
        self.assertEqual(positive["source_line_shared_count"],2)
        self.assertEqual(impossible["source_line_shared_count"],2)
        self.assertGreater(Fraction(positive["joint_probability_one_complete_GLOBAL_g"]),0)
        self.assertEqual(Fraction(impossible["joint_probability_one_complete_GLOBAL_g"]),0)
        self.assertNotEqual(positive["canonical_ORIGINAL_line_C6_gluing"],
                            impossible["canonical_ORIGINAL_line_C6_gluing"])
        self.assertEqual(exact_two_D6_gluing_kernel(
            2,(0,1,2,3,4,5),(0,1,2,3,4,5))[
                "joint_probability_one_complete_GLOBAL_g"],"1/5005")
        self.assertEqual(exact_two_D6_gluing_kernel(
            2,(0,1,2,3,4,5),(0,1,2,3,5,4))[
                "joint_probability_one_complete_GLOBAL_g"],"0")

    def test_003_original_two_cycle_gluing_genuine_GQ_dual_independent_canon(self):
        first=(10,11,12,13,14,15)
        second=(10,16,13,17,18,19)
        initial=canonical_two_source_C6_gluing(first,second)
        for rot in range(6):
            for sign in (-1,1):
                f=tuple(first[(rot+sign*i)%6] for i in range(6))
                for shift in range(6):
                    for flip in (-1,1):
                        r=tuple(second[(shift+flip*i)%6] for i in range(6))
                        self.assertEqual(initial,canonical_two_source_C6_gluing(f,r))
        self.assertEqual(sum(x<6 for x in initial),2)
        # A line graph of 6 original source line factors and two physical
        # C6 halfs. This is a combinatorial type test; actual GQ
        # membership is independently enforced in the source oracle.

    def test_004_all_h_genuine_minimal_Ka_r0_and_r6_recover_parent(self):
        for h in range(1,15):
            s=1<<h
            z0=exact_two_D6_gluing_kernel(s,
                (0,1,2,3,4,5),(6,7,8,9,10,11))
            p=Fraction(z0["one_event_true_original_D6_probability"])
            self.assertGreater(Fraction(z0["joint_probability_one_complete_GLOBAL_g"]),0)
            identical=exact_two_D6_gluing_kernel(s,
                (0,1,2,3,4,5),(0,1,2,3,4,5))
            disagree=exact_two_D6_gluing_kernel(s,
                (0,1,2,3,4,5),(0,1,2,3,5,4))
            self.assertEqual(Fraction(identical[
                "joint_probability_one_complete_GLOBAL_g"]),p)
            self.assertEqual(Fraction(disagree[
                "joint_probability_one_complete_GLOBAL_g"]),0)
            self.assertFalse(z0["all_maps_global_seven_GF5_lower_PROVED"])

    def test_005_actual_W32_original_S68_S72_anchored_all_21186_Q(self):
        for scheme in ("S68","S72"):
            z=genuine_W32_anchored_FULL_shared_line_D6_kernel(scheme)
            self.assertEqual(z["source_Q_in_true_original_anchored_row"],21186)
            self.assertEqual(z["source_right_LINE_overlap_counts"],{
                0:305,1:3061,2:7934,3:7173,4:2426,5:279,6:8})
            self.assertGreater(z["distinct_two_C6_gluing_isomorphism_types"],5)
            self.assertEqual(
                z["number_positive_joint_probability_pairs_from_this_anchor"]+
                z["number_zero_joint_probability_pairs_from_this_anchor"],21186)
            self.assertEqual(sum(z["exact_original_gluing_type_counts"].values()),21186)
            self.assertGreater(Fraction(z[
                "exact_all_21186_genuine_Q_anchored_joint_D6_probability_sum"]),Fraction(1,5005))
            self.assertTrue(z["partial_anchored_row_NOT_full_conditional_second_moment"])

    def test_006_two_TRUE_ORIGINAL_W32_Q_r2_different_physical_gluings(self):
        for scheme in ("S68","S72"):
            yes=independent_W32_TWO_real_D6_global_right_completion(scheme,
                    shared_count=2,require_positive=True)
            no=independent_W32_TWO_real_D6_global_right_completion(scheme,
                    shared_count=2,require_positive=False)
            self.assertEqual(yes["shared_original_LINE_source_factors"],2)
            self.assertEqual(no["shared_original_LINE_source_factors"],2)
            self.assertGreater(yes["exact_independent_SIX_physical_color_bruteforce_count"],0)
            self.assertEqual(no["exact_independent_SIX_physical_color_bruteforce_count"],0)
            self.assertIsNone(no["one_complete_g_construction"])
            g=tuple(tuple(e) for e in yes["one_complete_g_construction"])
            self.assertEqual(len(g),15)
            self.assertEqual(set(g),set(combinations(range(6),2)))
            m=fixture(1,scheme)
            f=m["left_labels"];inc=m["incidences"]
            self.assertEqual(
                classify_seven_prechecked(yes["Q0_original_six_incidence_IDs"],f,g,inc),
                "D6")
            self.assertEqual(
                classify_seven_prechecked(yes["Q1_original_six_incidence_IDs"],f,g,inc),
                "D6")
            self.assertEqual(yes["historical_original_Q_two_GF5_tags"],("D6","D6"))

    def test_007_fail_closed_invalid_original_two_cycle_gluing(self):
        for bad in ((0,0,1,2,3,4),(0,1,2),(0,1,2,3,4,13)):
            with self.assertRaises(ValueError):
                exact_second_cycle_coordinate_color_coefficients(bad)
        for bad in ((0,0,1,2,3,4),(0,1,2)):
            with self.assertRaises(ValueError):
                canonical_two_source_C6_gluing(tuple(range(6)),bad)
        for s in (0,1,3,True,False):
            with self.assertRaises(ValueError):
                exact_two_D6_gluing_kernel(s,tuple(range(6)),tuple(range(6,12)))


if __name__=="__main__":
    unittest.main()
