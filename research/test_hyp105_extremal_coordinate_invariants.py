"""Tests for HYP-105 Extremal Coordinate Invariants on W(3,s)."""
import math
import unittest

from hyp105_extremal_coordinate_invariants import (
    canonical_gq_parameters,
    extremal_degree_collision_bound,
    path_universe_census,
    formal_resolution_status,
)


class TestExtremalCoordinateInvariants(unittest.TestCase):
    def test_canonical_parameters_powers_of_two(self):
        """Verify parameters for W(3,s) across powers of 2."""
        for s, expected_v, expected_a in [(2, 15, 6), (4, 85, 14), (8, 585, 35)]:
            p = canonical_gq_parameters(s)
            self.assertEqual(p["V"], expected_v)
            self.assertEqual(p["a"], expected_a)
            self.assertGreaterEqual(p["K"], p["V"])
            self.assertLessEqual(p["m"], p["a"] - 2)
            self.assertEqual(p["d"], s + 1)

    def test_convex_optimization_degree_bound_universality(self):
        """Verify sum d_u(d_u - 1) <= 2V(a - 2) for uniform and peaked distributions."""
        for s in [2, 4, 8, 16, 32]:
            p = canonical_gq_parameters(s)
            V, a = p["V"], p["a"]
            max_bound = 2 * V * (a - 2)

            # Uniform degree sequence
            d_mean = 2 * V / a
            uniform_sum = a * d_mean * (d_mean - 1)
            self.assertLessEqual(uniform_sum, max_bound)

            # Peaked degree sequence
            k = (2 * V) // (a - 1)
            rem = (2 * V) % (a - 1)
            peaked_sum = k * (a - 1) * (a - 2) + rem * max(0, rem - 1)
            self.assertLessEqual(peaked_sum, max_bound)

    def test_leading_coefficient_is_sqrt2(self):
        """Verify leading coefficient of sum binom(d_u, 2) is sqrt(2), NOT 1/sqrt(2)."""
        for s in [4, 8, 16, 32, 64]:
            deg = extremal_degree_collision_bound(s)
            s_9_2 = s ** 4.5
            ratio = deg["base_pair_sum"] / s_9_2
            # Must approach sqrt(2) approx 1.4142, NOT 1/sqrt(2) approx 0.7071
            self.assertGreater(ratio, 1.40, f"Ratio {ratio} must exceed 1.40 for s={s}")
            self.assertLess(abs(ratio - math.sqrt(2)), 0.50)

    def test_small_s_bad_ratio_exceeds_unity(self):
        """Verify 4(a-2)/(s(s+1)) > 1.0 for s in {2, 4, 8, 16}.

        Demonstrates that analytical bound alone provides zero guaranteed positive
        floor on good pairs at small s, explaining the need for computational certificates.
        """
        for s in [2, 4, 8, 16]:
            deg = extremal_degree_collision_bound(s)
            self.assertTrue(deg["ratio_exceeds_unity"])
            self.assertGreater(deg["theoretical_bad_ratio_bound"], 1.0)

        # For s >= 32, ratio drops below 1.0
        for s in [32, 64]:
            deg = extremal_degree_collision_bound(s)
            self.assertFalse(deg["ratio_exceeds_unity"])
            self.assertLess(deg["theoretical_bad_ratio_bound"], 1.0)

    def test_path_universe_separation(self):
        """Verify path universes are distinguished to prevent denominator conflation."""
        u4 = path_universe_census(4)
        self.assertEqual(u4["total_gq_3paths"], 85 * 5 * 16)  # 6800
        self.assertIn("P_proper", u4["universes"])
        self.assertIn("P_noninc", u4["universes"])
        self.assertIn("P_unblocked", u4["universes"])

    def test_formal_resolution_status(self):
        """Verify fail-closed governance and certified counterexample reporting."""
        status = formal_resolution_status()
        self.assertEqual(status["status"], "OPEN_WITH_FORMAL_BLOCKER")
        self.assertEqual(len(status["formal_blockers"]), 3)
        self.assertTrue(status["certified_counterexample_w34"]["candidate_floor_5768_refuted"])
        self.assertGreaterEqual(status["certified_counterexample_w34"]["deficit"], 368)


if __name__ == "__main__":
    unittest.main()
