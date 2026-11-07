"""Independent proof-obligation red team for HYP-105 original Branch A theorem."""
from fractions import Fraction
from math import comb
import unittest

from hyp105_branch_a_standalone_source_proof import (
    SCHEMA, ROOT_STATE, R, K, PAL, D6_WEIGHT, BBO_ALL_WEIGHT,
    BBO_PRODUCED_WEIGHT, SOURCE_MOTIF_CLASSES,
    exact_ceil, sqrt_ceil, original_all_order_theorem,
    original_adversarial_branch_witness, genuine_source_falsifier,
    genuine_original_d6_seed_cycle, canonical_report,
)


class TestBranchAStandaloneOriginalSource(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.x=canonical_report()

    def test_exact_formal_external_graph_constant_inputs_and_all_h_threshold(self):
        cases=((Fraction(1),Fraction(1),810),
               (Fraction(2),Fraction(1,5),840),
               (Fraction(7,3),Fraction(1,17),847))
        for C,c,h in cases:
            with self.subTest(C=C,c=c):
                z=original_all_order_theorem(C,c)
                self.assertEqual(z["h0"],h)
                self.assertEqual(z["T"],exact_ceil(Fraction(17*R**3,2)*C**3))
                self.assertEqual(Fraction(z["delta_original_seven_motif_S_s"]),
                                 c/Fraction(R**6))
                self.assertTrue(all(z["quantified_30_original_math_gates"].values()))
                self.assertEqual(len(z["quantified_30_original_math_gates"]),31)
                self.assertFalse(z["formal_graph_constant_values_are_CERTIFIED_PUBLISHED"])

    def test_root_issue_original_seven_class_S_is_not_GF5_signed_event_count(self):
        cls=SOURCE_MOTIF_CLASSES
        self.assertEqual(cls,("D6","U_B_left","U_B_right","U_CA",
                              "U_CB","U_BB_overlap","U_BB_disjoint"))
        self.assertEqual(len(set(cls)),7)
        self.assertEqual(BBO_ALL_WEIGHT,53526)
        self.assertEqual(BBO_PRODUCED_WEIGHT,53838)
        self.assertEqual(D6_WEIGHT,54162)
        self.assertEqual(PAL,51)
        self.assertNotEqual(D6_WEIGHT,BBO_PRODUCED_WEIGHT)
        self.assertGreaterEqual(
            Fraction(D6_WEIGHT,PAL**6),Fraction(BBO_PRODUCED_WEIGHT,PAL**6))

    def test_HEAVY_SOURCE_direct_original_sixset_S_and_R3_floor(self):
        z=original_all_order_theorem(Fraction(1),Fraction(1))
        delta=Fraction(z["delta_original_seven_motif_S_s"])
        v=original_adversarial_branch_witness(z,delta,Fraction(0))
        self.assertEqual(v["branch"],"HEAVY_OR_LOW_HIGH_D6")
        self.assertTrue(v["branch_premise_satisfied"])
        self.assertTrue(v["implication_valid"])
        self.assertTrue(v["universal_original_S_s_GEQ_delta"])
        self.assertTrue(v["universal_R3_GEQ_required_floor"])
        self.assertEqual(Fraction(v["R3_lower_two_original_signed_sixset_families"]),
                         D6_WEIGHT*delta/PAL**6)

    def test_LOW_TRUE_ORIGINAL_produced_BBo_source_subfamily_only(self):
        for C,c in ((Fraction(1),Fraction(1)),
                    (Fraction(2),Fraction(1,5)),
                    (Fraction(7,3),Fraction(1,17))):
            z=original_all_order_theorem(C,c)
            delta=Fraction(z["delta_original_seven_motif_S_s"])
            B=Fraction(z["low_BBo_produced_at_max_deletion_floor"])
            for d6 in (Fraction(0),delta/4,delta/2,delta*Fraction(3,4)):
                r=original_adversarial_branch_witness(z,d6,B)
                self.assertTrue(r["branch_premise_satisfied"])
                self.assertEqual(r["branch"],"LOW_SMALL_D6")
                self.assertTrue(r["universal_original_S_s_GEQ_delta"])
                self.assertTrue(r["universal_R3_GEQ_required_floor"])
                self.assertTrue(r["implication_valid"])
            self.assertEqual(B,Fraction(D6_WEIGHT,BBO_PRODUCED_WEIGHT)*delta)

    def test_unqualified_LOW_with_no_source_BBo_NOT_wrongly_promoted(self):
        z=original_all_order_theorem(Fraction(1),Fraction(1))
        delta=Fraction(z["delta_original_seven_motif_S_s"])
        r=original_adversarial_branch_witness(z,Fraction(0),Fraction(0))
        self.assertFalse(r["branch_premise_satisfied"])
        self.assertFalse(r["universal_original_S_s_GEQ_delta"])
        self.assertFalse(r["universal_R3_GEQ_required_floor"])
        self.assertTrue(r["implication_valid"])
        v=original_adversarial_branch_witness(z,Fraction(0),delta)
        # delta BBo source motifs alone meet original S_s target, but
        # do NOT meet stronger GF5 HEAVY risk coefficient because
        # 53838<54162. Full LOW theorem supplies greater BBo floor.
        self.assertTrue(v["universal_original_S_s_GEQ_delta"])
        self.assertFalse(v["universal_R3_GEQ_required_floor"])
        self.assertFalse(v["branch_premise_satisfied"])

    def test_exact_absolute_existence_quantifier_same_held_C0_c0_all_s(self):
        z=original_all_order_theorem(Fraction(2),Fraction(1,5))
        h=z["h0"]
        self.assertGreaterEqual(h,64)
        self.assertTrue((1<<h)>=z["s0"]>(1<<(h-1)))
        self.assertEqual(z["h0"],840)
        self.assertGreater(Fraction(z["S_s_universal_positive_motif_floor"]),0)
        self.assertEqual(Fraction(z["R3_full_additive_original_GF5_risk_floor"]),
                         D6_WEIGHT*Fraction(z["S_s_universal_positive_motif_floor"])/PAL**6)
        self.assertEqual(z["HEAVY_original_source_D6_risk_floor"],
                         z["LOW_original_source_BBo_risk_floor"])
        self.assertGreater(Fraction(z["deletion_improvement_ratio"]),Fraction(3,2))

    def test_new_rho_does_not_break_previous_original_heavy_or_low_gates(self):
        for row in self.x["full_original_source_formal_quantified_theorem_probes"]:
            rho=Fraction(row["rho_star"])
            self.assertLess(rho,Fraction(1,32))
            self.assertLess(rho,Fraction(3,64))
            self.assertGreater(rho,Fraction(row["rho_old_740"])*Fraction(3,2))
            q3=row["q3"];L6=row["L6"]
            self.assertEqual(12*q3*q3*L6*rho,Fraction(row["t_star"])**2)
            self.assertLess(Fraction(row["t_star"]),Fraction(119,24))

    def test_true_original_five_source_fixtures_fullGQ_Z_and_source_srg(self):
        a=self.x["actual_original_symplectic_source_falsifiers"]
        self.assertEqual(len(a),5)
        self.assertEqual([(z["s"],z["scheme"]) for z in a][:4],
                         [(2,"lex"),(2,"reverse-line"),
                          (4,"lex"),(4,"reverse-line")])
        for z in a:
            with self.subTest(s=z["s"],scheme=z["scheme"]):
                s=z["s"]
                V=(s+1)*(s*s+1);N=(s+1)*V
                self.assertEqual(z["original_incidence_IDs_total"],N)
                self.assertGreater(z["ORIGINAL_adversarial_Z_deleted_IDs"],0)
                self.assertEqual(z["exact_original_full_GQ_offincident_projections"],
                                 V*(V-s-1))
                self.assertEqual(z["each_original_flag_projection_exposure_per_role"],s*s)
                self.assertEqual(z["true_original_full_source_J_edges"],
                                 z["true_original_point_collinear_f_label_collisions"]+
                                 z["true_original_line_collinear_g_label_collisions"])
                self.assertLessEqual(z["true_original_point_collinear_f_label_collisions"],
                                     (s*s+1)*(s*s+comb(V+1,2)-2))
                self.assertEqual(z["actual_physical_full_original_two_diagonal_edges"],2*N)
                self.assertLessEqual(
                    z["actual_ORIGINAL_Q_edges_deleted_at_most_2Z"],
                    2*z["ORIGINAL_adversarial_Z_deleted_IDs"])
                self.assertEqual(z["true_CORE_physical_edges"],
                                 2*z["true_ORIGINAL_paired_CORE_IDs"])
                self.assertGreater(z["true_ORIGINAL_paired_CORE_IDs"],0)
                self.assertLessEqual(z["true_CORE_physical_max_degree"],4*s)

    def test_true_original_BBo_produced_from_physical_paths_exact_0or2(self):
        a=self.x["actual_original_symplectic_source_falsifiers"]
        positive=0
        for z in a:
            b=z["real_produced_BBo_distinct_original_six_ID_sets"]
            n=z["real_produced_BBo_accepted_directed_3paths"]
            self.assertEqual(n,2*b)
            self.assertGreaterEqual(z["actual_proper_directed_physical_P3"],n)
            self.assertTrue(z["source_produced_BBo_exact_two_directed_reversal"])
            positive+=b
        self.assertGreater(positive,0)

    def test_independent_actual_original_W34_heavy_D6_physical_C6_seeds(self):
        z=self.x["actual_original_W34_physical_C6_to_D6_heavy_seed_falsifiers"]
        self.assertEqual(len(z),3)
        self.assertEqual([x["scheme"] for x in z],
                         ["lex","lex","reverse-line"])
        for x in z:
            self.assertEqual(x["physical_original_seed_diagonals"],12)
            self.assertEqual(x["physical_coordinate_proper_C6_seed"],1)
            self.assertEqual(x["all_physical_simple_C6_seed"],1)
            self.assertTrue(x["source_cycle_six_ORIGINAL_distinct_owner_IDs"])
            self.assertTrue(x["same_original_source_owner_order_in_two_physical_factors"])
        with self.assertRaises(ValueError):
            genuine_original_d6_seed_cycle("lex",(111,111,203,224,383,412))

    def test_new_root_quantitative_root_ledger_agrees_with_frozen_PARENT_ONLY_in_TESTS(self):
        # Main new module imports NONE of the old proof/flow/energy modules.
        from hyp105_original_global_rho_pareto_referee import optimal_source_rho_frontier
        from hyp105_original_risk_additive_ie_rootbridge import root_symbolic_bridge
        for C,c in ((Fraction(1),Fraction(1)),
                    (Fraction(2),Fraction(1,5)),
                    (Fraction(7,3),Fraction(1,17))):
            old=optimal_source_rho_frontier(C,c)
            older=root_symbolic_bridge(C,c)
            fresh=original_all_order_theorem(C,c)
            for key in ("T","q2","q3","L6","L4","B0","E","D","s0","h0"):
                self.assertEqual(fresh[key],old[key])
                self.assertEqual(fresh[key],older[key])
            self.assertEqual(Fraction(fresh["rho_star"]),old["rho_star"])
            self.assertEqual(Fraction(fresh["delta_original_seven_motif_S_s"]),
                             old["delta"])

    def test_false_external_graph_values_and_fake_original_flags_fail_closed(self):
        invalid=((1,Fraction(1)),(Fraction(1),1),
                 (Fraction(0),Fraction(1)),(Fraction(1),Fraction(0)),
                 (Fraction(1),Fraction(2)),(Fraction(1,2),Fraction(1)))
        for C,c in invalid:
            with self.assertRaises(ValueError):
                original_all_order_theorem(C,c)
        with self.assertRaises(ValueError):
            sqrt_ceil(-2)
        with self.assertRaises(ValueError):
            exact_ceil(1)
        with self.assertRaises(ValueError):
            genuine_source_falsifier(3,"lex",(0,))
        with self.assertRaises(ValueError):
            genuine_source_falsifier(1,"lex",(0,0))
        with self.assertRaises(ValueError):
            genuine_source_falsifier(1,"lex",(90,))
        z=original_all_order_theorem(Fraction(1),Fraction(1))
        with self.assertRaises(ValueError):
            original_adversarial_branch_witness(z,0,Fraction(0))
        with self.assertRaises(ValueError):
            original_adversarial_branch_witness(z,Fraction(-1),Fraction(1))

    def test_root_accepted_facts_do_not_promote_undischarged_governance(self):
        z=self.x
        self.assertEqual(z["schema"],SCHEMA)
        self.assertEqual(z["root_230_status"],ROOT_STATE)
        self.assertTrue(z["root_Branch_A_mathematical_implication_is_explicit_all_h"])
        self.assertTrue(z["root_S_s_is_original_sixID_MOTIF_sum_not_signed_event_count"])
        self.assertTrue(z["all_h_candidate_is_absolute_positive_existence_not_explicit_h"])
        self.assertTrue(z["no_published_numeric_graph_supersaturation_constants_assumed"])
        self.assertFalse(z["root_full_scientific_governance_acceptance"])
        self.assertFalse(z["root_ASET_exponent_proved"])
        self.assertEqual(len(z["full_original_source_formal_quantified_theorem_probes"]),3)


if __name__=="__main__":
    unittest.main()
