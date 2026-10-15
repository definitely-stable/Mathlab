"""RCP-COV-001: adversarial completeness and scientific non-promotion tests."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest

from research.rcp.claim_registry import RegistryError
from research.rcp.context_builder import seal_snapshot
from research.rcp.coverage_audit import build_coverage, markdown, main
from research.test_rcp_context import build


def fixture():
    data = deepcopy(build())
    for i, p in enumerate(data["inventory"]["open_prs"]):
        p["focus"] = p["number"] in (455, 466, 469, 470, 471, 475, 478, 481)
        p["title"] = (
            "HYP-105 #230 all-h ORIGINAL GF5 research D6 Q"
            if p["number"] == 475 else p["title"]
        )
        p["updated_at"] = "2026-10-15T06:00:%02dZ" % i
    return seal_snapshot(data)


class CoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample = fixture()

    def test_registered_coverage_exact_subset_not_completeness_claim(self):
        x = build_coverage(self.sample)
        self.assertEqual(x["registered_claim_count"], 7)
        self.assertEqual(x["registered_source_pr_count"], 5)
        self.assertEqual(x["open_hyp105_pr_count"], 8)
        self.assertEqual(x["registered_open_hyp105_source_pr_count"], 5)
        self.assertEqual(x["unregistered_open_hyp105_pr_count"], 3)
        self.assertFalse(x["coverage_is_exhaustive"])

    def test_scientific_root_open_but_not_proved(self):
        x = build_coverage(self.sample)
        self.assertEqual(x["root_issue_github_state"], "OPEN")
        self.assertEqual(x["mathematical_root_acceptance"],
                         "NOT_INFERRED_FROM_GITHUB_STATE_OR_CI")

    def test_even_closing_root_is_not_acceptance(self):
        x = deepcopy(self.sample)
        x["issues"]["root"]["state"] = "CLOSED"
        y = build_coverage(seal_snapshot(x))
        self.assertEqual(y["root_issue_github_state"], "CLOSED")
        self.assertIn("NOT_INFERRED", y["mathematical_root_acceptance"])

    def test_unregistered_open_pr_status_is_not_a_new_claim(self):
        x = build_coverage(self.sample)
        pr = next(p for p in x["coverage_queue"] if p["pr"] == 475)
        self.assertEqual(pr["proof_status"], "NOT_INSPECTED_BY_COVERAGE_AUDIT")
        self.assertEqual(pr["registered_claim_ids"], [])
        self.assertIn("ALL_H", pr["discovery_tags_unverified"])
        self.assertIn("GF5", pr["discovery_tags_unverified"])

    def test_absent_registered_source_not_asserted_merged(self):
        x = deepcopy(self.sample)
        x["inventory"]["open_prs"] = [
            p for p in x["inventory"]["open_prs"] if p["number"] != 455]
        x["inventory"]["open_pr_count"] -= 1
        d = build_coverage(seal_snapshot(x))
        missing = next(z for z in
                       d["registered_source_prs_absent_from_open_inventory"]
                       if z["pr"] == 455)
        self.assertEqual(missing["merge_status"],
                         "UNVERIFIED_DO_NOT_INFER_MERGED")

    def test_duplicate_open_pr_fails(self):
        x = deepcopy(self.sample)
        x["inventory"]["open_prs"].append(
            deepcopy(x["inventory"]["open_prs"][0]))
        x["inventory"]["open_pr_count"] += 1
        with self.assertRaisesRegex(RegistryError, "duplicate open PR"):
            build_coverage(seal_snapshot(x))

    def test_missing_evidence_fails(self):
        x = deepcopy(self.sample)
        x["research"]["evidence"] = [
            e for e in x["research"]["evidence"]
            if e["id"] != "HYP105-EV-LOCAL"]
        with self.assertRaisesRegex(RegistryError, "without evidence receipts"):
            build_coverage(seal_snapshot(x))

    def test_duplicate_claim_id_fails(self):
        x = deepcopy(self.sample)
        x["research"]["claims"].append(
            deepcopy(x["research"]["claims"][0]))
        with self.assertRaisesRegex(RegistryError, "invalid registered claim"):
            build_coverage(seal_snapshot(x))

    def test_incomplete_pr_inventory_fails(self):
        x = deepcopy(self.sample)
        x["inventory"]["complete_open_pr_pagination"] = False
        with self.assertRaisesRegex(RegistryError, "complete open-PR"):
            build_coverage(seal_snapshot(x))

    def test_no_artificial_coverage_queue_limit(self):
        x = deepcopy(self.sample)
        seed = deepcopy(x["inventory"]["open_prs"][0])
        for n in range(1000, 1205):
            p = deepcopy(seed)
            p["number"] = n
            p["title"] = "HYP-105 #230 queued ORIGINAL research all-h"
            p["focus"] = True
            p["head_sha"] = "%040x" % n
            p["updated_at"] = "2026-10-15T07:00:00Z"
            x["inventory"]["open_prs"].append(p)
            x["inventory"]["open_pr_count"] += 1
        out = build_coverage(seal_snapshot(x))
        self.assertEqual(out["unregistered_open_hyp105_pr_count"], 208)
        self.assertEqual(len(out["coverage_queue"]), 208)

    def test_sort_deterministic_and_updated_priority_not_novelty(self):
        a = build_coverage(self.sample)
        b = build_coverage(deepcopy(self.sample))
        self.assertEqual(a, b)
        times = [p["updated_at"] for p in a["coverage_queue"]]
        self.assertEqual(times, sorted(times, reverse=True))
        self.assertEqual(a["provenance"],
                         "OPEN_PR_TITLE_AND_PINNED_REGISTRY_METADATA_ONLY")

    def test_current_head_ci_not_math(self):
        x = deepcopy(self.sample)
        row = x["inventory"]["open_prs"][0]
        row["head_sha"] = "f" * 40
        row["checks"] = {"status": "SUCCESS", "verified_head": "f" * 40}
        out = build_coverage(seal_snapshot(x))
        self.assertEqual(out["mathematical_root_acceptance"],
                         "NOT_INFERRED_FROM_GITHUB_STATE_OR_CI")

    def test_readable_markdown_contains_total_queue(self):
        txt = markdown(build_coverage(self.sample))
        self.assertIn("## Unregistered open research PRs", txt)
        self.assertIn("3 open tagged research PRs", txt)
        self.assertIn("Absence does not establish a merge", txt)

    def test_offline_cli_exports_both(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            src = root / "snapshot.json"
            src.write_text(json.dumps(self.sample), encoding="utf-8")
            out = root / "out"
            self.assertEqual(main(["--snapshot", str(src),
                                   "--output", str(out)]), 0)
            content = json.loads((out / "coverage.json").read_text())
            self.assertEqual(content["registered_claim_count"], 7)
            self.assertIn("Coverage", (out / "coverage.md").read_text())

    def test_unsealed_corruption_rejected_by_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "bad.json"
            value = deepcopy(self.sample)
            value["inventory"]["open_pr_count"] += 1
            p.write_text(json.dumps(value), encoding="utf-8")
            with self.assertRaisesRegex(RegistryError, "digest mismatch"):
                main(["--snapshot", str(p),
                      "--output", str(Path(tmp) / "out")])


if __name__ == "__main__":
    unittest.main()
