"""UCT-005 G2-A source identity and scope gates. Not a scientific proof."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Uct005G2AImportTests(unittest.TestCase):
    def test_canonical_six_added_and_existing_stoc_reused(self):
        entries = json.loads(
            (ROOT / "docs/research/catalog/literature.json").read_text(encoding="utf-8")
        )["entries"]
        self.assertEqual(len(entries), 215
        by = {e["id"]: e for e in entries}
        expected = {
            "LIT-199": "doi:10.1007/978-3-032-01878-6_6",
            "LIT-200": "doi:10.1007/978-3-032-25330-9_7",
            "LIT-201": "doi:10.4230/LIPIcs.ITCS.2026.71",
            "LIT-202": "doi:10.1007/978-3-642-00457-5_30",
            "LIT-203": "publisher:iacr:2025-110",
            "LIT-204": "doi:10.1007/978-3-642-14712-8_11",
        }
        canonical_plus_alias = [
            identity.lower()
            for entry in entries
            for identity in [entry["identity"], *entry.get("alternate_identities", [])]
        ]
        self.assertEqual(len(canonical_plus_alias), len(set(canonical_plus_alias)))
        self.assertEqual(by["LIT-072"]["identity"], "doi:10.1145/3798129.3800843")
        for lid, identity in expected.items():
            paper = by[lid]
            self.assertEqual(paper["identity"], identity)
            self.assertEqual(paper["mentioned_in"][0]["kind"], "model_overlap")
            self.assertEqual(paper["mentioned_in"][0]["source_sha"],
                             "cd5a7ec2b0ed442d03bac0b03e091421ab5446ef")
            self.assertEqual(paper["mentioned_in"][0]["path"],
                             "docs/research/UCT-005-G2-A-NEW-FUNDAMENTAL-BARRIERS.md")
            self.assertFalse(paper["full_proof_verified"])
            self.assertFalse(paper["independent_reproduction"])
        self.assertEqual(by["LIT-201"]["verification"],
                         "publisher_full_text_spotchecked")
        self.assertIn("publisher:iacr:2025-234",
                      by["LIT-199"]["alternate_identities"])
        self.assertIn("publisher:iacr:2025-1558",
                      by["LIT-200"]["alternate_identities"])

    def test_g2a_is_assumption_guard_not_new_root_proof(self):
        text = (ROOT / "docs/research/UCT-005-G2-A-NEW-FUNDAMENTAL-BARRIERS.md"
                ).read_text(encoding="utf-8")
        for marker in ("LIT-072", "write-probe", "FSS", "omega(n)",
                       "STOP 1D-as-root", "ROOT_NEW_THEOREM_UNPROVED"):
            self.assertIn(marker, text)
        tree = json.loads((ROOT / "docs/research/UCT-005-THEOREM-TREE.json"
                           ).read_text(encoding="utf-8"))
        self.assertEqual(tree["root_novelty"], "OPEN_UNPROVED")
        self.assertIn("UCT005G2A", [node["id"] for node in tree["nodes"]])
        self.assertIn(
            {"parent": "CERTIFICATION", "child": "UCT005G2A",
             "relation": "PROOF_INGREDIENT_ONLY"}, tree["edges"]
        )


if __name__ == "__main__":
    unittest.main()
