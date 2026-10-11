"""HYP-105 E1-K3-C: exact C4-pair book decomposition and Kikuchi lift.

All-graph statements are finite identities. GQ coordinate-alignment caps
are all-h necessary conditions for valid global physical pair injections.
Neither result proves an Omega(s^6) seven-motif floor or an all-h
control of mixed-coordinate codegree/book mass.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb
import json

from hyp105_g5e2b3e1k1_kikuchi_c6 import (
    gq_pair_model, kikuchi_graph, six_cycle_census,
)
from hyp105_g5e2b3e1k2_cycle_pattern_weights import four_cycles


def _comb3(value):
    return comb(value, 3) if value >= 3 else 0


def _column_index(model):
    """Independent inverse physical labels: Kikuchi graph edge -> original incidence."""
    if model is None:
        return None
    a = model["a"]
    point = {tuple(e): i for i, e in enumerate(model["left_labels"])}
    line = {tuple(e): j for j, e in enumerate(model["right_labels"])}
    inc = set(model["incidences"])
    if len(point) != len(model["left_labels"]) or len(line) != len(model["right_labels"]):
        raise ValueError("physical labels must be injective")
    def find(e):
        u, v = tuple(e)
        x, y = divmod(u, a)
        z, t = divmod(v, a)
        if x == z or y == t:
            raise AssertionError("Kikuchi edge must change both coordinates")
        p = point.get(tuple(sorted((x, z))))
        l = line.get(tuple(sorted((y, t))))
        if p is None or l is None or (p, l) not in inc:
            raise AssertionError("Kikuchi edge is not an original incidence")
        return (p, l)
    return find


def triangle_and_k4_counts(neighbors):
    """Independent clique counts via common neighborhoods, no C4 enumeration."""
    n = len(neighbors)
    triangles = sum(len(neighbors[u] & neighbors[v])
                    for u in range(n) for v in neighbors[u] if u < v)
    if triangles % 3:
        raise AssertionError("triangle multiplicity must be three")
    six_k4 = 0
    for u in range(n):
        for v in neighbors[u]:
            if u >= v:
                continue
            common = sorted(neighbors[u] & neighbors[v])
            for w, z in combinations(common, 2):
                if z in neighbors[w]:
                    six_k4 += 1
    if six_k4 % 6:
        raise AssertionError("K4 edge multiplicity must be six")
    return triangles // 3, six_k4 // 6


def book_moments(neighbors, a=None):
    """Book moment B = 3*sum_{u<v} binom(|N(u) intersect N(v)|,3).

    The two diagonal endpoints of two C4s sharing a 2-edge path are
    uniquely determined. Choosing an unordered triple of their common
    neighbors gives exactly THREE unordered pairs of C4s sharing
    exactly that 2-edge path.

    Optionally split pairs of Kikuchi vertices by physical coordinate
    relation; when a is provided len(neighbors) must equal a*a.
    """
    n = len(neighbors)
    if a is not None and (type(a) is not int or a < 2 or n != a * a):
        raise ValueError("Kikuchi coordinate shape must be a^2")
    bins = Counter()
    max_aligned = 0
    max_mixed = 0
    for u in range(n):
        for v in range(u + 1, n):
            c = len(neighbors[u] & neighbors[v])
            group = "unclassified"
            if a is not None:
                x, y = divmod(u, a)
                xx, yy = divmod(v, a)
                group = ("same-x" if x == xx else
                         "same-y" if y == yy else "mixed")
                if group == "mixed":
                    max_mixed = max(max_mixed, c)
                else:
                    max_aligned = max(max_aligned, c)
                    if c > a - 2:
                        raise AssertionError("GQ-aligned codegree cap a-2 violated")
            bins[(group, "pairs")] += 1
            bins[(group, "c4_diagonal_mass")] += comb(c, 2) if c >= 2 else 0
            bins[(group, "triples")] += _comb3(c)
    total = sum(v for (group, metric), v in bins.items() if metric == "triples")
    return {
        "book_pairs_formula": 3 * total,
        "codegree_cubic_sum": total,
        "book_same_x": 3 * bins[("same-x", "triples")],
        "book_same_y": 3 * bins[("same-y", "triples")],
        "book_mixed": 3 * bins[("mixed", "triples")],
        "max_aligned_codegree": max_aligned,
        "max_mixed_codegree": max_mixed,
        "max_aligned_bound": a - 2 if a is not None else None,
    }


def classify_c4_pair_overlaps(neighbors, *, model=None, max_pair_incidents=300_000):
    """Independent C4-set overlap enumeration: H, B, T, K.

    Let A = sum_e binom(c4(e),2). For any simple graph,
      A = H + 2*B + T + 2*K,
      B = 3*sum_{u<v} binom(c(u,v),3),
      K = 3 * #K4.
    H counts C4 pairs sharing exactly one edge and precisely its two
    endpoints; each yields a SIX-cycle with that edge as an antipodal
    chord. Every C6 has at most three antipodal chords.

    For genuine Kikuchi graphs, proper H cycles are proper D6, and
    distinct-column H cycles contribute to full R3, subject to the
    accepted GF5 multiplicity weights from K2. Neither is an all-h
    positive lower bound without a new packing inequality.
    """
    if type(max_pair_incidents) is not int or max_pair_incidents < 0:
        raise ValueError("max_pair_incidents must be nonnegative")
    cyc = [frozenset(q) for q in four_cycles(neighbors)]
    rows = defaultdict(list)
    vertices = []
    for i, q in enumerate(cyc):
        vertices.append(frozenset().union(*q))
        if len(q) != 4 or len(vertices[-1]) != 4:
            raise AssertionError("four-cycle oracle malformed")
        for e in q:
            rows[e].append(i)
    incidences = sum(comb(len(items), 2) for items in rows.values())
    if incidences > max_pair_incidents:
        raise RuntimeError("C4 pair-incidence budget exceeded (fail closed)")
    pairs = set()
    for entries in rows.values():
        pairs.update(combinations(sorted(entries), 2))

    kinds = Counter()
    chorded = defaultdict(set)
    proper_chords = distinct_chords = 0
    get_column = _column_index(model)
    if model is not None and len(neighbors) != model["a"] ** 2:
        raise ValueError("GQ Kikuchi graph must have a^2 vertices")
    for i, j in pairs:
        a, b = cyc[i], cyc[j]
        shared_edges = len(a & b)
        shared_vertices = len(vertices[i] & vertices[j])
        key = (shared_edges, shared_vertices)
        kinds[key] += 1
        if key not in ((1, 2), (1, 3), (2, 3), (2, 4)):
            raise AssertionError("unclassified two-C4 intersection: %r" % (key,))
        if key == (1, 3):
            common_e = next(iter(a & b))
            x, y = tuple(common_e)
            z = next(iter((vertices[i] & vertices[j]) - set(common_e)))
            if z not in neighbors[x] or z not in neighbors[y]:
                raise AssertionError("one-edge three-vertex overlap must contain triangle")
        if key != (1, 2):
            continue
        cycle = a ^ b
        vset = frozenset().union(*cycle)
        if len(cycle) != 6 or len(vset) != 6:
            raise AssertionError("chorded symmetric difference must be C6")
        degree = Counter(v for e in cycle for v in e)
        if set(degree.values()) != {2}:
            raise AssertionError("chorded symmetric difference is not a C6")
        chord = next(iter(a & b))
        if chord & cycle:
            raise AssertionError("antipodal chord must not be a cycle edge")
        chorded[cycle].add(chord)
        if model is not None:
            physical_a = model["a"]
            proper = (len({w // physical_a for w in vset}) == 6 and
                      len({w % physical_a for w in vset}) == 6)
            cols = [get_column(e) for e in cycle]
            distinct = len(set(cols)) == 6
            proper_chords += int(proper)
            distinct_chords += int(distinct)
            if proper and not distinct:
                raise AssertionError("proper Kikuchi C6 cannot repeat original incidence")

    h = kinds[(1, 2)]
    b = kinds[(2, 3)]
    t = kinds[(1, 3)]
    k = kinds[(2, 4)]
    if sum(kinds.values()) != len(pairs):
        raise AssertionError("overlap pair sum mismatch")
    if any(len(cs) > 3 for cs in chorded.values()):
        raise AssertionError("at most three antipodal chords per six-cycle")
    if h != sum(map(len, chorded.values())):
        raise AssertionError("chorded witness representation not injective")
    edge_pair_a = incidences
    if edge_pair_a != h + 2 * b + t + 2 * k:
        raise AssertionError("edge-sharing C4 decomposition identity failed")
    moments = book_moments(neighbors, model["a"] if model is not None else None)
    triangles, k4 = triangle_and_k4_counts(neighbors)
    if b != moments["book_pairs_formula"]:
        raise AssertionError("independent cubic-codegree book identity failed")
    if k != 3 * k4:
        raise AssertionError("independent K4-clique identity failed")
    n_e = sum(map(len, neighbors)) // 2
    c4_count = len(cyc)
    jensen = Fraction(8 * c4_count * c4_count, n_e) - 2 * c4_count if n_e else Fraction(0)
    if Fraction(edge_pair_a) < jensen:
        raise AssertionError("Jensen C4 pair bound failed")
    result = {
        "C4": c4_count, "C3": triangles, "K4_cliques": k4,
        "E": n_e, "A_edge_pairs": edge_pair_a,
        "H_single_edge_only": h, "B_two_edge_path": b,
        "T_triangle_hook": t, "K_two_opposite_edges": k,
        "book_cubic_formula": moments["book_pairs_formula"],
        "K4_formula": 3 * k4,
        "exact_A_rhs": h + 6 * moments["codegree_cubic_sum"] + t + 6 * k4,
        "jensen_A_floor": str(jensen),
        "C6_from_chord_floor": (h + 2) // 3,
        "distinct_chorded_C6": len(chorded),
        "max_antipodal_chords": max(map(len, chorded.values()), default=0),
        **moments,
    }
    if model is not None:
        result["H_proper"] = proper_chords
        result["H_distinct_columns"] = distinct_chords
        result["D6_from_proper_chord_floor"] = (proper_chords + 2) // 3
        result["distinct_C6_from_chord_floor"] = (distinct_chords + 2) // 3
    return result


def report():
    out = {"slice": "HYP-105-B3.2-E1-K3-C",
           "all_h_seven_family_floor_proved": False,
           "uniform_mixed_book_bound_proved": False, "models": {}}
    for power, scheme, seed in ((1, "lex", None),
                                (1, "reverse-line", None),
                                (2, "random", 20261011)):
        model = gq_pair_model(power, scheme, seed)
        graph = kikuchi_graph(model)
        result = classify_c4_pair_overlaps(graph, model=model)
        cycle = six_cycle_census(graph, model["a"])
        if result["D6_from_proper_chord_floor"] > cycle["proper_D6"]:
            raise AssertionError("proper D6 chord floor fails")
        if result["C6_from_chord_floor"] > cycle["C6"]:
            raise AssertionError("full six-cycle chord floor fails")
        result["actual_C6"] = cycle["C6"]
        result["actual_proper_D6"] = cycle["proper_D6"]
        out["models"]["s%s-%s" % (model["s"], scheme)] = result
    return out


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True))
