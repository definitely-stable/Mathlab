"""G6-F2 independent original-source six-ID / global selector audit tests.

Unlike old G6-C2/C3 tests, this evaluates ALL five-owner conflict
graphs, ALL 729 masks on a single genuine original six-ID BBo, ALL
ROOTED proper physical C6 on true W32, TWO separate independent
endpoint and blocker census implementations, and all four true NUMERIC
closure budgets with proven ordinary C6 constants.
"""
import unittest
from fractions import Fraction as Q

from gio_t3f1_explicit_c6 import exact_explicit_constants
from gio_t3f2_original_selector_audit import (
    SCHEMA,PARENT_G6F1,
    independent_priority_exhaustive,
    actual_global_source_priority_and_typed_cuts,
    independent_endpoint_precedence,
    independent_four_inner_blockers,
    exact_original_BBo_ternary_mask_cube,
    independent_original_six_cycle_inverse,
    graph_C6_heavy_density_gate,
    independent_numeric_four_LOW_regime,
    certificate,
)


class TestG6F2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.z=certificate()

    def test_01_exact_parent_scientific_scope(self):
        z=self.z
        self.assertEqual(z["schema"],SCHEMA)
        self.assertEqual(z["issue"],793)
        self.assertEqual(z["parent_G6F1_HEAD"],PARENT_G6F1)
        self.assertTrue(z["all_graph_C6_numeric_constants_proven_in_G6F1"])
        self.assertTrue(z["old_GENERIC_FORMAL_ONLY_label_intentionally_unmodified"])
        self.assertTrue(z["G6C2_G6C3_original_source_general_lemmas_remain_proof_dependencies"])
        self.assertTrue(z["no_unrestricted_abstract_T3_or_dependent_GF5_ASET"])
        self.assertTrue(z["no_external_human_peer_review_or_Lean_proof"])

    def test_02_exact_all_1024_global_priority_conflict_graphs(self):
        z=self.z[
            "exhaustive_one_global_original_priority_on_every_five_owner_J"]
        self.assertEqual(z["number_of_owner_labels"],5)
        self.assertEqual(z["original_owner_conflict_simple_graphs_exhausted"],
                         2**10)
        self.assertGreater(z["independent_nonempty_owner_subsets_exhausted"],5000)
        self.assertGreater(z["equality_cases"],0)
        self.assertGreater(z["strict_shared_competitor_cases"],0)
        self.assertGreaterEqual(Q(z["exact_minimum_probability_to_product_ratio"]),1)
        self.assertTrue(z["one_GLOBAL_owner_priority_order_used"])
        self.assertTrue(z["no_independent_owner_event_assumption"])

    def test_03_conflicting_target_owner_negative_falsifier(self):
        z=self.z[
            "exhaustive_one_global_original_priority_on_every_five_owner_J"]
        self.assertTrue(z["exact_adjacency_counterexample_breaks_bound_for_non_independent_S"])
        self.assertEqual(Q(z["zero_probability_for_two_adjacent_local_minima"]),0)
        self.assertEqual(Q(z["false_positive_independence_product"]),Q(1,4))
        self.assertLess(Q(z["zero_probability_for_two_adjacent_local_minima"]),
                        Q(z["false_positive_independence_product"]))

    def test_04_five_owner_shared_competitor_independent_old_oracle(self):
        old=self.z["previous_fiveowner_SHARED_competitor_control"]
        self.assertEqual(old["exact_all_priority_orders"],120)
        self.assertGreater(Q(old["exact_probability"]),
                           Q(old["independent_event_product_lower"]))
        self.assertTrue(old["shared_competitor_correlation_nontrivial"])
        self.assertTrue(old["all_priorities_are_ONE_global_order"])

    def test_05_TRUE_original_physical_W32_path_and_competing_flags(self):
        p=self.z[
            "ACTUAL_original_W32_threeowner_one_priority_two_global_cuts"]
        self.assertEqual(p["actual_geometry"],"original_W32")
        self.assertEqual(len(p["actual_original_path_vertices"]),4)
        self.assertEqual(len(p["actual_three_DISTINCT_named_original_owners"]),3)
        self.assertIn(p["actual_core_size"],(4,5))
        self.assertGreaterEqual(p["actual_max_shared_competitor_target_neighbors"],1)
        self.assertTrue(p["original_J_independent_target_owners"])
        self.assertTrue(p["physical_path_ACTUALLY_survives_one_common_selector"])

    def test_06_TRUE_global_typed_cuts_and_exact_priority_Jensen_input(self):
        p=self.z[
            "ACTUAL_original_W32_threeowner_one_priority_two_global_cuts"]
        self.assertEqual(p["one_global_symbol_cut_assignments"],256)
        self.assertEqual(p["original_threeedge_path_cut_favorable_assignments"],4)
        self.assertEqual(Q(p["exact_cut_probability"]),Q(1,64))
        self.assertGreaterEqual(Q(p["exact_joint_priority_probability"]),
                                Q(p["valid_non_independent_winner_probability_lower"]))
        self.assertEqual(Q(p["exact_joint_priority_AND_cuts_probability"]),
                         Q(p["exact_joint_priority_probability"])*Q(1,64))
        self.assertGreaterEqual(Q(p["exact_joint_priority_AND_cuts_probability"]),
                                Q(p["lower_joint_probability"]))
        self.assertTrue(p["global_source_owner_priority_and_typed_bits_NOT_resampled"])

    def test_07_ALL_729_original_six_ID_FULL_CORE_masks(self):
        b=self.z["original_FULL_CORE_3pow6_ternary_mask_source_inverse"]
        self.assertEqual(b["actual_source"],"original_W32")
        self.assertEqual(b["all_ternary_FULL_CORE_deletion_masks_exhaustively_checked"],729)
        self.assertTrue(b["physical_source_middle_owner_THREE_independent_algorithms_equal"])
        self.assertTrue(b["missing_original_projection_never_synthesized"])

    def test_08_original_six_distinct_FULl_CORE_required_not_faked(self):
        b=self.z["original_FULL_CORE_3pow6_ternary_mask_source_inverse"]
        six=set(b["six_DISTINCT_original_flag_IDs"])
        resid=set(b["actual_original_CORE_residual_flag_IDs"])
        anchor=set(b["actual_original_FULL_projection_anchor_flag_IDs"])
        self.assertEqual(len(six),6)
        self.assertEqual(len(resid),len(anchor),3)
        self.assertFalse(resid&anchor)
        self.assertEqual(six,resid|anchor)
        self.assertEqual(b["positive_original_six_ID_produced_masks"],8)
        self.assertEqual(b["negative_original_six_ID_masks"],721)
        self.assertEqual(b["predicted_positive_MASKS_exactly"],8)
        self.assertTrue(b["no_finite_case_claims_asymptotic_T3"])

    def test_09_independently_enumerated_ALL_genuine_original_D6(self):
        d=self.z["original_six_distinct_source_D6_from_TRUE_physical_C6"]
        self.assertEqual(d["actual_source"],"original_W32")
        self.assertGreater(d["true_original_named_six_ID_D6_count"],0)
        self.assertEqual(d["literal_rooted_DIRECTED_original_physical_C6_count"],
                         12*d["true_original_named_six_ID_D6_count"])
        self.assertTrue(d["each_original_D6_has_exactly_12_oriented_rooted_C6"])
        self.assertTrue(d["independent_physical_first_and_original_source_first_D6_equal"])
        self.assertTrue(d["all_original_D6_six_owners_GLOBAL_J_independent"])

    def test_10_exact_original_D6_one_global_cut_orientation_norm(self):
        d=self.z["original_six_distinct_source_D6_from_TRUE_physical_C6"]
        self.assertEqual(Q(d["one_global_typed_cut_D6_probability"]),Q(1,1024))
        self.assertTrue(d["no_fake_GQ_projection_or_nonproper_C6_count"])

    def test_11_independent_original_W32_endpoint_precedence(self):
        a=self.z["independent_original_endpoint_BAD_precedence_cases"][0]
        self.assertEqual(a["actual_source"],"W32")
        self.assertEqual(a["mask"],"mixed")
        self.assertGreater(a["exact_original_endpoint_universe"],0)
        self.assertTrue(a["independent_partition_equals_old_G6C2"])
        self.assertTrue(a["all_five_bad_original_endpoint_caps_checked"])
        self.assertTrue(a["true_missing_projections_never_completed"])

    def test_12_independent_nonGQ_Moore_holes_not_completed(self):
        a=self.z["independent_original_endpoint_BAD_precedence_cases"][1]
        self.assertEqual(a["actual_source"],"switchedDoubleW32")
        self.assertEqual(a["scheme"],"correlated")
        self.assertGreater(a["exactly_original_missing_projections"],0)
        self.assertGreater(a["exact_independent_original_endpoint_classes"][
            "unprojected"],0)
        self.assertTrue(a["independent_partition_equals_old_G6C2"])

    def test_13_original_BAD_endpoints_EXACT_good_plus_bad(self):
        for a in self.z["independent_original_endpoint_BAD_precedence_cases"]:
            part=a["exact_independent_original_endpoint_classes"]
            self.assertEqual(sum(part.values()),
                             a["exact_original_endpoint_universe"])
            self.assertGreaterEqual(part["good"],0)
            self.assertTrue(a["independent_partition_equals_old_G6C2"])

    def test_14_independent_original_inner_blocker_counts_W32(self):
        b=self.z["independently_counted_four_original_inner_blocker_cases"][0]
        self.assertEqual((b["actual_source"],b["scheme"],b["mask"]),
                         ("W32","lex","mixed"))
        self.assertTrue(b["old_and_independent_blocker_classifiers_agree"])
        self.assertTrue(b["exact_source_book_triple_injection_on_ALL_FOUR_positions"])
        self.assertTrue(b["FULL_anchor_original_only_not_CORE"])

    def test_15_independent_original_inner_blocker_counts_NON_GQ(self):
        b=self.z["independently_counted_four_original_inner_blocker_cases"][1]
        self.assertEqual(b["actual_source"],"switchedDoubleW32")
        self.assertEqual(b["scheme"],"correlated")
        self.assertTrue(b["old_and_independent_blocker_classifiers_agree"])
        self.assertEqual(set(b["independently_counted_four_inner_blockers"]),
                         {"x1","x2","y1","y2"})
        self.assertGreaterEqual(b["eligible_original_proper_physical_3walks"],0)

    def test_16_all_five_G6_C3_and_D7_USE_REAL_F1_constants(self):
        cases=self.z["all_five_real_G6C3_G6D7_numeric_closure_regimes"]
        self.assertEqual(len(cases),5)
        names=[x["regime"] for x in cases]
        self.assertEqual(names,[
            "linear_GQ_base","G6E1_GQ_PDS_zero_PSD",
            "G6E2_first_odd_q7","G6E2_E3_q_ge8",
            "G6E2_E3_q_ge18"])
        for a in cases:
            self.assertEqual(a["actual_proven_graph_C0"],2**41)
            self.assertEqual(Q(a["actual_proven_graph_c0"]),Q(1,98304))
            self.assertTrue(a["output_PROVEN_graph_numeric_premise_not_external_placeholder"])
            self.assertTrue(a["actual_legacy_ledger_FORMAL_ONLY_metadata_preserved"])
            self.assertTrue(a["actual_original_source_C2_C3_all_order_lemmas_still_inherited"])

    def test_17_all_four_LOW_errors_true_numeric_r0_not_synthetic_source(self):
        cases=self.z["all_five_real_G6C3_G6D7_numeric_closure_regimes"]
        for a in cases:
            err=a["four_LOW_errors"]
            self.assertEqual(len(err),4)
            self.assertTrue(all(err.values()))
            self.assertGreater(Q(a["exact_rho"]),0)
            self.assertGreater(Q(a["exact_delta"]),0)
            self.assertGreater(int(a["cutoff_r0_decimal_digits"]),1)
            self.assertTrue(a["source_r0_threshold_is_not_claimed_small_finite_fixture"])

    def test_18_one_GLOBAL_owner_selector_K_q2_q3_shapes(self):
        for a in self.z["all_five_real_G6C3_G6D7_numeric_closure_regimes"]:
            K=a["original_source_selector_K"]
            self.assertEqual(a["original_global_selector_q2"],16*(K+1)**2)
            self.assertEqual(a["original_global_selector_q3"],64*(K+1)**3)
            self.assertGreater(a["fixed_HEAVY_R"],K)
            self.assertGreaterEqual(a["fixed_HEAVY_graph_density_T_digits"],1)

    def test_19_fixed_source_premises_genuine_E1_E2_E3_cutoffs(self):
        a=self.z["all_five_real_G6C3_G6D7_numeric_closure_regimes"]
        self.assertEqual((a[1]["original_fixed_excess_C"],a[1]["original_cutoff_ell"],
                          a[1]["original_ZERO_PSD_M"]),(2,2,0))
        self.assertEqual((a[2]["original_fixed_excess_C"],a[2]["original_cutoff_ell"],
                          a[2]["original_ZERO_PSD_M"]),(5,4,0))
        self.assertEqual((a[3]["original_fixed_excess_C"],a[3]["original_cutoff_ell"],
                          a[3]["original_ZERO_PSD_M"]),(5,3,0))
        self.assertEqual((a[4]["original_fixed_excess_C"],a[4]["original_cutoff_ell"],
                          a[4]["original_ZERO_PSD_M"]),(5,2,0))

    def test_20_HEAVY_graph_C6_density_is_NOT_assumed_almost_regular(self):
        for a in self.z["all_five_real_G6C3_G6D7_numeric_closure_regimes"]:
            self.assertTrue(a["HEAVY_graph_C6_density_implication_int_check"])
        g=exact_explicit_constants()
        self.assertTrue(g["host_simple_graph_NO_other_hypotheses"])
        self.assertEqual(g["threshold_C0"],2**41)

    def test_21_HEAVY_GRAPH_density_exact_negative_controls(self):
        self.assertFalse(graph_C6_heavy_density_gate(
            10,1,10,2,2)["resulting_PROVEN_graph_C6_density_gate"])
        g=graph_C6_heavy_density_gate(10,1,10,2,2)
        self.assertFalse(g["frozen_HEAVY_average_degree_gate_exact"])
        with self.assertRaises(ValueError):
            graph_C6_heavy_density_gate(5,100,10,2,2)
        with self.assertRaises(ValueError):
            graph_C6_heavy_density_gate(True,0,1,1,1)

    def test_22_EXPLICIT_C6_external_numeric_equals_C3_D7_input(self):
        x=exact_explicit_constants()
        self.assertEqual(x["threshold_C0"],
                         self.z["all_five_real_G6C3_G6D7_numeric_closure_regimes"][0][
                             "actual_proven_graph_C0"])
        self.assertEqual(Q(x["cycle_coefficient_c0"]),
                         Q(self.z["all_five_real_G6C3_G6D7_numeric_closure_regimes"][0][
                             "actual_proven_graph_c0"]))

    def test_23_no_false_claim_ALL_source_abstract_T3(self):
        z=self.z
        self.assertTrue(z["G6C2_G6C3_original_source_general_lemmas_remain_proof_dependencies"])
        self.assertTrue(z["no_unrestricted_abstract_T3_or_dependent_GF5_ASET"])
        self.assertTrue(z["no_external_human_peer_review_or_Lean_proof"])
        for a in z["all_five_real_G6C3_G6D7_numeric_closure_regimes"]:
            self.assertTrue(a["actual_original_source_C2_C3_all_order_lemmas_still_inherited"])

    def test_24_SOURCE_PRIORITY_fully_exhausted_against_one_claim(self):
        # A totally independent direct n=3 exhaustive graph count:
        # every one of its 2^(3choose2)=8 possible J graphs is
        # included and passes all independent target owner sets.
        z=independent_priority_exhaustive(3)
        self.assertEqual(z["original_owner_conflict_simple_graphs_exhausted"],8)
        self.assertEqual(Q(z["exact_minimum_probability_to_product_ratio"]),1)
        self.assertTrue(z["one_GLOBAL_owner_priority_order_used"])


if __name__=="__main__":
    unittest.main()
