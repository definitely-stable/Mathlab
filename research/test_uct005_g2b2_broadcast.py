"""UCT-005 G2-B2: exhaustive independent checks for restricted quotient broadcast."""
from itertools import product
import unittest
from uct005_g2b2_broadcast import (
    all_nonempty_update_alphabets, apply_message, conflict_colors_exact,
    encode_and_decode, image_set, iter_all_binary_matrices,
    min_fixed_broadcast_bits, outputs_for, rank_gf2, syndrome,
)


class ExactBroadcastQuotientTests(unittest.TestCase):
    def test_small_matrices_and_all_update_alphabets_independently(self):
        # All 2^9 matrices and all 2^(2^3)-1 nonempty delta subsets.
        for m in (1, 2, 3):
            for h in (1, 2, 3):
                for rows in iter_all_binary_matrices(h, m):
                    for ds in all_nonempty_update_alphabets(m):
                        images = {tuple((row & d).bit_count() % 2
                                        for row in rows) for d in ds}
                        expected = (len(images) - 1).bit_length()
                        self.assertEqual(min_fixed_broadcast_bits(rows, ds),
                                         expected, (m, h, rows, ds))
                        self.assertEqual(len(image_set(rows, ds)), len(images))
                        code, words = encode_and_decode(rows, ds)
                        self.assertEqual(len(code), len(images))
                        for d in ds:
                            decoded = words[code[syndrome(rows, d)]]
                            self.assertEqual(decoded, syndrome(rows, d))

    def test_independent_conflict_graph_coloring_tiny_instances(self):
        # Exhaustively enumerate all color assignments; this does NOT invoke
        # rank, quotient/image-size calculation for the conflict predicate.
        for m in (1, 2):
            for h in (1, 2):
                for rows in iter_all_binary_matrices(h, m):
                    for ds in all_nonempty_update_alphabets(m):
                        min_colors = next(k for k in range(1, len(ds) + 1)
                                          if conflict_colors_exact(rows, ds, k))
                        self.assertEqual((min_colors - 1).bit_length(),
                                         min_fixed_broadcast_bits(rows, ds))
                        self.assertEqual(min_colors, len(image_set(rows, ds)))

    def test_full_cube_equals_gf2_rank(self):
        for m in range(1, 6):
            for h in range(1, 6):
                for rows in iter_all_binary_matrices(h, m):
                    # Larger dimensions are checked exhaustively for h*m<=15
                    # only; below all 32-dimensional masks are always checked.
                    if h * m > 15:
                        break
                    ds = range(1 << m)
                    self.assertEqual(min_fixed_broadcast_bits(rows, ds),
                                     rank_gf2(rows), (m, h, rows))

    def test_unit_update_columns_not_rank_counterexample(self):
        for m in range(2, 14):
            rows = tuple(1 << i for i in range(m))
            units = tuple(1 << i for i in range(m))
            self.assertEqual(rank_gf2(rows), m)
            expected = (m - 1).bit_length()
            self.assertEqual(min_fixed_broadcast_bits(rows, units), expected)
            distinct_columns = {syndrome(rows, d) for d in units}
            self.assertEqual(len(distinct_columns), m)
        rows = tuple(1 << i for i in range(8))
        self.assertEqual(rank_gf2(rows), 8)
        self.assertEqual(min_fixed_broadcast_bits(rows,
                         [1 << i for i in range(8)]), 3)
        all_rows_equal = (0b111111, ) * 20
        self.assertEqual(min_fixed_broadcast_bits(
            all_rows_equal, range(1 << 6)), 1)
        # Mandatory tick (no no-op), each singleton update flips every
        # subscriber bit; no update-dependent broadcast needed in this layer.
        self.assertEqual(min_fixed_broadcast_bits(
            all_rows_equal, [1 << i for i in range(6)]), 0)

    def test_no_op_vs_known_tick_is_explicit_not_hidden(self):
        rows = (0b11111, 0b11111)
        only_flips = [1 << i for i in range(5)]
        self.assertEqual(min_fixed_broadcast_bits(rows, only_flips), 0)
        self.assertEqual(min_fixed_broadcast_bits(rows, [0] + only_flips), 1)
        # A zero column included among unit updates can include 0 syndrome.
        self.assertEqual(min_fixed_broadcast_bits((0b0011,),
                         [1, 2, 4, 8]), 1)

    def test_exact_adaptive_multi_epoch_subscribers(self):
        # Five subscribers, seven source bits; no subscriber ever observes
        # d except from the single common finite-alphabet message.
        rows = (0b1000001, 0b0111011, 0b1111111,
                0b0101010, 0b0000000)
        alphabet = (0, 1, 2, 4, 8, 16, 32, 64, 65, 12)
        code, words = encode_and_decode(rows, alphabet)
        epoch = 0
        x = 0
        outputs = outputs_for(rows, x)
        for step in range(180):
            d = alphabet[(step * 7 + x.bit_count() + epoch // 5) % len(alphabet)]
            msg = code[syndrome(rows, d)]
            outputs = apply_message(rows, outputs, msg, words)
            x ^= d
            epoch += 1
            self.assertEqual(outputs, outputs_for(rows, x))
            self.assertLess(msg, 1 << min_fixed_broadcast_bits(rows, alphabet))

    def test_finite_dag_path_parity_as_subscription_matrix(self):
        # s0->a,b; both a,b->t. t has two structural paths but
        # zero algebraic derivative. Subscriber rows are DAG derivatives.
        # Outputs (s0,a,b,t) == (x,x,x,0), so only two delta syndromes.
        rows = (0b1, 0b1, 0b1, 0b0)
        self.assertEqual(min_fixed_broadcast_bits(rows, (0, 1)), 1)
        self.assertEqual(min_fixed_broadcast_bits(rows, (1,)), 0)
        self.assertEqual(rank_gf2(rows), 1)


if __name__ == "__main__":
    unittest.main()
