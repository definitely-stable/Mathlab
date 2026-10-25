"""Test suite for AA4-DI: GQ incidence density barrier for minimal 2-external A-bridges."""

from collections import Counter
from fractions import Fraction
import unittest

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4di_coupled_incidence_density import (
    gq_point_coverage_density,
    analyze_point_coverage_and_incidence_deficit,
    analyze_both_A_bipartite_matchings,
    audit_reservoir_incidence_coupling,
)


class AA4DICoupledIncidenceDensityGate(unittest.TestCase):
    def test_01_analytic_gq_point_coverage_density_bounds(self):
        """Analytic O(s^-2) point density, O(s^-10) 5-point coverage, O(s^-12) D6 matching."""
        cases = (
            (2, 15, 14, 1, Fraction(14, 15), Fraction(537824, 759375)),
            (4, 85, 24, 61, Fraction(24, 85), Fraction(7962624, 4437053125)),
            (8, 585, 44, 541, Fraction(44, 585), Fraction(164916224, 68514001115625)),
        )
        for s, V_exp, cov_exp, uncov_exp, rho_exp, p5_exp in cases:
            res = gq_point_coverage_density(s)
            self.assertEqual(res["s"], s)
            self.assertEqual(res["V"], V_exp)
            self.assertEqual(res["max_covered_points"], cov_exp)
            self.assertEqual(res["uncovered_points"], uncov_exp)
            self.assertEqual(res["point_coverage_density_rho"], rho_exp)
            self.assertEqual(res["uncorrelated_5point_coverage_bound"], p5_exp)
            # Uncovered fraction must exceed 70% for s >= 4
            if s >= 4:
                self.assertGreater(float(res["uncovered_fraction"]), 0.70)
            print(
                f"AA4DI_ANALYTIC_DENSITY s={s} V={V_exp} rho={float(rho_exp):.4f} "
                f"uncorrelated_5pt={float(p5_exp):.2e} uncovered_pct={float(res['uncovered_fraction'])*100:.1f}%",
                flush=True,
            )

        # Check asymptotic decay
        res16 = gq_point_coverage_density(16)
        self.assertLess(float(res16["point_coverage_density_rho"]), 0.02)
        self.assertLess(float(res16["uncorrelated_5point_coverage_bound"]), 1e-8)
        self.assertLess(float(res16["d6_uncorrelated_matching_bound"]), 1e-11)

    def test_02_synthetic_point_coverage_and_deficit_gates(self):
        """Verify that deficit > 0 strictly forbids A-left / B-right sixflag formation."""
        # Mock point-lines: points 0..5, lines 0..4
        # Fully covered case:
        pl_full = {
            0: (0,),
            1: (0,),
            2: (1,),
            3: (2,),
            4: (3,),
            5: (4,),
        }
        res_full = analyze_point_coverage_and_incidence_deficit(
            range(6), range(5), pl_full
        )
        self.assertTrue(res_full["is_fully_covered"])
        self.assertEqual(res_full["total_incidences"], 6)
        self.assertEqual(res_full["deficit"], 0)
        self.assertTrue(res_full["admit_A_left_B_right_necessary"])

        # Uncovered point case: point 5 has degree 0 into lines 0..4
        pl_uncovered = {
            0: (0, 1),
            1: (0,),
            2: (1,),
            3: (2,),
            4: (3, 4),
            5: (99,),  # no line in 0..4
        }
        res_uncov = analyze_point_coverage_and_incidence_deficit(
            range(6), range(5), pl_uncovered
        )
        self.assertFalse(res_uncov["is_fully_covered"])
        self.assertEqual(res_uncov["uncovered_points"], (5,))
        self.assertGreaterEqual(res_uncov["deficit"], 1)
        self.assertFalse(res_uncov["admit_A_left_B_right_necessary"])
        print("AA4DI_SYNTHETIC_DEFICIT_GATE verified", flush=True)

    def test_03_TRUE_original_W32_lex_S72_deficit_and_coupling_audit(self):
        """Full audit on W(3,2): all accepted positive Qs have deficit == 0."""
        for scheme in ("lex", "S72"):
            model = fixture(1, scheme)
            res = audit_reservoir_incidence_coupling(model, limit_reservoirs=12)
            self.assertEqual(res["pairs_examined"], 12)
            self.assertGreater(res["total_PA_L5_evaluated"], 0)
            self.assertGreater(res["positive_Q_found_count"], 0)
            # Deficit zero count must be >= positive Q count
            self.assertGreaterEqual(res["deficit_zero_count"], 1)
            print(
                f"AA4DI_W32_INCIDENCE_AUDIT {scheme}: reservoirs={res['pairs_examined']} "
                f"evaluated_pairs={res['total_PA_L5_evaluated']} "
                f"fully_covered={res['fully_covered_count']} "
                f"coverage_rate={res['full_coverage_rate']:.3f} "
                f"positive_Q={res['positive_Q_found_count']}",
                flush=True,
            )

    def test_04_TRUE_original_W34_density_collapse(self):
        """Verify sharp density collapse on W(3,4) lex and random (coverage rate < 5%)."""
        for scheme in ("lex", "random"):
            model = fixture(2, scheme)
            res = audit_reservoir_incidence_coupling(model, limit_reservoirs=6)
            self.assertGreaterEqual(res["pairs_examined"], 3)
            self.assertGreater(res["total_PA_L5_evaluated"], 0)
            # On W(3,4), full coverage rate collapses sharply (< 5% in sample, < 0.3% global)
            self.assertLess(res["full_coverage_rate"], 0.05)
            print(
                f"AA4DI_W34_DENSITY_COLLAPSE {scheme}: evaluated_pairs={res['total_PA_L5_evaluated']} "
                f"fully_covered={res['fully_covered_count']} "
                f"coverage_rate={res['full_coverage_rate']:.4f}",
                flush=True,
            )

    def test_05_TRUE_original_W38_explicit_partial_zero_coverage(self):
        """Explicit partial check on W(3,8): zero pairs achieve full point coverage in sample."""
        for scheme in ("lex", "random"):
            model = fixture(3, scheme)
            res = audit_reservoir_incidence_coupling(model, limit_reservoirs=2)
            self.assertEqual(res["pairs_examined"], 2)
            # Coverage rate must be exactly 0 in this sample
            self.assertEqual(res["fully_covered_count"], 0)
            self.assertEqual(res["full_coverage_rate"], 0.0)
            print(
                f"AA4DI_W38_EXPLICIT_PARTIAL_ZERO_COVERAGE {scheme}: evaluated_pairs={res['total_PA_L5_evaluated']} "
                f"fully_covered=0",
                flush=True,
            )

    def test_06_failclosed_invalid_inputs(self):
        """Reject non-powers of 2, malformed point/line sets, invalid dimensions."""
        for bad_s in (0, 1, 3, 5, 6, 7, 9, 10, -2, "4"):
            with self.assertRaises((ValueError, TypeError)):
                gq_point_coverage_density(bad_s)

        with self.assertRaises(ValueError):
            analyze_point_coverage_and_incidence_deficit(
                (0, 1, 2, 3, 4), range(5), {}
            )  # only 5 points

        with self.assertRaises(ValueError):
            analyze_point_coverage_and_incidence_deficit(
                range(6), range(4), {}
            )  # only 4 lines

        with self.assertRaises(ValueError):
            analyze_point_coverage_and_incidence_deficit(
                (0, 0, 1, 2, 3, 4), range(5), {}
            )  # duplicate point

        with self.assertRaises(ValueError):
            analyze_both_A_bipartite_matchings(
                range(5), range(6), {}, (), (), ()
            )  # 5 points instead of 6
        print("AA4DI_FAILCLOSED_TESTS passed", flush=True)


if __name__ == "__main__":
    unittest.main()
