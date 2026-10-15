"""HYP-105 AA4-Z-SRC: exact all-h true-ORIGINAL matching polynomial tests."""
import unittest
from fractions import Fraction
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4u_source_forest_frechet import (
    exact_W32_source_six_forest_universe,
)
from hyp105_issue230_d6aa4w_full_seven_quenched_kernel import (
    two_uniform_complete_global_maps_full_seven_expectation,
)
from hyp105_issue230_d6aa4x_exact_source_forest_capacities import (
    checked_gq_parameters,
)
from hyp105_issue230_d6aa4z_original_matching_moments import (
    regular_tree_matching_root_even_moment,
    matching_polynomial_from_root_power_sums,
    all_h_original_matching_source_AA,
    formal_cavity_monomer_star_ratio,
    all_h_original_one_P2_plus_four_matching_AB,
    all_h_two_new_selected_GF5_ensemble_sectors,
    independent_actual_true_GQ_six_matching_and_P2_4matching,
    strict_actual_source_GQ_adjacency,
    independent_actual_source_SAW_matching_polynomial,
)


class SixOriginalMatchingAndP2CavityTests(unittest.TestCase):
    def test_001_all_h_original_GQ_six_matching_exact_integer(self):
        for h in range(1,21):
            s=1<<h
            obj=all_h_original_matching_source_AA(s)
            V,d,N=checked_gq_parameters(s)
            self.assertEqual(obj["N_actual_original_flag_IDs"],N)
            self.assertEqual(obj["original_source_matching_numbers_m0_to_m6"][1],N)
            self.assertEqual(obj["original_source_matching_numbers_m0_to_m6"][6],
                             obj["source_original_A/A_six_distinct_point_line_flags"])
            self.assertEqual(obj["regular_original_source_root_closed_walk_moments_2k"],
                             [regular_tree_matching_root_even_moment(d,k)
                              for k in range(1,7)])
            self.assertTrue(obj["Godsil_1981_preexisting_path_tree_method_not_claimed_new"])
            self.assertTrue(obj["all_h_physical_global_maps_NOT_used"])

    def test_002_all_h_root_P2_monomer_cavity_matching_four(self):
        for h in range(1,21):
            s=1<<h
            o=all_h_original_one_P2_plus_four_matching_AB(s)
            self.assertEqual(o["original_LINE_centered_P2_source_roots"],
                             o["V"]*comb(o["d"],2))
            self.assertEqual(o["source_original_A/B_one_P2_plus_4_disjoint_flags"],
                             o["source_original_B/A_by_true_GQ_duality"])
            self.assertEqual(o["source_original_A/B_one_P2_plus_4_disjoint_flags"],
                             o["original_LINE_centered_P2_source_roots"]*
                             o["original_true_P2_deleted_residual_4matching_count"])
            cav=formal_cavity_monomer_star_ratio(o["d"],4)
            x=cav["cavity_x_coefficients"]
            self.assertEqual(x[0],1)
            self.assertEqual(x[1],-(o["d"]-1))
            self.assertEqual(cav["original_P2_three_vertex_joint_monomer_ratio"],
                             o["original_P2_formal_cavity_monomer_ratio"])
            self.assertTrue(o["all_h_girth_eight_rooted_P2_cavity_PROVED"])
            self.assertTrue(o["adversarial_joint_physical_acceptance_NOT_PROVED"])

    def test_003_exact_FULL_true_original_W32_forest_catalog_reconciliation(self):
        full=exact_W32_source_six_forest_universe(fixture(1,"lex"))
        ref=full["original_source_forest_universe"]
        aa=all_h_original_matching_source_AA(2)
        ab=all_h_original_one_P2_plus_four_matching_AB(2)
        self.assertEqual(full["total_original_45_choose_6"],comb(45,6))
        self.assertEqual(aa["source_original_A/A_six_distinct_point_line_flags"],
                         1566360)
        self.assertEqual(ab["source_original_A/B_one_P2_plus_4_disjoint_flags"],
                         1666980)
        self.assertEqual(aa["source_original_A/A_six_distinct_point_line_flags"],
                         ref["A/A"])
        self.assertEqual(ab["source_original_A/B_one_P2_plus_4_disjoint_flags"],
                         ref["A/B"])
        self.assertEqual(ab["source_original_B/A_by_true_GQ_duality"],ref["B/A"])
        self.assertEqual(aa["original_source_matching_numbers_m0_to_m6"],
                         [1,45,900,10560,80820,424404,1566360])
        self.assertEqual(ab["original_true_P2_deleted_residual_4matching_count"],
                         37044)
        self.assertEqual(ab["original_P2_formal_cavity_monomer_ratio"],
                         [1,-7,47,-319,2199])

    def test_004_true_original_W32_finite_actual_graph_SAW_matching_independent(self):
        z=independent_actual_true_GQ_six_matching_and_P2_4matching(
            fixture(1,"S68"),max_P2_samples=9)
        self.assertEqual(z["exact_original_source_U_AA"],1566360)
        self.assertEqual(z["exact_original_source_U_AB"],1666980)
        self.assertEqual(
            z["all_original_full_source_matchings"]["actual_matchings_m0_to_mk"],
            [1,45,900,10560,80820,424404,1566360])
        self.assertEqual(len(z["independently_checked_actual_P2_roots"]),9)
        self.assertTrue(all(q["actual_source_residual_m4"]==37044
                            for q in z["independently_checked_actual_P2_roots"]))
        self.assertTrue(z["true_original_GQ_projection_unique_anchor_VALIDATED"])

    def test_005_true_original_W34_full_graph_SAW_m6_and_actual_P2_deleted_m4(self):
        z=independent_actual_true_GQ_six_matching_and_P2_4matching(
            fixture(2,"lex"),max_P2_samples=3)
        self.assertEqual(z["exact_original_source_U_AA"],5903320937600)
        self.assertEqual(z["exact_original_source_U_AB"],894185475200)
        self.assertEqual(z["all_original_full_source_matchings"]["actual_matchings_m0_to_mk"],
                         [1,425,88400,11995200,1194216000,
                          93020741440,5903320937600])
        self.assertEqual(len(z["independently_checked_actual_P2_roots"]),3)
        self.assertTrue(all(q["actual_source_residual_m4"]==1051982912
                            for q in z["independently_checked_actual_P2_roots"]))

    def test_006_no_regular_tree_assumption_in_independent_residual_SAW_oracle(self):
        G,adj=strict_actual_source_GQ_adjacency(fixture(1,"lex"))
        V=G.v
        # Remove one genuine original point-line-point source P2:
        p1,p2=sorted(u for u in adj[V] if u<V)[:2]
        cut={V,p1,p2}
        residual=tuple(frozenset(v for v in row if v not in cut)
                       if i not in cut else frozenset()
                       for i,row in enumerate(adj))
        z=independent_actual_source_SAW_matching_polynomial(residual,4)
        self.assertEqual(z["actual_matchings_m0_to_mk"][4],37044)
        self.assertNotEqual(z["actual_matchings_m0_to_mk"],
                            all_h_original_matching_source_AA(2)[
                                "original_source_matching_numbers_m0_to_m6"][:5])
        self.assertTrue(z["actual_original_graph_agnostic_Godsil_SAW_independent"])

    def test_007_exact_two_new_original_GF5_expected_tags_vs_prior_full_W32(self):
        whole=two_uniform_complete_global_maps_full_seven_expectation(
            2,exact_W32_source_six_forest_universe(fixture(1,"lex"))[
                "original_source_forest_universe"])
        z=all_h_two_new_selected_GF5_ensemble_sectors(2)
        self.assertEqual(z["exact_both_complete_global_uniform_selected_D6"],
                         Fraction(3759264,1002001))
        self.assertEqual(z["exact_both_complete_global_uniform_selected_AB_plus_BA"],
                         Fraction(2857680,20449))
        self.assertEqual(z["exact_both_complete_global_uniform_selected_D6"],
                         whole["exact_tag_expectations"]["D6"])
        self.assertEqual(
            z["exact_both_complete_global_uniform_selected_AB_plus_BA"],
            whole["exact_tag_expectations"]["B-left/A-right"]+
            whole["exact_tag_expectations"]["A-left/B-right"])
        self.assertEqual(z["five_distinct_selected_GF5_tag_expectation"],
                         Fraction(158761764,1002001))
        self.assertLess(z["five_distinct_selected_GF5_tag_expectation"],
                        whole["exact_expected_seven_S"])

    def test_008_exact_true_W34_source_AND_GF5_expected_AB_AA_fractions(self):
        z=all_h_two_new_selected_GF5_ensemble_sectors(4)
        self.assertEqual(z["exact_TRUE_SOURCE_U_AA"],5903320937600)
        self.assertEqual(z["exact_TRUE_SOURCE_U_AB_and_BA"],894185475200)
        self.assertEqual(z["exact_both_complete_global_uniform_selected_D6"],
                         Fraction(88549814064000,12317226289))
        self.assertEqual(z["exact_both_complete_global_uniform_selected_AB_plus_BA"],
                         Fraction(93889474896000,286447123))

    def test_009_five_selected_GF5_asymptotic_contributions_scope(self):
        for h in range(1,19):
            s=1<<h
            z=all_h_two_new_selected_GF5_ensemble_sectors(s)
            self.assertEqual(z["leading_AA_source_over_s24"],Fraction(1,720))
            self.assertEqual(z["leading_AB_BA_source_each_over_s21"],Fraction(1,48))
            self.assertEqual(z["leading_selected_D6_over_s6"],Fraction(16,3))
            self.assertEqual(z["leading_selected_AB_plus_BA_over_s6"],280)
            self.assertEqual(z["leading_three_previous_tags_over_s6"],Fraction(160,3))
            self.assertEqual(z["leading_five_selected_tags_over_s6"],Fraction(1016,3))
            self.assertTrue(z["ensemble_not_adversarial_minimum"])
            self.assertTrue(z["source_original_BB_disjoint_still_UNCLOSED"])
            self.assertGreater(z["five_distinct_selected_GF5_tag_expectation"],0)
            if s>=2048:
                self.assertLess(abs(z["exact_both_complete_global_uniform_selected_D6"]
                                    /s**6-Fraction(16,3)),Fraction(1,2))
                self.assertLess(abs(z["exact_both_complete_global_uniform_selected_AB_plus_BA"]
                                    /s**6-280),Fraction(20))

    def test_010_fake_original_GQ_source_C6_and_global_noninjection_rejected(self):
        base=fixture(1,"lex")
        fake={**base,"incidences":tuple(
            (p,l) for l in range(15)
            for p in (l,(l+1)%15,(l+3)%15))}
        with self.assertRaises(ValueError):
            strict_actual_source_GQ_adjacency(fake)
        with self.assertRaises(ValueError):
            independent_actual_true_GQ_six_matching_and_P2_4matching(fake)
        bad={**base,"left_labels":tuple(
            [base["left_labels"][0]]*len(base["left_labels"]))}
        with self.assertRaises(ValueError):
            independent_actual_true_GQ_six_matching_and_P2_4matching(bad)
        for s in (0,1,-2,3,6,True,2.0):
            with self.assertRaises(ValueError):
                all_h_original_matching_source_AA(s)
        for d in (0,1,-1,2.0,True):
            with self.assertRaises(ValueError):
                formal_cavity_monomer_star_ratio(d)
        with self.assertRaises(ValueError):
            independent_actual_source_SAW_matching_polynomial((frozenset(),),7)


if __name__=="__main__":
    unittest.main()
