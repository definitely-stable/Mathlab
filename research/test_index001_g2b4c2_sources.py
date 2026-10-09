"""C2 SODA 2026 primary-source title, provenance, and non-duplication."""
import json
import unittest
from pathlib import Path
from literature import DATA, SOURCE_TITLE_PINS
ROOT=Path(__file__).resolve().parents[1]
NOTE=ROOT/"docs/research/INDEX-001-G2-B4-C2-ADAPTIVE-PARTITIONS.md"
class AdaptiveSourceTest(unittest.TestCase):
    def test_soda2026_primary_identity(self):
        data=json.loads(DATA.read_text(encoding="utf-8"))
        group=[e for e in data["entries"] if e["identity"]=="doi:10.1137/1.9781611978971.65"]
        self.assertEqual(len(group),1)
        e=group[0]
        self.assertEqual(e["id"],"LIT-252")
        self.assertEqual(e["title"],SOURCE_TITLE_PINS[e["identity"]])
        self.assertEqual(e["authors"],["Dominik Kempa","Tomasz Kociumaka"])
        self.assertEqual(e["verification"],"publisher_abstract_checked")
        self.assertFalse(e["full_proof_verified"])
        self.assertFalse(e["independent_reproduction"])
        self.assertIn("ML-006",e["maps_to"])
        self.assertEqual(e["mentioned_in"],[{
            "repo":"MATHLAB","path":str(NOTE.relative_to(ROOT)),
            "kind":"model_overlap","source_sha":"cb9dc19e328154977914fba167191d01fe92ebde"}])
        self.assertIn(e["identity"][4:],NOTE.read_text(encoding="utf-8"))
if __name__=="__main__":
    unittest.main()
