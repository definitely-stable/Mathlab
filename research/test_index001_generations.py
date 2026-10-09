"""Independent dense-array and file-state falsification of INDEX-001 G2-B3-A.

Checks process-stop boundaries on GitHub-hosted POSIX, NOT actual power loss,
multiwriter linearizability, disk-sector atomicity or physical NAND writes.
"""
import itertools
import os
from pathlib import Path
import tempfile
import unittest

from index001_durable import CorruptStore, InjectedCrash, WAL_ENTRY, encode_wal
from index001_generations import (
    MANIFEST_LENGTH, GenerationRangeStore, decode_manifest, encode_manifest,
)


def dense_runs(cells, left, right):
    if left == right:
        return ()
    out = []
    at = left
    for pos in range(left + 1, right + 1):
        if pos == right or cells[pos] != cells[at]:
            out.append((at, pos, cells[at]))
            at = pos
    return tuple(out)


def assert_exact(test, obj, cells):
    test.assertEqual(obj.size, len(cells))
    for pos in range(len(cells)):
        test.assertEqual(obj.lookup(pos), cells[pos])
    for left in range(len(cells) + 1):
        for right in range(left, len(cells) + 1):
            test.assertEqual(obj.scan(left, right),
                             dense_runs(cells, left, right))


class Index001GenerationTests(unittest.TestCase):
    def test_manifest_binary_exact_crc_and_reserved_bits(self):
        for slot in (0, 1):
            payload = encode_manifest(slot, 28)
            self.assertEqual(len(payload), MANIFEST_LENGTH)
            self.assertEqual(decode_manifest(payload), (slot, 28))
            for offset in (0, 4, 5, 10, 19):
                changed = bytearray(payload)
                changed[offset] ^= 1
                with self.assertRaises(CorruptStore):
                    decode_manifest(bytes(changed))
        with self.assertRaises(CorruptStore):
            decode_manifest(encode_manifest(0, 0)[:-1])
        with self.assertRaises(ValueError):
            encode_manifest(2, 0)
        with self.assertRaises(ValueError):
            encode_manifest(0, -1)

    def test_exhaustive_two_range_updates_across_slot_switches(self):
        for n in range(1, 4):
            ops = [(left, right, value)
                   for left in range(n)
                   for right in range(left + 1, n + 1)
                   for value in (0, 1)]
            for first, second in itertools.product(ops, repeat=2):
                with tempfile.TemporaryDirectory() as temp:
                    obj = GenerationRangeStore(temp, n)
                    oracle = [0] * n
                    for lo, hi, value in (first, second):
                        obj.assign(lo, hi, value)
                        oracle[lo:hi] = [value] * (hi - lo)
                        obj.checkpoint()
                        obj = GenerationRangeStore(temp, n)
                        assert_exact(self, obj, oracle)
                    self.assertEqual(obj.seq, 2)
                    self.assertEqual(obj.checkpoint_seq, 2)
                    self.assertEqual(obj.active_slot, 0)
                    self.assertEqual(obj.wal_path.stat().st_size, 0)
                    sizes = obj.file_lengths()
                    self.assertIsNotNone(sizes["snapshot.0.bin"])
                    self.assertIsNotNone(sizes["snapshot.1.bin"])
                    self.assertEqual(sizes["manifest.bin"], 20)

    def test_nested_trace_gc_and_checkpoint_switches(self):
        with tempfile.TemporaryDirectory() as temp:
            s = GenerationRangeStore(temp, 11)
            oracle = [0] * 11
            trace = [(0, 11, 1), (2, 9, 2), (4, 7, 3),
                     (3, 8, 4), (0, 1, 9), (10, 11, 8)]
            for i, (lo, hi, v) in enumerate(trace):
                s.assign(lo, hi, v)
                oracle[lo:hi] = [v] * (hi - lo)
                if i in (1, 3, 5):
                    prev_slot = s.active_slot
                    s.checkpoint()
                    self.assertNotEqual(s.active_slot, prev_slot)
                    assert_exact(self, GenerationRangeStore(temp, 11), oracle)
                    self.assertTrue(s.gc_inactive())
                    self.assertIsNone(s.file_lengths()[f"snapshot.{prev_slot}.bin"])
                    self.assertFalse(s.gc_inactive())
            self.assertEqual(s.seq, len(trace))
            assert_exact(self, GenerationRangeStore(temp, 11), oracle)

    def test_full_checkpoint_fault_matrix_preserves_acknowledged_state(self):
        stages = (
            "after_snapshot_partial", "after_snapshot_sync",
            "after_snapshot_replace", "after_snapshot_dirsync",
            "after_manifest_partial", "after_manifest_sync",
            "after_manifest_replace", "after_manifest_dirsync",
            "after_wal_truncate",
        )
        for stage in stages:
            with self.subTest(stage=stage), tempfile.TemporaryDirectory() as temp:
                obj = GenerationRangeStore(temp, 6)
                obj.assign(1, 5, 4)
                oracle = [0, 4, 4, 4, 4, 0]
                with self.assertRaises(InjectedCrash):
                    obj.checkpoint(failure=stage)
                after = obj.file_lengths()
                new_manifest = stage in (
                    "after_manifest_replace", "after_manifest_dirsync",
                    "after_wal_truncate")
                recovered = GenerationRangeStore(temp, 6)
                assert_exact(self, recovered, oracle)
                self.assertEqual(recovered.seq, 1)
                self.assertEqual(recovered.active_slot, 1 if new_manifest else 0)
                self.assertEqual(after["wal.bin"],
                                 0 if stage == "after_wal_truncate" else WAL_ENTRY.size)
                self.assertEqual(after["manifest.bin"], MANIFEST_LENGTH)
                if stage.endswith("partial") and "snapshot" in stage:
                    self.assertGreater(after["snapshot.1.tmp"], 0)
                    self.assertLess(after["snapshot.1.tmp"], 48)
                recovered.assign(0, 1, 7)
                recovered.checkpoint()
                assert_exact(self, GenerationRangeStore(temp, 6),
                             [7, 4, 4, 4, 4, 0])

    def test_second_checkpoint_partial_cannot_damage_pinned_active_slot(self):
        for stage in ("after_snapshot_partial", "after_snapshot_replace",
                      "after_manifest_partial", "after_manifest_replace"):
            with self.subTest(stage=stage), tempfile.TemporaryDirectory() as temp:
                obj = GenerationRangeStore(temp, 5)
                obj.assign(0, 5, 1)
                obj.checkpoint()
                self.assertEqual(obj.active_slot, 1)
                obj.assign(2, 4, 2)
                with self.assertRaises(InjectedCrash):
                    obj.checkpoint(failure=stage)
                old_selected = stage not in ("after_manifest_replace",)
                recovered = GenerationRangeStore(temp, 5)
                self.assertEqual(recovered.active_slot, 1 if old_selected else 0)
                assert_exact(self, recovered, [1, 1, 2, 2, 1])

    def test_unacknowledged_range_is_complete_old_or_new(self):
        old = [0, 0, 4, 0, 0, 0]
        new = [0, 8, 8, 8, 0, 0]
        # First baseline update is overwritten by new only in part.
        new = [0, 8, 8, 8, 0, 0]
        for stage in ("before_wal", "after_wal_partial",
                      "after_wal_write", "after_wal_sync"):
            with self.subTest(stage=stage), tempfile.TemporaryDirectory() as temp:
                st = GenerationRangeStore(temp, 6)
                st.assign(2, 3, 4)
                with self.assertRaises(InjectedCrash):
                    st.assign(1, 4, 8, failure=stage)
                recovered = GenerationRangeStore(temp, 6)
                self.assertIn(recovered.cells, (old, new))
                if stage in ("before_wal", "after_wal_partial"):
                    self.assertEqual(recovered.cells, old)
                recovered.assign(4, 6, 9)
                assert_exact(self, GenerationRangeStore(temp, 6),
                             (new if recovered.seq == 3 else old)[:4] + [9, 9])

    def test_gc_fault_matrix_never_unlinks_active(self):
        for stage in ("before_gc", "after_gc_unlink", "after_gc_dirsync"):
            with self.subTest(stage=stage), tempfile.TemporaryDirectory() as temp:
                st = GenerationRangeStore(temp, 5)
                st.assign(1, 4, 6)
                st.checkpoint()
                self.assertEqual(st.active_slot, 1)
                with self.assertRaises(InjectedCrash):
                    st.gc_inactive(failure=stage)
                self.assertTrue((Path(temp) / "snapshot.1.bin").exists())
                self.assertEqual((Path(temp) / "snapshot.0.bin").exists(),
                                 stage == "before_gc")
                reopened = GenerationRangeStore(temp, 5)
                assert_exact(self, reopened, [0, 6, 6, 6, 0])

    def test_fail_closed_manifest_snapshot_mismatch_and_missing_files(self):
        with tempfile.TemporaryDirectory() as temp:
            st = GenerationRangeStore(temp, 4)
            st.assign(0, 4, 1)
            st.checkpoint()
            (Path(temp) / "manifest.bin").write_bytes(encode_manifest(1, 999))
            with self.assertRaisesRegex(CorruptStore, "LSN"):
                GenerationRangeStore(temp, 4)
        with tempfile.TemporaryDirectory() as temp:
            st = GenerationRangeStore(temp, 4)
            st.assign(0, 4, 1)
            st.checkpoint()
            (Path(temp) / "snapshot.1.bin").unlink()
            with self.assertRaisesRegex(CorruptStore, "missing active"):
                GenerationRangeStore(temp, 4)
        with tempfile.TemporaryDirectory() as temp:
            st = GenerationRangeStore(temp, 4)
            st.assign(0, 4, 1)
            st.checkpoint()
            path = Path(temp) / "snapshot.1.bin"
            data = bytearray(path.read_bytes())
            data[-1] ^= 1
            path.write_bytes(data)
            with self.assertRaisesRegex(CorruptStore, "CRC"):
                GenerationRangeStore(temp, 4)
        with tempfile.TemporaryDirectory() as temp:
            st = GenerationRangeStore(temp, 4)
            (Path(temp) / "wal.bin").unlink()
            with self.assertRaisesRegex(CorruptStore, "WAL missing"):
                GenerationRangeStore(temp, 4)
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp)
            (path / "snapshot.0.tmp").write_bytes(b"orphan")
            with self.assertRaisesRegex(CorruptStore, "incomplete creation"):
                GenerationRangeStore(temp, 4)

    def test_torn_and_corrupt_full_wal_with_generations(self):
        with tempfile.TemporaryDirectory() as temp:
            st = GenerationRangeStore(temp, 4)
            st.assign(0, 1, 1)
            with st.wal_path.open("ab") as f:
                f.write(encode_wal(2, 2, 4, 3)[:13])
            obj = GenerationRangeStore(temp, 4)
            self.assertEqual(obj.wal_path.stat().st_size, WAL_ENTRY.size)
            self.assertEqual(obj.seq, 1)
            obj.assign(2, 4, 3)
            assert_exact(self, GenerationRangeStore(temp, 4), [1, 0, 3, 3])
        with tempfile.TemporaryDirectory() as temp:
            st = GenerationRangeStore(temp, 4)
            st.assign(0, 1, 1)
            with st.wal_path.open("ab") as f:
                bad = bytearray(encode_wal(2, 2, 4, 3))
                bad[-1] ^= 1
                f.write(bad)
            with self.assertRaisesRegex(CorruptStore, "CRC"):
                GenerationRangeStore(temp, 4)

    def test_application_written_bytes_include_manifest_and_gc_events(self):
        for n in (2, 6):
            with tempfile.TemporaryDirectory() as temp:
                st = GenerationRangeStore(temp, n)
                frame = 24 + 4 * n
                self.assertEqual(st.ledger.snapshot_written, frame)
                self.assertEqual(st.ledger.manifest_written, 20)
                self.assertEqual(st.ledger.total_application_written, frame + 20)
                self.assertEqual(st.ledger.snapshot_replaces, 1)
                self.assertEqual(st.ledger.manifest_replaces, 1)
                st.assign(0, n, 2)
                st.checkpoint()
                self.assertEqual(st.ledger.wal_written, WAL_ENTRY.size)
                self.assertEqual(st.ledger.snapshot_written, 2 * frame)
                self.assertEqual(st.ledger.manifest_written, 40)
                self.assertEqual(st.ledger.total_application_written,
                                 2 * (frame + 20) + WAL_ENTRY.size)
                self.assertEqual(st.ledger.wal_truncates, 1)
                sizes = st.file_lengths()
                self.assertEqual(sizes["snapshot.0.bin"], frame)
                self.assertEqual(sizes["snapshot.1.bin"], frame)
                self.assertEqual(sizes["manifest.bin"], 20)
                self.assertEqual(sizes["wal.bin"], 0)
                new = GenerationRangeStore(temp, n)
                self.assertEqual(new.ledger.snapshot_read, frame)
                self.assertEqual(new.ledger.manifest_read, 20)
                self.assertEqual(new.ledger.wal_read, 0)
                self.assertEqual(new.ledger.total_application_read, frame + 20)
                assert_exact(self, new, [2] * n)
                self.assertTrue(st.gc_inactive())
                self.assertEqual(st.ledger.inactive_gc_unlinks, 1)
                self.assertIsNone(st.file_lengths()["snapshot.0.bin"])

    def test_noop_validation_and_manifest_reopen(self):
        with tempfile.TemporaryDirectory() as temp:
            st = GenerationRangeStore(temp, 4)
            st.assign(2, 2, 3)
            st.checkpoint()
            self.assertEqual(st.seq, 0)
            self.assertEqual(st.wal_path.stat().st_size, 0)
            self.assertFalse(st.gc_inactive())
            for lo, hi in ((-1, 1), (1, 5), (4, 3)):
                with self.assertRaises(ValueError):
                    st.assign(lo, hi, 1)
            with self.assertRaises(ValueError):
                st.assign(0, 1, -1)
            with self.assertRaises(ValueError):
                st.lookup(4)
            with self.assertRaises(ValueError):
                GenerationRangeStore(temp, 5)


if __name__ == "__main__":
    unittest.main()
