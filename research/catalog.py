#!/usr/bin/env python3
"""RESEARCH-INDEX-001: offline, deterministic provenance catalog validator/renderer.

No network access, no external packages, no proof/novelty inference.
Usage: python research/catalog.py --check | --write
"""
import argparse
import json
from collections import Counter
from pathlib import Path
import re
import sys
from urllib.parse import quote, urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs/research/catalog/registry.json"
INDEX = ROOT / "docs/research/catalog/INDEX.md"
SHA = re.compile(r"^[0-9a-f]{40}$")
ID = re.compile(r"^(ML|DL|DM|OM)-[0-9]{3}$")
URL = re.compile(r"^https://[^\s<>]+$")
STATUSES = {
    "DERIVED_RESULT", "EXACT_NUMERICAL", "EMPIRICAL_RESULT", "OPEN_QUESTION",
    "PRIOR_ART_AUDIT", "RESEARCH_MAP", "RESEARCH_DECISION",
    "RESEARCH_SYNTHESIS", "RESEARCH_EVIDENCE", "RESEARCH_PLAN",
    "RESEARCH_PROTOCOL", "REPRODUCTION", "EXTERNAL_CATALOG",
    "EXTERNAL_MANUSCRIPT_CLAIM",
}
VERIFICATION = {
    "repository_proof", "exact_hosted_ci", "primary_source_review",
    "repository_review", "exact_retained_measurement", "repository_tests",
    "source_inspected", "source_catalog",
}
RELATIONS = {
    "related", "constrained_by", "method_compare", "audits", "precedes",
    "refined_by", "corrects", "extends", "foundation_for", "informs",
    "updated_by", "background_for", "motivates", "context", "follows",
    "followed_by", "system_extension", "uses", "counterpart", "bounded_by",
    "catalogued_in", "contains", "conceptual_link", "adjacent_application",
}
REPOS = {"MATHLAB": "ML", "DELSK": "DL", "DELTAMETER": "DM", "OPENAI_MATH": "OM"}


def check(data):
    errors = []
    def require(test, message):
        if not test:
            errors.append(message)

    require(data.get("schema_version") == "mathlab.research-catalog.v1", "schema version")
    require(re.fullmatch(r"20\d\d-\d\d-\d\d", data.get("snapshot_date", "")) is not None, "snapshot date")
    repositories = data.get("repositories", {})
    require(set(repositories) == set(REPOS), "repository keys")
    for name, info in repositories.items():
        require(bool(SHA.fullmatch(info.get("sha", ""))), f"{name}: SHA")
        require("/" in info.get("full", ""), f"{name}: full repo")
    entries = data.get("entries", [])
    require(isinstance(entries, list) and len(entries) >= 1, "entries required")
    id_set, paths = set(), set()
    for r in entries:
        ident = r.get("id", "")
        require(bool(ID.fullmatch(ident)), f"{ident}: invalid ID")
        require(ident not in id_set, f"{ident}: duplicate ID")
        id_set.add(ident)
        repo = r.get("repository", "")
        require(repo in REPOS, f"{ident}: unknown repository")
        if repo in REPOS:
            require(ident.startswith(REPOS[repo] + "-"), f"{ident}: wrong ID prefix")
        for k in ("title", "summary_ru", "application_ru", "limitations_ru"):
            require(isinstance(r.get(k), str) and len(r[k].strip()) >= 15,
                    f"{ident}: {k} missing/short")
        require(r.get("status") in STATUSES, f"{ident}: status")
        require(r.get("verification") in VERIFICATION, f"{ident}: verification")
        tags = r.get("topics", [])
        require(isinstance(tags, list) and bool(tags) and len(tags) == len(set(tags)),
                f"{ident}: topic tags")
        src = r.get("source", {})
        if repo in repositories:
            cfg = repositories[repo]
            require(src.get("repo") == cfg.get("full"), f"{ident}: source repo mismatch")
            require(src.get("revision") == cfg.get("sha"), f"{ident}: revision mismatch")
            path = src.get("path", "")
            require(bool(path) and not path.startswith("/") and
                    not any(x in (".", "..") for x in path.split("/")),
                    f"{ident}: unsafe path")
            require((repo, path) not in paths, f"{ident}: duplicated source file")
            paths.add((repo, path))
            root = f"https://github.com/{cfg['full']}/blob/"
            require(src.get("permalink") == root + cfg["sha"] + "/" + path,
                    f"{ident}: source permalink not revision-pinned")
            require(src.get("latest") == root + "main/" + path,
                    f"{ident}: latest path malformed")
        for ref in r.get("primary_sources", []):
            require(isinstance(ref, str) and bool(URL.fullmatch(ref)),
                    f"{ident}: malformed primary reference")
        relations = r.get("related", [])
        require(isinstance(relations, list), f"{ident}: relationships missing")
        for edge in relations:
            require(edge.get("relation") in RELATIONS, f"{ident}: invalid relation")
            require(edge.get("id") != ident, f"{ident}: self relation")
        if r.get("status") == "EXTERNAL_MANUSCRIPT_CLAIM":
            require(repo == "OPENAI_MATH" and r.get("verification") == "source_catalog",
                    f"{ident}: external manuscript claim may not be promoted")
        if repo == "OPENAI_MATH":
            require(r.get("status") in {"EXTERNAL_CATALOG", "EXTERNAL_MANUSCRIPT_CLAIM"},
                    f"{ident}: imported claim improperly classified")
    for r in entries:
        seen = set()
        for edge in r.get("related", []):
            target = edge.get("id")
            require(target in id_set, f"{r['id']}: broken relationship {target}")
            require((target, edge.get("relation")) not in seen,
                    f"{r['id']}: duplicate edge")
            seen.add((target, edge.get("relation")))
    return errors


