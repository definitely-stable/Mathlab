"""Independent finite falsifiers of a density-only 3-codegree-clique inference."""
from fractions import Fraction
from math import comb
import unittest

from hyp105_codegree_clique_density_nogo import (
    projective_plane_prime,projective_triangle_count_exact,
    projective_nogo_certificate,density_threshold_symbolic,
)
from hyp105_independent_codegree_c6_source_referee import (
    bipartite_c6_direct_six_vertex_oracle,
)


class DensityOnlyCodegreeCliqueNoGo(unittest.TestCase):
    def test_projective_plane_fano_three_independent_cycle_oracles(self):
        report=projective_nogo_certificate(2,direct_small=True)
        self.assertEqual(report["v"],14)
        self.assertEqual(report["e"],21)
        self.assertEqual(report["exact_C6"],28)
        self.assertEqual(report["max_left_pair_codegree"],1)
        self.assertEqual(report["positive_codegree_local_lower"],0)
        self.assertFalse(report["local_k_ge_3_codegree_clique_exists"])

    def test_pg2_three_independent_oracles_and_234_cycles(self):
        report=projective_nogo_certificate(3,direct_small=True)
        self.assertEqual(report["v"],26)
        self.assertEqual(report["e"],52)
        self.assertEqual(report["exact_C6"],234)
        self.assertEqual(report["max_left_pair_codegree"],1)

    def test_actual_prime_plane_incidence_for_p2_p3_p5_p7_p11(self):
        counts={2:28,3:234,5:3875,7:26068}
        for p in (2,3,5,7,11):
            with self.subTest(p=p):
                pg=projective_plane_prime(p)
                n=p*p+p+1
                self.assertEqual(pg["n_side"],n)
                self.assertEqual(len(pg["row_neighborhoods"]),n)
                self.assertEqual(pg["pairwise_left_codegrees"],frozenset({1}))
                self.assertTrue(all(row.bit_count()==p+1
                                    for row in pg["row_neighborhoods"]))
                report=projective_nogo_certificate(p)
                self.assertEqual(report["exact_C6"],projective_triangle_count_exact(p))
                self.assertEqual(report["exact_C6"],
                                 comb(n,3)-n*comb(p+1,3))
                self.assertEqual(report["positive_codegree_local_lower"],0)
                self.assertGreater(report["exact_C6"],0)
                if p in counts:self.assertEqual(report["exact_C6"],counts[p])

    def test_exact_unbounded_balanced_density_symbolic_lower_p_over16(self):
        for p in (2,3,5,7,11,17,23,31,53,101):
            with self.subTest(p=p):
                result=density_threshold_symbolic(p,Fraction(1,4))
                self.assertTrue(result["exact_balanced_edge_threshold_met"])
                self.assertTrue(result["sufficient_p_ge16C3"])
                self.assertGreaterEqual(result["ratio_e3_over_v4"],Fraction(p,16))
                self.assertTrue(result["does_not_constrain_original_source_selected_graphs"])
        # Witness an ACTUAL graph threshold with trial C=1; p17 is
        # enough, without assuming C=1 is the published SS6 constant.
        self.assertFalse(density_threshold_symbolic(7,1)["exact_balanced_edge_threshold_met"])
        self.assertTrue(density_threshold_symbolic(17,1)["exact_balanced_edge_threshold_met"])

    def test_arbitrarily_large_prime_symbolic_argument_no_GQ_claim(self):
        # For every positive real C, any prime p>=16*C^3 suffices:
        # e^3/v^4 >= p/16 >= C^3 while ALL pair codegrees equal 1.
        # Euclid guarantees arbitrarily large primes. Finite tests
        # check exact integer/rational identity only.
        for C,p in ((Fraction(1,2),3),(1,17),(Fraction(3,2),59),(2,131)):
            with self.subTest(C=C,p=p):
                d=density_threshold_symbolic(p,C)
                self.assertTrue(d["sufficient_p_ge16C3"])
                self.assertTrue(d["exact_balanced_edge_threshold_met"])
        self.assertEqual(
            projective_nogo_certificate(7)["scale"],
            "ordinary simple bipartite graphs, NOT original W(3,2^h) maps")

    def test_projective_incidence_vector_normalization_is_unique(self):
        for p in (2,3,5,7):
            pg=projective_plane_prime(p)
            vectors=pg["normalized_projective_vectors"]
            self.assertEqual(len(set(vectors)),p*p+p+1)
            self.assertTrue(all(any(v) and next(x for x in v if x)==1
                                for v in vectors))
            self.assertTrue(all(
                sum(v[i]*line[i] for i in range(3))%p==0
                for j,v in enumerate(vectors)
                for k,line in enumerate(vectors)
                if (pg["row_neighborhoods"][j]>>k)&1))

    def test_invalid_nonprime_or_nonpositive_graph_constants_fail_closed(self):
        for p in (0,1,4,6,8,9,15,21,2.0,True,None,"5"):
            with self.subTest(p=p):
                with self.assertRaises(ValueError):
                    projective_plane_prime(p)
                with self.assertRaises(ValueError):
                    density_threshold_symbolic(p,1)
        for C in (0,-1,False,0.5,None,"1"):
            with self.subTest(C=C):
                with self.assertRaises(ValueError):
                    density_threshold_symbolic(5,C)


if __name__=="__main__":
    unittest.main()
