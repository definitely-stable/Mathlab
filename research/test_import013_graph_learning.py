"""IMPORT-013: pinned PMLR/ICML 2026 source identities and transfer-firewall tests."""
import copy
import json
import unittest
from literature import DATA, INTERNAL, INDEX, REVERSE, valid, render, render_reverse

RELATIONS = DATA.parent.parent / "IMPORT-013-GRAPH-LEARNING-RELATIONS.json"
KEYS = ["wittig26a", "fetrat-qharabagh26a", "zhu26e", "koke26a", "li26ig"]
IDS = [f"LIT-{i}" for i in range(388, 393)]

class Import013Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(DATA.read_text(encoding="utf-8"))
        cls.catalog = json.loads(INTERNAL.read_text(encoding="utf-8"))
        cls.relations = json.loads(RELATIONS.read_text(encoding="utf-8"))

    def test_canonical_396_with_no_duplicate_identity(self):
        rows = self.data["entries"]
        self.assertEqual(len(rows), 396)
        self.assertEqual(len({x["id"] for x in rows}), 396)
        self.assertEqual(len({x["identity"].lower() for x in rows}), 396)
        self.assertEqual(len({x["track"] for x in rows}), 22)
        self.assertEqual(valid(self.data, self.catalog), [])

    def test_five_pmlr_sources_and_origin_pins(self):
        records = {e["id"]:e for e in self.data["entries"]}
        for n,key in zip(IDS,KEYS):
            r = records[n]
            self.assertEqual(r["identity"], "publisher:pmlr-v306-" + key)
            self.assertEqual(r["primary_url"], "https://proceedings.mlr.press/v306/" + key + ".html")
            self.assertEqual(r["verification"], "publisher_abstract_checked")
            self.assertEqual(r["publication_stage"], "peer_reviewed_proceedings")
            self.assertFalse(r["full_proof_verified"])
            self.assertFalse(r["independent_reproduction"])
            self.assertEqual(r["mentioned_in"], [{"repo":"MATHLAB","kind":"model_overlap",
                "path":"docs/research/RESEARCH-LITERATURE-013-ICML-GRAPH-LEARNING-2026.md",
                "source_sha":"ceb08432c1b2c611bde225a9279eecf5bc165a6e"}])
        self.assertEqual({records[n]["track"] for n in IDS[:4]}, {"graph-learning-theory"})
        self.assertEqual(records["LIT-392"]["track"], "graph-reasoning")

    def test_primary_title_tamper_is_rejected(self):
        for n in IDS:
            altered = copy.deepcopy(self.data)
            next(x for x in altered["entries"] if x["id"] == n)["title"] = "Wrong title"
            self.assertTrue(any("primary source title mismatch" in x for x in valid(altered, self.catalog)))

    def test_typed_edges_and_cross_model_firewall(self):
        rel=self.relations
        self.assertEqual(rel["schema"], "mathlab.import013.typed-relations.v1")
        self.assertEqual(rel["new_literature"], IDS)
        all_ids={x["id"] for x in self.data["entries"]}
        seen=set()
        for x in rel["links"]:
            self.assertIn(x["source"], IDS)
            self.assertIn(x["target"], all_ids)
            self.assertIn(x["relation"], {"contrasts_with","model_overlap","assumption_incompatible","evaluation_baseline"})
            self.assertIs(x["theorem_transfer"], False)
            self.assertGreaterEqual(len(x["scope_note_en"]), 30)
            key=(x["source"],x["target"],x["relation"])
            self.assertNotIn(key, seen)
            seen.add(key)
        self.assertEqual({x["target"] for x in rel["model_bridges"]},{"DAG-002","ALG-001","UCT-005","INDEX-001"})
        for x in rel["model_bridges"]:
            self.assertGreaterEqual(len(x["boundary"]), 50)
            self.assertTrue(set(x["literature"]).issubset(set(IDS)))

    def test_regenerated_navigation_exact(self):
        self.assertEqual(INDEX.read_text(encoding="utf-8"), render(self.data))
        self.assertEqual(REVERSE.read_text(encoding="utf-8"), render_reverse(self.data,self.catalog))
        for n in IDS:
            self.assertIn("### " + n, INDEX.read_text(encoding="utf-8"))
            self.assertIn(n + "](LITERATURE.md#", REVERSE.read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
