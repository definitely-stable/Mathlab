"""AA4-BB independent original source/physical two-overlap covariance falsifiers."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4az_quenched_good_opposite import (
    genuine_original_fixed_point_GOOD_source_potential,
    quenched_genuine_original_GOOD_opposite_mean,
    support_bad_clean_energy,
)
from hyp105_issue230_d6aa4az_quenched_allD_variance import (
    uniform_original_GOOD_variance_envelope,
)
from hyp105_issue230_d6aa4bb_overlap_covariance import (
    all_three_source_line_overlap,
    four_overlap_probability_certificate,
    exact_weighted_global_permutation_second_moment_bound,
    true_original_GOOD_source_second_moment,
    uniform_GOOD_variance_envelope,
)


def direct_opposite(center,left,right):
    x=set(center)&set(left)
    y=set(center)&set(right)
    return len(x)==len(y)==1 and x!=y


def independent_pair_joint_probability(support, first, second):
    """Explicit four distinct physical edge labels, single GLOBAL assignment."""
    if len(set(first+second))!=4:
        raise ValueError("expected two shared original source line IDs")
    tested=0
    favorable=0
    for images in permutations(support,4):
        g=dict(zip(range(4),images))
        tested+=1
        if direct_opposite(*(g[x] for x in first)) and direct_opposite(
                *(g[x] for x in second)):
            favorable+=1
    return Fraction(favorable,tested)


def full_720_bijection_moments(support,weights):
    vals=[]
    for images in permutations(support):
        value=sum(w for ids,w in weights.items()
                  if direct_opposite(*(images[x] for x in ids)))
        vals.append(value)
    mu=Fraction(sum(vals),len(vals))
    v=sum((Fraction(x)-mu)**2 for x in vals)/len(vals)
    return mu,v


def independent_true_W32_clean_line_triples(m):
    """Direct original triple enumeration without the source helper's stars."""
    I=tuple(tuple(q) for q in m["incidences"])
    f=tuple(map(tuple,m["left_labels"]))
    clean=set(support_bad_clean_energy(f,6)["clean_induced_occupied_edges"])
    ans=Counter()
    for p,l in I:
        if tuple(sorted(f[p])) not in clean:
            continue
        u,v=f[p]
        for q0,k0 in I:
            if q0==p or k0==l or tuple(sorted(f[q0])) not in clean:
                continue
            if u not in f[q0] or v in f[q0]:
                continue
            for q1,k1 in I:
                if len({p,q0,q1})!=3 or len({l,k0,k1})!=3:
                    continue
                if tuple(sorted(f[q1])) not in clean:
                    continue
                if v in f[q1] and u not in f[q1]:
                    ans[l,k0,k1]+=1
    return dict(ans)


