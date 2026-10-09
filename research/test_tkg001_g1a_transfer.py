"""Independent finite oracles for DAG-002 ↔ TKG-001 ↔ INDEX-001 transfer."""
import itertools
import unittest

from tkg001_bitemporal import TemporalDag
from tkg001_g1a_transfer import (
    SinkAppendDAG, OldEdgeInsertionDAG, PageCost, independent_closure,
    public_parent_label, remote_membership_bitmap, append_parent_log,
    public_decode, remote_decode, log_decode,
)


class DAGTransferTests(unittest.TestCase):
    def test_every_four_vertex_dag_and_every_new_sink_parent_set(self):
        arcs = tuple(itertools.combinations(range(4), 2))
        comparisons = 0
        for mask in range(1 << len(arcs)):
            old = [arc for i, arc in enumerate(arcs) if mask & (1 << i)]
            expected_old = independent_closure(4, old)
            for choices in range(1 << 4):
                parents = [u for u in range(4) if choices & (1 << u)]
                graph = SinkAppendDAG(4, old)
                graph.append(parents)
                independent = independent_closure(5, graph.edges)
                for u in range(4):
                    for v in range(4):
                        self.assertEqual(graph.reach(u, v), expected_old[u][v])
                        self.assertEqual(independent[u][v], expected_old[u][v])
                        comparisons += 1
                for u in range(5):
                    for v in range(5):
                        self.assertEqual(graph.reach(u, v), independent[u][v])
        self.assertEqual(comparisons, 64 * 16 * 16)

    def test_existing_edge_insertion_changes_old_old_answer(self):
        edge_dag = OldEdgeInsertionDAG(3)
        self.assertFalse(edge_dag.reach(0, 2))
        edge_dag.insert(0, 1)
        edge_dag.insert(1, 2)
        self.assertTrue(edge_dag.reach(0, 2))
        self.assertEqual(independent_closure(3, edge_dag.edges)[0][2], True)
        with self.assertRaises(ValueError):
            edge_dag.insert(2, 0)

    def test_three_same_answer_contracts_every_parent_subset(self):
        observations = 0
        for n in range(1, 9):
            for mask in range(1 << n):
                parents = {u for u in range(n) if mask & (1 << u)}
                p = public_parent_label(n, parents, 1)
                r = remote_membership_bitmap(n, parents, 1)
                l = append_parent_log(n, parents, 1)
                self.assertEqual((p.client_label_bits, p.manifest_bits), (n, 0))
                self.assertEqual((r.client_label_bits, r.remote_payload_bits), (0, n))
                self.assertEqual((p.write_page_images, r.write_page_images),
                                 ((n + 7) // 8, (n + 7) // 8))
                self.assertEqual((p.worst_query_page_reads, r.worst_query_page_reads),
                                 (0, 1))
                self.assertEqual((l.write_page_images, l.worst_query_page_reads),
                                 (len(parents) + 1, len(parents) + 1))
                for u in range(n):
                    truth = u in parents
                    self.assertEqual(public_decode(n, parents, u), truth)
                    self.assertEqual(remote_decode(n, parents, u), truth)
                    self.assertEqual(log_decode(n, parents, u), truth)
                    observations += 1
        self.assertGreater(observations, 1000)

    def test_false_entropy_transfer_to_just_one_remote_probe(self):
        n = 65
        remote = remote_membership_bitmap(n, {0, 64}, page_bytes=1)
        self.assertEqual(remote.client_label_bits + remote.manifest_bits, 0)
        self.assertEqual(remote.worst_query_page_reads, 1)
        self.assertEqual(remote.remote_payload_bits, 65)
        self.assertEqual(remote.write_page_images, 9)
        # b + g + q*w = 8 < 65 is NOT a universal lower bound:
        # the n separate queries use independently addressed remote cells.
        self.assertLess(0 + 0 + remote.worst_query_page_reads * 8, n)
        self.assertEqual(public_parent_label(n, {0, 64}, 1).client_label_bits, 65)
        self.assertEqual(append_parent_log(n, {0, 64}, 1).worst_query_page_reads, 3)

    def test_invalid_cost_models_and_inputs(self):
        for call in (
            lambda: remote_membership_bitmap(4, (0, 0), 1),
            lambda: public_parent_label(4, (4,), 1),
            lambda: append_parent_log(4, (0,), 0),
            lambda: append_parent_log(257, (256,), 1),
            lambda: append_parent_log(256, range(256), 1),
            lambda: public_decode(3, {0}, 3),
            lambda: SinkAppendDAG(3, ((2, 1),)),
        ):
            with self.assertRaises(ValueError):
                call()

    def test_bitemporal_old_old_answers_retract_and_backdate(self):
        # Existing-vertex edge assertion changes past world-valid answer at
        # later transaction epoch. This operation is FORBIDDEN in sink-append.
        model = TemporalDag()
        first = model.add("a", 0, 1, 0, 12)
        self.assertFalse(model.witnesses(0, 2, first, 3))
        second = model.add("late", 1, 2, -10, 5)
        self.assertEqual(model.witnesses(0, 2, second, 3), [("a", "late")])
        self.assertEqual(model.witnesses(0, 2, first, 3), [])
        third = model.retract("late")
        self.assertEqual(model.witnesses(0, 2, third, 3), [])
        self.assertEqual(model.witnesses(0, 2, second, 3), [("a", "late")])
        # A positive locally checked path is not a negative completeness
        # certificate and says nothing about globally latest signed epoch.

if __name__ == "__main__":
    unittest.main()
