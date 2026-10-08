"""G2B-B independent weak Sidon bounds, correspondence and witness."""
from itertools import combinations
import unittest

from lent_exhaustive import is_exact_family, sparse_nonzero_vectors
from lent_hypergraph import build_forbidden_hypergraph, solve_exact_or_certified_interval
from lent_weak_sidon import (
    difference_multiplicities,
    is_weak_sidon_with_zero,
    weak_sidon_difference_certificate,
    weak_sidon_max_size,
    weak_sidon_upper_v,
)


class WeakSidonTests(unittest.TestCase):
    def test_integer_bound_and_near_threshold(self):
        for n in (3, 5, 7, 11, 19, 25, 27, 49, 81, 125, 343, 625):
            s = weak_sidon_max_size(n)
            self.assertLessEqual(s * (s - 3) + 1, n)
            self.assertGreater((s + 1) * (s - 2) + 1, n)
        self.assertEqual(weak_sidon_max_size(125), 12)
        self.assertEqual(weak_sidon_upper_v(5, 3), 11)
        self.assertEqual(weak_sidon_upper_v(3, 3), 5)
        self.assertEqual(weak_sidon_upper_v(7, 1), 3)

    def test_correspondence_on_every_small_candidate_subset(self):
        # ASET -> weak Sidon, but weak Sidon -> ASET requires additionally
        # that the empty sum 0 is not a sum of two DISTINCT S-elements.
        for q, m, w in ((3, 2, 2), (3, 3, 1), (5, 1, 1), (7, 1, 1)):
            candidates = tuple(sparse_nonzero_vectors(q, m, w))
            for mask in range(1 << len(candidates)):
                columns = [
                    x for i, x in enumerate(candidates) if mask & (1 << i)
                ]
                exact = is_exact_family(columns, q, 2)
                weak = is_weak_sidon_with_zero(columns, q)
                if exact:
                    self.assertTrue(weak)
                    self.assertLessEqual(len(columns), weak_sidon_upper_v(q, m))
                if weak:
                    self.assertLessEqual(
                        len(columns), weak_sidon_upper_v(q, m)
                    )
                    cert = weak_sidon_difference_certificate(columns, q)
                    self.assertLessEqual(
                        cert["duplicate_excess"], 2 * (len(columns) + 1)
                    )

    def test_weak_sidon_is_not_equivalent_to_full_aset(self):
        # Known extremal weak Sidon set in Z_11; 4+7=0 creates an
        # empty-vs-two collision, so the reverse reduction is invalid.
        columns = [(1,), (2,), (4,), (7,)]
        self.assertTrue(is_weak_sidon_with_zero(columns, 11))
        self.assertFalse(is_exact_family(columns, 11, 2))
        cert = weak_sidon_difference_certificate(columns, 11)
        self.assertEqual(cert["weak_sidon_points"], 5)
        self.assertEqual(cert["ordered_differences"], 20)
        self.assertEqual(cert["group_size"], 11)
        self.assertEqual(5 * (5 - 3) + 1, 11)

    def test_original_q5_witness_still_independently_exact(self):
        columns = [
            (0, 1, 1), (0, 1, 2), (0, 1, 3), (0, 3, 1),
            (1, 0, 2), (1, 3, 0), (2, 0, 4), (2, 4, 0),
            (3, 0, 0), (4, 0, 0),
        ]
        self.assertTrue(is_exact_family(columns, 5, 2))
        certificate = weak_sidon_difference_certificate(columns, 5)
        self.assertTrue(certificate["is_exact_aset"])
        self.assertEqual(certificate["aset_columns"], 10)
        self.assertEqual(certificate["weak_sidon_bound_v"], 11)
        self.assertEqual(certificate["ordered_differences"], 110)
        self.assertLessEqual(certificate["duplicate_excess"], 22)

    def test_q5_search_uses_sharper_global_bound_not_heuristics(self):
        graph = build_forbidden_hypergraph(5, 3, 2)
        result = solve_exact_or_certified_interval(graph, max_nodes=25_000)
        self.assertEqual(result["weak_sidon_upper"], 11)
        self.assertEqual(result["hamming_upper"], 15)
        self.assertEqual(result["global_upper"], 11)
        self.assertLessEqual(10, result["lower"])
        self.assertLessEqual(result["lower"], result["upper"])
        self.assertLessEqual(result["upper"], 11)
        self.assertTrue(is_exact_family(
            [tuple(x) for x in result["witness"]], 5, 2
        ))
        if result["exact"]:
            self.assertEqual(result["lower"], result["upper"])
        else:
            self.assertFalse(result["search_exhausted"])

    def test_fail_closed_and_malformed_groups(self):
        for n in (-1, 0, 2, 10, 12, True, 3.0):
            with self.assertRaises(ValueError):
                weak_sidon_max_size(n)
        for q, m in ((2, 3), (4, 3), (5, 0), (5, -1), (5, True)):
            with self.assertRaises(ValueError):
                weak_sidon_upper_v(q, m)
        with self.assertRaises(ValueError):
            is_weak_sidon_with_zero([(1, 2), (0,)], 5)
        with self.assertRaises(ValueError):
            is_weak_sidon_with_zero([(5,)], 5)
        with self.assertRaises(ValueError):
            weak_sidon_difference_certificate([(1,), (1,)], 5)

    def test_characteristic_three_3cycle(self):
        # In Z3 all three points are weak Sidon and both nonzero
        # differences have multiplicity THREE, not two. The proof
        # correctly counts collision pairs rather than assuming
        # multiplicity<=2.
        frequencies = difference_multiplicities([(0,), (1,), (2,)], 3)
        self.assertEqual(frequencies[(1,)], 3)
        self.assertEqual(frequencies[(2,)], 3)
        cert = weak_sidon_difference_certificate([(1,), (2,)], 3)
        self.assertEqual(cert["colliding_difference_pairs"], 6)
        self.assertEqual(cert["centered_progressions"], 3)
        self.assertEqual(cert["duplicate_excess"], 4)


if __name__ == "__main__":
    unittest.main()
