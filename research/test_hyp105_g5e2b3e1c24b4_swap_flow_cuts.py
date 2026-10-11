"""C24-B4: true W32 third neighborhood, all-h flow and cut identities."""
from itertools import combinations
import unittest

from hyp105_g5e2b3e1c24b_three_collision import W32_LEFT_H45
from hyp105_g5e2b3e1c24b2_joint_seven import (
    TAGS, GF5_WEIGHTS, compile_left, full_left_score, right_first_independent)
from hyp105_g5e2b3e1c24b3_joint_swap_gradient import (
    exact_exchange_neighborhood, legal_transpose)
from hyp105_g5e2b3e1c24b4_swap_flow_cuts import (
    W32_RIGHT_AFTER_TWO_SWAPS, genuine_w32_third_neighborhood,
    signed_swap_cut_certificate, swap_flow_certificate)


class OriginalW32ThirdExchangeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = compile_left(W32_LEFT_H45)
        cls.g = W32_RIGHT_AFTER_TWO_SWAPS
        cls.neighborhood = exact_exchange_neighborhood(cls.source, cls.g)

    def test_exact_third_neighborhood_is_global_and_complete(self):
        n = self.neighborhood
        self.assertEqual(n["baseline"]["S_seven"], 111)
        self.assertEqual(set(tuple(x["swap"]) for x in n["entries"]),
                         set(combinations(range(15), 2)))
        self.assertEqual(len(set(self.g)), 15)
        for test in ((0, 1), (6, 14), (12, 13)):
            trial = next(x for x in n["entries"] if x["swap"] == test)
            full = full_left_score(self.source, legal_transpose(self.g, *test))
            self.assertEqual(full["seven_counts"], trial["seven_counts"])
            self.assertEqual(full["right_C_accepted"], trial["right_C_accepted"])

    def test_true_independent_62370_source_score_and_one_swap_witness(self):
        report = genuine_w32_third_neighborhood()
        self.assertEqual(report["original_source_size"], 62370)
        self.assertEqual(report["two_swap_S"], 111)
        self.assertEqual(report["third_neighborhood_size"], 105)
        self.assertTrue(report["independent_right_first_census"])
        self.assertEqual(
            report["after_optional_third_S"],
            min(111, report["third_best_neighbor_S"]))
        self.assertEqual(
            report["third_strictly_improving_neighbors"] > 0,
            report["third_move_taken"])
        self.assertEqual(
            report["after_two_swaps_stationary"],
            report["third_strictly_improving_neighbors"] == 0)
        self.assertEqual(report["third_best_swap"], (7, 11))
        self.assertEqual(report["third_best_neighbor_S"], 102)
        self.assertEqual(report["third_strictly_improving_neighbors"], 8)
        self.assertEqual(report["two_swap_seven_vector"],
                         dict(zip(TAGS, (0, 54, 46, 4, 0, 3, 4))))
        self.assertEqual(report["best_neighbor_flow"]["gain"], 49)
        self.assertEqual(report["best_neighbor_flow"]["loss"], 58)
        witness = report["explicit_five_step_witness"]
        self.assertEqual([x["after"] for x in witness["moves"]],
                         [102, 93, 86, 76, 72])
        self.assertEqual([x["swap"] for x in witness["moves"]],
                         [(7, 11), (6, 8), (5, 9), (2, 8), (1, 13)])
        self.assertEqual(witness["final_S"], 72)
        self.assertEqual(witness["final_seven_counts"],
                         dict(zip(TAGS, (0, 36, 31, 2, 0, 1, 2))))
        self.assertEqual(witness["final_Q7_necessary"], 3283610)
        self.assertEqual(witness["final_right_C"], 0)
        self.assertEqual(witness["final_original_right_perm"],
                         (12, 9, 11, 2, 8, 6, 0, 13, 5, 14, 3, 7, 4, 10, 1))
        self.assertTrue(witness["strict_one_swap_local_minimum"])
        self.assertTrue(witness["all_105_final_neighbors_checked"])
        self.assertEqual(witness["strictly_improving_final_neighbors"], 0)
        self.assertEqual(witness["best_final_neighbor_swap"], (1, 14))
        self.assertEqual(witness["best_final_neighbor_S"], 74)
        self.assertEqual(witness["s2_all_s_gradient_gate_c_upper"], "9/8")
        self.assertTrue(witness["not_asymptotic_all_h_c_upper"])
        self.assertFalse(report["all_h_positive_lower_proved"])
        self.assertFalse(report["full_GF5_R3_upper_proved"])

    def test_each_signed_difference_and_cut_pair_reconstruction(self):
        n = self.neighborhood
        cuts = signed_swap_cut_certificate(n["entries"], 15)
        self.assertTrue(cuts["all_edge_gradients_recovered_exactly"])
        self.assertEqual(cuts["edges"], 105)
        self.assertEqual(cuts["strict_improving_edges"],
                         n["strict_S_improving_global_neighbors"])
        self.assertEqual(cuts["one_swap_stationary"],
                         n["one_swap_local_minimum_S"])
        for trial in n["entries"]:
            self.assertEqual(
                trial["exchange"]["delta_S"],
                sum(trial["exchange"]["delta_seven"].values()))

    def test_source_flow_independent_best_and_selected_swap(self):
        n = self.neighborhood
        for pair in ((0, 1), tuple(n["min_S"]["swap"])):
            row = next(x for x in n["entries"] if x["swap"] == pair)
            flow = swap_flow_certificate(self.source, self.g, *pair)
            self.assertEqual(flow["delta_S"], row["exchange"]["delta_S"])
            self.assertEqual(flow["delta_by_tag"], row["exchange"]["delta_seven"])
            self.assertEqual(flow["original_right_C_delta"],
                             row["exchange"]["delta_original_right_C"])
            self.assertEqual(flow["delta_Q7_necessary"],
                             row["exchange"]["delta_Q7"])
            self.assertEqual(flow["delta_S"], flow["gain"] - flow["loss"])
            self.assertEqual(flow["delta_Q7_necessary"],
                             sum(w * flow["delta_by_tag"][tag]
                                 for w, tag in zip(GF5_WEIGHTS, TAGS)))
            self.assertGreater(flow["affected_original_sixsets"], 0)
            self.assertEqual(flow["gain"] > flow["loss"],
                             flow["delta_S"] > 0)

    def test_singleton_cut_sign_is_not_exchange_stationarity(self):
        # Signed swap edge weights: d01=-1, d02=+1, d12=+1.
        # ALL singleton cuts are nonnegative (0,0,2), but swap 01 improves.
        es = [
            {"swap": (0, 1), "exchange": {"delta_S": -1}},
            {"swap": (0, 2), "exchange": {"delta_S": 1}},
            {"swap": (1, 2), "exchange": {"delta_S": 1}},
        ]
        cuts = signed_swap_cut_certificate(es, 3)
        self.assertTrue(cuts["all_singleton_cuts_nonnegative"])
        self.assertEqual(cuts["minimum_singleton_cut"], 0)
        self.assertEqual(cuts["strict_improving_edges"], 1)
        self.assertEqual(cuts["pair_cut_inequality_violations"], 1)
        self.assertFalse(cuts["one_swap_stationary"])
        # This abstract signed graph is NOT asserted to come from a GQ f,g.
        self.assertEqual(cuts["negative_cut_count_unoriented"], 0)

    def test_reject_incomplete_or_invalid_cut_matrices(self):
        with self.assertRaises(ValueError):
            signed_swap_cut_certificate([], 15)
        with self.assertRaises(ValueError):
            signed_swap_cut_certificate([{"swap": (0, 1),
                                          "exchange": {"delta_S": 1}}], 3)
        with self.assertRaises(ValueError):
            signed_swap_cut_certificate([], 2)
        with self.assertRaises(ValueError):
            swap_flow_certificate(self.source, self.g, 1, 1)


if __name__ == "__main__":
    unittest.main()
