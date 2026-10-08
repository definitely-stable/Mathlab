#!/usr/bin/env python3
"""External literature: offline metadata validator and deterministic navigation.

Do NOT equate cited external literature with a verified proof, benchmark, or
novelty claim. No network, no dependencies, no external code execution.
Usage: python research/literature.py --check | --write
"""
import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs/research/catalog/literature.json"
INTERNAL = ROOT / "docs/research/catalog/registry.json"
INDEX = ROOT / "docs/research/catalog/LITERATURE.md"
REVERSE = ROOT / "docs/research/catalog/LITERATURE-BY-RESEARCH.md"
REPO_ID = re.compile(r"^LIT-[0-9]{3}$")
SHA = re.compile(r"^[a-f0-9]{40}$")
URL = re.compile(r"^https://[^\s<>]+$")
IDENTITY = re.compile(
    r"^(?:doi:10\.[0-9]{4,9}/[^\s]+|arxiv:[0-9]{4}\.[0-9]{4,5}"
    r"|usenix:[a-z0-9-]+:[a-z0-9-]+|publisher:[a-z0-9:-]+)$"
)
TRACKS = {
    "sparse-coding": "Кодирование, ограниченная поддержка, экстремальные границы",
    "dynamic-data-structures": "Динамические структуры, каноничность и локальность правок",
    "incremental-computation": "Инкрементальные вычисления и сертификаты",
    "delta-base-selection": "DELSK: поиск delta-базы, сжатие, признаки",
    "streaming-reconciliation": "DeltaMeter: потоковые оценки и согласование множеств",
}
VERIFICATIONS = {
    "primary_abstract_checked",
    "publisher_abstract_checked",
    "publisher_bibliography_checked",
    "publisher_full_text_spotchecked",
    "author_paper_or_bibliography_checked",
}
SOURCE_REPOS = {"MATHLAB", "DELSK", "DELTAMETER"}


def valid(data, catalog):
    errors = []

    def check(ok, message):
        if not ok:
            errors.append(message)

    check(data.get("schema") == "mathlab.external-literature.v1", "invalid schema")
    snaps = data.get("source_snapshots", {})
    check(set(snaps) == SOURCE_REPOS, "unexpected/missing source snapshots")
    for key, source in snaps.items():
        check(key in SOURCE_REPOS and isinstance(source.get("repo"), str), "invalid snapshot repo")
        check(bool(SHA.fullmatch(source.get("sha", ""))), f"{key}: invalid snapshot SHA")

    allowed_research = {e["id"] for e in catalog["entries"]}
    entries = data.get("entries", [])
    check(isinstance(entries, list) and len(entries) >= 30, "literature corpus too small")
    seen_ids, seen_ident, seen_urls = set(), set(), set()

    for e in entries:
        ident = e.get("id", "?")
        check(bool(REPO_ID.fullmatch(ident)), f"{ident}: malformed ID")
        check(ident not in seen_ids, f"{ident}: duplicate ID")
        seen_ids.add(ident)
        ref = e.get("identity", "")
        check(bool(IDENTITY.fullmatch(ref)), f"{ident}: malformed canonical identity")
        check(ref.lower() not in seen_ident, f"{ident}: duplicate canonical identity")
        seen_ident.add(ref.lower())
        url = e.get("primary_url", "")
        check(bool(URL.fullmatch(url)), f"{ident}: malformed primary URL")
        check(url not in seen_urls, f"{ident}: duplicate primary URL")
        seen_urls.add(url)
        if ref.startswith("doi:"):
            check(url.lower() == "https://doi.org/" + ref[4:].lower(), f"{ident}: DOI mismatch")
        elif ref.startswith("arxiv:"):
            check(url.lower() == "https://arxiv.org/abs/" + ref[6:].lower(), f"{ident}: arxiv mismatch")
        check(isinstance(e.get("year"), int) and 1950 <= e["year"] <= 2026,
              f"{ident}: invalid year")
        for key in ("title", "summary_ru", "limits_ru"):
            check(isinstance(e.get(key), str) and len(e[key].strip()) >= 12,
                  f"{ident}: missing {key}")
        check(e.get("track") in TRACKS, f"{ident}: invalid track")
        check(e.get("verification") in VERIFICATIONS, f"{ident}: invalid verification")
        check(e.get("full_proof_verified") is False and
              e.get("independent_reproduction") is False,
              f"{ident}: unsupported proof/reproduction promotion")
        relates = e.get("maps_to", [])
        check(isinstance(relates, list) and len(relates) >= 1, f"{ident}: missing research links")
        for rid in relates:
            check(rid in allowed_research, f"{ident}: dangling research link {rid}")
        check(len(relates) == len(set(relates)), f"{ident}: duplicate research mapping")
        mentions = e.get("mentioned_in", [])
        check(isinstance(mentions, list) and len(mentions) >= 1,
              f"{ident}: missing pinned provenance")
        seen_origins = set()
        for origin in mentions:
            r = origin.get("repo")
            path = origin.get("path", "")
            check(r in SOURCE_REPOS, f"{ident}: origin repository invalid")
            check(origin.get("kind") in ("cited", "model_overlap"),
                  f"{ident}: origin kind invalid")
            check(bool(path) and not path.startswith("/") and
                  ".." not in Path(path).parts and path.endswith(".md"),
                  f"{ident}: origin path unsafe")
            check((r, path) not in seen_origins, f"{ident}: duplicate origin")
            seen_origins.add((r, path))
    return errors


