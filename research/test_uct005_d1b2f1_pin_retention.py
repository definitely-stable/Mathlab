"""Independent D1-B2-F1 shared-retention and exact GC page delta falsifiers."""
import itertools
import unittest

from uct005_d1b2f1_pin_retention import (
    CLASSIFICATION, retention_audit, exercise,
)
from uct005_d1b0_f1_reference import SnapshotF1Reference
from uct005_d1b2b_page_cow import PageCowTree, Abort as CowAbort
from uct005_d1b2b1_segmented_bitmap import SegmentedPageCowTree


class ExactPinnedRetentionTests(unittest.TestCase):
    def test_exhaustive_gf2_words_same_roots_two_pins_gc(self):
        for n in range(1, 6):
            for bits in itertools.product((0,1), repeat=n):
                for p in (1, 2, 64):
                    result = exercise(n,p,bits)
                    self.assertEqual(result["status"],CLASSIFICATION)
                    self.assertEqual(result["root_novelty"],"OPEN_UNPROVED")
                    self.assertTrue(result["same_finite_F1_answers_verified"])
                    self.assertFalse(result["completed_full_F1_pareto"])
                    self.assertEqual([m["model"] for m in result["models"]],
                                     ["PAGE001_SNAPSHOT", "GLOBAL_BITMAP_COW",
                                      "SEGMENTED_BITMAP_COW"])
                    for model in result["models"]:
                        stages=model["stages"]
                        self.assertEqual([s["stage"] for s in stages],
                                         ["PIN0_PIN2","PIN2_ONLY","LATEST_ONLY"])
                        self.assertEqual([s["offline_audit"]["distinct_pinned_epochs"]
                                          for s in stages], [[0,2],[2],[]])
                        self.assertEqual([s["offline_audit"]["active_pin_entries"]
                                          for s in stages],[2,1,0])
                        for stage in stages:
                            audit=stage["offline_audit"]
                            self.assertEqual(
                                audit["authenticated_kept_remote_pages_including_metadata"],
                                stage["after_gc_remote_pages"])
                            self.assertEqual(
                                audit["latest_only_remote_pages_including_metadata"]
                                + stage["PIN_incremental_pages"],
                                stage["after_gc_remote_pages"])
                            self.assertEqual(
                                stage["before_gc_remote_pages"] -
                                stage["after_gc_remote_pages"],
                                stage["freed_logical_remote_pages"])
                            self.assertGreater(
                                sum(audit["offline_audit_charged"].values()),0)
                            self.assertFalse(audit["online_gc_price_reused_for_audit"])
                            self.assertFalse(audit["full_F1_pinned_retained_axis_proven"])
                            self.assertGreaterEqual(stage["PIN_incremental_pages"],0)
                            self.assertGreaterEqual(audit["root_slot_pages"],1)
                        self.assertEqual(stages[-1]["PIN_incremental_pages"],0)
                        self.assertGreater(stages[0]["PIN_incremental_pages"],0)
                        self.assertGreater(stages[1]["PIN_incremental_pages"],0)

    def test_page_sizes_and_sharing(self):
        for n,p in ((1,1),(2,2),(5,64),(33,2),(257,4096)):
            x=exercise(n,p)
            s,g,t=x["models"]
            self.assertEqual(
                [v["stage"] for v in s["stages"]],
                [v["stage"] for v in g["stages"]])
            self.assertEqual(
                [v["stage"] for v in g["stages"]],
                [v["stage"] for v in t["stages"]])
            for stage in range(3):
                a=g["stages"][stage]["offline_audit"]
                b=t["stages"][stage]["offline_audit"]
                self.assertEqual(a["incremental_PIN_remote_pages_over_latest"],
                                 b["incremental_PIN_remote_pages_over_latest"])
                self.assertEqual(a["latest_reachable_COW_nodes"],
                                 b["latest_reachable_COW_nodes"])
                self.assertEqual(a["union_reachable_COW_nodes"],
                                 b["union_reachable_COW_nodes"])
                self.assertEqual(a["shared_references_elided_by_COW"],
                                 b["shared_references_elided_by_COW"])
                self.assertEqual(a["root_slot_pages"],b["root_slot_pages"])
                # Node/epoch allocation bitmap pages are not implicitly
                # attributed to PIN roots.
                self.assertEqual(
                    a["authenticated_kept_remote_pages_including_metadata"]
                    - a["bitmap_remote_pages_charged"],
                    b["authenticated_kept_remote_pages_including_metadata"]
                    - b["bitmap_remote_pages_charged"])
                self.assertEqual(a["offline_64bit_id_list_bytes_NOT_python_heap"],
                                 8*a["union_reachable_COW_nodes"])
            if n>1:
                self.assertGreater(
                    t["stages"][0]["offline_audit"]["shared_references_elided_by_COW"],0)
            if n==1:
                self.assertEqual(t["stages"][0]["offline_audit"]["shared_references_elided_by_COW"],0)

    def test_duplicate_reader_pin_same_epoch_deduplicates_remote_pages(self):
        for cls in (SnapshotF1Reference,PageCowTree,SegmentedPageCowTree):
            m=cls((0,1,1,0,1),page_bytes=2)
            e0=m.pin_current(0)
            baseline=retention_audit(m)
            self.assertEqual(e0,0)
            self.assertEqual(m.pin_current(1),0)
            duplicated=retention_audit(m)
            self.assertEqual(baseline["distinct_pinned_epochs"],[])
            self.assertEqual(duplicated["distinct_pinned_epochs"],[])
            self.assertEqual(duplicated["authenticated_kept_remote_pages_including_metadata"],
                             baseline["authenticated_kept_remote_pages_including_metadata"])
            self.assertEqual(duplicated["incremental_PIN_remote_pages_over_latest"],0)
            self.assertEqual(duplicated["active_pin_entries"],2)
            m.unpin(1,0)
            after=retention_audit(m)
            self.assertEqual(after["active_pin_entries"],1)
            self.assertEqual(after["authenticated_kept_remote_pages_including_metadata"],
                             baseline["authenticated_kept_remote_pages_including_metadata"])

    def test_abort_if_an_authenticated_pin_node_or_root_is_withheld(self):
        for cls in (PageCowTree,SegmentedPageCowTree):
            m=cls((0,1,0,1,1),page_bytes=2)
            m.pin_current(0)
            m.set(0,1)
            m.pin_current(1)
            self.assertGreater(retention_audit(m)["authenticated_kept_remote_pages_including_metadata"],0)
            root=m.roots.pop(0)
            with self.assertRaises(CowAbort):
                retention_audit(m)
            m.roots[0]=root
            target=m.next_id-1  # latest COW root node, definitely reachable
            node=m.nodes.pop(target)
            with self.assertRaises(CowAbort):
                retention_audit(m)
            m.nodes[target]=node
            raw=bytearray(node)
            raw[-1]^=1
            m.nodes[target]=bytes(raw)
            with self.assertRaises(CowAbort):
                retention_audit(m)
            m.nodes[target]=node
            self.assertGreater(retention_audit(m)["offline_audit_charged"]["retention_audit_node_page_reads"],0)

    def test_offline_audit_does_not_change_online_f1_ledgers(self):
        for cls in (SnapshotF1Reference,PageCowTree,SegmentedPageCowTree):
            m=cls((0,1,1,0),page_bytes=1)
            m.pin_current(0)
            m.set(0,1)
            before={k:v for k,v in m.ledger.items() if not k.startswith("retention_audit_")}
            x=retention_audit(m)
            after={k:v for k,v in m.ledger.items() if not k.startswith("retention_audit_")}
            self.assertEqual(before,after)
            self.assertGreater(sum(x["offline_audit_charged"].values()),0)
            self.assertIn("retention_audit",repr(x))


if __name__=="__main__":
    unittest.main()
