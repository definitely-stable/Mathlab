"""UCT-005 G2-B2 typed bibliography and careful novelty status gates."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs/research/UCT-005-G2-B2-SOURCES.json"
CANON = ROOT / "docs/research/catalog/literature.json"
NOTE = ROOT / "docs/research/UCT-005-G2-B2-EXACT-BROADCAST-QUOTIENT-AND-STOP.md"
TREE = ROOT / "docs/research/UCT-005-THEOREM-TREE.json"


class G2B2PrimarySourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(DATA.read_text(encoding="utf8"))

    def test_unique_publisher_identities_and_provenance_tier(self):
        d = self.data
        self.assertEqual(d["schema"], "mathlab.uct005.g2b2.source-inventory.v1")
        rows = d["new_sources"]
        self.assertEqual(len(rows), 3)
        expected = {
            "G2B2-SRC-01": "doi:10.1016/j.tcs.2022.05.006",
            "G2B2-SRC-02": "doi:10.4230/LIPIcs.DISC.2018.25",
            "G2B2-SRC-03": "doi:10.4230/LIPIcs.OPODIS.2021.21",
        }
        self.assertEqual({e["id"] for e in rows}, set(expected))
        identities = []
        for e in rows:
            self.assertEqual(e["identity"], expected[e["id"]])
            self.assertEqual(e["primary_url"],
                             "https://doi.org/" + e["identity"][4:])
            self.assertEqual(e["verification"], "publisher_abstract_checked")
            self.assertGreater(len(e["nontransfer"]), 65)
            self.assertIn("202", str(e["year"])) if e["id"] != "G2B2-SRC-02" else None
            identities.extend([e["identity"], *e.get("alternate_identities", [])])
        self.assertEqual(len(identities), len({s.lower() for s in identities}))
        self.assertEqual(rows[-1]["year"], 2021)
        self.assertIn("2022-02-28", rows[-1]["venue"])

    def test_no_duplicate_of_existing_canonical_or_author_version(self):
        docs = json.loads(CANON.read_text(encoding="utf8"))["entries"]
        by = {}
        for e in docs:
            for ident in [e["identity"], *e.get("alternate_identities", [])]:
                by.setdefault(ident.lower(), set()).add(e["id"])
        for e in self.data["new_sources"]:
            hits = set()
            for ident in [e["identity"], *e.get("alternate_identities", [])]:
                hits.update(by.get(ident.lower(), set()))
            self.assertLessEqual(len(hits), 1)

    def test_root_is_not_proof_promoted(self):
        note = NOTE.read_text(encoding="utf8")
        for marker in ("G2-B2-L1", "STOP_AS_ROOT", "Sigma(A,D)",
                       "Patt-Shamir", "Fischer", "Feuilloley",
                       "OPEN_UNPROVED"):
            self.assertIn(marker, note)
        tree = json.loads(TREE.read_text(encoding="utf8"))
        self.assertEqual(tree["root_novelty"], "OPEN_UNPROVED")
        self.assertIn("UCT005G2B2", {e["id"] for e in tree["nodes"]})
        self.assertIn({"parent": "UCT005G2B1", "child": "UCT005G2B2",
                       "relation": "RESTRICTED_LEMMA_NOT_ROOT_PROOF"},
                      tree["edges"])


if __name__ == "__main__":
    unittest.main()
