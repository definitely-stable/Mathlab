"""Independent TRUE original HEAVY SRG and real top-r publication referee."""
import unittest
from fractions import Fraction as F
from math import comb

from hyp105_original_heavy_publication_srg_referee import (
    SCHEMA,STATUS,ISSUE,PARENT_PR,H_FIXED,R_FIXED,
    ceilq,true_envelopes,exact_GQ_SRG_params,
    prove_analytic_J_bound,genuine_model,
    _conditional_expected_cut,greedy_Caro_Wei_source_independent,
    genuine_heavy_case,formal_HEAVY_external_scenario,certificate,
)


class TestTrueOriginalHeavyPublication(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate=certificate()

    def test_01_ALL_H_exact_gq_srg_source_parameters(self):
        for s in (2,4,16,256):
            p=exact_GQ_SRG_params(s)
            self.assertEqual(p["V"],(s+1)*(s*s+1))
            self.assertEqual(p["degree"],s*(s+1))
            self.assertEqual(p["lam"],s-1)
            self.assertEqual(p["mu"],s+1)
            self.assertEqual(p["nontrivial_eig_max"],s-1)
            self.assertEqual(p["nontrivial_eig_min"],-(s+1))

    def test_02_analytical_proof_strict_Ms_ALL_s_ge256(self):
        z=prove_analytic_J_bound()
        self.assertEqual(z["threshold_min_s"],256)
        self.assertEqual(z["source_sqrt_2V_over_s3_LESS_than"],"10/7")
        self.assertLess(F(z["true_bound_2V_nonlinear_square"]),
                        F(z["sqrt_ceiling_square"]))
        self.assertGreater(F(z["positive_margin_lower_exact"]),0)
        self.assertTrue(z["source_eJ_strict_2M_Hs4_all_h_proved"])

    def test_03_H32_true_original_R33281_and_alphabet(self):
        z=true_envelopes(32)
        self.assertEqual(z["R"],33281)
        self.assertTrue(F(2)<z["A"]<F(9,4))
        self.assertTrue(F(1)<z["M"]<F(35,32))
        self.assertTrue(F(1)<z["nu"]<F(17,16))

    def test_04_source_spectrum_even_H>=8(self):
        for H in (8,10,16,24,32,40):
            z=true_envelopes(H)
            self.assertLess(z["R"],93312)
            self.assertGreater(z["A"],2)
            self.assertGreater(z["M"],1)

    def test_05_real_original_W32_W34_GQ_srg_degree_lambda_mu(self):
        cases=self.certificate["genuine_W32_W34_source_cases"]
        for z in cases:
            s=z["s"]
            self.assertEqual(z["true_original_SRG_parameters"],
                             exact_GQ_SRG_params(s))
            self.assertEqual(z["source_original_V"],(s+1)*(s*s+1))
            self.assertEqual(z["original_named_I"],(s+1)**2*(s*s+1))

    def test_06_true_point_line_original_SRG_Gram_pencil_conflict(self):
        for z in self.certificate["genuine_W32_W34_source_cases"]:
            self.assertEqual(z["TRUE_original_J_point_pencils"],
                             z["source_SRG_y_pencils"]["exact"])
            self.assertEqual(z["TRUE_original_J_line_pencils"],
                             z["source_SRG_x_pencils"]["exact"])
            self.assertEqual(z["original_source_J_edges"],
                             z["TRUE_original_J_point_pencils"]+
                             z["TRUE_original_J_line_pencils"])

    def test_07_actual_source_spectral_bound_on_both_dual_pencils(self):
        for z in self.certificate["genuine_W32_W34_source_cases"]:
            for key in ("source_SRG_y_pencils","source_SRG_x_pencils"):
                p=z[key]
                self.assertLessEqual(p["exact"],p["cap"])
                self.assertLessEqual(p["max_fiber"],
                                     z["physical_alphabet_a"]-1)

    def test_08_both_disjoint_TRUE_original_diagonals_and_ownership(self):
        for z in self.certificate["genuine_W32_W34_source_cases"]:
            self.assertEqual(z["all_physical_real_owned_diagonal_edges"],
                             2*z["original_named_I"])
            self.assertEqual(comb(z["physical_alphabet_a"]-1,2)<
                             z["source_original_V"]<=comb(z["physical_alphabet_a"],2),
                             True)

    def test_09_one_frozen_Q_multiple_T_diagnostic_original_cases(self):
        for z in self.certificate["genuine_W32_W34_source_cases"]:
            cases=z["real_frozen_HEAVY_top_r_cases"]
            self.assertEqual([x["T"] for x in cases],[0,1,2])
            self.assertGreater(cases[0]["original_E_T"],0)
            self.assertGreater(cases[0]["frozen_Q_count"],0)
            self.assertTrue(cases[0]["heavy"])

    def test_10_true_original_source_Caro_Wei_independent_set(self):
        for z in self.certificate["genuine_W32_W34_source_cases"]:
            for h in z["real_frozen_HEAVY_top_r_cases"]:
                if h["true_heavy_owners"]==0:continue
                self.assertGreater(h["independent_owner_count"],0)
                self.assertLessEqual(h["independent_owner_count"],
                                     h["true_heavy_owners"])
                self.assertTrue(h["original_source_J_independent_actual_source"])

    def test_11_global_two_bit_cuts_keep_AT_LEAST_QUARTER_owners(self):
        for z in self.certificate["genuine_W32_W34_source_cases"]:
            for h in z["real_frozen_HEAVY_top_r_cases"]:
                if h["true_heavy_owners"]==0:continue
                self.assertGreaterEqual(4*h["true_selected_original_whole_IDs"],
                                        h["independent_owner_count"])
                self.assertTrue(h["TWO_global_symbol_cuts_whole_flags"])

    def test_12_real_witness_E_RY_at_least_half_selected_source(self):
        for z in self.certificate["genuine_W32_W34_source_cases"]:
            for h in z["real_frozen_HEAVY_top_r_cases"]:
                if h["true_heavy_owners"]==0:continue
                self.assertGreaterEqual(
                    2*h["actual_real_source_RQ_Y_cross_edges"],
                    h["true_selected_original_whole_IDs"])
                self.assertGreaterEqual(
                    2*h["source_heavy_majority_witness_count"],
                    h["true_selected_original_whole_IDs"])

    def test_13_real_topr_no_clones_v_le2r(self):
        for z in self.certificate["genuine_W32_W34_source_cases"]:
            for h in z["real_frozen_HEAVY_top_r_cases"]:
                if h["true_heavy_owners"]==0:continue
                self.assertGreater(h["actual_genuine_simple_F_edges"],0)
                self.assertLessEqual(
                    h["actual_genuine_simple_F_vertices"],
                    2*h["actual_frozen_Q_R_count"])
                self.assertLessEqual(
                    h["actual_top_r_physical_Y_count"],
                    h["actual_frozen_Q_R_count"])
                self.assertTrue(h["top_r_no_vertex_or_edge_clones"])

    def test_14_real_topr_density_not_loose_partition(self):
        for z in self.certificate["genuine_W32_W34_source_cases"]:
            for h in z["real_frozen_HEAVY_top_r_cases"]:
                if h["true_heavy_owners"]==0:continue
                self.assertGreaterEqual(
                    F(h["genuine_original_F_density"]),
                    F(h["guaranteed_selected_source_density"]))
                self.assertTrue(
                    h["original_full_frozen_Q_global_cut_real_vertices"])

    def test_15_actual_heavy_degree_monotonic_wrt_T(self):
        for z in self.certificate["genuine_W32_W34_source_cases"]:
            cases=z["real_frozen_HEAVY_top_r_cases"]
            self.assertGreaterEqual(cases[0]["original_E_T"],
                                    cases[1]["original_E_T"])
            self.assertGreaterEqual(cases[1]["original_E_T"],
                                    cases[2]["original_E_T"])
            self.assertGreaterEqual(cases[0]["frozen_Q_count"],
                                    cases[1]["frozen_Q_count"])
            self.assertGreaterEqual(cases[1]["frozen_Q_count"],
                                    cases[2]["frozen_Q_count"])

    def test_16_true_source_both_coordinate_families_not_lex_only(self):
        cs=self.certificate["genuine_W32_W34_source_cases"]
        self.assertEqual(len(cs),6)
        self.assertEqual({(z["s"],z["scheme"]) for z in cs},
                         {(s,m) for s in (2,4)
                          for m in ("lex","reverse","shift")})
        self.assertTrue(any(z["TRUE_original_J_point_pencils"]>0 for z in cs))
        self.assertTrue(any(z["TRUE_original_J_line_pencils"]>0 for z in cs))

    def test_17_true_fixed_H_s_R_and_external_graph_FORMAL_only(self):
        for C0,c0 in ((F(1),F(1)),(F(2),F(1,5)),(F(7,3),F(1,17))):
            z=formal_HEAVY_external_scenario(C0,c0)
            self.assertEqual(z["fixed_HEAVY_R"],33281)
            T=int(z["common_source_T_exact"])
            self.assertGreaterEqual(T,F(17*33281**3,2)*C0**3)
            self.assertEqual(F(z["original_HEAVY_D6_delta"]),
                             c0/F(33281**6))
            self.assertTrue(z["exact_ordinary_graph_threshold_applies"])
            self.assertFalse(z["actual_numerical_graph_constants_known"])

    def test_18_external_numerical_constants_MUST_NOT_invent(self):
        for a,b in ((F(0),F(1)),(F(1),F(0)),(F(1),F(2)),(1,F(1)),(F(1),0.5)):
            with self.assertRaises(ValueError):
                formal_HEAVY_external_scenario(a,b)

    def test_19_invalid_GQ_orders_H_modes_fail_closed(self):
        for s in (0,1,3,8):
            with self.assertRaises(ValueError):
                genuine_model(s,"lex")
        with self.assertRaises(ValueError):
            genuine_model(2,"other")
        for H in (0,7,9,31):
            with self.assertRaises(ValueError):
                true_envelopes(H)
        with self.assertRaises(TypeError):
            ceilq(0.5)

    def test_20_negative_case_original_T_must_be_nonnegative(self):
        z=genuine_model(2,"reverse")
        with self.assertRaises(ValueError):
            genuine_heavy_case(z,-1)

    def test_21_original_FULL_low_HEAVY_shared_ancestry_root_NOT_PROVED(self):
        c=self.certificate
        self.assertEqual(c["schema"],SCHEMA)
        self.assertEqual(c["issue"],230)
        self.assertEqual(c["parent_pr"],782)
        self.assertEqual(c["status"],STATUS)
        self.assertTrue(c["original_HEAVY_no_clone_Caro_Wei_twocut_topr_refereed_all_h"])
        self.assertTrue(c["original_HEAVY_simple_graph_F_external_C6_hypotheses_proved_conditional"])
        self.assertTrue(c["true_original_D6_sixID_cycle_inverse_inherited_from_separate_referee"])
        self.assertTrue(c["LOW_PRODUCED_publication_acceptance_still_open"])
        self.assertFalse(c["original_ROOT_PROVED_A"])

    def test_22_original_source_HEAVY_formal_nonvacuous_cert(self):
        c=self.certificate
        self.assertTrue(c["published_ordinary_graph_C6_theorem_constants_numeric_unknown"])
        self.assertEqual(c["fixed_H"],32)
        self.assertEqual(c["R"],33281)
        self.assertEqual(len(c["formal_external_unknown_graph_scenarios"]),3)
        self.assertEqual(len(c["genuine_W32_W34_source_cases"]),6)
        self.assertGreater(
            sum(h["actual_genuine_simple_F_edges"] for z in
                c["genuine_W32_W34_source_cases"]
                for h in z["real_frozen_HEAVY_top_r_cases"]
                if h["true_heavy_owners"]>0),0)


if __name__=="__main__":
    unittest.main()
