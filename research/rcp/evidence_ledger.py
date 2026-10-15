"""RCP-001-C: immutable archived proof artifacts and scoped no-go research ledger.

Metadata and bytes verification are separate from mathematical peer review.
Uses only the Python standard library.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
from pathlib import Path
import re
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

from research.rcp.claim_registry import (
    REPO, SHA, IDENT, RegistryError, read_registry, validate_registry,
    parse_json, safe_source_path, nonblank,
)

E_SCHEMA = "mathlab.rcp.evidence.v1"
N_SCHEMA = "mathlab.rcp.no-go.v1"
KINDS = {"SCOPED_COUNTEREXAMPLE", "INVALID_INFERENCE", "MODEL_MISMATCH"}
ARTIFACT_ROLES = {"ORACLE_SOURCE", "INDEPENDENT_TEST", "FROZEN_FIXTURE"}
PREFIX = "research/rcp/hyp105/archive"


def require(condition, message):
    if not condition:
        raise RegistryError(message)


def relative_archive_path(receipt, artifact=None):
    """Deterministic immutable Git-tree aliases of existing source blobs."""
    pr = receipt["source"]["pr"]
    base = f"{PREFIX}/PR{pr}"
    if artifact is None:
        return base + "/proof.md"
    role = artifact["role"]
    if role == "ORACLE_SOURCE":
        return base + "/oracle.py.txt"
    if role == "INDEPENDENT_TEST":
        return base + "/independent_test.py.txt"
    return base + "/fixtures/" + Path(artifact["path"]).name


def load_ledgers(root):
    evid_paths = sorted((root / "evidence").glob("*.json"))
    nogo_paths = sorted((root / "no_go").glob("*.json"))
    require(bool(evid_paths) and bool(nogo_paths), "evidence and no-go ledgers required")
    evidence = [parse_json(p) for p in evid_paths]
    nogos = [parse_json(p) for p in nogo_paths]
    for items, paths in ((evidence, evid_paths), (nogos, nogo_paths)):
        for item, p in zip(items, paths):
            require(isinstance(item, dict) and item.get("id") == p.stem,
                    "filename must equal immutable record ID: " + str(p))
    return evidence, nogos


def validate_ledgers(root):
    """Cross-reference claims and invalidate any unsupported scope promotion."""
    root = Path(root)
    claims_validation = validate_registry(root)
    _, claims = read_registry(root)
    cmap = {c["id"]: c for c in claims}
    evidence, nogos = load_ledgers(root)
    by_id = {}
    source_pairs = set()
    artifact_count = 0
    archive_paths = set()
    for e in evidence:
        rid = e.get("id")
        require(isinstance(rid, str) and IDENT.fullmatch(rid) and
                rid.startswith("HYP105-EV-"), "invalid evidence ID")
        require(rid not in by_id, "duplicate evidence ID " + rid)
        by_id[rid] = e
        require(e.get("schema") == E_SCHEMA, rid + " invalid schema")
        ids = e.get("claim_ids")
        require(isinstance(ids, list) and ids and
                len(set(ids)) == len(ids) and all(i in cmap for i in ids),
                rid + " references missing or duplicate claims")
        s = e.get("source")
        require(isinstance(s, dict) and s.get("repository") == REPO and
                type(s.get("pr")) is int and s["pr"] > 0,
                rid + " invalid source repository or PR")
        require(isinstance(s.get("commit"), str) and SHA.fullmatch(s["commit"]),
                rid + " missing immutable source SHA")
        require(safe_source_path(s.get("proof_path")) and
                s["proof_path"].startswith("docs/research/") and
                isinstance(s.get("proof_blob_sha"), str) and
                SHA.fullmatch(s["proof_blob_sha"]),
                rid + " invalid pinned proof blob")
        pair = (s["pr"], s["commit"])
        require(pair not in source_pairs, rid + " duplicate source receipt")
        source_pairs.add(pair)
        for cid in ids:
            expected = cmap[cid]["source"]
            require(all(s[k] == expected[k] for k in
                        ("repository", "pr", "commit", "proof_path",
                         "proof_blob_sha")),
                    rid + " proof source differs from registered claim " + cid)
        arts = e.get("artifacts")
        require(isinstance(arts, list) and len(arts) >= 2,
                rid + " missing source/oracle/test artifacts")
        roles = [a.get("role") for a in arts if isinstance(a, dict)]
        require(roles.count("ORACLE_SOURCE") == 1 and
                roles.count("INDEPENDENT_TEST") == 1 and
                all(v in ARTIFACT_ROLES for v in roles) and len(roles) == len(arts),
                rid + " must pin oracle and independent test")
        local = [relative_archive_path(e)]
        src_paths = {s["proof_path"]}
        for a in arts:
            require(safe_source_path(a.get("path")) and
                    isinstance(a.get("git_blob_sha"), str) and
                    SHA.fullmatch(a["git_blob_sha"]),
                    rid + " unpinned artifact")
            require(a["path"] not in src_paths, rid + " duplicate source path")
            src_paths.add(a["path"])
            local.append(relative_archive_path(e, a))
        require(len(local) == len(set(local)), rid + " archive path collision")
        require(not (archive_paths & set(local)), rid + " archive aliases collide")
        archive_paths.update(local)
        replay = e.get("reproduction")
        require(isinstance(replay, dict) and
                replay.get("runner") == "GITHUB_HOSTED" and
                replay.get("checkout_commit") == s["commit"] and
                nonblank(replay.get("command")) and
                replay.get("execution_status") ==
                "COMMAND_DOCUMENTED_NOT_EXECUTED_BY_RCP_C",
                rid + " replay must be explicit and never fabricated as run")
        require(e.get("ci", {}).get("status") == "NOT_ARCHIVED_AS_PROOF",
                rid + " CI is not a mathematical certificate")
        require(nonblank(e.get("retention")) and
                isinstance(e.get("limitations"), list) and e["limitations"],
                rid + " must state retention and mathematical limits")
        artifact_count += 1 + len(arts)
    require(set(cmap) == {i for e in evidence for i in e["claim_ids"]},
            "some registered claims are missing evidence receipts")

    no_go_ids = set()
    for n in nogos:
        nid = n.get("id")
        require(isinstance(nid, str) and IDENT.fullmatch(nid) and
                nid.startswith("HYP105-NG-"), "invalid no-go ID")
        require(nid not in no_go_ids, "duplicate no-go ID " + nid)
        no_go_ids.add(nid)
        require(n.get("schema") == N_SCHEMA and n.get("root_issue") == 230 and
                n.get("program") == "HYP-105",
                nid + " unexpected no-go schema, root issue, or program")
        require(n.get("kind") in KINDS, nid + " unknown no-go kind")
        ids = n.get("related_claim_ids")
        evs = n.get("evidence_ids")
        require(isinstance(ids, list) and ids and len(ids) == len(set(ids)) and
                all(i in cmap for i in ids), nid + " missing related claim")
        require(isinstance(evs, list) and evs and len(evs) == len(set(evs)) and
                all(i in by_id for i in evs), nid + " missing evidence ID")
        require(all(set(ids) & set(by_id[eid]["claim_ids"]) for eid in evs),
                nid + " evidence unrelated to declared mathematical claims")
        for field in ("rejected_inference", "witness_scope", "mathematical_basis",
                      "reopen_only_if", "do_not_repeat"):
            require(nonblank(n.get(field)), nid + " missing " + field)
        limits = n.get("does_not_refute")
        require(isinstance(limits, list) and limits and
                all(nonblank(v) for v in limits),
                nid + " must explicitly delimit what is not refuted")
        require(n.get("root_status") == "OPEN_WITH_FORMAL_BLOCKER" and
                n.get("review_status") ==
                "DOCUMENTED_SCOPE_NOT_INDEPENDENTLY_REVIEWED",
                nid + " may not silently close root or assert independent proof")
        require(n.get("prior_registry_ref") ==
                "docs/research/KNOWN-AND-STOPPED-RESEARCH.json",
                nid + " must crosslink existing no-rediscovery registry")
    return {
        "schema": "mathlab.rcp.ledger.validation.v1",
        "status": "METADATA_AND_ARCHIVE_PROVENANCE_NOT_MATHEMATICAL_PROOF",
        "claim_count": claims_validation["claims"],
        "evidence_count": len(evidence),
        "no_go_count": len(nogos),
        "archived_blob_count": artifact_count,
        "archive_paths": sorted(archive_paths),
    }


def git_blob_sha(payload):
    """Git SHA-1 object name, not plain-file SHA-1."""
    return hashlib.sha1(b"blob " + str(len(payload)).encode("ascii") +
                        b"\0" + payload).hexdigest()


def expected_blobs(root):
    """Return (archive relative path, Git blob id, exact GitHub source ref)."""
    evidence, _ = load_ledgers(root)
    items = []
    for e in evidence:
        src = e["source"]
        sha = src["commit"]
        items.append((relative_archive_path(e), src["proof_blob_sha"],
                      sha, src["proof_path"]))
        items.extend((relative_archive_path(e, a), a["git_blob_sha"],
                      sha, a["path"]) for a in e["artifacts"])
    return sorted(items)


def verify_archives(root, repo_root):
    """Independently validate byte-for-byte escrow copies without any API."""
    report = []
    for rel, blob, commit, origin in expected_blobs(root):
        path = Path(repo_root) / rel
        try:
            payload = path.read_bytes()
        except OSError as exc:
            raise RegistryError("archive bytes unavailable: " + rel) from exc
        require(git_blob_sha(payload) == blob, "archive Git blob mismatch: " + rel)
        report.append({
            "archive": rel, "origin": origin, "source_commit": commit,
            "git_blob_sha": blob,
            "sha256": hashlib.sha256(payload).hexdigest(),
            "size": len(payload),
        })
    return report


def github_contents_bytes(url):
    import os
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "mathlab-rcp-evidence",
    }
    if os.getenv("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    try:
        with urlopen(Request(url, headers=headers), timeout=30) as response:
            raw = json.load(response)
    except (HTTPError, URLError, OSError, ValueError) as exc:
        raise RegistryError("GitHub pinned source could not be fetched") from exc
    require(isinstance(raw, dict) and raw.get("type") == "file" and
            raw.get("encoding") == "base64" and
            isinstance(raw.get("content"), str),
            "GitHub returned missing/non-base64 pinned source")
    try:
        payload = base64.b64decode("".join(raw["content"].split()), validate=True)
    except (ValueError, base64.binascii.Error) as exc:
        raise RegistryError("invalid GitHub source base64") from exc
    require(raw.get("sha") == git_blob_sha(payload),
            "GitHub source blob id inconsistent with downloaded bytes")
    return payload


def verify_originals(root, *, get=None):
    """Optional independent API cross-check; does not assert original CI PASS."""
    read_bytes = get or github_contents_bytes
    checked = []
    for rel, blob, commit, source_path in expected_blobs(root):
        url = ("https://api.github.com/repos/" + REPO + "/contents/" +
               quote(source_path, safe="/") + "?ref=" + commit)
        payload = read_bytes(url)
        require(isinstance(payload, bytes) and git_blob_sha(payload) == blob,
                "remote pinned origin content mismatch: " + source_path)
        checked.append(rel)
    return checked


def index_markdown(report, nogos, validation):
    lines = [
        "# RCP-001-C — durable HYP-105 evidence and no-go index",
        "",
        "**Byte identity validated, NOT a mathematical proof or CI acceptance.**",
        "",
        "Root #230: OPEN_WITH_FORMAL_BLOCKER.",
        "",
        "Claims: %d; evidence receipts: %d; no-go records: %d; escrow blobs: %d" %
        (validation["claim_count"], validation["evidence_count"],
         validation["no_go_count"], validation["archived_blob_count"]),
        "",
        "## Git-pinned source escrow",
        "",
        "| Archive | Original source | SHA256 |",
        "|---|---|---|",
    ]
    for v in report:
        lines.append("| " + v["archive"] + " | " + v["origin"] +
                     " | " + v["sha256"] + " |")
    lines.extend(["", "## No-go and invalid inference registry", ""])
    for n in nogos:
        lines.extend([
            "### " + n["id"] + " — " + n["kind"],
            "",
            "**Rejected:** " + n["rejected_inference"],
            "",
            "**Applies only to:** " + n["witness_scope"],
            "",
            "**Does NOT refute:** " + "; ".join(n["does_not_refute"]),
            "",
            "**Reopen only if:** " + n["reopen_only_if"],
            "",
            "**References:** " + ", ".join(n["related_claim_ids"]) + " / " +
            ", ".join(n["evidence_ids"]),
            "",
        ])
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path,
                        default=Path("research/rcp/hyp105"))
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path)
    parser.add_argument("--verify-originals", action="store_true")
    args = parser.parse_args(argv)
    validated = validate_ledgers(args.registry)
    archive_report = verify_archives(args.registry, args.repo_root)
    if args.verify_originals:
        validated["remote_origins_verified"] = len(
            verify_originals(args.registry))
    _, no_gos = load_ledgers(args.registry)
    no_gos.sort(key=lambda n: n["id"])
    result = {
        "schema": "mathlab.rcp.evidence-index.v1",
        "root_status": "OPEN_WITH_FORMAL_BLOCKER",
        "acceptance": "PROVENANCE_NOT_MATHEMATICAL_PROOF",
        "validation": validated,
        "archived_sources": archive_report,
        "no_go": no_gos,
    }
    if args.output:
        args.output.mkdir(parents=True, exist_ok=True)
        (args.output / "evidence.json").write_text(
            json.dumps(result, indent=2, ensure_ascii=False,
                       sort_keys=True) + "\n", encoding="utf-8")
        (args.output / "evidence.md").write_text(
            index_markdown(archive_report, no_gos, validated), encoding="utf-8")
    print("RCP-001-C BYTE PROVENANCE VERIFIED: %d receipts, %d no-go, %d blobs%s" %
          (validated["evidence_count"], validated["no_go_count"],
           len(archive_report),
           "; remote source cross-check complete" if args.verify_originals
           else "; remote source checks NOT REQUESTED"))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RegistryError as exc:
        raise SystemExit("RCP-001-C INVALID: " + str(exc)) from exc
