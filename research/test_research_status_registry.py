"""Unit tests for local research status metadata."""
import copy
import json
import unittest

from research_status_registry import REGISTRY, DASHBOARD, render_dashboard, validate_registry


class RegistryTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(REGISTRY.read_text(encoding="utf-8"))

    def test_baseline_and_dashboard(self):
        validate_registry(self.data)
        self.assertEqual(DASHBOARD.read_text(encoding="utf-8"), render_dashboard(self.data))

    def test_duplicate_id(self):
        self.data["programs"].append(copy.deepcopy(self.data["programs"][0]))
        with self.assertRaises(ValueError):
            validate_registry(self.data)

    def test_dangling_parent(self):
        self.data["programs"][1]["parent"] = "UNKNOWN"
        with self.assertRaises(ValueError):
            validate_registry(self.data)

    def test_cycle(self):
        self.data["dependencies"].append({"from": "UCT-005-F1", "to": "UCT-005-COW"})
        with self.assertRaises(ValueError):
            validate_registry(self.data)

    def test_missing_file(self):
        self.data["programs"][0]["evidence"] = ["docs/research/NONEXISTENT.md"]
        with self.assertRaises(ValueError):
            validate_registry(self.data)

    def test_root_status(self):
        self.data["programs"][0]["scientific_status"] = "CLASSICAL_RESTRICTED"
        with self.assertRaises(ValueError):
            validate_registry(self.data)

    def test_unproved_transfer(self):
        self.data["typed_edges"][0]["status"] = "CLASSICAL_RESTRICTED"
        with self.assertRaises(ValueError):
            validate_registry(self.data)

    def test_ci_without_exact_run(self):
        self.data["programs"][0]["ci"]["status"] = "SUCCESS"
        with self.assertRaises(ValueError):
            validate_registry(self.data)

    def test_f1_model(self):
        self.data["programs"][1]["model_id"] = "invalid-model"
        with self.assertRaises(ValueError):
            validate_registry(self.data)

    def test_allocator_owner_drift(self):
        item = next(x for x in self.data["programs"]
                    if x["id"] == "UCT-005-ALLOCATOR")
        item["owner_issue"] = 244
        with self.assertRaisesRegex(ValueError, "owner, parent"):
            validate_registry(self.data)

    def test_cow_issue_closed_scoped(self):
        item = next(x for x in self.data["programs"]
                    if x["id"] == "UCT-005-COW")
        self.assertEqual(item["workflow_status"], "CLOSED_ISSUE")
        self.assertEqual(item["scientific_status"], "MODEL_ONLY")
        item["workflow_status"] = "OPEN_ISSUE"
        with self.assertRaisesRegex(ValueError, "scoped completed issue"):
            validate_registry(self.data)

    def test_allocator_remains_scoped_closed(self):
        item = next(x for x in self.data["programs"]
                    if x["id"] == "UCT-005-ALLOCATOR")
        item["scientific_status"] = "OPEN_UNPROVED"
        with self.assertRaisesRegex(ValueError, "owner, parent or scientific status"):
            validate_registry(self.data)

    def test_pin_trust_false_promotion(self):
        item = next(x for x in self.data["programs"]
                    if x["id"] == "UCT-005-PIN-TRUST")
        item["scientific_status"] = "MODEL_ONLY"
        with self.assertRaisesRegex(ValueError, "owner, parent"):
            validate_registry(self.data)

    def test_unknown_fields(self):
        self.data["programs"][0]["extra"] = True
        with self.assertRaises(ValueError):
            validate_registry(self.data)


if __name__ == "__main__":
    unittest.main()
