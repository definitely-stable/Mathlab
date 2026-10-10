"""Independent structural and exact rational checks of E0-C random intensity."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial

from hyp105_g5e2b3e0_random_intensity import (
    CLASSES, EXPECTED_LEADING_NUMERATORS,
    TOTAL_EXPECTED_LEADING_NUMERATOR, DENOM,
    asymptotic_weight_coefficients, embedding_sandwich, report,
)
from hyp105_g5e2b3_forests import (
    restricted_growth_partitions, is_six_factor_forest, profile_for,
)


def independent_leading_forest_named_shapes():
    """Independent 203^2 scan, no imported E0-C template list."""
    names = Counter()
    for left in restricted_growth_partitions():
        p = profile_for(left)
        for right in restricted_growth_partitions():
            q = profile_for(right)
            if not is_six_factor_forest(left, right):
                continue
            if (p, q) in (
                    ((2, 2, 2), (1,)*6),
                    ((1,)*6, (2, 2, 2))):
                names["C/A"] += 1
            elif (p, q) in (
                    ((2, 2, 2), (2, 1, 1, 1, 1)),
                    ((2, 1, 1, 1, 1), (2, 2, 2))):
                names["C/B"] += 1
            elif p == q == (2, 1, 1, 1, 1):
                first = {v for v in set(left)
                         if left.count(v) == 2}
                second = {v for v in set(right)
                          if right.count(v) == 2}
                # Exactly two column IDs in each repeated original factor
                # endpoint. Overlap 1 creates a duplicate factor edge only
                # if BOTH endpoints were repeated over the SAME TWO IDs,
                # which the independent forest predicate already rejects.
                L = {i for i, v in enumerate(left) if v in first}
                R = {i for i, v in enumerate(right) if v in second}
                if len(L) != 2 or len(R) != 2:
                    raise AssertionError("bad repeated factor-pair projection")
                if L & R:
                    names["B/B-intersect"] += 1
                else:
                    names["B/B-disjoint"] += 1
    return names


class JointRandomIntensityTests(unittest.TestCase):
    def test_203_by_203_structural_census_independent_of_template_table(self):
        counts = independent_leading_forest_named_shapes()
        self.assertEqual(counts, Counter({
            "C/A":30, "C/B":360,
            "B/B-intersect":120, "B/B-disjoint":90,
        }))
        self.assertEqual(sum(counts.values()), 600)
        self.assertEqual(sum(x[1] for x in CLASSES), 600)

    def test_exact_GF5_asymptotic_coefficient_arithmetic(self):
        q = asymptotic_weight_coefficients()
        for name, named, rL, rR, c, divisor, GF5 in CLASSES:
            independently = Fraction(64*named, factorial(6)*divisor)*GF5
            self.assertEqual(independently, EXPECTED_LEADING_NUMERATORS[name])
            self.assertEqual(q["by_class"][name], independently)
            self.assertEqual(c, rL + rR - 6)
        self.assertEqual(q["total"], TOTAL_EXPECTED_LEADING_NUMERATOR)
        self.assertEqual(q["limit_total_over_s6"],
                         Fraction(4165300, 51**6))
        self.assertEqual(DENOM, 17596287801)
        self.assertFalse(q["all_h_fixed_label_lower"])
        self.assertFalse(q["strict_ASET_improvement"])

    def test_all_h_large_field_injective_forest_sandwich(self):
        for s in (16, 32, 64, 128, 256):
            x = embedding_sandwich(s)
            self.assertEqual(x["s"], s)
            self.assertEqual(len(x["by_class"]), 4)
            for kind, data in x["by_class"].items():
                self.assertGreater(data["M_lower"], 0)
                self.assertLessEqual(data["M_lower"], data["M_upper"])
                self.assertLessEqual(data["expected_R3_lower"],
                                     data["expected_R3_upper"])
                self.assertGreater(data["expected_R3_lower"], 0)
            self.assertFalse(x["universal_fixed_label_bound"])
        x = embedding_sandwich(1024)
        target = Fraction(4165300, DENOM)
        lower = sum((d["expected_R3_lower"] for d in x["by_class"].values()),
                    Fraction()) / 1024**6
        upper = sum((d["expected_R3_upper"] for d in x["by_class"].values()),
                    Fraction()) / 1024**6
        # Conservative 25% interval: checks real convergence, no power fit.
        self.assertGreater(lower, target * Fraction(3, 4))
        self.assertLess(upper, target * Fraction(5, 4))

    def test_fail_closed_bad_fields_and_scope(self):
        for s in (0, 2, 4, 8, 12, 15, 18):
            with self.assertRaises(ValueError):
                embedding_sandwich(s)
        q = report()
        self.assertTrue(q["new_600_leading_nonmatching_forest_shapes"])
        self.assertTrue(q["asymptotic_h_consequence_only"])
        self.assertTrue(q["no_per_label_lower_or_strict_ASET"])
        self.assertIn("4165300", q["total_leading_independent_uniform_R3"])


if __name__ == "__main__":
    unittest.main()
