"""Strict exact-source tests for AA4 LOW publication partition referee."""
import unittest
from collections import Counter
from itertools import combinations
from math import comb

from hyp105_low_publication_partition_referee import (
    SCHEMA, STATUS, genuine_gq, model, labels, multiply, canonical,
    bracket, endpoint_status, check_source_inverse, classify,
    integer_gf5_flow_mass, census, certificate, prove_root_endpoint_17,
)


class TestLowPublicationIndependent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = certificate()

    def test_01_original_field_arithmetic(self):
        self.assertEqual(multiply(2,2,4),3)
        self.assertEqual(multiply(2,3,4),1)
        self.assertEqual(multiply(3,3,4),2)
        self.assertEqual(canonical((0,2,3,0),4),(0,1,2,0))
        self.assertEqual(bracket((1,0,0,0),(0,0,1,0),2),1)

    def test_02_true_original_symplectic_geometry(self):
        for s,V,N in ((2,15,45),(4,85,425)):
            m=genuine_gq(s)
            self.assertEqual(m["V"],V)
            self.assertEqual(len(m["lines"]),V)
            self.assertEqual(len(m["flags"]),N)
            self.assertTrue(all(len(l)==s+1 for l in m["lines"]))
            self.assertEqual(len(m["projection"]),V*(V-(s+1)))
            self.assertTrue(all(len(set(l))==s+1 for l in m["lines"]))

    def test_03_actual_minimal_physical_alphabet(self):
        for s,a in ((2,6),(4,14)):
            V=(s+1)*(s*s+1)
            for scheme in ("lex","reverse","correlated"):
                aa,f,g=labels(V,scheme)
                self.assertEqual(aa,a)
                self.assertTrue(comb(a-1,2)<V<=comb(a,2))
                self.assertEqual(len(set(f)),V)
                self.assertEqual(len(set(g)),V)

    def test_04_exact_two_opposite_diagonals_no_clone(self):
        for s in (2,4):
            for core in ("full","even","deleted"):
                m=model(s,core=core)
                self.assertEqual(len(m["owned"]),2*len(m["C"]))
                self.assertEqual(len(m["owned"]),len(set(m["owned"])))

    def test_05_every_real_walk_partitioned_exactly_once(self):
        for z in self.c["real_cases"]:
            counts=z["disjoint_first_failure"]
            self.assertEqual(sum(counts.values()),z["physical_three_walks"])
            self.assertGreater(z["physical_three_walks"],0)
            self.assertGreater(counts.get("improper",0),0)

    def test_06_original_unordered_BBo_exact_two_direction_inverse(self):
        for z in self.c["real_cases"]:
            self.assertEqual(
                z["disjoint_first_failure"].get("accepted",0),
                2*z["true_original_produced_sixsets"])
        self.assertGreater(sum(z["true_original_produced_sixsets"]
                               for z in self.c["real_cases"]),0)

    def test_07_exact_missing_and_incident_endpoint_identities(self):
        for z in self.c["real_cases"]:
            a=z["a"]
            B=comb(a,2)
            M=B-z["V"]
            self.assertEqual(z["endpoint_types"]["missing"],4*(2*B*M-M*M))
            self.assertEqual(z["endpoint_types"]["incident"],4*z["I"])
            self.assertEqual(z["bad_endpoint_count"],
                             sum(z["endpoint_types"].get(t,0) for t in
                                 ("missing","incident","endbad","deleted")))

    def test_08_true_endpoint_Frobenius_Cauchy(self):
        for z in self.c["real_cases"]:
            self.assertLessEqual(z["true_bad_endpoint_path_count"]**2,
                                 z["bad_endpoint_count"]*
                                 z["real_proper_endpoint_energy"])

    def test_09_four_inner_blockers_are_one_union_not_four_sums(self):
        found=False
        for z in self.c["real_cases"]:
            bits=z["four_inner_blocker_nonexclusive_signatures"]
            self.assertEqual(sum(bits.values()),
                             z["disjoint_first_failure"].get("blocked",0))
            found=found or bool(bits)
            self.assertTrue(all(len(k)==4 and
                                set(k)<=set("01") and "1" in k
                                for k in bits))
        self.assertTrue(found)

    def test_10_non_vacuous_original_GF5_signed_positive_source(self):
        self.assertGreater(len(self.c["positive_GF5_examples"]),0)
        self.assertTrue(all(x["exact_GF5_ten_sign_mass"]==53838 for x in
                            self.c["positive_GF5_examples"]))

    def test_11_all_legal_full_and_smaller_CORE_cases(self):
        expected={(s,scheme,core)
                  for s in (2,4)
                  for scheme,core in
                  (("lex","full"),("reverse","full"),
                   ("correlated","full"),("lex","even"),
                   ("reverse","deleted"))}
        actual={(z["s"],z["scheme"],z["core"]) for z in self.c["real_cases"]}
        self.assertEqual(actual,expected)
        self.assertTrue(any(z["deleted_flags"]>0 for z in self.c["real_cases"]))
        self.assertTrue(any(z["original_CORE_flags"]<z["I"]
                            for z in self.c["real_cases"]))

    def test_12_strict_original_produced_source_inverse_adversarial(self):
        m=model(2,"lex","full")
        z=census(m)
        if z["sixsets"]:
            six=z["sixsets"][0]
            self.assertTrue(check_source_inverse(m,six))
            self.assertEqual(integer_gf5_flow_mass(m,six),53838)
            altered=dict(m)
            altered["C"]=set()
            self.assertFalse(check_source_inverse(altered,six))
        else:
            self.assertGreater(
                sum(v["true_original_produced_sixsets"]
                    for v in self.c["real_cases"]),0)

    def test_13_field_order_and_labels_fail_closed(self):
        for s in (0,1,3,8):
            with self.assertRaises(ValueError):
                genuine_gq(s)
        with self.assertRaises(ValueError):
            labels(15,"bad")
        with self.assertRaises(ValueError):
            model(2,"lex","unknown")

    def test_15_true_all_h_new_17s5_source_endpoint_bound(self):
        from fractions import Fraction as Q
        e=prove_root_endpoint_17()
        self.assertEqual(e["fixed_H"],32)
        self.assertTrue(e["Z_empty_only"])
        self.assertGreater(Q(e["combined_strict_coefficient_upper"]),16)
        self.assertLess(Q(e["combined_strict_coefficient_upper"]),17)
        self.assertLess(Q(e["exact_source_missing_coefficient_upper"]),Q(1,1000))
        self.assertLess(Q(e["exact_source_incident_coefficient_upper"]),Q(1,1000))
        self.assertEqual(e["consequence_proper_P3_endpoint_error_coefficient"],
                         "q3*ceil_sqrt(17*L6)")
        self.assertTrue(e["all_h_original_bad_endpoints_STRICT_LT_17_s5"])
        self.assertFalse(e["original_ROOT_PROVED_A"])

    def test_16_exact_spectral_error_component_sum_no_float(self):
        from fractions import Fraction as Q
        e=self.c["NEW_all_h_original_17s5_endpoint_referee"]
        total=(Q(e["exact_source_endbad_coefficient_upper"])
               +Q(e["exact_source_missing_coefficient_upper"])
               +Q(e["exact_source_incident_coefficient_upper"]))
        self.assertEqual(total,Q(e["combined_strict_coefficient_upper"]))
        self.assertLess(total,17)
        self.assertEqual(e["genuine_GQ_source_SRG_positive_eigenvalue"],"s-1")
        self.assertTrue(e["independent_correlated_f_g_alphabet"])

    def test_14_status_and_all_h_quantifier_firewall(self):
        c=self.c
        self.assertEqual(c["schema"],SCHEMA)
        self.assertEqual(c["status"],STATUS)
        self.assertEqual(c["issue"],230)
        self.assertEqual(c["parent_pr"],783)
        self.assertTrue(c["original_GQ_fixture_independent_GF2_GF4"])
        self.assertTrue(c["exact_partition_from_all_actual_physical_P3"])
        self.assertTrue(c["exact_original_unordered_sixID_two_direction_inverse"])
        self.assertTrue(c["original_GF5_integer_sign_palette_independent"])
        self.assertTrue(c["all_h_LOW_moment_and_full_AC_books_publication_signoff_still_open"])
        self.assertFalse(c["original_ROOT_PROVED_A"])


if __name__=="__main__":
    unittest.main()
