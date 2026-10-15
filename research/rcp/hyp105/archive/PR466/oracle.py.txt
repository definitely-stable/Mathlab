"""Two exact local transfer falsifiers with a real W(3,8) embedding.

The source subuniverse has 18 incidences: an induced matching of size 15,
and its disjoint genuine GQ endpoint projection path q--ell--p--r.
This is NOT a full-map small-S example, nor an EICE-002 G* example.
No Mathlab modules are imported.
"""

from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb
import json

from hyp105_issue230_local_cycle_pattern import labels, build_graph, graph_cycles, connected_dual


def source_patch():
    base = [(name, tuple(sorted(x)), tuple(sorted(y)), name, name)
            for name, x, y in labels()]
    return base + [
        ("D", (5, 6), (0, 1), "q", "ell"),
        ("E", (0, 2), (0, 1), "p", "ell"),
        ("F", (0, 2), (5, 6), "p", "r"),
    ]


def direct_original_sixsets(items):
    counts = Counter({name: 0 for name in (
        "D6", "B_left", "B_right", "CA", "CB", "BB_overlap", "BB_disjoint")})
    leafless = []
    for ids in combinations(range(len(items)), 6):
        six = [items[i] for i in ids]
        if not all(len(c := Counter(z for e in six for z in e[j])) == 6
                   and set(c.values()) == {2} for j in (1, 2)):
            continue
        leafless.append([e[0] for e in six])
        profiles = [tuple(sorted(Counter(e[j] for e in six).values(), reverse=True))
                    for j in (3, 4)]
        aa, bb, cc = (1,) * 6, (2, 1, 1, 1, 1), (2, 2, 2)
        if profiles == [aa, aa]:
            left, right = connected_dual(six, 1), connected_dual(six, 2)
            if left is not None and left == right:
                counts["D6"] += 1
        elif profiles == [bb, aa]:
            counts["B_left"] += 1
        elif profiles == [aa, bb]:
            counts["B_right"] += 1
        elif profiles in ([cc, aa], [aa, cc]):
            counts["CA"] += 1
        elif profiles in ([cc, bb], [bb, cc]):
            counts["CB"] += 1
        elif profiles == [bb, bb]:
            repeated = []
            for side in (3, 4):
                multiplicities = Counter(e[side] for e in six)
                repeated.append({i for i, e in enumerate(six)
                                 if multiplicities[e[side]] == 2})
            overlap = len(repeated[0] & repeated[1])
            assert overlap in (0, 1)  # source graph is simple
            counts["BB_overlap" if overlap else "BB_disjoint"] += 1
    return counts, leafless


def gf8_multiply(x, y):
    # GF(2)[T]/(T^3+T+1), represented by three-bit polynomials.
    out = 0
    while y:
        if y & 1:
            out ^= x
        y >>= 1
        x <<= 1
        if x & 8:
            x ^= 11
    return out


def geometry_w38():
    inverses = {x: next(y for y in range(1, 8) if gf8_multiply(x, y) == 1)
                for x in range(1, 8)}
    points = [tuple([0] * leading + [1] + list(tail))
              for leading in range(4)
              for tail in product(range(8), repeat=3 - leading)]
    index = {point: i for i, point in enumerate(points)}

    def normalize(v):
        inv = inverses[next(x for x in v if x)]
        return tuple(gf8_multiply(inv, x) for x in v)

    def orthogonal(v, w):
        return (gf8_multiply(v[0], w[3]) ^ gf8_multiply(v[3], w[0])
                ^ gf8_multiply(v[1], w[2]) ^ gf8_multiply(v[2], w[1])) == 0

    line_sets = set()
    for i, j in combinations(range(len(points)), 2):
        v, w = points[i], points[j]
        if not orthogonal(v, w):
            continue
        line = {j}
        for scalar in range(8):
            z = tuple(x ^ gf8_multiply(scalar, y) for x, y in zip(v, w))
            line.add(index[normalize(z)])
        assert len(line) == 9
        line_sets.add(tuple(sorted(line)))
    lines = sorted(line_sets)
    pencils = [set() for _ in points]
    for ell, line in enumerate(lines):
        for p in line:
            pencils[p].add(ell)
    assert len(points) == len(lines) == 585
    assert all(len(pencil) == 9 for pencil in pencils)
    # Independent original partial linearity, without relying on construction.
    seen = set()
    for line in lines:
        for pair in combinations(line, 2):
            assert pair not in seen
            seen.add(pair)
    return points, lines, pencils, orthogonal


