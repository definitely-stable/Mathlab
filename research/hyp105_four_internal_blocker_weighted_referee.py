"""AA4-MIX4REF: original-ID full/core four-position blocker referee.

All-h inequalities are proved in the companion manuscript. This module is
a FINITE falsifier on genuine W(3,2) and W(3,4), not an asymptotic oracle.
The direct physical and original-source enumerators do not call the older
#672/#676/#678 mixed-blocker classifiers or reuse their reference counts.
"""
from collections import Counter, defaultdict
from itertools import combinations

from hyp105_full_physical_degree_tail import genuine_source


def _check_labels(V, labels):
    a = 2
    while a * (a - 1) // 2 < V:
        a += 1
    if len(labels) != V:
        raise ValueError("incomplete source label assignment")
    pairs = tuple(tuple(p) for p in labels)
    if any(len(p) != 2 or not (0 <= p[0] < p[1] < a) for p in pairs):
        raise ValueError("illegal physical coordinate pair")
    if len(set(pairs)) != V:
        raise ValueError("source point/line injection not global")
    return a, pairs


def _source_projection(V, flags):
    pencils = [set() for _ in range(V)]
    through = [set() for _ in range(V)]
    for p, ell in flags:
        pencils[p].add(ell)
        through[ell].add(p)
    collinear = [
        set().union(*(through[ell] for ell in pencils[p])) - {p}
        for p in range(V)
    ]
    projection = {}
    for q in range(V):
        for r in range(V):
            if r in pencils[q]:
                continue
            anchors = through[r] & collinear[q]
            if len(anchors) != 1:
                raise AssertionError("not a genuine generalized quadrangle projection")
            p = next(iter(anchors))
            common_lines = pencils[q] & pencils[p]
            if len(common_lines) != 1:
                raise AssertionError("original source connecting line not unique")
            projection[q, r] = (p, next(iter(common_lines)))
    return pencils, collinear, projection


def _physical_graph(flags, left, right, ids):
    adjacency = defaultdict(set)
    owners = {}
    for i in ids:
        p, ell = flags[i]
        x, z = left[p]
        y, w = right[ell]
        for v, t in (((x, y), (z, w)), ((x, w), (z, y))):
            key = frozenset((v, t))
            if key in owners:
                raise AssertionError("physical edge owner is not unique")
            owners[key] = i
            adjacency[v].add(t)
            adjacency[t].add(v)
    return adjacency, owners


def _source_books(flags, left, right, ids, pencils, collinear, projection):
    """Enumerate original records, not physical candidate endpoint pairs."""
    V = len(left)
    a = max(max(x) for x in left) + 1
    stars = [set() for _ in range(a)]
    for p, (x, z) in enumerate(left):
        stars[x].add(p)
        stars[z].add(p)
    phi = psi = 0
    triples = set()
    for i in ids:
        u, lam = flags[i]
        for x, k in ((left[u][0], left[u][1]), (left[u][1], left[u][0])):
            for y, t in ((right[lam][0], right[lam][1]),
                         (right[lam][1], right[lam][0])):
                v0, v1 = (x, y), (k, t)
                for p in stars[k]:
                    for q in stars[x] & collinear[p]:
                        z = left[q][0] if left[q][1] == x else left[q][1]
                        for r in pencils[p]:
                            if y not in right[r]:
                                continue
                            phi += 1
                            if r in pencils[q]:
                                psi += 1
                                continue
                            if projection[q, r][0] != p:
                                raise AssertionError("wrong full-source projection")
                            w = right[r][0] if right[r][1] == y else right[r][1]
                            triples.add((v0, v1, (z, w)))
    if phi - psi != len(triples):
        raise AssertionError("nonincident ORIGINAL records are not unique triples")
    return phi, psi, triples


def _physical_triples(adjacency, left, right, projection):
    """Independently enumerate actual physical endpoint cells and first edges."""
    a = max(max(x) for x in left) + 1
    inv_left = {pair: p for p, pair in enumerate(left)}
    inv_right = {pair: r for r, pair in enumerate(right)}
    triples = set()
    for v0, neighbours in adjacency.items():
        x, y = v0
        for v1 in neighbours:
            k = v1[0]
            for z in range(a):
                if x == z:
                    continue
                q = inv_left.get(tuple(sorted((x, z))))
                if q is None:
                    continue
                for w in range(a):
                    if y == w:
                        continue
                    r = inv_right.get(tuple(sorted((y, w))))
                    if r is None:
                        continue
                    anchor = projection.get((q, r))
                    if anchor is not None and k in left[anchor[0]]:
                        triples.add((v0, v1, (z, w)))
    return triples


def _a2_moments(adjacency):
    a2 = {}
    for vertex, neighbours in adjacency.items():
        row = Counter()
        for middle in neighbours:
            row.update(adjacency[middle])
        a2[vertex] = row
    trace4 = sum(value * value for row in a2.values() for value in row.values())
    theta = sum(len(adjacency[v]) *
                sum(value * value for value in row.values())
                for v, row in a2.items())
    delta = max((len(neighbours) for neighbours in adjacency.values()), default=0)
    assert theta <= delta * trace4
    return a2, trace4, theta, delta


