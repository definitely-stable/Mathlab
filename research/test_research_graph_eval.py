"""Regression tests for the fixed Mathlab bilingual retrieval quality fixtures."""
import copy
import json
import unittest

from research_graph import ingest
from research_graph_eval import FIXTURES, evaluate


class RetrievalQualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = ingest()
        cls.data = json.loads(FIXTURES.read_text(encoding="utf-8"))

    def test_bilingual_fixtures_recall(self):
        result = evaluate(self.data, self.graph)
        self.assertTrue(result["passed"], [
            (x["query"], x["expected"], x["ranked_ids"])
            for x in result["cases"] if x["recall_at_k"] < 1.0])
        self.assertEqual(result["mean_recall_at_k"], 1.0)

    def test_no_unknown_source_ids(self):
        fixture = copy.deepcopy(self.data)
        fixture["queries"][0]["relevant"] = ["T:PROVED_BY_HALLUCINATION"]
        with self.assertRaisesRegex(ValueError, "unknown canonical ID"):
            evaluate(fixture, self.graph)

    def test_fixtures_no_ambiguous_duplicates(self):
        fixture = copy.deepcopy(self.data)
        fixture["queries"].append(copy.deepcopy(fixture["queries"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate query-kind"):
            evaluate(fixture, self.graph)

    def test_invalid_recall_k_fails_closed(self):
        fixture = copy.deepcopy(self.data)
        fixture["queries"][0]["k"] = 0
        with self.assertRaisesRegex(ValueError, "invalid recall cutoff"):
            evaluate(fixture, self.graph)


if __name__ == "__main__":
    unittest.main()