def manuscript_link(e):
    return f"[{e['title']}]({e['primary_url']})"


def source_link(snapshot, origin):
    source = snapshot[origin["repo"]]
    path = origin["path"]
    return (f"[{origin['repo']}:{path}]("
            f"https://github.com/{source['repo']}/blob/{source['sha']}/{path})")


def render(data):
    rows = data["entries"]
    snap = data["source_snapshots"]
    groups = defaultdict(list)
    for e in rows:
        groups[e["track"]].append(e)
    out = [
        "# External primary literature — тематический каталог",
        "",
        "> Generated from `literature.json` by `research/literature.py`. "
        "Редактировать следует только JSON.",
        "",
        f"Срез: **{data['snapshot_date']}** · **{len(rows)}** проверенных ссылок "
        "на первичные публикации/авторские рукописи.",
        "",
        "**Критически важно:** проверенная библиография или авторский abstract "
        "не равны независимо проверенному доказательству, статистическому "
        "результату либо научной новизне. Точные условия — в каждой записи.",
        "",
        "Связи в обратную сторону: [LITERATURE-BY-RESEARCH.md]"
        "(LITERATURE-BY-RESEARCH.md). "
        "Внутренние исследования: [INDEX.md](INDEX.md).",
        "",
        "| Направление | Записей |",
        "| --- | ---: |",
    ]
    for track, title in TRACKS.items():
        out.append(f"| [{title}](#{track}) | {len(groups[track])} |")
    for track, title in TRACKS.items():
        out += ["", f"## {track}", f"*{title}*", ""]
        for e in sorted(groups[track], key=lambda x: x["id"]):
            links = ", ".join(
                f"[{item}](INDEX.md#{item.lower()})" for item in e["maps_to"])
            sources = "; ".join(
                f"{source_link(snap, o)} ({o['kind']})" for o in e["mentioned_in"])
            out += [
                f"### {e['id']}",
                f"**{manuscript_link(e)}** ({e['year']})",
                "",
                e["summary_ru"],
                "",
                f"**Ограничение:** {e['limits_ru']}",
                "",
                f"**Идентичность:** `{e['identity']}` · "
                f"**Проверка:** `{e['verification']}` · "
                "**Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.",
                "",
                f"**Связь с исследованиями →** {links}",
                "",
                f"**Происхождение цитаты / пересечения →** {sources}",
                "",
            ]
    return "\n".join(out).rstrip() + "\n"


def render_reverse(data, catalog):
    by_research = defaultdict(list)
    for e in data["entries"]:
        for rid in e["maps_to"]:
            by_research[rid].append(e)
    out = [
        "# External literature by Mathlab research record",
        "",
        "> Generated from `literature.json` and `registry.json`. "
        "Связи обозначают релевантность, но не логическое следствие.",
        "",
        f"**{len(data['entries'])}** работ сопоставлены с "
        f"**{len(by_research)}** внутренними исследованиями.",
        "",
        "[Основной индекс литературы](LITERATURE.md) · "
        "[Индекс исследований](INDEX.md)",
        "",
    ]
    for rec in sorted(catalog["entries"], key=lambda z: z["id"]):
        related = by_research.get(rec["id"])
        if not related:
            continue
        out += [f"## {rec['id']}", "",
                f"**[{rec['title']}](INDEX.md#{rec['id'].lower()})**", ""]
        for e in sorted(related, key=lambda x: x["id"]):
            out.append(
                f"- [{e['id']}](LITERATURE.md#{e['id'].lower()}) — "
                f"{e['title']} ({e['year']}; {e['verification']})"
            )
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser()
    command = parser.add_mutually_exclusive_group(required=True)
    command.add_argument("--check", action="store_true")
    command.add_argument("--write", action="store_true")
    args = parser.parse_args()
    data = json.loads(DATA.read_text(encoding="utf-8"))
    catalog = json.loads(INTERNAL.read_text(encoding="utf-8"))
    errors = valid(data, catalog)
    if errors:
        for error in errors:
            print("LITERATURE_ERROR:", error)
        raise SystemExit(1)
    expected = render(data)
    expected_reverse = render_reverse(data, catalog)
    if args.write:
        INDEX.write_text(expected, encoding="utf-8")
        REVERSE.write_text(expected_reverse, encoding="utf-8")
    else:
        if not INDEX.exists() or INDEX.read_text(encoding="utf-8") != expected:
            raise SystemExit("LITERATURE_ERROR: LITERATURE.md drift; run --write")
        if not REVERSE.exists() or REVERSE.read_text(encoding="utf-8") != expected_reverse:
            raise SystemExit("LITERATURE_ERROR: LITERATURE-BY-RESEARCH.md drift; run --write")
    print("LITERATURE_SCHEMA_AND_SOURCE_PINS_PASS")
    print("LITERATURE_CANONICAL_IDENTITIES_PASS")
    print("LITERATURE_GENERATED_DOCUMENTS_PASS")
    print("LITERATURE_NO_NOVELTY_PROMOTION_PASS")


if __name__ == "__main__":
    main()
