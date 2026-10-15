"""Independent HYP-105 AA4-W-CYC all-h genuine ORIGINAL GQ moment proof QA."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb,perm,isqrt
import unittest

from hyp105_issue230_d6aa4r_quenched_original_d6 import (
    _params,quenched_original_D6_theorem)
from hyp105_issue230_d6aa4tcyc_fixed_f_d6_pair import (
    genuine_W32_fixed_f_original_connected_left_Q)
from hyp105_issue230_d6aa4wcyc_uniform_second_moment import (
    source_line_overlap_pair_capacity,
    same_global_g_second_D6_conditional_bound,
    exact_uniform_original_D6_E2_upper,
    elementary_ALL_h_constant_certificate,
    UNIFORM_SUCCESS_DENOMINATOR,
    UNIFORM_E2_S12_CONSTANT,
    PROVED_EXPLICIT_E2_S12_COEFFICIENT,
)


class EveryFixedTrueOriginalGQSecondMomentUpperTests(unittest.TestCase):
    def test_001_symbolic_seven_overlap_sector_integer_proof_is_not_finite_fit(self):
        c=elementary_ALL_h_constant_certificate()
        self.assertEqual(c["exact_constant_from_all_seven_TRUE_original_source_LINE_overlap_sectors"],
                         25_793_703_936)
        self.assertEqual(c["r0_disjoint_original_LINES_s12_coefficient"],2_030_043_136)
        self.assertEqual(c["r1_to_r5_original_LINE_overlap_s12_coefficients"],{
            1:12_630_097_920,2:7_893_811_200,3:2_631_270_400,
            4:493_363_200,5:49_336_320})
        self.assertEqual(c["r6_same_original_LINE_factor_set_s12_coefficient"],65_781_760)
        self.assertEqual(c["exact_constant_from_all_seven_TRUE_original_source_LINE_overlap_sectors"],
                         c["r0_disjoint_original_LINES_s12_coefficient"]+
                         sum(c["r1_to_r5_original_LINE_overlap_s12_coefficients"].values())+
                         c["r6_same_original_LINE_factor_set_s12_coefficient"])
        self.assertTrue(c["uniform_original_E2_upper_30b_s12_proof"])
        self.assertTrue(c["uniform_original_P_D6_positive_at_least_1_over_1920000000000"])

    def test_002_exact_all_h_rational_proof_checks_genuine_original_orders(self):
        for h in range(3,24):
            s=1<<h
            r=exact_uniform_original_D6_E2_upper(s)
            self.assertEqual(r["s"],s)
            self.assertEqual(r["V"],(s+1)*(s*s+1))
            self.assertEqual(r["K"],comb(r["a"],2))
            self.assertEqual(r["source_degree_d"],s+1)
            self.assertEqual(r["physical_C6_upper_count_all_Ka"],perm(r["a"],6)//12)
            self.assertEqual(r["original_left_connected_six_original_ID_Q_upper"],
                             perm(r["a"],6)//12*(s+1)**6)
            self.assertLessEqual(r["a"]**2,4*s**3)
            self.assertGreaterEqual(r["K"]-11,s**3//2)
            self.assertLessEqual(Fraction(r["exact_Bs_over_s12"]),UNIFORM_E2_S12_CONSTANT)
            self.assertGreaterEqual(Fraction(
                r["previous_all_h_fixed_point_map_E_g_D6_lower"]),Fraction(s**6,8))
            self.assertGreaterEqual(Fraction(
                r["true_original_PZ_improved_specific_s_lower"]),
                Fraction(1,UNIFORM_SUCCESS_DENOMINATOR))
            self.assertEqual(Fraction(
                r["new_ALL_h_every_fixed_f_one_uniform_GLOBAL_g_D6_positive_probability_lower"]),
                Fraction(1,1_920_000_000_000))
            self.assertTrue(r["all_h_E2_bound_uniform_in_f_PROVED"])
            self.assertFalse(r["all_h_for_every_f_g_seven_GF5_S_omega_s6_PROVED"])

    def test_003_exact_all_seven_true_ORIGINAL_LINE_overlap_sectors(self):
        for s in (8,16,32,128,1024):
            V,a,K,m=_params(s)
            r=exact_uniform_original_D6_E2_upper(s)
            sectors=r["full_g_shared_source_LINE_overlap_E2_sector_upper_bounds"]
            terms=[Fraction(sectors["r0_no_shared_source_lines"])]
            for i in range(1,7):
                cap=source_line_overlap_pair_capacity(s,i,a)
                q=same_global_g_second_D6_conditional_bound(s,i,a,K)
                self.assertEqual(cap,720*(s+1)**6*a**max(5-i,0))
                self.assertTrue(Fraction(0)<=q<=1)
                self.assertEqual(q,Fraction(min(Fraction(1),
                    Fraction(2**i*a**max(5-i,0),perm(K-6,6-i)))))
                terms.append(Fraction(sectors[f"r{i}_actual_original_line_overlap_upper"]))
            self.assertEqual(sum(terms),Fraction(
                r["exact_genuine_original_E_g_D6_squared_upper_Bs"]))
            self.assertGreater(terms[0],0)
            self.assertTrue(all(q>0 for q in terms))

    def test_004_real_original_W32_source_LINE_incidence_cap_falsification_oracle(self):
        # Although W-CYC theorem is s>=8, source-incidence capacity
        # is a pure ALL-h combinatorial upper and should hold on real
        # ORIGINAL W32 as a stringent independent small-source test.
        for scheme in ("S68","S72"):
            m,rows=genuine_W32_fixed_f_original_connected_left_Q(scheme)
            byline={r:Counter() for r in range(1,7)}
            for Q,(_,line_mask) in rows.items():
                lines=tuple(l for l in range(15) if line_mask&(1<<l))
                self.assertEqual(len(lines),6)
                for r in range(1,7):
                    for L in combinations(lines,r):
                        byline[r][L]+=1
            for r in range(1,7):
                max_count=max(byline[r].values())
                self.assertLessEqual(max_count,
                    source_line_overlap_pair_capacity(2,r,6))
                self.assertGreater(max_count,0)

    def test_005_true_global_right_injection_pair_bound_vs_exact_previous_kernel(self):
        from hyp105_issue230_d6aa4ucyc_shared_line_gluing import (
            exact_two_D6_gluing_kernel)
        for s in (2,4,8):
            V,a,K,m=_params(s)
            first=tuple(range(6))
            for second in ((6,7,8,9,10,11),
                           (0,6,7,8,9,10),(0,6,3,7,8,9),
                           (0,1,2,6,7,8),(0,1,2,3,4,5)):
                old=exact_two_D6_gluing_kernel(s,first,second)
                r=old["source_line_shared_count"]
                conditional=Fraction(old["conditional_second_probability_after_first_D6"])
                self.assertLessEqual(conditional,
                                     same_global_g_second_D6_conditional_bound(s,r,a,K))
                self.assertGreaterEqual(conditional,0)

    def test_006_fail_closed_out_of_scope_physical_alphabet_and_order(self):
        for s in (0,1,2,4,6,True,False,-8):
            with self.assertRaises(ValueError):
                exact_uniform_original_D6_E2_upper(s)
        for r in (-1,0,7,True):
            with self.assertRaises(ValueError):
                source_line_overlap_pair_capacity(8,r,_params(8)[1])
        s=8
        V,a,K,m=_params(s)
        with self.assertRaises(ValueError):
            same_global_g_second_D6_conditional_bound(s,2,a+1,K)
        with self.assertRaises(ValueError):
            source_line_overlap_pair_capacity(s,2,a+1)
        for r in (-1,7,True):
            with self.assertRaises(ValueError):
                same_global_g_second_D6_conditional_bound(s,r,a,K)


if __name__=="__main__":
    unittest.main()
