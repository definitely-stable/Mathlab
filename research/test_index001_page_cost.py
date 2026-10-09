"""Independent dense-oracle verification of G2-A synthetic page models."""
import itertools
import unittest

from index001_page_cost import DirectArrayComparator, OverlayPageComparator, pages_for_records


def dense_runs(vals, lo, hi):
    if lo == hi:
        return ()
    out = []
    left = lo
    for i in range(lo + 1, hi + 1):
        if i == hi or vals[i] != vals[left]:
            out.append((left, i, vals[left]))
            left = i
    return tuple(out)


class Index001PageCostTests(unittest.TestCase):
    def test_exhaustive_two_overwrites_vs_independent_dense_array(self):
        for n in (1, 2, 3, 4, 5):
            operations = [(l, h, v) for l in range(n + 1)
                          for h in range(l, n + 1) for v in (0, 1)]
            for op1, op2 in itertools.product(operations, repeat=2):
                expected = [0] * n
                a = DirectArrayComparator(n, blocks_per_page=2)
                o = OverlayPageComparator(n, page_bytes=32, record_bytes=16,
                                          max_pending=3)
                for lo, hi, val in (op1, op2):
                    expected[lo:hi] = [val] * (hi - lo)
                    a.assign(lo, hi, val)
                    o.assign(lo, hi, val)
                for p in range(n):
                    self.assertEqual(a.lookup(p), expected[p])
                    self.assertEqual(o.lookup(p), expected[p], (n, op1, op2, p))
                for lo in range(n + 1):
                    for hi in range(lo, n + 1):
                        self.assertEqual(a.scan(lo, hi), dense_runs(expected, lo, hi))
                        self.assertEqual(o.scan(lo, hi), dense_runs(expected, lo, hi))
                self.assertGreaterEqual(o.writes.wal_bytes, 0)
                self.assertGreaterEqual(o.metadata_cold_read_bytes, 0)

    def test_page_cost_numeric_accounting_and_no_double_count(self):
        d = DirectArrayComparator(size=9, blocks_per_page=4)
        d.assign(3, 8, 1)
        self.assertEqual(d.page_writes, 2)
        d.assign(0, 9, 0)
        self.assertEqual(d.page_writes, 5)
        self.assertEqual(d.scan(2, 8), ((2, 8, 0),))
        self.assertEqual(d.page_reads, 2)
        o = OverlayPageComparator(size=9, page_bytes=64, record_bytes=16,
                                  max_pending=2)
        self.assertEqual(o.metadata_page_footprint, 1)
        o.assign(1, 8, 1)
        self.assertEqual(o.writes.wal_bytes, 64)
        self.assertEqual(o.lookup(2), 1)
        o.assign(3, 5, 2)  # reaches threshold -> compact
        self.assertEqual(o.counters.compactions, 1)
        self.assertEqual(o.base.runs,
                         ((0, 1, 0), (1, 3, 1), (3, 5, 2),
                          (5, 8, 1), (8, 9, 0)))
        self.assertEqual(o.writes.wal_bytes, 128)
        self.assertEqual(o.writes.compaction_bytes, 128)
        self.assertEqual(o.total_metadata_written_bytes, 256)
        self.assertEqual(o.counters.compact_read_pages, 2)
        self.assertEqual(o.metadata_page_footprint, 2)
        o.compact()
        self.assertEqual(o.counters.compactions, 1)
        self.assertEqual(o.total_metadata_written_bytes, 256)

    def test_workload_changes_read_and_compaction_costs(self):
        # An older overlay read can inspect more metadata than a fresh hit.
        a = OverlayPageComparator(8, page_bytes=64, record_bytes=16,
                                  max_pending=10)
        for lo, hi, v in ((0, 2, 1), (4, 6, 2), (7, 8, 3)):
            a.assign(lo, hi, v)
        before = a.counters.metadata_probes
        self.assertEqual(a.lookup(7), 3)
        fresh = a.counters.metadata_probes - before
        before = a.counters.metadata_probes
        self.assertEqual(a.lookup(0), 1)
        old = a.counters.metadata_probes - before
        self.assertLess(fresh, old)
        self.assertEqual(a.writes.wal_bytes, 3 * 64)
        a.compact()
        self.assertEqual(a.lookup(0), 1)
        self.assertEqual(len(a.pending), 0)

    def test_invalid_parameters_empty_updates_and_ceiling(self):
        self.assertEqual(pages_for_records(0, 4), 0)
        self.assertEqual(pages_for_records(5, 4), 2)
        with self.assertRaises(ValueError):
            pages_for_records(-1, 4)
        with self.assertRaises(ValueError):
            OverlayPageComparator(2, page_bytes=31, record_bytes=16)
        with self.assertRaises(ValueError):
            OverlayPageComparator(2, max_pending=0)
        d = DirectArrayComparator(3, 2)
        o = OverlayPageComparator(3, 64, 16)
        d.assign(1, 1, 1)
        o.assign(1, 1, 1)
        self.assertEqual(d.page_writes, 0)
        self.assertEqual(o.total_metadata_written_bytes, 0)
        self.assertEqual(o.scan(2, 2), ())
        with self.assertRaises(ValueError):
            o.lookup(3)


if __name__ == "__main__":
    unittest.main()
