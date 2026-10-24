"""Independent tests for AA4-DM: Ramanujan expander mixing and simultaneous annihilation barrier."""
import unittest

from hyp105_issue230_d6aa4dm_ramanujan_expansion_annihilation_barrier import (
    ramanujan_spectrum_parameters,
    expander_mixing_bounds,
    simultaneous_annihilation_tradeoff,
    w32_all_schemes_tradeoff_census,
    all_h_hyp105_resolution_summary,
)


class AA4DMRamanujanExpansionTests(unittest.TestCase):
    def test_01_super_ramanujan_spectrum_all_h(self):
        """Verify that bipartite incidence graph of W(3,s) is strictly super-Ramanujan for all h."""
        for s in (2, 4, 8, 16, 32, 64, 128, 256):
            res = ramanujan_spectrum_parameters(s)
            self.assertTrue(res["is_super_ramanujan"])
            self.assertLess(res["lambda_2"], res["ramanujan_bound"])
            self.assertLess(res["expander_ratio"], 1.0)
            print(
                f"AA4DM_SPECTRUM s={s} d={res['degree_d']} lambda_2={res['lambda_2']:.3f} "
                f"Ramanujan_bound={res['ramanujan_bound']:.3f} ratio={res['expander_ratio']:.4f}"
            )

        # Asymptotic decay of expander ratio
        r16 = ramanujan_spectrum_parameters(16)["expander_ratio"]
        r64 = ramanujan_spectrum_parameters(64)["expander_ratio"]
        r256 = ramanujan_spectrum_parameters(256)["expander_ratio"]
        self.assertLess(r64, r16)
        self.assertLess(r256, r64)

    def test_02_expander_mixing_bounds(self):
        """Verify bipartite expander mixing lemma bounds on test point and line sets."""
        for s in (2, 4, 8):
            params = ramanujan_spectrum_parameters(s)
            V = params["V"]
            # Test small 6x6 sets corresponding to physical cycles
            b6 = expander_mixing_bounds(s, 6, 6)
            self.assertGreaterEqual(b6["upper_edge_bound"], b6["lower_edge_bound"])
            self.assertGreater(b6["fluctuation"], 0.0)

            # Test macroscopic sets: for X=Y=V, expected edges = d*V, fluctuation = lambda_2 * V
            b_full = expander_mixing_bounds(s, V, V)
            self.assertGreater(b_full["expected_edges"], b_full["fluctuation"])
            print(
                f"AA4DM_EXPANDER_MIXING s={s} V={V} 6x6_expected={b6['expected_edges']:.3f} "
                f"full_expected={b_full['expected_edges']:.1f} full_fluc={b_full['fluctuation']:.1f}"
            )

    def test_03_simultaneous_annihilation_tradeoff_positive(self):
        """Verify that spectral expander retention ensures strictly positive D6+BA+AB floor."""
        for s in (4, 8, 16, 32, 64, 128):
            tradeoff = simultaneous_annihilation_tradeoff(s)
            self.assertTrue(tradeoff["annihilation_barrier_positive"])
            self.assertGreater(tradeoff["theoretical_floor_s6"], 0.0)
            print(
                f"AA4DM_TRADEOFF s={s} retention={tradeoff['expander_retention']*100:.2f}% "
                f"floor_s6={tradeoff['theoretical_floor_s6']:.2f}"
            )

    def test_04_w32_all_schemes_tradeoff_census(self):
        """Verify genuine W(3,2) empirical trade-off: min(D6 + BA + AB) == 65 > 0."""
        audit = w32_all_schemes_tradeoff_census()
        self.assertTrue(audit["simultaneous_zero_refuted"])
        self.assertEqual(audit["min_core_sum"], 65)
        self.assertEqual(audit["certified_core_floor"], 65)
        self.assertEqual(audit["min_total_S"], 68)

        # Check that S68 and S72 have D6 == 0 but core_sum >= 65
        s68 = audit["schemes"]["S68"]
        self.assertEqual(s68["D6"], 0)
        self.assertEqual(s68["BA"], 44)
        self.assertEqual(s68["AB"], 21)
        self.assertEqual(s68["core_sum"], 65)
        self.assertTrue(s68["d6_zero_compensated"])

        s72 = audit["schemes"]["S72"]
        self.assertEqual(s72["D6"], 0)
        self.assertEqual(s72["BA"], 36)
        self.assertEqual(s72["AB"], 31)
        self.assertEqual(s72["core_sum"], 67)
        self.assertTrue(s72["d6_zero_compensated"])
        print(f"AA4DM_W32_CENSUS: min_core={audit['min_core_sum']} min_S={audit['min_total_S']}")

    def test_05_all_h_hyp105_resolution_summary(self):
        """Verify formal resolution summary of Hypothesis 105 across all 5 stages."""
        summary = all_h_hyp105_resolution_summary()
        self.assertEqual(summary["Hypothesis"], 105)
        self.assertEqual(summary["Issue"], 230)
        theorems = summary["KeyTheorems"]
        self.assertIn("AA4-DI", theorems)
        self.assertIn("AA4-DJ", theorems)
        self.assertIn("AA4-DK", theorems)
        self.assertIn("AA4-DL", theorems)
        self.assertIn("AA4-DM", theorems)
        status = summary["ResolutionStatus"]
        self.assertEqual(status["ConstructiveDerandomizedCarrier"], "PROVED_OMEGA_S6")
        self.assertEqual(status["AlmostSureOrbitConcentration"], "PROVED_CONCENTRATED")
        self.assertEqual(status["SimultaneousAnnihilation"], "REFUTED_NO_GO")
        self.assertEqual(status["W32_DeterministicInfimum"], "CERTIFIED_GE_68")
        print(f"AA4DM_RESOLUTION_SUMMARY: {summary}")

    def test_06_failclosed_invalid_inputs(self):
        """Reject non-powers of 2, non-integers, invalid subset dimensions fail-closed."""
        for invalid_s in (0, 1, 3, 5, 6, 7, 9, 10, -4, 4.5, "4"):
            with self.assertRaises((ValueError, TypeError)):
                ramanujan_spectrum_parameters(invalid_s)

        # Invalid subset dimensions
        with self.assertRaises(ValueError):
            expander_mixing_bounds(4, 0, 10)
        with self.assertRaises(ValueError):
            expander_mixing_bounds(4, 10, 999999)
        print("AA4DM_FAILCLOSED_TESTS passed")


if __name__ == "__main__":
    unittest.main()
