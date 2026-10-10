"""Independent finite oracles and negative-scope gates for UCT-005 D1-A."""
import itertools
import unittest

from uct005_d1a_causal_falsifiers import (
    HonestFenwickSet,
    encode_interval_table,
    fenwick_overstrong_candidate_falsifier,
    interval_parity,
    intervals,
    one_probe_certificate,
    table_flip,
)


class D1AExactFalsifierTests(unittest.TestCase):
    def test_exact_one_probe_witness_table_all_binary_words(self):
        for n in range(1, 7):
            expected = n * (n + 1) // 2
            certificate = one_probe_certificate(n)
            self.assertEqual(certificate["minimum_remote_bits"], expected)
            self.assertEqual(certificate["minimum_worst_changed_bits"],
                             max(certificate["per_flip_minimum_changed_bits"]))
            qs = intervals(n)
            self.assertEqual(len(qs), expected)
            # Independent truth-table oracle: each interval parity is a
            # distinct nonconstant Boolean function, even up to complement.
            signatures = set()
            for a, b in qs:
                truth = tuple(sum(bits[a:b]) & 1 for bits in
                              itertools.product((0, 1), repeat=n))
                self.assertIn(0, truth)
                self.assertIn(1, truth)
                inverse = tuple(v ^ 1 for v in truth)
                canonical = min(truth, inverse)
                self.assertNotIn(canonical, signatures)
                signatures.add(canonical)
            self.assertEqual(len(signatures), expected)
            for word in itertools.product((0, 1), repeat=n):
                encoded = encode_interval_table(word)
                self.assertEqual(encoded,
                                 tuple(sum(word[a:b]) & 1 for a, b in qs))
                for pos in range(n):
                    changed = table_flip(encoded, n, pos)
                    other = tuple(x ^ int(i == pos) for i, x in enumerate(word))
                    self.assertEqual(changed, encode_interval_table(other))
                    self.assertEqual(
                        sum(a != b for a, b in zip(changed, encoded)),
                        (pos + 1) * (n - pos),
                    )

    def test_fenwick_independent_set_range_oracle_exhaustive(self):
        for n in range(1, 9):
            for word in itertools.product((0, 1), repeat=n):
                for pos in range(n):
                    oracle = HonestFenwickSet(word)
                    same = oracle.set(pos, word[pos])
                    self.assertEqual((same.remote_reads, same.remote_writes), (1, 0))
                    flip = oracle.set(pos, word[pos] ^ 1)
                    self.assertEqual(flip.remote_reads, 1)
                    self.assertLessEqual(flip.remote_writes, n.bit_length() + 1)
                    after = list(word)
                    after[pos] ^= 1
                    for a, b in intervals(n):
                        observed, cost = oracle.query(a, b)
                        self.assertEqual(observed, sum(after[a:b]) & 1)
                        self.assertLessEqual(cost.remote_reads, 2 * n.bit_length())
                        self.assertEqual(cost.remote_writes, 0)

    def test_overstrong_candidate_is_false_in_honest_bit_cell_model(self):
        for power in (7, 8, 10, 12, 16):
            report = fenwick_overstrong_candidate_falsifier(power)
            self.assertLess(report["product_upper"], report["n"])
            self.assertIn("honest", report["semantic_scope"])
            self.assertIn("authenticated F1", report["does_not_refute"])

    def test_broad_scope_must_not_be_promoted(self):
        cert = one_probe_certificate(6)
        self.assertIn("not F1", cert["model"])
        self.assertNotIn("authenticated", cert["model"])
        self.assertGreater(cert["minimum_remote_bits"], 6)
        self.assertRaises(ValueError, one_probe_certificate, 0)
        self.assertRaises(ValueError, fenwick_overstrong_candidate_falsifier, 6)
        self.assertRaises(ValueError, HonestFenwickSet, ())
        self.assertRaises(ValueError, interval_parity, (1, 0), 0, 3)
        self.assertRaises(ValueError, table_flip, (0, 1), 2, 1)


if __name__ == "__main__":
    unittest.main()
