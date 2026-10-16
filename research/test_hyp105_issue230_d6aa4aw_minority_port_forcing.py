"""AA4-AW: independent sharp minority-port transport and TRUE source W32/W34."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_d6aa4aw_minority_port_forcing import (
    exact_two_type_integer_port_marginal_minimum,
    exact_true_original_good_minority_port_certificate,
    conditional_all_h_minor_ports_to_seven_GF5)
from hyp105_issue230_d6aa4ar_good_wedges_port_balance import (
    _good_D_edge_graph,exact_true_original_good_D_two_port_wedge_certificate)
from hyp105_issue230_d6aa4av_global_source_aa_good_wedges import (
    independent_literal_true_original_good_D_source_partition)
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32)
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model)


def independent_literal_original_source_both_port_support_referee(model):
    """Genuine original source neighbor-first, but NO marginal optimizer use.

    Count EXACT physical two-type opposite port centered wedges using
    original source incidence-ID outer FLAG pairs, and separately
    whether each TRUE original source center sees two physical point
    endpoint ports and two line endpoint ports.
    """
    G,good,neighbors,badP,badL=_good_D_edge_graph(model)
    categories=Counter()
    total=0
    centers_with_R=0
    for i,row in enumerate(neighbors):
        cp,cl=G["inc"][i]
        pc={x:0 for x in G["left"][cp]}
        lc={x:0 for x in G["right"][cl]}
        for _,p,l in row:
            pc[p]+=1
            lc[l]+=1
        hasp=all(pc.values())
        hasl=all(lc.values())
        categories[(bool(hasp),bool(hasl))]+=1
        val=0
        for a,b in combinations(row,2):
            if a[1]!=b[1] and a[2]!=b[2]:
                val+=1
        if (val>0)!=(hasp and hasl):
            raise AssertionError("independent TRUE ORIGINAL wedge-orientation enumeration disproves binary one-sided port gate")
        centers_with_R+=bool(val)
        total+=val
    return dict(
        literal_real_source_OPPOSITE_port_good_wedges=total,
        source_center_good_port_support_categories=dict(categories),
        literal_centers_with_both_typed_nonzero_opposite_wedges=centers_with_R)


class TrueOriginalMinorityPortForcing(unittest.TestCase):
    def test_01_all_small_four_bin_integers_exact_integer_marginal_minimax_and_sharpness(self):
        checked=0
        for n in range(16):
            for a in range(n+1):
                for b in range(n-a+1):
                    for c in range(n-a-b+1):
                        d=n-a-b-c
                        z=exact_two_type_integer_port_marginal_minimum((a,b,c,d))
                        r0,r1=z["point_port_marginals"]
                        c0,c1=z["line_port_marginals"]
                        # Completely INDEPENDENT brute transportation table
                        # using row/col sums only; do NOT use vertex formula.
                        values=[]
                        for t in range(n+1):
                            u=r0-t;v=c0-t;w=r1-v
                            if min(t,u,v,w)<0 or u+w!=c1 or t+v!=c0:
                                continue
                            values.append(t*w+u*v)
                        self.assertTrue(values)
                        self.assertEqual(z[
                            "sharp_integer_minimum_OPPOSITE_for_fixed_point_line_marginals"],min(values))
                        self.assertEqual(z[
                            "sharp_integer_maximum_OPPOSITE_for_fixed_point_line_marginals"],max(values))
                        self.assertGreaterEqual(z["source_good_two_typed_opposite_wedges"],
                                             z["all_margins_minority_lower"])
                        self.assertGreaterEqual(
                            z["all_margins_minority_lower"],
                            z["half_minor_product_lower"])
                        self.assertEqual(
                            z["both_one_sided_point_line_ports_nonempty"],
                            z["source_good_two_typed_opposite_wedges"]>0)
                        self.assertTrue(z["gamma_delta_exact_one_sided_polarization"])
                        checked+=1
        self.assertGreater(checked,3000)
        # SHARPNESS at balanced point/line ports: all x=m/2 for even m,
        # R=m²/2 and k=l=m. This is a 2x2 MATRIX example, NOT
        # a synthetic original symplectic GQ realization claim.
        for m in (2,4,6,8,10,12):
            z=exact_two_type_integer_port_marginal_minimum((m//2,)*4)
            self.assertEqual(z["source_good_two_typed_opposite_wedges"],m*m//2)
            self.assertEqual(z["all_margins_minority_lower"],m*m//2)
        for fail in ((-1,0,0,0),(1,2,3),(1,2,3,4,5),
                     (True,0,0,0),(0,0,0,0.5),None):
            with self.assertRaises(ValueError):
                exact_two_type_integer_port_marginal_minimum(fail)
        print("AA4AW_ALL_SMALL_2x2_INTEGER_TRANSPORT",checked,"tables exact sharp minimax + point/line marginal positivity equivalence")

    def test_02_five_real_original_W32_GLOBAL_f_g_full_GOOD_2type_referee(self):
        known={
            "dual_zero":(277,2675,870),
            "lex":(307,3259,1105),
            "reverse":(300,3141,1013),
            "S68":(257,2268,697),
            "S72":(261,2346,750),
        }
        for name,m in [("dual_zero",zero_split_original_W32())]+[
                 (x,fixture(1,x)) for x in ("lex","reverse","S68","S72")]:
            z=exact_true_original_good_minority_port_certificate(m)
            old=exact_true_original_good_D_two_port_wedge_certificate(m)
            literal=independent_literal_original_source_both_port_support_referee(m)
            self.assertEqual((z["original_good_D_pair_count"],
                              z["original_source_AA_good_threeflag_wedge_count"],
                              z["original_both_typed_opposite_GOOD_threeflag_wedge_count"]),
                             known[name])
            self.assertEqual(z[
                "original_both_typed_opposite_GOOD_threeflag_wedge_count"],
                literal["literal_real_source_OPPOSITE_port_good_wedges"])
            self.assertEqual(z["original_source_port_support_categories"],
                             {("two_point_ports" if p else "one_point_port",
                               "two_line_ports" if l else "one_line_port"):val
                              for (p,l),val in literal[
                                  "source_center_good_port_support_categories"].items()})
            self.assertEqual(z[
                "original_both_typed_opposite_GOOD_threeflag_wedge_count"],
                old["good_D_original_OPPOSITE_TWO_TYPED_port_wedges"])
            self.assertLessEqual(z["true_original_SHARP_fixed_marginals_lower"],
                                 z["original_both_typed_opposite_GOOD_threeflag_wedge_count"])
            self.assertLessEqual(z["true_original_improved_integer_minority_bound"],
                                 z["true_original_SHARP_fixed_marginals_lower"])
            print("AA4AW_GENUINE_W32",name,
                  "minority_product_sum",z["original_sum_two_marginal_minor_products"],
                  "sharp_fixed_marginal_lower",z["true_original_SHARP_fixed_marginals_lower"],
                  "minority_lower",z["true_original_improved_integer_minority_bound"],
                  "actual_opposite_GOOD",z["original_both_typed_opposite_GOOD_threeflag_wedge_count"],
                  "true_original_source_both_one_side_support",
                  z["original_source_port_support_categories"])

    def test_03_true_original_W34_global_K14_both_physical_holes_and_two_single_sided_port_margins(self):
        expected={"lex":(2072,20650,3544),
                  "random":(147,158,10)}
        for name in ("lex","random"):
            model=fixture(2,name)
            z=exact_true_original_good_minority_port_certificate(model)
            independent=independent_literal_original_source_both_port_support_referee(model)
            self.assertEqual((z["original_good_D_pair_count"],
                              z["original_source_AA_good_threeflag_wedge_count"],
                              z["original_both_typed_opposite_GOOD_threeflag_wedge_count"]),expected[name])
            self.assertEqual(z["original_source_port_support_categories"],{
                ("two_point_ports" if p else "one_point_port",
                 "two_line_ports" if l else "one_line_port"):v
                 for (p,l),v in independent[
                    "source_center_good_port_support_categories"].items()})
            self.assertEqual(independent["literal_real_source_OPPOSITE_port_good_wedges"],
                             expected[name][2])
            print("AA4AW_GENUINE_W34",name,
                  "true_source_minority_product_sum",z["original_sum_two_marginal_minor_products"],
                  "marginal_only_sharp_lower",z["true_original_SHARP_fixed_marginals_lower"],
                  "observed_opposite_good",z["original_both_typed_opposite_GOOD_threeflag_wedge_count"],
                  "real_incidence_flag_one_side_support_types",z["original_source_port_support_categories"])

    def test_04_all_h16_to_60_conditional_alpha_beta_s6_sixty(self):
        for h in (1,2,13,14,15,16,17,23,24,30,40,60):
            s=1<<h
            for a,b in ((Fraction(0),Fraction(0)),(Fraction(1,16),Fraction(1,2)),
                        (Fraction(1,8),Fraction(1,3)),(Fraction(1,4),Fraction(1))):
                z=conditional_all_h_minor_ports_to_seven_GF5(s,a,b)
                self.assertTrue(z["hypothesis_H1_all_f_g_one_sided_port_minority_mass_UNPROVED"])
                self.assertTrue(z["hypothesis_H2_all_f_g_six_original_ID_GF5_continuation_UNPROVED"])
                if h>=16:
                    val=a*b*Fraction(s**6,60)
                    self.assertEqual(z["all_h_sufficient_conditional_original_S_GF5_lower_rational"],val)
                    self.assertEqual(z["conditional_integer_minimum_S"],
                                     (val.numerator+val.denominator-1)//val.denominator)
                else:
                    self.assertIsNone(z["conditional_integer_minimum_S"])
        for a,b in ((Fraction(-1,2),Fraction(1,2)),
                    (Fraction(1,2),Fraction(1,2)),
                    (Fraction(1,8),Fraction(3,2))):
            with self.assertRaises(ValueError):
                conditional_all_h_minor_ports_to_seven_GF5(1<<16,a,b)

    def test_05_true_source_symplectic_global_physical_independent_typed_coordinate_permutations(self):
        m=zero_split_original_W32()
        p,l=symplectic_transvection_source(m,1)
        changed=transform_model(
            m,point_sources=p,line_sources=l,
            point_coordinates=tuple(reversed(range(6))),
            line_coordinates=tuple((i+2)%6 for i in range(6)))
        a=exact_true_original_good_minority_port_certificate(m)
        b=exact_true_original_good_minority_port_certificate(changed)
        for field in ("original_good_D_pair_count",
                      "original_source_AA_good_threeflag_wedge_count",
                      "original_both_typed_opposite_GOOD_threeflag_wedge_count",
                      "original_sum_two_marginal_minor_products",
                      "true_original_improved_integer_minority_bound",
                      "true_original_SHARP_fixed_marginals_lower",
                      "original_source_port_support_categories"):
            self.assertEqual(a[field],b[field])

    def test_06_independent_actual_original_Hall_GF5_NO_LIFT_and_forged_physical_sources(self):
        from hyp105_issue230_d6aa4as_threeflag_hall_frontier import (
            original_opposite_wedge_context)
        from hyp105_issue230_d6aa4ar_good_wedges_port_balance import (
            exact_true_W32_original_seven_covered_good_wedges)
        # True S68/S72 have MANY real opposite two-type good original
        # threeflag wedges but minuscule selected seven-Q original coverage.
        for scheme in ("S68","S72"):
            model=fixture(1,scheme)
            source=exact_true_original_good_minority_port_certificate(model)
            selected=exact_true_W32_original_seven_covered_good_wedges(model)
            self.assertGreater(source["original_both_typed_opposite_GOOD_threeflag_wedge_count"],0)
            self.assertGreater(source["true_original_improved_integer_minority_bound"],0)
            self.assertLessEqual(
                selected["distinct_good_wedges_covered_by_some_true_original_seven_Q"],
                source["original_both_typed_opposite_GOOD_threeflag_wedge_count"])
            self.assertEqual(selected["distinct_good_wedges_covered_by_some_true_original_seven_Q"],
                             6 if scheme=="S68" else 11)
        m=zero_split_original_W32()
        for corrupted in (dict(m,left_labels=((0,1),)*15),
                          dict(m,right_labels=((0,1),)*15),
                          dict(m,incidences=m["incidences"][:-1])):
            with self.assertRaises((ValueError,AssertionError)):
                exact_true_original_good_minority_port_certificate(corrupted)


if __name__=="__main__":
    unittest.main()
