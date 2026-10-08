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
    "proof-complexity": "Сложность доказательств, сертификаты, PIT/IPS",
    "algebraic-complexity": "Алгебраическая сложность и условные барьеры",
    "fine-grained-algorithms": "Строки, edit distance и тонкая сложность",
    "graph-algorithms": "Динамические графы, обновления и алгоритмы",
    "randomized-sampling": "Рандомизированная выборка, подсчёт, память",
}
VERIFICATIONS = {
    "primary_abstract_checked",
    "publisher_abstract_checked",
    "publisher_bibliography_checked",
    "publisher_full_text_spotchecked",
    "author_paper_or_bibliography_checked",
}
SOURCE_REPOS = {"MATHLAB", "DELSK", "DELTAMETER"}

SOURCE_TITLE_PINS = {
    # Authoritative arXiv title checks: forbid a paper ID being paired with
    # a hallucinated or different publication title.
    "arxiv:2501.01046": "SEDD: Scalable and Efficient Dataset Deduplication with GPUs",
    "arxiv:1507.00954": "Bounds and Constructions for overline-3-Separable Codes with Length 3",
    "arxiv:2509.11121": "The Chonkers Algorithm: Content-Defined Chunking with Provable Strict Guarantees on Size and Locality",
    "arxiv:2609.14442": "Toward Optimal Time-Space Tradeoffs for Set Reconciliation",
}




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
        aliases = e.get("alternate_identities", [])
        check(isinstance(aliases, list), f"{ident}: invalid alternate identity list")
        all_identity = [ref] + (aliases if isinstance(aliases, list) else [])
        for name in all_identity:
            if not isinstance(name, str):
                check(False, f"{ident}: invalid alternate identity")
                continue
            check(bool(IDENTITY.fullmatch(name)), f"{ident}: malformed canonical/alternate identity")
            check(name.lower() not in seen_ident, f"{ident}: duplicate canonical identity")
            seen_ident.add(name.lower())
        pinned_title = SOURCE_TITLE_PINS.get(ref)
        if pinned_title is not None:
            check(e.get("title") == pinned_title, f"{ident}: primary source title mismatch")
        authors = e.get("authors")
        if authors is not None:
            check(isinstance(authors, list) and bool(authors) and all(
                isinstance(a, str) and len(a) > 3 for a in authors
            ), f"{ident}: invalid author list")
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
        if ident >= "LIT-050":
            check(e.get("year") == 2026, f"{ident}: 2026-only batch contains non-2026 work")
            check(e.get("venue") in {"STOC 2026", "ICALP 2026", "EuroSys 2026"},
                  f"{ident}: missing audited venue")
            check(bool(URL.fullmatch(e.get("source_listing_url", ""))),
                  f"{ident}: missing first-party listing URL")
            expected = {
                "STOC 2026": "https://acm-stoc.org/stoc2026/toc.html",
                "ICALP 2026": "https://drops.dagstuhl.de/entities/document/" + ref[4:] if ref.startswith("doi:") else "",
                "EuroSys 2026": "https://2026.eurosys.org/papers.html",
            }
            check(e.get("source_listing_url") == expected.get(e.get("venue")),
                  f"{ident}: primary listing/DOI mismatch")
            check(e.get("verification") in ("publisher_abstract_checked",
                                             "publisher_bibliography_checked"),
                  f"{ident}: ungrounded external full-proof verification")
            check(e.get("source_access") in (
                "official_conference_toc_abstract_linked_doi",
                "publisher_article_abstract_and_bibliography_checked",
                "conference_paper_list_and_delsk_fulltext_review"),
                f"{ident}: undocumented source access")
            check(e.get("mentioned_in") and all(
                o.get("kind") == "model_overlap" for o in e["mentioned_in"]),
                f"{ident}: 2026 cross-domain overlap mislabeled cited")

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
                f"**Идентичность:** `{e['identity']}`"
                + (f" · **Также:** {', '.join(e['alternate_identities'])}"
                   if e.get("alternate_identities") else "")
                + (f" · **Авторы:** {', '.join(e['authors'])}"
                   if e.get("authors") else "")
                + " · "
                + f"**Проверка:** `{e['verification']}` · "
                "**Доказательство:** НЕ перепроверено · **Бенчмарк:** НЕ воспроизведён.",
                "",
                *([f"**Проверенный издательский реестр:** "
                    f"[{e['venue']}]({e['source_listing_url']}) · "
                    f"**Доступ:** \`{e['source_access']}\`", ""]
                  if e.get("source_listing_url") else []),
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
