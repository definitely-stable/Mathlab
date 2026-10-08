"""RESEARCH-LITERATURE-001: deterministic primary-source metadata checks."""
import copy
import json
import re
import unittest
from literature import DATA, INTERNAL, INDEX, REVERSE, valid, render, render_reverse


class LiteratureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(DATA.read_text(encoding="utf-8"))
        cls.catalog = json.loads(INTERNAL.read_text(encoding="utf-8"))

    def test_real_collection_has_no_metadata_errors(self):
        self.assertEqual(valid(self.data, self.catalog), [])

    def test_108_distinct_works_and_fourteen_lanes(self):
        entries = self.data["entries"]
        self.assertEqual(len(entries), 108)
        self.assertEqual(len({e["identity"].lower() for e in entries}), 108)
        self.assertEqual(len({e["id"] for e in entries}), 108)
        self.assertEqual({f"LIT-{i:03d}" for i in range(1, 109)},
                         {e["id"] for e in entries})
        self.assertEqual(len({e["track"] for e in entries}), 14)

    def test_2026_report_links_match_bibliographic_identities(self):
        """Check real publisher URLs (part A) and internal anchors (part B)."""
        research = DATA.parent.parent
        reports = (
            DATA.parent / "LITERATURE-003-2026-OPPORTUNITY-AUDIT.md",
            research / "RESEARCH-LITERATURE-003B-2026-STOC-ICALP-EUROSYS.md",
        )
        registry = {e["id"]: e for e in self.data["entries"]}
        for report, expected in zip(reports, (20, 26)):
            with self.subTest(report=report.name):
                raw = report.read_text(encoding="utf-8")
                self.assertEqual(
                    self._check_report_paper_links(raw, registry), expected)

    @staticmethod
    def _check_report_paper_links(content, registry):
        """Match each visible paper ID to its exact canonical source."""
        pattern = re.compile(
            r"\[[^\]\n]*?\b(LIT-\d{3})\b[^\]\n]*?\]"
            r"\(([^)\s]+)\)",
            re.IGNORECASE,
        )
        links = list(pattern.finditer(content))
        for link in links:
            visible, target_url = link.group(1).upper(), link.group(2)
            paper = registry.get(visible)
            if paper is None:
                raise AssertionError(f"missing bibliographic work: {visible}")
            if target_url.startswith("https://"):
                if target_url != paper["primary_url"]:
                    raise AssertionError(
                        f"wrong bibliographic primary URL: {visible} -> "
                        f"{target_url}, expected {paper['primary_url']}")
            else:
                match = re.fullmatch(
                    r"(?:catalog/)?LITERATURE\.md#lit-(\d{3})",
                    target_url, re.IGNORECASE)
                if match is None:
                    raise AssertionError(
                        f"unknown bibliographic destination: {target_url}")
                target = "LIT-" + match.group(1)
                if target not in registry:
                    raise AssertionError(
                        f"missing bibliographic work: {visible} -> {target}")
                if visible != target:
                    raise AssertionError(
                        f"wrong bibliographic anchor: {visible} -> {target}")
        return len(links)

    def test_report_link_mismatch_is_rejected(self):
        registry = {e["id"]: e for e in self.data["entries"]}
        with self.assertRaisesRegex(AssertionError, "wrong bibliographic anchor"):
            self._check_report_paper_links(
                "[LIT-072](catalog/LITERATURE.md#lit-052)", registry)
        with self.assertRaisesRegex(AssertionError, "missing bibliographic work"):
            self._check_report_paper_links(
                "[LIT-999](catalog/LITERATURE.md#lit-999)", registry)
        with self.assertRaisesRegex(AssertionError,
                                    "wrong bibliographic primary URL"):
            self._check_report_paper_links(
                "[LIT-063](https://doi.org/10.1145/wrong)", registry)

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

    def test_26_new_venue_sources_are_broad_and_nonreconciliation(self):
        new = [e for e in self.data["entries"]
               if "LIT-070" <= e["id"] <= "LIT-095"]
        self.assertEqual(len(new), 26)
        self.assertGreaterEqual(len({e["track"] for e in new}), 8)
        self.assertFalse(any(e["track"] == "streaming-reconciliation"
                             for e in new))
        self.assertEqual({e["year"] for e in new}, {2026})
        self.assertEqual({e["venue"] for e in new},
                         {"STOC 2026", "ICALP 2026", "EuroSys 2026"})
        self.assertEqual(len({e["identity"] for e in new}), 26)
        self.assertEqual(len([e for e in self.data["entries"]
                              if e["id"] <= "LIT-069"]), 69)
        self.assertTrue(all(e["publication_stage"] == "peer_reviewed_proceedings"
                            and not e["full_proof_verified"]
                            and not e["independent_reproduction"]
                            for e in new))

    def test_2026_venue_identity_and_year_falsifications(self):
        d = copy.deepcopy(self.data)
        target = next(e for e in d["entries"] if e["id"] == "LIT-070")
        target["source_listing_url"] = "https://example.com/spurious"
        target["year"] = 2025
        errors = valid(d, self.catalog)
        self.assertTrue(any("primary 2026 listing/identity mismatch" in x
                            for x in errors))
        self.assertTrue(any("venue-2026 cohort has non-2026 work" in x
                            for x in errors))

    def test_2026_source_cannot_be_promoted_to_independent_proof(self):
        d = copy.deepcopy(self.data)
        target = next(e for e in d["entries"] if e["id"] == "LIT-095")
        target["verification"] = "publisher_full_text_spotchecked"
        target["full_proof_verified"] = True
        errors = valid(d, self.catalog)
        self.assertTrue(any("unsupported 2026 full-text verification" in x
                            for x in errors))
        self.assertTrue(any("unsupported proof/reproduction promotion" in x
                            for x in errors))

    def test_concurrent_2026_primary_cohorts_are_both_preserved(self):
        original = {e["id"] for e in self.data["entries"]}
        self.assertTrue({f"LIT-{i:03d}" for i in range(50, 96)} <= original)
        self.assertTrue({f"LIT-{i:03d}" for i in range(1, 96)} <= original)
        self.assertEqual(len(self.data["entries"]), 108)
        all_ids = [e["identity"].lower() for e in self.data["entries"]]
        self.assertEqual(len(all_ids), len(set(all_ids)))

    def test_tom007_seven_source_identity_and_provenance_are_retained(self):
        expected = {
            "LIT-096": "arxiv:1503.07792",
            "LIT-097": "arxiv:1407.3008",
            "LIT-098": "arxiv:2011.02615",
            "LIT-099": "doi:10.4230/LIPIcs.CPM.2026.20",
            "LIT-100": "arxiv:1211.1056",
            "LIT-101": "publisher:pmlr:cohen25c",
            "LIT-102": "usenix:atc22:curtsinger",
        }
        selected = {e["id"]: e for e in self.data["entries"]
                    if "LIT-096" <= e["id"] <= "LIT-102"}
        self.assertEqual(set(selected), set(expected))
        for key, identity in expected.items():
            with self.subTest(paper=key):
                paper = selected[key]
                self.assertEqual(paper["identity"], identity)
                self.assertEqual(paper["mentioned_in"], [{
                    "repo": "MATHLAB",
                    "path": "docs/research/TOM-007-SIX-HYPOTHESIS-AUDIT.md",
                    "kind": "model_overlap",
                }])
                self.assertFalse(paper["full_proof_verified"])
                self.assertFalse(paper["independent_reproduction"])
        self.assertEqual(len([e for e in self.data["entries"]
                              if e["id"] <= "LIT-095"]), 95)
        # A false/changed primary title cannot pass the metadata authority.
        changed = copy.deepcopy(self.data)
        next(e for e in changed["entries"] if e["id"] == "LIT-101")["title"] = "Adaptive Sketches"
        self.assertTrue(any("primary source title mismatch" in problem
                            for problem in valid(changed, self.catalog)))

    def test_hyp103_six_primary_source_identities_and_old_cohorts(self):
        expected = {
            "LIT-103": "doi:10.4230/LIPIcs.MFCS.2024.46",
            "LIT-104": "doi:10.4230/LIPIcs.ESA.2020.2",
            "LIT-105": "doi:10.4230/LIPIcs.ITCS.2020.56",
            "LIT-106": "publisher:eccc:tr26-206",
            "LIT-107": "arxiv:2602.01042",
            "LIT-108": "doi:10.1016/S0304-3975(01)00144-X",
        }
        rows = {e["id"]: e for e in self.data["entries"]
                if "LIT-103" <= e["id"] <= "LIT-108"}
        self.assertEqual(set(rows), set(expected))
        for key, identity in expected.items():
            with self.subTest(primary=key):
                row = rows[key]
                self.assertEqual(row["identity"], identity)
                self.assertEqual(row["mentioned_in"], [{
                    "repo": "MATHLAB",
                    "path": "docs/research/HYP-103-G0-CERTIFICATE-REDUCTION.md",
                    "kind": "model_overlap",
                }])
                self.assertFalse(row["full_proof_verified"])
                self.assertFalse(row["independent_reproduction"])
        self.assertEqual(
            {f"LIT-{i:03d}" for i in range(1, 103)},
            {e["id"] for e in self.data["entries"] if e["id"] <= "LIT-102"})
        modified = copy.deepcopy(self.data)
        next(e for e in modified["entries"] if e["id"] == "LIT-106")["title"] = "Misattributed result"
        self.assertTrue(any("primary source title mismatch" in x
                            for x in valid(modified, self.catalog)))

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
        self.assertEqual(len({e["id"] for e in entries}), 108)
        tracks = {e["track"] for e in entries}
        self.assertEqual(len(tracks), 14)
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
