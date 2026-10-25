"""Test suite for AA4-DK: Sparse covariance decoupling and orbit concentration audit."""

from fractions import Fraction
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4dk_sparse_covariance_decoupling import (
    gq_line_overlap_distribution,
    measure_sampled_flag_line_overlaps,
    exact_k6_two_factor_covariance,
    exact_r0_covariance_sign,
    variance_ratio_decay_bound,
)


class AA4DKSparseCovarianceDecoupling(unittest.TestCase):
    def test_01_exact_line_overlap_hypergeometric_distribution(self):
        """Verify exact rational probabilities P(R=r) and >94% at s=4, >99.8% at s=8."""
        cases = (
            (2, 0.15),  # small s has more overlap
            (4, 0.94),  # s=4: 94.47% share <= 1
            (8, 0.998),  # s=8: 99.87% share <= 1
            (16, 0.9998),  # s=16: 99.98% share <= 1
        )
        for s, min_pct in cases:
            res = gq_line_overlap_distribution(s)
            self.assertEqual(res["s"], s)
            self.assertEqual(sum(res["probabilities"].values()), 1)
            self.assertGreaterEqual(res["share_at_most_1_float"], min_pct)

    def test_02_k6_counterexample_positive_covariance(self):
        """Verify the exact K_6 counterexample: disjoint 2-factors have STRICTLY POSITIVE covariance."""
        k6 = exact_k6_two_factor_covariance()
        self.assertEqual(k6["num_two_factors"], 70)
        self.assertEqual(k6["disjoint_pairs_count"], 300)
        self.assertEqual(k6["total_disjoint_6_pairs"], 420420)
        self.assertEqual(k6["p_A"], Fraction(2, 143))
        self.assertEqual(k6["p_joint"], Fraction(5, 7007))
        self.assertEqual(k6["covariance"], Fraction(519, 1002001))
        self.assertTrue(k6["is_strictly_positive"])
        self.assertGreater(float(k6["covariance"]), 0.0)

        # Naive formula audit shows negative sign for independent subsets but fails for 2-factors
        naive = exact_r0_covariance_sign(15, Fraction(2, 143))
        self.assertTrue(naive["naive_formula_negative"])
        self.assertFalse(naive["universal_negative_covariance_holds"])

    def test_03_TRUE_original_W32_empirical_sampled_overlaps(self):
        """Sample genuine 6-flags with distinct endpoints on W(3,2) lex and S72."""
        for scheme in ("lex", "S72"):
            model = fixture(1, scheme)
            res = measure_sampled_flag_line_overlaps(model, num_samples=60, seed=42)
            self.assertGreaterEqual(res["num_flags_sampled"], 25)
            self.assertGreater(res["total_pairs_evaluated"], 100)

    def test_04_TRUE_original_W34_empirical_overlap_sparsity(self):
        """Verify empirical fraction of pairs sharing <= 1 line exceeds 88% on W(3,4)."""
        for scheme in ("lex", "random"):
            model = fixture(2, scheme)
            res = measure_sampled_flag_line_overlaps(model, num_samples=100, seed=42)
            self.assertGreaterEqual(res["num_flags_sampled"], 50)
            self.assertGreaterEqual(res["empirical_fraction_at_most_1"], 0.88)

    def test_05_variance_ratio_open_conjecture_status(self):
        """Verify variance ratio bound is marked OPEN_CONJECTURE_UNPROVEN."""
        for s in (2, 4, 8, 16):
            res = variance_ratio_decay_bound(s)
            self.assertEqual(res["status"], "OPEN_CONJECTURE_UNPROVEN")
            self.assertEqual(res["heuristic_variance_ratio_conjecture"], Fraction(10, s))

    def test_06_failclosed_invalid_inputs(self):
        """Reject non-powers of 2, invalid dimensions, non-positive parameters."""
        for bad_s in (0, 1, 3, 5, 7, -2, "8"):
            with self.assertRaises((ValueError, TypeError)):
                gq_line_overlap_distribution(bad_s)

        for bad_s in (0, 1, 3, 5, -8):
            with self.assertRaises((ValueError, TypeError)):
                variance_ratio_decay_bound(bad_s)

        with self.assertRaises(ValueError):
            exact_r0_covariance_sign(10, Fraction(1, 100))  # V <= 12

        with self.assertRaises(ValueError):
            exact_r0_covariance_sign(20, -1)  # p_A <= 0


if __name__ == "__main__":
    unittest.main()
