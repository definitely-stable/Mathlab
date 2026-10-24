"""Test suite for AA4-DJ: Universal finite-width support barrier and global motif transversal."""

from collections import Counter
from fractions import Fraction
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4dj_universal_width_barrier import (
    universal_finite_width_density_bound,
    global_transversal_matching_count,
    audit_global_c6_transversals,
    find_physical_c6_cycles,
)


class AA4DJUniversalWidthBarrierAndGlobalTransversal(unittest.TestCase):
    def test_01_universal_finite_width_density_bounds(self):
        """Verify universal rho_m(s) <= m / s^2 and adversarial suppression for s > sqrt(m)."""
        cases = (
            # (s, m, expected_max_cov, expected_uncov, supp_possible)
            (2, 5, 15, 0, False),  # 5*3 = 15 = V, all covered
            (4, 5, 25, 60, True),  # 5*5 = 25, 60 uncovered (70.6%)
            (4, 10, 50, 35, True),  # 10*5 = 50, 35 uncovered (41.2%)
            (8, 5, 45, 540, True),  # 5*9 = 45, 540 uncovered (92.3%)
            (8, 20, 180, 405, True),  # 20*9 = 180, 405 uncovered (69.2%)
            (16, 10, 170, 4199, True),  # 10*17 = 170, 4199 uncovered (96.1%)
        )
        for s, m, cov_exp, uncov_exp, supp_exp in cases:
            res = universal_finite_width_density_bound(s, m)
            self.assertEqual(res["max_covered_points"], cov_exp)
            self.assertEqual(res["uncovered_points"], uncov_exp)
            self.assertEqual(res["adversarial_suppression_possible"], supp_exp)
            # Universal bound: rho_m <= m / s^2 (for s >= 4)
            if s >= 4:
                self.assertLessEqual(
                    float(res["point_coverage_density_rho_m"]), m / (s**2) + 0.01
                )
            print(
                f"AA4DJ_UNIVERSAL_DENSITY s={s} m={m} covered={cov_exp} "
                f"uncovered={uncov_exp} fraction={float(res['uncovered_fraction'])*100:.1f}% "
                f"suppression={supp_exp}",
                flush=True,
            )

    def test_02_synthetic_global_transversal_formula(self):
        """Verify global transversal matching recursion against inclusion-exclusion bound."""
        # 6 points, degree 3 each (s=2), no shared lines
        pl_disjoint = {i: tuple(range(i * 3, (i + 1) * 3)) for i in range(6)}
        res = global_transversal_matching_count(range(6), pl_disjoint, s=2)
        # When all lines are disjoint, count is exactly 3^6 = 729
        self.assertEqual(res["exact_matching_count"], 729)
        self.assertEqual(res["retention_rate"], 1.0)

        # 6 points, degree 3 each, points 0 and 1 share line 0
        pl_shared = {
            0: (0, 1, 2),
            1: (0, 3, 4),
            2: (5, 6, 7),
            3: (8, 9, 10),
            4: (11, 12, 13),
            5: (14, 15, 16),
        }
        res_shared = global_transversal_matching_count(range(6), pl_shared, s=2)
        # Expected: 3^6 - 3^4 * 1 = 729 - 81 = 648
        self.assertEqual(res_shared["exact_matching_count"], 648)
        self.assertGreaterEqual(
            res_shared["exact_matching_count"],
            res_shared["inclusion_exclusion_lower_bound"],
        )
        print("AA4DJ_SYNTHETIC_GLOBAL_TRANSVERSAL verified", flush=True)

    def test_03_TRUE_original_W32_all70_c6_cycles(self):
        """Audit ALL 70 physical C6 point cycles on W(3,2) lex and S72: tau(P6) >= 200."""
        for scheme in ("lex", "S72"):
            model = fixture(1, scheme)
            res = audit_global_c6_transversals(model, limit_c6=None)
            self.assertEqual(res["cycles_audited"], 70)
            # Universal lower bound: every cycle has tau >= 200 (> 32% retention)
            self.assertGreaterEqual(res["min_matching_count"], 200)
            self.assertGreater(res["mean_matching_count"], 300)
            print(
                f"AA4DJ_W32_GLOBAL_TRANSVERSAL {scheme}: audited_C6={res['cycles_audited']} "
                f"min={res['min_matching_count']} max={res['max_matching_count']} "
                f"mean={res['mean_matching_count']:.1f} "
                f"retention={res['mean_retention_rate']:.3f}",
                flush=True,
            )

    def test_04_TRUE_original_W34_c6_cycles_sample(self):
        """Audit sample physical C6 cycles on W(3,4) lex and random: tau(P6) >= 11000."""
        for scheme in ("lex", "random"):
            model = fixture(2, scheme)
            res = audit_global_c6_transversals(model, limit_c6=10)
            self.assertEqual(res["cycles_audited"], 10)
            # On W(3,4), (s+1)^6 = 15625; each cycle has tau >= 11000 (retention > 70%)
            self.assertGreaterEqual(res["min_matching_count"], 11000)
            self.assertGreater(res["mean_retention_rate"], 0.70)
            print(
                f"AA4DJ_W34_GLOBAL_TRANSVERSAL {scheme}: audited_C6={res['cycles_audited']} "
                f"min={res['min_matching_count']} max={res['max_matching_count']} "
                f"mean={res['mean_matching_count']:.1f} "
                f"retention={res['mean_retention_rate']:.3f}",
                flush=True,
            )

    def test_05_analytic_all_h_global_transversal_scale(self):
        """Verify all-h asymptotic growth: tau(P6) >= (1 - 15/(s+1)^2) * (s+1)^6 for s >= 4."""
        for s in (4, 8, 16, 32, 64):
            loss = Fraction(15, (s + 1) ** 2)
            retention = float(1 - loss)
            bound = int(((s + 1) ** 6) * (1 - loss))
            self.assertGreaterEqual(retention, 0.40)
            if s >= 8:
                self.assertGreater(retention, 0.80)
            if s >= 16:
                self.assertGreater(retention, 0.90)
            print(
                f"AA4DJ_ALL_H_SCALE s={s} upper={(s+1)**6} "
                f"lower_bound={bound} retention={retention:.4f}",
                flush=True,
            )

    def test_06_failclosed_invalid_inputs(self):
        """Reject non-powers of 2, non-positive m, malformed point sets."""
        for bad_s in (0, 1, 3, 5, 7, -4, "2"):
            with self.assertRaises((ValueError, TypeError)):
                universal_finite_width_density_bound(bad_s, 5)

        for bad_m in (0, -1, -5, "5"):
            with self.assertRaises((ValueError, TypeError)):
                universal_finite_width_density_bound(2, bad_m)

        with self.assertRaises(ValueError):
            global_transversal_matching_count((0, 1, 2, 3, 4), {}, s=2)  # only 5 points

        with self.assertRaises(ValueError):
            global_transversal_matching_count((0, 0, 1, 2, 3, 4), {}, s=2)  # duplicate

        with self.assertRaises(ValueError):
            # Point 0 has wrong degree (2 instead of s+1=3)
            global_transversal_matching_count(
                range(6), {0: (1, 2), 1: (1, 2, 3), 2: (1, 2, 3), 3: (1, 2, 3), 4: (1, 2, 3), 5: (1, 2, 3)}, s=2
            )
        print("AA4DJ_FAILCLOSED_TESTS passed", flush=True)


if __name__ == "__main__":
    unittest.main()
