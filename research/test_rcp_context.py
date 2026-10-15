"""Independent adversarial tests for RCP-001-D live context and semantic delta."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from research.rcp.context_builder import (
    build_snapshot, capture_github, digest, format_levels, read_snapshot,
    seal_snapshot, write_context, issue_view, run
)
from research.rcp.context_delta import compare_snapshots, format_delta, main as delta_main
from research.rcp.claim_registry import RegistryError, REPO
from research.rcp.github_inventory import (
    GitHubAPI, InventoryError, build_inventory
)
from research.test_rcp_inventory import pr

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "research/rcp/hyp105"
MAIN = "a" * 40
WHEN = "2026-10-15T04:45:00+00:00"


def pull(n, base="main", bsha=MAIN, **kwargs):
    return pr(n, "test_" + str(n), base=base, bsha=bsha, **kwargs)


def inv(rows=None, when=WHEN):
    if rows is None:
        rows = [pull(n) for n in (455, 466, 469, 470, 471, 475, 478, 481)]
    return build_inventory(REPO, rows, MAIN, when)


def issues(root="OPEN", operations="OPEN"):
    return {
        "root": {"number": 230, "state": root,
                 "url": "https://github.com/" + REPO + "/issues/230",
                 "updated_at": WHEN, "title": "HYP-105"},
        "operations": {"number": 474, "state": operations,
                       "url": "https://github.com/" + REPO + "/issues/474",
                       "updated_at": WHEN, "title": "RCP-001"},
    }


def build(rows=None, when=WHEN):
    return build_snapshot(REGISTRY, ROOT, inv(rows=rows, when=when),
                          issues(), origin="REPLAYED_INPUT",
                          checkout="b" * 40)


def altered(s, change):
    r = deepcopy(s)
    change(r)
    return seal_snapshot(r)


def kinds(delta, group="operational_events"):
    return [v["kind"] for v in delta[group]]


class ContextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.snapshot = build()

    def test_complete_registry_no_arbitrary_limit(self):
        x = self.snapshot
        self.assertGreaterEqual(len(x["research"]["claims"]), 7)
        self.assertGreaterEqual(len(x["research"]["evidence"]), 5)
        self.assertEqual(len(x["research"]["no_go"]), 5)
        self.assertGreaterEqual(len(x["research"]["escrow"]), 17)
        self.assertEqual(x["inventory"]["open_pr_count"], 8)

    def test_live_root_state_is_separate_from_mathematical_status(self):
        r = altered(self.snapshot, lambda x:
                    x["issues"]["root"].update(state="CLOSED"))
        l0 = format_levels(r)["L0.md"]
        self.assertIn("GitHub CLOSED", l0)
        self.assertIn("NOT ESTABLISHED BY THIS REGISTRY", l0)

    def test_registered_claims_preserve_original_proof_sha(self):
        x = self.snapshot
        c = next(c for c in x["research"]["claims"] if
                 c["id"] == "HYP105-AA4O-QUINTIC-IDENTITY")
        self.assertEqual(c["source"]["commit"],
                         "b086566d8be17307b102e7bd89d28d4167af86a6")
        self.assertNotEqual(c["source_pr_current"]["head"], c["source"]["commit"])
        self.assertEqual(c["source_pr_current"]["checks"]["status"],
                         "NOT_INSPECTED")

    def test_three_levels_complete_and_separate(self):
        x = format_levels(self.snapshot)
        self.assertEqual(set(x), {"L0.md", "L1.md", "L2.md"})
        self.assertIn("HYP105-NG-SWAP-OPTIMUM", x["L0.md"])
        self.assertIn("Ordered quantifiers", x["L1.md"])
        self.assertIn("SHA256", x["L2.md"])
        self.assertIn("source", x["L2.md"].lower())

    def test_exact_same_snapshot_render_is_deterministic(self):
        self.assertEqual(format_levels(self.snapshot),
                         format_levels(deepcopy(self.snapshot)))

    def test_seal_and_read_snapshot(self):
        with tempfile.TemporaryDirectory() as tmp:
            write_context(self.snapshot, Path(tmp))
            v = read_snapshot(Path(tmp) / "snapshot.json")
            self.assertEqual(v, self.snapshot)
            for n in ("L0.md", "L1.md", "L2.md"):
                self.assertTrue((Path(tmp) / n).is_file())

    def test_tampered_stored_snapshot_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            write_context(self.snapshot, Path(tmp))
            path = Path(tmp) / "snapshot.json"
            value = json.loads(path.read_text(encoding="utf-8"))
            value["inventory"]["main_head"] = "0" * 40
            path.write_text(json.dumps(value), encoding="utf-8")
            with self.assertRaisesRegex(RegistryError, "digest mismatch"):
                read_snapshot(path)

    def test_wrong_program_snapshot_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "bad.json"
            s = altered(self.snapshot, lambda d:
                        d.update(program="OTHER"))
            p.write_text(json.dumps(s), encoding="utf-8")
            with self.assertRaisesRegex(RegistryError, "different research program"):
                read_snapshot(p)

    def test_offline_replay_does_not_require_github(self):
        with tempfile.TemporaryDirectory() as tmp:
            src, out = Path(tmp) / "snapshot.json", Path(tmp) / "out"
            src.write_text(json.dumps(self.snapshot), encoding="utf-8")
            self.assertEqual(run(["--output", str(out),
                                  "--snapshot-in", str(src)]), 0)
            self.assertEqual(read_snapshot(out / "snapshot.json"), self.snapshot)

    def test_live_check_rejected_when_replaying_old_snapshot(self):
        with tempfile.TemporaryDirectory() as tmp:
            src, out = Path(tmp) / "snapshot.json", Path(tmp) / "out"
            src.write_text(json.dumps(self.snapshot), encoding="utf-8")
            with self.assertRaisesRegex(RegistryError, "cannot inspect live checks"):
                run(["--output", str(out), "--snapshot-in", str(src),
                     "--check-pr", "471"])

    def test_wrong_source_repo_refused(self):
        bad = inv()
        bad["repo"] = "bad/fork"
        with self.assertRaisesRegex(RegistryError, "wrong-repository"):
            build_snapshot(REGISTRY, ROOT, bad, issues(), origin="REPLAYED_INPUT")

    def test_unknown_issue_state_not_interpreted_as_open(self):
        bad = issues()
        bad["root"]["state"] = "UNKNOWN"
        with self.assertRaisesRegex(RegistryError, "unverified root"):
            build_snapshot(REGISTRY, ROOT, inv(), bad, origin="REPLAYED_INPUT")

    def test_bad_issue_url_rejected_by_issue_fetch(self):
        with self.assertRaisesRegex(RegistryError, "invalid issue URL"):
            issue_view({"number": 230, "state": "open",
                        "html_url": "https://evil.invalid/issues/230"}, 230)

    def test_api_main_changes_mid_scan_fails_closed(self):
        rows = [pull(455)]
        class Fake:
            def __init__(self):
                self.n = 0
            def main_head(self):
                self.n += 1
                return MAIN if self.n == 1 else "c" * 40
            def open_pulls(self):
                return rows
            def get(self, url):
                n = int(url.rsplit("/", 1)[-1])
                return ({
                    "number": n, "state": "open",
                    "html_url": "https://github.com/" + REPO +
                                "/issues/" + str(n)
                }, "")
            def checks(self, sha):
                return {"status": "UNKNOWN", "verified_head": sha}
        with self.assertRaisesRegex(InventoryError, "main moved"):
            capture_github(Fake(), set(), set(), WHEN)

    def test_requested_closed_pr_checks_rejected(self):
        class Fake:
            def main_head(self): return MAIN
            def open_pulls(self): return [pull(455)]
        with self.assertRaisesRegex(RegistryError, "not open"):
            capture_github(Fake(), {999}, set(), WHEN)

    def test_check_claim_prs_only_inspects_open_claims(self):
        class Fake:
            def main_head(self): return MAIN
            def open_pulls(self): return [pull(455)]
            def get(self, url):
                n = int(url.rsplit("/", 1)[-1])
                return ({"number": n, "state": "open",
                         "html_url": "https://github.com/" + REPO +
                                     "/issues/" + str(n)}, "")
            def checks(self, sha):
                return {"status": "SUCCESS", "verified_head": sha}
        scan, state = capture_github(Fake(), set(), {455, 469}, WHEN)
        self.assertEqual(scan["open_prs"][0]["checks"]["verified_head"],
                         scan["open_prs"][0]["head_sha"])
        self.assertEqual(state["root"]["state"], "OPEN")

    def test_very_large_pr_inventory_not_artificially_capped(self):
        rows = [pull(n) for n in range(1, 211)]
        x = inv(rows)
        self.assertEqual(x["open_pr_count"], 210)
        r = build_snapshot(REGISTRY, ROOT, x, issues(),
                           origin="REPLAYED_INPUT")
        self.assertEqual(r["inventory"]["open_pr_count"], 210)


class DeltaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = build()

    def test_observation_time_change_no_fake_theorem(self):
        x = altered(self.a, lambda v: v.update(
            observed_at_utc="2026-10-15T05:20:00Z"))
        d = compare_snapshots(self.a, x)
        self.assertEqual(d["scientific_registry_event_count"], 0)
        self.assertEqual(d["operational_event_count"], 0)

    def test_changed_pr_head_requires_new_ci(self):
        def f(s):
            p = next(x for x in s["inventory"]["open_prs"] if x["number"] == 471)
            p["head_sha"] = "c" * 40
            p["checks"] = {"status": "NOT_INSPECTED"}
        x = altered(self.a, f)
        k = kinds(compare_snapshots(self.a, x))
        self.assertIn("PR_HEAD_SHA_CHANGED", k)
        self.assertIn("CI_NEW_HEAD_REQUIRES_RECHECK", k)
        self.assertNotIn("CI_OBSERVATION_CHANGED", k)

    def test_same_head_ci_observation_change(self):
        def f(s):
            p = s["inventory"]["open_prs"][0]
            p["checks"] = {"status": "SUCCESS",
                           "verified_head": p["head_sha"]}
        d = compare_snapshots(self.a, altered(self.a, f))
        self.assertIn("CI_OBSERVATION_CHANGED", kinds(d))
        self.assertNotIn("CI_NEW_HEAD_REQUIRES_RECHECK", kinds(d))

    def test_disappearing_pr_does_not_imply_merge(self):
        def f(s):
            s["inventory"]["open_prs"] = [
                p for p in s["inventory"]["open_prs"] if p["number"] != 471
            ]
            s["inventory"]["open_pr_count"] -= 1
        d = compare_snapshots(self.a, altered(self.a, f))
        events = [e for e in d["operational_events"]
                  if e["kind"] == "PR_NO_LONGER_IN_OPEN_INVENTORY"]
        self.assertEqual(len(events), 1)
        self.assertIn("unverified", events[0]["warning"])
        self.assertNotIn("PR_MERGED", kinds(d))

    def test_added_pr_event_not_new_theorem(self):
        def f(s):
            p = deepcopy(s["inventory"]["open_prs"][0])
            p["number"] = 900
            s["inventory"]["open_prs"].append(p)
            s["inventory"]["open_pr_count"] += 1
        d = compare_snapshots(self.a, altered(self.a, f))
        self.assertIn("PR_ADDED_TO_OPEN_INVENTORY", kinds(d))
        self.assertEqual(d["scientific_registry_event_count"], 0)

    def test_issue_close_does_not_mark_root_proof(self):
        d = compare_snapshots(self.a, altered(self.a,
            lambda x: x["issues"]["root"].update(state="CLOSED")))
        self.assertIn("ISSUE_STATE_CHANGED", kinds(d))
        self.assertEqual(d["scientific_registry_event_count"], 0)

    def test_scientific_statement_and_quantifier_changes(self):
        def f(s):
            c = s["research"]["claims"][0]
            c["statement"] += " altered"
            c["quantifiers"][0]["domain"] = "unsupported"
            c["fingerprint"] = digest(c)
        d = compare_snapshots(self.a, altered(self.a, f))
        e = [x for x in d["scientific_registry_events"] if x["kind"] ==
             "CLAIM_SEMANTICS_CHANGED"]
        self.assertEqual(len(e), 1)
        self.assertIn("statement", e[0]["changed_fields"])
        self.assertIn("quantifiers", e[0]["changed_fields"])

    def test_claim_proof_commit_changed_separately(self):
        def f(s):
            c = s["research"]["claims"][0]
            c["source"]["commit"] = "f" * 40
            c["fingerprint"] = digest(c)
        d = compare_snapshots(self.a, altered(self.a, f))
        self.assertEqual([e["kind"] for e in d["scientific_registry_events"]],
                         ["CLAIM_SEMANTICS_CHANGED"])
        self.assertIn("source",
                      d["scientific_registry_events"][0]["changed_fields"])

    def test_added_no_go_record_is_scientific_event(self):
        def f(s):
            x = deepcopy(s["research"]["no_go"][0])
            x["id"] = "HYP105-NG-NEW"
            x["fingerprint"] = digest(x)
            s["research"]["no_go"].append(x)
        d = compare_snapshots(self.a, altered(self.a, f))
        self.assertIn("NO_GO_ADDED", kinds(d, "scientific_registry_events"))

    def test_receipt_content_changed(self):
        def f(s):
            s["research"]["evidence"][0]["fingerprint"] = "d" * 64
        d = compare_snapshots(self.a, altered(self.a, f))
        self.assertIn("EVIDENCE_CONTENT_CHANGED",
                      kinds(d, "scientific_registry_events"))

    def test_model_definition_modified(self):
        def f(s):
            s["research"]["models"]["MODEL-GQ-ORIGINAL"]["definition"] += " modified"
        d = compare_snapshots(self.a, altered(self.a, f))
        self.assertIn("MODEL_DEFINITION_CHANGED",
                      kinds(d, "scientific_registry_events"))

    def test_archive_tamper_is_scientific_integrity_event(self):
        def f(s):
            s["research"]["escrow"][0]["sha256"] = "0" * 64
        d = compare_snapshots(self.a, altered(self.a, f))
        self.assertIn("ESCROW_CONTENT_CHANGED",
                      kinds(d, "scientific_registry_events"))

    def test_cross_issue_or_program_delta_rejected(self):
        altered_ = altered(self.a, lambda s: s.update(root_issue=999))
        with self.assertRaisesRegex(RegistryError, "cross-program"):
            compare_snapshots(self.a, altered_)

    def test_json_and_markdown_offline_delta_reproducible(self):
        with tempfile.TemporaryDirectory() as tmp:
            a, b, output = [Path(tmp) / p for p in ("a.json", "b.json", "diff")]
            a.write_text(json.dumps(self.a), encoding="utf-8")
            b.write_text(json.dumps(altered(self.a, lambda s:
                         s["issues"]["operations"].update(state="CLOSED"))),
                         encoding="utf-8")
            self.assertEqual(delta_main(["--before", str(a), "--after", str(b),
                                         "--output", str(output)]), 0)
            data = json.loads((output / "delta.json").read_text(encoding="utf-8"))
            self.assertEqual(data["operational_event_count"], 1)
            self.assertIn("ISSUE_STATE_CHANGED",
                          (output / "delta.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
