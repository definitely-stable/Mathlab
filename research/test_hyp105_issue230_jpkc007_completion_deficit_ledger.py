"""JPKC007 exact ORIGINAL source-incidence deficit and local palette checks."""
from fractions import Fraction
from itertools import combinations,permutations
import unittest

from hyp105_issue230_projection import ProjectionClosure,fixture
from hyp105_issue230_jpkc002_path_collision_taxonomy import _path_fibers
from hyp105_issue230_jpkc005_alternate_three_completion import _bad_seed_paths
from hyp105_issue230_jpkc007_completion_deficit_ledger import (
    _physical_half_palette,_source_wedge_stages,
    _source_matching_stages,deficit_certificate,
)


class JPKC007Tests(unittest.TestCase):
    def test_true_original_W32_complete_positive_and_palette_hole_falsifier(self):
        known={
            "lex":(786,154,214),
            "reverse":(676,86,90),
            "S68":(544,8,8),
            "S72":(600,10,10),
        }
        for scheme,(E,covered,hits) in known.items():
            with self.subTest(scheme=scheme):
                r=deficit_certificate(fixture(1,scheme))
                self.assertEqual(r["true_full_endpoint_bad_seed_population"],E)
                self.assertEqual(r["exact_selected_endpoint_bad_seeds"],E)
                self.assertTrue(r["complete_endpoint_seed_census"])
                self.assertEqual(r["seeds_with_positive_true_source_Q"],covered)
                self.assertEqual(r["isolated_true_source_seeds"],E-covered)
                self.assertEqual(r["loss_budget"]["genuine_original_positive_PQ"],hits)
                self.assertTrue(r["J22_exact_A_half_palette_hole_identity"])
                self.assertTrue(r["J23_exact_geometry_matching_wedge_dual_deficit_telescope"])
                self.assertTrue(r["J24_palette_only_A_half_lower_verified"])
                self.assertTrue(r["full_original_W32_seven_GF5_index_compared"])
                self.assertFalse(r["root_A_proved"])
                # The true W32 physical f/g images are the COMPLETE K6.
                # EVERY proper P3 has two physical A completions PER half,
                # yet S68/S72 overwhelmingly lack ORIGINAL positive Q.
                for side in ("L","R"):
                    self.assertEqual(r["loss_budget"][side+"_available_A_half"],2*E)
                    self.assertEqual(
                        r["loss_budget"][side+"_all_physical_A_half_candidates"],2*E)
                    for stage in ("missing_first_chord",
                                  "missing_last_chord_after_first",
                                  "missing_internal_chord_after_both",
                                  "physical_global_missing_Ka_edges"):
                        self.assertEqual(r["loss_budget"][side+"_"+stage],0)
                self.assertEqual(
                    r["loss_budget"]["isolation_despite_both_physical_A_halves"],
                    E-covered)
                self.assertEqual(sum(r["actual_source_positive_Q_class_counts"].values()),
                                 hits)

    def test_W32_independently_enumerated_complete_two_sided_palette(self):
        for scheme in ("S68","S72"):
            ctx=ProjectionClosure(fixture(1,scheme))
            _,fibers,_=_path_fibers(ctx,2_000_000)
            for path,T,qr in _bad_seed_paths(ctx,fibers):
                for side in (0,1):
                    p=_physical_half_palette(ctx,path,side)
                    self.assertEqual(p["all_physical_A_half_candidates"],2)
                    self.assertEqual(p["available_A_half"],2)
                    self.assertEqual(p["J24_local_palette_guaranteed_A_half"],2)
                    self.assertEqual(p["J22_closed_form_A_half"],2)
                    self.assertTrue(p["J24_P4_endpoints_have_no_missing_outside_chord"])

    def test_original_W34_targeted_true_maps_and_strict_partial_scope(self):
        for scheme in ("lex","random"):
            with self.subTest(scheme=scheme):
                r=deficit_certificate(fixture(2,scheme),
                                      limit_seeds=32,exact_W32=False)
                self.assertEqual(r["exact_selected_endpoint_bad_seeds"],32)
                self.assertFalse(r["complete_endpoint_seed_census"])
                self.assertTrue(r["scope_no_full_W34_seven_S"])
                self.assertFalse(r["full_original_W32_seven_GF5_index_compared"])
                self.assertEqual(r["s"],4)
                self.assertEqual(r["loss_budget"]["L_physical_global_missing_Ka_edges"],
                                 6*32)
                self.assertEqual(r["loss_budget"]["R_physical_global_missing_Ka_edges"],
                                 6*32)
                self.assertEqual(r["seeds_with_positive_true_source_Q"]+
                                 r["isolated_true_source_seeds"],32)
                self.assertEqual(sum(r["actual_source_positive_Q_class_counts"].values()),
                                 r["loss_budget"]["genuine_original_positive_PQ"])

    def test_D4_true_original_W34_source_deficits_not_synthetic(self):
        from hyp105_issue230_jpkc_spread_adversary import spread_adversary_model
        model,cert=spread_adversary_model(2)
        self.assertEqual(cert["M_f_original_exact"],259)
        r=deficit_certificate(model,limit_seeds=32,exact_W32=False)
        self.assertEqual(r["exact_selected_endpoint_bad_seeds"],32)
        self.assertEqual(r["true_full_endpoint_bad_seed_population"],35190)
        self.assertTrue(r["J23_exact_geometry_matching_wedge_dual_deficit_telescope"])
        self.assertFalse(r["root_B_constructed"])

    def test_exact_source_stage_telescope_per_true_original_P3(self):
        ctx=ProjectionClosure(fixture(1,"S68"))
        _,fibers,_=_path_fibers(ctx,2_000_000)
        for path,T,qr in list(_bad_seed_paths(ctx,fibers))[:48]:
            A=_physical_half_palette(ctx,path,0)
            B=_physical_half_palette(ctx,path,1)
            matching,D6=_source_matching_stages(ctx,path)
            l,plus=_source_wedge_stages(ctx,path,0)
            r,minus=_source_wedge_stages(ctx,path,1)
            self.assertEqual(matching["raw_matching_bijections"],
                             6*A["available_A_half"]*B["available_A_half"])
            self.assertEqual(l["source_wedge_proposals"],
                             3*A["available_A_half"])
            self.assertEqual(r["source_wedge_proposals"],
                             3*B["available_A_half"])
            self.assertEqual(matching["source_positive_D6"],len(D6))
            self.assertEqual(l["source_positive_wedges"],len(plus))
            self.assertEqual(r["source_positive_wedges"],len(minus))
            self.assertEqual(matching["raw_matching_bijections"],
                             matching["missing_original_incidence_matching"]+
                             matching["nonaligned_AA_original_duals"]+
                             matching["source_positive_D6"])

    def test_fail_closed_original_global_labels_scopes_and_budgets(self):
        with self.assertRaisesRegex(ValueError,"W32"):
            deficit_certificate(fixture(2,"lex"))
        with self.assertRaisesRegex(ValueError,"selected source seed limit"):
            deficit_certificate(fixture(1,"lex"),limit_seeds=0)
        with self.assertRaisesRegex(ValueError,"path budget"):
            deficit_certificate(fixture(1,"S68"),max_paths=1)
        bad=fixture(1,"S68")
        g=list(bad["right_labels"]);g[0]=g[1]
        bad["right_labels"]=tuple(g)
        with self.assertRaises(ValueError):
            deficit_certificate(bad)


if __name__=="__main__":
    unittest.main()
