"""HYP-105 G5-C3-B1.0: exact symplectic W(3,2^h) field/incidence oracle.

A reusable *classical* GQ(s,s) foundation, not an ASET construction.
All numeric checks for s=2/4 have an independent projective GQ axiom oracle.
No integer arithmetic modulo 4 is ever used as GF(4) multiplication.
"""
from itertools import product, combinations
from collections import Counter


IRREDUCIBLE = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011}


class GF2Power:
    def __init__(self, power):
        if power not in IRREDUCIBLE:
            raise ValueError("supported extensions GF(2), GF(4), GF(8), GF(16)")
        self.h = power
        self.q = 1 << power
        self.polynomial = IRREDUCIBLE[power]
        self.mask = self.q - 1

    def check(self, value):
        if not isinstance(value, int) or value < 0 or value >= self.q:
            raise ValueError("field element outside GF(2^h)")
        return value

    def add(self, a, b):
        return self.check(a) ^ self.check(b)

    def mul(self, a, b):
        """Multiply polynomials modulo the chosen irreducible polynomial."""
        self.check(a)
        self.check(b)
        result = 0
        while b:
            if b & 1:
                result ^= a
            a <<= 1
            if a & self.q:
                a ^= self.polynomial
            b >>= 1
        return result & self.mask

    def pow(self, a, e):
        self.check(a)
        if not isinstance(e, int) or e < 0:
            raise ValueError("nonnegative integer exponent required")
        value = 1
        while e:
            if e & 1:
                value = self.mul(value, a)
            a = self.mul(a, a)
            e >>= 1
        return value

    def inv(self, a):
        self.check(a)
        if not a:
            raise ZeroDivisionError("GF inversion of zero")
        return self.pow(a, self.q - 2)


def normalized(vec, field):
    """Unique projective representative, earliest nonzero entry = 1."""
    if len(vec) != 4 or any(not isinstance(x, int) or x < 0 or x >= field.q
                            for x in vec):
        raise ValueError("expected vector GF(q)^4")
    first = next((x for x in vec if x), None)
    if first is None:
        raise ValueError("zero vector not a projective point")
    inv = field.inv(first)
    return tuple(field.mul(x, inv) for x in vec)


def projective_points(field):
    return tuple(sorted({
        normalized(v, field) for v in product(range(field.q), repeat=4)
        if any(v)
    }))


def symplectic(u, v, field):
    """Nondegenerate alternating 4D form u0*v2+u2*v0+u1*v3+u3*v1."""
    if len(u) != 4 or len(v) != 4:
        raise ValueError("expected GF(q)^4")
    return (field.mul(u[0], v[2]) ^ field.mul(u[2], v[0])
            ^ field.mul(u[1], v[3]) ^ field.mul(u[3], v[1]))


def span_projective_line(u, v, field):
    """Projective 2-subspace, u and v are distinct normalized points."""
    if u == v or symplectic(u, v, field) != 0:
        raise ValueError("distinct orthogonal points required")
    members = {normalized(v, field)}
    for lam in range(field.q):
        members.add(normalized(tuple(
            x ^ field.mul(lam, y) for x, y in zip(u, v)), field))
    if len(members) != field.q + 1:
        raise AssertionError("projective line must have q+1 points")
    return frozenset(members)


def symplectic_gq(power):
    """Enumerate W(3, 2^h) using symplectic orthogonal pair spans."""
    field = GF2Power(power)
    points = projective_points(field)
    index = {p: i for i, p in enumerate(points)}
    lines = set()
    for u, v in combinations(points, 2):
        if symplectic(u, v, field) == 0:
            members = span_projective_line(u, v, field)
            lines.add(tuple(sorted(index[p] for p in members)))
    lines = tuple(sorted(lines))
    incidences = tuple((p, j) for j, line in enumerate(lines)
                       for p in line)
    return field, points, lines, incidences


def exact_gq_certificate(power):
    field, points, lines, incidences = symplectic_gq(power)
    s = field.q
    v = (s + 1) * (s * s + 1)
    if len(points) != v or len(lines) != v:
        raise AssertionError("projective/GQ point or line formula")
    if len(incidences) != v * (s + 1):
        raise AssertionError("GQ incidence formula")
    if len(set(incidences)) != len(incidences):
        raise AssertionError("duplicate incidence")
    degree = Counter(p for p, _ in incidences)
    if len(degree) != v or set(degree.values()) != {s + 1}:
        raise AssertionError("incorrect regular degree")
    if any(len(line) != s + 1 for line in lines):
        raise AssertionError("incorrect isotropic line size")
    if any(symplectic(points[u], points[w], field)
           for line in lines for u, w in combinations(line, 2)):
        raise AssertionError("nonisotropic projective line")
    return {
        "field": f"GF(2^{power})", "s": s,
        "points": len(points), "lines": len(lines),
        "incidences": len(incidences), "degree": s + 1,
        "classical_preexisting": True,
        "new_aset_exponent": False,
    }


if __name__ == "__main__":
    import json
    print(json.dumps([exact_gq_certificate(1), exact_gq_certificate(2)],
                     sort_keys=True, indent=2))
