"""Independent all-h one-sided positive 6-coordinate template lower falsifiers."""
from itertools import combinations
from math import comb
from fractions import Fraction
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1a_fixed_leading import finite_census
from hyp105_g5e2b3e1b1a_one_sided import (
    COEFFICIENTS, TOTAL_LIMIT, gq_parameters, template_counts,
    left_six_mass, exact_physical_counts, report,
)


class UniversalOneSidedSixTests(unittest.TestCase):
    def test_W32_full_alphabet_matches_independent_original_factor_oracle(self):
        p=gq_parameters(2)
        self.assertEqual({key:p[key] for key in ("V","Delta","a","K","missing")},
                         {"V":15,"Delta":3,"a":6,"K":15,"missing":0})
        result=left_six_mass(2)
        self.assertEqual(result["left_original_sixsets_lower"],
                         {"A":51030,"B":10935,"C":405})
        self.assertEqual(result["left_original_sixsets_upper"],
                         {"A":51030,"B":10935,"C":405})
        self.assertEqual(result["total_left_lower"],62370)
        # Independent accepted 45-original-incidence projection census:
        model=pair_labeled_symplectic(1,"lex")
        accepted=finite_census(model)
        self.assertEqual(accepted["candidate_counts_by_left_type"],
                         {"A":51030,"B":10935,"C":405})
        self.assertEqual(exact_physical_counts(6,combinations(range(6),2)),
                         {"A":70,"B":45,"C":15})

    def test_independent_exhaustive_missing_K14_graph_census(self):
        p=gq_parameters(4)
        self.assertEqual((p["V"],p["a"],p["K"],p["missing"]),
                         (85,14,91,6))
        legal=tuple(combinations(range(14),2))
        graphs=(
            {(0,1),(0,2),(0,3),(0,4),(0,5),(0,6)},
            {(0,1),(2,3),(4,5),(6,7),(8,9),(10,11)},
        )
        b=left_six_mass(4)
        for omitted in graphs:
            edges=tuple(e for e in legal if e not in omitted)
            self.assertEqual(len(edges),85)
            exact=exact_physical_counts(14,iter(edges))
            for kind in ("A","B","C"):
                self.assertGreaterEqual(exact[kind],
                                        b["physical_pattern_bounds"]["lower"][kind])
                self.assertLessEqual(exact[kind],
                                     b["physical_pattern_bounds"]["full"][kind])
            lifted=sum(exact[k]*b["lift_multiplicities"][k]
                       for k in ("A","B","C"))
            self.assertGreaterEqual(lifted,b["total_left_lower"])
            self.assertLessEqual(lifted,b["total_left_upper"])
        self.assertTrue(any(b["physical_pattern_bounds"]["lower"][k] <
                            b["physical_pattern_bounds"]["full"][k]
                            for k in ("A","B","C")))

    def test_exact_k_edge_transitivity_union_bound_finite_fields(self):
        for s in (2,4,8,16,32,64,128,256):
            b=left_six_mass(s)
            p=b["physical_pattern_bounds"]
            self.assertEqual(p["missing"], b["K"]-b["V"])
            for kind,k in (("A",6),("B",5),("C",3)):
                full=p["full"][kind]
                self.assertEqual(full*k%b["K"],0)
                self.assertEqual(p["per_missing_edge"][kind],
                                 full*k//b["K"])
                self.assertEqual(p["lower"][kind],
                                 max(0,full-p["missing"]*(full*k//b["K"])))
                self.assertGreaterEqual(b["left_original_sixsets_lower"][kind],0)
                self.assertLessEqual(b["left_original_sixsets_lower"][kind],
                                     b["left_original_sixsets_upper"][kind])
            self.assertGreater(b["total_left_lower"],0)

    def test_uniform_all_h_limit_151_over_144_and_proof_scope(self):
        self.assertEqual(COEFFICIENTS, {
            "A":Fraction(7,9),
            "B":Fraction(1,4),
            "C":Fraction(1,48),
        })
        self.assertEqual(TOTAL_LIMIT,Fraction(151,144))
        for s in (128,256,1024):
            b=left_six_mass(s)
            for name,c in COEFFICIENTS.items():
                ratio_lower=Fraction(b["left_original_sixsets_lower"][name],
                                     s**15)
                ratio_upper=Fraction(b["left_original_sixsets_upper"][name],
                                     s**15)
                self.assertLess(ratio_lower,c*Fraction(6,5))
                self.assertGreater(ratio_lower,c*Fraction(3,4))
                self.assertLess(ratio_upper,c*Fraction(6,5))
                self.assertGreater(ratio_upper,c*Fraction(3,4))
            lower=Fraction(b["total_left_lower"],s**15)
            upper=Fraction(b["total_left_upper"],s**15)
            self.assertLess(lower,TOTAL_LIMIT*Fraction(6,5))
            self.assertGreater(lower,TOTAL_LIMIT*Fraction(3,4))
            self.assertLess(upper,TOTAL_LIMIT*Fraction(6,5))
            self.assertGreater(upper,TOTAL_LIMIT*Fraction(3,4))
            self.assertFalse(b["same_label_seven_family_lower"])
            self.assertFalse(b["strict_GQ_GF5_R3_exponent"])

    def test_reject_impossible_parameters_and_noninjective_physical_graph(self):
        for s in (0,1,3,6,9,True,-2,1.5):
            with self.assertRaises(ValueError):
                gq_parameters(s)
        for a in (0,2,5,True):
            with self.assertRaises(ValueError):
                template_counts(a,0)
        with self.assertRaises(ValueError):
            template_counts(6,16)
        with self.assertRaises(ValueError):
            template_counts(6,False)
        with self.assertRaises(ValueError):
            exact_physical_counts(15,())
        with self.assertRaises(ValueError):
            exact_physical_counts(6,[(0,1),(0,1)])
        with self.assertRaises(ValueError):
            exact_physical_counts(6,[(0,6)])
        self.assertFalse(report()["two_sided_motif_Omega_s6"])
        self.assertFalse(report()["actual_full_GF5_R3_bound"])


if __name__=="__main__":
    unittest.main()
