"""JPKC-015 independently checked global injection ensemble expectation."""
import unittest
from fractions import Fraction
from math import comb, factorial
from itertools import combinations

from hyp105_issue230_projection import fixture
from hyp105_issue230_jpkc015_ensemble_d6_capacity import (
    falling, finite_original_geometry, original_six_matching_bounds,
    exact_D6_probability_minimal_alphabet,
    all_h_ensemble_certificate, exact_original_W32_six_matchings,
    independent_small_physical_sixcycle_count,
    finite_W32_exact_expectation,
)


class JPKC015Tests(unittest.TestCase):
    def test_independent_original_W32_left_right_six_matching_DPs(self):
        vals=[]
        for scheme in ("lex","reverse","S68","S72"):
            with self.subTest(scheme=scheme):
                model=fixture(1,scheme)
                forward=exact_original_W32_six_matchings(model)
                backward=exact_original_W32_six_matchings(
                    model,swap_bipartition=True)
                self.assertEqual(forward["true_original_W32_6_matching_count"],
                                 backward["true_original_W32_6_matching_count"])
                vals.append(forward["true_original_W32_6_matching_count"])
                self.assertGreater(vals[-1],0)
        self.assertEqual(len(set(vals)),1)
        self.assertEqual(vals[0],1566360)

    def test_physical_connected_D6_dual_formula_independent_graph_cycles(self):
        for a in (6,7,8,12,20):
            self.assertEqual(independent_small_physical_sixcycle_count(a),
                             comb(a,6)*(factorial(5)//2)*factorial(6))
            self.assertEqual(independent_small_physical_sixcycle_count(a),
                             60*falling(a,6))
        a=6
        self.assertEqual(independent_small_physical_sixcycle_count(a),43200)
        p=exact_D6_probability_minimal_alphabet(2)
        self.assertEqual(p,Fraction(60*43200**2,
                                  (60*falling(comb(a,2),6))**2))
        self.assertTrue(0<p<1)

    def test_all_h_positive_ensemble_D6_Omega_with_exact_16over3_limit(self):
        for s in (2,4,8,16,32,128):
            with self.subTest(s=s):
                g=finite_original_geometry(s)
                self.assertEqual(g["original_points"],(s+1)*(s*s+1))
                self.assertGreaterEqual(g["physical_pairs_available"],
                                        g["original_points"])
                self.assertLess(comb(g["minimal_physical_coordinate_symbols"]-1,2),
                                g["original_points"])
                low,high=original_six_matching_bounds(s)
                self.assertLessEqual(low,high)
                d=all_h_ensemble_certificate(s)
                self.assertFalse(d["all_h_minimum_over_labelings_proved"])
                self.assertTrue(d["asymptotic_limit_proof_by_degree_greedy_squeeze"])
                self.assertEqual(d["asymptotic_exact_ensemble_E_D6_over_s6_limit"],"16/3")
                self.assertGreaterEqual(Fraction(d["all_h_rigorous_ensemble_E_D6_lower"]),
                                        Fraction(d["all_h_simple_explicit_ensemble_E_D6_Omega_s6_lower"]))
                self.assertEqual(d["GF5_floor_denominator"],51**6)
                if s>=128:
                    target=Fraction(16,3)
                    self.assertLess(abs(Fraction(d["all_h_rigorous_ensemble_E_D6_lower"])
                                        /s**6-target),Fraction(1,3))
                    self.assertLess(abs(Fraction(d["all_h_rigorous_ensemble_E_D6_upper"])
                                        /s**6-target),Fraction(1,3))

    def test_exact_finite_W32_uniform_global_injection_mean_independent_of_scheme(self):
        cases=[finite_W32_exact_expectation(x) for x in
               ("lex","reverse","S68","S72")]
        self.assertEqual(len({c["true_original_W32_6_matching_count"]
                              for c in cases}),1)
        self.assertEqual(len({c["exact_uniform_GLOBAL_injection_ensemble_D6_expectation"]
                              for c in cases}),1)
        for c in cases:
            self.assertTrue(c["independent_swapped_source_matching_dp_equal"])
            self.assertTrue(c["independent_graph_cycle_vs_dual_cycle_count_equal"])
            self.assertEqual(c["physical_sixcycle_named_edge_assignment_count"],43200)
            self.assertTrue(c["mean_not_worst_case"])
        p=exact_D6_probability_minimal_alphabet(2)
        self.assertEqual(cases[0]["true_original_W32_6_matching_count"],1566360)
        self.assertEqual(Fraction(cases[0][
            "exact_uniform_GLOBAL_injection_ensemble_D6_expectation"]),
                         Fraction(3759264,1002001))
        self.assertEqual(Fraction(cases[0][
            "exact_uniform_GLOBAL_injection_ensemble_D6_expectation"]),
                         cases[0]["true_original_W32_6_matching_count"]*p)

    def test_fail_closed_illegal_unproven_physical_models_and_budgets(self):
        for s in (0,1,3,5,True,-2,2.0):
            with self.subTest(s=s),self.assertRaises(ValueError):
                all_h_ensemble_certificate(s)
        for a in (0,1,5,True):
            with self.assertRaises(ValueError):
                independent_small_physical_sixcycle_count(a)
        with self.assertRaises(ValueError):
            falling(5,6)
        with self.assertRaises(ValueError):
            finite_W32_exact_expectation("W34")
        with self.assertRaises(ValueError):
            exact_original_W32_six_matchings(fixture(2,"lex"))
        with self.assertRaisesRegex(ValueError,"budget"):
            exact_original_W32_six_matchings(fixture(1,"lex"),max_dp_states=1)


if __name__=="__main__":
    unittest.main()
