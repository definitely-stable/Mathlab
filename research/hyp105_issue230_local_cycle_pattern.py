"""Independent definition-level local paired-source counterexample.

This is a 15-incidence source subuniverse, not a full-map small-S witness.
No Mathlab code is imported. The selected source incidences form a matching.
"""

from collections import Counter, defaultdict
from itertools import combinations
import json


def labels():
    # Left/right endpoint coordinates 5,6; internal coordinates 0,...,4.
    out = []
    for i in range(5):
        out.append((f"A{i}", (5, i), (5, i)))
        out.append((f"B{i}", (i, (i + 1) % 5), (i, (i + 2) % 5)))
        out.append((f"C{i}", ((i + 1) % 5, 6), ((i + 2) % 5, 6)))
    return out


def build_graph(items):
    adj = defaultdict(set)
    source = {}
    for name, (x, xx), (y, yy) in items:
        for u, v in (((x, y), (xx, yy)), ((x, yy), (xx, y))):
            assert u != v and v not in adj[u]
            adj[u].add(v)
            adj[v].add(u)
            source[frozenset((u, v))] = name
    return adj, source


def graph_cycles(adj, k):
    found = set()
    for start in sorted(adj):
        def visit(path):
            if len(path) == k:
                if start in adj[path[-1]]:
                    found.add(frozenset(
                        frozenset((path[i], path[(i + 1) % k]))
                        for i in range(k)
                    ))
                return
            for v in sorted(adj[path[-1]]):
                if v > start and v not in path:
                    visit(path + [v])
        visit([start])
    return found


def connected_dual(items, side):
    # Independent six-column degree-two dual; detects connected C6.
    coord = defaultdict(list)
    for i, item in enumerate(items):
        for x in item[side]:
            coord[x].append(i)
    if len(coord) != 6 or any(len(ids) != 2 for ids in coord.values()):
        return None
    dual = frozenset(frozenset(ids) for ids in coord.values())
    if len(dual) != 6:
        return None
    graph = defaultdict(set)
    for edge in dual:
        x, y = tuple(edge)
        graph[x].add(y)
        graph[y].add(x)
    if any(len(graph[i]) != 2 for i in range(6)):
        return None
    seen = {0}
    todo = [0]
    while todo:
        for j in graph[todo.pop()]:
            if j not in seen:
                seen.add(j)
                todo.append(j)
    return dual if len(seen) == 6 else None


def main():
    items = labels()
    assert len({frozenset(x) for _, x, _ in items}) == 15
    assert len({frozenset(y) for _, _, y in items}) == 15
    adj, source = build_graph(items)
    assert len(source) == 30
    for u, ns in adj.items():
        assert len({v[0] for v in ns}) == len(ns)
        assert len({v[1] for v in ns}) == len(ns)
    cycles = graph_cycles(adj, 6)
    assert not graph_cycles(adj, 3)
    assert not graph_cycles(adj, 4)
    cycle_profile = Counter()
    for cyc in cycles:
        vertices = set().union(*cyc)
        cycle_profile[(len({x for x, _ in vertices}),
                       len({y for _, y in vertices}))] += 1
        assert len({source[e] for e in cyc}) == 6
    assert cycle_profile == {(5, 6): 5, (6, 5): 5}

    # Direct unordered original-sixset selector, independent of graph cycles.
    # Every selected source is a distinct point and a distinct line.
    # Consequently only A/A can occur; its accepted family is D6.
    degree_two_both = 0
    d6 = 0
    for six in combinations(items, 6):
        cc = [Counter(x for item in six for x in item[side])
              for side in (1, 2)]
        if all(len(c) == 6 and set(c.values()) == {2} for c in cc):
            degree_two_both += 1
        a, b = connected_dual(six, 1), connected_dual(six, 2)
        if a is not None and a == b:
            d6 += 1
    assert d6 == 0

    u, v = (5, 5), (6, 6)
    paths = [(u, a, b, v) for a in adj[u] for b in adj[a] if v in adj[b]]
    assert len(paths) == 5
    for path in paths:
        assert len({x for x, _ in path}) == 4
        assert len({y for _, y in path}) == 4
    assert len(set().union(*(set(p[1:3]) for p in paths))) == 10
    result = {
        "source_incidence_count": 15,
        "physical_edge_count": len(source),
        "nonisolated_physical_vertices": len(adj),
        "degree_histogram": dict(Counter(map(len, adj.values()))),
        "P3_fixed_endpoints": len(paths),
        "simple_C6": len(cycles),
        "C6_physical_coordinate_profiles": {
            f"{x}/{y}": n for (x, y), n in sorted(cycle_profile.items())
        },
        "degree_two_six_coordinate_original_sixsets": degree_two_both,
        "D6": d6,
        "S_seven": 0,
        "scope": "selected 15-incidence source subuniverse only",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
