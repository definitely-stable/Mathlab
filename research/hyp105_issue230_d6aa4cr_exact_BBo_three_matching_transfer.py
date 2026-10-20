"""AA4-CR: EXACT original GQ source-3path -> historical physical B/B-overlap.

For every real symplectic W(3,2^h), fixed arbitrary complete globally
injected correlated typed f,g, and any original NONINCIDENT endpoint
pair (p,l), the GQ has exactly one original 3-edge path
(p,l0),(q,l0),(q,l). Source-only matching-triple extensions
become accepted historical GF5 B/B-overlap iff:
  (i) f(p) and f(q) are disjoint physical coordinate edges;
  (ii) g(l) and g(l0) are disjoint;
  (iii) the 3 other POINT images complete a physical C4 including
        f(p), disjoint from f(q); 3 LINE images analogously
        complete a C4 including g(l), disjoint from g(l0);
  (iv) the real original 3x3 incidence matrix on those two
       triples has a perfect matching.
The 3x3 permanent is 0 or 1, since two distinct matchings imply
a source alternating incidence C4 or C6, forbidden by genuine GQ girth8.

This is an all-h EXACT positive-source-to-physical conversion identity
for ONE historical sevenclass, not a positive lower on S_s nor full R3.
"""
from collections import Counter
from itertools import combinations, permutations
from math import comb

from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_seven_all_a_original_Q,
)

GF5_BBO_WEIGHT = 51750


def c4_completions_from_single_and_doubled(single, doubled, inverse_images, a):
    """Distinct physical C4 choices as triples of REAL source factor IDs.

    The physical double-edged source factor is already degree2 at
    BOTH its coordinates. The single physical source edge lies in
    the remaining four-vertex C4. Exactly 2*C(a-4,2) templates in
    a completely occupied K_a; omitted edges are simply excluded.
    """
    e, d = frozenset(single), frozenset(doubled)
    if len(e) != 2 or len(d) != 2:
        raise ValueError("genuine source image physical simple pair required")
    if not e.isdisjoint(d):
        return ()
    if any(type(v) is not int or not 0 <= v < a for v in e | d):
        raise ValueError("physical coordinate outside original alphabet")
    u, v = sorted(e)
    free = sorted(set(range(a)) - e - d)
    out = []
    for z, w in combinations(free, 2):
        for edges in (
            ((u, z), (z, w), (w, v)),
            ((u, w), (w, z), (z, v)),
        ):
            ids = tuple(inverse_images.get(tuple(sorted(edge))) for edge in edges)
            if all(i is not None for i in ids):
                if len(set(ids)) != 3:
                    raise AssertionError("full original factor injection violated")
                out.append(tuple(sorted(ids)))
    if len(out) != len(set(out)):
        raise AssertionError("same physical original C4 source triple generated twice")
    if len(out) > 2 * comb(a - 4, 2):
        raise AssertionError("original C4 completion exceeds exact physical bound")
    return tuple(out)


def original_nonincident_threepath(p, l, point_lines, line_points):
    """Read immutable TRUE incidence flags; exactly one path iff nonincident."""
    if p not in range(len(point_lines)) or l not in range(len(line_points)):
        raise ValueError("actual source original POINT and LINE IDs required")
    if l in point_lines[p]:
        raise ValueError("source original endpoints must be NONINCIDENT")
    matches = tuple(
        (q, l0)
        for l0 in point_lines[p]
        for q in line_points[l0]
        if q != p and l in point_lines[q]
    )
    if len(matches) != 1:
        raise AssertionError("true original GQ unique 3-incidence path violated")
    q, l0 = matches[0]
    return ((p, l0), (q, l0), (q, l))


def exact_three_by_three_incidence_matching(points, lines, point_lines):
    """All distinct true flags match iff permanent of actual 3x3 source matrix=1.

    In any GQ the result is either ZERO or ONE. Two different perfect
    matchings force a source incidence C4 or C6, impossible (girth8).
    """
    if len(points) != 3 or len(set(points)) != 3 or (
        len(lines) != 3 or len(set(lines)) != 3):
        raise ValueError("three pairwise distinct true source factor IDs on each side")
    found = ()
    for perm in permutations(lines):
        if all(l in point_lines[p] for p, l in zip(points, perm)):
            if found:
                raise AssertionError("two original 3x3 perfect matchings force GQ C4/C6")
            found = tuple(zip(points, perm))
    return found


