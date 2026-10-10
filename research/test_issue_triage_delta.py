"""Negative regression controls for GitHub issue delta and scope boundaries."""
import json
import unittest
from issue_triage_snapshot import SNAPSHOT
from issue_triage_delta import DELTA, validate_delta, audit

class IssueTriageDeltaTests(unittest.TestCase):
    def setUp(self):
        self.archive = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
        self.delta = json.loads(DELTA.read_text(encoding="utf-8"))

    def test_dated_delta_and_documents(self):
        audit()

    def test_mismatched_issue_count(self):
        self.delta["captured_open_issue_count"] += 1
        with self.assertRaisesRegex(ValueError, "captured open issue"):
            validate_delta(self.delta, self.archive)

    def test_duplicate_issue_id(self):
        self.delta["captured_open_issue_ids"].append(self.delta["captured_open_issue_ids"][-1])
        with self.assertRaisesRegex(ValueError, "captured open issue"):
            validate_delta(self.delta, self.archive)

    def test_removed_added_issue(self):
        self.delta["added"].pop()
        with self.assertRaisesRegex(ValueError, "added issue set"):
            validate_delta(self.delta, self.archive)

    def test_removed_closed_issue(self):
        self.delta["closed"].pop()
        with self.assertRaisesRegex(ValueError, "closed issue set"):
            validate_delta(self.delta, self.archive)

    def test_false_theorem_promotion(self):
        self.delta["scientific_root"]["state"] = "PROVED"
        with self.assertRaisesRegex(ValueError, "root promotion"):
            validate_delta(self.delta, self.archive)

    def test_external_issue_cross_repo_transfer(self):
        next(x for x in self.delta["added"] if x["number"] == 289)["category"] = "UCT-005"
        with self.assertRaisesRegex(ValueError, "cross-repository"):
            validate_delta(self.delta, self.archive)

    def test_pr_duplicates(self):
        self.delta["open_pr_ids"].append(self.delta["open_pr_ids"][-1])
        self.delta["open_pr_count"] += 1
        with self.assertRaisesRegex(ValueError, "open PR IDs"):
            validate_delta(self.delta, self.archive)

    def test_fabricated_live_claim(self):
        self.delta["warning"] = "Always live and proved"
        with self.assertRaisesRegex(ValueError, "live/theorem"):
            validate_delta(self.delta, self.archive)

    def test_untracked_extra_closed_issue(self):
        self.delta["closed"].append({
            "number": 123456, "title": "Invented closed issue",
            "url": "https://github.com/definitely-stable/Mathlab/issues/123456"
        })
        with self.assertRaisesRegex(ValueError, "closed issue set"):
            validate_delta(self.delta, self.archive)

if __name__ == "__main__":
    unittest.main()
