"""AA4-CT: complete physical K_a minus <a holes forces C4 reservoirs.

This controls TWO *physical* occupied-C4 conditions in AA4-CR for
many genuine original P3 anchors. It never asserts any actual GQ 3x3
matching, six-original-flag GF(5) acceptance, or Root #230 Branch A.
"""
from itertools import combinations
from math import comb

from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import original_nonincident_threepath
from hyp105_issue230_d6aa4cs_uniform_disjoint_original_source_cut import (
    dyadic_all_h_disjoint_macro_arithmetic,
)


def physical_graph(labels, a):
    """Entire occupied typed image, holes, and physical hole degrees."""
    if type(a) is not int or a < 4:
        raise ValueError("physical alphabet must contain at least four coordinates")
    edges = set()
    for pair in labels:
        pair = tuple(pair)
        if (len(pair) != 2 or any(type(v) is not int or not 0 <= v < a for v in pair)
                or pair[0] == pair[1]):
            raise ValueError("each physical image must be a simple coordinate pair")
        edge = frozenset(pair)
        if edge in edges:
            raise ValueError("global factor-image injection required")
        edges.add(edge)
    holes = frozenset(frozenset((u, v)) for u in range(a)
                      for v in range(u + 1, a)
                      if frozenset((u, v)) not in edges)
    degree = tuple(sum(v in edge for edge in holes) for v in range(a))
    return edges, holes, degree


def c4_count_via_holes(single, doubled, edges, holes, a):
    """Exact occupied ordered (z,w) C4 completion count, WITHOUT GQ matching.

    Independent from the older C4 triple-enumerator: use a bipartite
    A x B potential pair count minus the forbidden diagonal and the
    internal absent physical edges. The doubled edge is excluded.
    """
    e, d = frozenset(single), frozenset(doubled)
    if (len(e) != 2 or len(d) != 2 or not e.isdisjoint(d)
            or e not in edges or d not in edges):
        raise ValueError("occupied disjoint original single/doubled images required")
    if not e | d <= set(range(a)):
        raise ValueError("coordinates outside physical K_a")
    u, v = sorted(e)
    free = set(range(a)) - e - d
    aa = {z for z in free if frozenset((u, z)) in edges}
    bb = {w for w in free if frozenset((v, w)) in edges}
    internal_absent = 0
    for hole in holes:
        if hole <= free:
            z, w = tuple(hole)
            internal_absent += (z in aa and w in bb) + (w in aa and z in bb)
    exact = len(aa) * len(bb) - len(aa & bb) - internal_absent
    if exact < 0:
        raise AssertionError("invalid hole complement inclusion-exclusion")
    return exact


def dense_side_certificate(single, doubled, edges, holes, degrees, a):
    """Physical lemma; if a>=16 and single avoids heavy, C4>=N/2."""
    n = a - 4
    N = n * (n - 1)
    H = len(holes)
    if H > a - 2:
        raise ValueError("image is not a minimal K_a factor labeling")
    if len(edges) + H != comb(a, 2):
        raise AssertionError("complete physical edge/holes partition invalid")
    e = frozenset(single)
    count = c4_count_via_holes(single, doubled, edges, holes, a)
    hole_upper = (sum(degrees[v] for v in e) * (n - 1) + 2 * H)
    no_heavy = all(16 * degrees[v] < a for v in e)
    if count < N - hole_upper:
        raise AssertionError("missing physical edge template charging violated")
    if a >= 16 and no_heavy and 2 * count < N:
        raise AssertionError("uniform dense physical C4 completion lemma violated")
    return {"occupied_C4_source_triples": count, "full_C4_templates": N,
            "hole_charging_lower": max(0, N - hole_upper),
            "single_endpoint_no_heavy": no_heavy}


def all_h_dense_c4_arithmetic(h):
    """Check all integer parameters; infinite proof is in AA4-CT Markdown."""
    z = dyadic_all_h_disjoint_macro_arithmetic(h)
    a, m, V, s = z["a"], z["m"], z["V"], z["s"]
    B = 32 * (a - 1)
    N = (a - 4) * (a - 5)
    if h >= 14:
        if not (a >= 16 and m >= 8 * B and 8 * m >= V
                and m >= 2 * (s + 1) + 8 * (a - 2) * s
                and N >= 0 and 8 * (a - 2) <= N):
            raise AssertionError("AA4-CT universal all-h numeric sufficient gate failed")
        if m * m * 256 < V * V:
            raise AssertionError("AA4-CT cut count arithmetic violated")
    return {"h": h, "s": s, "V": V, "a": a, "m": m,
            "max_heavy_occupied_endpoint_edges_per_typed_map": B,
            "C4_templates_per_disjoint_original_anchor_side": N,
            "guarantee_for_all_h_ge_14": h >= 14,
            "root_230": "OPEN_WITH_FORMAL_BLOCKER"}


