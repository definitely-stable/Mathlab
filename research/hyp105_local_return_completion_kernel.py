"""HYP-105 #230 AA4-COMP: exact physical returning-wedge C6 completion kernel.

The ALL-h lemma holds for ANY simple graph. In the genuine original
symplectic W(3,s) physical-corner model, every physical arc is also
verified to carry exactly one TRUE original point-line incidence ID.

For a fixed simple physical wedge a-b-c with a,c sharing one physical
coordinate and S={a,b,c}:
 comp6(a,b,c) =
 sum_{u in N(c)\S} sum_{w in N(a)\S, w != u}
        |N(u) intersect N(w) \ S|.
Every term represents the unique simple C6
a-b-c-u-v-w-a, for v a common neighbor of u,w outside S.

No all-h comp=O(s) bound (pointwise OR in average) is claimed.
Finite W(3,2), W(3,4) oracle uses complete globally injected typed
maps; source labels may be arbitrarily correlated.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations

from hyp105_b1_symplectic import symplectic_gq
from hyp105_physical_rainbow_c6 import build_original_physical_graph
from hyp105_original_source_pencil_wedges import original_source_pencil_wedges


def returning_wedge_completion_kernel(adjacency, a, b, c):
    """Exact number of simple 6cycle completions of this UNORIENTED wedge.

    a and c are interchangeable. The physical graph has no loops or
    multiedges, all 3 wedge corners are DISTINCT, with a-b and b-c edges.
    This routine avoids enumerating simple six-cycles and uses only
    2-hop common-neighbor intersections with the three forbidden corners.
    """
    if a == b or b == c or a == c:
        raise ValueError("three distinct physical wedge corners required")
    if b not in adjacency.get(a, ()) or c not in adjacency.get(b, ()):
        raise ValueError("two genuine physical wedge edges required")
    if ((a[0] == c[0]) == (a[1] == c[1])):
        raise ValueError("wedge must return on exactly one coordinate axis")
    excluded = frozenset((a, b, c))
    left = adjacency[c].difference(excluded)
    right = adjacency[a].difference(excluded)
    n = 0
    for u in left:
        for w in right:
            if u == w:
                continue
            n += len((adjacency[u] & adjacency[w]) - excluded)
    return n


def independent_four_path_dfs(adjacency, a, b, c):
    """Second implementation: enumerate actual ordered 4-edge paths c->a.

    This does not use common-neighbor intersections and must match the
    sparse completion kernel. Intended for independent finite tests.
    """
    if a == b or b == c or a == c or (
            b not in adjacency.get(a, ()) or
            c not in adjacency.get(b, ())):
        raise ValueError("true physical wedge required")
    if ((a[0] == c[0]) == (a[1] == c[1])):
        raise ValueError("returning coordinate wedge required")
    forbidden = frozenset((a, b, c))
    n = 0
    for u in adjacency[c] - forbidden:
        for v in adjacency[u] - forbidden - {u}:
            for w in adjacency[v] - forbidden - {u, v}:
                if w in adjacency[a]:
                    n += 1
    return n


def original_wedge_completion_profile(power, f, g,
                                      *, verify_independent_c6=True):
    """Complete true-original W32/W34 profile, including full weighted moments.

    Expensive exact physical-graph and true-source oracles h=1,2 only.
    Every wedge is identified by a physical middle corner and unordered
    endpoint pair; each returning wedge is enumerated exactly once.
    """
    if type(power) is not int or power not in (1, 2):
        raise ValueError("exact finite completion profile limited to h=1,2")
    s = 1 << power
    _,points,lines,flags = symplectic_gq(power)
    v_expected = (s+1)*(s*s+1)
    if len(points) != v_expected or len(lines) != v_expected:
        raise AssertionError("not true symplectic W(3,s)")
    f, g = tuple(map(tuple, f)), tuple(map(tuple, g))
    graph, source_arc = build_original_physical_graph(s, f, g, flags)
    totals = Counter()
    maxima = {"x": 0, "y": 0}
    maximizers = {"x": None, "y": None}
    visited_samples = {"x": 0, "y": 0}
    nonzero = {"x": 0, "y": 0}

    for b, neighbors in graph.items():
        for axis in ("x", "y"):
            groups = defaultdict(list)
            k = 0 if axis == "x" else 1
            for q in neighbors:
                groups[q[k]].append(q)
            for endpoints in groups.values():
                for a, c in combinations(sorted(endpoints), 2):
                    if ((a[0] == c[0]) == (a[1] == c[1])):
                        raise AssertionError("returning wedge must share exactly one coordinate")
                    left_flag = flags[source_arc[a,b]]
                    right_flag = flags[source_arc[b,c]]
                    if axis == "x":
                        if (left_flag[0] != right_flag[0] or
                                left_flag[1] == right_flag[1]):
                            raise AssertionError("x wedge must share original point, not line")
                    else:
                        if (left_flag[1] != right_flag[1] or
                                left_flag[0] == right_flag[0]):
                            raise AssertionError("y wedge must share original line, not point")
                    comp = returning_wedge_completion_kernel(graph,a,b,c)
                    totals["J_"+axis] += 1
                    totals["W2_"+axis] += comp
                    totals["Qcomp_"+axis] += comp * comp
                    nonzero[axis] += comp > 0
                    if comp > maxima[axis]:
                        maxima[axis] = comp
                        maximizers[axis] = {
                            "three_physical_corners": (a,b,c),
                            "two_genuine_source_flag_ids": (
                                source_arc[a,b],source_arc[b,c]
                            ),
                            "two_original_source_flags": (
                                left_flag,right_flag
                            ),
                        }
                    # Complete alternative DFS on ALL W32 wedges, and at
                    # least 12 canonical W34 samples per axis, INCLUDING
                    # each newly found maximum.
                    if power == 1 or visited_samples[axis] < 12 or comp == maxima[axis]:
                        if independent_four_path_dfs(graph,a,b,c) != comp:
                            raise AssertionError("independent 4-edge path DFS disagrees")
                        visited_samples[axis] += 1

    original = original_source_pencil_wedges(
        s,f,g,flags,check_physical_independently=True
    )
    if ((totals["J_x"],totals["J_y"]) != (
            original["Jx_point_pencil_two_edge_wedges"],
            original["Jy_line_pencil_two_edge_wedges"])):
        raise AssertionError("pencil-incidence wedge oracle disagrees")
    if verify_independent_c6:
        from hyp105_local_coordinate_return_c6 import original_coordinate_return_census
        independent = original_coordinate_return_census(
            power,f,g,check_independent=True)
        freq = independent["return_signature_counts"]
        x_sum = sum(int(signature.split(",")[0]) * count
                    for signature,count in freq.items())
        y_sum = sum(int(signature.split(",")[2]) * count
                    for signature,count in freq.items())
        if (totals["W2_x"],totals["W2_y"]) != (x_sum,y_sum):
            raise AssertionError("independent ALL-physical-C6 return census disagrees")
    if totals["J_x"] <= 0 or totals["J_y"] <= 0:
        raise AssertionError("verified finite certificate unexpectedly has no returning wedges")
    return {
        "s":s,
        "J_x":totals["J_x"],"J_y":totals["J_y"],
        "W2_x":totals["W2_x"],"W2_y":totals["W2_y"],
        "max_completion_x":maxima["x"],
        "max_completion_y":maxima["y"],
        "sum_squared_completion_x":totals["Qcomp_x"],
        "sum_squared_completion_y":totals["Qcomp_y"],
        "nonzero_completion_wedges_x":nonzero["x"],
        "nonzero_completion_wedges_y":nonzero["y"],
        "mean_completion_x":str(Fraction(totals["W2_x"],totals["J_x"])),
        "mean_completion_y":str(Fraction(totals["W2_y"],totals["J_y"])),
        "maximizer_x":maximizers["x"],
        "maximizer_y":maximizers["y"],
        "independent_sample_checks":dict(visited_samples),
        "all_h_kernel_identity_proved":True,
        "all_h_uniform_O_s_completion_proved":False,
        "all_h_average_O_s_completion_proved":False,
        "root_sevenclass_proved":False,
    }
