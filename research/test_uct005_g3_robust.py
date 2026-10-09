"""UCT-005 G3-A: independent finite oracles and explicit outside-model controls."""
from itertools import combinations, product
from math import comb
import unittest

from uct005_g3_robust import (
    volume, possible_probe_support, potential_query_nodes, robust_packing_bound,
    ball_words, hamming, exact_ball_packing, sparse_masks, encode_subset,
    near_trade_witness, sparse_code_capacity_bound, nearest_unique_decode,
)


def independent_ball_count(q, n, radius):
    return len([x for x in product(range(q), repeat=n)
                if sum(v != 0 for v in x) <= radius])


def independent_packing(q, n, radius, errors):
    words = [word for word in product(range(q), repeat=n)
             if sum(x != 0 for x in word) <= radius]
    # Separate combinations oracle (not the clique recurrence in production).
    # Deliberately small; deterministic and exhaustive.
    for k in range(len(words), -1, -1):
        for chosen in combinations(range(len(words)), k):
            if all(sum(a != b for a, b in zip(words[i], words[j])) > 2 * errors
                   for i, j in combinations(chosen, 2)):
                return k
    raise AssertionError("empty code should always exist")


def independent_syndromes(columns, rows, prime, d):
    """Raw enumeration via subset tuples, not production sparse bitmasks."""
    result = []
    for size in range(min(d, len(columns)) + 1):
        for selected in combinations(range(len(columns)), size):
            word = tuple(sum(columns[i][j] for i in selected) % prime
                         for j in range(rows))
            result.append((selected, word))
    return result


class Uct005G3RobustTests(unittest.TestCase):
    def test_ball_volume_qary_against_literal_cartesian_enumeration(self):
        for q in (2, 3):
            for cells in range(5):
                for radius in range(cells + 3):
                    self.assertEqual(volume(q, cells, radius),
                                     independent_ball_count(q, cells, radius))
                    self.assertEqual(len(ball_words(q, cells, radius)),
                                     independent_ball_count(q, cells, radius))

    def test_robust_packing_exact_against_independent_subsets(self):
        for q, max_n, max_radius in ((2, 4, 2), (3, 2, 2)):
            for n in range(max_n + 1):
                for r in range(min(max_radius, n) + 1):
                    for e in (0, 1, 2):
                        actual = exact_ball_packing(q, n, r, e)
                        expected = independent_packing(q, n, r, e)
                        self.assertEqual(actual, expected, (q, n, r, e))
                        local_sphere = volume(q, n, r + e) // volume(q, n, e)
                        self.assertLessEqual(actual, local_sphere)

    def test_joint_error_and_reachable_ball_strict_numeric_gain(self):
        # m=8, d*w=2, e=1, all queried coordinates exposed.
        self.assertEqual(volume(2, 8, 2), 37)
        self.assertEqual(volume(2, 8, 3), 93)
        self.assertEqual(volume(2, 8, 1), 9)
        self.assertEqual((1 << 8) // 9, 28)
        self.assertEqual(robust_packing_bound(2, 8, 2, 1, 1, 8, 1, 0), 10)
        self.assertGreater(28, 10)
        self.assertGreater(37, 10)
        # P=0, W=0, and H paid trusted bits: no phantom remote information.
        self.assertEqual(robust_packing_bound(2, 8, 2, 1, 1, 8, 0, 0), 1)
        self.assertEqual(robust_packing_bound(2, 8, 2, 0, 1, 8, 4, 1), 2)

    def test_potential_adaptive_query_addresses_and_zero_probes(self):
        for q in (2, 3, 4):
            for probes in range(5):
                expected = sum(q ** i for i in range(probes))
                self.assertEqual(potential_query_nodes(q, probes), expected)
                self.assertEqual(possible_probe_support(q, 100, 3, probes),
                                 min(100, 3 * expected))
        with self.assertRaises(ValueError):
            robust_packing_bound(2, 4, 1, 1, 0, 0, 1, 0)
        with self.assertRaises(ValueError):
            volume(1, 4, 2)

    def test_near_trades_independent_gf2_gf3_gf5_matrix_enumeration(self):
        for prime, rows, cols, d in ((2, 2, 2, 1),
                                     (3, 2, 2, 1),
                                     (5, 2, 2, 1),
                                     (3, 2, 3, 2)):
            vectors = tuple(product(range(prime), repeat=rows))
            for selected in product(vectors, repeat=cols):
                raw = independent_syndromes(selected, rows, prime, d)
                for e in (0, 1):
                    expected = None
                    for i in range(len(raw)):
                        for j in range(i + 1, len(raw)):
                            distance = sum(x != y for x, y
                                           in zip(raw[i][1], raw[j][1]))
                            if distance <= 2 * e:
                                expected = distance
                                break
                        if expected is not None:
                            break
                    actual = near_trade_witness(selected, rows, prime, d, e)
                    self.assertEqual(actual is None, expected is None)
                    if actual is not None:
                        self.assertEqual(actual[2], expected)

    def test_sparse_exact_and_robust_recovery_are_distinct(self):
        for n in range(1, 6):
            identity = tuple(tuple(int(i == j) for j in range(n))
                             for i in range(n))
            self.assertIsNone(near_trade_witness(identity, n, 2, 1, 0))
            self.assertIsNotNone(near_trade_witness(identity, n, 2, 1, 1))
        repeated = ((1, 1, 1, 0, 0, 0), (0, 0, 0, 1, 1, 1))
        self.assertIsNone(near_trade_witness(repeated, 6, 2, 1, 1))
        codebook = {
            mask: encode_subset(repeated, 6, 2, mask)
            for mask in sparse_masks(2, 1)
        }
        for mask, word in codebook.items():
            for pos in range(6):
                corrupted = tuple((v ^ int(j == pos)) for j, v
                                  in enumerate(word))
                self.assertEqual(nearest_unique_decode(codebook, corrupted, 1),
                                 mask)
        left, right = sparse_code_capacity_bound(2, 6, 2, 1, 3, 1)
        self.assertLessEqual(left, right)

    def test_no_false_equation_between_recover_u_and_observe_CA_u(self):
        repeated_columns = ((1, 0), (0, 1))
        u1 = encode_subset(repeated_columns, 2, 2, 1)
        u2 = encode_subset(repeated_columns, 2, 2, 2)
        self.assertNotEqual(u1, u2)
        # Observer C=(1,1), both have same response. Distinguishable
        # sparse INPUTS need not imply distinguishable subscriber OUTPUTS.
        self.assertEqual((u1[0] ^ u1[1]), (u2[0] ^ u2[1]))

    def test_reject_false_input_types_and_mismatched_dimensions(self):
        with self.assertRaises(ValueError):
            sparse_masks(-1, 2)
        with self.assertRaises(ValueError):
            encode_subset(((1, 0), (0, 1)), 3, 2, 1)
        with self.assertRaises(ValueError):
            encode_subset(((1, 0),), 2, 4, 0)
        with self.assertRaises(ValueError):
            exact_ball_packing(2, 10, 5, 1)


if __name__ == "__main__":
    unittest.main()
