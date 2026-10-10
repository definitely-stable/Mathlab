"""Independent finite F3-A dual-model priced PIN retention oracle."""
import itertools
from math import ceil
import unittest

from uct005_d1b0_f1_reference import Abort
from uct005_d1b2d_remote_pin_bitmap import RemotePinBitmapF1
from uct005_d1b2b1_segmented_bitmap import SegmentedPageCowTree
from uct005_d1b2f1_pin_retention import retention_audit, _path_coordinates
from uct005_d1b2f3a_joint_retention import (
    bulk_authenticated_retention_audit, compare_joint_trace, UNKNOWN_AXES,
)


class JointRetentionF3Tests(unittest.TestCase):
    def test_every_binary_word_and_exact_identical_f1_history(self):
        for n in range(1, 6):
            for bits in itertools.product((0,1), repeat=n):
                for P in (1,2,64):
                    with self.subTest(n=n,bits=bits,P=P):
                        r=compare_joint_trace(bits,P)
                        self.assertEqual(r["root_novelty"],"OPEN_UNPROVED")
                        self.assertTrue(r["same_three_SET_noop_PIN_and_all_applicable_range_answers"])
                        self.assertEqual(r["query_profile"],"all_intervals")
                        self.assertIsNone(r["strict_Pareto_dominance"])
                        self.assertFalse(r["new_joint_lower_bound"])
                        self.assertEqual([z["stage"] for z in r["stages"]],
                                         ["PIN0_PIN2","PIN2_ONLY","LATEST_ONLY"])
                        self.assertEqual([z["PIN_epochs"] for z in r["stages"]],
                                         [(0,2),(2,),()])
                        self.assertTrue(all(v is None for v in r["resource_vector"].values()))
                        self.assertEqual(set(r["resource_vector"]),set(UNKNOWN_AXES))
                        for z in r["stages"]:
                            self.assertGreater(z["bulk_offline_audit"]["bitmap_verified_page_reads"],0)
                            self.assertGreater(z["cow_offline_audit"]["retention_audit_node_page_reads"],0)
                            self.assertGreaterEqual(z["cow_PIN_extra_pages"],0)
                            self.assertGreaterEqual(z["bulk_PIN_extra_pages"],0)

    def test_direct_independent_snapshot_page_formula(self):
        for n,P,C in ((1,1,8),(5,2,8),(33,2,17),(257,64,257)):
            bits=tuple(i&1 for i in range(n))
            rows=compare_joint_trace(bits,P,C)["stages"]
            snapshot_pages=ceil(ceil(n/8)/P)+ceil(48/P)
            bitmap_pages=ceil(ceil(2*C/8)/P)
            for row, k in zip(rows,(2,1,0)):
                self.assertEqual(row["bulk_PIN_extra_pages"],k*snapshot_pages)
                self.assertEqual(row["bulk_live_remote_pages"],
                                 (k+1)*snapshot_pages+bitmap_pages)
                self.assertEqual(row["bulk_bitmap_pages"],bitmap_pages)

    def test_independent_three_update_checkpoint_path_union(self):
        for n in (1,2,3,5,33,257):
            row=compare_joint_trace(tuple(i&1 for i in range(n)),64)["stages"]
            x0,x1,x2=(0,min(n-1,1),n-1)
            p0,p1,p2=(_path_coordinates(n,x) for x in (x0,x1,x2))
            self.assertEqual(row[0]["cow_extra_historical_node_IDs"],
                             len(p0|p1)+len(p2))
            self.assertEqual(row[1]["cow_extra_historical_node_IDs"],len(p2))
            self.assertEqual(row[2]["cow_extra_historical_node_IDs"],0)

    def test_remote_PIN_is_not_the_empty_trusted_registry(self):
        m=RemotePinBitmapF1((0,1,1,0),page_bytes=2,epoch_capacity=8)
        self.assertEqual(m.pin_registry,{})
        m.pin_current(0)
        m.set(0,1)
        snap=bulk_authenticated_retention_audit(m)
        self.assertEqual(snap["distinct_PIN_epochs"],(0,))
        self.assertEqual(snap["PIN_entries"],1)
        self.assertGreater(snap["PIN_incremental_pages"],0)
        self.assertEqual(snap["authenticated_kept_pages"],m.remote_pages)
        self.assertTrue(snap["offline_audit_not_online_cost"])

    def test_same_epoch_two_reader_PINs_share_one_snapshot(self):
        for P in (1,2,64):
            m=RemotePinBitmapF1((1,0,1),P,8)
            m.pin_current(0)
            m.pin_current(1)
            m.set(0,0)
            z=bulk_authenticated_retention_audit(m)
            self.assertEqual(z["PIN_entries"],2)
            self.assertEqual(z["distinct_PIN_epochs"],(0,))
            m.unpin(0,0)
            z2=bulk_authenticated_retention_audit(m)
            self.assertEqual(z2["PIN_entries"],1)
            self.assertEqual(z2["PIN_incremental_pages"],z["PIN_incremental_pages"])
            m.unpin(1,0)
            self.assertEqual(bulk_authenticated_retention_audit(m)["PIN_incremental_pages"],0)

    def test_byzantine_corruption_and_pin_divergence_abort(self):
        m=RemotePinBitmapF1((0,1,0),1,8)
        m.pin_current(0)
        m.set(0,1)
        saved=m.remote_pin_bitmap
        b=bytearray(saved)
        b[0]^=1
        m.remote_pin_bitmap=bytes(b)
        with self.assertRaises(Abort):
            bulk_authenticated_retention_audit(m)
        m.remote_pin_bitmap=saved
        original=m.remote.pop(0)
        with self.assertRaises(Abort):
            bulk_authenticated_retention_audit(m)
        m.remote[0]=original
        old=m.remote_manifests[0]
        m.remote_manifests[0]=bytes(48)
        with self.assertRaises(Abort):
            bulk_authenticated_retention_audit(m)
        m.remote_manifests[0]=old
        token=m.readers[0].pop(0)
        with self.assertRaises(Abort):
            bulk_authenticated_retention_audit(m)
        m.readers[0][0]=token
        self.assertEqual(bulk_authenticated_retention_audit(m)["distinct_PIN_epochs"],(0,))

    def test_audit_does_not_invent_zero_cost_or_modify_normal_ledger(self):
        m=RemotePinBitmapF1((0,1,0,1),2,8)
        m.pin_current(0)
        m.set(0,1)
        before={k:v for k,v in m.ledger.items() if not k.startswith("bitmap_audit_")}
        z=bulk_authenticated_retention_audit(m)
        after={k:v for k,v in m.ledger.items() if not k.startswith("bitmap_audit_")}
        self.assertEqual(before,after)
        self.assertEqual(z["paid_OFFLINE_audit"]["bitmap_verified_full_response_bytes"],
                         m.bitmap_pages*m.page_bytes)
        self.assertEqual(z["paid_OFFLINE_audit"]["snapshot_verified_full_response_bytes"],
                         2*m._pages_per_snapshot()*m.page_bytes)
        self.assertEqual(z["paid_OFFLINE_audit"]["bitmap_trusted_root_reads"],1)

    def test_fail_closed_inputs_and_scope(self):
        with self.assertRaises(ValueError):
            compare_joint_trace((),1)
        with self.assertRaises(ValueError):
            compare_joint_trace((0,2),1)
        with self.assertRaises(ValueError):
            compare_joint_trace((0,1),0)
        with self.assertRaises(ValueError):
            compare_joint_trace((0,1),1,3)
        with self.assertRaises(TypeError):
            bulk_authenticated_retention_audit(SegmentedPageCowTree((0,1),2))


if __name__=="__main__":
    unittest.main()
