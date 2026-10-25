"""AA4-WE independent fixed-label weighted endpoint finite falsifiers."""
import json
import os
import unittest
from fractions import Fraction

from hyp105_w34_independent_oracle import independent_w34_census
from hyp105_w34_weighted_endpoint import (
    weighted_endpoint_profile, moment_sufficient_conditions,
)


class TestWeightedEndpointProfile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(os.path.join(os.path.dirname(__file__),
                               "hyp105_w34_adversarial_certificate.json"),
                  encoding="utf-8") as stream:
            cls.certificate = json.load(stream)

    def test_two_independent_oracle_methods_and_exact_moments(self):
        c = self.certificate
        p = weighted_endpoint_profile(c["f"], c["g"])
        self.assertEqual(p["source_nonincident_pairs"], 6800)
        self.assertEqual((p["bad_pairs"], p["good_pairs"]), (4086, 2714))
        self.assertEqual((p["left_pairs"], p["right_pairs"], p["both_pairs"]),
                         (2408, 2496, 818))
        self.assertEqual((p["bad_path_mass"], p["good_path_mass"]),
                         (35616, 23114))
        self.assertEqual((p["left_path_mass"], p["right_path_mass"],
                          p["both_path_mass"]), (21238, 21714, 7336))
        self.assertEqual((p["proper_P3"], p["missing"], p["incident"]),
                         (70476, 8306, 3440))
        self.assertEqual(p["path_mass"], 58730)
        self.assertEqual(p["good_internal_blocked_path_mass"], 12592)
        self.assertEqual(p["projected_unblocked_path_mass"], 10522)
        self.assertEqual(p["projected_synchronized_BBo"], 5261)
        self.assertEqual(2*p["projected_synchronized_BBo"],
                         p["path_mass"]-p["bad_path_mass"]
                         -p["good_internal_blocked_path_mass"])
        self.assertEqual(p["N3_sum_squares"], 676700)
        self.assertEqual((p["bad_N3_sum_squares"], p["good_N3_sum_squares"]),
                         (415704, 260996))
        self.assertEqual((p["N3_zero_pairs"], p["N3_max"]), (187, 38))
        self.assertEqual(p["weighted_minus_unweighted_fraction"],
                         Fraction(35616, 58730)-Fraction(4086, 6800))
        self.assertEqual(p["covariance_indicator_N3"],
                         Fraction(35616*6800-4086*58730, 6800**2))

    def test_bad_endpoint_implies_blocked_physical_path(self):
        """The point/line projection blocks EVERY bad-pair proper path."""
        c = self.certificate
        p = weighted_endpoint_profile(c["f"], c["g"], verify_join=False)
        exact_census = independent_w34_census(c["f"], c["g"])
        self.assertEqual(p["path_mass"],
                         exact_census["blocked"] + exact_census["unblocked"])
        self.assertLessEqual(p["bad_path_mass"], exact_census["blocked"])
        self.assertEqual(exact_census["blocked"] - p["bad_path_mass"], 12592)
        self.assertEqual(exact_census["blocked"],
                         p["bad_path_mass"] +
                         p["good_internal_blocked_path_mass"])
        self.assertEqual(exact_census["synchronized_BBo"],
                         p["projected_synchronized_BBo"])
        self.assertEqual(exact_census["unblocked"], 10522)

    def test_independent_physical_coordinate_relabeling(self):
        """Permutation of x- and y-coordinate alphabets must not change N3."""
        c = self.certificate
        baseline = weighted_endpoint_profile(c["f"], c["g"])
        # Both multipliers are invertible modulo 14.
        f = [sorted(((3*x+1) % 14, (3*y+1) % 14)) for x, y in c["f"]]
        g = [sorted(((5*x+3) % 14, (5*y+3) % 14)) for x, y in c["g"]]
        transformed = weighted_endpoint_profile(f, g)
        self.assertEqual(transformed, baseline)

    def test_fail_closed_invalid_injections(self):
        c = self.certificate
        f = list(map(list, c["f"]))
        f[0] = f[1]
        with self.assertRaises(ValueError):
            weighted_endpoint_profile(f, c["g"])

    def test_moment_upper_bound_is_explicitly_conditional(self):
        output = moment_sufficient_conditions(4, 4086, 415704)
        self.assertEqual(output["integer_ceiling_cs_upper"],
                         __import__("math").isqrt(4086*415704) +
                         (__import__("math").isqrt(4086*415704)**2 != 4086*415704))
        self.assertTrue(output["is_upper_bound_assumption"])
        self.assertFalse(output["root_proved"])
        with self.assertRaises(ValueError):
            moment_sufficient_conditions(4, 4086, -1)


if __name__ == "__main__":
    unittest.main()
