"""Issue230: exact finite falsifiers and all-h restricted source theorems.

No universal S=Omega(s^6), infinite counterfamily, full GF5 risk upper,
or ASET exponent is asserted. Finite geometry execution is capped at V<=600.
The analytic proof, including the sharp Delta^2 source exponent, is in docs.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import ceil, comb, isqrt, prod
import json

from hyp105_b1_symplectic import symplectic_gq
from hyp105_g5e2b3e1b1a_one_sided import (
    left_six_mass, uniform_right_completion_BA,
)

HALF_RANDOM_CONSTANT = 140*Fraction(6, 7)**12*Fraction(5, 7)*Fraction(67, 81)
CYCLE_ORDERS = ((0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3))
F0 = (13, 4, 2, 14, 0, 11, 1, 7, 10, 6, 9, 5, 12, 3, 8)
G68 = (12, 9, 11, 4, 1, 6, 0, 13, 5, 14, 3, 7, 2, 10, 8)
G72 = (12, 9, 11, 2, 8, 6, 0, 13, 5, 14, 3, 7, 4, 10, 1)


def parameters(s):
    if isinstance(s, bool) or not isinstance(s, int) or s < 2 or s & (s-1):
        raise ValueError("s=2^h, h>=1 required")
    v = (s+1)*(s*s+1)
    a = (1+isqrt(1+8*v))//2
    if comb(a, 2) < v:
        a += 1
    return {"s": s, "V": v, "Delta": s+1, "a": a, "K": comb(a, 2)}


def analytic_certificate(s):
    """Exact rational instances of proven bounds; no finite exponent fit."""
    p = parameters(s)
    probability = Fraction(70*comb(p["a"], 6), comb(p["K"], 6))
    eta = Fraction(15*(s+1), s*s+s+1)
    ratio_squared = max(Fraction(), 1/eta-1)*(1-probability)/probability
    mass = left_six_mass(s)
    h_lower = (mass["left_original_sixsets_lower"]["B"]
               *max(Fraction(), 1-Fraction(14, (s+1)**2)))
    coefficient = min((s+1)**4, 12*(s+1)**2, 6*comb(p["a"]-2, 4))
    return {
        **p, "rho": probability, "eta": eta,
        "cs_error_to_mean_squared_lower": ratio_squared,
        "expected_BA_lower": uniform_right_completion_BA(s)["expected_U_Bleft_Aright_lower"],
        "half_random_constant_for_s_at_least_8": HALF_RANDOM_CONSTANT,
        "source_weight_per_meeting_pair_cap": coefficient,
        "source_support_lower": ceil(h_lower/(15*coefficient)),
        "source_support_asymptotic": "(1/720+o(1))*s^13 uniformly in f",
        "universal_S_lower_proved": False,
    }


def _physical_edges(edges, a):
    try:
        values = tuple(tuple(e) for e in edges)
    except TypeError as exc:
        raise ValueError("physical pair sequence required") from exc
    if (len(set(values)) != len(values)
            or any(len(e) != 2 or any(isinstance(x, bool) or not isinstance(x, int) for x in e)
                   or not 0 <= e[0] < e[1] < a for e in values)):
        raise ValueError("distinct canonical unordered physical pairs required")
    return frozenset(values)


def _adjacency(edges):
    out = {}
    for u, v in edges:
        out.setdefault(u, set()).add(v)
        out.setdefault(v, set()).add(u)
    return out


def _two_paths(first, second):
    out = Counter()
    for x, ys in first.items():
        for y in ys:
            for z in second.get(y, ()):
                out[x, z] += 1
    return out


def colored_c4(colors, a):
    """Exact four-distinct-vertex trace, summed over three color orders.

