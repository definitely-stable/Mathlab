"""CI-OPT-001: conservative pull-request research scope, no cached scientific results.

Only explicitly isolated file families may skip unrelated research shards.
Any unknown/mixed/shared input or invalid git checkout fails closed.
The routing changes *which checks run*, never removes a named research
command from the full `push main` / `workflow_dispatch` suite.
"""
import argparse
import json
import os
import subprocess
from pathlib import PurePosixPath

SHARDS = ("foundation", "hyp_foundation", "hyp_census", "catalog")
KNOWN_EVENTS = ("pull_request", "push", "workflow_dispatch")


def all_required():
    return {key: True for key in (*SHARDS, "index")}


def _classify_file(path):
    """Return (named shards, index relevance), or None for unsafe/unknown.

    Documentation-only MD changes may bypass scientific computations, but
    metadata in docs/research/catalog is checked by the catalog shard.
    Existing scientific Python changes use conservative family whitelists.
    """
    if (not isinstance(path, str) or not path or "\x00" in path
            or "\\" in path or path.startswith("/")
            or any(part in ("", ".", "..") for part in path.split("/"))):
        return None
    if path.startswith("docs/research/catalog/"):
        return ({"catalog"}, False)
    if path == "README.md" or (path.startswith("docs/") and path.endswith(".md")):
        return (set(), False)
    if path.startswith("research/") and path.endswith(".py"):
        leaf = PurePosixPath(path).name
        if leaf.startswith(("hyp105_", "test_hyp105_")):
            return ({"hyp_foundation", "hyp_census"}, False)
        if leaf.startswith(("index001_", "test_index001_")):
            return ({"foundation"}, True)
        if leaf.startswith(("uct005_", "test_uct005_",
                             "dag002_", "test_dag002_")):
            return ({"foundation"}, False)
    return None


def classify_changes(changed_paths, event="pull_request"):
    """Fail closed by requesting ALL shards for unknown/shared/mixed paths.

    'full' is used for main pushes, manual dispatch and ambiguous input.
    In a scoped PR, the final aggregator requires exactly the selected
    shards to pass and all unselected shards to have been skipped.
    """
    if event not in KNOWN_EVENTS or event != "pull_request":
        chosen = all_required()
        return {"mode": "full", **chosen}
    paths = tuple(changed_paths)
    if not paths:
        return {"mode": "full", **all_required()}
    selected = set()
    index = False
    for path in paths:
        classified = _classify_file(path)
        if classified is None:
            return {"mode": "full", **all_required()}
        shards, applies_index = classified
        selected.update(shards)
        index = index or applies_index
    return {"mode": "scoped" if selected else "docs",
            **{name: name in selected for name in SHARDS}, "index": index}


def pull_request_changed_paths():
    """Compare *merge checkout* with its first (PR base) parent.

    No untrusted GitHub event string enters a shell command. A missing
    merge parent or inaccessible git tree makes detection FAIL, never an
    optimistic docs-only bypass.
    """
    parents = subprocess.check_output(
        ["git", "rev-list", "--parents", "-n", "1", "HEAD"], stderr=subprocess.PIPE
    ).decode("ascii").strip().split()
    if len(parents) != 3:
        raise RuntimeError("PR checkout must be a merge commit with TWO parents")
    raw = subprocess.check_output(
        ["git", "diff", "--name-only", "-z", "HEAD^1", "HEAD"],
        stderr=subprocess.PIPE,
    )
    return tuple(p.decode("utf-8", errors="strict")
                 for p in raw.split(b"\0") if p)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", required=True)
    parser.add_argument("--output", help="GitHub Actions GITHUB_OUTPUT path")
    args = parser.parse_args()
    if args.event == "pull_request":
        paths = pull_request_changed_paths()
    else:
        paths = ()
    decision = classify_changes(paths, args.event)
    if args.output:
        with open(args.output, "a", encoding="utf-8") as dest:
            for key, value in decision.items():
                print(f"{key}={str(value).lower() if isinstance(value, bool) else value}", file=dest)
    else:
        print(json.dumps(decision, sort_keys=True))
    print("CI-OPT scope:", decision["mode"],
          "shards:", ",".join(name for name in SHARDS if decision[name]) or "none",
          "index:", decision["index"], "changed:", len(paths))


if __name__ == "__main__":
    main()
