"""C6 independent Johnson energy, 8! common-map, and transposition falsifiers."""
from fractions import Fraction
from itertools import combinations,permutations
from collections import Counter
from math import comb
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1a_fixed_leading import _two_factors_K6
from hyp105_g5e2b3e1c0_weighted_overlap import source_weighted_BA_hypergraph
from hyp105_g5e2b3e1c5_common_bijection import (
    common_bijection_moments,fixed_map_overlap,physical_occupied_target,
)
from hyp105_g5e2b3e1c6_johnson_variance import (
    johnson_sixset_energies,common_permutation_harmonic_variance,
)


def independent_brute_marginal_squares(w,V):
    """No use of production binomial-inversion source algorithm."""
    out=[]
    for k in range(7):
        marg=Counter()
        for R,v in w.items():
            for Q in combinations(sorted(R),k):
                marg[Q]+=v
        out.append(sum(v*v for v in marg.values()))
    return tuple(out)


class JohnsonVarianceC6Tests(unittest.TestCase):
    def test_exact_johnson_orthogonal_norms_from_independent_small_dense_vectors(self):
        for V in (7,8,9,12,15):
            sixsets=tuple(combinations(range(V),6))
            src={frozenset(S):i%5+1 for i,S in enumerate(sixsets)
                 if i%4!=0}
            x=johnson_sixset_energies(src,V)
            self.assertEqual(x["squared_marginal_moments"],
                             independent_brute_marginal_squares(src,V))
            self.assertEqual(sum(x["squared_J_r_norms"]),
                             sum(v*v for v in src.values()))
            self.assertEqual(x["W0_squared_norm"],
                             Fraction(sum(src.values())**2,comb(V,6)))
            self.assertTrue(all(v>=0 for v in x["squared_J_r_norms"]))
            self.assertEqual(
                x["irreducible_dimensions"],
                tuple(comb(V,r)-comb(V,r-1) if r else 1
                      for r in range(min(6,V-6)+1)))
            for k in range(min(6,V-6)+1):
                self.assertEqual(
                    sum(comb(6-r,k-r)*comb(V-k-r,6-k)*
                        x["squared_J_r_norms"][r] for r in range(k+1)),
                    x["squared_marginal_moments"][k])

    def test_exact_8factorial_one_common_pi_variance_and_random_swap_dirichlet(self):
        palette=tuple(combinations(range(6),2))
        cycle=_two_factors_K6()[0]
        F=tuple(cycle)+tuple(e for e in palette if e not in cycle)[:2]
        target=physical_occupied_target(6,F)
        src={frozenset((0,1,2,3,4,5)):3,
             frozenset((0,1,2,3,4,6)):2,
             frozenset((0,1,2,3,6,7)):4,
             frozenset((0,2,3,4,5,7)):1}
        cert=common_permutation_harmonic_variance(src,target,8)
        vals={}
        for pi in permutations(range(8)):
            vals[pi]=fixed_map_overlap(src,target,pi)
        self.assertEqual(len(vals),40320)
        m=Fraction(sum(vals.values()),len(vals))
        var=sum((Fraction(v)-m)**2 for v in vals.values())/len(vals)
        self.assertEqual(cert["mean_one_common_pi"],m)
        self.assertEqual(cert["variance_one_common_pi"],var)
        swap_half=Fraction(0)
        swaps=tuple(combinations(range(8),2))
        # Independently enumerate 8! * C(8,2) actual pair changes.
        for pi,value in vals.items():
            for i,j in swaps:
                p=list(pi)
                p[i],p[j]=p[j],p[i]
                diff=vals[tuple(p)]-value
                swap_half+=diff*diff
        swap_half=swap_half/(2*len(vals)*len(swaps))
        self.assertEqual(cert["random_swap_dirichlet_half_mean_square"],
                         swap_half)
        self.assertGreaterEqual(cert["variance_one_common_pi"],0)
        self.assertEqual(
            cert["variance_one_common_pi"],
            sum(cert["per_degree_variance_contribution"]))
        self.assertTrue(cert["independent_global_moment_agreement"])
        self.assertFalse(cert["all_correlated_g_lower_proved"])

    def test_full_W32_real_GQ_target_low_harmonic_energy_and_two_fixed_maps(self):
        F=tuple(combinations(range(6),2))
        target=physical_occupied_target(6,F)
        t=johnson_sixset_energies({R:1 for R in target},15)
        self.assertEqual(t["squared_J_r_norms"][0],Fraction(70*70,5005))
        self.assertEqual(t["squared_J_r_norms"][1],0)
        self.assertEqual(t["squared_J_r_norms"][2],Fraction(42,11))
        self.assertEqual(t["squared_J_r_norms"][3],Fraction(710,1001))
        self.assertEqual(
            sum(t["squared_J_r_norms"][4:]),Fraction(4966,77))
        index={e:i for i,e in enumerate(F)}
        for label in ("lex","reverse-line"):
            model=pair_labeled_symplectic(1,label)
            source=source_weighted_BA_hypergraph(model)
            c=common_permutation_harmonic_variance(source,target,15)
            self.assertTrue(c["W1_target_zero"])
            self.assertEqual(c["mean_one_common_pi"],
                             Fraction(5000*70,5005))
            self.assertEqual(c["per_degree_variance_contribution"][0],0)
            g=tuple(index[e] for e in model["right_labels"])
            U=fixed_map_overlap(source,target,g)
            self.assertLessEqual(
                (Fraction(U)-c["mean_one_common_pi"])**2,
                c["deterministic_fixed_g_cauchy_error_squared_upper"])
            if label=="reverse-line":
                self.assertEqual(U,77)
                g=list(g)
                g[4],g[13]=g[13],g[4]
                self.assertEqual(fixed_map_overlap(source,target,g),57)
                self.assertLessEqual(
                    (Fraction(57)-c["mean_one_common_pi"])**2,
                    c["deterministic_fixed_g_cauchy_error_squared_upper"])
            self.assertFalse(c["all_correlated_g_lower_proved"])

    def test_W1_nonzero_when_physical_occupied_image_breaks_target_symmetry(self):
        palette=tuple(combinations(range(6),2))
        T=_two_factors_K6()[0]
        F=tuple(T)+tuple(e for e in palette if e not in T)[:2]
        target=physical_occupied_target(6,F)
        h=johnson_sixset_energies({R:1 for R in target},8)
        self.assertGreater(h["squared_J_r_norms"][1],0)
        # Full K6 target instead is 1-design (zero W1).
        full=physical_occupied_target(6,palette)
        self.assertTrue(johnson_sixset_energies({R:1 for R in full},15)["W1_zero"])

    def test_generic_onehot_fixed_map_minimum_does_not_follow_from_spectra(self):
        palette=tuple(combinations(range(6),2))
        T=physical_occupied_target(6,palette)
        inT=next(iter(T))
        notT=next(frozenset(R) for R in combinations(range(15),6)
                  if frozenset(R) not in T)
        left=common_permutation_harmonic_variance({inT:1},T,15)
        right=common_permutation_harmonic_variance({notT:1},T,15)
        self.assertEqual(left,right)
        identity=tuple(range(15))
        self.assertEqual(fixed_map_overlap({inT:1},T,identity),1)
        self.assertEqual(fixed_map_overlap({notT:1},T,identity),0)

    def test_invalid_source_fails_closed(self):
        with self.assertRaises(ValueError):
            johnson_sixset_energies({frozenset(range(5)):1},15)
        with self.assertRaises(ValueError):
            common_permutation_harmonic_variance(
                {frozenset(range(6)):-1},
                {frozenset(range(6))},15)


if __name__=="__main__":
    unittest.main()
