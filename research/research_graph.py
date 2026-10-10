#!/usr/bin/env python3
"""Mathlab research knowledge graph: offline deterministic metadata + retrieval.

The canonical registries remain authoritative. Graph relations never assert
a new theorem, a proof implication, scientific novelty, or current GitHub CI.
No network requests, external Python packages, embeddings, or API keys.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict, deque
import hashlib
import json
from pathlib import Path
from urllib.parse import quote
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CURATION = ROOT / "docs/research/graph/curation.json"
CATALOG = ROOT / "docs/research/catalog/registry.json"
LITERATURE = ROOT / "docs/research/catalog/literature.json"
TREE = ROOT / "docs/research/UCT-005-THEOREM-TREE.json"
KNOWN = ROOT / "docs/research/KNOWN-AND-STOPPED-RESEARCH.json"
BRIDGES = ROOT / "docs/research/UCT-005-G4-TYPED-BRIDGES.json"
GENEALOGY = ROOT / "docs/research/IMPORT-012-SOURCE-GENEALOGY.json"
STATUS = ROOT / "docs/research/RESEARCH-STATUS-REGISTRY.json"
ISSUES = ROOT / "docs/research/ISSUE-TRIAGE-SNAPSHOT.json"
DEFAULT_OUT = ROOT / ".work/research-graph"
WORDS = re.compile(r"[^\W_]+", re.UNICODE)
HEAD = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.M)
LIT_REF = re.compile(r"\bLIT-[0-9]{3}\b")
ID_REF = re.compile(r"\b(?:ML|DM|DL|OM)-[0-9]{3}\b")
POLICY = "All edges are provenance, organizational, source-context or search relations. No edge certifies theorem implication, freshness, novelty, physical page or cryptographic security."


def read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:20]


def terms(value: str) -> list[str]:
    return [s.casefold() for s in WORDS.findall(value)]


def check(condition: bool, explanation: str) -> None:
    if not condition:
        raise ValueError(explanation)


def safe_path(path: str) -> Path:
    check(isinstance(path, str) and path and "\\" not in path
          and not path.startswith("/") and ".." not in Path(path).parts,
          f"unsafe path: {path}")
    return ROOT / path


def validate_curation(meta: dict) -> None:
    required = {"schema", "policy", "taxonomy", "issue_anchors",
                "document_annotations", "relation_classes"}
    check(isinstance(meta, dict) and set(meta) == required,
          "curation schema root keys drift")
    check(meta["schema"] == "mathlab.research-graph-curation.v1",
          "unsupported curation version")
    check("No graph edge" in meta["policy"] and "proof" in meta["policy"],
          "curation must disclaim proof transfer")
    relations = meta["relation_classes"]
    check(isinstance(relations, dict) and relations,
          "missing edge vocabulary")
    allowed = {"provenance", "index_only", "classification",
               "semantic_non_implication", "organization_non_implication",
               "source_audited_non_implication", "ownership_non_implication",
               "classification_non_implication", "model_overlap_non_implication"}
    check(set(relations.values()).issubset(allowed),
          "unsupported or unsafe relation semantics")
    tag_ids: set[str] = set()
    alias_owner: dict[str, str] = {}
    for tag in meta["taxonomy"]:
        check(set(tag) == {"id", "prefLabel", "aliases", "broader"},
              "invalid taxonomy fields")
        tid = tag["id"]
        check(re.fullmatch(r"[a-z][a-z0-9-]*", tid) is not None
              and tid not in tag_ids, "duplicate/invalid concept ID")
        tag_ids.add(tid)
        check(isinstance(tag["aliases"], list)
              and all(isinstance(x, str) and x.strip()
                      for x in tag["aliases"]), "bad concept aliases")
        for alias in [tag["prefLabel"], *tag["aliases"]]:
            key = alias.casefold().strip()
            check(key not in alias_owner or alias_owner[key] == tid,
                  "cross-concept alias collision: " + alias)
            alias_owner[key] = tid
    issue_anchors: set[tuple] = set()
    for anchor in meta["issue_anchors"]:
        check(set(anchor) == {"issue", "target", "relation", "evidence_path"},
              "unknown issue anchor field")
        pair = (anchor["issue"], anchor["target"], anchor["relation"])
        check(type(anchor["issue"]) is int and anchor["issue"] > 0
              and pair not in issue_anchors, "duplicate/invalid issue anchor")
        issue_anchors.add(pair)
        check(anchor["relation"] in ("TRACKS_RESEARCH", "CURATES_BRIDGE_ATLAS"),
              "unsafe issue anchor relation")
        check(safe_path(anchor["evidence_path"]).is_file(),
              "missing issue anchor evidence")
    doc_paths: set[str] = set()
    for item in meta["document_annotations"]:
        check(set(item) == {"path", "tags", "aliases", "focus"},
              "unknown document annotation field")
        path = item["path"]
        check(path not in doc_paths and safe_path(path).is_file(),
              "duplicate/absent annotated document: " + path)
        doc_paths.add(path)
        check(all(tag in tag_ids for tag in item["tags"]),
              "unregistered document topic")
        check(all(isinstance(s, str) and s for s in item["aliases"]),
              "invalid document aliases")
        check(bool(item["focus"]), "missing annotated document focus")


class Graph:
    def __init__(self):
        self.nodes: dict[str, dict] = {}
        self.edges: dict[str, dict] = {}
        self.chunks: list[dict] = []
        self.relations: dict[str, str] = {}

    def node(self, node_id: str, kind: str, title: str, *, summary: str = "",
             status: str = "", tags: list[str] | None = None,
             path: str = "", aliases: list[str] | None = None,
             limitations: str = "", provenance: str = "") -> None:
        check(isinstance(node_id, str) and node_id
              and node_id not in self.nodes, f"duplicate graph node: {node_id}")
        self.nodes[node_id] = {
            "id": node_id, "kind": kind, "title": title,
            "summary": summary, "status": status, "tags": sorted(set(tags or [])),
            "path": path, "aliases": sorted(set(aliases or [])),
            "limitations": limitations, "provenance": provenance
        }

    def edge(self, source: str, target: str, relation: str, *,
             source_path: str, qualifier: str = "") -> None:
        check(relation in self.relations, f"unregistered edge class: {relation}")
        check(source in self.nodes and target in self.nodes,
              f"dangling edge {source} -> {target} [{relation}]")
        check(source != target, f"self-link: {source}")
        safe_path(source_path)
        check(safe_path(source_path).is_file(), f"absent edge evidence: {source_path}")
        key = digest(json.dumps([source, target, relation, source_path, qualifier],
                                ensure_ascii=False))
        if key in self.edges:
            return
        self.edges[key] = {"id": "E:" + key, "from": source, "to": target,
                           "relation": relation,
                           "semantics": self.relations[relation],
                           "evidence_path": source_path, "qualifier": qualifier}

    def doc(self, path: str) -> str | None:
        target = safe_path(path)
        if not target.is_file():
            return None
        doc_id = "DOC:" + path
        if doc_id not in self.nodes:
            name = target.stem.replace("-", " ").replace("_", " ")
            if target.suffix.lower() == ".md":
                raw = target.read_text(encoding="utf-8")
                m = HEAD.search(raw)
                if m:
                    name = m.group(2).strip()
            self.node(doc_id, "artifact", name[:240], path=path,
                      provenance="filesystem:repository-artifact")
        return doc_id

    def document(self, source: str, path: str, provenance: str) -> None:
        doc_id = self.doc(path)
        if doc_id:
            self.edge(source, doc_id, "DOCUMENTED_AT", source_path=provenance)

    def tag(self, source: str, label: str, provenance: str) -> None:
        check(bool(label) and re.fullmatch(r"[\w-]+", label, re.UNICODE) is not None,
              f"bad concept tag {label}")
        node_id = "TAG:" + label
        if node_id not in self.nodes:
            self.node(node_id, "concept", label)
        # Tag edges are authoritative for graph topology, and facets are a
        # derived materialized view for lexical/FTS retrieval. Keep both synced.
        self.nodes[source]["tags"] = sorted(set(
            self.nodes[source]["tags"] + [label]))
        self.edge(source, node_id, "TAGGED_WITH", source_path=provenance)


def ingest() -> Graph:
    graph = Graph()
    curation = read(CURATION)
    validate_curation(curation)
    graph.relations = curation["relation_classes"]
    check(all("implication" not in v or "non_implication" in v
              for v in graph.relations.values()), "edge semantics allow implication")
    catalog = read(CATALOG)
    literature = read(LITERATURE)
    tree = read(TREE)
    known = read(KNOWN)
    bridges = read(BRIDGES)
    genealogy = read(GENEALOGY)
    check(tree["root"] == "UCT005" and tree["root_novelty"] == "OPEN_UNPROVED",
          "UCT-005 theorem root must be OPEN_UNPROVED")

    # All canonical IDs are preserved exactly; prefix only distinguishes node types.
    for r in catalog["entries"]:
        graph.node("R:" + r["id"], "internal_research", r["title"],
                   summary=r.get("summary_ru", ""), status=r.get("status", ""),
                   tags=r.get("topics", []),
                   path=r["source"]["path"],
                   limitations=r.get("limitations_ru", ""),
                   provenance="docs/research/catalog/registry.json")
        graph.nodes["R:" + r["id"]]["repository"] = r["repository"]
        graph.nodes["R:" + r["id"]]["source_revision"] = r["source"].get("revision", "")
        graph.nodes["R:" + r["id"]]["source_permalink"] = r["source"].get("permalink", "")
    identities: set[str] = set()
    for r in literature["entries"]:
        identity = r["identity"].casefold().strip()
        check(identity not in identities, "duplicate literature identity: " + identity)
        identities.add(identity)
        graph.node("P:" + r["id"], "publication", r["title"],
                   summary=r.get("summary_ru", ""), status=r.get("verification", ""),
                   tags=[r.get("track", "")],
                   aliases=[r["identity"], r.get("primary_url", "")],
                   limitations=r.get("limits_ru", ""),
                   provenance="docs/research/catalog/literature.json")
        pub = graph.nodes["P:" + r["id"]]
        pub["identity"] = r["identity"]
        pub["primary_url"] = r["primary_url"]
        pub["full_proof_verified"] = r.get("full_proof_verified", False)
        pub["independent_reproduction"] = r.get("independent_reproduction", False)
    for r in tree["nodes"]:
        graph.node("T:" + r["id"], "theorem_tree", r["id"].replace("_", " "),
                   status=r["status"], summary="UCT-005 typed theorem-tree node: "
                   + r.get("kind", ""), path=r.get("source", ""),
                   provenance="docs/research/UCT-005-THEOREM-TREE.json")
    for r in known["entries"]:
        graph.node("K:" + r["id"], "prior_art_or_stopped", r["title"],
                   summary=r.get("scope", ""), status=r.get("disposition", ""),
                   tags=[r.get("area", "").lower()],
                   limitations=r.get("do_not_repeat", ""),
                   provenance="docs/research/KNOWN-AND-STOPPED-RESEARCH.json")
    graph.node("B:G4-ATLAS", "bridge_atlas", "UCT-005 G4 typed bridge atlas",
               summary="Typed reductions, countermodels, non-transfers; not a second root proof",
               status=bridges["status"], provenance="docs/research/UCT-005-G4-TYPED-BRIDGES.json")
    for r in bridges["bridges"]:
        graph.node("B:" + r["id"], "typed_bridge", r["source"] + " → " + r["target"],
                   summary=r.get("assumptions", "") + "; " + r.get("resource_map", ""),
                   status=r["classification"], limitations=r.get("non_transfer", ""),
                   provenance="docs/research/UCT-005-G4-TYPED-BRIDGES.json")
    graph.node("ISSUE:105", "issue", "UCT-005 root issue",
               status="SNAPSHOT_ONLY", provenance="docs/research/graph/curation.json")
    for a in curation["issue_anchors"]:
        ident = "ISSUE:" + str(a["issue"])
        if ident not in graph.nodes:
            graph.node(ident, "issue", "Mathlab issue #" + str(a["issue"]),
                       status="SNAPSHOT_ONLY",
                       provenance="docs/research/graph/curation.json")
    if ISSUES.is_file():
        snapshot = read(ISSUES)
        for r in snapshot["issues"]:
            ident = "ISSUE:" + str(r["number"])
            if ident not in graph.nodes:
                graph.node(ident, "issue", r["title"], summary=r["acceptance_gate"],
                           status=r["state_at_snapshot"],
                           provenance="docs/research/ISSUE-TRIAGE-SNAPSHOT.json")
            else:
                graph.nodes[ident]["title"] = r["title"]
                graph.nodes[ident]["summary"] = r["acceptance_gate"]
                graph.nodes[ident]["status"] = r["state_at_snapshot"]
                graph.nodes[ident]["provenance"] = "docs/research/ISSUE-TRIAGE-SNAPSHOT.json"
    if STATUS.is_file():
        status = read(STATUS)
        for r in status["programs"]:
            ident = "S:" + r["id"]
            graph.node(ident, "research_gate", r["id"],
                       summary=r.get("next_falsifier", ""),
                       status=r["scientific_status"],
                       provenance="docs/research/RESEARCH-STATUS-REGISTRY.json")
            graph.nodes[ident].update({
                "proof_grade": r.get("proof_grade", ""),
                "source_audit_grade": r.get("source_audit_grade", ""),
                "novelty_status": r.get("novelty_status", ""),
                "model_id": r.get("model_id", ""),
                "ci_snapshot": r.get("ci", {}),
                "last_verified_sha": r.get("last_verified_sha", "")
            })
            issue = "ISSUE:" + str(r["owner_issue"])
            if issue not in graph.nodes:
                graph.node(issue, "issue", "Mathlab issue #" + str(r["owner_issue"]),
                           status="REFERENCE_ONLY",
                           provenance="docs/research/RESEARCH-STATUS-REGISTRY.json")
            graph.edge(issue, ident, "TRACKS_RESEARCH",
                       source_path="docs/research/RESEARCH-STATUS-REGISTRY.json")

    # Graph of canonical relations: semantics remain explicitly non-implicative.
    for r in catalog["entries"]:
        rid = "R:" + r["id"]
        # Cross-repository source paths are not Mathlab-local artifacts.
        if r["repository"] == "MATHLAB":
            local = r["source"]["path"]
            check(graph.doc(local) is not None,
                  "canonical Mathlab study source file missing: " + local)
            graph.document(rid, local,
                           "docs/research/catalog/registry.json")
        for tag in r.get("topics", []):
            graph.tag(rid, tag, "docs/research/catalog/registry.json")
        for rel in r.get("related", []):
            graph.edge(rid, "R:" + rel["id"], "CATALOG_RELATED",
                       source_path="docs/research/catalog/registry.json",
                       qualifier=rel["relation"])
    for r in literature["entries"]:
        pid = "P:" + r["id"]
        if r.get("track"):
            graph.tag(pid, r["track"], "docs/research/catalog/literature.json")
        for target_id in r.get("maps_to", []):
            # Literature model relevance, NOT a proved theorem implication.
            graph.edge(pid, "R:" + target_id, "MAPS_TO_RESEARCH",
                       source_path="docs/research/catalog/literature.json")
        for mention in r.get("mentioned_in", []):
            if mention.get("repo") == "MATHLAB":
                did = graph.doc(mention["path"])
                check(did is not None,
                      "canonical literature mention has missing Mathlab file: "
                      + mention["path"])
                graph.edge(pid, did, "MENTIONED_IN",
                           source_path="docs/research/catalog/literature.json",
                           qualifier=mention.get("kind", ""))
    for r in known["entries"]:
        kid = "K:" + r["id"]
        for path in r.get("authority", []):
            graph.document(kid, path, "docs/research/KNOWN-AND-STOPPED-RESEARCH.json")
        if r.get("area"):
            graph.tag(kid, r["area"].lower(), "docs/research/KNOWN-AND-STOPPED-RESEARCH.json")
    for r in tree["nodes"]:
        if r.get("source"):
            graph.document("T:" + r["id"], r["source"],
                           "docs/research/UCT-005-THEOREM-TREE.json")
    for r in tree["edges"]:
        graph.edge("T:" + r["parent"], "T:" + r["child"], "ORG_TREE",
                   source_path="docs/research/UCT-005-THEOREM-TREE.json",
                   qualifier=r["relation"])
    for r in genealogy["edges"]:
        left = ("P:" if r["from"].startswith("LIT-") else "R:") + r["from"]
        right = ("P:" if r["to"].startswith("LIT-") else "R:") + r["to"]
        graph.edge(left, right, "SOURCE_GENEALOGY",
                   source_path="docs/research/IMPORT-012-SOURCE-GENEALOGY.json",
                   qualifier=r["type"])
    for r in bridges["bridges"]:
        graph.edge("B:G4-ATLAS", "B:" + r["id"], "BRIDGE_OF_ATLAS",
                   source_path="docs/research/UCT-005-G4-TYPED-BRIDGES.json",
                   qualifier=r["classification"])
    for a in curation["issue_anchors"]:
        graph.edge("ISSUE:" + str(a["issue"]), a["target"], a["relation"],
                   source_path=a["evidence_path"])
    for r in curation["taxonomy"]:
        ident = "TAG:" + r["id"]
        if ident not in graph.nodes:
            graph.node(ident, "concept", r["prefLabel"], aliases=r["aliases"],
                       provenance="docs/research/graph/curation.json")
        else:
            graph.nodes[ident]["title"] = r["prefLabel"]
            graph.nodes[ident]["aliases"] = sorted(set(r["aliases"]))
        for higher in r["broader"]:
            if "TAG:" + higher not in graph.nodes:
                graph.node("TAG:" + higher, "concept", higher,
                           provenance="docs/research/graph/curation.json")
            graph.edge(ident, "TAG:" + higher, "BROADER_TAG",
                       source_path="docs/research/graph/curation.json")
    for r in curation["document_annotations"]:
        docid = graph.doc(r["path"])
        check(docid is not None, "annotation path missing: " + r["path"])
        graph.nodes[docid]["aliases"] = sorted(set(
            graph.nodes[docid]["aliases"] + r["aliases"]))
        for tag in r["tags"]:
            graph.tag(docid, tag, "docs/research/graph/curation.json")
        for focus in r["focus"]:
            graph.edge(docid, focus, "CURATED_FOCUS",
                       source_path="docs/research/graph/curation.json")

    # New Markdown files become searchable automatically, even without frontmatter.
    for file in sorted((ROOT / "docs/research").rglob("*.md")):
        rel = file.relative_to(ROOT).as_posix()
        docid = graph.doc(rel)
        if docid is None:
            continue
        raw = file.read_text(encoding="utf-8")
        # Zero-maintenance, index-only discovery of explicit canonical IDs.
        # A textual mention is NOT a scholarly citation audit or theorem transfer.
        lexical = {}
        for regex, prefix in ((LIT_REF, "P:"), (ID_REF, "R:")):
            for match in regex.finditer(raw):
                target_id = prefix + match.group()
                if target_id in graph.nodes and target_id not in lexical:
                    lexical[target_id] = raw.count("\n", 0, match.start()) + 1
        for target_id, first_line in sorted(lexical.items()):
            graph.edge(docid, target_id, "TEXT_MENTIONS_ID",
                       source_path=rel,
                       qualifier="line=" + str(first_line)
                       + ";AUTOMATIC_TEXT_MENTION_NOT_VERIFIED_CITATION")
        matches = list(HEAD.finditer(raw))
        sections: list[tuple[str, str, int]] = []
        if not matches:
            sections = [("", raw, 0)]
        else:
            if raw[:matches[0].start()].strip():
                sections.append(("", raw[:matches[0].start()], 0))
            for i, hit in enumerate(matches):
                end = matches[i+1].start() if i+1 < len(matches) else len(raw)
                sections.append((hit.group(2).strip(), raw[hit.start():end],
                                 hit.start()))
        seen_headings: Counter = Counter()
        for heading, section, section_start in sections:
            seen_headings[heading] += 1
            # Character windows, fixed overlap. These chunks are retrieval aids,
            # never immutable claim IDs or independent evidence of a theorem.
            step = 2200
            for n, offset in enumerate(range(0, len(section), step)):
                local_start = max(0, offset-160)
                raw_part = section[local_start:offset+step]
                if not raw_part.strip():
                    continue
                # Preserve exact text bytes for trustworthy line/fragment citation.
                begin = section_start + local_start
                finish = begin + len(raw_part)
                part = raw_part
                cid = "C:" + digest(rel + "|" + heading + "|" +
                                    str(seen_headings[heading]) + "|" + str(n))
                graph.chunks.append({"id": cid, "doc_id": docid, "path": rel,
                                     "heading": heading, "part": n,
                                     "line_start": raw.count("\n", 0, begin) + 1,
                                     "line_end": raw.count("\n", 0, finish) + 1,
                                     "text": part, "sha256": hashlib.sha256(
                                         part.encode("utf-8")).hexdigest()})
    # Document tags inherit connected research metadata for retrieval facets.
    for edge in graph.edges.values():
        if edge["relation"] == "DOCUMENTED_AT":
            source = graph.nodes[edge["from"]]
            doc = graph.nodes[edge["to"]]
            doc["tags"] = sorted(set(doc["tags"] + source["tags"]))
    return graph


def validate(graph: Graph) -> dict:
    check(graph.nodes["T:UCT005"]["status"] == "OPEN_UNPROVED",
          "scientific root promoted without proof")
    for e in graph.edges.values():
        check(e["from"] in graph.nodes and e["to"] in graph.nodes, "dangling edge")
        check("implication" not in e["semantics"] or "non_implication" in e["semantics"],
              "edge claims a proof implication")
    by_chunk = [x["id"] for x in graph.chunks]
    check(len(by_chunk) == len(set(by_chunk)), "duplicate chunk ID")
    check(all(x["doc_id"] in graph.nodes for x in graph.chunks),
          "chunk points to missing document")
    # Organization tree is a DAG. Citation/semantic overlaps MAY contain cycles.
    adjacency: dict[str, list[str]] = defaultdict(list)
    for e in graph.edges.values():
        if e["relation"] == "ORG_TREE":
            adjacency[e["from"]].append(e["to"])
    visiting: set[str] = set()
    done: set[str] = set()

    def walk(node: str) -> None:
        if node in visiting:
            raise ValueError("cyclic theorem organization at " + node)
        if node in done:
            return
        visiting.add(node)
        for nxt in adjacency[node]:
            walk(nxt)
        visiting.remove(node)
        done.add(node)

    for node in adjacency:
        walk(node)
    kinds = Counter(r["kind"] for r in graph.nodes.values())
    by_relation = Counter(e["relation"] for e in graph.edges.values())
    return {"nodes": len(graph.nodes), "edges": len(graph.edges),
            "chunks": len(graph.chunks), "by_kind": dict(sorted(kinds.items())),
            "by_relation": dict(sorted(by_relation.items())),
            "root_scientific_status": "OPEN_UNPROVED",
            "guarantee": POLICY}


def neighbors(graph: Graph, anchor: str, hops: int = 1, *, max_nodes: int = 80,
              direction: str = "both", relations: set[str] | None = None) -> dict:
    check(anchor in graph.nodes, "unknown node ID: " + anchor)
    check(0 <= hops <= 4, "hops must be within 0..4")
    check(1 <= max_nodes <= 1000, "max_nodes must be within 1..1000")
    check(direction in ("in", "out", "both"), "bad direction")
    if relations is not None:
        check(relations <= set(graph.relations), "unknown relation filter")
    adj: dict[str, list[tuple[str, dict]]] = defaultdict(list)
    for e in graph.edges.values():
        if relations is not None and e["relation"] not in relations:
            continue
        if direction in ("both", "out"):
            adj[e["from"]].append((e["to"], e))
        if direction in ("both", "in"):
            adj[e["to"]].append((e["from"], e))
    queue = deque([(anchor, 0)])
    found = {anchor}
    edges: dict[str, dict] = {}
    while queue and len(found) < max_nodes:
        node, level = queue.popleft()
        if level == hops:
            continue
        for nxt, edge in sorted(adj[node], key=lambda p: (p[0], p[1]["id"])):
            edges[edge["id"]] = edge
            if nxt not in found and len(found) < max_nodes:
                found.add(nxt)
                queue.append((nxt, level+1))
    kept = [edges[e] for e in sorted(edges)
            if edges[e]["from"] in found and edges[e]["to"] in found]
    return {"anchor": anchor, "direction": direction,
            "relations": sorted(relations) if relations is not None else None,
            "max_nodes": max_nodes,
            "nodes": [graph.nodes[n] for n in sorted(found)],
            "edges": kept, "semantics": POLICY}


def impact(graph: Graph, source_id: str, max_depth: int = 2,
           limit: int = 100) -> dict:
    """Conservative influence discovery, not a causal or mathematical proof.

    Traverse *only* evidence-bearing relations relevant to an imported paper
    or internal study. Reversed citation mentions are tagged as text-only.
    Paths never inherit the proof status of another node.
    """
    check(source_id in graph.nodes, "unknown canonical impact source: " + source_id)
    check(graph.nodes[source_id]["kind"] in
          ("publication", "internal_research", "theorem_tree"),
          "impact source must be a publication or research record")
    check(1 <= max_depth <= 3, "impact depth must be 1..3")
    check(1 <= limit <= 1000, "impact limit must be 1..1000")
    allowed = {
        "MAPS_TO_RESEARCH": ("forward", "CURATED_MODEL_OVERLAP_NOT_PROOF"),
        "SOURCE_GENEALOGY": ("forward", "SOURCE_RELATION_NOT_PROOF"),
        "CATALOG_RELATED": ("forward", "CATALOG_RELATION_NOT_PROOF"),
        "DOCUMENTED_AT": ("forward", "DOCUMENT_POINTER_ONLY"),
        "MENTIONED_IN": ("forward", "CATALOG_MENTION_NOT_PROOF"),
        "TEXT_MENTIONS_ID": ("reverse", "UNVERIFIED_TEXT_MENTION")
    }
    adjacency: dict[str, list[tuple[str, dict, str, str]]] = defaultdict(list)
    for edge in graph.edges.values():
        kind = edge["relation"]
        if kind not in allowed:
            continue
        direction, grade = allowed[kind]
        if direction == "forward":
            adjacency[edge["from"]].append((edge["to"], edge, grade, "out"))
        else:
            # Docs point to cited IDs. For impact, query what docs mention
            # a changed paper/study, but never upgrade the mention.
            adjacency[edge["to"]].append((edge["from"], edge, grade, "reverse"))
    queue = deque([(source_id, [])])
    seen = {source_id}
    affected: list[dict] = []
    while queue and len(affected) < limit:
        current, path = queue.popleft()
        if len(path) >= max_depth:
            continue
        for node_id, edge, grade, traversal in sorted(
                adjacency[current], key=lambda row: (
                    row[0], row[1]["relation"], row[1]["id"])):
            if node_id in seen:
                continue
            seen.add(node_id)
            new_path = path + [{
                "edge_id": edge["id"], "relation": edge["relation"],
                "traversal": traversal, "grade": grade,
                "from": edge["from"], "to": edge["to"],
                "qualifier": edge["qualifier"],
                "evidence_path": edge["evidence_path"]
            }]
            target = graph.nodes[node_id]
            affected.append({
                "id": node_id, "kind": target["kind"],
                "title": target["title"], "status": target["status"],
                "depth": len(new_path), "path": new_path,
                "limitations": target["limitations"],
                "document_path": target["path"]
            })
            queue.append((node_id, new_path))
            if len(affected) >= limit:
                break
    return {
        "source": source_id, "max_depth": max_depth, "affected": affected,
        "count": len(affected),
        "is_complete_within_depth": (
            not queue or all(len(path) >= max_depth for _, path in queue)
        ),
        "semantics": "Potential review targets, not theorem implications, "
                     "verified citations, or causal dependencies."
    }


def search(graph: Graph, query: str, limit: int = 10, kind: str = "") -> dict:
    tokens = terms(query)
    check(tokens, "query must contain searchable words")
    check(1 <= limit <= 50, "limit must be 1..50")
    rows: list[dict] = []
    # Controlled, bilingual concept lookup. A matched RU/EN alias expands to
    # explicitly tagged documents; it never creates a semantic/proof edge.
    query_folded = query.casefold().strip()
    token_set = set(tokens)
    expanded_tags = set()
    for concept in graph.nodes.values():
        if concept["kind"] != "concept":
            continue
        labels = [concept["title"], *concept["aliases"]]
        if any(query_folded == label.casefold().strip() or
               (len(token_set) > 1 and token_set <= set(terms(label)))
               for label in labels):
            expanded_tags.add(concept["id"].removeprefix("TAG:"))
    # Explicit weights: title/ID > aliases > tags > abstract > body.
    for node in graph.nodes.values():
        if kind and node["kind"] != kind:
            continue
        pieces = [
            (node["id"].casefold(), 16),
            (node["title"].casefold(), 8),
            (" ".join(node["aliases"]).casefold(), 7),
            (" ".join(node["tags"]).casefold(), 5),
            (node["summary"].casefold(), 3),
            (node["limitations"].casefold(), 1)
        ]
        score = sum(weight * sum(1 for t in tokens if t in terms(text))
                    for text, weight in pieces)
        if query.casefold() in node["title"].casefold():
            score += 20
        if node["id"].casefold() == query.casefold():
            score += 200
        if expanded_tags.intersection(node["tags"]):
            score += 18
        if score:
            result = {"id": node["id"], "kind": node["kind"],
                      "title": node["title"], "status": node["status"],
                      "path": node["path"], "score": score,
                      "provenance": node["provenance"],
                      "limitations": node["limitations"]}
            # Evidence and freshness belong to the source's own registry;
            # omit absent fields instead of filling them with inferred grades.
            for field in ("identity", "primary_url", "full_proof_verified",
                          "independent_reproduction", "repository",
                          "source_revision", "source_permalink",
                          "proof_grade", "source_audit_grade", "novelty_status",
                          "model_id", "ci_snapshot", "last_verified_sha"):
                if field in node:
                    result[field] = node[field]
            rows.append(result)
    if not kind or kind == "chunk":
        for ch in graph.chunks:
            body = ch["text"]
            hit = len(set(tokens) & set(terms(body)))
            head_hits = len(set(tokens) & set(terms(ch["heading"])))
            if hit:
                rows.append({"id": ch["id"], "kind": "chunk",
                             "title": ch["heading"] or graph.nodes[ch["doc_id"]]["title"],
                             "status": "SEARCHABLE_TEXT_NOT_PROOF",
                             "path": ch["path"], "score": hit*2 + head_hits*8,
                             "parent_doc": ch["doc_id"], "sha256": ch["sha256"],
                             "line_start": ch["line_start"], "line_end": ch["line_end"],
                             "excerpt": body[:420], "provenance": ch["path"]})
    rows.sort(key=lambda row: (-row["score"], row["id"]))
    selected = rows[:limit]
    # Graph-aware second stage: attach short bidirectional, evidence-scoped
    # neighborhoods to the best matches. Never use graph distance as proof.
    by_anchor: dict[str, list[dict]] = defaultdict(list)
    for edge in graph.edges.values():
        by_anchor[edge["from"]].append({
            "id": edge["to"], "direction": "out",
            "relation": edge["relation"], "evidence_path": edge["evidence_path"],
            "semantics": edge["semantics"]})
        by_anchor[edge["to"]].append({
            "id": edge["from"], "direction": "in",
            "relation": edge["relation"], "evidence_path": edge["evidence_path"],
            "semantics": edge["semantics"]})
    for result in selected[:5]:
        node_id = result.get("parent_doc", result["id"])
        edges = by_anchor.get(node_id, [])
        # Prefer substantive/source edges over high-fanout taxonomy links.
        edges.sort(key=lambda x: (x["relation"] in
                                 ("TAGGED_WITH", "MENTIONED_IN"),
                                 x["id"], x["relation"]))
        result["graph_context"] = edges[:12]
    return {"query": query, "expanded_concepts": sorted(expanded_tags),
            "results": selected,
            "returned": len(selected), "matches": len(rows),
            "semantics": POLICY}


def export(graph: Graph, target: Path) -> dict:
    target.mkdir(parents=True, exist_ok=True)
    summary = validate(graph)
    nodes = [graph.nodes[key] for key in sorted(graph.nodes)]
    edges = [graph.edges[key] for key in sorted(graph.edges)]
    (target / "graph.json").write_text(json.dumps({
        "schema": "mathlab.research-graph.v1", "policy": POLICY,
        "source_of_truth": [str(x.relative_to(ROOT)) for x in
                            (CATALOG, LITERATURE, TREE, KNOWN, BRIDGES, GENEALOGY)],
        "summary": summary, "nodes": nodes, "edges": edges
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # JSON-LD 1.1 *projection*, not RO-Crate conformance or proof semantics.
    def iri(node_id: str) -> str:
        return "urn:mathlab:graph-node:" + quote(node_id, safe="")

    kind_to_type = {
        "publication": "schema:ScholarlyArticle",
        "concept": "schema:DefinedTerm",
        "artifact": "schema:DigitalDocument",
        "theorem_tree": "schema:CreativeWork",
        "typed_bridge": "schema:CreativeWork",
    }
    graph_ld = []
    for node in nodes:
        item = {
            "@id": iri(node["id"]),
            "@type": kind_to_type.get(node["kind"], "schema:CreativeWork"),
            "schema:name": node["title"],
            "mathlab:canonicalId": node["id"],
            "mathlab:kind": node["kind"],
            "mathlab:status": node["status"],
            "mathlab:provenancePath": node["provenance"]
        }
        if node.get("summary"):
            item["schema:description"] = node["summary"]
        if node.get("path"):
            item["mathlab:documentPath"] = node["path"]
        if node.get("limitations"):
            item["mathlab:limitations"] = node["limitations"]
        graph_ld.append(item)
    for edge in edges:
        graph_ld.append({
            "@id": "urn:mathlab:graph-edge:" + edge["id"][2:],
            "@type": "mathlab:TypedRelation",
            "mathlab:source": {"@id": iri(edge["from"])},
            "mathlab:target": {"@id": iri(edge["to"])},
            "mathlab:relationType": edge["relation"],
            "mathlab:nonProofSemantics": edge["semantics"],
            "mathlab:evidencePath": edge["evidence_path"],
            "mathlab:qualifier": edge["qualifier"]
        })
    (target / "graph.jsonld").write_text(json.dumps({
        "@context": {"@version": 1.1,
                     "schema": "https://schema.org/",
                     "mathlab": "https://github.com/definitely-stable/Mathlab/graph/v1#"},
        "@graph": graph_ld
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    input_paths = [CATALOG, LITERATURE, TREE, KNOWN, BRIDGES,
                   GENEALOGY, CURATION]
    # An index is reproducible only for a fixed *generator version* as
    # well as a fixed corpus. Include code/schema/evaluation sources.
    for rel in ("research/research_graph.py",
                "research/research_graph_fts.py",
                "research/research_graph_eval.py",
                "docs/research/graph/curation.schema.json",
                "docs/research/graph/retrieval-fixtures.json"):
        file = ROOT / rel
        if file.is_file():
            input_paths.append(file)
    if ISSUES.is_file():
        input_paths.append(ISSUES)
    if STATUS.is_file():
        input_paths.append(STATUS)
    input_paths.extend(sorted((ROOT / "docs/research").rglob("*.md")))
    manifest = {
        "schema": "mathlab.research-graph-input-hashes.v1",
        "rule": "Input and generator hashes only; NOT an exact GitHub HEAD/CI attestation.",
        "files": {
            path.relative_to(ROOT).as_posix():
                hashlib.sha256(path.read_bytes()).hexdigest()
            for path in input_paths
        }
    }
    (target / "manifest.json").write_text(json.dumps(
        manifest, ensure_ascii=False, sort_keys=True, indent=2
    ) + "\n", encoding="utf-8")
    reverse: dict[str, list[dict]] = defaultdict(list)
    forward: dict[str, list[dict]] = defaultdict(list)
    for e in edges:
        forward[e["from"]].append({"id": e["to"], "relation": e["relation"],
                                   "evidence_path": e["evidence_path"]})
        reverse[e["to"]].append({"id": e["from"], "relation": e["relation"],
                                 "evidence_path": e["evidence_path"]})
    (target / "adjacency.json").write_text(json.dumps({
        "schema": "mathlab.research-graph-adjacency.v1",
        "outbound": dict(sorted(forward.items())),
        "inbound": dict(sorted(reverse.items()))
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    linked_docs = {e["to"] for e in edges
                   if e["relation"] in ("DOCUMENTED_AT", "MENTIONED_IN",
                                         "CURATED_FOCUS")}
    unlinked = [
        {"id": n["id"], "path": n["path"], "title": n["title"]}
        for n in nodes if n["kind"] == "artifact"
        and n["path"].startswith("docs/research/")
        and n["path"].endswith(".md") and n["id"] not in linked_docs
    ]
    (target / "coverage.json").write_text(json.dumps({
        "schema": "mathlab.research-graph-coverage.v1",
        "note": "Unlinked Markdown remains fulltext searchable. It is not a claim that research is invalid.",
        "unlinked_markdown": unlinked,
        "unlinked_count": len(unlinked)
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (target / "retrieval.jsonl").open("w", encoding="utf-8") as stream:
        for r in nodes:
            stream.write(json.dumps({"type": "node", **r,
                                      "neighbors_out": forward.get(r["id"], []),
                                      "neighbors_in": reverse.get(r["id"], [])},
                                     ensure_ascii=False, sort_keys=True) + "\n")
        for r in graph.chunks:
            stream.write(json.dumps({"type": "chunk", **r},
                                     ensure_ascii=False, sort_keys=True) + "\n")
    md = ["# Mathlab research graph (generated)", "",
          "Graph is a discovery and provenance index, **not a proof system**.",
          f"Nodes: **{summary['nodes']}**; relations: **{summary['edges']}**;"
          f" retrieval chunks: **{summary['chunks']}**.", "",
          "## Node kinds", "", "| Kind | Count |", "| --- | ---: |"]
    for key, value in summary["by_kind"].items():
        md.append(f"| {key} | {value} |")
    md.extend(["", "Generated outputs: graph.json, graph.jsonld, adjacency.json, retrieval.jsonl, manifest.json, coverage.json.",
               "To search: python research/research_graph.py search GF5 --limit 10",
               "To traverse: python research/research_graph.py neighbors T:UCT005 --hops 2",
               "To regenerate: python research/research_graph.py build --out .work/research-graph",
               "Canonical catalogs remain authoritative; all snapshot statuses require live verification.",
               ""])
    (target / "INDEX.md").write_text("\n".join(md), encoding="utf-8")
    return summary


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    cmd = p.add_subparsers(dest="command", required=True)
    cmd.add_parser("validate")
    build = cmd.add_parser("build")
    build.add_argument("--out", default=str(DEFAULT_OUT))
    query = cmd.add_parser("search")
    query.add_argument("query", nargs="+")
    query.add_argument("--limit", type=int, default=10)
    query.add_argument("--kind", default="")
    impact_cmd = cmd.add_parser("impact")
    impact_cmd.add_argument("id", help="canonical source ID e.g. P:LIT-355")
    impact_cmd.add_argument("--depth", type=int, default=2)
    impact_cmd.add_argument("--limit", type=int, default=100)
    traverse = cmd.add_parser("neighbors")
    traverse.add_argument("id")
    traverse.add_argument("--hops", type=int, default=1)
    traverse.add_argument("--max-nodes", type=int, default=80)
    traverse.add_argument("--direction", choices=("in", "out", "both"),
                          default="both")
    traverse.add_argument("--relation", action="append",
                          help="repeatable edge-type filter; source-direction preserved")
    args = p.parse_args()
    try:
        graph = ingest()
        if args.command == "validate":
            output = validate(graph)
        elif args.command == "build":
            output = export(graph, Path(args.out))
        elif args.command == "search":
            output = search(graph, " ".join(args.query), args.limit, args.kind)
        elif args.command == "impact":
            output = impact(graph, args.id, args.depth, args.limit)
        else:
            output = neighbors(graph, args.id, args.hops,
                               max_nodes=args.max_nodes,
                               direction=args.direction,
                               relations=set(args.relation) if args.relation else None)
        print(json.dumps(output, ensure_ascii=False, sort_keys=True, indent=2))
        return 0
    except (KeyError, OSError, ValueError, TypeError) as exc:
        print("RESEARCH_GRAPH_FAIL:", str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
