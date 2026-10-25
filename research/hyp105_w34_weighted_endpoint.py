"""AA4-WE: exact finite weighted endpoint/pseudo-covariance audit for W(3,4).

This is an evidence-only bridge to issue #230. The original GQ incidence
source is immutable and genuine; globally injected f (points) and g
(lines) need not be independent. This counts all correctly projected,
coordinate-distinct, directed physical 3-walks, NOT accepted GF(5)
six-original-flag motifs.
"""
from collections import Counter
from fractions import Fraction

from hyp105_w34_independent_oracle import _source_and_labels


def _physical_adjacency(f, g, flags):
    """Physical directed multigraph; duplicate source-generated arcs count."""
    adjacent = {}
    for p, l in flags:
        u, v = f[p]
        x, y = g[l]
        for start, end in (((u, x), (v, y)), ((u, y), (v, x))):
            adjacent.setdefault(start, []).append(end)
            adjacent.setdefault(end, []).append(start)
    return adjacent


def _source_projection(lines, point_lines):
    """Each nonincident original point-line pair has one 3-edge path."""
    result = {}
    for point in range(85):
        for line in range(85):
            if line in point_lines[point]:
                continue
            choices = [
                (middle_point, middle_line)
                for middle_point in lines[line]
                for middle_line in point_lines[point]
                if middle_point in lines[middle_line]
            ]
            if len(choices) != 1:
                raise AssertionError("nonincident GQ 3-path is not unique")
            result[point, line] = choices[0]
    if len(result) != 85 * 4 * 4 * 5:
        raise AssertionError("incorrect GQ nonincident endpoint universe")
    return result


def _bad_endpoint_classes(f, g, projection):
    out = {}
    for (q, r), (p, l0) in projection.items():
        left = bool(set(f[q]) & set(f[p]))
        right = bool(set(g[r]) & set(g[l0]))
        out[q, r] = (left, right)
    return out


def _sparse_join_per_pair(point, line, f, g, adjacent_counts):
    """Second independent indexing: 4 ordered opposite-corner pairs.

    Exactly reproduce multigraph adjacency multiplicity products rather
    than enumerating physical 3-walks and then recovering source ids.
    """
    x0, x3 = f[point]
    y0, y3 = g[line]
    total = 0
    for u0, u3 in ((x0, x3), (x3, x0)):
        for v0, v3 in ((y0, y3), (y3, y0)):
            start, end = (u0, v0), (u3, v3)
            for middle1, m01 in adjacent_counts.get(start, {}).items():
                if middle1[0] in (u0, u3) or middle1[1] in (v0, v3):
                    continue
                for middle2, m12 in adjacent_counts.get(middle1, {}).items():
                    if (middle2[0] in (u0, u3, middle1[0]) or
                            middle2[1] in (v0, v3, middle1[1])):
                        continue
                    total += m01 * m12 * adjacent_counts.get(
                        middle2, {}
                    ).get(end, 0)
    return total


