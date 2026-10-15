"""Offline adversarial coverage for RCP-001-A; no network credentials required."""
from __future__ import annotations
import json
import tempfile
import unittest
from unittest.mock import patch

from research.rcp.github_inventory import (
    GitHubAPI, InventoryError, build_inventory, markdown
)

REPO = "definitely-stable/Mathlab"
MAIN = "a" * 40

def pr(n, head, base="main", *, hsha=None, bsha=None, title=None,
       head_repo=REPO, base_repo=REPO, body=""):
    return {
        "number": n, "state": "open", "draft": True,
        "title": title or "HYP-105 #230 slice %d" % n, "body": body,
        "html_url": "https://github.com/definitely-stable/Mathlab/pull/%d" % n,
        "updated_at": "2026-10-15T00:00:00Z",
        "head": {"sha": hsha or format(n, "040x"), "ref": head,
                 "repo": {"full_name": head_repo}},
        "base": {"sha": bsha or MAIN, "ref": base,
                 "repo": {"full_name": base_repo}},
    }

def run(rows, **kwargs):
    return build_inventory(REPO, rows, MAIN, "2026-10-15T00:00:00Z", **kwargs)

class InventoryTests(unittest.TestCase):
    def test_stack_and_sibling_ancestry(self):
        p1 = pr(1, "alpha")
        p2 = pr(2, "beta", base="alpha", bsha=p1["head"]["sha"])
        p3 = pr(3, "gamma", base="alpha", bsha=p1["head"]["sha"])
        p4 = pr(4, "delta", base="beta", bsha=p2["head"]["sha"])
        d = run([p4, p3, p1, p2])
        by = {r["number"]: r for r in d["open_prs"]}
        self.assertEqual([by[n]["parent_pr"] for n in (1, 2, 3, 4)],
                         [None, 1, 1, 2])
        self.assertEqual([by[n]["depth"] for n in (1, 2, 3, 4)],
                         [0, 1, 1, 2])
        self.assertEqual(d["max_stack_depth"], 2)
        self.assertEqual(d["diagnostics"], [])
        self.assertEqual(by[4]["checks"]["status"], "NOT_INSPECTED")

    def test_stale_parent_sha_detected_not_passed(self):
        d = run([pr(1, "a"), pr(2, "b", base="a", bsha="f" * 40)])
        self.assertEqual(d["diagnostics"][0]["kind"], "PARENT_BASE_SHA_DRIFT")
        self.assertFalse(d["open_prs"][1]["parent_sha_match"])

    def test_main_drift_flag(self):
        d = run([pr(1, "alpha", bsha="e" * 40)])
        self.assertEqual(d["diagnostics"][0]["kind"], "MAIN_BASE_SHA_DRIFT")

    def test_unresolved_branch_not_mistaken_for_main(self):
        d = run([pr(1, "a", base="historical-merged-branch")])
        self.assertEqual(d["diagnostics"][0]["kind"], "UNRESOLVED_BASE")

    def test_ambiguous_parent(self):
        d = run([pr(1, "shared"), pr(2, "shared"), pr(3, "child", base="shared")])
        self.assertEqual(d["diagnostics"][0]["kind"], "AMBIGUOUS_PARENT")
        self.assertIsNone(d["open_prs"][2]["parent_pr"])

    def test_fork_name_collision_not_parent(self):
        x = pr(1, "same", head_repo="someone/fork")
        y = pr(2, "child", base="same")
        d = run([x, y])
        self.assertIsNone(d["open_prs"][1]["parent_pr"])

    def test_cycle_rejected(self):
        with self.assertRaisesRegex(InventoryError, "cycle"):
            run([pr(1, "a", base="b"), pr(2, "b", base="a")])

    def test_bad_sha_rejected(self):
        with self.assertRaisesRegex(InventoryError, "head sha"):
            run([pr(1, "x", hsha="short")])

    def test_missing_selected_check_rejected(self):
        with self.assertRaisesRegex(InventoryError, "missing PR"):
            run([pr(1, "a")], check_prs={999})

    def test_focus_ancestor(self):
        a = pr(1, "a", title="Foundation")
        b = pr(2, "b", base="a", bsha=a["head"]["sha"])
        d = run([a, b])
        self.assertEqual(d["hyp105_direct_count"], 1)
        self.assertEqual(d["hyp105_with_ancestors_count"], 2)
        self.assertIn("Foundation", markdown(d))

    def test_stable_output_independent_of_api_order(self):
        x, y = pr(7, "a"), pr(8, "b")
        d1, d2 = run([x, y]), run([y, x])
        self.assertEqual(json.dumps(d1, sort_keys=True), json.dumps(d2, sort_keys=True))
        self.assertEqual(markdown(d1), markdown(d2))

