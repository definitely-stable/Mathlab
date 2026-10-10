"""Independent one-pass speculative staging adversarial and resource tests."""
from hashlib import sha256
from itertools import product
from math import ceil
import unittest

from uct005_d1b0_f1_reference import Abort
from uct005_d1b2f3c_onepass_speculative_pin import (
    OnePassStagedPinBitmapF1, same_history_onepass,
)


class OnePassSpeculativeF3CTests(unittest.TestCase):
    def test_all_gf2_initial_states_all_intervals_and_page_sizes(self):
        for n in range(1,6):
            for bits in product((0,1),repeat=n):
                for P in (1,2,64):
                    with self.subTest(n=n,P=P,bits=bits):
                        z=same_history_onepass(bits,P)
                        M=ceil(ceil(2*8/8)/P)
                        self.assertEqual(z["online_bitmap_page_reads"],
                            {"bulk":7*M,"two_pass_stream":11*M,
                             "speculative_one_pass":7*M})
                        self.assertEqual(z["onepass_saves_online_pages_vs_twopass"],4*M)
                        self.assertEqual(z["remote_page_images_at_each_stage"],
                            [3*z["S"]+M,2*z["S"]+M,z["S"]+M])
                        self.assertTrue(z["logical_two_pass_is_NOT_required_under_speculative_untrusted_staging"])
                        self.assertFalse(z["full_crash_or_powerloss_safety"])
                        self.assertFalse(z["novel_joint_lower_bound"])
                        self.assertEqual(z["root_novelty"],"OPEN_UNPROVED")

    def test_capacity_and_page_boundary_exact_cost(self):
        for n,P,C in ((1,1,8),(5,2,17),(33,1,17),(257,64,257),(2,4096,8)):
            with self.subTest(n=n,P=P,C=C):
                z=same_history_onepass(tuple(i&1 for i in range(n)),P,C)
                M=ceil(ceil(2*C/8)/P)
                S=ceil(ceil(n/8)/P)+ceil(48/P)
                self.assertEqual(z["M"],M)
                self.assertEqual(z["S"],S)
                self.assertEqual(z["onepass_speculative_full_page_writes_before_authentication"],4*M)
                self.assertEqual(z["onepass_remote_peak_page_images"],3*S+2*M)
                self.assertLessEqual(z["onepass_conceptual_payload_scratch_upper_bytes"],
                                     2*min(ceil(2*C/8),P))

    def test_failure_late_sha_mismatch_cleans_M_speculative_pages(self):
        for P,C in ((1,17),(2,17),(64,257)):
            m=OnePassStagedPinBitmapF1((0,1,0,1),P,C)
            # Malicious remote returns a wrong, complete, canonically-padded
            # active first page. All M speculative stage writes occur BEFORE
            # the single old-root digest is compared and rejected.
            old=m.bitmap_store[0]
            corrupt=bytearray(old)
            corrupt[0]^=1
            m.bitmap_store[0]=bytes(corrupt)
            orig_root=m.trusted_bitmap_digest
            orig_gen=m.bitmap_generation
            orig_pages=m.remote_pages
            with self.assertRaises(Abort):
                m.pin_current(0)
            self.assertIsNone(m.bitmap_stage)
            self.assertEqual(m.trusted_bitmap_digest,orig_root)
            self.assertEqual(m.bitmap_generation,orig_gen)
            self.assertEqual(m.remote_pages,orig_pages)
            self.assertEqual(m.readers[0],{})
            self.assertEqual(m.ledger["bitmap_remote_page_read_attempts"],m.bitmap_pages)
            self.assertEqual(m.ledger["bitmap_stream_stage_page_writes"],m.bitmap_pages)
            self.assertEqual(m.ledger["bitmap_stream_stage_abort_drop_calls"],m.bitmap_pages)
            self.assertEqual(m.ledger["bitmap_trusted_root_publications"],0)
            m.bitmap_store[0]=old
            self.assertEqual(m.pin_current(0),0)
            self.assertEqual(m.ledger["bitmap_trusted_root_publications"],1)

    def test_midway_missing_bitmap_aborts_after_paid_prefix_and_cleans(self):
        m=OnePassStagedPinBitmapF1((0,1),1,17)
        M=m.bitmap_pages
        self.assertGreaterEqual(M,2)
        old=m.bitmap_store.pop(M-1)
        root=m.trusted_bitmap_digest
        with self.assertRaises(Abort):
            m.pin_current(0)
        self.assertEqual(m.ledger["bitmap_remote_page_read_attempts"],M)
        self.assertEqual(m.ledger["bitmap_stream_stage_page_writes"],M-1)
        self.assertEqual(m.ledger["bitmap_stream_stage_abort_drop_calls"],M-1)
        self.assertEqual(m.bitmap_generation,0)
        self.assertEqual(m.trusted_bitmap_digest,root)
        self.assertIsNone(m.bitmap_stage)
        m.bitmap_store[M-1]=old
        m.pin_current(0)
        self.assertTrue(m.readers[0])

    def test_client_PIN_token_vs_authenticated_remote_bit_conflict(self):
        m=OnePassStagedPinBitmapF1((1,0,1),2,8)
        m.pin_current(0)
        oldtoken=m.readers[0][0]
        oldgen=m.bitmap_generation
        original_page=m.bitmap_store[0]
        bitmap=bytearray(original_page)
        bitmap[0] &= ~1
        m.bitmap_store[0]=bytes(bitmap)
        # Deliberate synthetic trusted-authority divergence, NOT a possible
        # untrusted attacker rewrite of SHA root. Verifies must_exist guard.
        m.trusted_bitmap_digest=sha256(
            m._DOMAIN + oldgen.to_bytes(8,"big")+
            b"".join(m.bitmap_store[i][:min(m.page_bytes,max(0,
                m.bitmap_payload_bytes-i*m.page_bytes))]
                for i in range(m.bitmap_pages))).digest()
        agreed=m.trusted_bitmap_digest
        with self.assertRaises(Abort):
            m.unpin(0,0)
        self.assertEqual(m.trusted_bitmap_digest,agreed)
        self.assertEqual(m.bitmap_generation,oldgen)
        self.assertEqual(m.readers[0][0],oldtoken)
        self.assertIsNone(m.bitmap_stage)
        self.assertEqual(m.ledger["bitmap_stream_stage_abort_drop_calls"],m.bitmap_pages)
        # Restore a coherent authority/client state for forward progress.
        m.bitmap_store[0]=original_page
        m.trusted_bitmap_digest=sha256(
            m._DOMAIN + oldgen.to_bytes(8,"big")+
            b"".join(m.bitmap_store[i][:min(m.page_bytes,max(0,
                m.bitmap_payload_bytes-i*m.page_bytes))]
                for i in range(m.bitmap_pages))).digest()
        m.unpin(0,0)
        self.assertFalse(m.readers[0])

    def test_duplicate_epoch_PIN_only_one_historical_snapshot(self):
        for P in (1,2,64):
            m=OnePassStagedPinBitmapF1((0,1,0,1),P,8)
            m.pin_current(0)
            m.pin_current(1)
            m.set(0,1)
            self.assertEqual(set(m.remote),{0,1})
            before=m.remote_pages
            m.unpin(0,0)
            self.assertEqual(before,m.remote_pages)
            m.unpin(1,0)
            self.assertEqual(set(m.remote),{1})
            self.assertEqual(m.remote_pages,before-m._pages_per_snapshot())

    def test_invalid_inputs_does_not_publish(self):
        with self.assertRaises(ValueError):
            same_history_onepass((),1)
        with self.assertRaises(ValueError):
            same_history_onepass((0,2),1)
        with self.assertRaises(ValueError):
            same_history_onepass((0,1),0)
        with self.assertRaises(ValueError):
            same_history_onepass((0,1),1,3)
        m=OnePassStagedPinBitmapF1((0,1),1,8)
        with self.assertRaises(ValueError):
            m._mutate(9,0,True)
        self.assertEqual(m.bitmap_generation,0)
        self.assertIsNone(m.bitmap_stage)


if __name__=="__main__":
    unittest.main()
