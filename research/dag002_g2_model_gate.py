"""DAG-002 G2-A: finite model-separation oracles, NOT a complexity theorem.

Immutable append-sink parent records are an abstract logical structure here.
Full-page I/O, allocation, RAM, codebook, freshness, and wall time are not priced.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterator

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "docs" / "research" / "DAG-002-G2-SOURCE-EQUIVALENCE.json"


def sources() -> dict:
    return json.loads(MATRIX.read_text(encoding="utf-8"))


def ordered_dags(n: int) -> Iterator[tuple[tuple[int, ...], ...]]:
    """Enumerate 2^(n(n-1)/2) DAGs in fixed topological vertex order."""
    if n < 0 or n > 5:
        raise ValueError("finite independent oracle permits 0<=n<=5")
    possible = [(p, v) for v in range(n) for p in range(v)]
    for edge_mask in range(1 << len(possible)):
        parents = [[] for _ in range(n)]
        for i, (p, v) in enumerate(possible):
            if (edge_mask >> i) & 1:
                parents[v].append(p)
        yield tuple(tuple(x) for x in parents)


def reach(parents: tuple[tuple[int, ...], ...], source: int, target: int) -> bool:
    """Reference backwards reachability, reflexive for source == target."""
    if not (0 <= source < len(parents) and 0 <= target < len(parents)):
        raise ValueError("invalid vertex")
    if source > target:
        return False
    pending = [target]
    visited: set[int] = set()
    while pending:
        v = pending.pop()
        if v == source:
            return True
        if v not in visited:
            visited.add(v)
            pending.extend(parents[v])
    return False


def lazy_append(
    old_records: tuple[tuple[int, ...], ...], parent_ids: tuple[int, ...]
) -> tuple[tuple[tuple[int, ...], ...], int]:
    """Append one parent record with zero reads OF OLD SOURCE RECORD CONTENTS.

    Tuple pointer-copying and metadata management are intentionally NOT physical I/O.
    The parent incidence payload is provided to the updater, not to the query.
    """
    n = len(old_records)
    if parent_ids != tuple(sorted(set(parent_ids))):
        raise ValueError("parent IDs must be sorted and unique")
    if any(not (0 <= p < n) for p in parent_ids):
        raise ValueError("parent must be old vertex")
    return old_records + (parent_ids,), 0


def lazy_query(
    records: tuple[tuple[int, ...], ...], source: int, target: int
) -> tuple[bool, int]:
    """Backward DFS; record reads are logically CHARGED, not claimed to be pages."""
    if not (0 <= source < len(records) and 0 <= target < len(records)):
        raise ValueError("invalid vertex")
    if source == target:
        return True, 0
    if source > target:
        return False, 0
    pending = [target]
    visited: set[int] = set()
    reads = 0
    while pending:
        v = pending.pop()
        if v == source:
            return True, reads
        if v in visited:
            continue
        visited.add(v)
        reads += 1
        pending.extend(records[v])
    return False, reads


def insert_old_edge(
    parents: tuple[tuple[int, ...], ...], source: int, target: int
) -> tuple[tuple[int, ...], ...]:
    """Different update alphabet: old-to-old edge, topological source<target."""
    if not (0 <= source < target < len(parents)):
        raise ValueError("must insert between existing vertices in topological order")
    out = list(parents)
    out[target] = tuple(sorted(set(out[target]) | {source}))
    return tuple(out)


def cross_history_prefix_pair() -> tuple[tuple[tuple[int, ...], ...], ...]:
    """Same final parent command, distinct earlier histories."""
    return (((), ()), ((), (0,)))


def run_report() -> dict:
    m = sources()
    number = 0
    lazy_queries = 0
    for graph in ordered_dags(4):
        for parent_mask in range(16):
            old_n = len(graph)
            parents = tuple(p for p in range(old_n) if (parent_mask >> p) & 1)
            appended, update_old_reads = lazy_append(graph, parents)
            assert update_old_reads == 0
            for u in range(old_n):
                for v in range(old_n):
                    assert reach(graph, u, v) == reach(appended, u, v)
            for u in range(old_n + 1):
                for v in range(old_n + 1):
                    ans, reads = lazy_query(appended, u, v)
                    assert ans == reach(appended, u, v)
                    assert 0 <= reads <= old_n + 1
                    lazy_queries += 1
            number += 1
    a, b = cross_history_prefix_pair()
    assert reach(lazy_append(a, (1,))[0], 0, 2) is False
    assert reach(lazy_append(b, (1,))[0], 0, 2) is True
    assert not reach(((), ()), 0, 1)
    assert reach(insert_old_edge(((), ()), 0, 1), 0, 1)
    return {
        "status": "FINITE_MODEL_BARRIERS_PASS; NO_NOVEL_THEOREM",
        "source_records": len(m["sources"]),
        "append_cases": number,
        "lazy_query_cases": lazy_queries,
        "source_proof_replay": False,
    }


if __name__ == "__main__":
    print(json.dumps(run_report(), sort_keys=True))
