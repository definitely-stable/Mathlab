"""HYP-105 K3-C independent C4-pair and original-GQ falsifiers."""
from collections import Counter, defaultdict
from itertools import combinations
import random
import unittest

from hyp105_g5e2b3e1k1_kikuchi_c6 import (
    gq_pair_model, kikuchi_graph, six_cycle_census,
)
from hyp105_g5e2b3e1k2_cycle_pattern_weights import edge_pair_identity
from hyp105_g5e2b3e1k3_local_collisions import book_graph, star_codegree_tensor
from hyp105_g5e2b3e1k3c_book_packing import (
    book_moments, classify_c4_pair_overlaps, triangle_and_k4_counts,
)


def independently_enumerated_c4(graph):
    """Walk-oriented brute-force closure, NOT K2 four_cycles function."""
    cycles = set()
    for u in range(len(graph)):
        for v in graph[u]:
            for w in graph[v]:
                if w == u:
                    continue
                for z in graph[w]:
                    if z in (u, v, w) or u not in graph[z]:
                        continue
                    cycles.add(frozenset((
                        frozenset((u, v)),
                        frozenset((v, w)),
                        frozenset((w, z)),
                        frozenset((z, u)),
                    )))
    return cycles


def brute_overlap_pairs(graph):
    """Definition-level quadratic pairs; no codegree sums or fast overlap index."""
    cycles = list(independently_enumerated_c4(graph))
    hist = Counter()
    edge_a = 0
    for i in range(len(cycles)):
        for j in range(i + 1, len(cycles)):
            overlap = cycles[i] & cycles[j]
            if not overlap:
                continue
            vert_i = set().union(*cycles[i])
            vert_j = set().union(*cycles[j])
            hist[(len(overlap), len(vert_i & vert_j))] += 1
            edge_a += len(overlap)
    return hist, edge_a


def graph_from_edges(n, edges):
    rows = [set() for _ in range(n)]
    for u, v in edges:
        rows[u].add(v)
        rows[v].add(u)
    return tuple(frozenset(row) for row in rows)


def random_graph(n, rng, p):
    return graph_from_edges(n, [(u, v) for u in range(n)
                                for v in range(u + 1, n)
                                if rng.random() < p])


