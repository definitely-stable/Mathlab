"""HEAVY genuine source physical no-clone, exact rational minimax and stop gates."""
import unittest
from fractions import Fraction as Q
from math import comb
from hyp105_heavy_srg_physical_density import (
    SCHEMA, ROOT_STATUS, H_FIXED, K_FIXED, ALPHA, R_OLD,
    ceilq, ceil_sqrt, envelope, formal_root, original_heavy_case,
    canonical_certificate,
)


class TestOriginalHeavySrgPhysicalDensity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=canonical_certificate()

    def test_01_all_order_source_envelope_exact_rational_thresholds(self):
        expected={8:72785,16:66930,24:66584,32:66562,40:66561,64:66561}
        for H,R in expected.items():
            z=envelope(H)
            self.assertEqual(z["R"],R)
            self.assertGreaterEqual(Q(R)*z["density_coeff"],1)
            self.assertLess(Q(R-1)*z["density_coeff"],1)
            self.assertLess(z["A"],Q(9,4))
            self.assertGreater(z["A"],Q(2))
            self.assertLess(z["M"],Q(35,32))
            self.assertEqual(z["selected_coeff"],z["alpha_coeff"]/4)
            self.assertEqual(z["density_coeff"],z["selected_coeff"]/(8*z["A"]))

    def test_02_strict_improvement_from_both_existing_coarse_envelopes(self):
        z=envelope(32)
        self.assertEqual(z["R"],66562)
        self.assertEqual(R_OLD,93312)
        self.assertGreater(Q(R_OLD,z["R"])**6,Q(7))
        self.assertLess(Q(R_OLD,z["R"])**6,Q(8))
        self.assertLess(z["A"],Q(2001,1000))
        self.assertLess(z["M"],Q(10001,10000))

    def test_03_physical_alphabet_bound_checked_independently_for_dyadic_orders(self):
        for H in (8,16,24,32):
            z=envelope(H)
            for exp in (H,H+2,H+4):
                s=2**exp
                V=(s+1)*(s*s+1)
                # integer-isqrt minimal a; avoids creating 2**48 candidate pairs.
                a=(1+__import__('math').isqrt(1+8*V))//2
                while comb(a,2)<V:
                    a+=1
                while comb(a-1,2)>=V:
                    a-=1
                self.assertLess(Q(a*a,s**3),z["A"])

    def test_04_true_symplectic_complete_W32_W34_real_no_clone_cases(self):
        rows=self.report["genuine_original_finite_cases"]
        self.assertEqual(len(rows),6)
        self.assertEqual({(r["s"],r["scheme"]) for r in rows},
                         {(s,t) for s in (2,4) for t in ("lex","reverse","shift")})
        for z in rows:
            s=z["s"]
            self.assertEqual(z["original_flags"],(s+1)**2*(s*s+1))
            self.assertEqual(z["physical_full_edges"],2*z["original_flags"])
            self.assertGreaterEqual(2*z["heavy_unique_owners"],z["real_heavy_edges"])
            self.assertGreaterEqual(4*z["after_two_cuts_owners"],z["independent_owners"])
            self.assertEqual(z["physical_selected_edges"],2*z["after_two_cuts_owners"])
            self.assertGreaterEqual(Q(z["F_density"]),Q(z["direct_source_density"]))
            self.assertTrue(z["real_F_no_clone"])
            self.assertTrue(z["source_J_independent"])
            self.assertTrue(z["retains_both_original_diagonals_before_F"])
            self.assertGreater(z["true_F_edges"],0)
            self.assertLessEqual(z["true_F_vertices"],2*z["physical_Q_vertices"])

    def test_05_independent_source_two_cut_diagnostic_thresholds(self):
        for s in (2,4):
            for mode in ("lex","reverse","shift"):
                z=original_heavy_case(s,mode,T=1)
                self.assertGreater(z["independent_owners"],0)
                self.assertGreater(z["after_two_cuts_owners"],0)
                self.assertGreater(z["true_F_edges"],0)

    def test_06_new_heavy_R_changes_both_T_and_delta_nontrivially(self):
        old_R=R_OLD
        new_R=envelope(32)["R"]
        self.assertLess(new_R,old_R)
        self.assertGreater(Q(old_R,new_R)**3,Q(2))
        self.assertLess(new_R**3,old_R**3)
        self.assertGreater(Q(old_R,new_R)**6,Q(7))

    def test_07_formal_root_probes_not_published_external_constants(self):
        inputs=((Q(1),Q(1),653),(Q(2),Q(1,5),683),
                (Q(7,3),Q(1,17),689))
        for C0,c0,h in inputs:
            z=formal_root(32,10,C0,c0)
            self.assertEqual(z["R"],66562)
            self.assertEqual(z["h0"],h)
            self.assertEqual(z["K"],10)
            self.assertEqual(z["q2"],1936)
            self.assertEqual(z["q3"],85184)
            self.assertGreater(z["BBo_floor"],z["delta"])
            self.assertFalse(z["root_PROVED_A"])
            self.assertFalse(z["external_C6_numeric_constants_known"])
            self.assertFalse(z["inherited_LOW_lemmas_independently_accepted"])
            self.assertGreaterEqual(z["s0"],2**z["H"])
            self.assertGreaterEqual(z["s0"],z["threshold_coord"])
            self.assertGreaterEqual(z["s0"],z["threshold_endpoint"])
            self.assertGreaterEqual(z["s0"],z["threshold_mixed_blocker"])

    def test_08_independent_parent_K10_H32_comparison_test_only(self):
        from hyp105_root_srg_frontier_independent import _ceilroot_budget
        for C0,c0,parent_h,new_h in ((Q(1),Q(1),667,653),
                                    (Q(2),Q(1,5),697,683),
                                    (Q(7,3),Q(1,17),704,689)):
            old=_ceilroot_budget(10,32,C0,c0)
            new=formal_root(32,10,C0,c0)
            self.assertEqual(old["exact_root_h0"],parent_h)
            self.assertEqual(new["h0"],new_h)
            self.assertEqual(Q(old["original_CORE_fraction"]),new["core"])
            self.assertEqual(old["q2"],new["q2"])
            self.assertEqual(old["q3"],new["q3"])
            self.assertEqual(old["R"],93312)
            self.assertLess(new["R"],old["R"])
            self.assertLess(new["T"],int(old["T"]))

    def test_09_invalid_source_scale_and_external_constants_fail_closed(self):
        for H in (0,2,7,9,31,33,True,8.0):
            with self.subTest(H=H),self.assertRaises(ValueError):
                envelope(H)
        for C0,c0 in ((Q(0),Q(1)),(Q(1),Q(0)),(Q(1),Q(2)),
                      (1,Q(1)),(Q(1),0.1)):
            with self.subTest(C0=C0,c0=c0),self.assertRaises(ValueError):
                formal_root(32,10,C0,c0)
        for K in (-1,0,1,2,3):
            with self.subTest(K=K),self.assertRaises(ValueError):
                formal_root(32,K,Q(1),Q(1))
        for s,mode,T in ((3,"lex",1),(2,"invalid",1),(2,"lex",0)):
            with self.assertRaises(ValueError):
                original_heavy_case(s,mode,T)

    def test_10_all_order_rational_cert_and_explicit_root_stop(self):
        r=self.report
        self.assertEqual(r["schema"],SCHEMA)
        self.assertEqual(r["issue"],230)
        self.assertEqual(r["parent_pr"],775)
        self.assertEqual(r["status"],ROOT_STATUS)
        self.assertEqual(r["head_scope"],"Z_EMPTY")
        self.assertEqual(r["new_R"],66562)
        self.assertEqual(r["previous_R"],93312)
        self.assertFalse(r["root_PROVED_A"])
        self.assertFalse(r["ASET_claimed"])
        self.assertTrue(r["external_C6_numerical_constants_NOT_established"])
        self.assertTrue(r["inherited_LOW_lemma_acceptance_still_open"])
        self.assertEqual([q["h0"] for q in r["formal_not_published_graph_probes"]],
                         [653,683,689])


if __name__=="__main__":
    unittest.main()
