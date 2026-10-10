#!/usr/bin/env python3
"""Evaluate Mathlab provenance-grounded retrieval against frozen bilingual IDs.

These fixtures check discovery quality, never proof validity. No embeddings,
network, or external packages. Run after each corpus/index change.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys

from research_graph import ROOT, ingest, search, validate


FIXTURES = ROOT / "docs/research/graph/retrieval-fixtures.json"


def evaluate(fixtures: dict, graph=None) -> dict:
    if fixtures.get("schema") != "mathlab.research-graph-retrieval-fixtures.v1":
        raise ValueError("unknown fixture schema")
    if graph is None:
        graph = ingest()
    validate(graph)
    cases = fixtures.get("queries")
    if not isinstance(cases, list) or not cases:
        raise ValueError("missing retrieval fixtures")
    results = []
    signatures = set()
    for case in cases:
        if set(case) != {"query", "kind", "relevant", "k"}:
            raise ValueError("fixture keys changed")
        query, kind, relevant, k = (case["query"], case["kind"],
                                     case["relevant"], case["k"])
        signature = (query, kind)
        if signature in signatures:
            raise ValueError("duplicate query-kind fixture")
        signatures.add(signature)
        if not relevant or len(relevant) != len(set(relevant)):
            raise ValueError("duplicate or empty relevance labels")
        if type(k) is not int or not 1 <= k <= 50:
            raise ValueError("invalid recall cutoff")
        known = set(graph.nodes)
        if not set(relevant) <= known:
            raise ValueError("relevance fixture points to unknown canonical ID")
        found = search(graph, query, k, kind)
        rank_ids = [x["id"] for x in found["results"]]
        hits = [x for x in relevant if x in rank_ids]
        results.append({"query": query, "kind": kind, "k": k,
                        "hits": hits, "expected": relevant,
                        "recall_at_k": len(hits) / len(relevant),
                        "ranked_ids": rank_ids})
    passed = all(row["recall_at_k"] == 1.0 for row in results)
    return {"schema": "mathlab.research-graph-retrieval-eval.v1",
            "passed": passed,
            "mean_recall_at_k": sum(row["recall_at_k"] for row in results)
                                / len(results),
            "cases": results,
            "caveat": "Relevance IDs and lexical recall do not verify research claims"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="fail when any fixture misses its expected canonical ID")
    parser.add_argument("--report", default="",
                        help="optional path to generated machine-readable report")
    args = parser.parse_args()
    try:
        report = evaluate(json.loads(FIXTURES.read_text(encoding="utf-8")))
        content = json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
        if args.report:
            target = Path(args.report)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
        print(content, end="")
        return int(args.check and not report["passed"])
    except (ValueError, KeyError, OSError, TypeError) as exc:
        print("RETRIEVAL_EVAL_FAIL:", exc, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