Full traces contain opposite-vertex collisions. Inclusion-exclusion
removes both collisions and restores the all-four-color common edge.
An original colored square is counted once, without an orientation factor.
"""
    if isinstance(a, bool) or not isinstance(a, int) or a < 2:
        raise ValueError("physical alphabet a>=2 required")
    if len(colors) != 4:
        raise ValueError("four named edge-color lists required")
    palettes = tuple(_physical_edges(c, a) for c in colors)
    graphs = tuple(_adjacency(c) for c in palettes)
    overlap = {}
    for i, j in combinations(range(4), 2):
        overlap[i, j] = Counter(x for edge in palettes[i]&palettes[j] for x in edge)
    def degrees(i, j):
        return overlap[tuple(sorted((i, j)))]
    def dot(x, y):
        return sum(n*y.get(v, 0) for v, n in x.items())
    common = 2*len(set.intersection(*(set(c) for c in palettes)))
    walks, simple = [], []
    for i, j, k, l in CYCLE_ORDERS:
        first = _two_paths(graphs[i], graphs[j])
        second = _two_paths(graphs[k], graphs[l])
        trace = sum(n*second.get((z, x), 0) for (x, z), n in first.items())
        count = trace-dot(degrees(i, j), degrees(k, l))-dot(degrees(j, k), degrees(l, i))+common
        if not 0 <= count <= trace or trace**2 > 16*prod(map(len, palettes)):
            raise AssertionError("distinct trace or Frobenius bound failed")
        walks.append(trace)
        simple.append(count)
    return {"simple": sum(simple), "simple_by_order": tuple(simple),
            "walks_by_order": tuple(walks)}


class QuarticSource:
    """Finite true-GQ source tensor; validation checks the GQ projection axiom."""
    def __init__(self, model):
        p = parameters(model["s"])
        self.s, self.a, self.delta, self.v = p["s"], p["a"], p["Delta"], p["V"]
        if self.v > 600:
            raise ValueError("finite geometry oracle capped at V<=600")
        if model["a"] != self.a:
            raise ValueError("minimal physical alphabet required")
        self.labels = tuple(tuple(x) for x in model["left_labels"])
        _physical_edges(self.labels, self.a)
        if len(self.labels) != self.v:
            raise ValueError("complete original point map required")
        edges = tuple(tuple(x) for x in model["incidences"])
        if (len(edges) != self.v*self.delta or len(set(edges)) != len(edges)
                or any(len(e) != 2 or any(isinstance(x, bool) or not isinstance(x, int)
                                        or not 0 <= x < self.v for x in e) for e in edges)):
            raise ValueError("distinct complete original incidences required")
        lines, point_lines = [set() for _ in range(self.v)], [set() for _ in range(self.v)]
        for q, l in edges:
            lines[l].add(q)
            point_lines[q].add(l)
        if any(len(x) != self.delta for x in lines+point_lines):
            raise ValueError("GQ degree metadata invalid")
        self.lines = tuple(tuple(sorted(x)) for x in lines)
        self.meeting = {}
        for q, neighbors in enumerate(point_lines):
            for pair in combinations(sorted(neighbors), 2):
                if pair in self.meeting:
                    raise ValueError("two original lines share two original points")
                self.meeting[pair] = q
        for q, neighbors in enumerate(point_lines):
            collinear = set().union(*(lines[l] for l in neighbors))-{q}
            for l, points in enumerate(lines):
                if l not in neighbors and len(points&collinear) != 1:
                    raise ValueError("original GQ projection axiom violated")
        self.line_labels = tuple(tuple(self.labels[q] for q in points) for points in self.lines)

    def _sixset(self, R):
        values = tuple(R)
        if (len(values) != 6 or len(set(values)) != 6
                or any(isinstance(x, bool) or not isinstance(x, int) or not 0 <= x < self.v for x in values)):
            raise ValueError("six distinct original line IDs required")
        return tuple(sorted(values))

    def anchors(self, R):
        values = self._sixset(R)
        for pair in combinations(values, 2):
            if pair in self.meeting:
                yield self.meeting[pair], tuple(x for x in values if x not in pair)

    def meeting_count(self, R):
        return sum(pair in self.meeting for pair in combinations(self._sixset(R), 2))

    def weight(self, R):
        count = 0
        for q, rest in self.anchors(R):
            blocked = set(self.labels[q])
            colors = tuple(tuple(e for e in self.line_labels[l] if not blocked&set(e)) for l in rest)
            count += colored_c4(colors, self.a)["simple"]
        if count > self.cap(R):
            raise AssertionError("all-h source cap falsified")
        return count

    def cap(self, R):
        c = min(self.delta**4, 12*self.delta**2, 6*comb(self.a-2, 4))
        return c*self.meeting_count(R)

    def ledger(self, *, max_sets=5005):
        if comb(self.v, 6) > max_sets:
            raise ValueError("complete original sixset ledger exceeds explicit budget")
        out = Counter()
        for R in combinations(range(self.v), 6):
            count = self.weight(R)
            if count:
                out[frozenset(R)] = count
        return out


def _model(s, points, lines, incidences, labels, right):
    a = parameters(s)["a"]
    return {"s": s, "a": a, "m": 2*a, "v": len(points), "N": len(incidences),
            "points": points, "lines": lines, "incidences": incidences,
            "left_labels": tuple(labels), "right_labels": tuple(right),
            "supports": tuple(tuple(sorted(labels[p]+tuple(a+x for x in right[l])))
                              for p, l in incidences)}


@lru_cache(maxsize=3)
def _geometry(power):
    return symplectic_gq(power)


def frozen_model(scheme):
    _, points, lines, incidences = _geometry(1)
    palette = tuple(combinations(range(6), 2))
    if scheme == "lex":
        f = g = tuple(range(15))
    elif scheme == "reverse":
        f, g = tuple(range(15)), tuple(reversed(range(15)))
    elif scheme in ("S68", "S72"):
        f, g = F0, G68 if scheme == "S68" else G72
    else:
        raise ValueError("unknown frozen source witness")
    return _model(2, points, lines, incidences,
                  tuple(palette[i] for i in f), tuple(palette[i] for i in g))


def finite_certificate(scheme):
    """Same-map accepted seven GF5 floor, Q4, and true dual source masses."""
    from hyp105_g5e2b3e1b0_seven_signature import seven_census, R3_CERTIFIED_FLOORS
    from hyp105_g5e2b3e1c0_weighted_overlap import source_weighted_BA_hypergraph
    model = frozen_model(scheme)
    source = source_weighted_BA_hypergraph(model)
    dual = dict(model, left_labels=model["right_labels"], right_labels=model["left_labels"],
                incidences=tuple((l, p) for p, l in model["incidences"]))
    dual_source = source_weighted_BA_hypergraph(dual)
    census = seven_census(model)
    counts = census["seven_class_motif_counts"]
    vector = tuple(counts[k] for k in R3_CERTIFIED_FLOORS)
    mean = Fraction(2*sum(source.values()), 143)
    return {"scheme": scheme, "seven_vector": vector, "S": sum(vector),
            "source_mass": sum(source.values()), "dual_source_mass": sum(dual_source.values()),
            "mu_f": mean, "P2_margin": vector[1]+vector[2]-mean,
            "P7_margin": sum(vector)-mean, "Q4": census["Q4"],
            "Q7_GF5_floor_numerator": census["GF5_seven_lower_numerator"],
            "GF5_denominator": 51**6, "counterexample_B": False}


def pencil_fixture(power, mode):
    """Actual global W34/W38 f proving sharp source exponent or local zero."""
    if power not in (2, 3) or mode not in ("sharp", "zero"):
        raise ValueError("finite true geometry fixtures: powers 2/3, sharp/zero")
    field, points, lines, incidences = _geometry(power)
    p = parameters(field.q)
    point_lines = [tuple(l for l, line in enumerate(lines) if q in line) for q in range(p["V"])]
    anchor = point_lines[0][:2]
    selected = list(anchor)
    line_sets = tuple(set(x) for x in lines)
    for l in range(p["V"]):
        if all(not line_sets[l]&line_sets[j] for j in selected):
            selected.append(l)
            if len(selected) == 6:
                break
    if len(selected) != 6:
        raise AssertionError("six-line skew fixture missing")
    d, a = p["Delta"], p["a"]
    if mode == "sharp":
        colors = (tuple((0, 2+i) for i in range(d)),
                  tuple((1, 2+i) for i in range(d)),
                  tuple((1, 2+d+i) for i in range(d)),
                  tuple((0, 2+d+i) for i in range(d)))
        edge = (2*d+2, 2*d+3)
    else:
        edge = (0, 1)
        available = tuple(e for e in combinations(range(a), 2) if e != edge and set(e)&set(edge))
        if len(available) < 4*d:
            raise AssertionError("zero fixture pair capacity")
        colors = tuple(available[i*d:(i+1)*d] for i in range(4))
    labels = [None]*p["V"]
    labels[0] = edge
    for l, color in zip(selected[2:], colors):
        for q, pair in zip(lines[l], color):
            if labels[q] is not None:
                raise AssertionError("original point sets must be disjoint")
            labels[q] = pair
    palette = tuple(combinations(range(a), 2))
    used = {x for x in labels if x is not None}
    remaining = iter(e for e in palette if e not in used)
    for q in range(p["V"]):
        if labels[q] is None:
            labels[q] = next(remaining)
    return _model(field.q, points, lines, incidences, labels, palette[:p["V"]]), tuple(sorted(selected))


def report():
    fixtures = []
    for power in (2, 3):
        for mode in ("sharp", "zero"):
            model, R = pencil_fixture(power, mode)
            source = QuarticSource(model)
            fixtures.append({"s": model["s"], "mode": mode, "R": R,
                             "meeting_pairs": source.meeting_count(R), "weight": source.weight(R)})
    return {"status": "RESTRICTED_THEOREM_C", "root": "OPEN_WITH_FORMAL_BLOCKER",
            "finite": [finite_certificate(x) for x in ("lex", "reverse", "S72", "S68")],
            "quartic_fixtures": fixtures,
            "analytic": [analytic_certificate(s) for s in (8, 16, 32, 64, 128)],
            "PROVED_A": False, "COUNTEREXAMPLE_B": False, "new_ASET_exponent": False}


if __name__ == "__main__":
    print(json.dumps(report(), default=str, indent=2, sort_keys=True))
