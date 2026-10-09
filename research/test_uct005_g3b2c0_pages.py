"""UCT-005 G3-B2-C0: independent physical-page accounting/countermodel tests."""
from itertools import product
from math import ceil
import unittest

from uct005_g3b2b_range_tree import Reader, query_writer
from uct005_g3b2c0_pages import (
    ColdLRU, FrozenPages, TreePageLedger, crash_cuts, novelty_falsifiers,
    replica_log_page_cost, snapshot_page_cost, ORDERED_COMMIT,
)


def direct_parity(bits, left, right):
    answer = 0
    for index in range(left, right + 1):
        if bits[index]:
            answer = 1 - answer
    return answer


def reference_path_height(n, index):
    lo, hi = 0, n - 1
    height = 1
    while lo < hi:
        mid = (lo + hi) // 2
        if index <= mid:
            hi = mid
        else:
            lo = mid + 1
        height += 1
    return height


class G3B2C0PhysicalTests(unittest.TestCase):
    def test_page_slot_capacity_and_invalid_configs(self):
        layout = FrozenPages()
        self.assertEqual(layout.payload_bytes, 4032)
        self.assertEqual(layout.slots, 25)
        for bad in (
            {"page_bytes": 127}, {"page_bytes": 128},
            {"header_bytes": 4096}, {"tree_record_bytes": 0},
            {"log_record_bytes": 0}, {"root_directory_bytes": 5000},
            {"ram_pages": -1}, {"page_bytes": True},
        ):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                FrozenPages(**bad)
        self.assertEqual(FrozenPages(page_bytes=256).slots, 1)

    def test_independent_lru_fault_trace_and_strict_ram_cap(self):
        sequence = (1, 2, 1, 3, 1, 2, 3, 3, 1)
        expected = {0: 9, 1: 8, 2: 6, 3: 3}
        for cap, misses in expected.items():
            cache = ColdLRU(cap)
            for page in sequence:
                cache.touch(page)
                self.assertLessEqual(len(cache.cache), cap)
            self.assertEqual(cache.faults, misses)
            self.assertEqual(tuple(cache.accesses), sequence)
        with self.assertRaises(ValueError):
            ColdLRU(-1)
        with self.assertRaises(ValueError):
            ColdLRU(1).touch(-1)

    def test_exhaustive_small_state_writer_and_range_trace_seams(self):
        cases = 0
        for n in (2, 3, 4, 5):
            for bits in product((0, 1), repeat=n):
                for index in range(n):
                    for bit in (0, 1):
                        ledger = TreePageLedger(bits)
                        layout = ledger.layout
                        self.assertEqual(
                            ledger.setup_data_pages, ceil((2*n-1)/layout.slots))
                        self.assertEqual(ledger.setup_write_pages,
                                         ledger.setup_data_pages + 1)
                        trace = ledger.update(index, bit)
                        height = reference_path_height(n, index)
                        self.assertEqual(trace.logical_node_reads, height)
                        self.assertEqual(trace.logical_node_writes, height)
                        self.assertEqual(trace.author_sha_calls, 2*height)
                        self.assertEqual(trace.remote_page_writes,
                                         ceil(height/layout.slots) + 1)
                        self.assertEqual(trace.remote_write_bytes,
                                         trace.remote_page_writes*layout.page_bytes)
                        self.assertGreaterEqual(trace.remote_page_reads, 1)
                        self.assertLessEqual(trace.remote_page_reads, height+1)
                        self.assertEqual(trace.anchor_publication_bytes, 40)
                        self.assertEqual(trace.trusted_checkpoint_bytes, 40)
                        self.assertEqual(trace.untrusted_request_bytes, 0)
                        self.assertEqual(trace.anchor_request_bytes, 0)
                        self.assertEqual(trace.anchor_response_bytes, 0)
                        self.assertEqual(trace.server_cache_bytes_cap, 4096)
                        expected = list(bits)
                        expected[index] = bit
                        for a in range(n):
                            for b in range(a, n):
                                read = ledger.query(1, a, b)
                                actual = query_writer(
                                    ledger.writer, Reader(ledger.writer.epochs[0]),
                                    1, a, b)
                                self.assertEqual(actual.status, "ACCEPT")
                                self.assertEqual(actual.value,
                                                 direct_parity(expected, a, b))
                                self.assertEqual(read.remote_response_bytes,
                                                 actual.cost.untrusted_response_bytes)
                                self.assertEqual(read.untrusted_request_bytes,
                                                 actual.cost.untrusted_request_bytes)
                                self.assertEqual(read.trusted_checkpoint_bytes, 40)
                                self.assertEqual(read.verifier_sha_calls,
                                                 actual.cost.verifier_hash_calls)
                                self.assertEqual(read.verifier_xor_ops,
                                                 actual.cost.verifier_xor_ops)
                                self.assertEqual(read.logical_node_reads,
                                                 actual.cost.server_node_reads)
                                self.assertGreaterEqual(read.remote_page_reads, 1)
                                self.assertLessEqual(read.remote_page_reads,
                                                     read.logical_node_reads+1)
                                self.assertEqual(read.remote_page_writes, 0)
                                self.assertEqual(read.author_sha_calls, 0)
                                self.assertEqual(read.anchor_request_bytes, 1)
                                self.assertEqual(read.anchor_response_bytes, 40)
                                cases += 1
        self.assertGreater(cases, 1000)

    def test_exact_consecutive_cow_packing_across_three_epochs(self):
        ledger = TreePageLedger((0,) * 64)
        expected_pages = ledger.setup_write_pages
        self.assertEqual(expected_pages, ceil(127/25)+1)
        for i in (0, 63, 3):
            before = ledger.next_page
            trace = ledger.update(i, 1)
            self.assertEqual(trace.logical_node_writes, 7)
            self.assertEqual(trace.remote_page_writes, 2)
            self.assertEqual(trace.retained_remote_pages, before+2)
            expected_pages += 2
        self.assertEqual(ledger.next_page, expected_pages)
        for epoch in range(4):
            for a, b in ((0, 0), (3, 63), (0, 63)):
                trace = ledger.query(epoch, a, b)
                self.assertGreater(trace.remote_response_bytes, 0)
                self.assertEqual(trace.remote_page_writes, 0)
        # Old-page versions persist: there is NO unpriced GC.
        self.assertEqual(len(ledger.epoch_directory), 4)

    def test_page_placement_changes_cost_without_changing_logical_work(self):
        packed = TreePageLedger((0,) * 64, FrozenPages(page_bytes=4096))
        sparse = TreePageLedger((0,) * 64, FrozenPages(page_bytes=256))
        a, b = packed.update(0, 1), sparse.update(0, 1)
        self.assertEqual(a.logical_node_writes, b.logical_node_writes)
        self.assertEqual((a.logical_node_writes, a.remote_page_writes,
                          b.remote_page_writes), (7, 2, 8))
        self.assertNotEqual(a.remote_write_bytes, b.remote_write_bytes)
        self.assertEqual(a.anchor_publication_bytes,
                         b.anchor_publication_bytes)

    def test_snapshot_replica_full_cost_boundaries_and_staleness(self):
        p = FrozenPages()
        for n in (1, 8, 9, 512, 32256, 32257):
            s = snapshot_page_cost(n, p)
            bitmap = (n+7)//8
            pages = (bitmap+p.payload_bytes-1)//p.payload_bytes
            self.assertEqual(s["initial_data_pages"], pages)
            self.assertEqual(s["update_remote_page_reads"], pages+1)
            self.assertEqual(s["update_remote_page_writes"], pages+1)
            self.assertEqual(s["query_remote_page_reads"], pages+1)
            self.assertEqual(s["sha_input_bytes_per_set"], n)
            for k in (0, 1, 2, 7):
                r = replica_log_page_cost(n, k, p)
                self.assertEqual(r["query_remote_page_reads"],
                                 k+int(k>0))
                self.assertEqual(r["trusted_checkpoint_bytes"],
                                 40+(n+7)//8)
                self.assertEqual(r["local_update_digest_calls"], k)
                self.assertEqual(r["update_remote_page_writes"], 2)
        with self.assertRaises(ValueError):
            snapshot_page_cost(0)
        with self.assertRaises(ValueError):
            replica_log_page_cost(8, -1)

    def test_ordered_crash_cut_and_inverted_anchor_falsifier(self):
        cuts = crash_cuts()
        self.assertEqual(len(cuts), len(ORDERED_COMMIT)+1)
        self.assertTrue(all(c.safe for c in cuts))
        self.assertFalse(cuts[4].new_anchor_visible)
        self.assertTrue(cuts[5].new_anchor_visible)
        self.assertTrue(cuts[5].data_durable)
        self.assertTrue(cuts[5].directory_durable)
        self.assertTrue(cuts[1].orphaned_new_data)
        unsafe = ("PUBLISH_ANCHOR", "WRITE_DATA", "FLUSH_DATA",
                  "WRITE_DIRECTORY", "FLUSH_DIRECTORY", "ACK_COMMIT")
        self.assertFalse(crash_cuts(unsafe)[1].safe)
        wrong_barrier = ("FLUSH_DATA", "WRITE_DATA", "WRITE_DIRECTORY",
                         "FLUSH_DIRECTORY", "PUBLISH_ANCHOR", "ACK_COMMIT")
        self.assertFalse(crash_cuts(wrong_barrier)[5].safe)
        with self.assertRaises(ValueError):
            crash_cuts(("WRITE_DATA",) * 6)

    def test_falsification_first_not_a_new_theorem(self):
        witness = novelty_falsifiers(256)
        self.assertEqual(witness["slots"], 25)
        self.assertEqual(witness["tree_logical_writes"], 9)
        self.assertEqual(witness["tree_physical_page_writes"], 2)
        self.assertEqual(witness["full_range_tree_query_logical_reads"], 1)
        self.assertEqual(witness["full_range_tree_query_page_reads"], 2)
        self.assertEqual(witness["replica_zero_backlog_page_reads"], 0)
        for flag in ("candidate_page_writes_at_least_logical_writes_rejected",
                     "candidate_every_range_requires_log_pages_rejected",
                     "candidate_universal_positive_remote_query_io_rejected"):
            self.assertTrue(witness[flag])


if __name__ == "__main__":
    unittest.main()
