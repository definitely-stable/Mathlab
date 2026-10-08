"""HYP-002-C: exhaustive independent affine decoding and product-gate tests."""
import unittest
from itertools import combinations, product

from affine_two_id import (
    canonical_line, checked_transition, decode, encode, line_points,
    size, storage_report, third, trusted_raw_update,
)
from lent_exhaustive import is_exact_family
from locality_transition import affine_sts_blocks


class AffineTwoIDTests(unittest.TestCase):
    def test_affine_third_unique_canonical_no_index_table(self):
        for rank in (1, 2, 3):
            m = size(rank)
            labels = tuple(product(range(3), repeat=rank))
            for a in range(m):
                for b in range(a+1, m):
                    z = third(a, b, rank)
                    self.assertNotIn(z, (a, b))
                    self.assertTrue(all(
                        (labels[a][j] + labels[b][j] + labels[z][j]) % 3 == 0
                        for j in range(rank)
                    ))
                    trip = tuple(sorted((a, b, z)))
                    ident = canonical_line(a, b, rank)
                    self.assertEqual(ident, (trip[0], trip[1]))
                    self.assertEqual(line_points(ident, rank), trip)

    def test_full_r2_independent_sum_oracle(self):
        rank = 2
        m, blocks = affine_sts_blocks(rank)
        ids = tuple((x, y) for x, y, _ in blocks)
        signatures = set()
        for family in [()] + [(x,) for x in ids] + list(combinations(ids, 2)):
            expected = [0] * m
            for ident in family:
                block = line_points(ident, rank)
                for p in block:
                    expected[p] = (expected[p] + 1) % 3
            sig = tuple(expected)
            self.assertNotIn(sig, signatures)
            signatures.add(sig)
            self.assertEqual(encode(family, rank), sig)
            self.assertEqual(decode(sig, rank), tuple(sorted(family)))
        self.assertEqual(len(signatures), 1 + len(ids) + len(ids)*(len(ids)-1)//2)
        columns = [
            tuple(int(j in block) for j in range(m)) for block in blocks
        ]
        self.assertTrue(is_exact_family(columns, 3, 2))

    def test_rank3_complete_decode_cases(self):
        m, blocks = affine_sts_blocks(3)
        ids = tuple((x, y) for x, y, _ in blocks)
        checked = 0
        for family in [()] + [(x,) for x in ids] + list(combinations(ids, 2)):
            self.assertEqual(decode(encode(family, 3), 3), tuple(sorted(family)))
            checked += 1
        self.assertEqual(checked, 1 + 117 + 117*116//2)

    def test_structurally_invalid_trits_and_shapes_rejected(self):
        rank = 2
        invalid_states = [
            (1,) + (0,) * 8,
            (2,) + (0,) * 8,
            (1, 1) + (0,) * 7,
            (1,) * 9,
            (1, 1, 1, 1) + (0,) * 5,
            (2, 2, 1, 1, 1) + (0,) * 4,
        ]
        for state in invalid_states:
            self.assertIsNone(decode(state, rank), state)
        for bad in [(0,) * 8, (3,) + (0,)*8, (1.0,) + (0,)*8]:
            with self.assertRaises(ValueError):
                decode(bad, rank)

    def test_over_capacity_alias_is_undetectable_from_state(self):
        # Three DISTINCT affine lines alias exactly two other lines.
        # No decoder can distinguish those histories from the snapshot.
        three = ((0, 1), (0, 3), (0, 4))
        two = ((1, 3), (2, 4))
        r = 2
        snapshot = encode((), r)
        for ident in three:
            snapshot = trusted_raw_update(snapshot, r, ident, +1)
        self.assertEqual(snapshot, encode(two, r))
        self.assertEqual(decode(snapshot, r), two)
        with self.assertRaises(ValueError):
            encode(three, r)

    def test_duplicate_raw_insertion_and_missing_delete_unsafe(self):
        ident = canonical_line(0, 1, 2)
        state = encode((), 2)
        for _ in range(3):
            state = trusted_raw_update(state, 2, ident, +1)
        self.assertEqual(state, encode((), 2))
        self.assertEqual(decode(state, 2), ())
        # The checked API rejects bad histories as long as the snapshot
        # remains within the promise; the trusted raw API cannot.
        with self.assertRaisesRegex(ValueError, "missing deletion"):
            checked_transition(encode((), 2), 2, ident, add=False)

    def test_checked_insert_delete_limits(self):
        ids = tuple((x, y) for x, y, _ in affine_sts_blocks(2)[1])
        zero = encode((), 2)
        first = checked_transition(zero, 2, ids[0], add=True)
        self.assertEqual(decode(first, 2), (ids[0],))
        with self.assertRaisesRegex(ValueError, "duplicate insertion"):
            checked_transition(first, 2, ids[0], add=True)
        second = checked_transition(first, 2, ids[1], add=True)
        self.assertEqual(decode(second, 2), tuple(sorted(ids[:2])))
        with self.assertRaisesRegex(ValueError, "capacity exceeded"):
            checked_transition(second, 2, ids[2], add=True)
        back = checked_transition(second, 2, ids[0], add=False)
        self.assertEqual(decode(back, 2), (ids[1],))
        self.assertEqual(checked_transition(back, 2, ids[1], add=False), zero)

    def test_noncanonical_and_invalid_ids(self):
        with self.assertRaises(ValueError):
            line_points((0, 2), 2)  # same line as canonical (0,1)
        with self.assertRaises(ValueError):
            canonical_line(0, 0, 2)
        with self.assertRaises(ValueError):
            line_points((0, 9), 2)
        with self.assertRaises(ValueError):
            encode(((0, 1), (0, 1)), 2)
        with self.assertRaises(ValueError):
            trusted_raw_update(encode((), 2), 2, (0, 1), 2)
        with self.assertRaises(ValueError):
            size(True)
        with self.assertRaises(ValueError):
            canonical_line(True, 1, 2)
        with self.assertRaises(ValueError):
            decode((True,) + (0,)*8, 2)
        with self.assertRaises(ValueError):
            trusted_raw_update(encode((), 2), 2, (0, 1), True)
        with self.assertRaises(ValueError):
            checked_transition(encode((), 2), 2, (0, 1), 1)

    def test_dense_memory_vs_canonical_pair(self):
        for rank in (1, 2, 3, 4, 5):
            report = storage_report(rank)
            self.assertEqual(report["V"], report["m"] * (report["m"]-1)//6)
            self.assertLessEqual(
                report["info_lower_bits"],
                report["dense_trit_information_bits"]
            )
        for rank in (3, 4, 5):
            report = storage_report(rank)
            self.assertGreater(
                report["dense_trit_information_bits"],
                report["direct_two_canonical_ids_bits"],
                report,
            )
            self.assertGreater(
                report["dense_2bit_bits"],
                report["direct_two_canonical_ids_bits"],
                report,
            )


if __name__ == "__main__":
    unittest.main()
