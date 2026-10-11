"""Fail-closed CI-OPT-001 scope tests: independent routing and git diff failures."""
import subprocess
import unittest
from unittest.mock import patch

from ci_scope import SHARDS, classify_changes, pull_request_changed_paths


class ResearchScopeTests(unittest.TestCase):
    def test_docs_only_does_not_consume_four_research_shards_or_index(self):
        actual = classify_changes(("README.md", "docs/CURRENT_STATE.md",
                                   "docs/research/HYP-105-B7-RESULT.md"))
        self.assertEqual(actual["mode"], "docs")
        self.assertFalse(any(actual[name] for name in (*SHARDS, "index")))

    def test_catalog_docs_get_catalog_checks_only(self):
        got = classify_changes(("docs/research/catalog/literature.json",
                                "docs/research/catalog/LITERATURE.md"))
        self.assertEqual(got["mode"], "scoped")
        self.assertTrue(got["catalog"])
        self.assertFalse(got["index"])
        self.assertFalse(any(got[n] for n in SHARDS if n != "catalog"))

    def test_scientific_family_routing(self):
        cases = (
            (("research/hyp105_a.py", "research/test_hyp105_a.py"),
             {"hyp_foundation", "hyp_census"}, False),
            (("research/uct005_model.py",), {"foundation"}, False),
            (("research/dag002_c2a.py",), {"foundation"}, False),
            (("research/index001_page_epochs.py",), {"foundation"}, True),
            (("research/hyp105_a.py", "research/index001_x.py"),
             {"foundation", "hyp_foundation", "hyp_census"}, True),
        )
        for paths, expected, index in cases:
            with self.subTest(paths=paths):
                got = classify_changes(paths)
                self.assertEqual({n for n in SHARDS if got[n]}, expected)
                self.assertEqual(got["index"], index)
                self.assertEqual(got["mode"], "scoped")

    def test_shared_unrecognized_workflow_policy_code_and_paths_force_full(self):
        unknown = (
            ("research/ci_scope.py",),
            ("research/test_ci_scope.py",),
            ("research/test_ci_research_shards.py",),
            (".github/workflows/research.yml",),
            (".github/workflows/index001-c5-page-epochs.yml",),
            ("research/unknown_new_primitive.py",),
            ("pyproject.toml",),
            ("docs/research/catalog/literature.json", "research/ci_scope.py"),
            ("research/hyp105_a.py", "research/other_module.py"),
            ("./docs/README.md",),
            ("docs/../README.md",),
            ("docs\\README.md",),
            ("/docs/README.md",),
            ("",),
            (),
        )
        for paths in unknown:
            with self.subTest(paths=paths):
                got = classify_changes(paths)
                self.assertEqual(got["mode"], "full")
                self.assertTrue(all(got[n] for n in (*SHARDS, "index")))

    def test_push_dispatch_and_unrecognized_event_never_scope(self):
        for event in ("push", "workflow_dispatch", "unexpected"):
            with self.subTest(event=event):
                got = classify_changes(("README.md",), event)
                self.assertEqual(got["mode"], "full")
                self.assertTrue(all(got[n] for n in (*SHARDS, "index")))

    def test_index_job_keeps_status_and_gates_both_scientific_steps(self):
        from pathlib import Path
        w = (Path(__file__).resolve().parents[1] /
             ".github/workflows/index001-c5-page-epochs.yml").read_text(
                 encoding="utf-8")
        self.assertIn("pull_request:", w)
        self.assertIn("workflow_dispatch:", w)
        self.assertIn("fetch-depth: 2", w)
        self.assertIn("python research/ci_scope.py", w)
        self.assertEqual(w.count("if: ${{ steps.scope.outputs.index == 'true' }}"), 3)
        self.assertIn("Report scoped INDEX exclusion", w)

    @patch("ci_scope.subprocess.check_output")
    def test_pr_merge_parent_diff_is_nul_delimited_and_no_shell(self, call):
        call.side_effect = [b"abc base head\n",
                            b"docs/a.md\x00research/hyp105_x.py\x00"]
        self.assertEqual(pull_request_changed_paths(),
                         ("docs/a.md", "research/hyp105_x.py"))
        self.assertEqual(call.call_args_list[0].args[0],
                         ["git", "rev-list", "--parents", "-n", "1", "HEAD"])
        self.assertEqual(call.call_args_list[1].args[0],
                         ["git", "diff", "--name-only", "-z", "HEAD^1", "HEAD"])
        self.assertTrue(all(isinstance(v.args[0], list) for v in call.call_args_list))

    @patch("ci_scope.subprocess.check_output", return_value=b"abc parent\n")
    def test_nonmerge_checkout_fails_not_silent_skip(self, ignored):
        with self.assertRaisesRegex(RuntimeError, "TWO parents"):
            pull_request_changed_paths()

    @patch("ci_scope.subprocess.check_output",
           side_effect=subprocess.CalledProcessError(128, "git"))
    def test_git_diff_failure_fails_not_silent_skip(self, ignored):
        with self.assertRaises(subprocess.CalledProcessError):
            pull_request_changed_paths()


if __name__ == "__main__":
    unittest.main()
