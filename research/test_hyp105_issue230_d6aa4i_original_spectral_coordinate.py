"""Independent exact ORIGINAL GQ collinearity/incidence spectral physical cuts."""
import random
import unittest
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4i_original_spectral_coordinate import (
    _cross_bound_per_center,all_h_source_disjoint_theorem,geometry,
    one_type_spectral_certificate,original_incidence_coordinate_certificate,
    finite_original_map_certificate)


class OriginalSpectralPhysicalCutsTests(unittest.TestCase):
    def test_001_symbolic_all_h_source_disjoint_omega_s5(self):
        w2=all_h_source_disjoint_theorem(2)
        self.assertEqual((w2["V"],w2["a"],w2["K"],w2["m"]),(15,6,15,0))
        self.assertEqual(w2["original_collinear_unordered_pairs"],45)
        self.assertEqual(w2["uniform_forced_physically_disjoint_collinear_lower"],5)
        w4=all_h_source_disjoint_theorem(4)
        self.assertEqual((w4["V"],w4["a"],w4["K"],w4["m"]),(85,14,91,6))
        self.assertEqual(w4["original_collinear_unordered_pairs"],850)
        self.assertEqual(w4["uniform_forced_physically_disjoint_collinear_lower"],374)
        for h in range(2,12):
            s=2**h
            r=all_h_source_disjoint_theorem(s)
            self.assertGreaterEqual(
                Fraction(r["uniform_forced_physically_disjoint_collinear_lower"]),
                Fraction(s**5,4))
            self.assertTrue(r["explicit_s_ge_4_lower_s_power5_over4"])
            self.assertFalse(r["all_h_original_seven_GF5_bound_PROVED"])
        for s in (0,3,-4):
            with self.assertRaises(ValueError):
                all_h_source_disjoint_theorem(s)

    def test_002_original_W32_SRG_source_incidence_spectrum_both_types(self):
        m=fixture(1,"lex")
        g=geometry(2,m["incidences"])
        self.assertEqual(g["V"],15)
        self.assertEqual(g["genuine_original_lambda"],1)
        self.assertEqual(g["genuine_original_mu"],3)
        self.assertEqual(g["source_collinearity_degree"],6)
        self.assertEqual(g["positive_nontrivial_spectral_eigenvalue"],1)
        self.assertEqual(g["negative_nontrivial_spectral_eigenvalue"],-3)
        self.assertEqual(len(g["original_incidences"]),45)
        self.assertEqual(sum(map(len,g["source_point_neighbors"])),90)
        self.assertEqual(sum(map(len,g["source_line_neighbors"])),90)

    def test_003_invalid_original_incidence_fails_closed(self):
        m=fixture(1,"lex")
        incidences=tuple(m["incidences"])
        with self.assertRaises(ValueError):
            geometry(2,incidences[:-1])
        with self.assertRaises(ValueError):
            geometry(2,incidences[:-1]+(incidences[0],))
        with self.assertRaises(ValueError):
            geometry(2,incidences[:-1]+((15,0),))
        with self.assertRaises(ValueError):
            geometry(8,fixture(3,"lex")["incidences"],max_v=100)

    def test_004_real_original_W32_full_coordinate_and_source_pair_oracles(self):
        for scheme in ("lex","reverse","S68","S72"):
            r=finite_original_map_certificate(1,scheme)
            for kind in ("original_point_spectral_cut","original_line_spectral_cut"):
                z=r[kind]
                self.assertEqual(sum(z["physical_center_degrees"]),30)
                self.assertEqual(z["physical_center_degrees"],(5,)*6)
                self.assertEqual(z["original_collinear_unordered_pair_total"],45)
                self.assertGreaterEqual(z["original_collinear_physically_disjoint"],9)
                self.assertEqual(
                    z["original_collinear_physically_disjoint"]
                    +z["original_collinear_physically_adjacent"],45)
                self.assertEqual(z["exact_per_center_spectral_adjacency_upper"],36)
                self.assertEqual(z["exact_per_center_forced_disjoint_lower"],9)
                self.assertEqual(z["all_h_uniform_forced_disjoint_lower"],5)
            pair=r["original_point_line_bipartite_cut"]
            self.assertLessEqual(
                pair["original_incidence_shared_physical_coordinate_count"],
                pair["two_type_source_physical_spectral_incidence_upper"])
            self.assertEqual(pair["original_incidences_total"],45)

    def test_005_independent_48_random_full_W32_global_typed_injections(self):
        model=fixture(1,"lex")
        g=geometry(2,model["incidences"])
        all_edges=list(combinations(range(g["a"]),2))
        rng=random.Random(2300441)
        for _ in range(48):
            rng.shuffle(all_edges)
            left=all_edges[:]
            rng.shuffle(all_edges)
            right=all_edges[:]
            p=one_type_spectral_certificate(g,left,source_type="P")
            l=one_type_spectral_certificate(g,right,source_type="L")
            cross=original_incidence_coordinate_certificate(g,left,right)
            self.assertGreaterEqual(p["original_collinear_physically_disjoint"],9)
            self.assertGreaterEqual(l["original_collinear_physically_disjoint"],9)
            self.assertLessEqual(cross["original_incidence_shared_physical_coordinate_count"],
                                 cross["two_type_source_physical_spectral_incidence_upper"])

    def test_006_real_W34_both_maps_and_exact_rational_center_bounds(self):
        for scheme in ("lex","random"):
            r=finite_original_map_certificate(2,scheme)
            self.assertEqual(r["s"],4)
            for kind in ("original_point_spectral_cut","original_line_spectral_cut"):
                z=r[kind]
                self.assertGreaterEqual(z["original_collinear_physically_disjoint"],374)
                self.assertLessEqual(z["original_collinear_physically_adjacent"],
                                     z["exact_per_center_spectral_adjacency_upper"])
                self.assertLessEqual(z["exact_per_center_spectral_adjacency_upper"],
                                     z["all_h_uniform_spectral_adjacency_upper"])
                self.assertLessEqual(max(z["physical_center_degrees"]),13)
                self.assertEqual(sum(z["physical_center_degrees"]),170)
            cross=r["original_point_line_bipartite_cut"]
            self.assertEqual(cross["original_incidences_total"],425)
            self.assertLessEqual(cross["original_incidence_shared_physical_coordinate_count"],
                                 cross["two_type_source_physical_spectral_incidence_upper"])

    def test_007_typed_map_and_non_original_geometry_rejection(self):
        model=fixture(1,"lex")
        g=geometry(2,model["incidences"])
        e=tuple(tuple(x) for x in model["left_labels"])
        with self.assertRaises(ValueError):
            one_type_spectral_certificate(g,e[:-1],source_type="P")
        with self.assertRaises(ValueError):
            one_type_spectral_certificate(g,e[:-1]+(e[0],),source_type="P")
        with self.assertRaises(ValueError):
            one_type_spectral_certificate(g,e,source_type="UNKNOWN")
        with self.assertRaises(ValueError):
            one_type_spectral_certificate(g,e[:-1]+((0,0),),source_type="P")
        with self.assertRaises(ValueError):
            original_incidence_coordinate_certificate(g,e,e[:-1])
        self.assertEqual(_cross_bound_per_center(2,15,5,5),11)

    def test_008_spectral_and_original_Q_classes_remain_distinct_claims(self):
        r=finite_original_map_certificate(1,"S68")
        self.assertTrue(r["original_point_spectral_cut"]["not_seven_GF5_motif_lower"])
        self.assertTrue(r["original_point_line_bipartite_cut"]["not_seven_GF5_motif_lower"])
        self.assertEqual(r["all_h_GF5_positive_root"],"OPEN")


if __name__=="__main__":
    unittest.main()
