"""AA4-ROOTGATE: independently falsify each ORIGINAL root heavy/low proof gate."""
import unittest
from fractions import Fraction
from math import comb

from hyp105_original_root_proof_dag_gate import (
    HEAVY_GF5_WEIGHT, LOW_GF5_WEIGHT, STATUS,
    at_dyadic_order, exact_conditional_ledger, gate_with_mutation,
    original_envelope, original_root_gate_report,
)


class TestOriginalRootProofDag(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.z=exact_conditional_ledger(Fraction(1),Fraction(1))

    def test_every_exact_symbolic_full_original_gate_closes_for_three_formal_constants(self):
        for C,c in ((Fraction(1),Fraction(1)),
                    (Fraction(2),Fraction(1,5)),
                    (Fraction(7,3),Fraction(1,17))):
            with self.subTest(C=C,c=c):
                z=exact_conditional_ledger(C,c)
                self.assertTrue(all(z["all_checks"].values()))
                self.assertFalse(z["root_230_mathematically_accepted"])
                self.assertTrue(at_dyadic_order(z,z["h0"])["all_gates_closed"])
                self.assertTrue(at_dyadic_order(z,z["h0"]+1)["all_gates_closed"])
                self.assertFalse(at_dyadic_order(z,z["h0"]-1)["all_gates_closed"])

    def test_original_genuine_source_envelope_at_multiple_dyadic_orders(self):
        for h in (6,7,8,10,14):
            with self.subTest(h=h):
                z=original_envelope(1<<h)
                self.assertTrue(all(z["checks"].values()))
                self.assertEqual(z["N"],(z["s"]+1)*z["V"])
                self.assertEqual(z["physical_corners"],z["alphabet"]**2)
                self.assertLess(comb(z["alphabet"]-1,2),z["V"])
                self.assertGreaterEqual(comb(z["alphabet"],2),z["V"])
                self.assertLessEqual(2*z["source_collision_book"],3*z["s"]**4)

    def test_original_heavy_source_Caro_Wei_and_exact_SS6_threshold(self):
        z=self.z
        self.assertEqual(z["K"],64)
        self.assertEqual(z["T"],2**64)
        self.assertEqual(z["heavy_source_independent_fraction"],Fraction(1,2**15))
        self.assertEqual(z["heavy_ordinary_density_coefficient"],Fraction(1,2**20))
        self.assertEqual(z["heavy_graph_SS6_threshold_lhs"],
                         z["heavy_graph_SS6_threshold_rhs"])
        self.assertEqual(z["heavy_D6_floor_per_s6"],Fraction(1,2**120))
        self.assertTrue(z["all_checks"]["SS6_actual_C0_threshold_closed"])

    def test_original_low_source_budget_three_errors_plus_deleted_mask(self):
        z=self.z
        self.assertGreaterEqual(z["low_original_retained_core_fraction"],Fraction(3,4))
        self.assertEqual(z["low_original_W3_floor_per_s6"],Fraction(27,16))
        self.assertEqual(z["low_original_deleted_mask_per_s6"],1)
        self.assertEqual(z["low_BBo_floor_per_s6"],Fraction(5,32))
        s=1<<z["h0"]
        self.assertGreaterEqual(s,672*z["T"])
        self.assertGreaterEqual(s,(8*z["E"])**2)
        self.assertGreaterEqual(s,(8*z["D"])**8)
        self.assertEqual(12*z["rho"]*z["q3"]**2*z["L6"],1)

    def test_NEW_sharper_GLOBAL_uniform_GF5_weighted_branch_minimum(self):
        z=self.z
        self.assertEqual(HEAVY_GF5_WEIGHT,54162)
        self.assertEqual(LOW_GF5_WEIGHT,53526)
        self.assertEqual(z["heavy_risk_numerator_per_s6"],
                         Fraction(54162,2**120))
        self.assertEqual(z["low_risk_numerator_per_s6"],
                         Fraction(53526*5,32))
        self.assertEqual(z["global_risk_numerator_per_s6"],
                         Fraction(54162,2**120))
        self.assertGreater(z["global_risk_numerator_per_s6"],
                           LOW_GF5_WEIGHT*z["delta"])
        self.assertEqual(Fraction(54162,53526),
                         Fraction(9027,8921))

    def test_previous_full_original_joint_core_ledger_agrees_not_reimplemented(self):
        # This separate test, not the main proof engine, compares frozen
        # parent's independent algebra. Failure detects numerical drift.
        from hyp105_original_joint_zcore_gate import uniform_original_joint_gate
        for C,c in ((Fraction(1),Fraction(1)),
                    (Fraction(2),Fraction(1,5))):
            parent=uniform_original_joint_gate(C,c)
            child=exact_conditional_ledger(C,c)
            for field in ("T","K","L6","L4","q2","q3","B0","E","D",
                          "rho","delta","s0","h0"):
                with self.subTest(field=field,C=C):
                    self.assertEqual(child[field],parent[field])
            self.assertEqual(child["low_BBo_floor_per_s6"],parent["lowtail_BBo_coefficient"])

    def test_red_team_reject_invalid_C6_constant_without_false_claim_of_counterexample(self):
        z=self.z
        bad=gate_with_mutation(Fraction(1),Fraction(1),
                               required_T=z["T"]-1)
        self.assertFalse(bad["all_valid"])
        self.assertFalse(bad["gates"]["heavy_external_SS6"]["valid"])
        self.assertTrue(bad["counterfactual_only"])

    def test_red_team_reject_increased_original_Z_radius_and_low_mask(self):
        bad=gate_with_mutation(Fraction(1),Fraction(1),
                               allowed_rho=self.z["rho"]*2)
        self.assertFalse(bad["all_valid"])
        self.assertFalse(bad["gates"]["low_proper_path_mask"]["valid"])
        self.assertTrue(bad["gates"]["low_original_density"]["valid"])

    def test_red_team_reject_source_GF5_sign_count_substitution(self):
        a=gate_with_mutation(Fraction(1),Fraction(1),heavy_GF5=53526)
        b=gate_with_mutation(Fraction(1),Fraction(1),low_GF5=51750)
        self.assertFalse(a["all_valid"])
        self.assertFalse(b["all_valid"])
        self.assertFalse(a["gates"]["GF5_original_source_nonzero"]["valid"])
        self.assertFalse(b["gates"]["GF5_original_source_nonzero"]["valid"])

    def test_reject_unjustified_graph_constants_and_nondyadic_source(self):
        for C,c in ((1,Fraction(1)),(Fraction(1),1),
                    (Fraction(0),Fraction(1)),
                    (Fraction(1),Fraction(0)),
                    (Fraction(1),Fraction(2)),
                    (Fraction(1),Fraction(2,1)+Fraction(1,4))):
            with self.subTest(C=C,c=c), self.assertRaises(ValueError):
                exact_conditional_ledger(C,c)
        for s in (1,63,65,96,True):
            with self.subTest(s=s),self.assertRaises(ValueError):
                original_envelope(s)
        for h in (0,-1,1.5,True):
            with self.subTest(h=h),self.assertRaises(ValueError):
                at_dyadic_order(self.z,h)
        with self.assertRaises(ValueError):
            gate_with_mutation(Fraction(1),Fraction(1),
                               allowed_rho=0.01)

    def test_all_durable_DAG_provenance_and_no_root_acceptance(self):
        r=original_root_gate_report()
        self.assertEqual(r["schema"],"mathlab.hyp105.original-root-proof-dag.v1")
        self.assertEqual(r["root_230_status"],STATUS)
        self.assertFalse(r["root_universally_accepted"])
        self.assertFalse(r["root_ASET_exponent_proved"])
        self.assertTrue(r["conditional_arithmetic_independently_closed"])
        self.assertTrue(r["original_six_ID_source_lifts_independent_review_pending"])
        self.assertEqual(r["uniform_old_class_weight"],53526)
        self.assertEqual(r["uniform_new_branch_weight"],54162)
        self.assertEqual(r["weighted_improvement_ratio"],"9027/8921")
        self.assertEqual(len(r["three_formal_rational_graph_theorem_ledgers"]),3)
        self.assertEqual(len(r["actual_original_source_envelopes"]),4)
        self.assertEqual(len(r["red_team_mutations"]),4)
        self.assertTrue(all(p["all_conditionals_hold"]
                            and not p["external_constants_numerically_verified"]
                            for p in r["three_formal_rational_graph_theorem_ledgers"]))


if __name__=="__main__":
    unittest.main()
