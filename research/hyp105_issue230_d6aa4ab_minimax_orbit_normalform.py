"""HYP-105 #230 / AA4-AB-SYM: exact adversarial pair-map orbit reduction.

Theorems (for genuine W(3,2^h), all h >= 1):
  (i) two independent physical-coordinate permutations and any *common*
      type-preserving original GQ automorphism preserve every one of the
      seven accepted GF(5) original-six-incidence motif counts;
  (ii) any pair of COMPLETE globally injective maps admits simultaneous
      physical-coordinate normalization f(p*)=g(l*)=(0,1) for arbitrary
      fixed original point p* and original line l*;
  (iii) this normalization retains every minimizer of the full S and
      the historical weighted 51-palette numerator.

Finite strict transvection and true-geometry checks below support
h=1,2,3 via the independently existing symplectic_gq generator. The
algebraic group-action proof applies to all h; the finite oracle does
not claim to construct GQ above its explicit memory/time cap.
"""
from collections import Counter
from itertools import combinations
from functools import lru_cache
from math import prod

from hyp105_b1_symplectic import normalized, symplectic, symplectic_gq
from hyp105_issue230_proof_audit import parameters
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS


def _permutation(value, n, label):
    p = tuple(value)
    if len(p) != n or set(p) != set(range(n)) or any(type(x) is not int for x in p):
        raise ValueError(label + " must be an actual full permutation")
    return p


@lru_cache(maxsize=3)
def _true_model_incidence(s):
    if s not in (2, 4, 8):
        raise ValueError("strict finite genuine-GQ oracle supports s=2,4,8 only")
    _, points, lines, truth = symplectic_gq(s.bit_length()-1)
    return len(points), len(lines), frozenset(truth)


def _valid_original_model(model, *, finite_true_geometry=True):
    s = model.get("s")
    par = parameters(s)
    v, a, d = par["V"], par["a"], par["Delta"]
    if model.get("a") != a:
        raise ValueError("not minimal physical coordinate alphabet")
    inc = tuple(tuple(x) for x in model["incidences"])
    if len(inc) != v*d or len(set(inc)) != v*d or any(
        len(e) != 2 or any(type(x) is not int or not 0 <= x < v for x in e)
        for e in inc
    ):
        raise ValueError("six-incidence source universe requires true distinct incidences")
    physical = set(combinations(range(a), 2))
    for key in ("left_labels", "right_labels"):
        arr = tuple(tuple(e) for e in model[key])
        if len(arr) != v or len(set(arr)) != v or any(e not in physical for e in arr):
            raise ValueError("one COMPLETE globally injective canonical physical map per type")
    if finite_true_geometry:
        np, nl, truth = _true_model_incidence(s)
        if np != v or nl != v or set(inc) != truth:
            raise ValueError("NOT the genuine original indexed W(3,s) incidence graph")
    return v, a, frozenset(inc)


def _apply_physical(edge, permutation):
    return tuple(sorted((permutation[edge[0]], permutation[edge[1]])))


def edge_to_zero_one_permutation(edge, a):
    """Deterministically send prescribed physical unordered pair to (0,1)."""
    if tuple(edge) not in set(combinations(range(a), 2)):
        raise ValueError("anchor must be a canonical physical K_a pair")
    u, v = edge
    image = [None] * a
    image[u], image[v] = 0, 1
    for index, x in enumerate(k for k in range(a) if k not in (u, v)), 2):
        image[x] = index
    return _permutation(image, a, "physical anchor")


def transform_model(model, *, point_sources=None, line_sources=None,
                    point_coordinates=None, line_coordinates=None):
    """Apply a genuine SOURCE automorphism and independent PHYSICAL S_a actions.

    Point/line-source changes must be a *joint original incidence
    automorphism*, never two unrelated arbitrary source permutations.
    """
    v, a, inc = _valid_original_model(model)
    p = _permutation(range(v) if point_sources is None else point_sources, v, "point source")
    l = _permutation(range(v) if line_sources is None else line_sources, v, "line source")
    cp = _permutation(range(a) if point_coordinates is None else point_coordinates,
                      a, "point physical")
    cl = _permutation(range(a) if line_coordinates is None else line_coordinates,
                      a, "line physical")
    if {(p[x], l[y]) for x, y in inc} != inc:
        raise ValueError("independent source permutations are NOT a GQ automorphism")
    f = [None] * v
    g = [None] * v
    for old in range(v):
        f[p[old]] = _apply_physical(model["left_labels"][old], cp)
        g[l[old]] = _apply_physical(model["right_labels"][old], cl)
    out = dict(model, left_labels=tuple(f), right_labels=tuple(g))
    out["supports"] = tuple(tuple(sorted(
        f[x]+tuple(a+t for t in g[y]))) for x, y in model["incidences"])
    _valid_original_model(out)
    return out


