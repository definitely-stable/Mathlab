"""UCT-005 C2-A independent page-file collector oracles. No production FS claims."""
from itertools import product
import unittest

from uct005_g3b2b_range_tree import TreeWriter, AnchorValue
from uct005_g3b2c2a_disk_gc import DiskGcArena


def oracle(bits, left, right):
    result = 0
    for i in range(left, right + 1):
        result ^= bits[i]
    return result


class DiskGcC2ATests(unittest.TestCase):
    def test_disk_collector_exhaustive_small_latest_and_history(self):
        scenarios = 0
        for n in (2, 3, 4):
            for initial in product((0, 1), repeat=n):
                for index in range(n):
                    for new_bit in (0, 1):
                        w = TreeWriter(initial)
                        previous = tuple(initial)
                        updated = list(initial)
                        updated[index] = new_bit
                        w.set(index, new_bit)
                        f = DiskGcArena.from_writer(w, page_bytes=256, clients=2)
                        try:
                            # Two independent reader slots, old root and latest.
                            p0 = f.pin_epoch(0, 0, w.epochs[0])
                            p1 = f.pin_epoch(1, 1, w.epochs[1])
                            self.assertEqual((p0["root_page_reads"],
                                              p1["pin_page_writes"]), (1, 1))
                            cost = f.collect(1)
                            self.assertEqual(cost.freed_nodes, 0)
                            self.assertEqual(cost.live_nodes, cost.total_nodes)
                            self.assertEqual(cost.max_collector_page_buffers, 6)
                            self.assertGreater(cost.queue_pages_read, 0)
                            self.assertGreater(cost.queue_pages_written, 0)
                            self.assertGreater(cost.bitmap_pages_read, 0)
                            self.assertGreater(cost.bitmap_pages_written, 0)
                            self.assertGreater(cost.metadata_init_writes, 0)
                            self.assertEqual(cost.page_reads,
                                             cost.queue_pages_read+
                                             cost.node_pages_read+
                                             cost.bitmap_pages_read+
                                             cost.root_pin_pages_read)
                            self.assertEqual(cost.page_writes,
                                             cost.queue_pages_written+
                                             cost.bitmap_pages_written+
                                             cost.metadata_init_writes)
                            self.assertEqual(cost.read_bytes,
                                             cost.page_reads*256)
                            self.assertEqual(cost.write_bytes,
                                             cost.page_writes*256)
                            for a in range(n):
                                for b in range(a, n):
                                    self.assertEqual(
                                        f.verify_range(0, a, b, w.epochs[0]),
                                        oracle(previous, a, b))
                                    self.assertEqual(
                                        f.verify_range(1, a, b, w.epochs[1]),
                                        oracle(updated, a, b))
                                    scenarios += 1
                            f.release(0)
                            f.release(1)
                            next_cost = f.collect(1)
                            self.assertGreaterEqual(next_cost.freed_nodes, 0)
                            self.assertEqual(f.verify_range(1, 0, n-1,
                                                            w.epochs[1]),
                                             oracle(updated, 0, n-1))
                            with self.assertRaises(ValueError):
                                f.verify_range(0, 0, n-1, w.epochs[0])
                            if next_cost.freed_nodes:
                                with self.assertRaises(ValueError):
                                    f.pin_epoch(0, 0, w.epochs[0])
                        finally:
                            f.close()
        self.assertGreater(scenarios, 500)

    def test_two_independent_historical_pins_survive_reclamation(self):
        w = TreeWriter((0, 0, 0, 0, 0, 0, 0, 0))
        w.set(0, 1)  # epoch 1
        w.set(4, 1)  # epoch 2
        w.set(2, 1)  # epoch 3
        f = DiskGcArena.from_writer(w, clients=2)
        try:
            f.pin_epoch(0, 0, w.epochs[0])
            f.pin_epoch(1, 2, w.epochs[2])
            charged = f.collect(3)
            self.assertGreater(charged.freed_nodes, 0)
            self.assertLess(charged.live_nodes, charged.total_nodes)
            self.assertEqual(f.verify_range(0, 0, 7, w.epochs[0]), 0)
            self.assertEqual(f.verify_range(2, 0, 7, w.epochs[2]), 0)
            self.assertEqual(f.verify_range(3, 0, 7, w.epochs[3]), 1)
            with self.assertRaises(ValueError):
                f.verify_range(1, 0, 7, w.epochs[1])
            f.release(0)
            f.collect(3)
            self.assertEqual(f.verify_range(2, 0, 7, w.epochs[2]), 0)
            f.release(1)
            f.collect(3)
            self.assertEqual(f.verify_range(3, 0, 7, w.epochs[3]), 1)
            with self.assertRaises(ValueError):
                f.pin_epoch(0, 2, w.epochs[2])
        finally:
            f.close()

    def test_restartable_gc_after_partial_reclaim_crash(self):
        w = TreeWriter((0,) * 16)
        for index in (0, 3, 7, 15):
            w.set(index, 1)
        f = DiskGcArena.from_writer(w, page_bytes=256, clients=1)
        try:
            with self.assertRaisesRegex(RuntimeError, "injected power-loss"):
                f.collect(w.anchor.epoch, interrupt_after_trims=1)
            # Re-running a full scan with same root/pin contract restores
            # logical progress; this is not proof of fsync/metadata durability.
            recovered = f.collect(w.anchor.epoch)
            self.assertGreater(recovered.freed_nodes, 0)
            self.assertEqual(f.verify_range(w.anchor.epoch, 0, 15, w.anchor), 0)
            self.assertEqual(f.verify_range(w.anchor.epoch, 3, 7, w.anchor), 0)
            repeat = f.collect(w.anchor.epoch)
            self.assertEqual(repeat.freed_nodes, 0)
            self.assertGreater(repeat.page_reads, 0)
            self.assertGreater(repeat.page_writes, 0)
        finally:
            f.close()

    def test_corruption_wrong_checkpoint_and_expired_epoch(self):
        w = TreeWriter((0, 1, 1, 0))
        w.set(2, 0)
        f = DiskGcArena.from_writer(w, clients=2)
        try:
            with self.assertRaises(ValueError):
                f.pin_epoch(0, 3, w.anchor)
            with self.assertRaises(ValueError):
                f.pin_epoch(-1, 1, w.anchor)
            with self.assertRaises(ValueError):
                f.pin_epoch(True, 1, w.anchor)
            wrong = AnchorValue(1, b"\0" * 32)
            with self.assertRaises(ValueError):
                f.pin_epoch(0, 1, wrong)
            with self.assertRaises(ValueError):
                f.verify_range(1, 0, 3, wrong)
            with self.assertRaises(ValueError):
                f.collect(0)
            with self.assertRaises(ValueError):
                f.collect(True)
            with self.assertRaises(ValueError):
                f.release(0)
            f.pin_epoch(0, 0, w.epochs[0])
            self.assertEqual(f.verify_range(0, 0, 3, w.epochs[0]), 0)
            # Modify one stored leaf physical page without rebuilding parent
            # commitment: conditional SHA tree verification must reject.
            f.nodes.seek(0)
            physical = bytearray(f.nodes.read(f.page_bytes))
            physical[15] ^= 1
            f.nodes.seek(0)
            f.nodes.write(physical)
            with self.assertRaises(ValueError):
                f.verify_range(1, 0, 3, w.epochs[1])
        finally:
            f.close()

    def test_gc_detects_byzantine_child_link_before_any_reclaim(self):
        w = TreeWriter((0, 1, 0, 1, 1, 0, 1, 0))
        w.set(3, 0)
        f = DiskGcArena.from_writer(w, clients=1)
        try:
            # Forging one child pointer of the latest root without changing
            # anchored digest is rejected BEFORE destructive GC sweep.
            root, digest = f._root(f.latest)
            self.assertEqual(digest, w.anchor.digest)
            f.nodes.seek(root*f.page_bytes)
            image = bytearray(f.nodes.read(f.page_bytes))
            from struct import pack_into
            pack_into("<Q", image, 0, root)  # root now points to itself
            f.nodes.seek(root*f.page_bytes)
            f.nodes.write(image)
            before = sum(
                f._page(f.alive, i).count(1)
                for i in range((f.count+f.page_bytes-1)//f.page_bytes)
            )
            with self.assertRaises(ValueError):
                f.collect(f.latest)
            after = sum(
                f._page(f.alive, i).count(1)
                for i in range((f.count+f.page_bytes-1)//f.page_bytes)
            )
            self.assertEqual(before, after)
        finally:
            f.close()

    def test_honest_setup_space_and_discrete_page_dimensions(self):
        for size in (256, 4096):
            w = TreeWriter((0,)*8)
            w.set(7, 1)
            f = DiskGcArena.from_writer(w, page_bytes=size, clients=2)
            try:
                cost = f.collect(f.latest)
                self.assertEqual(cost.page_size, size)
                self.assertEqual(cost.max_collector_page_buffers, 6)
                self.assertGreater(f.setup_page_writes, f.count)
                self.assertGreaterEqual(cost.logical_trim_commands, 1)
                self.assertEqual(cost.logical_trim_commands, cost.freed_nodes)
                self.assertEqual(cost.read_bytes % size, 0)
                self.assertEqual(cost.write_bytes % size, 0)
            finally:
                f.close()
        with self.assertRaises(ValueError):
            DiskGcArena(page_bytes=64)
        with self.assertRaises(ValueError):
            DiskGcArena(clients=0)


if __name__ == "__main__":
    unittest.main()
