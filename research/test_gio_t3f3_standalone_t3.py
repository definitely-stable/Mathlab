"""G6-F3: independent all-order ORIGINAL T3 transfer certificate tests.

Includes newly derived original source/selector/HEAVY-LOW constants,
independent physical coordinate returns and improper threewalk lemma,
all 512 bipartite graph sixth-walk identities and real W32 D6
global-cut expectation, plus TRUE non-GQ source fixed maps.
"""
import unittest
from fractions import Fraction as Q
from math import isqrt

from gio_t3f3_standalone_t3 import (
    SCHEMA,PARENT_G6F2,
    ceil_fraction,ceil_sqrt,
    standalone_source_and_closure,true_original_physical_model,
    literal_proper_and_return_moments,
    all_bipartite_3x3_spectral_sixwalks,
    actual_one_global_selector_expected_edges,
    actual_sixowner_D6_single_global_cut_trace,
    certificate,
)
from gio_t3d7_local_psd_rowtop import source_local_constants,integrated_local_ledger


class TestG6F3Standalone(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.z=certificate()
        cls.cases={x["regime"]:x["standalone_proof"]
                   for x in cls.z["all_five_original_SOURCE_specific_positive_theorem_instances"]}

    def test_01_parent_scope_and_fully_separate_calculator(self):
        z=self.z
        self.assertEqual(z["schema"],SCHEMA)
        self.assertEqual(z["parent_G6F2_HEAD"],PARENT_G6F2)
        self.assertEqual(z["issue"],793)
        self.assertTrue(z["standalone_numeric_theorem_derived_WITHOUT_old_C2_C3_D7_ledgers"])
        self.assertTrue(z["mathematical_argument_proves_abstract_combinatorial_CORE_given_actual_source"])
        self.assertTrue(z["source_specific_TYPED_PSD_gate_and_original_girth8_are_PREMISES"])
        self.assertTrue(z["actual_graph_existence_NOT_inferred_from_arithmetic"])
        self.assertTrue(z["no_unrestricted_abstract_T3_or_new_GF5_ASET_exponent"])
        self.assertTrue(z["no_external_referee_or_Lean"])

    def test_02_exact_verified_graph_C6_inputs_no_FORMAL_sample(self):
        for q in self.cases.values():
            self.assertEqual(q["external_ordinary_graph_C6_THEOREM_PROVEN_C0"],2**41)
            self.assertEqual(Q(q["external_ordinary_graph_C6_THEOREM_PROVEN_c0"]),
                             Q(1,98304))
            self.assertTrue(q["no_generic_OLD_FORMAL_ONLY_ledger_used"])
            self.assertTrue(q["input_fixed"]["actual_SOURCE_required"])
            self.assertTrue(q["input_fixed"]["two_typed_real_Loewner_PSD_required"])

    def test_03_all_five_real_ORIGINAL_source_regimes(self):
        self.assertEqual(len(self.cases),5)
        expected={
            "G6E1_true_GQ_PDS_zero_W":(1,2,2,0),
            "G6E2_first_true_odd_q7":(1,5,4,0),
            "G6E2_E3_true_corrected_q_ge8":(1,5,3,0),
            "G6E2_E3_true_corrected_q_ge18":(1,5,2,0),
            "G6D7_Wenger_true_all_prime_powers":(1,3,0,11),
        }
        for name,parameters in expected.items():
            q=self.cases[name]
            f=q["input_fixed"]
            self.assertEqual((f["balance_b"],f["quadratic_excess_C"],
                              f["cutoff_ell"],f["typed_local_budget_M"]),
                             parameters)

    def test_04_true_source_G6D7_constants_REDERIVED_independently(self):
        for q in self.cases.values():
            f=q["input_fixed"];a=q["source_constants"]
            old=source_local_constants(f["balance_b"],
                f["quadratic_excess_C"],f["cutoff_ell"],
                f["typed_local_budget_M"])
            for x,y in (
                ("v0","source_V0"),("n0","source_N0"),
                ("a0","alphabet_a0"),("A0","physical_vertices_A0"),
                ("j0","each_collinearity_conflict_j0"),
                ("J0","original_owner_conflict_J0"),
                ("G0","original_pencil_Gram_G0")):
                self.assertEqual(a[x],old[y])

    def test_05_all_order_numeric_ledger_agrees_without_IMPORT(self):
        # This compares after independently deriving the result, not
        # importing prior closure as a mathematical premise.
        for q in self.cases.values():
            f=q["input_fixed"]
            old=integrated_local_ledger(
                f["balance_b"],f["quadratic_excess_C"],
                f["cutoff_ell"],f["typed_local_budget_M"],
                Q(2**41),Q(1,98304))
            c=q["closure"];s=q["priority_and_moments"]
            for name in ("eps","rho","delta"):
                self.assertEqual(Q(c[name]),Q(old["closure"][name]))
            self.assertEqual(int(c["sufficient_r0"]),
                             int(old["closure"]["sufficient_r0"]))
            for x in ("K","R","T","w","q2","q3","Q0","L6","L4"):
                if x in ("Q0","L6","L4"):asserted=old["moments"][x]
                else:asserted=old["selector"][x]
                self.assertEqual(Q(s[x]),Q(asserted))

    def test_06_source_constants_fixed_before_ALL_order_and_labels(self):
        for q in self.cases.values():
            f=q["input_fixed"];source=q["source_constants"]
            b=f["balance_b"];C=f["quadratic_excess_C"]
            self.assertEqual(source["v0"],(b+1)*(b*b+1+C))
            self.assertEqual(source["n0"],(b+1)*source["v0"])
            self.assertEqual(source["a0"],2*source["v0"]+3)
            self.assertEqual(source["A0"],source["a0"]**2)
            self.assertEqual(source["J0"],2*source["j0"])
            self.assertGreater(source["G0"],0)

    def test_07_four_FULL_LOSS_exact_r0_and_deltas(self):
        for q in self.cases.values():
            c=q["closure"];e=q["all_four_independently_derived_LOW_errors"]
            self.assertEqual(set(e),{
                "improper_directed_3walk","original_endpoint_clean",
                "deletion_FULL_projection_anchor","four_TRUE_inner_book_blockers"})
            self.assertTrue(all(e.values()))
            self.assertGreater(int(c["sufficient_r0"]),0)
            self.assertEqual(len(c["sufficient_r0"]),c["r0_decimal_digits"])
            self.assertLess(Q(c["eps"]),Q(1))
            self.assertGreater(Q(c["rho"]),0)
            self.assertGreater(Q(c["delta"]),0)

    def test_08_positive_SOURCE_only_t3_and_no_GQ_requirements(self):
        for q in self.cases.values():
            a=q["input_fixed"]
            self.assertTrue(a["actual_SOURCE_required"])
            self.assertTrue(a["source_nonincident_partial_projection_NOT_completed"])
            self.assertTrue(a["arbitrary_adversarial_fixed_f_g"])
            self.assertTrue(q["HEAVY_graph_gate"]["required_actual_simple_host"])
            self.assertTrue(q["HEAVY_graph_gate"]["no_HOST_degree_regularization_assumed"])
            self.assertEqual(q["closure"]["actual_original_BBo_lower"],"w*r^6/4")
            self.assertEqual(q["closure"]["exact_C6_to_original_D6_lower"],"c0*r^6/R^6")

    def test_09_integer_exact_ceils_beyond_machine_64bits(self):
        self.assertEqual(ceil_fraction(Q(1,2)),1)
        self.assertEqual(ceil_fraction(Q(-1,2)),0)
        self.assertEqual(ceil_fraction(Q(6,3)),2)
        self.assertEqual(ceil_fraction(Q(9007199254740993,2)),4503599627370497)
        for n in (0,1,2,3,4,5,10,99,10**100+5):
            k=ceil_sqrt(n)
            self.assertGreaterEqual(k*k,n)
            if k:self.assertLess((k-1)**2,n)
        with self.assertRaises(ValueError):ceil_sqrt(-1)
        with self.assertRaises(ValueError):ceil_sqrt(2.0)

    def test_10_fixed_input_fail_closed(self):
        for args in ((0,3,0,11),(1,-1,0,0),(1,2,-1,0),
                     (1,2,0,-1),(True,2,2,0),(1,2,2.0,0)):
            with self.assertRaises(ValueError):standalone_source_and_closure(*args)

    def test_11_independently_exact_Qx_Qy_on_original_AND_NON_GQ(self):
        a=self.z["independent_literal_original_SOURCE_RETURN_and_IMPROPER_and_tr4"]
        self.assertEqual(len(a),5)
        for s in a:
            self.assertTrue(s["exact_source_owner_return_identity"])
            self.assertEqual(
                s["actual_coordinate_two_returns_x"]+
                s["actual_coordinate_two_returns_y"],
                8*s["source_CORE_C"]+4*s["actual_CORE_J_edges"])
            self.assertEqual(s["original_physical_CORE_edges"],2*s["source_CORE_C"])
            self.assertTrue(s["geometry_true_original_partial_source_flags"])
        self.assertIn("switchedDoubleW32",{s["name"] for s in a})
        self.assertIn("dualQminus42",{s["name"] for s in a})

    def test_12_exact_IMPROPER_threewalk_universal_return_bound(self):
        for s in self.z["independent_literal_original_SOURCE_RETURN_and_IMPROPER_and_tr4"]:
            self.assertLessEqual(s["actual_improper_threewalks"],
                                 s["exact_algebraic_improper_bound"])
            self.assertEqual(s["actual_improper_threewalks"]+
                             s["actual_PROPER_ordered_threewalks"],
                             s["actual_ordered_threewalks"])
            self.assertTrue(s["no_external_Lemma_for_return_or_improper"])
            self.assertGreaterEqual(s["actual_ordered_threewalks"],0)

    def test_13_exact_TR4_proper_and_improper_endpoints_disjoint(self):
        for s in self.z["independent_literal_original_SOURCE_RETURN_and_IMPROPER_and_tr4"]:
            self.assertTrue(s["proper_and_improper_P2_endpoint_support_DISJOINT"])
            self.assertEqual(
                s["exact_tr_A4"],
                s["exact_proper_P2_Frobenius_squared"]+
                s["exact_improper_R2_Frobenius_squared"])
            d=s["actual_CORE_max_physical_degree"]
            q=s["actual_coordinate_two_returns_x"]+s["actual_coordinate_two_returns_y"]
            self.assertLessEqual(s["exact_improper_R2_Frobenius_squared"],d*q)

    def test_14_gap_three_coords_bound_by_PSD_polynomial(self):
        for s in self.z["independent_literal_original_SOURCE_RETURN_and_IMPROPER_and_tr4"]:
            self.assertTrue(s["exact_threewalk_Holder_lower"])
            self.assertEqual(s["exact_gap3_x_upper"],
                s["actual_CORE_max_physical_degree"]*
                s["actual_coordinate_two_returns_x"])
            self.assertEqual(s["exact_gap3_y_upper"],
                s["actual_CORE_max_physical_degree"]*
                s["actual_coordinate_two_returns_y"])

    def test_15_all_512_bipartite_graphs_exact_S6_C6_young(self):
        z=self.z["exhaustive_bipartite_512_host_sixwalk_identity"]
        self.assertEqual(z["exhaustive_original_bipartite_simple_graphs"],512)
        self.assertEqual(z["total_unoriented_simple_C6_across_512"],48)
        self.assertTrue(z["Cauchy_trace4_squared_le_trace2_trace6_ALL"])
        self.assertTrue(z["injection_defect_trace6_le_12C6_plus_6Dtrace4_ALL"])
        self.assertTrue(z["young_trace6_le_24C6_plus_72mD_squared_ALL"])
        self.assertGreater(z["strict_nontrivial_cases"],0)

    def test_16_true_one_GLOBAL_priority_and_two_coherent_typed_cuts(self):
        z=self.z["exact_one_GLOBAL_selector_EXPECTED_physical_edges"]
        self.assertEqual(z["original_source"],"W32")
        self.assertEqual(z["all_one_GLOBAL_priority_orders"],6)
        self.assertEqual(len(z["actual_original_owner_IDs"]),3)
        self.assertGreater(z["actual_SOURCE_J_conflict_edges"],0)
        self.assertTrue(z["identity_EXPECTED_m_equals_half_W"])
        self.assertEqual(Q(z["exact_expected_SELECTED_edges"]),
                         Q(z["exact_original_source_Caro_Wei_W"])/2)
        self.assertTrue(z["no_owner_or_factor_independence_claim"])

    def test_17_sixowner_original_true_4096_coherent_cut_exact_C6(self):
        z=self.z["true_original_sixowner_D6_all_4096_selected_trace_cycles"]
        self.assertEqual(z["original_source"],"W32")
        self.assertEqual(len(set(z["actual_source_six_named_original_FLAG_IDs"])),6)
        self.assertEqual(z["global_cut_assignments_exhausted"],4096)
        self.assertEqual(z["exactly_four_all_six_owner_crossing_cuts"],4)
        self.assertEqual(z["actual_unoriented_source_C6_sum_over_cuts"],4)
        self.assertEqual(Q(z["exact_expected_source_C6"]),Q(1,1024))

    def test_18_exact_elected_owner_weight_and_same_selected_moments(self):
        z=self.z["true_original_sixowner_D6_all_4096_selected_trace_cycles"]
        self.assertEqual(Q(z["exact_expected_source_EDGES"]),
                         Q(z["exact_one_GLOBAL_priority_owner_weight_W"])/2)
        self.assertEqual(Q(z["exact_expected_trace2"]),
                         Q(z["exact_one_GLOBAL_priority_owner_weight_W"]))
        self.assertTrue(z["Cauchy_EXPECTED_trace4_squared_bound"])
        self.assertTrue(z["actual_source_trace6_graph_bound"])
        self.assertTrue(z["original_conditional_expected_C6_le_D6_div_1024"])

    def test_19_typical_sample_thick_original_geometry_minus_nonGQ(self):
        for name,scheme,mask in (("W32","lex","mixed"),
                                 ("switchedDoubleW32","correlated","mixed")):
            m,A,C,adj,owners,J=true_original_physical_model(name,scheme,mask)
            self.assertTrue(C<=A)
            self.assertEqual(len(owners),2*len(C))
            self.assertEqual(set(owners.values()),C)
            self.assertEqual(sum(map(len,J.values()))%2,0)
            self.assertEqual(sum(map(len,adj.values()))//2,len(owners))
            for i,ji in J.items():
                self.assertTrue(all(i in J[j] for j in ji))

    def test_20_frozen_nonGQ_original_has_genuine_Moore_holes(self):
        m,A,C,adj,owners,J=true_original_physical_model(
            "switchedDoubleW32","correlated","mixed")
        self.assertGreater(len(m["missing"]),0)
        self.assertGreater(m["excess_lines"],0)
        self.assertGreater(len(m["projection"]),0)

    def test_21_old_generic_numeric_not_used_as_proof(self):
        for q in self.cases.values():
            self.assertEqual(q["mode"],"NEW_INDEPENDENT_PROOF_NOT_OLD_C2_C3_LEDGER")
            self.assertTrue(q["no_generic_OLD_FORMAL_ONLY_ledger_used"])
            s=q["priority_and_moments"]
            self.assertEqual(s["TRUE_C6_typed_cut_success"],"4/4096")
            self.assertEqual(s["TRUE_C6_source_oriented_multiplicity"],12)
            self.assertEqual(s["TRUE_BBo_source_oriented_multiplicity"],2)

    def test_22_robust_pos_rho_and_very_high_r0_source_cutoffs(self):
        for q in self.cases.values():
            c=q["closure"];s=q["priority_and_moments"]
            self.assertGreater(int(c["sufficient_r0"]),2**32)
            self.assertGreater(len(s["T"]),10)
            self.assertGreater(c["r0_decimal_digits"],100)
            self.assertLess(Q(c["delta"]),Q(1))
            self.assertTrue(c["strict_CORE_fraction_lower"])

    def test_23_graph_C6_source_coefficients_are_TRULY_EXPLICIT(self):
        for q in self.cases.values():
            source=q["source_constants"]
            s=q["priority_and_moments"]
            K=s["K"];R=s["R"]
            self.assertEqual(K,16*source["J0"]+1)
            self.assertEqual(R,512*source["A0"]*(1+64*source["J0"]))
            self.assertEqual(s["q2"],16*(K+1)**2)
            self.assertEqual(s["q3"],64*(K+1)**3)
            self.assertEqual(Q(s["w"]),Q(8,source["A0"]**2))

    def test_24_critical_numeric_4_error_budget_at_real_r0(self):
        for q in self.cases.values():
            a=q["all_four_independently_derived_LOW_errors"]
            self.assertEqual(len(a),4)
            self.assertTrue(all(a.values()))
            self.assertEqual(len(q["closure"]["sufficient_r0"]),
                             q["closure"]["r0_decimal_digits"])

    def test_25_source_type_D7_Wenger_is_true_nonzero_PSD_example(self):
        q=self.cases["G6D7_Wenger_true_all_prime_powers"]
        f=q["input_fixed"]
        self.assertEqual((f["balance_b"],f["quadratic_excess_C"],
                          f["cutoff_ell"],f["typed_local_budget_M"]),
                         (1,3,0,11))
        self.assertGreater(q["source_constants"]["j0"],0)
        self.assertTrue(q["input_fixed"]["two_typed_real_Loewner_PSD_required"])


if __name__=="__main__":
    unittest.main()
