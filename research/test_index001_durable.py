"""INDEX-001 G2-B1: dense-array and independent restart/fault oracles.

Validates an explicitly limited POSIX reference protocol; does not claim
power-loss hardware proof, physical NAND byte counts, or concurrent safety.
"""
import itertools
import os
from pathlib import Path
import tempfile
import unittest

from index001_durable import (
    CorruptStore, DurableRangeStore, InjectedCrash, SnapshotReference,
    WAL_ENTRY, SNAP_HEAD, decode_snapshot, decode_wal, encode_snapshot,
    encode_wal,
)


def exact_scan(values, lo, hi):
    if lo == hi:
        return ()
    out, start = [], lo
    for i in range(lo + 1, hi + 1):
        if i == hi or values[i] != values[start]:
            out.append((start, i, values[start]))
            start = i
    return tuple(out)


def assert_full_map(test, store, values):
    test.assertEqual(store.size, len(values))
    for i in range(len(values)):
        test.assertEqual(store.lookup(i), values[i])
    for lo in range(len(values) + 1):
        for hi in range(lo, len(values) + 1):
            test.assertEqual(store.scan(lo, hi), exact_scan(values, lo, hi))


class Index001DurableTests(unittest.TestCase):
    def test_wire_grammar_checksums_exact_lengths(self):
        cells = (0, 4, 0, 2)
        snap = encode_snapshot(2, cells)
        self.assertEqual(len(snap), SNAP_HEAD.size + 4 * len(cells) + 4)
        self.assertEqual(decode_snapshot(snap, len(cells)), (2, list(cells)))
        with self.assertRaisesRegex(CorruptStore, "CRC"):
            x = bytearray(snap)
            x[-1] ^= 1
            decode_snapshot(bytes(x), len(cells))
        with self.assertRaises(CorruptStore):
            decode_snapshot(snap[:-1], len(cells))
        with self.assertRaises(CorruptStore):
            decode_snapshot(snap, len(cells) + 1)
        entry = encode_wal(3, 0, 4, 9)
        self.assertEqual(len(entry), WAL_ENTRY.size)
        self.assertEqual(decode_wal(entry, 4), (3, 0, 4, 9))
        with self.assertRaises(CorruptStore):
            t = bytearray(entry)
            t[7] ^= 1
            decode_wal(bytes(t), 4)

    def test_exhaustive_small_two_updates_and_reopen(self):
        for n in range(1, 4):
            # Exhaustive 1- and 2-operation binary histories, including overlaps.
            ops = [(l, h, v) for l in range(n + 1)
                   for h in range(l + 1, n + 1) for v in (0, 1)]
            for first, second in itertools.product(ops, repeat=2):
                with tempfile.TemporaryDirectory() as tmp:
                    d = DurableRangeStore(Path(tmp) / "wal", n)
                    s = SnapshotReference(Path(tmp) / "snapshot", n)
                    expected = [0] * n
                    for lo, hi, value in (first, second):
                        expected[lo:hi] = [value] * (hi - lo)
                        d.assign(lo, hi, value)
                        s.assign(lo, hi, value)
                    # Reopening must not rely on the old instance's memory.
                    d = DurableRangeStore(Path(tmp) / "wal", n)
                    s = SnapshotReference(Path(tmp) / "snapshot", n)
                    assert_full_map(self, d, expected)
                    assert_full_map(self, s, expected)
                    self.assertEqual(d.seq, 2)
                    self.assertEqual(s.seq, 2)

    def test_nested_alternating_and_checkpoint_replay(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "map"
            store = DurableRangeStore(path, 9)
            expected = [0] * 9
            steps = [(1, 8, 1), (3, 6, 2), (0, 9, 3),
                     (0, 1, 4), (8, 9, 4)]
            steps += [(i, i + 1, i % 2) for i in range(9)]
            for i, (lo, hi, v) in enumerate(steps):
                store.assign(lo, hi, v)
                expected[lo:hi] = [v] * (hi - lo)
                if i in (2, 5, 9):
                    store.checkpoint()
                    store = DurableRangeStore(path, 9)
                    assert_full_map(self, store, expected)
            self.assertEqual(store.seq, len(steps))
            store.checkpoint()
            store = DurableRangeStore(path, 9)
            self.assertEqual(store.checkpoint_seq, len(steps))
            self.assertEqual(store.wal_path.stat().st_size, 0)
            assert_full_map(self, store, expected)

    def test_fatal_corrupt_complete_wal_and_snapshot(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp)
            store = DurableRangeStore(path, 4)
            store.assign(1, 3, 7)
            with store.wal_path.open("r+b") as f:
                f.seek(5)
                value = f.read(1)
                f.seek(5)
                f.write(bytes([value[0] ^ 0x20]))
                f.flush()
                os.fsync(f.fileno())
            with self.assertRaises(CorruptStore):
                DurableRangeStore(path, 4)
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp)
            store = DurableRangeStore(path, 4)
            with store.snapshot_path.open("r+b") as f:
                f.seek(13)
                value = f.read(1)
                f.seek(13)
                f.write(bytes([value[0] ^ 1]))
                f.flush()
                os.fsync(f.fileno())
            with self.assertRaises(CorruptStore):
                DurableRangeStore(path, 4)

    def test_gap_duplicate_and_invalid_complete_record_are_fatal(self):
        for extra in (encode_wal(3, 1, 2, 1),
                      encode_wal(1, 2, 3, 1),
                      encode_wal(2, 1, 5, 1)):
            with tempfile.TemporaryDirectory() as temp:
                path = Path(temp)
                st = DurableRangeStore(path, 4)
                st.assign(0, 1, 1)
                with st.wal_path.open("ab") as f:
                    f.write(extra)
                    f.flush()
                    os.fsync(f.fileno())
                with self.assertRaises(CorruptStore):
                    DurableRangeStore(path, 4)

    def test_torn_wal_tail_is_truncated_only_on_restart(self):
        for count in (1, 13, WAL_ENTRY.size - 1):
            with tempfile.TemporaryDirectory() as tmp:
                path = Path(tmp)
                st = DurableRangeStore(path, 5)
                st.assign(0, 2, 1)
                oldsize = st.wal_path.stat().st_size
                with st.wal_path.open("ab") as f:
                    f.write(encode_wal(2, 3, 4, 2)[:count])
                    f.flush()
                    os.fsync(f.fileno())
                reopened = DurableRangeStore(path, 5)
                self.assertEqual(reopened.seq, 1)
                self.assertEqual(reopened.wal_path.stat().st_size, oldsize)
                self.assertGreaterEqual(reopened.ledger.wal_truncates, 1)
                reopened.assign(3, 4, 2)
                assert_full_map(self, DurableRangeStore(path, 5),
                                [1, 1, 0, 2, 0])

    def test_update_failpoints_do_not_produce_mixed_states(self):
        before = (0, 4, 0, 0, 0, 0)
        after = (0, 4, 7, 7, 7, 0)
        for failure in ("before_wal", "after_wal_partial",
                        "after_wal_write", "after_wal_sync"):
            with self.subTest(failure=failure), tempfile.TemporaryDirectory() as temp:
                st = DurableRangeStore(temp, len(before))
                st.assign(1, 2, 4)
                self.assertEqual(tuple(st.cells), before)
                with self.assertRaises(InjectedCrash):
                    st.assign(2, 5, 7, failure=failure)
                recovered = DurableRangeStore(temp, len(before))
                self.assertIn(tuple(recovered.cells), (before, after))
                # Torn prefix must be absent; a complete unacked record may survive.
                if failure in ("before_wal", "after_wal_partial"):
                    self.assertEqual(tuple(recovered.cells), before)
                recovered.assign(0, 1, 9)
                self.assertEqual(DurableRangeStore(temp, len(before)).lookup(0), 9)

    def test_checkpoint_failpoints_preserve_all_acknowledged_data(self):
        stages = ("after_checkpoint_partial", "after_checkpoint_sync",
                  "after_checkpoint_replace", "after_checkpoint_dirsync",
                  "after_wal_truncate")
        for failure in stages:
            with self.subTest(failure=failure), tempfile.TemporaryDirectory() as temp:
                st = DurableRangeStore(temp, 5)
                st.assign(1, 4, 3)
                st.assign(2, 3, 5)
                expected = [0, 3, 5, 3, 0]
                with self.assertRaises(InjectedCrash):
                    st.checkpoint(failure=failure)
                restarted = DurableRangeStore(temp, 5)
                assert_full_map(self, restarted, expected)
                self.assertEqual(restarted.seq, 2)
                restarted.assign(4, 5, 8)
                restarted.checkpoint()
                assert_full_map(self, DurableRangeStore(temp, 5),
                                [0, 3, 5, 3, 8])

    def test_snapshot_baseline_failpoints_whole_old_or_new(self):
        old = [0, 2, 0, 0]
        new = [0, 2, 9, 9]
        for failure in ("after_checkpoint_partial", "after_checkpoint_sync",
                        "after_checkpoint_replace", "after_checkpoint_dirsync"):
            with self.subTest(failure=failure), tempfile.TemporaryDirectory() as temp:
                st = SnapshotReference(temp, 4)
                st.assign(1, 2, 2)
                with self.assertRaises(InjectedCrash):
                    st.assign(2, 4, 9, failure=failure)
                reopened = SnapshotReference(temp, 4)
                self.assertIn(reopened.cells, (old, new))
                if failure in ("after_checkpoint_partial", "after_checkpoint_sync"):
                    self.assertEqual(reopened.cells, old)

    def test_application_byte_counters_and_no_double_count(self):
        with tempfile.TemporaryDirectory() as temp:
            st = DurableRangeStore(Path(temp) / "wal", 4)
            snap_bytes = SNAP_HEAD.size + 4 * 4 + 4
            self.assertEqual(st.ledger.snapshot_written, snap_bytes)
            st.assign(0, 3, 7)
            st.assign(2, 4, 8)
            self.assertEqual(st.ledger.wal_written, 2 * WAL_ENTRY.size)
            self.assertEqual(st.ledger.acknowledged_blocks, 5)
            self.assertEqual(st.application_written_bytes,
                             snap_bytes + 2 * WAL_ENTRY.size)
            st.checkpoint()
            self.assertEqual(st.ledger.snapshot_written, snap_bytes * 2)
            self.assertEqual(st.application_written_bytes,
                             snap_bytes * 2 + 2 * WAL_ENTRY.size)
            self.assertEqual(st.ledger.wal_truncates, 1)
            self.assertGreater(st.ledger.fsync_files, 0)
            self.assertGreater(st.ledger.fsync_dirs, 0)
            st = DurableRangeStore(Path(temp) / "wal", 4)
            self.assertEqual(st.ledger.snapshot_read, snap_bytes)
            self.assertEqual(st.ledger.wal_read, 0)
            self.assertEqual(st.ledger.total_application_read, snap_bytes)
            assert_full_map(self, st, [7, 7, 8, 8])
            s = SnapshotReference(Path(temp) / "only", 4)
            s.assign(0, 3, 7)
            s.assign(2, 4, 8)
            self.assertEqual(s.ledger.snapshot_written, snap_bytes * 3)
            self.assertEqual(s.ledger.wal_written, 0)

    def test_invalid_and_empty_updates(self):
        with tempfile.TemporaryDirectory() as temp:
            st = DurableRangeStore(temp, 3)
            st.assign(1, 1, 3)
            self.assertEqual(st.seq, 0)
            self.assertEqual(st.wal_path.stat().st_size, 0)
            for lo, hi in ((-1, 1), (1, 4), (2, 1)):
                with self.assertRaises(ValueError):
                    st.assign(lo, hi, 2)
            with self.assertRaises(ValueError):
                st.assign(0, 1, -1)
            with self.assertRaises(ValueError):
                st.lookup(3)
            with self.assertRaises(ValueError):
                DurableRangeStore(temp, 4)
        with self.assertRaises(ValueError):
            encode_wal(0, 0, 1, 1)


if __name__ == "__main__":
    unittest.main()
