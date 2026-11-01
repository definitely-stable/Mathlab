"""Adversarial independently recomputed original-W(3,s) path covariance tests."""
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial
import unittest

from hyp105_real_source_negative_path_covariance_referee import (
    P, Q, complete_labels, minimal_a, original_three_matching,
    labelled_original_source, original_edge_owners, path_owners,
    original_conflicts, pair_local_minima_probability,
    two_color_probability, cut_probabilities,
    real_source_covariance_certificate,
)


class RealOriginalSourceCovarianceReferee(unittest.TestCase):
    def test_true_W32_W34_complete_correlated_source_and_physical_provenance(self):
        for h in (1, 2):
            with self.subTest(h=h):
                s, v, flags, f, g, triple = labelled_original_source(h)
                self.assertEqual(v, (s+1)*(s*s+1))
                self.assertEqual(len(flags), (s+1)*v)
                self.assertEqual(len(set(f)), v)
                self.assertEqual(len(set(g)), v)
                self.assertEqual(path_owners(P, original_edge_owners(flags, f, g)),
                                 triple[:2])
                self.assertEqual(path_owners(Q, original_edge_owners(flags, f, g)),
                                 triple[1:])
                self.assertEqual(
                    {flags[i][0] for i in triple}.__len__(), 3)
                self.assertEqual(
                    {flags[i][1] for i in triple}.__len__(), 3)
                graph = original_conflicts(triple, flags, f, g)
                self.assertTrue(all(not graph[i] for i in triple))

    def test_exact_negative_covariance_both_actual_full_and_three_flag_core(self):
        for h in (1, 2):
            for full in (False, True):
                with self.subTest(h=h, full=full):
                    d = real_source_covariance_certificate(h, full_source=full)
                    self.assertEqual(d["physical_edges_full"], 2*d["N"])
                    self.assertEqual(d["typed_cut_P"], Fraction(1,16))
                    self.assertEqual(d["typed_cut_Q"], Fraction(1,16))
                    self.assertEqual(d["typed_cut_joint"], Fraction(0))
                    self.assertEqual(d["joint_survival"], 0)
                    self.assertGreater(d["path_P_marginal"], 0)
                    self.assertGreater(d["path_Q_marginal"], 0)
                    self.assertEqual(
                        d["covariance"],
                        -d["path_P_marginal"]*d["path_Q_marginal"])
                    self.assertLess(d["covariance"], 0)
                    self.assertFalse(d["root_branch_a_refuted"])
                    self.assertFalse(d["external_qualified_review_completed"])
                    if not full:
                        self.assertEqual(d["source_priority_P"], 1)
                        self.assertEqual(d["source_priority_Q"], 1)
                        self.assertEqual(d["covariance"], Fraction(-1,256))

    def test_source_parity_formula_vs_independent_all_128_bit_colorings(self):
        for h in (1,2):
            _, _, flags, f, g, triple = labelled_original_source(h)
            actual, edges = cut_probabilities(f, g, flags, triple)
            lp, lq, rp, rq = edges
            self.assertEqual((lp, lq, rp, rq),
                             (((0,1),(1,2)), ((1,2),(0,2)),
                              ((0,1),(1,2)), ((1,2),(2,3))))
            self.assertEqual(two_color_probability(lp), Fraction(1,4))
            self.assertEqual(two_color_probability(lq), Fraction(1,4))
            self.assertEqual(two_color_probability(lp+lq), 0)
            self.assertEqual(two_color_probability(rp+rq), Fraction(1,8))
            self.assertEqual(actual, (Fraction(1,16), Fraction(1,16), 0))

    def test_exact_two_source_minimum_integral_vs_independent_orders(self):
        # Every labeled simple conflict graph on five IDs with (0,1) nonedge:
        # all 2^9=512 possibilities independently enumerated over 5!=120
        # STRICT priority orders, not relying on the integral calculation.
        n = 5
        edges = tuple(e for e in combinations(range(n),2) if e != (0,1))
        for mask in range(1<<len(edges)):
            graph = {i: set() for i in range(n)}
            for k, (i,j) in enumerate(edges):
                if mask>>k & 1:
                    graph[i].add(j)
                    graph[j].add(i)
            exact = pair_local_minima_probability(graph,0,1)
            count = 0
            for perm in permutations(range(n)):
                rank = {v:i for i,v in enumerate(perm)}
                if all(rank[t] < rank[w]
                       for t in (0,1) for w in graph[t]):
                    count += 1
            self.assertEqual(exact, Fraction(count,factorial(n)),
                             msg="conflict graph mask="+str(mask))

    def test_odd_triangle_is_a_genuine_allh_not_just_finite_witness(self):
        # Algebraic validation of the all-h extension hypotheses:
        # V>(4) for any s>=2 gives three independent source flags by
        # greedy incidence matching; a>=6 permits the 3+3 fixed labels.
        for h in range(1, 26):
            s = 1 << h
            v = (s+1)*(s*s+1)
            a = minimal_a(v)
            self.assertGreater(v, 4)
            self.assertGreater(v*(s+1), 4*(s+1))
            self.assertGreaterEqual(a, 6)
            self.assertGreaterEqual(a*(a-1)//2, v)
            self.assertLess((a-1)*(a-2)//2, v)

    def test_bad_source_inputs_fail_closed(self):
        with self.assertRaises(ValueError):
            minimal_a(14)
        with self.assertRaises(ValueError):
            complete_labels(4, 6, {0:(0,1),1:(0,1)})
        with self.assertRaises(ValueError):
            pair_local_minima_probability({0:{1},1:{0}},0,0)
        self.assertEqual(
            pair_local_minima_probability({0:{1},1:{0}},0,1), 0)
        self.assertEqual(two_color_probability(((0,1),(1,2),(0,2))), 0)


if __name__ == "__main__":
    unittest.main()
