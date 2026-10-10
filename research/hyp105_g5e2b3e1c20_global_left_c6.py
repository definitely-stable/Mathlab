"""HYP-105 C20: unavoidable GLOBAL original-left six-cycle witness pressure.

The bound applies to ONE globally consistent injection of EVERY original
W(3,s) point into one fixed occupied physical K_a edge set F. It is
NOT a bound on the simultaneously accepted RIGHT projection or S_seven.

A K_a has 60*C(a,6) unoriented simple 6-cycles. Each missing physical
edge belongs to exactly 24*C(a-2,4) of these cycles. A union bound
therefore leaves at least

    c6_lower = 60*C(a,6) - 24*t*C(a-2,4),

where t=C(a,2)-V and V=(s+1)(s*s+1). This is POSITIVE for every
s=2**h>=2 in the MINIMAL physical coordinate model. A physical 6-cycle
uses six distinct original points, each of degree s+1 in the TRUE
original GQ. Selecting one original incidence at each point gives
(s+1)**6 DISTINCT ORIGINAL six-incidence A-left witnesses. Different
physical cycles cannot duplicate these incidence sets.

All-h N_left_A(f) >= c6_lower*(s+1)**6 = Omega(s**15).
There is NO conclusion for right acceptance, full GF5, or the
universal all-h positive S_seven target in issue #230.
"""
from itertools import combinations, permutations, product
from math import comb

from hyp105_g5e2b3e1c18_zero_star_barrier import (
    minimal_physical_coordinates,
)


def all_h_global_left_c6_lower(s):
    """Exact integer formula plus fully quantified all-powers proof gate."""
    if type(s) is not int or s < 2 or s & (s - 1):
        raise ValueError("requires s=2^h with h>=1")
    v = (s+1)*(s*s+1)
    a = minimal_physical_coordinates(v)
    t = comb(a, 2)-v
    if not (comb(a-1, 2) < v <= comb(a, 2) and 0 <= t < a-1):
        raise AssertionError("invalid minimal K_a physical occupancy")
    all_cycles = 60*comb(a, 6)
    destroyed_per_missing_edge = 24*comb(a-2, 4)
    surviving_lower = all_cycles-t*destroyed_per_missing_edge
    if s == 2:
        if (v, a, t, surviving_lower) != (15, 6, 0, 60):
            raise AssertionError("GF2 full K6 base case failed")
    elif (a < 14
          or not (all_cycles > t*destroyed_per_missing_edge)
          or not (2*a*(a-1) > 24*(a-2))):
        # All s>=4 have a>=14. For ANY admissible t<=a-2,
        # a lower is 2*a*(a-1)-24*(a-2), strictly positive.
        raise AssertionError("all-h positivity arithmetic failed")
    left_pressure_lower = surviving_lower*(s+1)**6
    if left_pressure_lower <= 0:
        raise AssertionError("unavoidable complete-global-left source lost")
    return {
        "s": s,
        "original_GQ_points": v,
        "original_lines_through_each_point": s+1,
        "minimal_physical_coordinates": a,
        "occupied_physical_pair_edges": v,
        "missing_physical_pair_edges": t,
        "all_Ka_simple_six_cycles": all_cycles,
        "cycles_destroyed_per_one_missing_edge": destroyed_per_missing_edge,
        "certified_remaining_physical_six_cycles": surviving_lower,
        "per_cycle_distinct_original_incidence_lifts": (s+1)**6,
        "certified_distinct_original_left_A_sixsets_lower":
            left_pressure_lower,
        "universal_global_left_only_positive": True,
        "asymptotic_left_A_growth": "Omega(s^15)",
        "no_simultaneous_right_seven_class_lower": True,
        "no_global_GF5_R3_or_ASET_exponent": True,
    }


def canonical_simple_six_cycles(occupied_edges, a, *, max_vertices=14):
    """Independent small-host brute oracle; does NOT count false 2-triangles.

    Identifies each undirected C6 once by smallest start coordinate and
    reversal symmetry, even if the occupied graph has extra chords.
    """
    if (type(a) is not int or a < 6
            or type(max_vertices) is not int or max_vertices < 6
            or a > max_vertices):
        raise ValueError("exact simple six-cycle enumeration exceeds hard cap")
    try:
        edges = tuple(tuple(x) for x in occupied_edges)
    except (TypeError, ValueError) as exc:
        raise ValueError("physical edges must be iterable coordinate pairs") from exc
    if (len(set(edges)) != len(edges)
            or any(len(x) != 2
                   or any(type(v) is not int or not 0 <= v < a for v in x)
                   or x[0] >= x[1] for x in edges)):
        raise ValueError("edges must be distinct canonical unordered K_a pairs")
    occupied = set(edges)
    for vertices in combinations(range(a), 6):
        start = vertices[0]
        for tail in permutations(vertices[1:]):
            if tail[0] > tail[-1]:
                continue
            walk = (start,)+tail
            cycle = tuple(sorted(
                tuple(sorted((walk[j], walk[(j+1)%6])))
                for j in range(6)))
            if all(e in occupied for e in cycle):
                yield cycle


