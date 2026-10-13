"""Exact reference-independent checks of the ORIGINAL endpoint-pair collision tensor."""
from collections import Counter
from fractions import Fraction
import unittest

from hyp105_issue230_jpkc002_path_collision_taxonomy import (
    GOOD, BLOCKED, STATUS, KINDS, collision_certificate, _edge_incidence_map,
)
from hyp105_issue230_projection import ProjectionClosure, fixture


class JPKC002Tests(unittest.TestCase):
    def test_true_original_K6_four_global_injections_and_seven_gf5(self):
        expected={
            "lex":(1346,15,259),
            "reverse":(1154,3,169),
            "S68":(678,0,68),
            "S72":(738,0,72),
        }
        for scheme,(p3good,d6,S) in expected.items():
            with self.subTest(scheme=scheme):
                r=collision_certificate(fixture(1,scheme),compare_seven=True)
                self.assertEqual(r["P3_good_coordinate_proper"],p3good)
                self.assertEqual(r["proper_D6_from_collision"],d6)
                self.assertEqual(r["true_original_seven_S"],S)
                self.assertTrue(r["J3_exact_identity_verified"])
                self.assertTrue(r["J4_exact_blocked_only_identity_verified"])
                self.assertTrue(r["J5_single_original_projection_anchor_verified"])
                self.assertEqual(r["J5_original_nonincident_qr_anchors"],180)
                self.assertEqual(r["J5_possible_oriented_endpoint_fibers"],720)
                self.assertLessEqual(r["J5_active_blocked_endpoint_fibers"],720)
                self.assertGreaterEqual(Fraction(r["J4_blocked_only_falling2"]),
                                        Fraction(r["J5_anchored_CS_floor_exact"]))
                self.assertGreaterEqual(Fraction(r["J5_anchored_CS_floor_exact"]),
                                        Fraction(r["J4_blocked_only_CS_floor"]))
                self.assertEqual(r["J4_blocked_original_P3"],
                                 sum(r["proper_P3_status_counts"][t]
                                     for t in BLOCKED))
                self.assertEqual(r["J4_blocked_only_falling2"],
                                 sum(r["J4_blockedblocked_ordered_distinct"].values()))
                self.assertGreaterEqual(
                    Fraction(r["J4_blocked_only_falling2"]),
                    Fraction(r["J4_blocked_only_CS_floor"]))
                self.assertTrue(r["full_K2_Theta_checked"])
                self.assertFalse(r["universal_S_lower_PROVED_A"])
                self.assertEqual(
                    sum(r["proper_P3_status_counts"][t] for t in GOOD),p3good)
                self.assertEqual(
                    sum(r["proper_P3_status_counts"].values()),r["P3_all"])
                self.assertEqual(
                    sum(r["collision_kinds"].values()),r["ordered_pair_count"])
                self.assertEqual(
                    sum(r["ordered_collision_tensor"].values()),r["ordered_pair_count"])
                self.assertEqual(
                    r["collision_kinds"]["proper_C6"],12*d6)
                self.assertEqual(r["cycle_ordered_repeated_original_incidences"]["proper_C6"],0)

    def test_true_original_W34_K1_K2_exact_pins_and_good_collision_mass(self):
        expected={
            "lex":(132644,8481,127684),
            "random":(122764,7295,89548),
        }
        for scheme,(P3,D6,Theta) in expected.items():
            with self.subTest(scheme=scheme):
                r=collision_certificate(fixture(2,scheme))
                self.assertEqual(r["P3_all"],P3)
                self.assertEqual(r["proper_D6_from_collision"],D6)
                self.assertEqual(r["collision_kinds"]["shared_internal"],Theta)
                self.assertEqual(
                    r["J3_goodgood_falling2"],
                    12*D6+
                    r["goodgood_ordered_distinct"]["shared_internal"]+
                    r["goodgood_ordered_distinct"]["improper_C6"])
                self.assertGreaterEqual(Fraction(r["J3_goodgood_endpoint_variance"]),0)
                self.assertEqual(r["J4_blocked_only_falling2"],
                                 sum(r["J4_blockedblocked_ordered_distinct"].values()))
                self.assertLessEqual(
                    r["J4_blockedblocked_ordered_distinct"]["proper_C6"],
                    12*D6)
                self.assertEqual(r["J5_original_nonincident_qr_anchors"],6800)
                self.assertEqual(r["J5_possible_oriented_endpoint_fibers"],27200)
                self.assertGreaterEqual(Fraction(r["J4_blocked_only_falling2"]),
                                        Fraction(r["J5_anchored_CS_floor_exact"]))
                self.assertGreaterEqual(
                    Fraction(r["J3_goodgood_falling2"]),
                    Fraction(r["J3_proper_only_CS_floor"]))

    def test_D4_actual_symplectic_spread_W34_joint_taxonomy(self):
        from hyp105_issue230_jpkc_spread_adversary import spread_adversary_model
        model,cert=spread_adversary_model(2)
        r=collision_certificate(model,max_ordered_pairs=8_000_000)
        self.assertGreaterEqual(cert["M_f_original_exact"],30)
        self.assertGreater(r["P3_good_coordinate_proper"],0)
        self.assertEqual(
            r["collision_kinds"]["proper_C6"],
            12*r["proper_D6_from_collision"])
        self.assertTrue(r["J3_exact_identity_verified"])

    def test_independent_canonical_original_edge_reconstruction(self):
        for scheme in ("lex","reverse","S68"):
            c=ProjectionClosure(fixture(1,scheme))
            mapping=_edge_incidence_map(c)
            self.assertEqual(len(mapping),2*len(c.edges))
            self.assertEqual(set(mapping.values()),set(range(len(c.edges))))
            self.assertTrue(all(sum(x==i for x in mapping.values())==2
                                for i in range(len(c.edges))))

    def test_fail_closed_budgets_invalid_original_injection_and_wrong_seven_scope(self):
        model=fixture(1,"lex")
        with self.assertRaisesRegex(ValueError,"path budget"):
            collision_certificate(model,max_paths=1)
        with self.assertRaisesRegex(ValueError,"collision-pair budget"):
            collision_certificate(model,max_ordered_pairs=1)
        bad=fixture(1,"lex")
        f=list(bad["left_labels"])
        f[0]=f[1]
        bad["left_labels"]=tuple(f)
        with self.assertRaises(ValueError):
            collision_certificate(bad)
        with self.assertRaisesRegex(ValueError,"W32"):
            collision_certificate(fixture(2,"lex"),compare_seven=True)


if __name__=="__main__":
    unittest.main()