def anchored_pair_normal_form(model, point_anchor=0, line_anchor=0):
    """Lossless minimax representative with two prescribed physical images."""
    v, a, _ = _valid_original_model(model)
    if (type(point_anchor) is not int or type(line_anchor) is not int
            or not 0 <= point_anchor < v or not 0 <= line_anchor < v):
        raise ValueError("source anchor not a true point and line index")
    cp = edge_to_zero_one_permutation(model["left_labels"][point_anchor], a)
    cl = edge_to_zero_one_permutation(model["right_labels"][line_anchor], a)
    out = transform_model(model, point_coordinates=cp, line_coordinates=cl)
    assert out["left_labels"][point_anchor] == (0, 1)
    assert out["right_labels"][line_anchor] == (0, 1)
    return out


def symplectic_transvection_source(model, seed_point=0):
    """Concrete type-preserving Sp(4,2^h) symplectic transvection.

    x -> x + <x,v>v, in characteristic two. This is a bijective
    symplectic isometry; the generator validates the ACTUAL incidence
    automorphism instead of relying on a guessed line-index permutation.
    """
    v, _, inc = _valid_original_model(model)
    field, points, lines, truth = symplectic_gq(model["s"].bit_length()-1)
    if type(seed_point) is not int or not 0 <= seed_point < v:
        raise ValueError("true original nonzero seed point required")
    seed = points[seed_point]
    point_index = {x: i for i, x in enumerate(points)}
    moved = []
    for x in points:
        scale = symplectic(x, seed, field)
        image = normalized(tuple(xi ^ field.mul(scale, vi)
                                 for xi, vi in zip(x, seed)), field)
        moved.append(point_index[image])
    line_index = {frozenset(x): i for i, x in enumerate(lines)}
    line_moved = tuple(line_index[frozenset(moved[x] for x in line)]
                       for line in lines)
    point_moved = tuple(moved)
    if any(point_moved[point_moved[i]] != i for i in range(v)):
        raise AssertionError("characteristic-two transvection must be an involution")
    if {(point_moved[p], line_moved[l]) for p, l in inc} != inc:
        raise AssertionError("claimed symplectic map did not preserve actual incidence")
    return point_moved, line_moved


def _six_physical_projection(Q, inc, labels, side):
    sources = Counter(inc[i][side] for i in Q)
    mult = sorted(sources.values(), reverse=True)
    kind = { (1, 1, 1, 1, 1, 1): "A",
             (2, 1, 1, 1, 1): "B",
             (2, 2, 2): "C" }.get(tuple(mult))
    if kind is None:
        return None, None
    bycoord = {}
    for i in Q:
        for coord in labels[inc[i][side]]:
            bycoord.setdefault(coord, []).append(i)
    if len(bycoord) != 6 or any(len(v) != 2 for v in bycoord.values()):
        return None, None
    physical_dual = frozenset(frozenset(x) for x in bycoord.values())
    if len(physical_dual) != 6:
        return None, None
    return kind, physical_dual


def _connected_position_cycle(dual):
    if len(dual) != 6:
        return False
    graph = {}
    for x in dual:
        a, b = tuple(x)
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)
    seen = set()
    stack = [next(iter(graph))]
    while stack:
        x = stack.pop()
        if x not in seen:
            seen.add(x)
            stack.extend(graph[x] - seen)
    return len(seen) == 6


def local_original_seven_tag(model, six_original_ids):
    """Independent definition-level ORIGINAL Q evaluator; no 62k join.

    Physical A/B/C half tests and AA positional six-cycle are all
    recomputed directly from one globally coherent input pair-map.
    """
    _, _, incset = _valid_original_model(model)
    inc = tuple(model["incidences"])
    Q = tuple(six_original_ids)
    if len(Q) != 6 or len(set(Q)) != 6 or any(
        type(i) is not int or not 0 <= i < len(inc) for i in Q
    ):
        raise ValueError("six DIFFERENT actual original source-incidence IDs required")
    lk, ld = _six_physical_projection(Q, inc, model["left_labels"], 0)
    rk, rd = _six_physical_projection(Q, inc, model["right_labels"], 1)
    if lk is None or rk is None:
        return None
    if lk == "A" and rk == "A":
        return "D6" if ld == rd and _connected_position_cycle(ld) else None
    if lk == "B" and rk == "A":
        return "B-left/A-right"
    if lk == "A" and rk == "B":
        return "A-left/B-right"
    if {lk, rk} == {"A", "C"}:
        return "C/A"
    if {lk, rk} == {"B", "C"}:
        return "C/B"
    if lk == rk == "B":
        pc = Counter(inc[i][0] for i in Q)
        lc = Counter(inc[i][1] for i in Q)
        repeated_p = next(x for x, c in pc.items() if c == 2)
        repeated_l = next(x for x, c in lc.items() if c == 2)
        overlap = any(inc[i] == (repeated_p, repeated_l) for i in Q)
        return "B/B-overlap" if overlap else "B/B-disjoint"
    if lk == rk == "C":
        raise AssertionError("GQ source girth eight forbids original C/C")
    return None


