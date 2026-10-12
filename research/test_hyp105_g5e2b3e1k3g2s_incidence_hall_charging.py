"""K3-G2-S: two independent EXACT algorithms for finite GQ Hall charging."""
from fractions import Fraction
import unittest

from hyp105_g5e2b3e1k3g2s_incidence_hall_charging import (
    exact_integer_maxflow, exhaustive_hall_deficit,
    incidence_charging_gate, report,
)


def zeros():
    return [0]*15


class K3G2SIncidenceHallTests(unittest.TestCase):
    def test_full_hall_and_flow_identical_on_feasible_small_geometry(self):
        demand=zeros()
        own=zeros()
        dual=zeros()
        incidence=[frozenset() for _ in range(15)]
        demand[0]=2
        own[0]=1
        dual[7]=1
        incidence[0]=frozenset({7})
        flow,cut,shortfall=exact_integer_maxflow(demand,own,dual,incidence)
        hall,worst=exhaustive_hall_deficit(demand,own,dual,incidence)
        self.assertEqual((flow,shortfall,hall),(2,0,0))

    def test_shared_dual_capacity_is_not_reused(self):
        demand=zeros()
        own=zeros()
        dual=zeros()
        incidence=[frozenset() for _ in range(15)]
        demand[0]=demand[1]=2
        dual[4]=3
        incidence[0]=incidence[1]=frozenset({4})
        flow,cut,shortfall=exact_integer_maxflow(demand,own,dual,incidence)
        hall,worst=exhaustive_hall_deficit(demand,own,dual,incidence)
        self.assertEqual((flow,shortfall,hall),(3,1,1))
        self.assertEqual(set(worst),{0,1})

    def test_hall_obstruction_can_coexist_with_positive_scalar_slack(self):
        demand=zeros()
        own=zeros()
        dual=zeros()
        incidence=[frozenset() for _ in range(15)]
        demand[0]=2
        dual[1]=3
        incidence[0]=frozenset({0})  # positive, but NOT incident credit
        flow,cut,shortfall=exact_integer_maxflow(demand,own,dual,incidence)
        hall,worst=exhaustive_hall_deficit(demand,own,dual,incidence)
        self.assertEqual((flow,shortfall,hall),(0,2,2))
        self.assertEqual(worst,(0,))
        self.assertGreater(sum(dual)-sum(demand),0)

    def test_malformed_capacities_fail_closed(self):
        with self.assertRaises(ValueError):
            exact_integer_maxflow([1]*14,zeros(),zeros(),
                                  [frozenset()]*15)
        with self.assertRaises(ValueError):
            exact_integer_maxflow([-1]+[0]*14,zeros(),zeros(),
                                  [frozenset()]*15)
        with self.assertRaises(ValueError):
            exact_integer_maxflow(zeros(),zeros(),zeros(),
                                  [frozenset({15})]+[frozenset()]*14)
        with self.assertRaises(ValueError):
            incidence_charging_gate(
                {"mass":zeros(),"hits":zeros(),"target_hits":0,
                 "source_mass":0},
                {"hits":zeros(),"target_hits":0},
                [frozenset()]*15, density=Fraction(1,1))

    def test_true_full_original_and_dual_frozen_W32_regressions(self):
        r=report()
        self.assertEqual(r["slice"],"HYP-105-E1-K3-G2-S")
        cases=r["original_and_true_dual_complete_W32_cases"]
        self.assertEqual([x["name"] for x in cases],["lex","hardest-M"])
        for x in cases:
            self.assertEqual(x["full_hall_subsets_checked"],32768)
            self.assertEqual(x["original_GQ_incidence_edges"],45)
            self.assertEqual(x["density"],[2,143])
            self.assertEqual(x["scaled_denominator"],143)
            self.assertEqual(x["hall_shortfall"],
                             x["independent_exhaustive_hall_max_deficit"])
            self.assertEqual(x["total_demand"]-x["exact_integer_maxflow"],
                             x["hall_shortfall"])
            self.assertEqual(x["finite_model_feasible"],
                             x["hall_shortfall"]==0)
            self.assertEqual(
                sum(x["original_GQ_point_anchor_permanent_one"])+2*
                sum(x["original_GQ_point_anchor_permanent_two"]),
                x["original_BA_source_mass"])
            self.assertEqual(
                x["total_demand"],2*x["original_BA_source_mass"])
            self.assertEqual(
                sum(x["actual_original_BA_own_target_capacity"]),
                143*x["original_BA_target_hits"])
            self.assertEqual(
                sum(x["actual_original_dual_AB_target_capacity"]),
                143*x["true_original_dual_AB_target_hits"])
            self.assertFalse(x["all_h_P2_proved"])
            self.assertFalse(x["finite_all_label_W32_proved"])
        hard=cases[1]
        self.assertEqual(
            (hard["original_BA_source_mass"],hard["original_BA_target_hits"],
             hard["true_original_dual_AB_target_hits"]), (4984,36,39))
        self.assertEqual(hard["scalar_P2_margin"],[757,143])
        self.assertEqual(hard["joint_signed_rank5"],[-2473,462])
        self.assertEqual(hard["joint_signed_rank6"],[-26,7])
        self.assertEqual(cases[0]["joint_signed_rank5"],[-3403,4620])
        self.assertEqual(cases[0]["joint_signed_rank6"],[422,105])


if __name__=="__main__":
    unittest.main()
