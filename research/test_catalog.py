"""RESEARCH-INDEX-001: offline index, provenance and falsification tests."""
import copy
import json
import unittest

from catalog import DATA, INDEX, REPOS, check, render


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(DATA.read_text(encoding="utf-8"))

    def test_full_catalog_valid(self):
        self.assertEqual(check(self.data), [])

    def test_all_four_repositories_have_curated_entries(self):
        observed = {e["repository"] for e in self.data["entries"]}
        self.assertEqual(observed, set(REPOS))
        self.assertGreaterEqual(len(self.data["entries"]), 20)

    def test_generated_readable_index_is_byte_for_byte_deterministic(self):
        self.assertEqual(render(self.data), INDEX.read_text(encoding="utf-8"))

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
