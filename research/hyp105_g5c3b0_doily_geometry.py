"""HYP-105 G5-C3-B0: exact finite W(3,2) ovoid/spread duad-syntheme map.

Classical finite geometry, NOT an all-s generalized-quadrangle construction.
All 15 point and 15 line labels are reconstructed by independent maximum
coclique enumeration, then mapped bijectively to K6 coordinate pairs.
"""
from itertools import combinations
import argparse
import json

from hyp105_g5c3_label_search import (
    PAIRS, IDENTITY, bounded_descent, certified_result,
    fast_minimal_conflicts
)
from test_hyp105_g5b_graph_realization import (
    quadrangle_w32, symplectic_4
)


def adjacency_from_triples(triples, count=15):
    """Pairs sharing one line/one point in a 15_3 incidence geometry."""
    neighbours = [set() for _ in range(count)]
    for triple in triples:
        if len(triple) != 3 or len(set(triple)) != 3 or any(
                not isinstance(v, int) or not 0 <= v < count for v in triple):
            raise ValueError("invalid three-vertex incidence")
        for a, b in combinations(triple, 2):
            neighbours[a].add(b)
            neighbours[b].add(a)
    return tuple(frozenset(row) for row in neighbours)


def max_fives(adjacency):
    """Exhaustively, exactly list independent 5-sets (no adjacency)."""
    if len(adjacency) != 15 or any(len(row) != 6 for row in adjacency):
        raise ValueError("expected degree-six 15-vertex doily point/line graph")
    return tuple(c for c in combinations(range(15), 5)
                 if all(b not in adjacency[a] for a, b in combinations(c, 2)))


def recover_duads(adjacency):
    """Map 15 points to pairs of its six 5-cocliques.

    Each coclique is an ovoid for the point collinearity graph, or a
    spread for the dual line-intersection graph. Require an exact
    bijection to all 15 K6 pair labels; never infer it from a picture.
    """
    fives = max_fives(adjacency)
    if len(fives) != 6:
        raise AssertionError("not exactly six ovoids/spreads")
    pair_to_index = {p: i for i, p in enumerate(PAIRS)}
    memberships = tuple(tuple(k for k, family in enumerate(fives)
                              if node in family) for node in range(15))
    if any(len(x) != 2 for x in memberships):
        raise AssertionError("each graph vertex must lie in exactly two fives")
    if set(memberships) != set(PAIRS):
        raise AssertionError("six max-coclique membership pairs are not K6")
    if any(len(set(a) & set(b)) != 1 for a, b in combinations(fives, 2)):
        raise AssertionError("pairwise fives must intersect in one vertex")
    return tuple(pair_to_index[p] for p in memberships), fives


def doily_dual_recovery():
    """Recover point-duads and line-duads from W(3,2) symplectic incidence."""
    lines, edges = quadrangle_w32()
    point_triples = tuple(tuple(v - 1 for v in line) for line in lines)
    point_adj = adjacency_from_triples(point_triples)
    for u in range(15):
        for v in range(u + 1, 15):
            if ((v in point_adj[u]) != (symplectic_4(u + 1, v + 1) == 0)):
                raise AssertionError("point adjacency does not match symplectic form")

    # The dual line graph has an edge for each pair of lines through a point.
    line_incidence = tuple(tuple(i for i, line in enumerate(lines)
                                 if p in line) for p in range(1, 16))
    if any(len(x) != 3 for x in line_incidence):
        raise AssertionError("a point must lie on 3 lines")
    line_adj = adjacency_from_triples(line_incidence)

    point_labels, ovoids = recover_duads(point_adj)
    line_labels, spreads = recover_duads(line_adj)

    # Each isotropic line yields a complete matching of K6 from point-duads.
    all_synthemes = []
    for line in point_triples:
        pairs = tuple(PAIRS[point_labels[i]] for i in line)
        if sorted(coord for pair in pairs for coord in pair) != list(range(6)):
            raise AssertionError("a line is not a partition into three duads")
        all_synthemes.append(tuple(sorted(pairs)))
    if len(set(all_synthemes)) != 15:
        raise AssertionError("not all fifteen distinct synthemes")

    # Dual: lines through each point are a partition into 3 line-duads.
    for triple in line_incidence:
        pairs = tuple(PAIRS[line_labels[i]] for i in triple)
        if sorted(coord for pair in pairs for coord in pair) != list(range(6)):
            raise AssertionError("dual point line labels not a perfect matching")
    if len(set(edges)) != 45:
        raise AssertionError("must have 45 incidence edges")
    return {
        "point_labels": point_labels,
        "line_labels": line_labels,
        "ovoid_fives": ovoids,
        "spread_fives": spreads,
        "point_synthemes": tuple(all_synthemes),
        "point_triples": point_triples,
        "line_incidence": line_incidence,
        "point_adj": point_adj,
        "line_adj": line_adj,
    }


