"""AA4-AL genuine global ORIGINAL incidence × two physical maps certificate."""
import unittest
from fractions import Fraction
from itertools import combinations
from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    all_h_global_original_transport_theorem,
    exact_original_global_transport,independent_original_flag_pair_oracle,
    independent_true_original_incidence_spectrum_certificate)
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32)
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model)


class GlobalOriginalTransportTest(unittest.TestCase):
    def test_01_exact_all_h_symbolic_coefficient_and_spectral_local_no_go(self):
        for h in (1,2,3,4,5,6,8,12,19,22,26,50):
            s=1<<h
            z=all_h_global_original_transport_theorem(s)
            V=(s+1)*(s*s+1);d=s+1;a=z["a"]
            self.assertEqual(z["V"],V)
            self.assertEqual(z["physical_palette_size"]-z["global_edge_image_missing"],V)
            self.assertEqual(sum(z["incidence_singular_values_squared_multiplicity"].values()),V)
            self.assertEqual(
                z["uniform_ordered_DISTINCT_source_point_line_flag_pair_lower"],
                Fraction(16*V*V*d*d,a*a)-4*V*d*d)
            self.assertGreaterEqual(
                z["uniform_ordered_DISTINCT_source_point_line_flag_pair_lower"],
                2*V*d*d)
            self.assertGreaterEqual(z["simple_explicit_ordered_good_pair_lower"],2*s**5)
            self.assertTrue(z["all_physical_center_cell_spectral_mixing_lower_NONPOSITIVE"])
            self.assertTrue(z["ALL_SIX_original_incidence_GF5_Omega_s6_NOT_PROVED"])

    def test_02_all_five_true_original_W32_globally_injected_maps_pairwise_oracle(self):
        maps=[("dual_zero",zero_split_original_W32())]+[
            (scheme,fixture(1,scheme)) for scheme in ("lex","reverse","S68","S72")]
        exact_counts={"dual_zero":277,"lex":307,"reverse":300,
                      "S68":257,"S72":261}
        for scheme,m in maps:
            z=exact_original_global_transport(m)
            literal=independent_original_flag_pair_oracle(m)
            self.assertEqual(literal,exact_counts[scheme])
            self.assertEqual(z[
                "exact_UNORDERED_DISTINCT_source_flag_pair_bilateral_physical_collision"],literal)
            self.assertGreaterEqual(
                z["exact_ordered_DISTINCT_source_flag_pair_bilateral_physical_collision"],
                z["refined_all_f_g_original_pair_lower"])
            self.assertEqual(
                z["transport_squared_Frobenius_energy"]-
                z["total_four_per_original_flag_transport"]-
                z["ordered_source_same_original_point_subtraction"]-
                z["ordered_source_same_original_line_subtraction"],2*literal)
            self.assertEqual(sum(z["transport_row_marginals"]),4*m["N"])
            self.assertEqual(sum(z["transport_col_marginals"]),4*m["N"])
            self.assertEqual(sum(z["point_physical_fiber_sizes"]),2*m["v"])
            self.assertEqual(sum(z["line_physical_fiber_sizes"]),2*m["v"])
            self.assertGreater(literal,0)
            print("AA4AL_TRUE_ORIGINAL_W32",scheme,
                  "valid_unordered_two_type_pairs",literal,
                  "good_ordered_lower_uniform",str(z["all_f_g_Cauchy_uniform_lower"]),
                  "variance_gain",str(z["physical_fiber_degree_variance_gain"]))

    def test_03_true_original_W34_nonsurjective_K14_lex_random_pairwise_oracle(self):
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            z=exact_original_global_transport(m)
            literal=independent_original_flag_pair_oracle(m)
            self.assertEqual(z["V"],85)
            self.assertEqual(z["a"],14)
            self.assertEqual(z["s"],4)
            self.assertEqual(z[
                "exact_UNORDERED_DISTINCT_source_flag_pair_bilateral_physical_collision"],literal)
            self.assertEqual(literal,{"lex":6529,"random":6327}[scheme])
            self.assertEqual(z["total_four_per_original_flag_transport"],4*425)
            self.assertLessEqual(
                z["ordered_source_same_original_point_subtraction"],2*85*5*4)
            self.assertLessEqual(
                z["ordered_source_same_original_line_subtraction"],2*85*5*4)
            print("AA4AL_TRUE_ORIGINAL_W34",scheme,
                  "valid_unordered_two_type_pairs",literal,
                  "point_fibers",z["point_physical_fiber_sizes"],
                  "line_fibers",z["line_physical_fiber_sizes"])

    def test_04_exact_original_symplectic_BBT_SRG_and_singular_values(self):
        for power,scheme in ((1,"lex"),(1,"S68"),(2,"random")):
            m=fixture(power,scheme)
            z=independent_true_original_incidence_spectrum_certificate(m)
            self.assertEqual(z["all_true_original_BBT_equals_dI_plus_A"],"PASS")
            self.assertEqual(z["all_true_original_A_squared_SRG_mu_lambda"],"PASS")
            self.assertEqual(z["rank_of_original_source_B"]+
                             z["source_nullspace_dimension"],z["V"])
            self.assertTrue(z["spectral_unexpanded_local_cell_lower_NONPOSITIVE"])

    def test_05_independent_source_automorphism_and_typed_physical_coordinate_permutations(self):
        m=zero_split_original_W32()
        original=exact_original_global_transport(m)
        p,l=symplectic_transvection_source(m,1)
        relabeled=transform_model(
            m,point_sources=p,line_sources=l,
            point_coordinates=tuple(reversed(range(6))),
            line_coordinates=tuple((i+2)%6 for i in range(6)))
        changed=exact_original_global_transport(relabeled)
        for key in ("exact_ordered_DISTINCT_source_flag_pair_bilateral_physical_collision",
                    "transport_squared_Frobenius_energy",
                    "ordered_source_same_original_point_subtraction",
                    "ordered_source_same_original_line_subtraction",
                    "physical_fiber_degree_variance_gain",
                    "two_margin_ANOVA_energy_lower"):
            self.assertEqual(original[key],changed[key])

    def test_06_no_fake_source_flags_and_invalid_global_physical_maps(self):
        m=zero_split_original_W32()
        for bad in (dict(m,left_labels=((0,1),)*15),
                    dict(m,right_labels=((0,1),)*15),
                    dict(m,incidences=m["incidences"][:-1]),
                    dict(m,incidences=((99,99),)*45)):
            with self.assertRaises((ValueError,AssertionError)):
                exact_original_global_transport(bad)
        for bad in (0,3,True,-2):
            with self.assertRaises(ValueError):
                all_h_global_original_transport_theorem(bad)

    def test_07_show_all_f_g_tensor_pair_lower_is_not_six_GF5_gate(self):
        # A pair of distinct ORIGINAL flags can share a physical
        # coordinate of each type; it does not supply any six-flag Q.
        # Physical threefold coordinate repetition violates the GF5
        # six-coordinate 2-regular projection. This test never converts
        # a lower on ORIGINAL PAIRS into one on accepted sixsets.
        m=zero_split_original_W32()
        z=exact_original_global_transport(m)
        self.assertTrue(z["positive_seven_GF5_sixset_lower_NOT_PROVED"])
        self.assertEqual(z[
            "exact_UNORDERED_DISTINCT_source_flag_pair_bilateral_physical_collision"],277)
        from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
            full_original_W32_sector_certificate)
        # A STRONG finite blocker against an invalid naive lift:
        # D>0 is universally true, but one concrete FULL global f,g
        # can have ZERO accepted original split-two-triangle B/A AND A/B.
        for side in (0,1):
            z6=full_original_W32_sector_certificate(m,side=side)
            self.assertEqual(z6["original_GF5_A_accepted_by_sector"][
                "split_two_triangles"],0)
            self.assertGreater(z6["full_original_BA_or_AB_accepted"],0)
        from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
            classify_physical_A_twofactor)
        with self.assertRaises(ValueError):
            classify_physical_A_twofactor(
                ((0,1),(0,2),(0,3),(1,4),(2,5),(3,4)),
                ((0,1),(0,2)))


if __name__=="__main__":
    unittest.main()
