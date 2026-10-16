"""HYP-105 #230 AA4-AR: real ORIGINAL good flag-wedge theorem."""
import unittest
from fractions import Fraction

from hyp105_issue230_d6aa4ar_good_wedges_port_balance import (
    all_h_original_good_wedge_lower,
    exact_true_original_good_D_two_port_wedge_certificate,
    independent_original_literal_good_two_port_wedges,
    conditional_all_h_good_wedge_to_original_seven_lower,
    exact_true_W32_original_seven_covered_good_wedges)
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
        # Frozen independently hosted literal ORIGINAL source D -> 3-flag
        # wedge census. Values: D, uncolored GOOD wedges, two-typed
        # opposite-port GOOD wedges, genuine global port defect.
        known={"dual_zero":(277,3203,870,226),
               "lex":(307,3924,1105,264),
               "reverse":(300,3768,1013,236),
               "S68":(257,2715,697,270),
               "S72":(261,2811,750,250)}
        for name,m in [("dual_zero",zero_split_original_W32())]+[
             (scheme,fixture(1,scheme))
             for scheme in ("lex","reverse","S68","S72")]:
            z=exact_true_original_good_D_two_port_wedge_certificate(m)
            independent=independent_original_literal_good_two_port_wedges(m)
            self.assertEqual(z["D_ALL_actual_original_bilateral_edges"],known[name][0])
            self.assertEqual(z["D_GOOD_actual_original_bilateral_edges"],known[name][0])
            self.assertEqual(z["D_BAD_actual_original_bilateral_edges"],0)
            self.assertEqual((z["good_D_original_TWO_EDGE_unordered_wedges"],
                              z["good_D_original_OPPOSITE_TWO_TYPED_port_wedges"],
                              z["true_original_two_typed_port_imbalance_energy"]),
                             known[name][1:])
            self.assertTrue(z["port_balance_conditional_hypothesis_fulfilled"])
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
        # Two TRUE original W34 complete globally injected point/line
        # maps already refute a proposed 'all h>=1 ALL f,g' port-defect
        # <=quarter-degree-energy lemma; this says NOTHING about h>=14.
        known={"lex":(6529,2072,23836,3544,15006,51816),
               "random":(6327,147,217,10,528,728)}
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            z=exact_true_original_good_D_two_port_wedge_certificate(m)
            r=independent_original_literal_good_two_port_wedges(m)
            g=finite_genuine_original_good_D_audit(m)
            self.assertEqual((z["D_ALL_actual_original_bilateral_edges"],
                              z["D_GOOD_actual_original_bilateral_edges"]),known[scheme][:2])
            self.assertEqual(g["good_D_avoiding_all_four_bad_PHYSICAL_ports"],
                             z["D_GOOD_actual_original_bilateral_edges"])
            self.assertEqual((z["good_D_original_TWO_EDGE_unordered_wedges"],
                              z["good_D_original_OPPOSITE_TWO_TYPED_port_wedges"],
                              z["true_original_two_typed_port_imbalance_energy"],
                              z["true_original_good_D_degree_squared_energy"]),
                             known[scheme][2:])
            self.assertFalse(z["port_balance_conditional_hypothesis_fulfilled"])
            self.assertGreater(4*z["true_original_two_typed_port_imbalance_energy"],
                               z["true_original_good_D_degree_squared_energy"])
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

    def test_04b_all_h_conditional_good_wedge_to_original_seven_Q_bounded_charge(self):
        for h in (1,13,14,15,24,40,60):
            s=1<<h
            for alpha in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(1)):
                z=conditional_all_h_good_wedge_to_original_seven_lower(s,alpha)
                self.assertEqual(z["per_genuine_original_six_ID_Q_max_centered_good_wedges"],6)
                self.assertTrue(z["this_fraction_hypothesis_NOT_PROVED_for_all_f_g"])
                if h>=14:
                    desired=Fraction(alpha*s**6,1200)
                    self.assertEqual(z["exact_rational_asymptotic_lower_if_h_ge_14"],desired)
                    self.assertEqual(z["conditional_minimum_selected_original_six_Q_count"],
                                     (desired.numerator+desired.denominator-1)//desired.denominator)
                else:
                    self.assertIsNone(z["conditional_minimum_selected_original_six_Q_count"])
        for bad in (Fraction(-1,10),Fraction(11,10)):
            with self.assertRaises(ValueError):
                conditional_all_h_good_wedge_to_original_seven_lower(1<<14,bad)

    def test_04c_complete_true_original_W32_good_wedge_seven_Q_coverage(self):
        # Literal source six-ID Q from pre-existing 62,370 genuine
        # W32 source oracle, not invented physical six-label patterns.
        from hyp105_g5e2b3e1b0_seven_signature import seven_census
        from hyp105_issue230_d6aa4ar_good_wedges_port_balance import (
            _good_D_edge_graph)
        from itertools import combinations
        # Frozen independent first-hosted six-ID source Q-to-3-flag
        # and literal 3-flag-to-Q intersection counts.
        expected={"dual_zero":(3203,38,3165,40),
                  "lex":(3924,172,3752,237),
                  "reverse":(3768,66,3702,68),
                  "S68":(2715,6,2709,6),
                  "S72":(2811,11,2800,11)}
        for name,m in [("dual_zero",zero_split_original_W32())]+[
             (name,fixture(1,name)) for name in ("lex","reverse","S68","S72")]:
            z=exact_true_W32_original_seven_covered_good_wedges(m)
            self.assertEqual((
                z["genuine_original_good_source_three_flag_wedges"],
                z["distinct_good_wedges_covered_by_some_true_original_seven_Q"],
                z["distinct_good_wedges_NOT_covered_by_ANY_seven_Q"],
                z["all_original_good_wedge_to_six_Q_charge_incidences"]),
                expected[name])
            original=seven_census(m,independent_checks=False,witness_sets=True)["sets"]
            self.assertEqual(z["true_original_seven_selected_six_ID_Q"],len(original))
            self.assertEqual(z["all_original_good_wedge_to_six_Q_charge_incidences"],
                             sum(z["original_seven_tag_charge_by_class"].values()))
            self.assertLessEqual(z["all_original_good_wedge_to_six_Q_charge_incidences"],
                                 6*z["true_original_seven_selected_six_ID_Q"])
            self.assertTrue(z["all_selected_six_Q_capacity_6_validated"])
            self.assertEqual(z["original_seven_tag_charge_by_class"].get("B/B-disjoint",0),0)
            self.assertEqual(z["original_seven_tag_charge_by_class"].get("C/A",0),0)
            self.assertEqual(z["original_seven_tag_charge_by_class"].get("C/B",0),0)
            self.assertEqual(z["original_seven_tag_charge_by_class"].get("D6",0),
                             6*z["original_seven_tag_Q_count"].get("D6",0))
            self.assertEqual(z["distinct_good_wedges_covered_by_some_true_original_seven_Q"]+
                             z["distinct_good_wedges_NOT_covered_by_ANY_seven_Q"],
                             z["genuine_original_good_source_three_flag_wedges"])
            self.assertLessEqual(
                z["distinct_good_wedges_covered_by_some_true_original_seven_Q"],
                z["all_original_good_wedge_to_six_Q_charge_incidences"])
            # Separate original wedge-centered direct Q-membership
            # referee; no dependence on source Q->wedge formula.
            if name in ("S68","S72"):
                G,good,neighbors,badP,badL=_good_D_edge_graph(m)
                candidates=set()
                for center,row in enumerate(neighbors):
                    ns=sorted(t for t,_,_ in row)
                    for a,b in combinations(ns,2):
                        candidates.add((center,a,b))
                Qsets=[frozenset(Q) for Q in original]
                direct=sum(any({c,a,b}.issubset(Q) for Q in Qsets)
                           for c,a,b in candidates)
                self.assertEqual(direct,z[
                    "distinct_good_wedges_covered_by_some_true_original_seven_Q"])
            print("AA4AR_W32_GENUINE_3_TO_6",name,
                  "all_original_good_wedges",z["genuine_original_good_source_three_flag_wedges"],
                  "covered_original_good_wedges",z[
                      "distinct_good_wedges_covered_by_some_true_original_seven_Q"],
                  "uncovered_original_good_wedges",z[
                      "distinct_good_wedges_NOT_covered_by_ANY_seven_Q"],
                  "charge_incidences",z[
                      "all_original_good_wedge_to_six_Q_charge_incidences"],
                  "covered_fraction",str(z["true_original_good_wedge_coverage_fraction"]))

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
        # Existing fixture(3) would create a much larger true W(3,8);
        # this research-only literal referee intentionally avoids that cost.
        self.assertTrue(independent_original_literal_good_two_port_wedges(
            zero_split_original_W32())["independent_from_four_bin_and_degree_identity"])


if __name__=="__main__":
    unittest.main()
