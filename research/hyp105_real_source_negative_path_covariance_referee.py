"""Original W(3,2^h) negative path-covariance referee.

An all-h constructive mathematical counterexample to the extrapolation that
two individually survivable physical paths must survive together. This is
NOT a counterexample to Branch A: its published selector proof only needs
one-path marginals and Jensen. This source module only imports the TRUE
finite GQ source fixture for h=1,2. The all-h extension is a separate
matching-and-injection proof in the companion document.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt

from hyp105_full_physical_degree_tail import genuine_source


P = ((0, 0), (1, 1), (2, 2))
Q = ((1, 1), (2, 2), (0, 3))


def minimal_a(v):
    if type(v) is not int or v < 15:
        raise ValueError("true ORIGINAL source V >= 15 required")
    a = (1 + isqrt(1 + 8*v)) // 2
    while comb(a, 2) < v:
        a += 1
    assert a >= 6 and (a == 2 or comb(a-1, 2) < v)
    return a


def original_three_matching(flags):
    """Greedy three-source-flag matching, never a synthetic incidence."""
    used_p, used_l, picked = set(), set(), []
    for i, (p, ell) in enumerate(flags):
        if p not in used_p and ell not in used_l:
            picked.append(i)
            used_p.add(p)
            used_l.add(ell)
            if len(picked) == 3:
                break
    if len(picked) != 3:
        raise AssertionError("genuine GQ must have three disjoint flags")
    return tuple(picked)


def complete_labels(v, a, pins):
    """Complete and separately injective pair map, with prescribed images."""
    all_pairs = list(combinations(range(a), 2))
    if len(set(pins.values())) != len(pins):
        raise ValueError("noninjective specified pairs")
    if any(i < 0 or i >= v or pair not in all_pairs for i, pair in pins.items()):
        raise ValueError("invalid original pin")
    remaining = iter(pair for pair in all_pairs if pair not in set(pins.values()))
    out = tuple(pins.get(i, None) if i in pins else next(remaining) for i in range(v))
    assert len(out) == v and len(set(out)) == v
    return out


def labelled_original_source(power):
    s, v, flags = genuine_source(power)
    a = minimal_a(v)
    chosen = original_three_matching(flags)
    lp = ((0, 1), (1, 2), (0, 2))
    rp = ((0, 1), (1, 2), (2, 3))
    f = complete_labels(v, a, {flags[i][0]: lp[j] for j, i in enumerate(chosen)})
    g = complete_labels(v, a, {flags[i][1]: rp[j] for j, i in enumerate(chosen)})
    assert len(set(f)) == len(set(g)) == v
    assert len({flags[i][0] for i in chosen}) == 3
    assert len({flags[i][1] for i in chosen}) == 3
    return s, v, flags, f, g, chosen


def original_edge_owners(flags, f, g):
    """Source-first physical edge provenance, both diagonals for every flag."""
    owners = {}
    for i, (p, ell) in enumerate(flags):
        x, xx = f[p]
        y, yy = g[ell]
        for u, w in (((x, y), (xx, yy)), ((x, yy), (xx, y))):
            edge = tuple(sorted((u, w)))
            if edge in owners:
                raise AssertionError("distinct original flags share a physical edge")
            owners[edge] = i
    if len(owners) != 2*len(flags):
        raise AssertionError("paired physical source incomplete")
    return owners


def path_owners(path, edge_owners):
    return tuple(edge_owners[tuple(sorted((a, b)))] for a, b in zip(path, path[1:]))


def original_conflicts(ids, flags, f, g):
    """Independent source-pencil conflict reconstruction; not an old selector."""
    graph = {i: set() for i in ids}
    buckets = defaultdict(list)
    for i in ids:
        p, ell = flags[i]
        for y in g[ell]:
            buckets[("point", p, y)].append(i)
        for x in f[p]:
            buckets[("line", ell, x)].append(i)
    for members in buckets.values():
        for i, j in combinations(members, 2):
            graph[i].add(j)
            graph[j].add(i)
    return graph


def pair_local_minima_probability(adjacency, i, j):
    """Exact priority probability for two NONADJACENT target source IDs.

    Neighbor sets A (only i), B (only j), C (shared) have sizes a,b,c.
    Integrate (1-t)^a (1-u)^b (1-max(t,u))^c over [0,1]^2.
    Splitting into t>=u and u>=t yields a closed rational expression.
    """
    if i == j or i not in adjacency or j not in adjacency:
        raise ValueError("distinct existing source owner IDs required")
    if j in adjacency[i] or i in adjacency[j]:
        return Fraction(0)
    ni = adjacency[i] - {i, j}
    nj = adjacency[j] - {i, j}
    a = len(ni - nj)
    b = len(nj - ni)
    c = len(ni & nj)
    n = a+b+c+2
    return (
        (Fraction(1, a+c+1) - Fraction(1, n)) / (b+1)
        + (Fraction(1, b+c+1) - Fraction(1, n)) / (a+1)
    )


def two_color_probability(edges):
    """Independent graph-parity oracle for unbiased symbol colors."""
    graph = defaultdict(set)
    for u, v in edges:
        if u == v:
            return Fraction(0)
        graph[u].add(v)
        graph[v].add(u)
    colors = {}
    components = 0
    for u in graph:
        if u in colors:
            continue
        components += 1
        colors[u] = 0
        stack = [u]
        while stack:
            x = stack.pop()
            for y in graph[x]:
                if y in colors:
                    if colors[y] == colors[x]:
                        return Fraction(0)
                else:
                    colors[y] = 1-colors[x]
                    stack.append(y)
    return Fraction(2**components, 2**len(colors))


def cut_probabilities(f, g, flags, triple):
    """Independent direct 128-assignment census vs parity-graph formulas."""
    ids_p, ids_q = triple[:2], triple[1:]
    def constraints(ids, labels, side):
        return tuple(labels[flags[i][side]] for i in ids)
    lp = constraints(ids_p, f, 0)
    lq = constraints(ids_q, f, 0)
    rp = constraints(ids_p, g, 1)
    rq = constraints(ids_q, g, 1)
    all_left = sorted(set(x for e in lp+lq for x in e))
    all_right = sorted(set(x for e in rp+rq for x in e))
    n = len(all_left) + len(all_right)
    count_p = count_q = count_both = 0
    for bits in range(1 << n):
        lc = {x: (bits >> j)&1 for j, x in enumerate(all_left)}
        rc = {y: (bits >> (j+len(all_left)))&1 for j,y in enumerate(all_right)}
        p = all(lc[x] != lc[y] for x,y in lp) and all(rc[x] != rc[y] for x,y in rp)
        q = all(lc[x] != lc[y] for x,y in lq) and all(rc[x] != rc[y] for x,y in rq)
        count_p += p
        count_q += q
        count_both += p and q
    direct = tuple(Fraction(z, 1 << n) for z in (count_p,count_q,count_both))
    parity = (
        two_color_probability(lp)*two_color_probability(rp),
        two_color_probability(lq)*two_color_probability(rq),
        two_color_probability(lp+lq)*two_color_probability(rp+rq),
    )
    assert direct == parity
    return direct, (lp, lq, rp, rq)


def real_source_covariance_certificate(power, *, full_source=True):
    """Actual W32/W34: signed covariance is STRICTLY NEGATIVE.

    On sparse I={three source flags}, it is exactly -1/256.
    On FULL genuine W(3,s), the probability is separately given by
    the original source-conflict priority integral; joint cut is zero.
    """
    s, v, flags, f, g, triple = labelled_original_source(power)
    owners = original_edge_owners(flags, f, g)
    if path_owners(P, owners) != triple[:2]:
        raise AssertionError("P not physically sourced by two original flags")
    if path_owners(Q, owners) != triple[1:]:
        raise AssertionError("Q not physically sourced by two original flags")
    if any(len({vertex[axis] for vertex in path}) != 3
           for path in (P,Q) for axis in (0,1)):
        raise AssertionError("the witness paths are not individually coordinate-proper")
    core = tuple(range(len(flags))) if full_source else triple
    graph = original_conflicts(core, flags, f, g)
    if any(j in graph[i] for i,j in combinations(triple,2)):
        raise AssertionError("source three matching has a conflict")
    cuts, edges = cut_probabilities(f, g, flags, triple)
    if cuts != (Fraction(1,16), Fraction(1,16), Fraction(0)):
        raise AssertionError("odd left triangle must kill only the joint path cut")
    first = pair_local_minima_probability(graph, triple[0], triple[1])
    second = pair_local_minima_probability(graph, triple[1], triple[2])
    marg_p, marg_q = first*cuts[0], second*cuts[1]
    covariance = -marg_p*marg_q
    if not (marg_p>0 and marg_q>0 and covariance<0):
        raise AssertionError("negative covariance counterexample lost")
    return {
        "power": power, "s": s, "V": v, "N": len(flags),
        "physical_edges_full": len(owners),
        "original_matching_flag_ids": triple,
        "all_original_maps_complete_injective": True,
        "scope": "FULL_ORIGINAL_SOURCE" if full_source else "THREE_FLAG_CORE",
        "source_priority_P": first,
        "source_priority_Q": second,
        "typed_cut_P": cuts[0],
        "typed_cut_Q": cuts[1],
        "typed_cut_joint": cuts[2],
        "path_P_marginal": marg_p, "path_Q_marginal": marg_q,
        "joint_survival": Fraction(0),
        "covariance": covariance,
        "invalid_inference": "PATH_PAIR_POSITIVE_COVARIANCE",
        "root_branch_a_refuted": False,
        "external_qualified_review_completed": False,
    }


if __name__ == "__main__":
    from json import dumps
    def _encode(obj):
        if isinstance(obj, Fraction):
            return str(obj)
        raise TypeError(type(obj))
    print(dumps([real_source_covariance_certificate(h, full_source=full)
                 for h in (1,2) for full in (False,True)],
                default=_encode, indent=2))