def finite_graph_C20_audit(s, occupied_edges, *, max_vertices=14):
    """Exact c6 enumeration and acceptance of ALL admissible F adversaries."""
    info = all_h_global_left_c6_lower(s)
    a, v = (info["minimal_physical_coordinates"],
            info["occupied_physical_pair_edges"])
    try:
        edges = tuple(tuple(e) for e in occupied_edges)
    except (TypeError, ValueError) as exc:
        raise ValueError("physical F must be an iterable") from exc
    if len(edges) != v:
        raise ValueError("F does not have the exact V occupied physical edges")
    cycles = tuple(canonical_simple_six_cycles(
        edges, a, max_vertices=max_vertices))
    if len(cycles) != len(set(cycles)):
        raise AssertionError("simple six-cycle duplicate in independent audit")
    if len(cycles) < info["certified_remaining_physical_six_cycles"]:
        raise AssertionError("all-h bound falsified by a legal physical F")
    return {
        "s": s,
        "physical_six_cycles_actual": len(cycles),
        "physical_six_cycles_certified_lower":
            info["certified_remaining_physical_six_cycles"],
        "original_left_A_sixsets_actual_by_cycle_lifts":
            len(cycles)*(s+1)**6,
        "original_left_A_sixsets_certified_lower":
            info["certified_distinct_original_left_A_sixsets_lower"],
        "no_original_GQ_GF4_incidence_enumeration_performed": s != 2,
    }


def genuine_W32_C20_report():
    """Independent true ORIGINAL W32 six-incidence A-source membership audit."""
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    from hyp105_g5e2b3e1a_fixed_leading import PAIRS, selected_left_six
    from hyp105_g5e2b3e1c14_domain_certificates import _filled_model

    info = all_h_global_left_c6_lower(2)
    cycles = tuple(canonical_simple_six_cycles(PAIRS, 6))
    if len(cycles) != 60:
        raise AssertionError("complete physical K6 has exactly 60 C6")
    cases = []
    for scheme in ("lex", "reverse-line"):
        baseline = pair_labeled_symplectic(1, scheme)
        for relabel in ("original", "swap-original-0-13"):
            if relabel == "original":
                m = baseline
            else:
                old = tuple(PAIRS.index(e) for e in baseline["left_labels"])
                changed = {i: old[i] for i in range(15)}
                changed[0], changed[13] = changed[13], changed[0]
                m = _filled_model(baseline, changed, {})
            inverse = {e: i for i, e in enumerate(m["left_labels"])}
            incidence = m["incidences"]
            by_point = [[] for _ in range(15)]
            for i, (p, _) in enumerate(incidence):
                by_point[p].append(i)
            if any(len(x) != 3 for x in by_point):
                raise AssertionError("invalid original W32 GQ point degree")
            expected = set()
            for cycle in cycles:
                orig_points = tuple(inverse[e] for e in cycle)
                if len(set(orig_points)) != 6:
                    raise AssertionError("physical simple cycle reused point")
                for selected in product(*(by_point[p] for p in orig_points)):
                    j = tuple(sorted(selected))
                    if j in expected:
                        raise AssertionError("global original source lifts collided")
                    expected.add(j)
            if len(expected) != 60*3**6:
                raise AssertionError("incorrect six-cycle lift count")
            source = set()
            all_source = set()
            for six, kind in selected_left_six(m):
                all_source.add(six)
                if kind == "A":
                    source.add(six)
            if (len(all_source) != 62370 or len(source) != 51030
                    or not expected.issubset(source)):
                raise AssertionError("independent actual original W32 A-source mismatch")
            cases.append({
                "scheme": scheme,
                "global_original_left_relabel": relabel,
                "all_true_original_left_sixsets": len(all_source),
                "true_left_A_sixsets": len(source),
                "certified_Hamilton_sixcycle_source": len(expected),
                "true_left_A_other_2triangle_sixsets":
                    len(source)-len(expected),
            })
    return {
        "scope": "REAL_ORIGINAL_W32_ONE_COMMON_GLOBAL_LEFT_MAP",
        "all_h_s2_analytic_gate": info,
        "independent_original_sixset_evidence": cases,
        "unavoidable_left_A_witnesses_not_right_seven_classes": True,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(genuine_W32_C20_report(), indent=2, sort_keys=True))
