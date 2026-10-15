"""D6-AA4-R independent original C6 and globally injected D6 tests."""
from collections import Counter
from itertools import combinations
from fractions import Fraction
from math import comb,perm
import unittest

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census,physical_column_dual,is_connected_column_cycle)
from hyp105_issue230_d6aa4r_quenched_original_d6 import (
    original_all_h_occupied_C6_lower,quenched_original_D6_theorem,
    _physical_six_cycle,genuine_original_W32_fixed_left_C6_source_count,
    original_W32_single_Q_all_720_right_D6_completions,
)


class GenuineOriginalQuenchedD6Tests(unittest.TestCase):
    def test_001_all_h_frozen_original_f_exact_rational_prob_and_positive_s6(self):
        for h in range(3,17):
            s=2**h
            row=quenched_original_D6_theorem(s)
            self.assertEqual(row["s"],s)
            self.assertEqual(row["V"],(s+1)*(s*s+1))
            self.assertEqual(row["K"],comb(row["a"],2))
            self.assertEqual(row["missing_edges_K_minus_V"],row["K"]-row["V"])
            self.assertLessEqual(row["missing_edges_K_minus_V"],row["a"]-2)
            self.assertGreater(row["occupied_C6_for_EVERY_complete_f_lower"],0)
            self.assertGreater(row["guaranteed_distinct_source_line_matchings_per_phys_C6"],0)
            self.assertEqual(row["guaranteed_distinct_source_line_matchings_per_phys_C6"],
                             perm(s+1,6))
            self.assertEqual(Fraction(
                row["uniform_COMPLETE_right_injection_true_D6_probability"]),
                Fraction(perm(row["a"],6),perm(row["K"],6)))
            self.assertGreaterEqual(Fraction(
                row["conditional_E_g_true_original_seven_GF5_D6_lower_for_EVERY_f"]),
                Fraction(s**6,8))
            self.assertEqual(row["explicit_all_h_s_ge_8_s6_over_8"],str(Fraction(s**6,8)))
            self.assertTrue(row["all_h_two_sided_s_ge_8_quenched_D6_theorem"])
            self.assertTrue(row["GQ_point_line_duality_also_every_fixed_g_E_f_D6"])
            self.assertFalse(row["all_h_original_S_minimax_omega_s6_PROVED"])

    def test_002_large_s_analytic_certificate_and_asymptotic_16_over_3(self):
        for h in range(8,23):
            s=2**h
            row=quenched_original_D6_theorem(s)
            self.assertTrue(row["s_ge_256_elementary_analytic_five_factor_certificate"])
            self.assertGreaterEqual(
                Fraction(row["conditional_expected_D6_lower_over_s6"]),Fraction(1,8))
            self.assertGreater(row["a"],60)
        last=quenched_original_D6_theorem(2**18)
        val=Fraction(last["conditional_expected_D6_lower_over_s6"])
        self.assertLess(abs(float(val)-16/3),0.05)

    def test_003_independent_K6_six_cycles_each_edge_in_24_physical_cycles(self):
        edges=tuple(combinations(range(6),2))
        cycles=tuple(six for six in combinations(edges,6)
                     if _physical_six_cycle(six))
        self.assertEqual(len(cycles),60)
        for edge in edges:
            self.assertEqual(sum(edge in six for six in cycles),24)
        row=original_all_h_occupied_C6_lower(2)
        self.assertEqual(row["all_Ka_unlabeled_undirected_C6"],60)
        self.assertEqual(row["physical_C6_containing_a_single_fixed_edge"],24)
        self.assertEqual(row["occupied_C6_for_EVERY_complete_f_lower"],60)
        self.assertEqual(row["missing_edges_K_minus_V"],0)

    def test_004_true_W32_source_C6_six_original_incidences_independent_old_enumerator(self):
        for name in ("lex","reverse","S68","S72"):
            model=fixture(1,name)
            new=genuine_original_W32_fixed_left_C6_source_count(model)
            self.assertEqual(new["physical_complete_K6_C6_source_cycles"],60)
            self.assertEqual(new["independent_unique_true_original_six_incidence_Q_count"],
                             new["genuine_source_AA_original_C6_left_with_six_distinct_lines"])
            old=0
            for Q,kind in selected_left_six(model):
                if kind!="A":
                    continue
                chosen=tuple(model["incidences"][j] for j in Q)
                if len(set(l for p,l in chosen))!=6:
                    continue
                dual=physical_column_dual(model["incidences"],model["left_labels"],
                                          tuple(p for p,l in chosen))
                if is_connected_column_cycle(dual):
                    old+=1
            self.assertEqual(old,new["genuine_source_AA_original_C6_left_with_six_distinct_lines"])
            self.assertEqual(Fraction(
                new["conditional_E_g_true_D6_given_this_fixed_global_f"]),
                Fraction(old,5005))
            self.assertGreater(old,0)
            self.assertTrue(new["one_f_across_ALL_Q"])

    def test_005_true_original_ALL_720_global_right_D6_completions_historical_classifier(self):
        for name in ("S68","S72"):
            r=original_W32_single_Q_all_720_right_D6_completions(fixture(1,name))
            self.assertEqual(r["right_global_completion_classified_historical_GF5_D6"],720)
            self.assertEqual(r["distinct_global_injection_aligned_assignments"],720)
            self.assertEqual(r["exact_uniform_complete_right_D6_probability"],"1/5005")
            self.assertEqual(len(r["actual_original_six_incidence_witness"]),6)
            self.assertTrue(r["one_complete_g_used_per_original_Q_test"])
            self.assertTrue(r["no_per_Q_independent_random_GF5_in_probability_theorem"])

    def test_006_fixed_right_can_have_zero_D6_without_disproving_positive_expectation(self):
        for scheme in ("S68","S72"):
            m=fixture(1,scheme)
            hist=seven_census(m,independent_checks=False)
            self.assertEqual(hist["seven_class_motif_counts"]["D6"],0)
            conditional=genuine_original_W32_fixed_left_C6_source_count(m)
            self.assertGreater(Fraction(
                conditional["conditional_E_g_true_D6_given_this_fixed_global_f"]),0)
            self.assertEqual(hist["S_seven"],{"S68":68,"S72":72}[scheme])

    def test_007_invalid_true_original_geometry_and_injection_fail_closed(self):
        for invalid in (-1,0,1,3,6,True,False):
            with self.assertRaises(ValueError):
                quenched_original_D6_theorem(invalid)
        m=fixture(1,"S68")
        with self.assertRaises(ValueError):
            genuine_original_W32_fixed_left_C6_source_count({**m,"s":4})
        with self.assertRaises(ValueError):
            genuine_original_W32_fixed_left_C6_source_count(
                {**m,"left_labels":tuple(m["left_labels"])[:-1]+
                 (m["left_labels"][0],)})
        with self.assertRaises(ValueError):
            genuine_original_W32_fixed_left_C6_source_count(
                {**m,"incidences":tuple(m["incidences"])[:-1]})
        self.assertFalse(_physical_six_cycle(((0,1),)*6))


if __name__=="__main__":
    unittest.main()
