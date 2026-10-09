"""Provenance gate for INDEX-001 G2-B4-A canonical primary-source imports."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs/research/catalog/literature.json"
DOCUMENT = ROOT / "docs/research/INDEX-001-G2-B4-A-VARIABLE-CHECKPOINT.md"


class Index001G2B4ASources(unittest.TestCase):
    def test_primary_identity_nonduplication_and_model_relevance(self):
        data = json.loads(CATALOG.read_text(encoding="utf-8"))
        entries = data["entries"]
        ids = {x["id"]: x for x in entries}
        self.assertEqual(len(entries), 212)
        self.assertEqual(len(ids), len(entries))
        all_identities = [alias.lower() for x in entries
                          for alias in [x["identity"], *x.get("alternate_identities", [])]]
        self.assertEqual(len(all_identities), len(set(all_identities)))
        document = DOCUMENT.read_text(encoding="utf-8")
        for number, identity, title in (
            ("LIT-212", "arxiv:2603.23119",
             "Compressing Dynamic Fully Indexable Dictionaries in Word-RAM"),
            ("LIT-213", "arxiv:2604.24080",
             "Dynamic Grammar-Compressed Self-Index in δ-Optimal Space"),
        ):
            e = ids[number]
            self.assertEqual(e["title"], title)
            self.assertEqual(e["identity"], identity)
            self.assertEqual(e["year"], 2026)
            self.assertEqual(e["verification"], "primary_abstract_checked")
            self.assertFalse(e["full_proof_verified"])
            self.assertFalse(e["independent_reproduction"])
            self.assertIn("ML-006", e["maps_to"])
            self.assertIn(identity.replace("arxiv:", ""), document)
            self.assertEqual(len(e["mentioned_in"]), 1)
            origin = e["mentioned_in"][0]
            self.assertEqual(origin["repo"], "MATHLAB")
            self.assertEqual(origin["kind"], "model_overlap")
            self.assertEqual(origin["path"], str(DOCUMENT.relative_to(ROOT)))
            self.assertRegex(origin["source_sha"], r"^[0-9a-f]{40}$")


if __name__ == "__main__":
    unittest.main()
