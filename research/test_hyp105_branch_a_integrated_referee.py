"""AA4-INTREF: independent conditional root quantifier and real source audit."""
import json
from fractions import Fraction
from pathlib import Path
import unittest

from hyp105_branch_a_integrated_referee import (
    _min_dyadic_at_least,
    _root_theorem_constants_from_source_lemmas,
    independently_certify_uniform_branch_A,
    true_original_finite_integration_certificate,
)
from hyp105_exact_exceptional_endpoints import recomputed_allh_dense_branch_s0
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_full_physical_degree_tail import genuine_source


class TestAllHBranchAIntegratedReferee(unittest.TestCase):
    def test_original_external_tail_constants_and_full_quantifier_ladder(self):
        # These are symbolic TEST PARAMETERS, not asserted actual
        # Jiang--Yepremyan constants! Generic proof is for ALL C,c>0.
        for C,c in (
            (Fraction(1,32),Fraction(1,10)),
            (Fraction(1),Fraction(1)),
            (Fraction(5,7),Fraction(2,11)),
            (Fraction(3),Fraction(1,9)),
            (Fraction(11,3),Fraction(13,17)),
            (Fraction(2**16),Fraction(1,2**20)),
        ):
            for extra in (0,1,3):
                with self.subTest(C=str(C),c=str(c),extra=extra):
                    q=independently_certify_uniform_branch_A(
                        C,c,power_offset=extra)
                    self.assertTrue(all(
                        q["all_three_s6_over_24_error_implications"].values()))
                    self.assertEqual(
                        q["original_BBo_sextic_lower_coefficient"],
                        Fraction(1,8))
                    self.assertEqual(
                        q["original_source_seven_class_uniform_coefficient"],
                        min(Fraction(1,8),c/Fraction(2**108)))
                    self.assertGreaterEqual(
                        q["tail_T_safe_integer"],
                        Fraction(2**59)*C**3)
                    self.assertFalse(
                        q["main_research_root_external_acceptance"])
                    self.assertTrue(q["original_external_theorem_constants_NOT_certified"])
                    self.assertGreaterEqual(
                        1<<q["minimum_dyadic_h0"],
                        q["s0_threshold_from_scratch"])
                    self.assertEqual(
                        q["tested_h"],q["minimum_dyadic_h0"]+extra)

    def test_double_implemented_root_moment_constants_and_dyadic_h0(self):
        # Cross-check old-local integration helper from #682 versus
        # independently rewritten integer derivation (NO call in source).
        for K,T in ((64,1),(64,3),(64,100),(64,2**65)):
            with self.subTest(K=K,T=T):
                original=recomputed_allh_dense_branch_s0(K,T)
                newly=_root_theorem_constants_from_source_lemmas(T)
                self.assertEqual(original["new_L6"],newly["L6"])
                self.assertEqual(
                    original["new_L4_integer_upper"],
                    newly["L4_upper_integer"])
                self.assertEqual(
                    original["conservative_B0_integer_upper"],
                    newly["B0_upper_integer"])
                self.assertEqual(
                    original["new_exceptional_LE_squared"],newly["LE_squared"])
                self.assertEqual(
                    original["exact_safe_s0_conservative_integer"],
                    newly["s0_integer"])
                h,s=_min_dyadic_at_least(newly["s0_integer"])
                self.assertGreaterEqual(s,newly["s0_integer"])
                if h>1:
                    self.assertLess(s//2,newly["s0_integer"])

    def test_true_original_W32_globally_reassigned_point_line_maps(self):
        m=pair_labeled_symplectic(1,"lex")
        f,g0=tuple(m["left_labels"]),tuple(m["right_labels"])
        n=len(m["incidences"])
        for shift,core in (
            (0,None),(1,()),(3,tuple(range(0,n,2))),
            (7,tuple(i for i in range(n) if i%3)),
        ):
            with self.subTest(shift=shift,core=core is None or len(core)):
                g=tuple(g0[(i+shift)%len(g0)] for i in range(len(g0)))
                z=true_original_finite_integration_certificate(1,f,g,core)
                self.assertTrue(z["all_checked"])
                self.assertTrue(all(z["cross_stack_checks"].values()))
                self.assertTrue(z["finite_not_all_h_root_proof"])
                if core==():
                    self.assertEqual(z["physical_proper_threewalk_count"],0)
                    self.assertEqual(z["original_accepted_BBo_count"],0)

    def test_true_original_W34_full_sparse_and_reassigned_g_same_original_IDs(self):
        fixture=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json").read_text())
        f,g=tuple(map(tuple,fixture["f"])),tuple(map(tuple,fixture["g"]))
        _,V,flags=genuine_source(2)
        for name,core,right in (
            ("full",None,g),
            ("sparse",tuple(i for i in range(len(flags)) if i%3),g),
            ("reassigned",tuple(i for i in range(len(flags)) if i%4),
             tuple(g[(i+17)%V] for i in range(V))),
        ):
            with self.subTest(name=name):
                q=true_original_finite_integration_certificate(
                    2,f,right,core)
                self.assertEqual(q["s"],4)
                self.assertTrue(all(q["cross_stack_checks"].values()))
                self.assertTrue(q["all_checked"])
                self.assertTrue(q["finite_not_all_h_root_proof"])

    def test_strict_fail_closed_math_input_constants_and_original_flags(self):
        for C,c in (
            (0,1),(-1,1),(1,0),(1,-1),(True,1),
            ("x",1),(1,None),
        ):
            with self.subTest(C=str(C),c=str(c)):
                with self.assertRaises(ValueError):
                    independently_certify_uniform_branch_A(C,c)
        for bad in (-1,True,1.5,6):
            with self.assertRaises(ValueError):
                independently_certify_uniform_branch_A(1,1,power_offset=bad)
        for bad in (0,-1,True,1.5):
            with self.assertRaises(ValueError):
                _min_dyadic_at_least(bad)
        for T in (0,-1,True):
            with self.assertRaises(ValueError):
                _root_theorem_constants_from_source_lemmas(T)
        m=pair_labeled_symplectic(1,"lex")
        f,g=m["left_labels"],m["right_labels"]
        for core in ((True,),(-1,),(0,0),(45,)):
            with self.assertRaises(ValueError):
                true_original_finite_integration_certificate(1,f,g,core)
        with self.assertRaises(ValueError):
            true_original_finite_integration_certificate(1,f[:-1],g)
        with self.assertRaises(ValueError):
            true_original_finite_integration_certificate(3,f,g)

    def test_machine_readable_rational_conditional_scope_and_status(self):
        q=independently_certify_uniform_branch_A(
            Fraction(1),Fraction(1),power_offset=0)
        print("HYP105_AA4_INTREF_CERTIFICATE="+json.dumps({
            "scope":"ALL dyadic h>=h0; ALL legal ORIGINAL W(3,s) correlated fixed f,g",
            "quantifier":"FOR ALL C_graph,c_graph>0 GIVEN the external true SS6 theorem",
            "example_C_graph_is_NOT_a_verified_graph_theorem_constant":True,
            "original_C6_tail_T_threshold":"T>=2^59*C_graph^3",
            "original_D6_delta":"min(1/8,c_graph*2^-108)",
            "integrated_sigma2_inverse":q["sigma2_inverse"],
            "integrated_sigma3_inverse":q["sigma3_inverse"],
            "integrated_L6_int":str(q["conservative_L6"]),
            "example_h0_from_placeholder_graph_constants":q["minimum_dyadic_h0"],
            "all_three_integrated_error_obligations_pass":
                all(q["all_three_s6_over_24_error_implications"].values()),
            "positive_original_BBo_ratio":"1/8",
            "same_original_ID_provenance_finite_integration":True,
            "not_a_new_independent_root_or_external_acceptance":True,
        },sort_keys=True))


if __name__=="__main__":
    unittest.main()
