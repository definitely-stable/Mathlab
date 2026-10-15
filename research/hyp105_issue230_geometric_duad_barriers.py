"""Independent finite falsifiers for the scoped all-h geometric duad no-go.

Read-only use of the downloaded source; writes no repository files.
Method A: direct 5D quadratic-space enumeration.
Method B: true-source point pencils mapped by exterior minors.
Also checks every true W32 source point subset against the sharp spectral
pair capacity inequality, and exact minimal-palette arithmetic.
"""
from itertools import combinations, product
from math import comb, isqrt
from pathlib import Path
import json
import sys

from hyp105_b1_symplectic import GF2Power, symplectic_gq, symplectic


def normalize(v, f):
    pivot = next((x for x in v if x), None)
    if pivot is None:
        raise ValueError("zero has no projective normalization")
    c = f.inv(pivot)
    return tuple(f.mul(x, c) for x in v)


def add(v, w):
    return tuple(x ^ y for x, y in zip(v, w))


def scale(c, v, f):
    return tuple(f.mul(c, x) for x in v)


def q_form(v, f):
    a, b, c, d, e = v
    return f.mul(a, e) ^ f.mul(b, b) ^ f.mul(c, d)


def polar(v, w, f):
    # Computed from the four-term polar expression independently of q_form.
    return (f.mul(v[0], w[4]) ^ f.mul(v[4], w[0]) ^
            f.mul(v[2], w[3]) ^ f.mul(v[3], w[2]))


def span2(v, w, f):
    return frozenset(add(scale(a, v, f), scale(b, w, f))
                     for a in range(f.q) for b in range(f.q))


def plucker5(v, w, f):
    # Minors 01,02,03,12,13,23; isotropy identifies 02=13.
    p = tuple(f.mul(v[i], w[j]) ^ f.mul(v[j], w[i])
              for i, j in combinations(range(4), 2))
    assert p[1] == p[4]
    return normalize((p[0], p[1], p[2], p[3], p[5]), f)


def direct_quadratic_planes(h):
    f = GF2Power(h)
    all_vectors = tuple(product(range(f.q), repeat=5))
    singular = tuple(v for v in all_vectors if q_form(v, f) == 0)
    points = tuple(sorted({normalize(v, f) for v in singular if any(v)}))
    planes = set()
    for v, w in combinations(points, 2):
        if polar(v, w, f) == 0:
            planes.add(span2(v, w, f))
    expected = (f.q + 1) * (f.q * f.q + 1)
    assert len(points) == expected
    assert len(planes) == expected
    # Exhaustive common-neighbor lemma in each maximal singular 2-space.
    for w_space in planes:
        v1 = next(v for v in w_space if any(v))
        v2 = next(v for v in w_space if any(v) and normalize(v, f) != normalize(v1, f))
        common = frozenset(v for v in singular
                           if polar(v, v1, f) == 0 and polar(v, v2, f) == 0)
        assert common == w_space
    return f, planes


def true_source_planes(h):
    # No quadratic-space point enumeration is used to construct this set.
    f, points, lines, incidences = symplectic_gq(h)
    line_vectors = tuple(plucker5(points[line[0]], points[line[1]], f)
                         for line in lines)
    assert len(set(line_vectors)) == len(lines)
    by_point = [[] for _ in points]
    for p, l in incidences:
        by_point[p].append(line_vectors[l])
    planes = set()
    for pencil in by_point:
        w = span2(pencil[0], pencil[1], f)
        assert {normalize(v, f) for v in w if any(v)} == set(pencil)
        planes.add(w)
    return planes


def all_w32_subsets_spectral_bound():
    f, points, _, _ = symplectic_gq(1)
    n = len(points)
    neighbors = [sum(1 << j for j in range(n)
                     if i != j and symplectic(points[i], points[j], f) == 0)
                 for i in range(n)]
    counts = [0] * (1 << n)
    for mask in range(1, 1 << n):
        bit = mask & -mask
        i = bit.bit_length() - 1
        smaller = mask ^ bit
        counts[mask] = counts[smaller] + (neighbors[i] & smaller).bit_count()
        x = mask.bit_count()
        assert 2 * (f.q + 1) * counts[mask] <= (f.q * f.q - 1) * x + x * x
    return len(counts)


