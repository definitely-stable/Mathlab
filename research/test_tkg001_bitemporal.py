"""TKG-001: independent batch path enumeration and adversarial evidence tests."""

import itertools
import unittest

from tkg001_bitemporal import TemporalDag, diamond


def independent_batch(events, at_epoch, when):
    """Replay separately from the implementation's snapshot logic."""
    live = {}
    for i, event in enumerate(events, 1):
        if i > at_epoch:
            break
        if event.op == "add":
            live[event.key] = event.edge
        elif event.op == "del":
            live.pop(event.key)
        else:
            raise AssertionError("unknown operation")
    return [e for e in live.values() if e.valid_from <= when < e.valid_to]


def independent_witnesses(edges, src, dst, n):
    """Enumerate *vertex permutations*, independently from DFS and DP."""
    if src == dst:
        return {()}
    if src > dst:
        return set()
    pair_edges = {}
    for edge in edges:
        pair_edges.setdefault((edge.src, edge.dst), []).append(edge.key)
    answer = set()
    intermediate = list(range(src + 1, dst))
    for length in range(len(intermediate) + 1):
        for chosen in itertools.permutations(intermediate, length):
            if list(chosen) != sorted(chosen):
                continue
            path = (src,) + chosen + (dst,)
            parts = [pair_edges.get((a, b), [])
                     for a, b in zip(path, path[1:])]
            if all(parts):
                for keys in itertools.product(*parts):
                    answer.add(keys)
    return answer


