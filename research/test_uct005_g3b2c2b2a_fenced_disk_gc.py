"""UCT-005 C2-B2-A: independent disk reachability and ideal crash-prefix oracles."""
import unittest
from itertools import product

from uct005_g3b2b_range_tree import TreeWriter
from uct005_g3b2c2a_disk_gc import DiskGcArena, ROOT, NODE, NULL
from uct005_g3b2c2b1_pin_generation import Crash, Integrity, PinJournal
from uct005_g3b2c2b2a_fenced_disk_gc import DiskFencedGC


def fixture(initial=(0, 0, 0, 0), clients=2):
    w = TreeWriter(initial)
    w.set(0, 1)
    w.set(len(initial)-1, 1)
    arena = DiskGcArena.from_writer(w, page_bytes=256, clients=clients)
    journal = PinJournal(w.epochs, b"C2-B2-A-owner-HMAC-secret-key-32bytes!",
                         page_bytes=256, clients=clients)
    service = DiskFencedGC(arena, journal)
    return w, arena, journal, service


def reachable(arena, epoch):
    """Independent test-only, unbounded oracle; production GC never calls it."""
    root, digest = ROOT.unpack_from(arena._page(arena.roots, epoch))
    seen = set()
    queue = [root]
    while queue:
        page = queue.pop()
        if page in seen:
            continue
        seen.add(page)
        a, b, *_ = NODE.unpack_from(arena._page(arena.nodes, page))
        if a != NULL:
            queue.extend([a, b])
    return seen


