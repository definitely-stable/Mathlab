"""AA4-CQ: all-h genuine-GQ path-cut transfer gate; NOT a seven-GF5 lower.

A genuine symplectic W(3,s) has exactly one simple original incidence
3-path between each NONINCIDENT original point and original line.
This is a source substrate, not a six-distinct-incidence positive GF5 Q.
"""
from math import comb

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source


def _validated_original(model):
    s, V, a, incidences, f, g, _, _ = _original_source(model)
    if s < 2 or s & (s - 1) or V != (s + 1) * (s * s + 1):
        raise ValueError("expected genuine dyadic symplectic W(3,s) parameters")
    if len(f) != V or len(g) != V or comb(a, 2) < V or (a > 2 and comb(a - 1, 2) >= V):
        raise ValueError("bad complete minimal physical pair alphabet")
    def edges(labels):
        out = []
        for pair in labels:
            if len(pair) != 2:
                raise ValueError("physical source factor image must be an unordered pair")
            u, v = pair
            if not (isinstance(u, int) and isinstance(v, int) and 0 <= u < v < a):
                raise ValueError("invalid physical source factor image")
            out.append((u, v))
        if len(set(out)) != V:
            raise ValueError("global typed injection violated")
        return tuple(out)
    f, g = edges(f), edges(g)
    if len(incidences) != V * (s + 1):
        raise ValueError("wrong genuine source flag count")
    point_lines = [set() for _ in range(V)]
    line_points = [set() for _ in range(V)]
    seen = set()
    for p, l in incidences:
        if not (0 <= p < V and 0 <= l < V) or (p, l) in seen:
            raise ValueError("repeated or out-of-range ORIGINAL flag")
        seen.add((p, l))
        point_lines[p].add(l)
        line_points[l].add(p)
    if any(len(x) != s + 1 for x in point_lines + line_points):
        raise ValueError("original symplectic incidence degree mismatch")
    return s, V, a, f, g, tuple(map(frozenset, point_lines)), tuple(map(frozenset, line_points))


def explicit_three_walks(p, l, point_lines, line_points):
    """Independently count actual 3-edge incidence WALKS p--l0--q--l.

    For NONINCIDENT endpoints every walk is the unique SIMPLE 3-path.
    For INCIDENT endpoints all 2s+1 walks backtrack (girth eight).
    """
    return sum(1 for l0 in point_lines[p]
               for q in line_points[l0] if l in point_lines[q])


def macro_path_cut(model, point_coordinates=None, line_coordinates=None):
    """Return a fully fixed ORIGINAL f,g path-cut certificate.

    The two physical coordinate subsets are GLOBAL, never redrawn by Q.
    For s>=8 and ANY two floor(a/2)-coordinate subsets the source 3-path
    count is at least V^2/128 > s^6/128. No R3/S_s claim follows.
    """
    s, V, a, f, g, point_lines, line_points = _validated_original(model)
    k = a // 2
    X = frozenset(range(k) if point_coordinates is None else point_coordinates)
    Y = frozenset(range(a - k, a) if line_coordinates is None else line_coordinates)
    if len(X) != k or len(Y) != k or not X.issubset(range(a)) or not Y.issubset(range(a)):
        raise ValueError("each coordinate cut must have floor(a/2) distinct valid symbols")
    P = tuple(p for p, e in enumerate(f) if set(e) <= X)
    L = tuple(l for l, e in enumerate(g) if set(e) <= Y)
    L_set = set(L)
    e_PL = sum(len(point_lines[p] & L_set) for p in P)
    nonincident = len(P) * len(L) - e_PL
    # Second independent arithmetic oracle, transposed ORIGINAL incidence traversal.
    e_transpose = sum(len(line_points[l] & set(P)) for l in L)
    if e_transpose != e_PL:
        raise AssertionError("original incidence endpoints transposition mismatch")
    K = comb(a, 2)
    H = K - V
    m = max(0, comb(k, 2) - H)
    if not (len(P) >= m and len(L) >= m and nonincident >= 0):
        raise AssertionError("occupied global map edge/hole invariant failed")
    macro_gate = s >= 8
    if macro_gate:
        if not (a >= 22 and m >= V / 8 and V >= 16 * (s + 1)):
            raise AssertionError("all-h arithmetic macro gate not established")
        if nonincident * 128 < V * V:
            raise AssertionError("original 3-path uniform c=1/128 lower falsified")
    # A six-coordinate palette has at most C(6,2)=15 occupied source
    # factor images per side. For s>=4, spectral mixing alone has
    # nonpositive lower for the incidence count on EVERY such pair.
    micro_spectral_gate = s >= 4 and 2 * s * (V - 15) ** 2 >= 225 * (s + 1) ** 2
    if s >= 4 and not micro_spectral_gate:
        raise AssertionError("six-palette expander-mixing no-go threshold failed")
    return {
        "s": s, "V": V, "a": a, "k": k, "holes": H, "m_min_cut_factor_images": m,
        "P_original_point_factor_ids": P, "L_original_line_factor_ids": L,
        "point_cut_size": len(P), "line_cut_size": len(L),
        "original_flag_edges_between_cuts": e_PL,
        "unique_original_simple_3path_count": nonincident,
        "direct_nonincidence_pair_count": sum(
            l not in point_lines[p] for p in P for l in L),
        "macro_s6_gate": macro_gate,
        "macro_lower_numerator_V2_over_128": V * V,
        "micro_six_palette_second_moment_floor_nonpositive": micro_spectral_gate,
        "root_status": "OPEN_WITH_FORMAL_BLOCKER",
        "count_is_positive_GF5_sixflag": False,
    }
