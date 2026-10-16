"""HYP-105 #230 AA4-AR: real ORIGINAL good flag-wedge theorem."""
import unittest
from fractions import Fraction

from hyp105_issue230_d6aa4ar_good_wedges_port_balance import (
    all_h_original_good_wedge_lower,
    exact_true_original_good_D_two_port_wedge_certificate,
    independent_original_literal_good_two_port_wedges)
from hyp105_issue230_d6aa4aq_colored_original_D_cycle import (
    exact_original_rainbow_D6_cycle_transfer)
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32)
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model)


class ActualOriginalGoodWedges(unittest.TestCase):
    def test_01_all_h14_and_above_rational_source_good_wedges(self):
        for h in list(range(14,27))+[28,30,40,48,60]:
            s=1<<h
            z=all_h_original_good_wedge_lower(s)
            self.assertEqual(z["universally_original_good_D_edge_lower"],Fraction(s**5,10))
            self.assertEqual(z[
                "unconditional_true_original_good_TWO_EDGE_wedge_lower"],
                Fraction(s**6,200))
            self.assertGreaterEqual(z["exact_Jensen_good_wedge_floor"],
                Fraction(s**6,200))
            self.assertEqual(z[
                "conditional_port_defect_le_quarter_degree_energy_then_true_original_opposite_wedges_lower"],
                Fraction(s**6,800))
            self.assertEqual(z["actual_original_flag_vertex_count"],
                (s+1)**2*(s*s+1))
            self.assertTrue(z["SOURCE_good_wedge_s6_PROVED_for_all_f_g"])
            self.assertTrue(z["OPPOSITE_wedge_s6_unconditional_NOT_PROVED"])
            self.assertTrue(z["original_full_seven_GF5_S_s6_NOT_PROVED"])
        for h in range(1,14):
            z=all_h_original_good_wedge_lower(1<<h)
            self.assertFalse(z["SOURCE_good_wedge_s6_PROVED_for_all_f_g"])
            self.assertIsNone(z["unconditional_true_original_good_TWO_EDGE_wedge_lower"])
        for invalid in (0,3,True,-2):
            with self.assertRaises(ValueError):
                all_h_original_good_wedge_lower(invalid)

    def test_02_true_W32_all_five_global_original_maps_literal_wedge_referee(self):
        known={"dual_zero":277,"lex":307,"reverse":300,"S68":257,"S72":261}
        for name,m in [("dual_zero",zero_split_original_W32())]+[
             (scheme,fixture(1,scheme))
             for scheme in ("lex","reverse","S68","S72")]:
            z=exact_true_original_good_D_two_port_wedge_certificate(m)
            independent=independent_original_literal_good_two_port_wedges(m)
            self.assertEqual(z["D_ALL_actual_original_bilateral_edges"],known[name])
            self.assertEqual(z["D_GOOD_actual_original_bilateral_edges"],known[name])
            self.assertEqual(z["D_BAD_actual_original_bilateral_edges"],0)
            self.assertEqual(z["good_D_original_TWO_EDGE_unordered_wedges"],
                             independent["actual_original_literal_all_wedges"])
            self.assertEqual(z["good_D_original_OPPOSITE_TWO_TYPED_port_wedges"],
                             independent["actual_original_literal_two_type_opposite_wedges"])
            self.assertEqual(z["true_original_two_typed_port_imbalance_energy"]*2+
                             8*z["good_D_original_OPPOSITE_TWO_TYPED_port_wedges"],
                             z["true_original_good_D_degree_squared_energy"]+
                             z["true_original_diagonal_group_imbalance_energy"])
            self.assertEqual(independent[
                "bad_repeated_original_factor_opposite_wedges"],0)
            self.assertGreater(z["good_D_original_TWO_EDGE_unordered_wedges"],0)
            self.assertGreater(z["good_D_original_OPPOSITE_TWO_TYPED_port_wedges"],0)
            print("AA4AR_TRUE_W32",name,
                  "D_good",z["D_GOOD_actual_original_bilateral_edges"],
                  "original_uncolored_good_wedges",z["good_D_original_TWO_EDGE_unordered_wedges"],
                  "original_two_type_opposite_good_wedges",
                      z["good_D_original_OPPOSITE_TWO_TYPED_port_wedges"],
                  "defect",z["true_original_two_typed_port_imbalance_energy"],
                  "balance_conditional",z["port_balance_conditional_hypothesis_fulfilled"])

    def test_03_original_W32_S68_S72_many_real_opposite_wedges_but_zero_D6(self):
        for scheme in ("S68","S72"):
            m=fixture(1,scheme)
            z=exact_true_original_good_D_two_port_wedge_certificate(m)
            self.assertGreater(z["good_D_original_OPPOSITE_TWO_TYPED_port_wedges"],0)
            d6=exact_original_rainbow_D6_cycle_transfer(m)
            self.assertTrue(d6["global_root_scan_complete"])
            self.assertEqual(d6["double_rainbow_D6_original_Q_count"],0)
            self.assertTrue(z["no_source_six_ID_D6_or_full_GF5_lower_claim"])

    def test_04_true_W34_lex_random_global_injected_source_original_flag_wedges(self):
        from hyp105_issue230_d6aa4ap_uniform_good_original_D_spectral import (
            finite_genuine_original_good_D_audit)
        known={"lex":(6529,2072),"random":(6327,147)}
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            z=exact_true_original_good_D_two_port_wedge_certificate(m)
            r=independent_original_literal_good_two_port_wedges(m)
            g=finite_genuine_original_good_D_audit(m)
            self.assertEqual((z["D_ALL_actual_original_bilateral_edges"],
                              z["D_GOOD_actual_original_bilateral_edges"]),known[scheme])
            self.assertEqual(g["good_D_avoiding_all_four_bad_PHYSICAL_ports"],
                             z["D_GOOD_actual_original_bilateral_edges"])
            self.assertEqual(z["good_D_original_TWO_EDGE_unordered_wedges"],
                             r["actual_original_literal_all_wedges"])
            self.assertEqual(z["good_D_original_OPPOSITE_TWO_TYPED_port_wedges"],
                             r["actual_original_literal_two_type_opposite_wedges"])
            self.assertEqual(r["bad_repeated_original_factor_opposite_wedges"],0)
            self.assertTrue(z["true_original_good_D_degree_squared_energy"]>=0)
            print("AA4AR_TRUE_W34",scheme,"Dgood",
                  z["D_GOOD_actual_original_bilateral_edges"],
                  "good_flag_wedges",z["good_D_original_TWO_EDGE_unordered_wedges"],
                  "opposite_2port_wedges",z["good_D_original_OPPOSITE_TWO_TYPED_port_wedges"],
                  "original_port_defect",z["true_original_two_typed_port_imbalance_energy"])

    def test_05_actual_source_symplectic_and_independent_typed_physical_invariance(self):
        m=zero_split_original_W32()
        p,l=symplectic_transvection_source(m,1)
        changed=transform_model(
            m,point_sources=p,line_sources=l,
            point_coordinates=tuple(reversed(range(6))),
            line_coordinates=tuple((i+2)%6 for i in range(6)))
        left=exact_true_original_good_D_two_port_wedge_certificate(m)
        right=exact_true_original_good_D_two_port_wedge_certificate(changed)
        for k in (
            "D_ALL_actual_original_bilateral_edges",
            "D_GOOD_actual_original_bilateral_edges",
            "good_D_original_TWO_EDGE_unordered_wedges",
            "good_D_original_OPPOSITE_TWO_TYPED_port_wedges",
            "true_original_good_D_degree_squared_energy",
            "true_original_two_typed_port_imbalance_energy",
            "true_original_diagonal_group_imbalance_energy"):
            self.assertEqual(left[k],right[k])

    def test_06_artificial_port_defect_warning_and_strict_false_model_rejection(self):
        # Algebraic countermodel to wedge positivity from edge degree alone,
        # NOT an actual globally mapped W(3,s) original source system.
        for degree in (1,2,8,1000):
            x00,x01,x10,x11=degree,0,0,0
            complement=x00*x11+x01*x10
            im=(x00-x11)**2+(x01-x10)**2
            grp=(x00+x11-x01-x10)**2
            self.assertEqual(complement,0)
            self.assertEqual(8*complement,degree**2+grp-2*im)
            if degree>=2:
                self.assertGreater(degree*(degree-1)//2,0)
        m=zero_split_original_W32()
        for corrupted in (
            dict(m,left_labels=((0,1),)*15),
            dict(m,right_labels=((0,1),)*15),
            dict(m,incidences=m["incidences"][:-1]),
        ):
            with self.assertRaises((ValueError,AssertionError)):
                exact_true_original_good_D_two_port_wedge_certificate(corrupted)
        with self.assertRaises(ValueError):
            independent_original_literal_good_two_port_wedges(fixture(3,"lex"))


if __name__=="__main__":
    unittest.main()
