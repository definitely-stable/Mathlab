"""HYP-105 B8-F independent full K4 bijection falsifiers and rational dual tests."""
from fractions import Fraction
from itertools import combinations, permutations
import unittest

from hyp105_g5e2b3e1c24b8f_signed_star_gate import (
    projection_factor, evaluate_full_star_form,
    star_dual_lower_certificate, conditional_residual_gate,
)


def alternating_four_cycle(a):
    """Nontrivial zero-row signed weights, not imported from the gate."""
    n=a*(a-1)//2
    w={pair:Fraction(0) for pair in combinations(range(n),2)}
    w[(0,1)]=Fraction(3,2)
    w[(0,2)]=-Fraction(3,2)
    w[(1,3)]=-Fraction(3,2)
    w[(2,3)]=Fraction(3,2)
    return w


class SignedStarTests(unittest.TestCase):
    def test_exact_k4_full_bijection_exhaustive_not_local_search(self):
        a=4
        edges=tuple(combinations(range(a),2))
        w=alternating_four_cycle(a)
        cert=star_dual_lower_certificate(w,a,sweeps=4)
        self.assertEqual(cert["star_subset_count"],20)
        self.assertEqual(projection_factor(a),Fraction(3,5))
        observed=[]
        for assigned in permutations(edges):
            z=sum((w[i,j] for i,j in combinations(range(6),2)
                   if set(assigned[i]) & set(assigned[j])),Fraction(0))
            outcome=evaluate_full_star_form(w,assigned,a)
            self.assertEqual(outcome["signed_T"],z)
            self.assertEqual(outcome["pair_projection"],Fraction(3,5)*z)
            self.assertTrue(outcome["pairwise_star_intersections_exactly_one"])
            observed.append(z)
        self.assertEqual(len(observed),720)
        self.assertLessEqual(cert["certified_lower_T"],min(observed))
        self.assertLessEqual(cert["naive_lower_T"],cert["certified_lower_T"])
        self.assertEqual(cert["certified_lower_T"],
                         2*sum(cert["dual_y"],Fraction(0)) +
                         a*cert["minimum_reduced_star_cost"])
        self.assertEqual(tuple(sorted(cert["dual_sweep_history"])),
                         cert["dual_sweep_history"])

    def test_k6_bijection_and_zero_weight_equality(self):
        a=6
        n=15
        w={p:Fraction(0) for p in combinations(range(n),2)}
        c=star_dual_lower_certificate(w,a,sweeps=1)
        self.assertEqual(c["star_subset_count"],3003)
        self.assertEqual(c["certified_lower_T"],0)
        self.assertEqual(c["certified_lower_pair_projection"],0)
        edges=tuple(combinations(range(a),2))
        self.assertEqual(evaluate_full_star_form(w,edges,a)["signed_T"],0)
        self.assertEqual(projection_factor(6),Fraction(6,7))

    def test_k6_nontrivial_and_coordinate_rename_invariance(self):
        a=6
        edges=tuple(combinations(range(a),2))
        w=alternating_four_cycle(a)
        images=edges[::-1]
        x=evaluate_full_star_form(w,images,a)
        renamed=tuple(tuple(sorted(((u+1)%a,(v+1)%a))) for u,v in images)
        self.assertEqual(evaluate_full_star_form(w,renamed,a)["signed_T"],
                         x["signed_T"])
        cert=star_dual_lower_certificate(w,a,sweeps=2)
        self.assertLessEqual(cert["certified_lower_T"],x["signed_T"])
        self.assertGreaterEqual(cert["certified_lower_T"],cert["naive_lower_T"])

    def test_gate_is_conditional_not_an_unproved_r3_conclusion(self):
        c=conditional_residual_gate(Fraction(10,3),Fraction(-15,2))
        self.assertEqual(c["residual_lower_needed_for_strict_positive"],
                         Fraction(25,6))
        self.assertTrue(c["requires_independent_all_g_pointwise_residual_bound"])
        self.assertTrue(c["is_conditional_not_an_accepted_score_lower"])
        with self.assertRaises(ValueError):
            conditional_residual_gate(0.1,2)

    def test_fail_closed_invalid_or_non_row_zero_influences_and_maps(self):
        weights=alternating_four_cycle(4)
        edges=tuple(combinations(range(4),2))
        with self.assertRaisesRegex(ValueError,"zero rows"):
            weights[(0,1)]+=1
            star_dual_lower_certificate(weights,4)
        weights=alternating_four_cycle(4)
        with self.assertRaises(ValueError):
            star_dual_lower_certificate(weights,4,sweeps=-1)
        with self.assertRaises(ValueError):
            evaluate_full_star_form(weights,edges[:-1]+(edges[0],),4)
        with self.assertRaises(ValueError):
            star_dual_lower_certificate({},4)
        with self.assertRaises(ValueError):
            projection_factor(3)


if __name__=="__main__":
    unittest.main()
