"""Independent D6-N exact physical 2-factor and ORIGINAL W32 falsifiers.

No approximation, Monte Carlo, swapped directions or fabricated W34 S.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial
import unittest

from hyp105_issue230_d6n_exact_correlated_ca_overlap import (
    exact_right_A_overlap_kernel, local_two_factor_overlap_table,
    ca_original_line_weights, ca_correlation_moments, real_W32_correlation_report,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six


def brute_independent_physical_A(a):
    """Enumerate physical K_a six-EDGE sets, not the 70 K6 templates."""
    edges = tuple(combinations(range(a), 2))
    valid = []
    for chosen in combinations(edges, 6):
        degrees = Counter(v for edge in chosen for v in edge)
        if len(degrees) == 6 and set(degrees.values()) == {2}:
            valid.append(frozenset(chosen))
    return valid


def brute_independent_original_CA_weights(model):
    """Three actual ORIGINAL points, two actual GQ lines per point."""
    original = [set() for _ in model["left_labels"]]
    for p, line in model["incidences"]:
        original[p].add(line)
    physical = [set(pair) for pair in model["left_labels"]]
    counts = Counter()
    for triple in combinations(range(len(original)), 3):
        if (not physical[triple[0]].isdisjoint(physical[triple[1]])
                or not physical[triple[0]].isdisjoint(physical[triple[2]])
                or not physical[triple[1]].isdisjoint(physical[triple[2]])):
            continue
        for choice in product(*(combinations(sorted(original[p]), 2)
                                for p in triple)):
            lines = tuple(sorted(line for pair in choice for line in pair))
            if len(set(lines)) == 6:
                counts[lines] += 1
    return counts


def independent_ordered_support_overlap_spectrum(weights):
    """Independent tuple-set overlap instead of production integer bit masks."""
    out = Counter()
    for a, wa in weights.items():
        for b, wb in weights.items():
            out[len(set(a).intersection(b))] += wa * wb
    return [out[k] for k in range(7)]


class ExactCorrelatedOverlapTests(unittest.TestCase):
    def test_every_local_factor_pair_intersection_identity(self):
        table = local_two_factor_overlap_table()
        self.assertEqual(len(table), 7)
        for t, row in enumerate(table):
            self.assertEqual(sum(row), 4900)
            self.assertTrue(all(row[k] == 0 for k in range(t+1, 7)))
        self.assertEqual(table[0][0], 4900)
        self.assertEqual(table[6][6], 70)

    def test_independent_physical_full_A_pair_census_K6_K7(self):
        for a in (6, 7):
            with self.subTest(a=a):
                A = brute_independent_physical_A(a)
                self.assertEqual(len(A), 70*comb(a, 6))
                by_common = Counter(len(x.intersection(y))
                                    for x in A for y in A)
                kernel = exact_right_A_overlap_kernel(a)
                self.assertEqual(
                    [by_common[k] for k in range(7)],
                    list(kernel["ordered_A_pairs_by_common_physical_edge_count"])
                )
                K = comb(a, 2)
                p = Fraction(factorial(6)*len(A), factorial(K)//factorial(K-6))
                self.assertEqual(kernel["single_A_probability"], p)
                for k, numerator in enumerate(
                        kernel["ordered_A_pairs_by_common_physical_edge_count"]):
                    expected = Fraction(
                        factorial(k)*factorial(6-k)**2*numerator,
                        factorial(K)//factorial(K-(12-k))
                    )
                    self.assertEqual(
                        kernel["joint_A_probability_by_common_original_line_count"][k],
                        expected
                    )

    def test_real_original_W32_left_weights_two_unrelated_oracles(self):
        for scheme in ("lex", "reverse", "S68", "S72"):
            with self.subTest(scheme=scheme):
                model = fixture(1, scheme)
                actual = ca_original_line_weights(model)
                independent = brute_independent_original_CA_weights(model)
                self.assertEqual(actual, independent)
                self.assertEqual(sum(actual.values()),
                                 209 if scheme in ("lex", "reverse") else 297)
                self.assertEqual(len(model["incidences"]), 45)
                self.assertEqual(len(model["left_labels"]), 15)

    def test_real_original_W32_conditional_moments_and_correlations(self):
        for scheme, mu, fixed in (("lex", "38/13", 4),
                                  ("reverse", "38/13", 0),
                                  ("S68", "54/13", 0),
                                  ("S72", "54/13", 2)):
            with self.subTest(scheme=scheme):
                model = fixture(1, scheme)
                weights = brute_independent_original_CA_weights(model)
                row = ca_correlation_moments(weights, model["right_labels"],
                                             model["a"])
                self.assertEqual(row["right_random_exact_mean"], mu)
                self.assertEqual(row["actual_fixed_g_Cleft_Aright_sixsets"], fixed)
                self.assertEqual(
                    row["ordered_support_pairs_by_shared_original_line_count"],
                    independent_ordered_support_overlap_spectrum(weights))
                self.assertEqual(
                    sum(row["ordered_support_pairs_by_shared_original_line_count"]),
                    sum(weights.values())**2)
                self.assertGreaterEqual(Fraction(
                    row["right_random_exact_variance"]), 0)
                pz = Fraction(row[
                    "right_random_P_positive_lower_Paley_Zygmund"])
                self.assertLessEqual(pz, 1)
                self.assertGreater(pz, 0)
                self.assertEqual(
                    Fraction(row["actual_fixed_g_minus_right_random_mean"]),
                    Fraction(fixed) - Fraction(mu))
                # Explicit null physical-correlation witnesses at fixed g
                # despite a STRICTLY POSITIVE conditional random mean.
                if scheme in ("reverse", "S68"):
                    self.assertEqual(
                        row["actual_fixed_g_positive_original_support_count"], 0)
                    self.assertEqual(
                        Fraction(row["actual_fixed_g_centered_discrepancy_over_mean"]),
                        -1)

    def test_d6m_directional_and_present_physical_A_are_kept_distinct(self):
        data = real_W32_correlation_report()
        self.assertEqual(data["Branch_A"], "OPEN")
        self.assertEqual(data["Branch_B"], "OPEN")
        rows = data["finite_W32_rows"]
        self.assertEqual([r["scheme"] for r in rows],
                         ["lex", "reverse", "S68", "S72"])
        self.assertEqual([r["complete_right_physical_A_patterns_available"]
                          for r in rows], [70]*4)
        self.assertEqual([r["actual_fixed_g_Cleft_Aright_sixsets"]
                          for r in rows], [4, 0, 0, 2])
        self.assertEqual(rows[0]["right_random_exact_mean"],
                         rows[1]["right_random_exact_mean"])

    def test_invalid_global_injections_and_bad_support_fail_closed(self):
        model = fixture(1, "lex")
        weights = ca_original_line_weights(model)
        labels = model["right_labels"]
        with self.assertRaises(ValueError):
            ca_correlation_moments(weights, (labels[0],)*15, 6)
        with self.assertRaises(ValueError):
            ca_correlation_moments({(0, 1, 2, 3, 4, 5): -1}, labels, 6)
        with self.assertRaises(ValueError):
            ca_correlation_moments({(0, 1, 2, 3, 4, 99): 1}, labels, 6)
        with self.assertRaises(ValueError):
            exact_right_A_overlap_kernel(5)
        with self.assertRaises(ValueError):
            ca_original_line_weights(fixture(2, "lex"))


if __name__ == "__main__":
    unittest.main()
