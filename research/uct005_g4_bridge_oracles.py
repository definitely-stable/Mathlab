#!/usr/bin/env python3
"""UCT-005 G4: finite classical bridge checks, not a new root theorem.

Independent of F1 authentication, page I/O, and product implementation.
"""
from __future__ import annotations

import itertools
import json
from math import comb


def _validate_machine(outputs, transitions):
    n = len(outputs)
    if n < 1 or not transitions:
        raise ValueError("nonempty finite machine and operations required")
    if any(len(mapping) != n or any(not 0 <= s < n for s in mapping)
           for mapping in transitions):
        raise ValueError("every operation must be a total state transition")


def future_partition_refinement(outputs, transitions, horizon):
    """Horizon-indexed Moore refinement; produces canonical state labels."""
    _validate_machine(outputs, transitions)
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")

    def labels(signatures):
        label_map = {}
        return tuple(label_map.setdefault(s, len(label_map)) for s in signatures)

    classes = labels(outputs)
    for _ in range(horizon):
        classes = labels(tuple((outputs[s], tuple(classes[mapping[s]]
                                               for mapping in transitions))
                               for s in range(len(outputs))))
    return classes


def future_partition_by_traces(outputs, transitions, horizon):
    """Independent oracle enumerates public operation sequences."""
    _validate_machine(outputs, transitions)
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    signatures = []
    for start in range(len(outputs)):
        answers = []
        for h in range(horizon + 1):
            for word in itertools.product(range(len(transitions)), repeat=h):
                state = start
                for operation in word:
                    state = transitions[operation][state]
                answers.append(outputs[state])
        signatures.append(tuple(answers))
    classes = {}
    return tuple(classes.setdefault(sig, len(classes)) for sig in signatures)


def hamming_ball(q, m, radius):
    if q < 2 or m < 0 or radius < 0:
        raise ValueError("invalid alphabet, dimension or radius")
    return sum(comb(m, i) * (q - 1) ** i for i in range(min(m, radius) + 1))


def future_probe_transfer_falsifier():
    """Two stored bits: immediate query sees u, future SWAP reveals v."""
    states = tuple((u, v) for u in (0, 1) for v in (0, 1))
    lookup = {pair: i for i, pair in enumerate(states)}
    operations = tuple(tuple(lookup[f(s)] for s in states) for f in (
        lambda z: (z[0] ^ 1, z[1]),
        lambda z: (z[0], z[1] ^ 1),
        lambda z: (z[1], z[0]),
    ))
    outputs = tuple(u for u, v in states)
    present = future_partition_refinement(outputs, operations, 0)
    future = future_partition_refinement(outputs, operations, 1)
    assert len(set(present)) == 2
    assert len(set(future)) == 4
    assert future == future_partition_by_traces(outputs, operations, 1)
    return {
        "current_classes": 2,
        "future_classes": 4,
        "invalid_naive_one_probe_upper": hamming_ball(2, 1, 1),
        "valid_all_storage_upper": hamming_ball(2, 2, 4),
        "status": "COUNTERMODEL_TO_UNPRICED_FUTURE_PROBE_TRANSFER",
        "not_a_counterexample_to": "immediate ROST or F1 authenticated queries",
    }


def qary_subset_sums(columns, q, d):
    if q < 2 or d < 1 or not columns:
        raise ValueError("positive d, nonempty columns, q>=2 required")
    m = len(columns[0])
    if m < 1 or any(len(v) != m or any(not 0 <= z < q for z in v)
                   for v in columns):
        raise ValueError("columns must share a positive dimension over Z/qZ")
    out = []
    for k in range(min(d, len(columns)) + 1):
        for choice in itertools.combinations(range(len(columns)), k):
            out.append(tuple(sum(columns[j][i] for j in choice) % q
                             for i in range(m)))
    return tuple(out)


def min_pair_distance(words):
    return min((sum(a != b for a, b in zip(u, v))
                for i, u in enumerate(words) for v in words[i + 1:]),
               default=0)


def robust_subset_sums(columns, q, d, e):
    if e < 0:
        raise ValueError("negative correction radius")
    words = qary_subset_sums(columns, q, d)
    return min_pair_distance(words) >= 2 * e + 1


def bounded_corruption_ball(word, q, e):
    """Independent full corruption oracle, bounded alphabets/dimensions only."""
    if e < 0:
        raise ValueError("negative correction radius")
    return {candidate for candidate in itertools.product(range(q), repeat=len(word))
            if sum(a != b for a, b in zip(word, candidate)) <= e}


def disjoint_triple_columns(n):
    if n < 1:
        raise ValueError("n must be positive")
    return tuple(tuple(int(3 * j <= i < 3 * j + 3) for i in range(3 * n))
                 for j in range(n))


def robust_support_gate_report():
    columns = disjoint_triple_columns(3)
    assert robust_subset_sums(columns, 5, 3, 1)
    assert not robust_subset_sums(columns, 5, 3, 2)
    return {
        "q": 5, "w": 4, "d": 3,
        "e1_disjoint_construct_n": 3,
        "e1_minimum_distance": min_pair_distance(qary_subset_sums(columns, 5, 3)),
        "e2_nonempty_capacity": 0,
        "reason": "empty-versus-singleton enforces w>=2e+1",
        "status": "PROVED_ELEMENTARY_FEASIBILITY_STOP_E_GE_2",
    }


def histories_by_observable_pins(horizon, pins):
    if horizon < 0 or any(not 0 <= p < horizon for p in pins):
        raise ValueError("pins must refer to historical epochs")
    normalized = tuple(sorted(set(pins)))
    signatures = {
        tuple(history[t] for t in normalized)
        for history in itertools.product((0, 1), repeat=horizon)
    }
    return len(signatures)


def dag_path_count(n, edges, src, dst):
    if not 0 <= src < dst < n or any(not 0 <= a < b < n for a, b in edges):
        raise ValueError("forward-only DAG and ordered endpoints required")
    paths = [0] * n
    paths[src] = 1
    for v in range(src, n):
        for a, b in edges:
            if a == v:
                paths[b] += paths[v]
    return paths[dst]


def dag_boolean_bfs(n, edges, src, dst):
    """Independent graph traversal; does not rely on path counts."""
    if not 0 <= src < dst < n or any(not 0 <= a < b < n for a, b in edges):
        raise ValueError("forward-only DAG and ordered endpoints required")
    seen, pending = {src}, [src]
    while pending:
        current = pending.pop()
        if current == dst:
            return True
        for a, b in edges:
            if a == current and b not in seen:
                seen.add(b)
                pending.append(b)
    return False


def graph_parity_falsifier():
    edges = ((0, 1), (1, 3), (0, 2), (2, 3))
    count = dag_path_count(4, edges, 0, 3)
    exists = dag_boolean_bfs(4, edges, 0, 3)
    assert count == 2 and exists and not count % 2
    return {
        "n": 4, "paths": count, "gf2_path_sum": count % 2,
        "boolean_reachability": exists,
        "status": "COUNTERMODEL_TO_GF2_COUNT_EQUALS_BOOLEAN_REACHABILITY",
    }


def report():
    return {
        "theorem_status": "DERIVED_CLASSICAL_ONLY_ROOT_OPEN",
        "future_probe": future_probe_transfer_falsifier(),
        "aset": robust_support_gate_report(),
        "historical_5_pins": histories_by_observable_pins(5, range(5)),
        "historical_2_pins": histories_by_observable_pins(5, (0, 4)),
        "graph": graph_parity_falsifier(),
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True))
