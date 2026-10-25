"""HYP-105 #230 D6-AA: exact six-incidence positional collision signatures.

All-h LOCAL factorization for arbitrary complete typed injective pair maps.
No GF5 flow algorithm or legacy seven-class classifier is used here.
"""
from collections import Counter
from itertools import combinations, combinations_with_replacement
from math import comb

WEIGHTS = {
    "D6": 5643,
    "B-left/A-right": 45600,
    "A-left/B-right": 45600,
    "C/A": 43320,
    "C/B": 49050,
    "B/B-overlap": 51750,
    "B/B-disjoint": 45010,
}
POSITIONS = tuple(range(6))
POSITION_PAIRS = tuple(combinations(POSITIONS, 2))


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def normalized_edge(edge):
    if (len(edge) != 2 or any(type(x) is not int or x < 0 for x in edge)
            or edge[0] == edge[1]):
        raise ValueError("each physical image is a pair of distinct nonnegative coordinates")
    return tuple(sorted(edge))


def local_signature(six_pairs):
    """15 indexed pair intersections, W2, W3, and position graph if 2-regular.

    Six positions are NEVER collapsed even when the physical pair repeats.
    A genuine 2-regular coordinate is an edge between its two occurrence
    positions, including multiplicity 2 between a pair of positions.
    """
    if len(six_pairs) != 6:
        raise ValueError("exactly six ORIGINAL incidence positions required")
    pairs = tuple(normalized_edge(p) for p in six_pairs)
    positions_by_coord = {}
    for i, pair in enumerate(pairs):
        for coord in pair:
            positions_by_coord.setdefault(coord, []).append(i)
    w2 = sum(choose(len(rows), 2) for rows in positions_by_coord.values())
    w3 = sum(choose(len(rows), 3) for rows in positions_by_coord.values())
    intersections = tuple(len(set(pairs[i]) & set(pairs[j]))
                          for i, j in POSITION_PAIRS)
    if w2 != sum(intersections):
        raise AssertionError("wedge and pairwise-column intersection identities disagree")
    regular = w2 == 6 and w3 == 0
    graph = None
    kind = None
    connected = False
    doubles = ()
    if regular:
        graph = tuple(sorted(tuple(sorted(rows)) for rows in positions_by_coord.values()))
        if len(graph) != 6 or any(len(edge) != 2 for edge in graph):
            raise AssertionError("W2=6 and W3=0 must force six degree-two coordinates")
        multi = Counter(graph)
        doubles = tuple(sorted(edge for edge, n in multi.items() if n == 2))
        if any(n > 2 for n in multi.values()):
            raise AssertionError("invalid physical pair multiplicity")
        if len(doubles) == 0:
            kind = "A"
        elif len(doubles) == 1:
            kind = "B"
        elif len(doubles) == 3:
            kind = "C"
        else:
            raise AssertionError("unexpected 2-regular multigraph on six positions")
        seen = {0}
        todo = [0]
        while todo:
            i = todo.pop()
            for a, b in graph:
                if a == i and b not in seen:
                    seen.add(b)
                    todo.append(b)
                elif b == i and a not in seen:
                    seen.add(a)
                    todo.append(a)
        connected = len(seen) == 6
    return {
        "pair_intersections": intersections,
        "W2": w2,
        "W3": w3,
        "regular": regular,
        "position_graph": graph,
        "kind": kind,
        "connected": connected,
        "doubled_positions": doubles,
    }


