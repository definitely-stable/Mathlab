"""Adversarial anti-rediscovery registry schema, citation, and gate tests."""
from copy import deepcopy
import json
import unittest

from known_registry import REGISTRY, VIEW, STATUSES, render, validate


class KnownAndStoppedRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = json.loads(REGISTRY.read_text(encoding="utf-8"))

    def modified(self):
        return deepcopy(self.original)

    def test_all_33_scoped_decisions_and_readable_render(self):
        entries = validate(self.original)
        self.assertGreaterEqual(len(entries), 33)
        self.assertEqual(len(set(item["id"] for item in entries)), 33)
        self.assertEqual(set(STATUSES), set(e["disposition"] for e in entries))
        self.assertEqual(render(self.original),
                         VIEW.read_text(encoding="utf-8"))

    def test_all_has_authority_and_concrete_reopen_gate(self):
        for item in validate(self.original):
            self.assertTrue(item["authority"], item["id"])
            self.assertGreater(len(item["reopen_only_if"]), 10)
            self.assertNotEqual(item["do_not_repeat"], item["reopen_only_if"])

    def test_finite_gf5_not_reopened_as_unknown_interval(self):
        indexed = {r["id"]: r for r in validate(self.original)}
        self.assertEqual(indexed["KR-009"]["disposition"], "CLOSED_PROVED")
        self.assertIn("=10", indexed["KR-009"]["scope"])
        self.assertIn("LENT-001-G2B-B2-EXACT10-CERTIFICATE.md",
                      indexed["KR-009"]["authority"][0])

    def test_prior_art_does_not_claim_full_model_equivalence(self):
        indexed = {r["id"]: r for r in validate(self.original)}
        for id_ in ("KR-011", "KR-012", "KR-026"):
            self.assertEqual(indexed[id_]["disposition"], "PRIOR_ART")
            self.assertGreater(len(indexed[id_]["reopen_only_if"]), 30)
        self.assertIn("NOT a global", self.original["purpose"])

    def test_duplicate_missing_and_changed_disposition_rejected(self):
        d = self.modified()
        d["entries"][1]["id"] = "KR-001"
        with self.assertRaises(ValueError):
            validate(d)
        d = self.modified()
        d["entries"].pop()
        with self.assertRaises(ValueError):
            validate(d)
        d = self.modified()
        d["entries"][5]["disposition"] = "ALREADY_PROVED_NOVEL"
        with self.assertRaises(ValueError):
            validate(d)

    def test_source_path_escape_and_absent_file_rejected(self):
        d = self.modified()
        d["entries"][0]["authority"] = [
            "docs/research/../../secrets.txt"
        ]
        with self.assertRaises(ValueError):
            validate(d)
        d = self.modified()
        d["entries"][0]["authority"] = [
            "docs/research/nonexistent-proof.md"
        ]
        with self.assertRaises(ValueError):
            validate(d)

    def test_forged_external_citation_and_empty_scope_rejected(self):
        d = self.modified()
        d["entries"][0]["primary_sources"] = ["file:///etc/passwd"]
        with self.assertRaises(ValueError):
            validate(d)
        d = self.modified()
        d["entries"][0]["scope"] = ""
        with self.assertRaises(ValueError):
            validate(d)

    def test_no_claim_of_exhaustive_literature(self):
        d = self.modified()
        d["purpose"] = "Complete and exhaustive proof of all math."
        with self.assertRaises(ValueError):
            validate(d)

    def test_superseded_hyp002_and_closed_tom_d2(self):
        indexed = {r["id"]: r for r in validate(self.original)}
        self.assertEqual(indexed["KR-013"]["disposition"], "SUPERSEDED")
        self.assertEqual(indexed["KR-020"]["disposition"], "STOP_PRODUCT")
        self.assertEqual(indexed["KR-033"]["disposition"], "DEFER")


if __name__ == "__main__":
    unittest.main()
