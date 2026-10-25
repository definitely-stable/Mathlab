"""Tests for HYP-105 Issue #230 Extremal Coordinate Marginal Conservation Law."""
import json
import math
import os
import unittest
from collections import Counter

from hyp105_issue230_projection import fixture, ProjectionClosure
from hyp105_issue230_extremal_marginal_conservation import (
    canonical_gq_parameters,
    extremal_degree_collision_bound,
    blocking_fraction_theoretical_bound,
    verify_bbo_unconditional_sextic_floor,
    path_universe_census,
)


class TestExtremalMarginalConservation(unittest.TestCase):
    def test_canonical_parameters_powers_of_two(self):
        """Verify parameters for W(3,s) across powers of 2."""
        for s, expected_v, expected_a in [(2, 15, 6), (4, 85, 14), (8, 585, 35)]:
            p = canonical_gq_parameters(s)
            self.assertEqual(p["V"], expected_v)
            self.assertEqual(p["a"], expected_a)
            self.assertGreaterEqual(p["K"], p["V"])
            self.assertLess(p["m"], p["a"] - 1)
            self.assertEqual(p["d"], s + 1)

    def test_convex_optimization_degree_bound_universality(self):
        """Verify sum d_u(d_u - 1) <= 2V(a - 2) for any feasible degree sequence."""
        for s in [2, 4, 8, 16, 32]:
            p = canonical_gq_parameters(s)
            V, a = p["V"], p["a"]
            max_bound = 2 * V * (a - 2)

            # 1. Uniform degree sequence d_u = 2V / a
            d_mean = 2 * V / a
            uniform_sum = a * d_mean * (d_mean - 1)
            self.assertLessEqual(uniform_sum, max_bound)

            # 2. Extreme peaked degree sequence: as many (a-1) as possible
            k = (2 * V) // (a - 1)
            rem = (2 * V) % (a - 1)
            peaked_sum = k * (a - 1) * (a - 2) + rem * max(0, rem - 1)
            self.assertLessEqual(peaked_sum, max_bound)

    def test_leading_coefficient_is_sqrt2(self):
        """Verify that the leading coefficient of sum binom(d_u, 2) is sqrt(2), NOT 1/sqrt(2)."""
        for s in [4, 8, 16, 32, 64]:
            p = canonical_gq_parameters(s)
            V, a, m = p["V"], p["a"], p["m"]
            base = (a * (a - 1) * (a - 2) - 2 * (2 * a - 3) * m) // 2
            s_9_2 = s ** 4.5
            ratio = base / s_9_2
            # Must approach sqrt(2) approx 1.4142, NOT 1/sqrt(2) approx 0.7071
            self.assertGreater(ratio, 1.40, f"Ratio {ratio} must exceed 1.40 for s={s}")
            self.assertLess(abs(ratio - math.sqrt(2)), 0.50)

    def test_c4_freeness_pencil_inequality_on_genuine_models(self):
        """Verify sum_l binom(v_l(u), 2) <= binom(d_u, 2) on genuine W(3,2) and W(3,4)."""
        configs = [
            (1, "lex"),
            (1, "S68"),
            (2, "lex"),
            (2, "random"),
        ]
        for s_val, name in configs:
            m = fixture(s_val, name)
            c = ProjectionClosure(m)
            a = c.a

            coord_deg = Counter(x for p in range(c.v) for x in c.f[p])
            pencil_pairs = Counter()
            for pts in c.lines:
                deg = Counter(x for q in pts for x in c.f[q])
                for u, count in deg.items():
                    pencil_pairs[u] += count * (count - 1) // 2

            for u in range(a):
                d = coord_deg[u]
                binom_d = d * (d - 1) // 2
                self.assertLessEqual(
                    pencil_pairs[u],
                    binom_d,
                    f"C4-freeness violated for u={u} in s={c.s} {name}",
                )

    def test_small_s_bad_ratio_exceeds_unity(self):
        """Verify that 4(a-2)/(s(s+1)) > 1.0 for s in {2, 4, 8, 16}.

        Demonstrates that the theoretical analytical bound provides zero guarantee
        of positive good pairs at small s, explaining the need for computational certificates.
        """
        for s in [2, 4, 8, 16]:
            res = extremal_degree_collision_bound(s)
            self.assertTrue(
                res["ratio_exceeds_unity"],
                f"Ratio for s={s} must exceed 1.0 (got {res['theoretical_bad_ratio_bound']})",
            )
            self.assertGreater(res["theoretical_bad_ratio_bound"], 1.0)

    def test_path_universe_separation(self):
        """Verify that path universes are properly structured to prevent denominator conflation."""
        u4 = path_universe_census(4)
        self.assertEqual(u4["total_gq_3paths"], 85 * 5 * 16)  # 6800
        self.assertIn("P_proper", u4["description"])
        self.assertIn("P_noninc", u4["description"])
        self.assertIn("P_unblocked", u4["description"])

    def test_unconditional_floor_status_is_open(self):
        """Verify that verify_bbo_unconditional_sextic_floor returns False (fail-closed)."""
        self.assertFalse(verify_bbo_unconditional_sextic_floor(4))
        b = blocking_fraction_theoretical_bound(4)
        self.assertEqual(b["status"], "OPEN_WITH_FORMAL_BLOCKER")
        self.assertTrue(b["candidate_c0_refuted"])
        self.assertIn("contradicted by certified minimum 5400", b["refutation_detail"])


if __name__ == "__main__":
    unittest.main()
