"""IMPORT-015: publisher identities, import graph and strict model fences."""
import copy
import json
import unittest
from literature import DATA, INTERNAL, INDEX, REVERSE, valid, render, render_reverse

REL = DATA.parent.parent / "IMPORT-015-ALGORITHM-RELATIONS.json"
IDS = [f"LIT-{i}" for i in range(398, 403)]
DOIS = ["10.1137/1.9781611978971.5", "10.1137/1.9781611978971.7",
        "10.1137/1.9781611978971.67", "10.1137/1.9781611978971.11"]

class Import015Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads(DATA.read_text(encoding="utf-8"))
        cls.registry=json.loads(INTERNAL.read_text(encoding="utf-8"))
        cls.rel=json.loads(REL.read_text(encoding="utf-8"))
        cls.rows={e["id"]:e for e in cls.data["entries"]}

    def test_five_new_canonical_records(self):
        entries=self.data["entries"]
        self.assertEqual(len(entries),401)
        self.assertEqual(len({e["id"] for e in entries}),401)
        self.assertEqual(len({e["identity"].lower() for e in entries}),401)
        self.assertEqual({e["id"] for e in entries if int(e["id"][4:])>=398},set(IDS))
        self.assertEqual(len({e["track"] for e in entries}),22)
        self.assertEqual(valid(self.data,self.registry),[])

    def test_publisher_and_preprint_disposition(self):
        for ident,doi in zip(IDS[:4],DOIS):
            e=self.rows[ident]
            self.assertEqual(e["identity"],"doi:"+doi)
            self.assertEqual(e["primary_url"],"https://doi.org/"+doi)
            self.assertEqual(e["publication_stage"],"peer_reviewed_proceedings")
            self.assertEqual(e["verification"],"publisher_abstract_checked")
        eccc=self.rows["LIT-402"]
        self.assertEqual(eccc["identity"],"publisher:eccc-tr26-129")
        self.assertEqual(eccc["primary_url"],"https://eccc.weizmann.ac.il/report/2026/129/")
        self.assertEqual(eccc["publication_stage"],"author_preprint")
        self.assertEqual(eccc["verification"],"primary_abstract_checked")
        for ident in IDS:
            e=self.rows[ident]
            self.assertFalse(e["full_proof_verified"])
            self.assertFalse(e["independent_reproduction"])
            self.assertEqual(e["mentioned_in"],[{
                "repo":"MATHLAB","kind":"model_overlap",
                "path":"docs/research/RESEARCH-LITERATURE-015-2026-DAG-LZ77-AUTOMATA.md",
                "source_sha":"808a07737c891d6d602ce999ab0b51f0042c4686"}])
            mutated=copy.deepcopy(self.data)
            next(x for x in mutated["entries"] if x["id"]==ident)["title"]="Forged publisher title"
            self.assertTrue(any("primary source title mismatch" in x for x in valid(mutated,self.registry)))

    def test_prior_work_dedup_and_graph(self):
        self.assertEqual(self.rows["LIT-258"]["identity"],"doi:10.1137/1.9781611978971.65")
        self.assertEqual(self.rel["rejected_duplicate"]["id"],"LIT-258")
        self.assertEqual(self.rel["new_literature"],IDS)
        self.assertEqual(self.rel["schema"],"mathlab.import015.typed-relations.v1")
        seen=set()
        self.assertGreaterEqual(len(self.rel["links"]),12)
        for e in self.rel["links"]:
            self.assertIn(e["source"],IDS)
            self.assertIn(e["target"],self.rows)
            self.assertIn(e["relation"],{"model_overlap","contrasts_with","assumption_incompatible","evaluation_baseline"})
            self.assertIs(e["theorem_transfer"],False)
            key=(e["source"],e["target"],e["relation"])
            self.assertNotIn(key,seen)
            seen.add(key)
        self.assertEqual({e["target"] for e in self.rel["model_bridges"]},
            {"DAG-002","INDEX-001","UCT-005","COMPRESSED-INDEXING","PROOF-COMPLEXITY"})

    def test_generated_navigation(self):
        self.assertEqual(INDEX.read_text(encoding="utf-8"),render(self.data))
        self.assertEqual(REVERSE.read_text(encoding="utf-8"),render_reverse(self.data,self.registry))
        for ident in IDS:
            self.assertIn("### "+ident,INDEX.read_text(encoding="utf-8"))
            self.assertIn(ident+"](LITERATURE.md#",REVERSE.read_text(encoding="utf-8"))

if __name__=="__main__":
    unittest.main()