def classify_position_signatures(left, right):
    """Pure finite Phi; accepted seven classes only, never total GF5 R3."""
    if not left["regular"] or not right["regular"]:
        return None
    a, b = left["kind"], right["kind"]
    if a == b == "A":
        if (left["connected"] and right["connected"]
                and left["position_graph"] == right["position_graph"]):
            return "D6"
        return None
    if (a, b) == ("B", "A"):
        return "B-left/A-right"
    if (a, b) == ("A", "B"):
        return "A-left/B-right"
    if {a, b} == {"C", "A"}:
        return "C/A"
    if {a, b} == {"C", "B"}:
        return "C/B"
    if (a, b) == ("B", "B"):
        overlap = len(set(left["doubled_positions"][0])
                      & set(right["doubled_positions"][0]))
        if overlap == 1:
            return "B/B-overlap"
        if overlap == 0:
            return "B/B-disjoint"
        # Two equal ORIGINAL endpoint pairs would duplicate an incidence.
        return None
    # C/C cannot be realized by six distinct edges in a girth-eight host.
    return None


def classify_original_six(original_six, left_labels, right_labels):
    """Factorization using the ACTUAL six DISTINCT ORIGINAL point-line rows."""
    six = tuple(tuple(row) for row in original_six)
    if (len(six) != 6 or len(set(six)) != 6
            or any(len(row) != 2 or any(type(t) is not int or t < 0 for t in row)
                   for row in six)):
        raise ValueError("six distinct ORIGINAL (point,line) incidences required")
    if any(p >= len(left_labels) or l >= len(right_labels) for p, l in six):
        raise ValueError("original factor outside complete typed labels")
    ls = local_signature(tuple(left_labels[p] for p, _ in six))
    rs = local_signature(tuple(right_labels[l] for _, l in six))
    return classify_position_signatures(ls, rs)


def enumerate_position_graphs():
    """Independent multigraph enumeration: 15 six-position edges, with repeats."""
    counts = Counter()
    graphs = set()
    for six_edges in combinations_with_replacement(POSITION_PAIRS, 6):
        deg = Counter(vertex for edge in six_edges for vertex in edge)
        if all(deg[i] == 2 for i in POSITIONS):
            graphs.add(six_edges)
            multi = Counter(six_edges)
            nd = sum(n == 2 for n in multi.values())
            counts[{0: "A", 1: "B", 3: "C"}[nd]] += 1
    if counts != Counter({"A": 70, "B": 45, "C": 15}) or len(graphs) != 130:
        raise AssertionError("all 130 positional two-regular graphs expected")
    # A consists of 60 C6 and 10 C3+C3.
    connected = 0
    for edges in graphs:
        if len(set(edges)) != 6:
            continue
        reached, todo = {0}, [0]
        while todo:
            i = todo.pop()
            for a, b in edges:
                j = b if i == a else a if i == b else None
                if j is not None and j not in reached:
                    reached.add(j)
                    todo.append(j)
        connected += len(reached) == 6
    if connected != 60:
        raise AssertionError("A-type split 60 C6 and 10 C3+C3 expected")
    return {"A_C6": connected, "A_C3_plus_C3": counts["A"]-connected,
            "B": counts["B"], "C": counts["C"], "total": len(graphs)}


def source_degree_moments(s, labels):
    """All-h aggregate M_k for k=1..6 on ONE typed side (regular W(3,s))."""
    if type(s) is not int or s < 2:
        raise ValueError("s must be at least two")
    V, delta = (s+1)*(s*s+1), s+1
    if len(labels) != V:
        raise ValueError("all V original typed factors must be labeled")
    pairs = tuple(normalized_edge(e) for e in labels)
    if len(set(pairs)) != V:
        raise ValueError("globally injective original typed pair map required")
    degrees = Counter(c for edge in pairs for c in edge)
    N = V*delta
    result = {}
    for k in range(1, 7):
        result[k] = choose(N-k, 6-k)*sum(choose(delta*n, k)
                                          for n in degrees.values())
    return result


def joint_cells(incidences, left_labels, right_labels):
    """Original-incidence-aware cell counts n11(c,d), n10, n01, n00.

    These are defined on distinct source edges, not independent f/g images.
    """
    E = tuple(tuple(e) for e in incidences)
    if len(E) != len(set(E)):
        raise ValueError("ORIGINAL incidences must be distinct")
    N = len(E)
    left_deg, right_deg, both = Counter(), Counter(), Counter()
    for p, l in E:
        a = normalized_edge(left_labels[p])
        b = normalized_edge(right_labels[l])
        for c in a:
            left_deg[c] += 1
            for d in b:
                both[(c, d)] += 1
        for d in b:
            right_deg[d] += 1
    return N, left_deg, right_deg, both


