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

    def test_69_distinct_works_and_ten_lanes(self):
        entries = self.data["entries"]
        self.assertEqual(len(entries), 69)
        self.assertEqual(len({e["identity"].lower() for e in entries}), 69)
        self.assertEqual(len({e["id"] for e in entries}), 69)
        self.assertEqual(len({e["track"] for e in entries}), 10)

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

    def test_original_sedd_arxiv_identity_is_not_misattributed(self):
        e = next(x for x in self.data["entries"] if x["id"] == "LIT-022")
        self.assertEqual(e["identity"], "arxiv:2501.01046")
        self.assertTrue(e["title"].startswith("SEDD:"))
        self.assertNotIn("FED:", e["title"])
        d = copy.deepcopy(self.data)
        next(x for x in d["entries"] if x["id"] == "LIT-022")["title"] = "FED: Fast Dataset Deduplication"
        self.assertTrue(any("primary source title mismatch" in x
                            for x in valid(d, self.catalog)))

    def test_2026_broad_selection_is_not_sketch_centric(self):
        selected = [e for e in self.data["entries"]
                    if 50 <= int(e["id"][4:]) <= 69]
        self.assertEqual(len(selected), 20)
        self.assertEqual({e["year"] for e in selected}, {2026})
        self.assertEqual(len({e["track"] for e in selected}), 7)
        self.assertFalse({"streaming-reconciliation", "sparse-coding"} &
                         {e["track"] for e in selected})
        self.assertEqual(sum(e["track"] == "proof-certification"
                             for e in selected), 7)
        self.assertEqual(sum(e["track"] == "compressed-indexing"
                             for e in selected), 5)
        self.assertEqual(sum(e["publication_stage"] ==
                             "peer_reviewed_proceedings" for e in selected), 16)
        self.assertEqual(sum(e["publication_stage"] ==
                             "author_preprint" for e in selected), 4)
        self.assertTrue(all(e["mentioned_in"][0]["kind"] == "model_overlap"
                            for e in selected))

    def test_2026_year_stage_and_priority_mislabeling_is_rejected(self):
        for key, value, diagnostic in (
            ("year", 2025, "non-2026 cohort entry"),
            ("publication_stage", "peer_reviewed_proceedings", "proceedings DOI missing"),
            ("selection_priority", "publication accepted", "missing 2026 selection priority"),
        ):
            d = copy.deepcopy(self.data)
            target = next(x for x in d["entries"] if x["id"] == "LIT-063")
            target[key] = value
            self.assertTrue(any(diagnostic in x for x in valid(d, self.catalog)),
                            f"{key} must fail on mismatched source identity")

    def test_2026_source_and_classification_guardrails(self):
        d = copy.deepcopy(self.data)
        x = next(x for x in d["entries"] if x["id"] == "LIT-055")
        x["mentioned_in"][0]["kind"] = "cited"
        self.assertTrue(any("invented existing citation" in problem
                            for problem in valid(d, self.catalog)))
        d = copy.deepcopy(self.data)
        x = next(x for x in d["entries"] if x["id"] == "LIT-052")
        x["title"] = "FSST Fast Random Access"
        self.assertTrue(any("primary source title mismatch" in problem
                            for problem in valid(d, self.catalog)))

    def test_cross_identifier_alias_collision_is_rejected(self):
        d = copy.deepcopy(self.data)
        target = next(x for x in d["entries"] if x["id"] == "LIT-039")
        self.assertIn("doi:10.1109/ALLERTON.2011.6120248",
                      target["alternate_identities"])
        wrong = next(x for x in d["entries"] if x["id"] == "LIT-040")
        wrong["alternate_identities"] = list(target["alternate_identities"])
        self.assertTrue(any("duplicate canonical identity" in x
                            for x in valid(d, self.catalog)))

    def test_identity_alias_is_never_reported_as_a_second_work(self):
        d = copy.deepcopy(self.data)
        riblt = next(x for x in d["entries"] if x["id"] == "LIT-027")
        self.assertIn("arxiv:2402.02668", riblt["alternate_identities"])
        self.assertEqual(sum("arxiv:2402.02668" in [e["identity"]] +
                             e.get("alternate_identities", []) for e in
                             d["entries"]), 1)

    def test_bibliography_expansion_covers_three_projects(self):
        entries = self.data["entries"]
        self.assertEqual(len({e["id"] for e in entries}), 49)
        tracks = {e["track"] for e in entries}
        self.assertEqual(len(tracks), 10)
        self.assertTrue({"LIT-043", "LIT-044", "LIT-047"}.issubset(
            {e["id"] for e in entries}))
        self.assertTrue({"MATHLAB", "DELSK", "DELTAMETER"}.issubset(
            {origin["repo"] for e in entries for origin in e["mentioned_in"]}))

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
        self.assertIn("overline{3}", lookup["LIT-004"]["limits_ru"])
        self.assertIn("GF(q)", lookup["LIT-005"]["limits_ru"])
        self.assertIn("байтам", lookup["LIT-027"]["limits_ru"])
        self.assertIn("finite-sample", lookup["LIT-023"]["limits_ru"])

    def test_distinguish_explicit_citation_from_model_overlap(self):
        r = next(e for e in self.data["entries"] if e["id"] == "LIT-031")
        self.assertEqual(r["mentioned_in"][0]["kind"], "model_overlap")
        self.assertIn("model_overlap", render(self.data))


if __name__ == "__main__":
    unittest.main()