def render(data):
    entries = data["entries"]
    incoming = {r["id"]: [] for r in entries}
    for r in entries:
        for edge in r["related"]:
            incoming[edge["id"]].append((r["id"], edge["relation"]))
    counts = Counter(x["repository"] for x in entries)
    output = [
        "# Research index — проверяемый каталог",
        "",
        "> Generated from `registry.json` by `research/catalog.py`. Edit JSON, not this file.",
        "",
        f"Snapshot: **{data['snapshot_date']}**. **{len(entries)}** selected entries; curated, not exhaustive.",
        "",
        "Обозначения: `EXTERNAL_MANUSCRIPT_CLAIM` — только заявление каталога автора,",
        "не независимо подтверждённая теорема. `EXACT_NUMERICAL` и `EMPIRICAL_RESULT`",
        "не подтверждают асимптотическую новизну. Политика: [README](README.md).",
        "",
        "| Источник | Записей | Раздел |",
        "| --- | ---: | --- |",
    ]
    captions = {"MATHLAB":"Mathlab","DELSK":"DELSK / Shift-lab","DELTAMETER":"DeltaMeter","OPENAI_MATH":"openai/math"}
    for key in REPOS:
        output.append(f"| {captions[key]} | {counts[key]} | [{key}](#{key.lower().replace('_','-')}) |")
    for key in REPOS:
        output += ["", f"## {key}", ""]
        for x in (e for e in entries if e["repository"] == key):
            identifier = x["id"]
            meta = x["source"]
            related = ", ".join(
                f"[{e['id']}](#{e['id'].lower()}) ({e['relation']})" for e in x["related"]
            ) or "—"
            backlinks = ", ".join(
                f"[{i}](#{i.lower()}) ({rel})" for i, rel in sorted(incoming[identifier])
            ) or "—"
            sources = ", ".join(
                f"[{n+1}]({u})" for n, u in enumerate(x["primary_sources"])
            ) or "—"
            output += [
                f"### {identifier} — {x['title']}",
                "",
                x["summary_ru"],
                "",
                f"**Статус:** `{x['status']}` · **Проверка:** `{x['verification']}` · "
                f"**Темы:** {', '.join(x['topics'])}",
                "",
                f"**Применение:** {x['application_ru']} **Ограничения:** {x['limitations_ru']}",
                "",
                f"**Происхождение:** [зафиксированная версия]({meta['permalink']}) · "
                f"[актуальная ветка]({meta['latest']}) · "
                f"первичные источники: {sources}",
                "",
                f"**Связи →** {related} · **Обратные ссылки ←** {backlinks}",
                "",
            ]
    return "\n".join(output).rstrip() + "\n"


def main():
    p = argparse.ArgumentParser()
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = p.parse_args()
    data = json.loads(DATA.read_text(encoding="utf-8"))
    errors = check(data)
    if errors:
        for message in errors:
            print("CATALOG_ERROR:", message)
        raise SystemExit(1)
    expected = render(data)
    if args.write:
        INDEX.write_text(expected, encoding="utf-8")
        print(f"CATALOG_GENERATED entries={len(data['entries'])}")
    else:
        if not INDEX.exists() or INDEX.read_text(encoding="utf-8") != expected:
            print("CATALOG_ERROR: INDEX.md out of sync; run python research/catalog.py --write")
            raise SystemExit(1)
        print(f"RESEARCH_INDEX_VALIDATION_PASS entries={len(data['entries'])}")
        print("RESEARCH_INDEX_BACKLINKS_PASS")
        print("RESEARCH_INDEX_GENERATED_DOC_PASS")


if __name__ == "__main__":
    main()
