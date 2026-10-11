"""IMPORT-012: typed scientific genealogy without theorem-laundering."""
import json
import unittest

from literature import DATA, INTERNAL, ROOT


class GenealogySourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = json.loads(
            (ROOT / "docs/research/IMPORT-012-SOURCE-GENEALOGY.json").read_text(encoding="utf-8"))
        cls.literature = json.loads(DATA.read_text(encoding="utf-8"))
        cls.catalog = json.loads(INTERNAL.read_text(encoding="utf-8"))

    def test_genealogy_sources_edges_and_typed_non_transfer(self):
        graph = self.graph
        self.assertEqual(graph["schema"], "mathlab.literature-genealogy.v1")
        names = set(graph["edge_types"])
        self.assertIn("PROPOSED_TRANSFER_STOP", names)
        self.assertIn("NEGATIVE_CONTROL", names)
        self.assertEqual(len(graph["edges"]), 29)
        ids = {p["id"] for p in self.literature["entries"]} | {
            r["id"] for r in self.catalog["entries"]}
        seen = set()
        for edge in graph["edges"]:
            self.assertIn(edge["from"], ids)
            self.assertIn(edge["to"], ids)
            self.assertIn(edge["type"], names)
            self.assertGreater(len(edge["detail"]), 18)
            key = (edge["from"], edge["to"], edge["type"])
            self.assertNotIn(key, seen)
            seen.add(key)
        self.assertTrue(any(e["from"] == "LIT-368" for e in graph["edges"]))
        self.assertTrue(any(e["from"] == "LIT-387" for e in graph["edges"]))

    def test_canonical_no_duplicates_and_proof_promotion(self):
        sources = self.literature["entries"]
        ids = set()
        for entry in sources:
            if entry["id"] >= "LIT-366":
                self.assertFalse(entry["full_proof_verified"])
                self.assertFalse(entry["independent_reproduction"])
            for name in [entry["identity"]] + entry.get("alternate_identities", []):
                self.assertNotIn(name.lower(), ids)
                ids.add(name.lower())
        lookup = {e["id"]: e for e in sources}
        self.assertEqual(lookup["LIT-216"]["identity"], "arxiv:2607.11464")
        self.assertIn("doi:10.1109/ICKG66886.2025.00019",
                      lookup["LIT-216"]["alternate_identities"])
        self.assertEqual(lookup["LIT-373"]["identity"],
                         "doi:10.4230/LIPIcs.CCC.2026.41")
        self.assertEqual(len(sources), 396)


if __name__ == "__main__":
    unittest.main()
