#!/usr/bin/env python3
"""TKG-001 G0: exact finite bitemporal provenance DAG reference, not production.

An update appends one transaction event, plus an auxiliary live-ID index edit.
This is a *logical* ledger, NOT measured physical I/O, durable WAL or crypto.
Every query replays its selected epoch and enumerates positive evidence paths.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Edge:
    key: str                  # Unique asserted-edge/evidence ID, never recycled.
    src: int
    dst: int
    valid_from: int           # Event-time half-open interval.
    valid_to: int


@dataclass(frozen=True)
class Event:
    epoch: int                # Transaction time / recorded order, starts at 1.
    op: str                   # "add" or "del".
    key: str
    edge: Edge | None


class TemporalDag:
    """Honest sequential writer, no cycles (each asserted arc src < dst)."""

    def __init__(self):
        self.events = []
        self._live = {}
        self._ever = set()
        self._id_index_mutations = 0

    @property
    def epoch(self):
        return len(self.events)

    @property
    def ledger(self):
        return {
            "event_log_appends": self.epoch,
            "live_id_index_mutations": self._id_index_mutations,
            "historical_id_claims": len(self._ever),
        }

    def add(self, key, src, dst, valid_from, valid_to):
        if not isinstance(key, str) or not key or key in self._ever:
            raise ValueError("invalid/recycled edge identity")
        vals = (src, dst, valid_from, valid_to)
        if any(type(x) is not int for x in vals):
            raise ValueError("only integer endpoints and timestamps")
        if not (0 <= src < dst and valid_from < valid_to):
            raise ValueError("DAG edge or half-open valid interval invalid")
        edge = Edge(key, src, dst, valid_from, valid_to)
        self.events.append(Event(self.epoch + 1, "add", key, edge))
        self._ever.add(key)
        self._live[key] = edge
        self._id_index_mutations += 1
        return self.epoch

    def retract(self, key):
        if key not in self._live:
            raise ValueError("only current assertions can be retracted")
        self.events.append(Event(self.epoch + 1, "del", key, None))
        del self._live[key]
        self._id_index_mutations += 1
        return self.epoch

    def active(self, epoch, valid_time):
        if type(epoch) is not int or not 0 <= epoch <= self.epoch:
            raise ValueError("unknown historical transaction epoch")
        if type(valid_time) is not int:
            raise ValueError("valid_time must be an integer")
        visible = {}
        for event in self.events[:epoch]:
            if event.op == "add":
                visible[event.key] = event.edge
            else:
                del visible[event.key]
        return {
            key: edge for key, edge in visible.items()
            if edge.valid_from <= valid_time < edge.valid_to
        }

    def witnesses(self, src, dst, epoch, valid_time):
        """Complete explicit list of source-ID paths: may use 2^k space."""
        if not (type(src) is int and type(dst) is int and src >= 0 and dst >= 0):
            raise ValueError("invalid query vertices")
        active = self.active(epoch, valid_time)
        if src == dst:
            return [()]     # Reflexive empty derivation; not evidence of a fact.
        adjacency = {}
        for e in active.values():
            adjacency.setdefault(e.src, []).append((e.dst, e.key))
        for edges in adjacency.values():
            edges.sort(key=lambda item: (item[0], item[1]))

        result = []

        def walk(vertex, trace):
            if vertex == dst:
                result.append(trace)
                return
            for next_v, key in adjacency.get(vertex, []):
                if next_v <= dst:   # Strict DAG topological IDs.
                    walk(next_v, trace + (key,))

        if src < dst:
            walk(src, ())
        return sorted(result)

    def count_factorized(self, src, dst, epoch, valid_time):
        """Dynamic-programmed exact path count; no explicit witness expansion."""
        if type(src) is not int or type(dst) is not int or src < 0 or dst < 0:
            raise ValueError("invalid query vertices")
        edges = list(self.active(epoch, valid_time).values())
        if src == dst:
            return 1
        if src > dst:
            return 0
        outgoing = {}
        for edge in edges:
            if src <= edge.src < edge.dst <= dst:
                outgoing.setdefault(edge.src, []).append(edge.dst)
        ways = {dst: 1}
        for v in range(dst - 1, src - 1, -1):
            ways[v] = sum(ways.get(next_v, 0) for next_v in outgoing.get(v, []))
        return ways.get(src, 0)

    def verify_positive_witness(self, src, dst, epoch, valid_time, keys):
        """Checks a claimed path *against an honest, locally held snapshot*.

        A remote verifier cannot use this as an authenticated/latest-state
        certificate without separately paid authentic data and freshness.
        """
        if not isinstance(keys, tuple):
            return False
        try:
            active = self.active(epoch, valid_time)
        except ValueError:
            return False
        if src == dst:
            return keys == ()
        if not keys:
            return False
        vertex = src
        for key in keys:
            edge = active.get(key)
            if edge is None or edge.src != vertex:
                return False
            vertex = edge.dst
        return vertex == dst


def diamond(k):
    """Acyclic fixture: 3k+1 vertices, 4k distinct edges, exactly 2^k paths."""
    if type(k) is not int or k < 1:
        raise ValueError("k must be positive")
    graph = TemporalDag()
    for i in range(k):
        src = 3 * i
        left, right, sink = src + 1, src + 2, src + 3
        for key, a, b in (
            (f"L{i}a", src, left), (f"L{i}b", left, sink),
            (f"R{i}a", src, right), (f"R{i}b", right, sink),
        ):
            graph.add(key, a, b, 0, 10)
    return graph