def _side_audit(flags, left, right, ids):
    V = len(left)
    pencils, collinear, projection = _source_projection(V, flags)
    graph, owners = _physical_graph(flags, left, right, ids)
    phi, psi, source_triples = _source_books(
        flags, left, right, ids, pencils, collinear, projection)
    physical_triples = _physical_triples(graph, left, right, projection)
    if source_triples != physical_triples:
        missing = len(source_triples - physical_triples)
        extra = len(physical_triples - source_triples)
        raise AssertionError(("source/physical full-core triple discrepancy", missing, extra))
    a2, trace4, theta, delta = _a2_moments(graph)
    weighted = sum(a2.get(v1, {}).get(v3, 0)
                   for _v0, v1, v3 in physical_triples)
    cells = Counter((v1, v3) for _v0, v1, v3 in physical_triples)
    cell_energy = sum(m * a2.get(v1, {}).get(v3, 0) ** 2
                      for (v1, v3), m in cells.items())
    if any(m > len(graph[v1]) for (v1, _v3), m in cells.items()):
        raise AssertionError("first-core-edge multiplicity exceeds physical degree")
    if not (weighted ** 2 <= len(physical_triples) * cell_energy
            <= len(physical_triples) * theta
            <= len(physical_triples) * delta * trace4):
        raise AssertionError("weighted mixed blocker chain failed")
    return {
        "phi": phi, "incident_defect": psi, "blocked_triples": len(physical_triples),
        "weighted_completions": weighted, "cell_energy": cell_energy,
        "degree_weighted_trace4": theta, "trace4": trace4, "delta": delta,
        "edges": len(owners), "source_physical_exact": True,
        "adjacency": graph, "projection": projection,
    }


def _actual_four_positions(graph, left, right, projection):
    """Direct PHYSICAL enumeration; never use any mixed source book or matrix power."""
    inv_left = {p: i for i, p in enumerate(left)}
    inv_right = {p: i for i, p in enumerate(right)}
    by_position = [0, 0, 0, 0]
    union = proper = all_first_left = all_first_right = 0
    for v0, near in graph.items():
        for v1 in near:
            for v2 in graph[v1]:
                for v3 in graph[v2]:
                    x0, y0 = v0
                    x3, y3 = v3
                    if x0 == x3 or y0 == y3:
                        continue
                    q = inv_left.get(tuple(sorted((x0, x3))))
                    r = inv_right.get(tuple(sorted((y0, y3))))
                    anchor = projection.get((q, r)) if q is not None and r is not None else None
                    if anchor is None:
                        continue
                    p, ell = anchor
                    flags = (v1[0] in left[p], v2[0] in left[p],
                             v1[1] in right[ell], v2[1] in right[ell])
                    all_first_left += flags[0]
                    all_first_right += flags[2]
                    if len({v[0] for v in (v0, v1, v2, v3)}) != 4:
                        continue
                    if len({v[1] for v in (v0, v1, v2, v3)}) != 4:
                        continue
                    proper += 1
                    for i, value in enumerate(flags):
                        by_position[i] += value
                    union += any(flags)
    return {
        "all_first_left": all_first_left, "all_first_right": all_first_right,
        "proper_paths_with_decoded_nonincident_ends": proper,
        "proper_blocked_by_position": tuple(by_position), "proper_union": union,
    }


def four_blocker_referee(power, f, g, core_ids=None):
    """Two source-book orientations + PHYSICAL 4-event audit on genuine W32/W34.

    Four indices: first/last inner LEFT, first/last inner RIGHT. Each is an
    actual original nonincident endpoint-projected event. Flags remain
    identical source IDs under duality; only source factor TYPES swap.
    """
    if type(power) is not int or power not in (1, 2):
        raise ValueError("finite original-source oracle only supports h=1,2")
    s, V, original = genuine_source(power)
    a, f = _check_labels(V, f)
    a2, g = _check_labels(V, g)
    if a != a2:
        raise AssertionError("point/line physical alphabets differ")
    ids = tuple(range(len(original))) if core_ids is None else tuple(core_ids)
    if any(type(i) is not int or i < 0 or i >= len(original) for i in ids):
        raise ValueError("unknown original incidence ID")
    if len(set(ids)) != len(ids):
        raise ValueError("duplicate original incidence ID")
    primal = _side_audit(original, f, g, ids)
    dual = _side_audit(tuple((ell, p) for p, ell in original), g, f, ids)
    if (primal["trace4"], primal["degree_weighted_trace4"], primal["delta"]) != (
            dual["trace4"], dual["degree_weighted_trace4"], dual["delta"]):
        raise AssertionError("physical transpose changed weighted fourth moments")
    actual = _actual_four_positions(
        primal["adjacency"], f, g, primal["projection"])
    L = primal["weighted_completions"]
    R = dual["weighted_completions"]
    if actual["all_first_left"] != L or actual["all_first_right"] != R:
        raise AssertionError("direct physical three-walk count disagrees with source books")
    counts = actual["proper_blocked_by_position"]
    if not (counts[0] == counts[1] <= L and counts[2] == counts[3] <= R):
        raise AssertionError("four positional reversal/duality counts do not agree")
    if actual["proper_union"] > 2 * (L + R):
        raise AssertionError("four-position union estimate invalid")
    output = {
        "s": s, "V": V, "core_flags": len(ids), "physical_alphabet": a,
        "primal": {k: v for k, v in primal.items() if k not in ("adjacency", "projection")},
        "dual": {k: v for k, v in dual.items() if k not in ("adjacency", "projection")},
        **actual, "four_position_envelope": 2 * (L + R),
        "all_checks_passed": True,
    }
    return output
