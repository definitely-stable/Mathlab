"""INDEX-001 G2-B3-A primary crash-consistency literature import guard."""
import json
from pathlib import Path
import unittest

from literature import DATA, INTERNAL, SOURCE_TITLE_PINS, valid


SOURCE_SHA = "6cc1496bf68a1909e1bccb4def731a3b7d5e99ad"
PATH = "docs/research/INDEX-001-G2-B3-A-GENERATION-COMMIT-PROTOCOL.md"
WORKS = {
    "LIT-206": ("usenix:osdi25:leblanc", 2025,
                "PoWER Never Corrupts: Tool-Agnostic Verification of Crash Consistency and Corruption Detection"),
    "LIT-207": ("doi:10.1145/2872362.2872406", 2016,
                "Specifying and Checking File System Crash-Consistency Models"),
    "LIT-208": ("doi:10.15514/ISPRAS-2026-38(1)-7", 2026,
                "Lightweight file system crash-consistency checking with differential fuzzing"),
}


class GenerationSourcesTests(unittest.TestCase):
    def test_primary_identities_and_source_provenance(self):
        data = json.loads(DATA.read_text(encoding="utf-8"))
        catalog = json.loads(INTERNAL.read_text(encoding="utf-8"))
        self.assertEqual(valid(data, catalog), [])
        entries = {e["id"]: e for e in data["entries"]}
        self.assertGreaterEqual(len(entries), 207)
        for name, (identity, year, title) in WORKS.items():
            with self.subTest(entry=name):
                e = entries[name]
                self.assertEqual((e["identity"], e["year"], e["title"]),
                                 (identity, year, title))
                self.assertEqual(SOURCE_TITLE_PINS[identity], title)
                self.assertEqual(e["track"], "proof-certification")
                self.assertEqual(e["maps_to"], ["ML-004", "ML-006"])
                self.assertEqual(e["mentioned_in"], [{
                    "repo": "MATHLAB", "path": PATH,
                    "kind": "model_overlap", "source_sha": SOURCE_SHA,
                }])
                self.assertFalse(e["full_proof_verified"])
                self.assertFalse(e["independent_reproduction"])

    def test_distinct_canonical_identity_and_primary_uri(self):
        data = json.loads(DATA.read_text(encoding="utf-8"))
        identities = [e["identity"].lower() for e in data["entries"]]
        self.assertEqual(len(identities), len(set(identities)))
        self.assertTrue((Path(__file__).resolve().parents[1] / PATH).exists())
        refs = [e for e in data["entries"] if e["id"] in WORKS]
        self.assertEqual(len(refs), len(WORKS))
        self.assertEqual(sum(e["year"] == 2026 for e in refs), 1)
        self.assertTrue(all(e["primary_url"].startswith("https://")
                            for e in refs))


if __name__ == "__main__":
    unittest.main()
