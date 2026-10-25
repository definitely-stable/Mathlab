"""Test for HYP-105 Issue #230: W(3,4) Adversarial Certificate Verification and Refutation.

Verifies:
1. The explicit adversarial labeling (f, g) saved in hyp105_w34_adversarial_certificate.json
   is valid and injective into binom([14], 2).
2. The independent reference oracle ProjectionClosure evaluates BBo(f, g) exactly matching the certificate.
3. Direct numerical refutation:
   BBo(f, g) <= 5400 < 5768 = ceil(8 * c_0(4) * 4^6),
   conclusively refuting the candidate lower bound formula BBo >= 8 c_0 s^6 for c_0(4) = 0.176.
"""
import json
import os
import unittest

from hyp105_issue230_projection import ProjectionClosure
from hyp105_issue230_proof_audit import _geometry


class TestW34AdversarialCertificate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cert_path = os.path.join(
            os.path.dirname(__file__), "hyp105_w34_adversarial_certificate.json"
        )
        if not os.path.exists(cert_path):
            raise unittest.SkipTest(f"Certificate file not found: {cert_path}")

        with open(cert_path, "r", encoding="utf-8") as f:
            cls.cert = json.load(f)

    def test_certificate_structure_and_injectivity(self):
        """Verify that f and g are valid injective mappings of 85 points and lines into K_14."""
        cert = self.cert
        self.assertEqual(cert["s"], 4)
        self.assertEqual(cert["a"], 14)
        self.assertEqual(cert["V"], 85)

        f = [tuple(p) for p in cert["f"]]
        g = [tuple(p) for p in cert["g"]]

        self.assertEqual(len(f), 85)
        self.assertEqual(len(g), 85)

        # All pairs in [14] with u < v
        for u, v in f:
            self.assertLess(u, v)
            self.assertGreaterEqual(u, 0)
            self.assertLess(v, 14)

        for u, v in g:
            self.assertLess(u, v)
            self.assertGreaterEqual(u, 0)
            self.assertLess(v, 14)

        # Injectivity
        self.assertEqual(len(set(f)), 85, "Point map f must be injective")
        self.assertEqual(len(set(g)), 85, "Line map g must be injective")

    def test_independent_reference_evaluation(self):
        """Verify using independent ProjectionClosure that census and BBo match certificate."""
        cert = self.cert
        f = [tuple(p) for p in cert["f"]]
        g = [tuple(p) for p in cert["g"]]

        # Build custom model compatible with ProjectionClosure
        _, points, lines, incidences = _geometry(2)
        model = {
            "s": 4,
            "a": 14,
            "left_labels": f,
            "right_labels": g,
            "incidences": incidences,
        }

        closure = ProjectionClosure(model)
        census = closure.census()

        expected_bbo = cert["final_bbo"]
        self.assertEqual(census["synchronized_BBo"], expected_bbo)
        self.assertEqual(census["unblocked"], cert["final_census"]["unblocked"])
        self.assertEqual(census["blocked"], cert["final_census"]["blocked"])
        self.assertEqual(census["proper_P3"], cert["final_census"]["proper_P3"])

    def test_refutation_of_candidate_lower_bound_5768(self):
        """Conclusively verify the contradiction identified by the peer reviewer:

        Candidate bound asserted:
          c_0(4) = 0.176 ==> BBo(f, g) >= ceil(8 * 0.176 * 4^6) = 5768.
        Actual certified adversarial minimum:
          BBo(f, g) <= 5400.
        Deficit: at least 368 motifs below the candidate bound!
        """
        actual_bbo = self.cert["final_bbo"]
        c0_candidate = 0.176
        claimed_floor = int(8.0 * c0_candidate * (4 ** 6)) + 1  # 5768

        self.assertLessEqual(actual_bbo, 5400)
        self.assertEqual(claimed_floor, 5768)
        self.assertLess(
            actual_bbo,
            claimed_floor,
            f"Actual BBo={actual_bbo} must strictly refute the candidate floor {claimed_floor}",
        )
        deficit = claimed_floor - actual_bbo
        self.assertGreaterEqual(deficit, 368)


if __name__ == "__main__":
    unittest.main()
