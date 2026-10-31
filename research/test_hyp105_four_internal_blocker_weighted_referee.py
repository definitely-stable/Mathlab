"""Independent exact abstract-graph and genuine ORIGINAL W32/W34 falsifiers."""
from collections import defaultdict
from itertools import combinations
import unittest

from hyp105_full_physical_degree_tail import genuine_source
from hyp105_four_internal_blocker_weighted_referee import (
    _a2_moments, four_blocker_referee,
)


def _minimal_pairs(V):
    a = 2
    while a * (a - 1) // 2 < V:
        a += 1
    return tuple(combinations(range(a), 2))[:V]


class FourBlockerWeightedReferee(unittest.TestCase):
    def test_all_64_small_bipartite_graphs_direct_closed_walks(self):
        # Separate direct walk oracle: not A² matrix multiplication.
        for mask in range(64):
            adjacency = defaultdict(set)
            vertices = tuple(range(5))
            for i in range(2):
                for j in range(3):
                    if mask & (1 << (3 * i + j)):
                        a, b = i, j + 2
                        adjacency[a].add(b)
                        adjacency[b].add(a)
            a2, trace4, theta, delta = _a2_moments(adjacency)
            direct4 = 0
            degree_weighted4 = 0
            for v in vertices:
                for v1 in adjacency[v]:
                    for v2 in adjacency[v1]:
                        for v3 in adjacency[v2]:
                            if v in adjacency[v3]:
                                direct4 += 1
                                degree_weighted4 += len(adjacency[v])
            self.assertEqual(trace4, direct4)
            self.assertEqual(theta, degree_weighted4)
            self.assertLessEqual(theta, delta * trace4)
            # Explicit original physical first-edge candidate triples,
            # with deterministic adversarial selection of endpoint cells.
            for residue in range(4):
                triples = {(v0, v1, v3)
                           for v0 in adjacency for v1 in adjacency[v0]
                           for v3 in vertices
                           if (v0 * 7 + v1 * 3 + v3 + mask) % 4 == residue}
                W = sum(a2.get(v1, {}).get(v3, 0)
                        for v0, v1, v3 in triples)
                cell = sum(a2.get(v1, {}).get(v3, 0) ** 2
                           for v0, v1, v3 in triples)
                self.assertLessEqual(W * W, len(triples) * cell)
                self.assertLessEqual(cell, theta)

    def test_true_w32_same_original_ids_four_positions(self):
        _, V, flags = genuine_source(1)
        f = _minimal_pairs(V)
        for k in (0, 3, 7):
            g = tuple(f[(i + k) % V] for i in range(V))
            for core in (None, tuple(range(0, len(flags), 2)),
                         tuple(i for i in range(len(flags)) if i % 5 != 0)):
                with self.subTest(shift=k, core_len=None if core is None else len(core)):
                    result = four_blocker_referee(1, f, g, core)
                    self.assertTrue(result["all_checks_passed"])
                    self.assertEqual(
                        result["primal"]["phi"] - result["primal"]["incident_defect"],
                        result["primal"]["blocked_triples"])
                    self.assertEqual(
                        result["dual"]["phi"] - result["dual"]["incident_defect"],
                        result["dual"]["blocked_triples"])
                    self.assertEqual(result["primal"]["edges"], 2 * result["core_flags"])
                    self.assertEqual(result["proper_blocked_by_position"][0],
                                     result["proper_blocked_by_position"][1])
                    self.assertEqual(result["proper_blocked_by_position"][2],
                                     result["proper_blocked_by_position"][3])

    def test_true_w34_full_and_sparse_correlated_global_maps(self):
        _, V, flags = genuine_source(2)
        f = _minimal_pairs(V)
        for k, core in ((0, None),
                        (17, tuple(i for i in range(len(flags)) if i % 3 == 0))):
            g = tuple(f[(i * 19 + k) % V] for i in range(V))
            with self.subTest(shift=k):
                result = four_blocker_referee(2, f, g, core)
                self.assertTrue(result["all_checks_passed"])
                self.assertLessEqual(result["proper_union"],
                                     result["four_position_envelope"])
                self.assertLessEqual(
                    result["primal"]["degree_weighted_trace4"],
                    result["primal"]["delta"] * result["primal"]["trace4"])
                self.assertEqual(result["primal"]["degree_weighted_trace4"],
                                 result["dual"]["degree_weighted_trace4"])

    def test_empty_core_and_fail_closed_illegal_inputs(self):
        _, V, flags = genuine_source(1)
        f = _minimal_pairs(V)
        z = four_blocker_referee(1, f, f, ())
        self.assertEqual(z["proper_union"], 0)
        self.assertEqual(z["four_position_envelope"], 0)
        self.assertEqual(z["primal"]["degree_weighted_trace4"], 0)
        with self.assertRaises(ValueError):
            four_blocker_referee(3, f, f)
        with self.assertRaises(ValueError):
            four_blocker_referee(1, f[:-1], f)
        with self.assertRaises(ValueError):
            four_blocker_referee(1, (f[0],) * V, f)
        with self.assertRaises(ValueError):
            four_blocker_referee(1, f, f, (0, 0))
        with self.assertRaises(ValueError):
            four_blocker_referee(1, f, f, (len(flags),))
        with self.assertRaises(ValueError):
            four_blocker_referee(1, f, f, (True,))


if __name__ == "__main__":
    unittest.main()
