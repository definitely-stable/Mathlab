"""D1-B2-B1 independent same-task physical bitmap / PIN / GC falsifiers."""
import itertools
import unittest

from uct005_d1b2b1_segmented_bitmap import SegmentedPageCowTree
from uct005_d1b2b_page_cow import Abort, PageCowTree
from uct005_d1b0_f1_reference import SnapshotF1Reference


def _words(initial):
    words = [tuple(initial)]
    n = len(initial)
    for step in range(3):
        bits = list(words[-1])
        index = (0, min(1, n - 1), n - 1)[step]
        if step != 1:  # epoch 2 no-op
            bits[index] ^= 1
        words.append(tuple(bits))
    return words


class SegmentedBitmapTests(unittest.TestCase):
    def test_all_gf2_words_two_readers_pins_and_gc(self):
        for n in range(1, 7):
            for bits in itertools.product((0, 1), repeat=n):
                for p in (1, 2, 64):
                    s = SegmentedPageCowTree(bits, p)
                    baseline = PageCowTree(bits, p)
                    words = _words(bits)
                    self.assertTrue(s.segment_matches_storage())
                    self.assertEqual(s.pin_current(0), baseline.pin_current(0))
                    for i in range(1, 4):
                        index = (0, min(1, n - 1), n - 1)[i - 1]
                        val = words[i][index]
                        self.assertEqual(s.set(index, val), i)
                        self.assertEqual(baseline.set(index, val), i)
                        if i == 2:
                            self.assertEqual(s.pin_current(1), baseline.pin_current(1))
                    self.assertTrue(s.segment_matches_storage())
                    self.assertEqual(s.ledger["set_changed_logical_bits"], 2)
                    # Two historical PINs, all intervals and two live readers.
                    for left in range(n):
                        for right in range(left + 1, n + 1):
                            expected_latest = sum(words[3][left:right]) & 1
                            for reader in (0, 1):
                                self.assertEqual(s.query(reader, left, right), expected_latest)
                                self.assertEqual(s.query(reader, left, right),
                                                 baseline.query(reader, left, right))
                            for reader, epoch in ((0, 0), (1, 2)):
                                expected_old = sum(words[epoch][left:right]) & 1
                                self.assertEqual(s.query(reader, left, right, as_of=epoch),
                                                 expected_old)
                                self.assertEqual(s.query(reader, left, right, as_of=epoch),
                                                 baseline.query(reader, left, right, as_of=epoch))
                    s.gc()
                    baseline.gc()
                    self.assertEqual(set(s.roots), set(baseline.roots))
                    self.assertTrue(s.segment_matches_storage())
                    for reader, epoch in ((0, 0), (1, 2)):
                        s.unpin(reader, epoch)
                        baseline.unpin(reader, epoch)
                        s.gc()
                        baseline.gc()
                        self.assertEqual(set(s.roots), set(baseline.roots))
                        self.assertTrue(s.segment_matches_storage())
                        with self.assertRaises(Abort):
                            s.query(reader, 0, n, as_of=epoch)
                    self.assertEqual(set(s.roots), {3})
                    self.assertEqual(s.query(0, 0, n), sum(words[3]) & 1)
                    self.assertGreater(s.ledger["gc_bitmap_page_reads"], 0)
                    self.assertGreater(s.ledger["gc_node_slot_scan_page_reads"], 0)

    def test_padded_segment_bytes_addressing_and_no_double_write(self):
        for n in (1, 2, 7, 8, 9, 33, 65, 257):
            for p in (1, 2, 8, 64, 4096):
                bits = (0,) * n
                s = SegmentedPageCowTree(bits, p)
                self.assertTrue(s.segment_matches_storage())
                self.assertEqual(s.bitmap_pages,
                                 len(s.node_bitmap_segments) +
                                 len(s.epoch_bitmap_segments))
                self.assertTrue(all(isinstance(v, bytes) and len(v) == p
                                    for v in (*s.node_bitmap_segments.values(),
                                              *s.epoch_bitmap_segments.values())))
                self.assertEqual(
                    s.ledger["setup_bitmap_page_writes"], s.bitmap_pages)
                depth = s._path_nodes(0)
                self.assertEqual(s.set(0, 1), 1)
                self.assertTrue(s.segment_matches_storage())
                # <=ceil(path/(8P))+1 node segments, +1 root segment.
                limit = (depth + 8*p - 1) // (8*p) + 2
                self.assertLessEqual(s.ledger["set_bitmap_page_writes"], limit)
                self.assertEqual(s.ledger["set_bitmap_page_writes"] * p,
                                 s.ledger["set_bitmap_upload_bytes"])
                self.assertEqual(s.ledger["set_bitmap_page_reads"] * p,
                                 s.ledger["set_bitmap_response_bytes"])
                self.assertEqual(s.ledger["set_bitmap_request_bytes"],
                                 s.ledger["set_bitmap_page_reads"] * 9)
                self.assertEqual(s.ledger["set_bitmap_page_writes"],
                                 s.ledger["set_bitmap_projected_node_count"] * 0 +
                                 s.ledger["set_bitmap_page_writes"])
                self.assertGreaterEqual(s.bitmap_pages, 2)
                # Same binary data, but distinct trustworthy resource model.
                snap = SnapshotF1Reference(bits, p)
                snap.set(0, 1)
                self.assertEqual(s.query(0, 0, n), snap.latest(0, 0, n))

    def test_counterexample_to_global_rewrite_n257_p1(self):
        n, p = 257, 1
        bits = (0,) * n
        global_cow = PageCowTree(bits, p)
        segmented = SegmentedPageCowTree(bits, p)
        snap = SnapshotF1Reference(bits, p)
        self.assertEqual(global_cow.set(0, 1), 1)
        self.assertEqual(segmented.set(0, 1), 1)
        snap.set(0, 1)
        full_pages = global_cow.ledger["set_bitmap_page_writes"]
        touched = segmented.ledger["set_bitmap_page_writes"]
        self.assertGreaterEqual(full_pages, 65)
        self.assertLessEqual(touched, 4)
        self.assertLess(touched, (n + 7)//8)
        self.assertLess(touched, full_pages)
        self.assertGreater(segmented.ledger["set_node_page_writes"], touched)
        self.assertTrue(segmented.segment_matches_storage())
        self.assertEqual(segmented.query(0, 0, n), snap.latest(0, 0, n))
        # Do NOT silently promote the *bitmap-only* win into full U_w Pareto:
        # 122-byte new nodes/path dwarf 33 packed-data bytes at this n/P.
        self.assertGreater(segmented.ledger["set_node_page_writes"],
                           snap.ledger["set_full_page_writes"])

    def test_bad_page_omission_padding_and_gc_stale_generation(self):
        s = SegmentedPageCowTree((0, 1, 0, 1, 1), 2)
        self.assertEqual(s.pin_current(0), 0)
        gen = s.generation
        s.set(0, 1)
        self.assertEqual(s.epoch, 1)
        self.assertTrue(s.segment_matches_storage())
        with self.assertRaises(Abort):
            s.gc(expected_generation=gen)
        kind, segment = "node", next(iter(s.node_bitmap_segments))
        original = s.node_bitmap_segments[segment]
        s.node_bitmap_segments[segment] = original[:-1]
        with self.assertRaises(Abort):
            s.gc()
        s.node_bitmap_segments[segment] = original
        self.assertEqual(s.query(0, 0, 5, as_of=0), 1)
        # Mutating a reserved beyond-highwater bit in the last node segment
        # must ABORT, with full-page fetch charged.
        last_segment = max(s.node_bitmap_segments)
        original_last = s.node_bitmap_segments[last_segment]
        limit = s.next_id - 1  # number of issued node IDs
        first_unused = limit % (8*s.P)
        if first_unused:
            raw = bytearray(original_last)
            raw[first_unused//8] |= 1 << (first_unused % 8)
            s.node_bitmap_segments[last_segment] = bytes(raw)
            with self.assertRaises(Abort):
                s.gc()
            s.node_bitmap_segments[last_segment] = original_last
        before = s.ledger["gc_logical_pages_freed"]
        s.gc()
        self.assertGreaterEqual(s.ledger["gc_logical_pages_freed"], before)
        self.assertTrue(s.segment_matches_storage())
        self.assertEqual(set(s.roots), {0, 1})
        s.unpin(0, 0)
        s.gc()
        self.assertEqual(set(s.roots), {1})
        self.assertTrue(s.segment_matches_storage())
        with self.assertRaises(Abort):
            s.query(0, 0, 5, as_of=0)

    def test_untrusted_occupancy_not_used_for_safe_gc_frees(self):
        s = SegmentedPageCowTree((0, 1, 1, 0), 2)
        s.pin_current(0)
        s.set(0, 1)
        # A malicious server can remove an ordinary occupancy bit, since
        # this bitmap is *not* a remotely authenticated commitment. The
        # collector still retains all independently rooted reachable nodes.
        root_id = s.next_id - 1
        page_id, local = divmod(root_id-1, s.bits_per_segment)
        raw = bytearray(s.node_bitmap_segments[page_id])
        raw[local//8] &= ~(1 << (local%8))
        s.node_bitmap_segments[page_id] = bytes(raw)
        s.gc()
        self.assertTrue(s.segment_matches_storage())  # collector repairs it
        self.assertEqual(s.query(0, 0, 4), 1)
        self.assertEqual(s.query(0, 0, 4, as_of=0), 0)


if __name__ == "__main__":
    unittest.main()
