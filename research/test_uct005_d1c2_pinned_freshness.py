"""D1-C2 independent F1 Byzantine replay, PIN/GC and freshness falsifiers."""
from itertools import product
from math import ceil
import unittest

from uct005_d1b0_f1_reference import Abort, SnapshotF1Reference
from uct005_d1c2_pinned_freshness import (
    two_world_without_fresh_authority, two_reader_paid_trace,
    duplicate_PIN_authority_GC, report,
)


class OfflinePINVersusLatestFreshnessTests(unittest.TestCase):
    def test_all_small_worlds_old_PIN_replay_indistinguishable_without_anchor(self):
        for n in range(1,6):
            for bits in product((0,1),repeat=n):
                for i in range(n):
                    for P in (1,2,64):
                        with self.subTest(n=n,bits=bits,i=i,P=P):
                            z=two_world_without_fresh_authority(bits,i,P)
                            self.assertTrue(z["same_preanchor_reader_state_and_replayed_old_snapshot"])
                            self.assertNotEqual(z["old_pinned_parity"],z["new_latest_parity"])
                            self.assertTrue(z["one_common_accepted_answer_must_be_wrong_in_one_world"])
                            self.assertTrue(z["equal_worlds_any_common_randomized_output_error_at_least_half"])
                            self.assertTrue(z["latest_with_authority_rejects_old_epoch_replay"])
                            self.assertTrue(z["as_of_old_pinned_root_remains_valid"])
                            self.assertFalse(z["Byzantine_availability_proved"])
                            self.assertFalse(z["new_joint_F1_lower_proved"])
                            self.assertEqual(z["root_novelty"],"OPEN_UNPROVED")

    def test_every_small_SET_and_half_open_parity_reads_charge_anchor_and_pages(self):
        for n in range(1,5):
            for bits in product((0,1),repeat=n):
                for i in range(n):
                    for target in (0,1):
                        for P in (1,2,64):
                            with self.subTest(n=n,bits=bits,i=i,target=target,P=P):
                                z=two_reader_paid_trace(bits,i,target,P)
                                q=n*(n+1)//2
                                S=ceil(ceil(n/8)/P)+ceil(48/P)
                                self.assertEqual(z["query_ranges"],q)
                                self.assertEqual(z["epoch_after_SET"],1)
                                self.assertEqual(z["set_was_noop"],bits[i]==target)
                                self.assertEqual(z["old_PIN_anchor_reads_per_AS_OF"],0)
                                self.assertEqual(z["LATEST_anchor_reads_per_query"],1)
                                self.assertEqual(z["latest_anchor_reads_total_including_two_PIN"],2+q)
                                self.assertEqual(z["retained_remote_history_pages"],S)
                                self.assertEqual(z["live_remote_pages"],2*S)
                                self.assertEqual(z["query_full_page_reads"],3*q*S)
                                self.assertEqual(z["query_remote_payload_bytes"],3*q*(48+ceil(n/8)))
                                self.assertEqual(z["reader_and_authoritative_PIN_record_bytes"],82)
                                self.assertGreater(z["trusted_bits_including_writer_and_reader_roots"],n)
                                self.assertFalse(z["complete_cryptographic_SUNDR_or_VC_theorem_transfer"])

    def test_noop_epoch_is_fresh_root_but_does_not_alter_parity(self):
        for P in (1,2,64):
            m=SnapshotF1Reference((0,1,0),P)
            m.pin_current(0)
            old_root=m.latest_root
            old_payload=m.remote[0]
            m.set(0,0)  # mandatory no-op creates epoch1
            self.assertEqual(m.remote[1],old_payload)
            self.assertNotEqual(old_root,m.latest_root)
            before=m.ledger["anchor_read_calls"]
            self.assertEqual(m.as_of(0,0,0,3),m.latest(0,0,3))
            self.assertEqual(m.ledger["anchor_read_calls"],before+1)
            with self.assertRaises(Abort):
                m.latest(0,0,3,presented_epoch=0)

    def test_two_independent_reader_PINs_same_epoch_retained_until_last_revoke(self):
        for P in (1,2,8,64):
            z=duplicate_PIN_authority_GC(P)
            S=ceil(1/P)+ceil(48/P)
            self.assertEqual(z["distinct_old_epoch_pages_retained"],S)
            self.assertEqual(z["freed_after_first_UNPIN"],0)
            self.assertEqual(z["freed_after_second_UNPIN"],S)
            self.assertTrue(z["historic_as_of_after_last_UNPIN_aborts"])
            self.assertFalse(z["root_implies_availability"])
            self.assertEqual(z["trusted_PIN_control_full_page_writes"],4*ceil(41/P))
            self.assertGreater(z["GC_directory_full_page_reads"],0)

    def test_withheld_remote_history_forces_abort_not_unsound_acceptance(self):
        m=SnapshotF1Reference((1,0,1,1),2)
        m.pin_current(0)
        m.set(0,0)
        prior_root=m.readers[0][0]
        old=m.remote.pop(0)
        before=m.ledger["anchor_read_calls"]
        with self.assertRaises(Abort):
            m.as_of(0,0,0,4)
        self.assertEqual(m.ledger["anchor_read_calls"],before)
        self.assertEqual(m.readers[0][0],prior_root)
        self.assertEqual(m.latest(0,0,4),0)
        self.assertEqual(m.ledger["anchor_read_calls"],before+1)
        m.remote[0]=old
        self.assertEqual(m.as_of(0,0,0,4),1)

    def test_bad_parameters_do_not_get_free_ledger(self):
        for bad in (((),0,1),((0,2),0,1),((0,),1,1),((0,),0,0)):
            with self.subTest(bad=bad),self.assertRaises(ValueError):
                two_world_without_fresh_authority(*bad)
        with self.assertRaises(ValueError):
            two_reader_paid_trace((0,1),0,3,1)
        with self.assertRaises(ValueError):
            two_reader_paid_trace((0,1),0,0,0)
        with self.assertRaises(ValueError):
            duplicate_PIN_authority_GC(True)

    def test_all_evidence_labels_keep_original_root_unproved(self):
        z=report()
        self.assertEqual(z["root_novelty"],"OPEN_UNPROVED")
        self.assertFalse(z["root_nonfactorizing_theorem_proved"])
        self.assertIsNone(z["FULL_VC_2026_REDUCTION"])
        self.assertIsNone(z["full_crypto_binding_reduction"])
        self.assertIsNone(z["real_fsync_powerloss"])


if __name__=="__main__":
    unittest.main()
