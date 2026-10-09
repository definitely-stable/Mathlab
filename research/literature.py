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
    "compressed-indexing": "Сжатые структуры, индексация строк и нижние границы",
    "online-optimization": "Онлайн-оптимизация, конкурентные оценки и барьеры",
    "caching": "Кэширование, online paging, консистентность и память",
    "graph-algorithms": "Динамические графы, гиперграфы и sparsification",
    "algebraic-algorithms": "Алгебраические алгоритмы, subset sum и разреженные матрицы",
    "proof-certification": "Машинные доказательства, сертификаты и верификация",
    "proof-complexity": "Нижние границы доказательств, IPS/PIT и сертификаты",
    "algebraic-complexity": "Алгебраические схемы, математика и нижние границы",
    "fine-grained-algorithms": "Edit distance, строки и тонкая сложность",
    "randomized-sampling": "Рандомизированная выборка, подсчёт и memory-sample",

}
VERIFICATIONS = {
    "primary_abstract_checked",
    "publisher_abstract_checked",
    "publisher_bibliography_checked",
    "publisher_full_text_spotchecked",
    "author_paper_or_bibliography_checked",
}
SOURCE_REPOS = {"MATHLAB", "DELSK", "DELTAMETER"}
NEW_2026_IDS = {f"LIT-{i:03d}" for i in range(50, 70)}
VENUE_2026_IDS = {f"LIT-{i:03d}" for i in range(70, 96)}
PUBLICATION_STAGES = {"peer_reviewed_proceedings", "author_preprint"}
PRIORITIES = {"A", "B"}

