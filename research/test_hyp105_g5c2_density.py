"""Independent finite falsification for the G5-C2 trade-density evidence gate."""
import itertools
import random
from math import comb
import unittest
from fractions import Fraction

from hyp105_g5c2_density import (
    bitset, collision_spectrum, conditional_expectation_extract, density_report,
    gf5_unit_four, has_forbidden_core, optimize_first_moment, w32_columns,
    six_cycle_pair_probability_lower, expected_minimal_six_trades_lower,
    generalized_quadrangle_expectation_lower,
    validate_cleaned
)
from test_hyp105_g5c_signed_oracles import direct_aset_collision, signed_trade


def exact_small_expectation(n, conflicts, p):
    """Independent oracle: enumerate the entire Bernoulli product distribution."""
    total = Fraction(0)
    for state in range(1 << n):
        bits = state.bit_count()
        score = bits - sum(state & edge == edge for edge in conflicts)
        total += score * p**bits * (1 - p)**(n - bits)
    return total


class G5C2TradeDensityTests(unittest.TestCase):
    def test_alteration_exact_expected_value_and_derandomization(self):
        n = 6
        samples = [
            (bitset((0, 1)), bitset((1, 2, 3))),
            (bitset((0, 1, 2, 3)), bitset((0, 1, 2, 3, 4, 5))),
            (bitset((0, 2, 4)), bitset((1, 3, 5))),
            (),
        ]
        for edges in samples:
            for p in (Fraction(0), Fraction(1, 4),
                      Fraction(1, 2), Fraction(3, 4), Fraction(1)):
                direct = exact_small_expectation(n, edges, p)
                algebraic = p * n - sum(p**e.bit_count() for e in edges)
                self.assertEqual(direct, algebraic)
                initial, cleaned, bound, score = (
                    conditional_expectation_extract(n, edges, p))
                self.assertEqual(bound, algebraic)
                self.assertGreaterEqual(Fraction(score), bound)
                self.assertGreaterEqual(Fraction(cleaned.bit_count()), bound)
                self.assertFalse(has_forbidden_core(cleaned, edges))
                self.assertTrue(initial < 1 << n and cleaned < 1 << n)

    def test_random_tiny_hypergraphs_against_independent_bruteforce(self):
        rng = random.Random(1912)
        n = 6
        pool = [bitset(c) for k in range(2, 7)
                for c in itertools.combinations(range(n), k)]
        for _ in range(45):
            chosen = tuple(sorted(rng.sample(pool, rng.randrange(0, 14))))
            p = Fraction(rng.randint(0, 8), 8)
            selected, cleaned, bound, score = (
                conditional_expectation_extract(n, chosen, p))
            self.assertEqual(bound, exact_small_expectation(n, chosen, p))
            self.assertGreaterEqual(score, bound)
            self.assertFalse(has_forbidden_core(cleaned, chosen))

    def test_gq_45_column_conflict_census_matches_full_subset_oracle(self):
        columns = w32_columns()
        self.assertEqual(len(columns), 45)
        gf5_unit_four(columns)
        c4, c6 = collision_spectrum(columns)
        self.assertTrue(c4)
        self.assertTrue(all(e.bit_count() == 4 for e in c4))
        self.assertTrue(all(e.bit_count() == 6 for e in c6))
        self.assertFalse(set(c4) & set(c6))
        for edge in (c4[:10] + c6[:10]):
            subset = tuple(columns[i] for i in range(45) if edge >> i & 1)
            self.assertIsNotNone(direct_aset_collision(subset, 5, 3))
            for omitted in range(len(subset)):
                proper = subset[:omitted] + subset[omitted+1:]
                self.assertIsNone(direct_aset_collision(proper, 5, 3))

        # Frozen original G5-B W32 2-vs-2 certificate must appear as a t4 core.
        support_indices = [
            tuple(i for i, x in enumerate(column) if x) for column in columns]
        named = ((2, 3, 6, 7), (0, 5, 8, 9), (0, 2, 6, 8), (3, 5, 7, 9))
        indices = tuple(support_indices.index(s) for s in named)
        self.assertIn(bitset(indices), c4)

        rng = random.Random(20261009)
        conflicts = c4 + c6
        for n in (4, 5, 6, 7, 8):
            for _ in range(38):
                selected = tuple(sorted(rng.sample(range(45), n)))
                mask = bitset(selected)
                direct = direct_aset_collision(
                    tuple(columns[i] for i in selected), 5, 3) is not None
                self.assertEqual(has_forbidden_core(mask, conflicts), direct)
                if n <= 6 and _ < 6:
                    signed = signed_trade(
                        tuple(columns[i] for i in selected), 5, 3) is not None
                    self.assertEqual(signed, direct)

    def test_alteration_outputs_genuine_finite_aset_for_multiple_labelings(self):
        for seed in (None, 0, 1, 2):
            columns = w32_columns(seed)
            c4, c6 = collision_spectrum(columns)
            conflicts = c4 + c6
            p, expected = optimize_first_moment(45, conflicts)
            selected, cleaned, lower, score = (
                conditional_expectation_extract(45, conflicts, p))
            self.assertEqual(expected, lower)
            self.assertGreaterEqual(score, lower)
            self.assertGreaterEqual(Fraction(cleaned.bit_count()), lower)
            self.assertTrue(validate_cleaned(columns, cleaned, conflicts))
            self.assertEqual(density_report(seed)["minimal_t4"], len(c4))
            self.assertEqual(density_report(seed)["minimal_t6"], len(c6))

    def test_frozen_w32_hosted_conflict_counts_and_exact_witness_sizes(self):
        # Pinned values from hosted Research #972, initial implementation HEAD.
        expected = {
            None: (69, 1940, 19),
            0: (53, 1874, 20),
            1: (46, 1722, 20),
            2: (50, 1750, 19),
        }
        for seed, (t4, t6, size) in expected.items():
            report = density_report(seed)
            self.assertEqual(
                (report["minimal_t4"], report["minimal_t6"],
                 report["certified_aset_columns"]),
                (t4, t6, size), seed)

    def test_six_cycle_probability_certified_by_independent_enumeration(self):
        # Independently enumerate all six distinct coordinate vertices.
        a = 6
        images = set()
        for x in itertools.permutations(range(a), 6):
            ordered_pairs = (
                (x[0], x[1]), (x[2], x[3]), (x[4], x[5]),
                (x[1], x[2]), (x[3], x[4]), (x[5], x[0]))
            labels = tuple(tuple(sorted(pair)) for pair in ordered_pairs)
            self.assertEqual(len(set(labels)), 6)
            images.add(labels)
            degree_delta = [0] * a
            for index, pair in enumerate(labels):
                sign = 1 if index < 3 else -1
                for coord in pair:
                    degree_delta[coord] += sign
            self.assertEqual(degree_delta, [0] * a)
        self.assertGreaterEqual(len(images), 720 // 12)
        lower = six_cycle_pair_probability_lower(a)
        self.assertGreaterEqual(Fraction(len(images),
                                         int(__import__("math").prod(
                                             comb(a, 2) - i for i in range(6)))),
                                lower)

    def test_gq_random_pair_labeling_expected_six_trade_lower(self):
        # This proves an EXPECTATION obstacle for uniformly random labels,
        # not a universal lower on every deterministic labeling.
        for order in (2, 4, 8, 16, 32):
            m, expected_lower = generalized_quadrangle_expectation_lower(order)
            self.assertGreaterEqual(m, 12)
            self.assertGreater(expected_lower, 0)
            self.assertGreater(expected_lower / m**4, 0)
        with self.assertRaises(ValueError):
            generalized_quadrangle_expectation_lower(3)
        self.assertEqual(expected_minimal_six_trades_lower(20, 3, 6, 6),
                         Fraction(0))
        self.assertGreater(expected_minimal_six_trades_lower(
            45, 3, 6, 6), 0)

    def test_unit_scope_rejects_weighted_and_repeated_input(self):
        with self.assertRaises(ValueError):
            gf5_unit_four(((1, 2, 1, 1),))
        with self.assertRaises(ValueError):
            gf5_unit_four(((1, 1, 1, 1), (1, 1, 1, 1)))


if __name__ == "__main__":
    unittest.main()
