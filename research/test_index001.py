"""INDEX-001 independently enumerated dense oracle and logical-cost regressions."""
import itertools
import unittest

from index001_oracle import (
    ExactRangeMap, PhysicalWriteLedger, canonicalize,
    complete_encoding_lower_bits, count_maps_with_k_runs,
)


def dense_runs(values, offset=0):
    if not values:
        return ()
    lo = 0
    out = []
    for i in range(1, len(values) + 1):
        if i == len(values) or values[i] != values[lo]:
            out.append((offset + lo, offset + i, values[lo]))
            lo = i
    return tuple(out)


def load_independent_snapshot(bits):
    actual = ExactRangeMap(len(bits), bits[0])
    for j, x in enumerate(bits[1:], 1):
        if x != bits[j - 1]:
            actual.assign(j, j + 1, x)
    return actual


class Index001Tests(unittest.TestCase):
    def test_complete_enumeration_all_symbols_and_run_counts(self):
        for a in (2, 3):
            for n in range(1, 7 if a == 2 else 6):
                observed = [0] * (n + 1)
                for values in itertools.product(range(a), repeat=n):
                    observed[len(dense_runs(values))] += 1
                for k in range(1, n + 1):
                    count = count_maps_with_k_runs(n, a, k)
                    self.assertEqual(observed[k], count, (n, a, k))
                    lower = complete_encoding_lower_bits(n, a, k)
                    self.assertLess(2 ** (lower - 1), count)
                    self.assertGreaterEqual(2 ** lower, count)

    def test_assign_exact_all_small_binary_states(self):
        for n in range(1, 7):
            for bits in itertools.product((0, 1), repeat=n):
                for lo in range(n + 1):
                    for hi in range(lo, n + 1):
                        for value in (0, 1):
                            run_map = load_independent_snapshot(bits)
                            old = run_map.boundaries
                            delta = run_map.assign(lo, hi, value)
                            expected = list(bits)
                            expected[lo:hi] = [value] * (hi - lo)
                            self.assertEqual(run_map.runs, dense_runs(expected))
                            self.assertEqual(tuple(run_map.lookup(i) for i in range(n)),
                                             tuple(expected))
                            self.assertEqual(delta.boundaries_removed, old - run_map.boundaries)
                            self.assertEqual(delta.boundaries_added, run_map.boundaries - old)
                            self.assertLessEqual(len(run_map.runs) - len(dense_runs(bits)), 2)
                            interior = set(range(lo + 1, hi))
                            self.assertTrue(not (run_map.boundaries & interior - old))
                            if lo != hi:
                                self.assertFalse(any(b in run_map.boundaries
                                                     for b in old if lo < b < hi))
                            for q_lo in range(n + 1):
                                for q_hi in range(q_lo, n + 1):
                                    self.assertEqual(run_map.scan(q_lo, q_hi),
                                                     dense_runs(expected[q_lo:q_hi], q_lo))

    def test_adversarial_sequences_and_idempotence(self):
        for n in (3, 5, 9):
            v = [0] * n
            actual = ExactRangeMap(n)
            for pos in range(1, n, 2):
                d = actual.assign(pos, pos + 1, 1)
                v[pos] = 1
                self.assertEqual(actual.runs, dense_runs(v))
                self.assertLessEqual(d.recourse, 2)
            self.assertEqual(actual.assign(0, n, 0).recourse, n - 1)
            self.assertEqual(actual.runs, ((0, n, 0),))
            self.assertEqual(actual.assign(0, n, 0).recourse, 0)
            self.assertEqual(actual.assign(2, 2, 1).recourse, 0)
        m = ExactRangeMap(8)
        for lo, hi, val in ((1, 7, 1), (3, 5, 2), (2, 6, 3),
                            (0, 8, 4), (0, 1, 5), (7, 8, 5)):
            m.assign(lo, hi, val)
        self.assertEqual(m.runs, ((0, 1, 5), (1, 7, 4), (7, 8, 5)))

    def test_disjoint_physical_write_ledger_not_double_counted(self):
        ledger = PhysicalWriteLedger()
        for category, count in (("foreground", 4096), ("wal", 1024),
                                ("compaction", 8192), ("other", 512)):
            ledger.add(category, count)
        self.assertEqual(ledger.total_physical_write_bytes, 13824)
        self.assertEqual(ledger.compaction_bytes, 8192)
        with self.assertRaises(ValueError):
            ledger.add("compaction", -1)
        with self.assertRaises(ValueError):
            ledger.add("garbage", 5)
        with self.assertRaises(ValueError):
            ledger.add("wal", 1.5)

    def test_invalid_inputs_and_gaps(self):
        for invalid in ((0, 0, 0), (-1, 1, 0)):
            with self.assertRaises(ValueError):
                canonicalize((invalid,))
        with self.assertRaises(ValueError):
            canonicalize(((0, 1, 0), (2, 3, 1)))
        with self.assertRaises(ValueError):
            count_maps_with_k_runs(3, 1, 2)
        with self.assertRaises(ValueError):
            complete_encoding_lower_bits(3, 2, 4)
        m = ExactRangeMap(4)
        for l, h in ((-1, 2), (2, 5), (3, 2)):
            with self.assertRaises(ValueError):
                m.assign(l, h, 1)
        with self.assertRaises(ValueError):
            m.lookup(4)
        with self.assertRaises(ValueError):
            ExactRangeMap(0)


if __name__ == "__main__":
    unittest.main()
