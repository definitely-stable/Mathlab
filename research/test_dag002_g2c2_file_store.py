"""File-backed, directory-priced backend finite oracles for DAG-002 C2-A."""
from __future__ import annotations

import os
import tempfile
from pathlib import Path
import unittest

from dag002_g2c2_file_store import FilePageStore, _ENTRY


class FileStoreTests(unittest.TestCase):
    def test_all_three_page_sizes_actual_files_and_reopen(self):
        for page in (16, 64, 4096):
            with tempfile.TemporaryDirectory() as root:
                with FilePageStore(root, page, 0) as s:
                    self.assertEqual(s.write("source:0", b""), 1)
                    self.assertEqual(s.write("support:1", bytes(range(91))),
                                     (91+page-1)//page)
                    self.assertEqual(s.read("source:0"), b"")
                    self.assertEqual(s.read("support:1"), bytes(range(91)))
                    before = s.report()
                    self.assertGreater(before["os_pread_directory_pages"], 0)
                    self.assertGreater(before["directory_entry_probes"], 0)
                    self.assertGreater(before["file_directory_bytes"], page)
                    self.assertEqual(before["file_data_bytes"] % page, 0)
                    self.assertEqual(before["file_directory_bytes"] % page, 0)
                    self.assertTrue(before["directory_lookup_paid"])
                    self.assertFalse(before["durable_on_crash"])
                    self.assertFalse(before["actual_process_rss_bounded"])
                with FilePageStore(root, page, 0) as restored:
                    self.assertEqual(restored.read("support:1"), bytes(range(91)))
                    self.assertEqual(restored.read("source:0"), b"")
                    with self.assertRaises(ValueError):
                        restored.write("source:0", b"cannot overwrite")
                    self.assertEqual(os.path.getsize(Path(root) / "data.bin"),
                                     before["file_data_bytes"])
                    self.assertEqual(restored.report()["cache_current_pages"], 0)

    def test_mutable_manifest_versions_persist_append_only(self):
        with tempfile.TemporaryDirectory() as root:
            with FilePageStore(root, 64, 2) as s:
                s.write("manifest", b"epoch-1", immutable=False)
                s.write("fixed", b"immutable!", immutable=True)
                old_directory_size = s.report()["file_directory_bytes"]
                s.write("manifest", b"epoch-2", immutable=False)
                self.assertEqual(s.read("manifest"), b"epoch-2")
                self.assertGreater(s.report()["file_directory_bytes"],
                                   old_directory_size)
                with self.assertRaises(ValueError):
                    s.write("fixed", b"tamper", immutable=False)
            with FilePageStore(root, 64, 0) as reopened:
                self.assertEqual(reopened.read("manifest"), b"epoch-2")
                self.assertEqual(reopened.read("fixed"), b"immutable!")
                self.assertGreaterEqual(reopened.report()["directory_entry_probes"], 3)

    def test_charged_directory_for_miss_and_first_item(self):
        with tempfile.TemporaryDirectory() as root:
            with FilePageStore(root, 16, 0) as s:
                for i in range(5):
                    s.write(f"vertex:{i}", bytes([i]) * 20)
                baseline = s.report()
                with self.assertRaises(KeyError):
                    s.read("absent")
                after = s.report()
                self.assertEqual(after["directory_entry_probes"] -
                                 baseline["directory_entry_probes"], 5)
                # Every entry takes 8 directory pages for P=16.
                self.assertEqual(after["os_pread_directory_pages"] -
                                 baseline["os_pread_directory_pages"],
                                 5 * s.slot_bytes // 16)
                delta = s.report()["os_pread_directory_pages"]
                self.assertEqual(s.read("vertex:0"), b"\0" * 20)
                self.assertGreater(s.report()["os_pread_directory_pages"],
                                   delta)

    def test_lru_capacity_and_repeated_lookup_caching(self):
        with tempfile.TemporaryDirectory() as root:
            with FilePageStore(root, 64, 3) as s:
                for i in range(4):
                    s.write(f"key:{i}", b"v" * 30)
                s.read("key:0")  # directory scan causes evictions
                s.read("key:3")
                before = s.report()
                s.read("key:3")
                after = s.report()
                self.assertLessEqual(after["cache_current_pages"], 3)
                self.assertLessEqual(after["cache_max_observed_pages"], 3)
                self.assertGreater(after["cache_hits"], before["cache_hits"])
                self.assertGreater(after["cache_evictions"], 0)
                self.assertEqual(after["read_page_bytes"], 64 * (
                    after["os_pread_directory_pages"] +
                    after["os_pread_payload_pages"]))

    def test_disk_corruption_rejected_and_not_masked_by_cache(self):
        with tempfile.TemporaryDirectory() as root:
            with FilePageStore(root, 64, 0) as s:
                s.write("proof", b"original payload")
                self.assertEqual(s.read("proof"), b"original payload")
            fd = os.open(Path(root) / "data.bin", os.O_RDWR)
            try:
                os.pwrite(fd, b"X", 0)
            finally:
                os.close(fd)
            with FilePageStore(root, 64, 0) as reopened:
                with self.assertRaisesRegex(IOError, "checksum"):
                    reopened.read("proof")

    def test_corrupt_directory_and_malformed_requests_fail(self):
        with tempfile.TemporaryDirectory() as root:
            with FilePageStore(root, 16, 0) as s:
                for key in ("", "a" * 65):
                    with self.assertRaises(ValueError):
                        s.exists(key)
                with self.assertRaises(TypeError):
                    s.write("x", bytearray(b"bad"))
                with self.assertRaises(ValueError):
                    s._write_pages("data", 1, bytes(16))
                s.write("valid", b"test")
            with self.assertRaises(ValueError):
                FilePageStore(root, 64, 0)
            fd = os.open(Path(root) / "directory.bin", os.O_RDWR)
            try:
                # First directory entry begins after the 16-byte header page.
                os.pwrite(fd, b"FAIL", 16)
            finally:
                os.close(fd)
            with FilePageStore(root, 16, 0) as reopened:
                with self.assertRaisesRegex(ValueError, "corrupt directory"):
                    reopened.read("valid")

    def test_real_os_io_not_misrepresented_as_device_latency(self):
        with tempfile.TemporaryDirectory() as root:
            with FilePageStore(root, 64, 0) as s:
                s.write("x", b"data")
                s.read("x")
                report = s.report()
                self.assertGreater(report["os_pwrite_payload_pages"], 0)
                self.assertGreater(report["os_pread_payload_pages"], 0)
                self.assertGreater(report["os_metadata_syscalls_counted_not_priced"], 0)
                self.assertFalse(report["filesystem_syscall_cost_model_complete"])
                self.assertFalse(report["novel_lower_bound_proved"])


if __name__ == "__main__":
    unittest.main()
