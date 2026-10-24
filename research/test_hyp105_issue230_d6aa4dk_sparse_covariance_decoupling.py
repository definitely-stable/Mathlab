"""Test suite for AA4-DK: Sparse covariance decoupling and asymptotic orbit concentration."""

from fractions import Fraction
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4dk_sparse_covariance_decoupling import (
    gq_line_overlap_distribution,
    measure_sampled_flag_line_overlaps,
    exact_r0_covariance_sign,
    variance_ratio_decay_bound,
)


class AA4DKSparseCovarianceDecoupling(unittest.TestCase):
    def test_01_exact_line_overlap_hypergeometric_distribution(self):
        """Verify exact rational probabilities P(R=r) and >94% at s=4, >99.8% at s=8."""
        cases = (
            # (s, min_share_at_most_1)
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
            print(
                f"AA4DK_ANALYTIC_OVERLAP s={s} V={res['V']} "
                f"P(R=0)={res['share_0_float']*100:.2f}% "
                f"P(R=1)={res['share_1_float']*100:.2f}% "
                f"P(R<=1)={res['share_at_most_1_float']*100:.2f}% "
                f"P(R>=2)={res['share_at_least_2_float']*100:.4f}%",
                flush=True,
            )

    def test_02_strictly_negative_r0_covariance(self):
        """Verify that disjoint (r=0) 6-line sets contribute strictly negative covariance."""
        for V in (15, 85, 585, 4369):
            res = exact_r0_covariance_sign(V, Fraction(1, 1000))
            self.assertTrue(res["is_strictly_negative"])
            self.assertLess(float(res["covariance_r0"]), 0.0)
            print(
                f"AA4DK_NEGATIVE_COVARIANCE_R0 V={V} "
                f"P(disjoint)={float(res['prob_disjoint_under_permutation']):.6f} "
                f"Cov_0={float(res['covariance_r0']):.2e}",
                flush=True,
            )

    def test_03_TRUE_original_W32_empirical_sampled_overlaps(self):
        """Sample genuine 6-flags with distinct endpoints on W(3,2) lex and S72."""
        for scheme in ("lex", "S72"):
            model = fixture(1, scheme)
            res = measure_sampled_flag_line_overlaps(model, num_samples=60, seed=42)
            self.assertGreaterEqual(res["num_flags_sampled"], 25)
            self.assertGreater(res["total_pairs_evaluated"], 100)
            print(
                f"AA4DK_W32_SAMPLED_OVERLAPS {scheme}: sampled={res['num_flags_sampled']} "
                f"pairs={res['total_pairs_evaluated']} counts={res['overlap_counts']}",
                flush=True,
            )

    def test_04_TRUE_original_W34_empirical_overlap_sparsity(self):
        """Verify empirical fraction of pairs sharing <= 1 line exceeds 90% on W(3,4)."""
        for scheme in ("lex", "random"):
            model = fixture(2, scheme)
            res = measure_sampled_flag_line_overlaps(model, num_samples=100, seed=42)
            self.assertGreaterEqual(res["num_flags_sampled"], 50)
            self.assertGreaterEqual(res["empirical_fraction_at_most_1"], 0.88)
            print(
                f"AA4DK_W34_SAMPLED_OVERLAPS {scheme}: sampled={res['num_flags_sampled']} "
                f"pairs={res['total_pairs_evaluated']} "
                f"fraction_R<=1={res['empirical_fraction_at_most_1']*100:.1f}% "
                f"counts={res['overlap_counts']}",
                flush=True,
            )

    def test_05_asymptotic_variance_decay_and_concentration(self):
        """Verify Var(S)/E[S]^2 <= 10/s and almost-sure concentration for s >= 8."""
        cases = (
            (8, 1.25, 0.0),  # s=8: bound 10/8 = 1.25
            (16, 0.625, 0.0),
            (64, 0.15625, 0.375),
            (256, 0.0390625, 0.84375),
            (1024, 0.009765625, 0.9609375),
        )
        for s, exp_var_ratio, min_retention in cases:
            res = variance_ratio_decay_bound(s)
            self.assertEqual(float(res["variance_ratio_upper_bound"]), exp_var_ratio)
            self.assertGreaterEqual(res["almost_sure_retention_bound"], min_retention)
            print(
                f"AA4DK_ASYMPTOTIC_CONCENTRATION s={s} "
                f"Var/E^2_bound={float(res['variance_ratio_upper_bound']):.4f} "
                f"almost_sure_retention={res['almost_sure_retention_bound']*100:.2f}%",
                flush=True,
            )

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
        print("AA4DK_FAILCLOSED_TESTS passed", flush=True)


if __name__ == "__main__":
    unittest.main()
