"""C24-B3 genuine original W32 full-seven exchange and exact penalty frontier."""
from fractions import Fraction
from itertools import permutations
import unittest

from hyp105_g5e2b3e1c24b_three_collision import W32_LEFT_H45, W32_RIGHT_H45_ZERO
from hyp105_g5e2b3e1c24b2_joint_seven import (
    TAGS, GF5_WEIGHTS, compile_left, full_left_score, right_first_independent)
from hyp105_g5e2b3e1c24b3_joint_swap_gradient import (
    legal_transpose, exact_joint_seven_swap_signature,
    exact_finite_penalty_frontier, exact_exchange_neighborhood,
    exhaustive_small_exchange_gate, verified_two_step_finite_descent,
)


class JointGlobalExchangeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = compile_left(W32_LEFT_H45)
        cls.neighbors = exact_exchange_neighborhood(cls.source, W32_RIGHT_H45_ZERO)

    def test_true_global_permutation_exchange_and_all_seven_conservation(self):
        base = self.neighbors["baseline"]
        self.assertEqual((base["S_seven"], base["right_C_accepted"]), (177, 0))
        self.assertEqual(len(self.neighbors["entries"]), 105)
        for x in self.neighbors["entries"]:
            delta = exact_joint_seven_swap_signature(base, x)
            self.assertEqual(delta, x["exchange"])
            self.assertEqual(delta["delta_S"], sum(delta["delta_seven"].values()))
            self.assertEqual(delta["delta_Q7"],
                             sum(GF5_WEIGHTS[i] * delta["delta_seven"][tag]
                                 for i, tag in enumerate(TAGS)))
        for swap in ((0, 1), (6, 14), (10, 14)):
            trial = next(t for t in self.neighbors["entries"] if t["swap"] == swap)
            self.assertEqual(
                full_left_score(self.source,
                                legal_transpose(W32_RIGHT_H45_ZERO, *swap))["S_seven"],
                trial["S_seven"])

    def test_exact_105_global_map_joint_regularization_two_phase_envelope(self):
        k = exact_finite_penalty_frontier(self.neighbors["entries"])
        self.assertEqual(k["positive_C_witness_swap"], (6, 14))
        self.assertEqual(k["zero_C_witness_swap"], (10, 14))
        self.assertEqual((k["positive_C_min_S"], k["zero_C_min_S"]), (129, 136))
        self.assertEqual(k["positive_C_at_best"], 1)
        self.assertEqual(k["switch_weight_lambda"], 7)
        self.assertTrue(k["for_every_nonnegative_lambda_exact"])
        for lam in (Fraction(0), Fraction(1), Fraction(13, 2),
                    Fraction(7), Fraction(15, 2), Fraction(1000)):
            direct = min(Fraction(x["S_seven"]) + lam * x["right_C_accepted"]
                         for x in self.neighbors["entries"])
            self.assertEqual(direct, min(129 + lam, Fraction(136)))
        with self.assertRaises(ValueError):
            exact_finite_penalty_frontier([])

    def test_stationarity_reduction_on_complete_small_groups(self):
        for n in (3, 4):
            f = {p: sum((i+1) * abs(v-i) for i, v in enumerate(p))
                 for p in permutations(range(n))}
            for T in (-1, 1, 3, 40):
                gate = exhaustive_small_exchange_gate(f, T)
                self.assertEqual(gate["global_min"], gate["least_local_min"])
                self.assertEqual(gate["all_scores_at_least_threshold"],
                                 gate["all_local_minima_at_least_threshold"])
        with self.assertRaises(ValueError):
            exhaustive_small_exchange_gate({(0, 1, 2): 0}, 1)

    def test_first_improvement_witness_checked_independently(self):
        n = self.neighbors
        self.assertEqual(n["min_S"]["swap"], (6, 14))
        g = legal_transpose(W32_RIGHT_H45_ZERO, 6, 14)
        b = right_first_independent(W32_LEFT_H45, g)
        self.assertEqual(b["seven_counts"], n["min_S"]["seven_counts"])
        self.assertEqual((b["S_seven"], b["right_C_accepted"]), (129, 1))
        self.assertGreater(n["strict_S_improving_global_neighbors"], 0)
        self.assertGreater(n["simultaneous_positive_negative_class_tradeoffs"], 0)

    def test_two_exact_neighborhoods_no_global_minimum_overclaim(self):
        report = verified_two_step_finite_descent()
        self.assertTrue(report["only_two_exact_neighborhoods_not_global_minimum"])
        self.assertEqual(report["first_initial_S"], 177)
        self.assertEqual(report["after_first_S"], 129)
        self.assertEqual(report["after_first_strict_improving_neighbors"], 17)
        self.assertFalse(report["after_first_one_swap_S_stationary"])
        self.assertTrue(report["second_move_taken"])
        self.assertEqual(report["second_applied_original_right_swap"], (12, 13))
        self.assertEqual(report["second_best_or_stationary_S"], 111)
        self.assertEqual(sum(report["second_seven_counts"].values()), 111)
        self.assertEqual(len(report["second_full_right_perm"]), 15)
        self.assertEqual(len(set(report["second_full_right_perm"])), 15)

    def test_invalid_transpositions_fail_closed(self):
        with self.assertRaises(ValueError):
            legal_transpose(W32_RIGHT_H45_ZERO, 0, 0)
        with self.assertRaises(ValueError):
            legal_transpose(W32_RIGHT_H45_ZERO, -1, 2)
        with self.assertRaises(ValueError):
            legal_transpose(tuple(range(14)), 1, 2)
        with self.assertRaises(ValueError):
            exact_joint_seven_swap_signature({"seven_counts": {}},
                                             {"seven_counts": {}})


if __name__ == "__main__":
    unittest.main()
