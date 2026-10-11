"""C24-A1 independent original-W32 left-first/right-first and swap falsifiers."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
from math import comb
import unittest

from hyp105_g5e2b3e1c24_right_c_certificate import (
    K6_PAIRS, W32_RIGHT_C_ZERO_WITNESS, original_W32,
    symplectic_form_gf2, W32_right_C_source, right_C_pair_weights,
    degree_two_on_six_coordinates, accepted_right_C,
    exact_star_collision_upper, star_collision_certificate,
    all_h_star_geometry_fraction, rigorous_centered_norm_upper,
    uniform_right_C_certificate, genuine_W32_C24_report,
)


def independent_left_first_W32_right_C():
    """Enumerate 62,370 original sixsets from full physical K6 2-factor source.

    For physical point-edge occurrence 1 choose one of three incidences;
    for occurrence 2 choose two distinct ORIGINAL incidence IDs.
    The generator does NOT call the right-first C24 source/compiler.
    """
    points, lines, _ = original_W32()
    rights = {p: tuple(i for i, line in enumerate(lines) if p in line)
              for p in points}
    right_C = Counter()
    total = 0
    profiles = Counter()
    for physical in combinations_with_replacement(range(15), 6):
        if not degree_two_on_six_coordinates(K6_PAIRS[k] for k in physical):
            continue
        counts = Counter(physical)
        groups = sorted(counts)
        picks = [tuple(combinations(rights[points[k]], counts[k]))
                 for k in groups]
        for assignment in product(*picks):
            total += 1
            profiles[tuple(sorted(counts.values(), reverse=True))] += 1
            right = Counter(j for group in assignment for j in group)
            if tuple(sorted(right.values())) == (2, 2, 2):
                right_C[tuple(sorted(right))] += 1
    return total, profiles, right_C


class C24RightCStarCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.triples = W32_right_C_source()
        cls.W = right_C_pair_weights(cls.triples, 15)

    def test_true_original_W32_host(self):
        pts, lines, incidences = original_W32()
        self.assertEqual((len(pts), len(lines), len(incidences)), (15, 15, 45))
        self.assertEqual(len(set(incidences)), 45)
        self.assertTrue(all(symplectic_form_gf2(p, q) == 0
                            for line in lines for p, q in combinations(line, 2)))

    def test_independent_left_first_62370_matches_right_first(self):
        total, profiles, source = independent_left_first_W32_right_C()
        self.assertEqual(total, 62370)
        self.assertEqual(profiles, {(1, 1, 1, 1, 1, 1): 51030,
                                    (2, 1, 1, 1, 1): 10935,
                                    (2, 2, 2): 405})
        self.assertEqual(source, self.triples)
        self.assertEqual((sum(source.values()), len(source)), (92, 83))

    def test_pair_tensor_sum_mu_and_norm_bound(self):
        self.assertEqual(sum(self.W[i][j] for i in range(15)
                             for j in range(i + 1, 15)), 276)
        self.assertEqual(max(max(row) for row in self.W), 7)
        norm_upper, mu = rigorous_centered_norm_upper(self.W, 92)
        self.assertEqual(mu, Fraction(92, 35))
        self.assertGreaterEqual(norm_upper, 0)

    def test_complete_global_witness_right_C_zero(self):
        perm = W32_RIGHT_C_ZERO_WITNESS
        self.assertEqual(sorted(perm), list(range(15)))
        self.assertEqual(accepted_right_C(self.triples, perm, K6_PAIRS), 0)
        witness = star_collision_certificate(self.triples, self.W,
                                             perm, K6_PAIRS)
        self.assertEqual(witness["H_C"], 92)
        self.assertEqual(witness["accepted_right_C"], 0)
        self.assertGreaterEqual(witness["star_conflict_upper"], 92)
        self.assertEqual(witness["certified_lower"], 0)
        self.assertEqual(genuine_W32_C24_report()["global_uniform_right_C_mean"],
                         "276/91")

    def test_105_genuine_complete_global_right_transpositions(self):
        perm = list(W32_RIGHT_C_ZERO_WITNESS)
        for i, j in combinations(range(15), 2):
            swapped = list(perm)
            swapped[i], swapped[j] = swapped[j], swapped[i]
            count = accepted_right_C(self.triples, swapped, K6_PAIRS)
            collisions = exact_star_collision_upper(self.W, swapped, K6_PAIRS)
            self.assertGreaterEqual(count, 92 - collisions)
            self.assertEqual(count, star_collision_certificate(
                self.triples, self.W, swapped, K6_PAIRS)["accepted_right_C"])

    def test_all_h_geometry_and_explicit_nontransfer(self):
        self.assertEqual(all_h_star_geometry_fraction(15, 6),
                         Fraction(-5, 7))
        for s in (2, 4, 8, 16, 32, 64, 128):
            V = (s + 1) * (s * s + 1)
            a = next(a for a in range(3, 4000) if comb(a, 2) >= V)
            self.assertEqual(all_h_star_geometry_fraction(V, a),
                             1 - Fraction(6 * (a - 2), V - 1))
        cert = uniform_right_C_certificate(self.W, 92, 6)
        self.assertEqual(cert["nonnegative_certified_lower"], 0)
        self.assertFalse(cert["is_universal_positive_proof"])

    def test_malformed_injections_fail_closed(self):
        with self.assertRaises(ValueError):
            accepted_right_C(self.triples, (0,) * 15, K6_PAIRS)
        with self.assertRaises(ValueError):
            accepted_right_C(self.triples, tuple(range(14)), K6_PAIRS)
        with self.assertRaises(ValueError):
            all_h_star_geometry_fraction(15, 5)
        with self.assertRaises(ValueError):
            right_C_pair_weights({(0, 1, 1): 1}, 15)
        with self.assertRaises(ValueError):
            rigorous_centered_norm_upper(((0, 0), (0, 0)), 1)


if __name__ == "__main__":
    unittest.main()
