"""HYP-105 #230 AA4-AX: strict original source mixed-cell port capacity and method no-go."""
import unittest
from collections import Counter
from fractions import Fraction
from math import comb

from hyp105_issue230_d6aa4ax_original_incidence_cell_port_caps import (
    all_h_spectral_original_port_cap_no_go,
    exact_true_original_incidence_cell_forced_good_ports,
    integer_half_ceiling,
)
from hyp105_issue230_d6aa4ar_good_wedges_port_balance import (
    _good_D_edge_graph,
)
from hyp105_issue230_d6aa4av_global_source_aa_good_wedges import (
    exact_original_corrected_two_type_four_bin_transport,
    universal_original_AA_good_wedge_lower,
)
from hyp105_issue230_d6aa4aw_sharp_original_twoport_marginals import (
    exact_TRUE_original_twoport_marginal_repair_frontier,
)
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32,
)
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model,
)


def independent_actual_true_original_FtBG_cell_literal_source_flags(model):
    """Direct ORIGINAL true point-line source incidence Q-first
    physical mixed cell oracle, independent of new port cap module.
    """
    G,good,nbrs,badP,badL=_good_D_edge_graph(model)
    inc,f,g,a=G["inc"],G["left"],G["right"],G["a"]
    M=[[0]*a for _ in range(a)]
    for p,l in inc:
        c0,c1=f[p]
        e0,e1=g[l]
        M[c0][e0]+=1
        M[c0][e1]+=1
        M[c1][e0]+=1
        M[c1][e1]+=1
    return tuple(tuple(row) for row in M)


def independent_good_physical_port_capacity_oracle(model):
    G,good,neighbors,badP,badL=_good_D_edge_graph(model)
    inc,f,g=G["inc"],G["left"],G["right"]
    M=independent_actual_true_original_FtBG_cell_literal_source_flags(model)
    from hyp105_issue230_d6aa4ap_uniform_good_original_D_spectral import (
        global_good_original_D_spectral_certificate)
    K=int(global_good_original_D_spectral_certificate(G["s"])[
        "original_coordinate_cell_incidence_uniform_upper"])
    charges={"spectral":0,"physical_raw":0,"source_corrected":0}
    seen_fullD=[]
    for i,(p,l) in enumerate(inc):
        point=tuple(sorted(f[p]));line=tuple(sorted(g[l]))
        cells=[[M[c][e] for e in line] for c in point]
        D=len(neighbors[i])
        # Independent REAL source-line and source-point factor
        # exclusion by literal enumeration, NOT previously implemented
        # F^TBG+BG+FB-1 corrected identity.
        allD=[[0,0],[0,0]]
        for j,(q,m) in enumerate(inc):
            if j==i or q==p or m==l:continue
            for u,c in enumerate(point):
                if c not in f[q]:continue
                for v,e in enumerate(line):
                    if e in g[m]:
                        allD[u][v]+=1
        seen_fullD.append(tuple(v for row in allD for v in row))
        limits=[
            (2*K-2,2*K-2,"spectral"),
            (max(sum(row)-2 for row in cells),
             max(cells[0][v]+cells[1][v]-2 for v in range(2)),
             "physical_raw"),
            (max(sum(row) for row in allD),
             max(allD[0][v]+allD[1][v] for v in range(2)),
             "source_corrected"),
        ]
        for up,ul,name in limits:
            mp=max(0,D-up)
            ml=max(0,D-ul)
            charges[name]+=(mp*ml+1)//2
    return charges,tuple(seen_fullD),M


