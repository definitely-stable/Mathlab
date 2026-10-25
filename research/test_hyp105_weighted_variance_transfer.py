"""AA4-VT: real W(3,2) fixed-map sign counterexamples and centered transfer."""
import unittest
from fractions import Fraction

from hyp105_weighted_variance_transfer import (
    _geometry, _physical_adj, centered_transfer,
    deterministic_k6_edges, witness_maps, w32_weighted_census,
)


class TestWeightedVarianceTransfer(unittest.TestCase):
    def test_both_covariance_signs_on_genuine_w32(self):
        # Both maps are complete typed globally injected f,g in K6.
        # They are deterministic full-size maps, not simulated averages.
        known = (
            # seed: bad_pairs, valid_walks, bad_walks, second_moment, diff_U
            (41, 145, 986, 822, 8612, 4990),
            (91, 146, 860, 636, 6312, -11080),
        )
        for seed, b, P, M, Q, diff in known:
            with self.subTest(seed=seed):
                f, g = witness_maps(seed)
                result = w32_weighted_census(f, g, verify_corner_join=True)
                self.assertEqual(result["U"], 180)
                self.assertEqual((result["b"], result["P"], result["M"],
                                  result["Q"]), (b, P, M, Q))
                self.assertEqual(result["deviation_numerator"], diff)
                self.assertGreaterEqual(result["exact_cauchy_slack"], 0)
                self.assertEqual(result["covariance"],
                                 Fraction(diff, 180 * 180))
                self.assertEqual(result["sign"], 1 if diff > 0 else -1)
                self.assertEqual(result["max_N3"], 18)
                self.assertTrue(result["chi_square"] > 0)

    def test_lex_complete_labeling_negative_sign(self):
        edges = deterministic_k6_edges(0)
        # A canonical lexicographic full K6 mapping, no randomness.
        lex = tuple((i, j) for i in range(6) for j in range(i+1, 6))
        self.assertEqual(len(set(edges)), 15)
        result = w32_weighted_census(lex, lex)
        self.assertEqual((result["b"], result["P"], result["M"],
                          result["Q"]), (153, 946, 786, 7604))
        self.assertEqual(result["deviation_numerator"], -3258)

    def test_exact_centered_variance_and_equality_case(self):
        result = centered_transfer(4, 2, 2, 2, 0)
        self.assertEqual(result["exact_cauchy_slack"], 0)
        self.assertEqual(result["chi_square"], Fraction(1))
        self.assertEqual(result["weighted_minus_unweighted_fraction"],
                         Fraction(-1, 2))
        with self.assertRaises(ValueError):
            centered_transfer(4, 2, 2, 0, 0)
        with self.assertRaises(ValueError):
            centered_transfer(4, 2, 2, 2, 3)
        with self.assertRaises(ValueError):
            centered_transfer(4, 2, 2, 2, 1.0)

    def test_tensor_reconstruction_and_absence_of_parallel_arcs(self):
        flags, _ = _geometry()
        f, g = witness_maps(41)
        adj = _physical_adj(f, g, flags)
        # Every genuine incidence contributes exactly two undirected arcs,
        # hence four directed matrix entries; no collisions under f/g injection.
        self.assertEqual(sum(map(len, adj.values())), 4 * len(flags))
        f_inverse = {frozenset(x): i for i, x in enumerate(f)}
        g_inverse = {frozenset(x): i for i, x in enumerate(g)}
        incidence = set(flags)
        for u in range(6):
            for x in range(6):
                a = (u, x)
                self.assertEqual(len(adj.get(a, ())), len(set(adj.get(a, ()))))
                for v in range(6):
                    for y in range(6):
                        b = (v, y)
                        p = f_inverse.get(frozenset((u, v))) if u != v else None
                        l = g_inverse.get(frozenset((x, y))) if x != y else None
                        expected = (p, l) in incidence if p is not None and l is not None else False
                        self.assertEqual(b in adj.get(a, ()), expected)

    def test_physical_coordinate_permutations_preserve_sign(self):
        f, g = witness_maps(91)
        base = w32_weighted_census(f, g)
        new_f = [tuple(sorted(((5*x + 1) % 6, (5*y + 1) % 6))) for x, y in f]
        new_g = [tuple(sorted(((5*x + 2) % 6, (5*y + 2) % 6))) for x, y in g]
        permuted = w32_weighted_census(new_f, new_g)
        self.assertEqual(permuted, base)

    def test_invalid_typed_maps_fail_closed(self):
        f, g = witness_maps(41)
        bad_f = list(f)
        bad_f[0] = bad_f[1]
        with self.assertRaises(ValueError):
            w32_weighted_census(bad_f, g)
        with self.assertRaises(ValueError):
            witness_maps(-1)

    def test_existing_w34_ledger_centered_cauchy(self):
        result = centered_transfer(6800, 4086, 58730, 676700, 35616)
        self.assertEqual(result["deviation_numerator"],
                         35616*6800-4086*58730)
        self.assertGreaterEqual(result["exact_cauchy_slack"], 0)
        self.assertEqual(result["chi_square"],
                         Fraction(6800*676700, 58730**2)-1)


if __name__ == "__main__":
    unittest.main()
