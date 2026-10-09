#!/usr/bin/env python3
"""DAG-002 G0: exact append-only DAG index, pure finite oracles and accounting.

This is a deliberately elementary, model-restricted implementation of the
KNOWN chain-top labeling principle (Jagadish/Felsner, SEA 2025), NOT a novel
algorithm and NOT physical I/O instrumentation. Standard library only.
"""
from bisect import bisect_left
from math import comb


def independent_reachable(parent_lists, ancestor, target):
    """Backwards DFS over actual source arcs, independent of label algorithm."""
    n = len(parent_lists)
    if not isinstance(ancestor, int) or not isinstance(target, int):
        raise ValueError("IDs must be integers")
    if not (0 <= ancestor < n and 0 <= target < n):
        raise ValueError("IDs outside graph")
    visited = set()
    todo = [target]
    while todo:
        current = todo.pop()
        if current == ancestor:
            return True
        if current in visited:
            continue
        visited.add(current)
        todo.extend(parent_lists[current])
    return False


def min_fixed_bits_for_states(states):
    """Integer-exact ceil(log2(states)), for states >= 1."""
    if not isinstance(states, int) or states < 1:
        raise ValueError("number of states must be positive")
    return (states - 1).bit_length()


def antichain_observable_masks(size, indegree=None):
    """Distinct truth vectors of reach(u_i, new_v) under antichain prefix."""
    if not isinstance(size, int) or size < 0:
        raise ValueError("size must be nonnegative")
    if indegree is not None and not (0 <= indegree <= size):
        raise ValueError("indegree out of range")
    for subset in range(1 << size):
        if indegree is None or subset.bit_count() == indegree:
            yield tuple((subset >> i) & 1 for i in range(size))


def antichain_label_lower_bits(size, indegree=None):
    if not isinstance(size, int) or size < 0:
        raise ValueError("size must be nonnegative")
    if indegree is None:
        return size
    if not isinstance(indegree, int) or not (0 <= indegree <= size):
        raise ValueError("indegree out of range")
    return min_fixed_bits_for_states(comb(size, indegree))


class AppendOnlyChainTopIndex:
    """First-compatible online chains; immutable published per-vertex tuples.

    The manifest chain_heads changes, but it is needed for *updates only*.
    query() reads immutable chain IDs and the target's sorted top-entry tuple.
    """
    def __init__(self):
        self.parents = []
        self.chain_of = []
        self.labels = []
        self.chain_heads = []
        self.parent_label_entries_read = 0
        self.label_entries_written = 0
        self.manifest_head_updates = 0

    def append(self, parents=()):
        v = len(self.labels)
        selected = tuple(parents)
        if any(not isinstance(p, int) or isinstance(p, bool) or p < 0 or p >= v
               for p in selected):
            raise ValueError("parent must be an already published node")
        if len(set(selected)) != len(selected):
            raise ValueError("duplicate parent")
        selected = tuple(sorted(selected))

        tops = {}
        for parent in selected:
            label = self.labels[parent]
            self.parent_label_entries_read += len(label)
            for chain, top in label:
                if top > tops.get(chain, -1):
                    tops[chain] = top

        chosen = None
        for chain, head in enumerate(self.chain_heads):
            if tops.get(chain) == head:
                chosen = chain
                break
        if chosen is None:
            chosen = len(self.chain_heads)
            self.chain_heads.append(v)
        else:
            self.chain_heads[chosen] = v
        tops[chosen] = v

        label = tuple(sorted(tops.items()))
        self.parents.append(selected)
        self.chain_of.append(chosen)
        self.labels.append(label)
        self.label_entries_written += len(label)
        self.manifest_head_updates += 1
        return v

    def query(self, ancestor, target):
        n = len(self.labels)
        if not isinstance(ancestor, int) or not isinstance(target, int):
            raise ValueError("IDs must be integers")
        if not 0 <= ancestor < n or not 0 <= target < n:
            raise ValueError("IDs outside graph")
        if ancestor > target:
            return False
        chain = self.chain_of[ancestor]
        index = bisect_left(self.labels[target], (chain, -1))
        if index == len(self.labels[target]):
            return False
        found_chain, top = self.labels[target][index]
        return found_chain == chain and ancestor <= top

    @property
    def logical_top_entry_count(self):
        return sum(len(label) for label in self.labels)

    @property
    def manifest_head_count(self):
        return len(self.chain_heads)

    def ledger(self):
        """Logical units only; NOT bytes, time or measured I/O."""
        return {
            "vertex_count": len(self.labels),
            "chain_count": len(self.chain_heads),
            "top_entries": self.logical_top_entry_count,
            "label_entries_written": self.label_entries_written,
            "parent_label_entries_read": self.parent_label_entries_read,
            "manifest_head_updates": self.manifest_head_updates,
        }


def topological_dag_parents(n, mask):
    """All DAGs oriented from lower IDs to higher IDs, unique n-choose-2 bits."""
    if not isinstance(n, int) or n < 0 or not isinstance(mask, int):
        raise ValueError("invalid parameters")
    if not 0 <= mask < (1 << (n * (n - 1) // 2)):
        raise ValueError("mask outside graph family")
    bit = 0
    output = []
    for v in range(n):
        parents = []
        for u in range(v):
            if mask & (1 << bit):
                parents.append(u)
            bit += 1
        output.append(tuple(parents))
    return tuple(output)
