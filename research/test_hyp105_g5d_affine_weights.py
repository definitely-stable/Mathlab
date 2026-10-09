"""Independent adversarial GF5 checks for affine-checksum sparse ASET."""
from itertools import combinations
import unittest

from hyp105_g5d_affine_weights import (
    P, M, CHECKSUM, add_field_encoded, checksum_pattern_palette,
    decode_field, encode_support, finite_weighted_greedy, summary,
    verify_independent_full_sums, w32_supports
)
from test_hyp105_g5c_signed_oracles import direct_aset_collision


class AffineChecksumGF5Tests(unittest.TestCase):
    def test_51_nonzero_coeff_palette_and_exact_checksum(self):
        patterns = checksum_pattern_palette()
        self.assertEqual(len(patterns), 51)
        self.assertIn((1, 1, 1, 1), patterns)
        self.assertTrue(all(all(1 <= x <= 4 for x in pattern)
                            and sum(pattern) % 5 == 4
                            for pattern in patterns))
        self.assertEqual(len(set(patterns)), len(patterns))
        # Finite exhaustive proof of affine-slice cardinality formula:
        # 4^4=256 possible nonzero patterns, 51 sum to each nonzero c.
        from itertools import product
        by_sum = [0] * 5
        for pattern in product(range(1, 5), repeat=4):
            by_sum[sum(pattern) % 5] += 1
        self.assertEqual(by_sum, [52, 51, 51, 51, 51])

    def test_field_arithmetic_is_digitwise_mod5_not_integer_addition(self):
        self.assertEqual(
            decode_field(add_field_encoded(encode_support((0, 1, 2, 3),
                                                          (4, 4, 4, 2)),
                                           encode_support((0, 1, 2, 3),
                                                          (4, 4, 4, 2)))),
            (3, 3, 3, 4) + (0,) * 8)
        with self.assertRaises(ValueError):
            encode_support((0, 1, 2, 3), (1, 1, 1, 2))
        with self.assertRaises(ValueError):
            encode_support((0, 0, 2, 3), (1, 1, 1, 1))
        with self.assertRaises(ValueError):
            add_field_encoded(-1, 0)

    def test_full_weighted_w32_45_column_certificate_against_old_gf5_oracle(self):
        r = finite_weighted_greedy(seed=20261009, max_attempts=4)
        self.assertEqual(r["accepted_columns"], 45)
        self.assertEqual(len(r["column_ids"]), 45)
        self.assertEqual(len(r["vectors"]), 45)
        self.assertEqual(r["m"], 12)
        self.assertEqual(r["palette_size"], 51)
        self.assertEqual(r["checksum"], 4)
        self.assertEqual(sum(x != 0 for row in r["vectors"] for x in row),
                         4 * 45)
        self.assertTrue(verify_independent_full_sums(r["vectors"]))
        self.assertIsNone(direct_aset_collision(r["vectors"], 5, 3))
        self.assertFalse(r["asymptotic_improvement_proven"])
        self.assertEqual((1 + 45 + 990 + 14190), 15226)
        self.assertEqual(summary(20261009)["accepted"], 45)
        self.assertEqual(summary(20261009)["seed"], 20261009)

    def test_held_out_greedy_seeds_and_independent_replay(self):
        for seed in (0, 3, 17):
            result = finite_weighted_greedy(seed, max_attempts=2)
            self.assertEqual(result, finite_weighted_greedy(seed, max_attempts=2))
            self.assertEqual(result["accepted_columns"], 45, seed)
            self.assertTrue(verify_independent_full_sums(result["vectors"]))
            self.assertIsNone(direct_aset_collision(result["vectors"], 5, 3))

    def test_unit_subfamily_really_does_have_trades_and_corruption_is_detected(self):
        old = []
        for support in w32_supports():
            row = [0] * 12
            for pos in support:
                row[pos] = 1
            old.append(tuple(row))
        self.assertIsNotNone(direct_aset_collision(tuple(old), 5, 3))
        self.assertFalse(verify_independent_full_sums(tuple(old)))
        result = finite_weighted_greedy(20261009, max_attempts=1)
        self.assertEqual(result["accepted_columns"], 45)
        vectors = list(result["vectors"])
        vectors[1] = vectors[0]
        self.assertFalse(verify_independent_full_sums(tuple(vectors)))
        vectors = list(result["vectors"])
        changed = list(vectors[0])
        changed[next(i for i, x in enumerate(changed) if x)] = 0
        vectors[0] = tuple(changed)
        self.assertFalse(verify_independent_full_sums(tuple(vectors)))

    def test_checksum_blocks_unequal_subset_sizes_for_all_gf5_vectors(self):
        # Pure algebraic implication independent of support, unit weights,
        # chosen W32 graph and even actual distinctness of equal sizes.
        for k in range(4):
            for ell in range(4):
                if k != ell:
                    self.assertNotEqual(k * CHECKSUM % P,
                                        ell * CHECKSUM % P)


if __name__ == "__main__":
    unittest.main()
