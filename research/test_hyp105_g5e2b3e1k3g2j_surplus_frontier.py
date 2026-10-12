"""Independent rational-polytope and true-W32 all-h falsifier tests."""
from fractions import Fraction
import unittest

from hyp105_g5e2b3e1k3g2j_surplus_frontier import (
    BEST_PATH_EXPECTED, _from_pair, finite_models,
    lower_line_envelope, independent_intersection_oracle,
    necessary_counterexample, report,
)


def fake(name,S,J):
    return {"name":name,"s":2,"S":S,"J":J,"GF5_numerator":0}


class K3G2JRationalSurplusTests(unittest.TestCase):
    def test_three_exact_rational_linear_regimes(self):
        points=[fake("a",3,8),fake("b",5,3),fake("c",15,1),
                fake("dominated",19,3)]
        pieces=lower_line_envelope(points)
        self.assertEqual([(p["S"],p["J"]) for p in pieces],
                         [(3,8),(5,3),(15,1)])
        self.assertEqual([p["beta_from"] for p in pieces],
                         [[0,1],[2,5],[5,1]])
        self.assertEqual([p["beta_to"] for p in pieces],
                         [[2,5],[5,1],None])
        self.assertEqual([p["alpha_intercept"] for p in pieces],
                         [[3,64],[5,64],[15,64]])
        self.assertGreater(independent_intersection_oracle(points,pieces),4)

    def test_independent_oracle_detects_wrong_support(self):
        points=[fake("a",3,8),fake("b",5,3),fake("c",15,1)]
        pieces=lower_line_envelope(points)
        corrupted=[dict(p) for p in pieces]
        corrupted[1]["J"]=9
        with self.assertRaises(AssertionError):
            independent_intersection_oracle(points,corrupted)

    def test_exact_w32_correlated_original_model_falsifiers(self):
        rows=finite_models(shell_limit=0,include_correlated=True)
        self.assertEqual(len(rows),9)
        self.assertEqual((rows[0]["S"],rows[0]["J"]),(259,36))
        self.assertEqual((rows[1]["S"],rows[1]["J"]),(169,28))
        self.assertEqual(
            [(p["S"],p["J"]) for p in rows[-6:]],
            list(BEST_PATH_EXPECTED))
        self.assertEqual(rows[-1]["GF5_numerator"],4289420)
        pieces=lower_line_envelope(rows)
        independent_intersection_oracle(rows,pieces)
        self.assertEqual(min(p["S"] for p in rows),90)
        # Candidate alpha=2,beta=0 requires S>=128 for s=2,
        # contradicted by a legal coherent W32 correlated source map.
        fail=necessary_counterexample(rows,2,0)
        self.assertTrue(fail["refuted"])
        self.assertEqual(fail["S"],90)
        self.assertEqual(fail["J"],21)
        self.assertEqual(fail["claimed_alpha_s6"],[128,1])
        self.assertFalse(necessary_counterexample(rows,Fraction(1,10),0)["refuted"])

    def test_brute_exact_envelope_on_rational_grid(self):
        rows=finite_models(shell_limit=0,include_correlated=True)
        pieces=lower_line_envelope(rows)
        for numerator in range(0,21):
            b=Fraction(numerator,4)
            min_actual=min(Fraction(p["S"])+b*p["J"] for p in rows)
            candidates=[p for p in pieces if (
                _from_pair(p["beta_from"])<=b and
                (p["beta_to"] is None or
                 b<=_from_pair(p["beta_to"])))]
            self.assertTrue(candidates)
            self.assertEqual(min_actual,min(
                Fraction(p["S"])+b*p["J"] for p in candidates))

    def test_small_report_does_not_claim_all_h_or_full_shell(self):
        r=report(shell_limit=0,include_correlated=True)
        self.assertEqual(r["finite_exact_model_count"],9)
        self.assertFalse(r["complete_single_swap_shell"])
        self.assertFalse(r["true_all_h_positive_alpha_beta_proved"])
        self.assertFalse(r["all_h_Jcross_leq_K_S_proved"])
        self.assertFalse(r["entire_W32_label_space_enumerated"])
        self.assertTrue(r["no_W34_partial_target_as_negative_evidence"])
        self.assertEqual(r["minimum_observed_S_at_beta_zero"]["S"],90)
        self.assertEqual(
            r["minimum_observed_S_at_beta_zero"]["alpha_upper"],[45,32])
        self.assertEqual(len(r["observations_sha256"]),64)

    def test_invalid_coefficients_and_finite_domain(self):
        point=[fake("a",3,8)]
        for alpha,beta in ((0,0),(-1,0),(1,-1),(0.5,0),(1,0.5)):
            with self.assertRaises(ValueError):
                necessary_counterexample(point,alpha,beta)
        for bad in (-1,106,True):
            with self.assertRaises(ValueError):
                finite_models(shell_limit=bad,include_correlated=False)
        with self.assertRaises(ValueError):
            finite_models(shell_limit=0,include_correlated=1)
        for pair in ([1,0],[1,-2],[1,2,3],[1,2.0]):
            with self.assertRaises(ValueError):
                _from_pair(pair)
        with self.assertRaises(ValueError):
            lower_line_envelope([])
        with self.assertRaises(ValueError):
            lower_line_envelope([fake("invalid",-1,2)])


if __name__=="__main__":
    unittest.main()
