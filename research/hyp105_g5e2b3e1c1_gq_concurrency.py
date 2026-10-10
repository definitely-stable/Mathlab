"""HYP-105 B3.2-E1-C1: GQ-specific concurrence and B/A wedge factorization.

ALL-h combinatorics assumes the classical W(3,s), s=2**h, h>=1,
and its regular bipartite incidence graph with no 4- or 6-cycles.
Executable original-incidence census is deliberately limited to W(3,2).
The all-h formulas are NOT an all-correlated right-map lower bound.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb
import json

from hyp105_g5e2b3e1b1a_one_sided import gq_parameters
from hyp105_g5e2b3e1a_fixed_leading import validated_small_model


def all_h_right_line_concurrency(s):
    """Exact concurrence graph triple census, from GQ(s,s) axioms.

    The right-line concurrence graph is strongly regular:
    (v,k,lambda,mu)=(V,s(s+1),s-1,s+1).
    These are classical GQ facts, not a new SRG theorem.
    """
    p = gq_parameters(s)
    v = p["V"]
    k = s * (s + 1)
    lam, mu = s - 1, s + 1
    edges = v * k // 2
    if v * k % 2:
        raise AssertionError("noninteger concurrence edge count")
    triangles_num = v * k * lam
    if triangles_num % 6:
        raise AssertionError("noninteger concurrence triangle count")
    n3 = triangles_num // 6
    n2 = v * comb(k, 2) - 3 * n3
    n1 = edges * (v - 2) - 2 * n2 - 3 * n3
    n0 = comb(v, 3) - n1 - n2 - n3
    if min(n0, n1, n2, n3) < 0:
        raise AssertionError("negative induced triple count")
    if k * (k - lam - 1) != (v - k - 1) * mu:
        raise AssertionError("GQ strongly regular relation")
    # Every 6-set R supporting a B-left source must include a pair
    # of intersecting original right lines. Markov on the number of
    # such pairs gives this strict asymptotic support restriction.
    concurrence_expectation = Fraction(15 * k, v - 1)
    max_supported_sixsets = min(
        comb(v, 6), edges * comb(v - 2, 4))
    return {
        "s": s, "V": v,
        "line_concurrence_degree": k,
        "adjacent_common_neighbors": lam,
        "nonadjacent_common_neighbors": mu,
        "line_concurrence_pairs": edges,
        "induced_three_line_counts_by_edges": (n0, n1, n2, n3),
        "random_sixset_mean_concurrent_pairs": concurrence_expectation,
        "all_BA_source_support_sixsets_upper": max_supported_sixsets,
        "source_support_requires_concurrent_line_pair": True,
        "universal_all_correlated_overlap_lower": False,
    }


def original_right_line_concurrency(model):
    """Independent original incidence graph, not physical pair adjacency."""
    _, _, original, _ = validated_small_model(model)
    line_to_points = [set() for _ in model["right_labels"]]
    for p, line in original:
        line_to_points[line].add(p)
    delta = model["s"] + 1
    if any(len(x) != delta for x in line_to_points):
        raise AssertionError("right GQ regularity lost")
    return tuple(
        frozenset(j for j in range(len(line_to_points)) if j != i
                  and line_to_points[i] & line_to_points[j])
        for i in range(len(line_to_points))
    )


def physical_four_cycles_on_other_coordinates(pair, a):
    """Construct the three 4-cycles on the complement of one K6 pair.

    This W32 oracle deliberately refuses a larger physical alphabet;
    the symbolic wedge identity applies to any legal f and s.
    """
    if a != 6:
        raise ValueError("finite wedge enumerator is W(3,2)/K6 only")
    coords = tuple(c for c in range(a) if c not in pair)
    edges = tuple(combinations(coords, 2))
    for four in combinations(edges, 4):
        if all(sum(c in e for e in four) == 2 for c in coords):
            yield four


def weighted_BA_via_original_point_wedges(model):
    """Independent W32 enumeration by doubled point and physical C4.

    Every selected original six-incidence B-left set has a UNIQUE
    repeated original left point p, a UNIQUE physical four-cycle on
    the other coordinates, and an UNORDERED pair of lines through p.
    The remaining four singleton original points choose one line each.
    Keep only six mutually distinct original right line endpoints.
    No use of selected_left_six() or the C0 source enumerator.
    """
    physical_left, _, original, _ = validated_small_model(model)
    point_at_physical = {edge: i for i, edge in enumerate(physical_left)}
    point_lines = [set() for _ in physical_left]
    for p, line in original:
        point_lines[p].add(line)
    if any(len(lines) != 3 for lines in point_lines):
        raise AssertionError("W32 point degree must be 3")
    result = Counter()
    total_B_candidates = 0
    for repeated, pair in enumerate(physical_left):
        for square in physical_four_cycles_on_other_coordinates(pair, 6):
            singles = tuple(point_at_physical[e] for e in square)
            if len(set(singles + (repeated,))) != 5:
                raise AssertionError("B-left physical labels noninjective")
            neighbors = tuple(tuple(sorted(point_lines[q])) for q in singles)
            for twice in combinations(sorted(point_lines[repeated]), 2):
                for rest in product(*neighbors):
                    total_B_candidates += 1
                    right = twice + rest
                    if len(set(right)) == 6:
                        result[frozenset(right)] += 1
    if total_B_candidates != 10935:
        raise AssertionError("independent B-left candidate count changed")
    if sum(result.values()) != 5000:
        raise AssertionError("W32 six-distinct-right GQ mass changed")
    return result


def exact_W32_source_concurrency_diagnostic(model, weights=None):
    """Compare independent GQ graph and source third marginals.

    R->weight is based on ORIGINAL six distinct right-line vertices.
    Third marginals are grouped by 0/1/2/3 concurrence pairs among
    their three named original lines, not by physical T_a edge orbits.
    """
    from hyp105_g5e2b3e1c0_weighted_overlap import source_weighted_BA_hypergraph
    if weights is None:
        weights = source_weighted_BA_hypergraph(model)
    graph = original_right_line_concurrency(model)
    v = len(graph)
    cert = all_h_right_line_concurrency(model["s"])
    if v != cert["V"]:
        raise AssertionError("wrong GQ parameters")
    if any(len(nbrs) != cert["line_concurrence_degree"] for nbrs in graph):
        raise AssertionError("right-line concurrence degree mismatch")
    if any(len(graph[i] & graph[j]) !=
           (cert["adjacent_common_neighbors"] if j in graph[i]
            else cert["nonadjacent_common_neighbors"])
           for i in range(v) for j in range(i + 1, v)):
        raise AssertionError("GQ lambda/mu mismatch")
    triples = Counter()
    for R, m in weights.items():
        if len(R) != 6 or m < 0 or not isinstance(m, int):
            raise ValueError("invalid weighted original right sixset")
        for t in combinations(sorted(R), 3):
            triples[t] += m
    if sum(triples.values()) != 20 * sum(weights.values()):
        raise AssertionError("third source-marginal moment not conserved")
    triple_universe = [0] * 4
    moment_sum = [0] * 4
    positive = [0] * 4
    for A in combinations(range(v), 3):
        c = sum(y in graph[x] for x, y in combinations(A, 2))
        triple_universe[c] += 1
        moment_sum[c] += triples[A]
        positive[c] += bool(triples[A])
        if c == 3:
            # GQ excludes nonconcurrent triangles (incidence 6-cycles).
            _, _, original, _ = validated_small_model(model)
            point_sets = [
                set(p for p, line in original if line == x) for x in A
            ]
            if not set.intersection(*point_sets):
                raise AssertionError("spurious nonconcurrent line triangle")
    if tuple(triple_universe) != cert["induced_three_line_counts_by_edges"]:
        raise AssertionError("all-h GQ three-line census mismatch")
    delta = model["s"] + 1
    # Concurrence-sensitive improvement of the 15 Delta^4 cap:
    # only each ACTUALLY concurrent pair in a chosen R can be doubled.
    for R in combinations(range(v), 6):
        concurrent_pairs = sum(y in graph[x] for x, y in combinations(R, 2))
        if weights.get(frozenset(R), 0) > concurrent_pairs * delta**4:
            raise AssertionError("GQ concurrence-fiber cap falsified")
    return {
        "s": model["s"],
        "source_total_mass": sum(weights.values()),
        "source_positive_sixsets": len(weights),
        "source_3marginal_by_concurrence_pairs": tuple(moment_sum),
        "source_3marginal_positive_triples_by_class": tuple(positive),
        "all_original_three_line_sets_by_class": tuple(triple_universe),
        "source_third_marginal_total": sum(moment_sum),
        "all_right_maps_universal_lower_proved": False,
    }


def report():
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    result = {}
    for s in (2, 4, 8, 16, 32, 64):
        c = all_h_right_line_concurrency(s)
        c["random_sixset_mean_concurrent_pairs"] = str(
            c["random_sixset_mean_concurrent_pairs"])
        result[str(s)] = c
    result["finite_W32"] = exact_W32_source_concurrency_diagnostic(
        pair_labeled_symplectic(1, "reverse-line"))
    return result


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True))