def real_source_embedding(items):
    points, lines, pencils, orthogonal = geometry_w38()
    p = 0
    ell, r = sorted(pencils[p])[:2]
    q = next(x for x in lines[ell] if x != p)
    assert q not in lines[r]
    # Independent exact GQ projection decoder from the entire true line r.
    projection_points = [x for x in lines[r] if orthogonal(points[q], points[x])]
    assert projection_points == [p]
    assert pencils[q] & pencils[p] == {ell}

    forbidden_points = set(lines[ell]) | set(lines[r])
    forbidden_lines = pencils[q] | pencils[p]
    selected = []
    for point, pencil in enumerate(pencils):
        if point in forbidden_points:
            continue
        line = next((j for j in sorted(pencil) if j not in forbidden_lines), None)
        if line is None:
            continue
        selected.append((point, line))
        forbidden_points.update(lines[line])
        forbidden_lines.update(pencils[point])
        if len(selected) == 15:
            break
    assert len(selected) == 15
    pm, lm = {"q": q, "p": p}, {"ell": ell, "r": r}
    for item, (point, line) in zip(items[:15], selected):
        pm[item[3]] = point
        lm[item[4]] = line
    real_edges = {(pm[e[3]], lm[e[4]]) for e in items}
    induced_edges = {(point, line) for point in pm.values() for line in lm.values()
                     if line in pencils[point]}
    assert real_edges == induced_edges and len(real_edges) == 18
    f = {pm[e[3]]: e[1] for e in items}
    g = {lm[e[4]]: e[2] for e in items}
    assert len(f) == len(g) == 17
    assert len(set(f.values())) == len(set(g.values())) == 17
    # Complete global injections into the minimal physical alphabet.
    a = next(a for a in range(2, 100) if comb(a, 2) >= len(points))
    for injection in (f, g):
        unused = iter(pair for pair in combinations(range(a), 2)
                      if pair not in set(injection.values()))
        for source in range(585):
            if source not in injection:
                injection[source] = next(unused)
        assert len(injection) == len(set(injection.values())) == 585
    assert a == 35
    return {
        "s": 8, "source_point_count": len(points), "source_line_count": len(lines),
        "a_minimal": a, "complete_f_size": len(f), "complete_g_size": len(g),
        "induced_selected_incidence_count": len(induced_edges),
        "anchor_ids": {"q": q, "p": p, "ell": ell, "r": r},
        "selected_matching": selected,
    }


def main():
    items = source_patch()
    counts, leafless = direct_original_sixsets(items)
    assert sum(counts.values()) == 0
    assert leafless == [
        ["A0", "C0", "A1", "B2", "C2", "E"],
        ["B0", "A1", "B2", "C2", "D", "F"],
    ]
    adj, provenance = build_graph([e[:3] for e in items])
    assert all(len({v[0] for v in ns}) == len(ns)
               and len({v[1] for v in ns}) == len(ns) for ns in adj.values())
    assert not graph_cycles(adj, 3) and not graph_cycles(adj, 4)
    cycles = graph_cycles(adj, 6)
    cycle_profiles = Counter(
        (len({x for edge in cyc for x, _ in edge}),
         len({y for edge in cyc for _, y in edge})) for cyc in cycles)
    assert cycle_profiles == {(5, 6): 5, (6, 5): 5}
    u, v = (5, 5), (6, 6)
    paths = [(u, a, b, v) for a in adj[u] for b in adj[a] if v in adj[b]]
    assert len(paths) == 5
    blockers = []
    for path in sorted(paths):
        xs, ys = {x for x, _ in path}, {y for _, y in path}
        assert len(xs) == len(ys) == 4
        assert not ({0, 2} & {5, 6}) and not ({0, 1} & {5, 6})
        left, right = bool({0, 2} & xs), bool({0, 1} & ys)
        assert left or right
        blockers.append({"i": path[1][0], "left": left, "right": right})
    # The main pentagon contains an odd cycle of retained physical pair labels
    # in EACH coordinate alphabet: neither coordinate bicolor cut exists.
    for side in (1, 2):
        mid_pairs = [e[side] for e in items[:15] if e[0].startswith("B")]
        assert len(set().union(*map(set, mid_pairs))) == 5
        assert all(degree == 2 for degree in Counter(x for pair in mid_pairs for x in pair).values())
    embedding = real_source_embedding(items)
    print(json.dumps({
        "scope": "18-incidence induced source subuniverse only; full S uncomputed",
        "original_sixsets_checked": comb(18, 6),
        "seven_counts": counts,
        "leafless_uncharged_sixsets": leafless,
        "physical_edges": len(provenance),
        "physical_vertices_active": len(adj),
        "degree_histogram": dict(Counter(map(len, adj.values()))),
        "C6_coordinate_profiles": {f"{x}/{y}": n for (x, y), n in cycle_profiles.items()},
        "fixed_endpoint_proper_P3": len(paths),
        "path_anchor_blockers": blockers,
        "coordinate_bicolor_cuts": False,
        "real_W38_embedding": embedding,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
