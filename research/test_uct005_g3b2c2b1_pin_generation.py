"""UCT-005 C2-B1: independent journal/GC crash-prefix and replay/tamper tests."""
import unittest
from itertools import product

from uct005_g3b2b_range_tree import TreeWriter, AnchorValue
from uct005_g3b2c2a_disk_gc import DiskGcArena, NODE, ROOT, NULL
from uct005_g3b2c2b1_pin_generation import (
    Crash, Integrity, PinJournal, GenerationalGC,
)


def model(n=4):
    w=TreeWriter((0,)*n)
    w.set(0,1)
    w.set(n-1,1)
    j=PinJournal(w.epochs,b"independent-owner-HMAC-secret-32!",clients=2,
                 page_bytes=256)
    g=GenerationalGC(j,{
        0:{0,1,2},
        1:{2,3,4},
        2:{3,4,5}
    },7)
    return w,j,g


def disk_oracle_roots(arena):
    """Independent old-version reachability over C2-A exported disk nodes."""
    per_epoch={}
    for epoch in range(arena.epochs):
        root,_=ROOT.unpack_from(arena._page(arena.roots,epoch))
        seen=set()
        stack=[root]
        while stack:
            idx=stack.pop()
            if idx in seen:
                continue
            seen.add(idx)
            left,right,*_=NODE.unpack_from(arena._page(arena.nodes,idx))
            if left != NULL:
                stack.extend((left,right))
        per_epoch[epoch]=seen
    return per_epoch


