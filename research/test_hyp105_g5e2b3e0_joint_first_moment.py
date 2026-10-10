"""Independent HYP-105 B3.2-E0 conditional expectation/quantifier falsifiers."""
import unittest
from fractions import Fraction
from itertools import permutations, product
from math import comb

from hyp105_g5e2b3e0_joint_first_moment import (
    FiniteInjectionSpace, exact_joint_table,
    conditional_expectation_certificate, finite_pair_label_diagnostic,
    self_report,
)


class HYP105JointFirstMomentTests(unittest.TestCase):
    def test_two_independent_injective_sides_and_every_completion(self):
        space = FiniteInjectionSpace(3, 2, 3)
        self.assertEqual(space.size, 36)
        generated = tuple(space.completions())
        self.assertEqual(len(generated), len(set(generated)))
        for labels in generated:
            self.assertEqual(len(set(labels[:2])), 2)
            self.assertEqual(len(set(labels[2:])), 3)
        # Independent enumeration, not calling tested generator.
        expected = {(a, b, c, d, e)
                    for a, b in permutations(range(comb(3, 2)), 2)
                    for c, d, e in permutations(range(comb(3, 2)), 3)}
        self.assertEqual(set(generated), expected)

    def test_independent_bruteforce_expected_pair_and_pareto(self):
        space = FiniteInjectionSpace(3, 2, 3)
        table = exact_joint_table(space, finite_pair_label_diagnostic)
        self.assertEqual(len(table), 36)
        means = tuple(sum((pair[i] for _, pair in table), Fraction()) / 36
                      for i in (0, 1))
        # Evaluate independent physical pair definitions directly.
        palette = tuple((0, 1), (0, 2), (1, 2))
        independent = []
        for left in permutations(palette, 2):
            for right in permutations(palette, 3):
                matched = (int(left[0] == right[0]) +
                           int(left[0] == right[1]) +
                           int(left[1] == right[1]) +
                           int(left[1] == right[2]))
                opposed = (int(left[0] == right[0] and left[1] == right[2]) +
                           int(left[0] == right[2] and left[1] == right[0]))
                independent.append((matched, opposed))
        self.assertEqual(means, tuple(
            Fraction(sum(x[i] for x in independent), len(independent))
            for i in (0, 1)))
        self.assertTrue(all(m > 0 for m in means))
        self.assertGreater(len(set(independent)), 1)

        for weight in (Fraction(1, 2), Fraction(1, 3)):
            q = conditional_expectation_certificate(
                space, finite_pair_label_diagnostic, weight)
            self.assertEqual((q["mean_R2"], q["mean_R3"]), means)
            self.assertEqual(q["normalized_initial_mean"], 1)
            self.assertLessEqual(q["terminal_normalized_score"], 1)
            self.assertLessEqual(q["selected_R2"], means[0]/weight)
            self.assertLessEqual(q["selected_R3"], means[1]/(1-weight))
            self.assertTrue(q["same_labels_for_both"])
            self.assertFalse(q["strict_R3_exponent"])
            self.assertFalse(q["aset_exponent_improved"])
            self.assertEqual(q["space_size"], 36)
            self.assertEqual(len(q["lex_conditional_history"]), 5)
            history = q["lex_conditional_history"]
            previous = Fraction(1)
            for step in history:
                self.assertLessEqual(step["remaining_mean"], previous)
                previous = step["remaining_mean"]
            self.assertEqual(previous, q["terminal_normalized_score"])

    def test_conditional_lex_ties_and_zero_expectations(self):
        space = FiniteInjectionSpace(3, 2, 3)
        def zero(left, right):
            return 0, 0
        q = conditional_expectation_certificate(space, zero)
        self.assertEqual(q["choice_indices"], (0, 1, 0, 1, 2))
        self.assertEqual(q["terminal_normalized_score"], 0)
        self.assertEqual((q["selected_R2"], q["selected_R3"]), (0, 0))
        def one_zero(left, right):
            return 0, 1 if left[0] == right[0] else 0
        q = conditional_expectation_certificate(space, one_zero)
        self.assertEqual(q["mean_R2"], 0)
        self.assertEqual(q["selected_R2"], 0)

    def test_scope_fail_closed_costs_probabilities_and_budget(self):
        space = FiniteInjectionSpace(3, 2, 3)
        with self.assertRaises(ValueError):
            FiniteInjectionSpace(3, 2, 3, max_outcomes=35)
        with self.assertRaises(ValueError):
            FiniteInjectionSpace(2, 2, 0)
        with self.assertRaises(ValueError):
            FiniteInjectionSpace(3, -1, 1)
        with self.assertRaises(ValueError):
            conditional_expectation_certificate(
                space, finite_pair_label_diagnostic, 0)
        with self.assertRaises(ValueError):
            conditional_expectation_certificate(
                space, finite_pair_label_diagnostic, 1)
        with self.assertRaises(ValueError):
            conditional_expectation_certificate(
                space, lambda f, g: (-1, 1))
        with self.assertRaises(ValueError):
            conditional_expectation_certificate(
                space, lambda f, g: (0.5, 1))
        with self.assertRaises(ValueError):
            exact_joint_table(space, lambda f, g: (1,))

    def test_report_never_promotes_strict_result(self):
        r = self_report()
        self.assertEqual(r["tiny_space"], 36)
        self.assertTrue(r["finite_toy_not_GF5_full_risks"])
        self.assertFalse(r["all_h_strict_R3"])
        self.assertFalse(r["novel_all_h_exponent"])


if __name__ == "__main__":
    unittest.main()
