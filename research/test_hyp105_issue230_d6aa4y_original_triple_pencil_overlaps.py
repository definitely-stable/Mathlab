"""HYP-105 #230 / AA4-Y-SRC independent exact ORIGINAL triple pencils."""
import unittest
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4u_source_forest_frechet import (
    exact_W32_source_six_forest_universe,
)
from hyp105_issue230_d6aa4w_full_seven_quenched_kernel import (
    two_uniform_complete_global_maps_full_seven_expectation,
)
from hyp105_issue230_d6aa4x_exact_source_forest_capacities import (
    all_h_two_closed_source_forest_expectations,
)
from hyp105_issue230_d6aa4y_original_triple_pencil_overlaps import (
    KINDS, all_h_true_original_triple_pencil_capacity,
    full_global_uniform_AC_CA_selected_GF5,
    independent_real_original_line_triple_census,
    real_original_W32_bruteforce_all_three_pencils,
)


class RealOriginalTriplePencilGirthEightTests(unittest.TestCase):
    def test_001_all_h_exact_four_line_center_triple_classes(self):
        for h in range(1,18):
            s=1<<h
            z=all_h_true_original_triple_pencil_capacity(s)
            V,d=z["V"],z["d"]
            T=z["three_source_line_center_triple_type_counts"]
            self.assertEqual(set(T),set(KINDS))
            self.assertEqual(sum(T.values()),comb(V,3))
            self.assertEqual(T["concurrent"],V*comb(d,3))
            self.assertEqual(T["two_meetings"],V*comb(d,2)*(d-1)**2)
            self.assertEqual(
                T["one_meeting"],
                V*comb(d,2)*(V-2)-2*T["two_meetings"]-
                3*T["concurrent"])
            self.assertEqual(
                T["disjoint"],
                comb(V,3)-sum(T[k] for k in KINDS if k!="disjoint"))
            self.assertTrue(z["forbidden_three_pairwise_distinct_meeting_triangle"])
            self.assertTrue(z["girth8_no_original_6cycle_used"])
            self.assertTrue(z["no_global_physical_maps_used_for_source_count"])

    def test_002_four_exact_collision_IE_local_2neighbor_count(self):
        for h in range(1,17):
            s=1<<h
            z=all_h_true_original_triple_pencil_capacity(s)
            d=z["d"];q=comb(d,2);r=d-1
            W=z["pairwise_disjoint_two_original_points_per_source_line_choices"]
            self.assertEqual(W["disjoint"],q**3)
            self.assertEqual(W["one_meeting"],q**3-r*r*q)
            self.assertEqual(W["two_meetings"],q**3-2*r*r*q+r*r)
            self.assertEqual(W["concurrent"],q**3-3*r*r*q+2*r**3)
            self.assertTrue(all(0<x<=q**3 for x in W.values()))
            self.assertEqual(
                z["source_original_A/C_six_incidence_Q"],
                sum(W[k]*z["three_source_line_center_triple_type_counts"][k]
                    for k in KINDS))

    def test_003_full_genuine_W32_original_six_incidence_source_universe(self):
        U=exact_W32_source_six_forest_universe(fixture(1,"lex"))
        z=all_h_true_original_triple_pencil_capacity(2)
        self.assertEqual(z["source_original_A/C_six_incidence_Q"],6225)
        self.assertEqual(z["source_original_C/A_by_true_GQ_duality"],6225)
        self.assertEqual(z["source_original_A/C_six_incidence_Q"],
                         U["original_source_forest_universe"]["A/C"])
        self.assertEqual(z["source_original_C/A_by_true_GQ_duality"],
                         U["original_source_forest_universe"]["C/A"])
        self.assertEqual(
            z["three_source_line_center_triple_type_counts"],
            {"disjoint":80,"one_meeting":180,"two_meetings":180,"concurrent":15})
        self.assertEqual(
            z["pairwise_disjoint_two_original_points_per_source_line_choices"],
            {"disjoint":27,"one_meeting":15,"two_meetings":7,"concurrent":7})

    def test_004_independent_all_W32_true_original_sixflag_AC_direct_enumeration(self):
        actual=real_original_W32_bruteforce_all_three_pencils(fixture(1,"S68"))
        self.assertEqual(actual["actual_original_A/C_sixset_count"],6225)
        self.assertEqual(
            actual["exhaustive_original_three_line_center_classes"],
            {"disjoint":2160,"one_meeting":2700,
             "two_meetings":1260,"concurrent":105})

    def test_005_independent_real_W32_W34_ALL_center_line_triple_census(self):
        for h in (1,2):
            actual=independent_real_original_line_triple_census(
                fixture(h,"lex"),max_weighted_trials=100)
            expected=all_h_true_original_triple_pencil_capacity(1<<h)
            self.assertEqual(actual["number_actual_source_line_triples"],
                             comb(expected["V"],3))
            self.assertEqual(
                actual["actual_original_line_triple_cell_counts"],
                expected["three_source_line_center_triple_type_counts"])
            self.assertEqual(actual["direct_source_local_triples_checked"],100)
            self.assertTrue(actual["source_closed_all_h_formula_matches_true_GQ"])
            self.assertEqual(len(actual["actual_original_source_witness_per_class"]),4)
            self.assertEqual(
                sum(actual["independently_bruteforced_source_point_pair_choices"].values()),
                100)

    def test_006_exact_new_W34_source_triple_cell_counts(self):
        z=all_h_true_original_triple_pencil_capacity(4)
        self.assertEqual(z["source_original_A/C_six_incidence_Q"],87808400)
        self.assertEqual(z["source_original_C/A_by_true_GQ_duality"],87808400)
        self.assertEqual(
            z["three_source_line_center_triple_type_counts"],
            {"disjoint":43520,"one_meeting":40800,
             "two_meetings":13600,"concurrent":850})
        self.assertEqual(
            z["pairwise_disjoint_two_original_points_per_source_line_choices"],
            {"disjoint":1000,"one_meeting":840,
             "two_meetings":696,"concurrent":648})

    def test_007_both_global_uniform_new_GF5_CA_exact_vs_prior_full_seven_W32(self):
        U=exact_W32_source_six_forest_universe(fixture(1,"lex"))[
            "original_source_forest_universe"]
        all7=two_uniform_complete_global_maps_full_seven_expectation(2,U)
        z=full_global_uniform_AC_CA_selected_GF5(2)
        self.assertEqual(z["two_UNIFORM_complete_global_maps_expected_selected_C/A"],
                         Fraction(74700,13013))
        self.assertEqual(z["two_UNIFORM_complete_global_maps_expected_selected_C/A"],
                         all7["exact_tag_expectations"]["C/A"])
        prior=all_h_two_closed_source_forest_expectations(2)
        self.assertEqual(z["prior_X_two_tag_selected_expected"],
                         prior["expected_two_tag_total"])
        self.assertEqual(z["three_positive_original_selected_tags_expected"],
                         Fraction(14976180,1002001))
        self.assertLess(z["three_positive_original_selected_tags_expected"],
                        all7["exact_expected_seven_S"])
        self.assertTrue(z["true_original_third_tag_new_mean_PROVED"])
        self.assertFalse(z["does_NOT_imply_adversarial_infimum"] is False)

    def test_008_new_W34_exact_GF5_selected_CA_complete_global_ensemble(self):
        z=full_global_uniform_AC_CA_selected_GF5(4)
        self.assertEqual(z["two_UNIFORM_complete_global_maps_expected_selected_C/A"],
                         Fraction(202837404000,9877487))
        self.assertEqual(z["source_original_U_A/C"],87808400)
        self.assertEqual(z["leading_source_U_AC_over_s15"],Fraction(1,48))
        self.assertEqual(z["leading_AC_CA_expected_GF5_tag_over_s6"],Fraction(70,3))
        self.assertEqual(z["leading_three_selected_tag_expected_over_s6"],
                         Fraction(160,3))
        self.assertTrue(z["does_NOT_imply_adversarial_infimum"])

    def test_009_exact_all_h_asymptotic_three_positive_GF5_class_limit_scoped(self):
        for h in range(2,18):
            s=1<<h
            z=full_global_uniform_AC_CA_selected_GF5(s)
            self.assertGreater(z["two_UNIFORM_complete_global_maps_expected_selected_C/A"],0)
            self.assertGreater(z["three_positive_original_selected_tags_expected"],0)
            self.assertFalse(z["does_NOT_imply_adversarial_infimum"] is False)
            self.assertEqual(z["leading_three_selected_tag_expected_over_s6"],Fraction(160,3))
        # No claim of finite-s lower matching the limiting leading constant.

    def test_010_nonGQ_6cycle_fake_and_injected_source_negative_controls(self):
        base=fixture(1,"lex")
        fake={**base,"incidences":tuple(
            (p,l) for l in range(15) for p in (l,(l+1)%15,(l+3)%15))}
        with self.assertRaises(ValueError):
            independent_real_original_line_triple_census(fake)
        with self.assertRaises(ValueError):
            real_original_W32_bruteforce_all_three_pencils(fake)
        bad={**base,"right_labels":tuple(
            [base["right_labels"][0]]*len(base["right_labels"]))}
        with self.assertRaises(ValueError):
            independent_real_original_line_triple_census(bad)
        for s in (0,1,3,6,-2,True,2.0):
            with self.assertRaises(ValueError):
                all_h_true_original_triple_pencil_capacity(s)
        with self.assertRaises(ValueError):
            real_original_W32_bruteforce_all_three_pencils(fixture(2,"lex"))


if __name__=="__main__":
    unittest.main()
