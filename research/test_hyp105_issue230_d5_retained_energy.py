"""Independent retained physical energy contract for issue230 D5."""
import unittest
from fractions import Fraction

from hyp105_issue230_d5_retained_energy import (
    finite_fixture, true_spread_global_model,
    retained_original_energy,selected_anchor_edge_oracle,report,
)
from hyp105_issue230_projection import ProjectionClosure
from hyp105_issue230_d4_spread_pencil_falsifier import plan


class Issue230D5RetainedEndpointTests(unittest.TestCase):
    def test_real_full_original_W34_and_W38_energy_matches_independent_D4(self):
        for power,expected in ((2,127932),(3,6614488)):
            with self.subTest(power=power):
                x=finite_fixture(power,"balanced")
                self.assertEqual(x["exact_original_bad_chord_energy_W_H"],expected)
                self.assertEqual(x["arbitrarily_deleted_TRUE_physical_edges"],0)
                self.assertEqual(x["selected_nonspread_TRUE_physical_edges"],
                                 2*x["selected_original_points"]*x["s"])
                self.assertEqual(x["selected_kept_TRUE_physical_edges"],
                                 x["selected_nonspread_TRUE_physical_edges"])
                self.assertEqual(x["all_original_G_physical_edges"],
                                 2*plan(x["s"])["V"]*(x["s"]+1))
                self.assertGreaterEqual(
                    Fraction(x["exact_original_bad_chord_energy_W_H"]),
                    Fraction(x["full_graph_retention_free_lower_num"],
                             x["full_graph_retention_free_lower_den"]))
                self.assertFalse(x["universal_S_six_positive_lower_proved"])
                self.assertFalse(x["infinite_small_S_Branch_B_proved"])

    def test_arbitrary_globally_permuted_right_g_does_not_break_theorem(self):
        for power in (2,3):
            with self.subTest(power=power):
                orig=finite_fixture(power,"balanced")
                rev=finite_fixture(power,"reverse")
                self.assertEqual(orig["full_graph_retention_free_lower_num"],
                                 rev["full_graph_retention_free_lower_num"])
                self.assertEqual(orig["full_graph_retention_free_lower_den"],
                                 rev["full_graph_retention_free_lower_den"])
                self.assertGreaterEqual(
                    Fraction(rev["exact_original_bad_chord_energy_W_H"]),
                    Fraction(rev["full_graph_retention_free_lower_num"],
                             rev["full_graph_retention_free_lower_den"]))
                self.assertTrue(rev["same_global_original_pair_injections"])

    def test_retain_all_but_every_nineteenth_physical_edge(self):
        for power in (2,3):
            with self.subTest(power=power):
                x=finite_fixture(power,"balanced",delete_every=19)
                self.assertGreater(x["arbitrarily_deleted_TRUE_physical_edges"],0)
                self.assertGreater(x["selected_kept_TRUE_physical_edges"],0)
                self.assertGreaterEqual(
                    Fraction(x["exact_original_bad_chord_energy_W_H"]),
                    Fraction(x["refined_retained_lower_num"],
                             x["refined_retained_lower_den"]))
                self.assertGreaterEqual(
                    Fraction(x["refined_retained_lower_num"],
                             x["refined_retained_lower_den"]),
                    Fraction(x["robust_removed_edges_lower_num"],
                             x["robust_removed_edges_lower_den"]))
                self.assertGreater(
                    Fraction(x["robust_removed_edges_lower_num"],
                             x["robust_removed_edges_lower_den"]),0)

    def test_adversarially_delete_selected_witness_edges_first(self):
        for power in (2,3):
            with self.subTest(power=power):
                x=finite_fixture(power,"balanced",adversarial=True)
                self.assertEqual(x["removed_selected_true_physical_edges"],
                                 x["arbitrarily_deleted_TRUE_physical_edges"])
                self.assertGreater(x["selected_kept_TRUE_physical_edges"],0)
                self.assertGreaterEqual(
                    Fraction(x["exact_original_bad_chord_energy_W_H"]),
                    Fraction(x["robust_removed_edges_lower_num"],
                             x["robust_removed_edges_lower_den"]))

    def test_empty_H_is_allowed_and_has_zero_energy(self):
        model,selected,group,spec=true_spread_global_model(2)
        core=ProjectionClosure(model)
        full,relevant=selected_anchor_edge_oracle(core,selected,group,spec)
        z=retained_original_energy(model,selected,group,spec,deleted_edges=tuple(full),
                                   assert_new_oracle=False)
        self.assertEqual(z["exact_original_bad_chord_energy_W_H"],0)
        self.assertEqual(z["selected_kept_TRUE_physical_edges"],0)
        self.assertEqual(z["robust_removed_edges_lower_num"],0)

    def test_reject_synthetic_or_duplicate_graph_edge(self):
        model,selected,group,spec=true_spread_global_model(2)
        core=ProjectionClosure(model)
        full,_=selected_anchor_edge_oracle(core,selected,group,spec)
        good=next(iter(full))
        with self.assertRaises(ValueError):
            retained_original_energy(model,selected,group,spec,
                                     deleted_edges=(good,good))
        with self.assertRaises(ValueError):
            retained_original_energy(model,selected,group,spec,
                                     deleted_edges=((0,0),))

    def test_rigorous_asymptotic_original_spread_coefficient_arithmetic(self):
        for s in (256,1024,4096,16384):
            with self.subTest(s=s):
                x=plan(s)
                g0=x["anchor_coordinates"];a=x["a"]
                k=x["spread_lines_per_anchor"]*(s+1)
                m=2*g0*k*s
                exact=Fraction(s*m*m,g0*a*s**6)
                self.assertGreater(exact,0)
                if s>=4096:
                    self.assertGreater(exact,Fraction(15,100))
                # Deleting <=s^3 original physical edges is asymptotically
                # o(s4), never use finite tests as an infinite proof.
                deleted=s**3
                keep=max(0,m-deleted)
                self.assertGreaterEqual(Fraction(s*keep*keep,g0*a),0)

    def test_eight_finite_true_original_retained_chord_energy_certificates(self):
        r=report()
        self.assertEqual(len(r["real_true_original_witnesses"]),8)
        self.assertEqual(r["all_h_unconditional_D2_D3_WH_little_o_s59over10"],
                         "FALSE")
        self.assertEqual(r["all_h_original_seven_family_S_lower"],"OPEN")
        self.assertEqual(r["all_h_small_S_branch_B"],"OPEN")
        self.assertFalse(r["adversarial_all_maps_counterexample_to_original_root"])
        pinned={
            (4,"balanced","none"):(127932,0,120),
            (4,"reverse","none"):(131936,0,120),
            (4,"balanced","every-19"):(121234,45,117),
            (4,"balanced","adversarial-original-selected"):(124146,24,96),
            (8,"balanced","none"):(6614488,0,1152),
            (8,"reverse","none"):(6663027,0,1152),
            (8,"balanced","every-19"):(6267591,555,1099),
            (8,"balanced","adversarial-original-selected"):(6474532,230,922),
        }
        for x in r["real_true_original_witnesses"]:
            case=(x["s"],x["right_global_original_label_mode"],
                  x["physical_edge_removal_scheme"])
            self.assertIn(case,pinned)
            self.assertEqual(
                (x["exact_original_bad_chord_energy_W_H"],
                 x["arbitrarily_deleted_TRUE_physical_edges"],
                 x["selected_kept_TRUE_physical_edges"]), pinned[case])
            self.assertGreaterEqual(
                Fraction(x["exact_original_bad_chord_energy_W_H"]),
                Fraction(x["robust_removed_edges_lower_num"],
                         x["robust_removed_edges_lower_den"]))
            self.assertEqual(
                x["selected_nonspread_TRUE_physical_edges"],
                2*x["selected_original_points"]*x["s"])


if __name__=="__main__":
    unittest.main()
