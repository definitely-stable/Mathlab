"""D6-B: full original incidence-paired PR394 pruning and falsifiers."""
from fractions import Fraction
import unittest

from hyp105_issue230_projection import ProjectionClosure
from hyp105_issue230_d5_retained_energy import (
    true_spread_global_model, selected_anchor_edge_oracle,
    retained_original_energy,
)
from hyp105_issue230_d6b_coherent_pruning import (
    _config, _root_floor, full_retention, original_diagonals,
    coherent_selected_first, prune_original_incidences,
    retained_path_census, report,
)


class TrueOriginalD6BPruningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=report()
        cls.rows=cls.report["same_complete_original_global_maps"]
        cls.by_case={(r["s"],r["policy"],r["full_global_original_seven_S"],r["W_retained_original_endpoint_energy"]):r
                     for r in cls.rows}

    def test_all_sixteen_true_original_pruned_masks_and_conservation(self):
        self.assertEqual(len(self.rows),16)
        for x in self.rows:
            with self.subTest(s=x["s"],scheme=x.get("policy")):
                self.assertEqual(sum(x["exact_sixteen_mask_histogram"]),
                                 x["nonincident_endpoint_complete"])
                self.assertEqual(sum(x["exact_sixteen_mask_histogram"][1:]),
                                 x["C_joint_blocked_proper_P3"])
                self.assertEqual(x["C_joint_blocked_proper_P3"],
                                 x["E_endpoint_bad_proper_P3"]+
                                 x["I_safe_endpoint_internal_only_proper_P3"])
                self.assertEqual(x["proper_P3"],
                                 x["missing"]+x["incident"]+
                                 x["nonincident_endpoint_complete"])
                self.assertEqual(x["exact_sixteen_mask_histogram"][0],
                                 2*x["BB_sync_accepted_sixsets"])
                self.assertEqual(x["retained_physical_edges"],
                                 2*x["retained_original_incidences"])
                self.assertEqual(x["removed_physical_edges"],
                                 2*x["removed_original_incidences"])
                self.assertEqual(x["retained_original_incidences"]+
                                 x["removed_original_incidences"],
                                 x["full_original_incidences"])
                self.assertTrue(x["independent_original_endpair_enumeration"])
                self.assertGreaterEqual(x["W_retained_original_endpoint_energy"],0)
        self.assertEqual(self.report["all_h_original_seven_S_lower"],"OPEN")
        self.assertEqual(self.report["all_h_C_compensation"],"OPEN")
        self.assertEqual(self.report["branch_B_infinite_small_S"],"OPEN")

    def test_literal_PR394_thresholds_are_exact_integers_not_float_guesses(self):
        self.assertEqual(_root_floor(2,16),1)
        self.assertEqual(_root_floor(4,16),1)
        self.assertEqual(_root_floor(8,16),1)
        self.assertEqual(_root_floor(2**16,16),2)
        for x in self.rows:
            if x["policy"]!="PR394-EXACT-AS-WRITTEN":
                continue
            self.assertEqual(x["missing_star_cap"],1)
            self.assertLessEqual(x["max_retained_coordinate_block"]**10,x["s"])
            d=x["min_positive_retained_degree"]
            if d:
                self.assertGreaterEqual(d**32,x["s"]**31)
            self.assertEqual(
                x["deleted_stage1_orig_incidences"]+
                x["deleted_stage2_orig_incidences"]+
                x["deleted_stage3_orig_incidences"]+
                x["retained_original_incidences"],
                x["full_original_incidences"])
            self.assertEqual(x["policy"],"PR394-EXACT-AS-WRITTEN")

    def test_calibration_is_never_called_theorem_and_counts_are_monotone(self):
        for i in range(0,len(self.rows),4):
            full,literal,calib,adversarial=self.rows[i:i+4]
            self.assertEqual(full["policy"],"FULL-TRUE-ORIGINAL-G")
            self.assertEqual(literal["policy"],"PR394-EXACT-AS-WRITTEN")
            self.assertEqual(calib["policy"],"CALIBRATION-NOT-PR394")
            self.assertTrue(adversarial["policy"].startswith("COHERENT-"))
            self.assertEqual(full["removed_physical_edges"],0)
            for item in (literal,calib,adversarial):
                for field in (
                    "proper_P3", "E_endpoint_bad_proper_P3",
                    "I_safe_endpoint_internal_only_proper_P3",
                    "C_joint_blocked_proper_P3",
                    "BB_sync_accepted_sixsets",
                    "W_retained_original_endpoint_energy"
                ):
                    self.assertLessEqual(item[field],full[field])
                self.assertEqual(item["full_global_original_seven_S"],
                                 full["full_global_original_seven_S"])

    def test_true_D5_spread_reference_full_and_retained_pruning_energy(self):
        reference={
            127932:(35190,17570,52760,7649),
            131936:(36014,17224,53238,7479),
        }
        for x in self.rows:
            if x["s"]==4 and x["policy"]=="FULL-TRUE-ORIGINAL-G":
                self.assertIn(x["W_retained_original_endpoint_energy"],reference)
                self.assertEqual(tuple(x[k] for k in (
                    "E_endpoint_bad_proper_P3",
                    "I_safe_endpoint_internal_only_proper_P3",
                    "C_joint_blocked_proper_P3","BB_sync_accepted_sixsets"
                )),reference[x["W_retained_original_endpoint_energy"]])
            if x["s"]==4:
                self.assertIsNone(x["full_global_original_seven_S"])
            if x["s"]==2:
                self.assertIn(x["full_global_original_seven_S"],(259,68))
            if x["s"]==4 and x["policy"]=="PR394-EXACT-AS-WRITTEN":
                self.assertIn("D5_selected_kept_original_spread_witness_edges",x)
                w=Fraction(x["W_retained_original_endpoint_energy"])
                floor=Fraction(x["D5_robust_lower_numerator"],
                               x["D5_robust_lower_denominator"])
                self.assertGreaterEqual(w,floor)

    def test_real_W38_PR394_literal_retained_nonnegative_spread_certificate(self):
        model,selected,group,spec=true_spread_global_model(3,"balanced")
        core=ProjectionClosure(model)
        literal=prune_original_incidences(core,"literal-pr394")
        self.assertEqual(literal["retained_physical_edges"],
                         2*literal["retained_original_incidences"])
        self.assertLessEqual(literal["max_retained_coordinate_block"]**10,8)
        row=retained_path_census(core,literal,max_walks=70_000_000,
                                 independent_endpoints=False)
        self.assertEqual(row["C_joint_blocked_proper_P3"],
                         row["E_endpoint_bad_proper_P3"]+
                         row["I_safe_endpoint_internal_only_proper_P3"])
        witness=retained_original_energy(
            model,selected,group,spec,
            deleted_edges=tuple(literal["deleted_physical_edges"]),
            assert_new_oracle=False)
        self.assertGreaterEqual(Fraction(witness["exact_original_bad_chord_energy_W_H"]),
                                Fraction(witness["robust_removed_edges_lower_num"],
                                         witness["robust_removed_edges_lower_den"]))
        self.assertFalse(witness["universal_S_six_positive_lower_proved"])

    def test_pinned_true_original_sixteen_retained_W32_W34_ledgers(self):
        # First exact GitHub-hosted PR401 Contract independently printed 16
        # complete ORIGINAL same-map policy cases, frozen here after success.
        pinned={
            ("W32-lex","FULL-TRUE-ORIGINAL-G"):(90,2977,1346,786,156,942,2),
            ("W32-lex","PR394-EXACT-AS-WRITTEN"):(0,0,0,0,0,0,0),
            ("W32-lex","CALIBRATION-NOT-PR394"):(14,473,0,0,0,0,0),
            ("W32-lex","COHERENT-EVERY-19-ORIGINAL-INCIDENCE"):(84,2781,1058,648,114,762,2),
            ("W32-S68","FULL-TRUE-ORIGINAL-G"):(90,3289,678,544,62,606,0),
            ("W32-S68","PR394-EXACT-AS-WRITTEN"):(0,0,0,0,0,0,0),
            ("W32-S68","CALIBRATION-NOT-PR394"):(48,1759,96,76,8,84,0),
            ("W32-S68","COHERENT-EVERY-19-ORIGINAL-INCIDENCE"):(84,3075,578,458,48,506,0),
            ("W34-D5-spread-balanced","FULL-TRUE-ORIGINAL-G"):(850,127932,82322,35190,17570,52760,7649),
            ("W34-D5-spread-balanced","PR394-EXACT-AS-WRITTEN"):(0,0,0,0,0,0,0),
            ("W34-D5-spread-balanced","CALIBRATION-NOT-PR394"):(482,72810,15892,6702,3588,10290,1376),
            ("W34-D5-spread-balanced","COHERENT-D5-SELECTED-WITNESS-FIRST-20PCT"):(818,122953,72942,31230,15652,46882,6695),
            ("W34-D5-spread-reverse","FULL-TRUE-ORIGINAL-G"):(850,131936,82288,36014,17224,53238,7479),
            ("W34-D5-spread-reverse","PR394-EXACT-AS-WRITTEN"):(0,0,0,0,0,0,0),
            ("W34-D5-spread-reverse","CALIBRATION-NOT-PR394"):(464,72094,14270,6170,3016,9186,1234),
            ("W34-D5-spread-reverse","COHERENT-D5-SELECTED-WITNESS-FIRST-20PCT"):(816,126309,73314,32278,15122,47400,6624),
        }
        assert len(pinned)==len(self.rows)
        for row in self.rows:
            pair=row["scheme"],row["policy"]
            self.assertIn(pair,pinned)
            got=tuple(row[k] for k in (
                "retained_physical_edges","W_retained_original_endpoint_energy",
                "proper_P3","E_endpoint_bad_proper_P3",
                "I_safe_endpoint_internal_only_proper_P3",
                "C_joint_blocked_proper_P3","BB_sync_accepted_sixsets"))
            self.assertEqual(got,pinned[pair])
        # Literal PR394 at tiny finite s has no nontrivial path reservoir,
        # which cannot falsify its asymptotic theorem or prove root A.
        self.assertTrue(all(
            r["proper_P3"]==0 and r["retained_physical_edges"]==0
            for r in self.rows if r["policy"]=="PR394-EXACT-AS-WRITTEN"))

    def test_invalid_policies_fail_closed(self):
        model,_,_,_=true_spread_global_model(2)
        core=ProjectionClosure(model)
        with self.assertRaises(ValueError):
            prune_original_incidences(core,"assume-spectral")
        with self.assertRaises(ValueError):
            coherent_selected_first(core,period=1)
        with self.assertRaises(ValueError):
            coherent_selected_first(core,selected_physical_edges={(0,0)})
        with self.assertRaises(ValueError):
            retained_path_census(core,full_retention(core),max_walks=0)


if __name__=="__main__":
    unittest.main()
