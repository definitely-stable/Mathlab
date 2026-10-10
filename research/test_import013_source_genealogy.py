"""IMPORT-013: source genealogy and no GF(5) model-transfer laundering."""
import json
import unittest

from literature import DATA, INTERNAL, ROOT


class Import013SourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = json.loads(
            (ROOT / "docs/research/IMPORT-013-SOURCE-GENEALOGY.json").read_text(
                encoding="utf-8"))
        cls.entries = json.loads(DATA.read_text(encoding="utf-8"))["entries"]
        cls.research = json.loads(INTERNAL.read_text(encoding="utf-8"))["entries"]

    def test_all_8_typed_sources_and_transfer_limits(self):
        g = self.graph
        self.assertEqual(g["schema"], "mathlab.import013.source-genealogy.v1")
        self.assertEqual(len(g["edges"]), 8)
        present = {x["id"] for x in self.entries} | {x["id"] for x in self.research}
        seen = set()
        for edge in g["edges"]:
            self.assertIn(edge["from"], present)
            self.assertIn(edge["to"], present)
            self.assertIn(edge["type"], ("METHOD_FAMILY", "PROPOSED_TRANSFER_STOP"))
            self.assertGreater(len(edge["detail"]), 20)
            key = (edge["from"], edge["to"], edge["type"])
            self.assertNotIn(key, seen)
            seen.add(key)
        for i in ("LIT-388", "LIT-389", "LIT-390"):
            self.assertTrue(any(x["from"] == i or x["to"] == i for x in g["edges"]))
            self.assertTrue(any(x["from"] == i and
                                x["type"] == "PROPOSED_TRANSFER_STOP"
                                for x in g["edges"]))

    def test_proof_status_and_nonduplicate_identities(self):
        self.assertEqual(len(self.entries), 389)
        by = {x["id"]: x for x in self.entries}
        self.assertEqual([by[f"LIT-{n}"]["identity"] for n in (388, 389, 390)],
                         ["arxiv:2512.07243", "arxiv:2507.14070",
                          "arxiv:2505.14322"])
        self.assertTrue(all(not by[f"LIT-{n}"]["full_proof_verified"] and
                            not by[f"LIT-{n}"]["independent_reproduction"]
                            for n in (388, 389, 390)))
        identities = [name.lower() for e in self.entries for name in
                      [e["identity"]] + e.get("alternate_identities", [])]
        self.assertEqual(len(identities), len(set(identities)))


if __name__ == "__main__":
    unittest.main()
