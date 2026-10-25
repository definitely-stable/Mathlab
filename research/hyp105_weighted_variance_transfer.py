"""HYP-105 #230 AA4-VT: centered-variance transfer and exact W(3,2) sign falsifiers.

Finitely certified counterexamples to both uniform sign assumptions on
Cov(1_B,N3). All-h transfer is an exact conditional inequality only:
no claimed variance bound or strict GF(5) six-original-flag result.
"""
from collections import Counter
from fractions import Fraction

from hyp105_b1_symplectic import symplectic_gq


def centered_transfer(U, b, P, Q, M):
    """A sharp finite-population centered Cauchy–Schwarz inequality.

    U: number of all source typed nonincident POINT/LINE pairs.
    b: count of bad source pairs; P: sum of N3 over all such pairs;
    Q: sum of N3**2; M: sum of N3 over bad pairs.

    All integer fields are exact. This theorem has no independence
    assumptions and does not imply M=o(s**6).
    """
    if any(type(x) is not int for x in (U, b, P, Q, M)):
        raise ValueError("exact integer inputs required")
    if U <= 0 or not (0 <= b <= U and 0 <= M <= P) or P < 0 or Q < 0:
        raise ValueError("invalid finite-population moments")
    variance_numerator = U * Q - P * P
    if variance_numerator < 0:
        raise ValueError("negative centered second moment")
    deviation_numerator = U * M - b * P
    slack_numerator = (
        b * (U - b) * variance_numerator - deviation_numerator**2
    )
    if slack_numerator < 0:
        raise ValueError("violates centered Cauchy–Schwarz: inconsistent ledger")
    if P == 0 and (M != 0 or Q != 0):
        raise ValueError("zero total nonnegative multiplicity requires Q=0")
    return {
        "deviation_numerator": deviation_numerator,
        "covariance": Fraction(deviation_numerator, U * U),
        "weighted_minus_unweighted_fraction": (
            Fraction(M, P) - Fraction(b, U) if P else Fraction(0)
        ),
        "chi_square": Fraction(U * Q, P * P) - 1 if P else Fraction(0),
        "centered_second_moment_numerator": variance_numerator,
        "exact_cauchy_slack": slack_numerator,
        "sign": 1 if deviation_numerator > 0 else (
            -1 if deviation_numerator < 0 else 0
        ),
    }


def deterministic_k6_edges(seed):
    """Fixed LCG/Fisher–Yates generator; independent of Python RNG versions."""
    edges = [(u, v) for u in range(6) for v in range(u + 1, 6)]
    state = seed & 0xFFFFFFFF
    for i in range(len(edges) - 1, 0, -1):
        state = (1664525 * state + 1013904223) & 0xFFFFFFFF
        j = (state * (i + 1)) // (1 << 32)
        edges[i], edges[j] = edges[j], edges[i]
    return tuple(edges)


def witness_maps(seed):
    """Full globally injective K6 labels for genuine W(3,2), arbitrary correlation."""
    if type(seed) is not int or seed < 0:
        raise ValueError("nonnegative integer seed required")
    return (deterministic_k6_edges(31 + 17 * seed),
            deterministic_k6_edges(900 + 29 * seed))


def _geometry():
    _, points, lines, flags = symplectic_gq(1)
    if (len(points), len(lines), len(flags)) != (15, 15, 45):
        raise AssertionError("not original symplectic W(3,2)")
    point_lines = [set() for _ in points]
    for p, l in flags:
        point_lines[p].add(l)
    projection = {}
    for q in range(15):
        for r in range(15):
            if r in point_lines[q]:
                continue
            candidates = [(p, l0) for p in lines[r]
                          for l0 in point_lines[q] if p in lines[l0]]
            if len(candidates) != 1:
                raise AssertionError("GQ unique nonincident 3-path failed")
            projection[q, r] = candidates[0]
    if len(projection) != 180:
        raise AssertionError("incorrect original nonincident universe")
    return flags, projection


