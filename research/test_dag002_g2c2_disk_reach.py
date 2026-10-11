"""Independent exact finite validation for actual file-backed DAG baselines."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from dag002_g2c2_file_store import FilePageStore
from dag002_g2c2_disk_reach import FileReachIndex, decode_parents


def independent_reach(parents: tuple[tuple[int, ...], ...],
                      source: int, target: int) -> bool:
    pending = [target]
    seen: set[int] = set()
    while pending:
        x = pending.pop()
        if x == source:
            return True
        if x not in seen:
            seen.add(x)
            pending.extend(parents[x])
    return False


class FileDagReferenceTests(unittest.TestCase):
    def test_all_64_four_node_dags_two_modes_two_page_sizes(self):
        pairs = [(u, v) for v in range(4) for u in range(v)]
        cases = 0
        for mask in range(1 << len(pairs)):
            trace = tuple(tuple(u for i, (u, t) in enumerate(pairs)
                                if t == v and mask & (1 << i))
                          for v in range(4))
            for p in (16, 64):
                for mode in ("lazy", "bitmap"):
                    with tempfile.TemporaryDirectory() as root:
                        with FileReachIndex(root, mode, 4, p, 2) as db:
                            for v, parents in enumerate(trace):
                                before = db.store.data_page_writes
                                entry = db.append(parents)
                                self.assertEqual(entry["parents_input_bits"], v)
                                self.assertGreater(db.store.data_page_writes,
                                                   before)
                                for source in range(v+1):
                                    for target in range(v+1):
                                        yes, req = db.query(source, target)
                                        self.assertEqual(
                                            yes, independent_reach(
                                                trace, source, target),
                                            (mask, mode, p, source, target))
                                        self.assertGreater(req, 0)
                            report = db.report()
                            self.assertTrue(report["directory_lookup_paid"])
                            self.assertTrue(report["charged_key_directory"])
                            self.assertLessEqual(
                                report["user_cache_high_water_pages"], 2)
                            self.assertFalse(report["bounded_actual_rss"])
                            self.assertFalse(report["device_io_measured"])
                            self.assertEqual(report["vertices"], 4)
                            self.assertEqual(
                                report["source_parent_incidence_bits"], 6)
                        with FileReachIndex(root, mode, 4, p, 0) as restored:
                            for source in range(4):
                                for target in range(4):
                                    self.assertEqual(
                                        restored.query(source, target)[0],
                                        independent_reach(
                                            trace, source, target))
                    cases += 1
        self.assertEqual(cases, 64*2*2)

    def test_manifest_mode_mismatch_and_reopen_rejection(self):
        with tempfile.TemporaryDirectory() as root:
            with FileReachIndex(root, "bitmap", 8, 64) as db:
                db.append(())
                db.append((0,))
            with FileReachIndex(root, "lazy", 8, 64) as wrong:
                with self.assertRaisesRegex(ValueError, "mode/horizon"):
                    wrong.query(0, 1)
                with self.assertRaisesRegex(ValueError, "mode/horizon"):
                    wrong.append(())
            with FileReachIndex(root, "bitmap", 16, 64) as wrong_h:
                with self.assertRaisesRegex(ValueError, "mode/horizon"):
                    wrong_h.query(0, 1)
            with FileReachIndex(root, "bitmap", 8, 64) as right:
                self.assertTrue(right.query(0, 1)[0])

    def test_old_rows_immutable_and_manifest_only_publishes(self):
        with tempfile.TemporaryDirectory() as root:
            with FileReachIndex(root, "lazy", 5, 64) as db:
                db.append(())
                initial = db.store.read("parents:0")
                db.append((0,))
                self.assertEqual(db.store.read("parents:0"), initial)
                with self.assertRaises(ValueError):
                    db.append((1, 0))
                with self.assertRaises(ValueError):
                    db.append((0, 0))
                with self.assertRaises(ValueError):
                    db.append((2,))
                with self.assertRaises(ValueError):
                    db.query(0, 2)
                # Extra image without manifest does not publish a vertex.
                db.store.write("parents:2", b"\0\0")
                with self.assertRaises(ValueError):
                    db.query(0, 2)
                self.assertEqual(db.report()["vertices"], 2)

    def test_directory_and_kernel_page_cache_are_not_free(self):
        for mode in ("lazy", "bitmap"):
            with tempfile.TemporaryDirectory() as cold_dir:
                with FileReachIndex(cold_dir, mode, 16, 64, 0) as db:
                    trace = [()] + [(i-1,) for i in range(1, 12)]
                    for p in trace:
                        db.append(p)
                    before = db.store.data_page_reads + db.store.directory_page_reads
                    for _ in range(5):
                        self.assertTrue(db.query(0, 11)[0])
                    cold_reads = db.store.data_page_reads + db.store.directory_page_reads - before
                    self.assertGreater(cold_reads, 0)
            with tempfile.TemporaryDirectory() as hot_dir:
                with FileReachIndex(hot_dir, mode, 16, 64, 256) as db:
                    for p in trace:
                        db.append(p)
                    before = db.store.data_page_reads + db.store.directory_page_reads
                    for _ in range(5):
                        self.assertTrue(db.query(0, 11)[0])
                    warm_reads = db.store.data_page_reads + db.store.directory_page_reads - before
                    self.assertLessEqual(db.store.max_cached_observed, 256)
                    self.assertLess(warm_reads, cold_reads)
                    self.assertGreater(db.store.cache_hits, 0)

    def test_query_uses_serialized_rows_not_reference_graph(self):
        with tempfile.TemporaryDirectory() as root:
            with FileReachIndex(root, "lazy", 8, 16, 0) as db:
                for parents in ((), (), (0,), (1,), (2, 3)):
                    db.append(parents)
                self.assertNotIn("parents", db.__dict__)
                self.assertNotIn("ancestor_bits", db.__dict__)
                self.assertNotIn("top", db.__dict__)
                self.assertTrue(db.query(0, 4)[0])
                self.assertTrue(db.query(1, 4)[0])
                self.assertFalse(db.query(4, 0)[0])
                self.assertEqual(decode_parents(
                    db.store.read("parents:4")), (2, 3))

    def test_fail_invalid_or_corrupt_storage_records(self):
        with tempfile.TemporaryDirectory() as root:
            with self.assertRaises(ValueError):
                FileReachIndex(root, "bad", 8)
            with FileReachIndex(root, "lazy", 8) as db:
                db.append(())
                with self.assertRaises(ValueError):
                    db.query(-1, 0)
                with self.assertRaises(ValueError):
                    db.append((1,))
                with self.assertRaises(ValueError):
                    decode_parents(b"\2\0")
                self.assertEqual(db.report()["vertices"], 1)
            with FilePageStore(root, 64, 0) as s:
                with self.assertRaises(ValueError):
                    s.write("parents:0", b"tamper", immutable=False)


if __name__ == "__main__":
    unittest.main()
