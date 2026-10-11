"""Independent exact tests: disk-backed Felsner/SEA power vs disk lazy/bitmap."""
from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

from dag002_g2c2_disk_power import (
    DiskPowerIndex, encode_state, decode_state,
)
from dag002_g2c2_disk_reach import FileReachIndex
from dag002_g2b2_felsner import (
    FelsnerUpGrowing, source_dfs, exact_width,
)


class DiskPowerTests(unittest.TestCase):
    def test_all_four_node_dags_against_independent_dfs_and_classical_chains(self):
        edges = [(u, v) for v in range(4) for u in range(v)]
        for mask in range(1 << len(edges)):
            trace = tuple(tuple(u for bit, (u, t) in enumerate(edges)
                                if t == v and mask & (1 << bit))
                          for v in range(4))
            for page in (16, 64):
                with tempfile.TemporaryDirectory() as root:
                    with DiskPowerIndex(root, 4, page, 2, 0) as db:
                        independent = FelsnerUpGrowing()
                        for v, parents in enumerate(trace):
                            step = db.append(parents)
                            separate = independent.append(parents)
                            self.assertEqual(step.chain, separate.chain)
                            self.assertEqual(step.level, separate.level)
                            self.assertFalse(independent.invariant_errors())
                            self.assertGreaterEqual(
                                exact_width(independent.anc) *
                                (exact_width(independent.anc)+1) // 2,
                                len(independent.chains))
                            n, heads, groups = db.state()
                            self.assertEqual(n, v+1)
                            self.assertEqual(len(heads), len(independent.chains))
                            self.assertEqual(sum(map(len, groups)), len(heads))
                            for u in range(v+1):
                                for t in range(v+1):
                                    got, requests = db.query(u, t)
                                    self.assertEqual(
                                        got, source_dfs(trace, u, t),
                                        (mask, page, v, u, t))
                                    self.assertGreater(requests, 0)
                        report = db.report()
                        self.assertTrue(report["charged_all_historical_support_reads"])
                        self.assertTrue(report["directory_lookup_paid"])
                        self.assertFalse(report["process_rss_bounded"])
                        self.assertFalse(report["physical_ssd_io_measured"])
                        self.assertGreater(report["os_pread_directory_pages"], 0)
                    with DiskPowerIndex(root, 4, page, 2, 0) as restored:
                        for u in range(4):
                            for t in range(4):
                                self.assertEqual(restored.query(u, t)[0],
                                                 source_dfs(trace, u, t))

    def test_same_source_bytes_as_lazy_and_bitmap_competitors(self):
        trace = ((), (), (0,), (1,), (2, 3), (0, 1, 4))
        with tempfile.TemporaryDirectory() as root:
            with DiskPowerIndex(Path(root) / "power", 8, 64, 2, 0) as a, \
                 FileReachIndex(Path(root) / "lazy", "lazy", 8, 64, 0) as b, \
                 FileReachIndex(Path(root) / "bitmap", "bitmap", 8, 64, 0) as c:
                for parents in trace:
                    a.append(parents)
                    b.append(parents)
                    c.append(parents)
                for v in range(len(trace)):
                    images = (
                        a.store.read(f"parents:{v}"),
                        b.store.read(f"parents:{v}"),
                        c.store.read(f"parents:{v}"),
                    )
                    self.assertEqual(images[0], images[1])
                    self.assertEqual(images[1], images[2])
                for u in range(len(trace)):
                    for v in range(len(trace)):
                        independent = source_dfs(trace, u, v)
                        self.assertEqual(a.query(u, v)[0], independent)
                        self.assertEqual(b.query(u, v)[0], independent)
                        self.assertEqual(c.query(u, v)[0], independent)
                self.assertGreater(a.report()["os_pread_payload_pages"], 0)

    def test_reopen_then_append_without_cached_old_poset(self):
        trace = ((), (), (0,), (1,), (2, 3), (4,), (0, 5))
        with tempfile.TemporaryDirectory() as root:
            with DiskPowerIndex(root, 9, 64, 3, 0) as original:
                for p in trace[:4]:
                    original.append(p)
            with DiskPowerIndex(root, 9, 64, 3, 0) as reopened:
                for p in trace[4:]:
                    reopened.append(p)
                for u in range(len(trace)):
                    for v in range(len(trace)):
                        self.assertEqual(reopened.query(u, v)[0],
                                         source_dfs(trace, u, v))
                self.assertNotIn("anc", reopened.__dict__)
                self.assertNotIn("partition", reopened.__dict__)
                self.assertNotIn("parents", reopened.__dict__)
                self.assertEqual(reopened.report()["vertices"], len(trace))

    def test_model_scratch_reject_before_files_publication(self):
        with tempfile.TemporaryDirectory() as root:
            with DiskPowerIndex(root, 16, 64, 2, 0, 1) as db:
                start = db.store.report()
                with self.assertRaises(MemoryError):
                    db.append(())
                after = db.store.report()
                self.assertEqual(after["file_directory_bytes"],
                                 start["file_directory_bytes"])
                self.assertEqual(after["file_data_bytes"],
                                 start["file_data_bytes"])
                self.assertEqual(db.state()[0], 0)

    def test_corrupt_manifest_and_wrong_parameters_fail_explicitly(self):
        payload = encode_state(3, 16, 2, [2, 1], [[0], [1]])
        self.assertEqual(decode_state(payload, 16, 2),
                         (3, [2, 1], [[0], [1]]))
        for invalid in (payload[:-1], payload+b"\0", b"x"):
            with self.assertRaises(ValueError):
                decode_state(invalid, 16, 2)
        duplicated = encode_state(2, 16, 2, [0, 1], [[0], [0]])
        with self.assertRaises(ValueError):
            decode_state(duplicated, 16, 2)
        with tempfile.TemporaryDirectory() as root:
            with DiskPowerIndex(root, 8, 64, 2) as db:
                db.append(())
            with DiskPowerIndex(root, 8, 64, 3) as wrong:
                with self.assertRaisesRegex(ValueError, "parameters"):
                    wrong.query(0, 0)
            with DiskPowerIndex(root, 16, 64, 2) as wrong:
                with self.assertRaisesRegex(ValueError, "parameters"):
                    wrong.append(())

    def test_application_cache_limit_and_repeated_queries(self):
        with tempfile.TemporaryDirectory() as root:
            with DiskPowerIndex(root, 32, 64, 2, 3) as db:
                for v in range(16):
                    db.append((v-1,) if v else ())
                for _ in range(3):
                    self.assertTrue(db.query(0, 15)[0])
                    self.assertFalse(db.query(15, 0)[0])
                r = db.report()
                self.assertLessEqual(r["cache_max_observed_pages"], 3)
                self.assertGreater(r["cache_evictions"], 0)
                self.assertGreater(r["os_pread_directory_pages"], 0)
                self.assertFalse(r["crash_durable"])
                self.assertFalse(r["kernel_cache_bounded"])


if __name__ == "__main__":
    unittest.main()
