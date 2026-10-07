from itertools import combinations
import unittest

from lent_exact import finite_bound_holds, hamming_ball, input_count
from lent_exhaustive import (
    collision_witness,
    has_small_gf2_dependency,
    is_exact_family,
    sparse_nonzero_vectors,
)


class ExactArithmeticTests(unittest.TestCase):
    def test_input_count(self) -> None:
        self.assertEqual(input_count(5, 2), 16)
        self.assertEqual(input_count(3, 99), 8)

    def test_hamming_ball(self) -> None:
        self.assertEqual(hamming_ball(2, 4, 2), 11)
        self.assertEqual(hamming_ball(3, 2, 1), 5)

    def test_known_exact_identity_family(self) -> None:
        columns = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        self.assertTrue(is_exact_family(columns, 2, 2))
        self.assertTrue(finite_bound_holds(3, 2, 3, 2, 1))

    def test_known_collision(self) -> None:
        columns = [(1, 0), (0, 1), (1, 1)]
        witness = collision_witness(columns, 2, 2)
        self.assertIsNotNone(witness)
        self.assertFalse(is_exact_family(columns, 2, 2))

    def test_binary_dependency_equivalence_small(self) -> None:
        candidates = sparse_nonzero_vectors(2, 4, 2)
        for v in range(1, 5):
            for columns in combinations(candidates, v):
                exact = is_exact_family(columns, 2, 2)
                dependency = has_small_gf2_dependency(columns, 4)
                self.assertEqual(exact, not dependency)


if __name__ == "__main__":
    unittest.main()
