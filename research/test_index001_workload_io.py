"""INDEX-001 G2-B2-A: independently check filesystem-IO byte formulas."""
import unittest

from index001_workload_io import build_report, compare_trace, workload_traces


class Index001WorkloadIoTests(unittest.TestCase):
    def test_four_frozen_traces_have_exact_update_and_io_accounting(self):
        rows = build_report()["workloads"]
        self.assertEqual(set(rows), {"full_overwrite", "alternating_singletons",
                                     "nested_ranges", "repeated_hot_region"})
        for name, info in rows.items():
            with self.subTest(trace=name):
                u = info["updates"]
                size = info["size"]
                s = 24 + 4 * size
                self.assertGreater(u, 0)
                self.assertEqual(info["snapshot_frame_bytes"], s)
                self.assertEqual(info["wal_frame_bytes"], 28)
                direct = info["snapshot_only"]
                self.assertEqual(direct["written_bytes"], s * (u + 1))
                self.assertEqual(direct["written_bytes"], direct["expected_bytes"])
                self.assertEqual(direct["restart_read_bytes"], s)
                self.assertEqual(len(info["wal_policies"]), 3)
                for row in info["wal_policies"]:
                    t = row["threshold"]
                    c = u // t
                    tail = u % t
                    self.assertEqual(row["checkpoints"], c)
                    self.assertEqual(row["remaining_log_records"], tail)
                    self.assertEqual(row["wal_bytes"], 28 * u)
                    self.assertEqual(row["snapshot_bytes"], s * (1 + c))
                    self.assertEqual(row["written_bytes"],
                                     s * (1 + c) + 28 * u)
                    self.assertEqual(row["written_bytes"], row["expected_bytes"])
                    self.assertEqual(row["wal_truncation_events"], c)
                    self.assertEqual(row["restart_read_bytes"], s + tail * 28)
                    self.assertGreater(row["file_syncs"], 0)
                    self.assertGreater(row["directory_syncs"], 0)
                    frac = row["amplification"]
                    self.assertEqual(frac["numerator"] * 4 *
                                     info["logical_blocks_assigned"],
                                     frac["denominator"] * row["written_bytes"])

    def test_thresholds_expose_real_reference_tradeoff_not_global_winner(self):
        for name, row in build_report()["workloads"].items():
            with self.subTest(name=name):
                direct = row["snapshot_only"]["written_bytes"]
                small, medium, large = row["wal_policies"]
                self.assertGreater(small["written_bytes"], direct)
                self.assertLess(medium["written_bytes"], small["written_bytes"])
                self.assertLess(large["written_bytes"], medium["written_bytes"])
                self.assertLess(large["written_bytes"], direct)
                # Retaining WAL reduces foreground full-map writes but increases
                # restart WAL bytes when it has no final checkpoint.
                self.assertLessEqual(small["restart_read_bytes"],
                                     large["restart_read_bytes"])

    def test_zero_updates_and_one_update_are_accounted_without_divide_by_zero(self):
        empty = compare_trace([], size=4, thresholds=(1, 4))
        self.assertEqual(empty["snapshot_only"]["written_bytes"], 40)
        self.assertIsNone(empty["snapshot_only"]["amplification"])
        for policy in empty["wal_policies"]:
            self.assertEqual(policy["written_bytes"], 40)
            self.assertEqual(policy["checkpoints"], 0)
            self.assertEqual(policy["remaining_log_records"], 0)
        one = compare_trace([(1, 3, 4)], size=4, thresholds=(1, 4))
        self.assertEqual(one["snapshot_only"]["written_bytes"], 80)
        self.assertEqual(one["wal_policies"][0]["written_bytes"], 108)
        self.assertEqual(one["wal_policies"][1]["written_bytes"], 68)
        self.assertEqual(one["wal_policies"][1]["restart_read_bytes"], 68)

    def test_reproducible_report_and_invalid_parameters(self):
        a = build_report()
        b = build_report()
        self.assertEqual(a, b)
        self.assertEqual(a["nand_physical_bytes"], "NOT_MEASURED")
        self.assertEqual(a["timing_metrics"], "NOT_MEASURED")
        self.assertIn("NOT_DEVICE_IO", a["classification"])
        self.assertEqual(len(workload_traces()), 4)
        for invalid in ((), (0, 2), (1, 1), (1.5, 4)):
            with self.assertRaises(ValueError):
                compare_trace([], thresholds=invalid)
        with self.assertRaises(ValueError):
            compare_trace([(3, 2, 1)], size=4)
        with self.assertRaises(ValueError):
            compare_trace([(0, 5, 1)], size=4)


if __name__ == "__main__":
    unittest.main()
