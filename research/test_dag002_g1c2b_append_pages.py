"""Independent exhaustive DAG reachability and physical-page ledger tests."""
import unittest

from dag002_g1c2b_append_pages import (
    PagedAppendClosure, pages_for, path_parity, direct_parent_bit,
    reachable_from_adjacency,
)


def all_dags(n):
    """Independent Cartesian product of all legal old-parent selections."""
    if n == 0:
        yield ()
        return
    for prefix in all_dags(n - 1):
        v = n - 1
        for mask in range(1 << v):
            yield prefix + (tuple(i for i in range(v) if mask & (1 << i)),)


class AppendPageTests(unittest.TestCase):
    def test_all_topological_dags_to_five_and_exact_counter_ledgers(self):
        for page_bytes in (1, 2):
            for n in range(1, 6):
                for graph in all_dags(n):
                    ref = PagedAppendClosure(page_bytes)
                    expected_reads = expected_writes = expected_ones = 0
                    expected_input_bits = 0
                    for v, pr in enumerate(graph):
                        frozen = ref.snapshot()
                        self.assertEqual(ref.append(pr), v)
                        self.assertTrue(all(ref.pages[key] == image
                                            for key, image in frozen.items()))
                        expected_reads += sum(pages_for(p, page_bytes) for p in pr)
                        expected_writes += pages_for(v, page_bytes)
                        expected_input_bits += v
                        true_ancestors = sum(1 << u for u in range(v)
                            if reachable_from_adjacency(ref.parents, u, v))
                        expected_ones += true_ancestors.bit_count()
                        self.assertEqual(ref.ledger().update_read_pages, expected_reads)
                        self.assertEqual(ref.ledger().update_write_pages, expected_writes)
                        self.assertEqual(ref.ledger().new_label_one_bits, expected_ones)
                        self.assertEqual(ref.ledger().input_parent_bits, expected_input_bits)
                        before_queries = ref.ledger().query_read_pages
                        charged = 0
                        for u in range(v + 1):
                            for target in range(v + 1):
                                self.assertEqual(ref.query(u, target),
                                                 reachable_from_adjacency(ref.parents, u, target),
                                                 (page_bytes, graph, u, target))
                                charged += int(u < target)
                        self.assertEqual(ref.ledger().query_read_pages - before_queries,
                                         charged)
                    last = ref.ledger()
                    self.assertEqual(last.update_write_bytes,
                                     last.update_write_pages * page_bytes)
                    self.assertEqual(last.update_read_bytes,
                                     last.update_read_pages * page_bytes)
                    self.assertEqual(last.query_read_bytes,
                                     last.query_read_pages * page_bytes)

    def test_antichain_parent_subset_gives_exact_2_to_n_outputs(self):
        for n in range(1, 8):
            observed = set()
            for mask in range(1 << n):
                s = PagedAppendClosure(1)
                for _ in range(n):
                    s.append(())
                frozen = s.snapshot()
                s.append(i for i in range(n) if mask & (1 << i))
                self.assertEqual({key: value for key, value in s.pages.items()
                                  if key in frozen}, frozen)
                observed.add(tuple(int(s.query(i, n)) for i in range(n)))
            self.assertEqual(len(observed), 1 << n)

    def test_nonantichain_direct_parent_not_transitive(self):
        s = PagedAppendClosure()
        for p in ((), (0,), (1,)):
            s.append(p)
        self.assertTrue(s.query(0, 2))
        self.assertFalse(direct_parent_bit(s.parents, 0, 2))

    def test_diamond_gf2_path_parity_is_not_boolean_reachability(self):
        s = PagedAppendClosure(1)
        for p in ((), (0,), (0,), (1, 2)):
            s.append(p)
        self.assertTrue(s.query(0, 3))
        self.assertEqual(path_parity(s.parents, 0, 3), 0)
        self.assertEqual(s.ledger().update_write_pages, 3)
        self.assertEqual(s.ledger().update_read_pages, 2)

    def test_old_old_queries_remain_immutable_after_new_sinks(self):
        s = PagedAppendClosure(1)
        for p in ((), (), (0,)):
            s.append(p)
        original = [[s.query(u, v) for v in range(3)] for u in range(3)]
        original_pages = s.snapshot()
        for p in ((0, 1, 2), (3,), (4, 1)):
            s.append(p)
            self.assertEqual(original,
                [[s.query(u, v) for v in range(3)] for u in range(3)])
            self.assertTrue(all(s.pages[key] == val
                                for key, val in original_pages.items()))
        self.assertFalse(original[0][1])

    def test_cross_byte_and_page_boundaries(self):
        for P in (1, 2, 4):
            s = PagedAppendClosure(P)
            for v in range(35):
                if v % 3 == 0:
                    s.append(())
                else:
                    s.append((v - 1,))
            for target in range(35):
                for u in range(35):
                    self.assertEqual(s.query(u, target),
                                     reachable_from_adjacency(s.parents, u, target))
            self.assertEqual(len(s.pages), sum(pages_for(v, P) for v in range(35)))

    def test_honest_page_io_not_authenticated(self):
        s = PagedAppendClosure(2)
        s.append(())
        s.append((0,))
        self.assertTrue(s.query(0, 1))
        s.pages[(1, 0)] = b'\0\0'
        self.assertFalse(s.query(0, 1))

    def test_invalid_inputs_and_page_sizes(self):
        for value in (0, -1, True, 1.5):
            with self.assertRaises(ValueError):
                PagedAppendClosure(value)
        for v, P in ((-1, 1), (1, 0), (1, True)):
            with self.assertRaises(ValueError):
                pages_for(v, P)
        s = PagedAppendClosure()
        with self.assertRaises(ValueError):
            s.append((0,))
        s.append(())
        for p in ((0, 0), (True,), (-1,), (1,)):
            with self.assertRaises(ValueError):
                s.append(p)
        for u, v in ((-1, 0), (0, 1), (True, 0)):
            with self.assertRaises(ValueError):
                s.query(u, v)


if __name__ == '__main__':
    unittest.main()