class BookDecompositionTests(unittest.TestCase):
    def test_independent_cycle_pair_oracle_small_graphs(self):
        rng = random.Random(230367)
        graphs = [book_graph(t) for t in (2, 3, 4, 7)]
        graphs += [graph_from_edges(4, combinations(range(4), 2)),
                   graph_from_edges(5, combinations(range(5), 2))]
        graphs += [random_graph(rng.randrange(5, 11), rng, p)
                   for p in (0.2, 0.4, 0.6, 0.85, 1.0)
                   for _ in range(6)]
        for graph in graphs:
            actual = classify_c4_pair_overlaps(graph)
            hist, a = brute_overlap_pairs(graph)
            self.assertEqual(actual["C4"], len(independently_enumerated_c4(graph)))
            self.assertEqual(actual["A_edge_pairs"], a)
            self.assertEqual(actual["H_single_edge_only"], hist[(1, 2)])
            self.assertEqual(actual["B_two_edge_path"], hist[(2, 3)])
            self.assertEqual(actual["T_triangle_hook"], hist[(1, 3)])
            self.assertEqual(actual["K_two_opposite_edges"], hist[(2, 4)])
            self.assertEqual(actual["exact_A_rhs"], a)
            self.assertGreaterEqual(actual["A_edge_pairs"],
                                    int(__import__("fractions").Fraction(actual["jensen_A_floor"])))
            self.assertEqual(actual["B_two_edge_path"],
                             3 * sum(
                                 len(graph[u] & graph[v]) *
                                 (len(graph[u] & graph[v])-1) *
                                 (len(graph[u] & graph[v])-2) // 6
                                 for u in range(len(graph))
                                 for v in range(u + 1, len(graph))))
            self.assertEqual(actual["H_single_edge_only"],
                             edge_pair_identity(graph)["edge_only_pairs"])

    def test_pure_book_and_k4_disjoint_terms(self):
        for t in (3, 4, 7):
            graph = book_graph(t)
            r = classify_c4_pair_overlaps(graph)
            self.assertEqual(r["C4"], t * (t - 1) // 2)
            self.assertEqual(r["H_single_edge_only"], 0)
            self.assertEqual(r["T_triangle_hook"], 0)
            self.assertEqual(r["K_two_opposite_edges"], 0)
            self.assertEqual(r["B_two_edge_path"], 3 * t*(t-1)*(t-2)//6)
            self.assertEqual(r["A_edge_pairs"], 2 * r["B_two_edge_path"])
            self.assertEqual(r["C6_from_chord_floor"], 0)
        k4 = graph_from_edges(4, combinations(range(4), 2))
        r = classify_c4_pair_overlaps(k4)
        self.assertEqual((r["C4"], r["K4_cliques"], r["A_edge_pairs"]),
                         (3, 1, 6))
        self.assertEqual(r["K_two_opposite_edges"], 3)
        self.assertEqual(r["B_two_edge_path"], 0)

    def test_true_original_w32_and_s4_global_labeling(self):
        models = [gq_pair_model(1, "lex"),
                  gq_pair_model(1, "reverse-line"),
                  gq_pair_model(2, "random", 20261011)]
        for model in models:
            graph = kikuchi_graph(model)
            r = classify_c4_pair_overlaps(graph, model=model)
            hist, a = brute_overlap_pairs(graph)
            self.assertEqual(r["A_edge_pairs"], a)
            self.assertEqual(r["H_single_edge_only"], hist[(1, 2)])
            self.assertEqual(r["B_two_edge_path"], hist[(2, 3)])
            self.assertEqual(r["T_triangle_hook"], hist[(1, 3)])
            self.assertEqual(r["K_two_opposite_edges"], hist[(2, 4)])
            census = six_cycle_census(graph, model["a"])
            self.assertLessEqual(r["C6_from_chord_floor"], census["C6"])
            self.assertLessEqual(r["D6_from_proper_chord_floor"], census["proper_D6"])
            self.assertLessEqual(r["H_distinct_columns"], r["H_single_edge_only"])
            self.assertLessEqual(r["H_proper"], r["H_distinct_columns"])
            self.assertLessEqual(r["max_aligned_codegree"], model["a"]-2)
            self.assertEqual(r["book_same_x"]+r["book_same_y"]+r["book_mixed"],
                             r["B_two_edge_path"])

    def test_aligned_original_gq_pencil_uniqueness(self):
        # Independent ORIGINAL incidence contraction, not the C4 code.
        model = gq_pair_model(2, "lex")
        graph = kikuchi_graph(model)
        a = model["a"]
        aligned = []
        for x in range(a):
            for y in range(a):
                for yy in range(y + 1, a):
                    aligned.append((x*a+y, x*a+yy))
        for y in range(a):
            for x in range(a):
                for xx in range(x+1, a):
                    aligned.append((x*a+y, xx*a+y))
        for u, v in aligned:
            self.assertLessEqual(star_codegree_tensor(model, u, v), a - 2)
            self.assertEqual(star_codegree_tensor(model, u, v),
                             len(graph[u] & graph[v]))

    def test_limits_and_non_gq_shapes(self):
        k4 = graph_from_edges(4, combinations(range(4), 2))
        with self.assertRaises(RuntimeError):
            classify_c4_pair_overlaps(k4, max_pair_incidents=0)
        with self.assertRaises(ValueError):
            classify_c4_pair_overlaps(k4, max_pair_incidents=-1)
        with self.assertRaises(ValueError):
            book_moments(k4, 3)
        empty = tuple(frozenset() for _ in range(6))
        r = classify_c4_pair_overlaps(empty)
        self.assertEqual(r["C4"], 0)
        self.assertEqual(r["A_edge_pairs"], 0)
        self.assertEqual(r["H_single_edge_only"], 0)


if __name__ == "__main__":
    unittest.main()
