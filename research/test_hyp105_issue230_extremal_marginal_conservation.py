"""Tests for HYP-105 Issue #230 Extremal Coordinate Marginal Conservation Law."""
import json
import os
import unittest
from collections import Counter

from hyp105_issue230_projection import fixture, ProjectionClosure
from hyp105_issue230_d5_retained_energy import true_spread_global_model
from hyp105_issue230_extremal_marginal_conservation import (
    canonical_gq_parameters,
    extremal_degree_collision_bound,
    blocking_fraction_theoretical_bound,
    verify_bbo_unconditional_sextic_floor,
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

            # Compute d_u for all u
            coord_deg = Counter(x for p in range(c.v) for x in c.f[p])

            # Compute v_l(u) for each line l and coordinate u
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

    def test_exterior_bad_endpoint_pairs_bound(self):
        """Verify that actual endpoint bad pairs never exceed the theoretical bound."""
        from hyp105_issue230_anchor_blocking import _original_endpoint_pair_census

        for s_val, name in [(1, "lex"), (1, "S68"), (2, "lex"), (2, "random")]:
            m = fixture(s_val, name)
            c = ProjectionClosure(m)
            census, _, _ = _original_endpoint_pair_census(c)
            actual_bad = census["union_endpoint_bad_pair_count"]

            b = extremal_degree_collision_bound(c.s)
            self.assertLess(actual_bad, b["max_bad_endpoint_pairs"])

    def test_c0_monotonic_positivity_and_convergence(self):
        """Verify that c_0(s) > 0 for all s >= 4 and increases monotonically."""
        c0_vals = []
        for s in [4, 8, 16, 32, 64]:
            res = blocking_fraction_theoretical_bound(s)
            self.assertGreater(res["c_0"], 0.0)
            self.assertLess(res["beta_max"], 1.0)
            self.assertEqual(res["status"], "PROVED_UNCONDITIONAL")
            c0_vals.append((s, res["c_0"]))

        # Verify strict positivity and asymptotic growth
        self.assertGreaterEqual(c0_vals[0][1], 0.176)  # s=4
        self.assertGreaterEqual(c0_vals[1][1], 0.556)  # s=8
        for i in range(len(c0_vals) - 1):
            self.assertLess(c0_vals[i][1], c0_vals[i + 1][1])

    def test_unconditional_sextic_overlap_floor(self):
        """Verify BBo(f, g) >= 8 c_0 s^6 = Omega(s^6) unconditionally."""
        for s in [4, 8, 16, 32]:
            self.assertTrue(verify_bbo_unconditional_sextic_floor(s))
            res = blocking_fraction_theoretical_bound(s)
            # Must strictly exceed 1.0 * s^6 for all s >= 4
            self.assertGreater(res["bbo_ratio_s6"], 1.0)

    def test_w34_adversarial_results_consistency(self):
        """Verify theory against the 10 adversarial optimization runs on W(3,4)."""
        json_path = os.path.join(
            os.path.dirname(__file__), "hyp105_w34_adversarial_results.json"
        )
        if not os.path.exists(json_path):
            self.skipTest("Adversarial JSON results not present")

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        s6 = 4096
        for run_name, run_data in data.items():
            final_bbo = run_data["final_bbo"]
            ratio = run_data["final_ratio"]
            census = run_data["census"]
            blocked_ratio = census["blocked_ratio"]

            # Theory states beta <= 0.824, leaving >= 17.6% unblocked
            self.assertLessEqual(blocked_ratio, 0.824)
            # Final BBo must remain strictly positive and above 1.0 s^6
            self.assertGreater(final_bbo, s6)
            self.assertGreater(ratio, 1.30)


if __name__ == "__main__":
    unittest.main()
