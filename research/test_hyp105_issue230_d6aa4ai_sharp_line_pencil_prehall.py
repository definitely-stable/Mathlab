"""Independent exact original GQ line-pencil sharper pre-Hall certificate."""
import unittest
from itertools import combinations
from fractions import Fraction
from math import comb,isqrt

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_sharp_line_pencil_prehall import (
    improved_all_h_original_line_pencil_preHall,
    original_true_rootpair_physical_safety_census,
)
from hyp105_issue230_d6aa4ag_deterministic_triangle_hall import (
    analytic_triangle_hall_barrier,
)
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model,
)


class OriginalTrueGQLinePencilImprovedBarrierTests(unittest.TestCase):
    def test_01_exact_new_all_h_s14_256_and_clean_scope(self):
        for h in range(1,40):
            s=1<<h
            x=improved_all_h_original_line_pencil_preHall(s)
            self.assertEqual(x["actual_original_root_two_lines_indexed_N"],
                             x["V"]*comb(s+1,2))
            self.assertEqual(x["hot_physical_coordinate_upper"],
                             (32*x["missing_physical_pair_images"])//x["a"])
            self.assertFalse(x["original_four_rook_Hall_positive_lower_PROVED"])
            self.assertFalse(x["issue230_universal_seven_GF5_lower_PROVED"])
            if s>=16:
                self.assertGreaterEqual(
                    256*x["indexed_original_global_preHall_physical_mass_lower"],
                    s**14)
                self.assertTrue(x["exact_s14_over_256_PROVED_for_all_h_ge4"])
                self.assertLessEqual(4*x["a"]*x["a"],9*s**3)
            else:
                self.assertFalse(x["exact_s14_over_256_PROVED_for_all_h_ge4"])

    def test_02_sharp_all_h_real_line_pencil_improvement_over_AG(self):
        for s in (2,4,8,16,32,64,128,256,1024,1<<19):
            new=improved_all_h_original_line_pencil_preHall(s)
            old=analytic_triangle_hall_barrier(s)
            self.assertEqual(new["s"],old["s"])
            self.assertEqual(new["a"],old["a"])
            self.assertEqual(new["actual_original_root_two_lines_indexed_N"],
                             old["original_root_line_pairs"])
            self.assertEqual(new["adjacent_pinned_physical_pairs_upper"],
                             old["adjacent_edge_pairs"])
            self.assertLessEqual(new["NEW_genuine_GQ_line_pencil_hot_touch_upper"],
                                 old["high_hole_vertices_upper"]*(new["a"]-1)*(new["V"]-1))
            self.assertGreaterEqual(
                new["safe_original_rootpairs_lower"],
                old["good_root_line_pairs_lower"])
            if s>=16:
                self.assertGreaterEqual(
                    new["indexed_original_global_preHall_physical_mass_lower"],
                    old["indexed_occupied_pre_Hall_lower"])
            self.assertTrue(new["AG_previous_first_valid_order"]==1<<19)

    def test_03_frozen_small_order_16_32_64_true_integer_exceptions(self):
        gold={
            16:(94,2,0,594184,402132,0,192052),
            32:(261,105,12,17859600,8787870,3294720,5777010),
            64:(731,510,22,553914400,194508135,66809600,292596665),
        }
        for s,(a,m,hot,N,adj,H,good) in gold.items():
            z=improved_all_h_original_line_pencil_preHall(s)
            self.assertEqual(
                (z["a"],z["missing_physical_pair_images"],
                 z["hot_physical_coordinate_upper"],
                 z["actual_original_root_two_lines_indexed_N"],
                 z["adjacent_pinned_physical_pairs_upper"],
                 z["NEW_genuine_GQ_line_pencil_hot_touch_upper"],
                 z["safe_original_rootpairs_lower"]),
                (a,m,hot,N,adj,H,good))
            self.assertGreater(good,0)
            self.assertGreaterEqual(
                256*z["indexed_original_global_preHall_physical_mass_lower"],
                s**14)
        self.assertEqual(
            improved_all_h_original_line_pencil_preHall(8)[
                "safe_original_rootpairs_lower"],0)

    def test_04_independent_genuine_W34_true_original_line_intersection_degree(self):
        model=fixture(2,"lex")
        true_edges=tuple(model["incidences"])
        V=len(model["left_labels"])
        for side in (0,1):
            opposite={x: set() for x in range(V)}
            for p,l in true_edges:
                opposite[(p,l)[1-side]].add((p,l)[side])
            for line_id in range(V):
                meetings=set()
                for p in opposite[line_id]:
                    for (u,v) in true_edges:
                        if (u,v)[side]==p and (u,v)[1-side]!=line_id:
                            meetings.add((u,v)[1-side])
                self.assertEqual(len(meetings),5*4)
        z=improved_all_h_original_line_pencil_preHall(4)
        self.assertFalse(z["exact_s14_over_256_PROVED_for_all_h_ge4"])

    def test_05_real_W34_lex_and_random_global_point_and_line_labelings(self):
        from hyp105_issue230_d6aa4af_rootpair_robust_quench import (
            independent_physical_C4_cycle_trace)
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            for side in (0,1):
                z=original_true_rootpair_physical_safety_census(
                    m,side=side,probe_good_pairs=4)
                self.assertEqual(z["missing_global_physical_edges"],6)
                c4=z["one_complete_B_global_image_C4_count"]
                source_root=z["one_complete_B_global_image_C4_true_source_root"]
                self.assertGreaterEqual(c4,945)
                self.assertEqual(
                    c4,independent_physical_C4_cycle_trace(
                        m,side=side,root=source_root))
                actual=z["actual_true_original_rootpairs"]
                self.assertEqual(actual["all_true_original_root_line_pairs"],850)
                self.assertEqual(actual["actual_bad_union"]+
                                 actual["genuinely_good_safe_original_rootpairs"],850)
                self.assertLessEqual(
                    actual["physically_adjacent"],
                    improved_all_h_original_line_pencil_preHall(4)[
                        "adjacent_pinned_physical_pairs_upper"])

    def test_06_real_W38_partial_physical_image_and_disjoint_census(self):
        for scheme in ("lex","random"):
            m=fixture(3,scheme)
            for side in (0,1):
                z=original_true_rootpair_physical_safety_census(
                    m,side=side,probe_good_pairs=6,probe_C4_root=False)
                self.assertEqual(z["a"],35)
                self.assertEqual(z["V"],585)
                self.assertEqual(z["missing_global_physical_edges"],10)
                d=z["actual_true_original_rootpairs"]
                self.assertEqual(d["all_true_original_root_line_pairs"],21060)
                self.assertEqual(
                    d["genuinely_good_safe_original_rootpairs"]+
                    d["actual_bad_union"],21060)
                self.assertTrue(z["actual_source_GQ_incidences_and_single_global_typed_maps_used"])
                self.assertFalse(z["all_map_source_Hall_positive_lower_NOT_PROVED"] is False)

    def test_07_true_GQ_source_automorphism_and_both_physical_permutations(self):
        model=fixture(2,"lex")
        ref=original_true_rootpair_physical_safety_census(
            model,side=0,probe_good_pairs=0,probe_C4_root=False)
        point,line=symplectic_transvection_source(model,4)
        a=model["a"]
        altered=transform_model(
            model,point_sources=point,line_sources=line,
            point_coordinates=tuple(reversed(range(a))),
            line_coordinates=tuple((i+5)%a for i in range(a)))
        same=original_true_rootpair_physical_safety_census(
            altered,side=0,probe_good_pairs=0,probe_C4_root=False)
        self.assertEqual(ref["actual_true_original_rootpairs"],
                         same["actual_true_original_rootpairs"])
        self.assertEqual(len(ref["actual_high_missing_degree_physical_coordinates"]),
                         len(same["actual_high_missing_degree_physical_coordinates"]))

    def test_08_invalid_GQ_and_noninjective_or_unsorted_labels_rejected(self):
        m=fixture(2,"lex")
        with self.assertRaises(ValueError):
            original_true_rootpair_physical_safety_census(
                m,side=2)
        with self.assertRaises(ValueError):
            original_true_rootpair_physical_safety_census(
                m,side=0,probe_good_pairs=-1)
        with self.assertRaises(ValueError):
            original_true_rootpair_physical_safety_census(
                m,side=0,probe_good_pairs=41)
        with self.assertRaises(ValueError):
            original_true_rootpair_physical_safety_census(
                dict(m,right_labels=((0,1),)*85),side=0)
        with self.assertRaises(ValueError):
            original_true_rootpair_physical_safety_census(
                dict(m,incidences=tuple(m["incidences"])[:-1]),side=0)
        with self.assertRaises(ValueError):
            improved_all_h_original_line_pencil_preHall(12)


if __name__=="__main__":
    unittest.main()
