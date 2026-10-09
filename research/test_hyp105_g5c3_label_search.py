"""Independent finite, model/quantifier-safe checks for HYP-105 G5-C3-A."""
import random
import unittest
import itertools
import math

from hyp105_g5c2_density import collision_spectrum, w32_columns
from hyp105_g5c3_label_search import (
    IDENTITY, LABEL_COUNT, PAIRS,
    apply_swap, bounded_descent, certified_result, compose_image,
    fast_minimal_conflicts, induced_pair_relabeling, report,
    seeded_labels, supports_for_labels, vectors_for_labels
)
from test_hyp105_g5b_graph_realization import (
    quadrangle_w32, recovered_factor_edges, shortest_cycle_bipartite
)
from test_hyp105_g5c_signed_oracles import direct_aset_collision, signed_trade


class G5C3StructuredPairLabelTests(unittest.TestCase):
    def test_fast_oracle_matches_independent_c2_on_known_and_held_out(self):
        frozen = {None: (69, 1940), 0: (53, 1874),
                  1: (46, 1722), 2: (50, 1750)}
        for seed, counts in frozen.items():
            left, right = seeded_labels(seed)
            fast4, fast6 = fast_minimal_conflicts(left, right)
            self.assertEqual((len(fast4), len(fast6)), counts)
            self.assertEqual((fast4, fast6),
                             collision_spectrum(vectors_for_labels(left, right)))
            if seed is None:
                self.assertEqual(vectors_for_labels(left, right), w32_columns())

        for seed in range(17, 29):
            left, right = seeded_labels(seed)
            fast4, fast6 = fast_minimal_conflicts(left, right)
            slow4, slow6 = collision_spectrum(vectors_for_labels(left, right))
            self.assertEqual((fast4, fast6), (slow4, slow6), seed)

    def test_coordinate_gauge_exactly_preserves_full_trade_hypergraph(self):
        # Every coordinate permutation acts on 15 unordered pairs of K6.
        # Its induced pair relabeling may change labels but only permutes
        # coordinates globally within the corresponding 6-coordinate block.
        rng = random.Random(6730)
        for seed in (None, 0, 1, 9):
            l, r = seeded_labels(seed)
            baseline = fast_minimal_conflicts(l, r)
            for _ in range(10):
                pi = list(range(6))
                rho = list(range(6))
                rng.shuffle(pi)
                rng.shuffle(rho)
                l_prime = compose_image(l, induced_pair_relabeling(pi))
                r_prime = compose_image(r, induced_pair_relabeling(rho))
                self.assertEqual(fast_minimal_conflicts(l_prime, r_prime),
                                 baseline)
                self.assertEqual(
                    collision_spectrum(vectors_for_labels(l_prime, r_prime)),
                    baseline)
        self.assertEqual(len(PAIRS), 15)
        self.assertEqual(induced_pair_relabeling(tuple(range(6))), IDENTITY)

    def test_coordinate_gauge_action_is_faithful_and_orbit_count_exact(self):
        # The full 15-edge K6 pair action determines an S6 permutation
        # uniquely. Every labeling uses every pair, hence stabilizer is
        # trivial. For two independent coordinate blocks, all orbits have
        # size (6!)^2 and there are (15!/6!)^2 quotient classes.
        induced = {
            induced_pair_relabeling(pi)
            for pi in itertools.permutations(range(6))
        }
        self.assertEqual(len(induced), math.factorial(6))
        self.assertEqual(math.factorial(15) % math.factorial(6), 0)
        orbit_classes_one_half = math.factorial(15) // math.factorial(6)
        self.assertEqual(orbit_classes_one_half, 1816214400)
        self.assertGreater(orbit_classes_one_half**2, 10**18)

    def test_structured_descent_preserves_bijections_girth_and_monotonicity(self):
        graph = quadrangle_w32()[1]
        self.assertEqual(shortest_cycle_bipartite(graph), 8)
        for seed in (0, 1, 2):
            l, r = seeded_labels(seed)
            result = bounded_descent(l, r, seed=20261009 + seed,
                                     rounds=3, probes_per_round=7)
            self.assertLessEqual(result["objective_finish"],
                                 result["objective_start"])
            self.assertEqual(result["finish"],
                             tuple(map(len, fast_minimal_conflicts(
                                 result["left_labels"], result["right_labels"]))))
            self.assertEqual(set(result["left_labels"]), set(IDENTITY))
            self.assertEqual(set(result["right_labels"]), set(IDENTITY))
            final_edges = supports_for_labels(result["left_labels"],
                                              result["right_labels"])
            self.assertEqual(len(final_edges), 45)
            self.assertEqual(len(set(final_edges)), 45)
            self.assertEqual(len(recovered_factor_edges(final_edges)), 45)
            # Invert the bijections: incidence graph must be original GQ
            # and thus retains its bipartite girth 8 exactly.
            inverse_left = {pair: v for v, pair in enumerate(result["left_labels"])}
            inverse_right = {pair: v for v, pair in enumerate(result["right_labels"])}
            pair_to_left = {pair: i for i, pair in enumerate(PAIRS)}
            recon = [(
                inverse_left[pair_to_left[tuple(sorted(s[:2]))]],
                inverse_right[pair_to_left[
                    tuple(sorted(x-6 for x in s[2:]))]]
            ) for s in final_edges]
            self.assertEqual(tuple(recon), graph)
            self.assertEqual(shortest_cycle_bipartite(recon), 8)
            proof = certified_result(result["left_labels"],
                                     result["right_labels"])
            self.assertEqual((proof["T4"], proof["T6"]), result["finish"])
            self.assertIsNone(direct_aset_collision(
                tuple(vectors_for_labels(result["left_labels"],
                                         result["right_labels"])[i]
                      for i in proof["column_ids"]), 5))
            self.assertGreaterEqual(proof["extracted_aset"], 1)

    def test_held_out_deterministic_report_replays_bitwise(self):
        one = report(seed=17, rounds=2, probes=5)
        two = report(seed=17, rounds=2, probes=5)
        self.assertEqual(one, two)
        self.assertLessEqual(one["after_objective"], one["before_objective"])
        self.assertEqual(len(one["left_labels"]), LABEL_COUNT)
        self.assertEqual(len(one["right_labels"]), LABEL_COUNT)

    def test_bad_injections_and_unsafe_weighted_transfer_are_rejected(self):
        bad = (0,) * 15
        for left, right in ((bad, IDENTITY), (IDENTITY, bad),
                            (IDENTITY[:14], IDENTITY)):
            with self.assertRaises(ValueError):
                supports_for_labels(left, right)
        with self.assertRaises(ValueError):
            induced_pair_relabeling((0, 0, 1, 2, 3, 4))
        with self.assertRaises(ValueError):
            apply_swap(IDENTITY, -1, 4)
        with self.assertRaises(ValueError):
            bounded_descent(IDENTITY, IDENTITY, seed=2, rounds=-1)
        # The 3-vs-2 minimal weighted GF5 obstruction from G5-C1
        # cannot be enumerated using only equal-cardinality unit trades.
        weighted = (
            (3, 1, 1, 1), (1, 3, 1, 1), (1, 1, 3, 1),
            (1, 1, 1, 4), (4, 4, 4, 4)
        )
        self.assertIsNotNone(direct_aset_collision(weighted, 5))
        self.assertIsNotNone(signed_trade(weighted, 5))
        with self.assertRaises(ValueError):
            collision_spectrum(weighted)


if __name__ == "__main__":
    unittest.main()
