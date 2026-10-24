"""Independent tests for HYP-105 Phase 2: Janson Dependency Inequality & Calibrated Cheeger Infimum.

Fast, self-contained, standard-library regression suite (< 0.1s execution).
"""
import unittest

from hyp105_exponential_concentration import (
    bipartite_cheeger_constant,
    calibrated_cheeger_infimum,
    flag_overlap_covariance_spectrum,
    janson_dependency_chernoff_bound,
    verify_calibrated_w32_envelope,
)


class Hyp105Phase2Tests(unittest.TestCase):
    def test_01_bipartite_cheeger_constant(self):
        """Verify bipartite Cheeger isoperimetric constant and asymptotic limit 0.5."""
        ch2 = bipartite_cheeger_constant(2)
        self.assertAlmostEqual(ch2["cheeger_lower_bound"], 1.0 / 6.0, places=5)
        self.assertEqual(ch2["d"], 3)
        self.assertAlmostEqual(ch2["lambda_2"], 2.0, places=5)

        # Monotonic convergence of h(G) -> 0.5
        prev_h = ch2["cheeger_lower_bound"]
        for s in (4, 8, 16, 32, 64, 128, 256):
            ch = bipartite_cheeger_constant(s)
            self.assertGreater(ch["cheeger_lower_bound"], prev_h)
            self.assertLess(ch["cheeger_lower_bound"], 0.5)
            prev_h = ch["cheeger_lower_bound"]

        ch256 = bipartite_cheeger_constant(256)
        self.assertGreater(ch256["cheeger_lower_bound"], 0.45)

    def test_02_calibrated_cheeger_infimum_positivity(self):
        """Verify analytical pointwise infimum positivity across all dyadic field extensions."""
        for s in (2, 4, 8, 16, 32, 64, 128, 256):
            inf = calibrated_cheeger_infimum(s)
            self.assertTrue(inf["strictly_positive"])
            self.assertGreater(inf["cheeger_infimum_coeff"], 0.0)
            self.assertGreater(inf["cheeger_floor_s6"], 0.0)

        # Asymptotic coefficient limit ~ 9.140625 (at s=256, reaches > 7.5)
        inf256 = calibrated_cheeger_infimum(256)
        self.assertGreater(inf256["cheeger_infimum_coeff"], 7.5)
        self.assertLessEqual(inf256["cheeger_infimum_coeff"], 9.2)

    def test_03_janson_dependency_chernoff_exponential_decay(self):
        """Verify subexponential Janson tail bounds for sparse dependency graph."""
        # For s = 2, exponent should already be negative
        b2 = janson_dependency_chernoff_bound(2, epsilon=0.5)
        self.assertLess(b2["janson_exponent"], 0.0)

        # For s >= 4, exponent is intensely negative, guaranteeing tail_prob == 0.0 in float64
        for s in (4, 8, 16, 32):
            b = janson_dependency_chernoff_bound(s, epsilon=0.5)
            self.assertTrue(b["is_superexponentially_small"])
            self.assertLess(b["log_tail_probability"], -100.0)
            self.assertEqual(b["tail_probability"], 0.0)

    def test_04_flag_overlap_covariance_spectrum(self):
        """Verify that disjoint pairs have Cov_0 < 0 while overlapping pairs have Cov_r > 0.

        Rigorously demonstrates why raw Negative Association fails and Janson applies.
        """
        for s in (2, 4, 8, 16):
            spec = flag_overlap_covariance_spectrum(s)
            self.assertTrue(spec["cov0_strictly_negative"])
            self.assertTrue(spec["overlapping_pairs_have_positive_covariance"])
            self.assertFalse(spec["full_negative_association_satisfied"])
            self.assertTrue(spec["sparse_dependency_graph_applicable"])

    def test_05_verify_calibrated_w32_envelope_strict_lower_bound(self):
        """Verify genuine W(3,2) calibrated envelope strictly satisfies floor <= empirical_min_S."""
        env = verify_calibrated_w32_envelope()
        self.assertEqual(env["s"], 2)
        self.assertEqual(env["empirical_min_S"], 68)
        self.assertEqual(env["cheeger_floor_s6"], 65.0)
        self.assertTrue(env["strictly_positive"])
        # THE CRITICAL AUDITED LOWER-BOUND TEST:
        self.assertTrue(env["is_valid_lower_bound"])
        self.assertLessEqual(env["cheeger_floor_s6"], env["empirical_min_S"])

    def test_06_failclosed_invalid_inputs(self):
        """Reject invalid epsilon and non-dyadic s fail-closed."""
        # Fail-closed invalid epsilon
        for bad_eps in (0.0, 1.0, -0.5, 1.5, "0.5"):
            with self.assertRaises((ValueError, TypeError)):
                janson_dependency_chernoff_bound(4, epsilon=bad_eps)

        # Fail-closed invalid s
        for bad_s in (0, 1, 3, 5, 6, 7, 9, 10, -2, 2.5):
            with self.assertRaises((ValueError, TypeError)):
                bipartite_cheeger_constant(bad_s)


if __name__ == "__main__":
    unittest.main()