class OriginalTrueSymplecticIncidencePortCellCapacity(unittest.TestCase):
    def test_01_all_dyadic_h1_to80_GQ_spectral_cell_and_ABSTRACT_scalar_no_go(self):
        for h in range(1,81):
            s=1<<h
            z=all_h_spectral_original_port_cap_no_go(s)
            self.assertEqual(z["V"],(s+1)*(s*s+1))
            self.assertEqual(z["d"],s+1)
            self.assertEqual(z["true_original_incidence_flag_vertices"],
                             (s+1)**2*(s*s+1))
            self.assertEqual(z[
                "all_global_true_original_one_typed_port_row_upper"],
                2*z["original_GQ_integer_cell_upper"]-2)
            self.assertGreaterEqual(z["original_GQ_integer_cell_upper"],
                                    2*z["d"]+1)
            self.assertGreaterEqual(
                z["abstract_relaxation_all_D_edges"],
                z["scalar_SOURCE_GOOD_unordered_D_uniform_floor"])
            if h>=16:
                self.assertTrue(z[
                    "for_h16_scalar_GOOD_and_AA_and_cell_CAP_consistent_with_abstract_R_zero"])
                self.assertGreaterEqual(
                    z["abstract_relaxation_source_distinct_wedges_NUMERICAL_proxy"],
                    Fraction(s**6,10))
                self.assertGreaterEqual(
                    z["original_GQ_integer_cell_upper"]-1,4*(s+1))
                self.assertEqual(
                    z["abstract_relaxation_four_bin"],(4*(s+1),0,0,0))
                self.assertTrue(z[
                    "ABSTRACT_not_global_true_original_GQ_source_or_real_global_f_g"])
                self.assertTrue(z[
                    "abstract_relaxation_twoport_opposite_wedges_ZERO"])
                source=universal_original_AA_good_wedge_lower(s)
                self.assertTrue(source["source_AA_all_global_s6_over_10_PROVED"])
            self.assertTrue(z["NO_unconditional_original_twoport_minorities_positive_proved"])
            self.assertTrue(z["root_issue230_original_seven_GF5_s6_OPEN"])
            if h in (1,2,3,14,15,16,17,24,40,80):
                print("AA4AX_ORIGINAL_GQ_SPECTRAL_CELL_SCALAR_NOGO",
                      "h",h,
                      "integer_K",z["original_GQ_integer_cell_upper"],
                      "row_cap",z["all_global_true_original_one_typed_port_row_upper"],
                      "abstract_deg",z["abstract_relaxation_all_center_degree"],
                      "only_RELAXATION",True)

    def test_02_TRUE_original_five_complete_W32_independent_Qfirst_mixed_cell_caps(self):
        for name,m in [("dual_zero",zero_split_original_W32())]+[
            (x,fixture(1,x)) for x in ("lex","reverse","S68","S72")]:
            z=exact_true_original_incidence_cell_forced_good_ports(m)
            check,full_D,M=independent_good_physical_port_capacity_oracle(m)
            t=exact_original_corrected_two_type_four_bin_transport(m)
            self.assertEqual(
                M,t["true_original_full_physical_coordinate_transport"])
            self.assertEqual(
                full_D,t["true_original_centered_flag_D_2by2_point_line_port_tensor"])
            for k in ("spectral","physical_raw","source_corrected"):
                self.assertEqual(
                    check[k],z[{
                      "spectral":"pure_GQ_SPECTRAL_cell_only_forced_opposite_integer_lower",
                      "physical_raw":"TRUE_original_mixed_FtBG_RAW_cell_forced_opposite_integer_lower",
                      "source_corrected":"SOURCE_DEGENERACY_corrected_ALL_D_cell_forced_good_opposite_lower"}[k]])
            original=exact_TRUE_original_twoport_marginal_repair_frontier(m)
            self.assertEqual(
                z["actual_physical_GOOD_D_opposite_twoport_3flag_wedges"],
                original["physically_opposite_ACTUAL_original_GOOD_D_centered_3flag_wedges"])
            self.assertEqual(
                z["full_GOOD_independently_colored_half_minority_opposite_lower"],
                original["universal_half_minority_product_ceiling_sum_lower"])
            self.assertTrue(z["root230_Branch_A_B_C_OPEN"])
            print("AA4AX_TRUE_ORIGINAL_W32",name,
                  "GOOD",z["actual_GOOD_D_original_unordered_source_edges"],
                  "SPECTRAL_CAP_lower",check["spectral"],
                  "RAW_FtBG_CELL_lower",check["physical_raw"],
                  "CORRECTED_ALL_D_CELL_lower",check["source_corrected"],
                  "ACTUAL_GOOD_OPPOSITE",z[
                    "actual_physical_GOOD_D_opposite_twoport_3flag_wedges"])

    def test_03_TRUE_original_W34_K14_nononto_both_typed_image_caps(self):
        for name in ("lex","random"):
            m=fixture(2,name)
            z=exact_true_original_incidence_cell_forced_good_ports(m)
            check,full_D,M=independent_good_physical_port_capacity_oracle(m)
            self.assertEqual(z["N_true_original_incidence_flag_IDs"],425)
            self.assertEqual(z["s"],4)
            self.assertEqual(z[
                "TRUE_original_mixed_FtBG_RAW_cell_forced_opposite_integer_lower"],
                check["physical_raw"])
            self.assertEqual(z[
                "SOURCE_DEGENERACY_corrected_ALL_D_cell_forced_good_opposite_lower"],
                check["source_corrected"])
            self.assertLessEqual(check["spectral"],check["physical_raw"])
            self.assertLessEqual(check["physical_raw"],check["source_corrected"])
            self.assertLessEqual(check["source_corrected"],z[
                "actual_physical_GOOD_D_opposite_twoport_3flag_wedges"])
            print("AA4AX_TRUE_ORIGINAL_W34",name,
                  "GOOD",z["actual_GOOD_D_original_unordered_source_edges"],
                  "SPECTRAL_CAP_lower",check["spectral"],
                  "RAW_FtBG_CELL_lower",check["physical_raw"],
                  "CORRECTED_ALL_D_CELL_lower",check["source_corrected"],
                  "ACTUAL_GOOD_OPPOSITE",z[
                    "actual_physical_GOOD_D_opposite_twoport_3flag_wedges"])

    def test_04_TRUE_original_source_symplectic_isometry_and_TYped_physical_relabelling(self):
        m=zero_split_original_W32()
        p,l=symplectic_transvection_source(m,1)
        alt=transform_model(
            m,point_sources=p,line_sources=l,
            point_coordinates=tuple(reversed(range(6))),
            line_coordinates=tuple((j+2)%6 for j in range(6)))
        a=exact_true_original_incidence_cell_forced_good_ports(m)
        b=exact_true_original_incidence_cell_forced_good_ports(alt)
        for key in (
            "actual_GOOD_D_original_unordered_source_edges",
            "actual_physical_GOOD_D_opposite_twoport_3flag_wedges",
            "TRUE_original_source_AA_GOOD_centered_wedges",
            "pure_GQ_SPECTRAL_cell_only_forced_opposite_integer_lower",
            "TRUE_original_mixed_FtBG_RAW_cell_forced_opposite_integer_lower",
            "SOURCE_DEGENERACY_corrected_ALL_D_cell_forced_good_opposite_lower",
        ):
            self.assertEqual(a[key],b[key])

    def test_05_pure_integer_port_CAP_forcing_abstract_sharp_high_degree_cases(self):
        for D in range(1,21):
            for max_port in range(0,21):
                forced=max(0,D-max_port)
                # Any two row counts summing to D while each <= max_port
                # has both minorities >= forced. Same for line.
                if 2*max_port<D:continue
                possible_rows=[(x,D-x) for x in range(D+1)
                               if x<=max_port and D-x<=max_port]
                self.assertTrue(possible_rows)
                self.assertEqual(
                    min(min(x,y) for x,y in possible_rows),forced)
                for mp in range(0,5):
                    self.assertEqual(integer_half_ceiling(forced*mp),
                                     (forced*mp+1)//2)
        with self.assertRaises(ValueError):
            integer_half_ceiling(-1)
        with self.assertRaises(ValueError):
            integer_half_ceiling(True)

    def test_06_abstract_relaxation_SAME_scalar_source_wedge_moments_NOT_true_GQ(self):
        # Important NEGATIVE scientific control: the abstract table
        # is a relaxation of the prior scalar AP/AV premises, NOT a
        # globally injected original source GQ construction.
        for h in (16,17,20,24,32,40,60):
            z=all_h_spectral_original_port_cap_no_go(1<<h)
            D=z["abstract_relaxation_all_center_degree"]
            x00,x01,x10,x11=z["abstract_relaxation_four_bin"]
            self.assertEqual((x00,x01,x10,x11),(D,0,0,0))
            self.assertEqual(x00*x11+x01*x10,0)
            self.assertGreaterEqual(
                z["abstract_relaxation_all_D_edges"],
                z["scalar_SOURCE_GOOD_unordered_D_uniform_floor"])
            self.assertGreaterEqual(
                z["abstract_relaxation_source_distinct_wedges_NUMERICAL_proxy"],
                Fraction((1<<h)**6,10))
            self.assertLessEqual(D+1,z["original_GQ_integer_cell_upper"])
            self.assertTrue(z[
                "ABSTRACT_not_global_true_original_GQ_source_or_real_global_f_g"])

    def test_08_FROZEN_seven_genuine_original_source_K6_K14_port_CAP_and_nonlift(self):
        # True source incidence Q-first independent literal source
        # cell capacity witnesses; no random per-Q f/g changes.
        exact=(
            ("dual_zero",zero_split_original_W32(),277,0,222,652,870),
            ("lex",fixture(1,"lex"),307,0,211,794,1105),
            ("reverse",fixture(1,"reverse"),300,0,375,784,1013),
            ("S68",fixture(1,"S68"),257,0,159,509,697),
            ("S72",fixture(1,"S72"),261,0,145,545,750),
            ("W34_lex",fixture(2,"lex"),2072,0,0,0,3544),
            ("W34_random",fixture(2,"random"),147,0,0,0,10),
        )
        for name,m,edges,spectral,raw,corrected,actual in exact:
            v=exact_true_original_incidence_cell_forced_good_ports(m)
            observed=(
                v["actual_GOOD_D_original_unordered_source_edges"],
                v["pure_GQ_SPECTRAL_cell_only_forced_opposite_integer_lower"],
                v["TRUE_original_mixed_FtBG_RAW_cell_forced_opposite_integer_lower"],
                v["SOURCE_DEGENERACY_corrected_ALL_D_cell_forced_good_opposite_lower"],
                v["actual_physical_GOOD_D_opposite_twoport_3flag_wedges"])
            self.assertEqual(observed,(edges,spectral,raw,corrected,actual))
            self.assertLessEqual(spectral,raw)
            self.assertLessEqual(raw,corrected)
            self.assertLessEqual(corrected,actual)
            self.assertTrue(v[
                "source_GQ_incidence_transport_forced_partial_GF5_preHall_not_final_selected"])
            self.assertTrue(v["all_global_positive_minority_sum_NOT_PROVED"])
            print("AA4AX_FROZEN_TRUE_ORIGINAL",name,
                  "ACTUAL_GOOD_D",edges,
                  "SPECTRAL_PORT_FLOOR",spectral,
                  "RAW_MIXED_FtBG_PORT_FLOOR",raw,
                  "CORRECTED_SOURCE_ALL_D_PORT_FLOOR",corrected,
                  "ACTUAL_GOOD_OPPOSITE",actual)

    def test_07_strict_invalid_source_global_injection_and_real_GQ(self):
        m=fixture(1,"S68")
        for forged in (
            dict(m,left_labels=((0,1),)*15),
            dict(m,right_labels=((0,1),)*15),
            dict(m,incidences=m["incidences"][:-1]),
        ):
            with self.assertRaises((AssertionError,ValueError)):
                exact_true_original_incidence_cell_forced_good_ports(forged)
        for bad in (0,3,-2,True):
            with self.assertRaises(ValueError):
                all_h_spectral_original_port_cap_no_go(bad)


if __name__=="__main__":
    unittest.main()
