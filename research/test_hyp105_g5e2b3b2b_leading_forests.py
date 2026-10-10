"""Independent finite structural falsifiers for HYP-105 B3.1-B2-B."""
import unittest
from collections import Counter
from itertools import combinations

from hyp105_g5e2b3b2b_leading_forests import (
    C_GRAPH, C_PAIRS, B_GRAPH, B_CHERRY, EXPECTED_NAMED,
    cases, signed_orbits, supports, report, regression,
    independent_checks, relabel_graph, relabel_sign, automorphisms,
    b_graphs,
)
from hyp105_g5e2b3b1_critical_flows import (
    SIGNS, two_factors, exact_nowherezero_signed_flow,
)
from hyp105_g5e2b3b1b_five_six_flows import exact_dual_GF5_six_flow


class LeadingNonmatchingForests(unittest.TestCase):
    def test_simple_double_and_triple_cherry_are_distinct(self):
        self.assertEqual(Counter(C_GRAPH), Counter({pair: 2 for pair in C_PAIRS}))
        self.assertEqual(Counter(B_GRAPH)[B_CHERRY], 2)
        self.assertEqual(len(b_graphs((0, 1))), 3)
        self.assertEqual(len(two_factors()), 70)
        self.assertEqual(len(SIGNS), 10)
        self.assertEqual(len(automorphisms(C_GRAPH)), 48)
        self.assertEqual(len(automorphisms(B_GRAPH)), 16)

    def test_no_duplicate_original_factor_incidences(self):
        # A/A is a factor matching (handled by #214).
        # B/A is a unique one-cherry factor forest (handled by #218).
        # C/A and C/B and the two B/B cases are NEW here.
        expected_fixed = {
            "C/A": 700, "C/B": 360,
            "B/B-overlap": 240, "B/B-disjoint": 180,
        }
        for kind, expected in expected_fixed.items():
            left, rights, multiplier = cases(kind)
            self.assertEqual(len(rights) * 10, expected)
            self.assertEqual(expected * multiplier, EXPECTED_NAMED[kind])
            for right in rights:
                selected = supports(left, right)
                self.assertEqual(len(selected), 6)
                self.assertEqual(len(set(selected)), 6)
                self.assertTrue(all(len(set(s)) == 4 for s in selected))
                for block in (left, right):
                    self.assertEqual(sorted(Counter(x for edge in block
                                                     for x in edge).values()), [2] * 6)

    def test_orbit_masses_and_actions_preserve_classes(self):
        for kind in EXPECTED_NAMED:
            left, orbits, multiplier = signed_orbits(kind)
            self.assertEqual(multiplier * sum(m for _, m in orbits),
                             EXPECTED_NAMED[kind])
            base_right, mask = orbits[0][0]
            value = exact_nowherezero_signed_flow(left, base_right, mask)
            for perm in automorphisms(left):
                right = relabel_graph(base_right, perm)
                signed = relabel_sign(mask, perm)
                self.assertEqual(value, exact_nowherezero_signed_flow(
                    left, right, signed))

    def test_complete_exact_GF5_certificate_and_prior_cherry(self):
        result = report()
        self.assertEqual(result["completed_named_cases"], 50700)
        self.assertTrue(result["all_new_signed_templates_positive"])
        self.assertEqual(result["all_new_named_GF5_weight_sum"], 297992160)
        self.assertEqual(result["per_original_factor_forest_signed_GF5_coefficients"], {
            "C/A": 4243968,
            "C/B": 173682,
            "B/B-overlap": 482670,
            "B/B-disjoint": 558080,
        })
        self.assertEqual(result["all_leading_named_cases_including_accepted"], 162700)
        self.assertEqual(result["all_leading_factor_partition_shapes"], 631)
        self.assertEqual(result["subleading_forest_shapes_open"], 11032)
        self.assertFalse(result["all_h_fixed_label_R3_upper"])
        self.assertFalse(result["improved_ASET_exponent"])
        for row in result["by_class"]:
            self.assertEqual(row["positive_named_cases"]+row["zero_named_cases"],
                             EXPECTED_NAMED[row["class"]])
            self.assertTrue(0 <= row["minimum_GF5_flow"]
                            <= row["maximum_GF5_flow"] <= 51 ** 6)
        self.assertEqual(regression(), 3902064)

    def test_independent_fourier_ie_and_full_GF5_mitm(self):
        independent = independent_checks()
        self.assertEqual(independent["independent_ie_cross_checks"], 12)
        self.assertEqual(independent["independent_full_51_palette_mitm"], 4)


if __name__ == "__main__":
    unittest.main()
