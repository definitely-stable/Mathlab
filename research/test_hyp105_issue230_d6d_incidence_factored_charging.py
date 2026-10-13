"""D6-D exact original positive-support incidence-Hall regression tests."""
import unittest
from hyp105_issue230_d6c_local_charge_hall import capacity_frontier
from hyp105_issue230_d6d_incidence_factored_charging import (
    _factored, factored_frontier, exact_incidence_union_hall_formula, report
)

class FactorizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=report()

    def test_original_W32_complete_all_seven_and_W34_BB_subset_only(self):
        rows=self.data["W32_COMPLETE_positive_all_seven"]
        self.assertEqual(len(rows),4)
        expected={"lex":(942,259,4),"reverse":(898,169,6),"S68":(606,68,9),"S72":(658,72,10)}
        for row in rows:
            C,S,K=expected[row["scheme"]]
            self.assertEqual((row["C_blocked_oriented"],row["full_seven_positive_S"]),(C,S))
            self.assertEqual(row["E_endpoint_bad"]+row["I_internal_only"],C)
            self.assertEqual(sum(row["real_positive_class_counts"].values()),S)
            self.assertEqual(len(row["one_class_deleted_coverage_diagnostics"]),7)
            result=row["r1_incidence_factorized"]
            self.assertEqual(result["status"],"EXACT-INCIDENCE-FACTORED-INTEGRAL-HALL-OPTIMUM")
            self.assertEqual(result["optimal_K"],row["independent_D6C_direct_min_K"])
            self.assertEqual(result["optimal_K"],K)
            self.assertEqual(result["extra_local_K_over_pigeonhole"],0)
            self.assertEqual(result["global_pigeonhole_K_floor"],K)
            self.assertTrue(all(x["one_overlap_source_uncovered_oriented_paths"]==0
                                for x in row["one_class_deleted_coverage_diagnostics"]))
            witness=result["K_minus_one_strict_Hall_witness"]
            self.assertEqual(witness["strict_hall_deficit"],witness["flow_shortfall"])
            self.assertGreater(witness["strict_hall_deficit"],0)
        partial=self.data["W34_ONLY_true_positive_sync_BB_subsets"]
        self.assertEqual(len(partial),4)
        for row in partial:
            self.assertIsNone(row["all_seven_positive_S"])
            self.assertFalse(row["BB_subset_is_entire_S"])
            self.assertFalse(row["all_h_universal_charge_proved"])
            self.assertEqual(row["E_endpoint_bad"]+row["I_internal_only"],
                             row["original_blocked_oriented"])
            self.assertGreater(row["full_synchronised_positive_BB_target_sixsets"],0)
            pinned={
                ("balanced","FULL-TRUE-ORIGINAL-G"):(52760,7649,7),
                ("reverse","FULL-TRUE-ORIGINAL-G"):(53238,7479,8),
                ("balanced","CALIBRATION-NOT-PR394"):(10290,7649,2),
                ("reverse","CALIBRATION-NOT-PR394"):(9186,7479,2),
            }
            C,BB,K=pinned[(row["mode"],row["policy"])]
            self.assertEqual((row["original_blocked_oriented"],
                              row["full_synchronised_positive_BB_target_sixsets"]),(C,BB))
            partial=row["r1_BB_subset_incidence_factorized"]
            self.assertEqual(partial["status"],
                             "EXACT-INCIDENCE-FACTORED-INTEGRAL-HALL-OPTIMUM")
            self.assertEqual(partial["optimal_K"],K)
            self.assertEqual(partial["extra_local_K_over_pigeonhole"],0)
            self.assertEqual(partial["uncovered_oriented_blocked_paths"],0)
            self.assertEqual(partial["factorized_flow_certificate"]["source_total"],C)
            self.assertEqual(partial["factorized_flow_certificate"]["value"],C)
        self.assertEqual(self.data["all_h_original_seven_lower"],"OPEN")

    def test_exact_factored_and_direct_synthetic_maxflow_mincut(self):
        a=(0,1,2);b=(3,4,5);q=(0,1,2,3,4,5)
        weights={a:2,b:1}; targets={q:"D6"}
        factored=factored_frontier(weights,targets)
        direct=capacity_frontier(weights,targets,1)
        self.assertEqual((factored["optimal_K"],direct["min_max_congestion"]),(3,3))
        self.assertEqual(factored["K_minus_one_strict_Hall_witness"]["strict_hall_deficit"],1)
        self.assertEqual(_factored(weights,targets,3)["value"],3)
        self.assertEqual(_factored(weights,targets,2)["value"],2)
        self.assertEqual(factored_frontier({(6,7,8):4},targets)["status"],
                         "UNSUPPORTED-ONE-INCIDENCE-NO-GO-FOR-GIVEN-TARGETS")
        self.assertEqual(factored_frontier({},targets)["status"],"EMPTY-SOURCE-NO-INFERENCE")

    def test_exact_incidence_union_subset_Hall_and_fail_closed(self):
        weights={(0,1,2):2,(1,2,3):3,(7,8,9):4}
        targets={(0,1,2,10,11,12):"D6",(3,4,5,6,13,14):"B/B-overlap"}
        rows=exact_incidence_union_hall_formula(weights,targets,[
            {0,1,2},{1,2,3},{0,1,2,3},{7,8,9}
        ])
        self.assertEqual([(r["oriented_source_demand_T_subset_F"],
                            r["eligible_positive_original_sixsets_meeting_active_union"])
                          for r in rows],[(2,1),(3,2),(5,2),(4,0)])
        self.assertTrue(rows[-1]["denominator_zero_with_positive_demand"])
        for bad in ({(0,1,2):-1},{(0,0,1):1},{(2,1,0):1}):
            with self.assertRaises(ValueError):
                factored_frontier(bad,targets)
        with self.assertRaises(ValueError):
            _factored({(0,1,2):1},targets,-1)

if __name__=="__main__":
    unittest.main()
