"""UCT-005 G2-B1 source and theorem-scope locks; not peer proof reproduction."""
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT/"docs/research/UCT-005-G2-B1-DAG-SEMANTIC-STRUCTURAL-COUNTERMODELS.md"
SOURCES = ROOT/"docs/research/UCT-005-G2-B1-SOURCES.json"
CATALOG = ROOT/"docs/research/catalog/literature.json"
TREE = ROOT/"docs/research/UCT-005-THEOREM-TREE.json"


class Uct005G2B1SourceTests(unittest.TestCase):
    def test_new_and_existing_papers_not_double_indexed(self):
        obj=json.loads(SOURCES.read_text(encoding="utf8"))
        self.assertEqual(obj["schema"],"mathlab.uct005.g2b1.source-inventory.v1")
        self.assertEqual(obj["source_sha"],
                         "d7fecfbcaaea21629ebf968c30122a3ba0b9236a")
        old={x["lit"]:x for x in obj["already_cataloged"]}
        self.assertEqual({*old},{"LIT-068","LIT-187"})
        new=obj["new_sources"]
        self.assertEqual({p["identity"] for p in new},{
            "doi:10.1137/24M1638215","publisher:iacr:2025-251"})
        self.assertEqual(len({p["id"] for p in new}),2)
        self.assertIn("Preprint",new[1]["publication_note"])
        self.assertIn("2025-02-13",new[0]["publication_note"])
        entries=json.loads(CATALOG.read_text(encoding="utf8"))["entries"]
        by_id={e["id"]:e for e in entries}
        for key,prior in old.items():
            self.assertEqual(by_id[key]["identity"],prior["identity"])
        identities={}
        for e in entries:
            for ident in [e["identity"],*e.get("alternate_identities",[])]:
                identities.setdefault(ident.lower(),set()).add(e["id"])
        for paper in new:
            keys=[paper["identity"],*paper.get("alternate_identities",[])]
            hits=set().union(*(identities.get(k.lower(),set()) for k in keys))
            self.assertLessEqual(len(hits),1)
            self.assertTrue(paper["primary_url"].startswith("https://"))
            self.assertIn(paper["verification"],{
                "publisher_abstract_checked","publisher_author_abstract_checked"})
            self.assertGreater(len(paper["limits"]),70)

    def test_exact_model_scope_and_no_novelty_promotion(self):
        text=NOTE.read_text(encoding="utf8")
        for marker in ("LIT-068","LIT-187","LIT-205","G2B1-L1",
                       "G2B1-L2","collision-free", "K+3",
                       "NO", "NOVEL_NONFACTORIZING_THEOREM_UNPROVED", "B_known", "G2B1-SRC"):
            self.assertIn(marker,text)
        self.assertNotIn("ROOT_THEOREM_PROVED",text)
        tree=json.loads(TREE.read_text(encoding="utf8"))
        self.assertEqual(tree["root_novelty"],"OPEN_UNPROVED")
        g2=next(n for n in tree["nodes"] if n["id"]=="UCT005G2B1")
        self.assertIn("OPEN",g2["status"])
        self.assertIn({"parent":"UCT005G2B","child":"UCT005G2B1",
                       "relation":"FALSIFICATION_NOT_IMPLICATION"},
                      tree["edges"])

if __name__=="__main__":
    unittest.main()
