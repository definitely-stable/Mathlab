"""INDEX-001 G2-B3-B external online theory source pins and provenance."""
import json
import unittest

from literature import DATA, INTERNAL, SOURCE_TITLE_PINS, valid

SOURCE_SHA = "7e62436374adc9e8cc15c98b68bf9d4a3a06644e"
ORIGIN = "docs/research/INDEX-001-G2-B3-B-ONLINE-ADVERSARY.md"
SOURCES = {
    "LIT-209": ("doi:10.4230/LIPIcs.ITCS.2026.75",
                "Prior-Independent and Subgame Optimal Online Algorithms"),
    "LIT-210": ("arxiv:2603.29233",
                "Robust and Consistent Ski Rental with Distributional Advice"),
    "LIT-211": ("doi:10.1016/j.orl.2025.107382",
                "A new performance metric for the ski rental problem"),
}


class Index001OnlineSourcesTests(unittest.TestCase):
    def test_unique_2026_ski_rental_sources_and_provenance(self):
        data = json.loads(DATA.read_text(encoding="utf-8"))
        catalog = json.loads(INTERNAL.read_text(encoding="utf-8"))
        self.assertEqual(valid(data, catalog), [])
        lookup = {e["id"]: e for e in data["entries"]}
        self.assertGreaterEqual(len(lookup), 210)
        self.assertEqual(len(lookup), len(data["entries"]))
        for k, (identity, title) in SOURCES.items():
            with self.subTest(source=k):
                paper = lookup[k]
                self.assertEqual(paper["identity"], identity)
                self.assertEqual(paper["title"], title)
                self.assertEqual(paper["year"], 2026)
                self.assertEqual(SOURCE_TITLE_PINS[identity], title)
                self.assertEqual(paper["track"], "online-optimization")
                self.assertEqual(paper["maps_to"], ["ML-004", "ML-006"])
                self.assertEqual(paper["mentioned_in"], [{
                    "repo": "MATHLAB", "path": ORIGIN,
                    "kind": "model_overlap", "source_sha": SOURCE_SHA,
                }])
                self.assertFalse(paper["full_proof_verified"])
                self.assertFalse(paper["independent_reproduction"])
        self.assertIn("publisher:pmlr:v306:kim26l",
                      lookup["LIT-210"]["alternate_identities"])
        self.assertEqual(len(set(
            x.lower() for e in data["entries"]
            for x in [e["identity"], *e.get("alternate_identities", [])])),
            sum(1 + len(e.get("alternate_identities", []))
                for e in data["entries"]))


if __name__ == "__main__":
    unittest.main()