def enumerate_synthemes_directly():
    """Independent construction: all perfect matchings of K6, no GQ input."""
    matches = set()
    symbols = tuple(range(6))

    def rec(remaining, pairs):
        if not remaining:
            matches.add(tuple(sorted(pairs)))
            return
        a = remaining[0]
        for b in remaining[1:]:
            rec(tuple(x for x in remaining if x != a and x != b),
                pairs + ((a, b),))
    rec(symbols, ())
    return tuple(sorted(matches))


def full_duad_disjointness_parameter_gate(order):
    """Necessary invariants for a FULL K_a-duad disjointness representation.

    If all V points of GQ(s,s) are exactly all C(a,2) duads and point
    collinearity iff their duads are disjoint, require BOTH
      C(a,2) = (s+1)(s^2+1)
      C(a-2,2) = s(s+1).
    Subtracting gives 2*a-3 = s^3+1, so 2*a=s^3+4.
    This is an elementary obstruction to this EXACT model only, not to
    embedding into a SUBSET of duads or arbitrary pair-label schemes.
    """
    if not isinstance(order, int) or order < 2:
        raise ValueError("integer generalized-quadrangle order >=2")
    s = order
    points = (s + 1) * (s*s + 1)
    degree = s * (s + 1)
    twice_a = s**3 + 4
    if twice_a & 1:
        return {"s": s, "points": points, "degree": degree,
                "implied_a": None, "exact_full_duad_model": False}
    a = twice_a // 2
    duads = a * (a - 1) // 2
    disjoint_degree = (a - 2) * (a - 3) // 2
    return {"s": s, "points": points, "degree": degree,
            "implied_a": a, "duads": duads,
            "duad_disjoint_degree": disjoint_degree,
            "exact_full_duad_model": (duads == points
                                       and disjoint_degree == degree)}


def certified_doily_report(rounds=4, probes=8):
    obj = doily_dual_recovery()
    point_labels, line_labels = obj["point_labels"], obj["line_labels"]
    c4, c6 = fast_minimal_conflicts(point_labels, line_labels)
    exact = certified_result(point_labels, line_labels)
    if (len(c4), len(c6)) != (exact["T4"], exact["T6"]):
        raise AssertionError("fast/independent census mismatch")
    descent = bounded_descent(point_labels, line_labels, seed=6302026,
                              rounds=rounds, probes_per_round=probes)
    final = certified_result(descent["left_labels"],
                             descent["right_labels"])
    if (final["T4"], final["T6"]) != descent["finish"]:
        raise AssertionError("descent exact certificate mismatch")
    return {
        "model": "W(3,2) finite classical doily/duad/syntheme, GF5 unit 2+2 m12",
        "point_pairs": list(point_labels),
        "line_pairs": list(line_labels),
        "ovoid_count": len(obj["ovoid_fives"]),
        "spread_count": len(obj["spread_fives"]),
        "syntheme_count": len(obj["point_synthemes"]),
        "incidences": 45,
        "geometry_T4": exact["T4"], "geometry_T6": exact["T6"],
        "geometry_aset": exact["extracted_aset"],
        "bounded_improved_T4": final["T4"],
        "bounded_improved_T6": final["T6"],
        "bounded_improved_aset": final["extracted_aset"],
        "bounded_swaps": len(descent["accepted"]),
        "bounded_evaluations": descent["evaluations"],
        "rounds": rounds, "probes": probes,
        "restricted_to_order_2": True,
        "unrestricted_aset_exponent_improved": False
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rounds", type=int, default=4)
    parser.add_argument("--probes", type=int, default=8)
    args = parser.parse_args()
    print(json.dumps(certified_doily_report(args.rounds, args.probes),
                     ensure_ascii=False, sort_keys=True, indent=2))
