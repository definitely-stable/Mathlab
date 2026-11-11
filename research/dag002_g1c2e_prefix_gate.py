#!/usr/bin/env python3
"""DAG-002 G1-C2-E: cross-history information gate, explicit non-transfer oracles.

The lower bound is an elementary indistinguishability/pigeonhole argument
restricted to zero remote update reads AND target-only queries. It is NOT a
new cell-probe theorem nor a consequence of per-history G1-B counting.
"""
from dataclasses import dataclass
from itertools import combinations

from dag002_oracle import topological_dag_parents


def strict_ancestor_mask(parents, target):
    """Compute reachability by raw reverse DFS, not a chain/bitmap index."""
    if type(target) is not int or not 0 <= target < len(parents):
        raise ValueError("target outside prefix")
    visited, pending = set(), list(parents[target])
    while pending:
        v = pending.pop()
        if v in visited:
            continue
        visited.add(v)
        pending.extend(parents[v])
    return sum(1 << i for i in visited)


def append_sink_truth(parents, selected):
    """Old-to-new reachability vector for a fresh sink with old parents."""
    n = len(parents)
    parents_new = tuple(selected)
    if any(type(p) is not int or not 0 <= p < n for p in parents_new):
        raise ValueError("invalid old parent ID")
    if len(parents_new) != len(set(parents_new)):
        raise ValueError("duplicate parent")
    return sum(1 << p for p in parents_new) | _union_ancestors(parents, parents_new)


def _union_ancestors(parents, selected):
    mask = 0
    for p in selected:
        mask |= strict_ancestor_mask(parents, p)
    return mask


def prefix_family(n):
    """All DAGs with frozen topological IDs and arbitrary preceding edges."""
    if type(n) is not int or not 1 <= n <= 5:
        raise ValueError("finite oracle supports 1 <= n <= 5")
    return (topological_dag_parents(n, mask)
            for mask in range(1 << (n * (n - 1) // 2)))


def same_command_fiber(n, selected):
    """All distinct old-to-new truth vectors across DIFFERENT old prefixes."""
    if type(n) is not int or not 1 <= n <= 5:
        raise ValueError("finite oracle supports 1 <= n <= 5")
    checked = tuple(selected)
    if any(type(p) is not int or not 0 <= p < n for p in checked):
        raise ValueError("invalid parent index")
    if len(checked) != len(set(checked)):
        raise ValueError("duplicate parent")
    return frozenset(append_sink_truth(prefix, checked) for prefix in prefix_family(n))


def min_local_bits_zero_update_reads(fiber_size):
    """Restricted cross-history necessity: K outcomes <= 2^H.

    Precondition: program/public IDs/fresh-record destination same across
    prefixes; updater sees only S and H retained local bits, NO remote/source
    reads; target-only decoder may see fresh record + retained local bits but
    NOT any old record, old pointer encoding, epoch-dependent public program,
    hidden input/cached data or side channel. Then output factors via H.
    """
    if type(fiber_size) is not int or fiber_size < 1:
        raise ValueError("fiber size must be positive")
    return (fiber_size - 1).bit_length()


@dataclass
class LazyAdjacencyDAG:
    """Exact zero-UPDATE-read, nonzero-QUERY-read counterconstruction.

    One complete new adjacency record per APPEND. Query performs raw DFS,
    charging *every* old adjacency-record read and its serialized bytes.
    Fixed public horizon prices each parent-ID width; updater never opens
    an old record. No RAM cap, crash/GC/authentication or page model claimed.
    """
    horizon: int

    def __post_init__(self):
        if type(self.horizon) is not int or not 1 <= self.horizon <= 1024:
            raise ValueError("invalid horizon")
        self.width = max(1, ((self.horizon - 1).bit_length() + 7)//8)
        self.parents = []
        self.update_read_records = 0
        self.update_written_records = 0
        self.update_written_bytes = 0
        self.parent_input_bits = 0
        self.query_read_records = 0
        self.query_read_bytes = 0

    def append(self, parents=()):
        n = len(self.parents)
        if n >= self.horizon:
            raise ValueError("frozen horizon exhausted")
        selected = tuple(parents)
        if any(type(p) is not int or not 0 <= p < n for p in selected):
            raise ValueError("not an old vertex")
        if len(set(selected)) != len(selected):
            raise ValueError("duplicate parents")
        self.parents.append(tuple(sorted(selected)))
        self.parent_input_bits += n
        self.update_written_records += 1
        self.update_written_bytes += 4 + self.width * len(selected)
        return n

    def _read_record(self, v):
        self.query_read_records += 1
        record = self.parents[v]
        self.query_read_bytes += 4 + self.width * len(record)
        return record

    def reach(self, ancestor, target):
        if any(type(x) is not int or not 0 <= x < len(self.parents)
               for x in (ancestor, target)):
            raise ValueError("query outside published vertices")
        if ancestor == target:
            return True
        if ancestor > target:
            return False
        pending, seen = [target], set()
        while pending:
            v = pending.pop()
            if v == ancestor:
                return True
            if v not in seen:
                seen.add(v)
                pending.extend(self._read_record(v))
        return False


def report():
    first = ((), ())
    second = ((), (0,))
    assert append_sink_truth(first, (1,)) == 0b10
    assert append_sink_truth(second, (1,)) == 0b11
    for n in range(1, 6):
        values = same_command_fiber(n, (n - 1,))
        assert len(values) == 1 << (n - 1)
        assert min_local_bits_zero_update_reads(len(values)) == n - 1
    for prefix in (first, second):
        store = LazyAdjacencyDAG(3)
        for pr in prefix:
            store.append(pr)
        store.append((1,))
        assert store.reach(0, 2) == bool(append_sink_truth(prefix, (1,)) & 1)
        assert store.update_read_records == 0
        assert store.query_read_records >= 2
    print("DAG_G1C2E_CROSS_HISTORY_FIBER_EXACT_PASS")
    print("DAG_G1C2E_ZERO_UPDATE_READ_TARGET_ONLY_GATE_PASS")
    print("DAG_G1C2E_LAZY_QUERY_READ_ESCAPE_PASS")
    print("STOP_THEOREM_NOVELTY_ELEMENTARY_INJECTION_ONLY")


if __name__ == "__main__":
    report()
