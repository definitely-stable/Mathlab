from itertools import combinations
import unittest

from lent_exact import finite_bound_holds, hamming_ball, input_count
from lent_exhaustive import (
    collision_witness,
    has_small_gf2_dependency,
    is_exact_family,
    linear_dependency_witness,
    signed_relation_witness,
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

    def test_signed_relation_equivalence_small_prime_fields(self) -> None:
        for q in (2, 3, 5):
            candidates = sparse_nonzero_vectors(q, 2, 1)
            for d in (1, 2):
                for v in range(1, min(3, len(candidates)) + 1):
                    for columns in combinations(candidates, v):
                        exact = is_exact_family(columns, q, d)
                        signed = signed_relation_witness(columns, q, d)
                        self.assertEqual(exact, signed is None)

    def test_full_independence_implies_aset_small(self) -> None:
        for q in (3, 5):
            candidates = sparse_nonzero_vectors(q, 2, 1)
            for v in range(1, min(3, len(candidates)) + 1):
                for columns in combinations(candidates, v):
                    dependency = linear_dependency_witness(columns, q, 2)
                    if dependency is None:
                        self.assertTrue(is_exact_family(columns, q, 1))

    def test_q3_pinned_separation_and_side_bound(self) -> None:
        columns = [(1,), (2,)]
        self.assertTrue(is_exact_family(columns, 3, 1))
        self.assertIsNone(signed_relation_witness(columns, 3, 1))
        self.assertIsNotNone(linear_dependency_witness(columns, 3, 2))

    def test_q5_pinned_separation(self) -> None:
        columns = [(1,), (2,)]
        self.assertTrue(is_exact_family(columns, 5, 1))
        self.assertIsNone(signed_relation_witness(columns, 5, 1))
        self.assertIsNotNone(linear_dependency_witness(columns, 5, 2))

    def test_d_zero_has_no_signed_relation(self) -> None:
        columns = [(1,), (2,)]
        self.assertTrue(is_exact_family(columns, 3, 0))
        self.assertIsNone(signed_relation_witness(columns, 3, 0))

    def test_g1a_rejects_nonprime_grid_field(self) -> None:
        with self.assertRaises(ValueError):
            linear_dependency_witness([(1,), (2,)], 4, 2)


if __name__ == "__main__":
    unittest.main()
