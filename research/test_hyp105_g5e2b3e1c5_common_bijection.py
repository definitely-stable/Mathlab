"""Independent exact overlap census and full 8! COMMON right-map falsifiers."""
from collections import Counter
from fractions import Fraction
from itertools import combinations,permutations
from math import comb
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1a_fixed_leading import _two_factors_K6
from hyp105_g5e2b3e1c0_weighted_overlap import (
    exact_BA_overlap,source_weighted_BA_hypergraph,
)
from hyp105_g5e2b3e1c5_common_bijection import (
    sixset_intersection_spectrum,physical_occupied_target,
    occupied_target_uniform_floor,common_bijection_moments,
    fixed_map_overlap,validate_weighted_sixsets,
)


def brute_sixset_spectrum(weights):
    """Independent ordered Cartesian product, no marginal inversion."""
    answer=Counter()
    for R,w in weights.items():
        for S,z in weights.items():
            answer[len(R&S)]+=w*z
    return tuple(answer[j] for j in range(7))


def brute_occupied_target(a,F):
    """Independent C(V,6) physical degree2 scan, not 70 template generator."""
    target=set()
    for ids in combinations(range(len(F)),6):
        deg=Counter(v for i in ids for v in F[i])
        if len(deg)==6 and set(deg.values())=={2}:
            target.add(frozenset(ids))
    return frozenset(target)


