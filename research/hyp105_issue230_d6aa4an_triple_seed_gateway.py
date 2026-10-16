"""HYP-105 #230 AA4-AN: sharp all-global one-sided triple crowding and
constructive COMPLETE physical three-flag -> six-coordinate 2-factor gate.

A selected seven-class GF5 ORIGINAL six-incidence Q has six physically
distinct coordinates of degree exactly 2 on EACH typed side (prior #530).
The new source-triple result is a no-go for proving seven-GF5 by extending
high-multiplicity physical fibers, NOT a lower on selected S.

No other research package imported: the algebra and 3-edge constructive
physical criterion can be independently falsified.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb, isqrt


def canonical_edge(u, v):
    if type(u) is not int or type(v) is not int or u == v:
        raise ValueError("two different integer physical coordinates required")
    return (u, v) if u < v else (v, u)


def falling3(t):
    if type(t) is not int or t < 0:
        raise ValueError("nonnegative integer required")
    return t * (t-1) * (t-2)


def minimal_physical_parameters(s):
    if type(s) is not int or s < 2 or s & (s - 1):
        raise ValueError("genuine W(3,2^h), h>=1 required")
    V = (s + 1)*(s*s + 1)
    a = (1 + isqrt(1 + 8*V))//2
    if comb(a, 2) < V:
        a += 1
    m = comb(a, 2) - V
    return V, a, m


def sharp_all_global_crowded_triple_floor(s):
    """Exact minimum over every complete global typed source factor f.

    `d^3 sum_x (t_x)_3`: ordered original triple-incidence flag IDs with
    THREE distinct original point IDs and all three f-images meeting at
    one shared physical coordinate (the other original type is free).
    Because different physical edges intersect in <=1 coordinate, the
    triples are counted once. For the point/line dual, use line labels.
    """
    V, a, m = minimal_physical_parameters(s)
    d = s + 1
    q, r = divmod(2*V, a)
    assert q >= a - 3 and 0 <= r < a
    sharp = d**3 * ((a-r)*falling3(q) + r*falling3(q+1))
    coarse = d**3 * a*(a-3)*(a-4)*(a-5)
    assert sharp >= coarse
    assert 9*coarse >= s**9
    return {
        "s": s, "V": V, "a": a, "m": m, "d": d,
        "global_physical_center_min_degree": q,
        "number_centers_degree_q_plus_one": r,
        "exact_minimum_ordered_distinct_original_source_point_triples": sharp,
        "coarse_all_maps_original_source_triple_lower": coarse,
        "universal_ordered_original_source_no_lift_at_least_s9_over9": True,
        "other_type_arbitrarily_globally_injected": True,
        "seven_GF5_positive_extension_from_crowded_triple_IMPOSSIBLE": True,
        "root_issue230_Branch_A_B_C_NOT_PROVED": True,
    }


def balanced_missing_edges(a, m):
    """Produce extremal near-regular missing K_a graph, with m<=a-2.

    m<=a//2: matching. Otherwise c=a-m components of vertex-disjoint
    paths, each of size >=2, occupying all a physical vertices. Their
    complement gives globally injective source physical labels with
    degree q or q+1, proving the sharp minimum is ATTAINABLE.
    """
    if type(a) is not int or a < 6 or type(m) is not int or m < 0 or m > a-2:
        raise ValueError("a>=6 and 0<=m<=a-2 required")
    if m <= a//2:
        E = {canonical_edge(2*i, 2*i+1) for i in range(m)}
    else:
        c = a-m
        assert 2*c <= a
        sizes = [2]*c
        sizes[0] += a-2*c
        E = set()
        offset = 0
        for k in sizes:
            E.update(canonical_edge(i,i+1)
                     for i in range(offset,offset+k-1))
            offset += k
        assert offset==a
    assert len(E) == m
    deg = Counter(v for e in E for v in e)
    assert max(deg.values(), default=0)-min(
        (deg[v] for v in range(a)),default=0)<=1
    return frozenset(E)


def count_original_distinct_source_crowded_triples(labels, degree):
    """Exact source-original incidence count for actual full injected map.

    labels are original factor labels on one type, one fixed globally
    injected physical edge per actual original source factor. Each actual
    factor has exactly d DIFFERENT original flags in genuine W(3,s).
    """
    if type(degree) is not int or degree <= 0:
        raise ValueError("actual original source graph degree required")
    labels = tuple(canonical_edge(*x) for x in labels)
    if len(set(labels)) != len(labels):
        raise ValueError("globally injected physical factor labels required")
    deg = Counter(v for e in labels for v in e)
    return degree**3 * sum(falling3(t) for t in deg.values())


def _degree(edges):
    D=Counter()
    for u,v in edges:
        D[u] += 1
        D[v] += 1
    return D


def complete_three_physical_edges_to_six_2regular(edges, a):
    """Construct one 6-edge 6-vertex physical 2-factor containing edges.

    Exact iff MAX physical vertex degree of the given three labeled
    edge occurrences is <=2. Physical edges may repeat, but no loops.
    This criterion is per-one-typed-side physical feasibility ONLY,
    with no guarantee that three additional actual source incidence
    flag IDs exist or simultaneously complete the other typed side.
    """
    if type(a) is not int or a < 6:
        raise ValueError("physical alphabet must have at least six vertices")
    E = tuple(canonical_edge(*e) for e in edges)
    if len(E) != 3 or any(v < 0 or v >= a for e in E for v in e):
        raise ValueError("three physical edge occurrences in K_a required")
    deg = _degree(E)
    if max(deg.values()) > 2:
        return None
    used = set(deg)
    fresh = iter(sorted(set(range(a))-used))
    extra = []
    multiplicity = Counter(E)
    doubled = tuple(e for e,n in multiplicity.items() if n==2)
    if doubled:
        # A closed physical 2-cycle is already full. The third edge
        # must be vertex-disjoint, and a new C4 uses TWO fresh vertices.
        pair = next(e for e in E if e != doubled[0])
        p,q = next(fresh),next(fresh)
        extra = [canonical_edge(pair[0],p),canonical_edge(p,q),
                 canonical_edge(q,pair[1])]
    elif len(used)==3 and set(deg.values())=={2}:
        # All 3 edges form a triangle; add one disjoint new triangle.
        p,q,r=next(fresh),next(fresh),next(fresh)
        extra = [canonical_edge(p,q),canonical_edge(q,r),
                 canonical_edge(r,p)]
    else:
        # A forest of nontrivial paths: concatenate component paths
        # and the 6-|V| new isolated vertices cyclically.
        adj=defaultdict(list)
        for u,v in E:
            adj[u].append(v); adj[v].append(u)
        components=[]
        unseen=set(used)
        while unseen:
            root=min(unseen)
            stack=[root]; vertices=set()
            while stack:
                z=stack.pop()
                if z in vertices: continue
                vertices.add(z); stack.extend(adj[z])
            unseen.difference_update(vertices)
            endpoints=sorted(v for v in vertices if deg[v]==1)
            assert len(endpoints)==2
            components.append(tuple(endpoints))
        components.sort()
        for _ in range(6-len(used)):
            v=next(fresh)
            components.append((v,v))
        for i,(_,end) in enumerate(components):
            start_next=components[(i+1)%len(components)][0]
            extra.append(canonical_edge(end,start_next))
    H=E+tuple(extra)
    check=_degree(H)
    assert len(H)==6 and len(check)==6 and set(check.values())=={2}
    assert not (Counter(E)-Counter(H))
    return tuple(H)


def classify_triple_physical_gateway(edges,a):
    H=complete_three_physical_edges_to_six_2regular(edges,a)
    return {"physical_gateway_eligible":H is not None,
            "constructed_6edge_2regular_H":H,
            "genuine_original_incidence_extension_NOT_PROVED":True}


def verify_balanced_sharpness(s):
    V,a,m=minimal_physical_parameters(s)
    missing=balanced_missing_edges(a,m)
    # Only small s: physically enumerate the complete K_a once.
    if a > 1000:
        raise ValueError("explicit extremal injection only for a<=1000")
    actual=tuple(e for e in combinations(range(a),2) if e not in missing)
    assert len(actual)==V
    sharp=sharp_all_global_crowded_triple_floor(s)
    return count_original_distinct_source_crowded_triples(actual,s+1)==sharp[
        "exact_minimum_ordered_distinct_original_source_point_triples"]
