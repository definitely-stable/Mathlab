"""AA4-HEAVYADAPT: independent 93313 physical no-clone source supersaturation."""
from fractions import Fraction
from math import comb
import unittest

from hyp105_original_heavy_adaptive_ss6_referee import (
    SCHEMA, ROOT_STATUS, R_OLD, R_NEW, R_ZERO_DELETION, K, PAL,
    RHO_CAP, LAMBDA_MIN, D6_WEIGHT, BBO_PRODUCED_WEIGHT,
    ceil_frac, ceil_sqrt, heavy_density_denominator,
    standalone_quantified_theorem, _actual_original_two_cuts,
    genuine_heavy_witness, canonical_report,
)


class TestOriginalHeavyAdaptiveSS6(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.x=canonical_report()

    def test_true_adaptive_original_CaroWei_graph_density_exact_93313(self):
        lam=Fraction(1,16)-RHO_CAP
        actual=heavy_density_denominator(RHO_CAP)
        self.assertEqual(lam,LAMBDA_MIN)
        self.assertEqual(ceil_frac(actual),R_NEW)
        self.assertEqual(R_NEW,93313)
        self.assertGreater(actual,R_ZERO_DELETION)
        self.assertLess(actual,R_NEW)
        self.assertEqual(heavy_density_denominator(Fraction(0)),
                         R_ZERO_DELETION)
        self.assertEqual(R_ZERO_DELETION,93312)
        self.assertEqual(R_OLD,370944)
        self.assertLess(R_NEW,R_OLD)

    def test_EXACT_CaroWei_original_source_owner_fraction_variable_rho(self):
        for rho in (Fraction(0),Fraction(1,2**32),
                    Fraction(1,512),Fraction(1,256),
                    Fraction(1,32)):
            lam=Fraction(1,16)-rho
            # Et>=s4/8, arbitrary ORIGINAL Z deletes <=2*|Z| edges,
            # each original source owner owns <=2 actual diagonals.
            owners=Fraction(1,16)-rho
            self.assertEqual(lam,owners)
            # e(J)<=5s4/2; original Caro--Wei alpha >=L²/(L+2e)
            independent=owners**2/(owners+5)
            retained=independent/4
            density=retained/18
            self.assertEqual(density,1/heavy_density_denominator(rho))
        self.assertGreater(1/heavy_density_denominator(RHO_CAP),
                           Fraction(1,R_NEW))
        self.assertLess(1/heavy_density_denominator(Fraction(1,32)),
                        Fraction(1,R_NEW))

    def test_uniform_source_rho_star_below_cap_without_assuming_C0_numeric(self):
        universal_upper=(Fraction(119,24)**2 /
                         Fraction(12*(64*comb(195,3))**2*24))
        self.assertLess(universal_upper,RHO_CAP)
        for z in self.x["all_order_formal_external_C0_c0_probes"]:
            self.assertLess(Fraction(z["rho_star"]),universal_upper)
            self.assertLess(Fraction(z["rho_star"]),RHO_CAP)
            self.assertEqual(Fraction(
                z["maximum_all_h_rho_from_palette_and_sixth_moment_MIN_L6"]
            ),universal_upper)
            self.assertEqual(z["R_no_original_Z_exact"],93312)
            self.assertTrue(all(z["all_h_18_quantified_exact_rational_crossbranch_gates"].values()))
            self.assertEqual(len(z["all_h_18_quantified_exact_rational_crossbranch_gates"]),19)

    def test_quantified_formal_graph_C0_c0_original_h0_59_and_60_decrease(self):
        probes=self.x["all_order_formal_external_C0_c0_probes"]
        self.assertEqual([(x["C0_FORMAL"],x["c0_FORMAL"],x["h0"]) for x in probes],
                         [("1","1",751),("2","1/5",781),("7/3","1/17",787)])
        self.assertTrue(all(x["R_ADAPT"]==R_NEW and x["R_OLD"]==R_OLD
                            for x in probes))
        self.assertTrue(all((1<<x["h0"])>=x["s0"]>(1<<(x["h0"]-1))
                            for x in probes))
        self.assertEqual(probes[0]["T"],ceil_frac(Fraction(17*R_NEW**3,2)))
        self.assertGreater(probes[0]["s0"],64)

    def test_new_original_D6_and_R3_sixset_lower_strictly_over_3900fold(self):
        mult=Fraction(R_OLD,R_NEW)**6
        self.assertGreater(mult,3900)
        self.assertLess(mult,4000)
        for z in self.x["all_order_formal_external_C0_c0_probes"]:
            c=Fraction(z["c0_FORMAL"])
            delta=c/Fraction(R_NEW**6)
            self.assertEqual(delta,Fraction(z["delta"]))
            self.assertEqual(delta,Fraction(
                z["new_original_SOURCE_motif_S_s_sextic_floor"]))
            self.assertEqual(Fraction(z["new_signed_GF5_R3_sextic_floor"]),
                             D6_WEIGHT*delta/PAL**6)
            self.assertEqual(Fraction(z["R_heavy_vs_frozen_root_delta_improvement_factor"]),
                             mult)
            self.assertEqual(Fraction(z["BBo_LOW_produced_sextic_at_rho_star"]),
                             Fraction(D6_WEIGHT,BBO_PRODUCED_WEIGHT)*delta)

    def test_genuine_original_heavy_finite_CW_priority_two_REAL_physical_cuts(self):
        cases=self.x["genuine_original_W32_W34_new_independent_heavy_physical_witnesses"]
        self.assertEqual(len(cases),5)
        self.assertEqual([(z["s"],z["scheme"]) for z in cases][:4],
                         [(2,"lex"),(2,"reverse-line"),
                          (4,"lex"),(4,"reverse-line")])
        for z in cases:
            with self.subTest(s=z["s"],scheme=z["scheme"]):
                self.assertTrue(z["diagnostic_heavy_nonvacuous"])
                self.assertGreater(z["original_full_heavy_edges"],0)
                self.assertGreater(z["original_surviving_heavy_edges"],0)
                self.assertGreater(z["surviving_original_heavy_IDs"],0)
                self.assertGreater(z["source_original_conflict_free_independent_flags"],0)
                self.assertGreater(z["after_two_REAL_coordinate_cuts_original_flags"],0)
                self.assertGreater(z["ordinary_NO_CLONE_heavy_F_physical_edges"],0)
                self.assertTrue(z["source_IDs_and_physical_vertices_are_never_cloned"])
                self.assertLessEqual(
                    z["original_full_heavy_edges"]-z["original_surviving_heavy_edges"],
                    2*z["Z"])
                self.assertGreaterEqual(
                    z["source_original_conflict_free_independent_flags"],
                    Fraction(z["source_caroweibound"]))
                self.assertGreaterEqual(
                    4*z["after_two_REAL_coordinate_cuts_original_flags"],
                    z["source_original_conflict_free_independent_flags"])

    def test_independent_true_physical_no_clone_F_exact_densities(self):
        for z in self.x["genuine_original_W32_W34_new_independent_heavy_physical_witnesses"]:
            with self.subTest(s=z["s"],scheme=z["scheme"]):
                density=Fraction(z["actual_NO_CLONE_F_edge_density"])
                guaranteed=Fraction(z["actual_SOURCE_S_over_8a2_density_bound"])
                self.assertEqual(density,Fraction(
                    z["ordinary_NO_CLONE_heavy_F_physical_edges"],
                    z["ordinary_NO_CLONE_heavy_F_physical_vertices"]))
                self.assertGreaterEqual(density,guaranteed)
                self.assertGreater(density,0)
                self.assertEqual(z["physical_original_flag_diagonals_in_selected_graph"],
                                 2*z["after_two_REAL_coordinate_cuts_original_flags"])
                self.assertGreaterEqual(z["source_independent_flags_with_heavy_witness"],
                                        z["after_two_REAL_coordinate_cuts_original_flags"])
                self.assertGreater(z["true_physical_Y_balance_block_count"],0)

    def test_NEW_full_quantified_branch_proof_arithmetic_matches_parent_TEST_ONLY(self):
        # Only the SEPARATE UNIT TEST imports previous proof/ledger.
        from hyp105_branch_a_standalone_source_proof import original_all_order_theorem
        for C,c in ((Fraction(1),Fraction(1)),
                    (Fraction(2),Fraction(1,5)),
                    (Fraction(7,3),Fraction(1,17))):
            old=original_all_order_theorem(C,c)
            new=standalone_quantified_theorem(C,c)
            self.assertLess(new["T"],old["T"])
            self.assertLess(new["s0"],old["s0"])
            self.assertLess(new["h0"],old["h0"])
            for k in ("q2","q3"):
                self.assertEqual(new[k],old[k])
            self.assertEqual(Fraction(new["delta"])/Fraction(old["delta_original_seven_motif_S_s"]),
                             Fraction(R_OLD,R_NEW)**6)
            self.assertGreater(Fraction(new["rho_star"]),Fraction(0))

    def test_invalid_published_numeric_constants_and_rho_fail_closed(self):
        for c0,c in ((1,Fraction(1)),(Fraction(1),1),
                     (Fraction(0),Fraction(1)),
                     (Fraction(1),Fraction(0)),
                     (Fraction(1),Fraction(2)),
                     (Fraction(1,2),Fraction(1))):
            with self.assertRaises(ValueError):
                standalone_quantified_theorem(c0,c)
        for rho in (Fraction(-1),Fraction(1,16),Fraction(1,4),1/16):
            with self.assertRaises(ValueError):
                heavy_density_denominator(rho)
        with self.assertRaises(ValueError):
            ceil_sqrt(-1)
        with self.assertRaises(ValueError):
            ceil_frac(12)

    def test_genuine_original_adversarial_Z_and_fake_source_fails_closed(self):
        with self.assertRaises(ValueError):
            genuine_heavy_witness(3,"lex",(),degree_threshold=1)
        with self.assertRaises(ValueError):
            genuine_heavy_witness(1,"lex",(-1,),degree_threshold=1)
        with self.assertRaises(ValueError):
            genuine_heavy_witness(1,"lex",(45,),degree_threshold=1)
        with self.assertRaises(ValueError):
            genuine_heavy_witness(True,"lex",(),degree_threshold=1)

    def test_finite_diag_T_is_not_misreported_as_asymptotic_theorem_T(self):
        for x in self.x["genuine_original_W32_W34_new_independent_heavy_physical_witnesses"]:
            self.assertEqual(x["diagnostic_T"],1)
        for row in self.x["all_order_formal_external_C0_c0_probes"]:
            self.assertGreater(row["T"],10000)

    def test_root_scientific_status_not_falsely_PROVED_A_by_green_CI(self):
        x=self.x
        self.assertEqual(x["schema"],SCHEMA)
        self.assertEqual(x["root_230_status"],ROOT_STATUS)
        self.assertFalse(x["root_ASET_exponent_proved"])
        self.assertFalse(x["root_Branch_A_formally_peer_review_accepted"])
        self.assertFalse(x["external_graph_SS6_actual_numeric_constants_verified"])
        self.assertTrue(x["all_order_heavy_adaptive_density_theorem_proved_from_named_prior_lemmas"])
        self.assertTrue(x["all_order_new_R_93313_and_delta_improvement_more_than_3900fold"])
        self.assertTrue(x["primary_root_target_is_seven_class_S_s_NOT_R3"])
        self.assertTrue(x["R3_is_the_separate_additive_signed_event_expectation"])
        self.assertTrue(x["prior_root_math_dependency_acceptance_still_outstanding"])


if __name__=="__main__":
    unittest.main()
