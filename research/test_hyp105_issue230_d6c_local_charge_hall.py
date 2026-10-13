"""D6-C: exact original blocked P3 -> accepted seven-class local Hall tests."""
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d5_retained_energy import true_spread_global_model
from hyp105_issue230_d6c_local_charge_hall import (
    capacity_frontier, one_model, report,
)


class OriginalD6CLocalChargingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=report()
        cls.rows=cls.report["records"]
        cls.by_case={(r["scheme"],r["policy"]):r for r in cls.rows}

    def test_true_original_all_seven_classes_and_exact_eight_policy_count(self):
        self.assertEqual(len(self.rows),8)
        self.assertEqual(
            self.report["all_h_direct_unique_projection_closure_for_blocked_paths"],
            "NO-GO-PROVED")
        self.assertEqual(self.report["original_root_A_and_B"],"OPEN")
        self.assertEqual(self.report["bounded_congestion_all_h"],"OPEN")
        for row in self.rows:
            with self.subTest(scheme=row["scheme"],policy=row["policy"]):
                self.assertEqual(row["s"],2)
                self.assertTrue(row["same_complete_globally_injective_original_f_g"])
                self.assertEqual(row["retained_paired_physical_edges"],
                                 2*row["retained_true_original_incidences"])
                self.assertEqual(len(row["source_overlap_frontiers"]),3)
                self.assertEqual(len(row["sixteen_original_mask_histogram"]),16)
                self.assertEqual(sum(row["sixteen_original_mask_histogram"]),
                                 row["total_true_original_oriented_blocked_paths"])
                self.assertEqual(sum(row["actual_seven_positive_classes"].values()),
                                 row["complete_original_seven_positive_S"])
                self.assertEqual(row["canonical_original_closure_outcomes"].get("ACCEPTED_BB",0),
                                 row["total_true_original_unblocked_proper_paths"])
                self.assertEqual(row["original_root_S_Omega_s6_proved"],False)
                self.assertEqual(row["asymptotic_bounded_congestion_charging_proved"],False)
                self.assertEqual(row["all_h_small_S_counterfamily_proved"],False)
                assert set(row["canonical_original_closure_outcomes"])<={
                    "BAD_LEFT","BAD_RIGHT","BAD_BOTH",
                    "REPEATED_ORIGINAL_INCIDENCE","ACCEPTED_BB"
                }
                for r,front in zip((3,2,1),row["source_overlap_frontiers"]):
                    self.assertEqual(front["required_original_source_incidence_overlap"],r)
                    self.assertIn(front["status"],{
                        "NO-GO-UNSUPPORTED-ORIGINAL-SOURCE",
                        "EXACT-FINITE-INTEGRAL-HALL-OPTIMUM",
                        "COVERED-EXACT-CAPACITY-NOT-SOLVED",
                        "EMPTY-SOURCE-NO-INFERENCE"})
                    if front["status"]=="NO-GO-UNSUPPORTED-ORIGINAL-SOURCE":
                        self.assertGreater(front["uncovered_oriented_source_paths"],0)
                        self.assertIsNotNone(front[
                            "uncovered_witness_source_original_incidence_triple"])
                        witness=row[f"r{r}_unsupported_TRUE_original_source"]
                        self.assertEqual(len(witness["source_three_original_incidences"]),3)
                    if front["status"]=="EXACT-FINITE-INTEGRAL-HALL-OPTIMUM":
                        self.assertEqual(row["policy"],"FULL-TRUE-ORIGINAL-G")
                        self.assertIsInstance(front["min_max_congestion"],int)
                        cut=front["optimal_capacity_lower_hall_cut"]
                        self.assertEqual(cut["capacity"],front["min_max_congestion"]-1)
                        self.assertEqual(
                            cut["original_path_demand_on_subset"]
                            -cut["capacity"]*cut["neighbor_positive_sixsets"],
                            cut["exact_hall_deficit"])

    def test_known_same_map_W32_full_and_true_coherent_retained_source_counts(self):
        pinned={
            ("lex","FULL-TRUE-ORIGINAL-G"):(942,259,4),
            ("lex","CALIBRATION-NOT-PR394"):(0,259,0),
            ("lex","COHERENT-EVERY-19-ORIGINAL-INCIDENCE"):(762,259,4),
            ("lex","PR394-EXACT-AS-WRITTEN"):(0,259,0),
            ("S68","FULL-TRUE-ORIGINAL-G"):(606,68,0),
            ("S68","CALIBRATION-NOT-PR394"):(84,68,0),
            ("S68","COHERENT-EVERY-19-ORIGINAL-INCIDENCE"):(506,68,0),
            ("S68","PR394-EXACT-AS-WRITTEN"):(0,68,0),
        }
        for key,(blocked,S,good) in pinned.items():
            row=self.by_case[key]
            self.assertEqual(row["total_true_original_oriented_blocked_paths"],blocked)
            self.assertEqual(row["complete_original_seven_positive_S"],S)
            self.assertEqual(row["total_true_original_unblocked_proper_paths"],good)
            if row["policy"]=="PR394-EXACT-AS-WRITTEN":
                self.assertEqual(row["retained_paired_physical_edges"],0)
                self.assertEqual(row["source_overlap_frontiers"][0]["status"],
                                 "EMPTY-SOURCE-NO-INFERENCE")

    def test_pure_integer_hall_cut_optimality_and_uncovered_no_go(self):
        a=(0,1,2); b=(3,4,5)
        single=(0,1,2,3,4,5)
        # Both positive demanded original source triples may charge only
        # this single accepted original target: exact integer min load=3.
        ret=capacity_frontier({a:2,b:1},{single:"D6"},3)
        self.assertEqual(ret["status"],"EXACT-FINITE-INTEGRAL-HALL-OPTIMUM")
        self.assertEqual(ret["min_max_congestion"],3)
        self.assertEqual(ret["optimal_capacity_lower_hall_cut"]["exact_hall_deficit"],1)
        uncovered=capacity_frontier({(6,7,8):4},{single:"D6"},1)
        self.assertEqual(uncovered["status"],"NO-GO-UNSUPPORTED-ORIGINAL-SOURCE")
        self.assertEqual(uncovered["uncovered_oriented_source_paths"],4)
        self.assertEqual(uncovered["uncovered_witness_source_original_incidence_triple"],[6,7,8])
        empty=capacity_frontier({}, {single:"D6"},3)
        self.assertEqual(empty["status"],"EMPTY-SOURCE-NO-INFERENCE")

    def test_no_W34_seven_recipients_imputation(self):
        model,_,_,_=true_spread_global_model(2)
        with self.assertRaises(ValueError):
            one_model(model,"not-an-accepted-full-W34-S")

    def test_invalid_source_overlap_gate_fails_closed(self):
        with self.assertRaises(ValueError):
            capacity_frontier({(0,1,2):1},{(0,1,2,3,4,5):"D6"},0)
        with self.assertRaises(ValueError):
            capacity_frontier({(0,1,2):1},{(0,1,2,3,4,5):"D6"},4)
        with self.assertRaises(ValueError):
            capacity_frontier({(0,1,2):-1},{(0,1,2,3,4,5):"D6"},3)


if __name__=="__main__":
    unittest.main()
