"""RCP-001-B: strictly scoped, commit-pinned mathematical claim registry.

No third-party dependencies. This validates metadata and GitHub source provenance,
not the mathematical correctness or novelty of any claimed proof.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import json
from pathlib import Path, PurePosixPath
import re
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


SHA = re.compile(r"^[0-9a-f]{40}$")
IDENT = re.compile(r"^[A-Z0-9]+(?:-[A-Z0-9]+)+$")
REPO = "definitely-stable/Mathlab"
SCHEMA = "mathlab.rcp.claim.v1"
MODEL_SCHEMA = "mathlab.rcp.models.v1"
MODES = frozenset({
    "ENSEMBLE_EXPECTATION", "CONDITIONAL_EXPECTATION",
    "ALL_H_IDENTITY", "LOCAL_CONSTRUCTION", "DETERMINISTIC_BOUND",
})
STATUSES = frozenset({"DOCUMENTED_IN_DRAFT", "REVIEWED", "FORMALLY_VERIFIED",
                      "REFUTED", "SUPERSEDED"})
REVIEWS = frozenset({"NOT_REVIEWED", "INDEPENDENTLY_REVIEWED"})
NOVELTIES = frozenset({"NOT_ASSESSED", "KNOWN", "POTENTIALLY_NEW", "AUDITED"})
ALLOWED_OPS = frozenset({"forall", "exists", "expectation", "finite_witness"})


class RegistryError(ValueError):
    pass


def demand(condition: bool, message: str) -> None:
    if not condition:
        raise RegistryError(message)


def parse_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError, UnicodeDecodeError) as exc:
        raise RegistryError("invalid JSON at " + str(path)) from exc


def nonblank(s: Any) -> bool:
    return isinstance(s, str) and bool(s.strip())


def positive_pr(n: Any) -> bool:
    return type(n) is int and n > 0


def safe_source_path(p: Any) -> bool:
    if not nonblank(p) or "\\" in p or p.startswith("/") or "%" in p:
        return False
    parts = PurePosixPath(p).parts
    return bool(parts) and all(x not in (".", "..") for x in p.split("/"))


def read_registry(root: Path) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    root = Path(root)
    manifest = parse_json(root / "models.json")
    demand(isinstance(manifest, dict) and manifest.get("schema") == MODEL_SCHEMA,
           "invalid model registry schema")
    models = manifest.get("models")
    demand(isinstance(models, list) and bool(models), "model registry must be nonempty")
    registry: dict[str, dict[str, Any]] = {}
    for model in models:
        demand(isinstance(model, dict), "model object expected")
        mid = model.get("id")
        demand(isinstance(mid, str) and bool(IDENT.fullmatch(mid)),
               "invalid model identifier")
        demand(mid not in registry, "duplicate model id: " + mid)
        demand(nonblank(model.get("definition")), "model needs definition: " + mid)
        demand(isinstance(model.get("sources"), list) and
               all(nonblank(s) for s in model["sources"]) and model["sources"],
               "model needs cited sources: " + mid)
        registry[mid] = model
    files = sorted((root / "claims").glob("*.json"))
    demand(files, "no claim documents found")
    claims = []
    for path in files:
        c = parse_json(path)
        demand(isinstance(c, dict), "invalid claim object: " + str(path))
        demand(path.stem == c.get("id"), "filename must equal immutable ID: " + str(path))
        claims.append(c)
    return registry, claims


def validate_registry(root: Path) -> dict[str, Any]:
    models, claims = read_registry(root)
    seen = {}
    for c in claims:
        cid = c.get("id")
        demand(isinstance(cid, str) and bool(IDENT.fullmatch(cid)),
               "invalid claim identifier")
        demand(cid not in seen, "duplicate claim id: " + cid)
        seen[cid] = c
        demand(c.get("schema") == SCHEMA, cid + " invalid schema")
        demand(c.get("program") == "HYP-105", cid + " unexpected research program")
        demand(c.get("root_issue") == 230, cid + " unexpected root issue")
        for field in ("title", "statement", "limitations"):
            if field != "limitations":
                demand(nonblank(c.get(field)), cid + " missing " + field)
        demand(c.get("mode") in MODES, cid + " unsupported claim mode")
        demand(c.get("mathematical_status") in STATUSES, cid + " invalid mathematical status")
        demand(c.get("review_status") in REVIEWS, cid + " invalid independent review status")
        demand(c.get("novelty_status") in NOVELTIES, cid + " invalid novelty status")
        if c["mathematical_status"] in {"REVIEWED", "FORMALLY_VERIFIED"}:
            demand(c["review_status"] == "INDEPENDENTLY_REVIEWED" and
                   nonblank(c.get("acceptance_evidence")),
                   cid + " cannot promote claim without independent acceptance evidence")
        if c["review_status"] == "INDEPENDENTLY_REVIEWED":
            demand(nonblank(c.get("acceptance_evidence")),
                   cid + " missing independent review evidence")
        if c["mathematical_status"] == "DOCUMENTED_IN_DRAFT":
            demand(c["review_status"] == "NOT_REVIEWED",
                   cid + " draft claim cannot assert independent review")
        refs = c.get("model_ids")
        demand(isinstance(refs, list) and refs and
               len(set(refs)) == len(refs) and all(x in models for x in refs),
               cid + " unknown/duplicate model IDs")
        demand("MODEL-GQ-ORIGINAL" in refs and
               "MODEL-TYPED-GLOBAL-INJECTION" in refs,
               cid + " cannot omit original geometry or global injection")
        quants = c.get("quantifiers")
        demand(isinstance(quants, list) and quants,
               cid + " needs explicitly ordered quantifiers")
        ops = []
        for q in quants:
            demand(isinstance(q, dict) and set(q) == {"op", "variable", "domain"},
                   cid + " malformed quantifier")
            demand(q["op"] in ALLOWED_OPS and nonblank(q["variable"]) and
                   nonblank(q["domain"]), cid + " ambiguous quantifier")
            ops.append(q["op"])
        demand(ops[0] == "forall" and quants[0]["variable"] == "h" and
               "2^h" in quants[0]["domain"], cid + " missing genuine s=2^h domain")
        if c["mode"] == "ENSEMBLE_EXPECTATION":
            demand(ops[-1] == "expectation" and ops.count("expectation") == 1 and
                   "exists" not in ops, cid + " expectation ensemble not explicit")
        elif c["mode"] == "CONDITIONAL_EXPECTATION":
            demand(ops[-1] == "expectation" and ops.count("expectation") == 1 and
                   len(ops) >= 3 and "forall" in ops[1:-1],
                   cid + " wrong conditional expectation order")
        elif c["mode"] == "LOCAL_CONSTRUCTION":
            demand("exists" in ops and "expectation" not in ops,
                   cid + " local witness cannot be presented as a mean")
        else:
            demand(all(op == "forall" for op in ops),
                   cid + " all-h deterministic mode cannot hide sampling")
        limitations = c.get("limitations")
        demand(isinstance(limitations, list) and limitations and
               all(nonblank(x) for x in limitations),
               cid + " missing non-implication limitations")
        demand(nonblank(c.get("root_impact")) and
               c["root_impact"] == "ROOT_BRANCHES_OPEN",
               cid + " root is not certified as proved")
        parents = c.get("depends_on_claims")
        demand(isinstance(parents, list) and len(parents) == len(set(parents)) and
               all(isinstance(d, str) for d in parents),
               cid + " malformed dependency list")
        external = c.get("external_dependencies")
        demand(isinstance(external, list) and
               all(nonblank(x) for x in external),
               cid + " malformed external dependencies")
        source = c.get("source")
        demand(isinstance(source, dict), cid + " missing source")
        demand(source.get("repository") == REPO and positive_pr(source.get("pr")),
               cid + " wrong source repo/PR")
        demand(isinstance(source.get("commit"), str) and
               SHA.fullmatch(source["commit"]) is not None,
               cid + " source commit must be full pinned SHA")
        demand(safe_source_path(source.get("proof_path")) and
               source["proof_path"].startswith("docs/research/"),
               cid + " unsafe/missing proof path")
        demand(isinstance(source.get("proof_blob_sha"), str) and
               SHA.fullmatch(source["proof_blob_sha"]) is not None,
               cid + " missing pinned proof blob SHA")
        demand(source.get("stage") == "OPEN_DRAFT_PR",
               cid + " source state should be explicitly scoped to draft")
        # All field values are authoritative on the pinned source commit,
        # not an assertion of the current PR HEAD.
        demand(nonblank(c.get("falsification_boundary")),
               cid + " missing falsification/model boundary")

    edges = {cid: c["depends_on_claims"] for cid, c in seen.items()}
    for cid, parents in edges.items():
        for dep in parents:
            demand(dep in seen, cid + " references unknown claim " + dep)
            demand(dep != cid, cid + " self-dependency")
    active: set[str] = set()
    done: set[str] = set()
    def visit(cid: str):
        if cid in active:
            raise RegistryError("mathematical dependency cycle at " + cid)
        if cid in done:
            return
        active.add(cid)
        for dep in edges[cid]:
            visit(dep)
        active.remove(cid)
        done.add(cid)
    for cid in sorted(seen):
        visit(cid)
    return {"schema": "mathlab.rcp.registry.validation.v1",
            "models": len(models), "claims": len(seen),
            "claim_ids": sorted(seen),
            "dependencies": sum(map(len, edges.values())),
            "status": "METADATA_VALIDATED_NOT_MATHEMATICALLY_VERIFIED"}


def verify_pinned_sources(root: Path, *, get=None) -> list[str]:
    """Optional live source check; validates SHA/path/blob, not mathematical proof."""
    _, claims = read_registry(root)
    unique = {(c["source"]["commit"], c["source"]["proof_path"],
               c["source"]["proof_blob_sha"]) for c in claims}
    def github(url):
        from os import environ
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "mathlab-rcp-claims",
        }
        if environ.get("GITHUB_TOKEN"):
            headers["Authorization"] = "Bearer " + environ["GITHUB_TOKEN"]
        try:
            with urlopen(Request(url, headers=headers), timeout=25) as response:
                return json.load(response)
        except (HTTPError, URLError, OSError, ValueError) as exc:
            raise RegistryError("source reference cannot be verified") from exc
    fetch = get or github
    checked = []
    for commit, path, blob_sha in sorted(unique):
        url = ("https://api.github.com/repos/" + REPO +
               "/contents/" + quote(path, safe="/") + "?ref=" + commit)
        obj = fetch(url)
        demand(isinstance(obj, dict) and obj.get("type") == "file" and
               obj.get("sha") == blob_sha,
               "pinned source mismatch: " + commit + ":" + path)
        checked.append(commit + ":" + path)
    return checked


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path,
                        default=Path("research/rcp/hyp105"))
    parser.add_argument("--verify-sources", action="store_true",
                        help="check pinned proof blobs via GitHub REST API")
    args = parser.parse_args(argv)
    result = validate_registry(args.registry)
    if args.verify_sources:
        result["pinned_sources_verified"] = len(verify_pinned_sources(args.registry))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RegistryError as exc:
        raise SystemExit("RCP-001-B INVALID: " + str(exc)) from exc
