"""RCP-001-A. GitHub open-PR ancestry, integrity and exact-HEAD inventory.

Standard library only. This is a non-atomic observation, not a theorem proof.
"""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse, parse_qsl, urlencode
from urllib.request import Request, urlopen

SHA = re.compile(r"^[0-9a-f]{40}$")
REPO = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
FOCUS = re.compile(r"\bHYP[\s-]?105\b|(?:^|[^\d])#230\b", re.I)
NEXT = re.compile(r'<([^>]+)>\s*;\s*rel="next"')

class InventoryError(RuntimeError):
    """An incomplete inventory must never be published as verified."""

class GitHubAPI:
    def __init__(self, repo, get=None):
        if not REPO.fullmatch(repo):
            raise InventoryError("invalid owner/repository")
        self.repo = repo
        self.get = get or self._http_get
        self.calls = 0

    @staticmethod
    def _http_get(url):
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "mathlab-rcp-inventory",
        }
        if os.getenv("GITHUB_TOKEN"):
            headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
        try:
            with urlopen(Request(url, headers=headers), timeout=30) as response:
                raw, link = response.read(), response.headers.get("Link", "")
        except HTTPError as e:
            raise InventoryError("GitHub HTTP %d at %s" % (e.code, urlparse(url).path)) from e
        except (URLError, OSError, TimeoutError) as e:
            raise InventoryError("GitHub request failed: " + type(e).__name__) from e
        try:
            return json.loads(raw), link
        except (ValueError, UnicodeDecodeError) as e:
            raise InventoryError("GitHub returned invalid JSON") from e

    def pages(self, path, key=None, query=""):
        expected = "/repos/" + self.repo + "/"
        if not path.startswith(expected):
            raise InventoryError("unexpected API path")
        url = "https://api.github.com" + path + "?" + (query + "&" if query else "") + "per_page=100"
        seen, rows = set(), []
        while url:
            parsed = urlparse(url)
            if (parsed.scheme, parsed.netloc, parsed.path) != (
                "https", "api.github.com", path
            ) or parsed.username or parsed.password or parsed.fragment:
                raise InventoryError("untrusted pagination link")
            if url in seen:
                raise InventoryError("pagination cycle")
            seen.add(url)
            self.calls += 1
            data, link = self.get(url)
            page = data.get(key) if key and isinstance(data, dict) else data
            if not isinstance(page, list):
                raise InventoryError("unexpected GitHub page structure")
            rows.extend(page)
            match = NEXT.search(link)
            if not match and 'rel="next"' in link:
                raise InventoryError("malformed next link")
            if match:
                url = match.group(1)
            elif len(page) == 100:
                # On an unlinked full page, probe the next page explicitly.
                params = dict(parse_qsl(parsed.query))
                params["page"] = str(int(params.get("page", "1")) + 1)
                url = "https://api.github.com" + path + "?" + urlencode(params)
            else:
                url = ""
        return rows

    def open_pulls(self):
        rows = self.pages("/repos/" + self.repo + "/pulls",
                          query="state=open")
        nums = [r.get("number") for r in rows if isinstance(r, dict)]
        if len(nums) != len(rows) or any(type(n) is not int or n < 1 for n in nums):
            raise InventoryError("malformed pull request identity")
        if len(nums) != len(set(nums)):
            raise InventoryError("duplicate PR in paginated result")
        if any(r.get("state") != "open" for r in rows):
            raise InventoryError("non-open PR in open-only inventory")
        return rows

    def main_head(self):
        url = "https://api.github.com/repos/" + self.repo + "/branches/main"
        obj, _ = self.get(url)
        sha = obj.get("commit", {}).get("sha") if isinstance(obj, dict) else None
        if not isinstance(sha, str) or not SHA.fullmatch(sha):
            raise InventoryError("invalid main HEAD")
        return sha

    def checks(self, sha):
        if not SHA.fullmatch(sha):
            raise InventoryError("invalid check SHA")
        rows = self.pages("/repos/" + self.repo + "/commits/" + sha + "/check-runs",
                          key="check_runs")
        if any(not isinstance(r, dict) or r.get("head_sha") != sha
               or not isinstance(r.get("name"), str) for r in rows):
            raise InventoryError("incorrect check SHA/name")
        tally = Counter(str(r.get("conclusion") or "pending") for r in rows)
        state = ("UNKNOWN" if not rows else
                 "SUCCESS" if all(r.get("status") == "completed" and
                                  r.get("conclusion") == "success" for r in rows) else
                 "INCOMPLETE" if any(r.get("status") != "completed" for r in rows)
                 else "NOT_SUCCESS")
        return {"status": state, "verified_head": sha, "count": len(rows),
                "conclusions": dict(sorted(tally.items())),
                "names": sorted(r["name"] for r in rows)}

