"""UCT-005 C2-B2-B independent page-COW, root publication and crash oracle."""
import unittest
from itertools import product

from uct005_g3b2b_range_tree import TreeWriter, AnchorValue
from uct005_g3b2c2b1_pin_generation import Crash, Integrity
from uct005_g3b2c2b2a_fenced_disk_gc import DiskFencedGC
from uct005_g3b2c2b2b_online_cow import OnlineCowAuthor, CUTS


def parity(bits, lo, hi):
    value=0
    for x in bits[lo:hi+1]:
        value ^= x
    return value


class OnlineCowTests(unittest.TestCase):
    def test_exhaustive_small_set_and_range_against_independent_tree(self):
        cases=0
        for n in (1,2,3,4,5,6):
            for initial in product((0,1), repeat=n):
                for position in range(n):
                    bit=(initial[position]^1)
                    obj=OnlineCowAuthor(initial,page_bytes=256)
                    ref=TreeWriter(initial)
                    try:
                        self.assertEqual(obj.trusted.epoch,0)
                        old=obj.trusted
                        obj.journal.event("PIN",0,old)
                        next_=obj.prepare(position,bit)
                        self.assertEqual(obj.trusted,old)
                        self.assertEqual(obj.epoch,0)
                        self.assertGreater(next_.node_pages,next_.previous_node_pages)
                        before_count=obj.committed_nodes
                        result=obj.publish(next_)
                        ref.set(position,bit)
                        self.assertEqual(result,ref.anchor)
                        self.assertGreater(obj.committed_nodes,before_count)
                        self.assertEqual(obj.arena.latest,result.epoch)
                        self.assertEqual(obj.query(0,0,n-1,old),parity(initial,0,n-1))
                        expected=list(initial);expected[position]=bit
                        for lo in range(n):
                            for hi in range(lo,n):
                                self.assertEqual(obj.query(result.epoch,lo,hi,result),
                                                 parity(expected,lo,hi))
                                cases+=1
                        obj.journal.event("UNPIN",0)
                        with self.assertRaises(ValueError):
                            obj.query(0,0,n-1,old)
                        self.assertEqual(obj.recover(),result)
                    finally:
                        obj.close()
        self.assertGreater(cases,1000)

    def test_two_historical_reader_pins_survive_multiple_online_sets(self):
        initial=(0,1,1,0,0,1,0)
        obj=OnlineCowAuthor(initial,page_bytes=256)
        ref=TreeWriter(initial)
        try:
            root0=obj.trusted
            obj.journal.event("PIN",0,root0)
            root1=obj.publish(obj.prepare(3,1))
            ref.set(3,1)
            self.assertEqual(root1,ref.anchor)
            obj.journal.event("PIN",1,root1)
            root2=obj.publish(obj.prepare(0,1))
            ref.set(0,1)
            self.assertEqual(root2,ref.anchor)
            self.assertEqual(obj.query(0,0,6,root0),1)
            self.assertEqual(obj.query(1,0,6,root1),0)
            self.assertEqual(obj.query(2,0,6,root2),1)
            obj.journal.event("UNPIN",0)
            with self.assertRaises(ValueError):
                obj.query(0,0,6,root0)
            self.assertEqual(obj.query(1,1,5,root1),0)
            obj.journal.event("UNPIN",1)
            self.assertEqual(obj.query(2,0,6,root2),1)
        finally:
            obj.close()

    def test_all_prepublication_crash_cuts_leave_trusted_old_root(self):
        for cut in (*[x for x in CUTS if x], "publish_before"):
            obj=OnlineCowAuthor((0,1,0,0),page_bytes=256)
            try:
                original=obj.trusted
                if cut=="publish_before":
                    stage=obj.prepare(1,0)
                    with self.assertRaises(Crash):
                        obj.publish(stage,fail_at=cut)
                else:
                    with self.assertRaises(Crash):
                        obj.prepare(1,0,fail_at=cut)
                self.assertEqual(obj.trusted,original)
                self.assertEqual(obj.recover(),original)
                self.assertEqual(obj.arena.latest,0)
                self.assertEqual(obj.committed_nodes,7)
                self.assertEqual(obj.query(0,0,3,original),1)
                new=obj.publish(obj.prepare(1,0))
                self.assertEqual(new.epoch,1)
                self.assertEqual(obj.query(1,0,3,new),0)
            finally:
                obj.close()

    def test_publish_then_lost_ack_recovers_exact_authoritative_root(self):
        for cut in ("publish","ack"):
            obj=OnlineCowAuthor((0,1,0),page_bytes=256)
            try:
                stage=obj.prepare(0,1)
                if cut=="publish":
                    with self.assertRaises(Crash):
                        obj.publish(stage,fail_at=cut)
                    self.assertEqual(obj.trusted.epoch,1)
                    with self.assertRaises(Integrity):
                        obj.query(1,0,2,obj.trusted)
                    self.assertEqual(obj.recover(),obj.trusted)
                else:
                    ack=obj.publish(stage,fail_at=cut)
                    self.assertEqual(ack.epoch,1)
                self.assertEqual(obj.query(1,0,2,obj.trusted),0)
                with self.assertRaises(Integrity):
                    obj.publish(stage)
            finally:
                obj.close()

    def test_corruption_root_meta_and_stale_anchor_fail_closed(self):
        obj=OnlineCowAuthor((0,1,0,1),page_bytes=256)
        try:
            stage=obj.prepare(2,1)
            obj.metadata.seek(256)
            page=bytearray(obj.metadata.read(256));page[8]^=1
            obj.metadata.seek(256);obj.metadata.write(page)
            with self.assertRaises(Integrity):
                obj.publish(stage)
            self.assertEqual(obj.trusted.epoch,0)
            obj.recover()
            stage=obj.prepare(2,1)
            obj.arena.roots.seek(256)
            page=bytearray(obj.arena.roots.read(256));page[0]^=1
            obj.arena.roots.seek(256);obj.arena.roots.write(page)
            with self.assertRaises(Integrity):
                obj.publish(stage)
            self.assertEqual(obj.trusted.epoch,0)
            obj.recover()
            obj.trusted=AnchorValue(1,b"\0"*32)
            with self.assertRaises(Integrity):
                obj.recover()
        finally:
            obj.close()

    def test_existing_root_image_forgery_rejected_before_any_new_publish(self):
        obj=OnlineCowAuthor((0,0,1,0),page_bytes=256)
        try:
            root,_=obj.arena._root(0)
            obj.arena.nodes.seek(root*256)
            data=bytearray(obj.arena.nodes.read(256))
            data[16]^=1  # mutate span
            obj.arena.nodes.seek(root*256);obj.arena.nodes.write(data)
            with self.assertRaises(Integrity):
                obj.prepare(0,1)
            self.assertEqual(obj.trusted.epoch,0)
            self.assertEqual(obj.io["anchor_publications"],0)
        finally:
            obj.close()

    def test_invalid_crash_name_no_side_effect_and_noop_still_new_epoch(self):
        obj=OnlineCowAuthor((1,),page_bytes=256)
        try:
            baseline=obj.counters()
            with self.assertRaises(ValueError):
                obj.prepare(0,1,fail_at="alien")
            self.assertEqual(obj.counters(),baseline)
            stage=obj.prepare(0,1)
            published=obj.publish(stage)
            self.assertEqual(published.epoch,1)
            self.assertEqual(obj.query(1,0,0,published),1)
            before=obj.counters()
            with self.assertRaises(ValueError):
                obj.publish(stage,fail_at="alien")
            self.assertEqual(obj.counters(),before)
        finally:
            obj.close()

    def test_bitmap_multiple_pages_and_exact_io_partitions(self):
        obj=OnlineCowAuthor((0,)*131,page_bytes=256)
        try:
            start=obj.committed_nodes
            self.assertGreater(start,256)
            stage=obj.prepare(100,1)
            self.assertGreater(stage.node_pages,start)
            self.assertEqual(obj.trusted.epoch,0)
            root=obj.publish(stage)
            self.assertEqual(obj.query(1,90,110,root),1)
            c=obj.counters()
            self.assertEqual(c["read_bytes"],c["page_reads"]*256)
            self.assertEqual(c["write_bytes"],c["page_writes"]*256)
            self.assertEqual(c["trusted_root_bytes"],40)
            self.assertEqual(c["anchor_publications"],1)
            self.assertGreaterEqual(c["node_writes"],8)
            self.assertGreaterEqual(c["node_fsyncs"],1)
            self.assertGreaterEqual(c["root_fsyncs"],1)
            self.assertGreaterEqual(c["meta_fsyncs"],2)
            self.assertGreaterEqual(c["bitmap_fsyncs"],1)
            self.assertGreaterEqual(c["bitmap_writes"],1)
            self.assertGreaterEqual(c["node_truncates"],1)
        finally:
            obj.close()

    def test_inflight_and_lost_ack_gc_leases_are_rejected_before_any_sweep(self):
        for cut in ("node_flush", "publish_before", "publish"):
            obj=OnlineCowAuthor((0,1,0,0),page_bytes=256)
            gc=DiskFencedGC(obj.arena,obj.journal)
            try:
                if cut=="node_flush":
                    with self.assertRaises(Crash):
                        obj.prepare(1,0,fail_at=cut)
                else:
                    staged=obj.prepare(1,0)
                    with self.assertRaises(Crash):
                        obj.publish(staged,fail_at=cut)
                for operation in (
                    lambda: gc.prepare(),
                    lambda: gc.recover(),
                    lambda: gc.query(0,0,3,AnchorValue(0,obj.journal.roots[0])),
                ):
                    with self.assertRaises(Integrity):
                        operation()
                obj.recover()
                if cut=="publish":
                    self.assertEqual(obj.trusted.epoch,1)
                    self.assertEqual(obj.query(1,0,3,obj.trusted),0)
                    with self.assertRaises(Integrity):
                        gc.prepare()
                else:
                    self.assertEqual(obj.trusted.epoch,0)
                    # Recovery of an uncommitted SET clears the writer lease
                    # so the preexisting frozen GC remains admissible.
                    staged_gc=gc.prepare()
                    gc.publish(staged_gc)
            finally:
                gc.close()
                obj.close()

    def test_online_set_invalidates_old_gc_forest_lease_and_prepared_generation(self):
        obj=OnlineCowAuthor((0,0,0,0,0,0,0,0),page_bytes=256)
        collector=DiskFencedGC(obj.arena,obj.journal)
        try:
            staged=collector.prepare()
            root=obj.publish(obj.prepare(3,1))
            self.assertEqual(root.epoch,1)
            for action in (
                lambda: collector.prepare(),
                lambda: collector.publish(staged),
                lambda: collector.recover(),
                lambda: collector.query(0,0,7,AnchorValue(0,obj.journal.roots[0])),
            ):
                with self.assertRaisesRegex(Integrity, "earlier writer/root epoch"):
                    action()
            self.assertEqual(obj.query(1,0,7,root),1)
        finally:
            collector.close()
            obj.close()


if __name__=="__main__":
    unittest.main()
