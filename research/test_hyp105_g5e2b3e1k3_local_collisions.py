"""Independent K3-A/B falsifiers; no reliance on local fast counting oracle."""
from itertools import combinations
import random
import unittest

from hyp105_g5e2b3e1k1_kikuchi_c6 import (
    codegree_profile, gq_pair_model, kikuchi_graph, path3_profile,
    six_cycle_census,
)
from hyp105_g5e2b3e1k3_local_collisions import (
    book_graph, endpoint_collision_rows, localized_certificate,
    star_codegree_tensor, star_degree_tensor,
)


def slow_endpoint_oracle(neighbors, u, v):
    """Quadratic PAIR-of-paths oracle, disjoint from fast internal loads."""
    paths = [(b, c) for b in neighbors[u]
             for c in neighbors[b] if c != u
             if v in neighbors[c] and v != b and v != u]
    one = two = disjoint = 0
    for i, p in enumerate(paths):
        for j, q in enumerate(paths):
            if i == j:
                continue
            k = len(set(p) & set(q))
            if k == 0:
                disjoint += 1
            elif k == 1:
                one += 1
            else:
                two += 1
    return (len(paths), one, two, disjoint)


def small_random_graph(rng, n, probability):
    rows = [set() for _ in range(n)]
    for a, b in combinations(range(n), 2):
        if rng.random() < probability:
            rows[a].add(b)
            rows[b].add(a)
    return tuple(frozenset(row) for row in rows)


class LocalCollisionTests(unittest.TestCase):
    def test_all_endpoint_rows_against_independent_quadratic_oracle(self):
        rng = random.Random(20261011)
        graphs = [book_graph(t) for t in (2, 3, 5, 8)]
        graphs += [small_random_graph(rng, rng.randrange(5, 9),
                                      rng.choice((0.2, 0.45, 0.8, 1.0)))
                   for _ in range(24)]
        for graph in graphs:
            rows = list(endpoint_collision_rows(graph))
            self.assertEqual(len(rows), len(graph) * (len(graph) - 1))
            for row in rows:
                p, one, two, disjoint = slow_endpoint_oracle(
                    graph, row["u"], row["v"])
                self.assertEqual(
                    (row["p3"], row["one_internal"],
                     row["two_internal"], row["disjoint"]),
                    (p, one, two, disjoint),
                )
                self.assertEqual(row["theta"], one + two)
            cert = localized_certificate(graph, "all")
            profile = path3_profile(graph)
            self.assertEqual(cert["all_P3"], profile["P3"])
            self.assertEqual(cert["all_Theta"], codegree_profile(graph)["Theta"])
            self.assertEqual(cert["all_disjoint"],
                             12 * six_cycle_census(graph, len(graph))["C6"])
            for mode, limit in (("active", None),
                                ("endpoint-codegree", 0),
                                ("endpoint-codegree", 2),
                                ("internal-load", 1),
                                ("internal-load", 3)):
                selected = localized_certificate(graph, mode, limit)
                self.assertLessEqual(selected["selected_disjoint"],
                                     cert["all_disjoint"])
                self.assertLessEqual(selected["C6_integer_floor"],
                                     cert["all_disjoint"] // 12)

    def test_book_obstruction_to_endpoint_codegree_filter(self):
        for t in (3, 5, 10):
            graph = book_graph(t)
            cert = localized_certificate(graph, "endpoint-codegree", 0)
            expected_paths = 4 * t * (t - 1)
            expected_theta = expected_paths * (t - 2)
            self.assertEqual(cert["all_P3"], expected_paths)
            self.assertEqual(cert["all_Theta"], expected_theta)
            self.assertEqual(cert["selected_P3"], expected_paths)
            self.assertEqual(cert["selected_Theta"], expected_theta)
            self.assertEqual(cert["selected_disjoint"], 0)
            self.assertEqual(cert["C6_integer_floor"], 0)
            # Every active (u,v) pair has zero common neighbors,
            # yet all their 3-paths collide internally.
            for row in endpoint_collision_rows(graph):
                if row["p3"]:
                    self.assertEqual(len(graph[row["u"]] & graph[row["v"]]), 0)

    def test_true_w32_s4_global_injections(self):
        for power, scheme, seed in ((1, "lex", None),
                                    (1, "reverse-line", None),
                                    (2, "random", 20261011)):
            model = gq_pair_model(power, scheme, seed)
            graph = kikuchi_graph(model)
            global_cert = localized_certificate(graph, "all")
            active_cert = localized_certificate(graph, "active")
            self.assertEqual(global_cert["all_P3"], path3_profile(graph)["P3"])
            self.assertEqual(global_cert["all_Theta"], codegree_profile(graph)["Theta"])
            self.assertEqual(global_cert["all_disjoint"],
                             12 * six_cycle_census(graph, model["a"])["C6"])
            self.assertEqual(active_cert["selected_P3"],
                             global_cert["selected_P3"])
            self.assertGreaterEqual(active_cert["selected_pairs"], 1)
            for mode, threshold in (("endpoint-codegree", 0),
                                    ("internal-load", 2)):
                loc = localized_certificate(graph, mode, threshold)
                self.assertLessEqual(loc["C6_integer_floor"],
                                     global_cert["all_disjoint"] // 12)

    def test_original_incidence_tensors_are_independent_of_kikuchi_graph(self):
        for power, scheme, seed in ((1, "lex", None),
                                    (1, "reverse-line", None),
                                    (2, "random", 20261011)):
            model = gq_pair_model(power, scheme, seed)
            graph = kikuchi_graph(model)
            self.assertEqual(star_degree_tensor(model),
                             tuple(map(len, graph)))
            rng = random.Random(230 + power)
            candidates = (list(combinations(range(len(graph)), 2))
                          if power == 1 else
                          [tuple(sorted(rng.sample(range(len(graph)), 2)))
                           for _ in range(100)])
            for u, v in candidates:
                self.assertEqual(star_codegree_tensor(model, u, v),
                                 len(graph[u] & graph[v]))

    def test_fail_closed_budgets_and_inputs(self):
        graph = book_graph(5)
        with self.assertRaises(RuntimeError):
            list(endpoint_collision_rows(graph, max_pairs=3))
        with self.assertRaises(RuntimeError):
            list(endpoint_collision_rows(graph, max_paths=2))
        with self.assertRaises(ValueError):
            list(endpoint_collision_rows(graph, max_paths=-1))
        with self.assertRaises(ValueError):
            localized_certificate(graph, "endpoint-codegree")
        with self.assertRaises(ValueError):
            localized_certificate(graph, "internal-load", True)
        with self.assertRaises(ValueError):
            localized_certificate(graph, "bad")
        with self.assertRaises(ValueError):
            localized_certificate(graph, "all", threshold=0)
        with self.assertRaises(ValueError):
            book_graph(1)
        with self.assertRaises(ValueError):
            star_codegree_tensor(gq_pair_model(1), 0, 0)
        with self.assertRaises(ValueError):
            list(endpoint_collision_rows((frozenset((1,)), frozenset())))
        with self.assertRaises(ValueError):
            list(endpoint_collision_rows((frozenset((0,)),)))

    def test_zero_graph_and_empty_selected_set(self):
        graph = tuple(frozenset() for _ in range(5))
        result = localized_certificate(graph, "active")
        self.assertEqual(result["selected_pairs"], 0)
        self.assertEqual(result["selected_P3"], 0)
        self.assertEqual(result["C6_integer_floor"], 0)
        self.assertEqual(localized_certificate(graph, "all")["C6_integer_floor"], 0)


if __name__ == "__main__":
    unittest.main()
