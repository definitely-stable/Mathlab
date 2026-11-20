"""All-order rational and genuine-original LOW mixed-book referee tests."""
import unittest
from fractions import Fraction as F
from math import comb

from hyp105_low_spectral_books46_referee import (
    SCHEMA,STATUS,H,K,R,PARENT,all_h_bound,source_book,scenario,
    original_collinear,grams,full_source_degrees,
    actual_source_conflict_max,physical_fourth_and_blockers,
    exact_root_formal,qceil,sqrt_ceil,certificate,
)
from hyp105_low_publication_partition_referee import model


class TestOriginalSpectralBooks46(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=certificate()

    def test_01_all_h_independent_rational_source_GQ_Gram_coefficient(self):
        z=all_h_bound()
        self.assertEqual(z["fixed_H"],32)
        self.assertGreater(F(z["strict_sqrt_2V_bound_margin"]),0)
        self.assertGreater(F(z["exact_Bx_squared_coefficient_bound"]),45)
        self.assertLess(F(z["exact_Bx_squared_coefficient_bound"]),46)
        self.assertEqual(z["certified_book_squared_integer_coefficient"],46)
        self.assertEqual(z["inherited_previous_book_squared_integer_coefficient"],360)

    def test_02_exact_R32_and_source_quantifier_firewall(self):
        z=self.c["new_all_h_original_source_Gram_book_46"]
        self.assertEqual(z["original_GQ_nonprincipal_positive_eigenvalue"],"s-1")
        self.assertTrue(z["valid_all_dyadic_s_at_least_2_to_32"])
        self.assertTrue(z["arbitrary_fixed_correlated_global_f_g"])
        self.assertTrue(z["root_only_Z_empty_core_degree_K_at_most_10"])
        self.assertTrue(z["external_graph_C6_constants_numeric_unknown"])
        self.assertFalse(z["root_PROVED_A"])

    def test_03_true_original_symplectic_dual_GQ_SRG_each_case(self):
        for z in self.c["genuine_original_independent_source_books"]:
            self.assertEqual(z["true_original_A_size"]+(
                3 if z["core"]=="deleted" else 0),
                (z["s"]+1)**2*(z["s"]**2+1))
            self.assertGreaterEqual(z["source_JC_max_degree"],0)

    def test_04_first_principle_f_g_Gram_matches_actual_SRG_polynomial(self):
        for z in self.c["genuine_original_independent_source_books"]:
            for key in ("source_Gf","source_Gg"):
                g=z[key]
                self.assertEqual(g["G"],g["formula"])
                self.assertLessEqual(g["G"],g["spectrum_upper"])
                self.assertGreater(g["max_fibre"],0)

    def test_05_point_and_line_source_Gram_not_artificially_equal(self):
        for z in self.c["genuine_original_independent_source_books"]:
            self.assertGreaterEqual(z["source_Gf"]["G"],0)
            self.assertGreaterEqual(z["source_Gg"]["G"],0)
        self.assertTrue(any(
            z["source_Gf"]["G"]!=z["source_Gg"]["G"] for z in
            self.c["genuine_original_independent_source_books"]))

    def test_06_actual_physical_FULL_A_and_paired_CORE_cross_Theta(self):
        for z in self.c["genuine_original_independent_source_books"]:
            theta=z["true_physical_A_C_cross_Theta"]
            self.assertEqual(theta,z["point_book"]["Theta_source"])
            self.assertEqual(theta,z["line_book"]["Theta_source"])
            self.assertEqual(theta,z["point_book"]["Theta_physical"])
            self.assertEqual(theta,z["line_book"]["Theta_physical"])

    def test_07_true_independent_mixed_source_book_Cauchy_F1_F2(self):
        for z in self.c["genuine_original_independent_source_books"]:
            for typ,gram in (("point_book","source_Gf"),
                             ("line_book","source_Gg")):
                q=z[typ]
                self.assertLessEqual(q["source_book_B"]**2,q["F1"]*q["F2"])
                self.assertLessEqual(q["F1"],2*z[gram]["G"])

    def test_08_original_source_JC_clique_not_assumed_fixed_K(self):
        for z in self.c["genuine_original_independent_source_books"]:
            Kc=z["source_JC_max_degree"]
            for typ in ("point_book","line_book"):
                q=z[typ]
                self.assertEqual(q["Kc"],Kc)
                self.assertLessEqual(q["max_mixed_entry"],
                                     2*(z["s"]+1)*(Kc+1))
                self.assertLessEqual(q["F2"],
                                     2*(z["s"]+1)*(Kc+1)*q["Theta_source"])

    def test_09_exact_FULL_A_CROSS_vertex_degree_sum(self):
        for z in self.c["genuine_original_independent_source_books"]:
            for typ in ("point_book","line_book"):
                q=z[typ]
                self.assertLessEqual(q["Theta_source"],
                                     4*z["true_original_A_size"]*q["Delta"])

    def test_10_point_line_dual_book_global_source_bound(self):
        for z in self.c["genuine_original_independent_source_books"]:
            for typ,gram in (("point_book","source_Gf"),
                             ("line_book","source_Gg")):
                q=z[typ]
                self.assertLessEqual(q["source_book_B"]**2,
                     16*(z["s"]+1)*(q["Kc"]+1)*
                     z["true_original_A_size"]*q["Delta"]*
                     z[gram]["G"])

    def test_11_independent_PHYSICAL_fourblockers_reversal(self):
        for z in self.c["genuine_original_independent_source_books"]:
            q=z["physical"]
            a,b,c,d=q["four_blocker_cardinalities"]
            self.assertEqual(a,b)
            self.assertEqual(c,d)
            self.assertLessEqual(q["four_blocker_union"],a+b+c+d)

    def test_12_physical_trace4_source_book_each_of_four(self):
        for z in self.c["genuine_original_independent_source_books"]:
            q=z["physical"]
            Delta=q["actual_Delta"]
            t4=q["actual_trace_A4"]
            self.assertEqual(Delta,z["point_book"]["Delta"])
            self.assertEqual(Delta,z["line_book"]["Delta"])
            for i,b in ((0,"point_source_Bx"),(1,"point_source_Bx"),
                        (2,"line_source_By"),(3,"line_source_By")):
                self.assertLessEqual(q["four_blocker_cardinalities"][i]**2,
                                     q[b]*Delta*t4)

    def test_13_exact_formal_global_R_and_B0_strict_improvement(self):
        for z in self.c["FORMAL_external_C6_constants_scenarios"]:
            self.assertEqual(z["R"],33281)
            self.assertEqual(z["root_K"],10)
            self.assertGreater(int(z["book_B0_historical_360"]),
                               int(z["book_B0_NEW_46"]))
            self.assertGreater(int(z["fourblocker_D_old"]),
                               int(z["fourblocker_D_NEW"]))
            self.assertGreater(int(z["endpoint_coefficient_old_24"]),
                               int(z["endpoint_coefficient_NEW_17"]))
            self.assertFalse(z["numeric_external_graph_constants_known"])

    def test_14_s0_dyadic_h0_exact_improved_but_root_unproved(self):
        for z in self.c["FORMAL_external_C6_constants_scenarios"]:
            self.assertGreater(z["root_previous_h0"],z["root_NEW_h0"])
            self.assertGreater(z["dyadic_h_gained"],0)
            self.assertEqual(z["dyadic_h_gained"],
                            z["root_previous_h0"]-z["root_NEW_h0"])
            self.assertFalse(z["original_ROOT_PROVED_A"])

    def test_15_exact_rational_and_negative_fail_closed(self):
        self.assertEqual(qceil(F(7,3)),3)
        self.assertEqual(sqrt_ceil(16),4)
        self.assertEqual(sqrt_ceil(17),5)
        with self.assertRaises(TypeError):qceil(1.5)
        with self.assertRaises(ValueError):sqrt_ceil(-1)
        with self.assertRaises(ValueError):sqrt_ceil(F(1,3))
        for C0,c0 in ((F(0),F(1)),(F(1),F(0)),
                      (F(1),F(2)),(1,F(1)),(F(1),1.0)):
            with self.assertRaises(ValueError):
                exact_root_formal(C0,c0)

    def test_16_genuine_source_cases_s32_s34_physical(self):
        a=self.c["genuine_original_independent_source_books"]
        self.assertEqual(len(a),10)
        self.assertEqual({(z["s"],z["scheme"],z["core"]) for z in a},
            {(s,scheme,core) for s in (2,4)
             for scheme,core in (("lex","full"),("reverse","full"),
                                  ("correlated","full"),("lex","even"),
                                  ("reverse","deleted"))})
        self.assertTrue(any(z["true_original_A_size"]!=
                            z["true_paired_C_size"] for z in a))
        self.assertTrue(any(z["physical"]["four_blocker_union"]>0 for z in a))

    def test_17_scope_of_publication_and_root_still_OPEN(self):
        c=self.c
        self.assertEqual(c["schema"],SCHEMA)
        self.assertEqual(c["status"],STATUS)
        self.assertEqual(c["issue"],230)
        self.assertEqual(c["parent_pr"],784)
        self.assertTrue(c["independent_FULL_A_not_equal_CORE_C"])
        self.assertTrue(c["independent_original_JC_K_observed_not_assumed_10"])
        self.assertTrue(c["low_selector_expected_moments_inherited_not_independently_refereed"])
        self.assertFalse(c["global_HYP105_root_PROVED_A"])


if __name__=="__main__":
    unittest.main()
