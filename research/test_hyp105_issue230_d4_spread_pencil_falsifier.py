"""Falsifiable REAL W(3,4)/W(3,8) symplectic spread infinite-route NO-GO."""
import unittest
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_issue230_d4_spread_pencil_falsifier import (
    plan, irreducible_symmetric_parameter, actual_original_symplectic_spread,
    balanced_right_labels, true_spread_counterfamily,report,
)
from hyp105_b1_symplectic import GF2Power,symplectic
from hyp105_issue230_proof_audit import parameters
from hyp105_issue230_projection import ProjectionClosure


class Issue230D4TrueSpreadTests(unittest.TestCase):
    def test_all_h_arithmetic_no_extrapolated_geometry(self):
        for power in range(2,14):
            with self.subTest(power=power):
                s=2**power
                q=plan(s)
                self.assertGreater(q["selected_disjoint_original_spread_lines"],0)
                self.assertLessEqual(q["selected_disjoint_original_spread_lines"],s*s+1)
                self.assertLessEqual(q["selected_original_points"],q["V"])
                self.assertLessEqual(q["selected_original_points"],comb(q["a"],2))
                self.assertEqual(q["forced_original_collinear_shared_coordinate_Mf_floor"],
                                 q["selected_disjoint_original_spread_lines"]*comb(s+1,2))
                self.assertEqual(q["forced_original_left_endpoint_bad_pairs_floor"],
                                 2*s*q["forced_original_collinear_shared_coordinate_Mf_floor"])
                self.assertLessEqual(q["spread_lines_per_anchor"]*(s+1),
                                     q["other_coordinates"])

    def test_asymptotic_constants_proved_from_exact_arithmetic(self):
        # These finite values are regression sanity; the proof that the
        # ratios converge to 3/32 and 9/32 is in the companion derivation.
        for s in (256,512,1024,2048,4096,8192,16384):
            x=plan(s)
            ratio_m=Fraction(x["forced_original_collinear_shared_coordinate_Mf_floor"],s**4)
            ratio_e=Fraction(x["exact_rational_mean_lower_numerator"],
                             x["exact_rational_mean_lower_denominator"]*s**6)
            self.assertGreater(ratio_m,0)
            self.assertGreater(ratio_e,0)
            if s>=4096:
                self.assertGreater(ratio_m,Fraction(6,100))
                self.assertGreater(ratio_e,Fraction(15,100))

    def test_true_spread_uses_nonzero_irreducible_binary_matrix(self):
        for h in (1,2,3,4):
            f=GF2Power(h)
            c=irreducible_symmetric_parameter(f)
            self.assertNotEqual(c,0)
            for z in range(f.q):
                self.assertNotEqual(f.mul(z,z)^f.mul(c,z)^1,0)

    def test_actual_original_W34_W38_spreads_are_isotropic_and_disjoint(self):
        for h in (2,3):
            with self.subTest(h=h):
                (field,points,lines,incidences),spread,c=actual_original_symplectic_spread(h)
                self.assertEqual(len(spread),field.q**2+1)
                self.assertEqual(len(set(spread)),len(spread))
                self.assertEqual(set(p for li in spread for p in lines[li]),
                                 set(range(len(points))))
                self.assertEqual(sum(map(lambda li:len(lines[li]),spread)),len(points))
                self.assertEqual(len(points),(field.q+1)*(field.q**2+1))
                self.assertEqual(len(incidences),len(points)*(field.q+1))
                for li in spread:
                    self.assertTrue(all(symplectic(points[p],points[q],field)==0
                                        for p,q in combinations(lines[li],2)))

    def test_actual_W34_explicit_global_f_g_and_signed_mean_lower(self):
        x=true_spread_counterfamily(2,check_full_energy=True)
        self.assertEqual(x["s"],4)
        self.assertTrue(x["global_left_unordered_pair_injection"])
        self.assertTrue(x["global_right_unordered_pair_injection"])
        self.assertTrue(x["mean_lower_checked"])
        self.assertGreaterEqual(x["Mf_actual"],
                                x["forced_original_collinear_shared_coordinate_Mf_floor"])
        self.assertGreaterEqual(Fraction(x["W_original_mean"]),
                                Fraction(x["exact_rational_mean_lower_numerator"],
                                         x["exact_rational_mean_lower_denominator"]))
        self.assertGreaterEqual(x["true_original_right_label_star_min"],x["a"]-3)

    def test_actual_W38_explicit_global_f_g_and_signed_mean_lower(self):
        x=true_spread_counterfamily(3,check_full_energy=True)
        self.assertEqual(x["s"],8)
        self.assertTrue(x["all_spread_lines_are_true_original_W3s"])
        self.assertEqual(x["selected_disjoint_original_spread_lines"],8)
        self.assertEqual(x["forced_original_collinear_shared_coordinate_Mf_floor"],288)
        self.assertGreaterEqual(x["Mf_actual"],288)
        self.assertEqual(x["true_original_right_label_star_min"],x["a"]-3)
        self.assertGreaterEqual(Fraction(x["W_original_mean"]),
                                Fraction(x["exact_rational_mean_lower_numerator"],
                                         x["exact_rational_mean_lower_denominator"]))
        self.assertFalse(x["original_7_family_S_lower_proved"])
        self.assertFalse(x["infinite_original_S_small_counterexample_proved"])

    def test_balanced_g_right_pair_map_has_at_most_two_omissions_per_coordinate(self):
        for s in (4,8,16,32,64):
            a=parameters(s)["a"]
            labels=balanced_right_labels(s,a)
            self.assertEqual(len(labels),parameters(s)["V"])
            self.assertEqual(len(set(labels)),len(labels))
            sums=[0]*a
            for u,v in labels:
                sums[u]+=1
                sums[v]+=1
            self.assertGreaterEqual(min(sums),a-3)
            self.assertLessEqual(max(sums),a-1)

    def test_report_marks_only_D3_route_falsified_not_root(self):
        r=report()
        self.assertTrue(r["all_h_counterfamily_for_D3_Mf_little_o"])
        self.assertTrue(r["all_h_counterfamily_for_D3_Wmean_little_o"])
        self.assertEqual(r["universal_original_Mf_o_s39over10"],"FALSE")
        self.assertEqual(r["universal_original_Wmean_o_s59over10"],"FALSE")
        self.assertEqual(r["universal_all_seven_S_lower"],"OPEN")
        self.assertEqual(r["infinite_Branch_B_S_small"],"NOT ESTABLISHED")
        self.assertEqual(len(r["actual_original_geometry_certificates"]),2)


if __name__=="__main__":
    unittest.main()
