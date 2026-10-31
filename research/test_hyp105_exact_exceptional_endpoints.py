"""AA4-EXCEND: exact source/physical endpoint 4-partition and weighted audit."""
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import unittest

from hyp105_exact_exceptional_endpoints import (
    allh_exact_exceptional_envelope,
    finite_true_original_endpoint_partition,
    finite_independent_physical_endpoint_partition,
    finite_genuine_core_path_endpoint_mass,
    recomputed_allh_dense_branch_s0,
)
from hyp105_full_physical_degree_tail import genuine_source,exact_bad_endpoint_population
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic


class TestExactOriginalExceptionalEndpointReferee(unittest.TestCase):
    def check_source_vs_physical(self,power,f,g):
        source=finite_true_original_endpoint_partition(power,f,g)
        phys=finite_independent_physical_endpoint_partition(power,f,g)
        self.assertEqual(
            phys,source["source_first_four_way_endpoint_partition"])
        old_independent=exact_bad_endpoint_population(power,f,g)
        self.assertEqual(
            source["original_bad_left"],old_independent["left_endpoint_bad"])
        self.assertEqual(
            source["original_bad_right"],old_independent["right_endpoint_bad"])
        self.assertEqual(
            source["original_bad_intersection_J"],
            old_independent["both_endpoint_bad"])
        self.assertEqual(
            source["original_bad_union"],
            old_independent["union_endpoint_bad"])
        self.assertEqual(
            source["source_first_total_ordered_distinct_coordinate_pairs"],
            4*source["M"]**2)
        self.assertEqual(
            source["source_first_four_way_endpoint_partition"][
                "original_nonincident_endbad"],
            4*(2*source["s"]*(
                source["M_f_FULL"]+source["M_g_FULL"])-
                source["original_bad_intersection_J"]))
        self.assertGreaterEqual(source["original_bad_intersection_J"],0)
        self.assertGreater(
            source["source_first_four_way_endpoint_partition"][
                "original_nonincident_good"],0)
        return source

    def test_independent_exact_four_part_endpoint_W32_five_correlated_g(self):
        m=pair_labeled_symplectic(1,"lex")
        f,g0=tuple(m["left_labels"]),tuple(m["right_labels"])
        total=0
        for shift in (0,1,3,7,11):
            g=tuple(g0[(i+shift)%len(g0)] for i in range(len(g0)))
            with self.subTest(shift=shift):
                x=self.check_source_vs_physical(1,f,g)
                self.assertEqual(
                    x["source_first_four_way_endpoint_partition"]["missing_physical"],
                    4*(x["M"]**2-x["V"]**2))
                # Minimal W32 has M=V=15, so no missing physical pairs.
                self.assertEqual(
                    x["source_first_four_way_endpoint_partition"]["missing_physical"],0)
                self.assertGreater(
                    x["source_first_four_way_endpoint_partition"]["original_incident"],0)
                self.assertGreater(
                    x["original_bad_left"]+x["original_bad_right"],0)
                total+=x["original_bad_union"]
        self.assertGreater(total,0)

    def test_independent_exact_four_part_endpoint_W34_full_and_swapped(self):
        fixture=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json").read_text())
        f,g=tuple(map(tuple,fixture["f"])),tuple(map(tuple,fixture["g"]))
        _,V,_=genuine_source(2)
        for label,right in (
            ("fixed",g),
            ("shift-17",tuple(g[(i+17)%V] for i in range(V))),
            ("shift-41",tuple(g[(i+41)%V] for i in range(V))),
        ):
            with self.subTest(label=label):
                self.check_source_vs_physical(2,f,right)

    def test_weighted_proper_threewalk_exceptional_cauchy_true_W32(self):
        m=pair_labeled_symplectic(1,"lex")
        f,g=m["left_labels"],m["right_labels"]
        _,_,flags=genuine_source(1)
        for core in (
            None,(),tuple(range(0,len(flags),2)),
            tuple(i for i in range(len(flags)) if i%3)
        ):
            with self.subTest(core=core is None or len(core)):
                x=finite_genuine_core_path_endpoint_mass(1,f,g,core)
                self.assertTrue(x["explicit_Cauchy_integer_inequality_verified"])
                self.assertGreaterEqual(
                    x["exact_unweighted_exceptional_endpoint_universe"],0)
                self.assertLessEqual(
                    x["physical_exceptional_path_weight"],
                    x["physical_proper_path_total"])
                self.assertEqual(
                    x["physical_proper_path_total"],
                    sum(x["physical_endpoint_weight_by_four_classes"].values()))
                if core==():
                    self.assertEqual(x["physical_proper_path_total"],0)

    def test_weighted_proper_threewalk_exceptional_cauchy_true_W34(self):
        x=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json").read_text())
        f,g=tuple(map(tuple,x["f"])),tuple(map(tuple,x["g"]))
        _,V,flags=genuine_source(2)
        for label,core,right in (
            ("full",None,g),
            ("sparse",tuple(i for i in range(len(flags)) if i%3),g),
            ("shifted",tuple(i for i in range(len(flags)) if i%4),
             tuple(g[(i+17)%V] for i in range(V))),
        ):
            with self.subTest(label=label):
                z=finite_genuine_core_path_endpoint_mass(2,f,right,core)
                self.assertTrue(z["path_weight_is_NOT_assumed_uniform_in_original_source_pairs"])
                self.assertTrue(z["explicit_Cauchy_integer_inequality_verified"])
                self.assertLessEqual(
                    z["physical_exceptional_path_weight"]**2,
                    z["exact_unweighted_exceptional_endpoint_universe"]*
                    z["physical_endpoint_proper_Frobenius_squared"])

    def test_21s5_allh_exact_arithmetic_and_huge_dyadic_ladder(self):
        for h in list(range(6,20))+[24,32,55,80]:
            s=1<<h
            with self.subTest(h=h):
                z=allh_exact_exceptional_envelope(s)
                self.assertEqual(z["M"],z["a"]*(z["a"]-1)//2)
                self.assertEqual(z["N"],(s+1)**2*(s*s+1))
                self.assertEqual(
                    z["new_exceptional_population_upper"],
                    z["missing_physical_pairs_exact"]+
                    z["original_incident_pairs_exact"]+
                    z["original_endbad_pairs_upper"])
                self.assertLessEqual(
                    z["new_exceptional_population_upper"],21*s**5)
                self.assertGreater(
                    z["old_672_uniform_exceptional_cap"],
                    z["all_h_uniform_exceptional_cap"])
                self.assertLess(
                    Fraction(z["new_exceptional_population_upper"],s**5),21)
        for bad in (0,2,63,65,-64,True):
            with self.assertRaises(ValueError):
                allh_exact_exceptional_envelope(bad)

    def test_integrated_allh_improved_constants_and_safe_exact_s0(self):
        for K,T in ((64,1),(64,3),(64,2**65),(0,1),(3,70)):
            with self.subTest(K=K,T=T):
                v=recomputed_allh_dense_branch_s0(K,T)
                self.assertEqual(v["new_L6"],24+288*T*T)
                self.assertEqual(
                    v["new_exceptional_LE_squared"],
                    21*(64*(K+1)**3)**2*(24+288*T*T))
                self.assertEqual(
                    v["new_L4_integer_upper"],
                    2*v["new_sigma2_inv"]**2*(
                        __import__("math").isqrt(8*v["new_L6"])+
                        (__import__("math").isqrt(8*v["new_L6"])**2<
                         8*v["new_L6"])
                    )+40*T)
                self.assertGreaterEqual(
                    v["exact_safe_s0_conservative_integer"],
                    max(v["exact_s0_threshold_components"].values()))
                self.assertTrue(v["s0_requires_original_parent_tail_input_C_c"])
                self.assertTrue(v["all_source_f_g_quantifiers_preserved"])
                self.assertFalse(v["no_external_peer_review_or_root_acceptance"] is False)
        for bad in ((-1,1),(64,0),(True,1),(64,1.1)):
            with self.assertRaises(ValueError):
                recomputed_allh_dense_branch_s0(*bad)

    def test_fail_closed_injections_and_finite_source_power(self):
        m=pair_labeled_symplectic(1,"lex")
        f,g=m["left_labels"],m["right_labels"]
        for bad_power in (0,3,True):
            with self.assertRaises(ValueError):
                finite_true_original_endpoint_partition(bad_power,f,g)
            with self.assertRaises(ValueError):
                finite_independent_physical_endpoint_partition(bad_power,f,g)
        with self.assertRaises(ValueError):
            finite_true_original_endpoint_partition(1,f[:-1],g)
        with self.assertRaises(ValueError):
            finite_independent_physical_endpoint_partition(1,f,g[:-1])
        with self.assertRaises(ValueError):
            finite_genuine_core_path_endpoint_mass(1,f,g,core_ids=(0,0))

    def test_machine_readable_exceptional_endpoint_certificate(self):
        v=allh_exact_exceptional_envelope(64)
        c=recomputed_allh_dense_branch_s0(64,2**65)
        print("HYP105_AA4_EXCEND_CERTIFICATE="+json.dumps({
            "new_exact_all_h_source_exceptional_partition":
                "4(M²−V²)+4N+8s(Mf+Mg)−4J",
            "new_exceptional_s5_upper":"21",
            "old_exceptional_s5_upper":"64",
            "new_weighted_LE_squared_formula":"21*sigma3_new^-2*L6_new",
            "21s5_proof_uses_minimal_Ka_not_iid":True,
            "example_s64_new_exact_exceptional_upper":str(
                v["new_exceptional_population_upper"]),
            "example_s64_total_21s5":str(21*64**5),
            "safe_s0_integer_bits":
                c["exact_safe_s0_conservative_integer"].bit_length(),
            "all_h_extension_conditional_on_original_root_tail":True,
            "root_external_referee_pending":True,
        },sort_keys=True))


if __name__=="__main__":
    unittest.main()
