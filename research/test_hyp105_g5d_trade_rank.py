"""Independent GF5 Gaussian/rank/probability adversarial tests."""
import unittest
from itertools import product
from fractions import Fraction
from random import Random
from hyp105_g5d_trade_rank import (
    gf5_rank, signed_trade_rank_report, trade_linear_system
)
from hyp105_g5d_affine_weights import checksum_pattern_palette


class G5DAffineRankTests(unittest.TestCase):
    def test_same_support_opposite_signs_exact_probabilities(self):
        supports = ((0, 1, 2, 3), (0, 1, 2, 3))
        r = signed_trade_rank_report(supports, (1, -1))
        self.assertEqual((r["t"], r["v"], r["components"]), (2, 4, 1))
        self.assertEqual((r["rank"], r["augmented_rank"]), (5, 5))
        self.assertEqual(r["affine_solution_count"], 125)
        self.assertEqual(r["full_affine_probability"], Fraction(1, 125))
        self.assertFalse(r["has_singleton_coordinate"])
        # Independent brute-force for each of 5^3 affine patterns
        allowed_zero = [
            (a, b, c, (4-a-b-c) % 5)
            for a,b,c in product(range(5), repeat=3)
        ]
        self.assertEqual(len(allowed_zero), 125)
        collisions = sum(x == y for x in allowed_zero for y in allowed_zero)
        self.assertEqual(Fraction(collisions, 125**2),
                         r["full_affine_probability"])
        nonzero = checksum_pattern_palette()
        positive_collisions = sum(x == y for x in nonzero for y in nonzero)
        self.assertEqual(Fraction(positive_collisions, 51**2),
                         Fraction(1, 51))
        self.assertLessEqual(Fraction(1, 51), r["nonzero_palette_upper"])

    def test_nonbalanced_components_and_singleton_eliminate_nonzero_trades(self):
        diff = signed_trade_rank_report(
            ((0,1,2,3), (4,5,6,7)), (1, -1))
        self.assertEqual(diff["components"], 2)
        self.assertFalse(diff["affine_consistent"])
        self.assertEqual(diff["full_affine_probability"], Fraction(0))
        overlap = signed_trade_rank_report(
            ((0,1,2,3), (0,1,4,5)), (1, -1))
        self.assertTrue(overlap["affine_consistent"])
        self.assertTrue(overlap["has_singleton_coordinate"])
        self.assertGreater(overlap["full_affine_probability"], 0)
        self.assertEqual(overlap["nonzero_palette_upper"], 0)

    def test_multiple_component_rank_and_rhs_consistency(self):
        a=(0,1,2,3)
        b=(4,5,6,7)
        r=signed_trade_rank_report((a,a,b,b), (1,-1,1,-1))
        self.assertEqual((r["t"],r["v"],r["components"]), (4,8,2))
        self.assertEqual(r["rank"],10)
        self.assertEqual(r["affine_solution_count"],5**6)
        self.assertEqual(r["full_affine_probability"],Fraction(1,5**6))
        bad=signed_trade_rank_report((a,a,b,b), (1,1,-1,-1))
        self.assertFalse(bad["affine_consistent"])
        self.assertNotEqual(bad["rank"],bad["augmented_rank"])

    def test_full_incidence_rank_falsification_on_held_out_supports(self):
        rng=Random(119590)
        for _ in range(80):
            t=rng.randrange(2,7)
            supports=tuple(tuple(sorted(rng.sample(range(12),4)))
                           for _ in range(t))
            signs=tuple(rng.choice((-1,1)) for _ in range(t))
            report=signed_trade_rank_report(supports,signs)
            matrix,rhs,coords,degree=trade_linear_system(supports,signs)
            self.assertEqual(gf5_rank(matrix),
                             t+len(coords)-report["components"])
            self.assertEqual(gf5_rank(tuple(
                row+[rhs[i]] for i,row in enumerate(matrix))),
                report["augmented_rank"])
            self.assertLessEqual(report["nonzero_palette_upper"],1)
        with self.assertRaises(ValueError):
            signed_trade_rank_report(((0,0,1,2),), (1,))
        with self.assertRaises(ValueError):
            signed_trade_rank_report(((0,1,2,3),), (0,))


if __name__=="__main__":
    unittest.main()
