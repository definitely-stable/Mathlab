"""Fail-closed D6-A ORIGINAL same-map diagnostic tests."""
import unittest
from fractions import Fraction

from hyp105_issue230_d6_joint_blocking_audit import (
    finite_frontier, joint_record, report,
)
from hyp105_issue230_d5_retained_energy import true_spread_global_model


class JointBlockingD6Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows=report()["finite_complete_same_original_labelings"]
        cls.byname={r["scheme"]:r for r in cls.rows}

    def test_joint_original_sixteen_atoms_are_disjoint_and_complete(self):
        self.assertEqual(len(self.rows),6)
        for r in self.rows:
            with self.subTest(r=r["scheme"]):
                self.assertTrue(r["complete_same_original_global_pair_maps"])
                self.assertEqual(len(r["sixteen_exact_blocking_atoms"]),16)
                self.assertEqual(sum(r["sixteen_exact_blocking_atoms"][1:]),
                                 r["C_joint_blocked_proper_P3"])
                self.assertEqual(r["E_endpoint_bad_proper_P3"]
                                 +r["I_safe_endpoint_internal_only_proper_P3"],
                                 r["C_joint_blocked_proper_P3"])
                self.assertEqual(
                    r["proper_P3"],
                    r["original_endpoint_missing"]+
                    r["original_endpoint_incident"]+
                    r["C_joint_blocked_proper_P3"]+
                    2*r["BB_sync_accepted_sixsets"])
                self.assertTrue(r["complete_W32_independent_endpoint_first_path_oracle"])
                self.assertFalse(r["all_h_universal_seven_S_lower_PROVED"])
                self.assertFalse(r["all_h_C_compensation_PROVED"])
                self.assertFalse(r["infinite_small_S_counterexample_PROVED"])

    def test_complete_W32_known_energy_and_full_positive_GF5_seven(self):
        energy={"lex":2977,"reverse":2709,"S68":3289,"S72":3303}
        for scheme,w in energy.items():
            r=self.byname["W32-"+scheme]
            self.assertEqual(r["D2_exact_bad_endpoint_energy_W"],w)
            self.assertEqual(sum(r["full_seven_counts"].values()),r["full_seven_S"])
            self.assertGreaterEqual(r["full_seven_counts"]["B/B-overlap"],
                                    r["BB_sync_accepted_sixsets"])
            self.assertGreaterEqual(r["full_seven_S"],r["BB_sync_accepted_sixsets"])
            self.assertGreater(r["seven_GF5_risk_necessary_numerator"],0)
            self.assertEqual(Fraction(r["finite_ZERO_remainder_eta_ceiling_at_Lambda1"])
                             -Fraction(r["finite_ZERO_remainder_eta_ceiling_at_Lambda0"]),
                             Fraction(r["full_seven_S"],2**6))
        self.assertEqual(self.byname["W32-S68"]["full_seven_S"],68)

    def test_D5_true_symplectic_spread_W34_energies_and_NO_fake_full_S(self):
        for mode,w in (("balanced",127932),("reverse",131936)):
            r=self.byname["W34-D5-spread-"+mode]
            self.assertEqual(r["D2_exact_bad_endpoint_energy_W"],w)
            self.assertIsNone(r["full_seven_S"])
            self.assertIsNone(r["seven_GF5_risk_necessary_numerator"])
            self.assertIsNone(r["finite_ZERO_remainder_eta_ceiling_at_Lambda0"])
            self.assertGreaterEqual(r["C_joint_blocked_proper_P3"],0)
        self.assertNotEqual(
            self.byname["W34-D5-spread-balanced"]["D2_exact_bad_endpoint_energy_W"],
            self.byname["W34-D5-spread-reverse"]["D2_exact_bad_endpoint_energy_W"])

    def test_exact_finite_zero_remainder_frontier_scope(self):
        self.assertEqual(finite_frontier(2,606,68,0),Fraction(16)-Fraction(606,64))
        self.assertEqual(finite_frontier(2,606,68,1),Fraction(16)-Fraction(538,64))
        for kwargs in (
            dict(s=4,blocked=1,seven=None),
            dict(s=3,blocked=1,seven=0),
            dict(s=4,blocked=-1,seven=0),
            dict(s=4,blocked=1,seven=-1),
            dict(s=4,blocked=1,seven=0,lam=-1),
        ):
            with self.assertRaises(ValueError):
                finite_frontier(**kwargs)

    def test_pinned_D6_same_map_real_original_coupling(self):
        # Exact hosted D6-A Contract observed all six complete SAME-map rows.
        pinned={
            "W32-lex":(2977,786,156,942,2,259),
            "W32-reverse":(2709,676,222,898,0,169),
            "W32-S68":(3289,544,62,606,0,68),
            "W32-S72":(3303,600,58,658,0,72),
            "W34-D5-spread-balanced":(127932,35190,17570,52760,7649,None),
            "W34-D5-spread-reverse":(131936,36014,17224,53238,7479,None),
        }
        for name,expected in pinned.items():
            row=self.byname[name]
            actual=tuple(row[k] for k in (
                "D2_exact_bad_endpoint_energy_W",
                "E_endpoint_bad_proper_P3",
                "I_safe_endpoint_internal_only_proper_P3",
                "C_joint_blocked_proper_P3",
                "BB_sync_accepted_sixsets",
                "full_seven_S",
            ))
            self.assertEqual(actual,expected)
        # EXACT finite W32 order inversion disproves any naive strictly
        # monotone S(W) rule. It is NOT an infinite-s asymptotic falsifier.
        lex=self.byname["W32-lex"]
        s68=self.byname["W32-S68"]
        self.assertGreater(s68["D2_exact_bad_endpoint_energy_W"],
                           lex["D2_exact_bad_endpoint_energy_W"])
        self.assertLess(s68["full_seven_S"],lex["full_seven_S"])
        self.assertLess(s68["C_joint_blocked_proper_P3"],
                        lex["C_joint_blocked_proper_P3"])

    def test_reject_mislabeled_full_W34_seven_census(self):
        model,_,_,_=true_spread_global_model(2)
        with self.assertRaises(ValueError):
            joint_record(model,"invalid-full-W34",compute_full_seven=True)


if __name__=="__main__":
    unittest.main()