def translate_six_original_ids(model, Q, p_sources, l_sources):
    """Transport TRUE Q under one common source incidence automorphism."""
    _, _, inc = _valid_original_model(model)
    v = parameters(model["s"])["V"]
    p = _permutation(p_sources, v, "point source")
    l = _permutation(l_sources, v, "line source")
    if {(p[x], l[y]) for x, y in inc} != inc:
        raise ValueError("source transport requires actual GQ automorphism")
    original = tuple(model["incidences"])
    inverse = {edge: i for i, edge in enumerate(original)}
    if len(set(Q)) != 6 or len(tuple(Q)) != 6:
        raise ValueError("six distinct original incidence indices")
    return tuple(sorted(inverse[(p[original[i][0]], l[original[i][1]])]
                        for i in Q))


def normalized_search_cardinality(s):
    """Exact anchored assignments only; NOT a quotient by all stabilizers."""
    par = parameters(s)
    k, v = par["K"], par["V"]
    if v > k:
        raise AssertionError("not enough physical pair labels")
    per_side = prod(range(k-v+1, k))  # (K-1)! / (K-V)!
    return {"s": s, "V": v, "K": k,
            "unanchored_per_side": k*per_side,
            "anchored_per_side": per_side,
            "two_sided_exact_search_reduction_factor": k*k,
            "anchored_both_side_candidate_count": per_side**2,
            "still_astronomical_not_full_minimax_enumeration": True,
            "all_h_exact_anchor_normal_form": True,
            "root_A_proved": False, "root_B_proved": False,
            "root_C_closed": False}


def finite_W32_symmetry_certificate(scheme="S68"):
    """Exact TRUE W32 seven-vector test using existing independently built join."""
    from hyp105_issue230_projection import fixture
    from hyp105_issue230_d6aa4q_two_sided_seven_join import (
        exact_two_sided_original_seven_join,
    )
    original = fixture(1, scheme)
    p, l = symplectic_transvection_source(original, 4)
    transformed = transform_model(
        original, point_sources=p, line_sources=l,
        point_coordinates=tuple(reversed(range(6))),
        line_coordinates=(1, 2, 3, 4, 5, 0))
    normal = anchored_pair_normal_form(transformed, 3, 7)
    base = exact_two_sided_original_seven_join(original, independent_history=False)
    changed = exact_two_sided_original_seven_join(normal, independent_history=False)
    keys = ("accepted_seven_GF5_original_Q_by_tag",
            "accepted_seven_GF5_original_S",
            "selected_GF5_51palette_certified_numerator",
            "physical_A_A_genuine_D6_only",
            "exact_source_original_Q_double_projection_intersection")
    if any(base[k] != changed[k] for k in keys):
        raise AssertionError("original same-Q seven-GF5 orbit-invariance FAILED")
    # The full-mode scalar polynomial would be invalid if ANY selected
    # historical GF5 risk weight changed under these permutations.
    assert set(base["accepted_seven_GF5_original_Q_by_tag"]) == set(R3_CERTIFIED_FLOORS)
    return {"scheme": scheme, "s": 2, "source_points": 15, "source_lines": 15,
            "original_Q_count": 45, "all_seven_GF5_tags":base[keys[0]],
            "S": base[keys[1]],
            "historical_51_palette_weighted_numerator": base[keys[2]],
            "D6": base[keys[3]],
            "transformed_with_actual_original_Sp4_source_automorphism": True,
            "two_independent_physical_coordinate_permutations": True,
            "anchored_point_source": 3, "anchored_line_source": 7,
            "true_original_global_coherence_checked": True,
            "root_230_remains_open": True}


if __name__ == "__main__":
    import json
    print(json.dumps({"normal_form_sizes":[normalized_search_cardinality(s)
                      for s in (2,4,8)], "finite_true_W32":
                      finite_W32_symmetry_certificate()},indent=2,sort_keys=True))
