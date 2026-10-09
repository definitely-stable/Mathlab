"""HYP-105 G3 independent tests of finite Smith-divisor core classification.

Complete only for unit columns, linear triple hypergraphs, <=6 edges.
Supports an all-characteristics>=5 deduction via integer minor gcds.
"""
import itertools
import unittest

from hyp105_minor import (
    classification,
    core_patterns,
    determinant_bareiss,
    is_grid,
    maximal_minor_gcd,
    rank_mod_prime,
)


class SixColumnCoreCertificateTests(unittest.TestCase):
    def test_exact_exhaustive_minor_histogram(self):
        self.assertEqual(classification(), {
            1: {}, 2: {}, 3: {},
            4: {2: 1},
            5: {3: 10},
            6: {0: 10, 1: 360, 2: 60, 3: 60, 4: 30},
        })

    def test_singular_iff_structural_grid_and_no_large_prime_divisors(self):
        total = 0
        for t in range(1, 7):
            for rows in core_patterns(t):
                gcd_minors = maximal_minor_gcd(rows, t)
                self.assertEqual(gcd_minors == 0, is_grid(rows, t),
                                 (t, rows, gcd_minors))
                self.assertIn(gcd_minors, (0, 1, 2, 3, 4))
                total += 1
        self.assertEqual(total, 1 + 10 + 520)

    def test_independent_field_ranks_equal_integer_minor_prediction(self):
        # All 531 row-unlabelled cores; an entirely separate modular
        # elimination procedure checks the exact integer minor oracle.
        for t in range(1, 7):
            for rows in core_patterns(t):
                d = maximal_minor_gcd(rows, t)
                for p in (2, 3, 5, 7, 11, 13, 17, 19, 23):
                    self.assertEqual(rank_mod_prime(rows, t, p) == t,
                                     d % p != 0 if d else False,
                                     (t, rows, p, d))

    def test_bareiss_against_permutation_determinant(self):
        # Independent Leibniz determinant for every binary matrix up to 3x3.
        for n in range(1, 4):
            for bits in itertools.product((0, 1), repeat=n*n):
                matrix = [bits[i*n:(i+1)*n] for i in range(n)]
                reference = 0
                for perm in itertools.permutations(range(n)):
                    inversions = sum(perm[i] > perm[j]
                                     for i in range(n)
                                     for j in range(i+1, n))
                    value = -1 if inversions % 2 else 1
                    for i, j in enumerate(perm):
                        value *= matrix[i][j]
                    reference += value
                self.assertEqual(determinant_bareiss(matrix), reference)

    def test_paschs_are_only_characteristic_two_and_five_edge_chars_three(self):
        cases4 = list(core_patterns(4))
        cases5 = list(core_patterns(5))
        self.assertEqual(len(cases4), 1)
        self.assertEqual(len(cases5), 10)
        self.assertEqual(rank_mod_prime(cases4[0], 4, 2), 3)
        self.assertEqual(rank_mod_prime(cases4[0], 4, 5), 4)
        for rows in cases5:
            self.assertLess(rank_mod_prime(rows, 5, 3), 5)
            self.assertEqual(rank_mod_prime(rows, 5, 5), 5)

    def test_grid_six_edges_singular_over_every_field(self):
        examples = [rows for rows in core_patterns(6) if is_grid(rows, 6)]
        self.assertEqual(len(examples), 10)
        for rows in examples:
            self.assertEqual(maximal_minor_gcd(rows, 6), 0)
            for p in (2, 3, 5, 7, 11):
                self.assertLess(rank_mod_prime(rows, 6, p), 6)


if __name__ == "__main__":
    unittest.main()