def weighted_endpoint_profile(f, g, *, verify_join=True):
    """Return independently inspectable exact integer moments of N3.

    N3(q,r): multiplicity of all *proper* physical 3-walks whose
    projected endpoint physical pair-images recover the original
    genuinely nonincident (POINT q, LINE r). Does not discard internal
    blocked walks (otherwise the bad-endpoint mass is trivially zero).
    """
    lines, flags, point_lines = _source_and_labels(f, g)
    f = [tuple(pair) for pair in f]
    g = [tuple(pair) for pair in g]
    adjacency = _physical_adjacency(f, g, flags)
    projection = _source_projection(lines, point_lines)
    bad = _bad_endpoint_classes(f, g, projection)
    point_of_pair = {frozenset(pair): k for k, pair in enumerate(f)}
    line_of_pair = {frozenset(pair): k for k, pair in enumerate(g)}
    multiplicities = Counter()
    total_proper = missing = incident = 0

    # Method A: genuine source flag -> physical adjacency list -> 3-walk.
    for vertex0, neighbors in adjacency.items():
        for vertex1 in neighbors:
            for vertex2 in adjacency.get(vertex1, ()):
                if (len({vertex0[0], vertex1[0], vertex2[0]}) != 3
                        or len({vertex0[1], vertex1[1], vertex2[1]}) != 3):
                    continue
                for vertex3 in adjacency.get(vertex2, ()):
                    if (len({vertex0[0], vertex1[0], vertex2[0], vertex3[0]}) != 4
                            or len({vertex0[1], vertex1[1], vertex2[1], vertex3[1]}) != 4):
                        continue
                    total_proper += 1
                    q = point_of_pair.get(frozenset((vertex0[0], vertex3[0])))
                    r = line_of_pair.get(frozenset((vertex0[1], vertex3[1])))
                    if q is None or r is None:
                        missing += 1
                    elif (q, r) not in projection:
                        incident += 1
                    else:
                        multiplicities[q, r] += 1

    # Method B: per-(q,r) 4-corner adjacency-multigraph join contraction.
    if verify_join:
        counts = {vertex: Counter(neighbors)
                  for vertex, neighbors in adjacency.items()}
        for q, r in projection:
            if _sparse_join_per_pair(q, r, f, g, counts) != multiplicities[q, r]:
                raise AssertionError(
                    f"independent 4-corner multiplicity mismatch: {(q,r)}"
                )

    histogram = Counter(multiplicities.get(key, 0) for key in projection)
    result = {
        "s": 4, "V": 85, "a": 14,
        "source_nonincident_pairs": len(projection),
        "proper_P3": total_proper, "missing": missing, "incident": incident,
        "path_mass": total_proper - missing - incident,
        "N3_zero_pairs": histogram.get(0, 0),
        "N3_max": max(histogram),
        "N3_sum_squares": sum(x * x * frequency
                              for x, frequency in histogram.items()),
        "N3_histogram": dict(sorted(histogram.items())),
    }
    for name, predicate in (
        ("bad", lambda left, right: left or right),
        ("good", lambda left, right: not (left or right)),
        ("left", lambda left, right: left),
        ("right", lambda left, right: right),
        ("both", lambda left, right: left and right),
    ):
        keys = [key for key, pair in bad.items() if predicate(*pair)]
        result[f"{name}_pairs"] = len(keys)
        result[f"{name}_path_mass"] = sum(multiplicities[key] for key in keys)
        result[f"{name}_N3_sum_squares"] = sum(
            multiplicities[key] ** 2 for key in keys
        )
    u, b, p, m = (result["source_nonincident_pairs"],
                   result["bad_pairs"], result["path_mass"],
                   result["bad_path_mass"])
    result["weighted_minus_unweighted_fraction"] = Fraction(m, p) - Fraction(b, u)
    result["covariance_indicator_N3"] = Fraction(m*u - b*p, u*u)
    result["bad_to_total_path_ratio"] = Fraction(m, p)
    result["bad_to_total_pair_ratio"] = Fraction(b, u)

    # Exact mass/covariance identities (no statistical independence).
    if result["bad_path_mass"] + result["good_path_mass"] != p:
        raise AssertionError("weighted mass partition failure")
    if result["bad_pairs"] + result["good_pairs"] != u:
        raise AssertionError("endpoint partition failure")
    if result["left_pairs"] + result["right_pairs"] - result["both_pairs"] != b:
        raise AssertionError("endpoint inclusion-exclusion failure")
    if (result["left_path_mass"] + result["right_path_mass"]
            - result["both_path_mass"] != m):
        raise AssertionError("weighted inclusion-exclusion failure")
    if (Fraction(b, u) * p + u * result["covariance_indicator_N3"] != m):
        raise AssertionError("covariance decomposition failure")
    if b > 4 * 85 * 4 * (14 - 2):
        raise AssertionError("unweighted typed bad endpoint theorem failed")
    return result


def moment_sufficient_conditions(s, bad_pairs_upper, bad_paths_sum_sq_upper):
    """Report ONLY conditional Cauchy bound, never infer it from Omega."""
    from math import isqrt
    if s < 2 or bad_pairs_upper < 0 or bad_paths_sum_sq_upper < 0:
        raise ValueError("nonnegative upper bounds and s >= 2 required")
    product = bad_pairs_upper * bad_paths_sum_sq_upper
    return {
        "integer_ceiling_cs_upper": isqrt(product) + (isqrt(product)**2 < product),
        "is_upper_bound_assumption": True,
        "root_proved": False,
    }
