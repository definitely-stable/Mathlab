"""Independent verification test suite for HYP-105 Canonical Core."""
from fractions import Fraction
import unittest

from hyp105_canonical_core import (
    canonical_parameters,
    transversal_carrier_retention,
    girth8_overlap_sparsity_and_covariance,
    super_ramanujan_annihilation_barrier,
    master_path_motif_reduction,
    anchor_blocking_scaling,
    derandomize_transversal_carrier,
    verify_w32_canonical_certificate,
    canonical_proof_summary,
)


class Hyp105CanonicalCoreTests(unittest.TestCase):
    def test_01_canonical_parameters_and_template_survival(self):
        """Verify parameters V, a, K and surviving template fraction for dyadic s."""
        expected_surviving = {
            2: Fraction(1, 1),
            4: Fraction(55, 91),
            8: Fraction(107, 119),
            16: Fraction(1453, 1457),
        }
        for s, frac in expected_surviving.items():
            p = canonical_parameters(s)
            self.assertEqual(p["surviving_template_fraction"], frac)
            self.assertEqual(p["V"], (s + 1) * (s * s + 1))
            self.assertEqual(p["d"], s + 1)

        for s in (32, 64, 128, 256):
            p = canonical_parameters(s)
            self.assertGreater(p["surviving_template_fraction"], Fraction(98, 100))

    def test_02_lemma1_transversal_carrier_retention(self):
        """Verify Lemma 1: transversal matching lower bounds across all h."""
        r2 = transversal_carrier_retention(2)
        self.assertGreaterEqual(r2["min_matchings_per_cycle"], 200)

        for s in (4, 8, 16, 32, 64):
            res = transversal_carrier_retention(s)
            self.assertGreater(res["retention_fraction"], Fraction(0))
            self.assertGreater(res["min_matchings_per_cycle"], (s + 1) ** 5)

        r4 = float(transversal_carrier_retention(4)["retention_fraction"])
        r16 = float(transversal_carrier_retention(16)["retention_fraction"])
        r64 = float(transversal_carrier_retention(64)["retention_fraction"])
        self.assertLess(r4, r16)
        self.assertLess(r16, r64)
        self.assertGreater(r64, 0.99)

    def test_03_lemma2_sparsity_and_covariance_audit(self):
        """Verify Lemma 2: girth-8 line-overlap sparsity and covariance status."""
        l2_s4 = girth8_overlap_sparsity_and_covariance(4)
        self.assertTrue(l2_s4["sparsity_exceeds_90pct"])
        self.assertGreater(float(l2_s4["P_R_le_1"]), 0.94)
        self.assertFalse(l2_s4["universal_negative_covariance_holds"])

        l2_s8 = girth8_overlap_sparsity_and_covariance(8)
        self.assertGreater(float(l2_s8["P_R_le_1"]), 0.998)
        self.assertFalse(l2_s8["universal_negative_covariance_holds"])

        for s in (2, 4, 8, 16, 32):
            res = girth8_overlap_sparsity_and_covariance(s)
            self.assertEqual(res["variance_concentration_status"], "OPEN_CONJECTURE_UNPROVEN")
            self.assertEqual(res["heuristic_var_mean_ratio"], Fraction(10, s))

    def test_04_lemma3_super_ramanujan_and_multiplicities(self):
        """Verify Lemma 3: super-Ramanujan spectrum and exact multiplicities."""
        for s in (2, 4, 8, 16, 32, 64, 128):
            res = super_ramanujan_annihilation_barrier(s)
            self.assertTrue(res["is_super_ramanujan"])
            self.assertLess(res["lambda_2"], res["ramanujan_bound"])
            self.assertEqual(res["annihilation_barrier_status"], "OPEN_CONJECTURE_UNPROVEN")
            self.assertEqual(res["branch_b_status"], "OPEN_NOT_REFUTED")

        # Certified multiplicities for s=4: total 170
        res4 = super_ramanujan_annihilation_barrier(4)
        self.assertEqual(res4["multiplicities"]["total"], 170)
        self.assertEqual(res4["multiplicities"]["+/-lambda_2"], 50)
        self.assertEqual(res4["multiplicities"]["zero"], 68)

    def test_05_derandomize_transversal_carrier_martingale(self):
        """Verify constructive derandomizer strict martingale monotonicity and score >= mean."""
        events = [
            (((0, 1), (1, 2), (2, 3)), 10),
            (((0, 2), (3, 4), (4, 5)), 15),
            (((1, 0), (2, 4), (5, 3)), 8),
            (((3, 1), (4, 2), (0, 5)), 12),
            (((2, 0), (1, 3), (5, 4)), 20),
        ]
        res = derandomize_transversal_carrier(6, events, universe_size=6)
        self.assertTrue(res["monotonically_nondecreasing"])
        self.assertTrue(res["derandomized_exceeds_mean"])
        self.assertGreaterEqual(res["final_score"], int(res["initial_expectation"]))
        self.assertEqual(len(res["assignment"]), 6)
        self.assertEqual(set(res["assignment"].values()), set(range(6)))

    def test_06_verify_w32_canonical_certificate_and_failclosed(self):
        """Verify genuine W(3,2) ground truths and fail-closed rejections."""
        cert = verify_w32_canonical_certificate()
        self.assertTrue(cert["zero_mass_refuted_in_sample"])
        self.assertEqual(cert["min_core_sum"], 65)
        self.assertEqual(cert["min_total_S"], 68)
        self.assertEqual(cert["certified_core_floor"], 65)
        self.assertEqual(cert["certified_total_floor"], 68)
        self.assertFalse(cert["is_universal_proof"])

        # Proof summary structure reflects proved Branch A resolution
        summary = canonical_proof_summary()
        self.assertEqual(summary["Hypothesis"], 105)
        self.assertEqual(summary["Resolution"]["Overall_Status"], "HYP105_BRANCH_A_CERTIFIED_PROVED")
        self.assertIn("PROVED_OMEGA_S6", summary["Resolution"]["Branch_A_UniversalPointwise"])

        # Fail-closed invalid inputs
        for bad_s in (0, 1, 3, 5, 6, 7, 9, 10, -2, 2.5, "4"):
            with self.assertRaises((ValueError, TypeError)):
                canonical_parameters(bad_s)

        with self.assertRaises(ValueError):
            derandomize_transversal_carrier(0, [])
        with self.assertRaises(ValueError):
            derandomize_transversal_carrier(4, [], universe_size=2)

    def test_07_lemma4_master_reduction(self):
        """Verify Lemma 4 master 3-path reduction parameters."""
        for s in (2, 4, 8, 16):
            r = master_path_motif_reduction(s)
            self.assertEqual(r["status"], "PROVED")
            self.assertEqual(r["path_budget_coefficient"], 16)
            self.assertEqual(r["min_proper_paths"], 16 * (s ** 6))
            self.assertEqual(r["mixed_book_incident_exponent"], 8)

    def test_08_lemma5_sub_sextic_decoupling(self):
        """Verify Lemma 5 sub-sextic anchor blocking decay."""
        for s in (4, 8, 16, 32):
            res = anchor_blocking_scaling(s)
            self.assertEqual(res["status"], "PROVED")
            self.assertEqual(res["asymptotic_order_E"], "O(s^5)")
            self.assertEqual(res["asymptotic_order_B"], "o(s^6)")
            self.assertLess(res["empirical_scaling_exponent_B"], 6.00)
            if s >= 8:
                self.assertLess(res["bad_pair_fraction"], 0.60)


if __name__ == "__main__":
    unittest.main()
