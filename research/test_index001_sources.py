"""INDEX-001 primary-source provenance and model-boundary locks."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs/research/catalog/literature.json"
AUDIT = ROOT / "docs/research/INDEX-001-G0-RANGE-MAP-FOUNDATION.md"

EXPECTED = {
    "LIT-177": ("doi:10.1137/S009753970240481X", "Optimal External Memory Interval Management"),
    "LIT-178": ("doi:10.1137/110842211",
                "The Limits of Buffering: A Tight Lower Bound for Dynamic Membership in the External Memory Model"),
    "LIT-179": ("doi:10.1109/FOCS57990.2023.00112",
                "Tight Cell-Probe Lower Bounds for Dynamic Succinct Dictionaries"),
    "LIT-180": ("doi:10.1002/spe.3433", "Practical Adaptive Dynamic Bitvectors"),
    "LIT-181": ("arxiv:2608.06066",
                "Dynamic Entropy-Encoded Arrays in O(1) Time with Nearly Optimal Space"),
    "LIT-182": ("doi:10.1145/3654978",
                "Structural Designs Meet Optimality: Exploring Optimized LSM-tree Structures in a Colossal Configuration Space"),
}


class Index001SourceTests(unittest.TestCase):
    def test_exact_six_new_identities_and_source_provenance(self):
        data = json.loads(CATALOG.read_text(encoding="utf-8"))
        self.assertEqual(len(data["entries"]), 215
        by_id = {x["id"]: x for x in data["entries"]}
        self.assertEqual(len(by_id), 215
        ids = {x for e in data["entries"] for x in
               [e["identity"], *e.get("alternate_identities", [])]}
        self.assertEqual(len(ids), sum(1 + len(e.get("alternate_identities", []))
                                      for e in data["entries"]))
        for key, (identity, title) in EXPECTED.items():
            e = by_id[key]
            self.assertEqual(e["identity"], identity)
            self.assertEqual(e["title"], title)
            self.assertFalse(e["full_proof_verified"])
            self.assertFalse(e["independent_reproduction"])
            self.assertEqual(e["mentioned_in"], [{
                "repo": "MATHLAB",
                "path": "docs/research/INDEX-001-G0-RANGE-MAP-FOUNDATION.md",
                "kind": "model_overlap",
                "source_sha": "a5a9b347940579650cdb8c8164f59911cb2602cb"
            }])

    def test_existing_sources_not_reidentified(self):
        by = {x["id"]: x for x in
              json.loads(CATALOG.read_text(encoding="utf-8"))["entries"]}
        self.assertEqual(by["LIT-098"]["identity"], "arxiv:2011.02615")
        self.assertEqual(by["LIT-175"]["identity"], "usenix:fast26:zhao")
        self.assertEqual(by["LIT-176"]["identity"], "usenix:fast26:ren")
        self.assertEqual(by["LIT-011"]["identity"], "arxiv:2608.06077")
        self.assertIn("arxiv:2306.02253", by["LIT-179"]["alternate_identities"])

    def test_audit_admits_compaction_and_stabbing_model_mismatch(self):
        doc = AUDIT.read_text(encoding="utf-8")
        for phrase in ("STANDALONE", "latest-write-wins",
                       "stabbing", "Verbin", "Smoose",
                       "PHYSICAL_LOWER_BOUND_OPEN", "RUST_NO_GO",
                       "WAL", "L1:", "L2:", "L3:"):
            self.assertIn(phrase.lower(), doc.lower())
        self.assertNotIn("ORIGINAL THEOREM PROVED", doc.upper())


if __name__ == "__main__":
    unittest.main()
