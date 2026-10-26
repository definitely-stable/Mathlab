"""HYP-105 #230 AA4-RC6: physical rainbow six-cycle = ORIGINAL accepted D6.

ALL-h identity for arbitrary complete typed globally injected f/g on genuine
symplectic W(3,2^h). Executable independent source-ID C6 oracle h=1,2 only.

This is a D6-only bridge and squarefree adjacency trace, not the seven-class
original-sixset obstruction or an all-h sixth-order lower bound.
"""
from collections import Counter, defaultdict

from hyp105_b1_symplectic import symplectic_gq
from hyp105_physical_degree_energy import (
    minimal_alphabet, _verified_source, _verify_typed_injections,
)


def build_original_physical_graph(s, f, g, flags):
    """Build physical H *from genuine original flags* and retain arc source IDs.

    The factor injections imply every physical undirected edge has exactly
    one original source incidence ID: never silently collapse multiedges.
    """
    if type(s) is not int or s < 2 or s & (s - 1):
        raise ValueError("dyadic s>=2 required")
    V = (s + 1)*(s*s + 1)
    a = minimal_alphabet(V)
    _verify_typed_injections(a, V, f, g)
    _verified_source(s, flags, V)
    adjacency = defaultdict(set)
    arc_flag = {}
    for colid, (p, l) in enumerate(flags):
        u, v = f[p]
        x, y = g[l]
        for z, w in (((u,x),(v,y)), ((u,y),(v,x))):
            if (z,w) in arc_flag or (w,z) in arc_flag:
                raise AssertionError("two original flags share one physical edge")
            arc_flag[z,w] = colid
            arc_flag[w,z] = colid
            adjacency[z].add(w)
            adjacency[w].add(z)
    if len(arc_flag) != 4*V*(s+1):
        raise AssertionError("original flag to physical edge count changed")
    if any(z == w for z, others in adjacency.items() for w in others):
        raise AssertionError("physical graph must be loopless")
    return {v: frozenset(neighbors) for v, neighbors in adjacency.items()}, arc_flag


def exact_rainbow_c6_finite(power, f, g, *, verify_GF5=True):
    """Count each simple undirected physical C6 exactly once, then D6 once.

    Canonical cycles: first corner is least; second corner < final corner.
    For each rainbow candidate recover the true source six ORIGINAL flag
    IDs and compare with the immutable seven-family GF5 D6 classifier.
    This is independent of the left K_a six-cycle / right incidence join
    enumerator and does NOT enumerate all 6-subsets of source flags.
    """
    if type(power) is not int or power not in (1,2):
        raise ValueError("finite physical six-cycle oracle supports h=1,2")
    s = 1 << power
    _,points,lines,flags = symplectic_gq(power)
    V = (s+1)*(s*s+1)
    if len(points) != V or len(lines) != V:
        raise AssertionError("non-genuine symplectic geometry")
    f = tuple(map(tuple,f))
    g = tuple(map(tuple,g))
    adjacency, arc_flag = build_original_physical_graph(s,f,g,flags)
    a = minimal_alphabet(V)
    vertices = sorted(adjacency)
    # Physical H can contain triangles, notwithstanding SOURCE girth eight.
    triangles = sum(
        v in adjacency[w]
        for i,u in enumerate(vertices)
        for v in adjacency[u] if u < v
        for w in adjacency[v] if v < w
        if w in adjacency and u in adjacency[w]
    )
    # Triangle count above deliberately traverses u<v<w once; its
    # extra membership check is harmless and enforces closure.
    counts = Counter()
    seen_six = set()
    if verify_GF5:
        from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
    used = set()
    path = []

    def visit(root, last):
        if len(path) == 6:
            if root not in adjacency[last] or path[1] >= last:
                return
            counts["physical_C6"] += 1
            unique_x = len({v[0] for v in path}) == 6
            unique_y = len({v[1] for v in path}) == 6
            counts["x_injective_C6"] += unique_x
            counts["y_injective_C6"] += unique_y
            if not (unique_x and unique_y):
                counts["defect_C6"] += 1
                if not unique_x and not unique_y:
                    counts["both_coord_repeat_C6"] += 1
                elif not unique_x:
                    counts["x_only_repeat_C6"] += 1
                else:
                    counts["y_only_repeat_C6"] += 1
                return
            ids = tuple(sorted(
                arc_flag[path[i],path[(i+1) % 6]] for i in range(6)
            ))
            if len(set(ids)) != 6:
                raise AssertionError("rainbow C6 repeats an original flag ID")
            if (len({flags[k][0] for k in ids}) != 6 or
                    len({flags[k][1] for k in ids}) != 6):
                raise AssertionError("rainbow C6 not an original factor matching")
            if ids in seen_six:
                raise AssertionError("one ORIGINAL sixset realized twice in physical H")
            seen_six.add(ids)
            if verify_GF5 and classify_seven_prechecked(ids,f,g,flags) != "D6":
                raise AssertionError("original sixset not accepted GF5 D6")
            counts["D6_rainbow_C6"] += 1
            return
        for nxt in sorted(adjacency[last]):
            if nxt <= root or nxt in used:
                continue
            used.add(nxt)
            path.append(nxt)
            visit(root,nxt)
            path.pop()
            used.remove(nxt)

    for root in vertices:
        path.append(root)
        used.add(root)
        visit(root,root)
        used.remove(root)
        path.pop()
    total = counts["physical_C6"]
    if (total != counts["D6_rainbow_C6"]+counts["defect_C6"] or
            counts["defect_C6"] !=
            counts["x_only_repeat_C6"]+counts["y_only_repeat_C6"]+
            counts["both_coord_repeat_C6"] or
            counts["x_injective_C6"]+counts["y_injective_C6"]-
            counts["D6_rainbow_C6"]+counts["both_coord_repeat_C6"] != total):
        raise AssertionError("rainbow/nonrainbow six-cycle partition failed")
    return {
        "s":s,"V":V,"a":a,
        "original_source_flags":len(flags),
        "physical_undirected_edges":len(arc_flag)//2,
        "physical_triangles":triangles,
        "physical_simple_C6":total,
        "D6_original_sixsets":counts["D6_rainbow_C6"],
        "nonrainbow_coordinate_defect":counts["defect_C6"],
        "x_distinct_physical_C6":counts["x_injective_C6"],
        "y_distinct_physical_C6":counts["y_injective_C6"],
        "x_only_repeat_C6":counts["x_only_repeat_C6"],
        "y_only_repeat_C6":counts["y_only_repeat_C6"],
        "both_repeat_C6":counts["both_coord_repeat_C6"],
        "exact_12D6_squarefree_physical_closed_walks":
            12*counts["D6_rainbow_C6"],
        "GF5_source_classifier_checked":verify_GF5,
        "universal_D6_Omega_s6_proved":False,
        "all_seven_GF5_sixclass_lower_proved":False,
    }
