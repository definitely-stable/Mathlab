"""22 independent all-order and real ORIGINAL root-return/quantifier tests."""
import unittest
from fractions import Fraction as F
from math import comb
from hyp105_original_root_independent_return_dag import (
    SCHEMA,ISSUE,PARENT_PR,STATUS,H_FIXED,K_FIXED,R_FIXED,ALPHA,
    SOURCE_VERIFICATION,PROOF_GATES,NEEDS_INDEPENDENT_PUBLICATION_SIGNOFF,
    ceilq,ceilsqrt,h0,source_envelopes,full_root_budget,
    compare_old_and_sharp,genuine_original_model,dependency_graph,certificate,
)


class TestOriginalRootReturnDag(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cert=certificate()

    def test_01_all_h_envelope_and_exact_R(self):
        z=source_envelopes(32)
        self.assertEqual(z["R"],33281)
        self.assertEqual(z["q2return"],17)
        self.assertEqual(z["q3return"],49)
        self.assertGreater(z["M"],1)
        self.assertLess(z["M"],F(10001,10000))
        self.assertLess(z["nu"],F(10001,10000))
        self.assertLess(z["A"],F(20001,10000))

    def test_02_exact_NEW_sharp_8_nu_M_return_envelope(self):
        z=source_envelopes(32)
        self.assertEqual(z["Qcoef"],8*(z["nu"]+z["M"]))
        self.assertGreater(z["Qcoef"],16)
        self.assertLess(z["Qcoef"],17)
        self.assertGreater(3*z["Qcoef"],48)
        self.assertLess(3*z["Qcoef"],49)
        self.assertEqual(ceilq(3*z["Qcoef"]),49)
        self.assertEqual(ceilq(z["Qcoef"]),17)
        self.assertLess(z["Qcoef"],F(37,2))
        self.assertLess(3*z["Qcoef"],F(111,2))

    def test_03_all_H_even_source_return_envelope_self_consistency(self):
        for H in range(8,42,2):
            z=source_envelopes(H)
            self.assertEqual(z["q2return"],ceilq(z["Qcoef"]))
            self.assertEqual(z["q3return"],ceilq(3*z["Qcoef"]))
            self.assertLess(z["Qcoef"],19)
            self.assertLess(3*z["Qcoef"],F(111,2))
            self.assertLess(z["R"],93312)

    def test_04_TRUE_symplectic_full_graph_two_diagonals_source_count(self):
        for c in self.cert["TRUE_W32_W34_named_original_source_cases"]:
            s=c["s"]
            self.assertEqual(c["original_N"],(s+1)**2*(s*s+1))
            self.assertEqual(c["genuine_physical_real_owned_edges"],
                             2*c["original_CORE_named_flags"])
            self.assertGreaterEqual(c["source_true_J_total"],0)

    def test_05_SOURCE_point_pencil_return_exact_all_cases(self):
        for c in self.cert["TRUE_W32_W34_named_original_source_cases"]:
            self.assertEqual(c["Qx_from_named_SOURCE"],c["Qx_from_physical_two_walks"])
            self.assertEqual(c["Qx_from_named_SOURCE"],
                4*c["original_CORE_named_flags"]+4*c["source_J_point_conflicts"])

    def test_06_SOURCE_line_pencil_return_exact_all_cases(self):
        for c in self.cert["TRUE_W32_W34_named_original_source_cases"]:
            self.assertEqual(c["Qy_from_named_SOURCE"],c["Qy_from_physical_two_walks"])
            self.assertEqual(c["Qy_from_named_SOURCE"],
                4*c["original_CORE_named_flags"]+4*c["source_J_line_conflicts"])

    def test_07_TRUE_original_FULL_J_two_source_type_sum(self):
        for c in self.cert["TRUE_W32_W34_named_original_source_cases"]:
            self.assertEqual(c["source_true_J_total"],
                             c["source_J_point_conflicts"]+c["source_J_line_conflicts"])
            self.assertEqual(c["TRUE_physical_Qtotal"],
                             8*c["original_CORE_named_flags"]+4*c["source_true_J_total"])
            self.assertEqual(c["TRUE_physical_Qtotal"],
                             c["exact_SOURCE_Qtotal_identity"])

    def test_08_REAL_physical_3walk_every_typed_improper_return(self):
        cases=self.cert["TRUE_W32_W34_named_original_source_cases"]
        self.assertTrue(any(c["real_coordinate_improper_directed_three_walks"]>0 for c in cases))
        for c in cases:
            self.assertLessEqual(c["real_coordinate_improper_directed_three_walks"],
                                 c["REAL_improper3_upper"])
            self.assertLessEqual(c["real_coordinate_improper_directed_three_walks"],
                                 c["real_ALL_directed_three_walks"])
            self.assertTrue(c["actual_original_coordinate_improper3_and_fourth_bounds_verified"])

    def test_09_REAL_improper_two_step_Frobenius_leq_Delta_Q(self):
        for c in self.cert["TRUE_W32_W34_named_original_source_cases"]:
            self.assertLessEqual(c["real_coordinate_improper_two_path_norm2"],
                                 c["real_improper_two_path_norm2_upper"])
            self.assertLessEqual(c["real_coordinate_improper_two_path_norm2"],
                                 c["real_full_physical_trace4"])

    def test_10_conflicted_original_source_nonvacuous(self):
        cs=self.cert["TRUE_W32_W34_named_original_source_cases"]
        self.assertGreater(sum(c["source_true_J_total"]>0 for c in cs),0)
        self.assertTrue(any(c["s"]==4 and c["mode"]=="reverse" and
                            c["source_J_point_conflicts"]>0 for c in cs))
        self.assertTrue(any(c["s"]==4 and c["source_J_line_conflicts"]>0 for c in cs))

    def test_11_same_fixed_f_g_but_multiple_actual_paired_cores(self):
        cs=self.cert["TRUE_W32_W34_named_original_source_cases"]
        self.assertEqual(len(cs),24)
        for s in (2,4):
            for mode in ("lex","reverse","shift"):
                vals=[c for c in cs if c["s"]==s and c["mode"]==mode]
                self.assertEqual({c["core"] for c in vals},
                                 {"full","even","thin","shifted"})
                self.assertEqual(len({c["original_N"] for c in vals}),1)
                self.assertEqual(len({c["original_CORE_named_flags"] for c in vals}),4)

    def test_12_NEW_L4_source_return_17T_without_new_randomness(self):
        z=source_envelopes(32)
        for C0,c0 in ((F(1),F(1)),(F(2),F(1,5)),(F(7,3),F(1,17))):
            new=full_root_budget(C0,c0,True)
            old=full_root_budget(C0,c0,False)
            T=int(new["T"])
            self.assertEqual(int(new["L4"]),
                new["q2"]**2*ceilsqrt(ceilq(z["nu"]*int(new["L6"])))+17*T)
            self.assertEqual(int(old["L4"])-int(new["L4"]),2*T)
            self.assertEqual(new["L6"],old["L6"])
            self.assertEqual(new["R"],old["R"])

    def test_13_NEW_coord_improper_49T_not_55_point5_T(self):
        for C0,c0 in ((F(1),F(1)),(F(2),F(1,5))):
            new=full_root_budget(C0,c0,True)
            old=full_root_budget(C0,c0,False)
            self.assertEqual(new["coordinate_bad_coefficient_exact"],"49")
            self.assertEqual(old["coordinate_bad_coefficient_exact"],"111/2")
            self.assertLess(int(new["coordinate_threshold"]),
                            int(old["coordinate_threshold"]))

    def test_14_SHARED_T_exact_HEAVY_C6_condition(self):
        for C0,c0 in ((F(1),F(1)),(F(2),F(1,5)),(F(7,3),F(1,17))):
            p=full_root_budget(C0,c0)
            R=p["R"];T=int(p["T"])
            self.assertGreaterEqual(F(T),F(17*R**3,2)*C0**3)
            self.assertLess(F(T-1),F(17*R**3,2)*C0**3)
            self.assertEqual(F(p["original_HEAVY_D6_delta"]),c0/F(R**6))

    def test_15_LOW_true_core_Blackley_Roy_Rsame_source_A(self):
        z=source_envelopes(32)
        c=F(7,8)-4*z["M"]/11
        self.assertGreater(c,0)
        w=(4*c)**3/z["A"]**2
        for C0,c0 in ((F(1),F(1)),(F(2),F(1,5))):
            p=full_root_budget(C0,c0)
            self.assertEqual(F(p["true_original_LOW_W3_floor"]),w)
            self.assertEqual(F(p["original_BBo_produced_conditional_floor"]),w/64)

    def test_16_asymmetric_3_error_thresholds_full_quantifiers(self):
        for C0,c0 in ((F(1),F(1)),(F(2),F(1,5)),(F(7,3),F(1,17))):
            p=full_root_budget(C0,c0)
            s0=int(p["all_h_sufficient_s0"])
            self.assertEqual(h0(s0),p["formal_dyadic_h0"])
            self.assertGreaterEqual(s0,2**32)
            self.assertGreaterEqual(s0,int(p["coordinate_threshold"]))
            self.assertGreaterEqual(s0,int(p["endpoint_threshold"]))
            self.assertGreaterEqual(s0,int(p["four_blocker_threshold"]))
            self.assertLess(F(p["original_HEAVY_D6_delta"]),
                            F(p["original_BBo_produced_conditional_floor"]))

    def test_17_formal_only_no_published_numeric_graph_constants(self):
        for C0,c0 in ((F(0),F(1)),(F(1),F(0)),(F(1),F(2)),
                      (1,F(1)),(F(1),0.5)):
            with self.assertRaises(ValueError):
                full_root_budget(C0,c0)
        for H in (1,3,7,9,31):
            with self.assertRaises(ValueError):
                source_envelopes(H)

    def test_18_original_PROOF_GATE_dependency_graph_is_acyclic(self):
        graph=self.cert["independent_root_dependency_gate_graph"]
        order=graph["order"];nodes=graph["nodes"]
        self.assertEqual(len(order),len(PROOF_GATES))
        self.assertEqual(len(set(order)),len(order))
        self.assertEqual(order[-1],"ROOT_SEVEN")
        for name in order:
            for dep in nodes[name]["deps"]:
                self.assertLess(order.index(dep),order.index(name))
        self.assertFalse(graph["ROOT_PROVED_A"])

    def test_19_gate_exposes_unaccepted_original_full_dependency(self):
        g=self.cert["independent_root_dependency_gate_graph"]
        self.assertIn("GRAPH_C6",g["order"])
        self.assertEqual(g["nodes"]["GRAPH_C6"]["gate_scope"],"external_published_theorem")
        self.assertIn("FULL_AC_BOOK",g["unaccepted_publication_gates"])
        self.assertIn("LOW_BBO_INVERSE",g["unaccepted_publication_gates"])
        self.assertIn("ROOT_SEVEN",g["unaccepted_publication_gates"])
        self.assertTrue(g["external_graph_C6_theorem_correctly_scoped_to_SIMPLE_UNDIRECTED_Graph"])
        self.assertTrue(g["all_h_new_SOURCE_RETURN_gate_proved_by_literal_identities"])

    def test_20_no_falsely_proved_new_sixset_or_GF5_class(self):
        c=self.cert
        self.assertEqual(c["parent_pr"],781)
        self.assertEqual(c["issue"],230)
        self.assertEqual(c["status"],STATUS)
        self.assertFalse(c["original_seven_unweighted_motif_ROOT_PROVED_A"])
        self.assertTrue(c["original_D6_BBo_sixset_nonoverlap_INHERITED_not_falsely_new"])
        self.assertTrue(c["published_Simonovits_graph_C6_constants_numeric_unknown"])

    def test_21_code_rejects_fake_original_geom_core_and_wrong_types(self):
        for bad in (3,8,-1):
            with self.assertRaises(ValueError):
                genuine_original_model(bad,"lex","full")
        with self.assertRaises(ValueError):
            genuine_original_model(2,"bad","full")
        with self.assertRaises(ValueError):
            genuine_original_model(2,"lex","bad")
        with self.assertRaises(TypeError):
            ceilq(0.5)
        with self.assertRaises(ValueError):
            ceilsqrt(-1)
        with self.assertRaises(ValueError):
            h0(0)

    def test_22_exact_THREE_formal_probes_and_ROOT_STOP(self):
        c=self.cert
        self.assertEqual(c["schema"],SCHEMA)
        self.assertEqual(c["fixed_H"],32)
        self.assertEqual(c["fixed_K"],10)
        self.assertEqual(c["fixed_R"],33281)
        self.assertEqual(c["new_integer_source_Qx_y_bound"],17)
        self.assertEqual(c["new_integer_coordinate_improper_bound"],49)
        self.assertTrue(c["new_all_h_exact_original_Qx_Qy_source_identity"])
        self.assertTrue(c["genuine_original_all_h_improper3_SHARP_49T_and_fourth_17T"])
        self.assertTrue(c["one_SHARED_full_original_J_envelope_for_HEAVY_and_LOW"])
        self.assertEqual(len(c["formal_unknown_graph_constant_ROOT_scenarios"]),3)
        for p in c["formal_unknown_graph_constant_ROOT_scenarios"]:
            self.assertTrue(p["T_same"])
            self.assertTrue(p["new_return_all_h_proved_from_named_SOURCE_pencils"])
            self.assertFalse(p["ROOT_PROVED_A"])
            self.assertLessEqual(p["new_h0"],p["old_h0"])


if __name__=="__main__":
    unittest.main()
