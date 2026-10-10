"""Independent exhaustive prefix-fiber falsifiers for HYP-105 C7."""
from fractions import Fraction
from itertools import combinations, permutations
from math import comb
import unittest

from hyp105_g5e2b3e1a_fixed_leading import _two_factors_K6
from hyp105_g5e2b3e1c5_common_bijection import (
    common_bijection_moments, fixed_map_overlap, physical_occupied_target,
)
from hyp105_g5e2b3e1c7_conditional_prefix import (
    conditional_overlap_mean, greedy_conditional_selector,
)


class ConditionalPrefixC7Tests(unittest.TestCase):
    @staticmethod
    def example():
        palette = tuple(combinations(range(6), 2))
        cycle = _two_factors_K6()[0]
        F = tuple(cycle) + tuple(e for e in palette if e not in cycle)[:2]
        target = physical_occupied_target(6, F)
        source = {
            frozenset((0, 1, 2, 3, 4, 5)): 3,
            frozenset((0, 1, 2, 3, 4, 6)): 2,
            frozenset((0, 1, 2, 3, 6, 7)): 4,
            frozenset((0, 2, 3, 4, 5, 7)): 1,
        }
        return source, target

    def test_independent_brute_all_720_completions_of_one_pinned_prefix(self):
        src, target = self.example()
        pinned = {0: 2, 3: 5}
        residual_original = tuple(i for i in range(8) if i not in pinned)
        residual_image = tuple(i for i in range(8) if i not in pinned.values())
        values = []
        for images in permutations(residual_image):
            pi = list(range(8))
            for i, v in pinned.items():
                pi[i] = v
            for i, v in zip(residual_original, images):
                pi[i] = v
            values.append(fixed_map_overlap(src, target, pi))
        self.assertEqual(len(values), 720)
        self.assertEqual(
            conditional_overlap_mean(src, target, 8, pinned),
            Fraction(sum(values), len(values)))
        # One shared permutation, not C4's separate per-pair conditionals.
        for next_original in residual_original[:2]:
            n = len(residual_image)
            parent = conditional_overlap_mean(src, target, 8, pinned)
            child_sum = sum(
                conditional_overlap_mean(
                    src, target, 8, {**pinned, next_original: j})
                for j in residual_image)
            self.assertEqual(child_sum, n * parent)

    def test_empty_prefix_equals_independent_C5_global_mean(self):
        src, target = self.example()
        self.assertEqual(
            conditional_overlap_mean(src, target, 8, {}),
            common_bijection_moments(src, target, 8)[
                "one_common_right_bijection_mean"])

    def test_complete_prefix_equals_independent_fixed_recount(self):
        src, target = self.example()
        for pi in (tuple(range(8)), tuple(reversed(range(8))),
                   (7, 1, 3, 5, 0, 4, 2, 6)):
            self.assertEqual(
                conditional_overlap_mean(
                    src, target, 8, {i: pi[i] for i in range(8)}),
                fixed_map_overlap(src, target, pi))

    def test_lex_greedy_tower_and_integer_zero_completion(self):
        # A one-hot source/target has mean 1 / C(8,6) < 1.
        R = frozenset(range(6))
        T = frozenset(range(1, 7))
        w = {R: 1}
        result = greedy_conditional_selector(w, {T}, 8)
        self.assertEqual(result["initial_uniform_mean"], Fraction(1, comb(8, 6)))
        self.assertEqual(result["actual_fixed_BA_overlap"], 0)
        self.assertTrue(all(
            a >= b for a, b in zip(
                result["conditional_means"], result["conditional_means"][1:])))
        self.assertEqual(len(result["conditional_means"]), 9)

    def test_real_W32_original_incidence_selector_and_independent_recount(self):
        from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
        from hyp105_g5e2b3e1c0_weighted_overlap import (
            source_weighted_BA_hypergraph,
        )
        model = pair_labeled_symplectic(1, "reverse-line")
        src = source_weighted_BA_hypergraph(model)
        physical = tuple(combinations(range(6), 2))
        target = physical_occupied_target(6, physical)
        old = tuple({e: i for i, e in enumerate(physical)}[e]
                    for e in model["right_labels"])
        self.assertEqual(fixed_map_overlap(src, target, old), 77)
        result = greedy_conditional_selector(src, target, 15)
        self.assertEqual(
            result["initial_uniform_mean"], Fraction(5000 * 70, 5005))
        self.assertLessEqual(result["actual_fixed_BA_overlap"], 69)
        self.assertEqual(
            fixed_map_overlap(src, target,
                              result["original_to_occupied_permutation"]),
            result["actual_fixed_BA_overlap"])
        self.assertFalse(result["full_seven_family_S_evaluated"])
        self.assertFalse(result["all_correlated_lower_proved"])

    def test_invalid_partial_injection_fails_closed(self):
        src, target = self.example()
        for invalid in ({0: 1, 1: 1}, {0: 8}, {-1: 0}, {True: 1},
                        {0: True}):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                conditional_overlap_mean(src, target, 8, invalid)
        with self.assertRaises(ValueError):
            conditional_overlap_mean(src, target, 8,
                                     {0: 0, 1: 1, 2: 2, 3: 3,
                                      4: 4, 5: 5, 6: 6, 7: 7, 8: 8})
        with self.assertRaises(ValueError):
            conditional_overlap_mean({frozenset(range(5)): 1},
                                     target, 8, {})


if __name__ == "__main__":
    unittest.main()
