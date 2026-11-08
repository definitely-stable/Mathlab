"""AA4-MIXSTAR independent original GQ/defect-mask theorem falsifiers."""
from fractions import Fraction
from math import comb
import unittest

from hyp105_original_mixed_star_defect_referee import (
    SCHEMA, ROOT_STATUS, R, K, D6_WEIGHT, BBO_PRODUCED_WEIGHT,
    all_h_defect_theorem, _fixture, _projection, _incident_line,
    genuine_original_defect_case, canonical_report,
)


class TestOriginalMixedStarDefectInterpolation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.z=canonical_report()

    def test_exact_all_h_quantifier_15_formal_C0_c0_kappa_cases(self):
        a=self.z["all_h_15_FORMAL_independent_source_defect_interpolation_ledgers"]
        self.assertEqual(len(a),15)
        self.assertEqual([(q["C0_FORMAL"],q["c0_FORMAL"],q["h0"])
                          for q in a[::5]],
                         [("1","1",751),("2","1/5",781),("7/3","1/17",787)])
        for q in a:
            with self.subTest(C=q["C0_FORMAL"],kappa=q["kappa"]):
                self.assertEqual(q["R"],93313)
                self.assertEqual(
                    len(q["all_h_17_independent_quantifier_gates"]),17)
                self.assertTrue(all(q["all_h_17_independent_quantifier_gates"].values()))
                self.assertFalse(q["external_graph_C0_c0_numerically_verified"])
                self.assertGreater(q["s0"],64)
                self.assertTrue((1<<q["h0"])>=q["s0"]>(1<<(q["h0"]-1)))

    def test_NEW_continuous_rho_kappa_exact_three_over_two_plus_kappa(self):
        probes=self.z["all_h_15_FORMAL_independent_source_defect_interpolation_ledgers"]
        for j in range(0,len(probes),5):
            arr=probes[j:j+5]
            self.assertEqual([q["kappa"] for q in arr],["0","1/4","1/2","3/4","1"])
            vals=[Fraction(q["rho_original_defect_kappa_Z"]) for q in arr]
            self.assertEqual(sorted(vals,reverse=True),vals)
            self.assertEqual(vals[0],Fraction(3,2)*vals[-1])
            for q in arr:
                k=Fraction(q["kappa"])
                rho=Fraction(q["rho_original_defect_kappa_Z"])
                rhoany=Fraction(q["rho_original_arbitrary_Z"])
                self.assertEqual(rho/rhoany,Fraction(3)/(2+k))
                self.assertEqual(rho*Fraction(8+4*k)*q["q3"]**2*q["L6"],
                                 Fraction(q["tstar"])**2)
                self.assertLess(rho,Fraction(1,2**32))
                self.assertEqual(Fraction(q["original_Z_endpoint_mask_multiplier"]),8+4*k)

    def test_same_HEAVY_and_LOW_s0_delta_and_GF5_risk_for_all_defect_kappa(self):
        data=self.z["all_h_15_FORMAL_independent_source_defect_interpolation_ledgers"]
        for j in range(0,len(data),5):
            a=data[j:j+5]
            for q in a:
                self.assertEqual(q["T"],a[0]["T"])
                self.assertEqual(q["L6"],a[0]["L6"])
                self.assertEqual(q["s0"],a[0]["s0"])
                self.assertEqual(q["h0"],a[0]["h0"])
                self.assertEqual(q["delta_original_seven_class_S_s"],
                                 a[0]["delta_original_seven_class_S_s"])
                delta=Fraction(q["delta_original_seven_class_S_s"])
                self.assertEqual(
                    Fraction(q["separate_original_additive_GF5_R3_floor"]),
                    Fraction(D6_WEIGHT,51**6)*delta)
                self.assertEqual(
                    Fraction(BBO_PRODUCED_WEIGHT,2)*
                    (Fraction(119,24)-Fraction(q["tstar"])),
                    D6_WEIGHT*delta)

    def test_full_real_source_ten_examples_and_actual_physical_typed_endpoints(self):
        cases=self.z["true_original_W32_W34_GQ_direct_physical_mask_cases"]
        self.assertEqual(len(cases),10)
        self.assertEqual([q["s"] for q in cases],[2,2,4,4,4,4,4,4,4,4])
        for q in cases:
            with self.subTest(s=q["s"],scheme=q["scheme"]):
                s=q["s"];V=(s+1)*(s*s+1);Z=q["original_deleted_SOURCE_ID_count"]
                self.assertEqual(q["original_full_GQ_nonincident_q_r_projections"],
                                 V*(V-s-1))
                self.assertTrue(q["all_three_original_source_anchor_roles_exact_s2"])
                self.assertEqual(q["original_GQ_middle_anchor_Z_exposures"],s*s*Z)
                self.assertEqual(q["physical_typed_real_endpoint_pairs_count"],
                                 4*V*(V-s-1))
                self.assertEqual(q["original_source_M_Z_mask_from_three_anchors"],
                                 q["actual_REAL_physical_oriented_endpoint_Z_masks"])
                self.assertTrue(q["new_original_defect_formula_and_true_physical_masks_match"])

    def test_new_exact_isolated_middle_defect_H_F_identity_for_ALL_Z(self):
        for q in self.z["true_original_W32_W34_GQ_direct_physical_mask_cases"]:
            s=q["s"];Z=q["original_deleted_SOURCE_ID_count"]
            D=q["D_isolated_original_middle_anchor_deletion_defect"]
            H=q["H_all_three_original_anchors_deleted"]
            F=q["F_two_ends_deleted_middle_NOT_deleted"]
            self.assertLessEqual(D,s*s*Z)
            self.assertEqual(
                q["original_source_credit_Xi_Z"],
                4*(s*s*Z-D+H+F))
            self.assertEqual(
                q["original_source_M_Z_mask_from_three_anchors"],
                8*s*s*Z+4*D-4*H-4*F)
            self.assertLessEqual(
                q["original_source_M_Z_mask_from_three_anchors"],
                q["new_DEFECT_based_mask_upper_8s2Z_plus_4D"])
            self.assertLessEqual(
                q["original_source_M_Z_mask_from_three_anchors"],
                q["old_arbitrary_original_Z_mask_upper_12s2Z"])
            self.assertEqual(
                Fraction(q["exact_original_source_kappa_effective"]),
                Fraction(D,s*s*Z))

    def test_MIXED_full_original_point_AND_line_STARS_defect_ZERO(self):
        cases=self.z["true_original_W32_W34_GQ_direct_physical_mask_cases"]
        mixed=cases[:6]
        self.assertEqual(len(mixed),6)
        for c in mixed:
            self.assertTrue(c["is_complete_point_OR_line_star_UNION"])
            self.assertTrue(c["is_genuine_MIXED_point_AND_line_star_UNION"])
            self.assertGreater(len(c["selected_original_POINT_stars"]),0)
            self.assertGreater(len(c["selected_original_LINE_stars"]),0)
            self.assertEqual(tuple(c["extra_ORIGINAL_deleted_incidence_IDs"]),())
            self.assertEqual(c["D_isolated_original_middle_anchor_deletion_defect"],0)
            self.assertEqual(c["exact_original_source_kappa_effective"],"0")
            self.assertLessEqual(
                c["original_source_M_Z_mask_from_three_anchors"],
                8*c["s"]**2*c["original_deleted_SOURCE_ID_count"])
        self.assertTrue(any(c["actual_selected_point_line_original_incidence_overlap"]>0
                            for c in mixed))
        self.assertTrue(any(c["actual_selected_point_line_original_incidence_overlap"]==0
                            for c in mixed))
        self.assertTrue(any(len(c["selected_original_POINT_stars"])>=2 for c in mixed))
        self.assertTrue(any(len(c["selected_original_LINE_stars"])>=2 for c in mixed))

    def test_isolated_SINGLE_named_original_flag_has_exact_kappa_ONE_no_false_improvement(self):
        q=self.z["true_original_W32_W34_GQ_direct_physical_mask_cases"][6]
        self.assertEqual(tuple(q["extra_ORIGINAL_deleted_incidence_IDs"]),(0,))
        self.assertFalse(q["is_complete_point_OR_line_star_UNION"])
        self.assertEqual(q["original_deleted_SOURCE_ID_count"],1)
        self.assertEqual(q["exact_original_source_kappa_effective"],"1")
        self.assertEqual(q["H_all_three_original_anchors_deleted"],0)
        self.assertEqual(q["F_two_ends_deleted_middle_NOT_deleted"],0)
        self.assertEqual(q["original_source_credit_Xi_Z"],0)
        self.assertEqual(
            q["original_source_M_Z_mask_from_three_anchors"],
            q["old_arbitrary_original_Z_mask_upper_12s2Z"])
        self.assertEqual(q["original_source_M_Z_mask_from_three_anchors"],192)

    def test_PARTIAL_source_point_STAR_plus_one_flag_has_strictly_INTERMEDIATE_kappa(self):
        q=self.z["true_original_W32_W34_GQ_direct_physical_mask_cases"][7]
        k=Fraction(q["exact_original_source_kappa_effective"])
        self.assertGreater(k,0)
        self.assertLess(k,1)
        self.assertFalse(q["is_complete_point_OR_line_star_UNION"])
        self.assertGreater(q["D_isolated_original_middle_anchor_deletion_defect"],0)
        self.assertLess(q["new_DEFECT_based_mask_upper_8s2Z_plus_4D"],
                        q["old_arbitrary_original_Z_mask_upper_12s2Z"])
        self.assertGreater(Fraction(3)/(2+k),1)

    def test_TRUE_point_ONLY_line_ONLY_star_as_edge_cases(self):
        for q in self.z["true_original_W32_W34_GQ_direct_physical_mask_cases"][8:]:
            self.assertTrue(q["is_complete_point_OR_line_star_UNION"])
            self.assertFalse(q["is_genuine_MIXED_point_AND_line_star_UNION"])
            self.assertEqual(q["D_isolated_original_middle_anchor_deletion_defect"],0)
            self.assertLessEqual(q["original_source_M_Z_mask_from_three_anchors"],
                                 8*q["s"]**2*q["original_deleted_SOURCE_ID_count"])

    def test_new_formal_all_h_consistent_with_FROZEN_parent_all_h_TEST_ONLY(self):
        # Test-only crosscheck, not a dependency in the main independent source.
        from hyp105_original_heavy_adaptive_ss6_referee import standalone_quantified_theorem
        from hyp105_original_full_star_z_50pct_referee import star_all_h
        for C,c in ((Fraction(1),Fraction(1)),
                    (Fraction(2),Fraction(1,5)),
                    (Fraction(7,3),Fraction(1,17))):
            prev=standalone_quantified_theorem(C,c)
            star=star_all_h(C,c)
            new0=all_h_defect_theorem(C,c,Fraction(0))
            new1=all_h_defect_theorem(C,c,Fraction(1))
            for key in ("T","L6","s0","h0"):
                self.assertEqual(new0[key],prev[key])
                self.assertEqual(new1[key],prev[key])
                self.assertEqual(new0[key],star[key])
            self.assertEqual(Fraction(new0["delta_original_seven_class_S_s"]),
                             Fraction(prev["delta"]))
            self.assertEqual(Fraction(new0["rho_original_MIXED_POINT_LINE_STAR_Z"]),
                             Fraction(star["rho_FULL_POINT_OR_LINE_STAR_original_Z"]))
            self.assertEqual(Fraction(new1["rho_original_defect_kappa_Z"]),
                             Fraction(prev["rho_star"]))

    def test_invalid_kappa_formal_external_source_inputs_and_fake_original_IDs_rejected(self):
        for k in (-1,Fraction(-1,4),Fraction(5,4),0,1,0.5,"1/2"):
            with self.assertRaises(ValueError):
                all_h_defect_theorem(Fraction(1),Fraction(1),k)
        for C,c in ((1,Fraction(1)),(Fraction(1),1),
                    (Fraction(0),Fraction(1)),(Fraction(1),Fraction(0))):
            with self.assertRaises(ValueError):
                all_h_defect_theorem(C,c,Fraction(0))
        with self.assertRaises(ValueError):
            genuine_original_defect_case(3,"lex",points=(0,),lines=(0,))
        with self.assertRaises(ValueError):
            genuine_original_defect_case(1,"lex",points=(0,0))
        with self.assertRaises(ValueError):
            genuine_original_defect_case(1,"lex",extra_flags=(99,))
        with self.assertRaises(ValueError):
            genuine_original_defect_case(1,"lex",points=(),lines=(),extra_flags=())

    def test_root_230_stays_open_for_prior_ALL_h_acceptance_even_if_CI_green(self):
        z=self.z
        self.assertEqual(z["schema"],SCHEMA)
        self.assertEqual(z["root_230_status"],ROOT_STATUS)
        self.assertFalse(z["root_Branch_A_PROVED_A"])
        self.assertFalse(z["root_new_ASET_exponent"])
        self.assertFalse(z["published_graph_SS6_numerical_constants_verified"])
        self.assertTrue(z["root_original_SEVEN_unweighted_motif_S_s_not_R3"])
        self.assertTrue(z["R3_separate_additive_full_GF5_sign_event_SUM"])
        self.assertTrue(z["NEW_all_h_exact_original_defect_identity_proved_in_manuscript"])
        self.assertTrue(z["NEW_all_h_MIXED_point_AND_line_source_STAR_50percent_radius"])
        self.assertTrue(z["NEW_all_h_continuous_defect_kappa_radius"])
        self.assertTrue(z["remaining_predecessor_proof_DAG_requires_final_mathematical_signoff"])


if __name__=="__main__":
    unittest.main()
