"""New 50% original complete point-/line-star adversarial Z source theorem."""
from fractions import Fraction
from math import comb
import unittest

from hyp105_original_full_star_z_50pct_referee import (
    SCHEMA, star_all_h, true_full_source_star_case, canonical_report,
)


class TestOriginalFullSourceStarZ50Percent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.x=canonical_report()

    def test_three_exact_FORMAL_all_h_source_STAR_risk_preserving_ledgers(self):
        z=self.x["all_h_original_point_and_line_STAR_risk_preserving_ledgers"]
        self.assertEqual([(x["C0_FORMAL"],x["c0_FORMAL"],x["h0"]) for x in z],
                         [("1","1",751),("2","1/5",781),("7/3","1/17",787)])
        for x in z:
            self.assertEqual(x["R"],93313)
            self.assertTrue(all(x["all_h_13_exact_structured_original_Z_theorem_gates"].values()))
            self.assertEqual(len(x["all_h_13_exact_structured_original_Z_theorem_gates"]),13)
            rhoany=Fraction(x["rho_arbitrary_original_Z"])
            rhostar=Fraction(x["rho_FULL_POINT_OR_LINE_STAR_original_Z"])
            self.assertEqual(rhostar,Fraction(3,2)*rhoany)
            self.assertLess(rhostar,Fraction(1,2**32))
            self.assertLess(rhostar,Fraction(3,64))
            self.assertGreater(rhostar,rhoany)
            delta=Fraction(x["delta"])
            self.assertEqual(Fraction(x["same_seven_original_motif_S_s_floor"]),delta)
            self.assertEqual(Fraction(x["same_GF5_additive_R3_floor"]),
                             Fraction(54162,51**6)*delta)
            self.assertFalse(x["numerical_graph_constants_published"])

    def test_source_point_AND_line_FULL_star_four_original_W32_W34_cases(self):
        z=self.x["true_original_symplectic_full_STAR_GQ_falsifiers"]
        self.assertEqual(len(z),6)
        self.assertEqual([(x["s"],x["type"]) for x in z][:4],
                         [(2,"point"),(2,"line"),(4,"point"),(4,"line")])
        for x in z:
            s=x["s"]
            self.assertEqual(x["all_deleted_original_incidence_IDs"],
                             (s+1)*len(x["selected_original_source_stars"]))
            self.assertEqual(x["original_nonincident_full_GQ_projections"],
                             (s+1)*(s*s+1)*((s+1)*(s*s+1)-s-1))
            self.assertTrue(x["each_source_role_s2_exact"])
            self.assertTrue(x["original_SOURCE_STAR_50percent_more_deletion_exact"])

    def test_exact_NEW_source_star_overlap_formula_and_mask_8s2Z(self):
        z=self.x["true_original_symplectic_full_STAR_GQ_falsifiers"]
        for x in z:
            s=x["s"];Z=x["all_deleted_original_incidence_IDs"]
            extra=x["source_extra_both_endpoint_and_middle_STAR_overlap"]
            self.assertEqual(x["source_projections_middle_STAR_selected"],s*s*Z)
            self.assertEqual(x["original_Z_overlap_rebate_exact"],4*s*s*Z+4*extra)
            self.assertEqual(x["actual_original_Z_masked_directed_typed_endpoints"],
                             8*s*s*Z-4*extra)
            self.assertLessEqual(x["actual_original_Z_masked_directed_typed_endpoints"],
                                 x["complete_source_STAR_sharp_8s2Z"])
            self.assertEqual(x["complete_source_STAR_crude_12s2Z"]*2,
                             3*x["complete_source_STAR_sharp_8s2Z"])
            self.assertGreater(x["original_Z_overlap_rebate_exact"],0)

    def test_real_W34_single_POINT_star_cluster_matches_independent_previous_GQ_case(self):
        cases=self.x["true_original_symplectic_full_STAR_GQ_falsifiers"]
        x=cases[2]
        self.assertEqual(x["s"],4)
        self.assertEqual(x["type"],"point")
        self.assertEqual(x["selected_original_source_stars"],[0])
        self.assertEqual(x["all_deleted_original_incidence_IDs"],5)
        self.assertEqual(x["actual_original_Z_masked_directed_typed_endpoints"],640)
        self.assertEqual(x["original_Z_overlap_rebate_exact"],320)
        self.assertEqual(x["complete_source_STAR_crude_12s2Z"],960)

    def test_genuine_independent_LINE_dual_and_multi_full_stars_not_just_point_fixture(self):
        z=self.x["true_original_symplectic_full_STAR_GQ_falsifiers"]
        self.assertEqual(z[3]["type"],"line")
        self.assertEqual(z[3]["s"],4)
        self.assertEqual(z[3]["all_deleted_original_incidence_IDs"],5)
        self.assertEqual(z[4]["type"],"point")
        self.assertEqual(z[4]["selected_original_source_stars"],[1,3])
        self.assertEqual(z[5]["type"],"line")
        self.assertEqual(z[5]["selected_original_source_stars"],[1,3])
        for x in z[4:]:
            self.assertEqual(x["all_deleted_original_incidence_IDs"],10)
            self.assertGreaterEqual(x["source_extra_both_endpoint_and_middle_STAR_overlap"],0)

    def test_parent_93313_original_universal_threshold_not_changed_BY_STAR_Z_TEST_ONLY(self):
        from hyp105_original_heavy_adaptive_ss6_referee import standalone_quantified_theorem
        for C,c in ((Fraction(1),Fraction(1)),
                    (Fraction(2),Fraction(1,5)),
                    (Fraction(7,3),Fraction(1,17))):
            previous=standalone_quantified_theorem(C,c)
            new=star_all_h(C,c)
            for k in ("T","L6","s0","h0"):
                self.assertEqual(new[k],previous[k])
            self.assertEqual(Fraction(new["delta"]),Fraction(previous["delta"]))
            self.assertEqual(Fraction(new["rho_arbitrary_original_Z"]),
                             Fraction(previous["rho_star"]))
            self.assertEqual(Fraction(new["rho_FULL_POINT_OR_LINE_STAR_original_Z"]),
                             Fraction(3,2)*Fraction(previous["rho_star"]))

    def test_invalid_graph_constants_or_fake_original_stars_fail_closed(self):
        for C,c in ((1,Fraction(1)),(Fraction(1),1),
                    (Fraction(0),Fraction(1)),(Fraction(1),Fraction(0)),
                    (Fraction(1),Fraction(2)),(Fraction(1,2),Fraction(1))):
            with self.assertRaises(ValueError):
                star_all_h(C,c)
        with self.assertRaises(ValueError):
            true_full_source_star_case(3,"lex","point",(0,))
        with self.assertRaises(ValueError):
            true_full_source_star_case(2,"lex","something",(0,))
        with self.assertRaises(ValueError):
            true_full_source_star_case(2,"lex","point",(0,0))
        with self.assertRaises(ValueError):
            true_full_source_star_case(1,"lex","line",(100,))

    def test_original_ROOT_issue_scientific_governance_not_falsely_promoted(self):
        x=self.x
        self.assertEqual(x["schema"],SCHEMA)
        self.assertEqual(x["root_230_status"],"OPEN_WITH_FORMAL_BLOCKER")
        self.assertFalse(x["root_ASET_exponent_proved"])
        self.assertFalse(x["root_Branch_A_independently_accepted"])
        self.assertFalse(x["graph_C6_SS6_actual_numeric_constants_known"])
        self.assertTrue(x["original_root_target_seven_class_S_s_not_R3"])
        self.assertTrue(x["new_original_POINT_LINE_STAR_mask_exact_all_h"])
        self.assertTrue(x["new_original_structured_Z_rho_exact_one_point_five_x"])


if __name__=="__main__":
    unittest.main()
