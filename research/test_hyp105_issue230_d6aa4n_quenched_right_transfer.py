"""Independent all-h quenched-right source GQ transfer and W32 finite tests."""
from fractions import Fraction
from itertools import combinations
from math import comb
import random
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4n_quenched_right_transfer import (
    all_right_quinched_bound,original_W32_fixed_g_right_A_counter
)


class QuenchedRightSourceTransferTests(unittest.TestCase):
    def test_001_exact_all_h_real_GQ_fixed_right_conditional_theorem(self):
        for h in range(3,17):
            s=2**h
            z=all_right_quinched_bound(s)
            self.assertTrue(z["all_power_two_s_ge_8_every_fixed_complete_g_bound"])
            self.assertGreater(z["remaining_good_original_source_line_pairs_lower"],0)
            self.assertGreater(z["actual_physical_C6_extensions_per_good_pair_lower"],0)
            self.assertGreater(z["actual_four_original_fresh_point_assignments_lower"],0)
            self.assertGreaterEqual(
                Fraction(z["conditional_E_f_true_seven_GF5_BA_internal_line_charge_lower"]),
                Fraction(z["explicit_3s6_over_65536"]))
            self.assertTrue(z["not_universal_GF5_s6_lower"])
            if s>=256:
                self.assertTrue(z["all_s_ge_256_analytic_five_factor_certificate"])
            else:
                self.assertTrue(z["small_8_16_32_64_128_exact_certificate"])

    def test_002_analytic_sge256_bounds_verified_without_large_original_graph(self):
        for h in range(8,30):
            s=2**h
            q=all_right_quinched_bound(s)
            a,K,V,m=(q[t] for t in ("a","K","V","m"))
            self.assertLessEqual(a,s*s)
            self.assertEqual(K,comb(a,2))
            self.assertEqual(K-V,m)
            self.assertLessEqual(m,a-2)
            self.assertLessEqual(q["maximum_bad_physical_centers"],24)
            self.assertGreaterEqual(16*q["remaining_good_original_source_line_pairs_lower"],s**5)
            self.assertGreaterEqual(4*q["actual_physical_C6_extensions_per_good_pair_lower"],s**3)
            self.assertGreaterEqual(16*q["actual_four_original_fresh_point_assignments_lower"],s**4)
            self.assertGreaterEqual(
                Fraction(q["exact_uniform_global_f_B_probability"])*64*s**6,3)

    def test_003_small_finite_exact_h3_to_h7_source_and_missing_edge_cuts(self):
        actual={
            8:(35,10,14755,2515,25),
            16:(94,2,504748,504748,68),
            32:(261,105,16544525,14897165,195),
            64:(731,510,534146375,500741575,547),
            128:(2057,931,17148295225,16910654521,1541),
        }
        for s,expected in actual.items():
            r=all_right_quinched_bound(s)
            self.assertEqual(tuple(r[f] for f in (
                "a","m",
                "spectral_all_right_original_concurrent_physically_disjoint_pairs_D",
                "remaining_good_original_source_line_pairs_lower",
                "legal_extra_physical_connector_symbols_per_side_lower"
            )),expected)

    def test_004_real_W32_frozen_right_direct_original_pencil_oracle(self):
        for scheme in ("lex","reverse","S68","S72"):
            model=fixture(1,scheme)
            r=original_W32_fixed_g_right_A_counter(model)
            self.assertEqual(r["physical_A_2factor_sixline_sets"],70)
            self.assertEqual(r["actual_original_point_pencil_two_line_roots"],45)
            self.assertGreater(r[
                "right_A_internal_concurrent_disjoint_original_line_pair_Q_T_g"],0)
            self.assertGreaterEqual(r[
                "right_A_source_BA_sixsets_T_g_plus_noncharged"],
                r["right_A_internal_concurrent_disjoint_original_line_pair_Q_T_g"])
            self.assertTrue(r["strictly_same_complete_right_mapping_across_every_original_Q"])
            self.assertTrue(r["four_point_frozen_outside_fiber_NOT_a_uniform_f_sample"])
            self.assertEqual(
                Fraction(r["exact_E_uniform_COMPLETE_point_f_INTERNAL_line_charge_given_g"]),
                Fraction(3,1001)*r[
                  "right_A_internal_concurrent_disjoint_original_line_pair_Q_T_g"])

    def test_005_random_full_original_W32_right_global_permutations(self):
        rng=random.Random(230049)
        model=fixture(1,"lex")
        physical=list(combinations(range(6),2))
        for _ in range(12):
            rng.shuffle(physical)
            m={**model,"right_labels":tuple(physical)}
            r=original_W32_fixed_g_right_A_counter(m)
            self.assertGreater(r["right_A_internal_concurrent_disjoint_original_line_pair_Q_T_g"],0)
            self.assertEqual(r["physical_A_2factor_sixline_sets"],70)

    def test_006_wrong_global_right_map_and_source_order_fail_closed(self):
        for s in (0,1,3,6,-8,True,False):
            with self.assertRaises(ValueError):
                all_right_quinched_bound(s)
        model=fixture(1,"S68")
        with self.assertRaises(ValueError):
            original_W32_fixed_g_right_A_counter({**model,"s":4})
        with self.assertRaises(ValueError):
            original_W32_fixed_g_right_A_counter(
                {**model,"right_labels":tuple(model["right_labels"])[:-1]})
        with self.assertRaises(ValueError):
            original_W32_fixed_g_right_A_counter(
                {**model,"right_labels":tuple(model["right_labels"])[:-1]+
                 (model["right_labels"][0],)})


if __name__=="__main__":
    unittest.main()
