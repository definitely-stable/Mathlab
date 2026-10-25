"""Independent tests for AA4-DM: Ramanujan expander spectrum and annihilation barrier audit."""
import unittest

from hyp105_issue230_d6aa4dm_ramanujan_expansion_annihilation_barrier import (
    ramanujan_spectrum_parameters,
    expander_mixing_bounds,
    simultaneous_annihilation_tradeoff,
    w32_all_schemes_tradeoff_census,
    all_h_hyp105_resolution_summary,
)


class AA4DMRamanujanExpansionTests(unittest.TestCase):
    def test_01_super_ramanujan_spectrum_and_multiplicities(self):
        """Verify super-Ramanujan spectrum and exact multiplicities matching graph dimension."""
        for s in (2, 4, 8, 16, 32, 64, 128, 256):
            res = ramanujan_spectrum_parameters(s)
            self.assertTrue(res["is_super_ramanujan"])
            self.assertLess(res["lambda_2"], res["ramanujan_bound"])
            self.assertLess(res["expander_ratio"], 1.0)
            mult = res["multiplicities"]
            self.assertEqual(mult["total"], res["total_vertices"])

        # Test specific W(3,2) multiplicities: 2*V = 30 vertices
        w32 = ramanujan_spectrum_parameters(2)
        self.assertEqual(w32["total_vertices"], 30)
        self.assertEqual(w32["multiplicities"]["+/-d"], 1)
        self.assertEqual(w32["multiplicities"]["+/-lambda_2"], 9)
        self.assertEqual(w32["multiplicities"]["zero"], 10)
        self.assertEqual(w32["multiplicities"]["total"], 30)

        # Test specific W(3,4) multiplicities: 2*V = 170 vertices
        w34 = ramanujan_spectrum_parameters(4)
        self.assertEqual(w34["total_vertices"], 170)
        self.assertEqual(w34["degree_d"], 5)
        self.assertEqual(w34["multiplicities"]["+/-d"], 1)
        self.assertEqual(w34["multiplicities"]["+/-lambda_2"], 50)  # NOT 170!
        self.assertEqual(w34["multiplicities"]["zero"], 68)          # NOT 272!
        self.assertEqual(w34["multiplicities"]["total"], 170)

    def test_02_expander_mixing_bounds(self):
        """Verify bipartite expander mixing lemma bounds on test point and line sets."""
        for s in (2, 4, 8):
            params = ramanujan_spectrum_parameters(s)
            V = params["V"]
            b6 = expander_mixing_bounds(s, 6, 6)
            self.assertGreaterEqual(b6["upper_edge_bound"], b6["lower_edge_bound"])
            self.assertGreater(b6["fluctuation"], 0.0)

            b_full = expander_mixing_bounds(s, V, V)
            self.assertGreater(b_full["expected_edges"], b_full["fluctuation"])

    def test_03_simultaneous_annihilation_tradeoff_status(self):
        """Verify simultaneous annihilation tradeoff is marked OPEN_CONJECTURE_UNPROVEN."""
        for s in (4, 8, 16):
            tradeoff = simultaneous_annihilation_tradeoff(s)
            self.assertEqual(tradeoff["status"], "OPEN_CONJECTURE_UNPROVEN")
            self.assertIn("Expander mixing", tradeoff["formal_blocker"])

    def test_04_w32_all_schemes_tradeoff_census(self):
        """Verify genuine W(3,2) empirical trade-off: min(D6 + BA + AB) == 65 > 0 across 4 schemes."""
        audit = w32_all_schemes_tradeoff_census()
        self.assertTrue(audit["simultaneous_zero_refuted_in_sample"])
        self.assertEqual(audit["min_core_sum"], 65)
        self.assertEqual(audit["certified_core_floor_in_sample"], 65)
        self.assertEqual(audit["min_total_S"], 68)

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

    def test_05_all_h_hyp105_resolution_summary(self):
        """Verify formal status summary of Hypothesis 105 across all 5 stages."""
        summary = all_h_hyp105_resolution_summary()
        self.assertEqual(summary["Hypothesis"], 105)
        self.assertEqual(summary["Issue"], 230)
        status = summary["ResolutionStatus"]
        self.assertEqual(status["ConstructiveDerandomizedCarrier"], "PROVED_EXISTENTIAL_OMEGA_S6")
        self.assertEqual(status["AlmostSureOrbitConcentration"], "OPEN_CONJECTURE_UNPROVEN")
        self.assertEqual(status["SimultaneousAnnihilation"], "OPEN_CONJECTURE_UNPROVEN")
        self.assertEqual(status["Branch_B_Refutation"], "NOT_REFUTED")

    def test_06_failclosed_invalid_inputs(self):
        """Reject non-powers of 2, non-integers, invalid subset dimensions fail-closed."""
        for invalid_s in (0, 1, 3, 5, 6, 7, 9, 10, -4, 4.5, "4"):
            with self.assertRaises((ValueError, TypeError)):
                ramanujan_spectrum_parameters(invalid_s)

        with self.assertRaises(ValueError):
            expander_mixing_bounds(4, 0, 10)
        with self.assertRaises(ValueError):
            expander_mixing_bounds(4, 10, 999999)


if __name__ == "__main__":
    unittest.main()
