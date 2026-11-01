"""Independent AA4-EPSOPT symbolic-root and TRUE original-source finite falsifiers."""
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_full_physical_degree_tail import genuine_source
from hyp105_heavy_tail_epsilon_optimal_root import (
    EPS_OLD,EPS_OPT,root_certificate,source_budget,
    verify_exact_dyadic_losses,genuine_original_pruning,minimal_alphabet,
)


def _maps(V,k=1):
    a=minimal_alphabet(V)
    labels=tuple(combinations(range(a),2))[:V]
    g=tuple(labels[(7*i+k)%V] for i in range(V))
    if len(set(g))!=V:
        raise AssertionError("invalid adversarial original typed mapping")
    return labels,g


class TrueOriginalOptimizedHeavyEpsilon(unittest.TestCase):
    def test_coarse_core_budget_exact_sharp_asymptotic_epsilon(self):
        self.assertEqual(EPS_OPT,Fraction(13,32))
        for s in (64,128,256,512,1024,2048):
            with self.subTest(s=s):
                o=source_budget(s,EPS_OLD)
                n=source_budget(s,EPS_OPT)
                self.assertGreaterEqual(o["uniform_m0_over_s4_lower"],1)
                self.assertEqual(n["uniform_m0_over_s4_lower"],1)
                self.assertGreater(n["source_sharper_m0_lower"],s**4)
                self.assertTrue(n["universal_coarse_density_valid"])
                self.assertGreaterEqual(n["N"],s**4)
                self.assertLessEqual(n["Cs"],Fraction(3,2)*s**4)
                self.assertLessEqual(n["a"]**2,4*s**3)
        # THIS ONLY establishes maximality in the unchanged uniform
        # coarse density budget, not counterexamples in genuine GQ.
        excess=EPS_OPT+Fraction(1,1024)
        z=source_budget(64,excess)
        self.assertFalse(z["universal_coarse_density_valid"])
        self.assertLess(z["uniform_m0_over_s4_lower"],1)

    def test_symbolic_tail_epsilon_independent_exact_certificates(self):
        examples=[
            (Fraction(1),Fraction(1)),
            (Fraction(1,2),Fraction(1,7)),
            (Fraction(17,5),Fraction(1,99)),
            (Fraction(1,100),Fraction(1,1000)),
            (Fraction(33),Fraction(2,3)),
        ]
        for C,c in examples:
            with self.subTest(C=C,c=c):
                old=root_certificate(C,c,EPS_OLD)
                new=root_certificate(C,c,EPS_OPT)
                self.assertLessEqual(new["T"],old["T"])
                self.assertLessEqual(new["h0_sufficient"],old["h0_sufficient"])
                self.assertGreaterEqual(new["delta_S_seven"],old["delta_S_seven"])
                self.assertEqual(
                    new["alpha_external_heavy_D6"],
                    c*EPS_OPT**12/Fraction(2**72))
                self.assertEqual(new["delta_S_seven"],
                                 min(Fraction(1,8),new["alpha_external_heavy_D6"]))
                self.assertEqual(
                    new["R3_floor_simple"],
                    Fraction(53526)*new["delta_S_seven"]/51**6)
                self.assertGreaterEqual(
                    new["R3_floor_conditioned_on_geometric_lemma"],
                    new["R3_floor_simple"])
                self.assertTrue(verify_exact_dyadic_losses(
                    C,c,EPS_OPT,new["h0_sufficient"])["all_three_errors_le_sixth_over24"])
                self.assertTrue(verify_exact_dyadic_losses(
                    C,c,EPS_OPT,new["h0_sufficient"]+50)["all_three_errors_le_sixth_over24"])

    def test_hypothetical_external_C_equal_c_equal_one_exact_h0(self):
        # TEST PLACEHOLDERS: paper does not supply numerical C,c!
        old=root_certificate(1,1,EPS_OLD)
        new=root_certificate(1,1,EPS_OPT)
        self.assertEqual(old["T"],2**58)
        self.assertEqual(new["T"],244590498757546)
        self.assertEqual(old["h0_sufficient"],816)
        self.assertEqual(new["h0_sufficient"],714)
        self.assertEqual(old["delta_S_seven"],Fraction(1,2**108))
        self.assertEqual(new["delta_S_seven"],Fraction(13**12,2**132))
        self.assertEqual(
            new["delta_S_seven"]/old["delta_S_seven"],
            Fraction(13**12,2**24))
        self.assertEqual(new["T"],-(-(2**70)//13**6))
        self.assertEqual(
            root_certificate(1,1,EPS_OPT)["h0_sufficient"],714)
        below=verify_exact_dyadic_losses(1,1,EPS_OPT,713)
        self.assertFalse(below["all_three_errors_le_sixth_over24"])
        self.assertTrue(
            verify_exact_dyadic_losses(1,1,EPS_OPT,714)["all_three_errors_le_sixth_over24"])

    def test_symbolic_exact_factor_and_sharp_32_over_13_gain(self):
        gain=EPS_OPT/EPS_OLD
        self.assertEqual(gain,Fraction(13,4))
        self.assertEqual(gain**6,Fraction(13**6,4**6))
        self.assertEqual(gain**12,Fraction(13**12,4**12))
        self.assertGreater(gain**6,1000)
        self.assertGreater(gain**12,1000000)
        for epsilon in (Fraction(1,8),Fraction(1,4),
                        Fraction(3,8),Fraction(13,32)):
            z=root_certificate(1,1,epsilon)
            self.assertGreater(z["h0_sufficient"],0)

    def test_real_original_W32_W34_correlated_full_heavy_core_bookkeeping(self):
        for power in (1,2):
            s,V,flags=genuine_source(power)
            f,g=_maps(V)
            for T,K in ((Fraction(1,2),1),(Fraction(1),2),
                        (Fraction(2),64),(Fraction(10),64)):
                with self.subTest(power=power,T=T,K=K):
                    report=genuine_original_pruning(power,f,g,T,K=K)
                    self.assertTrue(report["bookkeeping_valid"])
                    self.assertEqual(report["full_edges"],2*len(flags))
                    self.assertEqual(report["full_degree_sum"],4*len(flags))
                    self.assertLessEqual(
                        report["deleted_heavy_original_flags"],
                        report["full_heavy_edges"])
                    self.assertEqual(
                        2*report["original_core_flags"],
                        report["core_physical_edges"])
                    self.assertLessEqual(report["core_max_degree"],T*s)
                    self.assertLessEqual(report["core_max_full_conflict_degree"],K)

    def test_adversarial_original_correlated_map_changes_no_constants(self):
        for power in (1,2):
            _,V,_=genuine_source(power)
            f,g=_maps(V)
            f2,g2=_maps(V,2)
            one=genuine_original_pruning(power,f,g,Fraction(1),K=3)
            two=genuine_original_pruning(power,f2,g2,Fraction(1),K=3)
            self.assertEqual(one["original_flags"],two["original_flags"])
            self.assertEqual(one["full_edges"],two["full_edges"])
            self.assertEqual(one["full_degree_sum"],two["full_degree_sum"])

    def test_fail_closed_invalid_constants_sizes_and_nonlegal_original_maps(self):
        for invalid in (None,0,-1,0.5,True,"1"):
            with self.subTest(value=invalid):
                with self.assertRaises(ValueError):
                    root_certificate(invalid,1)
                with self.assertRaises(ValueError):
                    root_certificate(1,invalid)
                with self.assertRaises(ValueError):
                    root_certificate(1,1,invalid)
        with self.assertRaises(ValueError):
            root_certificate(1,1,Fraction(13,32)+Fraction(1,999))
        for invalid in (0,32,96,63,65,64.0):
            with self.assertRaises(ValueError):
                source_budget(invalid)
        with self.assertRaises(ValueError):
            verify_exact_dyadic_losses(1,1,EPS_OPT,False)
        _,V,_=genuine_source(1)
        f,g=_maps(V)
        for invalid in (0,-1,1.0,True):
            with self.assertRaises(ValueError):
                genuine_original_pruning(1,f,g,invalid)
        with self.assertRaises(ValueError):
            genuine_original_pruning(1,f[:-1],g,1)
        with self.assertRaises(ValueError):
            genuine_original_pruning(1,(f[0],)*V,g,1)
        with self.assertRaises(ValueError):
            genuine_original_pruning(3,f,g,1)


if __name__=="__main__":
    unittest.main()