def repo_name(obj):
    return obj.get("full_name", "") if isinstance(obj, dict) else ""

def normalize(row):
    n = row["number"]
    h, b = row.get("head"), row.get("base")
    if not isinstance(h, dict) or not isinstance(b, dict):
        raise InventoryError("PR #%s missing head/base" % n)
    hs, bs = h.get("sha"), b.get("sha")
    if not isinstance(hs, str) or not SHA.fullmatch(hs):
        raise InventoryError("PR #%s invalid head sha" % n)
    if not isinstance(bs, str) or not SHA.fullmatch(bs):
        raise InventoryError("PR #%s invalid base sha" % n)
    if not h.get("ref") or not b.get("ref") or not repo_name(b.get("repo")):
        raise InventoryError("PR #%s invalid ref or base repository" % n)
    title = row.get("title") or ""
    body = row.get("body") or ""
    return {"number": n, "title": title, "url": row.get("html_url") or "",
            "updated_at": row.get("updated_at"), "draft": bool(row.get("draft")),
            "head_sha": hs, "head_ref": h["ref"],
            "head_repo": repo_name(h.get("repo")),
            "base_sha": bs, "base_ref": b["ref"],
            "base_repo": repo_name(b.get("repo")),
            "focus": bool(FOCUS.search(title + "\n" + body)),
            "parent_pr": None, "parent_sha_match": None, "base_relation": None,
            "depth": None, "checks": {"status": "NOT_INSPECTED"}}

def build_inventory(repo, rows, main_sha, as_of, api=None, check_prs=None,
                    checks_all=False):
    if not SHA.fullmatch(main_sha):
        raise InventoryError("main is not a pinned 40-character SHA")
    if not isinstance(rows, list):
        raise InventoryError("invalid PR collection")
    prs = [normalize(row) for row in rows]
    by_num = {p["number"]: p for p in prs}
    if len(by_num) != len(prs):
        raise InventoryError("duplicate PR number")
    branch_to_pr = {}
    for p in prs:
        if p["head_repo"]:
            branch_to_pr.setdefault((p["head_repo"], p["head_ref"]), []).append(
                p["number"])
    diag = []
    for p in prs:
        parents = branch_to_pr.get((p["base_repo"], p["base_ref"]), [])
        if len(parents) > 1:
            p["base_relation"] = "AMBIGUOUS"
            diag.append({"pr": p["number"], "kind": "AMBIGUOUS_PARENT",
                         "candidates": sorted(parents)})
        elif parents:
            parent = by_num[parents[0]]
            p["base_relation"], p["parent_pr"] = "OPEN_PARENT", parent["number"]
            p["parent_sha_match"] = parent["head_sha"] == p["base_sha"]
            if not p["parent_sha_match"]:
                diag.append({"pr": p["number"], "kind": "PARENT_BASE_SHA_DRIFT",
                             "parent": parent["number"]})
        elif p["base_repo"] == repo and p["base_ref"] == "main":
            p["base_relation"] = "MAIN"
            p["parent_sha_match"] = p["base_sha"] == main_sha
            if not p["parent_sha_match"]:
                diag.append({"pr": p["number"], "kind": "MAIN_BASE_SHA_DRIFT"})
        else:
            p["base_relation"] = "UNRESOLVED_BASE"
            diag.append({"pr": p["number"], "kind": "UNRESOLVED_BASE",
                         "base_repo": p["base_repo"], "base_ref": p["base_ref"]})
    visiting, depths = set(), {}
    def find_depth(n):
        if n in visiting:
            raise InventoryError("PR ancestry cycle at #%s" % n)
        if n in depths:
            return depths[n]
        visiting.add(n)
        pn = by_num[n]["parent_pr"]
        value = 0 if pn is None else 1 + find_depth(pn)
        visiting.remove(n)
        depths[n] = value
        return value
    for p in prs:
        p["depth"] = find_depth(p["number"])
    requested = set(check_prs or [])
    if requested - set(by_num):
        raise InventoryError("requested CI for missing PR: " +
                             repr(sorted(requested - set(by_num))))
    if (requested or checks_all) and api is None:
        raise InventoryError("CI requested without GitHub access")
    for p in prs:
        if checks_all or p["number"] in requested:
            p["checks"] = api.checks(p["head_sha"])
    prs.sort(key=lambda p: p["number"])
    diag.sort(key=lambda d: (d["pr"], d["kind"]))
    focused = {p["number"] for p in prs if p["focus"]}
    expanded = set(focused)
    for n in focused:
        parent = by_num[n]["parent_pr"]
        while parent is not None:
            expanded.add(parent)
            parent = by_num[parent]["parent_pr"]
    return {"schema": "mathlab.rcp.inventory.v1", "repo": repo,
            "as_of_utc": as_of, "main_head": main_sha,
            "consistency": "NON_ATOMIC_GITHUB_API_OBSERVATION",
            "ci_semantics": "EXACT_HEAD_CHECK_RUNS_NOT_MATHEMATICAL_PROOF",
            "open_pr_count": len(prs), "hyp105_direct_count": len(focused),
            "hyp105_with_ancestors_count": len(expanded),
            "max_stack_depth": max(depths.values(), default=0),
            "complete_open_pr_pagination": True,
            "open_prs": prs, "diagnostics": diag}

