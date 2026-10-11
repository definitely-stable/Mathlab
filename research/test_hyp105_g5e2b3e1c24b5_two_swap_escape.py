"""C24-B5: exact original W32 right-template pullback and double swap gates.

Fast unit tests avoid a redundant 5005-state exhaustive scan in each broad
Research 'Unit tests' invocation. The 5005-state run is explicit in both
dedicated Contract and independent Research script steps.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb
import unittest

from hyp105_g5e2b3e1c24b_three_collision import (
    W32_LEFT_H45, W32_RIGHT_H45_ZERO)
from hyp105_g5e2b3e1c24b2_joint_seven import (
    TAGS, GF5_WEIGHTS, compile_left, full_left_score,
    right_first_independent, right_masks)
from hyp105_g5e2b3e1c24b3_joint_swap_gradient import legal_transpose
from hyp105_g5e2b3e1c24b5_two_swap_escape import (
    ALL_SWAPS, N_DISTANCE_TWO, N_DOUBLE_TRANSPOSITIONS,
    N_THREE_CYCLES, audit_two_swap_ball, compile_right_pullback_fibers,
    template_pullback_score, disjoint_swap_curvature,
    independent_disjoint_original_source_curvature)


class TrueOriginalW32DoubleSwapTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = compile_left(W32_LEFT_H45)
        cls.fibers = compile_right_pullback_fibers(cls.source)
        cls.g = (12, 9, 11, 2, 8, 6, 0, 13, 5, 14, 3, 7, 4, 10, 1)

    def test_template_compiler_original_sources_fail_closed(self):
        f = self.fibers
        self.assertEqual(len(f["templates"]), 130)
        self.assertEqual(self.source["left_source_size"], 62370)
        self.assertEqual(f["original_eligible"], self.source["static_eligible"])
        self.assertTrue(f["ordinary"])
        self.assertTrue(f["D6"])
        with self.assertRaises(ValueError):
            compile_right_pullback_fibers({"left_source_size": 62369,
                                          "by_line": ()})
        with self.assertRaises(ValueError):
            template_pullback_score(f, tuple(range(14)))

    def test_reconstructed_seven_vector_matches_all_original_left_fibers(self):
        for g in (self.g, W32_RIGHT_H45_ZERO,
                  legal_transpose(self.g, 1, 14),
                  legal_transpose(legal_transpose(self.g, 0, 1), 1, 2),
                  legal_transpose(legal_transpose(self.g, 0, 1), 2, 3)):
            self.assertEqual(template_pullback_score(self.fibers, g),
                             full_left_score(self.source, g))

    def test_frozen_true_W32_72_with_independent_right_first(self):
        quick = template_pullback_score(self.fibers, self.g)
        self.assertEqual(quick["S_seven"], 72)
        self.assertEqual(tuple(quick["seven_counts"][k] for k in TAGS),
                         (0, 36, 31, 2, 0, 1, 2))
        self.assertEqual(quick["Q7_necessary_numerator"], 3283610)
        slow = right_first_independent(W32_LEFT_H45, self.g)
        self.assertEqual(quick["seven_counts"], slow["seven_counts"])
        self.assertEqual(quick["right_C_accepted"], slow["right_C_accepted"])

    def test_105_first_neighbors_match_baseline_strictness(self):
        base = 72
        scores = []
        for pair in ALL_SWAPS:
            score = template_pullback_score(
                self.fibers, legal_transpose(self.g, *pair))["S_seven"]
            self.assertGreater(score, base, pair)
            scores.append(score)
        self.assertEqual(len(scores), 105)
        self.assertEqual(min(scores), 74)

    def test_distance_two_group_combinatorics_independent_small_S4(self):
        # An independently brute-forced S4 transposition Cayley sphere.
        ident = tuple(range(4))
        swaps = tuple(combinations(range(4), 2))
        def swap(a, x):
            a = list(a)
            i, j = x
            a[i], a[j] = a[j], a[i]
            return tuple(a)
        representations = defaultdict(set)
        for first in swaps:
            for second in swaps:
                if first != second:
                    final = swap(swap(ident, first), second)
                    representations[final].add((first, second))
        self.assertEqual(len(representations),
                         2*comb(4, 3)+3*comb(4, 4))
        self.assertNotIn(ident, representations)
        counts = Counter(len(reps) for reps in representations.values())
        self.assertEqual(counts, Counter({3: 8, 2: 3}))
        self.assertEqual(N_THREE_CYCLES, 910)
        self.assertEqual(N_DOUBLE_TRANSPOSITIONS, 4095)
        self.assertEqual(N_DISTANCE_TWO, 5005)

    def test_true_original_joint_touch_negative_mixed_curvature(self):
        a, b = (4, 14), (3, 12)
        for x, y in ((a, b), (b, a)):
            r = independent_disjoint_original_source_curvature(
                self.source, self.g, x, y)
            self.assertEqual(r["mixed_curvature"], -31)
            self.assertEqual(
                r["mixed_curvature"],
                sum(r["mixed_curvature_by_tag"].values()))
            self.assertGreater(r["jointly_touched_original_sixsets"], 0)
            self.assertGreater(r["nonzero_mixed_original_sixsets"], 0)
            self.assertLessEqual(r["nonzero_mixed_original_sixsets"],
                                 r["jointly_touched_original_sixsets"])
            self.assertEqual(
                r["mixed_Q7_necessary"],
                sum(w * r["mixed_curvature_by_tag"][tag]
                    for tag, w in zip(TAGS, GF5_WEIGHTS)))
        with self.assertRaises(ValueError):
            independent_disjoint_original_source_curvature(
                self.source, self.g, (0, 1), (1, 2))

    def test_mixed_curvature_disjoint_and_nontrivial_escape_equivalence(self):
        d = disjoint_swap_curvature(72, 74, 76, 70)
        self.assertEqual((d["delta_first"], d["delta_second_independent"]),
                         (2, 4))
        self.assertEqual(d["mixed_curvature"], -8)
        self.assertTrue(d["escape_iff_curvature_below_negative_first_sum"])
        self.assertTrue(d["escapes"])
        other = disjoint_swap_curvature(72, 74, 76, 80)
        self.assertFalse(other["escapes"])
        self.assertTrue(other["escape_iff_curvature_below_negative_first_sum"])
        with self.assertRaises(ValueError):
            disjoint_swap_curvature(72, -1, 76, 70)


if __name__ == "__main__":
    unittest.main()
