"""UCT-005 G3-B1 typed prior-art provenance and no-false-novelty gate."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "docs/research/UCT-005-G3-B1-SOURCES.json"
CATALOG = ROOT / "docs/research/catalog/literature.json"
DOC = ROOT / "docs/research/UCT-005-G3-B1-TEMPORAL-TRAJECTORY-PACKING.md"


class G3B1PriorArtAndProofScope(unittest.TestCase):
    def test_2026_source_one_underlying_publication(self):
        src = json.loads(SOURCES.read_text(encoding="utf-8"))
        self.assertEqual(src["schema"], "mathlab.uct005.g3b1.prior-art.v1")
        self.assertEqual(len(src["new_sources"]), 1)
        pub = src["new_sources"][0]
        self.assertEqual(pub["identity"], "doi:10.1016/j.jisa.2026.104444")
        self.assertEqual(pub["alternate_identities"], ["publisher:iacr:2025-404"])
        self.assertEqual(pub["year"], 2026)
        self.assertEqual(pub["source_tier"], "peer_reviewed_journal")
        self.assertFalse("full_proof_reproduced" in pub["verification"])
        self.assertIn("full formal proof not independently reproduced", pub["limits"])
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))["entries"]
        all_hits = [
            p for p in catalog if any(
                x.lower() in (str(p.get("identity", "")).lower(),
                              *(z.lower() for z in p.get("alternate_identities", [])))
                for x in [pub["identity"], *pub["alternate_identities"]])
        ]
        self.assertLessEqual(len(all_hits), 1)

    def test_classical_dedup_and_scope_closure(self):
        src = json.loads(SOURCES.read_text(encoding="utf-8"))
        lits = {e["id"] for e in src["already_indexed"]}
        self.assertEqual(lits, {"LIT-127", "LIT-118", "LIT-133",
                                "LIT-072", "LIT-157"})
        available = {e["id"] for e in
            json.loads(CATALOG.read_text(encoding="utf-8"))["entries"]}
        self.assertTrue(lits.issubset(available))
        doc = DOC.read_text(encoding="utf-8")
        for term in ("G3B1-T1", "2784", "3072", "262144", "2^{Hd}",
                     "OPEN_UNPROVED", "Prefix Hamming",
                     "CRYPTO_AND_PHYSICAL_UPDATE_PROBES_NOT_PROVED",
                     "Reinhart", "SNARK", "2026", "LIT-127"):
            self.assertIn(term, doc)
        self.assertNotIn("NOVEL_ASYMPTOTIC_ROOT_PROVED", doc)


if __name__ == "__main__":
    unittest.main()
