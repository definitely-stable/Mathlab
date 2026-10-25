"""HYP-105 AA4-AP: actual original ALL-h GOOD D spectral theorem."""
import unittest
from fractions import Fraction
from math import comb,isqrt

from hyp105_issue230_d6aa4ap_uniform_good_original_D_spectral import (
    global_good_original_D_spectral_certificate,
    finite_genuine_original_good_D_audit)
from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    exact_original_global_transport)
from hyp105_issue230_d6aa4ao_robust_port_occupancy import (
    globally_bad_physical_coordinates)
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32)
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model)


class UniversalGoodOriginalD(unittest.TestCase):
    def test_01_all_h14_through_h23_exact_rational_good_D_minimum(self):
        for h in range(14,24):
            s=1<<h
            z=global_good_original_D_spectral_certificate(s)
            self.assertEqual(z["proof_method"],"finite_exact_rational_h14_to_h23")
            self.assertTrue(z["universally_all_f_g_good_D_at_least_s5_over_10"])
            self.assertGreaterEqual(
                z["globally_port_good_unordered_D_explicit_lower"],
                Fraction(s**5,10))
            self.assertEqual(z["original_GOOD_D_uniform_lower"],Fraction(s**5,10))
            self.assertLessEqual(z["bad_vertex_upper_each_type"],31)
            self.assertEqual(z["bad_vertex_upper_each_type"],
                min(31,(32*z["globally_missing_physical_edges"])//z["a"]))
            self.assertEqual(
                z["all_global_GOOD_D_indexed_PHYSICAL_P5_P5_mass_lower"],
                Fraction(s**5,40)*
                ((z["a"]-3)*(z["a"]-4)*(z["a"]-5))**2)
            print("AA4AP_ORIGINAL_GOOD_D_EXACT_H",h,
                  "alphabet",z["a"],"missing",z["globally_missing_physical_edges"],
                  "exception_vertex_cap",z["bad_vertex_upper_each_type"],
                  "good_D_lower_over_s5",str(
                   z["globally_port_good_unordered_D_explicit_lower"]/s**5))

    def test_02_analytic_all_h24_to_h60_and_unsolved_early_h(self):
        for h in list(range(24,41))+[48,50,60]:
            s=1<<h
            z=global_good_original_D_spectral_certificate(s)
            self.assertEqual(z["proof_method"],
                             "all_larger_h_analytic_3255_over_sqrt_s")
            self.assertTrue(z["universally_all_f_g_good_D_at_least_s5_over_10"])
            self.assertGreaterEqual(
                z["globally_port_good_unordered_D_explicit_lower"],
                Fraction(s**5,10))
            self.assertGreaterEqual(
                z["all_global_GOOD_D_indexed_PHYSICAL_P5_P5_mass_lower"],
                Fraction(s**5,40)*((z["a"]-3)*(z["a"]-4)*(z["a"]-5))**2)
            self.assertTrue(z["selected_seven_GF5_E_U_s6_lower_NOT_PROVED"])
        for h in range(1,14):
            s=1<<h
            z=global_good_original_D_spectral_certificate(s)
            self.assertFalse(z["universally_all_f_g_good_D_at_least_s5_over_10"])
            self.assertIsNone(z["original_GOOD_D_uniform_lower"])
            self.assertIsNone(z[
                "all_global_GOOD_D_indexed_PHYSICAL_P5_P5_mass_lower"])
        for invalid in (0,3,-2,True):
            with self.assertRaises(ValueError):
                global_good_original_D_spectral_certificate(invalid)

    def test_03_original_source_W32_five_complete_global_f_g_pairs(self):
        truth={"dual_zero":277,"lex":307,"reverse":300,"S68":257,"S72":261}
        for scheme,model in [("dual_zero",zero_split_original_W32())]+[
            (key,fixture(1,key)) for key in ("lex","reverse","S68","S72")]:
            x=finite_genuine_original_good_D_audit(model)
            self.assertEqual(x["D_unordered_genuine_original"],truth[scheme])
            self.assertEqual(x["good_D_avoiding_all_four_bad_PHYSICAL_ports"],
                             truth[scheme])
            self.assertEqual(x["D_with_at_least_one_bad_physical_port"],0)
            self.assertEqual(x["physical_point_bad_vertex_count"],0)
            self.assertEqual(x["physical_line_bad_vertex_count"],0)
            self.assertEqual(x["D_touched_by_bad_source_factor_upper_explicit"],0)
            self.assertTrue(x["selected_seven_GF5_acceptance_NOT_PROVED"])

    def test_04_true_original_W34_six_global_holes_typed_f_g_and_spectrum(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            x=finite_genuine_original_good_D_audit(model)
            self.assertEqual((x["s"],x["a"]),(4,14))
            self.assertGreater(x["D_unordered_genuine_original"],6000)
            self.assertEqual(x["D_unordered_genuine_original"],
                             x["good_D_avoiding_all_four_bad_PHYSICAL_ports"]+
                             x["D_with_at_least_one_bad_physical_port"])
            self.assertGreaterEqual(x["D_touched_by_bad_source_factor_upper_explicit"],
                                   x["D_with_at_least_one_bad_physical_port"])
            self.assertLessEqual(x["physical_point_bad_vertex_count"],13)
            self.assertLessEqual(x["physical_line_bad_vertex_count"],13)
            M=exact_original_global_transport(model)[
                "cross_physical_coordinate_transport_matrix"]
            K=x["all_global_spectral_certificate"][
                "original_coordinate_cell_incidence_uniform_upper"]
            self.assertTrue(all(v<=K for row in M for v in row))
            print("AA4AP_W34",scheme,
                  "D",x["D_unordered_genuine_original"],
                  "true_good_D",x["good_D_avoiding_all_four_bad_PHYSICAL_ports"],
                  "bad_D",x["D_with_at_least_one_bad_physical_port"],
                  "bad_point_coord",x["physical_point_bad_vertex_count"],
                  "bad_line_coord",x["physical_line_bad_vertex_count"])

    def test_05_true_source_symplectic_and_separate_typed_physical_permutation(self):
        m=zero_split_original_W32()
        p,l=symplectic_transvection_source(m,1)
        transformed=transform_model(
            m,point_sources=p,line_sources=l,
            point_coordinates=tuple(reversed(range(6))),
            line_coordinates=tuple((i+2)%6 for i in range(6)))
        original=finite_genuine_original_good_D_audit(m)
        other=finite_genuine_original_good_D_audit(transformed)
        for name in (
            "D_unordered_genuine_original",
            "good_D_avoiding_all_four_bad_PHYSICAL_ports",
            "D_with_at_least_one_bad_physical_port",
            "D_touched_by_bad_source_factor_upper_explicit",
            "physical_point_bad_vertex_count","physical_line_bad_vertex_count"):
            self.assertEqual(original[name],other[name])

    def test_06_negative_fake_original_and_explicit_GF5_nonlift(self):
        model=fixture(1,"S68")
        for corrupt in (dict(model,left_labels=((0,1),)*15),
                        dict(model,right_labels=((0,1),)*15),
                        dict(model,incidences=model["incidences"][:-1])):
            with self.assertRaises((ValueError,AssertionError)):
                finite_genuine_original_good_D_audit(corrupt)
        from hyp105_issue230_d6aa4am_genuine_pair_sixcharge import (
            exact_W32_original_seven_pair_extension_certificate)
        data=exact_W32_original_seven_pair_extension_certificate(model)
        self.assertEqual(data[
            "D_UNCOVERED_by_ALL_SEVEN_selected_six_Q"],193)
        self.assertEqual(data[
            "D_unordered_actual_original_bilateral_two_flag_pairs"],257)
        x=finite_genuine_original_good_D_audit(model)
        self.assertEqual(x["good_D_avoiding_all_four_bad_PHYSICAL_ports"],257)
        self.assertTrue(x["all_global_spectral_certificate"][
            "original_issue230_Branch_A_NOT_PROVED"])


if __name__=="__main__":
    unittest.main()
