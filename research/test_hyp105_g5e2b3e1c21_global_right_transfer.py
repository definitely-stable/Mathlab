"""Independent C21 all-h arithmetic, physical D6, and genuine W32 oracles."""
from fractions import Fraction
from itertools import combinations, product
from math import comb, perm
import unittest

from hyp105_g5e2b3e1c20_global_left_c6 import all_h_global_left_c6_lower
from hyp105_g5e2b3e1c21_global_right_transfer import (
    _gq_right_distinct_floor,
    _line_sdr_dp,
    all_h_global_random_right_D6_transfer,
    all_h_joint_uniform_right_seven_mean_lower,
    exact_K6_D6_compatible_right_orderings,
    genuine_W32_C21_report,
)


class C21GlobalRightTransferTests(unittest.TestCase):
    def test_all_h_exact_rational_shared_right_mean_not_all_g(self):
        for s in (2, 4, 8, 16, 32, 64, 128):
            new = all_h_global_random_right_D6_transfer(s)
            prior = all_h_global_left_c6_lower(s)
            c6 = prior["certified_remaining_physical_six_cycles"]
            d = s+1
            self.assertEqual(new["right_distinct_original_line_lifts_per_left_C6_floor"],
                             max(1, d**6-15*d**4))
            self.assertEqual(new["certified_leftC6_rightDistinct_original_sixsets"],
                             c6*max(1, d**6-15*d**4))
            prob = Fraction(new["one_common_uniform_random_right_D6_probability_floor"])
            mean = Fraction(new["one_common_uniform_random_right_D6_expectation_floor"])
            self.assertEqual(prob, Fraction(12*c6, perm(prior["original_GQ_points"],6)))
            self.assertEqual(mean, prob*c6*_gq_right_distinct_floor(s))
            self.assertGreater(mean, 0)
            self.assertTrue(new["not_fixed_adversarial_g_lower"])
        self.assertEqual(_gq_right_distinct_floor(4), 6250)
        self.assertEqual(_gq_right_distinct_floor(2), 1)

    def test_same_global_g_C5_BA_plus_C21_D6_joint_mean(self):
        from hyp105_g5e2b3e1c5_common_bijection import occupied_target_uniform_floor
        for s in (2, 4, 8, 16, 32, 64, 128):
            combined = all_h_joint_uniform_right_seven_mean_lower(s)
            b = Fraction(combined["C5_B_left_A_right_mean_lower"])
            d = Fraction(combined["C21_D6_mean_lower"])
            total = Fraction(
                combined["same_global_random_g_disjoint_seven_classes_mean_lower"])
            self.assertEqual(b, occupied_target_uniform_floor(s)[
                "one_common_right_bijection_mean_lower"])
            self.assertEqual(d, Fraction(all_h_global_random_right_D6_transfer(s)[
                "one_common_uniform_random_right_D6_expectation_floor"]))
            self.assertEqual(total, b+d)
            self.assertTrue(combined["same_g_without_independence"])
            self.assertTrue(combined["not_adversarial_minimum"])
            self.assertEqual(
                Fraction(combined["same_global_random_g_GF5_R3_necessary_mean_lower"]),
                (45600*b+5643*d)/51**6)
        self.assertGreater(Fraction(
            all_h_joint_uniform_right_seven_mean_lower(4)[
                "same_global_random_g_disjoint_seven_classes_mean_lower"]), 0)

    def test_s2_exact_K6_right_D6_ordered_cycle_isomorphisms(self):
        info = exact_K6_D6_compatible_right_orderings()
        self.assertEqual(info["right_C6"], 60)
        self.assertEqual(info["compatible_ordered_right_edge_six_tuples"], 720)
        self.assertEqual(Fraction(info["right_D6_probability_exact"]),
                         Fraction(1, 5005))
        self.assertEqual(
            all_h_global_random_right_D6_transfer(2)[
                "one_common_uniform_random_right_D6_probability_floor"],
            "1/5005")

    def test_GQ_regular_Hall_and_collision_count_tiny_independent_model(self):
        # A 3-regular bipartite 6+6 host: each of six ORIGINAL points has
        # three ORIGINAL lines. All six can choose distinct lines.
        n = tuple(tuple(sorted(((i+j) % 6 for j in range(3))))
                  for i in range(6))
        by_product = sum(len(set(chosen)) == 6 for chosen in product(*n))
        self.assertEqual(_line_sdr_dp(n), by_product)
        self.assertGreater(by_product, 0)
        # Six distinct points with disjoint neighbor sets have Delta^6 SDR.
        d = tuple(tuple(3*i+j for j in range(3)) for i in range(6))
        self.assertEqual(_line_sdr_dp(d), 3**6)

    def test_GQ_collision_union_bound_for_s4_and_higher(self):
        for s in (4, 8, 16, 32):
            d = s + 1
            self.assertEqual(_gq_right_distinct_floor(s), d**6-15*d**4)
            self.assertGreater(d**6-15*d**4, 0)
            # Pair-collision count is 15*Delta^4, using at most ONE
            # common source line of two different GQ points.
            self.assertEqual(comb(6, 2)*d**4, 15*d**4)

    def test_exact_real_W32_cyclewise_DP_product_and_fixed_right_D6(self):
        report = genuine_W32_C21_report()
        cases = report["four_true_global_original_GQ_left_mappings"]
        self.assertEqual(len(cases), 4)
        self.assertEqual({x["scheme"] for x in cases}, {"lex", "reverse-line"})
        self.assertEqual({x["global_original_left_relabel"] for x in cases},
                         {"original", "swap-original-0-13"})
        for x in cases:
            self.assertEqual(x["true_original_left_C6_sixsets"], 43740)
            distinct = x["right_distinct_original_line_sixsets"]
            self.assertTrue(60 <= distinct <= 43740)
            self.assertEqual(sum(x["per_left_cycle_SDR_histogram"].values()), 60)
            self.assertEqual(sum(k*v for k,v in x["per_left_cycle_SDR_histogram"].items()),
                             distinct)
            self.assertEqual(Fraction(x["one_shared_uniform_random_global_right_D6_exact_mean"]),
                             Fraction(distinct,5005))
            self.assertEqual(
                Fraction(x["one_shared_global_right_joint_B_plus_D6_exact_mean"]),
                Fraction(x["one_shared_uniform_random_global_right_B_left_A_right_exact_mean"])
                + Fraction(x["one_shared_uniform_random_global_right_D6_exact_mean"]))
            self.assertGreaterEqual(x["true_actual_one_fixed_global_right_B_left_A_right"],0)
            self.assertTrue(x["independently_verified_SDR_dynamic_program"])
            self.assertTrue(x["finite_adversarial_minimum_not_proved"])
        # Independently enumerate the historical full seven-class source
        # for the two unchanged, genuine common GLOBAL left/right maps.
        from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
        from hyp105_g5e2b3e1b0_seven_signature import seven_census
        for scheme in ("lex", "reverse-line"):
            historical = seven_census(
                pair_labeled_symplectic(1,scheme),
                independent_checks=False)["seven_class_motif_counts"]
            expected_D6 = historical["D6"]
            actual_D6 = next(x["true_actual_one_fixed_global_right_D6"]
                             for x in cases if x["scheme"]==scheme and
                             x["global_original_left_relabel"]=="original")
            self.assertEqual(actual_D6, expected_D6)
            actual_B = next(x["true_actual_one_fixed_global_right_B_left_A_right"]
                            for x in cases if x["scheme"]==scheme and
                            x["global_original_left_relabel"]=="original")
            self.assertEqual(actual_B, historical["B-left/A-right"])

    def test_bad_inputs_and_enumeration_cap_fail_closed(self):
        for s in (0, 1, 3, 6, True, "4"):
            with self.assertRaises(ValueError):
                all_h_global_random_right_D6_transfer(s)
        for cap in (0, -1, True, "174960", 174959):
            with self.assertRaises(ValueError):
                genuine_W32_C21_report(max_sixset_evaluations=cap)


if __name__ == "__main__":
    unittest.main()
