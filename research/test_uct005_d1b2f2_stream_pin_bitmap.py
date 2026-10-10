"""Independent F1 PIN bitmap streaming, page conservation and TOCTOU tests."""
import itertools
import unittest

from uct005_d1b0_f1_reference import Abort
from uct005_d1b2d_remote_pin_bitmap import RemotePinBitmapF1
from uct005_d1b2f2_stream_pin_bitmap import (
    StreamedRemotePinBitmapF1, compare, STATUS,
)


class StreamedPINFiniteTests(unittest.TestCase):
    def test_all_initial_small_gf2_words_and_page_shapes(self):
        for n in range(1, 6):
            for word in itertools.product((0, 1), repeat=n):
                for p in (1, 2, 64):
                    outcome = compare(word, p, 8)
                    self.assertEqual(outcome["classification"], STATUS)
                    self.assertTrue(outcome["same_all_honest_answers"])
                    self.assertTrue(outcome["same_live_pages_with_two_PINS"])
                    self.assertTrue(outcome["trusted_persistent_bits_same"])
                    self.assertEqual(outcome["root_novelty"], "OPEN_UNPROVED")
                    self.assertEqual(outcome["total_peak_trust_state_bound"],
                                     "UNKNOWN_CRYPTO_AND_OTHER_TRANSIENT_SCRATCH")
                    self.assertEqual(outcome["stream_remote_staging_peak_additional_pages"],
                                     outcome["bitmap_pages"])
                    self.assertEqual(outcome["stream_second_pass_extra_bitmap_page_reads"],
                                     4 * outcome["bitmap_pages"])
                    self.assertEqual(outcome["stream_bitmap_page_reads"],
                                     outcome["bulk_bitmap_page_reads"]
                                     + 4 * outcome["bitmap_pages"])
                    self.assertEqual(outcome["stream_bitmap_page_writes"],
                                     outcome["bulk_bitmap_page_writes"])
                    self.assertEqual(outcome["stream_protocol_peak_trusted_bitmap_buffer_bytes"],
                                     2 * min(outcome["bitmap_bytes"], p))

    def test_large_capacity_exposes_persistent_not_peak_trust(self):
        for cap, p in ((8,1),(8,64),(128,2),(256,64),(4096,2),(4096,64)):
            result=compare((0,)*33,p,cap)
            B=(2*cap+7)//8
            M=(B+p-1)//p
            self.assertEqual(result["bitmap_bytes"],B)
            self.assertEqual(result["bitmap_pages"],M)
            self.assertEqual(result["bulk_abstract_three_resident_bitmap_images_bytes"],
                             3*B)
            self.assertEqual(result["stream_protocol_peak_trusted_bitmap_buffer_bytes"],
                             2*min(B,p))
            if B > 2*p:
                self.assertLess(result["stream_protocol_peak_trusted_bitmap_buffer_bytes"],
                                result["bulk_abstract_three_resident_bitmap_images_bytes"])
            self.assertGreaterEqual(result["stream_remote_page_peak"],
                                    result["bulk_remote_page_peak"])

    def test_two_readers_same_historical_epoch_keep_last_pin(self):
        for p in (1,2,64):
            x=StreamedRemotePinBitmapF1((0,1,0),p,8)
            self.assertEqual(x.pin_current(0),0)
            self.assertEqual(x.pin_current(1),0)
            self.assertEqual(x.set(0,1),1)
            self.assertEqual(set(x.remote),{0,1})
            x.unpin(0,0)
            self.assertIn(0,x.remote)
            self.assertEqual(x.as_of(1,0,0,3),1)
            x.unpin(1,0)
            self.assertEqual(set(x.remote),{1})
            self.assertRaises(Abort,x.as_of,1,0,0,3)
            before=x.ledger["bitmap_remote_page_read_attempts"]
            x.assert_streamed_live_set()
            self.assertEqual(x.ledger["bitmap_remote_page_read_attempts"],before)
            self.assertEqual(x.ledger["bitmap_audit_remote_page_read_attempts"],
                             x.bitmap_pages)

    def test_tamper_replay_and_withhold_abort_before_client_or_anchor_change(self):
        for p in (1,2,64):
            x=StreamedRemotePinBitmapF1((0,1,1),p,8)
            original=x.remote_pin_bitmap
            self.assertEqual(x.pin_current(0),0)
            clean=x.remote_pin_bitmap
            generation=x.bitmap_generation
            digest=x.trusted_bitmap_digest
            self.assertNotEqual(original,clean)
            x.remote_pin_bitmap=original
            self.assertRaises(Abort,x.pin_current,1)
            self.assertRaises(Abort,x.unpin,0,0)
            self.assertRaises(Abort,x.set,0,1)
            self.assertEqual(x.epoch,0)
            self.assertEqual(x.bitmap_generation,generation)
            self.assertEqual(x.trusted_bitmap_digest,digest)
            self.assertEqual(set(x.readers[0]),{0})
            self.assertEqual(x.readers[1],{})
            x.remote_pin_bitmap=None
            self.assertRaises(Abort,x.pin_current,1)
            self.assertEqual(x.bitmap_generation,generation)
            x.remote_pin_bitmap=clean
            x.unpin(0,0)
            self.assertEqual(set(x.readers[0]),set())

    def test_changed_server_bitmap_between_two_passes_aborts_no_publication(self):
        class TamperAfterAuthentication(StreamedRemotePinBitmapF1):
            change_once=True
            def _stream_verify(self,epoch=None):
                result=super()._stream_verify(epoch)
                if self.change_once:
                    self.change_once=False
                    bad=bytearray(self.remote_pin_bitmap)
                    bad[0] ^= 0x80
                    self.remote_pin_bitmap=bytes(bad)
                return result
        for p in (1,2,64):
            x=TamperAfterAuthentication((0,1),p,8)
            before=x.bitmap_generation
            digest=x.trusted_bitmap_digest
            with self.assertRaises(Abort):
                x.pin_current(0)
            self.assertEqual(x.bitmap_generation,before)
            self.assertEqual(x.trusted_bitmap_digest,digest)
            self.assertEqual(x.epoch,0)
            self.assertEqual(x.readers[0],{})
            self.assertGreater(x.ledger["stream_aborted_unpublished_staging_pages"],0)
            self.assertEqual(x.ledger["bitmap_trusted_root_publications"],0)

    def test_page_accounting_exact_without_hidden_history_lookup(self):
        for p in (1,2,64):
            x=StreamedRemotePinBitmapF1((0,)*33,p,17)
            bitmap_bytes=(2*17+7)//8
            pages=(bitmap_bytes+p-1)//p
            snapshot=(5+p-1)//p + (48+p-1)//p
            self.assertEqual(x.bitmap_pages,pages)
            self.assertEqual(x._slot_start_page(0),pages)
            self.assertEqual(x.remote_pages,snapshot+pages)
            x.pin_current(0)
            self.assertEqual(x.ledger["stream_first_pass_page_reads"],pages)
            self.assertEqual(x.ledger["stream_second_pass_page_reads"],pages)
            self.assertEqual(x.ledger["bitmap_remote_page_read_attempts"],2*pages)
            self.assertEqual(x.ledger["bitmap_remote_page_writes"],pages)
            self.assertEqual(x.ledger["stream_staged_remote_bitmap_page_writes"],pages)
            self.assertEqual(x.ledger["stream_peak_extra_remote_bitmap_pages"],pages)
            self.assertGreaterEqual(x.ledger["peak_remote_pages"],
                                    snapshot+2*pages)
            x.set(0,1)
            self.assertEqual(x.ledger["stream_first_pass_page_reads"],2*pages)
            self.assertEqual(x.ledger["stream_second_pass_page_reads"],pages)
            self.assertEqual(x.ledger["bitmap_remote_page_read_attempts"],3*pages)
            self.assertEqual(x.ledger["bitmap_remote_page_writes"],pages)
            self.assertEqual(x.ledger["bitmap_remote_drop_page_calls"],0)
            x.unpin(0,0)
            self.assertEqual(x.ledger["bitmap_remote_drop_page_calls"],snapshot)
            self.assertEqual(x.ledger["bitmap_remote_drop_request_bytes"],8*snapshot)

    def test_epoch_capacity_noop_and_bad_operations(self):
        x=StreamedRemotePinBitmapF1((1,),2,4)
        self.assertEqual(x.pin_current(0),0)
        self.assertEqual(x.set(0,1),1)
        self.assertEqual(x.set(0,1),2)
        self.assertEqual(x.set(0,1),3)
        self.assertRaises(ValueError,x.set,0,0)
        self.assertRaises(ValueError,x.set,1,1)
        self.assertRaises(ValueError,x.pin_current,2)
        self.assertRaises(ValueError,x.unpin,0,3)
        self.assertEqual(x.as_of(0,0,0,1),1)


if __name__=="__main__":
    unittest.main()
