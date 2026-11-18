"""Independent all-order GQ SRG + ORIGINAL physical source J frontier tests."""
from fractions import Fraction as F
from math import comb
import unittest

from hyp105_root_srg_frontier_independent import (
    SCHEMA,ROOT_STATUS,R_Z0,K_NEW,H_SOURCE,ALLOC,
    source_numerical_spectral_bound,all_h_spectral_envelope,
    minimal_original_alphabet,ceil_fraction,ceil_sqrt,dyadic_h,
    true_symplectic_geometry,complete_original_maps,
    typed_collinear_overlap,typed_symbol_spectral_energy,
    genuine_original_case,_ceilroot_budget,previous_K11_uniform_original_budget,
    formal_original_root_compare,certificate
)


class TestRootSrgIndependent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cert=certificate()

    def test_01_genuine_symplectic_W32_point_line_SRG_params(self):
        x=true_symplectic_geometry(2)
        self.assertEqual(x["V"],15)
        self.assertEqual(len(x["flags"]),45)
        self.assertEqual(x["multiplicity_plus"],9)
        self.assertEqual(x["multiplicity_minus"],5)
        self.assertTrue(all(len(a)==6 for a in x["point_adj"]))
        self.assertTrue(all(len(a)==6 for a in x["line_adj"]))

    def test_02_genuine_symplectic_W34_dual_SRG_eigenspace_dims(self):
        x=true_symplectic_geometry(4)
        self.assertEqual(x["V"],85)
        self.assertEqual(len(x["flags"]),425)
        self.assertEqual(x["multiplicity_plus"],50)
        self.assertEqual(x["multiplicity_minus"],34)
        self.assertTrue(all(len(a)==20 for a in x["point_adj"]))
        self.assertTrue(all(len(a)==20 for a in x["line_adj"]))

    def test_03_true_original_GQ_off_line_projection_ALL_pairs(self):
        for s in (2,4):
            x=true_symplectic_geometry(s)
            for p in range(x["V"]):
                for l in range(x["V"]):
                    if l not in x["point_flags"][p]:
                        self.assertEqual(len(x["point_adj"][p]&x["line_flags"][l]),1)

    def test_04_true_dual_original_J_census_equals_collinear_pair_overlap(self):
        for x in self.cert["real_original_W32_W34_genuine_symplectic_dual_SRG_censuses"]:
            self.assertEqual(x["true_original_J_edges"],
                x["true_original_point_collinear_overlaps"]+
                x["true_original_line_collinear_overlaps"])
            self.assertTrue(x["actual_true_J_no_more_than_2Cs"])
            self.assertTrue(x["original_point_line_spectral_SRG_identities_passed"])
            self.assertTrue(x["projection_off_each_original_nonincident_point_line_is_unique"])

    def test_05_true_source_spectral_energy_direct_Gram_equals_polynomial(self):
        for x in self.cert["real_original_W32_W34_genuine_symplectic_dual_SRG_censuses"]:
            for k in ("full_original_point_symbol_energy",
                      "full_original_line_symbol_energy"):
                e=x[k]
                self.assertEqual(e["true_original_SRG_G_energy"],
                                 e["true_original_SRG_expected_G_energy"])
                self.assertGreaterEqual(F(e["spectral_instance_adaptive_upper"]),
                                        e["e_col_from_symbol_induced"])
                self.assertLessEqual(F(e["spectral_instance_adaptive_upper"]),
                                     e["universal_original_Cs"])
            self.assertLessEqual(x["true_original_J_edges"],
                  2*x["full_original_point_symbol_energy"]["universal_original_Cs"])

    def test_06_true_original_f_g_are_global_and_minimal_pair_injective(self):
        for s in (2,4):
            x=true_symplectic_geometry(s)
            for mode in ("lex","reverse","shift"):
                a,f,g=complete_original_maps(x["V"],mode)
                self.assertEqual(a,minimal_original_alphabet(x["V"]))
                self.assertEqual(len(set(f)),x["V"])
                self.assertEqual(len(set(g)),x["V"])
                self.assertTrue(all(0<=p<q<a for p,q in f+g))
                self.assertLess(comb(a-1,2),x["V"])
                self.assertGreaterEqual(comb(a,2),x["V"])

    def test_07_reject_invalid_source_labels_before_SRG_claim(self):
        x=true_symplectic_geometry(2)
        a,f,g=complete_original_maps(x["V"],"lex")
        bad=(f[0],f[0])+f[2:]
        with self.assertRaises(ValueError):
            typed_symbol_spectral_energy(x["point_adj"],bad,a,2)
        with self.assertRaises(ValueError):
            typed_collinear_overlap(x["point_adj"],bad)
        with self.assertRaises(ValueError):
            typed_symbol_spectral_energy(x["point_adj"],f,a-1,2)
        with self.assertRaises(ValueError):
            typed_collinear_overlap(x["point_adj"],((0,0),)+f[1:])

    def test_08_exact_minimal_original_alphabet_dyadic_scales(self):
        for s,expected in ((2,6),(4,14),(64,731),(128,2057),
                           (256,5805),(512,16401)):
            x=source_numerical_spectral_bound(s)
            self.assertEqual(x["a"],expected)
            self.assertLess(comb(expected-1,2),x["V"])
            self.assertGreaterEqual(comb(expected,2),x["V"])

    def test_09_all_h_original_J_less_19over8_at_s_ge64(self):
        H=all_h_spectral_envelope(8)
        # This is a symbolic s>=2^8 envelope: its analog at s>=64
        # uses the exact 151/128 * 4097/4096 ceiling.
        M64=F(151,128)*F(4097,4096)
        self.assertLess(M64,F(19,16))
        self.assertLess(2*M64,F(19,8))
        for s in (64,128,256,512,1024):
            x=source_numerical_spectral_bound(s)
            self.assertTrue(x["s_ge64_uniform_19over8_applicable"])
            self.assertLess(F(x["dimensionless_J_ratio_upper"]),F(19,8))

    def test_10_K4_impossible_from_crude64_bound_but_valid_s_ge256(self):
        x=source_numerical_spectral_bound(64)
        y=source_numerical_spectral_bound(128)
        z=source_numerical_spectral_bound(256)
        self.assertLess(F(x["K4_CORE_fraction_after_FULL_Q"]),0)
        self.assertLess(F(y["K4_CORE_fraction_after_FULL_Q"]),0)
        self.assertGreater(F(z["K4_CORE_fraction_after_FULL_Q"]),0)
        H8=all_h_spectral_envelope(8)
        self.assertEqual(H8["M"],F(18284823,16777216))
        self.assertEqual(H8["K4_original_CORE_floor"],F(65257,20971520))
        self.assertLess(H8["M"],F(35,32))
        self.assertLess(2*H8["M"],F(35,16))

    def test_11_all_H_even_spectral_envelope_is_monotonically_stronger(self):
        x=[all_h_spectral_envelope(H) for H in (8,16,32,64)]
        for i in range(1,len(x)):
            self.assertLess(x[i]["M"],x[i-1]["M"])
            self.assertGreater(x[i]["K4_original_CORE_floor"],
                               x[i-1]["K4_original_CORE_floor"])
        for H in (0,7,9,31,33):
            with self.assertRaises(ValueError):
                all_h_spectral_envelope(H)

    def test_12_K4_first_valid_asymptotic_ROOT_source_budget_not_best_h0(self):
        r=_ceilroot_budget(4,8,F(1),F(1))
        self.assertEqual(r["K"],4)
        self.assertEqual(r["exact_root_h0"],823)
        self.assertEqual(F(r["original_CORE_fraction"]),F(65257,20971520))
        self.assertLess(F(r["unchanged_heavy_D6_delta"]),
                        F(r["original_produced_BBo_floor"]))
        with self.assertRaises(ValueError):
            _ceilroot_budget(3,8,F(1),F(1))

    def test_13_new_K10_H32_root_real_scope_and_old_parent_exact_GQ(self):
        r=_ceilroot_budget(10,32,F(1),F(1))
        self.assertEqual(r["H"],32)
        self.assertEqual(r["actual_original_FULL_J_high_source_degree_pruned_gt_K"],11)
        self.assertEqual(r["q2"],1936)
        self.assertEqual(r["q3"],85184)
        self.assertEqual(r["R"],93312)
        self.assertGreater(F(r["original_CORE_fraction"]),F(0))
        self.assertGreater(F(r["all_walk_Blackley_Roy_lower"]),F(0))
        self.assertTrue(r["all_order_inherited_global_LOW_moment_proof_STILL_SEPARATE"])
        self.assertFalse(r["root_PROVED_A"])

    def test_14_exact_formal_c0_c0_previous_and_new_thresholds(self):
        probes=((F(1),F(1),673,667),
                (F(2),F(1,5),703,697),
                (F(7,3),F(1,17),710,704))
        for C0,c0,old_h,new_h in probes:
            old=previous_K11_uniform_original_budget(C0,c0)
            new=_ceilroot_budget(10,32,C0,c0)
            self.assertEqual(old["h0"],old_h)
            self.assertEqual(new["exact_root_h0"],new_h)
            self.assertEqual(formal_original_root_compare(C0,c0)["h0_reduction"],
                             old_h-new_h)
            self.assertGreater(F(new["original_produced_BBo_floor"]),
                               F(new["unchanged_heavy_D6_delta"]))

    def test_15_K10_with_fixed_H32_is_among_formal_optima_not_global_claim(self):
        for q in self.cert["formal_graph_constant_conditional_ROOT_comparison"]:
            self.assertIn(10,q["K_winners_from_4_to_64"])
            self.assertTrue(q["formal_not_published_C6_constants"])
            self.assertFalse(q["root_PROVED_A"])

    def test_16_invalid_external_graph_params_or_source_s_fail_closed(self):
        for C0,c0 in ((F(0),F(1)),(F(1),F(0)),(F(1),F(2)),
                      (1,F(1)),(F(1),0.2)):
            with self.assertRaises(ValueError):
                _ceilroot_budget(10,32,C0,c0)
        for s in (-2,1,3,65,257):
            with self.assertRaises(ValueError):
                source_numerical_spectral_bound(s)
        with self.assertRaises(ValueError):
            minimal_original_alphabet(0)

    def test_17_exact_threshold_carries_all_three_LOW_errors_separately(self):
        for K in (4,7,10,11,64):
            q=_ceilroot_budget(K,32,F(1),F(1))
            s0=int(q["exact_root_s0"])
            self.assertGreaterEqual(s0,2**32)
            self.assertGreaterEqual(s0,int(q["s_coordinate"]))
            self.assertGreaterEqual(s0,int(q["s_endpoint"]))
            self.assertGreaterEqual(s0,int(q["s_four_original_blockers"]))
            self.assertEqual(dyadic_h(s0),q["exact_root_h0"])
            self.assertEqual(q["retained_source_alpha_errors"],
                             ["1/64","1/64","15/16"])
            self.assertEqual(q["L6"],str(24+153*int(q["T"])**2))
            self.assertLessEqual(F(q["unchanged_heavy_D6_delta"]),
                                 F(q["original_produced_BBo_floor"]))

    def test_18_no_fake_graph_external_constants_or_GF5_risk(self):
        c=self.cert
        self.assertTrue(c["external_C6_unknown_numerical_constants"])
        self.assertTrue(c["retained_original_predecessor_heavy_and_LOW_lemmas_REVIEW_OPEN"])
        self.assertEqual(c["first_following_open_proof_gate"],"HEAVY_OWNER_AND_SELECTED_F")
        self.assertEqual(c["source_GQ_SRG_prerequisite_local_status"],
                         "INDEPENDENT_PROOF_CHECKED")
        self.assertFalse(c["root_PROVED_A"])
        self.assertFalse(c["ASET_exponent_claimed"])

    def test_19_cert_genuine_original_cases_and_spectral_ratios(self):
        c=self.cert
        self.assertEqual(c["schema"],SCHEMA)
        self.assertEqual(c["status"],ROOT_STATUS)
        self.assertEqual(c["issue"],230)
        self.assertEqual(c["parent_pr"],773)
        self.assertEqual(len(c["real_original_W32_W34_genuine_symplectic_dual_SRG_censuses"]),6)
        self.assertEqual(len(c["true_dyadic_exact_original_Cs_envelopes"]),5)
        self.assertEqual(len(c["all_h_symbolic_rational_envelope_cases"]),4)
        self.assertEqual(len(c["formal_graph_constant_conditional_ROOT_comparison"]),3)
        self.assertTrue(c["independently_proved_all_h_original_GQ_SRG_source_collision_bound"])
        self.assertTrue(c["all_h_original_J_stronger_19_over_8_for_s_ge64"])
        self.assertTrue(c["all_h_new_K4_original_core_for_dyadic_s_ge256"])
        self.assertEqual(c["K4_uniform_core_floor_dyadic_256"],
                         "65257/20971520")


if __name__=="__main__":
    unittest.main()