def markdown(data):
    tick = chr(96)
    lines = ["# HYP-105 — RCP-001-A live PR inventory", "",
             "- Observed: " + data["as_of_utc"],
             "- Repository: " + data["repo"],
             "- main HEAD: " + tick + data["main_head"] + tick,
             "- Open PR: %d; direct HYP-105: %d; with ancestors: %d" %
             (data["open_pr_count"], data["hyp105_direct_count"],
              data["hyp105_with_ancestors_count"]),
             "- Maximum open-PR ancestry depth: %d" % data["max_stack_depth"],
             "- Non-atomic API observation; older checks are never asserted for new HEAD.",
             "- NOT_INSPECTED means unknown CI, not a PASS.",
             "- Root #230 remains OPEN unless separately mathematically resolved.", "",
             "## Diagnostics", ""]
    if not data["diagnostics"]:
        lines.append("No structural diagnostics.")
    for d in data["diagnostics"]:
        lines.append("- PR #%d: %s (%s)" %
                     (d["pr"], d["kind"], json.dumps(d, sort_keys=True)))
    lines.extend(["", "## Open HYP-105 PR and their open parents", "",
                  "| PR | Parent/base | Depth | HEAD | CI | Title |",
                  "|---|---|---:|---|---|---|"])
    by_num = {p["number"]: p for p in data["open_prs"]}
    focus = {n for n, p in by_num.items() if p["focus"]}
    for n in list(focus):
        parent = by_num[n]["parent_pr"]
        while parent is not None:
            focus.add(parent)
            parent = by_num[parent]["parent_pr"]
    for p in data["open_prs"]:
        if p["number"] not in focus:
            continue
        parent = ("#" + str(p["parent_pr"])) if p["parent_pr"] else p["base_relation"]
        title = p["title"].replace("|", "\\|").replace("\n", " ")
        lines.append("| [#%d](%s) | %s | %d | %s | %s | %s |" %
                     (p["number"], p["url"], parent, p["depth"],
                      tick + p["head_sha"][:12] + tick,
                      p["checks"]["status"], title))
    return "\n".join(lines) + "\n"

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default="definitely-stable/Mathlab")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--check-pr", action="append", type=int, default=[])
    parser.add_argument("--checks-all", action="store_true")
    parser.add_argument("--as-of", default=None)
    args = parser.parse_args(argv)
    api = GitHubAPI(args.repo)
    main_sha = api.main_head()
    rows = api.open_pulls()
    time = args.as_of or datetime.now(timezone.utc).isoformat(timespec="seconds")
    data = build_inventory(args.repo, rows, main_sha, time, api=api,
                           check_prs=args.check_pr, checks_all=args.checks_all)
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "inventory.json").write_text(
        json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8")
    (args.output / "inventory.md").write_text(markdown(data), encoding="utf-8")
    print("RCP-001-A PASS: open=%d, HYP-105=%d, warnings=%d, API calls=%d" %
          (data["open_pr_count"], data["hyp105_direct_count"],
           len(data["diagnostics"]), api.calls))
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except InventoryError as exc:
        raise SystemExit("RCP-001-A FAIL CLOSED: " + str(exc)) from exc
