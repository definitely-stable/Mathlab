"""Canonical 2025 shared-page prior art provenance and identity gates."""
import json
import unittest
from pathlib import Path
from literature import DATA, SOURCE_TITLE_PINS
ROOT=Path(__file__).resolve().parents[1]
NOTE=ROOT/"docs/research/INDEX-001-G2-B4-C3-SHARED-PAGES.md"

class C3SourceTests(unittest.TestCase):
    def test_new_primary_works_unique_and_properly_scoped(self):
        data=json.loads(DATA.read_text(encoding="utf-8"))
        all_ident=[x["identity"].lower() for x in data["entries"]]
        self.assertEqual(len(all_ident),len(set(all_ident)))
        desired={"LIT-281":"doi:10.4230/LIPIcs.MFCS.2025.87",
                 "LIT-282":"doi:10.1007/s00224-025-10238-7"}
        for key,identity in desired.items():
            group=[x for x in data["entries"] if x["id"]==key]
            self.assertEqual(len(group),1)
            entry=group[0]
            self.assertEqual(entry["identity"],identity)
            self.assertEqual(entry["title"],SOURCE_TITLE_PINS[identity])
            self.assertEqual(entry["verification"],"publisher_abstract_checked")
            self.assertFalse(entry["full_proof_verified"])
            self.assertFalse(entry["independent_reproduction"])
            self.assertEqual(entry["mentioned_in"],[{
                "repo":"MATHLAB",
                "path":str(NOTE.relative_to(ROOT)),
                "kind":"model_overlap",
                "source_sha":"9077e9ee52b1ec5fab50fc8f40004759184a6949"}])
        self.assertEqual(len([x for x in data["entries"]
            if x["identity"]=="doi:10.1145/3810240"]),1)  # existing LIT-008

if __name__=="__main__":
    unittest.main()
