#!/usr/bin/env python3
"""Optional incremental local FTS5 index for Mathlab graph/retrieval.jsonl.

SQLite is a *derived cache*, never a source of scientific claims. Does not
contact network or need embedding services. Built-in SQLite FTS5 required.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import sys

DEFAULT_JSONL = Path(".work/research-graph/retrieval.jsonl")
DEFAULT_DB = Path(".work/research-graph/retrieval.sqlite")
TOKEN = re.compile(r"[^\W_]+", re.UNICODE)


def canonical(value: dict) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def connect(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        conn.execute("CREATE VIRTUAL TABLE IF NOT EXISTS search_docs USING fts5("
                     "id UNINDEXED, title, aliases, tags, summary, content,"
                     "tokenize='unicode61')")
    except sqlite3.OperationalError as exc:
        conn.close()
        raise ValueError("SQLite FTS5 unavailable; use research_graph.py search") from exc
    conn.execute("CREATE TABLE IF NOT EXISTS records("
                 "id TEXT PRIMARY KEY, sha256 TEXT NOT NULL,"
                 "fts_rowid INTEGER NOT NULL UNIQUE, json TEXT NOT NULL)")
    return conn


def fields(obj: dict) -> tuple[str, str, str, str, str, str]:
    check_type = obj.get("type")
    if check_type == "node":
        return (obj["id"], obj["title"], " ".join(obj.get("aliases", [])),
                " ".join(obj.get("tags", [])), obj.get("summary", ""),
                obj.get("limitations", ""))
    if check_type == "chunk":
        return (obj["id"], obj.get("heading", ""), "", "",
                obj.get("path", ""), obj["text"])
    raise ValueError("unknown retrieval record type")


def sync(db: Path, input_file: Path) -> dict:
    if not input_file.is_file():
        raise ValueError("missing derived JSONL; run research_graph.py build first")
    con = connect(db)
    seen: set[str] = set()
    metrics = {"added": 0, "updated": 0, "unchanged": 0, "deleted": 0}
    try:
        # Stream JSONL: future large corpora must not require another
        # full in-memory copy of retrieval text during each incremental sync.
        with con, input_file.open(encoding="utf-8") as stream:
            for line in stream:
                if not line.strip():
                    continue
                obj = json.loads(line)
                identifier = obj["id"]
                if identifier in seen:
                    raise ValueError("duplicate JSONL ID: " + identifier)
                seen.add(identifier)
                serialized = canonical(obj)
                hashvalue = hashlib.sha256(serialized.encode("utf-8")).hexdigest()
                old = con.execute("SELECT sha256,fts_rowid FROM records WHERE id=?",
                                  (identifier,)).fetchone()
                if old and old[0] == hashvalue:
                    metrics["unchanged"] += 1
                    continue
                if old:
                    con.execute("DELETE FROM search_docs WHERE rowid=?", (old[1],))
                    con.execute("DELETE FROM records WHERE id=?", (identifier,))
                values = fields(obj)
                cursor = con.execute("INSERT INTO search_docs("
                                     "id,title,aliases,tags,summary,content)"
                                     " VALUES(?,?,?,?,?,?)", values)
                con.execute("INSERT INTO records(id,sha256,fts_rowid,json)"
                            " VALUES(?,?,?,?)",
                            (identifier, hashvalue, cursor.lastrowid, serialized))
                metrics["updated" if old else "added"] += 1
            # Removal is mandatory when a document disappears or changes its ID.
            # The operation is transaction-scoped, so no stale content survives.
            old_ids = [row[0] for row in con.execute("SELECT id FROM records")]
            for ident in old_ids:
                if ident not in seen:
                    rowid = con.execute("SELECT fts_rowid FROM records WHERE id=?",
                                        (ident,)).fetchone()[0]
                    con.execute("DELETE FROM search_docs WHERE rowid=?", (rowid,))
                    con.execute("DELETE FROM records WHERE id=?", (ident,))
                    metrics["deleted"] += 1
        metrics["total"] = con.execute("SELECT COUNT(*) FROM records").fetchone()[0]
    finally:
        con.close()
    return metrics


def query(db: Path, raw: str, limit: int) -> dict:
    terms = [x.casefold() for x in TOKEN.findall(raw)]
    if not terms or not (1 <= limit <= 100):
        raise ValueError("query requires words and limit between 1 and 100")
    if not db.is_file():
        raise ValueError("no FTS database; sync from generated JSONL first")
    expression = " OR ".join('"' + word + '"' for word in terms)
    con = connect(db)
    try:
        # bm25() is a relative retrieval ranking, not scientific confidence.
        rows = con.execute(
            "SELECT records.json, bm25(search_docs,0,8,5,5,3,1) "
            "FROM search_docs JOIN records ON records.fts_rowid=search_docs.rowid "
            "WHERE search_docs MATCH ? ORDER BY 2,records.id LIMIT ?",
            (expression, limit)).fetchall()
    finally:
        con.close()
    results = []
    for payload, rank in rows:
        obj = json.loads(payload)
        results.append({
            "id": obj["id"], "type": obj["type"], "title":
                obj.get("title", obj.get("heading", "")),
            "path": obj.get("path", ""), "status": obj.get("status", ""),
            "line_start": obj.get("line_start"),
            "line_end": obj.get("line_end"),
            "sha256": obj.get("sha256", ""),
            "provenance": obj.get("provenance", obj.get("path", "")),
            "identity": obj.get("identity"),
            "primary_url": obj.get("primary_url"),
            "source_revision": obj.get("source_revision"),
            "source_permalink": obj.get("source_permalink"),
            "full_proof_verified": obj.get("full_proof_verified"),
            "independent_reproduction": obj.get("independent_reproduction"),
            "model_id": obj.get("model_id"),
            "limitations": obj.get("limitations", ""),
            "rank": rank,
        })
    return {
        "query": raw, "results": results,
        "warning": "FTS5 lexical ranking is not proof, source freshness or theorem implication"
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    choices = parser.add_subparsers(dest="command", required=True)
    build = choices.add_parser("sync")
    build.add_argument("--jsonl", default=str(DEFAULT_JSONL))
    build.add_argument("--db", default=str(DEFAULT_DB))
    search = choices.add_parser("search")
    search.add_argument("words", nargs="+")
    search.add_argument("--limit", type=int, default=10)
    search.add_argument("--db", default=str(DEFAULT_DB))
    args = parser.parse_args()
    try:
        data = sync(Path(args.db), Path(args.jsonl)) if args.command == "sync" else (
            query(Path(args.db), " ".join(args.words), args.limit))
        print(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    except (ValueError, KeyError, sqlite3.Error, OSError) as exc:
        print("GRAPH_FTS_FAIL:", str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
