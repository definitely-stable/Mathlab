"""ALG-001 G0: independent GF(2)/GF(3) elimination and rank/output barrier."""
import itertools
import unittest

from alg001_oracle import (
    rank_mod_prime, all_matrices, entry_update, fixed_rank_one_rows,
    rank_one_observation_lower_bits,
)
from dag002_oracle import antichain_observable_masks


class Alg001G0Tests(unittest.TestCase):
    def test_all_small_field_matrices_and_all_one_cell_changes(self):
        for p, dims in ((2, ((1, 1), (2, 2), (3, 3))),
                        (3, ((1, 1), (2, 2)))):
            for nr, nc in dims:
                for matrix in all_matrices(p, nr, nc):
                    rank = rank_mod_prime(matrix, p)
                    self.assertGreaterEqual(rank, 0)
                    self.assertLessEqual(rank, min(nr, nc))
                    for i in range(nr):
                        for j in range(nc):
                            for value in range(p):
                                changed = entry_update(matrix, i, j, value)
                                other_rank = rank_mod_prime(changed, p)
                                self.assertLessEqual(abs(rank - other_rank), 1)
                                if matrix[i][j] == value:
                                    self.assertEqual(rank, other_rank)

    def test_nonzero_rank_one_rows_require_many_coordinate_patterns(self):
        for p in (2, 3):
            for n in range(1, 9 if p == 2 else 6):
                vectors = set()
                for one_row_matrix in fixed_rank_one_rows(n, p):
                    self.assertEqual(rank_mod_prime(one_row_matrix, p), 1)
                    vectors.add(tuple(one_row_matrix[0][i] for i in range(n)))
                self.assertEqual(len(vectors), p ** n - 1)
                expected = (p ** n - 2).bit_length()
                self.assertEqual(rank_one_observation_lower_bits(n, p), expected)
                if p == 2 and n >= 2:
                    self.assertEqual(expected, n)
                if n == 1 and p == 2:
                    # Only nonzero row is (1), so rank and its coordinates
                    # are both fixed and the restricted capacity bound is 0.
                    self.assertEqual(expected, 0)

    def test_independent_binary_antichain_vs_row_vector_outputs(self):
        for n in range(1, 9):
            dag_patterns = set(antichain_observable_masks(n))
            matrix_patterns = {(0,) * n} | {
                tuple(row[0]) for row in fixed_rank_one_rows(n, 2)
            }
            self.assertEqual(matrix_patterns, dag_patterns)

    def test_rank_only_promised_family_needs_no_input_dependent_output(self):
        for n in range(1, 7):
            results = {rank_mod_prime(mat, 2)
                       for mat in fixed_rank_one_rows(n, 2)}
            self.assertEqual(results, {1})
            self.assertEqual((len(results) - 1).bit_length(), 0)

    def test_invalid_fields_and_ragged_rows(self):
        with self.assertRaises(ValueError):
            rank_mod_prime(((1,),), 4)
        with self.assertRaises(ValueError):
            rank_mod_prime(((1, 2), (1,)), 3)
        with self.assertRaises(ValueError):
            rank_one_observation_lower_bits(0)
        self.assertEqual(rank_mod_prime((), 2), 0)
        self.assertEqual(rank_mod_prime(((0, 0), (0, 0)), 2), 0)
        self.assertEqual(rank_mod_prime(((1, 0), (0, 1)), 2), 2)


if __name__ == "__main__":
    unittest.main()
