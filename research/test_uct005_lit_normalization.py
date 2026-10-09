"""UCT-005: all G2-B/B1/B2 primary works now canonical, no theorem promotion."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAT = ROOT / "docs/research/catalog/literature.json"
SOURCES = [
    (ROOT / "docs/research/UCT-005-G2-B-SOURCES.json", 209, 5, "sources"),
    (ROOT / "docs/research/UCT-005-G2-B1-SOURCES.json", 214, 2, "new_sources"),
    (ROOT / "docs/research/UCT-005-G2-B2-SOURCES.json", 216, 3, "new_sources"),
]


class Uct005CanonicalSourceGraduation(unittest.TestCase):
    def test_ten_distinct_identity_pins_exact_correspondence(self):
        catalog = json.loads(CAT.read_text(encoding="utf-8"))["entries"]
        self.assertEqual(len(catalog), 218)
        byid = {entry["id"]: entry for entry in catalog}
        self.assertEqual(set(byid), {"LIT-" + str(i).zfill(3)
                                    for i in range(1, 219)})
        all_identifiers = []
        for p in catalog:
            all_identifiers.extend([p["identity"], *p.get("alternate_identities", [])])
        self.assertEqual(len(all_identifiers),
                         len({value.lower() for value in all_identifiers}))
        for source, start, length, key in SOURCES:
            data = json.loads(source.read_text(encoding="utf-8"))
            items = data[key]
            self.assertEqual(len(items), length)
            for index, item in enumerate(items):
                lid = f"LIT-{start + index:03d}"
                paper = byid[lid]
                self.assertEqual(item["canonical_lit_id"], lid)
                self.assertEqual(paper["identity"], item["identity"])
                self.assertEqual(paper["title"], item["title"])
                self.assertEqual(paper["year"], item["year"])
                self.assertEqual(set(paper.get("alternate_identities", [])),
                                 set(item.get("alternate_identities", [])))
                self.assertFalse(paper["full_proof_verified"])
                self.assertFalse(paper["independent_reproduction"])
                self.assertEqual(paper["mentioned_in"][0]["kind"], "model_overlap")
                self.assertTrue((ROOT / paper["mentioned_in"][0]["path"]).is_file())
                self.assertEqual(len(paper["mentioned_in"][0]["source_sha"]), 40)
        self.assertEqual(byid["LIT-212"]["identity"], "arxiv:2608.25206")
        self.assertEqual(byid["LIT-212"]["verification"],
                         "author_paper_or_bibliography_checked")
        self.assertEqual(byid["LIT-215"]["identity"], "publisher:iacr:2025-251")
        self.assertEqual(byid["LIT-215"]["verification"], "primary_abstract_checked")
        self.assertEqual(byid["LIT-218"]["year"], 2021)
        self.assertEqual(byid["LIT-205"]["identity"], "doi:10.3390/sym12060963")

    def test_provenance_sources_remain_only_evidence_not_new_root_proof(self):
        tree = json.loads(
            (ROOT/"docs/research/UCT-005-THEOREM-TREE.json").read_text(encoding="utf-8"))
        self.assertEqual(tree["root_novelty"], "OPEN_UNPROVED")
        for path in [
                "docs/research/UCT-005-G2-B-VERIFIED-2D-PARITY-AND-NOVELTY-GATE.md",
                "docs/research/UCT-005-G2-B1-DAG-SEMANTIC-STRUCTURAL-COUNTERMODELS.md",
                "docs/research/UCT-005-G2-B2-EXACT-BROADCAST-QUOTIENT-AND-STOP.md"]:
            self.assertTrue((ROOT/path).is_file())


if __name__ == "__main__":
    unittest.main()
