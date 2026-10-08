"""Research catalog: offline provenance, discovery and falsification checks."""
import copy
import json
import unittest

from catalog import DATA, INDEX, THEMES, REPOS, check, render, render_themes


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(DATA.read_text(encoding="utf-8"))

    def test_full_catalog_valid(self):
        self.assertEqual(check(self.data), [])

    def test_all_four_repositories_have_curated_entries(self):
        observed = {e["repository"] for e in self.data["entries"]}
        self.assertEqual(observed, set(REPOS))
        self.assertGreaterEqual(len(self.data["entries"]), 49)

    def test_generated_readable_index_is_byte_for_byte_deterministic(self):
        self.assertEqual(render(self.data), INDEX.read_text(encoding="utf-8"))

    def test_generated_theme_index_is_deterministic(self):
        self.assertEqual(render_themes(self.data),
                         THEMES.read_text(encoding="utf-8"))
        self.assertIn("[ML-008](INDEX.md#ml-008)", render_themes(self.data))
        self.assertIn("[OM-132](INDEX.md#om-132)", render_themes(self.data))

    def test_expanded_import_counts_and_mathlab_revision(self):
        counts = {key: sum(e["repository"] == key for e in self.data["entries"])
                  for key in REPOS}
        self.assertGreaterEqual(counts["MATHLAB"], 9)
        self.assertGreaterEqual(counts["DELSK"], 12)
        self.assertGreaterEqual(counts["DELTAMETER"], 14)
        self.assertGreaterEqual(counts["OPENAI_MATH"], 14)
        self.assertEqual(
            self.data["repositories"]["MATHLAB"]["sha"],
            "0c41da53d39aaeecc4f736ee063cc9f8bc4ff1d7")

    def test_external_imports_remain_unverified_author_claims(self):
        for e in self.data["entries"]:
            if e["repository"] == "OPENAI_MATH":
                self.assertIn(e["status"],
                              {"EXTERNAL_CATALOG", "EXTERNAL_MANUSCRIPT_CLAIM"})
                self.assertEqual(e["verification"], "source_catalog")

    def test_new_g2b_evidence_is_not_an_asymptotic_theorem(self):
        g2b = next(e for e in self.data["entries"]
                   if e["id"] == "ML-008")
        self.assertEqual(g2b["status"], "EXACT_NUMERICAL")
        self.assertIn("10–15", g2b["summary_ru"])

    def test_all_source_revision_pins_match_repository_snapshots(self):
        for e in self.data["entries"]:
            meta = self.data["repositories"][e["repository"]]
            self.assertEqual(e["source"]["revision"], meta["sha"])
            self.assertIn("/blob/" + meta["sha"] + "/", e["source"]["permalink"])

    def test_topic_index_contains_distinct_source_and_status(self):
        topic_page = render_themes(self.data)
        self.assertIn("EXTERNAL_MANUSCRIPT_CLAIM", topic_page)
        self.assertIn("RESEARCH_DECISION", topic_page)
        self.assertIn("MATHLAB", topic_page)
        self.assertIn("DELTAMETER", topic_page)

    def test_duplicate_id_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["entries"][1]["id"] = data["entries"][0]["id"]
        self.assertTrue(any("duplicate ID" in e for e in check(data)))

    def test_dangling_link_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["entries"][0]["related"].append(
            {"id": "ML-999", "relation": "related"}
        )
        self.assertTrue(any("broken relationship" in e for e in check(data)))

    def test_branch_link_cannot_replace_pinned_evidence(self):
        data = copy.deepcopy(self.data)
        data["entries"][0]["source"]["permalink"] = (
            data["entries"][0]["source"]["latest"]
        )
        self.assertTrue(any("permalink not revision-pinned" in e
                            for e in check(data)))

    def test_external_manuscript_status_not_promoted(self):
        data = copy.deepcopy(self.data)
        external = next(e for e in data["entries"]
                        if e["status"] == "EXTERNAL_MANUSCRIPT_CLAIM")
        external["status"] = "DERIVED_RESULT"
        self.assertTrue(any("imported claim improperly classified" in e
                            for e in check(data)))

    def test_cross_repo_related_backlinks_emitted(self):
        page = render(self.data)
        self.assertIn("**Обратные ссылки ←**", page)
        self.assertIn("[OM-099](#om-099)", page)
        self.assertIn("[ML-006](#ml-006)", page)

    def test_source_revision_mismatch_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["entries"][0]["source"]["revision"] = "0" * 40
        self.assertTrue(any("revision mismatch" in e for e in check(data)))


if __name__ == "__main__":
    unittest.main()