SOURCE_TITLE_PINS = {
    # UCT-005 G2-A: six canonical new works; STOC 2026 retained as LIT-072.
    "doi:10.1007/978-3-032-01878-6_6": "Merkle Mountain Ranges are Optimal: On Witness Update Frequency for Cryptographic Accumulators",
    "doi:10.1007/978-3-032-25330-9_7": "Lower Bounding Update Frequency in Short Accumulators and Vector Commitments",
    "doi:10.4230/LIPIcs.ITCS.2026.71": "Lower Bounds on FSS from Dynamic Data Structures",
    "doi:10.1007/978-3-642-00457-5_30": "How Efficient Can Memory Checking Be?",
    "publisher:iacr:2025-110": "Verification-efficient Homomorphic Signatures for Verifiable Computation over Data Streams",
    "doi:10.1007/978-3-642-14712-8_11": "On the Impossibility of Batch Update for Cryptographic Accumulators",
    # INDEX-001 G0: original source identity pins (six new works; no aliases duplicated).
    "doi:10.1137/S009753970240481X": "Optimal External Memory Interval Management",
    "doi:10.1137/110842211": "The Limits of Buffering: A Tight Lower Bound for Dynamic Membership in the External Memory Model",
    "doi:10.1109/FOCS57990.2023.00112": "Tight Cell-Probe Lower Bounds for Dynamic Succinct Dictionaries",
    "doi:10.1002/spe.3433": "Practical Adaptive Dynamic Bitvectors",
    "arxiv:2608.06066": "Dynamic Entropy-Encoded Arrays in O(1) Time with Nearly Optimal Space",
    "doi:10.1145/3654978": "Structural Designs Meet Optimality: Exploring Optimized LSM-tree Structures in a Colossal Configuration Space",
    # IMPORT-004: official source/title pins 2025–2026.
    "doi:10.4230/LIPIcs.ICALP.2025.123": "New and Improved Bounds for Markov Paging",
    "doi:10.1145/3717823.3718217": "Tight Results for Online Convex Paging",
    "doi:10.1145/3717823.3718131": "The Cost of Consistency: Submodular Maximization with Constant Recourse",
    "doi:10.4230/LIPIcs.ICALP.2025.111": "A Simple Dynamic Spanner via APSP",
    "doi:10.4230/LIPIcs.ICALP.2025.92": "Fully Dynamic Algorithms for Transitive Reduction",
    "doi:10.4230/LIPIcs.ICALP.2025.77": "Minimizing Recourse in an Adaptive Balls and Bins Game",
    "doi:10.1145/3717823.3718168": "Bounded Edit Distance: Optimal Static and Dynamic Algorithms for Small Integer Weights",
    "usenix:fast25:zhou-wenbin": "3L-Cache: Low Overhead and Precise Learning-based Eviction Policy for Caches",
    "usenix:osdi25:lyerly": "Skybridge: Bounded Staleness for Distributed Caches",
    "usenix:osdi25:park-sujin": "Principles and Methodologies for Serial Performance Optimization",
    "usenix:osdi26:li-liujia": "Merlin: An Efficient Adaptive Cache Eviction Algorithm via Fine-Grained Characterization",
    "usenix:osdi26:xia": "Learning-Augmented Heuristics: Simple Yet Smart, Robust and Interpretable Cache Eviction",
    "usenix:osdi26:mao-ziming-writeguards": "WriteGuards: Distributed Storage Support for Strongly Consistent Caches",
    "usenix:osdi26:xie-yizheng": "Incr: Faster Re-Execution via Bolt-On Incrementalization",
    "usenix:osdi26:yang-zhijun": "FORGE: Mitigating Synchronization Amplification for Memory-Disaggregated Caching Systems",
    "usenix:fast26:zhao": "\"Range as a Key\" is the Key! Fast and Compact Cloud Block Store Index with RASK",
    "usenix:fast26:ren": "Holistic and Automated Task Scheduling for Distributed LSM-tree-based Storage",
    "doi:10.1109/SFCS.1991.185352": "Checking the Correctness of Memories",
    "doi:10.1145/3618260.3649686": "Memory Checking Requires Logarithmic Overhead",
    "doi:10.1007/978-3-031-91092-0_11": "The Complexity of Memory Checking with Covert Security",
    "doi:10.4230/LIPIcs.AFT.2023.29": "Vector Commitments with Efficient Updates",
    # Authoritative arXiv title checks: forbid a paper ID being paired with
    # a hallucinated or different publication title.
    "arxiv:2501.01046": "SEDD: Scalable and Efficient Dataset Deduplication with GPUs",
    "arxiv:1507.00954": "Bounds and Constructions for overline-3-Separable Codes with Length 3",
    "arxiv:2509.11121": "The Chonkers Algorithm: Content-Defined Chunking with Provable Strict Guarantees on Size and Locality",
    "arxiv:2609.14442": "Toward Optimal Time-Space Tradeoffs for Set Reconciliation",
    "arxiv:2607.11271": "OptFSST: Optimized FSST String Compression",
    "arxiv:2602.08692": "PBLean: Pseudo-Boolean Proof Certificates for Lean 4",
    "arxiv:2607.00563": "Certificate-Carrying Transformation of Event-Driven Block Programs",
    "arxiv:2606.09600": "Formal Foundations and Proof-Carrying Certificates for q-ary Covering Codes in Lean 4",
    "arxiv:1503.07792": "Incremental Computation with Names",
    "arxiv:1407.3008": "Bigtable Merge Compaction",
    "arxiv:2011.02615": "Competitive Data-Structure Dynamization",
    "doi:10.4230/LIPIcs.CPM.2026.20": "Longest Common Extension of a Dynamic String in Parallel Constant Time",
    "arxiv:1211.1056": "How Robust are Linear Sketches to Adaptive Inputs?",
    "publisher:pmlr:cohen25c": "Breaking the Quadratic Barrier: Robust Cardinality Sketches for Adaptive Queries",
    "usenix:atc22:curtsinger": "Riker: Always-Correct and Fast Incremental Builds from Simple Specifications",
    "doi:10.4230/LIPIcs.MFCS.2024.46": "Query Maintenance Under Batch Changes with Small-Depth Circuits",
    "doi:10.4230/LIPIcs.ESA.2020.2": "Parallel Batch-Dynamic Trees via Change Propagation",
    "doi:10.4230/LIPIcs.ITCS.2020.56": "Instance Complexity and Unlabeled Certificates in the Decision Tree Model",
    "publisher:eccc:tr26-206": "Certification complexity of Boolean functions",
    "arxiv:2602.01042": "On Condensation of Block Sensitivity, Certificate Complexity and the $\\mathsf{AND}$ (and $\\mathsf{OR}$) Decision Tree Complexity",
    "doi:10.1016/S0304-3975(01)00144-X": "Complexity measures and decision tree complexity: a survey",
    "doi:10.1007/3-540-48658-5_22": "Incremental Cryptography: The Case of Hashing and Signing",
    "doi:10.1007/3-540-69053-0_13": "A New Paradigm for Collision-Free Hashing: Incrementality at Reduced Cost",
    # UCT-001 source-title identities (abstract/bibliography verified; not proof verified).
    "doi:10.1145/73007.73040": "The cell probe complexity of dynamic data structures",
    "doi:10.1137/S0097539705447256": "Logarithmic Lower Bounds in the Cell-Probe Model",
    "doi:10.1137/1.9781611973075.12": "On the Cell Probe Complexity of Dynamic Membership",
    "doi:10.1016/j.tcs.2007.02.058": "On dynamic bit-probe complexity",
    "doi:10.1016/j.tcs.2019.01.043": "New amortized cell-probe lower bounds for dynamic problems",
    "doi:10.1109/TIT.1973.1055037": "Noiseless coding of correlated information sources",
    "doi:10.1016/j.entcs.2005.11.043": "A Library for Self-Adjusting Computation",
    "doi:10.1002/rsa.20069": "Lower bounds for adaptive locally decodable codes",
    "publisher:eccc:tr26-047": "An $\\Omega((\\log n / \\log\\log n)^2)$ Cell-Probe Lower Bound for Dynamic Boolean Data Structures",
    "doi:10.1016/0095-8956(75)90067-2": "On cubical graphs",
    "doi:10.1016/S0019-9958(85)80012-7": "The complexity of cubical graphs",
    "doi:10.1016/0895-7177(88)90486-4": "Embeddings in hypercubes",
    "doi:10.1137/1.9781611975031.99": "Optimal Dynamic Strings",
    "doi:10.1016/j.tcs.2026.115746": "A textbook solution for dynamic strings",
    "publisher:c2sp:blake3-v1-0-0": "The BLAKE3 Hashing Framework (C2SP v1.0.0)",
    "doi:10.1007/s00224-026-10266-x": "Logarithmic-Time Internal Pattern Matching Queries in Compressed and Dynamic Texts",
    # UCT-002 sourced identities, NOT full theorem proofs.
    "doi:10.1007/978-3-642-54242-8_21": "Locally Updatable and Locally Decodable Codes",
    "arxiv:1305.3224": "Update-Efficiency and Local Repairability Limits for Capacity Approaching Codes",
    "doi:10.1145/2636924": "Annotations in Data Streams",
    "arxiv:1304.3816": "Annotations for Sparse Data Streams",
    "doi:10.4230/LIPIcs.ITCS.2024.53": "New Lower Bounds in Merlin-Arthur Communication and Graph Streaming Verification",
    "doi:10.1016/j.ic.2014.12.011": "Arthur–Merlin streaming complexity",
    "doi:10.1016/j.ic.2019.05.001": "Tight upper and lower bounds for leakage-resilient, locally decodable and updatable non-malleable codes",
    "doi:10.1214/aoms/1177729032": "Equivalent Comparisons of Experiments",
    "doi:10.1016/0095-8956(91)90097-4": "Extremal graphs with no C4\'s, C6\'s, or C10\'s",
    "arxiv:1111.3279": "An explicit formula for obtaining (q+1,8)-cages and others small regular graphs of girth 8",
    "doi:10.1090/proc/15673": "Constructing dense grid-free linear 3-graphs",
    "doi:10.1109/ISIT.2005.1523645": "Improved bounds on the size of sparse parity check matrices",
    "arxiv:2508.09841": "The Brown-Erdős-Sós conjecture in dense triple systems",
    "doi:10.37236/14115": "Triangle-Free Triple Systems",
    "doi:10.1137/090766619": "Bit-Probe Lower Bounds for Succinct Data Structures",
    # UCT-004 G2-A: certificate, adversary and 2026 R-vs-C original identities.
    "doi:10.1016/j.jcss.2007.06.020": "Quantum Certificate Complexity",
    "doi:10.1145/3442357": "All Classical Adversary Methods Are Equivalent for Total Functions",
    "arxiv:2609.15063": "Randomized Query Complexity Can Beat Certificate Complexity",
    "arxiv:2602.14716": "Grid-free linear hypergraphs via Cayley-Bacharach",
    "doi:10.1016/j.disc.2022.113025": "The linear Turán number of small triple systems or why is the wicket interesting?",
    "doi:10.1016/j.disc.2024.114029": "Wickets in 3-uniform hypergraphs",
    "doi:10.1006/jctb.2002.2123": "The Size of Bipartite Graphs with a Given Girth",
    "doi:10.1137/20M1325769": "New Turán Exponents for Two Extremal Hypergraph Problems",
    "doi:10.1007/s00493-008-2195-2": "Parity check matrices and product representations of squares",
    "arxiv:2609.39680": "Additive codes arising from hypergraphs",
    # G2-C original certification and PCPP source identities.
    "arxiv:2609.26757": "Certification complexity of Boolean functions",
    "doi:10.1145/1595391.1595394": "Sound 3-Query PCPPs Are Long",
    # G2-D source statement spotchecks (classical PPZ/MFCS).
    "doi:10.4086/cjtcs.1999.011": "Satisfiability Coding Lemma",
    "doi:10.4230/LIPIcs.MFCS.2022.47": "CNF Encodings of Parity",
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
        if ident in NEW_2026_IDS:
            check(e.get("year") == 2026, f"{ident}: non-2026 cohort entry")
            check(e.get("publication_stage") in PUBLICATION_STAGES,
                  f"{ident}: unverified 2026 publication status")
            check(e.get("selection_priority") in PRIORITIES,
                  f"{ident}: missing 2026 selection priority")
            if e.get("publication_stage") == "peer_reviewed_proceedings":
                check(ref.startswith("doi:"), f"{ident}: proceedings DOI missing")
            check(all(o.get("kind") == "model_overlap" for o in e.get("mentioned_in", [])),
                  f"{ident}: invented existing citation; new survey must use model_overlap")

        if ident in VENUE_2026_IDS:
            check(e.get("year") == 2026, f"{ident}: venue-2026 cohort has non-2026 work")
            check(e.get("publication_stage") == "peer_reviewed_proceedings",
                  f"{ident}: 2026 venue cohort publication status incorrect")
            check(e.get("selection_priority") in PRIORITIES,
                  f"{ident}: 2026 venue cohort missing source priority")
            check(e.get("venue") in {"STOC 2026", "ICALP 2026", "EuroSys 2026"},
                  f"{ident}: 2026 venue cohort unknown venue")
            check(bool(URL.fullmatch(e.get("source_listing_url", ""))),
                  f"{ident}: primary 2026 venue URL missing")
            expected_listing = {
                "STOC 2026": "https://acm-stoc.org/stoc2026/toc.html",
                "ICALP 2026": ("https://drops.dagstuhl.de/entities/document/" + ref[4:]
                               if ref.startswith("doi:") else ""),
                "EuroSys 2026": "https://2026.eurosys.org/papers.html",
            }
            check(e.get("source_listing_url") ==
                  expected_listing.get(e.get("venue")),
                  f"{ident}: primary 2026 listing/identity mismatch")
            check(e.get("verification") in {"publisher_abstract_checked",
                                             "publisher_bibliography_checked"},
                  f"{ident}: unsupported 2026 full-text verification")
            check(e.get("source_access") in {
                "official_conference_toc_abstract_linked_doi",
                "publisher_article_abstract_and_bibliography_checked",
                "conference_paper_list_and_delsk_fulltext_review"},
                  f"{ident}: unknown 2026 source access")
            check(all(o.get("kind") == "model_overlap"
                      for o in e.get("mentioned_in", [])),
                  f"{ident}: false explicit citation for imported 2026 paper")

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
            if "source_sha" in origin:
                check(bool(SHA.fullmatch(origin["source_sha"])),
                      f"{ident}: origin pin SHA malformed")
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
            f"https://github.com/{source['repo']}/blob/{origin.get('source_sha', source['sha'])}/{path})")


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
                *([f"**Первоисточник / издательский список:** "
                    f"[{e['venue']}]({e['source_listing_url']}) · "
                    f"**Доступ:** `{e['source_access']}`", ""]
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
