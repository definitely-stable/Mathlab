"""Independent finite scope checks for UCT-005 G4 derived-classical bridges."""
import itertools
import unittest

from uct005_g4_bridge_oracles import (
    bounded_corruption_ball, dag_boolean_bfs, dag_path_count,
    disjoint_triple_columns, future_partition_by_traces,
    future_partition_refinement, future_probe_transfer_falsifier,
    graph_parity_falsifier, hamming_ball, histories_by_observable_pins,
    finite_horizon_congruence_falsifier, dna_indel_falsifier,
    min_pair_distance, qary_subset_sums, robust_subset_sums,
    robust_support_gate_report,
)


class FutureEquivalenceChecks(unittest.TestCase):
    def test_trace_oracle_vs_refinement_all_small_machines(self):
        # Exhaustive total 1..3 state machines, two public operations,
        # every Boolean output labelling, horizons 0..3.
        for n in (1, 2, 3):
            maps = tuple(itertools.product(range(n), repeat=n))
            for output in itertools.product((0, 1), repeat=n):
                for a in maps:
                    for b in maps:
                        operations = (a, b)
                        previous = 0
                        for h in range(4):
                            refined = future_partition_refinement(output, operations, h)
                            brute = future_partition_by_traces(output, operations, h)
                            self.assertEqual(refined, brute)
                            self.assertGreaterEqual(len(set(refined)), previous)
                            previous = len(set(refined))

    def test_present_vs_future_scope_falsifier(self):
        result = future_probe_transfer_falsifier()
        self.assertEqual(result["current_classes"], 2)
        self.assertEqual(result["future_classes"], 4)
        self.assertEqual(result["invalid_naive_one_probe_upper"], 2)
        self.assertEqual(result["valid_all_storage_upper"], 4)

    def test_invalid_partially_specified_machines_are_rejected(self):
        with self.assertRaises(ValueError):
            future_partition_refinement((0, 1), ((0,),), 1)
        with self.assertRaises(ValueError):
            future_partition_by_traces((0, 1), ((0, 2),), 1)
        with self.assertRaises(ValueError):
            future_partition_refinement((0,), ((0,),), -1)
        with self.assertRaises(ValueError):
            hamming_ball(1, 2, 1)


class AlgebraicErrorChecks(unittest.TestCase):
    def test_support_gate_and_explicit_e1_witness(self):
        report = robust_support_gate_report()
        self.assertEqual(report["e2_nonempty_capacity"], 0)
        self.assertEqual(report["e1_minimum_distance"], 3)
        for n in range(1, 5):
            columns = disjoint_triple_columns(n)
            self.assertTrue(robust_subset_sums(columns, 5, 3, 1))
            self.assertFalse(robust_subset_sums(columns, 5, 3, 2))

    def test_independent_full_corruption_ball_oracle(self):
        # Brute-force radius balls independently of min-pair-distance.
        for q in (2, 3):
            for m in (1, 2, 3):
                candidates = tuple(itertools.product(range(q), repeat=m))
                sample = candidates[:min(5, len(candidates))]
                for a, b in itertools.combinations(sample, 2):
                    for e in (0, 1):
                        no_overlap = bounded_corruption_ball(a, q, e).isdisjoint(
                            bounded_corruption_ball(b, q, e))
                        self.assertEqual(no_overlap,
                                         sum(x != y for x, y in zip(a, b)) >= 2 * e + 1)

    def test_subset_zero_singleton_and_repeated_columns(self):
        for q in (2, 5):
            for m in (1, 2, 3, 4):
                for v in itertools.product(range(q), repeat=m):
                    if not any(v):
                        continue
                    if sum(z != 0 for z in v) <= 4:
                        self.assertFalse(robust_subset_sums((v,), q, 3, 2))
                        self.assertEqual(min_pair_distance(qary_subset_sums((v,), q, 3)),
                                         sum(x != 0 for x in v))
            self.assertFalse(robust_subset_sums(((1, 0), (1, 0)), q, 2, 0))

    def test_bad_alphabet_and_dimensions(self):
        for args in (((), 5, 3), (((1, 2), (1,)), 5, 3),
                     (((1, 2),), 2, 0), (((5, 0),), 5, 1)):
            with self.assertRaises(ValueError):
                qary_subset_sums(*args)


class HistoryAndGraphChecks(unittest.TestCase):
    def test_history_entropy_exact_pins_all_small_traces(self):
        for h in range(1, 7):
            for mask in itertools.product((0, 1), repeat=h):
                pins = [i for i, bit in enumerate(mask) if bit]
                self.assertEqual(histories_by_observable_pins(h, pins), 1 << len(pins))

    def test_one_step_right_invariance_cannot_be_assumed(self):
        result = finite_horizon_congruence_falsifier()
        self.assertTrue(result["same_present_class"])
        self.assertTrue(result["distinct_after_one_update"])

    def test_dna_shifted_words_share_one_deletion_outcome(self):
        result = dna_indel_falsifier()
        self.assertEqual(result["hamming_distance"], 6)
        a, b = "ACACAC", "CACACA"
        common_a = {a[:i] + a[i+1:] for i in range(len(a))}
        common_b = {b[:i] + b[i+1:] for i in range(len(b))}
        self.assertIn(result["common_one_deletion_observation"], common_a & common_b)

    def test_graph_two_path_collision(self):
        result = graph_parity_falsifier()
        self.assertTrue(result["boolean_reachability"])
        self.assertEqual(result["gf2_path_sum"], 0)

    def test_all_forward_dags_bfs_vs_integer_count(self):
        for n in range(2, 6):
            pairs = tuple((i, j) for i in range(n) for j in range(i + 1, n))
            for mask in range(1 << len(pairs)):
                edges = tuple(p for index, p in enumerate(pairs) if mask & (1 << index))
                for i, j in pairs:
                    count = dag_path_count(n, edges, i, j)
                    self.assertEqual(dag_boolean_bfs(n, edges, i, j), count > 0)

    def test_invalid_graph_and_pins(self):
        with self.assertRaises(ValueError):
            dag_path_count(3, ((1, 0),), 0, 2)
        with self.assertRaises(ValueError):
            histories_by_observable_pins(3, (3,))


if __name__ == "__main__":
    unittest.main()
