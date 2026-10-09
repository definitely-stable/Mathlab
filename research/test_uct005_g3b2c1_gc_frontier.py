"""UCT-005 G3-B2-C1 independent finite GC safety and candidate audit."""
import unittest
from itertools import product
from math import ceil

from uct005_g3b2b_range_tree import Reader, checked_query
from uct005_g3b2c0_pages import FrozenPages
from uct005_g3b2c1_gc_frontier import EpochGcModel, typed_candidate_gate


def independent_nodes(root):
    stack = [root]
    while stack:
        node = stack.pop()
        yield node
        if node.right is not None:
            stack.append(node.right)
            stack.append(node.left)


def independent_pages(service, epochs):
    ledger = service.ledger
    pages = set()
    for epoch in epochs:
        pages.add(ledger.epoch_directory[epoch])
        for node in independent_nodes(ledger.writer.roots[epoch]):
            pages.add(ledger.addresses[id(node)])
    return pages


def independent_parity(bits, left, right):
    out = 0
    for i in range(left, right+1):
        out ^= bits[i]
    return out


class G3B2C1GarbageCollectionTests(unittest.TestCase):
    def test_all_small_latest_queries_safe_after_cow_collection(self):
        count = 0
        for n in (2, 3, 4):
            for initial in product((0, 1), repeat=n):
                for index in range(n):
                    for bit in (0, 1):
                        store = EpochGcModel(initial)
                        base = store.latest
                        before = store.ledger.next_page
                        store.set(index, bit)
                        latest = store.latest
                        self.assertEqual(latest, base+1)
                        live = independent_pages(store, {latest})
                        expected_garbage = set(range(store.ledger.next_page)) - live
                        cost = store.sweep(latest)
                        self.assertEqual(cost.pages_freed, len(expected_garbage))
                        self.assertEqual(cost.live_after, len(live))
                        self.assertEqual(store.resident, live)
                        self.assertEqual(cost.resident_before, store.ledger.next_page)
                        self.assertEqual(cost.allocated_page_ids,
                                         store.ledger.next_page)
                        self.assertEqual(cost.bytes_capacity_recovered,
                                         len(expected_garbage) * 4096)
                        self.assertEqual(cost.remote_read_bytes,
                                         (cost.root_mark_page_reads+
                                          cost.metadata_page_reads)*4096)
                        self.assertEqual(cost.remote_write_bytes,
                                         cost.metadata_page_writes*4096)
                        self.assertGreater(cost.metadata_page_writes, 0)
                        self.assertGreater(cost.root_mark_page_reads, 0)
                        self.assertEqual(cost.anchor_publications, 0)
                        self.assertEqual(cost.trusted_checkpoint_bytes, 40)
                        bits = list(initial)
                        bits[index] = bit
                        for a in range(n):
                            for b in range(a, n):
                                trace = store.current_query(a, b)
                                self.assertGreater(trace.remote_page_reads, 0)
                                signed, touches = store.ledger.writer.serve(latest, a, b)
                                verified = checked_query(
                                    Reader(store.ledger.writer.epochs[0]), n,
                                    a, b, signed, touches, store.ledger.writer.anchor)
                                self.assertEqual(verified.status, "ACCEPT")
                                self.assertEqual(verified.value,
                                                 independent_parity(bits, a, b))
                                count += 1
                        # Newly allocated pages do not implicitly recycle freed IDs.
                        store.set(index, 1-bit)
                        self.assertGreater(store.ledger.next_page, before)
                        next_cost = store.sweep(store.latest)
                        self.assertGreaterEqual(next_cost.allocated_page_ids,
                                                cost.allocated_page_ids)
                        self.assertEqual(store.resident,
                                         independent_pages(store, {store.latest}))
        self.assertGreater(count, 400)

    def test_pinned_historical_root_preserves_old_branch_and_asof(self):
        store = EpochGcModel((0, 0, 0, 0))
        store.pin_asof(0)
        store.set(0, 1)
        store.set(1, 1)
        store.set(2, 1)
        before = len(store.resident)
        latest = store.latest
        pinned_live = independent_pages(store, {0, latest})
        pinned_cost = store.sweep(latest)
        self.assertEqual(store.resident, pinned_live)
        self.assertEqual(pinned_cost.pinned_epochs, (0,))
        self.assertLessEqual(pinned_cost.live_after, before)
        self.assertEqual(store.historical_query(0, 0, 3).status, "ACCEPT")
        self.assertEqual(store.historical_query(0, 0, 3).value, 0)
        self.assertEqual(store.current_query(0, 3).operation, "RANGE_PARITY")
        store.release_asof(0)
        unpinned_cost = store.sweep(latest)
        self.assertGreater(unpinned_cost.pages_freed, 0)
        self.assertEqual(store.resident, independent_pages(store, {latest}))
        with self.assertRaises(ValueError):
            store.historical_query(0, 0, 3)
        with self.assertRaises(ValueError):
            store.pin_asof(0)
        # A latest-only offline reader need not retain the old remote page.
        signed, touches = store.ledger.writer.serve(latest, 0, 3)
        accepted = checked_query(Reader(store.ledger.writer.epochs[0]), 4,
                                 0, 3, signed, touches, store.ledger.writer.anchor)
        self.assertEqual((accepted.status, accepted.value), ("ACCEPT", 1))

    def test_two_historical_independent_pins_and_idempotent_sweep(self):
        store = EpochGcModel((1, 0, 1))
        store.pin_asof(0)
        store.set(2, 0)
        store.pin_asof(1)
        store.set(1, 1)
        kept = independent_pages(store, {0, 1, 2})
        charge = store.sweep(2)
        self.assertEqual(store.resident, kept)
        self.assertEqual(charge.pinned_epochs, (0, 1))
        self.assertEqual(store.historical_query(1, 0, 2).value, 1)
        self.assertEqual(store.historical_query(0, 0, 2).value, 0)
        again = store.sweep(2)
        self.assertEqual(again.pages_freed, 0)
        self.assertGreater(again.remote_read_bytes, 0)
        self.assertGreater(again.remote_write_bytes, 0)
        store.release_asof(0)
        store.sweep(2)
        self.assertEqual(store.resident, independent_pages(store, {1, 2}))
        self.assertEqual(store.historical_query(1, 0, 2).status, "ACCEPT")
        store.release_asof(1)
        store.sweep(2)
        self.assertEqual(store.resident, independent_pages(store, {2}))

    def test_epoch_validation_and_no_resurrection(self):
        store = EpochGcModel((0, 1, 0))
        with self.assertRaises(ValueError):
            store.pin_asof(-1)
        with self.assertRaises(ValueError):
            store.pin_asof(1)
        with self.assertRaises(ValueError):
            store.sweep(True)
        with self.assertRaises(ValueError):
            store.release_asof(0)
        store.set(0, 1)
        with self.assertRaises(ValueError):
            store.sweep(0)  # concurrent root publication invalidates mark
        with self.assertRaises(ValueError):
            store.sweep(2)
        store.sweep(1)
        with self.assertRaises(ValueError):
            store.pin_asof(0)
        with self.assertRaises(ValueError):
            store.historical_query(0, 0, 2)
        with self.assertRaises(ValueError):
            EpochGcModel((0, 1), FrozenPages(ram_pages=0))

    def test_bitmap_accounting_one_page_and_many_page_boundaries(self):
        # 256-byte pages have 192 payload bytes -> 1536 bitmap slots.
        small = FrozenPages(page_bytes=256, ram_pages=1)
        store = EpochGcModel((0,) * 64, small)
        store.set(0, 1)
        charge = store.sweep(1)
        expected = ceil(store.ledger.next_page/(8*small.payload_bytes))
        self.assertEqual(charge.metadata_page_reads, expected)
        self.assertEqual(charge.metadata_page_writes, expected)
        self.assertEqual(charge.remote_write_bytes, expected * 256)
        self.assertEqual(charge.ram_budget_bytes, 256)
        self.assertEqual(charge.trim_commands, charge.pages_freed)
        with self.assertRaises(ValueError):
            typed_candidate_gate(2)

    def test_candidate_gate_quantifiers_and_scope(self):
        res = typed_candidate_gate(4096)
        self.assertEqual(res["status"],
                         "EXPLICIT_FALSE_CANDIDATES_NOT_ORIGINAL_LOWER_BOUND")
        self.assertEqual(res["s_trusted_bytes"], 40)
        self.assertEqual(res["server_ram_cap_bytes"], 4096)
        candidate = res["wrong_all_query_bound"]
        self.assertEqual(candidate["claimed_min_product"], 12)
        self.assertEqual(candidate["observed_full_range_product"], 4)
        self.assertTrue(candidate["rejected"])
        self.assertTrue(res["zero_cost_gc_rejected"]["rejected"])


if __name__ == "__main__":
    unittest.main()
