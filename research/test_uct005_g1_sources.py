"""UCT-005 G1: bibliography/transfer identity locks; not an original theorem proof."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/research/UCT-005-G1-MEMORY-CHECKING-AND-VC-PRIMARY-AUDIT.md"
LIT = ROOT / "docs/research/catalog/literature.json"

class Uct005G1SourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc = DOC.read_text(encoding="utf-8")
        cls.items = json.loads(LIT.read_text(encoding="utf-8"))["entries"]

    def test_four_unique_canonical_primary_publications(self):
        self.assertEqual(len(self.items), 215
        by = {e["id"]: e for e in self.items}
        expected = {
            "LIT-156": ("doi:10.1109/SFCS.1991.185352", "publisher_abstract_checked"),
            "LIT-157": ("doi:10.1145/3618260.3649686", "publisher_full_text_spotchecked"),
            "LIT-158": ("doi:10.1007/978-3-031-91092-0_11", "publisher_abstract_checked"),
            "LIT-159": ("doi:10.4230/LIPIcs.AFT.2023.29", "publisher_full_text_spotchecked")
        }
        allident = set()
        for entry in self.items:
            for ident in [entry["identity"], *entry.get("alternate_identities", [])]:
                self.assertNotIn(ident.lower(), allident)
                allident.add(ident.lower())
        for ident, (identity, tier) in expected.items():
            e = by[ident]
            self.assertEqual(e["identity"], identity)
            self.assertEqual(e["verification"], tier)
            self.assertFalse(e["full_proof_verified"])
            self.assertFalse(e["independent_reproduction"])
            self.assertEqual(e["mentioned_in"][0]["kind"], "model_overlap")
            self.assertEqual(e["mentioned_in"][0]["source_sha"], "536fd3aab5aedcc89ca80c24333162991e51ec4b")
            self.assertEqual(e["mentioned_in"][0]["path"], "docs/research/UCT-005-G1-MEMORY-CHECKING-AND-VC-PRIMARY-AUDIT.md")
        self.assertIn("doi:10.1145/3707202", by["LIT-157"]["alternate_identities"])
        self.assertIn("arxiv:2307.04085", by["LIT-159"]["alternate_identities"])

    def test_no_unsound_model_transfer_or_novelty_promotion(self):
        required = ["read-only reads", "proof-binding", "position-binding",
                    "q_r", "q_w", "physically changed", "public updated positions",
                    "covert", "STOP_GENERIC", "OPEN_UNPROVED"]
        for phrase in required:
            self.assertIn(phrase, self.doc)
        self.assertIn("FULL", self.doc.upper())
        self.assertNotIn("NEW UNIVERSAL THEOREM PROVED", self.doc)

if __name__ == "__main__":
    unittest.main()
