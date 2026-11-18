"""Independent combined #776 alphabet + #777 top-r ORIGINAL GQ falsifiers."""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import unittest
from hyp105_original_heavy_low_alphabet_synthesis import (
    SCHEMA,STATUS,H_FIXED,K_FIXED,R_PARENT_777,R_SIBLING_776,R_PARENT_775,
    ceilq,ceilsqrt,hceil,min_alphabet,envelope,actual_alphabet_envelope,
    root_budget,combined_formal_scenario,original_symplectic_fixture,
    finite_dual_referee,certificate,
)


class TestAA4HeavyLowSynergy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=certificate()

    def test_01_exact_H32_physical_and_source_envelopes_and_R(self):
        z=envelope(32)
        self.assertGreater(z["M"],1)
        self.assertLess(z["M"],F(10001,10000))
        self.assertGreater(z["A"],2)
        self.assertLess(z["A"],F(20001,10000))
        self.assertLess(F(33280),256*z["A"]*(1+64*z["M"]))
        self.assertLess(256*z["A"]*(1+64*z["M"]),F(33281))
        self.assertEqual(z["R"],33281)
        self.assertEqual(z["R_top_r_parent_777"],37441)
        self.assertEqual(z["R_chunk_sibling_776"],66562)
        self.assertEqual(2*z["R"],z["R_chunk_sibling_776"])
        self.assertEqual(R_PARENT_775,93312)

    def test_02_h32_ceil_is_integer_optimum_within_this_exact_envelope(self):
        z=envelope(32)
        raw=256*z["A"]*(1+64*z["M"])
        self.assertEqual(ceilq(raw),33281)
        self.assertFalse(F(33280)>=raw)
        self.assertTrue(F(33281)>raw)
        self.assertEqual(z["exact_unrounded_density"],1/raw)

    def test_03_all_even_H_8_to_40_source_and_physical_are_compatible(self):
        previous_R=None
        for H in range(8,42,2):
            z=envelope(H)
            self.assertLess(z["A"],F(9,4))
            self.assertLess(z["M"],F(35,32))
            self.assertLess(z["R"],z["R_top_r_parent_777"])
            self.assertEqual(z["R_chunk_sibling_776"],
                             ceilq(2*(256*z["A"]*(1+64*z["M"]))))
            self.assertGreater(z["source_positive_CORE_K4"],0)
            if previous_R is not None:
                self.assertLessEqual(z["R"],previous_R)
            previous_R=z["R"]
        self.assertEqual(envelope(30)["R"],33282)
        self.assertEqual(envelope(32)["R"],33281)
        self.assertEqual(envelope(40)["R"],33281)

    def test_04_actual_MINIMAL_pair_alphabet_exact_large_dyadic_s(self):
        for s in (2**32,2**34,2**40):
            p=actual_alphabet_envelope(s,32)
            V=int(p["V"])
            a=int(p["a"])
            self.assertLess(comb(a-1,2),V)
            self.assertGreaterEqual(comb(a,2),V)
            self.assertLess(F(p["actual_a2_over_s3"]),F(p["certified_A_H"]))
            self.assertLess(F(p["actual_original_source_Cs_over_s4"]),F(p["certified_M_H"]))

    def test_05_original_true_W32_W34_two_disjoint_physical_diagonals(self):
        for s in (2,4):
            for mode in ("lex","reverse","shift"):
                m=original_symplectic_fixture(s,mode)
                V=(s+1)*(s*s+1)
                self.assertEqual(len(m["flags"]),(s+1)*V)
                self.assertEqual(len(m["physical"]),2*len(m["flags"]))
                self.assertEqual(sum(m["degree"].values()),4*len(m["flags"]))
                self.assertEqual(len(set(m["f"])),V)
                self.assertEqual(len(set(m["g"])),V)
                for i,diags in m["per"].items():
                    self.assertEqual(len(diags),2)
                    self.assertFalse(set(diags[0])&set(diags[1]))
                    self.assertEqual(m["physical"][diags[0]],i)
                    self.assertEqual(m["physical"][diags[1]],i)

    def test_06_source_J_and_original_genuine_full_physical_graph_same_instance(self):
        for row in self.c["TRUE_original_W32_W34_finite_same_H_heavy_low_Q_cases"]:
            self.assertEqual(row["original_source_N"],
                             (row["s"]+1)**2*(row["s"]**2+1))
            self.assertEqual(row["full_genuine_original_physical_edges"],
                             2*row["original_source_N"])
            self.assertGreaterEqual(row["full_original_J_conflicts"],0)
            self.assertTrue(row["heavy_source_unchanged_all_alphabet_labels"])
            self.assertTrue(row["LOW_true_Blackley_Roy_exact_verified"])

    def test_07_separate_frozen_full_Q_with_matching_REAL_heavy_and_LOW_CORE(self):
        for row in self.c["TRUE_original_W32_W34_finite_same_H_heavy_low_Q_cases"]:
            self.assertEqual(row["LOW_original_paired_physical_edges"],
                             2*row["LOW_original_named_core_flags"])
            self.assertGreaterEqual(row["LOW_true_physical_W3"],0)
            H=row["HEAVY_real_no_clone_top_r"]
            if H is None:
                continue
            self.assertGreater(H["selected_original_F_real_edges"],0)
            self.assertGreater(H["selected_original_F_real_vertices"],0)
            self.assertTrue(H["actual_F_edges_only_from_original_owners"])
            self.assertTrue(H["all_selected_source_J_independent"])
            self.assertGreaterEqual(H["selected_source_independent_count"],
                                    F(H["original_CaroWei_lower"]))
            self.assertGreaterEqual(2*H["after_x_cut"],
                                    H["selected_source_independent_count"])
            self.assertGreaterEqual(2*H["after_both_cuts"],H["after_x_cut"])
            self.assertEqual(H["original_selected_paired_edges"],
                             2*H["after_both_cuts"])
            self.assertGreaterEqual(2*H["actual_heavy_witness_bit_majority"],
                                    H["after_both_cuts"])
            self.assertGreaterEqual(F(H["physical_actual_F_density"]),
                                    F(H["physical_no_clone_F_topr_bound"]))
            self.assertEqual(H["physically_checked_actual_C6_original_source_inverse"]
                             ["actual_ordinary_simple_unoriented_C6"],
                             H["physically_checked_actual_C6_original_source_inverse"]
                             ["distinct_TRUE_original_D6_sixsets"])

    def test_08_nonvacuous_TRUE_original_W34_F_C6_in_combined_reconstruction(self):
        cases=[q for q in self.c["TRUE_original_W32_W34_finite_same_H_heavy_low_Q_cases"]
               if q["HEAVY_real_no_clone_top_r"] is not None and
               q["HEAVY_real_no_clone_top_r"]
                ["physically_checked_actual_C6_original_source_inverse"]
                ["actual_ordinary_simple_unoriented_C6"]>0]
        self.assertGreater(len(cases),0)
        self.assertTrue(any(q["s"]==4 and q["mode"]=="reverse" for q in cases))
        for q in cases:
            c=q["HEAVY_real_no_clone_top_r"]["physically_checked_actual_C6_original_source_inverse"]
            self.assertGreater(c["actual_ordinary_simple_unoriented_C6"],0)
            self.assertTrue(c["no_original_sixset_cloning_or_twelve_fold_loss"])

    def test_09_true_original_full_Q_changes_actual_CORE_and_w3_not_fake_empty(self):
        cases=[q for q in self.c["TRUE_original_W32_W34_finite_same_H_heavy_low_Q_cases"]
               if 0<q["LOW_original_named_core_flags"]<q["original_source_N"]
               and q["full_physical_Q_real_vertices"]>0]
        self.assertTrue(cases)
        self.assertTrue(any(q["s"]==4 for q in cases))
        self.assertTrue(any(q["LOW_true_physical_W3"]>0 for q in cases))

    def test_10_exact_Blackley_Roy_on_original_full_and_empty_CORE(self):
        for s in (2,4):
            for mode in ("lex","reverse"):
                q0=finite_dual_referee(s,mode,0)
                qinf=finite_dual_referee(s,mode,10**6)
                self.assertEqual(q0["LOW_original_named_core_flags"],0)
                self.assertEqual(q0["LOW_true_physical_W3"],0)
                self.assertGreater(qinf["LOW_original_named_core_flags"],0)
                self.assertTrue(qinf["LOW_true_Blackley_Roy_exact_verified"])
                self.assertEqual(qinf["full_physical_Q_real_vertices"],0)

    def test_11_exact_walk_floor_increase_81_over_16A2(self):
        z=envelope(32)
        C=F(7,8)-4*z["M"]/11
        old=F(16,81)*(4*C)**3
        new=(4*C)**3/z["A"]**2
        self.assertEqual(new/old,F(81,16)/z["A"]**2)
        self.assertGreater(new/old,F(126,100))
        self.assertLess(new/old,F(127,100))

    def test_12_three_parent_sibling_and_combined_formal_c0_scenarios(self):
        cases=((F(1),F(1),667,650,628,620),
               (F(2),F(1,5),697,680,658,650),
               (F(7,3),F(1,17),704,687,664,657))
        for C0,c0,p775,p776,p777,pnew in cases:
            q=combined_formal_scenario(C0,c0)
            self.assertEqual(q["baseline_pr775_h0"],p775)
            self.assertEqual(q["sibling_pr776_h0"],p776)
            self.assertEqual(q["parent_pr777_h0"],p777)
            self.assertEqual(q["combined_h0"],pnew)
            self.assertLess(pnew,min(p776,p777))
            self.assertTrue(q["actual_original_sixset_and_moments_STILL_PROOF_GATES"])

    def test_13_HEAVY_sextic_gain_against_BOTH_last_sibling_PRs(self):
        q=combined_formal_scenario(F(1),F(1))
        self.assertEqual(F(q["sextic_delta_gain_vs_pr776"]),F(2)**6)
        self.assertEqual(F(q["sextic_delta_gain_vs_pr777"]),F(37441,33281)**6)
        self.assertGreater(F(q["sextic_delta_gain_vs_pr775"]),F(485))
        self.assertGreater(F(q["sextic_delta_gain_vs_pr777"]),F(2))
        self.assertLess(F(q["sextic_delta_gain_vs_pr777"]),F(3))

    def test_14_common_T_recalculated_when_both_HEAVY_and_LOW_change(self):
        C0,c0=F(1),F(1)
        z=envelope(32)
        a=root_budget(C0,c0,z["R_top_r_parent_777"],False)
        b=root_budget(C0,c0,z["R_chunk_sibling_776"],True)
        c=root_budget(C0,c0,z["R"],True)
        self.assertLess(int(c["T"]),int(a["T"]))
        self.assertLess(int(c["T"]),int(b["T"]))
        self.assertLess(int(c["L6"]),int(a["L6"]))
        self.assertLess(int(c["L6"]),int(b["L6"]))
        self.assertLess(int(c["mixed_four_blocker_cutoff"]),
                        int(a["mixed_four_blocker_cutoff"]))
        self.assertEqual(c["q2"],a["q2"])
        self.assertEqual(c["q3"],a["q3"])
        self.assertEqual(c["alpha"],["1/64","1/64","15/16"])

    def test_15_new_ROOT_BBo_margin_dominate_NEW_graph_delta(self):
        for C0,c0 in ((F(1),F(1)),(F(2),F(1,5)),(F(7,3),F(1,17))):
            q=root_budget(C0,c0,33281,True)
            self.assertGreater(F(q["original_BBo_produced_conditional_floor"]),
                               F(q["original_D6_HEAVY_delta"]))
            self.assertLess(int(q["coordinate_cutoff"]),int(q["exact_s0"])+1)
            self.assertLess(int(q["endpoint_cutoff"]),int(q["exact_s0"])+1)
            self.assertLess(int(q["mixed_four_blocker_cutoff"]),int(q["exact_s0"])+1)
            self.assertTrue(q["original_LOW_global_moment_proofs_inherited"])
            self.assertFalse(q["ROOT_PROVED_A"])

    def test_16_bad_external_graph_constants_fail_closed(self):
        for inputs in ((F(0),F(1)),(F(1),F(0)),(F(1),F(2)),
                       (1,F(1)),(F(1),0.5)):
            with self.assertRaises(ValueError):
                root_budget(*inputs,33281,True)
        for H in (0,7,9,31):
            with self.assertRaises(ValueError):
                envelope(H)
        with self.assertRaises(ValueError):
            min_alphabet(0)

    def test_17_bad_original_source_geometry_and_diagnostic_T_fail_closed(self):
        for s in (2,4):
            with self.assertRaises(ValueError):
                finite_dual_referee(s,"lex",-1)
            with self.assertRaises(ValueError):
                finite_dual_referee(s,"lex",F(1,2))
        with self.assertRaises(ValueError):
            original_symplectic_fixture(3,"lex")
        with self.assertRaises(ValueError):
            original_symplectic_fixture(2,"not-a-real-map")

    def test_18_actual_large_s_envelope_is_not_claimed_at_W32(self):
        with self.assertRaises(ValueError):
            actual_alphabet_envelope(2,32)
        with self.assertRaises(ValueError):
            actual_alphabet_envelope(4,32)
        self.assertEqual(len(self.c["true_large_dyadic_minimal_alphabet_envelopes"]),3)

    def test_19_external_C6_numerical_constants_still_unknown(self):
        for q in self.c["formal_ROOT_comparisons"]:
            self.assertTrue(q["actual_original_sixset_and_moments_STILL_PROOF_GATES"])
            self.assertFalse(q["root_PROVED_A"])
        self.assertTrue(self.c["external_graph_C6_constants_remain_existential"])
        self.assertTrue(self.c["original_full_LOW_moments_and_BBo_inverse_not_newly_accepted"])
        self.assertFalse(self.c["original_ROOT_unweighted_seven_sixset_PROVED_A"])

    def test_20_scientific_ancestry_and_no_automatic_main_merge(self):
        c=self.c
        self.assertEqual(c["schema"],SCHEMA)
        self.assertEqual(c["issue"],230)
        self.assertEqual(c["parent_pr"],777)
        self.assertEqual(c["parallel_pr"],776)
        self.assertEqual(c["status"],STATUS)
        self.assertEqual(c["branch_Z_scope"],"EMPTY")
        self.assertEqual(c["fixed_H"],32)
        self.assertEqual(c["fixed_K"],10)
        self.assertEqual(c["combined_R"],33281)
        self.assertEqual(c["old_R_parent_777"],37441)
        self.assertEqual(c["old_R_parallel_776"],66562)
        self.assertTrue(c["new_synthesis_all_h_mathematical_proof_in_manuscript"])
        self.assertTrue(c["no_GF5_or_ASET_exponent_claimed"])
        self.assertEqual(len(c["TRUE_original_W32_W34_finite_same_H_heavy_low_Q_cases"]),24)


if __name__=="__main__":
    unittest.main()
