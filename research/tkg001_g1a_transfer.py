#!/usr/bin/env python3
"""TKG-001 G1-A: exact finite model-transfer counterexamples, not a new lower bound.

Logical full-page images are *charged simulator units*, not real SSD I/O.
Only an exact antichain one-sink parent-membership question is priced.
"""
from dataclasses import dataclass


def _check_parent_set(n, parents):
    if type(n) is not int or n < 0:
        raise ValueError("vertex count must be a nonnegative integer")
    if len(set(parents)) != len(parents) or any(
        type(i) is not int or i < 0 or i >= n for i in parents
    ):
        raise ValueError("parents must be distinct old vertices")
    return frozenset(parents)


class SinkAppendDAG:
    """New vertex v only has incoming old->v edges; no old adjacency edits."""

    def __init__(self, n=0, old_edges=()):
        if type(n) is not int or n < 0:
            raise ValueError("invalid n")
        self.n = n
        self.edges = set()
        for u, v in old_edges:
            if not (type(u) is int and type(v) is int and 0 <= u < v < n):
                raise ValueError("old DAG vertices must be topologically ordered")
            self.edges.add((u, v))

    def append(self, parents):
        p = _check_parent_set(self.n, tuple(parents))
        v = self.n
        self.edges.update((u, v) for u in p)
        self.n += 1
        return v

    def reach(self, src, dst):
        if not (type(src) is int and type(dst) is int
                and 0 <= src < self.n and 0 <= dst < self.n):
            raise ValueError("invalid endpoints")
        seen, todo = {src}, [src]
        while todo:
            u = todo.pop()
            if u == dst:
                return True
            for a, b in self.edges:
                if a == u and b not in seen:
                    seen.add(b)
                    todo.append(b)
        return False


class OldEdgeInsertionDAG(SinkAppendDAG):
    """Same topological labels, but insertions may change old->old answers."""

    def insert(self, u, v):
        if not (type(u) is int and type(v) is int
                and 0 <= u < v < self.n):
            raise ValueError("only forward existing-vertex arcs allowed")
        self.edges.add((u, v))


def independent_closure(n, edges):
    """Boolean Warshall: separate reachability oracle from DFS."""
    c = [[i == j for j in range(n)] for i in range(n)]
    for u, v in edges:
        c[u][v] = True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                c[i][j] = c[i][j] or (c[i][k] and c[k][j])
    return c


@dataclass(frozen=True)
class PageCost:
    """Frozen units: separately charged client label and remote state."""
    client_label_bits: int
    manifest_bits: int
    remote_payload_bits: int
    write_page_images: int
    worst_query_page_reads: int

    def bytes_written(self, page_bytes):
        return self.write_page_images * page_bytes


def _pages(bits, page_bytes):
    if type(page_bytes) is not int or page_bytes <= 0:
        raise ValueError("page_bytes must be a positive integer")
    return (bits + (8 * page_bytes - 1)) // (8 * page_bytes)


def public_parent_label(n, parents, page_bytes):
    """n locally resident label bits; client pays n bits and publication pages.

    The query may inspect the client-resident label without REMOTE reads.
    Preloading/cold-client fetch is a separate service cost, not a free disk I/O.
    """
    _check_parent_set(n, parents)
    return PageCost(n, 0, 0, _pages(n, page_bytes), 0)


def remote_membership_bitmap(n, parents, page_bytes):
    """One exact remote bit lookup at a publicly known page+offset.

    The whole n-bit mutable source bitmap is billed. No uncharged directory,
    no globally materialized answers and no free remote array.
    """
    _check_parent_set(n, parents)
    return PageCost(0, 0, n, _pages(n, page_bytes), 1 if n else 0)


def append_parent_log(n, parents, page_bytes):
    """One full header image + one *whole page* per parent ID; scan all d.

    Header and records are counted as remote pages, including a negative query.
    This is a deliberately naive upper point (no packed-record normalization).
    """
    p = _check_parent_set(n, parents)
    _pages(n, page_bytes)
    d = len(p)
    return PageCost(0, 0, (d + 1) * 8 * page_bytes, d + 1, d + 1)


def public_decode(n, parents, query_vertex):
    _check_parent_set(n, parents)
    if type(query_vertex) is not int or not 0 <= query_vertex < n:
        raise ValueError("invalid query")
    return query_vertex in parents


def remote_decode(n, parents, query_vertex):
    """Semantically identical to public decoder, billed under remote bitmap."""
    return public_decode(n, parents, query_vertex)


def log_decode(n, parents, query_vertex):
    """Scan entire stream even when positive, to pin worst-case read contract."""
    _check_parent_set(n, parents)
    if type(query_vertex) is not int or not 0 <= query_vertex < n:
        raise ValueError("invalid query")
    result = False
    for key in sorted(parents):
        result |= key == query_vertex
    return result
