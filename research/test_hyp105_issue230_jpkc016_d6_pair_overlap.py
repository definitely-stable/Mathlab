"""Independent second-moment sector, true ORIGINAL source-overlap guards."""
import unittest
from fractions import Fraction
from math import comb, factorial

from hyp105_issue230_projection import fixture
from hyp105_issue230_jpkc015_ensemble_d6_capacity import (
    exact_D6_probability_minimal_alphabet,
)
from hyp105_issue230_jpkc016_d6_pair_overlap import (
    physical_cycle_avoidance_count, physical_cycle_avoidance_bruteforce,
    disjoint_original_source_D6_joint,
    original_W32_anchor_matching, original_W32_anchor_overlap_row,
    analytic_disjoint_original_source_sixmatching_min,
    ensemble_second_moment_disjoint_sector,
)


class JPKC016Tests(unittest.TestCase):
    def test_completely_independent_graph_C6_complement_cycle_oracle(self):
        expected={6:3,7:45,8:327,9:1509}
        for a,answer in expected.items():
            with self.subTest(a=a):
                brute=physical_cycle_avoidance_bruteforce(a)
                self.assertEqual(brute["physical_cycles_avoiding_first_C6"],answer)
                self.assertEqual(physical_cycle_avoidance_count(a),answer)
                self.assertEqual(brute["physical_cycles_total"],60*comb(a,6))
        self.assertGreater(physical_cycle_avoidance_count(14),0)

    def test_exact_true_source_disjoint_joint_is_not_product_of_marginals(self):
        c=disjoint_original_source_D6_joint(6)
        self.assertEqual(c["physical_sixcycles_avoiding_prior_D6_pair_images"],3)
        self.assertEqual(
            Fraction(c["second_D6_conditional_on_first_and_source_disjoint"]),
            Fraction(1,47040))
        self.assertEqual(Fraction(c["joint_two_D6_events_source_factor_disjoint"]),
                         Fraction(1,19639219600))
        self.assertEqual(
            Fraction(c["single_original_matching_D6_probability"]),
            exact_D6_probability_minimal_alphabet(2))
        self.assertGreater(
            Fraction(c["covariance_for_two_source_factor_disjoint_events"]),0)
        self.assertGreater(Fraction(c["joint_over_independent_product"]),8)
        self.assertEqual(Fraction(c["joint_over_independent_product"]),
                         Fraction(20449,2304))
        self.assertLess(Fraction(disjoint_original_source_D6_joint(8)[
            "joint_over_independent_product"]),1)
        self.assertGreater(Fraction(disjoint_original_source_D6_joint(14)[
            "joint_over_independent_product"]),1)
        self.assertFalse(c["different_original_matchings_pairwise_independence_claimed"])
        for a in (7,8,14,35):
            with self.subTest(a=a):
                row=disjoint_original_source_D6_joint(a)
                self.assertGreater(
                    Fraction(row["joint_two_D6_events_source_factor_disjoint"]),0)
                self.assertLessEqual(
                    Fraction(row["joint_two_D6_events_source_factor_disjoint"]),
                    Fraction(row["single_original_matching_D6_probability"]))
        ratio=Fraction(disjoint_original_source_D6_joint(500)[
            "joint_over_independent_product"])
        self.assertLess(abs(ratio-1),Fraction(1,10))

    def test_true_original_W32_anchored_source_overlap_exact_transposition(self):
        m=fixture(1,"lex")
        anchor=original_W32_anchor_matching(m)
        self.assertEqual(len(anchor),len(set(anchor)))
        a=original_W32_anchor_overlap_row(m,anchor)
        b=original_W32_anchor_overlap_row(m,anchor,swapped=True)
        self.assertEqual(a["source_original_six_matching_population"],1566360)
        self.assertEqual(a["source_diagonal_original_six_matching_count"],1)
        self.assertEqual(a["overlap_signature_to_number_of_original_six_matchings"],
                         b["overlap_signature_to_number_of_original_six_matchings"])
        self.assertEqual(a["source_factor_disjoint_six_matching_count"],1556)
        self.assertEqual(a["nonempty_overlap_signatures"],120)
        self.assertEqual(sum(a["overlap_signature_to_number_of_original_six_matchings"].values()),
                         1566360)
        self.assertFalse(a["complete_PAIR_source_overlap_histogram_over_ALL_Q0_claimed"])

    def test_true_disjoint_all_h_source_greedy_second_moment_sector_bounds(self):
        for s in (2,4,8,16):
            with self.subTest(s=s):
                b=analytic_disjoint_original_source_sixmatching_min(s)
                x=ensemble_second_moment_disjoint_sector(
                    s,finite_W32_anchor=(s==2))
                self.assertFalse(x["full_exact_D6_second_moment_computed"])
                self.assertFalse(x["all_source_overlap_gluing_sectors_computed"])
                self.assertGreater(
                    Fraction(x["all_h_rigorous_second_moment_disjoint_sector_lower"]),0)
                self.assertEqual(x["source_disjoint_matching_count_lower_for_every_Q"],
                                 b["rigorous_uniform_over_Q_source_disjoint_matching_lower"])
                if s>=4:
                    self.assertTrue(b["positive_all_h_disjoint_source_count_from_greedy"])
                    self.assertGreater(Fraction(x[
                        "source_disjoint_matching_count_lower_for_every_Q"]),0)
                else:
                    self.assertFalse(b["positive_all_h_disjoint_source_count_from_greedy"])
                    self.assertGreater(x["finite_exact_one_anchor_source_disjoint_count"],0)
                    self.assertGreater(
                        Fraction(x["finite_exact_anchored_pair_second_moment_lower"]),
                        Fraction(x["all_h_rigorous_second_moment_disjoint_sector_lower"]))

    def test_fail_closed_repeated_original_factor_and_illegal_alphabet(self):
        for a in (0,4,5,True,6.5):
            with self.subTest(a=a):
                with self.assertRaises(ValueError):
                    disjoint_original_source_D6_joint(a)
                with self.assertRaises(ValueError):
                    physical_cycle_avoidance_count(a)
        model=fixture(1,"lex")
        anchor=original_W32_anchor_matching(model)
        with self.assertRaisesRegex(ValueError,"genuine bipartite"):
            invalid=tuple(range(6))
            original_W32_anchor_overlap_row(model,invalid)
        with self.assertRaises(ValueError):
            original_W32_anchor_overlap_row(model,anchor,max_states=1)
        with self.assertRaises(ValueError):
            original_W32_anchor_overlap_row(fixture(2,"lex"),anchor)
        with self.assertRaises(ValueError):
            ensemble_second_moment_disjoint_sector(4,finite_W32_anchor=True)


if __name__=="__main__":
    unittest.main()
