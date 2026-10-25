"""Independent AA4-CA original sixcube coefficient tests (no SciPy dependency)."""
import unittest
from fractions import Fraction

from hyp105_issue230_d6aa4ca_exact_n3_boolean_kernel import (
    AA4CA_EXACT_ABSTRACT_N3_ETA6,
    AA4CA_BZ_TO_CA_SAVING,
    PAIRS, TRIPLES, QUADS, _triple_incidence,
    exhaustive_pair_triple_lemma, independent_pair_graph_orbit_lemma,
    assert_n3_independent_cube, signed_kernel_numerator,
    sharp_abstract_witnesses, exact_n3_boolean_sixcube_certificate,
    original_W32_f_only_all_seven_exact_n3_envelope,
    original_W32_all64_true_center_exact_n3,
)
from hyp105_issue230_projection import fixture

PACKETS = ((0,1),(2,3),(4,5),(6,7),(8,9),(10,11))


class AA4CAExactBooleanN3Kernel(unittest.TestCase):
    def test_01_full_exhaustive_subset_dp_finite_lemma(self):
        a = exhaustive_pair_triple_lemma()
        self.assertEqual(a["max_layer2_plus_layer3"], 14)
        self.assertEqual(a["valid_triple_families"], 348644)
        self.assertEqual(a["triple_family_domain_size"], 1<<20)
        self.assertEqual(a["pair_graph_domain_size"], 1<<15)
        self.assertEqual(a["lex_first_maximizer_triple_mask"], 261091)
        self.assertEqual(a["lex_first_maximizer_number_pairs"], 0)
        self.assertEqual(len(PAIRS), 15)
        self.assertEqual(len(TRIPLES), 20)
        self.assertEqual(len(QUADS), 15)

    def test_02_independent_graph_orbit_full_enumeration(self):
        b = independent_pair_graph_orbit_lemma()
        self.assertEqual(b["max_layer2_plus_layer3"], 14)
        self.assertEqual(b["nonisomorphic_degree3_pair_graphs"], 62)
        self.assertEqual(b["all_pair_graphs_checked"], 32768)
        self.assertEqual(b["symmetric_group_size"], 720)

    def test_03_sharp_abstract_positive_negative_and_all_centers(self):
        pos, neg = sharp_abstract_witnesses()
        self.assertEqual(sum(pos), 16)
        self.assertEqual(sum(neg), 12)
        self.assertEqual(signed_kernel_numerator(pos), 60)
        self.assertEqual(signed_kernel_numerator(neg), -48)
        for v in range(64):
            self.assertLessEqual(abs(signed_kernel_numerator(pos, v)), 60)
            self.assertLessEqual(abs(signed_kernel_numerator(neg, v)), 60)
        self.assertEqual(AA4CA_EXACT_ABSTRACT_N3_ETA6, Fraction(15,16))
        self.assertEqual(AA4CA_BZ_TO_CA_SAVING, Fraction(19,128))
        cert=exact_n3_boolean_sixcube_certificate()
        self.assertEqual(cert["signed_upper"], 60)
        self.assertEqual(cert["signed_lower"], -48)
        self.assertFalse(cert["sharp_for_actual_physical_GF5"])
        self.assertEqual(cert["root_230"], "OPEN_WITH_FORMAL_BLOCKER")

    def test_04_adversarial_nonbinary_and_bad_boolean_oracles(self):
        good=[0]*64
        assert_n3_independent_cube(good)
        with self.assertRaises(ValueError):
            assert_n3_independent_cube(good[:63])
        with self.assertRaises(ValueError):
            assert_n3_independent_cube(good[:63]+[2])
        a=[0]*64; a[0]=a[1]=1
        with self.assertRaises(ValueError):
            assert_n3_independent_cube(a)
        a=[0]*64
        for i in range(4):a[1<<i]=1
        with self.assertRaises(ValueError):
            assert_n3_independent_cube(a)
        with self.assertRaises(ValueError):
            signed_kernel_numerator(good,center=64)

    def test_05_real_original_W32_f_only_all_seven_certificates(self):
        expected={
            "lex": (4690929, Fraction(89127651,128),
                    Fraction(8113433771,16),11225795),
            "S72":(3731790, Fraction(35452005,64),
                   Fraction(3883420431,8),3283610)
        }
        for scheme,(mass,saving,new,actual) in expected.items():
            model=fixture(1,scheme)
            env=original_W32_f_only_all_seven_exact_n3_envelope(model,PACKETS)
            self.assertEqual(env["original_source_Q_weight"],mass)
            self.assertEqual(env["strict_saving"],saving)
            self.assertEqual(env["new_AA4CA_E"],new)
            self.assertEqual(env["parent_BZ_E"]-new,saving)
            self.assertEqual(env["new_sixcube_eta6"],Fraction(15,16))
            adverse=dict(model,right_labels=tuple(reversed(model["right_labels"])))
            self.assertEqual(
                original_W32_f_only_all_seven_exact_n3_envelope(adverse,PACKETS)["new_AA4CA_E"],
                new)
            center=original_W32_all64_true_center_exact_n3(model,PACKETS)
            self.assertEqual(center["original_weighted_center"],actual)
            self.assertEqual(center["new_error_bound"],new)
            self.assertEqual(center["certified_center_lower"],0)
            print("AA4CA",scheme,"sixpacket_mass",mass,
                  "delta",saving,"new_error",new,flush=True)


if __name__ == "__main__":
    unittest.main()
