"""F3-B independent exact three-construction PIN pages, scratch and failures."""
import itertools
from math import ceil
import unittest

from uct005_d1b0_f1_reference import Abort
from uct005_d1b2f2_streamed_pin_bitmap import StreamedPinBitmapF1
from uct005_d1b2f3b_three_model_pareto import (
    authenticated_streamed_PIN_audit, compare_all_three, UNKNOWN,
)


class F3BJointParetoFiniteTests(unittest.TestCase):
    def test_every_small_Gf2_word_same_three_constructions(self):
        for n in range(1,6):
            for word in itertools.product((0,1),repeat=n):
                for P in (1,2,64):
                    with self.subTest(n=n,P=P,word=word):
                        z=compare_all_three(word,P)
                        self.assertTrue(z["three_models_one_frozen_logical_F1_transcript"])
                        self.assertEqual(z["root_novelty"],"OPEN_UNPROVED")
                        self.assertIsNone(z["all_axis_pareto_order"])
                        self.assertFalse(z["novel_joint_lower_bound"])
                        self.assertEqual(len(z["history_stages"]),3)
                        self.assertEqual([q["remote_PIN_epochs"] for q in z["history_stages"]],
                                         [(0,2),(2,),()])
                        self.assertTrue(all(v is None for v in z["unknown_resource_axes"].values()))

    def test_independent_4_mutation_and_3_SET_cost_formula(self):
        for P in (1,2,64):
            for C in (8,17,257):
                z=compare_all_three((1,0,0,1),P,C)
                B=ceil(2*C/8)
                M=ceil(B/P)
                S=ceil(ceil(4/8)/P)+ceil(48/P)
                self.assertEqual(z["B"],B)
                self.assertEqual(z["M"],M)
                self.assertEqual(z["known_F2_total_online_bitmap_read_pages"],11*M)
                self.assertEqual(z["known_F2_additional_online_bitmap_full_page_reads_vs_bulk"],4*M)
                self.assertEqual(z["known_F2_staged_full_page_writes"],4*M)
                self.assertEqual(z["known_F2_staged_full_page_upload_bytes"],4*M*P)
                self.assertEqual(z["known_F2_retire_address_bytes"],4*M*8)
                self.assertEqual(z["known_F2_offline_authentication_bitmap_read_pages"],3*C*M)
                self.assertEqual(z["known_F2_remote_peak_pages_with_double_slot"],3*S+2*M)
                self.assertEqual(z["known_bulk_remote_peak_pages_without_double_slot"],3*S+M)
                self.assertLessEqual(z["known_F2_conceptual_bitmap_payload_scratch_upper_bytes"],
                                     2*min(B,P))
                self.assertGreater(z["chosen_bulk_three_image_conceptual_scratch_upper_bytes"],
                                   z["known_F2_conceptual_bitmap_payload_scratch_upper_bytes"])

    def test_distinct_historical_epochs_deduplicated_independent_readers(self):
        for P in (1,2,64):
            m=StreamedPinBitmapF1((1,0,1),P,8)
            m.pin_current(0)
            m.pin_current(1)
            m.set(1,1)
            report=authenticated_streamed_PIN_audit(m)
            self.assertEqual(report["PIN_entries"],2)
            self.assertEqual(report["PIN_epochs"],(0,))
            self.assertEqual(report["extra_PIN_page_images"],m._pages_per_snapshot())
            m.unpin(0,0)
            after=authenticated_streamed_PIN_audit(m)
            self.assertEqual(after["PIN_entries"],1)
            self.assertEqual(after["extra_PIN_page_images"],report["extra_PIN_page_images"])
            m.unpin(1,0)
            self.assertEqual(authenticated_streamed_PIN_audit(m)["PIN_entries"],0)
            self.assertEqual(authenticated_streamed_PIN_audit(m)["PIN_epochs"],())

    def test_authenticated_remote_bitmap_and_snapshot_negative_falsifiers(self):
        for P in (1,2,64):
            m=StreamedPinBitmapF1((0,1,0),P,8)
            m.pin_current(0)
            m.set(0,1)
            old=m.bitmap_store[0]
            mod=bytearray(old);mod[0]^=2
            m.bitmap_store[0]=bytes(mod)
            with self.assertRaises(Abort):
                authenticated_streamed_PIN_audit(m)
            m.bitmap_store[0]=old
            saved=m.remote.pop(0)
            with self.assertRaises(Abort):
                authenticated_streamed_PIN_audit(m)
            m.remote[0]=saved
            original=m.remote_manifests[0]
            m.remote_manifests[0]=bytes(48)
            with self.assertRaises(Abort):
                authenticated_streamed_PIN_audit(m)
            m.remote_manifests[0]=original
            token=m.readers[0].pop(0)
            with self.assertRaises(Abort):
                authenticated_streamed_PIN_audit(m)
            m.readers[0][0]=token
            self.assertEqual(authenticated_streamed_PIN_audit(m)["PIN_epochs"],(0,))

    def test_all_staged_pages_are_explicit_and_no_online_audit_freebie(self):
        for P,C in ((1,8),(2,17),(64,257)):
            z=compare_all_three((0,1,0),P,C)
            M=ceil(ceil(2*C/8)/P)
            for row in z["history_stages"]:
                auth=row["stream_offline_PIN_audit"]
                self.assertFalse(auth["audit_is_free_online_operation"])
                self.assertEqual(auth["offline_PIN_scan_pages"],C*M)
                self.assertEqual(auth["offline_PIN_scan_request_address_bytes"],8*C*M)
                self.assertEqual(auth["offline_PIN_scan_full_page_response_bytes"],P*C*M)
                self.assertTrue(auth["offline_diagnostic_excluded_from_bitmap_scratch_upper"])
                self.assertEqual(
                    row["retained_remote_snapshot_pages_bulk_and_stream"],
                    (len(row["remote_PIN_epochs"])+1)*
                        (ceil(ceil(3/8)/P)+ceil(48/P))+M
                )
            self.assertEqual(z["known_F2_staged_full_page_writes"],4*M)

    def test_no_one_axis_result_may_upgrade_full_pareto(self):
        z=compare_all_three((0,1,0,0,1),2)
        self.assertGreater(z["known_F2_additional_online_bitmap_full_page_reads_vs_bulk"],0)
        self.assertGreater(z["known_F2_remote_peak_pages_with_double_slot"],
                           z["known_bulk_remote_peak_pages_without_double_slot"])
        self.assertLess(z["known_F2_conceptual_bitmap_payload_scratch_upper_bytes"],
                        z["chosen_bulk_three_image_conceptual_scratch_upper_bytes"])
        self.assertIsNone(z["all_axis_pareto_order"])
        self.assertEqual(set(z["unknown_resource_axes"]),set(UNKNOWN))
        self.assertFalse(z["real_crash_durability_proof"])

    def test_invalid_inputs_do_not_become_zero_costs(self):
        with self.assertRaises(ValueError):
            compare_all_three((),1)
        with self.assertRaises(ValueError):
            compare_all_three((0,2),1)
        with self.assertRaises(ValueError):
            compare_all_three((0,1),0)
        with self.assertRaises(ValueError):
            compare_all_three((0,1),1,3)
        with self.assertRaises(TypeError):
            authenticated_streamed_PIN_audit(object())


if __name__=="__main__":
    unittest.main()
