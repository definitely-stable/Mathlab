"""AA4-M independent source-flag and uniform full physical injection expectation tests."""
from fractions import Fraction
from itertools import combinations
from math import comb, factorial, perm, prod
import unittest

from hyp105_issue230_d6aa4m_random_injection_charge import (
    exact_random_projection_probabilities,original_BA_source_lower,
    exact_random_global_charge_theorem,
    genuine_original_W32_exact_BA_source_count,
    original_W32_BA_internal_charge_fiber,
)


class RandomTrueGlobalInjectionChargeTests(unittest.TestCase):
    def test_001_pinned_true_original_W32_exact_half_projection_probabilities(self):
        z=exact_random_projection_probabilities(2)
        self.assertEqual((z["V"],z["a"],z["K"]),(15,6,15))
        self.assertEqual(z["A_ordered_injective_good_images"],70*factorial(6))
        self.assertEqual(z["B_ordered_injective_good_images"],15*3*factorial(4))
        self.assertEqual(z["pA_exact"],Fraction(70*factorial(6),perm(15,6)))
        self.assertEqual(z["pB_exact"],Fraction(15*3*factorial(4),perm(15,5)))
        self.assertTrue(z["independent_full_typed_global_injections_not_per_Q_assignments"])

    def test_002_independent_exhaustive_K6_2factor_and_doubled_edge_C4(self):
        edges=tuple(combinations(range(6),2))
        A=0
        for chosen in combinations(edges,6):
            counts=[sum(c in edge for edge in chosen) for c in range(6)]
            if counts==[2]*6:
                A+=1
        self.assertEqual(A,70)
        # Double physical edge together with 4 distinct single-occurred
        # images, all FIVE original source factor image edges are injective.
        B=0
        for twice in edges:
            for four in combinations(tuple(e for e in edges if e!=twice),4):
                degrees=[2*int(c in twice)+sum(c in e for e in four)
                         for c in range(6)]
                if degrees==[2]*6:
                    B+=1
        self.assertEqual(B,15*3)
        self.assertEqual(B*factorial(4),
                         exact_random_projection_probabilities(2)[
                             "B_ordered_injective_good_images"])

    def test_003_true_original_all_h_BA_source_GQ_incidence_lower(self):
        for h in range(1,13):
            s=1<<h
            z=original_BA_source_lower(s)
            V=(s+1)*(s*s+1)
            d=s+1
            self.assertEqual(z["V"],V)
            self.assertEqual(z["four_sequential_flag_choice_lower_bounds"],
                             tuple(d*(V-3-2*j) for j in range(4)))
            self.assertEqual(z["guaranteed_original_B_point_A_line_sixsets_lower"],
                             Fraction(V*comb(d,2)*prod(
                                 d*(V-3-2*j) for j in range(4)),24))
            self.assertGreater(z["guaranteed_original_B_point_A_line_sixsets_lower"],0)
            self.assertTrue(z["repeated_original_point_has_two_distinct_source_lines"])
            self.assertTrue(z["four_additional_true_original_flags_point_line_fresh"])

    def test_004_all_h_real_complete_typed_map_random_expectation_and_limits(self):
        for h in range(1,13):
            s=1<<h
            a=exact_random_global_charge_theorem(s)
            S=Fraction(a["expected_true_B_left_A_right_seven_GF5_count_lower"])
            I=Fraction(a["expected_internal_ORIGINAL_line_pair_GF5_charge_lower"])
            self.assertEqual(I,Fraction(3,5)*S)
            self.assertEqual(Fraction(a["rational_internal_charge_lower_over_s6"]),I/s**6)
            self.assertGreater(I,0)
            self.assertFalse(a["universal_all_maps_charge_lower_PROVED"])
            self.assertFalse(a["universal_S_s6_lower_PROVED"])
            self.assertTrue(a["complete_GLOBAL_uniform_typed_injections_symmetric"])
            self.assertTrue(a["stochastic_positivity_is_not_deterministic_minimax"])
        last=exact_random_global_charge_theorem(2048)
        self.assertLess(abs(float(Fraction(
            last["rational_internal_charge_lower_over_s6"]))-84),1)
        self.assertLess(abs(float(Fraction(
            last["rational_BA_expectation_lower_over_s6"]))-140),2)

    def test_005_independently_enumerated_genuine_W32_source_BA_Q(self):
        z=genuine_original_W32_exact_BA_source_count()
        self.assertEqual(z["s"],2)
        self.assertEqual(z["all_true_original_incidence_ID_count"],45)
        self.assertEqual(z["source_two_star_roots"],15*3)
        self.assertEqual(z["independently_enumerated_original_B_point_A_line_Q_exact"],1666980)
        self.assertEqual(z["minimum_completion_count_per_two_star_root"],37044)
        self.assertEqual(z["maximum_completion_count_per_two_star_root"],37044)
        self.assertGreater(z["independently_enumerated_original_B_point_A_line_Q_exact"],
                           Fraction(z["all_h_greedy_source_lower"]))
        px=exact_random_projection_probabilities(2)
        expected=1666980*px["pB_exact"]*px["pA_exact"]
        self.assertEqual(expected,Fraction(1428840,20449))
        self.assertEqual(Fraction(3,5)*expected,Fraction(857304,20449))
        self.assertTrue(z["no_physical_GF5_classification_in_original_source_count"])

    def test_006_true_original_W32_24_complete_state_BA_internal_charge(self):
        for scheme,baseline in (("S68",68),("S72",72)):
            z=original_W32_BA_internal_charge_fiber(scheme)
            self.assertEqual(z["scheme"],scheme)
            self.assertEqual(z["complete_genuinely_injected_K6_states"],24)
            self.assertEqual(z["all_original_sixset_candidates_per_state"],62370)
            self.assertEqual(z["exact_ranges"]["seven_original_S"]["min"],baseline)
            self.assertEqual(len(z["all_24_full_original_GF5_observations"]),24)
            self.assertTrue(z["all_h_random_injection_expectation_theorem_not_mean_of_this_fiber"])
            for row in z["all_24_full_original_GF5_observations"]:
                B=row["B_left_A_right_actual_positive_Q"]
                I=row["B_left_A_right_true_original_internal_line_charge"]
                self.assertLessEqual(I,B)
                self.assertLessEqual(I,row["independent_class_sensitive_original_L_charge"])
                self.assertEqual(B-I,row["B_left_A_right_true_original_internal_line_charges_uncovered"])
                self.assertTrue(row["actual_source_L_internal_charge_subset_verified"])
            self.assertEqual(z["root_A"],"OPEN")
            self.assertEqual(z["root_B"],"OPEN")

    def test_007_invalid_alphabet_and_s_fail_closed(self):
        for s in (0,1,3,6,-2,True,False):
            with self.assertRaises(ValueError):
                exact_random_projection_probabilities(s)
            with self.assertRaises(ValueError):
                original_BA_source_lower(s)
            with self.assertRaises(ValueError):
                exact_random_global_charge_theorem(s)
        with self.assertRaises(ValueError):
            original_W32_BA_internal_charge_fiber("lex")


if __name__=="__main__":
    unittest.main()
