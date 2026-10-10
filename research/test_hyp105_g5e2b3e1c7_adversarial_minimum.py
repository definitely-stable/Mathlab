"""Independent full 7!/8! minima and fail-closed budget falsifiers."""
from itertools import combinations, permutations
import unittest
from hyp105_g5e2b3e1c5_common_bijection import fixed_map_overlap
from hyp105_g5e2b3e1c7_adversarial_minimum import (
    rearrangement_lower_bound, exact_adversarial_minimum, W32_rearrangement_report,
)


class FixedAdversarialC7Tests(unittest.TestCase):
    @staticmethod
    def independent_enumeration(source, target, V):
        return min(fixed_map_overlap(source, target, p)
                   for p in permutations(range(V)))

    def test_dense_support_positive_pigeonhole_and_zero(self):
        for V in (6, 7, 8):
            sets = list(combinations(range(V), 6))
            src = {frozenset(R): 1 for R in sets[:-1]}
            target = {frozenset(R) for R in sets[:2]}
            got = exact_adversarial_minimum(src, target, V)
            expected = max(0, len(target) - 1)
            self.assertEqual(got["exact_minimum"], expected)
            self.assertEqual(got["certified_lower"], expected)
            self.assertEqual(got["witness_upper"], expected)
            self.assertEqual(fixed_map_overlap(src, target,
                             got["witness_permutation"]), expected)

    def test_independent_complete_7factorial_and_8factorial(self):
        for V in (7, 8):
            sets = list(combinations(range(V), 6))
            src = {frozenset(R): 1 + i % 3 for i, R in enumerate(sets)
                   if i % 3 != 0}
            targets = (
                {frozenset(sets[i]) for i in range(0, len(sets), 4)},
                {frozenset(sets[i]) for i in range(1, len(sets), 3)},
            )
            for target in targets:
                got = exact_adversarial_minimum(src, target, V)
                expected = self.independent_enumeration(src, target, V)
                self.assertEqual(got["exact_minimum"], expected)
                self.assertEqual(fixed_map_overlap(src, target,
                                 got["witness_permutation"]), expected)
                self.assertLessEqual(rearrangement_lower_bound(
                    src, target, V), expected)
                self.assertNotEqual(got["status"], "UNKNOWN_BUDGET")

    def test_star_geometry_positive_minimum_despite_zero_rearrangement(self):
        # At V=8 sixsets are complements of pairs. The original source
        # and physical target are ALL 7 complements of star edges (0,j).
        # Under one genuine common pi, their centers are 0 and pi(0):
        # same center gives 7 overlapping sixsets, different gives 1.
        # An arbitrary permutation of 28 sixset cells could give zero.
        V = 8
        star = {frozenset(set(range(V)) - {0, j})
                for j in range(1, V)}
        src = {R: 1 for R in star}
        self.assertEqual(rearrangement_lower_bound(src, star, V), 0)
        got = exact_adversarial_minimum(src, star, V)
        self.assertEqual(self.independent_enumeration(src, star, V), 1)
        self.assertEqual(got["exact_minimum"], 1)
        self.assertEqual(got["status"], "CERTIFIED_MINIMUM")
        self.assertEqual(fixed_map_overlap(src, star,
                         got["witness_permutation"]), 1)

    def test_budget_cut_must_not_certify_positive_result(self):
        V = 8
        star = {frozenset(set(range(V)) - {0, j})
                for j in range(1, V)}
        src = {R: 1 for R in star}
        got = exact_adversarial_minimum(src, star, V, max_nodes=1)
        self.assertEqual(got["status"], "UNKNOWN_BUDGET")
        self.assertIsNone(got["exact_minimum"])
        self.assertEqual(got["certified_lower"], 0)
        self.assertEqual(got["witness_upper"], 1)
        self.assertEqual(fixed_map_overlap(src, star,
                         got["witness_permutation"]), 1)

    def test_true_GQ_W32_lower_relaxation_is_zero_not_positive_proof(self):
        result = W32_rearrangement_report()
        self.assertEqual(result["lex"]["one_actual_fixed_map_overlap"], 98)
        self.assertEqual(result["reverse-line"]["one_actual_fixed_map_overlap"], 77)
        for r in result.values():
            self.assertEqual(r["V"], 15)
            self.assertEqual(r["source_support"], 3076)
            self.assertEqual(r["target_support"], 70)
            self.assertEqual(r["ambient_sixsets"], 5005)
            self.assertEqual(r["support_only_rearrangement_lower"], 0)
            self.assertFalse(r["full_minimum_certified"])

    def test_inputs_fail_closed_and_empty_source(self):
        R = frozenset(range(6))
        for bad in (5, 10):
            with self.assertRaises(ValueError):
                exact_adversarial_minimum({R: 1}, {R}, bad)
        with self.assertRaises(ValueError):
            exact_adversarial_minimum({R: -1}, {R}, 7)
        with self.assertRaises(ValueError):
            exact_adversarial_minimum({R: 1}, {R}, 7, max_nodes=0)
        self.assertEqual(exact_adversarial_minimum({}, {R}, 7)["exact_minimum"], 0)


if __name__ == "__main__":
    unittest.main()
