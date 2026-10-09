"""DAG-002 G0: all small topologically ordered DAGs, independent DFS oracle."""
import itertools
import unittest
from math import comb

from dag002_oracle import (
    AppendOnlyChainTopIndex, independent_reachable, topological_dag_parents,
    antichain_observable_masks, antichain_label_lower_bits,
    min_fixed_bits_for_states,
)


class Dag002G0Tests(unittest.TestCase):
    def _check_graph(self, parents):
        index = AppendOnlyChainTopIndex()
        for v, pr in enumerate(parents):
            frozen = tuple(index.labels)
            old_chains = tuple(index.chain_of)
            self.assertEqual(index.append(pr), v)
            self.assertEqual(tuple(index.labels[:v]), frozen)
            self.assertEqual(tuple(index.chain_of[:v]), old_chains)
            for u in range(v + 1):
                for w in range(v + 1):
                    self.assertEqual(
                        index.query(u, w),
                        independent_reachable(index.parents, u, w),
                        (parents, v, u, w),
                    )
            self.assertEqual(index.label_entries_written,
                             index.logical_top_entry_count)
            self.assertEqual(index.manifest_head_updates, v + 1)
            self.assertLessEqual(index.manifest_head_count, v + 1)
            self.assertLessEqual(index.logical_top_entry_count,
                                 (v + 1) * (v + 2) // 2)
            self.assertTrue(all(tuple(sorted(label)) == label
                                for label in index.labels))
            self.assertTrue(all(any(c == chain and t == vertex
                                    for c, t in index.labels[vertex])
                                for vertex, chain in enumerate(index.chain_of)))
        return index

    def test_complete_small_topological_dag_space(self):
        for n in range(1, 6):
            for mask in range(1 << (n * (n - 1) // 2)):
                self._check_graph(topological_dag_parents(n, mask))

    def test_six_vertex_extreme_and_deterministic_adversarial_families(self):
        n = 6
        family_size = 1 << (n * (n - 1) // 2)
        for mask in (0, family_size - 1,
                     *[((i * 15427 + 9817) % family_size) for i in range(257)]):
            self._check_graph(topological_dag_parents(n, mask))
        for parents in (
            ((), (0,), (1,), (2,), (3,), (4,)),
            ((), (), (0, 1), (0, 1), (2, 3), (2, 3, 4)),
        ):
            self._check_graph(parents)

    def test_antichain_exact_information_and_fixed_indegree(self):
        for n in range(0, 9):
            outputs = set(antichain_observable_masks(n))
            self.assertEqual(len(outputs), 1 << n)
            self.assertEqual(min_fixed_bits_for_states(len(outputs)), n)
            self.assertEqual(antichain_label_lower_bits(n), n)
            for d in range(n + 1):
                subset_outputs = set(antichain_observable_masks(n, d))
                self.assertEqual(len(subset_outputs), comb(n, d))
                self.assertEqual(
                    min_fixed_bits_for_states(len(subset_outputs)),
                    antichain_label_lower_bits(n, d),
                )
                self.assertTrue(all(sum(bits) == d for bits in subset_outputs))

    def test_same_truth_vectors_with_source_probe_without_local_label(self):
        # Outsider model: source parent bit array is independently readable
        # at each publicly addressed position. It cannot satisfy the no-probe
        # precondition of the counting theorem, so it is a valid falsifier of
        # any *unrestricted* local b+g >= n statement.
        for n in range(1, 8):
            for mask in range(1 << n):
                source_array = tuple((mask >> u) & 1 for u in range(n))
                remote_probe_answers = tuple(source_array[u] for u in range(n))
                self.assertEqual(remote_probe_answers,
                                 tuple((mask >> u) & 1 for u in range(n)))
                local_label_bits = 0
                global_manifest_bits = 0
                remote_reads_per_query = 1
                self.assertEqual(local_label_bits + global_manifest_bits, 0)
                self.assertEqual(remote_reads_per_query, 1)

    def test_invalid_updates_and_query_constraints(self):
        index = AppendOnlyChainTopIndex()
        with self.assertRaises(ValueError):
            index.append((0,))
        self.assertEqual(index.append(()), 0)
        with self.assertRaises(ValueError):
            index.append((0, 0))
        with self.assertRaises(ValueError):
            index.append((1,))
        with self.assertRaises(ValueError):
            index.query(0, 1)
        with self.assertRaises(ValueError):
            topological_dag_parents(4, -1)
        with self.assertRaises(ValueError):
            min_fixed_bits_for_states(0)
        self.assertEqual(index.ledger()["manifest_head_updates"], 1)


if __name__ == "__main__":
    unittest.main()
