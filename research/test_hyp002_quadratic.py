"""HYP-002: C4 fiber necessity and finite quadratic upper falsification."""
from itertools import combinations
import unittest

from lent_exhaustive import is_exact_family, sparse_nonzero_vectors
from hyp002_quadratic import (
    c4_witness,
    fiber_pair_certificate,
    prefix_pair_fibers,
    quadratic_capacity_bound,
)
from locality_transition import affine_sts_blocks, block_incidence_columns


class QuadraticCapacityTests(unittest.TestCase):
    def test_closed_bound_monotonic_and_below_raw_column_count(self):
        for q in (2, 3, 5, 7):
            last = -1
            for m in range(1, 36):
                result = quadratic_capacity_bound(m, q)
                self.assertLessEqual(
                    result["proved_upper"], result["all_nonzero_support_le_3"]
                )
                self.assertGreaterEqual(result["proved_upper"], last)
                last = result["proved_upper"]
                if m >= 12 and q == 3:
                    self.assertLess(
                        result["proved_upper"],
                        result["all_nonzero_support_le_3"],
                    )

    def test_prefix_fiber_c4_is_actual_four_column_collision(self):
        # Different two-coordinate prefixes, common two right states.
        # This is the exact 2+2 collision counted in the proof, for all q.
        for q in (2, 3, 5, 7):
            vectors = [
                tuple(int(i in block) for i in range(5))
                for block in ((0, 1, 3), (0, 1, 4),
                              (0, 2, 3), (0, 2, 4))
            ]
            self.assertIsNotNone(c4_witness(prefix_pair_fibers(vectors, q)))
            self.assertTrue(fiber_pair_certificate(vectors, q)["has_forbidden_c4"])
            self.assertFalse(is_exact_family(vectors, q, 2))
            left = tuple((a + b) % q for a, b in zip(vectors[0], vectors[3]))
            right = tuple((a + b) % q for a, b in zip(vectors[1], vectors[2]))
            self.assertEqual(left, right)

    def test_weighted_prefix_c4_is_actual_signed_collision(self):
        q = 5
        # Prefix labels include coefficients; right labels include coefficients.
        def v(pair, suffix):
            ans = [0] * 5
            for i, coefficient in pair + (suffix,):
                ans[i] = coefficient
            return tuple(ans)
        a = ((0, 2), (1, 3))
        b = ((0, 1), (2, 4))
        r = (3, 2)
        s = (4, 3)
        cols = [v(a, r), v(a, s), v(b, r), v(b, s)]
        self.assertIsNotNone(c4_witness(prefix_pair_fibers(cols, q)))
        self.assertFalse(is_exact_family(cols, q, 2))

    def test_c4_criterion_is_not_sufficient_for_aset(self):
        # Adversarial 2+2 collision not explained by a fiber C4:
        # (012)+(345)=(013)+(245).
        cols = [
            tuple(int(i in block) for i in range(6))
            for block in ((0, 1, 2), (3, 4, 5), (0, 1, 3), (2, 4, 5))
        ]
        for q in (3, 5, 7):
            self.assertIsNone(c4_witness(prefix_pair_fibers(cols, q)))
            self.assertFalse(is_exact_family(cols, q, 2))

    def test_exhaustive_small_subsets_independent_aset_oracle(self):
        # All subset families from weight-three vectors over GF(3)^3.
        # The "if exact then no-C4" implication is checked independently.
        for q, m, w in ((3, 3, 3), (3, 4, 2), (5, 3, 2)):
            population = sparse_nonzero_vectors(q, m, w)
            # Cover all 1/2/3-column combinations from the full grid.
            for v in range(1, 4):
                for family in combinations(population, v):
                    if is_exact_family(family, q, 2):
                        self.assertIsNone(
                            c4_witness(prefix_pair_fibers(family, q))
                        )
                        self.assertLessEqual(
                            len(family), quadratic_capacity_bound(m, q)["proved_upper"]
                        )

    def test_affine_large_exact_witness_and_proof_certificate(self):
        for rank in (2, 3):
            m, blocks = affine_sts_blocks(rank)
            for q in (3, 5, 7):
                cols = block_incidence_columns(m, blocks, q)
                self.assertTrue(is_exact_family(cols, q, 2))
                cert = fiber_pair_certificate(cols, q)
                self.assertFalse(cert["has_forbidden_c4"])
                self.assertLessEqual(
                    cert["right_pair_uses"], cert["right_pair_budget"]
                )
                self.assertLessEqual(
                    len(cols), quadratic_capacity_bound(m, q)["proved_upper"]
                )

    def test_fail_closed(self):
        with self.assertRaises(ValueError):
            quadratic_capacity_bound(4, 4)
        with self.assertRaises(ValueError):
            quadratic_capacity_bound(-1, 3)
        with self.assertRaises(ValueError):
            prefix_pair_fibers([(1, 0, 0), (1, 0, 0)], 3)
        with self.assertRaises(ValueError):
            prefix_pair_fibers([(0, 0, 0)], 3)
        with self.assertRaises(ValueError):
            prefix_pair_fibers([(1, 1, 1, 1)], 3)
        with self.assertRaises(ValueError):
            prefix_pair_fibers([(1, 0, 0), (1, 0)], 3)
        with self.assertRaises(ValueError):
            prefix_pair_fibers([(3, 0, 0)], 3)


if __name__ == "__main__":
    unittest.main()
