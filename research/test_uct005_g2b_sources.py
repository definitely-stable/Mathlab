"""UCT-005 G2-B: source provenance and nontransfer guard, not a proof."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/research/UCT-005-G2-B-SOURCES.json"
CATALOG = ROOT / "docs/research/catalog/literature.json"
NOTE = ROOT / "docs/research/UCT-005-G2-B-VERIFIED-2D-PARITY-AND-NOVELTY-GATE.md"

class G2BPrimarySourceGate(unittest.TestCase):
    def test_five_distinct_primary_identities_with_honest_verification(self):
        data = json.loads(SOURCE.read_text(encoding="utf-8"))
        works = data["sources"]
        self.assertEqual(data["schema"], "mathlab.uct005.g2b.source-inventory.v1")
        self.assertEqual(len(works), 5)
        expected = {
            "G2B-SRC-01": "doi:10.1049/iet-ifs.2014.0408",
            "G2B-SRC-02": "doi:10.1109/ACCESS.2019.2957346",
            "G2B-SRC-03": "doi:10.14778/3748191.3748219",
            "G2B-SRC-04": "arxiv:2608.25206",
            "G2B-SRC-05": "doi:10.1016/j.is.2018.06.009",
        }
        by = {e["id"]: e for e in works}
        self.assertEqual(set(by), set(expected))
        allids = []
        for k, ident in expected.items():
            paper = by[k]
            self.assertEqual(paper["identity"], ident)
            self.assertIn(paper["verification"], {
                "publisher_abstract_checked", "publisher_full_text_spotchecked",
                "author_paper_or_bibliography_checked"})
            self.assertGreaterEqual(len(paper["limits"]), 40)
            self.assertTrue(paper["primary_url"].startswith("https://"))
            if ident.startswith("doi:"):
                self.assertEqual(paper["primary_url"], "https://doi.org/" + ident[4:])
            if ident.startswith("arxiv:"):
                self.assertEqual(paper["primary_url"], "https://arxiv.org/abs/" + ident[6:])
            allids.extend([ident, *paper.get("alternate_identities", [])])
        self.assertEqual(len({s.lower() for s in allids}), len(allids))
        self.assertEqual(by["G2B-SRC-04"]["year"], 2026)
        self.assertIn("preprint", by["G2B-SRC-04"]["limits"])
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))["entries"]
        canonical = {}
        for e in catalog:
            for s in [e["identity"], *e.get("alternate_identities", [])]:
                canonical.setdefault(s.lower(), set()).add(e["id"])
        for e in works:
            hits = {id for s in [e["identity"], *e.get("alternate_identities", [])]
                    for id in canonical.get(s.lower(), set())}
            # Before/after graduation into the canonical catalog, a
            # bibliography identity may have at most ONE canonical row.
            self.assertLessEqual(len(hits), 1)

    def test_model_and_novelty_scope(self):
        note = NOTE.read_text(encoding="utf-8")
        for name in ("Wang", "Pennino", "Sun", "Shangguan", "Shekelyan"):
            self.assertIn(name, note)
        for text in ("OPEN_UNPROVED", "STOP_AS_ROOT", "FLIP(i,j)",
                     "OUTSIDE", "PARTIAL", "FULL", "lambda",
                     "H(N,lambda)", "T_program_bits"):
            self.assertIn(text, note)
        self.assertNotIn("NEW FUNDAMENTAL THEOREM PROVED", note)

if __name__ == "__main__":
    unittest.main()