def original_cut_dense_c4_certificate(model, X=None, Y=None, sample_limit=12):
    """Count true ORIGINAL P3 anchors surviving double disjointness/heavy cuts.

    Sample C4 counts are finite falsifiers only; NO original permanent=1
    is implied by arbitrarily large physical completion pair counts.
    """
    s, V, a, f, g, pl, lp = _validated_original(model)
    if type(sample_limit) is not int or sample_limit < 0:
        raise ValueError("nonnegative exact integer sample size required")
    k = a // 2
    X = tuple(range(k)) if X is None else tuple(X)
    Y = tuple(range(a-k, a)) if Y is None else tuple(Y)
    for cut in (X, Y):
        if (len(cut) != k or len(set(cut)) != k or
                any(type(v) is not int or not 0 <= v < a for v in cut)):
            raise ValueError("valid half-coordinate physical cuts required")
    xf, yg = frozenset(X), frozenset(Y)
    point_graph = physical_graph(f, a)
    line_graph = physical_graph(g, a)
    heaviest_p = frozenset(v for v,deg in enumerate(point_graph[2]) if 16*deg >= a)
    heaviest_l = frozenset(v for v,deg in enumerate(line_graph[2]) if 16*deg >= a)
    # Two independent physical hole-count bounds (typed maps can correlate).
    for graph, heavy in ((point_graph, heaviest_p), (line_graph, heaviest_l)):
        if len(graph[1]) > a - 2 or len(heavy) > 31:
            raise AssertionError("minimal physical K_a hole/exception bound false")
    P = tuple(p for p in range(V) if frozenset(f[p]) <= xf)
    L = tuple(l for l in range(V) if frozenset(g[l]) <= yg)
    excluded_P = sum(bool(frozenset(f[p]) & heaviest_p) for p in P)
    excluded_L = sum(bool(frozenset(g[l]) & heaviest_l) for l in L)
    B = 32 * (a - 1)
    if excluded_P > B or excluded_L > B:
        raise AssertionError("typed source endpoint exceptional charging false")
    T = good = retained = 0
    examples = []
    for p in P:
        for l in L:
            if l in pl[p]:
                continue
            T += 1
            source = original_nonincident_threepath(p, l, pl, lp)
            q, l0 = source[1][0], source[0][1]
            if set(f[p]) & set(f[q]) or set(g[l]) & set(g[l0]):
                continue
            good += 1
            if frozenset(f[p]) & heaviest_p or frozenset(g[l]) & heaviest_l:
                continue
            retained += 1
            if len(examples) < sample_limit:
                left = dense_side_certificate(f[p], f[q], *point_graph, a)
                right = dense_side_certificate(g[l], g[l0], *line_graph, a)
                examples.append(((p, l, q, l0), left, right))
    if retained > good or retained < good - B * (len(P) + len(L)):
        raise AssertionError("exceptional true original GQ threepath charge violated")
    if s >= (1 << 14):
        z = all_h_dense_c4_arithmetic(s.bit_length()-1)
        if (4 * retained < len(P) * len(L) or
                256 * retained < V * V or
                8 * z["m"] < z["V"]):
            raise AssertionError("all-h genuine original P3+C4 reservoir bound violated")
    return {"s": s, "V": V, "a": a, "source_X": len(P), "source_Y": len(L),
            "true_original_P3_cut": T,
            "double_disjoint_P3": good,
            "double_disjoint_nonheavy_P3": retained,
            "point_holes": len(point_graph[1]), "line_holes": len(line_graph[1]),
            "point_heavy_vertices": len(heaviest_p),
            "line_heavy_vertices": len(heaviest_l),
            "exceptional_point_source_endpoints": excluded_P,
            "exceptional_line_source_endpoints": excluded_L,
            "C4_samples_original_p_l_q_l0_left_right": tuple(examples),
            "true_original_3x3_matching_UNPROVED": True,
            "root_230": "OPEN_WITH_FORMAL_BLOCKER"}
