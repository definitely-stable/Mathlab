"""IMPORT-014: unique publisher primary sources, dedup and nontransfer graph."""
import copy
import json
import unittest
from literature import DATA, INTERNAL, INDEX, REVERSE, valid, render, render_reverse

REL = DATA.parent.parent / "IMPORT-014-GRAPH-AI-RELATIONS.json"
IDS = [f"LIT-{i}" for i in range(393, 398)]
PMLR = ["ye26f", "john26a", "de-castelli26a", "wang26ip", "shi26n"]

class Import014Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads(DATA.read_text(encoding="utf-8"))
        cls.catalog=json.loads(INTERNAL.read_text(encoding="utf-8"))
        cls.edges=json.loads(REL.read_text(encoding="utf-8"))
        cls.entries={e["id"]:e for e in cls.data["entries"]}

    def test_exactly_five_new_and_total_396(self):
        self.assertEqual(len(self.data["entries"]),396)
        self.assertEqual(len({e["id"] for e in self.data["entries"]}),396)
        self.assertEqual(len({e["identity"].lower() for e in self.data["entries"]}),396)
        self.assertEqual({e["id"] for e in self.data["entries"] if int(e["id"][4:])>=393},set(IDS))
        self.assertEqual(len({e["track"] for e in self.data["entries"]}),22)
        self.assertEqual(valid(self.data,self.catalog),[])

    def test_all_publisher_source_pins_and_proof_fences(self):
        for ident,key in zip(IDS,PMLR):
            e=self.entries[ident]
            self.assertEqual(e["identity"],"publisher:pmlr-v306-"+key)
            self.assertEqual(e["primary_url"],"https://proceedings.mlr.press/v306/"+key+".html")
            self.assertEqual(e["verification"],"publisher_abstract_checked")
            self.assertEqual(e["publication_stage"],"peer_reviewed_proceedings")
            self.assertFalse(e["full_proof_verified"])
            self.assertFalse(e["independent_reproduction"])
            self.assertEqual(e["mentioned_in"],[{"repo":"MATHLAB","kind":"model_overlap",
                "path":"docs/research/RESEARCH-LITERATURE-014-GRAPH-AI-2026.md",
                "source_sha":"38d5dc52464d2c54fe00de22f2a3ea1025072f7b"}])
            tampered=copy.deepcopy(self.data)
            next(z for z in tampered["entries"] if z["id"]==ident)["title"]="Forged author paper title"
            self.assertTrue(any("primary source title mismatch" in z for z in valid(tampered,self.catalog)))
        self.assertEqual([self.entries[x]["track"] for x in IDS],
            ["graph-learning-theory","graph-learning-theory","graph-learning-theory","graph-reasoning","graph-rag"])

    def test_existing_mragent_is_not_reimported(self):
        existing=self.entries["LIT-230"]
        self.assertEqual(existing["title"],"Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents")
        self.assertEqual(existing["identity"],"arxiv:2606.06036")
        self.assertEqual(sum("Memory is Reconstructed, Not Retrieved" in e["title"] for e in self.data["entries"]),1)
        self.assertEqual(self.edges["known_duplicate"]["id"],"LIT-230")
        self.assertIn("ji26d",self.edges["known_duplicate"]["publisher_url"])

    def test_typed_edge_targets_and_nonpromotion(self):
        self.assertEqual(self.edges["schema"],"mathlab.import014.typed-relations.v1")
        self.assertEqual(self.edges["new_literature"],IDS)
        allowed={"contrasts_with","model_overlap","assumption_incompatible","evaluation_baseline","useful_design_analogy"}
        seen=set()
        self.assertGreaterEqual(len(self.edges["links"]),15)
        for x in self.edges["links"]:
            self.assertIn(x["source"],IDS)
            self.assertIn(x["target"],self.entries)
            self.assertIn(x["relation"],allowed)
            self.assertIs(x["theorem_transfer"],False)
            self.assertGreaterEqual(len(x["scope_note_en"]),40)
            edge=(x["source"],x["target"],x["relation"])
            self.assertNotIn(edge,seen)
            seen.add(edge)
        self.assertEqual({x["target"] for x in self.edges["model_bridges"]},
            {"DAG-002","ALG-001","UCT-005","INDEX-001","RESEARCH-INDEX"})
        for bridge in self.edges["model_bridges"]:
            self.assertTrue(set(bridge["literature"]).issubset(set(IDS)))
            self.assertGreaterEqual(len(bridge["boundary"]),50)

    def test_deterministic_generated_navigation(self):
        self.assertEqual(INDEX.read_text(encoding="utf-8"),render(self.data))
        self.assertEqual(REVERSE.read_text(encoding="utf-8"),render_reverse(self.data,self.catalog))
        for ident in IDS:
            self.assertIn("### "+ident,INDEX.read_text(encoding="utf-8"))
            self.assertIn(ident+"](LITERATURE.md#",REVERSE.read_text(encoding="utf-8"))

if __name__=="__main__":
    unittest.main()
