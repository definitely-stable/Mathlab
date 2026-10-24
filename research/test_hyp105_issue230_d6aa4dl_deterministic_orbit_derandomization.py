"""Independent tests for AA4-DL: deterministic transversal derandomization and universal positivity gate."""
from fractions import Fraction
import unittest

from hyp105_issue230_d6aa4dl_deterministic_orbit_derandomization import (
    derandomized_orbit_parameters,
    dense_template_survival_fraction,
    transversal_rigidity_counting,
    synthetic_conditional_expectation_derandomization,
    w32_universal_positivity_envelope,
    all_h_branch_a_status_ledger,
)


class AA4DLDeterministicDerandomizationTests(unittest.TestCase):
    def test_01_dense_template_survival_fraction_all_h(self):
        """Verify exact rational template survival fractions under ANY right image E."""
        expected = {
            2: Fraction(1, 1),
            4: Fraction(55, 91),
            8: Fraction(107, 119),
            16: Fraction(1453, 1457),
        }
        for s, frac in expected.items():
            actual = dense_template_survival_fraction(s)
            self.assertEqual(actual, frac)
            params = derandomized_orbit_parameters(s)
            self.assertEqual(params["surviving_fraction"], frac)
            self.assertGreater(frac, Fraction(1, 2))
            print(f"AA4DL_TEMPLATE_SURVIVAL s={s} surviving={float(frac)*100:.2f}% ({frac})")

        # Test large asymptotic fields
        for s in (32, 64, 128, 256):
            actual = dense_template_survival_fraction(s)
            self.assertGreater(actual, Fraction(98, 100))
            print(f"AA4DL_ASYMPTOTIC_SURVIVAL s={s} surviving={float(actual)*100:.4f}%")

    def test_02_transversal_rigidity_counting_superlinear_carrier_ratio(self):
        """Verify that total carrier volume Theta(s^15) vastly outnumbers edge budget Theta(s^3)."""
        for s in (2, 4, 8, 16):
            res = transversal_rigidity_counting(s)
            self.assertTrue(res["carrier_to_edge_ratio_superlinear"])
            self.assertGreater(res["guaranteed_surviving_c6"], 0)
            self.assertGreater(res["min_matchings_per_cycle"], 0)
            self.assertGreater(res["total_carrier_volume"], res["V"])
            print(
                f"AA4DL_TRANSVERSAL_RIGIDITY s={s} V={res['V']} surviving_C6={res['guaranteed_surviving_c6']} "
                f"matchings/cycle={res['min_matchings_per_cycle']} total_carriers={res['total_carrier_volume']} "
                f"density_per_edge={float(res['carrier_density_per_edge']):.1f}"
            )

    def test_03_synthetic_conditional_expectation_derandomization(self):
        """Verify monotone potential non-decrease and score >= initial expectation."""
        # Define 5 weighted target events on 6 items
        events = [
            (((0, 1), (1, 2), (2, 3)), 10),
            (((0, 2), (3, 4), (4, 5)), 15),
            (((1, 0), (2, 4), (5, 3)), 8),
            (((3, 1), (4, 2), (0, 5)), 12),
            (((2, 0), (1, 3), (5, 4)), 20),
        ]
        res = synthetic_conditional_expectation_derandomization(6, events, universe_size=6)
        self.assertTrue(res["derandomized_exceeds_mean"])
        self.assertGreaterEqual(res["final_score"], int(res["initial_expectation"]))

        # Check step-by-step martingale monotonicity
        history = res["potential_history"]
        self.assertEqual(len(history), 7)
        for i in range(len(history) - 1):
            self.assertGreaterEqual(
                history[i + 1],
                history[i],
                f"Potential decreased at step {i}: {history[i+1]} < {history[i]}",
            )
        print(
            f"AA4DL_DERANDOMIZATION_MARTINGALE initial={float(res['initial_expectation']):.4f} "
            f"final={res['final_score']} history={[float(x) for x in history]}"
        )

    def test_04_w32_universal_positivity_envelope(self):
        """Verify genuine W(3,2) certified lower floor min S(f, g) >= 68 > 0."""
        env = w32_universal_positivity_envelope()
        self.assertTrue(env["strictly_positive"])
        self.assertEqual(env["certified_floor"], 68)
        self.assertEqual(env["min_S"], 68)
        self.assertEqual(env["max_S"], 259)
        self.assertEqual(env["schemes"]["lex"], 259)
        self.assertEqual(env["schemes"]["reverse"], 169)
        self.assertEqual(env["schemes"]["S68"], 68)
        self.assertEqual(env["schemes"]["S72"], 72)
        print(f"AA4DL_W32_ENVELOPE certified_floor={env['certified_floor']} min_S={env['min_S']}")

    def test_05_all_h_branch_a_status_ledger(self):
        """Verify synthesis of Hypothesis 105 Branch A resolution status."""
        ledger = all_h_branch_a_status_ledger()
        self.assertEqual(ledger["Branch_A_derandomized_carrier"], "PROVED_CONSTRUCTIVE_OMEGA_S6")
        self.assertEqual(ledger["Branch_A_almost_sure_orbit"], "PROVED_CHEBYSHEV_CONCENTRATION")
        self.assertEqual(ledger["Branch_A_pointwise_all_adversarial_pairs"], "OPEN_WITH_FORMAL_BLOCKER")
        self.assertEqual(ledger["W32_deterministic_infimum"], 68)
        self.assertEqual(ledger["asymptotic_scaling"], "Omega(s^6)")
        self.assertIn("symplectic polar", ledger["formal_blocker"])
        print(f"AA4DL_STATUS_LEDGER: {ledger}")

    def test_06_failclosed_invalid_inputs(self):
        """Reject non-powers of 2, non-integers, invalid dimensions fail-closed."""
        for invalid_s in (0, 1, 3, 5, 6, 7, 9, 10, -2, 2.5, "2"):
            with self.assertRaises((ValueError, TypeError)):
                derandomized_orbit_parameters(invalid_s)

        # Invalid synthetic V
        with self.assertRaises(ValueError):
            synthetic_conditional_expectation_derandomization(0, [])
        with self.assertRaises(ValueError):
            synthetic_conditional_expectation_derandomization(5, [], universe_size=3)
        print("AA4DL_FAILCLOSED_TESTS passed")


if __name__ == "__main__":
    unittest.main()
