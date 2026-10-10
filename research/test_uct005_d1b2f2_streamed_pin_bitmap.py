"""Finite independent streamed PIN bitmap oracle and page-image negative cases."""
import itertools
import unittest

from uct005_d1b0_f1_reference import Abort
from uct005_d1b2f2_streamed_pin_bitmap import StreamedPinBitmapF1, compare_streamed_history


class StreamingPINTests(unittest.TestCase):
    def test_all_initial_words_same_F1_transcript(self):
        for n in range(1, 6):
            for bits in itertools.product((0, 1), repeat=n):
                for p in (1, 2, 64):
                    row = compare_streamed_history(bits, p, cap=8)
                    self.assertLessEqual(
                        row["peak_trusted_bitmap_payload_buffer_bytes"], row["bound"])
                    self.assertGreater(row["stream_bitmap_page_reads"],
                                       row["bulk_bitmap_page_reads"])
                    self.assertEqual(row["root_novelty"], "OPEN_UNPROVED")

    def test_precise_page_rounding_and_transient_staging(self):
        for cap in (4, 8, 17, 257):
            for p in (1, 2, 64):
                m = StreamedPinBitmapF1((0, 1), p, cap)
                B = (2 * cap + 7) // 8
                N = (B + p - 1) // p
                self.assertEqual(m.bitmap_pages, N)
                self.assertEqual(m._slot_start_page(0), 2 * N)
                self.assertEqual(m._bitmap_page_address(0, 0), 0)
                self.assertEqual(m._bitmap_page_address(0, 1), N)
                with self.assertRaises(RuntimeError):
                    _ = m.retained_pinned_pages
                with self.assertRaises(RuntimeError):
                    m._read_verified_bitmap()
                self.assertEqual(m.bitmap_peak_trusted_payload_buffers, min(B, p))
                self.assertEqual(m.trusted_bits, 2 + 8 * 80)
                self.assertEqual(m.pin_current(0), 0)
                self.assertEqual(m.bitmap_generation, 1)
                self.assertEqual(m.ledger["bitmap_stream_pass1_page_read_attempts"], N)
                self.assertEqual(m.ledger["bitmap_stream_pass2_page_read_attempts"], N)
                self.assertEqual(m.ledger["bitmap_stream_stage_page_writes"], N)
                self.assertEqual(m.ledger["bitmap_remote_upload_bytes"], N * p)
                self.assertEqual(m.ledger["bitmap_stream_peak_payload_buffer_bytes"],
                                 2 * min(B, p))
                self.assertEqual(m.ledger["peak_remote_pages"],
                                 m._pages_per_snapshot() + 2 * N)
                self.assertEqual(m.trusted_bits, 2 + 8 * 120)
                m.set(1, 1)
                self.assertEqual(m.ledger["bitmap_stream_set_scan_page_read_attempts"], N)
                m.unpin(0, 0)
                self.assertEqual(m.bitmap_generation, 2)
                self.assertEqual(set(m.remote), {1})
                m.assert_live_invariant()

    def test_missing_replayed_corrupt_and_noncanonical_wire_abort(self):
        for p in (1, 2, 64):
            m = StreamedPinBitmapF1((0, 1, 1), p, 17)
            baseline = dict(m.bitmap_store)
            initial = (m.epoch, m.bitmap_generation, m.trusted_bitmap_digest)
            changed = bytearray(baseline[0])
            changed[0] ^= 8
            m.bitmap_store[0] = bytes(changed)
            with self.assertRaises(Abort):
                m.pin_current(0)
            with self.assertRaises(Abort):
                m.set(0, 1)
            self.assertEqual(initial, (m.epoch, m.bitmap_generation,
                                       m.trusted_bitmap_digest))
            m.bitmap_store = dict(baseline)
            m.bitmap_store[0] = baseline[0][:-1]
            with self.assertRaises(Abort):
                m.pin_current(0)
            m.bitmap_store = dict(baseline)
            del m.bitmap_store[0]
            with self.assertRaises(Abort):
                m.pin_current(0)
            m.bitmap_store = dict(baseline)
            if m.bitmap_pages * p > m.bitmap_payload_bytes:
                altered = bytearray(m.bitmap_store[m.bitmap_pages - 1])
                altered[-1] = 1
                m.bitmap_store[m.bitmap_pages - 1] = bytes(altered)
                with self.assertRaises(Abort):
                    m.pin_current(0)
                m.bitmap_store = dict(baseline)
            m.pin_current(0)
            m.bitmap_store = dict(baseline)
            with self.assertRaises(Abort):
                m.unpin(0, 0)
            self.assertIn(0, m.readers[0])
            self.assertEqual(m.bitmap_generation, 1)

    def test_between_passes_change_discards_stage(self):
        class SwitchingPage(StreamedPinBitmapF1):
            switch = False
            def _page(self, page, *, pass_name):
                if self.switch and pass_name == "pass2" and page == 1:
                    img = bytearray(self.bitmap_store[page])
                    img[0] ^= 1
                    self.bitmap_store[page] = bytes(img)
                return super()._page(page, pass_name=pass_name)

        m = SwitchingPage((1, 0), 1, 8)
        m.switch = True
        with self.assertRaises(Abort):
            m.pin_current(0)
        self.assertEqual(m.bitmap_generation, 0)
        self.assertIsNone(m.bitmap_stage)
        self.assertGreater(m.ledger["bitmap_stream_stage_abort_drop_calls"], 0)
        self.assertFalse(m.readers[0])


if __name__ == "__main__":
    unittest.main()
