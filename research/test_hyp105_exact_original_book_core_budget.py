"""Independent AA4-BOOKBUD original-source all-h inequality falsifiers."""
from fractions import Fraction
from math import comb,isqrt
from itertools import combinations
import unittest

from hyp105_exact_original_book_core_budget import (
    EPS_689, EPS_NEW, LOWER_BUDGET, ANALYTIC_PENALTY,
    universal_analytic_certificate, original_core_budget, root_symbolic,
    independent_true_source_books, true_minimal_alphabet,
)


class AllHSourceBookExactBudget(unittest.TestCase):
    def test_independent_all_real_s_analytic_proof_certificate(self):
        out=universal_analytic_certificate()
        self.assertEqual(ANALYTIC_PENALTY,Fraction(38245,33554432))
        self.assertEqual(LOWER_BUDGET,
                         Fraction(7,16)-Fraction(38245,33554432))
        self.assertEqual(EPS_NEW,Fraction(1787,4096))
        self.assertEqual(EPS_689,Fraction(13,32))
        self.assertGreater(out["strict_margin"],0)
        self.assertLess(out["epsilon_improved"],out["epsilon_analytic_upper_certificate"])
        self.assertGreater(out["epsilon_improved"],out["epsilon_prior"])
        # Verify the quadratic discriminant completion by rational algebra.
        b=Fraction(97,64)
        self.assertEqual(b*b/Fraction(2048)+Fraction(1,65536)+b/Fraction(524288),
                         ANALYTIC_PENALTY)

    def test_true_exact_minimal_pair_alphabet_independent_binomial(self):
        for h in range(1,18):
            s=1<<h
            V=(s+1)*(s*s+1)
            a=true_minimal_alphabet(V)
            self.assertGreaterEqual(comb(a,2),V)
            self.assertLess(comb(a-1,2),V)
            if s>=64:
                self.assertLessEqual(Fraction(a*a, s**3),Fraction(97,64)**2)

    def test_exact_original_source_budget_many_dyadic_h(self):
        # No floating point, very large s supported by integer isqrt.
        for h in range(6,27):
            s=1<<h
            z=original_core_budget(s)
            self.assertTrue(z["above_s4"])
            self.assertGreaterEqual(z["exact_max_epsilon_for_m0_ge_s4"],LOWER_BUDGET)
            self.assertGreater(z["exact_max_epsilon_for_m0_ge_s4"],EPS_NEW)
            self.assertGreater(z["paired_core_lower"],s**4)
            self.assertLessEqual(z["Cs"],(s*s+1)*(s*s+z["a"]-2))
            self.assertEqual(z["N"],(s+1)**2*(s*s+1))

    def test_old_new_all_h_root_exact_integer_symbolic_threshold(self):
        for C,c in ((Fraction(1),Fraction(1)),
                    (Fraction(1,7),Fraction(7,3)),
                    (Fraction(17,5),Fraction(1,99)),
                    (Fraction(100),Fraction(1,1000))):
            with self.subTest(C=C,c=c):
                older=root_symbolic(C,c,EPS_689)
                newer=root_symbolic(C,c,EPS_NEW)
                self.assertLessEqual(newer["T"],older["T"])
                self.assertLessEqual(newer["h0_sufficient"],older["h0_sufficient"])
                self.assertGreaterEqual(newer["delta_original_sixsets"],
                                        older["delta_original_sixsets"])
                self.assertGreaterEqual(
                    newer["exact_signed_GF5_R3_lower_coefficient"],
                    older["exact_signed_GF5_R3_lower_coefficient"])
                self.assertEqual(
                    newer["alpha_heavy"], c*EPS_NEW**12/Fraction(2**72))
                h=newer["h0_sufficient"]
                self.assertTrue((1<<h)>=newer["s0_sufficient"])
                self.assertTrue((1<<(h-1))<newer["s0_sufficient"])

    def test_hypothetical_one_one_h0_708_not_actual_published_constants(self):
        # Absolutely NO statement that real C_graph,c_graph are 1.
        old=root_symbolic(1,1,EPS_689)
        new=root_symbolic(1,1,EPS_NEW)
        self.assertEqual(old["h0_sufficient"],714)
        self.assertEqual(new["h0_sufficient"],708)
        self.assertEqual(old["T"],244590498757546)
        self.assertEqual(new["T"],159445475251527)
        self.assertEqual(new["delta_original_sixsets"],
                         EPS_NEW**12/Fraction(2**72))
        self.assertGreater(
            new["alpha_heavy"]/old["alpha_heavy"],2)
        self.assertLess(
            new["T"]/old["T"],Fraction(2,3))

    def test_original_W32_W34_source_book_and_conflict_independent_scans(self):
        for power in (1,2):
            for shift in (0,1,3,7,11):
                with self.subTest(power=power,shift=shift):
                    z=independent_true_source_books(power,shift)
                    s=z["s"]
                    self.assertTrue(z["original_source_identity_verified"])
                    self.assertEqual(z["original_flags"],(s+1)**2*(s*s+1))
                    self.assertEqual(z["direct_original_conflicts"],
                                     z["Mf"]+z["Mg"])
                    self.assertLessEqual(z["Mf"],z["Cs_all_h"])
                    self.assertLessEqual(z["Mg"],z["Cs_all_h"])

    def test_input_types_and_unproven_epsilon_rejected(self):
        for invalid in (0,-1,None,"1",True,1.0):
            with self.assertRaises(ValueError):
                root_symbolic(invalid,1)
            with self.assertRaises(ValueError):
                root_symbolic(1,invalid)
            with self.assertRaises(ValueError):
                root_symbolic(1,1,invalid)
        with self.assertRaises(ValueError):
            root_symbolic(1,1,LOWER_BUDGET+Fraction(1,99999))
        with self.assertRaises(ValueError):
            original_core_budget(64,LOWER_BUDGET+Fraction(1,99999))
        for invalid in (2,32,63,65,96,64.0,True):
            with self.assertRaises(ValueError):
                original_core_budget(invalid)
        with self.assertRaises(ValueError):
            independent_true_source_books(3)
        with self.assertRaises(ValueError):
            independent_true_source_books(1,1.0)
        with self.assertRaises(ValueError):
            true_minimal_alphabet(False)


if __name__=="__main__":
    unittest.main()