class TemporalKGTests(unittest.TestCase):
    def test_all_four_vertex_dags_and_time_windows_against_batch_oracle(self):
        arcs = tuple(itertools.combinations(range(4), 2))
        checks = 0
        for mask in range(1 << len(arcs)):
            graph = TemporalDag()
            selected = [(i, a, b) for i, (a, b) in enumerate(arcs)
                        if (mask >> i) & 1]
            for i, a, b in selected:
                graph.add("e" + str(i), a, b, i % 2, 2 + (i % 2))
            snapshots = [0, graph.epoch]
            if selected:
                graph.retract("e" + str(selected[0][0]))
                snapshots.append(graph.epoch)
            for epoch in snapshots:
                for when in range(4):
                    facts = independent_batch(graph.events, epoch, when)
                    for src in range(4):
                        for dst in range(4):
                            expected = independent_witnesses(facts, src, dst, 4)
                            actual = graph.witnesses(src, dst, epoch, when)
                            self.assertEqual(set(actual), expected)
                            self.assertEqual(len(actual),
                                             graph.count_factorized(src, dst, epoch, when))
                            for witness in actual:
                                self.assertTrue(graph.verify_positive_witness(
                                    src, dst, epoch, when, witness))
                            checks += 1
        self.assertGreater(checks, 1000)

    def test_bitemporal_correction_and_history_are_independent(self):
        graph = TemporalDag()
        t1 = graph.add("old", 0, 1, 0, 10)
        t2 = graph.add("continuation", 1, 2, 0, 10)
        self.assertEqual(graph.witnesses(0, 2, t2, 2),
                         [("old", "continuation")])
        t3 = graph.retract("old")
        self.assertEqual(graph.witnesses(0, 2, t3, 2), [])
        self.assertEqual(graph.witnesses(0, 2, t2, 2),
                         [("old", "continuation")])
        self.assertEqual(graph.witnesses(0, 1, t1, 10), [])
        self.assertEqual(graph.witnesses(0, 1, 0, 2), [])
        self.assertFalse(graph.verify_positive_witness(
            0, 2, t3, 2, ("old", "continuation")))

    def test_simultaneous_valid_time_not_individual_edge_existence(self):
        graph = TemporalDag()
        graph.add("a", 0, 1, 0, 2)
        graph.add("b", 1, 2, 2, 4)
        self.assertEqual(graph.witnesses(0, 2, 2, 0), [])
        self.assertEqual(graph.witnesses(0, 2, 2, 2), [])
        self.assertEqual(graph.witnesses(0, 2, 2, 4), [])
        self.assertEqual(graph.count_factorized(0, 2, 2, 2), 0)

    def test_alternative_source_prevents_ghost_path_retraction(self):
        graph = TemporalDag()
        graph.add("a", 0, 1, 0, 5)
        graph.add("b", 0, 1, 0, 5)
        graph.add("c", 1, 2, 0, 5)
        old = graph.epoch
        self.assertEqual(set(graph.witnesses(0, 2, old, 1)),
                         {("a", "c"), ("b", "c")})
        graph.retract("a")
        self.assertEqual(graph.witnesses(0, 2, graph.epoch, 1),
                         [("b", "c")])
        self.assertTrue(graph.verify_positive_witness(
            0, 2, graph.epoch, 1, ("b", "c")))
        self.assertFalse(graph.verify_positive_witness(
            0, 2, graph.epoch, 1, ("a", "c")))
        self.assertFalse(graph.verify_positive_witness(
            0, 2, graph.epoch, 1, ("b", "nonexistent")))

    def test_one_update_changes_k_explicit_answers_not_all_representations(self):
        k = 24
        graph = TemporalDag()
        graph.add("bridge", 0, 1, 0, 9)
        for i in range(k):
            graph.add("leaf" + str(i), 1, 2 + i, 0, 9)
        old = graph.epoch
        before = [bool(graph.witnesses(0, 2 + i, old, 1))
                  for i in range(k)]
        ledger = graph.ledger.copy()
        new = graph.retract("bridge")
        after = [bool(graph.witnesses(0, 2 + i, new, 1))
                 for i in range(k)]
        self.assertEqual(sum(a != b for a, b in zip(before, after)), k)
        self.assertEqual(graph.ledger["event_log_appends"] -
                         ledger["event_log_appends"], 1)
        self.assertEqual(graph.ledger["live_id_index_mutations"] -
                         ledger["live_id_index_mutations"], 1)
        self.assertTrue(all(graph.witnesses(1, 2 + i, new, 1)
                            for i in range(k)))

    def test_diamond_exponential_path_supports_with_compact_count(self):
        for k in range(1, 9):
            graph = diamond(k)
            witnesses = graph.witnesses(0, 3 * k, graph.epoch, 2)
            self.assertEqual(len(witnesses), 2 ** k)
            self.assertEqual(graph.count_factorized(
                0, 3 * k, graph.epoch, 2), 2 ** k)
            self.assertEqual(graph.epoch, 4 * k)
            self.assertEqual(len({x for p in witnesses for x in p}), 4 * k)
            self.assertTrue(all(len(p) == 2 * k for p in witnesses))

    def test_input_rejection_asof_reuse_and_symbolic_certificate_limits(self):
        graph = TemporalDag()
        for args in [
            ("bad", 1, 1, 0, 2),
            ("bad", 2, 1, 0, 2),
            ("bad", 0, 1, 3, 3),
            ("bad", 0, 1, 4, 2),
            ("bad", True, 1, 0, 2),
        ]:
            with self.assertRaises(ValueError):
                graph.add(*args)
        self.assertEqual(graph.epoch, 0)
        graph.add("e", 0, 1, -5, 5)
        with self.assertRaises(ValueError):
            graph.add("e", 0, 2, 0, 5)
        with self.assertRaises(ValueError):
            graph.retract("missing")
        graph.retract("e")
        with self.assertRaises(ValueError):
            graph.retract("e")
        with self.assertRaises(ValueError):
            graph.add("e", 0, 2, 0, 5)
        with self.assertRaises(ValueError):
            graph.active(graph.epoch + 1, 2)
        self.assertFalse(graph.verify_positive_witness(
            0, 1, graph.epoch + 1, 2, ("e",)))
        self.assertFalse(graph.verify_positive_witness(0, 1, 1, 1, ["e"]))
        self.assertTrue(graph.verify_positive_witness(2, 2, 1, 1, ()))
        self.assertFalse(graph.verify_positive_witness(0, 1, 1, 1, ()))


if __name__ == "__main__":
    unittest.main()
