"""AA4-AG independent all-h physical and TRUE ORIGINAL GQ Hall falsifiers."""
import unittest
from itertools import combinations
from math import comb
from hyp105_issue230_d6aa4ag_deterministic_triangle_hall import (
    minimal_alphabet,analytic_triangle_hall_barrier,
    occupied_two_triangles,independent_common_neighbors,
    original_triangle_hall_cohort)
from hyp105_issue230_d6aa4af_rootpair_robust_quench import (
    rootpair_robust_all_h,occupied_root_C4_source_factors)
from hyp105_issue230_d6aa4ad_opposite_a_hall_transfer import (
    opposite_physical_A_Hall_transfer)
from hyp105_issue230_projection import fixture

class GQPhysicalTriangleHall(unittest.TestCase):
    def test_01_conservative_all_h_large_exact_integers(self):
        for h in range(19,31):
            s=1<<h
            z=analytic_triangle_hall_barrier(s)
            self.assertTrue(z["all_f_all_g_s14_over_256_PROVED"])
            self.assertGreaterEqual(z["indexed_occupied_pre_Hall_lower"],s**14//256)
            self.assertGreaterEqual(2*z["good_root_line_pairs_lower"],
                                    z["original_root_line_pairs"])
            self.assertTrue(z["original_Hall_positive_s6_lower_NOT_PROVED"])

    def test_02_crosscheck_AF_minimal_alphabet_and_occupied_C4(self):
        for h in (1,2,3,4,8,16,19):
            s=1<<h
            V,a,m=minimal_alphabet(s)
            z=analytic_triangle_hall_barrier(s)
            af=rootpair_robust_all_h(s)
            self.assertEqual((V,a,m),(af["V"],af["a"],
                                      af["missing_physical_edge_images_m"]))
            self.assertEqual(z["point_C4_per_root_lower"],
                             af["universal_per_original_root_physical_occupied_C4_floor"])

    def test_03_all_disjoint_full_K6_K7_edges_literal_vs_neighbors(self):
        for a in (6,7):
            E=tuple(combinations(range(a),2))
            for e0,e1 in combinations(E,2):
                expected=(a-4)*(a-5) if not set(e0)&set(e1) else 0
                self.assertEqual(independent_common_neighbors(E,e0,e1,a),expected)
                self.assertEqual(len(occupied_two_triangles(E,e0,e1,a)),expected)

    def test_04_physical_holes_and_adversarial_pinned_leaf(self):
        for a in (7,8,10):
            full=set(combinations(range(a),2))
            e0,e1=(0,1),(2,3)
            for holes in (((0,4),),((0,4),(2,5)),((0,4),(1,5),(2,6),(3,7))):
                E=full-set(holes)
                self.assertEqual(len(occupied_two_triangles(E,e0,e1,a)),
                                 independent_common_neighbors(E,e0,e1,a))
            # A pinned physical rootpair may have zero completions.
            E=full-{(0,x) for x in range(2,a)}
            self.assertEqual(independent_common_neighbors(E,e0,e1,a),0)

    def test_05_original_W32_three_full_maps_multiple_real_rootpairs(self):
        for scheme in ("lex","S68","S72"):
            model=fixture(1,scheme)
            for side in (0,1):
                for root in (0,4,11):
                    for pair_offset in (0,1,2):
                        z=original_triangle_hall_cohort(
                            model,side=side,root=root,pair_offset=pair_offset,max_C4=3)
                        self.assertEqual(z["physical_C4_total"],3)
                        self.assertEqual(z["indexed_occupied_triangle_candidates"],
                                         3*z["independent_triangle_count"])
                        self.assertEqual(z["accepted_original_GF5_restricted"],
                                         z["original_Hall_positive"]
                                          +z["induced_original_C8_extra"])

    def test_06_exact_original_full_A_completion_dominates_triangle_subset(self):
        model=fixture(1,"lex")
        for side in (0,1):
            labels=model["left_labels" if side==0 else "right_labels"]
            for root in (0,3,11):
                inc=model["incidences"]
                flags=[i for i,e in enumerate(inc) if e[side]==root]
                four=occupied_root_C4_source_factors(model,side=side,root=root)[0]
                small=original_triangle_hall_cohort(
                    model,side=side,root=root,pair_offset=0,max_C4=1)
                big=opposite_physical_A_Hall_transfer(
                    model,B_side=side,root=root,
                    pinned_original_Q=tuple(flags[:2]),four_sources=four)
                self.assertLessEqual(small["accepted_original_GF5_restricted"],
                                     big["accepted_distinct_original_six_Q_through_permanents"])

    def test_07_genuine_original_W34_nononto_physical_holes(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            for side in (0,1):
                z=original_triangle_hall_cohort(
                    model,side=side,root=0,pair_offset=0,max_C4=2)
                self.assertGreaterEqual(z["physical_C4_total"],945)
                self.assertEqual(z["independent_triangle_count"],
                                 z["occupied_two_triangles_per_C4"])
                self.assertEqual(z["accepted_original_GF5_restricted"],
                                 z["indexed_occupied_triangle_candidates"]
                                 -z["original_Hall_failed"]+z["induced_original_C8_extra"])

    def test_08_strict_validation_and_nonclosure(self):
        for bad in (0,1,3,6,-2,True):
            with self.assertRaises(ValueError):minimal_alphabet(bad)
        m=fixture(1,"lex")
        with self.assertRaises(ValueError):original_triangle_hall_cohort(m,side=2)
        with self.assertRaises(ValueError):original_triangle_hall_cohort(m,root=999)
        with self.assertRaises(ValueError):original_triangle_hall_cohort(m,pair_offset=3)
        with self.assertRaises(ValueError):
            occupied_two_triangles(tuple(combinations(range(6),2)),(0,1),(0,1),6)
        self.assertTrue(analytic_triangle_hall_barrier(1<<19)[
            "full_seven_GF5_omega_s6_NOT_PROVED"])

if __name__=="__main__":
    unittest.main()
