"""Independent HYP-105 C1 GQ concurrence and wedge falsifiers."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1a_fixed_leading import (
    selected_left_six, validated_small_model,
)
from hyp105_g5e2b3e1c0_weighted_overlap import source_weighted_BA_hypergraph
from hyp105_g5e2b3e1c1_gq_concurrency import (
    all_h_right_line_concurrency, original_right_line_concurrency,
    physical_four_cycles_on_other_coordinates,
    weighted_BA_via_original_point_wedges,
    exact_W32_source_concurrency_diagnostic,
)


def independent_original_B_source(model):
    """Use original six-INCIDENCE selections, not the point-wedge generator."""
    _, _, original, _ = validated_small_model(model)
    counts = Counter()
    nB = 0
    for ids, kind in selected_left_six(model):
        if kind != "B":
            continue
        nB += 1
        R = frozenset(original[i][1] for i in ids)
        if len(R) == 6:
            counts[R] += 1
    if nB != 10935:
        raise AssertionError("independent accepted original B census changed")
    return counts


class GQConcurrenceTests(unittest.TestCase):
    def test_exact_all_h_concurrency_srg_counts(self):
        pinned = {
            2: (80, 180, 180, 15),
            4: (43520, 40800, 13600, 850),
        }
        for s in (2, 4, 8, 16, 32, 64, 128):
            data = all_h_right_line_concurrency(s)
            v = data["V"]
            k = data["line_concurrence_degree"]
            n = data["induced_three_line_counts_by_edges"]
            self.assertEqual(sum(n), v * (v-1) * (v-2) // 6)
            self.assertEqual(n[3], v * k * (s-1) // 6)
            self.assertEqual(n[2], v * (k*(k-1)//2) - 3*n[3])
            self.assertEqual(data["random_sixset_mean_concurrent_pairs"],
                             Fraction(15*k, v-1))
            self.assertEqual(data["line_concurrence_pairs"], v*k//2)
            self.assertTrue(data["source_support_requires_concurrent_line_pair"])
            self.assertFalse(data["universal_all_correlated_overlap_lower"])
            if s in pinned:
                self.assertEqual(n, pinned[s])
        self.assertLess(
            all_h_right_line_concurrency(16)["random_sixset_mean_concurrent_pairs"],
            1)
        for invalid in (1, 3, 5, True):
            with self.assertRaises(ValueError):
                all_h_right_line_concurrency(invalid)

    def test_independent_original_line_graph_and_triples_W32(self):
        model = pair_labeled_symplectic(1, "lex")
        _, _, original, _ = validated_small_model(model)
        graph = original_right_line_concurrency(model)
        adj = [set() for _ in range(15)]
        incidences = [set() for _ in range(15)]
        for p, l in original:
            incidences[l].add(p)
        for i in range(15):
            for j in range(i+1, 15):
                if incidences[i] & incidences[j]:
                    self.assertEqual(len(incidences[i] & incidences[j]), 1)
                    adj[i].add(j)
                    adj[j].add(i)
        self.assertEqual(graph, tuple(frozenset(n) for n in adj))
        self.assertEqual({len(n) for n in graph}, {6})
        frequencies = Counter()
        for A in combinations(range(15), 3):
            e = sum(y in adj[x] for x, y in combinations(A, 2))
            frequencies[e] += 1
            if e == 3:
                self.assertEqual(len(set.intersection(*(incidences[i] for i in A))),1)
        self.assertEqual(tuple(frequencies[i] for i in range(4)),
                         (80, 180, 180, 15))

    def test_wedge_source_equals_independent_original_sixsets(self):
        for scheme in ("lex", "reverse-line"):
            model = pair_labeled_symplectic(1, scheme)
            wedge = weighted_BA_via_original_point_wedges(model)
            direct = independent_original_B_source(model)
            reference = source_weighted_BA_hypergraph(model)
            self.assertEqual(wedge, direct)
            self.assertEqual(wedge, reference)
            self.assertEqual(sum(wedge.values()), 5000)
            self.assertEqual(len(wedge), 3076)
            self.assertEqual(max(wedge.values()), 6)

    def test_third_source_moments_are_model_based_not_target_orbits(self):
        cert = all_h_right_line_concurrency(2)
        for scheme in ("lex", "reverse-line"):
            model = pair_labeled_symplectic(1, scheme)
            wedge = weighted_BA_via_original_point_wedges(model)
            data = exact_W32_source_concurrency_diagnostic(model, wedge)
            self.assertEqual(data["all_original_three_line_sets_by_class"],
                             cert["induced_three_line_counts_by_edges"])
            self.assertEqual(data["source_total_mass"], 5000)
            self.assertEqual(data["source_3marginal_total"], 100000)
            self.assertEqual(sum(data["source_3marginal_by_concurrence_pairs"]),
                             100000)
            self.assertTrue(all(a <= b for a,b in zip(
                data["source_3marginal_positive_triples_by_class"],
                data["all_original_three_line_sets_by_class"])))
            self.assertFalse(data["all_right_maps_universal_lower_proved"])

    def test_wedge_rejects_out_of_scope_and_enumerates_three_cycles(self):
        self.assertEqual(
            len(tuple(physical_four_cycles_on_other_coordinates((0, 1), 6))),3)
        with self.assertRaises(ValueError):
            tuple(physical_four_cycles_on_other_coordinates((0,1), 14))


if __name__ == "__main__":
    unittest.main()
