"""Independent exhaustive falsifiers for the append-DAG cross-history gate."""
import itertools
import unittest

from dag002_g1c2e_prefix_gate import (
    append_sink_truth, same_command_fiber, strict_ancestor_mask, prefix_family,
    min_local_bits_zero_update_reads, LazyAdjacencyDAG,
)


def independent_reachable(parents, u, v):
    todo, visited = [v], set()
    while todo:
        current = todo.pop()
        if current == u:
            return True
        if current not in visited:
            visited.add(current)
            todo += list(parents[current])
    return False


def graph_space(n):
    """Separate recursive family, unlike module's triangular-bit construction."""
    if n == 0:
        yield ()
    else:
        for old in graph_space(n - 1):
            for subset in itertools.product((0, 1), repeat=n - 1):
                yield old + (tuple(i for i, bit in enumerate(subset) if bit),)


class G1C2EPrefixGateTests(unittest.TestCase):
    def test_complete_small_dag_and_all_command_oracle(self):
        for n in range(1, 5):
            prefixes = list(graph_space(n))
            self.assertEqual(set(prefixes), set(prefix_family(n)))
            for parents in prefixes:
                for mask in range(1 << n):
                    chosen = tuple(i for i in range(n) if mask & (1 << i))
                    new = parents + (chosen,)
                    by_dfs = sum(1 << u for u in range(n)
                                 if independent_reachable(new, u, n))
                    self.assertEqual(append_sink_truth(parents, chosen), by_dfs)

    def test_single_latest_parent_exact_fiber_in_all_prefixes(self):
        for n in range(1, 6):
            latest = n - 1
            all_outputs = same_command_fiber(n, (latest,))
            expected = frozenset((1 << latest) | lower
                                 for lower in range(1 << latest))
            self.assertEqual(all_outputs, expected)
            self.assertEqual(min_local_bits_zero_update_reads(len(all_outputs)), n - 1)

    def test_empty_command_has_exactly_one_cross_history_output(self):
        for n in range(1, 6):
            self.assertEqual(same_command_fiber(n, ()), frozenset((0,)))
            self.assertEqual(min_local_bits_zero_update_reads(1), 0)

    def test_two_prefix_twin_impossibility_and_paid_lazy_escape(self):
        examples = (((), ()), ((), (0,)))
        observations = set()
        for prefix in examples:
            new_mask = append_sink_truth(prefix, (1,))
            observations.add(new_mask)
            store = LazyAdjacencyDAG(3)
            for parents in prefix:
                store.append(parents)
            self.assertEqual(store.append((1,)), 2)
            self.assertEqual(store.parent_input_bits, 3)
            self.assertEqual(store.update_read_records, 0)
            self.assertEqual(store.update_written_records, 3)
            self.assertEqual(store.update_written_bytes,
                             sum(4 + store.width * len(p) for p in prefix + ((1,),)))
            for u in range(3):
                self.assertEqual(store.reach(u, 2),
                                 independent_reachable(prefix + ((1,),), u, 2))
            self.assertGreater(store.query_read_records, 0)
            self.assertGreater(store.query_read_bytes, 0)
        self.assertEqual(observations, {2, 3})

    def test_lazy_adjacency_all_four_vertex_graphs(self):
        for parents in graph_space(4):
            store = LazyAdjacencyDAG(4)
            for pr in parents:
                store.append(pr)
            for u, t in itertools.product(range(4), repeat=2):
                self.assertEqual(store.reach(u, t),
                                 independent_reachable(parents, u, t))
            self.assertEqual(store.update_read_records, 0)
            self.assertEqual(store.update_written_records, 4)
            self.assertEqual(store.parent_input_bits, 6)

    def test_query_cost_varies_but_never_becomes_zero_for_nontrivial_false_query(self):
        store = LazyAdjacencyDAG(4)
        for pr in ((), (), (1,), (2,)):
            store.append(pr)
        self.assertFalse(store.reach(0, 3))
        self.assertEqual(store.query_read_records, 3)
        self.assertTrue(store.reach(1, 3))
        self.assertEqual(store.query_read_records, 5)
        self.assertEqual(store.update_read_records, 0)

    def test_validation_and_no_hidden_free_inputs(self):
        for value in (0, -1, True, 1025):
            with self.assertRaises(ValueError):
                LazyAdjacencyDAG(value)
        with self.assertRaises(ValueError):
            min_local_bits_zero_update_reads(0)
        with self.assertRaises(ValueError):
            min_local_bits_zero_update_reads(True)
        for val in (0, 6, True):
            with self.assertRaises(ValueError):
                same_command_fiber(val, ())
        x = LazyAdjacencyDAG(2)
        with self.assertRaises(ValueError):
            x.append((0,))
        x.append(())
        for bad in ((0, 0), (1,), (True,), (-1,)):
            with self.assertRaises(ValueError):
                x.append(bad)
        with self.assertRaises(ValueError):
            x.reach(0, 1)
        self.assertEqual(strict_ancestor_mask(((), (0,)), 1), 1)


if __name__ == "__main__":
    unittest.main()