def overlap_coefficient(n11, n10, n01, r, t, j):
    """Count ordered (A,B): |A|=r, |B|=t, |A intersect B|=j.

    [x^(r-j) y^(t-j) z^j] (1+x+y+z)^n11
                              (1+x)^n10 (1+y)^n01.
    """
    if j < 0 or j > min(r, t) or n11 < j:
        return 0
    u, v = r-j, t-j
    subtotal = 0
    for a in range(u+1):
        for b in range(v+1):
            subtotal += (choose(n11, j)*choose(n11-j, a)
                         * choose(n11-j-a, b)
                         * choose(n10, u-a)*choose(n01, v-b))
    return subtotal


def joint_moment_sum(incidences, left_labels, right_labels, r, t):
    """Exact global SUM_Q M_r^L(Q) M_t^R(Q), using ORIGINAL joint cells.

    No C(N,6) scan: sum over physical-coordinate pairs and intersection
    size j, with union of selected incidence positions of size r+t-j.
    """
    if any(type(k) is not int or not 1 <= k <= 6 for k in (r, t)):
        raise ValueError("moment orders must lie in 1..6")
    N, L, R, both = joint_cells(incidences, left_labels, right_labels)
    if N < 6:
        raise ValueError("six ORIGINAL incidences required")
    pieces = {}
    for j in range(max(0, r+t-6), min(r,t)+1):
        u = r+t-j
        subtotal = 0
        for c, nl in L.items():
            for d, nr in R.items():
                n11 = both[(c,d)]
                subtotal += overlap_coefficient(
                    n11, nl-n11, nr-n11, r, t, j)
        pieces[j] = choose(N-u, 6-u)*subtotal
    return {"r": r, "t": t, "total": sum(pieces.values()),
            "by_overlap": pieces, "joint_original_incidence_sensitive": True}


def original_W32_census(model):
    """Complete 62,370 left-generator census, with an INDEPENDENT Phi."""
    from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
    from hyp105_issue230_d6z_original_incidence_wedge_moment import (
        validated_original_regular_model)
    p, left, right, incidences = validated_original_regular_model(model)
    if model["s"] != 2:
        raise ValueError("full left enumeration is only permitted for W(3,2)")
    result = Counter()
    n = 0
    for ids, _ in selected_left_six(model):
        n += 1
        tag = classify_original_six(
            (incidences[i] for i in ids), left, right)
        if tag:
            result[tag] += 1
    if n != 62370:
        raise AssertionError("incomplete original W32 six-incidence census")
    return {"candidate_count": n, "by_class": dict(result),
            "S_seven": sum(result.values()),
            "GF5_floor_numerator": sum(result[k]*v for k,v in WEIGHTS.items())}


def report():
    from hyp105_issue230_projection import fixture
    records = []
    for scheme in ("S68", "S72"):
        row = original_W32_census(fixture(1, scheme))
        row["scheme"] = scheme
        records.append(row)
    if [r["S_seven"] for r in records] != [68, 72]:
        raise AssertionError("true ORIGINAL S68/S72 oracle drift")
    return {
        "slice": "HYP105-ISSUE230-D6-AA1-AA3",
        "all_h_local_exact_Phi": True,
        "position_graph_census": enumerate_position_graphs(),
        "original_W32": records,
        "all_h_single_side_moments_exact": True,
        "joint_original_incidence_moment_identity": True,
        "full_GF5_R3": False,
        "all_h_positive_S_lower": False,
        "Branch_A": "OPEN",
        "Branch_B": "OPEN",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(report(), indent=2, sort_keys=True))
