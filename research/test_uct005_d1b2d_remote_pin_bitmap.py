"""D1-B2-D independent PIN history and authenticated bitmap finite oracles."""
import itertools
import unittest

from uct005_d1b0_f1_reference import Abort
from uct005_d1b2d_remote_pin_bitmap import (
    RemotePinBitmapF1, compare_history, future_pin_signature_count,
)


class RemotePinBitmapTests(unittest.TestCase):
    def test_all_short_binary_histories_same_page_service(self):
        for n in range(1, 6):
            for bits in itertools.product((0, 1), repeat=n):
                for p in (1, 2, 64):
                    row = compare_history(bits, p)
                    self.assertTrue(row["latest_snapshot_only"])
                    self.assertEqual(row["root_novelty"], "OPEN_UNPROVED")
                    self.assertEqual(row["cost_frontier"], "PARTIAL_NO_FULL_PARETO")
                    self.assertGreater(row["bitmap_remote_page_read_attempts"], 0)
                    self.assertGreater(row["bitmap_remote_page_writes"], 0)
                    self.assertGreater(row["bitmap_remote_drop_page_calls"], 0)
                    self.assertEqual(row["remote_pin_registry_local_trusted_bytes_excluding_reader_roots"], 40)
                    self.assertGreater(row["bitmap_verifier_hashed_bytes"], 0)

    def test_history_quotient_independent_subsets(self):
        for horizon in range(0, 9):
            for mask in range(1 << horizon):
                eligible = tuple(i for i in range(horizon) if mask & (1 << i))
                self.assertEqual(future_pin_signature_count(horizon, eligible),
                                 1 << len(eligible))
        self.assertEqual(future_pin_signature_count(5, tuple(range(5))), 32)
        self.assertEqual(future_pin_signature_count(5, (0, 2, 4)), 8)

    def test_exact_bitmap_page_rounding_and_trusted_state(self):
        for cap in (2, 5, 8, 17):
            for p in (1, 2, 8, 64):
                m = RemotePinBitmapF1((0,) * 33, p, cap)
                bytes_expected = (2 * cap + 7) // 8
                pages_expected = (bytes_expected + p - 1) // p
                data_pages = (5 + p - 1) // p
                manifest_pages = (48 + p - 1) // p
                self.assertEqual(m.bitmap_payload_bytes, bytes_expected)
                self.assertEqual(m.bitmap_pages, pages_expected)
                self.assertEqual(len(m.remote_pin_bitmap), bytes_expected)
                self.assertEqual(m.remote_pages, data_pages + manifest_pages + pages_expected)
                self.assertEqual(m.ledger["bitmap_setup_page_writes"], pages_expected)
                self.assertEqual(m.ledger["bitmap_setup_upload_bytes"], pages_expected * p)
                self.assertEqual(m.trusted_bits, 33 + 8 * 80)
                e0 = m.pin_current(0)
                self.assertEqual(e0, 0)
                self.assertEqual(m.trusted_bits, 33 + 8 * 120)
                self.assertEqual(m.ledger["bitmap_remote_page_writes"], pages_expected)
                self.assertEqual(m.ledger["bitmap_trusted_root_publication_bytes"], 40)
                self.assertEqual(m.ledger["bitmap_remote_upload_bytes"], pages_expected * p)
                m.assert_live_invariant()

    def test_two_readers_same_pin_and_independent_revoke(self):
        for p in (1, 2, 8, 64):
            m = RemotePinBitmapF1((0, 1, 0), p, 8)
            self.assertEqual(m.pin_current(0), 0)
            self.assertEqual(m.pin_current(1), 0)
            m.set(0, 1)
            self.assertEqual(set(m.remote), {0, 1})
            self.assertEqual(m.as_of(1, 0, 0, 3), 1)
            m.unpin(0, 0)
            self.assertIn(0, m.remote)
            self.assertEqual(m.as_of(1, 0, 0, 3), 1)
            m.unpin(1, 0)
            self.assertNotIn(0, m.remote)
            self.assertEqual(m.latest(0, 0, 3), 0)
            self.assertRaises(Abort, m.as_of, 1, 0, 0, 3)
            m.assert_live_invariant()
            self.assertEqual(set(m.remote), {1})

    def test_bitmap_tamper_replay_and_withholding_abort_before_author_change(self):
        for p in (1, 2, 64):
            m = RemotePinBitmapF1((0, 1, 1), p, 8)
            pre_root = m.trusted_bitmap_digest
            pre_bytes = m.remote_pin_bitmap
            m.pin_current(0)
            self.assertNotEqual(m.trusted_bitmap_digest, pre_root)
            # Correct old bitmap bytes with wrong current generation/root:
            m.remote_pin_bitmap = pre_bytes
            self.assertRaises(Abort, m.set, 0, 1)
            self.assertEqual(m.epoch, 0)
            self.assertRaises(Abort, m.unpin, 0, 0)
            self.assertIn(0, m.readers[0])
            m.remote_pin_bitmap = None
            self.assertRaises(Abort, m.pin_current, 1)
            self.assertEqual(m.epoch, 0)
            self.assertEqual(m.bitmap_generation, 1)
            # Restore only the exact authentic bitmap for current generation.
            m.remote_pin_bitmap = m._set_bit(pre_bytes, m._index(0, 0), True)
            self.assertEqual(m.unpin(0, 0), None)
            m.assert_live_invariant()

    def test_capacity_and_input_scope(self):
        self.assertRaises(ValueError, RemotePinBitmapF1, (0,), 1, 1)
        self.assertRaises(ValueError, RemotePinBitmapF1, (0,), 1, 65537)
        m = RemotePinBitmapF1((0,), 2, 2)
        self.assertEqual(m.set(0, 1), 1)
        self.assertRaises(ValueError, m.set, 0, 0)
        self.assertRaises(ValueError, m.pin_current, 2)
        self.assertRaises(ValueError, m.unpin, 0, 0)
        self.assertRaises(ValueError, future_pin_signature_count, 2, (2,))
        self.assertRaises(ValueError, future_pin_signature_count, 3, (1, 1))


if __name__ == "__main__":
    unittest.main()
