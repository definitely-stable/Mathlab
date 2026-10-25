"""HYP-105 D6-AA4-E independent exact tiny-factor global injection tests."""
from fractions import Fraction
from itertools import permutations
import random
import unittest

from hyp105_issue230_d6aa4e_global_assignment_dual import (
    alphabet_capacity, dual_bound, exact_tiny_optimum, finite_toy_report,
    make_motif, min_cost_injection, true_w32_occupancy_falsifier)


class AssignmentDualTests(unittest.TestCase):
    def test_minimal_physical_pair_capacity_and_slack_all_h(self):
        for s, v, a, k, m in ((2, 15, 6, 15, 0), (4, 85, 14, 91, 6),
                               (8, 585, 35, 595, 10), (16, 4369, 94, 4371, 2)):
            r = alphabet_capacity(s)
            self.assertEqual((r["V"], r["a"], r["K"], r["m"]), (v, a, k, m))
            self.assertLess(m, a-1)
        for bad in (0, 1, 3, 6, 7, True, 2.0):
            with self.assertRaises(ValueError):
                alphabet_capacity(bad)

    def test_hungarian_against_independent_bruteforce_signed_fractions(self):
        rng = random.Random(230)
        for n in range(1, 5):
            for k in range(n, 6):
                for _ in range(8):
                    costs = [[Fraction(rng.randrange(-15, 16), rng.randrange(1, 5))
                              for _ in range(k)] for _ in range(n)]
                    value, matching = min_cost_injection(costs)
                    truth = min(sum(costs[i][j] for i, j in enumerate(t))
                                for t in permutations(range(k), n))
                    self.assertEqual(value, truth)
                    self.assertEqual(len(set(matching)), n)
        self.assertEqual(min_cost_injection([]), (0, ()))
        for invalid in ([[1], [1]], [[1, 2], [3]]):
            with self.assertRaises(ValueError):
                min_cost_injection(invalid)

    def test_real_capacity_and_coherence_fixtures(self):
        t = finite_toy_report()
        for name in ("physical_capacity_sharp", "shared_factor_coherence_sharp"):
            self.assertEqual(t[name], {"local_min_sum": 0, "dual": 1, "true_min": 1})
        self.assertEqual(t["Branch_A"], "OPEN")
        self.assertEqual(t["Branch_B"], "OPEN")
        self.assertFalse(t["universal_W3s_GF5_bound_proved"])

    def test_same_physical_edge_on_opposite_types_allowed(self):
        motifs = (make_motif((("P", 0), ("L", 0)), 2,
                             lambda t: int(t[0] != t[1])),)
        truth = exact_tiny_optimum(1, 1, 2, motifs)
        self.assertEqual(truth["globally_injective_states"], 4)
        self.assertEqual(truth["global_minimum"], 0)
        self.assertEqual(dual_bound(1, 1, 2, motifs)["dual_lower"], 0)

    def test_random_signed_duals_never_exceed_true_complete_typed_optimum(self):
        rng = random.Random(105)
        motifs = (
            make_motif((("P", 0), ("P", 1), ("L", 0)), 3,
                       lambda t: 2*int(t[0] != t[2]) + int(t[1] == t[2])),
            make_motif((("P", 1), ("L", 0)), 3,
                       lambda t: int((t[0] + t[1]) % 2 == 1)))
        exact = exact_tiny_optimum(2, 1, 3, motifs)["global_minimum"]
        for _ in range(80):
            prices = {(q, v, e): Fraction(rng.randrange(-6, 7), 3)
                      for q, (support, _) in enumerate(motifs)
                      for v in support for e in range(3)}
            self.assertLessEqual(dual_bound(2, 1, 3, motifs, prices)["dual_lower"], exact)

    def test_three_factor_cycle_rejects_entire_unary_dual_family(self):
        triangle = tuple(make_motif((("P", i), ("P", j)), 3,
                         lambda t: int(t[1] != (t[0]+1) % 3))
                         for i, j in ((0, 1), (1, 2), (0, 2)))
        truth = exact_tiny_optimum(3, 0, 3, triangle)
        self.assertEqual(truth["globally_injective_states"], 6)
        self.assertEqual(truth["global_minimum"], 1)
        self.assertEqual(dual_bound(3, 0, 3, triangle)["dual_lower"], 0)
        # Exact analytic proof: for each Q uniform three zero-cost states
        # give uniform singleton marginals; likewise uniform true injections.
        rng = random.Random(230)
        for _ in range(100):
            prices = {(q, v, e): Fraction(rng.randrange(-9, 10), 5)
                      for q, (support, _) in enumerate(triangle)
                      for v in support for e in range(3)}
            self.assertLessEqual(dual_bound(3, 0, 3, triangle, prices)["dual_lower"], 0)

    def test_fail_closed_complete_local_oracle_and_prices(self):
        m = make_motif((("P", 0),), 2, lambda t: int(t[0] == 0))
        with self.assertRaises(ValueError):
            dual_bound(1, 0, 2, ((m[0], {(0,): 0}),))
        with self.assertRaises(ValueError):
            dual_bound(1, 0, 2, (m,), {(0, ("P", 1), 0): 1})
        with self.assertRaises(ValueError):
            dual_bound(1, 0, 2, (m,), {(1, ("P", 0), 0): 1})
        with self.assertRaises(ValueError):
            exact_tiny_optimum(2, 0, 1, (m,))
        with self.assertRaises(ValueError):
            make_motif((("P", 0), ("P", 0)), 2, lambda t: 0)
        with self.assertRaises(ValueError):
            make_motif((("P", 0),), 2, lambda t: -1)

    def test_true_original_W32_identical_images_different_accepted_GF5(self):
        actual = true_w32_occupancy_falsifier()
        self.assertEqual((actual["S68"], actual["S72"]), (68, 72))
        self.assertTrue(actual["same_original_W32_geometry"])
        self.assertTrue(actual["same_left_and_right_occupied_K6_edges"])
        self.assertFalse(actual["image_occupancy_alone_determines_seven_S"])


if __name__ == "__main__":
    unittest.main()
