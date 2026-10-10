"""C21-D independent original W32 global right D6-zero falsifiers."""
from fractions import Fraction
from itertools import combinations
from collections import Counter
import unittest

from hyp105_g5e2b3e1c21d_adversarial_right import (
    W32_LEX_RIGHT_ZERO_D6, W32_SEVEN_EXPECTED,
    W32_EXPECTED_GF5_NECESSARY_NUMERATOR,
    genuine_global_W32_model,
    direct_original_C6_D6_oracle,
    exact_global_right_swap_neighborhood,
    genuine_W32_C21D_certificate,
)


class C21DAdversarialGlobalRightTests(unittest.TestCase):
    def test_legal_single_global_original_right_permutation(self):
        self.assertEqual(len(W32_LEX_RIGHT_ZERO_D6), 15)
        self.assertEqual(set(W32_LEX_RIGHT_ZERO_D6), set(range(15)))
        m = genuine_global_W32_model()
        self.assertEqual(len(m["incidences"]), 45)
        self.assertEqual(len(set(m["left_labels"])), 15)
        self.assertEqual(len(set(m["right_labels"])), 15)
        self.assertEqual([len([e for e in m["incidences"] if e[0]==p])
                          for p in range(15)], [3]*15)
        self.assertEqual([len([e for e in m["incidences"] if e[1]==l])
                          for l in range(15)], [3]*15)

    def test_original_C6_right_distinct_and_direct_zero_D6(self):
        model = genuine_global_W32_model()
        found = direct_original_C6_D6_oracle(model)
        self.assertEqual(found["physical_left_C6"], 60)
        self.assertEqual(found["true_original_left_C6_sixsets"], 43740)
        self.assertEqual(found["true_original_right_distinct_left_C6_sixsets"], 18716)
        self.assertEqual(sum(found["per_physical_left_C6_right_distinct_counts"]),18716)
        self.assertEqual(found["independent_direct_strict_D6"], 0)

    def test_complete_seven_class_witness_positive_but_strict_D6_zero(self):
        result = genuine_W32_C21D_certificate()
        self.assertTrue(result["right_permutation_is_one_complete_global_bijection"])
        self.assertEqual(result["actual_true_original_seven_family_counts"],
                         W32_SEVEN_EXPECTED)
        self.assertEqual(result["actual_seven_total"],146)
        self.assertEqual(result["actual_GF5_seven_necessary_numerator"],
                         W32_EXPECTED_GF5_NECESSARY_NUMERATOR)
        self.assertEqual(result["independent_weighted_B_left_A_right"],60)
        self.assertEqual(Fraction(result["common_random_right_D6_exact_mean_for_this_f"]),
                         Fraction(18716,5005))
        self.assertTrue(result["restricted_s2_fixed_f_min_over_all_right_g_exactly_zero"])
        self.assertTrue(result["no_all_h_counterexample_family_proved"])

    def test_independent_identity_global_right_baseline_is_not_zero(self):
        # Same actual W32 original left f, a DIFFERENT legal complete right g.
        # Both direct 60x3^6 and full seven_class agree on actual D6.
        reference = genuine_W32_C21D_certificate(tuple(range(15)))
        self.assertEqual(reference["actual_true_original_seven_family_counts"]["D6"],15)
        self.assertEqual(reference["direct_C6_original_right_D6"][
            "independent_direct_strict_D6"],15)
        self.assertEqual(reference["actual_seven_total"],259)
        self.assertEqual(reference["independent_weighted_B_left_A_right"],98)
        self.assertFalse(reference["restricted_s2_fixed_f_min_over_all_right_g_exactly_zero"])

    def test_all_105_actual_one_swap_right_maps_exact_D6_histogram(self):
        neighborhood = exact_global_right_swap_neighborhood()
        self.assertEqual(neighborhood["shared_original_right_source"],18716)
        self.assertEqual(neighborhood["one_global_right_transposition_neighbors"],105)
        self.assertEqual(neighborhood["D6_histogram"],
                         {0:40, 1:29, 2:24, 3:6, 4:4, 5:1, 9:1})
        self.assertEqual(neighborhood["zero_D6_right_swap_neighbors"],40)
        self.assertTrue(
            neighborhood["not_global_right_full_15_factorial_minimum_enumeration"])
        self.assertTrue(neighborhood["not_all_h_or_all_seven_no_go"])

    def test_invalid_global_right_maps_and_budget_fail_closed(self):
        for bad in (
            (), tuple(range(14)), tuple(range(14))+(13,),
            tuple(range(14))+(99,), tuple(range(14))+(True,),
            tuple(range(14))+("14",),
        ):
            with self.assertRaises(ValueError):
                genuine_global_W32_model(bad)
        for cap in (0, 1, -1, 43739, True, 43740.0):
            with self.assertRaises(ValueError):
                direct_original_C6_D6_oracle(
                    genuine_global_W32_model(),max_original_sixsets=cap)

    def test_zero_D6_not_universal_all_h_or_seven_sum_zero(self):
        c = genuine_W32_C21D_certificate()
        self.assertEqual(c["actual_true_original_seven_family_counts"]["D6"],0)
        self.assertGreater(c["actual_seven_total"],0)
        self.assertTrue(c["no_all_h_counterexample_family_proved"])
        self.assertTrue(c["no_all_g_seven_S_zero_or_GF5_R3_upper"])


if __name__ == "__main__":
    unittest.main()