def _physical_adj(f, g, flags):
    if len(f) != 15 or len(g) != 15:
        raise ValueError("15 images per typed source factor required")
    for image in (f, g):
        if (len(set(map(tuple, image))) != 15 or
                any(len(pair) != 2 or
                    any(type(x) is not int for x in pair) or
                    not 0 <= pair[0] < pair[1] < 6
                    for pair in image)):
            raise ValueError("globally injected ordered K6 physical edges required")
    adj = {}
    for p, l in flags:
        u, v = f[p]
        x, y = g[l]
        for z, w in (((u, x), (v, y)), ((u, y), (v, x))):
            adj.setdefault(z, []).append(w)
            adj.setdefault(w, []).append(z)
    # All-h simple adjacency lemma: the two unordered coordinate pairs
    # of any physical arc uniquely identify one original (p,l) flag.
    if any(len(neighbors) != len(set(neighbors))
           for neighbors in adj.values()):
        raise AssertionError("source global injections forbid parallel arcs")
    return adj


def w32_weighted_census(f, g, *, verify_corner_join=True):
    """Compute true W(3,2) N3 by direct walks and independent corner contraction."""
    flags, projection = _geometry()
    f = tuple(map(tuple, f))
    g = tuple(map(tuple, g))
    adj = _physical_adj(f, g, flags)
    f_inv = {frozenset(pair): i for i, pair in enumerate(f)}
    g_inv = {frozenset(pair): i for i, pair in enumerate(g)}
    bad = {
        (q, r): bool(set(f[q]) & set(f[p]) or set(g[r]) & set(g[l0]))
        for (q, r), (p, l0) in projection.items()
    }
    counts = Counter()
    proper = missing = incident = 0
    for v0, nb0 in adj.items():
        for v1 in nb0:
            for v2 in adj.get(v1, ()):
                if (len({v0[0], v1[0], v2[0]}) < 3
                        or len({v0[1], v1[1], v2[1]}) < 3):
                    continue
                for v3 in adj.get(v2, ()):
                    if (len({v0[0], v1[0], v2[0], v3[0]}) != 4
                            or len({v0[1], v1[1], v2[1], v3[1]}) != 4):
                        continue
                    proper += 1
                    q = f_inv.get(frozenset((v0[0], v3[0])))
                    r = g_inv.get(frozenset((v0[1], v3[1])))
                    if q is None or r is None:
                        missing += 1
                    elif (q, r) not in projection:
                        incident += 1
                    else:
                        counts[q, r] += 1
    if verify_corner_join:
        # Other enumeration: fix each ORIGINAL (q,r) endpoint pair and
        # contract its four physical opposite-corner orientations.
        arc = {key: Counter(val) for key, val in adj.items()}
        for (q, r) in projection:
            x0, x3 = f[q]
            y0, y3 = g[r]
            value = 0
            for startx, endx in ((x0, x3), (x3, x0)):
                for starty, endy in ((y0, y3), (y3, y0)):
                    start, end = (startx, starty), (endx, endy)
                    for v1, m1 in arc.get(start, {}).items():
                        if v1[0] in (startx, endx) or v1[1] in (starty, endy):
                            continue
                        for v2, m2 in arc.get(v1, {}).items():
                            if (v2[0] in (startx, endx, v1[0]) or
                                    v2[1] in (starty, endy, v1[1])):
                                continue
                            value += m1 * m2 * arc.get(v2, {}).get(end, 0)
            if value != counts[q, r]:
                raise AssertionError(f"independent corner mismatch {(q, r)}")
    U = len(projection)
    b = sum(bad.values())
    P = sum(counts.values())
    Q = sum(counts[k] ** 2 for k in projection)
    M = sum(counts[k] for k in projection if bad[k])
    certificate = centered_transfer(U, b, P, Q, M)
    certificate.update({
        "U": U, "b": b, "P": P, "Q": Q, "M": M,
        "proper": proper, "missing": missing, "incident": incident,
        "max_N3": max(counts.values(), default=0),
        "zero_N3": sum(counts[k] == 0 for k in projection),
    })
    if P != proper - missing - incident:
        raise AssertionError("invalid physical walk endpoint partition")
    return certificate
