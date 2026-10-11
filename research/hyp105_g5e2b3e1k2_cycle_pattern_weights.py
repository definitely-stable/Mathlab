"""HYP-105 B3.2-E1-K2: GF5 weights of ALL Kikuchi cycle patterns, Theorem K'.

All-h finite classification (the support pattern of a Kikuchi cycle does not
depend on s):

* K4. Six columns read along a six-cycle of the Kikuchi graph have a support
  pattern fixed by two cyclic closed-walk patterns (x and y). There are 41
  such walk patterns, 879 pattern pairs with six distinct columns, and 50
  degenerate pairs that use both diagonals of one column. Every one of the
  879 has full 51-palette alternating 3v3 GF5 weight >= 5643, with equality
  exactly for proper cycles (accepted D6). One six-column set carries at most
  4 Kikuchi six-cycles.
* K5. All 9 Kikuchi four-cycle patterns have 2v2 weight >= 531 (equality:
  accepted Q4); at most 2 four-cycles per four-column set.
* D2. sum_e C(c4(e),2) = #(six-cycle, antipodal chord) + book + degenerate.

Theorem K' (all s=2^h, all legal f,g):
  51^6 R3 >= (5643/4) * [ (L(P3) - Theta)/12 - C6_rep ],
and 51^4 R2 >= (531/2) * C4(Kikuchi). R3 here is the full 51-palette 3v3 risk
summed over ALL original six-incidence sets, not only the seven families S.
Still conditional on controlling Theta: no Branch A/B decision, no ASET exponent.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
import json

from hyp105_g5e2b3b1b_five_six_flows import exact_dual_GF5_six_flow
from hyp105_g5e2b3e1k1_kikuchi_c6 import (
    codegree_profile, cs_floor, gq_pair_model, kikuchi_graph, path3_profile,
)

ALTERNATING_SIX = (1, -1, 1, -1, 1, -1)
ALTERNATING_FOUR = (1, -1, 1, -1)
PALETTE = tuple(t for t in product(range(1, 5), repeat=4) if sum(t) % 5 == 4)


def cyclic_walk_patterns(length):
    """Closed walks of given length up to relabelling (cyclic neighbours differ)."""
    if type(length) is not int or length < 3:
        raise ValueError("cycle length >= 3 required")
    out = []

    def grow(seq, top):
        if len(seq) == length:
            if seq[-1] != seq[0]:
                out.append(tuple(seq))
            return
        for c in range(top + 2):
            if c != seq[-1]:
                grow(seq + [c], max(top, c))

    grow([0], 0)
    return tuple(out)


def pattern_columns(xs, ys):
    n = len(xs)
    return tuple((tuple(sorted((xs[i], xs[(i + 1) % n]))),
                  tuple(sorted((ys[i], ys[(i + 1) % n])))) for i in range(n))


def column_supports(columns, shift=100):
    return [tuple(sorted(left + tuple(shift + y for y in right)))
            for left, right in columns]


def cycles_on_columns(columns):
    """Kikuchi cycles that use every given column exactly once (as edge sets)."""
    adjacency = defaultdict(list)
    for k, (left, right) in enumerate(columns):
        for u, v in (((left[0], right[0]), (left[1], right[1])),
                     ((left[0], right[1]), (left[1], right[0]))):
            adjacency[u].append((v, k))
            adjacency[v].append((u, k))
    n = len(columns)
    found = set()
    for start in list(adjacency):
        def walk(path, used):
            last = path[-1]
            if len(path) == n:
                for w, k in adjacency[last]:
                    if w == start and k not in used:
                        found.add(frozenset(frozenset(e) for e in
                                            zip(path, path[1:] + [start])))
                return
            for w, k in adjacency[last]:
                if w not in path and k not in used:
                    walk(path + [w], used | {k})
        walk([start], frozenset())
    return len(found)


def classify_six_cycle_patterns():
    patterns = cyclic_walk_patterns(6)
    minimum = {}
    weights = {}
    degenerate = 0
    max_multiplicity = 0
    for xs in patterns:
        for ys in patterns:
            if len({(xs[i], ys[i]) for i in range(6)}) < 6:
                continue  # not a cycle of a simple graph
            columns = pattern_columns(xs, ys)
            if len(set(columns)) < 6:
                degenerate += 1
                continue
            w = exact_dual_GF5_six_flow(column_supports(columns), ALTERNATING_SIX)
            weights[(xs, ys)] = w
            key = (len(set(xs)), len(set(ys)))
            minimum[key] = min(minimum.get(key, w), w)
            max_multiplicity = max(max_multiplicity, cycles_on_columns(columns))
    return {
        "walk_patterns": len(patterns),
        "distinct_column_patterns": len(weights),
        "degenerate_repeated_column_patterns": degenerate,
        "min_weight_by_coordinate_counts": {f"{k[0]}x{k[1]}": v
                                             for k, v in sorted(minimum.items())},
        "global_min_weight": min(weights.values()),
        "min_attained_only_by_proper": all(
            w > 5643 for (xs, ys), w in weights.items()
            if (len(set(xs)), len(set(ys))) != (6, 6)),
        "max_cycles_per_six_column_set": max_multiplicity,
        "weights": weights,
    }


def two_v_two_weight(supports, signs=ALTERNATING_FOUR):
    """Exact 51-palette count with signed sum zero, meet in the middle."""
    coords = sorted({c for col in supports for c in col})
    index = {c: i for i, c in enumerate(coords)}

    def vectors(i):
        out = Counter()
        for t in PALETTE:
            v = [0] * len(coords)
            for c, w in zip(supports[i], t):
                v[index[c]] = (signs[i] * w) % 5
            out[tuple(v)] += 1
        return out

    left = Counter()
    for a, na in vectors(0).items():
        for b, nb in vectors(1).items():
            left[tuple((p + q) % 5 for p, q in zip(a, b))] += na * nb
    total = 0
    v2, v3 = vectors(2), vectors(3)
    for a, na in v2.items():
        for b, nb in v3.items():
            total += na * nb * left[tuple((-(p + q)) % 5 for p, q in zip(a, b))]
    return total


def classify_four_cycle_patterns():
    patterns = cyclic_walk_patterns(4)
    weights = {}
    max_multiplicity = 0
    for xs in patterns:
        for ys in patterns:
            if len({(xs[i], ys[i]) for i in range(4)}) < 4:
                continue
            columns = pattern_columns(xs, ys)
            if len(set(columns)) < 4:
                raise AssertionError("a Kikuchi four-cycle cannot repeat a column")
            weights[(xs, ys)] = two_v_two_weight(column_supports(columns))
            max_multiplicity = max(max_multiplicity, cycles_on_columns(columns))
    return {
        "walk_patterns": len(patterns),
        "cycle_patterns": len(weights),
        "global_min_weight": min(weights.values()),
        "proper_weight": weights[((0, 1, 2, 3), (0, 1, 2, 3))],
        "max_cycles_per_four_column_set": max_multiplicity,
        "weights": weights,
    }


def four_cycles(neighbors):
    found = set()
    for u in range(len(neighbors)):
        for b, d in combinations(sorted(neighbors[u]), 2):
            for v in neighbors[b] & neighbors[d]:
                if v != u:
                    found.add(frozenset((frozenset((u, b)), frozenset((b, v)),
                                         frozenset((v, d)), frozenset((d, u)))))
    return found


def edge_pair_identity(neighbors):
    """D2: pairs of four-cycles through an edge, split by intersection type."""
    by_edge = defaultdict(list)
    for q in four_cycles(neighbors):
        for e in q:
            by_edge[e].append(q)
    total = only_edge = book = other = 0
    for e, qs in by_edge.items():
        for q1, q2 in combinations(qs, 2):
            total += 1
            v1 = set().union(*q1)
            v2 = set().union(*q2)
            if v1 & v2 == set(e):
                only_edge += 1
            elif len(q1 & q2) == 2 and len(v1 & v2) == 3:
                book += 1
            else:
                other += 1
    chorded = 0
    for start in range(len(neighbors)):
        def walk(path):
            nonlocal chorded
            last = path[-1]
            if len(path) == 6:
                if start in neighbors[last] and path[1] < last:
                    chorded += sum(path[i + 3] in neighbors[path[i]] for i in range(3))
                return
            for w in neighbors[last]:
                if w > start and w not in path:
                    walk(path + (w,))
        walk((start,))
    if only_edge != chorded:
        raise AssertionError("D2: edge-only C4 pairs must equal chorded six-cycles")
    return {"sum_edge_C4_pairs": total, "edge_only_pairs": only_edge,
            "chorded_six_cycles": chorded, "book_pairs": book,
            "degenerate_pairs": other}


def kikuchi_r3_witness(model, max_cycles=200000):
    """Distinct six-incidence sets from Kikuchi cycles and their R3 weights."""
    a = model["a"]
    g = kikuchi_graph(model)
    left, right = model["left_labels"], model["right_labels"]
    column = {}
    for k, (p, l) in enumerate(model["incidences"]):
        x, x2 = left[p]
        y, y2 = right[l]
        column[frozenset((x * a + y, x2 * a + y2))] = k
        column[frozenset((x * a + y2, x2 * a + y))] = k

    def support(k):
        p, l = model["incidences"][k]
        return tuple(sorted(left[p] + tuple(a + y for y in right[l])))

    sets = Counter()
    weight = {}
    repeated = cycles = 0
    for start in range(a * a):
        def walk(path):
            nonlocal repeated, cycles
            last = path[-1]
            if len(path) == 6:
                if start in g[last] and path[1] < last:
                    cycles += 1
                    if cycles > max_cycles:
                        raise RuntimeError("cycle budget exceeded (fail closed)")
                    cols = [column[frozenset((path[i], path[(i + 1) % 6]))]
                            for i in range(6)]
                    if len(set(cols)) < 6:
                        repeated += 1
                        return
                    key = frozenset(cols)
                    sets[key] += 1
                    w = exact_dual_GF5_six_flow([support(k) for k in cols],
                                                ALTERNATING_SIX, dimension=2 * a)
                    if w < 5643:
                        raise AssertionError("K4 weight floor violated")
                    weight[key] = max(weight.get(key, 0), w)
                return
            for w in g[last]:
                if w > start and w not in path:
                    walk(path + (w,))
        walk((start,))
    if max(sets.values(), default=0) > 4:
        raise AssertionError("K4 multiplicity bound violated")
    paths = path3_profile(g)
    theta = codegree_profile(g)["Theta"]
    bound = Fraction(5643, 4) * ((cs_floor(paths["P3"], a) - theta) / 12 - repeated)
    numerator = sum(weight.values())
    if numerator < bound:
        raise AssertionError("Theorem K' violated")
    return {"s": model["s"], "scheme": model["scheme"], "C6": cycles,
            "C6_repeated_column": repeated, "distinct_six_sets": len(sets),
            "max_cycles_per_set": max(sets.values(), default=0),
            "R3_kikuchi_numerator_lower": numerator,
            "theorem_K_prime_bound": str(bound)}


def report():
    six = classify_six_cycle_patterns()
    four = classify_four_cycle_patterns()
    for d in (six, four):
        d.pop("weights")
    witnesses = [kikuchi_r3_witness(gq_pair_model(1, s)) for s in ("lex", "reverse-line")]
    d2 = [edge_pair_identity(kikuchi_graph(gq_pair_model(1, "lex")))]
    return {"slice": "HYP-105-B3.2-E1-K2", "six_cycle_patterns": six,
            "four_cycle_patterns": four, "w32_theorem_K_prime": witnesses,
            "w32_D2_identity": d2, "theta_control_proved": False,
            "branch_A_or_B_decided": False, "full_R3_or_ASET_exponent": False}


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True, default=str))
