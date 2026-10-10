"""UCT-005 F3-E exact independent failure-side P-byte ledger falsifiers."""
from math import ceil
import unittest

from uct005_d1b2f3e_failure_amp import (
    compare_preverification_fault, between_pass_F2_mutation,
    post_publication_availability_attack, repeated_failed_attempts,
)


class FailureSidePageAmplificationTests(unittest.TestCase):
    def test_all_preexisting_SHA_corrupt_page_sizes_capacity_boundaries(self):
        for C in (8,17,257):
            for P in (1,2,64):
                with self.subTest(C=C,P=P):
                    row=compare_preverification_fault(
                        C=C,P=P,kind="preexisting_wrong_SHA")
                    M=ceil(ceil(2*C/8)/P)
                    self.assertEqual(row["M"],M)
                    self.assertEqual(row["two_pass"]["online_bitmap_read_attempts"],M)
                    self.assertEqual(row["one_pass"]["online_bitmap_read_attempts"],M)
                    self.assertEqual(row["two_pass"]["stage_page_writes"],0)
                    self.assertEqual(row["two_pass"]["abort_stage_drop_calls"],0)
                    self.assertEqual(row["one_pass"]["stage_page_writes"],M)
                    self.assertEqual(row["one_pass"]["abort_stage_drop_calls"],M)
                    self.assertEqual(row["additional_failure_side_full_page_upload_bytes"],M*P)
                    self.assertEqual(row["additional_failure_side_drop_address_bytes"],M*8)
                    self.assertEqual(row["one_pass"]["trusted_root_publications"],0)
                    self.assertFalse(row["one_pass"]["unpublished_stage_after_abort"])
                    self.assertEqual(row["root_novelty"],"OPEN_UNPROVED")

    def test_every_missing_bitmap_page_exact_prefix_writes_and_drops(self):
        for C,P in ((8,1),(17,1),(17,2),(257,64)):
            M=ceil(ceil(2*C/8)/P)
            for j in range(M):
                with self.subTest(C=C,P=P,j=j):
                    r=compare_preverification_fault(
                        C=C,P=P,kind="withheld_complete_page",j=j)
                    self.assertEqual(r["two_pass"]["online_bitmap_read_attempts"],j+1)
                    self.assertEqual(r["one_pass"]["online_bitmap_read_attempts"],j+1)
                    self.assertEqual(r["two_pass"]["stage_page_writes"],0)
                    self.assertEqual(r["one_pass"]["stage_page_writes"],j)
                    self.assertEqual(r["one_pass"]["abort_stage_drop_calls"],j)
                    self.assertEqual(r["one_pass"]["stage_upload_bytes"],P*j)
                    self.assertEqual(r["one_pass"]["abort_stage_drop_address_bytes"],8*j)
                    self.assertEqual(r["additional_failure_side_stage_page_writes_due_to_speculation"],j)
                    self.assertEqual(r["one_pass"]["trusted_local_reader_PIN_entries"],0)

    def test_noncanonical_padding_last_page_fault(self):
        for C,P in ((8,64),(17,2),(17,64),(257,64)):
            B=ceil(2*C/8)
            if B%P==0:
                continue
            r=compare_preverification_fault(
                C=C,P=P,kind="noncanonical_last_page_padding")
            M=ceil(B/P)
            self.assertEqual(r["two_pass"]["online_bitmap_read_attempts"],M)
            self.assertEqual(r["two_pass"]["stage_page_writes"],0)
            self.assertEqual(r["one_pass"]["stage_page_writes"],M-1)
            self.assertEqual(r["one_pass"]["abort_stage_drop_calls"],M-1)

    def test_second_pass_mutation_falsifies_F2_never_writes_on_failure(self):
        for C,P in ((8,1),(17,2),(257,64)):
            M=ceil(ceil(2*C/8)/P)
            for target in (0,M-1):
                with self.subTest(C=C,P=P,target=target):
                    r=between_pass_F2_mutation(C,P,target)
                    cost=r["F2_after_pass1_failure_cost"]
                    self.assertEqual(cost["online_bitmap_read_attempts"],2*M)
                    self.assertEqual(cost["stage_page_writes"],M)
                    self.assertEqual(cost["abort_stage_drop_calls"],M)
                    self.assertEqual(cost["stage_upload_bytes"],M*P)
                    self.assertEqual(cost["abort_stage_drop_address_bytes"],M*8)
                    self.assertEqual(cost["trusted_root_publications"],0)
                    self.assertFalse(cost["unpublished_stage_after_abort"])

    def test_postpublication_active_slot_tamper_does_not_forge_new_trusted_root(self):
        for C,P in ((8,1),(17,2),(257,64)):
            r=post_publication_availability_attack(C,P)
            for status in r["models"].values():
                self.assertTrue(status["old_trusted_root_unchanged"])
                self.assertTrue(status["pin_epoch_0_remains_trusted_to_reader"])
                self.assertTrue(status["tampered_remote_page_caused_fail_closed_next_SET"])
                self.assertEqual(status["trusted_root_publication_count"],1)
                self.assertFalse(status["availability_guarantee"])
            self.assertFalse(r["real_fsync_or_powerloss_proof"])

    def test_renewed_bad_source_can_amplify_failed_staging_arbitrarily_by_attempts(self):
        for C,P in ((17,1),(257,64)):
            M=ceil(ceil(2*C/8)/P)
            for k in (1,2,5):
                r=repeated_failed_attempts(C,P,k)
                self.assertEqual(r["full_page_speculative_uploads"],k*M)
                self.assertEqual(r["full_page_speculative_upload_bytes"],k*M*P)
                self.assertEqual(r["charged_cleanup_drop_request_bytes"],k*M*8)
                self.assertTrue(r["no_trusted_publication"])
                self.assertTrue(r["unbounded_failure_side_cost_if_attempts_are_unbounded"])

    def test_invalid_scenarios_and_resource_dimensions_abort(self):
        with self.assertRaises(ValueError):
            compare_preverification_fault(C=3,P=1,kind="preexisting_wrong_SHA")
        with self.assertRaises(ValueError):
            compare_preverification_fault(C=8,P=0,kind="preexisting_wrong_SHA")
        with self.assertRaises(ValueError):
            compare_preverification_fault(C=8,P=1,kind="withheld_complete_page",j=-1)
        with self.assertRaises(ValueError):
            compare_preverification_fault(C=8,P=1,kind="withheld_complete_page",j=200)
        with self.assertRaises(ValueError):
            compare_preverification_fault(C=8,P=1,kind="noncanonical_last_page_padding")
        with self.assertRaises(ValueError):
            compare_preverification_fault(C=8,P=1,kind="not_known")
        with self.assertRaises(ValueError):
            between_pass_F2_mutation(8,1,99)
        with self.assertRaises(ValueError):
            repeated_failed_attempts(17,1,0)


if __name__=="__main__":
    unittest.main()
