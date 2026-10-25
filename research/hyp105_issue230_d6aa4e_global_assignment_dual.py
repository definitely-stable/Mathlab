"""Issue #230 D6-AA4-E: exact typed-source global assignment dual.
All-h conditional weak dual; small exact positive and negative falsifiers.
NO claimed all-h positive GF5 seven-motif bound or ASET exponent.
"""
from fractions import Fraction
from itertools import permutations, product
from math import comb, factorial, isqrt


def alphabet_capacity(s):
    if type(s) is not int or s < 2 or s & (s-1):
        raise ValueError("s must be 2**h, h>=1")
    v = (s+1)*(s*s+1)
    a = (1+isqrt(1+8*v))//2
    while comb(a, 2) < v:
        a += 1
    while a > 2 and comb(a-1, 2) >= v:
        a -= 1
    k = comb(a, 2)
    assert 0 <= k-v < a-1
    return {"s": s, "V": v, "a": a, "K": k, "m": k-v,
            "occupied_fraction": str(Fraction(v, k)), "strict_slack_bound": a-1}


def _legal_tuple(support, values):
    for ty in ("P", "L"):
        ix = [i for i, x in enumerate(support) if x[0] == ty]
        if len({values[i] for i in ix}) != len(ix):
            return False
    return True


def make_motif(support, slots, cost):
    """Exhaust only tiny locally type-injective cost tables; no large-h claim."""
    support = tuple(support)
    if not support or len(set(support)) != len(support) or type(slots) is not int or slots < 1:
        raise ValueError("unique support and physical alphabet required")
    if any(not isinstance(x, tuple) or len(x) != 2 or x[0] not in ("P", "L")
           or type(x[1]) is not int or x[1] < 0 for x in support):
        raise ValueError("invalid ORIGINAL typed factor")
    if slots**len(support) > 1_000_000:
        raise ValueError("local model exceeds exact tiny-table budget")
    out = {}
    for values in product(range(slots), repeat=len(support)):
        if _legal_tuple(support, values):
            v = Fraction(cost(values))
            if v < 0:
                raise ValueError("nonnegative motif costs required")
            out[values] = v
    if not out:
        raise ValueError("no legal local assignment")
    return (support, out)


def _validate(npoints, nlines, slots, motifs):
    if any(type(z) is not int or z < 0 for z in (npoints, nlines)) or (
            type(slots) is not int or slots < max(1, npoints, nlines)):
        raise ValueError("bad typed dimensions")
    for support, table in motifs:
        if not support or len(set(support)) != len(support):
            raise ValueError("duplicate or empty local support")
        for ty, ix in support:
            if ty not in ("P", "L") or type(ix) is not int or not 0 <= ix < (
                    npoints if ty == "P" else nlines):
                raise ValueError("unknown source factor")
        if slots**len(support) > 1_000_000:
            raise ValueError("exact tiny-table verification budget exceeded")
        expected = {t for t in product(range(slots), repeat=len(support))
                    if _legal_tuple(support, t)}
        if set(table) != expected:
            raise ValueError("missing or extra locally injective states")
        if any(Fraction(z) < 0 for z in table.values()):
            raise ValueError("negative local cost")


