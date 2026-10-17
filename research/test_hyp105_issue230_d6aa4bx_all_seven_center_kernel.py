"""AA4-BX true-original seven-GF5 sixcube sharp Boolean center envelope."""
import unittest
from fractions import Fraction
from itertools import permutations
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census, R3_CERTIFIED_FLOORS,
)
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    apply_disjoint_factor_swaps,
)
from hyp105_issue230_d6aa4bx_all_seven_center_kernel import (
    high_degree_boolean_kernel,
    exact_boolean_high_pass_operator_norm,
    all_h_boolean_six_source_kernel_certificate,
    true_original_W32_left_f_quenched_high_pass_envelope,
    true_original_W32_all_seven_center_envelope,
)
SWAPS=((0,1),(2,3),(4,5),(6,7),(8,9),(10,11))

def independent_kernel_formula(k):
    """Second oracle: enumerate spectral masks and bits with no K utility."""
    n=1<<k
    vals=[]
    for x in range(n):
        z=0
        for subset in range(n):
            if len([i for i in range(k) if subset & 1<<i])>=4:
                z+=(-1 if sum(bool(subset & x & 1<<i) for i in range(k))%2 else 1)
        vals.append(z)
    return tuple(vals)

class RealOriginalAllSevenCenterEnvelope(unittest.TestCase):
    def test_01_exact_sharp_boolean_kernel_k0to6_and_independent_extremizers(self):
        expect=(Fraction(0),Fraction(0),Fraction(0),Fraction(0),
                Fraction(1,2),Fraction(15,16),Fraction(51,32))
        self.assertEqual(all_h_boolean_six_source_kernel_certificate()[
            "uniform_boolean_per_Q_high_pass_exact_operator_norms"],expect)
        for k in range(7):
            K=high_degree_boolean_kernel(k)
            self.assertEqual(K,independent_kernel_formula(k))
            n=1<<k
            value=Fraction(sum(z for z in K if z>0),n)
            self.assertEqual(value,expect[k])
            self.assertEqual(-Fraction(sum(z for z in K if z<0),n),expect[k])
            self.assertEqual(Fraction(sum(abs(z) for z in K),2*n),expect[k])
            # These are abstract Boolean indicators, NOT actual W3 GF5 Q:
            # extremizer 1_{K>0} proves universal Boolean norm sharp.
        for k in (-1,7,True,6.0):
            with self.assertRaises(ValueError):
                high_degree_boolean_kernel(k)

    def test_02_fixed_f_original_W32_source_envelope_no_g_dependency(self):
        for scheme in ("lex","S72"):
            m=fixture(1,scheme)
            a=true_original_W32_left_f_quenched_high_pass_envelope(m,SWAPS)
            self.assertEqual(a["n_original_left_sixflag_candidates"],62370)
            self.assertEqual(sum(a["source_Q_touch_count_histogram"].values()),
                             a["n_original_Q_with_possible_selected_GF5_class"])
            self.assertLess(a["fixed_f_all_seven_weighted_high_pass_error_upper"],
                            a["older_naive_22_termwise_triangle_error_upper"])
            shuffled=dict(m,right_labels=tuple(reversed(m["right_labels"])))
            b=true_original_W32_left_f_quenched_high_pass_envelope(shuffled,SWAPS)
            self.assertEqual(a["fixed_f_all_seven_weighted_high_pass_error_upper"],
                             b["fixed_f_all_seven_weighted_high_pass_error_upper"])
            self.assertEqual(a["source_selected_class_by_touch_count"],
                             b["source_selected_class_by_touch_count"])
            print("AA4BX_REAL_W32_GEOMETRIC_ENVELOPE",scheme,
                  "E_f",a["fixed_f_all_seven_weighted_high_pass_error_upper"],
                  "naive",a["older_naive_22_termwise_triangle_error_upper"],
                  "source_degree_histogram",a["source_Q_touch_count_histogram"],flush=True)

    def test_03_true_original_FULL_64_global_right_maps_ALL_SEVEN_GF5(self):
        for scheme in ("lex","S72"):
            m=fixture(1,scheme)
            result=true_original_W32_all_seven_center_envelope(m,SWAPS)
            full=result["full_64_true_original_historical_seven_class_counts"]
            self.assertEqual(len(full),64)
            self.assertEqual(result["original_center_actual_weighted_necessary_GF5_numerator"],
                             seven_census(m,independent_checks=False)[
                                 "GF5_seven_lower_numerator"])
            self.assertEqual(result["original_center_actual_weighted_necessary_GF5_numerator"],
                             result["original_center_degree_at_most_three_part"]+
                             result["original_center_signed_high_order_correction"])
            bound=result["quenched_geometric_source_envelope"][
                "fixed_f_all_seven_weighted_high_pass_error_upper"]
            self.assertLessEqual(
                max(abs(x) for x in result["signed_higher_order_weighted_values"]),bound)
            for vertex in range(64):
                expected=sum(full[vertex][c]*R3_CERTIFIED_FLOORS[c]
                             for c in R3_CERTIFIED_FLOORS)
                self.assertEqual(
                  result["full_64_original_GF5_seven_weighted_necessary_numerators"][vertex],
                  expected)
            print("AA4BX_REAL_W32_CENTER",scheme,
                  "weighted_score",result["original_center_actual_weighted_necessary_GF5_numerator"],
                  "signed_tail",result["original_center_signed_high_order_correction"],
                  "P_leq3",result["original_center_degree_at_most_three_part"],
                  "lower",result["original_center_certified_lower"],flush=True)

    def test_04_exact_source_LOCAL_same_Q_high_order_vs_FULL_historical_census(self):
        m=fixture(1,"lex")
        result=true_original_W32_all_seven_center_envelope(
            m,SWAPS,local_oracle=True)
        self.assertEqual(result["exact_source_Q_local_signed_higher_order_at_original_center"],
                         result["original_center_signed_high_order_correction"])

    def test_05_independent_original_CENTER_signed_fourier_inversion(self):
        m=fixture(1,"S72")
        result=true_original_W32_all_seven_center_envelope(m,SWAPS)
        vals=result["full_64_original_GF5_seven_weighted_necessary_numerators"]
        n=64
        for x in (0,1,3,7,11,31,32,63):
            # Direct signed transform, independent of fast Walsh routine.
            approx=Fraction(sum(
                sum(((-1 if (T&y).bit_count()%2 else 1)*vals[y])
                    for y in range(n))*
                (-1 if (T&x).bit_count()%2 else 1)
                for T in range(n) if T.bit_count()<=3),n)
            self.assertEqual(approx,result["degree_at_most_three_weighted_values"][x])
            self.assertEqual(Fraction(vals[x])-approx,
                             result["signed_higher_order_weighted_values"][x])

    def test_06_guards_original_line_pairs_true_W32_only(self):
        m=fixture(1,"lex")
        with self.assertRaises(ValueError):
            true_original_W32_left_f_quenched_high_pass_envelope(m,SWAPS[:5])
        with self.assertRaises(ValueError):
            true_original_W32_left_f_quenched_high_pass_envelope(
                m,((0,1),(1,2),(3,4),(5,6),(7,8),(9,10)))
        with self.assertRaises(ValueError):
            true_original_W32_all_seven_center_envelope(fixture(2,"lex"),SWAPS)
        with self.assertRaises(ValueError):
            high_degree_boolean_kernel(5,cutoff=-1)
        with self.assertRaises(ValueError):
            high_degree_boolean_kernel(5,cutoff=True)

if __name__=="__main__":
    unittest.main()
