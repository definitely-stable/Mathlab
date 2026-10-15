"""Independent fixed-f two-original-D6 globally injected one-g pair tests."""
import unittest
from fractions import Fraction
from itertools import combinations,permutations
from math import comb,perm

from hyp105_issue230_d6aa4tcyc_fixed_f_d6_pair import (
    physical_C6_complement_inclusion_exclusion,
    exact_one_sided_fixed_f_disjoint_LINE_D6_kernel,
    brute_physical_Ka_cycle_complement,
    genuine_W32_fixed_f_anchored_line_overlap,
    independent_real_W32_two_Q_one_complete_g,
    genuine_W32_fixed_f_original_connected_left_Q,
)


class GenuineFixedFConditionalTwoD6Tests(unittest.TestCase):
    def test_001_exact_64_subsets_vs_independent_simple_physical_cycle_brute(self):
        pinned={6:3,7:45,8:327,9:1509}
        for a,H in pinned.items():
            x=brute_physical_Ka_cycle_complement(a)
            y=physical_C6_complement_inclusion_exclusion(a)
            self.assertEqual(x["brute_disjoint_from_fixed_C6"],H)
            self.assertEqual(y["physical_Ka_C6_avoiding_fixed_C6_H"],H)
            self.assertEqual(x["brute_physical_C6_total"],perm(a,6)//12)
            self.assertEqual(y["number_of_exact_64_inclusion_exclusion_subsets"],64)
            self.assertEqual(y["included_subsets_by_cardinality_weighted_sums"][6],1)
            self.assertEqual(y["included_subsets_by_cardinality_weighted_sums"][0],perm(a,6)//12)

    def test_002_exact_all_h_two_true_D6_given_fixed_point_map_probability(self):
        for h in range(1,17):
            s=1<<h
            z=exact_one_sided_fixed_f_disjoint_LINE_D6_kernel(s)
            a=z["a"]; K=z["K"]
            p=Fraction(perm(a,6),perm(K,6))
            H=physical_C6_complement_inclusion_exclusion(a)[
                "physical_Ka_C6_avoiding_fixed_C6_H"]
            q=Fraction(12*H,perm(K-6,6))
            self.assertEqual(
                Fraction(z["exact_single_Q_D6_probability_fixed_f_uniform_complete_g"]),p)
            self.assertEqual(
                Fraction(z["exact_second_Q_D6_given_first_AND_disjoint_original_line_factors"]),q)
            self.assertEqual(
                Fraction(z["exact_two_Q_D6_joint_probability_disjoint_original_LINE_factors"]),p*q)
            self.assertEqual(Fraction(z["exact_conditional_covariance"]),p*(q-p))
            self.assertEqual(Fraction(z["joint_over_independent_product"]),q/p)
            self.assertTrue(z["true_original_POINT_factors_between_Q_may_overlap"])
            self.assertFalse(z["full_conditional_variance_PROVED"])
            self.assertFalse(z["all_h_root_minimax_seven_positive_PROVED"])

    def test_003_exact_K6_conditional_depletion_and_covariance_sign_changes(self):
        z=exact_one_sided_fixed_f_disjoint_LINE_D6_kernel(2)
        self.assertEqual(z["a"],6)
        self.assertEqual(z["physical_C6_complement_count_H"],3)
        self.assertEqual(z["exact_single_Q_D6_probability_fixed_f_uniform_complete_g"],"1/5005")
        self.assertEqual(z["exact_second_Q_D6_given_first_AND_disjoint_original_line_factors"],"1/1680")
        self.assertEqual(z["exact_two_Q_D6_joint_probability_disjoint_original_LINE_factors"],"1/8408400")
        self.assertEqual(z["covariance_sign"],"positive")
        self.assertNotEqual(Fraction(z["joint_over_independent_product"]),1)
        # s=4 uses a=14; the sign is not silently assumed from the
        # small K6 physical alphabet for larger original GQ hosts.
        for s in (4,8,16,32):
            z=exact_one_sided_fixed_f_disjoint_LINE_D6_kernel(s)
            self.assertNotEqual(Fraction(z["joint_over_independent_product"]),0)

    def test_004_true_W32_frozen_f_anchored_original_line_overlap_counts(self):
        for scheme in ("S68","S72"):
            m,rows=genuine_W32_fixed_f_original_connected_left_Q(scheme)
            r=genuine_W32_fixed_f_anchored_line_overlap(scheme)
            self.assertEqual(len(rows),21186)
            self.assertEqual(r["true_original_W32_left_C6_six_incidence_Q_count"],21186)
            self.assertEqual(sum(r["anchor_original_line_support_overlap_histogram"].values()),21186)
            self.assertGreater(r["number_of_LINE_disjoint_Q_in_one_anchored_row"],0)
            self.assertEqual(r["anchor_original_line_support_overlap_histogram"][0],
                             r["number_of_LINE_disjoint_Q_in_one_anchored_row"])
            self.assertTrue(r["anchor_and_other_LINE_factors_disjoint"])
            self.assertTrue(r["anchor_and_other_POINT_factors_overlap"])
            self.assertTrue(r["anchored_row_is_NOT_full_conditional_variance"])
            kernel=exact_one_sided_fixed_f_disjoint_LINE_D6_kernel(2)
            self.assertEqual(Fraction(
                r["anchored_row_DISJOINT_sector_partial_E_D6_squared_contribution"]),
                Fraction(r["number_of_LINE_disjoint_Q_in_one_anchored_row"])*
                Fraction(kernel["exact_two_Q_D6_joint_probability_disjoint_original_LINE_factors"]))

    def test_005_two_actual_original_source_Q_simultaneously_positive_D6_same_g(self):
        from hyp105_issue230_projection import fixture
        from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
        for scheme in ("S68","S72"):
            r=independent_real_W32_two_Q_one_complete_g(scheme)
            original=fixture(1,scheme)
            f=tuple(tuple(x) for x in original["left_labels"])
            inc=tuple(original["incidences"])
            g=tuple(tuple(x) for x in r["same_global_complete_right_physical_edge_labels"])
            self.assertEqual(len(g),15)
            self.assertEqual(set(g),set(combinations(range(6),2)))
            Q0=r["real_original_Q0"];Q1=r["real_original_Q1"]
            self.assertEqual(len(set(Q0)),6)
            self.assertEqual(len(set(Q1)),6)
            self.assertTrue(set(inc[q][0] for q in Q0)&
                            set(inc[q][0] for q in Q1))
            self.assertFalse(set(inc[q][1] for q in Q0)&
                             set(inc[q][1] for q in Q1))
            self.assertEqual(classify_seven_prechecked(Q0,f,g,inc),"D6")
            self.assertEqual(classify_seven_prechecked(Q1,f,g,inc),"D6")
            self.assertEqual(r["number_second_right_alignment_tuples_without_first_six_edges"],36)
            self.assertEqual(r["conditional_probability_second_D6_given_first_and_disjoint_lines"],"1/1680")
            self.assertTrue(r["one_COMPLETE_right_mapping_accepts_BOTH_true_original_D6_Q"])

    def test_006_valid_kernel_limits_invalid_physical_a_and_model(self):
        for a in (0,1,5,10,True,-1):
            with self.assertRaises(ValueError):
                brute_physical_Ka_cycle_complement(a)
        for a in (0,1,5,True,False,-1):
            with self.assertRaises(ValueError):
                physical_C6_complement_inclusion_exclusion(a)
        for s in (-4,0,1,3,6,True,False):
            with self.assertRaises(ValueError):
                exact_one_sided_fixed_f_disjoint_LINE_D6_kernel(s)


if __name__=="__main__":
    unittest.main()
