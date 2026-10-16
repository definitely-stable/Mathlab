"""AA4-AV: independent all-global original good AA source triple lower."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_d6aa4av_global_source_aa_good_wedges import (
    universal_original_AA_good_wedge_lower,
    exact_true_original_good_D_source_multiplicity_partition,
    independent_literal_true_original_good_D_source_partition,
    exact_original_corrected_two_type_four_bin_transport)
from hyp105_issue230_d6aa4ar_good_wedges_port_balance import (
    _good_D_edge_graph,exact_true_original_good_D_two_port_wedge_certificate)
from hyp105_issue230_d6aa4aq_colored_original_D_cycle import (
    original_bicolored_D_flag_graph)
from hyp105_issue230_d6aa4au_source_triple_hall_polynomials import (
    all_h_original_threeflag_source_motif_population)
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32)
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model)


class GlobalTrueOriginalAAWedge(unittest.TestCase):
    def test_01_all_h16_and_above_exact_rational_original_source_AA_lower(self):
        for h in list(range(1,29)) + [30,32,40,48,60]:
            s=1<<h
            z=universal_original_AA_good_wedge_lower(s)
            self.assertEqual(z["N_true_original_incidence_flag_vertices"],
                             (s+1)**2*(s*s+1))
            self.assertEqual(z["exact_good_source_collision_upper_coefficient"],2*s)
            self.assertTrue(z[
                "source_BB_original_P4_reservoir_DISJOINT_from_source_D_wedges"])
            self.assertTrue(z["physically_opposite_two_type_port_fraction_NOT_PROVED"])
            self.assertTrue(z["original_GF5_six_Q_s6_NOT_PROVED"])
            if h>=16:
                self.assertTrue(z["source_AA_all_global_s6_over_10_PROVED"])
                self.assertGreaterEqual(
                    z["exact_Cauchy_minus_source_collision_bound"],
                    Fraction(s**6,10))
                self.assertEqual(
                    z["universal_source_AA_good_centered_two_D_edge_wedge_lower"],
                    Fraction(s**6,10))
                self.assertEqual(z["proof_method"],
                    "all_h_ge_24_symbolic_analytic_11_over_100"
                    if h>=24 else "eight_exact_rational_h16_to_h23")
            else:
                self.assertFalse(z["source_AA_all_global_s6_over_10_PROVED"])
                self.assertIsNone(z[
                    "universal_source_AA_good_centered_two_D_edge_wedge_lower"])
                if h==15:
                    self.assertTrue(z["h15_not_certified_from_this_original_good_D_floor"])
                    self.assertLess(z["exact_Cauchy_minus_source_collision_bound"],
                                    Fraction(s**6,10))
            if h in (14,15,16,17,18,23,24,25,32,60):
                E=z["E_GOOD_genuine_original_D_lower"]
                R=z["exact_Cauchy_minus_source_collision_bound"]
                print("AA4AV_ALL_H_SOURCE_AA",h,
                      "good_D_bound_ratio_s5",str(E/Fraction(s**5)),
                      "AA_wedge_bound_ratio_s6",str(R/Fraction(s**6)),
                      "proved",z["source_AA_all_global_s6_over_10_PROVED"])
        for bad in (0,3,-4,True):
            with self.assertRaises(ValueError):
                universal_original_AA_good_wedge_lower(bad)

    def test_02_five_original_W32_global_f_g_source_AA_BA_AB_partition_independent(self):
        good_counts={"dual_zero":277,"lex":307,"reverse":300,
                     "S68":257,"S72":261}
        # Frozen by independent literal TRUE ORIGINAL centered source
        # 3-flag enumeration, not merely AA4-AR global degree identity.
        # Each tuple is (A/A distinct-source, B/A outer point repeat,
        # A/B outer line repeat), with B/B exactly zero.
        original_source_type_counts={
            "dual_zero":(2675,267,261),
            "lex":(3259,331,334),
            "reverse":(3141,316,311),
            "S68":(2268,216,231),
            "S72":(2346,223,242),
        }
        for name,m in [("dual_zero",zero_split_original_W32())]+[
              (name,fixture(1,name))
              for name in ("lex","reverse","S68","S72")]:
            z=exact_true_original_good_D_source_multiplicity_partition(m)
            literal=independent_literal_true_original_good_D_source_partition(m)
            old=exact_true_original_good_D_two_port_wedge_certificate(m)
            self.assertEqual(z["true_original_GOOD_D_edges"],good_counts[name])
            self.assertEqual((z["source_AA_three_distinct_point_and_line_GOOD_D_wedges"],
                              z["source_BA_outer_original_point_collision_GOOD_wedges"],
                              z["source_AB_outer_original_line_collision_GOOD_wedges"]),
                             original_source_type_counts[name])
            self.assertEqual(z["source_all_GOOD_centered_two_D_edge_wedges"],
                             old["good_D_original_TWO_EDGE_unordered_wedges"])
            self.assertEqual((z[
              "source_AA_three_distinct_point_and_line_GOOD_D_wedges"],
              z["source_BA_outer_original_point_collision_GOOD_wedges"],
              z["source_AB_outer_original_line_collision_GOOD_wedges"]),
              tuple(literal["true_original_source_first_literal_GOOD_threeflag_wedge_types"].get(k,0)
                    for k in ("A/A","B/A","A/B")))
            self.assertEqual(
                literal["genuine_original_opposite_two_typed_good_wedges"],
                old["good_D_original_OPPOSITE_TWO_TYPED_port_wedges"])
            self.assertEqual(z["source_BB_good_D_wedges_EXACT"],0)
            self.assertTrue(z[
                "source_AA_three_distinct_point_and_line_GOOD_D_wedges"]>=
                literal["genuine_original_opposite_two_typed_good_wedges"])
            orig=all_h_original_threeflag_source_motif_population(2)
            self.assertEqual(orig["three_DISTINCT_original_source_flag_ID_type_counts"]["B/B"],180)
            print("AA4AV_TRUE_W32",name,"D_GOOD",z["true_original_GOOD_D_edges"],
                  "source_type_wedge_census",literal[
                  "true_original_source_first_literal_GOOD_threeflag_wedge_types"],
                  "opposite_two_typed_port_wedges",literal[
                  "genuine_original_opposite_two_typed_good_wedges"])

    def test_03_real_original_W34_two_global_K14_maps_strict_same_source_partition(self):
        expected={"lex":(20650,1607,1579,3544),
                  "random":(158,38,21,10)}
        for name in ("lex","random"):
            m=fixture(2,name)
            z=exact_true_original_good_D_source_multiplicity_partition(m)
            lit=independent_literal_true_original_good_D_source_partition(m)
            old=exact_true_original_good_D_two_port_wedge_certificate(m)
            for field,key in ((
                "source_AA_three_distinct_point_and_line_GOOD_D_wedges","A/A"),
                ("source_BA_outer_original_point_collision_GOOD_wedges","B/A"),
                ("source_AB_outer_original_line_collision_GOOD_wedges","A/B")):
                self.assertEqual(z[field],
                                 lit["true_original_source_first_literal_GOOD_threeflag_wedge_types"].get(key,0))
            self.assertEqual(z["source_all_GOOD_centered_two_D_edge_wedges"],
                             old["good_D_original_TWO_EDGE_unordered_wedges"])
            self.assertEqual(lit["genuine_original_opposite_two_typed_good_wedges"],
                             old["good_D_original_OPPOSITE_TWO_TYPED_port_wedges"])
            self.assertEqual(z["source_BB_good_D_wedges_EXACT"],0)
            self.assertEqual((z["source_AA_three_distinct_point_and_line_GOOD_D_wedges"],
                              z["source_BA_outer_original_point_collision_GOOD_wedges"],
                              z["source_AB_outer_original_line_collision_GOOD_wedges"],
                              lit["genuine_original_opposite_two_typed_good_wedges"]),
                             expected[name])
            self.assertEqual(z["true_original_GOOD_D_edges"],
                             2072 if name=="lex" else 147)
            print("AA4AV_TRUE_W34",name,
                  "good_source_type_wedges",
                  lit["true_original_source_first_literal_GOOD_threeflag_wedge_types"],
                  "actual_original_opposite_wedges",
                  lit["genuine_original_opposite_two_typed_good_wedges"])

    def test_04_actual_original_corrected_FtBG_four_color_port_tensor_source_first(self):
        for name,m in [("dual_zero",zero_split_original_W32())]+[
                (name,fixture(1,name)) for name in ("lex","reverse","S68","S72")]+[
                ("W34_lex",fixture(2,"lex")),("W34_random",fixture(2,"random"))]:
            t=exact_original_corrected_two_type_four_bin_transport(m)
            G=original_bicolored_D_flag_graph(m)
            self.assertEqual(t["true_original_all_D_edges"],len(G["D_edges"]))
            self.assertEqual(t["N_true_original_incidence_flags"],len(G["inc"]))
            independently_opposite=0
            independently_uncolored=0
            for i,row in enumerate(G["neighbors"]):
                p,l=G["inc"][i]
                pts={c:a for a,c in enumerate(sorted(G["left"][p]))}
                lns={e:b for b,e in enumerate(sorted(G["right"][l]))}
                expected=[0,0,0,0]
                for j,c,e in row:
                    expected[2*pts[c]+lns[e]]+=1
                self.assertEqual(tuple(expected),
                                 t["true_original_centered_flag_D_2by2_point_line_port_tensor"][i])
                independently_opposite+=expected[0]*expected[3]+expected[1]*expected[2]
                independently_uncolored+=len(row)*(len(row)-1)//2
            self.assertEqual(independently_opposite,
                             t["genuine_original_ALL_D_two_typed_physically_opposite_wedges"])
            self.assertEqual(independently_uncolored,
                             t["genuine_original_all_D_centered_uncolored_wedges"])
            self.assertTrue(t["source_original_local_4bin_tensor_M_minus_BG_minus_FB_plus_1_exact"])
            print("AA4AV_ORIGINAL_FtBG_CORRELATION",name,
                  "original_D",len(G["D_edges"]),
                  "source_opposite_physically_two_port",independently_opposite)

    def test_05_actual_original_symplectic_and_independent_typed_physical_invariance(self):
        m=zero_split_original_W32()
        p,l=symplectic_transvection_source(m,1)
        n=transform_model(
            m,point_sources=p,line_sources=l,
            point_coordinates=tuple(reversed(range(6))),
            line_coordinates=tuple((i+2)%6 for i in range(6)))
        z=exact_true_original_good_D_source_multiplicity_partition(m)
        zz=exact_true_original_good_D_source_multiplicity_partition(n)
        for field in (
            "source_AA_three_distinct_point_and_line_GOOD_D_wedges",
            "source_BA_outer_original_point_collision_GOOD_wedges",
            "source_AB_outer_original_line_collision_GOOD_wedges",
            "source_all_GOOD_centered_two_D_edge_wedges"):
            self.assertEqual(z[field],zz[field])
        a=exact_original_corrected_two_type_four_bin_transport(m)
        b=exact_original_corrected_two_type_four_bin_transport(n)
        for field in ("true_original_all_D_edges",
                      "genuine_original_all_D_centered_uncolored_wedges",
                      "genuine_original_ALL_D_two_typed_physically_opposite_wedges"):
            self.assertEqual(a[field],b[field])

    def test_06_critical_no_lift_to_two_physical_ports_or_GF5_and_forged_source(self):
        # An ABSTRACT four-bin example can have many distinct-source
        # neighbor flags all in the SAME typed physical port, producing
        # many source A/A wedges but ZERO opposite two-color wedges.
        # Not claimed to realize a globally labelled W(3,s).
        for degree in (3,10,100):
            aa=degree*(degree-1)//2
            opposite=degree*0+0*0
            self.assertGreater(aa,0)
            self.assertEqual(opposite,0)
        for m in (zero_split_original_W32(),fixture(1,"S68")):
            true=exact_true_original_good_D_source_multiplicity_partition(m)
            self.assertGreater(true["source_AA_three_distinct_point_and_line_GOOD_D_wedges"],0)
            self.assertTrue(true["source_only_AA_not_equivalent_to_physically_two_typed_opposite"])
        m=zero_split_original_W32()
        for corrupted in (dict(m,left_labels=((0,1),)*15),
                          dict(m,right_labels=((0,1),)*15),
                          dict(m,incidences=m["incidences"][:-1])):
            with self.assertRaises((ValueError,AssertionError)):
                exact_true_original_good_D_source_multiplicity_partition(corrupted)
            with self.assertRaises((ValueError,AssertionError)):
                exact_original_corrected_two_type_four_bin_transport(corrupted)


if __name__=="__main__":
    unittest.main()
