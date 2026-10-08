"""UCT-001 exact finite falsification; tests do NOT prove originality/asymptotic bounds."""
from itertools import product
from math import comb
import unittest


def reachable(graph, start, radius):
    # Independent breadth-first oracle over directed edges, no use of a code.
    seen = {start}
    frontier = {start}
    for _ in range(radius):
        frontier = {v for u in frontier for v in graph[u] if v not in seen}
        seen |= frontier
    return seen


def graph_for_bits(bits, count=3):
    directed = [(u, v) for u in range(count) for v in range(count) if u != v]
    g = [set() for _ in range(count)]
    for i, (u, v) in enumerate(directed):
        if bits & (1 << i):
            g[u].add(v)
    return g


def encodes(graph, words, outputs, locality):
    for i in range(len(words)):
        for j in range(len(words)):
            if words[i] == words[j] and outputs[i] != outputs[j]:
                return False
    for u, targets in enumerate(graph):
        for v in targets:
            if (words[u] ^ words[v]).bit_count() > locality:
                return False
    return True


class Uct001FiniteTests(unittest.TestCase):
    def test_all_three_node_directed_graphs_and_current_observations(self):
        # Exhaust all directed loopless 3-node graphs, 2-valued observables,
        # q=2 representations of lengths m=0,1,2, and all possible words.
        # Reachable observations are independently enumerated by graph BFS.
        checks = 0
        for edge_bits in range(1 << 6):
            graph = graph_for_bits(edge_bits)
            reach = {(x, d): reachable(graph, x, d)
                     for x in range(3) for d in range(4)}
            for m in range(3):
                universe = tuple(range(1 << m))
                for outputs in product((0, 1), repeat=3):
                    for words in product(universe, repeat=3):
                        for w in range(m + 1):
                            if not encodes(graph, words, outputs, w):
                                continue
                            for d in range(4):
                                radius = min(d * w, m)
                                exact_ball = sum(
                                    (words[0] ^ v).bit_count() <= radius
                                    for v in universe
                                )
                                formula_ball = sum(comb(m, j) for j in range(radius + 1))
                                self.assertEqual(exact_ball, formula_ball)
                                for x in range(3):
                                    centered_ball = sum(
                                        (words[x] ^ v).bit_count() <= radius
                                        for v in universe
                                    )
                                    observations = len({
                                        outputs[y] for y in reach[(x, d)]
                                    })
                                    self.assertLessEqual(observations, centered_ball)
                                    checks += 1
        self.assertGreater(checks, 1000)

    def test_volume_is_not_sufficient_triangle_vs_path(self):
        path = [{1}, {0, 2}, {1}]
        triangle = [{1, 2}, {0, 2}, {0, 1}]
        distinct = (0, 1, 2)
        def feasible(graph):
            return any(encodes(graph, words, distinct, 1)
                       for words in product(range(4), repeat=3))
        self.assertTrue(feasible(path))
        self.assertFalse(feasible(triangle))
        for center in range(3):
            self.assertEqual(len(reachable(triangle, center, 1)), 3)
        self.assertEqual(sum(comb(2, j) for j in range(2)), 3)

    def test_bipartite_k23_is_not_hypercube_subgraph(self):
        # Complete bipartite K(2,3) satisfies all radius counts at m=3,
        # but is not a cubical graph (any pair shares <=2 neighbors).
        from itertools import permutations
        graph = [{2, 3, 4}, {2, 3, 4}, {0, 1}, {0, 1}, {0, 1}]
        for x in range(5):
            for d in range(4):
                radius = min(d, 3)
                ball = sum(comb(3, j) for j in range(radius + 1))
                self.assertLessEqual(len(reachable(graph, x, d)), ball)
        self.assertFalse(any(
            encodes(graph, words, tuple(range(5)), 1)
            for words in permutations(range(8), 5)
        ))
        for m in range(1, 6):
            words = range(1 << m)
            for a in words:
                for b in words:
                    if a == b:
                        continue
                    self.assertLessEqual(sum(
                        (a ^ z).bit_count() == 1 and (b ^ z).bit_count() == 1
                        for z in words
                    ), 2)

    def test_current_observation_does_not_define_dynamic_state(self):
        # Exhaustive truth tables / all state pairs / common overwrites.
        witnesses = []
        for truth in range(16):
            f = lambda a, b: (truth >> (2*a+b)) & 1
            for left in product((0, 1), repeat=2):
                for right in product((0, 1), repeat=2):
                    if f(*left) != f(*right):
                        continue
                    for idx in range(2):
                        for bit in (0, 1):
                            la, ra = list(left), list(right)
                            la[idx], ra[idx] = bit, bit
                            if f(*la) != f(*ra):
                                witnesses.append((truth, left, right, idx, bit))
        # AND truth table: only (1,1) evaluates to 1, so truth=0b1000.
        self.assertIn((0b1000, (0, 0), (0, 1), 0, 1), witnesses)

    def test_star_bound_is_exact_for_one_coordinate_writes(self):
        for q in (2, 3):
            for m in (1, 2, 3):
                center = (0,) * m
                leaves = []
                for j in range(m):
                    for nonzero in range(1, q):
                        value = [0] * m
                        value[j] = nonzero
                        leaves.append(tuple(value))
                self.assertEqual(len(set([center] + leaves)), 1 + m * (q - 1))
                self.assertTrue(all(sum(a != b for a, b in zip(center, leaf)) == 1
                                    for leaf in leaves))
                # Independent exhaustive q-ary ball cardinality.
                ball = sum(
                    sum(a != b for a, b in zip(center, vec)) <= 1
                    for vec in product(range(q), repeat=m)
                )
                self.assertEqual(ball, 1 + m * (q - 1))


if __name__ == "__main__":
    unittest.main()
