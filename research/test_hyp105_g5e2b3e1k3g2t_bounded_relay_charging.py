"""HYP-105 K3-G2-T: two independent flow solvers and geometric cut gates."""
from fractions import Fraction
import unittest

from hyp105_g5e2b3e1k3g2t_bounded_relay_charging import (
    _certificate, exact_bounded_relay_gate, report,
)


class K3G2TBoundedRelayTests(unittest.TestCase):
    def test_single_original_two_hop_line_threshold(self):
        demand=[2,0,0]
        own=[0,2,0]
        dual=[0,0,0]
        original=[(0,),(0,),()]
        z=exact_bounded_relay_gate(
            demand,own,dual,original,unit_denominator=1)
        self.assertEqual(z["zero_relay"]["deficit"],2)
        self.assertEqual(z["one_physical_credit_per_line"]["deficit"],1)
        self.assertEqual(z["minimal_uniform_relay_scaled"],2)
        self.assertEqual(z["minimal_uniform_relay_physical_units"],[2,1])
        self.assertEqual(z["minimal_minus_one_certificate"]["deficit"],1)
        self.assertTrue(z["minimal_relay_certificate"]["feasible"])
        self.assertEqual(z["minimal_relay_certificate"]["relay_line_used"],
                         [2,0,0])

    def test_shared_relay_gate_must_not_be_used_twice(self):
        demand=[2,0,2]
        own=[0,4,0]
        dual=[0,0,0]
        original=[(0,),(0,),(0,)]
        low=_certificate(demand,own,dual,original,[3,0,0])
        high=_certificate(demand,own,dual,original,[4,0,0])
        self.assertEqual((low["flow"],low["deficit"]),(3,1))
        self.assertEqual((high["flow"],high["deficit"]),(4,0))
        self.assertEqual(low["relay_line_used"],[3,0,0])
        self.assertEqual(high["relay_line_used"],[4,0,0])

    def test_BA_positive_credit_consumed_once_even_with_large_relay(self):
        demand=[2,2,0]
        own=[0,0,3]
        dual=[0,0,0]
        original=[(0,),(0,),(0,)]
        x=_certificate(demand,own,dual,original,[10,0,0])
        self.assertEqual((x["flow"],x["deficit"]),(3,1))
        self.assertEqual(x["independent_flow"],3)

    def test_direct_original_dual_credit_preserved_at_kappa_zero(self):
        d=[2,0,0]
        own=[0,0,0]
        dual=[2,0,0]
        gq=[(0,),(0,),()]
        x=_certificate(d,own,dual,gq,[0]*3)
        self.assertEqual((x["flow"],x["deficit"]),(2,0))
        self.assertEqual(x["relay_line_used"],[0,0,0])

    def test_Hall_cut_is_exact_on_bottleneck_synthetic(self):
        d=[2,0,0]
        a=[0,2,0]
        b=[0,0,0]
        inc=[(0,),(0,),()]
        x=_certificate(d,a,b,inc,[1,0,0])
        self.assertEqual(x["mincut_demand_points"],[0])
        self.assertEqual(x["mincut_incident_original_lines"],[0])
        self.assertEqual(x["mincut_demand"],2)
        self.assertEqual(x["deficit"],1)
        self.assertEqual(
            x["mincut_demand"]-x["mincut_BA_credit"]-
            x["mincut_AB_credit"]-x["mincut_relay_cut_capacity"],1)

    def test_bad_balanced_origins_rejected(self):
        with self.assertRaises(ValueError):
            _certificate([1,0],[1],[0,0],[(0,),()], [1,0])
        with self.assertRaises(ValueError):
            _certificate([1],[0],[0],[(1,)], [1])
        with self.assertRaises(ValueError):
            _certificate([1],[0],[0],[(0,0)], [1])
        with self.assertRaises(ValueError):
            _certificate([1],[0],[0],[(0,)], [-1])
        with self.assertRaises(ValueError):
            exact_bounded_relay_gate([1],[0],[0],[(0,)],unit_denominator=0)

    def test_real_complete_original_and_true_dual_W32_seal(self):
        r=report()
        self.assertEqual(r["slice"],"HYP-105-E1-K3-G2-T")
        cases=r["genuine_original_and_dual_complete_W32_cases"]
        self.assertEqual([x["name"] for x in cases],["lex","hardest-M"])
        for x in cases:
            self.assertEqual(
                x["zero_relay"]["deficit"],x["parent_S_Hall_shortfall"])
            self.assertEqual(
                x["zero_relay"]["flow"],
                x["zero_relay"]["independent_flow"])
            self.assertEqual(
                x["one_physical_credit_per_line"]["flow"],
                x["one_physical_credit_per_line"]["independent_flow"])
            self.assertEqual(
                x["zero_relay"]["total_demand"],
                x["one_physical_credit_per_line"]["total_demand"])
            self.assertTrue(
                x["all_32768_old_Hall_cuts_independently_matched_at_kappa_zero"])
            self.assertFalse(x["all_h_P2_proved"])
            self.assertFalse(x["relay_budget_derived_from_GQ_theorem"])
            self.assertFalse(x["finite_all_label_W32_proved"])
            if x["minimal_uniform_relay_scaled"] is not None:
                self.assertTrue(x["minimal_relay_certificate"]["feasible"])
                m=x["minimal_uniform_relay_scaled"]
                if m:
                    self.assertEqual(
                        x["minimal_minus_one_certificate"]["deficit"]>0,True)
                self.assertLessEqual(
                    x["minimal_uniform_relay_scaled"],
                    x["one_physical_credit_per_line"]["total_demand"])
        hard=cases[1]
        self.assertEqual(hard["parent_S_original_point_cut"],
                         [1,2,3,5,8,13,14])
        self.assertEqual(hard["zero_relay"]["deficit"],530)
        self.assertEqual(hard["zero_relay"]["total_demand"],9968)
        self.assertEqual(hard["scalar_P2_margin"],[757,143])
        self.assertEqual((hard["true_BA"],hard["true_dual_AB"]),(36,39))
        self.assertEqual(hard["joint_C5"],[-2473,462])
        self.assertEqual(hard["joint_C6"],[-26,7])
        self.assertEqual(cases[0]["zero_relay"]["deficit"],0)


if __name__=="__main__":
    unittest.main()
