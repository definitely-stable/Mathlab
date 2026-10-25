"""Independent W(3,4) adversarial B/B-overlap certificate oracle.

This deliberately does NOT import the optimizer, cached projection matrix,
ProjectionClosure, or the JSON's reported counts. The geometric incidence
relation comes from the foundational GF(4) symplectic construction; the
physical graph, 3-walks and unique original source projections are rebuilt.
"""
from collections import Counter
from hyp105_b1_symplectic import symplectic_gq


def _source_and_labels(f, g):
    _, points, lines, flags = symplectic_gq(2)
    a = 14
    v = len(points)
    if v != 85 or len(lines) != v or len(flags) != 425:
        raise AssertionError("not the genuine symplectic W(3,4) geometry")
    if len(f) != v or len(g) != v:
        raise ValueError("exactly 85 typed images of each kind are required")
    for images in (f, g):
        pairs = [tuple(edge) for edge in images]
        if any(len(edge) != 2 or type(edge[0]) is not int
               or type(edge[1]) is not int or not 0 <= edge[0] < edge[1] < a
               for edge in pairs) or len(set(pairs)) != v:
            raise ValueError("images must be distinct, ordered K14 edges")
    point_lines = [set() for _ in points]
    for p, l in flags:
        point_lines[p].add(l)
    return lines, flags, point_lines


def independent_w34_census(f, g):
    """Count all four-coordinate-injective physical directed 3-walks.

    Each true original flag (p,l) produces two undirected physical
    opposite-corner edges, one per bijection between its point and line
    image coordinate pairs. Source endpoints are recovered from the
    first/last physical coordinates, then the *unique* GQ 3-path is
    resolved by direct original incidence intersection. No stored
    projections, optimizer scoring routine, or expected counts are read.
    """
    lines, flags, point_lines = _source_and_labels(f, g)
    f = [tuple(e) for e in f]
    g = [tuple(e) for e in g]
    point_of_edge = {frozenset(pair): i for i, pair in enumerate(f)}
    line_of_edge = {frozenset(pair): i for i, pair in enumerate(g)}
    adjacent = {}
    for p, l in flags:
        u, v = f[p]
        x, y = g[l]
        for start, end in (((u, x), (v, y)), ((u, y), (v, x))):
            adjacent.setdefault(start, []).append(end)
            adjacent.setdefault(end, []).append(start)

    # Independent geometric projection: the unique point on target line
    # collinear with the source point, and their common original line.
    projection = {}
    for q in range(85):
        for r in range(85):
            if r in point_lines[q]:
                continue
            candidates = [
                (p, l0)
                for p in lines[r]
                for l0 in point_lines[q]
                if p in lines[l0]
            ]
            if len(candidates) != 1:
                raise AssertionError("GQ nonincident 3-path is not unique")
            projection[q, r] = candidates[0]

    result = Counter()
    for a0, destinations in adjacent.items():
        for a1 in destinations:
            for a2 in adjacent[a1]:
                if len({a0[0], a1[0], a2[0]}) != 3 or len(
                    {a0[1], a1[1], a2[1]}
                ) != 3:
                    continue
                for a3 in adjacent[a2]:
                    xcoords = {a0[0], a1[0], a2[0], a3[0]}
                    ycoords = {a0[1], a1[1], a2[1], a3[1]}
                    if len(xcoords) != 4 or len(ycoords) != 4:
                        continue
                    result["proper_P3"] += 1
                    q = point_of_edge.get(frozenset((a0[0], a3[0])))
                    r = line_of_edge.get(frozenset((a0[1], a3[1])))
                    if q is None or r is None:
                        result["missing"] += 1
                        continue
                    if r in point_lines[q]:
                        result["incident"] += 1
                        continue
                    middle_point, middle_line = projection[q, r]
                    left = not xcoords.isdisjoint(f[middle_point])
                    right = not ycoords.isdisjoint(g[middle_line])
                    if left or right:
                        result["blocked"] += 1
                        result["blocked_left"] += int(left)
                        result["blocked_right"] += int(right)
                        result["blocked_both"] += int(left and right)
                    else:
                        result["unblocked"] += 1
    if result["unblocked"] % 2:
        raise AssertionError("unblocked physical directed paths must pair")
    result["synchronized_BBo"] = result["unblocked"] // 2
    if result["proper_P3"] != (result["missing"] + result["incident"]
                              + result["blocked"] + result["unblocked"]):
        raise AssertionError("physical path partition is not exhaustive")
    if result["blocked"] != (result["blocked_left"] + result["blocked_right"]
                            - result["blocked_both"]):
        raise AssertionError("blocking inclusion-exclusion broken")
    return dict(result)


def independent_bad_endpoint_census(f, g):
    """Typed nonincident (POINT q, LINE r) bad-anchor union.

    For each (q,r), its uniquely projected source 3-path is
    q--l0--p--r. Left-bad means f(q) meets f(p); right-bad means
    g(l0) meets g(r). This is NOT the same measure as bad physical
    3-walks, which may carry unequal multiplicities.
    """
    lines, flags, point_lines = _source_and_labels(f, g)
    left = right = both = 0
    total = 0
    for q in range(85):
        for r in range(85):
            if r in point_lines[q]:
                continue
            paths = [(p, l0) for p in lines[r]
                     for l0 in point_lines[q] if p in lines[l0]]
            if len(paths) != 1:
                raise AssertionError("non-unique GQ projection")
            p, l0 = paths[0]
            is_left = not set(f[q]).isdisjoint(f[p])
            is_right = not set(g[l0]).isdisjoint(g[r])
            total += 1
            left += is_left
            right += is_right
            both += is_left and is_right
    bound_each = 2 * (14 - 2) * 85 * 4
    if left > bound_each or right > bound_each:
        raise AssertionError("typed endpoint union bound violated")
    return {
        "nonincident": total, "left": left, "right": right,
        "both": both, "union": left + right - both,
        "two_sided_upper": 2 * bound_each,
    }
