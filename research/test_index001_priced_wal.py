"""Independent finite/cost tests for INDEX-001 G2-B4-C0 comparator."""
from itertools import product
import unittest

from index001_page_recourse import image_for, packed_image, page_difference
from index001_variable_checkpoint import encode_wal, decode_snapshot
from index001_priced_wal import (
    assign, budget, bounded_epoch_limit, compare_trace, flat_update, initial_wal, pages, report,
    wal_disk_bytes, wal_lookup, wal_step,
)


def independent_page_changes(before, after, block):
    """Bytewise block census, not the production padded_pages routine."""
    cap = max(len(before), len(after))
    differing = set()
    for offset in range(cap):
        left = before[offset] if offset < len(before) else 0
        right = after[offset] if offset < len(after) else 0
        if left != right:
            differing.add(offset // block)
    return len(differing)


def independent_replay(base, frames):
    result = list(decode_snapshot(packed_image(base)))
    for record in frames:
        # Decode by a distinct independent dense replay process.
        from index001_variable_checkpoint import decode_wal
        lo, hi, value = decode_wal(len(result), record)
        for i in range(lo, hi):
            result[i] = value
    return tuple(result)


class PricedWalTest(unittest.TestCase):
    def test_exact_finite_one_step_exhaustion(self):
        seen = 0
        for n in range(1, 5):
            group = min(8, n)
            for before in product((0, 1), repeat=n):
                for lo in range(n):
                    for hi in range(lo + 1, n + 1):
                        for bit in (0, 1):
                            op = (lo, hi, bit)
                            after = assign(before, op)
                            output = compare_trace(before, [op], 32, group, 2)
                            rows = output[0]["strategies"]
                            self.assertEqual(len(rows), 3)
                            self.assertEqual([x["layout"] for x in rows],
                                             ["packed", "segmented", "wal"])
                            for layout in ("packed", "segmented"):
                                old = image_for(layout, before, group, 32)
                                new = image_for(layout, after, group, 32)
                                expected = independent_page_changes(old, new, 32)
                                row = next(x for x in rows if x["layout"] == layout)
                                self.assertEqual(row["written_model_bytes"], expected*32)
                                expected_reads = (pages(len(old), 32) if layout == "packed"
                                                  else ((hi - 1)//group - lo//group + 1) *
                                                       pages(len(image_for("segmented", before[:group], group, 32)), 32))
                                self.assertEqual(row["read_update_pages"], expected_reads)
                                self.assertEqual(row["disk_bytes_after"], pages(len(new), 32)*32)
                                self.assertEqual(row["peak_bytes"],
                                                 max(pages(len(old), 32),
                                                     pages(len(new), 32))*32)
                                self.assertEqual(row["within_steady_budget"],
                                                 row["disk_bytes_after"] <= budget(after, 32))
                                self.assertEqual(row["state"], "".join(map(str, after)))
                            # One WAL append (threshold 2) plus paid control page.
                            appended = rows[2]
                            self.assertEqual(appended["operation"], "wal_append")
                            self.assertEqual(appended["written_model_bytes"], 64)
                            self.assertEqual(appended["allocated_pages"], 1)
                            self.assertEqual(appended["read_update_pages"], 1)
                            self.assertEqual(appended["disk_bytes_after"], 96)
                            self.assertEqual(appended["retired_pages"], 0)
                            seen += 1
        self.assertEqual(seen, 4 + 24 + 96 + 320)

    def test_paired_wal_rollback_and_checkpoint_oracles(self):
        for n in range(1, 4):
            ops = [(lo, hi, bit) for lo in range(n)
                   for hi in range(lo+1, n+1) for bit in (0, 1)]
            for before in product((0, 1), repeat=n):
                for first in ops:
                    s1, r1 = wal_step(initial_wal(before), first, 32, 2)
                    self.assertEqual(s1.latest, independent_replay(s1.base, s1.frames))
                    self.assertEqual(r1["operation"], "wal_append")
                    for second in ops:
                        s2, r2 = wal_step(s1, second, 32, 2)
                        self.assertEqual(r2["operation"], "checkpoint")
                        self.assertEqual(s2.latest, assign(assign(before, first), second))
                        self.assertEqual(independent_replay(s2.base, s2.frames), s2.latest)
                        self.assertEqual(len(s2.frames), 0)
                        self.assertEqual(r2["retired_pages"],
                                         pages(len(packed_image(before)), 32) + 1)
                        self.assertEqual(r2["read_update_pages"], 3)
                        self.assertEqual(r2["allocated_pages"],
                                         pages(len(packed_image(s2.latest)), 32))
                        self.assertEqual(r2["materialized_checkpoint_payload"],
                                         len(packed_image(s2.latest)))
                        self.assertEqual(r2["peak_bytes"],
                                         wal_disk_bytes(s1, 32) +
                                         pages(len(packed_image(s2.latest)), 32)*32)
                        for p, v in enumerate(s2.latest):
                            self.assertEqual(wal_lookup(s2, p, 32)[0], v)

    def test_explicit_budget_counterexample_not_general_tradeoff(self):
        zero = (0,) * 64
        self.assertEqual(len(packed_image(zero)), 12)
        self.assertEqual(len(image_for("segmented", zero, 8, 32)), 256)
        self.assertEqual(budget(zero, 32), 112)
        self.assertGreater(256, budget(zero, 32))
        self.assertLessEqual(32, budget(zero, 32))
        self.assertLessEqual(wal_disk_bytes(initial_wal(zero), 32), budget(zero, 32))
        info = report()
        self.assertEqual(info["zero64"]["slots_bytes"], 256)
        self.assertEqual(len(info["trace"]), 6)

    def test_bounded_epoch_certificate_and_fourth_effective_toggle(self):
        state = (0,) * 64
        frame_size = len(encode_wal(64, 0, 1, 1))
        self.assertEqual(frame_size, 9)
        cap = bounded_epoch_limit(state, 32, 14, frame_size)
        self.assertEqual(cap["max_log_pages"], 1)
        self.assertEqual(cap["max_uncheckpointed_appends"], 3)
        wal = initial_wal(state)
        for value in (1, 0, 1):
            wal, ledger = wal_step(wal, (0, 1, value), 32, threshold=10)
            self.assertEqual(ledger["operation"], "wal_append")
            self.assertTrue(ledger["disk_bytes_after"] <= budget(wal.latest, 32))
        wal, fourth = wal_step(wal, (0, 1, 0), 32, threshold=10)
        self.assertEqual(fourth["operation"], "wal_append")
        self.assertEqual(fourth["disk_bytes_after"], 128)
        self.assertGreater(fourth["disk_bytes_after"], budget(wal.latest, 32))
        # A checkpoint-enabled policy avoids this steady violation at t=4,
        # while necessarily charging materialization and generation overlap.
        policy = initial_wal(state)
        for value in (1, 0, 1, 0):
            policy, action = wal_step(policy, (0, 1, value), 32, threshold=4)
        self.assertEqual(action["operation"], "checkpoint")
        self.assertLessEqual(action["disk_bytes_after"], budget(policy.latest, 32))
        self.assertGreater(action["peak_bytes"], action["disk_bytes_after"])

    def test_point_vs_range_segmentation_and_wal_amplification(self):
        bits = (0,) * 64
        local = flat_update(bits, (0, 1, 1), 32, 8, "segmented")
        large = flat_update(bits, (0, 64, 1), 32, 8, "segmented")
        self.assertEqual(local["changed_page_images"], 1)
        self.assertEqual(large["changed_page_images"], 8)
        self.assertEqual(local["max_point_query_pages"], 1)
        wal = initial_wal(bits)
        for idx in range(2):
            wal, rec = wal_step(wal, (0, 1, 0), 32, 3)
            self.assertEqual(rec["operation"], "wal_append")
        self.assertEqual(len(wal.frames), 2)
        self.assertEqual(rec["read_update_pages"], 2)
        self.assertEqual(wal.latest, bits)  # semantically idempotent, physically charged
        self.assertGreaterEqual(wal_disk_bytes(wal, 32), 96)
        wal, rec = wal_step(wal, (0, 1, 0), 32, 3)
        self.assertEqual(rec["operation"], "checkpoint")
        self.assertEqual(rec["retired_pages"], 2)
        self.assertEqual(len(wal.frames), 0)

    def test_bounds_fail_closed(self):
        with self.assertRaises(ValueError):
            wal_step(initial_wal((0,)), (0, 1, 1), threshold=0)
        with self.assertRaises(ValueError):
            assign((0, 1), (1, 1, 0))
        with self.assertRaises(ValueError):
            budget((0,), 32, alpha=-1)
        self.assertEqual(budget((0,), 32, gamma=3, m_bits=0), budget((0,), 32))
        self.assertEqual(budget((0,), 32, gamma=3, m_bits=9), budget((0,), 32) + 6)
        with self.assertRaises(ValueError):
            compare_trace((0, 1), [(0, 1, 1)], group=3)


if __name__ == "__main__":
    unittest.main()