class FakeAPI:
    def __init__(self, mapping):
        self.mapping = mapping
    def __call__(self, url):
        if url not in self.mapping:
            raise AssertionError("unexpected url " + url)
        return self.mapping[url]

class PaginationTests(unittest.TestCase):
    def test_two_pages_complete_with_link(self):
        root = "https://api.github.com/repos/" + REPO + "/pulls"
        url1, url2 = root + "?per_page=100", root + "?page=2&per_page=100"
        fetch = FakeAPI({
            url1: ([pr(i, "b%d" % i) for i in range(1, 101)],
                   '<' + url2 + '>; rel="next", <unused>; rel="last"'),
            url2: ([pr(101, "b101")], ""),
        })
        api = GitHubAPI(REPO, get=fetch)
        self.assertEqual(len(api.open_pulls()), 101)
        self.assertEqual(api.calls, 2)

    def test_duplicate_across_pages_fails_closed(self):
        root = "https://api.github.com/repos/" + REPO + "/pulls"
        u1, u2 = root + "?per_page=100", root + "?page=2"
        api = GitHubAPI(REPO, get=FakeAPI({
            u1: ([pr(1, "a")], '<' + u2 + '>; rel="next"'),
            u2: ([pr(1, "a")], ""),
        }))
        with self.assertRaisesRegex(InventoryError, "duplicate"):
            api.open_pulls()

    def test_untrusted_pagination_link_rejected(self):
        u = "https://api.github.com/repos/" + REPO + "/pulls?per_page=100"
        api = GitHubAPI(REPO, get=FakeAPI({
            u: ([pr(1, "a")], '<https://evil.invalid/collect>; rel="next"'),
        }))
        with self.assertRaisesRegex(InventoryError, "untrusted"):
            api.open_pulls()

    def test_pagination_cycle_rejected(self):
        u = "https://api.github.com/repos/" + REPO + "/pulls?per_page=100"
        api = GitHubAPI(REPO, get=FakeAPI({
            u: ([pr(1, "a")], '<' + u + '>; rel="next"'),
        }))
        with self.assertRaisesRegex(InventoryError, "cycle"):
            api.open_pulls()

    def test_malformed_page_rejected(self):
        u = "https://api.github.com/repos/" + REPO + "/pulls?per_page=100"
        api = GitHubAPI(REPO, get=FakeAPI({u: ({"items": []}, "")}))
        with self.assertRaisesRegex(InventoryError, "page"):
            api.open_pulls()

    def test_exact_sha_checks_only(self):
        sha = "1" * 40
        u = "https://api.github.com/repos/" + REPO + "/commits/" + sha + "/check-runs?per_page=100"
        def check(checked_sha):
            api = GitHubAPI(REPO, get=FakeAPI({u: ({
                "total_count": 1, "check_runs": [{
                    "name": "proof", "head_sha": checked_sha,
                    "status": "completed", "conclusion": "success"
                }]}, "")}))
            return api.checks(sha)
        self.assertEqual(check(sha)["status"], "SUCCESS")
        with self.assertRaisesRegex(InventoryError, "SHA"):
            check("2" * 40)

    def test_empty_checks_are_unknown(self):
        sha = "1" * 40
        u = "https://api.github.com/repos/" + REPO + "/commits/" + sha + "/check-runs?per_page=100"
        api = GitHubAPI(REPO, get=FakeAPI({
            u: ({"total_count": 0, "check_runs": []}, ""),
        }))
        self.assertEqual(api.checks(sha)["status"], "UNKNOWN")

if __name__ == "__main__":
    unittest.main()
