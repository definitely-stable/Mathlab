"""Independent bounded oracles for the six-factor-forest E2-B3.0 proof."""
from collections import Counter
from itertools import combinations, permutations
from fractions import Fraction
import random
import unittest

from hyp105_g5e2b3_forests import (
    integer_partitions, six_projection_coefficients,
    leafless_projection_probability, projection_power_loss,
    restricted_growth_partitions, is_six_factor_forest,
    six_forest_power_report,
)
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic


def direct_leafless_ratio(a, profile):
    """Separate exhaustive actual injective edge tuples, no polynomial."""
    palette = list(combinations(range(a), 2))
    good = total = 0
    for ordered in permutations(palette, len(profile)):
        degree = Counter()
        for edge, weight in zip(ordered, profile):
            degree[edge[0]] += weight
            degree[edge[1]] += weight
        good += bool(degree) and min(degree.values()) >= 2
        total += 1
    return Fraction(good, total)


def independent_dfs_forest(left, right):
    """Separate component counting, rejects parallel factor edges."""
    edges = tuple(zip(left, right))
    if len(set(edges)) != len(edges):
        return False
    adjacency = {}
    for u, v in edges:
        lhs, rhs = ("P", u), ("L", v)
        adjacency.setdefault(lhs, set()).add(rhs)
        adjacency.setdefault(rhs, set()).add(lhs)
    remaining = set(adjacency)
    components = 0
    while remaining:
        components += 1
        stack = [remaining.pop()]
        while stack:
            for node in adjacency[stack.pop()]:
                if node in remaining:
                    remaining.remove(node)
                    stack.append(node)
    return len(edges) == len(adjacency) - components


class SixEdgeForestProjectionTests(unittest.TestCase):
    def test_profiles_and_known_exact_polynomial_coefficients(self):
        profiles = tuple(integer_partitions(6))
        self.assertEqual(len(profiles), 11)
        self.assertEqual(len(set(profiles)), 11)
        self.assertEqual(dict(six_projection_coefficients((6,))),
                         {2: Fraction(1, 2)})
        self.assertEqual(six_projection_coefficients((5, 1)), ())
        self.assertEqual(dict(six_projection_coefficients((1,)*6)),
                         {4: Fraction(30), 5: Fraction(510), 6: Fraction(70)})
        self.assertEqual(projection_power_loss((1,)*6), 9)
        self.assertIsNone(projection_power_loss((5,1)))
        self.assertEqual(leafless_projection_probability(6, (6,)), 1)
        self.assertEqual(leafless_projection_probability(6, (5,1)), 0)

    def test_exact_probabilities_match_independent_bruteforce(self):
        for profile in integer_partitions(6):
            self.assertEqual(leafless_projection_probability(4, profile),
                             direct_leafless_ratio(4, profile), profile)
        # K5 still bounded: at most (10)_6 = 151200 assignments.
        for profile in integer_partitions(6):
            self.assertEqual(leafless_projection_probability(5, profile),
                             direct_leafless_ratio(5, profile), profile)
        with self.assertRaises(ValueError):
            leafless_projection_probability(3, (1,)*6)
        with self.assertRaises(ValueError):
            six_projection_coefficients((1, 5))

    def test_all_six_factor_partition_graphs_independent_oracle(self):
        shapes = restricted_growth_partitions()
        self.assertEqual(len(shapes), 203)
        self.assertEqual(len(set(shapes)), 203)
        for left in shapes:
            for right in shapes:
                self.assertEqual(is_six_factor_forest(left, right),
                                 independent_dfs_forest(left, right))

    def test_real_symplectic_gf2_gf4_six_edges_acyclic(self):
        for h, trials in ((1, 120), (2, 250)):
            model = pair_labeled_symplectic(h, "lex")
            edges = model["incidences"]
            rng = random.Random(105_600+h)
            for _ in range(trials):
                selected = rng.sample(edges, 6)
                self.assertTrue(independent_dfs_forest(
                    tuple(p for p,_ in selected),
                    tuple(q for _,q in selected)))

    def test_r3_scope_and_sharp_method_exponent(self):
        report = six_forest_power_report()
        self.assertEqual(report["admissible_leafless_factor_forest_shapes"], 11663)
        self.assertEqual(report["max_leafless_expected_count_power_in_s"], "6")
        self.assertEqual(sum(report["shape_exponents"].values()), 11663)
        self.assertEqual(report["shape_exponents"]["6"], 631)
        self.assertFalse(report["strict_R3_exponent_proved"])
        self.assertFalse(report["positive_GF5_flow_classification_done"])
        self.assertFalse(report["new_ASET_power_proved"])


if __name__ == "__main__":
    unittest.main()
