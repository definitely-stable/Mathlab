"""HYP-105 C24-A1: deterministic right-C star-collision certificate.

All-h bound concerns one globally coherent original-right pair-label map.
W(3,2) provides a finite C-only zero witness, NOT a seven-class minimum.
The generator is deliberately independent of previous Mathlab classifiers.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import isqrt

K6_PAIRS = tuple(combinations(range(6), 2))
# Sorted ORIGINAL GF(2)^4 symplectic lines; i -> K6_PAIRS[perm[i]].
W32_RIGHT_C_ZERO_WITNESS = (1, 13, 3, 6, 10, 9, 8, 0, 7, 2, 11, 5, 14, 12, 4)


def symplectic_form_gf2(x, y):
    return ((x & 1) * ((y >> 2) & 1) + ((x >> 2) & 1) * (y & 1)
            + ((x >> 1) & 1) * ((y >> 3) & 1)
            + ((x >> 3) & 1) * ((y >> 1) & 1)) & 1


def original_W32():
    """Fifteen points, fifteen totally isotropic lines, forty-five incidences."""
    points = tuple(range(1, 16))
    lines = tuple(sorted({tuple(sorted((p, q, p ^ q)))
                          for p, q in combinations(points, 2)
                          if symplectic_form_gf2(p, q) == 0}))
    incidences = tuple((p, j) for j, line in enumerate(lines) for p in line)
    if (len(lines), len(incidences)) != (15, 45) or any(
            sum(p in line for line in lines) != 3 for p in points):
        raise AssertionError("invalid original W(3,2) incidence host")
    if any(sum(p in line and q in line for line in lines) > 1
           for p, q in combinations(points, 2)):
        raise AssertionError("original GQ contains a forbidden 4-cycle")
    return points, lines, incidences


def degree_two_on_six_coordinates(edges):
    degree = Counter(u for e in edges for u in e)
    return len(degree) == 6 and set(degree.values()) == {2}


def W32_right_C_source():
    """Right-first: three distinct ORIGINAL lines, two incID edges each.

    One ORIGINAL point->physical-pair bijection: p=1..15 to lex K6_PAIRS.
    """
    points, lines, _ = original_W32()
    point_to_pair = {p: K6_PAIRS[i] for i, p in enumerate(points)}
    triples = Counter()
    for ids in combinations(range(15), 3):
        for picks in product(*(combinations(lines[j], 2) for j in ids)):
            physical_left = (point_to_pair[p] for pair in picks for p in pair)
            if degree_two_on_six_coordinates(physical_left):
                triples[ids] += 1
    if (sum(triples.values()), len(triples)) != (92, 83):
        raise AssertionError("W32 exact right-C source mismatch")
    return triples


def right_C_pair_weights(triples, V):
    """W_ij counts ORIGINAL sixsets containing both i,j; sum(i<j)W_ij=3H."""
    if type(V) is not int or V < 3:
        raise ValueError("V must be integer >= 3")
    W = [[0] * V for _ in range(V)]
    H = 0
    for triple, count in triples.items():
        if (len(triple) != 3 or len(set(triple)) != 3 or
            any(type(x) is not int or not 0 <= x < V for x in triple) or
            type(count) is not int or count <= 0):
            raise ValueError("invalid ORIGINAL right triple and multiplicity")
        H += count
        for i, j in combinations(sorted(triple), 2):
            W[i][j] += count
            W[j][i] += count
    if sum(sum(row) for row in W) != 6 * H:
        raise AssertionError("right-C pair weights lost original multiplicity")
    return tuple(tuple(row) for row in W)


def checked_global_right_map(perm, occupied):
    V = len(occupied)
    if (len(perm) != V or any(type(x) is not int for x in perm)
            or set(perm) != set(range(V))):
        raise ValueError("one complete global ORIGINAL right bijection required")
    if len(set(occupied)) != V or any(
        len(e) != 2 or type(e[0]) is not int or type(e[1]) is not int or
        not 0 <= e[0] < e[1] for e in occupied
    ):
        raise ValueError("distinct canonical occupied physical K_a pairs required")
    return tuple(occupied[i] for i in perm)


def accepted_right_C(triples, perm, occupied):
    mapped = checked_global_right_map(perm, occupied)
    return sum(n for triple, n in triples.items()
               if all(set(mapped[i]).isdisjoint(mapped[j])
                      for i, j in combinations(triple, 2)))


def exact_star_collision_upper(W, perm, occupied):
    """SUM_x SUM_{i<j in L_x(g)} W_ij, an upper on rejected C sixsets."""
    mapped = checked_global_right_map(perm, occupied)
    V = len(mapped)
    if len(W) != V or any(len(row) != V for row in W):
        raise ValueError("W must match global-right universe")
    stars = {}
    for i, edge in enumerate(mapped):
        for x in edge:
            stars.setdefault(x, []).append(i)
    return sum(W[i][j] for ids in stars.values()
               for i, j in combinations(ids, 2))


def star_collision_certificate(triples, W, perm, occupied):
    H = sum(triples.values())
    if (len(W) != len(occupied) or
        any(len(row) != len(W) for row in W) or
        any(W[i][i] != 0 or any(W[i][j] != W[j][i] or W[i][j] < 0
                                for j in range(len(W))) for i in range(len(W))) or
        sum(sum(row) for row in W) != 6 * H):
        raise ValueError("malformed symmetric ORIGINAL right-C pair tensor")
    S = accepted_right_C(triples, perm, occupied)
    bad_upper = exact_star_collision_upper(W, perm, occupied)
    if S < H - bad_upper:
        raise AssertionError("deterministic right-C star inequality is false")
    return {"H_C": H, "accepted_right_C": S,
            "star_conflict_upper": bad_upper,
            "certified_lower": max(0, H - bad_upper),
            "number_of_original_right_triples": len(triples)}


def all_h_star_geometry_fraction(V, a):
    if (type(V) is not int or type(a) is not int or
            V < 3 or a < 3 or V > a * (a - 1) // 2):
        raise ValueError("invalid physical pair alphabet")
    return 1 - Fraction(6 * (a - 2), V - 1)


def rigorous_centered_norm_upper(W, H):
    """Exact rational upper on ||B||_op, NOT an exact eigenvalue.

    B = W - mu*(J-I), mu=6H/(V*(V-1)).
    Both max absolute row sum and ceil Frobenius norm upper bound ||B||op.
    """
    V = len(W)
    if (V < 3 or any(len(row) != V for row in W) or
        any(W[i][j] != W[j][i] or W[i][j] < 0
            for i in range(V) for j in range(V)) or
        any(W[i][i] for i in range(V)) or
        sum(sum(row) for row in W) != 6 * H):
        raise ValueError("W must be symmetric right-C weights with sum 6H")
    mu = Fraction(6 * H, V * (V - 1))
    rows = [sum((abs(Fraction(W[i][j]) - mu)
                 for j in range(V) if i != j), Fraction(0)) for i in range(V)]
    sq = sum(((Fraction(W[i][j]) - mu) ** 2
              for i in range(V) for j in range(V) if i != j), Fraction(0))
    ceiling = (sq.numerator + sq.denominator - 1) // sq.denominator
    frobenius_integer = isqrt(ceiling)
    if frobenius_integer ** 2 < ceiling:
        frobenius_integer += 1
    return min(max(rows), Fraction(frobenius_integer)), mu


def uniform_right_C_certificate(W, H, a):
    """All-f,g CONDITIONAL bound; without all-f control it proves no Omega(s6)."""
    V = len(W)
    geometry = all_h_star_geometry_fraction(V, a)
    norm_upper, mu = rigorous_centered_norm_upper(W, H)
    raw = H * geometry - V * norm_upper
    return {"H_C": H, "V": V, "a": a,
            "geometry_coefficient": geometry, "mu": mu,
            "certified_operator_norm_upper": norm_upper,
            "raw_lower_bound": raw,
            "nonnegative_certified_lower": max(Fraction(0), raw),
            "is_universal_positive_proof": False}


def genuine_W32_C24_report():
    import json
    triples = W32_right_C_source()
    W = right_C_pair_weights(triples, 15)
    fixed = star_collision_certificate(triples, W,
                                       W32_RIGHT_C_ZERO_WITNESS, K6_PAIRS)
    uniform = uniform_right_C_certificate(W, fixed["H_C"], 6)
    return {"true_original_W32_15_points_lines_45_incidences": True,
            "right_C_exact_global_zero_witness": list(W32_RIGHT_C_ZERO_WITNESS),
            **fixed,
            "global_uniform_right_C_mean": str(Fraction(3, 91) * fixed["H_C"]),
            "s2_star_geometry_coefficient": str(uniform["geometry_coefficient"]),
            "s2_certified_uniform_lower": str(uniform["nonnegative_certified_lower"]),
            "no_all_h_S_seven_minimum_claim": True}


if __name__ == "__main__":
    import json
    print(json.dumps(genuine_W32_C24_report(), indent=2, sort_keys=True))
