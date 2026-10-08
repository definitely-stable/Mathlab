"""RESEARCH-LITERATURE-001: deterministic primary-source metadata checks."""
import copy
import json
import unittest
from literature import DATA, INTERNAL, INDEX, REVERSE, valid, render, render_reverse


class LiteratureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(DATA.read_text(encoding="utf-8"))
        cls.catalog = json.loads(INTERNAL.read_text(encoding="utf-8"))

    def test_real_collection_has_no_metadata_errors(self):
        self.assertEqual(valid(self.data, self.catalog), [])

    def test_32_distinct_works_and_five_lanes(self):
        entries = self.data["entries"]
        self.assertEqual(len(entries), 32)
        self.assertEqual(len({e["identity"].lower() for e in entries}), 32)
        self.assertEqual(len({e["id"] for e in entries}), 32)
        self.assertEqual(len({e["track"] for e in entries}), 5)

    def test_forward_and_reverse_indices_are_exactly_reproducible(self):
        self.assertEqual(render(self.data), INDEX.read_text(encoding="utf-8"))
        self.assertEqual(render_reverse(self.data, self.catalog),
                         REVERSE.read_text(encoding="utf-8"))

    def test_research_anchors_are_pinned_and_do_not_claim_novelty(self):
        for e in self.data["entries"]:
            self.assertTrue(e["mentioned_in"])
            self.assertTrue(e["maps_to"])
            self.assertFalse(e["full_proof_verified"])
            self.assertFalse(e["independent_reproduction"])
            self.assertIn(e["verification"],
                          {"primary_abstract_checked", "publisher_abstract_checked",
                           "publisher_bibliography_checked", "publisher_full_text_spotchecked",
                           "author_paper_or_bibliography_checked"})

    def test_duplicate_doi_is_rejected(self):
        d = copy.deepcopy(self.data)
        d["entries"][1]["identity"] = d["entries"][0]["identity"]
        self.assertTrue(any("duplicate canonical identity" in err
                            for err in valid(d, self.catalog)))

    def test_missing_internal_research_link_is_rejected(self):
        d = copy.deepcopy(self.data)
        d["entries"][0]["maps_to"].append("ML-999")
        self.assertTrue(any("dangling research link" in err
                            for err in valid(d, self.catalog)))

    def test_unpinned_origin_and_invalid_sha_are_rejected(self):
        d = copy.deepcopy(self.data)
        d["source_snapshots"]["DELSK"]["sha"] = "main"
        self.assertTrue(any("invalid snapshot SHA" in err
                            for err in valid(d, self.catalog)))
        d = copy.deepcopy(self.data)
        d["entries"][1]["mentioned_in"][0]["path"] = "../escape.md"
        self.assertTrue(any("origin path unsafe" in err
                            for err in valid(d, self.catalog)))

    def test_promotion_to_independent_theorem_is_rejected(self):
        d = copy.deepcopy(self.data)
        d["entries"][0]["full_proof_verified"] = True
        d["entries"][0]["independent_reproduction"] = True
        self.assertTrue(any("unsupported proof/reproduction promotion" in err
                            for err in valid(d, self.catalog)))

    def test_non_equivalence_boundaries_are_documented(self):
        lookup = {e["id"]: e for e in self.data["entries"]}
        self.assertIn("t=3", lookup["LIT-004"]["limits_ru"])
        self.assertIn("GF(q)", lookup["LIT-005"]["limits_ru"])
        self.assertIn("байтам", lookup["LIT-027"]["limits_ru"])
        self.assertIn("finite-sample", lookup["LIT-023"]["limits_ru"])

    def test_distinguish_explicit_citation_from_model_overlap(self):
        r = next(e for e in self.data["entries"] if e["id"] == "LIT-031")
        self.assertEqual(r["mentioned_in"][0]["kind"], "model_overlap")
        self.assertIn("model_overlap", render(self.data))


if __name__ == "__main__":
    unittest.main()
