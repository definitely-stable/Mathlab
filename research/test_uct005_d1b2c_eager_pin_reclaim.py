"""D1-B2-C independent finite tests: eager versus scanning PAGE-001 F1."""
import itertools
import unittest

from uct005_d1b0_f1_reference import Abort, SnapshotF1Reference
from uct005_d1b2c_eager_pin_reclaim import EagerPinReclaim, exercise


class EagerPINReclaimFiniteTests(unittest.TestCase):
    def test_shared_exact_transcript_all_small_initial_words_and_pages(self):
        for n in range(1, 7):
            for bits in itertools.product((0, 1), repeat=n):
                for p in (1, 2, 64):
                    row = exercise(bits, p)
                    self.assertTrue(row["same_latest_and_historical_answers"])
                    self.assertTrue(row["same_data_write_pages"])
                    self.assertEqual(row["root_status"], "OPEN_UNPROVED")
                    self.assertEqual(row["no_op_set_epochs"], 1)
                    self.assertEqual(row["independent_pins"], 2)
                    self.assertEqual(row["eager_remote_slot_reads_for_gc"], 0)
                    self.assertGreater(row["scan_remote_slot_reads_for_gc"], 0)
                    self.assertEqual(row["eager_peak_pages"], 3 * row["page_slot_full_pages"])
                    self.assertEqual(row["scan_peak_pages"], 4 * row["page_slot_full_pages"])
                    self.assertEqual(row["scan_before_first_gc_pages"],
                                     4 * row["page_slot_full_pages"])
                    self.assertEqual(row["scan_initial_gc_freed_pages"],
                                     row["page_slot_full_pages"])
                    self.assertEqual(row["eager_remote_page_delete_calls"],
                                     3 * row["page_slot_full_pages"])
                    self.assertEqual(row["eager_remote_delete_request_bytes"],
                                     8 * row["eager_remote_page_delete_calls"])
                    self.assertEqual(row["eager_logical_reclaimed_pages"],
                                     row["scan_logical_reclaimed_pages"])
                    self.assertGreater(row["eager_trusted_pin_record_page_reads"], 0)

    def test_without_any_pins_reclaim_is_immediate_after_every_set(self):
        for n, p in ((1, 1), (8, 2), (33, 2), (65, 64)):
            m = EagerPinReclaim((0,) * n, p)
            L = (n + 7) // 8
            expected = (L + p - 1) // p + (48 + p - 1) // p
            for e in range(1, 10):
                old = m.epoch
                bit = e & 1
                self.assertEqual(m.set(0, bit), e)
                self.assertNotIn(old, m.remote)
                self.assertEqual(set(m.remote), {e})
                self.assertEqual(m.remote_pages, expected)
                self.assertEqual(m.gc(), 0)
            self.assertEqual(m.ledger["peak_remote_pages"], 2 * expected)
            self.assertEqual(m.ledger["gc_directory_page_reads"], 0)
            self.assertEqual(m.ledger["eager_remote_drop_page_calls"], 9 * expected)
            self.assertEqual(m.ledger["eager_remote_drop_page_request_bytes"], 72 * expected)
            self.assertEqual(m.ledger["eager_authority_pin_record_page_reads"], 0)

    def test_two_independent_pins_prevent_premature_reclaim(self):
        for p in (1, 2, 8, 64):
            m = EagerPinReclaim((0, 1, 0), p)
            e0 = m.pin_current(0)
            self.assertEqual(m.pin_current(1), e0)  # same epoch, two readers
            m.set(0, 1)
            self.assertEqual(m.as_of(0, e0, 0, 3), 1)
            m.set(2, 1)
            self.assertIn(0, m.remote)
            self.assertNotIn(1, m.remote)
            m.unpin(0, e0)
            self.assertIn(0, m.remote, "reader 1 still PINs the epoch")
            self.assertEqual(m.as_of(1, e0, 0, 3), 1)
            m.unpin(1, e0)
            self.assertNotIn(0, m.remote)
            self.assertRaises(Abort, m.as_of, 1, e0, 0, 3)
            self.assertEqual(set(m.remote), {2})
            self.assertEqual(set(m.remote), set(m.remote_manifests))
            self.assertEqual(m.latest(0, 0, 3), 1)

    def test_explicit_unpin_latest_is_not_deletion(self):
        for p in (1, 2, 16, 64):
            m = EagerPinReclaim((1, 0, 1, 1), p)
            epoch = m.pin_current(0)
            m.unpin(0, epoch)
            self.assertEqual(set(m.remote), {0})
            self.assertEqual(m.latest(1, 0, 4), 1)
            self.assertEqual(m.gc(), 0)
            self.assertEqual(m.ledger["eager_remote_drop_page_calls"], 0)

    def test_replay_corruption_and_invalid_operations(self):
        for p in (1, 2, 64):
            m = EagerPinReclaim((0, 1), p)
            e0 = m.pin_current(0)
            m.set(0, 1)
            self.assertRaises(Abort, m.latest, 0, 0, 2, presented_epoch=0)
            self.assertRaises(Abort, m.latest, 0, 0, 2, presented=b"\xff")
            self.assertEqual(m.as_of(0, e0, 0, 2), 1)
            m.unpin(0, e0)
            self.assertRaises(Abort, m.as_of, 0, e0, 0, 2)
            self.assertRaises(ValueError, m.pin_current, 2)
            self.assertRaises(ValueError, m.set, -1, 1)
            self.assertRaises(ValueError, m.unpin, 0, e0)

    def test_explicit_cost_separation_no_fictitious_full_pareto(self):
        row = exercise((1, 0, 1, 0), 2)
        self.assertEqual(row["pareto_verdict"],
                         "UNDECIDABLE_WITHOUT_FULL_TRUSTED_CPU_AND_DELETE_API_COSTS")
        self.assertGreater(row["eager_trusted_pin_record_page_reads"], 0)
        self.assertGreater(row["eager_remote_page_delete_calls"], 0)
        self.assertEqual(row["eager_trusted_root_bytes_read"], 40 * 5)
        self.assertEqual(row["eager_remote_slot_reads_for_gc"], 0)
        self.assertGreater(row["scan_remote_slot_reads_for_gc"], 0)


if __name__ == "__main__":
    unittest.main()