def min_cost_injection(matrix):
    """Exact rectangular Hungarian min-cost injection, signed rational entries."""
    matrix = tuple(tuple(Fraction(z) for z in row) for row in matrix)
    n = len(matrix)
    if not n:
        return Fraction(0), ()
    k = len(matrix[0])
    if k < n or any(len(row) != k for row in matrix):
        raise ValueError("need consistent rectangular K>=V matrix")
    u, v = [Fraction(0)]*(n+1), [Fraction(0)]*(k+1)
    p, way = [0]*(k+1), [0]*(k+1)
    for i in range(1, n+1):
        p[0] = i
        j0 = 0
        mins = [None]*(k+1)
        used = [False]*(k+1)
        while True:
            used[j0] = True
            i0 = p[j0]
            delta = j1 = None
            for j in range(1, k+1):
                if used[j]:
                    continue
                cur = matrix[i0-1][j-1]-u[i0]-v[j]
                if mins[j] is None or cur < mins[j]:
                    mins[j], way[j] = cur, j0
                if delta is None or mins[j] < delta:
                    delta, j1 = mins[j], j
            if j1 is None:
                raise AssertionError("failed min-cost injection")
            for j in range(k+1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                elif mins[j] is not None:
                    mins[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break
    a = [None]*n
    for j in range(1, k+1):
        if p[j]:
            a[p[j]-1] = j-1
    if any(x is None for x in a) or len(set(a)) != n:
        raise AssertionError("invalid matching")
    return sum((matrix[i][j] for i, j in enumerate(a)), Fraction(0)), tuple(a)


def dual_bound(npoints, nlines, slots, motifs, potentials=None):
    """For all global typed injections: sum_Q c_Q >= sum_Q alpha_Q+A_P+A_L.

    alpha_Q=min_t (c_Q(t)-sum_{v in T_Q}u[Q,v,t_v]).
    A_T=min over global injective assignments of summed one-factor prices.
    Only small locally COMPLETE test tables are computed here; the identity
    itself applies for every original W(3,2**h) and the genuine GF5 predicate.
    """
    motifs = tuple(motifs)
    _validate(npoints, nlines, slots, motifs)
    potentials = dict(potentials or {})
    sums = {(ty, i, e): Fraction(0)
            for ty, n in (("P", npoints), ("L", nlines))
            for i in range(n) for e in range(slots)}
    for (q, factor, e), value in potentials.items():
        if type(q) is not int or not 0 <= q < len(motifs) or factor not in motifs[q][0] or (
                type(e) is not int or not 0 <= e < slots):
            raise ValueError("price outside ORIGINAL motif support")
        sums[(*factor, e)] += Fraction(value)
    alpha, local = [], []
    for q, (support, table) in enumerate(motifs):
        alpha.append(min(value-sum((Fraction(potentials.get((q, factor, vals[j]), 0))
                                   for j, factor in enumerate(support)), Fraction(0))
                         for vals, value in table.items()))
        local.append(min(table.values()))
    lp, left = min_cost_injection([[sums[("P", i, e)] for e in range(slots)]
                                   for i in range(npoints)])
    lr, right = min_cost_injection([[sums[("L", i, e)] for e in range(slots)]
                                    for i in range(nlines)])
    return {"dual_lower": sum(alpha, Fraction(0))+lp+lr,
            "point_assignment_cost": lp, "line_assignment_cost": lr,
            "local_offsets": tuple(alpha), "independent_local_minima": tuple(local),
            "point_matching": left, "line_matching": right}


def exact_tiny_optimum(npoints, nlines, slots, motifs, *, state_budget=100000):
    """Independent enumeration: both types injective within type ONLY."""
    motifs = tuple(motifs)
    _validate(npoints, nlines, slots, motifs)
    states = (factorial(slots)//factorial(slots-npoints)) * (
        factorial(slots)//factorial(slots-nlines))
    if states > state_budget:
        raise ValueError("large model not exhaustively checked")
    optimum = witness = None
    for left in permutations(range(slots), npoints):
        for right in permutations(range(slots), nlines):
            labels = {("P", i): e for i, e in enumerate(left)}
            labels.update({("L", i): e for i, e in enumerate(right)})
            v = sum((table[tuple(labels[x] for x in support)]
                     for support, table in motifs), Fraction(0))
            if optimum is None or v < optimum:
                optimum, witness = v, (left, right)
    return {"global_minimum": optimum, "witness": witness,
            "globally_injective_states": states}


def finite_toy_report():
    occupancy = tuple(make_motif((("P", i),), 2, lambda t: int(t[0] == 0))
                      for i in range(2))
    cp = {(q, ("P", q), e): int(e == 0) for q in range(2) for e in range(2)}
    cb = dual_bound(2, 0, 2, occupancy, cp)
    co = exact_tiny_optimum(2, 0, 2, occupancy)
    shared = (make_motif((("P", 0),), 2, lambda t: int(t[0] == 0)),
              make_motif((("P", 0),), 2, lambda t: int(t[0] == 1)))
    sp = {(q, ("P", 0), e): int(e == q) for q in range(2) for e in range(2)}
    sb = dual_bound(1, 0, 2, shared, sp)
    so = exact_tiny_optimum(1, 0, 2, shared)
    triangle = tuple(make_motif((("P", i), ("P", j)), 3,
                      lambda t: int(t[1] != (t[0]+1) % 3))
                     for i, j in ((0, 1), (1, 2), (0, 2)))
    tb = dual_bound(3, 0, 3, triangle)
    to = exact_tiny_optimum(3, 0, 3, triangle)
    # Proof of sup_all_unary_prices dual<=0: each edge's three zero-cost
    # successor states have uniform singleton marginals, equal to those
    # of a uniform mixture over all six true injective global permutations.
    # Compare local expected minorants and expected global price assignment.
    for support, table in triangle:
        zero = [t for t, c in table.items() if c == 0]
        assert len(zero) == 3
        assert all(sorted(t[j] for t in zero) == [0, 1, 2] for j in range(2))
    assert cb["dual_lower"] == co["global_minimum"] == 1
    assert sb["dual_lower"] == so["global_minimum"] == 1
    assert tb["dual_lower"] == 0 < to["global_minimum"] == 1
    return {"physical_capacity_sharp": {"local_min_sum": 0, "dual": 1, "true_min": 1},
            "shared_factor_coherence_sharp": {"local_min_sum": 0, "dual": 1, "true_min": 1},
            "unary_global_dual_no_go": {"all_unary_potentials_upper_bound": 0,
                "dual": 0, "true_min": 1,
                "witness": "3 same-type factors, 3 slots, cyclic successor constraints"},
            "universal_W3s_GF5_bound_proved": False,
            "Branch_A": "OPEN", "Branch_B": "OPEN"}


def true_w32_occupancy_falsifier():
    """Actual accepted ORIGINAL W32 seven-class oracle, NOT a toy model."""
    from hyp105_issue230_projection import fixture
    from hyp105_g5e2b3e1b0_seven_signature import seven_census
    a, b = fixture(1, "S68"), fixture(1, "S72")
    for ty in ("left_labels", "right_labels"):
        assert len(set(map(tuple, a[ty]))) == len(set(map(tuple, b[ty]))) == 15
        assert set(map(tuple, a[ty])) == set(map(tuple, b[ty]))
    ca = seven_census(a, independent_checks=False)
    cb = seven_census(b, independent_checks=False)
    assert (ca["S_seven"], cb["S_seven"]) == (68, 72)
    assert (ca["GF5_seven_lower_numerator"], cb["GF5_seven_lower_numerator"]) == (
        3112510, 3283610)
    return {"same_original_W32_geometry": True,
            "same_left_and_right_occupied_K6_edges": True,
            "S68": ca["S_seven"], "S72": cb["S_seven"],
            "GF5_S68_numerator": ca["GF5_seven_lower_numerator"],
            "GF5_S72_numerator": cb["GF5_seven_lower_numerator"],
            "image_occupancy_alone_determines_seven_S": False}


def report(include_w32=False):
    result = {"slice": "HYP105-ISSUE230-D6-AA4-E-UNARY-ASSIGNMENT-DUAL",
              "classification": "ALL-H CONDITIONAL WEAK DUAL + FINITE EXACT NO-GO",
              "all_h_typed_source_injection": True,
              "all_h_physical_slack_m_less_than_a_minus_one": True,
              "capacity": [alphabet_capacity(2**h) for h in range(1, 7)],
              "tiny_falsifiers": finite_toy_report(),
              "root_A_or_B_solved": False, "independent_math_review": "OPEN"}
    if include_w32:
        result["original_W32"] = true_w32_occupancy_falsifier()
    return result


if __name__ == "__main__":
    import argparse
    import json
    parser = argparse.ArgumentParser()
    parser.add_argument("--w32", action="store_true")
    args = parser.parse_args()
    print(json.dumps(report(args.w32), default=str, indent=2, sort_keys=True))
