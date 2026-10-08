"""G2B regression: signed side bounds, exact graph correspondence and solver."""
from itertools import combinations
import unittest

from lent_exhaustive import is_exact_family
from lent_hypergraph import (
    build_forbidden_hypergraph,
    independent,
    solve_exact_or_certified_interval,
    verify_independent_oracle,
)


class G2BHypergraphTests(unittest.TestCase):
    def test_gf7_three_positive_zero_sum_is_legal(self):
        # 1 + 2 + 4 = 0 (mod 7), but all subset sums of size <=2
        # (0,1,2,4,3,5,6) are distinct. No +++ prohibition is legal.
        self.assertTrue(is_exact_family([(1,), (2,), (4,)], 7, 2))
        graph = build_forbidden_hypergraph(7, 1, 1)
        selected = 0
        for i, vector in enumerate(graph.columns):
            if vector in ((1,), (2,), (4,)):
                selected |= 1 << i
        self.assertEqual(selected.bit_count(), 3)
        self.assertTrue(independent(selected, graph.edges))
        self.assertTrue(verify_independent_oracle(graph, selected))

    def test_every_small_family_matches_independent_aset_oracle(self):
        # Exhaust all subsets, including cases with cross-cardinality
        # collisions. The oracle is independent of the graph construction.
        for q, m, w in ((3, 2, 2), (3, 3, 1), (5, 2, 1), (7, 1, 1)):
            graph = build_forbidden_hypergraph(q, m, w)
            for mask in range(1 << len(graph.columns)):
                self.assertEqual(
                    independent(mask, graph.edges),
                    verify_independent_oracle(graph, mask),
                    (q, m, w, mask),
                )

    def test_every_edge_is_necessary_and_minimal(self):
        for q, m, w in ((3, 3, 2), (5, 2, 2)):
            graph = build_forbidden_hypergraph(q, m, w)
            edges = graph.edges
            self.assertEqual(len(edges), len(set(edges)))
            for edge in edges:
                self.assertFalse(verify_independent_oracle(graph, edge))
                for i in range(len(graph.columns)):
                    if edge & (1 << i):
                        self.assertTrue(
                            verify_independent_oracle(graph, edge ^ (1 << i))
                        )

    def test_frozen_g2a_calibration(self):
        graph = build_forbidden_hypergraph(3, 3, 2)
        result = solve_exact_or_certified_interval(graph, max_nodes=100_000)
        self.assertTrue(result["exact"])
        self.assertEqual((result["lower"], result["upper"]), (5, 5))

    def test_g2b_q3_genuinely_sparse_exact(self):
        graph = build_forbidden_hypergraph(3, 4, 2)
        result = solve_exact_or_certified_interval(graph, max_nodes=300_000)
        self.assertTrue(result["search_exhausted"])
        self.assertTrue(result["exact"])
        self.assertEqual(result["lower"], 7)
        self.assertEqual(result["upper"], 7)
        self.assertEqual(len(result["witness"]), 7)

    def test_g2b_q5_budget_is_never_claimed_exact_without_proof(self):
        graph = build_forbidden_hypergraph(5, 3, 2)
        result = solve_exact_or_certified_interval(graph, max_nodes=25_000)
        self.assertEqual(result["search_nodes"], 25_000)
        self.assertGreaterEqual(result["lower"], 9)
        self.assertLessEqual(result["upper"], 15)
        self.assertLessEqual(result["lower"], result["upper"])
        self.assertTrue(is_exact_family(
            [tuple(v) for v in result["witness"]], 5, 2
        ))
        if not result["search_exhausted"]:
            self.assertFalse(result["exact"] or result["lower"] == result["upper"])

    def test_fail_closed_parameters(self):
        with self.assertRaises(ValueError):
            build_forbidden_hypergraph(4, 3, 2)  # 4 is not prime
        with self.assertRaises(ValueError):
            build_forbidden_hypergraph(3, 2, 3)
        with self.assertRaises(ValueError):
            solve_exact_or_certified_interval(
                build_forbidden_hypergraph(3, 2, 1), max_nodes=0
            )


if __name__ == "__main__":
    unittest.main()