def affine_three_wedge_condition(h):
    f = GF2Power(h)
    left_count = right_count = 0
    # Every nonzero triple summing to zero is (D,E,D+E), D!=E.
    differences = [(d, e, d ^ e) for d in range(1, f.q)
                   for e in range(1, f.q) if d != e]
    for first_parameters in product(range(f.q), repeat=3):
        for delta in differences:
            first = 0
            left_second = right_second = 0
            for u, d in zip(first_parameters, delta):
                first ^= f.mul(u, d)
                left_second ^= f.mul(f.mul(u, u), d)
                right_second ^= f.mul(u, f.mul(d, d))
            if first == 0 and left_second == 0:
                assert len(set(first_parameters)) == 1
                left_count += 1
            if first == 0 and right_second == 0:
                assert len(set(first_parameters)) == 1
                right_count += 1
    expected = f.q * (f.q - 1) * (f.q - 2)
    assert left_count == right_count == expected
    return {"s": f.q, "left_C_same_first_parameter_solutions": left_count,
            "right_C_same_first_parameter_solutions": right_count,
            "nonzero_three_differences_exhaustive": True}


def affine_chart_true_source(h):
    f, points, lines, incidences = symplectic_gq(h)
    original_index = {p: i for i, p in enumerate(points)}
    true_lines = {frozenset(line): l for l, line in enumerate(lines)}
    affine_point_ids = {original_index[(1, u, v, w)]
                        for u, v, w in product(range(f.q), repeat=3)}
    generated = set()
    actual_chart_inc = set()
    for d, c, b in product(range(f.q), repeat=3):
        basis0 = (1, 0, b, c)
        basis1 = (0, 1, c, d)
        assert symplectic(basis0, basis1, f) == 0
        line_points = {original_index[normalize(add(basis0, scale(u, basis1, f)), f)]
                       for u in range(f.q)}
        line_points.add(original_index[normalize(basis1, f)])
        l = true_lines[frozenset(line_points)]
        generated.add(l)
        for u in range(f.q):
            v = b ^ f.mul(c, u)
            w = c ^ f.mul(d, u)
            z = v ^ f.mul(u, w)
            assert (w ^ c) == f.mul(u, d)
            assert (z ^ b) == f.mul(f.mul(u, u), d)
            actual_chart_inc.add((original_index[(1, u, v, w)], l))
    from_original = {(p, l) for p, l in incidences
                     if p in affine_point_ids and l in generated}
    assert actual_chart_inc == from_original
    assert len(generated) == f.q ** 3
    assert len(actual_chart_inc) == f.q ** 4
    return {"s": f.q, "affine_chart_original_points": len(affine_point_ids),
            "affine_chart_original_lines": len(generated),
            "pointwise_true_original_incidence_identity": True,
            "affine_chart_incidence_count": len(actual_chart_inc)}


def palette_arithmetic(h):
    s = 1 << h
    v = (s + 1) * (s * s + 1)
    a = isqrt(2 * v)
    while comb(a, 2) < v:
        a += 1
    assert comb(a - 1, 2) < v <= comb(a, 2)
    holes = comb(a, 2) - v
    assert 0 <= holes <= a - 2
    # All-h proof uses these three inequalities from s>=8.
    if h >= 3:
        assert a >= 35
        assert 100 * (s + 1) <= a * a
        # .18a²-.3a-(s+1) exceeds a²/100.
        assert 17 * a * a > 30 * a + 100 * (s + 1)
    if h >= 5:
        assert a >= 200
        assert a * a - 100 * a >= v
    # Rounded exact sharp source-geometric duad distinct-line capacity.
    joined_lines_upper = ((s * s - 1) * a + a * a) // (2 * (s + 1))
    return {"h": h, "s": s, "V": v, "a": a, "holes": holes,
            "literal_source_duad_line_upper": joined_lines_upper,
            "V_fraction_geometric_line_upper": joined_lines_upper / v}


def main():
    quadratic = []
    for h in (1, 2):
        f, direct = direct_quadratic_planes(h)
        source = true_source_planes(h)
        assert direct == source
        quadratic.append({"s": f.q, "direct_maximal_singular_planes": len(direct),
                          "independent_true_source_pencils": len(source),
                          "common_neighbor_lemma_exhaustive": True,
                          "pointwise_plane_set_identity": True})
    print(json.dumps({"status": "RESTRICTED_CONSTRUCTION_NO_GO_ONLY",
                      "quadratic_two_method_falsifiers": quadratic,
                      "all_w32_point_subsets_spectral_bound": all_w32_subsets_spectral_bound(),
                      "affine_true_source_chart": [affine_chart_true_source(h) for h in (1, 2)],
                      "affine_three_wedge_exact_falsifiers": [affine_three_wedge_condition(h) for h in (1, 2, 3)],
                      "exact_palette_arithmetic": [palette_arithmetic(h) for h in range(1, 13)],
                      "Branch_B_constructed": False}, indent=2))


if __name__ == "__main__":
    main()
