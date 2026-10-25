"""Independent actual original rootpair robust B/A first-gate and mean."""
import unittest
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4af_rootpair_robust_quench import (
    rootpair_robust_all_h,occupied_root_C4_source_factors,
    independent_physical_C4_cycle_trace,
    genuine_W34_rootpair_local_certificate,
)
from hyp105_g5e2b3e1b1a_one_sided import uniform_right_completion_BA
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    symplectic_transvection_source,transform_model,
)


class OriginalRootpairQuenchedBAGuarantees(unittest.TestCase):
    def test_01_explicit_all_h_root_flagpair_lower_for_all_powers(self):
        for h in range(1,19):
            s=1<<h
            z=rootpair_robust_all_h(s)
            self.assertGreaterEqual(z["all_full_physical_C4_patterns_per_fixed_pair_root"],
                                    z["universal_per_original_root_physical_occupied_C4_floor"])
            self.assertEqual(
                z["all_full_physical_C4_patterns_per_fixed_pair_root"],
                3*comb(z["a"]-2,4))
            self.assertEqual(z["missing_physical_edge_images_m"],
                             z["K"]-z["V"])
            if s>=8:
                local=Fraction(z["per_rootpair_eligible_opposite_A_mean_lower"])
                global_mean=Fraction(z["aggregate_over_actual_GQ_roots_and_flags_mean_lower"])
                self.assertGreaterEqual(local,Fraction(s,128))
                self.assertGreaterEqual(global_mean,Fraction(s**6,256))
                self.assertTrue(z["per_rootpair_lower_ge_s_over_128_for_s_ge8"])
                self.assertTrue(z["aggregate_lower_ge_s6_over_256_for_s_ge8"])
            self.assertTrue(z["forall_f_forall_g_minimax_lower_NOT_PROVED"])

    def test_02_exact_uniform_GLOBALLY_injected_six_factor_A_probability(self):
        for s in (2,4,8,16,64):
            z=rootpair_robust_all_h(s)
            x=uniform_right_completion_BA(s)
            self.assertEqual(
                Fraction(z["exact_uniform_COMPLETE_global_opposite_A_probability"]),
                x["right_2factor_probability"])
            self.assertTrue(z["prior_all_h_global_one_sided_conditional_mean_ALREADY_KNOWN"])
            self.assertLessEqual(
                Fraction(z["aggregate_over_actual_GQ_roots_and_flags_mean_lower"]),
                x["expected_U_Bleft_Aright_upper"])

    def test_03_full_K6_exact_every_root_physical_C4_and_independent_walk(self):
        for scheme in ("S68","S72","lex","reverse"):
            model=fixture(1,scheme)
            for side in (0,1):
                for root in range(15):
                    x=occupied_root_C4_source_factors(model,side=side,root=root)
                    self.assertEqual(len(x),3)
                    self.assertEqual(
                        independent_physical_C4_cycle_trace(model,side=side,root=root),
                        3)
                    self.assertEqual(len(set(x)),3)

    def test_04_true_ORIGINAL_W34_nononto_full_global_lex_each_typed_side(self):
        m=fixture(2,"lex")
        p=rootpair_robust_all_h(4)
        self.assertEqual((p["a"],p["K"]-p["V"]),(14,6))
        self.assertEqual(p["universal_per_original_root_physical_occupied_C4_floor"],945)
        self.assertEqual(p["GQ_original_per_realized_C4_source_rook_floor"],106)
        for side,root in ((0,0),(1,0),(0,17),(1,17)):
            z=genuine_W34_rootpair_local_certificate(
                m,side=side,root=root,pinned_offset=0,check_first_C4=8)
            self.assertEqual(z["physical_C4_occupied"],
                             z["independent_physical_C4_adj_trace"])
            self.assertGreaterEqual(z["physical_C4_occupied"],945)
            self.assertEqual(len(z["actual_original_four_rook_direct_counts_sample"]),8)
            self.assertGreaterEqual(
                min(z["actual_original_four_rook_direct_counts_sample"]),106)

    def test_05_true_ORIGINAL_W34_global_random_maps_no_fake_Ka_bijection(self):
        m=fixture(2,"random")
        for side in (0,1):
            for root in (0,1,8):
                z=genuine_W34_rootpair_local_certificate(
                    m,side=side,root=root,pinned_offset=3,check_first_C4=4)
                self.assertGreaterEqual(z["physical_C4_occupied"],945)
                self.assertGreaterEqual(
                    min(z["actual_original_four_rook_direct_counts_sample"]),106)
                self.assertTrue(z["all_h_every_global_g_lower_NOT_PROVED"])

    def test_06_genuine_source_symplectic_and_physical_relabel_invariance(self):
        m=fixture(2,"lex")
        a=m["a"]
        original=genuine_W34_rootpair_local_certificate(
            m,side=0,root=0,check_first_C4=2)
        p,l=symplectic_transvection_source(m,1)
        changed=transform_model(
            m,point_sources=p,line_sources=l,
            point_coordinates=tuple(reversed(range(a))),
            line_coordinates=tuple((x+3)%a for x in range(a)))
        alt=genuine_W34_rootpair_local_certificate(
            changed,side=0,root=p[0],check_first_C4=2)
        self.assertEqual(original["physical_C4_occupied"],alt["physical_C4_occupied"])
        self.assertEqual(original["all_h_universal_C4_floor"],alt["all_h_universal_C4_floor"])

    def test_07_all_h_true_B_source_lift_from_girth8_no_pseudoforests(self):
        for s in (4,8,16,32):
            z=rootpair_robust_all_h(s)
            actual_root_pairs=z["V"]*comb(s+1,2)
            self.assertGreater(
                z["per_fixed_original_root_two_actual_flags_SOURCE_BA_floor"],0)
            self.assertEqual(
                Fraction(z["per_rootpair_eligible_opposite_A_mean_lower"])*actual_root_pairs,
                Fraction(z["aggregate_over_actual_GQ_roots_and_flags_mean_lower"]))

    def test_08_bad_actual_original_map_and_root_pair_rejected(self):
        m=fixture(2,"lex")
        with self.assertRaises(ValueError):
            occupied_root_C4_source_factors(m,side=0,root=85)
        with self.assertRaises(ValueError):
            occupied_root_C4_source_factors(m,side=2,root=0)
        with self.assertRaises(ValueError):
            genuine_W34_rootpair_local_certificate(
                m,side=0,root=0,pinned_offset=99)
        with self.assertRaises(ValueError):
            genuine_W34_rootpair_local_certificate(
                m,side=0,root=0,check_first_C4=0)
        with self.assertRaises(ValueError):
            genuine_W34_rootpair_local_certificate(
                dict(m,left_labels=((0,1),)*85),side=0,root=0)
        with self.assertRaises(ValueError):
            genuine_W34_rootpair_local_certificate(
                dict(m,incidences=tuple(m["incidences"])[:-1]),side=0,root=0)


if __name__=="__main__":
    unittest.main()