def live_nodes(arena):
    result = set()
    for node in range(arena.count):
        page = arena._page(arena.alive, node // arena.page_bytes)
        if page[node % arena.page_bytes]:
            result.add(node)
    return result


def close(arena, journal, service):
    service.close()
    journal.close()
    arena.close()


class FencedDiskGcTests(unittest.TestCase):
    def test_finite_all_bits_two_historical_pins_then_release(self):
        count = 0
        for n in (2, 3, 4, 5):
            for initial in product((0, 1), repeat=n):
                w, arena, journal, gc = fixture(initial)
                try:
                    journal.event("PIN", 0, w.epochs[0])
                    journal.event("PIN", 1, w.epochs[1])
                    staged = gc.prepare()
                    self.assertEqual(staged.total_nodes, arena.count)
                    self.assertEqual(staged.collector_cost.max_collector_page_buffers, 6)
                    self.assertEqual(live_nodes(arena), set(range(arena.count)),
                                     "prepare must never mutate committed pages")
                    freed = gc.publish(staged)
                    expected = reachable(arena, 0)|reachable(arena, 1)|reachable(arena, 2)
                    self.assertEqual(live_nodes(arena), expected)
                    self.assertEqual(freed, arena.count-len(expected))
                    self.assertEqual(gc.query(0, 0, n-1, w.epochs[0]),
                                     sum(initial) % 2)
                    updated = list(initial)
                    updated[0] = 1
                    self.assertEqual(gc.query(1, 0, n-1, w.epochs[1]),
                                     sum(updated) % 2)
                    updated[-1] = 1
                    self.assertEqual(gc.query(2, 0, n-1, w.epochs[2]),
                                     sum(updated) % 2)
                    journal.event("UNPIN", 0)
                    journal.event("UNPIN", 1)
                    stage2 = gc.prepare()
                    gc.publish(stage2)
                    self.assertEqual(live_nodes(arena), reachable(arena, 2))
                    with self.assertRaises(ValueError):
                        gc.query(0, 0, n-1, w.epochs[0])
                    with self.assertRaises(ValueError):
                        journal.event("PIN", 0, w.epochs[0])
                    self.assertEqual(gc.recover(), 0)
                    count += 1
                finally:
                    close(arena, journal, gc)
        self.assertGreaterEqual(count, 60)

    def test_latest_pinned_snapshot_changed_blocks_publication(self):
        w, arena, journal, gc = fixture()
        try:
            stage = gc.prepare()
            before = live_nodes(arena)
            journal.event("PIN", 0, w.epochs[0])
            with self.assertRaises(Integrity):
                gc.publish(stage)
            self.assertEqual(gc.anchor.generation, 0)
            self.assertEqual(live_nodes(arena), before)
            self.assertEqual(gc.recover(), 0)  # discard unpublished stage
            new = gc.prepare()
            gc.publish(new)
            self.assertTrue(reachable(arena, 0) <= live_nodes(arena))
        finally:
            close(arena, journal, gc)

    def test_pins_cannot_change_into_abandoned_old_version_after_gc(self):
        w, arena, journal, gc = fixture()
        try:
            gc.publish(gc.prepare())
            with self.assertRaises(ValueError):
                journal.event("PIN", 0, w.epochs[0])
            self.assertEqual(journal.event("PIN", 0, w.epochs[2]).seq, 1)
            self.assertEqual(gc.publish(gc.prepare()), 0)
        finally:
            close(arena, journal, gc)

    def test_each_prepublication_crash_cut_never_trims_active_bitmap(self):
        for cut in ("copy", "mark", "write", "flush", "publish_before"):
            w, arena, journal, gc = fixture()
            try:
                full = set(range(arena.count))
                if cut in ("copy", "mark", "write", "flush"):
                    with self.assertRaises(Crash):
                        gc.prepare(fail_at=cut)
                else:
                    stage = gc.prepare()
                    with self.assertRaises(Crash):
                        gc.publish(stage, fail_at=cut)
                self.assertEqual(live_nodes(arena), full)
                self.assertEqual(gc.anchor.generation, 0)
                self.assertEqual(gc.recover(), 0)
                self.assertEqual(live_nodes(arena), full)
                gc.publish(gc.prepare())
                self.assertEqual(live_nodes(arena), reachable(arena, 2))
            finally:
                close(arena, journal, gc)

    def test_postpublication_cuts_are_retryable_without_liveness_loss(self):
        for cut in ("publish", "trim"):
            w, arena, journal, gc = fixture()
            try:
                journal.event("PIN", 0, w.epochs[0])
                stage = gc.prepare()
                with self.assertRaises(Crash):
                    gc.publish(stage, fail_at=cut)
                self.assertEqual(gc.anchor.generation, 1)
                saved = live_nodes(arena)
                self.assertTrue(reachable(arena, 0) <= saved)
                self.assertEqual(gc.recover(),
                                 arena.count-len(reachable(arena, 0)|reachable(arena, 2))
                                 - (arena.count-len(saved)))
                self.assertEqual(live_nodes(arena),
                                 reachable(arena, 0)|reachable(arena, 2))
                self.assertEqual(gc.recover(), 0)
                self.assertEqual(gc.query(0, 0, 3, w.epochs[0]), 0)
            finally:
                close(arena, journal, gc)

    def test_disk_generation_tampered_before_trusted_publish_fails_closed(self):
        w, arena, journal, gc = fixture()
        try:
            stage = gc.prepare()
            original = live_nodes(arena)
            gc.generations.seek(gc.page_bytes)
            raw = bytearray(gc.generations.read(gc.page_bytes))
            raw[0] ^= 1
            gc.generations.seek(gc.page_bytes)
            gc.generations.write(raw)
            with self.assertRaises(Integrity):
                gc.publish(stage)
            self.assertEqual(gc.anchor.generation, 0)
            self.assertEqual(live_nodes(arena), original)
        finally:
            close(arena, journal, gc)

    def test_committed_corrupt_metadata_rejected_before_trim(self):
        w, arena, journal, gc = fixture()
        try:
            with self.assertRaises(Crash):
                gc.publish(gc.prepare(), fail_at="publish")
            before = live_nodes(arena)
            gc.generations.seek(0)
            raw = bytearray(gc.generations.read(gc.page_bytes))
            raw[1] ^= 1
            gc.generations.seek(0)
            gc.generations.write(raw)
            with self.assertRaises(Integrity):
                gc.recover()
            self.assertEqual(live_nodes(arena), before)
        finally:
            close(arena, journal, gc)

    def test_forged_pin_journal_record_prevents_gc_deletion(self):
        w, arena, journal, gc = fixture()
        try:
            journal.event("PIN", 0, w.epochs[0])
            journal.file.seek(0)
            raw = bytearray(journal.file.read(journal.page_bytes))
            raw[32] ^= 1
            journal.file.seek(0)
            journal.file.write(raw)
            before = live_nodes(arena)
            with self.assertRaises(Integrity):
                gc.prepare()
            self.assertEqual(gc.anchor.generation, 0)
            self.assertEqual(live_nodes(arena), before)
        finally:
            close(arena, journal, gc)

    def test_byzantine_tree_child_pointer_fails_before_live_bitmap_mutation(self):
        w, arena, journal, gc = fixture()
        try:
            root, _ = ROOT.unpack_from(arena._page(arena.roots, arena.latest))
            arena.nodes.seek(root*arena.page_bytes)
            raw = bytearray(arena.nodes.read(arena.page_bytes))
            struct = __import__("struct")
            struct.pack_into("<Q", raw, 0, root)
            arena.nodes.seek(root*arena.page_bytes)
            arena.nodes.write(raw)
            before = live_nodes(arena)
            with self.assertRaises((ValueError, Integrity)):
                gc.prepare()
            self.assertEqual(live_nodes(arena), before)
            self.assertEqual(gc.anchor.generation, 0)
        finally:
            close(arena, journal, gc)

    def test_invalid_crash_cut_never_modifies_anchor_or_active_live(self):
        w, arena, journal, gc = fixture()
        try:
            before = live_nodes(arena)
            with self.assertRaises(ValueError):
                gc.prepare(fail_at="alien")
            self.assertEqual(gc.io["candidate_bitmap_writes"], 0)
            stage = gc.prepare()
            with self.assertRaises(ValueError):
                gc.publish(stage, fail_at="alien")
            with self.assertRaises(ValueError):
                gc.recover(fail_at="alien")
            self.assertEqual(gc.anchor.generation, 0)
            self.assertEqual(live_nodes(arena), before)
        finally:
            close(arena, journal, gc)

    def test_two_bitmap_file_pages_and_io_categories(self):
        w, arena, journal, gc = fixture((0,)*130)
        try:
            self.assertGreater(arena.count, 256)
            s = gc.prepare()
            self.assertGreater(gc.blocks, 1)
            freed = gc.publish(s)
            self.assertGreater(freed, 0)
            c = gc.cost()
            self.assertEqual(c["gc_explicit_page_buffers"], 6)
            self.assertEqual(c["page_reads"]*gc.page_bytes, c["read_bytes"])
            self.assertEqual(c["page_writes"]*gc.page_bytes, c["write_bytes"])
            self.assertEqual(c["trusted_gc_anchor_bytes"], 48)
            self.assertEqual(c["source_bitmap_reads"], gc.blocks)
            self.assertEqual(c["candidate_bitmap_writes"], gc.blocks)
            self.assertGreaterEqual(c["generation_page_writes"],
                                    1+gc.blocks)
            self.assertGreaterEqual(c["metadata_fsyncs"], 1)
            self.assertEqual(c["logical_trim_commands"], freed)
            self.assertEqual(gc.query(2, 0, 129, w.epochs[2]), 0)
        finally:
            close(arena, journal, gc)


if __name__ == "__main__":
    unittest.main()
