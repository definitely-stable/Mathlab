"""Original W(3,s) LOW one-global-selector mean-edge and moment audit."""
from fractions import Fraction as F
from itertools import combinations
import unittest

from hyp105_original_low_moment_expected_edges import (
    SCHEMA,STATUS,PARENT_PR,H_FIXED,K_FIXED,R_FIXED,ALPHA,
    ceilq,ceilsqrt,hd,envelopes,local_selected_edge_mass,
    proof_budget,formal_renewal,original_case,_actual_physical_graph,
    _trace_even_and_cycles,exhaustive_one_global_priorities_and_two_cuts,
    proper_paths,exhaustive_nonvacuous_original_D6_cut_moments,certificate,
)


class TestAA4LowMeanRank(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=certificate()

    def test_01_exact_source_Fraction_envelopes_and_fixed_ancestry(self):
        z=envelopes(32)
        self.assertEqual(z["R"],33281)
        self.assertGreater(z["nu"],1)
        self.assertLess(z["nu"],F(10001,10000))
        self.assertGreater(z["A"],2)
        self.assertLess(z["A"],F(20001,10000))
        self.assertLess(z["M"],F(10001,10000))

    def test_02_genuine_full_original_W32_and_W34_pair_owners(self):
        for s in (2,4):
            for scheme in ("lex","reverse","shift"):
                z=original_case(s,scheme)
                self.assertEqual(len(z["flags"]),(s+1)**2*(s*s+1))
                self.assertEqual(len(z["owners"]),2*len(z["flags"]))
                self.assertEqual(len(set(z["owners"].values())),len(z["flags"]))
                self.assertEqual(len(set(z["f"])),(s+1)*(s*s+1))
                self.assertEqual(len(set(z["g"])),(s+1)*(s*s+1))
                for i,diags in z["per"].items():
                    self.assertEqual(len(diags),2)
                    self.assertFalse(set(diags[0])&set(diags[1]))
                    self.assertEqual(z["owners"][diags[0]],i)
                    self.assertEqual(z["owners"][diags[1]],i)

    def test_03_REAL_original_J_is_undirected_and_full_pencil(self):
        for s in (2,4):
            z=original_case(s,"reverse")
            for i,neighbors in z["J"].items():
                self.assertNotIn(i,neighbors)
                self.assertTrue(all(i in z["J"][j] for j in neighbors))
                self.assertTrue(all(j!=i for j in neighbors))

    def test_04_selected_edge_mass_is_exact_harmonic_source_rank(self):
        z=original_case(2,"lex")
        A={0}|set(z["J"][0])
        sample=tuple(sorted(A))[:6]
        subset=original_case(2,"lex",sample)
        P=local_selected_edge_mass(subset["J"],sample)
        W=sum((F(1,1+len(subset["J"][i])) for i in sample),F(0))
        self.assertEqual(P["exact_source_priority_degree_weight"],W)
        self.assertEqual(P["exact_EXPECTED_true_selected_edges"],W/2)
        self.assertEqual(P["exact_EXPECTED_true_selected_trace2"],W)
        self.assertLessEqual(P["exact_EXPECTED_true_selected_edges"],F(len(sample),2))
        self.assertEqual(P["core_full_physical_edges"],2*len(sample))

    def test_05_empty_source_mass_and_invalid_J_inputs(self):
        self.assertEqual(local_selected_edge_mass({},())["exact_source_priority_degree_weight"],0)
        with self.assertRaises(ValueError):
            local_selected_edge_mass({0:set()},(0,0))
        with self.assertRaises(ValueError):
            local_selected_edge_mass({0:{1}},(0,))
        with self.assertRaises(ValueError):
            local_selected_edge_mass({0:{0}},(0,))

    def test_06_full_global_W32_priority_and_BOTH_cuts_exhausted(self):
        q=self.report["original_source_full_J_priority_and_cut_TRUE_W32"]
        self.assertEqual(q["s"],2)
        self.assertEqual(len(q["named_original_ids"]),3)
        self.assertEqual(q["full_joint_global_owner_priority_orderings"],6)
        self.assertGreater(q["full_joint_rank_and_global_bit_outcomes"],6)
        self.assertEqual(F(q["exact_EXPECTED_selected_tr2"]),
                         2*F(q["exact_EXPECTED_selected_m"]))
        self.assertGreater(F(q["exact_EXPECTED_selected_tr6"]),0)
        self.assertTrue(q["all_outcomes_one_global_priority_and_two_global_coloring"])
        self.assertTrue(q["expectation_Jensen_trace2_trace6_verified"])
        self.assertTrue(q["expected_sixth_walk_SW2_using_actual_mean_m_verified"])
        self.assertTrue(q["individual_selected_SW2_verified"])
        deg=list(q["original_J_induced_degree"].values())
        self.assertIn(1,deg)
        self.assertIn(0,deg)

    def test_07_REAL_W34_six_ID_source_nonvacuous_physical_C6(self):
        c=self.report["original_W34_NONVACUOUS_C6_full_global_two_cut_expectation"]
        self.assertEqual(c["s"],4)
        self.assertEqual(c["mode"],"lex")
        self.assertEqual(len(c["real_source_named_positive_sixset"]),6)
        self.assertTrue(c["all_original_source_J_independent"])
        self.assertGreater(c["original_full_graph_simple_physical_C6"],0)
        self.assertGreater(c["outcomes_with_true_selected_physical_C6"],0)
        self.assertGreater(F(c["exact_EXPECTED_selected_C6"]),0)
        self.assertEqual(F(c["exact_EXPECTED_selected_m"]),3)
        self.assertEqual(F(c["exact_EXPECTED_selected_tr2"]),6)
        self.assertTrue(c["all_true_selected_physical_source_edges_kept_in_pairs"])

    def test_08_REAL_W34_owner_proper_paths_exact_global_Jensen_r2_r3(self):
        c=self.report["original_W34_NONVACUOUS_C6_full_global_two_cut_expectation"]
        self.assertGreater(c["original_proper_2_path_count"],0)
        self.assertGreater(c["original_proper_3_path_count"],0)
        self.assertTrue(c["expected_true_global_r2_Jensen_and_survival_verified"])
        self.assertTrue(c["expected_true_global_r3_Jensen_and_survival_verified"])
        self.assertGreater(F(c["exact_EXPECTED_selected_tr4"]),0)
        self.assertGreater(F(c["exact_EXPECTED_selected_tr6"]),0)

    def test_09_no_assumption_owners_or_paths_independent_across_global_bits(self):
        c=self.report["original_W34_NONVACUOUS_C6_full_global_two_cut_expectation"]
        self.assertEqual(c["global_first_alphabet_symbols"],6)
        self.assertEqual(c["global_second_alphabet_symbols"],6)
        self.assertEqual(c["exact_global_color_outcomes"],4096)
        self.assertEqual(c["outcomes_with_true_selected_physical_C6"],4)
        self.assertGreaterEqual(c["original_full_graph_simple_physical_C6"],1)

    def test_10_expected_moment_source_bound_stronger_than_old_pointwise(self):
        for C0,c0 in ((F(1),F(1)),(F(2),F(1,5)),(F(7,3),F(1,17))):
            old=proof_budget(C0,c0,False)
            new=proof_budget(C0,c0,True)
            self.assertEqual(old["common_T"],new["common_T"])
            self.assertEqual(old["R"],new["R"])
            self.assertEqual(old["q2"],new["q2"])
            self.assertEqual(old["q3"],new["q3"])
            self.assertLess(int(new["L6"]),int(old["L6"]))
            self.assertLess(int(new["L4"]),int(old["L4"]))
            self.assertLess(int(new["E"]),int(old["E"]))
            self.assertLess(int(new["D"]),int(old["D"]))
            self.assertLess(new["all_h_sufficient_h0"],old["all_h_sufficient_h0"])

    def test_11_new_expected_sixth_coefficient_exact_all_h_source_N(self):
        z=envelopes(32)
        for C0,c0 in ((F(1),F(1)),(F(2),F(1,5))):
            x=proof_budget(C0,c0,True)
            T=int(x["common_T"])
            self.assertEqual(int(x["L6"]),24+ceilq(36*z["nu"]*T*T))
            self.assertLess(36*z["nu"],F(153))
            self.assertGreater(36*z["nu"],F(36))
            self.assertTrue(x["improved_selected_sixth_EXPECTATION_bound_only"])

    def test_12_new_expected_fourth_coefficient_uses_trace2_source_weight(self):
        z=envelopes(32)
        for C0,c0 in ((F(1),F(1)),(F(2),F(1,5))):
            x=proof_budget(C0,c0,True)
            self.assertEqual(int(x["L4"]),
                             x["q2"]**2*ceilsqrt(ceilq(z["nu"]*int(x["L6"])))
                             +19*int(x["common_T"]))
            self.assertTrue(x["exact_original_priority_global_event_probability_requires_single_selector"])

    def test_13_exact_same_T_new_vs_parent_R33281_three_formal_cases(self):
        cases=((F(1),F(1),620,612),
               (F(2),F(1,5),650,642),
               (F(7,3),F(1,17),657,648))
        for C0,c0,oldh,newh in cases:
            p=formal_renewal(C0,c0)
            self.assertEqual(p["old_root_h0"],oldh)
            self.assertEqual(p["new_root_h0"],newh)
            self.assertEqual(p["strict_dyadic_gain"],oldh-newh)
            self.assertEqual(p["R_exact_same_parent"],33281)
            self.assertTrue(p["new_selected_L6_only_in_expectation"])
            self.assertFalse(p["root_PROVED_A"])

    def test_14_exact_new_threshold_has_no_hidden_dyadic_s0_assumption(self):
        for C0,c0 in ((F(1),F(1)),(F(2),F(1,5)),(F(7,3),F(1,17))):
            p=proof_budget(C0,c0,True)
            s0=int(p["all_h_sufficient_s0"])
            self.assertGreaterEqual(s0,2**32)
            self.assertEqual(hd(s0),p["all_h_sufficient_h0"])
            for k in ("LOW_coordinate_threshold","LOW_endpoint_threshold",
                      "LOW_mixed_four_blocker_threshold"):
                self.assertLessEqual(int(p[k]),s0)
            self.assertGreater(F(p["true_produced_original_BBo_conditional_floor"]),
                               F(p["true_original_HEAVY_D6_delta"]))

    def test_15_graph_constants_formal_not_actual_numeric_results(self):
        for C0,c0 in ((F(0),F(1)),(F(1),F(0)),(F(1),F(2)),
                      (1,F(1)),(F(1),0.5)):
            with self.assertRaises(ValueError):
                proof_budget(C0,c0)
        for H in (0,7,9,31):
            with self.assertRaises(ValueError):
                envelopes(H)

    def test_16_true_sources_cannot_be_synthetic_or_duplicate(self):
        with self.assertRaises(ValueError):
            original_case(3,"lex")
        with self.assertRaises(ValueError):
            original_case(2,"fake")
        with self.assertRaises(ValueError):
            original_case(2,"lex",(0,0))
        with self.assertRaises(ValueError):
            original_case(4,"lex",(-1,1))

    def test_17_true_original_selected_graph_traces_are_integer_walks(self):
        for s in (2,4):
            q=original_case(s,"lex",(0,1,2))
            tr=_trace_even_and_cycles(_actual_physical_graph(q,q["ids"]))
            self.assertEqual(tr["tr2"],2*tr["m"])
            self.assertLessEqual(tr["tr4"]**2,tr["tr2"]*tr["tr6"])
            self.assertLessEqual(tr["tr6"],
                                 24*tr["physical_C6"]+72*tr["m"]*tr["Delta"]**2)

    def test_18_ROOT_stop_and_inherited_full_BBo_gate(self):
        c=self.report
        self.assertEqual(c["schema"],SCHEMA)
        self.assertEqual(c["status"],STATUS)
        self.assertEqual(c["issue"],230)
        self.assertEqual(c["parent_pr"],778)
        self.assertEqual(c["H"],32)
        self.assertEqual(c["K"],10)
        self.assertEqual(c["R"],33281)
        self.assertTrue(c["exact_ALL_h_source_rank_weight_expected_physical_edges_theorem_proved"])
        self.assertTrue(c["new_all_h_selected_sixth_moment_EXPECTATION_only"])
        self.assertTrue(c["new_all_h_selected_fourth_moment_Cauchy_across_ONE_selector"])
        self.assertTrue(c["actual_source_graph_GQ_and_proper_path_prerequisites_inherited"])
        self.assertTrue(c["original_LOW_full_mixed_books_and_BBo_inverses_still_open"])
        self.assertFalse(c["full_root_PROVED_A"])
        self.assertFalse(c["ASET_exponent_claimed"])
        self.assertTrue(c["no_fabricated_external_graph_C6_numerical_constants"])

    def test_19_certificate_complete_three_formal_and_real_source_cases(self):
        c=self.report
        self.assertEqual(len(c["FORMAL_not_published_graph_constants_common_T_ROOT"]),3)
        self.assertEqual(len(c["original_source_full_J_priority_and_cut_TRUE_W32"]
                             ["named_original_ids"]),3)
        self.assertEqual(len(c["original_W34_NONVACUOUS_C6_full_global_two_cut_expectation"]
                             ["real_source_named_positive_sixset"]),6)
        self.assertGreater(F(c["NEW_original_N_to_s4_envelope_nu_H"]),1)

    def test_20_prior_selected_sixth_bound_only_EXPECTED_not_all_omega(self):
        c=self.report
        self.assertFalse(c["full_root_PROVED_A"])
        for p in c["FORMAL_not_published_graph_constants_common_T_ROOT"]:
            self.assertTrue(p["new_selected_L6_only_in_expectation"])
            self.assertTrue(p["exact_rank_mass_bound_all_h"])
            self.assertEqual(p["new_root_delta_unchanged"],
                             proof_budget(F(p["C0_FORMAL_NOT_PUBLISHED"]),
                                          F(p["c0_FORMAL_NOT_PUBLISHED"]),True)
                             ["true_original_HEAVY_D6_delta"])


if __name__=="__main__":
    unittest.main()
