"""HYP-105 #230 AA4-AM: genuine original 3rd factorial transport / non-lift."""
import unittest
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32,
)
from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    exact_original_global_transport,
)
from hyp105_issue230_d6aa4am_mixed_triple_transport import (
    falling3,all_h_mixed_triple_transport_theorem,
    exact_mixed_original_triple_transport,
    independent_actual_original_triple_oracle,
    independent_brute_original_flag_triplets,
)
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model,
)


class GenuineOriginalMixedThirdFactorialTests(unittest.TestCase):
    def test_01_all_h_uniform_alpha_and_nonlift_exact_integer(self):
        for h in range(1,61):
            s=1<<h
            z=all_h_mixed_triple_transport_theorem(s)
            V=(s+1)*(s*s+1)
            d=s+1
            self.assertEqual(z["V"],V)
            self.assertLessEqual(5*z["a"]**2,12*V)
            self.assertGreaterEqual(z["exact_transport_entry_mean_mu"],Fraction(5*d,3))
            self.assertGreaterEqual(
                z["ordered_mixed_original_source_triples_uniform_lower"],
                Fraction(64,9)*V*d**3-8*V*d**2)
            self.assertGreaterEqual(
                z["simple_every_complete_global_f_g_mixed_lower"],4*s**6)
            self.assertTrue(z["physical_coord_degree_at_least_three_prevents_2regular_GF5_lift"])
            self.assertTrue(z["all_three_original_points_AND_lines_distinct_NOT_PROVED"])
            self.assertTrue(z["root_issue230_Branch_A_B_C_OPEN"])

    def test_02_true_original_W32_five_complete_global_map_schemes_two_independent_oracles(self):
        cases=[("dual-zero",zero_split_original_W32())]+[
            (name,fixture(1,name)) for name in ("lex","reverse","S68","S72")]
        for name,m in cases:
            e=exact_mixed_original_triple_transport(m)
            cell=independent_actual_original_triple_oracle(m)
            direct=independent_brute_original_flag_triplets(m)
            self.assertEqual(e[
                "exact_UNORDERED_MIXED_true_original_3flag_bilateral_coord_triples"],
                cell["unordered_mixed_actual_original_triples_brute"])
            self.assertEqual(
                cell["unordered_mixed_actual_original_triples_brute"],
                direct["unordered_mixed_actual_original_triples_brute"])
            self.assertEqual(
                cell["observed_finite_ONLY_all_3_points_and_lines_distinct"],
                direct["observed_finite_ONLY_all_3_points_and_lines_distinct"])
            self.assertEqual(e["actual_transport_3rd_factorial_moment_all_original_flags"],
                             cell["all_point_line_physical_coordinate_bicell_ordered_triples"])
            self.assertGreaterEqual(
                e["exact_ordered_MIXED_true_original_3flag_bilateral_coord_triples"],4*15*27)
            print("AA4-AM REAL W32",name,
                  "ordered_mixed",e["exact_ordered_MIXED_true_original_3flag_bilateral_coord_triples"],
                  "unordered_mixed",cell["unordered_mixed_actual_original_triples_brute"],
                  "3point_3line_finite",cell[
                      "observed_finite_ONLY_all_3_points_and_lines_distinct"])

    def test_03_true_original_W34_with_global_physical_holes_independent_cells(self):
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            self.assertEqual((m["a"],len(m["left_labels"])),(14,85))
            e=exact_mixed_original_triple_transport(m)
            independent=independent_actual_original_triple_oracle(m)
            self.assertEqual(
                e["exact_UNORDERED_MIXED_true_original_3flag_bilateral_coord_triples"],
                independent["unordered_mixed_actual_original_triples_brute"])
            self.assertEqual(
                e["actual_transport_3rd_factorial_moment_all_original_flags"],
                independent["all_point_line_physical_coordinate_bicell_ordered_triples"])
            self.assertGreaterEqual(
                e["exact_ordered_MIXED_true_original_3flag_bilateral_coord_triples"],
                4*85*125)
            self.assertTrue(e["NO_direct_GF5_lift_due_to_degree_3_in_BOTH_physical_types"])

    def test_04_true_original_W38_full_global_maps_not_full_K35(self):
        for scheme in ("lex","random"):
            m=fixture(3,scheme)
            self.assertEqual((m["a"],len(m["right_labels"])),(35,585))
            e=exact_mixed_original_triple_transport(m)
            independent=independent_actual_original_triple_oracle(m)
            self.assertEqual(
                e["exact_UNORDERED_MIXED_true_original_3flag_bilateral_coord_triples"],
                independent["unordered_mixed_actual_original_triples_brute"])
            self.assertEqual(
                e["actual_transport_3rd_factorial_moment_all_original_flags"],
                independent["all_point_line_physical_coordinate_bicell_ordered_triples"])
            self.assertGreaterEqual(
                e["exact_ordered_MIXED_true_original_3flag_bilateral_coord_triples"],
                4*585*9**3)

    def test_05_exact_Jensen_tangent_transport_and_independent_pair_frontier(self):
        for power,name in ((1,"lex"),(1,"S68"),(2,"random"),(3,"lex")):
            model=fixture(power,name)
            z=exact_mixed_original_triple_transport(model)
            earlier=exact_original_global_transport(model)
            self.assertEqual(
                z["independent_preexisting_original_two_flag_pair_collision"],
                earlier["exact_ordered_DISTINCT_source_flag_pair_bilateral_physical_collision"])
            self.assertGreaterEqual(z["exact_nonnegative_Jensen_tangent_remainder"],0)
            self.assertEqual(
                Fraction(z["actual_transport_3rd_factorial_moment_all_original_flags"]),
                z["Jensen_3rd_factorial_transport_lower"]+
                z["exact_nonnegative_Jensen_tangent_remainder"])
            self.assertGreaterEqual(
                z["exact_ordered_MIXED_true_original_3flag_bilateral_coord_triples"],
                z["every_global_map_lower_from_symbolic_proof"])
            self.assertEqual(
                z["exact_ordered_MIXED_true_original_3flag_bilateral_coord_triples"],
                6*z["exact_UNORDERED_MIXED_true_original_3flag_bilateral_coord_triples"])

    def test_06_original_source_symplectic_and_separate_physical_permutation_invariance(self):
        m=zero_split_original_W32()
        before=exact_mixed_original_triple_transport(m)
        pt,ln=symplectic_transvection_source(m,1)
        tr=transform_model(
            m,point_sources=pt,line_sources=ln,
            point_coordinates=tuple(reversed(range(m["a"]))),
            line_coordinates=tuple((i+2)%m["a"] for i in range(m["a"])))
        after=exact_mixed_original_triple_transport(tr)
        for key in (
            "actual_transport_3rd_factorial_moment_all_original_flags",
            "exact_source_all_same_point_ordered_3flag_subtraction",
            "exact_source_all_same_line_ordered_3flag_subtraction",
            "exact_ordered_MIXED_true_original_3flag_bilateral_coord_triples",
            "exact_nonnegative_Jensen_tangent_remainder",
        ):
            self.assertEqual(before[key],after[key])

    def test_07_any_degree_two_physical_six_edge_multigraph_forbids_a_triple_star(self):
        # These are physical two-factor shapes (including a repeated B
        # edge and a complementary C4); NOT a statement about arbitrary
        # seven-GF5 tags with unverified physical projection topology.
        two_triangles=[(0,1),(1,2),(0,2),(3,4),(4,5),(3,5)]
        six_cycle=[(0,1),(1,2),(2,3),(3,4),(4,5),(0,5)]
        repeated_B=[(0,1),(0,1),(2,3),(3,4),(4,5),(2,5)]
        for labels in (two_triangles,six_cycle,repeated_B):
            self.assertEqual(
                tuple(sum(x in e for e in labels) for x in range(6)),
                (2,2,2,2,2,2))
            for inds in combinations(range(6),3):
                self.assertFalse(set.intersection(
                    *(set(labels[i]) for i in inds)))
        # A legitimate mixed original triple has degree >=3 in EACH
        # physical coordinate projection; no two-regular six-Q can
        # retain that triple without violating its degree=2 condition.

    def test_08_bad_models_and_non_dyadic_or_impossible_brute_rejected(self):
        m=zero_split_original_W32()
        for bad in (dict(m,left_labels=((0,1),)*15),
                    dict(m,right_labels=((0,1),)*15),
                    dict(m,incidences=tuple(m["incidences"])[:-1])):
            with self.assertRaises(ValueError):
                exact_mixed_original_triple_transport(bad)
        with self.assertRaises(ValueError):
            all_h_mixed_triple_transport_theorem(12)
        with self.assertRaises(ValueError):
            falling3(-1)
        with self.assertRaises(ValueError):
            independent_brute_original_flag_triplets(
                fixture(2,"lex"),max_flags=80)
        with self.assertRaises(ValueError):
            independent_actual_original_triple_oracle(
                m,max_direct_flags=40)


if __name__=="__main__":
    unittest.main()