class CommonBijectionC5Tests(unittest.TestCase):
    def test_overlap_intersection_moments_binary_inversion_vs_brute(self):
        for V in (7,8,10):
            subsets=list(combinations(range(V),6))
            weighted={frozenset(R):(i%7)+1 for i,R in enumerate(subsets)
                      if i%3!=1}
            cert=sixset_intersection_spectrum(weighted,V)
            self.assertEqual(cert["ordered_pair_overlap_spectrum"],
                             brute_sixset_spectrum(weighted))
            self.assertEqual(sum(cert["ordered_pair_overlap_spectrum"]),
                             cert["mass"]**2)
            self.assertEqual(cert["binomial_squared_marginal_moments"][0],
                             cert["mass"]**2)
            self.assertEqual(cert["binomial_squared_marginal_moments"][6],
                             sum(w*w for w in weighted.values()))

    def test_K6_K7_complete_occupied_physical_target_not_full_proxy(self):
        for a in (6,7):
            alphabet=tuple(combinations(range(a),2))
            deletions=((),alphabet[:1],alphabet[:3],
                       tuple(e for e in alphabet if e[0]==0 and e[1]>=2))
            for remove in deletions:
                F=tuple(e for e in alphabet if e not in remove)
                if len(F)<6: continue
                physical=physical_occupied_target(a,F)
                brute=brute_occupied_target(a,F)
                self.assertEqual(physical,brute)
                total=70*comb(a,6)
                degree=28*comb(a-2,4)
                self.assertGreaterEqual(
                    len(physical),max(0,total-len(remove)*degree))
                if not remove:self.assertEqual(len(physical),total)

    def test_one_shared_random_bijection_exact_mean_second_variance_8factorial(self):
        a=6
        palette=tuple(combinations(range(a),2))
        triangle_factor=_two_factors_K6()[0]
        F=tuple(triangle_factor)+tuple(
            e for e in palette if e not in triangle_factor)[:2]
        self.assertEqual(len(F),8)
        T=physical_occupied_target(a,F)
        self.assertEqual(T,brute_occupied_target(a,F))
        source={
            frozenset((0,1,2,3,4,5)):3,
            frozenset((0,1,2,3,4,6)):2,
            frozenset((0,1,2,3,6,7)):4,
            frozenset((0,2,3,4,5,7)):1,
        }
        cert=common_bijection_moments(source,T,8,retain_spectra=True)
        vals=[fixed_map_overlap(source,T,p) for p in permutations(range(8))]
        self.assertEqual(len(vals),40320)
        mean=Fraction(sum(vals),len(vals))
        second=Fraction(sum(x*x for x in vals),len(vals))
        self.assertEqual(cert["one_common_right_bijection_mean"],mean)
        self.assertEqual(cert["one_common_right_bijection_second_moment"],second)
        self.assertEqual(cert["one_common_right_bijection_variance"],
                         second-mean*mean)
        self.assertEqual(cert["source_ordered_overlap_spectrum"],
                         brute_sixset_spectrum(source))
        self.assertEqual(cert["target_ordered_overlap_spectrum"],
                         brute_sixset_spectrum({R:1 for R in T}))
        self.assertLessEqual(cert["one_common_right_bijection_positive_probability_lower"],
                             Fraction(sum(x>0 for x in vals),len(vals)))
        self.assertGreaterEqual(cert["one_common_right_bijection_zero_probability_Chebyshev_upper"],
                                Fraction(sum(x==0 for x in vals),len(vals)))

    def test_actual_GQ_W32_global_same_moments_vs_distinct_fixed_labelings(self):
        palette=tuple(combinations(range(6),2))
        target=physical_occupied_target(6,palette)
        index={e:i for i,e in enumerate(palette)}
        moment_pair=None
        for scheme in ("lex","reverse-line"):
            model=pair_labeled_symplectic(1,scheme)
            src=source_weighted_BA_hypergraph(model)
            cert=common_bijection_moments(src,target,15,retain_spectra=True)
            self.assertEqual(cert["source_mass"],5000)
            self.assertEqual(cert["physically_occupied_target_size"],70)
            self.assertEqual(cert["one_common_right_bijection_mean"],
                             Fraction(5000*70,5005))
            right=list(model["right_labels"])
            fixed=tuple(index[e] for e in right)
            actual=fixed_map_overlap(src,target,fixed)
            self.assertEqual(actual,exact_BA_overlap(src,right))
            if scheme=="reverse-line":
                self.assertEqual(actual,77)
                varied=set()
                for i,j in combinations(range(15),2):
                    sw=list(fixed)
                    sw[i],sw[j]=sw[j],sw[i]
                    varied.add(fixed_map_overlap(src,target,sw))
                    if (i,j)==(4,13):
                        self.assertEqual(fixed_map_overlap(src,target,sw),57)
                self.assertGreater(len(varied),1)
            if moment_pair is None:
                moment_pair=cert
            else:
                # Physical left f is relabeled, so exact source intersection
                # spectra may differ; do not assert them equal across f.
                self.assertEqual(moment_pair["one_common_right_bijection_mean"],
                                 cert["one_common_right_bijection_mean"])
        self.assertFalse(cert["all_correlated_fixed_g_lower_proved"])

    def test_all_h_occupied_target_density_and_random_mean_scope(self):
        for s in (2,4,8,16,32,64,128,256,512,1024):
            c=occupied_target_uniform_floor(s)
            a=c["a"]
            t=c["missing_physical_labels"]
            self.assertLess(t,a)
            self.assertEqual(c["destroyed_target_fraction_upper_union"],
                             Fraction(12*t,a*(a-1)))
            self.assertEqual(
                c["occupied_target_count_lower"],
                max(0,c["target_full_Ka_count"]-
                    t*c["target_each_physical_edge_degree"]))
            self.assertEqual(
                c["one_common_right_bijection_mean_lower"],
                Fraction(
                    c["GQ_original_BA_source_mass_lower"]*
                    c["occupied_target_count_lower"],comb(c["V"],6)))
            self.assertFalse(c["not_fixed_adversarial_g_lower"])
            # Correct flag is True: this benchmark MUST NEVER be
            # misinterpreted as a deterministic all-correlated bound.
        for bad in (1,3,True):
            with self.assertRaises(ValueError):
                occupied_target_uniform_floor(bad)

    def test_genuine_fixed_g_zero_and_nonzero_indistinguishable_global_moments(self):
        palette=tuple(combinations(range(6),2))
        target=physical_occupied_target(6,palette)
        good=next(iter(target))
        bad=next(frozenset(R) for R in combinations(range(15),6)
                 if frozenset(R) not in target)
        g={good:1}
        b={bad:1}
        x=common_bijection_moments(g,target,15)
        y=common_bijection_moments(b,target,15)
        self.assertEqual(x,y)
        identity=tuple(range(15))
        self.assertEqual(fixed_map_overlap(g,target,identity),1)
        self.assertEqual(fixed_map_overlap(b,target,identity),0)
        self.assertFalse(x["all_correlated_fixed_g_lower_proved"])

    def test_reject_invalid_source_occupied_and_map(self):
        R=frozenset(range(6))
        for data in ({R:-1},{R:True},{frozenset((0,1,2,3,4,15)):1},
                     {frozenset(range(5)):1}):
            with self.assertRaises(ValueError):
                validate_weighted_sixsets(data,15)
        with self.assertRaises(ValueError):
            physical_occupied_target(6,[(0,1)]*8)
        with self.assertRaises(ValueError):
            fixed_map_overlap({R:1},{R},list(range(14))+[0])


if __name__=="__main__":
    unittest.main()
