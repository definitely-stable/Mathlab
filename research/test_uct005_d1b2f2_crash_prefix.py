"""Independent crash-prefix falsifiers for the F2 dual-slot PIN bitmap."""
import hashlib
import itertools
import unittest

from uct005_d1b2f2_crash_prefix import (
    all_canonical_cuts, crash_prefix, digest, framed_pages, recover,
    RecoveryAbort, DOMAIN,
)
from uct005_d1b2f2_streamed_pin_bitmap import StreamedPinBitmapF1


class F2CrashPrefixTests(unittest.TestCase):
    def test_every_stage_commit_retire_cut_for_nontrivial_c_p(self):
        for C, P in itertools.product((2, 3, 8, 17, 33, 257), (1, 2, 7, 64)):
            for reader in (0, 1):
                for epoch in (0, C - 1):
                    with self.subTest(C=C, P=P, reader=reader, epoch=epoch):
                        report = all_canonical_cuts(C, P, reader, epoch)
                        self.assertEqual(report["distinct_crash_cuts"],
                                         2 * report["bitmap_pages"] + 2)
                        self.assertFalse(report["real_powerloss_safety_proved"])

    def test_trusted_root_selects_exactly_one_slot_and_never_falls_back(self):
        C, P = 17, 2
        B = (2 * C + 7) // 8
        zero, changed = bytes(B), bytearray(B)
        changed[0] |= 1
        slots = {0: framed_pages(zero, P), 1: framed_pages(bytes(changed), P)}
        self.assertEqual(recover(slots, 0, digest(0, zero), B, P).bitmap, zero)
        self.assertEqual(recover(slots, 1, digest(1, bytes(changed)), B, P).bitmap,
                         bytes(changed))
        # Even though the other slot is intact, we MUST NOT fall back.
        del slots[1][0]
        with self.assertRaises(RecoveryAbort):
            recover(slots, 1, digest(1, bytes(changed)), B, P)
        # Trusted generation anti-rollback is an external premise.
        with self.assertRaises(RecoveryAbort):
            recover(slots, 0, digest(1, bytes(changed)), B, P)

    def test_out_of_order_transitions_falsify_crash_safe_claim(self):
        for C, P in ((8, 1), (17, 2), (33, 64)):
            for order in ("publish-first", "retire-first"):
                r = crash_prefix(C, P, 0, 0, 1, order=order)
                self.assertFalse(r["accepted"])
                self.assertFalse(r["real_powerloss_safety_proved"])

    def test_tamper_missing_and_noncanonical_padding_abort(self):
        for C, P in ((8, 1), (17, 2), (17, 64)):
            M = ((2 * C + 7) // 8 + P - 1) // P
            for attack in ("active-flip", "active-missing"):
                for cut in (0, M + 1, 2 * M + 1):
                    self.assertFalse(crash_prefix(C, P, 1, C - 1, cut,
                                                  tamper=attack)["accepted"])
            if ((2 * C + 7) // 8) % P:
                for cut in (0, M + 1):
                    self.assertFalse(crash_prefix(C, P, 1, C - 1, cut,
                                                  tamper="active-padding")[
                                                      "accepted"])

    def test_physical_page_byte_and_address_conservation(self):
        for C, P in ((8, 1), (17, 2), (33, 64)):
            M = (((2 * C + 7) // 8) + P - 1) // P
            for cut in range(2 * M + 2):
                z = crash_prefix(C, P, 1, C - 1, cut)
                self.assertEqual(z["stage_upload_bytes"],
                                 P * z["stage_page_writes"])
                self.assertEqual(z["retirement_address_bytes"],
                                 8 * z["old_slot_drop_calls"])
                self.assertEqual(z["recovery_page_reads"], M)
                self.assertEqual(z["recovery_request_bytes"], 8 * M)
                self.assertEqual(z["recovery_response_bytes"], P * M)
                self.assertEqual(z["trusted_root_publications"],
                                 int(cut > M))
                self.assertEqual(z["recovered_bitmap"],
                                 z["expected_bitmap"])

    def test_independent_streamed_final_image_matches_crash_oracle(self):
        for C, P, reader, epoch in ((8, 1, 0, 0),
                                     (17, 2, 1, 0),
                                     (257, 64, 0, 0)):
            srv = StreamedPinBitmapF1((0, 1, 0), P, C)
            self.assertEqual(srv.pin_current(reader), epoch)
            r = crash_prefix(C, P, reader, epoch,
                             2 * srv.bitmap_pages + 1)
            self.assertTrue(r["accepted"])
            # Direct untrusted physical page bytes, no call to the recovery model.
            physical = b"".join(srv.bitmap_store[k]
                                for k in range(srv.bitmap_pages))
            self.assertEqual(physical[:srv.bitmap_payload_bytes],
                             r["recovered_bitmap"])
            self.assertEqual(srv.bitmap_generation, r["trusted_generation"])
            self.assertEqual(srv.trusted_bitmap_digest,
                             digest(r["trusted_generation"], r["recovered_bitmap"]))
            self.assertEqual(srv.ledger["bitmap_stream_stage_page_writes"],
                             r["stage_page_writes"])
            self.assertEqual(srv.ledger["bitmap_stream_retired_bitmap_page_drop_calls"],
                             r["old_slot_drop_calls"])

    def test_invalid_inputs_fail_closed(self):
        with self.assertRaises(ValueError):
            crash_prefix(1, 1, 0, 0, 0)
        with self.assertRaises(ValueError):
            crash_prefix(8, 0, 0, 0, 0)
        with self.assertRaises(ValueError):
            crash_prefix(8, 1, 2, 0, 0)
        with self.assertRaises(ValueError):
            crash_prefix(8, 1, 0, 0, 1000)
        with self.assertRaises(ValueError):
            crash_prefix(8, 1, 0, 0, 1, order="unknown")
        with self.assertRaises(ValueError):
            recover({0: {}}, 0, bytes(31), 2, 1)


if __name__ == "__main__":
    unittest.main()