class PinJournalTests(unittest.TestCase):
    def test_all_pin_crash_prefixes_and_trusted_ack_boundary(self):
        for cut,expected in (("write",{}),("flush",{}),
                             ("publish",{0:0}),(None,{0:0})):
            w,j,g=model()
            try:
                if cut is None:
                    tip=j.event("PIN",0,w.epochs[0])
                    self.assertEqual(tip.seq,1)
                else:
                    with self.assertRaises(Crash):
                        j.event("PIN",0,w.epochs[0],fail_at=cut)
                self.assertEqual(j.crash_recover(),expected)
                self.assertEqual(j.tip.seq,1 if expected else 0)
                if not expected:
                    self.assertEqual(j.event("PIN",0,w.epochs[0]).seq,1)
                    self.assertEqual(j.replay(),{0:0})
            finally:
                g.close()
                j.close()

    def test_unpin_release_is_durable_or_discarded_exactly_at_fence(self):
        for cut,retained in (("write",True),("flush",True),
                             ("publish",False),(None,False)):
            w,j,g=model()
            try:
                j.event("PIN",0,w.epochs[0])
                if cut is None:
                    j.event("UNPIN",0)
                else:
                    with self.assertRaises(Crash):
                        j.event("UNPIN",0,fail_at=cut)
                recovered=j.crash_recover()
                self.assertEqual(0 in recovered,retained)
                self.assertEqual(j.tip.seq,1 if retained else 2)
            finally:
                g.close()
                j.close()

    def test_mac_sequence_replay_truncation_wrong_root_and_bad_client(self):
        w,j,g=model()
        try:
            with self.assertRaises(ValueError):
                j.event("PIN",0,AnchorValue(0,b"\0"*32))
            with self.assertRaises(ValueError):
                j.event("PIN",True,w.epochs[0])
            with self.assertRaises(ValueError):
                j.event("PIN",2,w.epochs[0])
            j.event("PIN",0,w.epochs[0])
            with self.assertRaises(ValueError):
                j.event("PIN",0,w.epochs[1])
            j.event("PIN",1,w.epochs[1])
            self.assertEqual(j.replay(),{0:0,1:1})
            first=j._read(1)
            j.file.seek(j.page_bytes)
            j.file.write(first)   # copy older valid HMAC to newer sequence
            with self.assertRaises(Integrity):
                j.crash_recover()
            j.file.seek(j.page_bytes)
            j.file.write(b"\0"*j.page_bytes)
            with self.assertRaises(Integrity):
                j.replay()
            j.file.truncate(j.page_bytes)
            with self.assertRaises(Integrity):
                j.crash_recover()
        finally:
            g.close()
            j.close()

    def test_wrong_owner_key_cannot_replay_authorized_log(self):
        w,j,g=model()
        try:
            j.event("PIN",0,w.epochs[0])
            j.key=b"different-key-cannot-replay-any-record!"
            with self.assertRaises(Integrity):
                j.replay()
        finally:
            g.close()
            j.close()


    def test_invalid_crash_cuts_are_pure_errors_even_after_valid_pin(self):
        w,j,g=model()
        try:
            original_tip=j.tip
            original_pages=j.durable_pages
            original_counts=dict(j.c.as_dict(j.page_bytes))
            with self.assertRaises(ValueError):
                j.event("PIN",0,w.epochs[0],fail_at="alien")
            self.assertEqual(j.tip,original_tip)
            self.assertEqual(j.durable_pages,original_pages)
            self.assertEqual(j.c.as_dict(j.page_bytes),original_counts)
            j.event("PIN",0,w.epochs[0])
            current_tip=j.tip
            with self.assertRaises(ValueError):
                j.event("UNPIN",0,fail_at="alien")
            self.assertEqual(j.tip,current_tip)
            self.assertEqual(j.replay(),{0:0})
        finally:
            g.close()
            j.close()

    def test_published_record_torn_or_unflushed_tail_fails_closed(self):
        w,j,g=model()
        try:
            j.event("PIN",0,w.epochs[0])
            original=j._read(1)
            # Already published record: a noncanonical partially torn page
            # may never be counted as a surviving authenticated PIN.
            j.file.seek(0)
            j.file.write(original[:j.page_bytes//2])
            j.file.write(b"X"*(j.page_bytes//2))
            with self.assertRaises(Integrity):
                j.crash_recover()
            j.file.seek(0)
            j.file.write(original)
            self.assertEqual(j.crash_recover(),{0:0})
            # A flushed but NOT yet trusted-anchored second image must be
            # disregarded after replay and replaced at the same sequence.
            with self.assertRaises(Crash):
                j.event("PIN",1,w.epochs[1],fail_at="flush")
            self.assertEqual(j.crash_recover(),{0:0})
            j.event("PIN",1,w.epochs[1])
            self.assertEqual(j.replay(),{0:0,1:1})
        finally:
            g.close()
            j.close()

class GenerationalPublishTests(unittest.TestCase):
    def test_crash_prefix_generation_before_and_after_anchor(self):
        for cut in ("write","flush","publish_before","publish","trim",None):
            w,j,g=model()
            try:
                # Keep epoch0 across GC while epoch1 is unnecessary.
                j.event("PIN",0,w.epochs[0])
                if cut in ("write","flush"):
                    with self.assertRaises(Crash):
                        g.stage(fail_at=cut)
                    self.assertEqual(g.recover(),0)
                    self.assertEqual(g.anchor.generation,0)
                    self.assertEqual(bytes(g.resident),b"\1"*7)
                    continue
                st=g.stage()
                if cut is None:
                    freed=g.publish(st)
                    self.assertEqual(freed,1)
                else:
                    with self.assertRaises(Crash):
                        g.publish(st,fail_at=cut)
                if cut=="publish_before":
                    self.assertEqual(g.anchor.generation,0)
                    self.assertEqual(g.recover(),0)
                    self.assertEqual(bytes(g.resident),b"\1"*7)
                else:
                    self.assertEqual(g.anchor.generation,1)
                    self.assertEqual(g.recover(),0 if cut in (None,"trim") else 1)
                    self.assertEqual({i for i,v in enumerate(g.resident) if v},
                                     {0,1,2,3,4,5})
            finally:
                g.close()
                j.close()

    def test_stale_snapshot_rejected_when_reader_pins_before_publication(self):
        w,j,g=model()
        try:
            st=g.stage()
            j.event("PIN",0,w.epochs[0])
            with self.assertRaises(Integrity):
                g.publish(st)
            self.assertEqual(g.anchor.generation,0)
            self.assertEqual(set(i for i,v in enumerate(g.resident) if v),
                             set(range(7)))
            fresh=g.stage()
            self.assertEqual(g.publish(fresh),1)
            self.assertEqual(j.replay(),{0:0})
            self.assertTrue(all(g.resident[i] for i in (0,1,2,3)))
        finally:
            g.close()
            j.close()

    def test_old_epoch_cannot_resurrect_after_committed_gc(self):
        w,j,g=model()
        try:
            no_pin=g.stage()
            self.assertGreater(g.publish(no_pin),0)
            with self.assertRaises(ValueError):
                j.event("PIN",0,w.epochs[0])
            self.assertEqual(j.event("PIN",0,w.epochs[2]).seq,1)
            another=g.stage()
            self.assertEqual(g.publish(another),0)
        finally:
            g.close()
            j.close()

    def test_modified_published_bitmap_fails_before_any_additional_trim(self):
        w,j,g=model()
        try:
            j.event("PIN",0,w.epochs[0])
            st=g.stage()
            with self.assertRaises(Crash):
                g.publish(st,fail_at="publish")
            before=bytes(g.resident)
            g.metadata.seek(g.page_bytes)
            page=bytearray(g.metadata.read(g.page_bytes))
            page[0]^=1
            g.metadata.seek(g.page_bytes)
            g.metadata.write(page)
            with self.assertRaises(Integrity):
                g.recover()
            self.assertEqual(bytes(g.resident),before)
        finally:
            g.close()
            j.close()

    def test_independently_recovered_pins_control_dag_node_survival(self):
        for n in (2,3,4,5):
            for initial in product((0,1),repeat=n):
                writer=TreeWriter(initial)
                writer.set(0,1)
                writer.set(n-1,0)
                arena=DiskGcArena.from_writer(writer,page_bytes=256,clients=2)
                roots=disk_oracle_roots(arena)
                j=PinJournal(writer.epochs,b"K"*32,page_bytes=256)
                g=GenerationalGC(j,roots,arena.count)
                try:
                    j.event("PIN",0,writer.epochs[0])
                    j.event("PIN",1,writer.epochs[1])
                    s=g.stage()
                    g.publish(s)
                    expected=roots[0] | roots[1] | roots[2]
                    actual={i for i,v in enumerate(g.resident) if v}
                    self.assertEqual(actual,expected)
                    # Durable release + next GC legitimately reclaims unpinned
                    # nodes but retains latest and still-pinned epoch1.
                    j.event("UNPIN",0)
                    g.publish(g.stage())
                    self.assertEqual(
                        {i for i,v in enumerate(g.resident) if v},
                        roots[1]|roots[2],
                    )
                finally:
                    g.close()
                    j.close()
                    arena.close()


    def test_unrecognized_failure_cut_does_not_publish_or_stage(self):
        w,j,g=model()
        try:
            stage_writes=g.c.page_writes
            with self.assertRaises(ValueError):
                g.stage(fail_at="alien")
            self.assertEqual(g.c.page_writes,stage_writes)
            self.assertEqual(g.metadata_durable_bytes,0)
            valid=g.stage()
            before=g.anchor
            with self.assertRaises(ValueError):
                g.publish(valid,fail_at="alien")
            self.assertEqual(g.anchor,before)
            self.assertEqual(g.c.gc_publications,0)
            with self.assertRaises(ValueError):
                g.recover(fail_at="alien")
            self.assertEqual(g.anchor,before)
            self.assertEqual(bytes(g.resident),b"\1"*7)
        finally:
            g.close()
            j.close()

    def test_staged_metadata_tamper_does_not_publish_or_reclaim(self):
        w,j,g=model()
        try:
            stage=g.stage()
            g.metadata.seek(0)
            orig=g.metadata.read(g.page_bytes)
            g.metadata.seek(0)
            g.metadata.write(b"Z"+orig[1:])
            with self.assertRaises(Integrity):
                g.publish(stage)
            self.assertEqual(g.anchor.generation,0)
            self.assertEqual(set(i for i,v in enumerate(g.resident) if v),
                             set(range(7)))
        finally:
            g.close()
            j.close()

    def test_retention_rule_even_when_old_pages_happen_to_be_shared(self):
        w,j,g=model()
        try:
            g.publish(g.stage())
            # Old e1 shares nodes with latest, but metadata refuses an old
            # version pin after a GC that did not promise its retention.
            with self.assertRaises(ValueError):
                j.event("PIN",0,w.epochs[1])
            self.assertEqual(j.event("PIN",0,w.epochs[2]).seq,1)
            self.assertEqual(j.replay(),{0:2})
            j.event("UNPIN",0)
            g.publish(g.stage())
            self.assertEqual({i for i,v in enumerate(g.resident) if v},
                             {3,4,5})
            self.assertGreater(g.c.trim_commands,0)
        finally:
            g.close()
            j.close()

if __name__=="__main__":
    unittest.main()
