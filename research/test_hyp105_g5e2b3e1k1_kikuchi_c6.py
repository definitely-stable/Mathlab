"""Independent K1 falsifiers: Kikuchi six-cycles versus accepted motif oracles.

The accepted W32 seven-family census (B0), the independent left-C6 DFS plus
right join (B2) and the coincident-C4 join are reused only as ORACLES; the
K2 coincidence mass is recomputed from its definition by explicit 3-path
pairs, never from the codegree formula under test.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import random
import unittest

from hyp105_b1_symplectic import exact_gq_certificate
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3b2_coincident_cycles import exact_coincident_c6
from hyp105_g5e2b3d_joint_risk import exact_coincident_c4
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_g5e2b3e1k1_kikuchi_c6 import (
    a_priori_p3_floor, a_priori_table, ahl_nb3_lower, codegree_profile,
    greedy_d6_adversary, gq_pair_model, kikuchi_graph, kikuchi_statistics,
    labeled_model, path3_profile, proper_six_cycles_pruned, six_cycle_census,
    two_core,
)

PAIRS6 = tuple(combinations(range(6), 2))


def s2_model_with(left, right):
    """Accepted pair_labeled_symplectic model with replaced bijections."""
    model = dict(pair_labeled_symplectic(1, "lex"))
    a = model["a"]
    model["left_labels"] = tuple(left)
    model["right_labels"] = tuple(right)
    model["supports"] = tuple(
        tuple(sorted(left[p] + tuple(a + x for x in right[l])))
        for p, l in model["incidences"])
    model["scheme"] = "test-permutation"
    return model


def three_paths(neighbors):
    """Explicit list of simple 3-paths, grouped by ordered endpoints."""
    grouped = defaultdict(list)
    for u in range(len(neighbors)):
        for b in neighbors[u]:
            for c in neighbors[b]:
                if c == u:
                    continue
                for v in neighbors[c]:
                    if v not in (b, u):
                        grouped[(u, v)].append((b, c))
    return grouped


def definition_level_k2(neighbors):
    """sum P3^2, 12*C6 as internally disjoint path pairs, Theta by definition."""
    grouped = three_paths(neighbors)
    p3 = sum(len(row) for row in grouped.values())
    squares = sum(len(row) ** 2 for row in grouped.values())
    disjoint = sharing = 0
    for row in grouped.values():
        for i, (b, c) in enumerate(row):
            for j, (b2, c2) in enumerate(row):
                if i == j:
                    continue
                if {b, c} & {b2, c2}:
                    sharing += 1
                else:
                    disjoint += 1
    return p3, squares, disjoint, sharing


def random_graph(n, p, rng):
    rows = [set() for _ in range(n)]
    for u, v in combinations(range(n), 2):
        if rng.random() < p:
            rows[u].add(v)
            rows[v].add(u)
    return tuple(frozenset(r) for r in rows)


def nb_walks(neighbors, length):
    """Direct count of non-backtracking walks with `length` edges."""
    frontier = [(u, w) for u in range(len(neighbors)) for w in neighbors[u]]
    for _ in range(length - 1):
        nxt = []
        for prev, cur in frontier:
            for w in neighbors[cur]:
                if w != prev:
                    nxt.append((cur, w))
        frontier = nxt
    return len(frontier)


class KikuchiEncodingTests(unittest.TestCase):
    def test_labels_match_accepted_w32_models(self):
        for scheme in ("lex", "reverse-line"):
            ours = gq_pair_model(1, scheme)
            accepted = pair_labeled_symplectic(1, scheme)
            self.assertEqual(ours["left_labels"], accepted["left_labels"])
            self.assertEqual(ours["right_labels"], accepted["right_labels"])
            self.assertEqual(ours["incidences"], accepted["incidences"])

    def test_w32_d6_and_q4_equal_proper_cycles(self):
        expected = {"lex": (15, 50), "reverse-line": (3, 32)}
        for scheme, (d6, q4) in expected.items():
            model = pair_labeled_symplectic(1, scheme)
            census = seven_census(model, independent_checks=True)
            self.assertEqual(census["seven_class_motif_counts"]["D6"], d6)
            self.assertEqual(census["Q4"], q4)
            ours = gq_pair_model(1, scheme)
            g = kikuchi_graph(ours)
            self.assertEqual(six_cycle_census(g, 6)["proper_D6"], d6)
            self.assertEqual(proper_six_cycles_pruned(g, 6), d6)
            self.assertEqual(codegree_profile(g, 6)["proper_C4_Q4"], q4)

    def test_w32_seeded_bijections_against_seven_census(self):
        rng = random.Random(230)
        for _ in range(12):
            left = list(PAIRS6)
            right = list(PAIRS6)
            rng.shuffle(left)
            rng.shuffle(right)
            model = s2_model_with(left, right)
            census = seven_census(model, independent_checks=False)
            c4 = exact_coincident_c4(model, witness_limit=0)["Q4"]
            ours = labeled_model(2, 6, model["incidences"], left, right)
            g = kikuchi_graph(ours)
            cyc = six_cycle_census(g, 6)
            self.assertEqual(cyc["proper_D6"],
                             census["seven_class_motif_counts"]["D6"])
            self.assertEqual(proper_six_cycles_pruned(g, 6), cyc["proper_D6"])
            self.assertEqual(codegree_profile(g, 6)["proper_C4_Q4"], c4)

    def test_s4_against_independent_left_cycle_join(self):
        for scheme, seed in (("lex", None), ("random", 20261011)):
            model = gq_pair_model(2, scheme, seed)
            oracle = dict(model, s=4, h=2)
            d6 = exact_coincident_c6(oracle, witness_limit=0)[
                "exact_coincident_C6_factor_matchings_D"]
            q4 = exact_coincident_c4(oracle, witness_limit=0)["Q4"]
            g = kikuchi_graph(model)
            self.assertEqual(proper_six_cycles_pruned(g, model["a"]), d6)
            self.assertEqual(six_cycle_census(g, model["a"])["proper_D6"], d6)
            self.assertEqual(codegree_profile(g, model["a"])["proper_C4_Q4"], q4)

    def test_graph_is_simple_with_2N_edges(self):
        for power in (1, 2, 3):
            model = gq_pair_model(power, "lex")
            g = kikuchi_graph(model)
            self.assertEqual(len(g), model["a"] ** 2)
            self.assertEqual(sum(map(len, g)), 4 * model["N"])
            cert = exact_gq_certificate(power)
            self.assertEqual(cert["incidences"], model["N"])


class CoincidenceIdentityTests(unittest.TestCase):
    def test_k2_on_dense_random_graphs(self):
        rng = random.Random(7)
        for _ in range(40):
            g = random_graph(rng.randint(5, 10), rng.choice((0.3, 0.6, 1.0)), rng)
            p3, squares, disjoint, sharing = definition_level_k2(g)
            profile = path3_profile(g)
            cod = codegree_profile(g)
            self.assertEqual(profile["P3"], p3)
            self.assertEqual(profile["sum_P3_squared"], squares)
            self.assertEqual(cod["Theta"], sharing)
            # every six-cycle is exactly 12 ordered internally disjoint pairs
            self.assertEqual(disjoint, 12 * six_cycle_census(g, len(g))["C6"])

    def test_k2_on_true_w32_and_s4_kikuchi_graphs(self):
        for power, scheme, seed in ((1, "lex", None), (1, "reverse-line", None),
                                    (2, "random", 5)):
            g = kikuchi_graph(gq_pair_model(power, scheme, seed))
            p3, squares, disjoint, sharing = definition_level_k2(g)
            self.assertEqual(codegree_profile(g)["Theta"], sharing)
            self.assertEqual(squares, p3 + disjoint + sharing)
            self.assertEqual(disjoint % 12, 0)

    def test_ahl_and_peeling_on_random_graphs(self):
        rng = random.Random(11)
        for _ in range(60):
            g = random_graph(rng.randint(6, 12), rng.choice((0.35, 0.5, 0.8)), rng)
            n_core, m_core = two_core(g)
            lower = ahl_nb3_lower(g)
            self.assertGreaterEqual(nb_walks(g, 3), lower)
            m = sum(map(len, g)) // 2
            if 2 * m >= 3 * len(g):
                d = Fraction(2 * m, len(g))
                self.assertGreaterEqual(lower, 2 * m * (d - 1) ** 2)
            if n_core:
                self.assertGreaterEqual(2 * m_core, 2 * n_core)

    def test_conditional_floor_and_a_priori_table(self):
        stats = kikuchi_statistics(gq_pair_model(2, "random", 3))
        self.assertTrue(stats["K2_identity_verified"])
        self.assertLessEqual(Fraction(stats["conditional_D6_floor"]),
                             stats["proper_D6"])
        table = a_priori_table(range(1, 5))
        self.assertEqual([row["a"] for row in table], [6, 14, 35, 94])
        for row in table:
            s, N, a = row["s"], row["N"], row["a"]
            d = Fraction(4 * N, a * a)
            self.assertAlmostEqual(row["mu0"], float(4 * N * (d - 1) ** 2 / a ** 4))
        self.assertGreater(table[2]["mu0"], 3.6)
        self.assertGreater(table[3]["mu0"], 4.0)


class AdversaryAndGuardTests(unittest.TestCase):
    def test_greedy_adversary_is_legal_and_monotone(self):
        model = gq_pair_model(2, "random", 11)
        run = greedy_d6_adversary(model, 6, 11)
        final = run["final_model"]
        self.assertLessEqual(run["final_D6"], run["start_D6"])
        self.assertEqual(len(set(final["left_labels"])), final["v_left"])
        self.assertEqual(len(set(final["right_labels"])), final["v_right"])
        g = kikuchi_graph(final)
        self.assertEqual(six_cycle_census(g, final["a"])["proper_D6"],
                         run["final_D6"])

    def test_fail_closed(self):
        inc = ((0, 0), (1, 1))
        with self.assertRaises(ValueError):
            labeled_model(2, 6, inc, ((0, 1), (0, 1)), ((0, 1), (2, 3)))
        with self.assertRaises(ValueError):
            labeled_model(2, 6, inc, ((0, 1), (1, 0)), ((0, 1), (2, 3)))
        with self.assertRaises(ValueError):
            labeled_model(2, 6, inc, ((0, 1), (0, 6)), ((0, 1), (2, 3)))
        with self.assertRaises(ValueError):
            labeled_model(2, 6, ((0, 0), (0, 0)), ((0, 1), (2, 3)), ((0, 1), (2, 3)))
        with self.assertRaises(ValueError):
            labeled_model(2, 6, ((0, 2),), ((0, 1), (2, 3)), ((0, 1), (2, 3)))
        with self.assertRaises(ValueError):
            gq_pair_model(4, "lex")
        with self.assertRaises(ValueError):
            gq_pair_model(1, "coordinate-flag")
        with self.assertRaises(ValueError):
            gq_pair_model(1, "random")
        with self.assertRaises(ValueError):
            a_priori_p3_floor(10, 6)
        with self.assertRaises(RuntimeError):
            six_cycle_census(kikuchi_graph(gq_pair_model(1, "lex")), 6, max_cycles=5)
        with self.assertRaises(ValueError):
            greedy_d6_adversary(gq_pair_model(1, "lex"), -1, 0)


if __name__ == "__main__":
    unittest.main()