class AA4BBSourceOverlapTests(unittest.TestCase):
    def test_01_exhaustive_small_global_permutation_var_four_cases(self):
        E=tuple(combinations(range(4),2))
        for weights in ({(0,1,2):2,(1,4,3):3,(2,4,5):1,(3,0,5):7},
                        {(0,1,2):1},
                        {(0,1,2):1,(3,4,5):1},
                        {(0,1,2):4,(1,2,0):2,(2,0,1):5}):
            z=exact_weighted_global_permutation_second_moment_bound(
                weights,E,4)
            mu,var=full_720_bijection_moments(E,weights)
            self.assertEqual(z["mean"],mu)
            self.assertLessEqual(var,z["relative_variance_upper"]*mu*mu)
            self.assertLessEqual(z["M3"],z["M2"])
            self.assertTrue(z["fully_correlated_global_right_map"])

    def test_02_ALL_sharing_two_original_LINE_positions_full_physical_tuples(self):
        for a in (4,5,6):
            E=tuple(combinations(range(a),2))
            V=len(E)
            t=a-2
            bound=Fraction(16*V*t**3,V*(V-1)*(V-2)*(V-3))
            for shared in ((0,1,3),(0,2,3),(1,2,3)):
                for other in permutations(shared):
                    actual=independent_pair_joint_probability(
                        E,(0,1,2),other)
                    self.assertLessEqual(actual,bound)
            P=four_overlap_probability_certificate(V,a,
                sum(direct_opposite(x,y,z) for x,y,z in permutations(E,3))//2)
            self.assertEqual(P["two_joint_upper"],bound)

    def test_03_genuine_original_W32_all_source_triples_independent(self):
        for scheme in ("S68","S72","lex","reverse"):
            m=fixture(1,scheme)
            direct=independent_true_W32_clean_line_triples(m)
            B,M1,M2,M3=all_three_source_line_overlap(direct,15)
            self.assertEqual(B,genuine_original_fixed_point_GOOD_source_potential(
                m)["CLEAN_original_fixed_f_physical_point_opposite_true_source_3flag_count"])
            cert=true_original_GOOD_source_second_moment(m)
            self.assertEqual((cert["B"],cert["M1"],cert["M2"],cert["M3"]),
                             (B,M1,M2,M3))
            self.assertEqual(cert["mean"],
                quenched_genuine_original_GOOD_opposite_mean(m)[
                    "exact_one_global_original_LINE_bijection_GOOD_opposite_wedge_mean"])
            self.assertGreater(B,0)
            self.assertLessEqual(M3,6*(m["s"]+1)**3)

    def test_04_true_original_W34_nononto_support_and_parent_mean(self):
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            cert=true_original_GOOD_source_second_moment(m)
            self.assertEqual(cert["V"],85)
            self.assertEqual(cert["mean"],
                quenched_genuine_original_GOOD_opposite_mean(m)[
                    "exact_one_global_original_LINE_bijection_GOOD_opposite_wedge_mean"])
            self.assertLessEqual(cert["M3"],6*(m["s"]+1)**3)
            self.assertGreaterEqual(cert["relative_variance_upper"],0)

    def test_05_dyadic_all_h_good_O_s_minus_three_certificates(self):
        for h in tuple(range(5,34))+(40,48,64,80):
            s=1<<h
            z=uniform_GOOD_variance_envelope(s)
            self.assertTrue(z["explicit_all_h_eta_le_220million_over_V"])
            self.assertLessEqual(z["relative_variance_upper"]*z["V"],220000000)
            self.assertGreaterEqual(z["mean_lower"],Fraction(s**6,128))
            self.assertFalse(not z["all_given_adversarial_g_lower_NOT_PROVED"])
            self.assertTrue(z["selected_seven_original_sixflag_GF5_NOT_PROVED"])
        with self.assertRaises(ValueError):
            uniform_GOOD_variance_envelope(16)
        for s in (64,128,512,4096):
            self.assertLess(uniform_GOOD_variance_envelope(s)[
                "relative_variance_upper"],
                uniform_original_GOOD_variance_envelope(s)[
                    "GOOD_relative_variance_upper"])
        self.assertLess(uniform_GOOD_variance_envelope(512)[
            "probability_R_GOOD_below_s6_over256_upper"],Fraction(1,10))

    def test_06_bad_source_triple_and_bad_global_physical_image_rejected(self):
        E=tuple(combinations(range(4),2))
        for w in ({(0,0,1):1}, {(0,1,6):1}, {(0,1,2):0}, {}):
            with self.assertRaises(ValueError):
                exact_weighted_global_permutation_second_moment_bound(w,E,4)
        with self.assertRaises(ValueError):
            exact_weighted_global_permutation_second_moment_bound(
                {(0,1,2):1},((0,1),(1,0),(0,2),(0,3),(1,2),(2,3)),4)
        with self.assertRaises(ValueError):
            four_overlap_probability_certificate(5,4,0)

    def test_07_right_physical_gauge_invariance_and_mean_vs_fixed_g(self):
        m=fixture(1,"S68")
        cert=true_original_GOOD_source_second_moment(m)
        E=m["right_labels"]
        pi=(1,2,3,4,5,0)
        E2=tuple(tuple(sorted((pi[u],pi[v]))) for u,v in E)
        # Literal original fixed f source weights independent of right physical gauge.
        w=independent_true_W32_clean_line_triples(m)
        other=exact_weighted_global_permutation_second_moment_bound(w,E2,6,clean=True)
        self.assertEqual(cert["mean"],other["mean"])
        self.assertEqual(cert["relative_variance_upper"],other["relative_variance_upper"])
        self.assertTrue(cert["root_230"]=="OPEN_WITH_FORMAL_BLOCKER")


if __name__=="__main__":
    unittest.main()
