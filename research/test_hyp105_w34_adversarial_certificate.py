"""True-original, optimizer-independent W(3,4) adversarial certificate tests."""
import json
import os
import unittest
from fractions import Fraction

from hyp105_w34_independent_oracle import (
    independent_w34_census, independent_bad_endpoint_census,
)


class TestW34AdversarialCertificate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(os.path.join(os.path.dirname(__file__),
                               "hyp105_w34_adversarial_certificate.json"),
                  encoding="utf-8") as stream:
            cls.cert = json.load(stream)

    def test_valid_typed_images_and_exact_graph(self):
        c = self.cert
        self.assertEqual((c["s"], c["a"], c["V"]), (4, 14, 85))
        for images in (c["f"], c["g"]):
            self.assertEqual(len(images), 85)
            self.assertEqual(len({tuple(x) for x in images}), 85)
            self.assertTrue(all(0 <= x < y < 14 for x, y in images))

    def test_independent_original_incidence_recount(self):
        """Recount ALL integer census fields, never trusting JSON as oracle."""
        c = self.cert
        actual = independent_w34_census(c["f"], c["g"])
        expected = c["final_census"]
        for key, value in actual.items():
            with self.subTest(key=key):
                self.assertEqual(value, expected[key])
        self.assertEqual(actual["unblocked"], 10522)
        self.assertEqual(actual["synchronized_BBo"], 5261)
        self.assertEqual(c["final_bbo"], actual["synchronized_BBo"])

    def test_certificate_is_not_a_self_consistency_only_check(self):
        c = self.cert
        actual = independent_w34_census(c["f"], c["g"])
        tampered = dict(c["final_census"], unblocked=10520,
                        synchronized_BBo=5260)
        # An internally consistent but forged figure is NOT evidence.
        self.assertNotEqual(actual["unblocked"], tampered["unblocked"])
        self.assertNotEqual(actual["synchronized_BBo"],
                            tampered["synchronized_BBo"])
        corrupted = list(map(list, c["f"]))
        corrupted[0] = corrupted[1]
        with self.assertRaises(ValueError):
            independent_w34_census(corrupted, c["g"])

    def test_candidate_finite_floor_refuted_with_exact_rational(self):
        actual = independent_w34_census(self.cert["f"], self.cert["g"])
        floor = (8 * Fraction(22, 125) * 4**6)
        ceiling = -(-floor.numerator // floor.denominator)
        self.assertEqual(ceiling, 5768)
        self.assertEqual(actual["synchronized_BBo"], 5261)
        self.assertLess(actual["synchronized_BBo"], ceiling)

    def test_typed_bad_endpoint_bound_and_partition(self):
        c = self.cert
        t = independent_bad_endpoint_census(c["f"], c["g"])
        self.assertEqual(t["nonincident"], 85 * 4**2 * 5)
        self.assertEqual(t["union"], t["left"] + t["right"] - t["both"])
        self.assertLessEqual(t["union"], 4 * (14-2) * 85 * 4)
        self.assertLessEqual(t["union"], t["nonincident"])
        self.assertGreaterEqual(t["both"], 0)


if __name__ == "__main__":
    unittest.main()
