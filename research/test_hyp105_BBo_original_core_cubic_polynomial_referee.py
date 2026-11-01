"""AA4-BBOCUBIC: independently source-first all-core cubic vs physical DFS."""
from itertools import combinations
from fractions import Fraction
from math import comb
import unittest

from hyp105_full_physical_degree_tail import genuine_source,planted_original_k44
from hyp105_BBo_original_core_cubic_polynomial_referee import (
    source_first_original_BBo_cubic_catalog,
    evaluate_original_BBo_core_polynomial,
    independent_physical_first_BBo_core_census,
    exact_independent_core_retention_moments,
)


def maps(power,shift=0):
    _,V,_=genuine_source(power)
    a=2
    while comb(a,2)<V:a+=1
    palette=tuple(combinations(range(a),2))[:V]
    return palette,tuple(palette[(19*i+shift)%V] for i in range(V))


def compare_core(testcase,power,f,g,catalog,core):
    source=evaluate_original_BBo_core_polynomial(catalog,core)
    physical=independent_physical_first_BBo_core_census(power,f,g,core)
    testcase.assertEqual(source["produced_true_ORIGINAL_BBo_sixsets"],
                         physical["actual_original_BBo_sixset_count"])
    testcase.assertEqual(source["actual_directed_proper_unblocked_source_paths"],
                         physical["actual_directed_source_paths"])
    testcase.assertEqual(set(source["produced_original_sixset_owners"]),
                         set(physical["original_source_sixset_path_witnesses"]))
    return source,physical


