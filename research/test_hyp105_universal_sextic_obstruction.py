"""Independent finite falsifiers, not all-h computational certification."""
from itertools import combinations, permutations, product
import json
from math import factorial
from pathlib import Path
import unittest

from hyp105_universal_sextic_obstruction import (
    certificate_suite, finite_source_certificate, walk_matrix,
    square_norm, simple_sixcycles,
)
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic


class UniversalSexticObstruction(unittest.TestCase):
    def test_sixth_moment_every_three_by_three_bipartite_graph(self):
        pairs = tuple(product(range(3), range(3, 6)))
        for mask in range(1 << len(pairs)):
            adj = {v: set() for v in range(6)}
            for bit, (u, v) in enumerate(pairs):
                if mask >> bit & 1:
                    adj[u].add(v)
                    adj[v].add(u)
            m, delta = mask.bit_count(), max(map(len, adj.values()))
            t4, t6 = square_norm(walk_matrix(adj, 2)), square_norm(walk_matrix(adj, 3))
            cycles = simple_sixcycles(adj)
            self.assertLessEqual(t6, 12*cycles+6*delta*t4)
            self.assertLessEqual(t4*t4, 2*m*t6)
            self.assertLessEqual(t6, 24*cycles+144*m*delta*delta)

    def test_selector_all_four_vertex_conflict_graphs_and_orders(self):
        pairs = tuple(combinations(range(4), 2))
        orders = tuple(permutations(range(4)))
        for mask in range(1 << len(pairs)):
            graph = {u: set() for u in range(4)}
            for bit, (u, v) in enumerate(pairs):
                if mask >> bit & 1:
                    graph[u].add(v)
                    graph[v].add(u)
            cap = max(map(len, graph.values()))
            for r in (2, 3):
                for target in combinations(range(4), r):
                    if any(v in graph[u] for u, v in combinations(target, 2)):
                        continue
                    survivors = 0
                    for order in orders:
                        rank = {u: i for i, u in enumerate(order)}
                        selected = {u for u in graph if all(rank[u] < rank[v] for v in graph[u])}
                        self.assertTrue(all(v not in graph[u] for u, v in combinations(selected, 2)))
                        survivors += set(target) <= selected
                    self.assertGreaterEqual(survivors*(r*(cap+1))**r, factorial(4))
        # Both coordinate cuts, with all symbols distinct on either side.
        for r in (2, 3):
            colors = tuple(product((0, 1), repeat=r+1))
            count = sum(all(x[i] != x[i+1] and y[i] != y[i+1] for i in range(r))
                        for x in colors for y in colors)
            self.assertEqual(count*4**r, len(colors)**2)

    def test_genuine_sources_mixed_full_core_bounds_and_original_BBo(self):
        result = certificate_suite()
        expected_path = Path(__file__).parent/'fixtures/hyp105_universal_sextic_obstruction.json'
        self.assertEqual(result, json.loads(expected_path.read_text()))
        full = result['W34_adversarial_full']
        self.assertEqual(full['accepted_original_BBo_subcount'], 5261)
        self.assertEqual(full['path_partition']['unblocked'], 10522)
        self.assertEqual(full['path_partition']['internal_blocked_good'], 12592)
        sparse = result['W34_adversarial_sparse_core']
        self.assertGreater(sparse['accepted_original_BBo_subcount'], 0)
        self.assertGreater(sparse['unblocked_paths_using_anchor_outside_core'], 0)
        self.assertTrue(all(not row['finite_computation_proves_all_h'] for row in result.values()))

    def test_coordinate_relabeling_and_fail_closed_inputs(self):
        model = pair_labeled_symplectic(1, 'lex')
        f, g = model['left_labels'], model['right_labels']
        baseline = finite_source_certificate(1, f, g)
        ff = [tuple(sorted((5*x+1) % 6 for x in pair)) for pair in f]
        gg = [tuple(sorted((5*x+3) % 6 for x in pair)) for pair in g]
        self.assertEqual(baseline, finite_source_certificate(1, ff, gg))
        empty = finite_source_certificate(1, f, g, ())
        self.assertEqual(empty['accepted_original_BBo_subcount'], 0)
        self.assertEqual(empty['physical_core_edges'], 0)
        for ids in ((0, 0), (-1,), (45,), (True,)):
            with self.assertRaises(ValueError):
                finite_source_certificate(1, f, g, ids)
        with self.assertRaises(ValueError):
            finite_source_certificate(1, f[:-1], g)


if __name__ == '__main__':
    unittest.main()
