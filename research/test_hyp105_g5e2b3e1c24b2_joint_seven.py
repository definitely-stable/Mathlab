"""C24-B2: two independently oriented original GQ sixset censuses and tradeoff."""
import unittest
from collections import Counter
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS
from hyp105_g5e2b3e1c24_right_c_certificate import K6_PAIRS
from hyp105_g5e2b3e1c24b_three_collision import (
    W32_LEFT_H45, W32_RIGHT_H45_ZERO, right_C_source_with_left_f,
    exact_collision_decomposition)
from hyp105_g5e2b3e1c24b2_joint_seven import (
    TAGS, GF5_WEIGHTS, compile_left, full_left_score,
    right_first_independent, right_swap_105, report, full_permutation)

BASE = {"D6": 1, "B-left/A-right": 80, "A-left/B-right": 83,
        "C/A": 4, "C/B": 0, "B/B-overlap": 2, "B/B-disjoint": 7}
MIN_FULL = {"D6": 1, "B-left/A-right": 64, "A-left/B-right": 52,
            "C/A": 4, "C/B": 0, "B/B-overlap": 2, "B/B-disjoint": 6}
MIN_C_ZERO = {"D6": 1, "B-left/A-right": 74, "A-left/B-right": 51,
              "C/A": 2, "C/B": 0, "B/B-overlap": 3, "B/B-disjoint": 5}


class JointAllSevenOriginalW32Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.src = compile_left()
        cls.neighborhood = right_swap_105(cls.src)

    def test_all_62370_original_sixsets_and_frozen_GF5_weights(self):
        self.assertEqual(self.src["left_source_size"], 62370)
        self.assertEqual(self.src["static_eligible"], 53907)
        self.assertEqual(self.src["compressed_records"], 51506)
        self.assertEqual(sum(rec[3] for rec in self.src["records"]), 53907)
        self.assertEqual(set(TAGS), set(rec[0] for rec in self.src["records"]))
        self.assertEqual(tuple(W32_LEFT_H45), self.src["f"])
        self.assertEqual(dict(zip(TAGS, GF5_WEIGHTS)), R3_CERTIFIED_FLOORS)

    def test_baseline_TWO_independent_full_original_GQ_censuses(self):
        a = full_left_score(self.src, W32_RIGHT_H45_ZERO)
        b = right_first_independent(W32_LEFT_H45, W32_RIGHT_H45_ZERO)
        self.assertEqual(b["right_source_size"], 62370)
        self.assertEqual(a["seven_counts"], b["seven_counts"])
        self.assertEqual(a["seven_counts"], BASE)
        self.assertEqual(a["S_seven"], 177)
        self.assertEqual(a["Q7_necessary_numerator"], 8030293)
        self.assertEqual(a["right_C_accepted"], 0)
        self.assertEqual(sum(BASE.values()), 177)
        self.assertEqual(sum(BASE[k] * R3_CERTIFIED_FLOORS[k] for k in TAGS),
                         8030293)
        triples = right_C_source_with_left_f(W32_LEFT_H45)
        self.assertEqual(sum(triples.values()), 45)
        c = exact_collision_decomposition(triples, W32_RIGHT_H45_ZERO, K6_PAIRS)
        self.assertEqual(c["accepted_right_C"], 0)
        # C/A=4 here is ORIGINAL-LEFT C, not ORIGINAL-RIGHT C.
        self.assertEqual(a["seven_counts"]["C/A"], 4)
        self.assertEqual(a["right_C_accepted"], c["accepted_right_C"])

    def test_all_105_globally_coherent_neighborhood_no_hidden_independent_g(self):
        t = self.neighborhood
        self.assertEqual(t["number_of_swaps"], 105)
        self.assertEqual(len(t["swaps"]), 105)
        self.assertEqual(len({row["swap"] for row in t["swaps"]}), 105)
        self.assertEqual(t["C_histogram"], {0: 58, 1: 35, 2: 8, 3: 3, 4: 1})
        self.assertEqual(t["C_zero_neighbors"], 58)
        self.assertEqual(t["min_S"]["swap"], (6, 14))
        self.assertEqual(t["min_S"]["seven_counts"], MIN_FULL)
        self.assertEqual((t["min_S"]["S_seven"],
                          t["min_S"]["Q7_necessary_numerator"],
                          t["min_S"]["right_C_accepted"]), (129, 5842083, 1))
        self.assertEqual(t["min_Q7"]["swap"], (6, 14))
        self.assertEqual(t["min_S_given_C_zero"]["swap"], (10, 14))
        self.assertEqual(t["min_S_given_C_zero"]["seven_counts"], MIN_C_ZERO)
        self.assertEqual((t["min_S_given_C_zero"]["S_seven"],
                          t["min_S_given_C_zero"]["Q7_necessary_numerator"],
                          t["min_S_given_C_zero"]["right_C_accepted"]),
                         (136, 6172583, 0))
        self.assertLess(t["min_S"]["S_seven"],
                        t["min_S_given_C_zero"]["S_seven"])

    def test_direct_right_first_original_census_for_global_swap_witnesses(self):
        for i, j in ((6, 14), (10, 14), (0, 1)):
            g = list(W32_RIGHT_H45_ZERO)
            g[i], g[j] = g[j], g[i]
            direct = right_first_independent(W32_LEFT_H45, g)
            row = next(t for t in self.neighborhood["swaps"] if t["swap"] == (i, j))
            self.assertEqual(direct["seven_counts"], row["seven_counts"])
            self.assertEqual(direct["S_seven"], row["S_seven"])
            self.assertEqual(direct["Q7_necessary_numerator"],
                             row["Q7_necessary_numerator"])
            self.assertEqual(direct["right_C_accepted"], row["right_C_accepted"])

    def test_surrogate_zero_is_not_full_joint_optimum(self):
        t = self.neighborhood
        self.assertEqual((t["baseline"]["right_C_accepted"],
                          t["baseline"]["S_seven"]), (0, 177))
        self.assertEqual(t["min_S"]["right_C_accepted"], 1)
        self.assertEqual(t["min_S_given_C_zero"]["right_C_accepted"], 0)
        self.assertEqual(136 - 129, 7)
        self.assertTrue(report()["no_global_15_factorial_or_all_h_minimum_claim"])

    def test_invalid_global_injections_fail_closed(self):
        with self.assertRaises(ValueError):
            compile_left((0,) * 15)
        with self.assertRaises(ValueError):
            full_left_score(self.src, (0,) * 15)
        with self.assertRaises(ValueError):
            right_first_independent(W32_LEFT_H45, range(14))
        with self.assertRaises(ValueError):
            right_swap_105(self.src, range(14))
        with self.assertRaises(ValueError):
            full_permutation(range(14))


if __name__ == "__main__":
    unittest.main()
