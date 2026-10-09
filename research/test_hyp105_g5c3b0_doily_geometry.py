"""Finite exact doily/duad-syntheme reconstruction audit, not all-s theorem."""
import unittest
from itertools import combinations

from hyp105_g5c3b0_doily_geometry import (
    adjacency_from_triples, certified_doily_report, doily_dual_recovery,
    enumerate_synthemes_directly, recover_duads
)
from hyp105_g5c3_label_search import (
    PAIRS, fast_minimal_conflicts, vectors_for_labels, certified_result
)
from test_hyp105_g5b_graph_realization import (
    quadrangle_w32, shortest_cycle_bipartite
)
from test_hyp105_g5c_signed_oracles import direct_aset_collision, signed_trade


class G5C3B0ExactDoilyTests(unittest.TestCase):
    def test_exact_six_ovoids_six_spreads_and_duad_membership(self):
        geo = doily_dual_recovery()
        self.assertEqual(len(geo["ovoid_fives"]), 6)
        self.assertEqual(len(geo["spread_fives"]), 6)
        self.assertTrue(all(len(set(five)) == 5
                            for five in geo["ovoid_fives"]))
        self.assertTrue(all(len(set(five)) == 5
                            for five in geo["spread_fives"]))
        self.assertEqual(set(geo["point_labels"]), set(range(15)))
        self.assertEqual(set(geo["line_labels"]), set(range(15)))
        for incidence_graph, fives in (
            (geo["point_adj"], geo["ovoid_fives"]),
            (geo["line_adj"], geo["spread_fives"]),
        ):
            for family in fives:
                self.assertTrue(all(
                    b not in incidence_graph[a]
                    for a, b in combinations(family, 2)))
            for i in range(15):
                self.assertEqual(sum(i in family for family in fives), 2)

    def test_independent_perfect_matching_model_recovers_full_incidence(self):
        geo = doily_dual_recovery()
        # Construct ALL 15 partitions of a six-set independently of
        # symplectic form and check exact set equality to recovered doily.
        synthemes = set(enumerate_synthemes_directly())
        self.assertEqual(len(synthemes), 15)
        self.assertEqual(set(geo["point_synthemes"]), synthemes)
        lines = geo["point_triples"]
        p_labels = geo["point_labels"]
        for i in range(15):
            for j, line in enumerate(lines):
                pair = PAIRS[p_labels[i]]
                matching = geo["point_synthemes"][j]
                self.assertEqual(i in line, pair in matching)
        # By construction, the second labeling comes from the DUAL
        # point-line geometry, not a relabeling of point pairs.
        for p in range(15):
            sy = [PAIRS[geo["line_labels"][idx]]
                  for idx in geo["line_incidence"][p]]
            self.assertEqual(len(sy), 3)
            self.assertEqual(set(k for pair in sy for k in pair),
                             set(range(6)))
        self.assertEqual(shortest_cycle_bipartite(quadrangle_w32()[1]), 8)

    def test_structured_labels_are_true_gf5_unit_columns_and_oracle_agrees(self):
        geo = doily_dual_recovery()
        left, right = geo["point_labels"], geo["line_labels"]
        cols = vectors_for_labels(left, right)
        self.assertEqual(len(cols), 45)
        self.assertEqual(len(set(cols)), 45)
        self.assertEqual({sum(x != 0 for x in row) for row in cols}, {4})
        fast4, fast6 = fast_minimal_conflicts(left, right)
        certified = certified_result(left, right)
        self.assertEqual((len(fast4), len(fast6)),
                         (certified["T4"], certified["T6"]))
        picked = tuple(cols[i] for i in certified["column_ids"])
        # COMPLETE full-family ASET oracle (0..3 subsets) is polynomial
        # for fixed d=3. The independent ternary signed kernel is 3^N:
        # restrict it to small held-out six-column selections, NOT N~20.
        self.assertIsNone(direct_aset_collision(picked, 5, 3))
        for start in range(min(10, max(0, len(picked) - 5))):
            self.assertIsNone(signed_trade(picked[start:start + 6], 5, 3))

    def test_bounded_doily_descent_is_replayable_and_finite_only(self):
        one = certified_doily_report(rounds=3, probes=7)
        two = certified_doily_report(rounds=3, probes=7)
        self.assertEqual(one, two)
        self.assertEqual(one["incidences"], 45)
        self.assertTrue(one["restricted_to_order_2"])
        self.assertFalse(one["unrestricted_aset_exponent_improved"])
        self.assertGreaterEqual(one["geometry_T4"], 0)
        self.assertGreaterEqual(one["geometry_T6"], 0)
        initial_score = one["geometry_T6"] + 16 * one["geometry_T4"]
        final_score = one["bounded_improved_T6"] + 16 * one["bounded_improved_T4"]
        self.assertLessEqual(final_score, initial_score)
        self.assertGreaterEqual(one["geometry_aset"], 1)
        self.assertGreaterEqual(one["bounded_improved_aset"], 1)

    def test_corruption_rejected_not_a_generic_graph_coding_model(self):
        with self.assertRaises(ValueError):
            recover_duads(tuple(frozenset() for _ in range(15)))
        with self.assertRaises(ValueError):
            adjacency_from_triples(((0, 1, 15),), count=15)
        # The fixture belongs to q=5 UNIT pairs, not weighted ASET.
        weighted = (
            (3, 1, 1, 1), (1, 3, 1, 1), (1, 1, 3, 1),
            (1, 1, 1, 4), (4, 4, 4, 4)
        )
        self.assertIsNotNone(signed_trade(weighted, 5))


if __name__ == "__main__":
    unittest.main()
