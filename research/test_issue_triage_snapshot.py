"""Fail-closed regression tests for the dated 55-issue snapshot."""
import copy
import json
import unittest

from issue_triage_snapshot import SNAPSHOT, DASHBOARD, PLAN, render, validate, validate_plan


class IssueTriageSnapshotTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(SNAPSHOT.read_text(encoding="utf-8"))

    def test_full_snapshot_and_generated_dashboard(self):
        validate(self.data)
        self.assertEqual(DASHBOARD.read_text(encoding="utf-8"),
                         render(self.data))

    def test_ranked_execution_plan(self):
        validate_plan(self.data, PLAN.read_text(encoding="utf-8"))

    def test_false_backlog_score(self):
        plan = PLAN.read_text(encoding="utf-8")
        self.assertIn("5×5=25", plan)
        with self.assertRaisesRegex(ValueError, "impact-times-tractability"):
            validate_plan(self.data, plan.replace("5×5=25", "5×5=24", 1))

    def test_bad_backlog_order(self):
        plan = PLAN.read_text(encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "ranks must be"):
            validate_plan(self.data, plan.replace("| 1 | P0 |", "| 99 | P0 |", 1)
                          .replace("| 99 | P0 |", "| 2 | P0 |", 1))

    def test_coverage_count_mismatch(self):
        self.data["issue_count"] -= 1
        with self.assertRaisesRegex(ValueError, "count"):
            validate(self.data)

    def test_duplicate_issue(self):
        self.data["issues"].append(copy.deepcopy(self.data["issues"][-1]))
        self.data["issue_count"] += 1
        with self.assertRaises(ValueError):
            validate(self.data)

    def test_dangling_parent(self):
        item = next(x for x in self.data["issues"] if x["number"] == 223)
        item["parent_issue"] = 999999
        with self.assertRaisesRegex(ValueError, "missing/self parent"):
            validate(self.data)

    def test_cycle(self):
        root = next(x for x in self.data["issues"] if x["number"] == 105)
        root["parent_issue"] = 223
        with self.assertRaisesRegex(ValueError, "cycle"):
            validate(self.data)

    def test_false_root_proof_promotion(self):
        root = next(x for x in self.data["issues"] if x["number"] == 105)
        root["acceptance_gate"] = "Proof established; close and promote now."
        with self.assertRaisesRegex(ValueError, "root proof status"):
            validate(self.data)

    def test_bad_issue_url(self):
        self.data["issues"][0]["url"] = "https://example.org/issues/1"
        with self.assertRaisesRegex(ValueError, "incorrect issue URL"):
            validate(self.data)

    def test_false_live_issue_state(self):
        self.data["issues"][0]["state_at_snapshot"] = "CLOSED"
        with self.assertRaisesRegex(ValueError, "not-open-at-snapshot"):
            validate(self.data)

    def test_wrong_track(self):
        self.data["issues"][0]["family"] = "UCT-005"
        with self.assertRaisesRegex(ValueError, "misclassified"):
            validate(self.data)

    def test_bad_action(self):
        self.data["issues"][0]["triage_action"] = "CLOSE_AUTOMATICALLY"
        with self.assertRaisesRegex(ValueError, "invalid triage action"):
            validate(self.data)

    def test_missing_gate(self):
        self.data["issues"][0]["acceptance_gate"] = ""
        with self.assertRaisesRegex(ValueError, "acceptance gate"):
            validate(self.data)


if __name__ == "__main__":
    unittest.main()