def original_BBo_exact_three_matching_transfer(model, *, anchor_pairs=None,
                                                point_cut=None, line_cut=None,
                                                collect_original_Q=True):
    """Count REAL physically accepted historic B/B-overlap Q at given anchors.

    If anchor_pairs is None, exhaust ALL original NONINCIDENT POINT-LINE
    pairs in this genuine W3 source host (costly for large h). Optional
    cuts/anchors restrict SOURCE endpoints only, not the actual full f,g.
    Counts true six-DISTINCT ORIGINAL incidence-ID subsets once.
    """
    s, V, a, f, g, point_lines, line_points = _validated_original(model)
    inc = tuple(tuple(e) for e in model["incidences"])
    original_flag_id = {(p, l):j for j, (p, l) in enumerate(inc)}
    if len(original_flag_id) != len(inc):
        raise ValueError("duplicate true source ORIGINAL flag IDs")
    inverse_point = {e:i for i, e in enumerate(f)}
    inverse_line = {e:i for i, e in enumerate(g)}
    if len(inverse_point) != V or len(inverse_line) != V:
        raise ValueError("single full injected original typed maps required")
    def check_cut(c):
        if c is None:
            return None
        t = tuple(c)
        if len(set(t)) != len(t) or any(type(v) is not int or not 0 <= v < a for v in t):
            raise ValueError("valid distinct physical cut coordinates needed")
        return frozenset(t)
    X = check_cut(point_cut)
    Y = check_cut(line_cut)
    if anchor_pairs is None:
        anchors = tuple((p, l) for p in range(V) for l in range(V)
                        if l not in point_lines[p]
                        and (X is None or set(f[p]) <= X)
                        and (Y is None or set(g[l]) <= Y))
    else:
        anchors = tuple(tuple(x) for x in anchor_pairs)
        if len(anchors) != len(set(anchors)):
            raise ValueError("duplicate same original source (p,l) 3path anchor")
        for p, l in anchors:
            if (type(p) is not int or type(l) is not int or not
                    (0 <= p < V and 0 <= l < V) or l in point_lines[p]):
                raise ValueError("each anchor must be one genuine nonincident original POINT/LINE pair")
            if (X is not None and not set(f[p]) <= X) or (
                    Y is not None and not set(g[l]) <= Y):
                raise ValueError("given anchor does not lie in requested true physical coordinate cuts")
    chosen = []
    matched = 0
    physical_disjoint_anchors = 0
    completion_pairs = 0
    perfect_matches = 0
    zero_permanents = 0
    candidate_cycle_triples_left = 0
    candidate_cycle_triples_right = 0
    for p, l in anchors:
        source_path = original_nonincident_threepath(p, l, point_lines, line_points)
        (p0, l0), (q, l1), (q1, l2) = source_path
        if (p0, q1, l0, l1, l2) != (p, q, l0, l0, l):
            raise AssertionError("genuine original 3path source flag orientation wrong")
        if set(f[p]) & set(f[q]) or set(g[l]) & set(g[l0]):
            continue
        physical_disjoint_anchors += 1
        triples_p = c4_completions_from_single_and_doubled(
            f[p], f[q], inverse_point, a)
        triples_l = c4_completions_from_single_and_doubled(
            g[l], g[l0], inverse_line, a)
        candidate_cycle_triples_left += len(triples_p)
        candidate_cycle_triples_right += len(triples_l)
        path_ids = tuple(original_flag_id[flag] for flag in source_path)
        for ps in triples_p:
            for ls in triples_l:
                completion_pairs += 1
                matching = exact_three_by_three_incidence_matching(
                    ps, ls, point_lines)
                if not matching:
                    zero_permanents += 1
                    continue
                perfect_matches += 1
                Q = tuple(sorted(path_ids + tuple(original_flag_id[e] for e in matching)))
                if len(Q) != 6 or len(set(Q)) != 6:
                    raise AssertionError("path and matched singleton genuine original flags not disjoint")
                if classify_seven_all_a_original_Q(Q, f, g, inc) != "B/B-overlap":
                    raise AssertionError("true original B/B-overlap accepted tag differs from physical C4 triple permanent")
                chosen.append(Q)
    if len(chosen) != len(set(chosen)) or len(chosen) != perfect_matches:
        raise AssertionError("accepted real original Q duplicated: unique source P3 anchor failed")
    result = {
        "s":s, "V":V, "a":a,
        "actual_unique_NONINCIDENT_original_3path_anchors":len(anchors),
        "physical_disjoint_original_3path_anchors":physical_disjoint_anchors,
        "source_point_physical_C4_triples_examined":candidate_cycle_triples_left,
        "source_line_physical_C4_triples_examined":candidate_cycle_triples_right,
        "paired_two_sided_C4_templates":completion_pairs,
        "three_by_three_source_PERMANENT_zero":zero_permanents,
        "three_by_three_source_PERMANENT_one":perfect_matches,
        "historical_accepted_original_BBo_sixflag_Q":len(chosen),
        "historical_accepted_GF5_weighted_numerator":GF5_BBO_WEIGHT*len(chosen),
        "actual_distinct_original_sixflag_Q_sets":tuple(sorted(chosen)) if collect_original_Q else None,
        "all_h_exact_equivalence_source_threepath_to_physical_BBo":True,
        "all_h_positive_uniform_physical_transfer_UNPROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER"
    }
    if zero_permanents + perfect_matches != completion_pairs:
        raise AssertionError("all physical pair completions must have permanent 0 or1")
    if result["historical_accepted_original_BBo_sixflag_Q"] > (
            len(anchors)*4*comb(a-4,2)**2):
        raise AssertionError("all-h physical C4 completion upper count invalid")
    return result


def original_dual_model_immutable_source_Q(model):
    """Full ORIGINAL POINT↔LINE source dual, keeping immutable flag IDs in order."""
    t = dict(model)
    t["left_labels"], t["right_labels"] = (
        model["right_labels"], model["left_labels"])
    t["incidences"] = tuple((l, p) for p, l in model["incidences"])
    return t
