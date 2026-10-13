"""D6-C: exact original blocked P3 -> accepted seven-class local Hall tests."""
import unittest

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6b_coherent_pruning import original_diagonals, _edge
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

    def test_pinned_exact_hosted_W32_Hall_no_go_and_optimal_K(self):
        # TRUE original W32 full all-seven exhaustive data from first hosted
        # Contract: r3 fails for both, r2 fails for S68 (8 oriented paths),
        # r1 is feasible with integral optimum 4 / 9 respectively.
        pinned={
            ("lex","FULL-TRUE-ORIGINAL-G"):(
                (760,None),(0,4),(0,4)),
            ("S68","FULL-TRUE-ORIGINAL-G"):(
                (596,None),(8,None),(0,9)),
            ("lex","COHERENT-EVERY-19-ORIGINAL-INCIDENCE"):(
                (606,None),(0,None),(0,None)),
            ("S68","COHERENT-EVERY-19-ORIGINAL-INCIDENCE"):(
                (496,None),(8,None),(0,None)),
            ("S68","CALIBRATION-NOT-PR394"):(
                (84,None),(6,None),(0,None)),
        }
        for key,expected in pinned.items():
            row=self.by_case[key]
            for f,(uncovered,K) in zip(row["source_overlap_frontiers"],expected):
                self.assertEqual(f["uncovered_oriented_source_paths"],uncovered)
                self.assertEqual(f["min_max_congestion"],K)
        lex=self.by_case["lex","FULL-TRUE-ORIGINAL-G"]
        s68=self.by_case["S68","FULL-TRUE-ORIGINAL-G"]
        self.assertEqual(lex["canonical_original_closure_outcomes"],{
            "ACCEPTED_BB":4,"BAD_BOTH":758,"BAD_LEFT":50,
            "BAD_RIGHT":46,"REPEATED_ORIGINAL_INCIDENCE":88})
        self.assertEqual(s68["canonical_original_closure_outcomes"],{
            "BAD_BOTH":474,"BAD_LEFT":22,
            "BAD_RIGHT":36,"REPEATED_ORIGINAL_INCIDENCE":74})
        self.assertEqual(
            lex["source_overlap_frontiers"][1]["status"],
            "EXACT-FINITE-INTEGRAL-HALL-OPTIMUM")
        self.assertEqual(
            s68["source_overlap_frontiers"][1]["status"],
            "NO-GO-UNSUPPORTED-ORIGINAL-SOURCE")
        self.assertEqual(
            s68["source_overlap_frontiers"][2]["status"],
            "EXACT-FINITE-INTEGRAL-HALL-OPTIMUM")
        self.assertEqual(
            s68["source_overlap_frontiers"][2]["unconstrained_global_congestion_floor"],9)
        self.assertEqual(
            lex["source_overlap_frontiers"][1]["unconstrained_global_congestion_floor"],4)

    def test_exact_S68_unrepairable_true_original_r2_witness_direct_seven_enumeration(self):
        # Source from the final exact-head hosted ORIGINAL full-G report.
        row=self.by_case["S68","FULL-TRUE-ORIGINAL-G"]
        witness=row["r2_unsupported_TRUE_original_source"]
        self.assertEqual(witness,{
            "four_original_grid_vertices":[26,15,7,34],
            "mask":13,
            "original_endpoint_line":13,
            "original_endpoint_point":3,
            "original_projection_line":8,
            "original_projection_point":13,
            "source_three_original_incidences":[5,16,35],
        })
        model=fixture(1,"S68")
        core=ProjectionClosure(model)
        _,owner=original_diagonals(core)
        path=witness["four_original_grid_vertices"]
        original_source=tuple(sorted(
            owner[_edge(u,v)] for u,v in zip(path,path[1:])))
        self.assertEqual(original_source,(5,16,35))
        a=core.a
        self.assertEqual(len({v//a for v in path}),4)
        self.assertEqual(len({v%a for v in path}),4)
        q=core.fi[_edge(path[0]//a,path[3]//a)]
        r=core.gi[_edge(path[0]%a,path[3]%a)]
        self.assertEqual((q,r,core.projection[q,r]),(3,13,(13,8)))
        targets=seven_census(model,independent_checks=True,witness_sets=True)["sets"]
        self.assertEqual(len(targets),68)
        histogram={}
        for target in targets:
            k=len(set(original_source)&set(target))
            histogram[k]=histogram.get(k,0)+1
        self.assertEqual(sum(histogram.values()),68)
        self.assertLessEqual(max(histogram),1)
        self.assertEqual(histogram.get(2,0),0)
        self.assertEqual(histogram.get(3,0),0)

    def test_invalid_source_overlap_gate_fails_closed(self):
        with self.assertRaises(ValueError):
            capacity_frontier({(0,1,2):1},{(0,1,2,3,4,5):"D6"},0)
        with self.assertRaises(ValueError):
            capacity_frontier({(0,1,2):1},{(0,1,2,3,4,5):"D6"},4)
        with self.assertRaises(ValueError):
            capacity_frontier({(0,1,2):-1},{(0,1,2,3,4,5):"D6"},3)


if __name__=="__main__":
    unittest.main()
