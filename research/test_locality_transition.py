"""HYP-001/HYP-002 finite witness tests and theorem-boundary regressions."""
from itertools import combinations
import unittest

from lent_exhaustive import is_exact_family
from locality_transition import (
    affine_sts_blocks,
    block_incidence_columns,
    fano_sts_blocks,
    is_c4_free_bipartite,
    is_linear_three_uniform,
    projective_incidence_blocks,
    projective_plane_points,
    verify_construction,
)


def independent_pair_sum_oracle(columns, q):
    """A second deliberately small enumerator independent of G1A state tables."""
    if not columns:
        return True
    m = len(columns[0])
    states = {}
    for indices in ((), *[(i,) for i in range(len(columns))],
                    *combinations(range(len(columns)), 2)):
        state = tuple(
            sum(columns[i][j] for i in indices) % q for j in range(m)
        )
        if state in states:
            return False
        states[state] = indices
    return True


class LocalityTransitionTests(unittest.TestCase):
    def test_projective_plane_counts_and_c4_freeness(self):
        for p in (2, 3):
            n = p * p + p + 1
            self.assertEqual(len(projective_plane_points(p)), n)
            m, blocks = projective_incidence_blocks(p)
            self.assertEqual(m, 2 * n)
            self.assertEqual(len(blocks), n * (p + 1))
            self.assertTrue(is_c4_free_bipartite(blocks, n))
            for q in (3, 5, 7):
                columns = block_incidence_columns(m, blocks, q)
                self.assertTrue(is_exact_family(columns, q, 2))
                self.assertTrue(independent_pair_sum_oracle(columns, q))

    def test_steiner_fano_and_affine_counts(self):
        for m, blocks in (fano_sts_blocks(), affine_sts_blocks(2),
                          affine_sts_blocks(3)):
            self.assertTrue(is_linear_three_uniform(blocks))
            self.assertEqual(len(blocks), m * (m - 1) // 6)
            self.assertEqual(len({
                pair for block in blocks for pair in combinations(block, 2)
            }), m * (m - 1) // 2)
            for q in (3, 5):
                self.assertTrue(verify_construction(m, blocks, q, 3)["aset_exact"])
                # The independent oracle is slower for 117 columns; still
                # manageable but only use it for the smaller fixed fixtures.
                if m <= 9:
                    self.assertTrue(independent_pair_sum_oracle(
                        block_incidence_columns(m, blocks, q), q
                    ))

    def test_odd_characteristic_is_essential(self):
        # Pasch configuration: distinct pairs of triples collide over GF(2)
        # because their two doubled coordinates disappear. They do NOT
        # collide in odd characteristic, even though it is linear.
        pasch = [(0, 1, 2), (0, 3, 4), (1, 3, 5), (2, 4, 5)]
        self.assertTrue(is_linear_three_uniform(pasch))
        self.assertFalse(verify_construction(6, pasch, 2, 3)["aset_exact"])
        for q in (3, 5, 7):
            self.assertTrue(verify_construction(6, pasch, q, 3)["aset_exact"])

    def test_c4_collision_rejected(self):
        square = [(0, 2), (0, 3), (1, 2), (1, 3)]
        self.assertFalse(is_c4_free_bipartite(square, 2))
        for q in (3, 5, 7):
            self.assertFalse(verify_construction(4, square, q, 2)["aset_exact"])

    def test_non_linear_triples_can_collide_even_over_odd_fields(self):
        # (012)+(345)=(013)+(245) for every characteristic.
        blocks = [(0, 1, 2), (3, 4, 5), (0, 1, 3), (2, 4, 5)]
        self.assertFalse(is_linear_three_uniform(blocks))
        for q in (3, 5, 7):
            self.assertFalse(verify_construction(6, blocks, q, 3)["aset_exact"])

    def test_inputs_are_fail_closed(self):
        with self.assertRaises(ValueError):
            projective_plane_points(4)
        with self.assertRaises(ValueError):
            affine_sts_blocks(0)
        with self.assertRaises(ValueError):
            block_incidence_columns(4, [(0, 1), (0, 1)], 3)
        with self.assertRaises(ValueError):
            block_incidence_columns(4, [(2, 1)], 3)
        with self.assertRaises(ValueError):
            block_incidence_columns(4, [(2, 5)], 3)
        with self.assertRaises(ValueError):
            block_incidence_columns(4, [(0, 1)], 9)


if __name__ == "__main__":
    unittest.main()
