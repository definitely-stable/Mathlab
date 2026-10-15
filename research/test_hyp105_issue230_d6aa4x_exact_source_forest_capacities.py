"""HYP105 #230 / AA4-X: independent all-h source B/C and B/B-overlap counts."""
import unittest
from math import comb,prod
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4u_source_forest_frechet import (
    exact_W32_source_six_forest_universe,
)
from hyp105_issue230_d6aa4w_full_seven_quenched_kernel import (
    two_uniform_complete_global_maps_full_seven_expectation,
)
from hyp105_issue230_d6aa4x_exact_source_forest_capacities import (
    checked_gq_parameters,
    all_h_BC_two_source_path_population,
    all_h_BB_overlap_path_matching_population,
    exact_residual_three_matching_formula,
    all_h_two_closed_source_forest_expectations,
    independent_actual_source_path_four_after_deletion,
    independent_actual_P3_deletion_three_matching,
)

U32={
    "A/A":1566360,"A/B":1666980,"B/A":1666980,
    "A/C":6225,"C/A":6225,"B/C":5220,"C/B":5220,
    "B/B-overlap":910080,"B/B-disjoint":707580,
}


class ExactOriginalSourceForestCapacitiesTests(unittest.TestCase):
    def test_001_all_h_integral_exact_BC_P4_plus_P2_source_paths(self):
        for h in range(1,19):
            s=1<<h
            z=all_h_BC_two_source_path_population(s)
            V,d,N=checked_gq_parameters(s)
            self.assertEqual((z["V"],z["d"],z["N_original_incidences"]),(V,d,N))
            self.assertEqual(z["root_original_point_ended_P4_count"],
                             V*d*(d-1)**3//2)
            self.assertEqual(
                z["disjoint_original_line_centered_P2_per_root_P4"],
                (3*d-4)*comb(d-1,2)+(V-3*d+2)*comb(d,2))
            self.assertEqual(z["source_original_B/C_count"],
                             z["root_original_point_ended_P4_count"]*
                             z["disjoint_original_line_centered_P2_per_root_P4"])
            self.assertEqual(z["source_original_B/C_count"],
                             z["source_original_C/B_by_true_GQ_duality"])
            self.assertTrue(z["girth_eight_all_h_original_source_theorem"])
            self.assertTrue(z["physical_global_maps_NOT_USED"])

    def test_002_all_h_P3_original_residual_linegraph_inclusion_exclusion(self):
        for h in range(1,19):
            s=1<<h;V,d,_=checked_gq_parameters(s)
            z=all_h_BB_overlap_path_matching_population(s)
            r=exact_residual_three_matching_formula(V,d)
            self.assertEqual(z["root_original_point_to_line_P3_count"],
                             V*d*(d-1)**2)
            self.assertEqual(r["residual_original_incidence_edges"],V*d-4*d+3)
            self.assertEqual(r["residual_low_degree_vertices"],4*d-6)
            self.assertEqual(r["residual_high_degree_vertices"],2*(V-2*d+1))
            self.assertEqual(r["residual_low_high_edges"],(4*d-6)*(d-1))
            self.assertEqual(r["residual_high_high_edges"],
                             V*d-4*d+3-(4*d-6)*(d-1))
            self.assertEqual(z["source_original_B/B-overlap_count"],
                             V*d*(d-1)**2*
                             r["actual_disjoint_original_three_edge_matchings"])
            self.assertTrue(z["all_h_closed_form_and_true_source_girth_PROVED"])

    def test_003_immutable_full_W32_universe_two_new_exact_closed_values(self):
        z=exact_W32_source_six_forest_universe(fixture(1,"lex"))
        self.assertEqual(z["total_original_45_choose_6"],comb(45,6))
        self.assertEqual(z["original_source_forest_universe"],U32)
        self.assertEqual(all_h_BC_two_source_path_population(2)
                         ["source_original_B/C_count"],5220)
        self.assertEqual(all_h_BB_overlap_path_matching_population(2)
                         ["source_original_B/B-overlap_count"],910080)
        self.assertEqual(all_h_BB_overlap_path_matching_population(2)
                         ["actual_disjoint_original_three_edge_matchings"],5056)

    def test_004_independent_true_original_GQ_W32_W34_P4_source_P2_census(self):
        for power in (1,2):
            model=fixture(power,"lex")
            z=independent_actual_source_path_four_after_deletion(model,limit=36)
            expected=all_h_BC_two_source_path_population(1<<power)
            self.assertEqual(z["sampled_oriented_actual_original_P4"],36)
            self.assertEqual(
                z["actual_P2_per_P4_histogram"],
                {expected["disjoint_original_line_centered_P2_per_root_P4"]:36})
            self.assertEqual(len(z["three_true_source_P4_witnesses"]),3)

    def test_005_true_original_GQ_W32_brute_force_source_three_matchings(self):
        model=fixture(1,"lex")
        z=independent_actual_P3_deletion_three_matching(
            model,max_root_samples=9,brute_force_when_small=True)
        self.assertEqual(z["all_h_exact_residual_m3"],5056)
        self.assertEqual(len(z["sampled_actual_original_P3"]),9)
        for row in z["sampled_actual_original_P3"]:
            self.assertEqual(row["residual_edges"],36)
            self.assertEqual(row["degree_low"],6)
            self.assertEqual(row["degree_high"],20)
            self.assertEqual(row["mixed_original_edges"],12)
            self.assertEqual(row["direct_enumerated_matchings"],5056)

    def test_006_true_original_GQ_W34_independent_P3_residual_graph_checks(self):
        model=fixture(2,"random")
        z=independent_actual_P3_deletion_three_matching(
            model,max_root_samples=21,brute_force_when_small=False)
        self.assertEqual(z["all_h_exact_residual_m3"],10594688)
        for row in z["sampled_actual_original_P3"]:
            self.assertEqual(row["residual_edges"],408)
            self.assertEqual(row["degree_low"],14)
            self.assertEqual(row["degree_high"],152)
            self.assertEqual(row["mixed_original_edges"],56)
            self.assertIsNone(row["direct_enumerated_matchings"])

    def test_007_new_exact_BC_BBo_expected_seven_GF5_against_previous_full_W(self):
        x=all_h_two_closed_source_forest_expectations(2)
        whole=two_uniform_complete_global_maps_full_seven_expectation(2,U32)
        self.assertEqual(x["expected_TRUE_original_selected_C/B_both_uniform_full_maps"],
                         whole["exact_tag_expectations"]["C/B"])
        self.assertEqual(x["expected_TRUE_original_selected_B/B-overlap_both_uniform_full_maps"],
                         whole["exact_tag_expectations"]["B/B-overlap"])
        self.assertEqual(x["expected_two_tag_total"],
                         whole["exact_tag_expectations"]["C/B"]+
                         whole["exact_tag_expectations"]["B/B-overlap"])
        self.assertLess(x["expected_two_tag_total"],
                        whole["exact_expected_seven_S"])
        self.assertFalse(x["conditional_vs_adversarial_all_f_g_lower_PROVED"])

    def test_008_all_h_asymptotic_independent_scalings_not_minimax(self):
        # True limits s->infinity in powers-of-two, exact rational
        # expressions, not finite-W32 polynomial extrapolation.
        prev=None
        for h in range(3,18):
            s=1<<h
            z=all_h_two_closed_source_forest_expectations(s)
            c=z["expected_TRUE_original_selected_C/B_both_uniform_full_maps"]
            b=z["expected_TRUE_original_selected_B/B-overlap_both_uniform_full_maps"]
            self.assertGreater(c,0)
            self.assertGreater(b,0)
            self.assertEqual(z["leading_asymptotic_EXPECTED_C_B_over_s6"],6)
            self.assertEqual(z["leading_asymptotic_EXPECTED_BB_overlap_over_s6"],24)
            self.assertEqual(z["leading_asymptotic_two_tag_EXPECTED_over_s6"],30)
            self.assertFalse(z["conditional_vs_adversarial_all_f_g_lower_PROVED"])
            if s>=1024:
                # Deliberately broad exact rational convergence checks,
                # the proof is in the all-h asymptotic derivation.
                self.assertLess(abs(c/Fraction(s**6)-6),Fraction(1,10))
                self.assertLess(abs(b/Fraction(s**6)-24),Fraction(1,10))
                self.assertLess(abs((c+b)/Fraction(s**6)-30),Fraction(1,5))

    def test_009_invalid_GQ_parameter_and_non_GQ_original_negative_controls(self):
        for s in (0,1,3,5,6,-2,True,2.0):
            with self.assertRaises(ValueError):
                checked_gq_parameters(s)
        base=fixture(1,"lex")
        fake={**base,"incidences":tuple((p,l) for l in range(15)
                                      for p in (l,(l+1)%15,(l+3)%15))}
        with self.assertRaises(ValueError):
            independent_actual_source_path_four_after_deletion(fake)
        with self.assertRaises(ValueError):
            independent_actual_P3_deletion_three_matching(fake)
        bad={**base,"left_labels":tuple([base["left_labels"][0]]*
                                          len(base["left_labels"]))}
        with self.assertRaises(ValueError):
            independent_actual_P3_deletion_three_matching(bad)


if __name__=="__main__":
    unittest.main()
