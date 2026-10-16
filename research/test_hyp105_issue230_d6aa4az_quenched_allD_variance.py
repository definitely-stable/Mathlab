"""AA4-AZ independent entire-global-permutation and true-original falsifiers."""
import unittest
from fractions import Fraction
from itertools import combinations, permutations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import (
    exact_original_source_point_opposite_potential,
    quenched_original_opposite_ALL_D_mean,
)
from hyp105_issue230_d6aa4az_quenched_allD_variance import (
    original_line_triple_weights, source_influences,
    permutation_variance_certificate, uniform_original_variance_envelope,
)


def independent_opposite(e,x,y):
    a,b=set(e)&set(x),set(e)&set(y)
    return len(a)==len(b)==1 and a!=b


def exhaustive_full_bijection_moments(weights,edges):
    values=[]
    for g in permutations(edges):
        values.append(sum(n for (i,j,k),n in weights.items()
                          if independent_opposite(g[i],g[j],g[k])))
    mu=Fraction(sum(values),len(values))
    var=sum((Fraction(x)-mu)**2 for x in values)/len(values)
    return mu,var


class OriginalAA4AZVarianceTests(unittest.TestCase):
    def test_01_all_720_real_global_permutations_tiny_independent_variance(self):
        E=tuple(combinations(range(4),2))
        for w in ({(0,1,2):2,(1,4,3):3,(2,4,5):1,(3,0,5):7},
                  {(0,1,2):1},
                  {(0,1,2):1,(3,4,5):1},
                  {(0,1,2):4,(1,2,0):2,(2,0,1):5}):
            cert=permutation_variance_certificate(w,E,4)
            mu,var=exhaustive_full_bijection_moments(w,E)
            self.assertEqual(mu,cert["mean"])
            self.assertLessEqual(var,mu**2*cert["relative_variance_upper"])
            self.assertEqual(cert["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
        self.assertEqual(permutation_variance_certificate({(0,1,2):1},E,4)["p"],Fraction(2,5))

    def test_02_all_original_W32_source_triples_and_mean_with_both_maps(self):
        for scheme in ("S68","S72","lex","reverse"):
            m=fixture(1,scheme)
            w=original_line_triple_weights(m)
            B,M1,M2=source_influences(w,15)
            self.assertEqual(B,exact_original_source_point_opposite_potential(m)[
                "point_opposite_centered_3distinct_original_source_incidence_triples"])
            self.assertGreaterEqual(M1,M2)
            self.assertTrue(all(len(set(ids))==3 for ids in w))
            q=permutation_variance_certificate(w,m["right_labels"],6)
            self.assertEqual(q["mean"],quenched_original_opposite_ALL_D_mean(m)[
                "EXACT_quenched_uniform_ONE_full_global_original_LINE_map_ALL_D_opposite_mean"])
            self.assertLessEqual(q["relative_variance_upper"],
                                 uniform_original_variance_envelope(2)["relative_variance_upper"])

    def test_03_true_original_W34_nononto_physical_right_six_holes(self):
        m=fixture(2,"lex")
        w=original_line_triple_weights(m)
        self.assertEqual(sum(w.values()),exact_original_source_point_opposite_potential(m)[
            "point_opposite_centered_3distinct_original_source_incidence_triples"])
        q=permutation_variance_certificate(w,m["right_labels"],14)
        self.assertEqual(q["V"],85)
        self.assertEqual(q["mean"],quenched_original_opposite_ALL_D_mean(m)[
            "EXACT_quenched_uniform_ONE_full_global_original_LINE_map_ALL_D_opposite_mean"])
        self.assertLessEqual(q["relative_variance_upper"],
                             uniform_original_variance_envelope(4)["relative_variance_upper"])

    def test_04_all_h_dyadic_integer_rational_variance_envelope(self):
        for h in tuple(range(1,36))+(40,48,64,80):
            s=1<<h
            q=uniform_original_variance_envelope(s)
            self.assertGreaterEqual(q["mean_lower"],Fraction(s**6,2))
            self.assertGreaterEqual(q["relative_variance_upper"],0)
            self.assertFalse(q["fixed_g_lower_PROVED"])
            self.assertFalse(q["good_or_sixGF5_PROVED"])
        self.assertLess(uniform_original_variance_envelope(16)[
            "relative_variance_upper"],Fraction(1,8))
        self.assertLess(uniform_original_variance_envelope(32)[
            "relative_variance_upper"],Fraction(1,32))
        self.assertLess(uniform_original_variance_envelope(64)[
            "relative_variance_upper"],Fraction(1,100))

    def test_05_reject_duplicate_source_IDs_right_edge_and_nondyadic_order(self):
        E=tuple(combinations(range(4),2))
        for w in ({(0,0,1):1},{(0,1,6):1},{(0,1,2):-1},{}):
            with self.assertRaises(ValueError):
                permutation_variance_certificate(w,E,4)
        with self.assertRaises(ValueError):
            permutation_variance_certificate({(0,1,2):1},
                ((0,1),(1,0),(0,2),(0,3),(1,2),(2,3)),4)
        for s in (1,3,6):
            with self.assertRaises(ValueError):
                uniform_original_variance_envelope(s)

    def test_06_genuine_original_typed_physical_right_gauge_invariance(self):
        m=fixture(1,"S68")
        w=original_line_triple_weights(m)
        z=permutation_variance_certificate(w,m["right_labels"],6)
        pi=(1,2,3,4,5,0)
        E=tuple(tuple(sorted((pi[u],pi[v]))) for u,v in m["right_labels"])
        other=permutation_variance_certificate(w,E,6)
        self.assertEqual(z["mean"],other["mean"])
        self.assertEqual(z["relative_variance_upper"],other["relative_variance_upper"])


    def test_07_original_W32_W34_CLEAN_GOOD_source_weights_and_mean(self):
        from hyp105_issue230_d6aa4az_quenched_good_opposite import (
            genuine_original_fixed_point_GOOD_source_potential,
            quenched_genuine_original_GOOD_opposite_mean,
        )
        from hyp105_issue230_d6aa4az_quenched_allD_variance import (
            clean_good_permutation_variance_certificate,
        )
        for h,scheme in ((1,"S68"),(1,"S72"),(1,"lex"),
                         (2,"lex"),(2,"random")):
            m=fixture(h,scheme)
            w=original_line_triple_weights(m,clean_only=True)
            self.assertEqual(sum(w.values()),
                genuine_original_fixed_point_GOOD_source_potential(m)[
                    "CLEAN_original_fixed_f_physical_point_opposite_true_source_3flag_count"])
            z=clean_good_permutation_variance_certificate(m)
            self.assertEqual(z["mean_GOOD"],
                quenched_genuine_original_GOOD_opposite_mean(m)[
                    "exact_one_global_original_LINE_bijection_GOOD_opposite_wedge_mean"])
            self.assertGreaterEqual(z["relative_variance_upper"],0)
            self.assertLessEqual(z["B_GOOD"],
                sum(original_line_triple_weights(m).values()))
            self.assertFalse(z["every_given_fixed_g_lower_PROVED"])

    def test_08_all_dyadic_genuine_original_GOOD_concentration(self):
        from hyp105_issue230_d6aa4az_quenched_allD_variance import (
            uniform_original_GOOD_variance_envelope,
        )
        for h in tuple(range(5,36))+(40,48,64,80):
            s=1<<h
            z=uniform_original_GOOD_variance_envelope(s)
            self.assertGreaterEqual(z["GOODEXPECT_mean_lower"],Fraction(s**6,128))
            self.assertGreaterEqual(z["GOOD_relative_variance_upper"],0)
            self.assertFalse(z["GOOD_given_fixed_g_minimax_PROVED"])
            self.assertFalse(z["selected_original_sixID_sevenGF5_PROVED"])
        with self.assertRaises(ValueError):
            uniform_original_GOOD_variance_envelope(16)
        # Exact finite substitutions only; no unproved all-h monotonicity.
        self.assertGreater(uniform_original_GOOD_variance_envelope(32)[
            "GOOD_relative_variance_upper"],1)
        self.assertLess(uniform_original_GOOD_variance_envelope(4096)[
            "GOOD_relative_variance_upper"],Fraction(1,32))


if __name__=="__main__":
    unittest.main()
