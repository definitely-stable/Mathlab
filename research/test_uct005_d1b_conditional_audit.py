"""UCT-005 D1-B: text-level 2026 3SUM/APSP source-dependency guard."""
import copy
import json
import tempfile
import unittest
from pathlib import Path

from uct005_d1b_conditional_audit import (
    ROOT, MANIFEST, CATALOG, SENSITIVE, audit, audit_docs, audit_catalog,
)


class ConditionalHardnessAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.catalog = json.loads(CATALOG.read_text(encoding="utf-8"))["entries"]

    def test_exact_repo_inventory(self):
        self.assertEqual(audit(), [])
        self.assertEqual(self.manifest["source"]["id"], "LIT-357")
        self.assertEqual(self.manifest["decision"],
                         "NO_EXPLICIT_3SUM_APSP_DEPENDENT_MATHLAB_THEOREM_LOCATED")
        self.assertIn("implicit", self.manifest["completeness"].lower())
        self.assertEqual(len(self.manifest["documented_occurrences"]), 9)
        self.assertEqual(len(self.manifest["catalog_occurrences"]), 3)

    def test_new_unreviewed_document_hardness_claim_fails_closed(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["documented_occurrences"] = []
        manifest["excluded_paths"] = []
        with tempfile.TemporaryDirectory() as scratch:
            path = Path(scratch) / "docs/research/new-proof.md"
            path.parent.mkdir(parents=True)
            path.write_text("By the 3SUM Hypothesis, this must take n^2.\n", encoding="utf-8")
            errors = audit_docs(manifest, Path(scratch))
            self.assertTrue(any("UNREVIEWED_HARDNESS_MENTION" in e for e in errors))

    def test_catalog_new_conditional_entry_fails_closed(self):
        new = {"id": "LIT-999", "identity": "arxiv:9999.99999",
               "title": "SETH-hardness for an invented data structure",
               "summary_ru": "An unreviewed hardness claim", "limits_ru": "unreviewed"}
        errors = audit_catalog(self.manifest, self.catalog + [new])
        self.assertIn("UNREVIEWED_CANONICAL_HARDNESS_MENTION",
                      " ".join(errors))

    def test_expected_anchor_tamper_fails_closed(self):
        modified = copy.deepcopy(self.manifest)
        modified["documented_occurrences"][0]["anchor"] = "A deliberately removed title"
        errors = audit_docs(modified, ROOT)
        self.assertTrue(any("MISSING_EXPECTED_ANCHOR" in e for e in errors))
        self.assertTrue(any("UNREVIEWED_HARDNESS_MENTION" in e for e in errors))

    def test_reviewed_anchor_text_change_fails_closed(self):
        manifest = copy.deepcopy(self.manifest)
        manifest["documented_occurrences"] = [{
            "path": "docs/research/example.md", "anchor": "By the 3SUM",
            "kind": "SCOPED_SOURCE_AUDIT",
            "expected_line": "By the 3SUM Hypothesis, no subquadratic algorithm exists."
        }]
        manifest["excluded_paths"] = []
        with tempfile.TemporaryDirectory() as scratch:
            path = Path(scratch) / "docs/research/example.md"
            path.parent.mkdir(parents=True)
            path.write_text("By the 3SUM Hypothesis, this lower bound is unconditional.\n",
                            encoding="utf-8")
            errors = audit_docs(manifest, Path(scratch))
            self.assertTrue(any("CHANGED_REVIEWED_MENTION" in e for e in errors))

    def test_existing_catalog_claim_edit_fails_even_if_identity_unchanged(self):
        mutated = copy.deepcopy(self.catalog)
        next(e for e in mutated if e["id"] == "LIT-058")["summary_ru"] += (
            " This SETH result has a changed claim that requires review."
        )
        errors = audit_catalog(self.manifest, mutated)
        self.assertTrue(any("SOURCE_IDENTITY_OR_FIELDS_MISMATCH" in e for e in errors))

    def test_breakthrough_source_and_unaffected_other_assumptions(self):
        cohort = {e["id"]: e for e in self.catalog}
        expected = {i["lit_id"]: i["identity"] for i in self.manifest["catalog_occurrences"]}
        self.assertEqual({lid: cohort[lid]["identity"] for lid in expected}, expected)
        self.assertEqual(cohort["LIT-058"]["identity"],
                         "doi:10.4230/LIPIcs.STACS.2026.68")
        states = {x["name"]: x["status"] for x in self.manifest["hypothesis_statuses"]}
        self.assertEqual(states["STANDARD_3SUM"], "REFUTED_BY_2026_ALGORITHM")
        self.assertEqual(states["STANDARD_APSP"], "REFUTED_BY_2026_ALGORITHM")
        self.assertEqual(states["SETH_OVH_AND_UNCONDITIONAL_CELL_PROBE"],
                         "NOT_IMPLIED_REFUTED")
        self.assertTrue(SENSITIVE.search("3SUM"))
        self.assertTrue(SENSITIVE.search("APSP"))
        self.assertTrue(SENSITIVE.search("SETH"))
        self.assertFalse(SENSITIVE.search("ordinary shortest-path algorithm claim"))


if __name__ == "__main__":
    unittest.main()
