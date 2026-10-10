"""C20 genuine original global-left source and missing-edge C6 falsifiers."""
from itertools import combinations
from math import comb
import unittest

from hyp105_g5e2b3e1c20_global_left_c6 import (
    all_h_global_left_c6_lower, canonical_simple_six_cycles,
    finite_graph_C20_audit, genuine_W32_C20_report,
)


class C20GlobalLeftCyclePressureTests(unittest.TestCase):
    def test_every_power_s_has_strict_positive_integer_global_source_floor(self):
        for s in (2, 4, 8, 16, 32, 64, 128):
            d = all_h_global_left_c6_lower(s)
            a, t = (d["minimal_physical_coordinates"],
                    d["missing_physical_pair_edges"])
            self.assertLess(comb(a-1,2), d["original_GQ_points"])
            self.assertLessEqual(d["original_GQ_points"], comb(a,2))
            self.assertLess(t,a-1)
            self.assertGreater(d["certified_remaining_physical_six_cycles"],0)
            self.assertEqual(
                d["certified_remaining_physical_six_cycles"],
                60*comb(a,6)-24*t*comb(a-2,4))
            self.assertEqual(
                d["certified_distinct_original_left_A_sixsets_lower"],
                d["certified_remaining_physical_six_cycles"]*(s+1)**6)
            self.assertTrue(d["no_simultaneous_right_seven_class_lower"])
        self.assertEqual(
            all_h_global_left_c6_lower(2)[
                "certified_distinct_original_left_A_sixsets_lower"], 43740)
        self.assertEqual(
            all_h_global_left_c6_lower(4)[
                "certified_distinct_original_left_A_sixsets_lower"], 1701562500)

    def test_missing_one_physical_pair_destroys_exact_known_sixcycle_count(self):
        for a in (6, 7, 8):
            full = tuple(combinations(range(a),2))
            all_cycles = sum(1 for _ in canonical_simple_six_cycles(full,a))
            self.assertEqual(all_cycles,60*comb(a,6))
            missing = (0,1)
            after = sum(1 for _ in canonical_simple_six_cycles(
                (e for e in full if e != missing), a))
            self.assertEqual(all_cycles-after,24*comb(a-2,4))

    def test_multiple_GF4_adversarial_missing_edges_true_C6_enumeration(self):
        a = 14
        physical = tuple(combinations(range(a),2))
        self.assertEqual(len(physical),91)
        cases = (
            physical[:6],
            physical[-6:],
            tuple((0,x) for x in range(1,7)),
            ((0,1),(2,3),(4,5),(6,7),(8,9),(10,11)),
        )
        for removed in cases:
            self.assertEqual(len(set(removed)),6)
            edges = tuple(e for e in physical if e not in set(removed))
            audit = finite_graph_C20_audit(4,edges)
            self.assertGreaterEqual(
                audit["physical_six_cycles_actual"], 108900)
            self.assertEqual(
                audit["physical_six_cycles_certified_lower"],108900)
            self.assertGreaterEqual(
                audit["original_left_A_sixsets_actual_by_cycle_lifts"],
                audit["original_left_A_sixsets_certified_lower"])

    def test_independent_true_W32_global_source_matches_all_four_renamings(self):
        report = genuine_W32_C20_report()
        self.assertEqual(len(report["independent_original_sixset_evidence"]),4)
        self.assertEqual(
            report["all_h_s2_analytic_gate"][
                "certified_distinct_original_left_A_sixsets_lower"],43740)
        for case in report["independent_original_sixset_evidence"]:
            self.assertEqual(case["certified_Hamilton_sixcycle_source"],43740)
            self.assertEqual(case["true_left_A_sixsets"],51030)
            self.assertEqual(case["true_left_A_other_2triangle_sixsets"],7290)
            self.assertEqual(case["all_true_original_left_sixsets"],62370)

    def test_fake_pair_edges_wrong_occupancy_and_caps_fail_closed(self):
        for s in (0, 1, 3, 6, True):
            with self.assertRaises(ValueError):
                all_h_global_left_c6_lower(s)
        pairs = tuple(combinations(range(6),2))
        with self.assertRaises(ValueError):
            finite_graph_C20_audit(2,pairs[:-1])
        with self.assertRaises(ValueError):
            list(canonical_simple_six_cycles(pairs,6,max_vertices=5))
        with self.assertRaises(ValueError):
            list(canonical_simple_six_cycles(pairs+(pairs[0],),6))
        with self.assertRaises(ValueError):
            list(canonical_simple_six_cycles(((0,1),(1,0)),6))
        with self.assertRaises(ValueError):
            list(canonical_simple_six_cycles(((0,9),),6))
        with self.assertRaises(ValueError):
            finite_graph_C20_audit(4,tuple(combinations(range(14),2))[:85],
                                   max_vertices=10)


if __name__ == "__main__":
    unittest.main()
