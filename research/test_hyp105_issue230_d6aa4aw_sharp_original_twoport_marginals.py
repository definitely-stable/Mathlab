"""HYP-105 #230 AA4-AW: genuinely SHARP 2x2 port margin pre-Hall bound."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_d6aa4aw_sharp_original_twoport_marginals import (
    _validate_port_bins,
    exact_sharp_integer_twoport_marginal_lower,
    all_h_abstract_good_original_port_marginal_gate,
    exact_TRUE_original_twoport_marginal_repair_frontier,
)
from hyp105_issue230_d6aa4ar_good_wedges_port_balance import (
    _good_D_edge_graph,
)
from hyp105_issue230_d6aa4av_global_source_aa_good_wedges import (
    universal_original_AA_good_wedge_lower,
)
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32,
)
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model,
)


def independent_brute_2by2_minimal_given_marginals(r0,r1,c0,c1):
    D=r0+r1
    if c0+c1!=D:
        raise ValueError("invalid marginal")
    values=[]
    for x00 in range(D+1):
        for x01 in range(D+1-x00):
            if x00+x01!=r0:continue
            for x10 in range(D+1-x00-x01):
                x11=D-x00-x01-x10
                if x00+x10!=c0 or x01+x11!=c1:continue
                values.append((x00*x11+x01*x10,(x00,x01,x10,x11)))
    if not values:
        raise AssertionError("no 2x2 matrix with valid point/line original port marginals")
    minimum=min(v for v,_ in values)
    return minimum,tuple(q for v,q in values if v==minimum)


def independent_literal_true_original_GOOD_opposite_center_census(model):
    G,good,nbrs,badP,badL=_good_D_edge_graph(model)
    inc=G["inc"];f=G["left"];g=G["right"]
    all_threeflag_opposite=set()
    both_centers=set()
    per_center=Counter()
    for center,row in enumerate(nbrs):
        p,l=inc[center]
        pports=[0,0];lports=[0,0]
        phys_p=tuple(sorted(f[p]))
        phys_l=tuple(sorted(g[l]))
        for k,cp,cl in row:
            pports[phys_p.index(cp)]+=1
            lports[phys_l.index(cl)]+=1
        if min(pports)>0 and min(lports)>0:
            both_centers.add(center)
        for a,b in combinations(row,2):
            if a[1]==b[1] or a[2]==b[2]:continue
            if (len({inc[j][0] for j in (center,a[0],b[0])})!=3 or
                    len({inc[j][1] for j in (center,a[0],b[0])})!=3):
                raise AssertionError("physical TRUE original opposite threeflag source factor collided")
            triple=(center,)+tuple(sorted((a[0],b[0])))
            if triple in all_threeflag_opposite:
                raise AssertionError("source same real three-ID GOOD wedge counted twice")
            all_threeflag_opposite.add(triple)
            per_center[center]+=1
    if set(per_center)!=both_centers:
        raise AssertionError("original source physical two-port activation iff opposite")
    return len(all_threeflag_opposite),len(both_centers)


class SharpTrueOriginalTwoportMarginals(unittest.TestCase):
    def test_01_exhaustive_abstract_all_integer_port_marginals_D0_to18(self):
        tested=0
        for D in range(19):
            for r0 in range(D+1):
                for c0 in range(D+1):
                    r1=D-r0;c1=D-c0
                    z=exact_sharp_integer_twoport_marginal_lower(
                        r0,r1,c0,c1)
                    v,m=independent_brute_2by2_minimal_given_marginals(
                        r0,r1,c0,c1)
                    self.assertEqual(z[
                        "exact_SHARP_fixed_both_marginals_minimum_opposite_wedges"],v)
                    self.assertEqual(
                        (z["unique_smallest_feasible_x00_argmin"],r0-
                         z["unique_smallest_feasible_x00_argmin"],
                         c0-z["unique_smallest_feasible_x00_argmin"],
                         D-r0-c0+z["unique_smallest_feasible_x00_argmin"]),
                        min(m,key=lambda x:x[0]))
                    self.assertGreaterEqual(v,z[
                        "uniform_half_minorities_CEILING_lower"])
                    self.assertEqual(v>0,
                        z["two_typed_opposite_FORCED_iff_each_typed_port_active"])
                    tested+=1
        self.assertGreater(tested,2300)

    def test_02_sharp_half_product_extremals_and_permutation_invariance(self):
        for half in (1,2,3,8,19):
            q=(half,half,half,half)
            r0=q[0]+q[1];c0=q[0]+q[2]
            z=exact_sharp_integer_twoport_marginal_lower(
                r0,r0,c0,c0)
            self.assertEqual(z[
                "exact_SHARP_fixed_both_marginals_minimum_opposite_wedges"],
                2*half*half)
            self.assertEqual(z[
                "uniform_half_minorities_CEILING_lower"],
                2*half*half)
        for bins in ((8,0,0,0),(0,5,7,0),(1,2,3,4),
                     (0,1,1,0),(15,12,19,3)):
            x00,x01,x10,x11=bins
            r0=x00+x01;r1=x10+x11
            c0=x00+x10;c1=x01+x11
            original=exact_sharp_integer_twoport_marginal_lower(
                r0,r1,c0,c1)
            for flipped in ((r1,r0,c0,c1),(r0,r1,c1,c0),
                            (c0,c1,r0,r1),(r1,r0,c1,c0)):
                transformed=exact_sharp_integer_twoport_marginal_lower(
                    *flipped)
                self.assertEqual(original[
                    "exact_SHARP_fixed_both_marginals_minimum_opposite_wedges"],
                    transformed[
                    "exact_SHARP_fixed_both_marginals_minimum_opposite_wedges"])

    def test_03_true_original_five_global_W32_ALL_centers_independent_brute(self):
        for name,m in [("dual_zero",zero_split_original_W32())]+[
            (x,fixture(1,x)) for x in ("lex","reverse","S68","S72")]:
            z=exact_TRUE_original_twoport_marginal_repair_frontier(m)
            q,c=independent_literal_true_original_GOOD_opposite_center_census(m)
            self.assertEqual(
                z["physically_opposite_ACTUAL_original_GOOD_D_centered_3flag_wedges"],q)
            self.assertEqual(
                z["number_of_both_physical_ports_active_TRUE_source_centers"],c)
            self.assertGreaterEqual(
                z["exact_only_port_marginal_sharp_lower"],
                z["universal_half_minority_product_ceiling_sum_lower"])
            self.assertEqual(
                z["physically_opposite_ACTUAL_original_GOOD_D_centered_3flag_wedges"],
                z["exact_only_port_marginal_sharp_lower"]+
                z["true_original_centered_marginal_lower_slack"])
            print("AA4AW TRUE ORIGINAL W32",name,
                "GOOD_E",z["actual_original_GOOD_D_edges"],
                "AA_good",z["parent_real_source_AA_good_wedges"],
                "real_opposite",q,
                "marginal_sharp_floor",z["exact_only_port_marginal_sharp_lower"],
                "minority_floor",z["universal_half_minority_product_ceiling_sum_lower"],
                "both_typed_ports_active_original_centers",c)

    def test_08_FROZEN_independent_original_W32_W34_marginal_lift_gap_ledger(self):
        # Values independently obtained from the TRUE source literal
        # Q-first original GOOD threeflag port oracle, not inferred by
        # fitting any all-h source/GQ result or resampling f/g per Q.
        expected=[
            ("dual_zero",zero_split_original_W32(),277,2675,870,821,652,45),
            ("lex",fixture(1,"lex"),307,3259,1105,1000,794,45),
            ("reverse",fixture(1,"reverse"),300,3141,1013,968,784,45),
            ("S68",fixture(1,"S68"),257,2268,697,683,509,45),
            ("S72",fixture(1,"S72"),261,2346,750,714,545,45),
            ("W34_lex",fixture(2,"lex"),2072,20650,3544,3174,2183,118),
            ("W34_random",fixture(2,"random"),147,158,10,8,6,6),
        ]
        for name,m,edges,aa,opposite,sharp,minority,active in expected:
            z=exact_TRUE_original_twoport_marginal_repair_frontier(m)
            observed=(
                z["actual_original_GOOD_D_edges"],
                z["parent_real_source_AA_good_wedges"],
                z["physically_opposite_ACTUAL_original_GOOD_D_centered_3flag_wedges"],
                z["exact_only_port_marginal_sharp_lower"],
                z["universal_half_minority_product_ceiling_sum_lower"],
                z["number_of_both_physical_ports_active_TRUE_source_centers"])
            self.assertEqual(observed,(edges,aa,opposite,sharp,minority,active))
            self.assertEqual(
                z["true_original_centered_marginal_lower_slack"],
                opposite-sharp)
            self.assertLessEqual(opposite,aa)
            print("AA4AW FROZEN ACTUAL TRUE ORIGINAL",name,
                  "AA_GOOD",aa,
                  "OPPOSITE_REAL_3FLAG",opposite,
                  "SHARP_FRECHET_MARGIN_MIN",sharp,
                  "PORT_MINORITIES_HALF",minority,
                  "GOOD_BOTH_TYPED_PORT_CENTERS",active,
                  "ACTUAL_PORT_CORRELATION_SLACK",opposite-sharp)

    def test_04_real_original_W34_both_nonsurjective_K14_line_supports(self):
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            z=exact_TRUE_original_twoport_marginal_repair_frontier(m)
            opposite,active=independent_literal_true_original_GOOD_opposite_center_census(m)
            self.assertEqual(z[
                "physically_opposite_ACTUAL_original_GOOD_D_centered_3flag_wedges"],opposite)
            self.assertEqual(z[
                "number_of_both_physical_ports_active_TRUE_source_centers"],active)
            self.assertEqual(z["s"],4)
            self.assertEqual(z["N_genuine_original_source_incidence_flags"],425)
            self.assertGreaterEqual(z["parent_real_source_AA_good_wedges"],opposite)
            print("AA4AW TRUE ORIGINAL W34",scheme,
                "GOOD",z["actual_original_GOOD_D_edges"],
                "opposite",opposite,"sharp_marginal",z[
                    "exact_only_port_marginal_sharp_lower"])

    def test_05_original_source_automorphism_and_independent_physical_typing_symmetry(self):
        m=zero_split_original_W32()
        p,l=symplectic_transvection_source(m,1)
        changed=transform_model(
            m,point_sources=p,line_sources=l,
            point_coordinates=tuple(reversed(range(6))),
            line_coordinates=tuple((j+2)%6 for j in range(6)))
        x=exact_TRUE_original_twoport_marginal_repair_frontier(m)
        y=exact_TRUE_original_twoport_marginal_repair_frontier(changed)
        for field in (
            "actual_original_GOOD_D_edges",
            "parent_real_source_AA_good_wedges",
            "physically_opposite_ACTUAL_original_GOOD_D_centered_3flag_wedges",
            "exact_only_port_marginal_sharp_lower",
            "universal_half_minority_product_ceiling_sum_lower",
            "number_of_both_physical_ports_active_TRUE_source_centers",
            "true_original_centered_marginal_lower_slack"):
            self.assertEqual(x[field],y[field])

    def test_06_all_h16_to60_source_good_s6_AND_honest_port_GAP(self):
        for h in (*range(1,29),30,40,60):
            s=1<<h
            source=universal_original_AA_good_wedge_lower(s)
            z=all_h_abstract_good_original_port_marginal_gate(s,
                                                          Fraction(s**6,16))
            self.assertEqual(
                z["all_fixed_original_f_g_source_AA_good_wedges_lower"],
                source["universal_source_AA_good_centered_two_D_edge_wedge_lower"])
            self.assertEqual(
                z["conditional_opposite_true_original_GOOD_3flag_lower"],
                Fraction(s**6,32))
            self.assertTrue(z["all_global_minority_product_positive_NOT_PROVED"])
            self.assertTrue(z["original_residual_threeflag_Hall_positive_NOT_PROVED"])
            self.assertTrue(z["selected_original_seven_GF5_sixQ_s6_NOT_PROVED"])
            if h>=16:
                self.assertGreaterEqual(
                    z["all_fixed_original_f_g_source_AA_good_wedges_lower"],
                    Fraction(s**6,10))
        with self.assertRaises(ValueError):
            all_h_abstract_good_original_port_marginal_gate(16,-1)

    def test_07_invalid_noninteger_buckets_and_invalid_true_source_global_models(self):
        for args in ((1,0,1,-1),(2,1,1,1),
                     (True,1,1,1),(-3,3,0,0),(2,2,1,0)):
            with self.assertRaises(ValueError):
                exact_sharp_integer_twoport_marginal_lower(*args)
        for bad in ((1,2,3),(-1,0,0,0),(True,0,0,0)):
            with self.assertRaises(ValueError):
                _validate_port_bins(bad)
        m=fixture(1,"S68")
        for corrupted in (
            dict(m,left_labels=((0,1),)*15),
            dict(m,right_labels=((0,1),)*15),
            dict(m,incidences=m["incidences"][:-1])):
            with self.assertRaises((ValueError,AssertionError)):
                exact_TRUE_original_twoport_marginal_repair_frontier(corrupted)


if __name__=="__main__":unittest.main()
