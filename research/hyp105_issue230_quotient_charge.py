"""Independent finite audit of the legal quotient-charge family and C/A lift expectation.

This certifies legal quotient charts and local expectation identities, not S=o(s6).
CLI output defaults to /tmp/issue230-quotient-charge; no fixtures are overwritten.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib
import json
import sys


def remainder(a, b):
    while a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a


def irreducible(n):
    return next(p for p in range((1 << n)|1, 1 << (n+1), 2)
                if all(remainder(p, d)
                       for j in range(1, n//2+1)
                       for d in range((1 << j)|1, 1 << (j+1), 2)))


class Field:
    def __init__(self, n):
        self.n, self.q, self.poly = n, 1 << n, irreducible(n)

    def mul(self, x, y):
        z = 0
        while y:
            if y & 1:
                z ^= x
            y >>= 1
            x <<= 1
            if x & self.q:
                x ^= self.poly
        return z

    def cube(self, x):
        return self.mul(x, self.mul(x, x))

    def inv(self, x):
        assert x
        return next(y for y in range(1, self.q) if self.mul(x, y) == 1)

    def trace(self, x):
        z = 0
        for _ in range(self.n):
            z ^= x
            x = self.mul(x, x)
        assert z in (0, 1)
        return z


def chart(h, r, delta, t):
    D = (3*h+1)//2
    packed = delta | ((t >> (h+1)) << D)
    mask = (1 << h)-1
    return (packed & mask, (packed >> h) & mask,
            ((t >> (r+1)) & ((1 << (h-r))-1)) << r)


def construct(h, r):
    assert h >= 3 and h % 2 and 0 <= r <= h
    s, D, H = 1 << h, (3*h+1)//2, 1 << r
    field = Field(D)
    Q, B, N = field.q, s*s+s+1, s**3
    V = N+B
    a = next(a for a in range(Q, 2*Q) if comb(a, 2) >= V)
    cubes = [field.cube(x) for x in range(Q)]
    pairs = defaultdict(lambda: defaultdict(list))
    for x, y in combinations(range(Q), 2):
        pairs[x ^ y][chart(h, r, x ^ y, cubes[x] ^ cubes[y])].append((x, y))
    slices = {delta: [chart(h, 0, delta, tail << 1)
                      for tail in range(Q//2)] for delta in range(Q)}
    assert len(set(t for rows in slices.values() for t in rows)) == N
    labels, fine, rough = {}, set(), set()
    bad_r, bad_h = [], []
    for delta in range(1, Q):
        inv_cube = field.inv(field.cube(delta))
        is_bad = lambda j: all(field.trace(field.mul(1 << i, inv_cube)) == 0
                               for i in range(j+1))
        br, bh = is_bad(r), is_bad(h)
        if br:
            bad_r.append(delta)
        if bh:
            bad_h.append(delta)
        left_pairs = []
        for base, group in sorted(pairs[delta].items()):
            assert len(group) == H*(1+br)
            for lift, pair in enumerate(group[:H]):
                labels[(base[0], base[1], base[2] | lift)] = pair
            left_pairs.extend(group[H:])
        missing = sorted(set(slices[delta])-labels.keys())
        assert len(missing) == len(left_pairs) == (Q//4 if br else 0)
        if bh:
            for raw, pair in zip(missing, sorted(left_pairs)):
                labels[raw] = pair
                fine.add(raw)
                rough.add(raw)
        elif br:
            raw_groups, pair_groups = defaultdict(list), defaultdict(list)
            for raw in missing:
                raw_groups[raw[:2]].append(raw)
            for x, y in left_pairs:
                key = chart(h, r, x ^ y, cubes[x] ^ cubes[y])[:2]
                pair_groups[key].append((x, y))
            assert raw_groups.keys() == pair_groups.keys()
            for key in raw_groups:
                assert len(raw_groups[key]) == len(pair_groups[key])
                for raw, pair in zip(raw_groups[key], sorted(pair_groups[key])):
                    labels[raw] = pair
                    fine.add(raw)
    extra = [p for p in combinations(range(a), 2) if p[1] >= Q]
    for raw, pair in zip(sorted(slices[0]), extra):
        labels[raw] = pair
        fine.add(raw)
        rough.add(raw)
    boundary_pairs = extra[Q//2:Q//2+B]
    assert len(labels) == N
    assert len(set(labels.values()) | set(boundary_pairs)) == V
    assert len(fine) == Q//2+len(bad_r)*Q//4
    assert len(rough) == Q//2+len(bad_h)*Q//4
    actual_fine, actual_rough = [], []
    for raw, (x, y) in labels.items():
        if y >= Q:
            actual_fine.append(raw)
            actual_rough.append(raw)
            continue
        ex, ey = chart(h, r, x, cubes[x]), chart(h, r, y, cubes[y])
        charge = tuple(a ^ b for a, b in zip(ex, ey))
        coarse_ok = raw[:2] == charge[:2]
        fine_ok = coarse_ok and raw[2] >> r == charge[2] >> r
        assert coarse_ok or raw in rough
        assert fine_ok or raw in fine
        if not coarse_ok:
            actual_rough.append(raw)
        if not fine_ok:
            actual_fine.append(raw)
    if D % 2:
        assert len(bad_r) == Q//(2*H)-1
        assert len(bad_h) == Q//(2*s)-1
    return {"h": h, "r": r, "s": s, "Q": Q, "a": a, "V": V,
            "holes": comb(a, 2)-V, "aux_polynomial": field.poly,
            "bad_r": bad_r, "bad_h": bad_h,
            "fine_exceptions_full": B+len(fine),
            "rough_exceptions_full": B+len(rough),
            "declared_fine_affine": sorted(fine),
            "declared_rough_affine": sorted(rough),
            "actual_fine_affine": sorted(actual_fine),
            "actual_rough_affine": sorted(actual_rough),
            "boundary_pairs": boundary_pairs,
            "affine_labels": [[*raw, *labels[raw]] for raw in sorted(labels)]}


def source_audit(h):
    f, s = Field(h), 1 << h
    points = {(0,)*p+(1,)+tail for p in range(4)
              for tail in product(range(s), repeat=3-p)}
    lines, affine, checked = [], 0, 0
    symp = lambda x, y: (f.mul(x[0], y[2]) ^ f.mul(x[2], y[0])
                        ^ f.mul(x[1], y[3]) ^ f.mul(x[3], y[1]))
    for p, q in combinations(range(4), 2):
        free = [(row, col) for row, pivot in ((0, p), (1, q))
                for col in range(pivot+1, 4) if col != q]
        for values in product(range(s), repeat=len(free)):
            rows = [[0]*4, [0]*4]
            rows[0][p] = rows[1][q] = 1
            for (row, col), value in zip(free, values):
                rows[row][col] = value
            x, y = map(tuple, rows)
            if symp(x, y):
                continue
            lines.append((x, y))
            if (p, q) != (0, 1):
                continue
            affine += 1
            d, c, b = y[3], x[3], x[2]
            assert x[3] == y[2]
            actual = {y} | {tuple(v ^ f.mul(t, w) for v, w in zip(x, y))
                            for t in range(s)}
            assert len(actual) == s+1 and actual <= points
            for u in range(s):
                w, z = c ^ f.mul(u, d), b ^ f.mul(f.mul(u, u), d)
                assert (1, u, z ^ f.mul(u, w), w) in actual
                checked += 1
    V = (s+1)*(s*s+1)
    assert len(points) == len(lines) == V and affine == s**3
    return {"h": h, "points": len(points), "lines": len(lines),
            "boundary_per_type": V-affine, "affine_incidences": checked}


def triangle_audit(h, r):
    f, s, H = Field(h), 1 << h, 1 << r
    same = generic = 0
    for d0, d1 in product(range(1, s), repeat=2):
        if d0 == d1:
            continue
        d2 = d0 ^ d1
        for u0, u1 in product(range(s), repeat=2):
            u2 = f.mul(f.mul(u0, d0) ^ f.mul(u1, d1), f.inv(d2))
            t = (f.mul(f.mul(u0, u0), d0) ^ f.mul(f.mul(u1, u1), d1)
                 ^ f.mul(f.mul(u2, u2), d2))
            if t >> r:
                continue
            if u0 == u1:
                assert u0 == u2
                same += 1
            else:
                assert len({u0, u1, u2}) == 3
                generic += 1
    scale = s**3//H
    assert same == s*(s-1)*(s-2)
    assert generic == same*(H-1)
    return {"h": h, "r": r, "same_u_triangles": scale*same,
            "generic_u_triangles": scale*generic}


def witness_audit():
    """Frozen witness recovered from the old finite oracle; all checks independent."""
    h, r, H = 3, 2, 4
    f, aux = Field(h), Field(5)
    cycle = [0, 4, 27, 1, 12, 9]
    points = [(1, 4, 0), (4, 6, 0), (7, 2, 6)]
    lines = [(4, 0, 4), (7, 7, 4), (2, 7, 0),
             (5, 1, 5), (5, 4, 3), (1, 5, 5)]
    point_pairs = [(4, 5), (1, 21), (7, 16)]
    line_pairs = [tuple(sorted((cycle[i], cycle[(i+1)%6]))) for i in range(6)]
    cubes = [aux.cube(x) for x in range(32)]
    def fine_charge(pair):
        x, y = pair
        return chart(h, r, x ^ y, cubes[x] ^ cubes[y])
    case = construct(h, r)
    bad = {0, *case["bad_r"]}
    for raw, pair in list(zip(points, point_pairs))+list(zip(lines, line_pairs)):
        assert pair[0] ^ pair[1] not in bad
        charge = fine_charge(pair)
        assert raw[:2] == charge[:2] and raw[2] >> r == charge[2] >> r
    six = [(i, j) for i in range(3) for j in (i, i+3)]
    assert len(set(six)) == 6
    for i, j in six:
        u, w, z = points[i]
        d, c, b = lines[j]
        assert w ^ c == f.mul(u, d)
        assert z ^ b == f.mul(f.mul(u, u), d)
    assert len(set(points)) == 3 and len(set(lines)) == 6
    assert len({x for pair in point_pairs for x in pair}) == 6
    for pairs in ([point_pairs[i] for i, j in six], [line_pairs[j] for i, j in six]):
        degrees = Counter(x for pair in pairs for x in pair)
        assert len(degrees) == 6 and set(degrees.values()) == {2}
    assert sorted(Counter(i for i, j in six).values()) == [2, 2, 2]
    assert sorted(Counter(j for i, j in six).values()) == [1]*6
    success = 0
    us = [p[0] for p in points]
    ds = [lines[i][0] ^ lines[i+3][0] for i in range(3)]
    assert len(set(us)) == 3 and all(ds)
    for lifts in product(range(H), repeat=6):
        bs = [(lines[i][2] >> r << r) | lifts[i] for i in range(6)]
        if all(bs[i] ^ bs[i+3] == f.mul(f.mul(us[i], us[i]), ds[i])
               for i in range(3)):
            success += 1
    assert success == H**3
    return {"h": h, "r": r, "class": "C/A",
            "cycle": cycle, "points": points, "lines": lines,
            "point_pairs": point_pairs, "line_pairs": line_pairs,
            "u": us, "D": ds, "all_factors_regular": True,
            "lift_assignments": H**6, "lift_successes": success}


def main(output_dir=Path("/tmp/issue230-quotient-charge")):
    evidence = {"status": "LEGAL_CHART_AND_SCOPED_EXPECTATION_ONLY",
                "source": source_audit(3),
                "cases": [construct(3, r) for r in (1, 2)],
                "triangles": [triangle_audit(3, r) for r in (1, 2)],
                "witness": witness_audit()}
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / "quotient_charge_evidence.json"
    path.write_text(json.dumps(evidence, indent=2)+"\n")
    for case in evidence["cases"]:
        print(json.dumps({k: case[k] for k in
                          ("h", "r", "Q", "a", "V", "holes",
                           "fine_exceptions_full", "rough_exceptions_full")}, sort_keys=True))
    print(json.dumps(evidence["source"], sort_keys=True))
    print(json.dumps(evidence["triangles"], sort_keys=True))
    print(json.dumps({"witness_class": evidence["witness"]["class"],
                      "lift_assignments": evidence["witness"]["lift_assignments"],
                      "lift_successes": evidence["witness"]["lift_successes"]}))
    print("sha256="+hashlib.sha256(path.read_bytes()).hexdigest())


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv)>1 else Path("/tmp/issue230-quotient-charge"))
