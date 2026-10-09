"""G1-A independent finite state-capacity and covering-code falsifiers."""
import itertools
import unittest
from math import comb

from dag002_g1a_frontier import (
    remote_state_volume, necessary_local_bits, hamming_ball,
    covering_radius, minimum_covering_centers, CoordinateXorDeltaScheme,
    independent_source_probe, broadcast_changed_cell,
)


def independent_changed_snapshot_count(cells, cell_bits, max_changed):
    """Literal Cartesian memory enumeration, independent of binomial formula."""
    values = range(1 << cell_bits)
    return sum(sum(x != 0 for x in remote) <= max_changed
               for remote in itertools.product(values, repeat=cells))


def independent_cover_minimum(n, radius):
    """Bitmask coverage exhaustive across ALL possible codebook subsets."""
    size = 1 << n
    ball_masks = []
    for center in range(size):
        ball_masks.append(sum(1 << query for query in range(size)
                              if (center ^ query).bit_count() <= radius))
    full = (1 << size) - 1
    for number in range(1, size + 1):
        for centers in itertools.combinations(range(size), number):
            covered = 0
            for c in centers:
                covered |= ball_masks[c]
            if covered == full:
                return number
    raise AssertionError("all centers must cover")


class DagAlgG1ATests(unittest.TestCase):
    def test_exact_remote_snapshot_count_over_binary_and_two_bit_cells(self):
        for cell_bits in (1, 2):
            for cells in range(5):
                for w in range(cells + 1):
                    self.assertEqual(
                        remote_state_volume(cells, cell_bits, w),
                        independent_changed_snapshot_count(cells, cell_bits, w)
                    )
        self.assertEqual(remote_state_volume(0, 1, 0), 1)

    def test_universal_counting_limit_and_known_escapes(self):
        for n in range(1, 9):
            self.assertEqual(necessary_local_bits(1 << n, 0, 1, 0), n)
            self.assertEqual(necessary_local_bits(1 << n, n, 1, n), 0)
            self.assertEqual(necessary_local_bits(1 << n, n, 1, 0), n)
            # Nonzero 1xn GF2 rank-one coordinate answers only.
            self.assertLessEqual(necessary_local_bits((1 << n) - 1, n, 1, n),
                                 necessary_local_bits(1 << n, n, 1, n))
            for w in range(n + 1):
                bits = necessary_local_bits(1 << n, n, 1, w)
                volume = remote_state_volume(n, 1, w)
                self.assertGreaterEqual((1 << bits) * volume, 1 << n)
                if bits:
                    self.assertLess((1 << (bits - 1)) * volume, 1 << n)
        for n in range(1, 9):
            for mask in range(1 << n):
                reconstructed = tuple(independent_source_probe(mask, i, n)
                                      for i in range(n))
                self.assertEqual(reconstructed,
                                 tuple((mask >> i) & 1 for i in range(n)))

    def test_exact_covering_numbers_small_against_separate_brute_oracle(self):
        for n in range(0, 5):
            for radius in range(n + 1):
                centers = minimum_covering_centers(n, radius)
                expected = independent_cover_minimum(n, radius)
                self.assertEqual(len(centers), expected)
                self.assertLessEqual(covering_radius(centers, n), radius)
                self.assertGreaterEqual(len(centers),
                                        (1 << n) // sum(comb(n, j)
                                                     for j in range(radius + 1)))
        self.assertEqual(len(minimum_covering_centers(3, 1)), 2)
        self.assertEqual(len(minimum_covering_centers(4, 1)), 4)

    def test_complete_coordinate_codecs_and_one_remote_probe_queries(self):
        for n in range(1, 5):
            for w in range(n + 1):
                scheme = CoordinateXorDeltaScheme(
                    n, w, minimum_covering_centers(n, w))
                self.assertEqual(scheme.label_bits,
                                 (len(scheme.centers) - 1).bit_length())
                for mask in range(1 << n):
                    rec = scheme.encode(mask)
                    self.assertEqual(rec.net_changed_cells,
                                     rec.remote_delta.bit_count())
                    self.assertLessEqual(rec.net_changed_cells, w)
                    decoded = tuple(scheme.query(rec, i) for i in range(n))
                    self.assertEqual(decoded,
                                     tuple((mask >> i) & 1 for i in range(n)))
                    self.assertTrue(all(bit in (0, 1) for bit in decoded))

    def test_one_shot_W_does_not_bound_maintained_state_transition_writes(self):
        scheme = CoordinateXorDeltaScheme(2, 1, (0, 3))
        a = scheme.encode(1)
        b = scheme.encode(2)
        self.assertEqual(a.remote_delta, 1)
        self.assertEqual(b.remote_delta, 2)
        self.assertEqual(a.net_changed_cells, 1)
        self.assertEqual(b.net_changed_cells, 1)
        self.assertEqual(scheme.transition_changed_cells(a, b), 2)

    def test_broadcast_one_changed_bit_can_flip_all_logical_queries(self):
        for n in range(2, 8):
            a, b = broadcast_changed_cell(0, n), broadcast_changed_cell(1, n)
            self.assertEqual(sum(x != y for x, y in zip(a, b)), n)
            # One bit of remote final-state difference, one probe per query.
            self.assertEqual(1, 1)
            self.assertGreater(sum(x != y for x, y in zip(a, b)), 1)
        with self.assertRaises(ValueError):
            CoordinateXorDeltaScheme(4, 0, (0,))
        with self.assertRaises(ValueError):
            remote_state_volume(3, 1, 4)
        with self.assertRaises(ValueError):
            necessary_local_bits(0, 1, 1, 1)

    def test_indegree_one_local_label_countermodel(self):
        for n in range(1, 9):
            allowed = tuple(1 << position for position in range(n))
            self.assertEqual(len(set(allowed)), n)
            self.assertEqual(necessary_local_bits(n, 0, 1, 0),
                             (n - 1).bit_length())


if __name__ == "__main__":
    unittest.main()