class TrueOriginalBBoCubicCore(unittest.TestCase):
    def test_true_W32_full_original_source_three_distinct_correlated_maps(self):
        _,V,flags=genuine_source(1)
        positive=0
        for shift in (0,1,3,7):
            with self.subTest(shift=shift):
                f,g=maps(1,shift)
                cat=source_first_original_BBo_cubic_catalog(1,f,g)
                full,phys=compare_core(self,1,f,g,cat,range(len(flags)))
                self.assertEqual(cat["aligned_original_BBo_sixset_count"],
                                 full["produced_true_ORIGINAL_BBo_sixsets"])
                self.assertGreaterEqual(
                    cat["source_compatible_original_three_flag_chains"],
                    cat["aligned_original_BBo_sixset_count"])
                self.assertEqual(2*cat["aligned_original_BBo_sixset_count"],
                                 phys["actual_directed_source_paths"])
                positive+=cat["aligned_original_BBo_sixset_count"]
        self.assertGreater(positive,0)

    def test_true_W34_full_original_source_independent_left_right(self):
        _,V,flags=genuine_source(2)
        f,g=maps(2,0)
        cat=source_first_original_BBo_cubic_catalog(2,f,g)
        self.assertGreater(cat["aligned_original_BBo_sixset_count"],0)
        self.assertEqual(cat["candidate_original_ID_count"],425)
        full,phys=compare_core(self,2,f,g,cat,range(len(flags)))
        self.assertEqual(full["actual_directed_proper_unblocked_source_paths"],
                         2*cat["aligned_original_BBo_sixset_count"])

    def test_true_W32_arbitrary_original_core_and_anchors_NOT_in_core(self):
        f,g=maps(1,0)
        cat=source_first_original_BBo_cubic_catalog(1,f,g)
        self.assertTrue(cat["sixset_supports"])
        Q,T=next(iter(cat["sixset_supports"].items()))
        anchors=set(Q)-set(T)
        self.assertEqual(len(anchors),3)
        self.assertTrue(anchors)
        self.assertTrue(anchors.isdisjoint(T))
        res,_=compare_core(self,1,f,g,cat,T)
        self.assertGreaterEqual(res["produced_true_ORIGINAL_BBo_sixsets"],1)
        # Appending a full-original ANCHOR ID is NOT necessary for Q
        # to be counted: all three path owner IDs are sufficient.
        for anchor in anchors:
            bigger=evaluate_original_BBo_core_polynomial(cat,T+(anchor,))
            self.assertGreaterEqual(
                bigger["produced_true_ORIGINAL_BBo_sixsets"],
                res["produced_true_ORIGINAL_BBo_sixsets"])
        for deleted in T:
            res2,_=compare_core(self,1,f,g,cat,tuple(i for i in T if i!=deleted))
            self.assertEqual(res2["produced_true_ORIGINAL_BBo_sixsets"],0)
        forb=evaluate_original_BBo_core_polynomial(cat,T,forbidden_ids=(next(iter(anchors)),))
        self.assertLess(forb["produced_true_ORIGINAL_BBo_sixsets"],
                        res["produced_true_ORIGINAL_BBo_sixsets"])
        self.assertEqual(evaluate_original_BBo_core_polynomial(cat,(),())[
            "produced_true_ORIGINAL_BBo_sixsets"],0)

    def test_true_W32_all_128_original_core_subsets_and_exact_variance(self):
        f,g=maps(1,0)
        cat=source_first_original_BBo_cubic_catalog(1,f,g)
        Q,T=next(iter(cat["sixset_supports"].items()))
        other=next((t for t in cat["sixset_supports"].values()
                    if set(t)!=set(T)),T)
        pool=tuple(dict.fromkeys((*T,*other,*range(45))))[:7]
        self.assertEqual(len(pool),7)
        sub=source_first_original_BBo_cubic_catalog(1,f,g,pool)
        prob={i:Fraction(1,2) for i in pool}
        moments=exact_independent_core_retention_moments(sub,prob)
        expected=Fraction();second=Fraction()
        for mask in range(128):
            core=tuple(pool[j] for j in range(7) if mask>>j&1)
            output,_=compare_core(self,1,f,g,sub,core)
            u=output["produced_true_ORIGINAL_BBo_sixsets"]
            expected+=Fraction(u,128)
            second+=Fraction(u*u,128)
        self.assertEqual(expected,moments["exact_expected_ORIGINAL_BBo_sixsets"])
        self.assertEqual(second,moments["exact_expected_square_if_computed"])
        self.assertEqual(second-expected*expected,
                         moments["exact_variance_if_computed"])

    def test_true_W32_nonuniform_independent_flag_retention_exact_moments(self):
        f,g=maps(1,1)
        full=source_first_original_BBo_cubic_catalog(1,f,g)
        Q,T=next(iter(full["sixset_supports"].items()))
        pool=tuple(dict.fromkeys((*T,*range(45))))[:7]
        sub=source_first_original_BBo_cubic_catalog(1,f,g,pool)
        p={i:Fraction((j%3)+1,5) for j,i in enumerate(pool)}
        moments=exact_independent_core_retention_moments(sub,p)
        mean=second=Fraction()
        for mask in range(128):
            core=tuple(pool[j] for j in range(7) if mask>>j&1)
            weight=Fraction(1)
            for j,i in enumerate(pool):
                weight*=p[i] if mask>>j&1 else (1-p[i])
            val=evaluate_original_BBo_core_polynomial(sub,core)[
                "produced_true_ORIGINAL_BBo_sixsets"]
            mean+=weight*val;second+=weight*val*val
        self.assertEqual(mean,moments["exact_expected_ORIGINAL_BBo_sixsets"])
        self.assertEqual(second,moments["exact_expected_square_if_computed"])
        self.assertGreaterEqual(moments["exact_variance_if_computed"],0)
        self.assertTrue(moments[
            "all_cubic_monomial_indicator_covariances_nonnegative"])

    def test_true_W34_original_16_flag_protected_matching_control(self):
        f,g,ids=planted_original_k44()
        cat=source_first_original_BBo_cubic_catalog(2,f,g,ids)
        res,phy=compare_core(self,2,f,g,cat,ids)
        self.assertEqual(res["produced_true_ORIGINAL_BBo_sixsets"],
                         phy["actual_original_BBo_sixset_count"])
        self.assertEqual(res["actual_directed_proper_unblocked_source_paths"],
                         2*res["produced_true_ORIGINAL_BBo_sixsets"])
        # K4,4 protection is a source D6, not a promise of BBo;
        # zero counts here are valid and scientifically expected.
        self.assertEqual(cat["candidate_original_ID_count"],16)

    def test_8_small_original_core_deletions_keep_anchors_full(self):
        f,g=maps(2,7)
        ids=tuple(range(0,425,6))
        cat=source_first_original_BBo_cubic_catalog(2,f,g,ids)
        for mod in (2,3,4,5,7,11,13,17):
            core=tuple(i for i in ids if i%mod)
            compare_core(self,2,f,g,cat,core)
        self.assertEqual(evaluate_original_BBo_core_polynomial(
            cat,ids)["produced_true_ORIGINAL_BBo_sixsets"],
            cat["aligned_original_BBo_sixset_count"])

    def test_fail_closed_incomplete_maps_forged_ids_and_bad_probabilities(self):
        f,g=maps(1)
        _,V,flags=genuine_source(1)
        for power,ff,gg,ids in ((0,f,g,None),(3,f,g,None),
                                (1,f[:-1],g,None),
                                (1,(f[0],)*len(f),g,None),
                                (1,f,g,(0,0)),(1,f,g,(True,)),
                                (1,f,g,(len(flags),))):
            with self.assertRaises(ValueError):
                source_first_original_BBo_cubic_catalog(power,ff,gg,ids)
        catalog=source_first_original_BBo_cubic_catalog(1,f,g)
        with self.assertRaises(ValueError):
            evaluate_original_BBo_core_polynomial(catalog,(1,1))
        with self.assertRaises(ValueError):
            evaluate_original_BBo_core_polynomial(catalog,(),(-1,))
        with self.assertRaises(ValueError):
            evaluate_original_BBo_core_polynomial(catalog,(),(True,))
        with self.assertRaises(ValueError):
            exact_independent_core_retention_moments(catalog,{})
        with self.assertRaises(ValueError):
            exact_independent_core_retention_moments(catalog,{0:1.4})
        with self.assertRaises(ValueError):
            exact_independent_core_retention_moments(catalog,{0:Fraction(-1,3)})


if __name__=="__main__":
    unittest.main()
