"""HYP-105 G5-E1: exact split-2+2 flow risk motif gates.

This is proof tooling for ALL-m finite-template reduction, not a
new ASET exponent or worldwide novelty claim. No R3 O(N^6) enumeration
is run at GQ(s=4) scale; direct finite enumerator caps N<=9.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations

from hyp105_g5d_trade_rank import signed_trade_rank_report


def _incidence_graph(supports, signs):
    if len(supports) == 0 or len(supports) != len(signs):
        raise ValueError("nonempty matched support and sign arrays required")
    if any(s not in (-1, 1) for s in signs):
        raise ValueError("signed columns must have signs +1 or -1")
    if any(len(row) != 4 or len(set(row)) != 4
           or any(not isinstance(x, int) or x < 0 for x in row)
           for row in supports):
        raise ValueError("every support must have four distinct nonnegative coords")
    t = len(supports)
    coords = sorted({coord for row in supports for coord in row})
    lookup = {coord: t + i for i, coord in enumerate(coords)}
    edges = tuple((i, lookup[coord]) for i, row in enumerate(supports)
                  for coord in row)
    adj = [[] for _ in range(t + len(coords))]
    for idx, (a, b) in enumerate(edges):
        adj[a].append((b, idx))
        adj[b].append((a, idx))
    degrees = Counter(c for row in supports for c in row)
    return coords, edges, adj, degrees


def _connected_reachable(adj, start, ignored_edge=None):
    seen = {start}
    todo = [start]
    while todo:
        current = todo.pop()
        for neighbor, eid in adj[current]:
            if eid == ignored_edge or neighbor in seen:
                continue
            seen.add(neighbor)
            todo.append(neighbor)
    return seen


def bridge_boundary_obstructions(supports, signs):
    """List bridges whose one-side sum of GF5 column demands is zero.

    A prescribed-boundary nowhere-zero flow cannot cross such a bridge:
    flow on the bridge equals the signed demand on either side.
    This is a NECESSARY zero-risk gate, NOT an iff characterization.
    """
    _, edges, adj, _ = _incidence_graph(supports, signs)
    t = len(supports)
    bad = []
    for eid, (a, b) in enumerate(edges):
        side = _connected_reachable(adj, a, eid)
        if b in side:
            continue
        signed_sum = sum(signs[i] for i in range(t) if i in side) % 5
        if signed_sum == 0:
            bad.append((eid, a, b))
    return tuple(bad)


def _components(adj, t, signs):
    remain = set(range(len(adj)))
    result = []
    while remain:
        first = min(remain)
        component = _connected_reachable(adj, first)
        remain.difference_update(component)
        members = tuple(sorted(i for i in component if i < t))
        result.append(members)
    return tuple(result)


def topology_gate(supports, signs, block_size=None):
    """Sound structural NO-FLOW filter for arbitrary GF5 signed support4.

    With block_size=a, enforce exactly two coords in [0,a), two in
    [a,2a), then the projected pair multigraphs must be leafless
    and have <=t touched coordinate vertices EACH.
    """
    coords, edges, adj, degrees = _incidence_graph(supports, signs)
    t = len(supports)
    components = _components(adj, t, signs)
    balanced = all(sum(signs[i] for i in comp) % 5 == 0
                   for comp in components)
    singletons = tuple(sorted(c for c, deg in degrees.items() if deg == 1))
    bridges = bridge_boundary_obstructions(supports, signs)
    projections = None
    if block_size is not None:
        if not isinstance(block_size, int) or block_size < 2:
            raise ValueError("positive split half-size >=2 required")
        if any(sum(0 <= c < block_size for c in row) != 2 or
               sum(block_size <= c < 2*block_size for c in row) != 2
               for row in supports):
            raise ValueError("model requires exact globally split 2+2 supports")
        left = {c for c in coords if c < block_size}
        right = {c for c in coords if c >= block_size}
        projections = {
            "left_vertices": len(left), "right_vertices": len(right),
            "edges_per_projection": t,
            "left_degree_one": sum(degrees[c] == 1 for c in left),
            "right_degree_one": sum(degrees[c] == 1 for c in right),
            "left_all_degrees_at_least_two":
                all(degrees[c] >= 2 for c in left),
            "right_all_degrees_at_least_two":
                all(degrees[c] >= 2 for c in right),
        }
        if not singletons and (len(left) > t or len(right) > t):
            raise AssertionError("degree-two projected graph theorem failed")
    return {
        "columns": t, "coordinates": len(coords),
        "components": components, "component_balanced": balanced,
        "singleton_coords": singletons, "zero_demand_bridges": bridges,
        "potential_nonzero_flow": balanced and not singletons and not bridges,
        "two_block_projection": projections,
        "necessary_only": True,
    }


def canonical_split_motif(supports, signs, block_size):
    """Complete signed, two-color bipartite graph isomorphism signature.

    Coordinate vertices relabel freely *within* left/right coordinate
    halves, column vertices relabel within each sign class, and the two
    sign classes may be globally exchanged. The tuple of each
    coordinate's column-incidence bitmask is a complete invariant:
    preserving 2-block color and +/- column partition is equivalent
    to equality of canonical signatures. Handles repeated pair labels.
    """
    gate = topology_gate(supports, signs, block_size)
    t = len(supports)
    positives = tuple(i for i in range(t) if signs[i] == 1)
    negatives = tuple(i for i in range(t) if signs[i] == -1)
    if len(positives) != len(negatives) or len(positives) not in (2, 3):
        raise ValueError("signed motifs here must be 2v2 or 3v3")
    k = len(positives)
    best = None
    for first, second in ((positives, negatives), (negatives, positives)):
        for pp in permutations(first):
            for nn in permutations(second):
                order = pp + nn
                left = defaultdict(int)
                right = defaultdict(int)
                for bit, i in enumerate(order):
                    for c in supports[i]:
                        (left if c < block_size else right)[c] |= 1 << bit
                signature = (k, tuple(sorted(left.values())),
                             tuple(sorted(right.values())))
                if best is None or signature < best:
                    best = signature
    if sum(x.bit_count() for x in best[1]) != 2*t or \
       sum(x.bit_count() for x in best[2]) != 2*t:
        raise AssertionError("canonical colored incidence lost an edge")
    return best


def classify_small_split_risk(supports, block_size, k=2, max_n=9):
    """Enumerate exact finite MOTIF multiplicities without O(N^6) at scale.

    Topology gate filters risk-zero patterns; positive survivors are only
    POSSIBLE GF5 flows. Sign is canonicalized up to exchanging P and Q.
    """
    if k not in (2, 3):
        raise ValueError("only k=2/3 required")
    n = len(supports)
    if n > max_n:
        raise ValueError("direct event enumeration has explicit N<=9 cap")
    if len({tuple(sorted(s)) for s in supports}) != n:
        raise ValueError("distinct support4 candidates required")
    CounterTypes = Counter()
    rejected = Counter()
    surviving = 0
    for plus in combinations(range(n), k):
        remaining = tuple(i for i in range(n) if i not in plus)
        for minus in combinations(remaining, k):
            if plus >= minus:
                continue
            group = plus + minus
            chosen = tuple(supports[i] for i in group)
            signs = (1,)*k+(-1,)*k
            gate = topology_gate(chosen, signs, block_size)
            if not gate["potential_nonzero_flow"]:
                if not gate["component_balanced"]:
                    rejected["component_imbalance"] += 1
                elif gate["singleton_coords"]:
                    rejected["singleton_coordinate"] += 1
                else:
                    rejected["balanced_bridge"] += 1
                continue
            signature = canonical_split_motif(chosen, signs, block_size)
            CounterTypes[signature] += 1
            surviving += 1
    return {
        "k": k, "n": n,
        "total_events": sum(CounterTypes.values())+sum(rejected.values()),
        "possible_events": surviving,
        "rejected_by_first_reason": dict(rejected),
        "motif_counts": dict(CounterTypes),
        "distinct_possible_motif_types": len(CounterTypes),
        "necessary_only": True,
    }


def unit_conflict_risk_floor(unit_conflict_bitmasks, t):
    """Provable lower bound on TRUE weighted R_{t/2}: T_t/51^t.

    Every distinct minimal actual *unit* trade support of size t has at
    least one balanced orientation. All-one coefficients are one of 51
    independent pattern choices per column, so that signed event has
    probability >=51^-t, and supports give distinct unordered events.
    """
    if t not in (4, 6):
        raise ValueError("requires balanced unit trades t=4 or 6")
    masks = tuple(unit_conflict_bitmasks)
    if len(masks) != len(set(masks)) or any(
        not isinstance(x, int) or x < 0 or x.bit_count() != t
        for x in masks
    ):
        raise ValueError("distinct true t-column conflict bitmasks required")
    return Fraction(len(masks), 51**t)


def topology_bound_check(supports, signs, block_size):
    """Exact D4 rank upper, zeroed by additional GF5 bridge criterion."""
    gate = topology_gate(supports, signs, block_size)
    if not gate["potential_nonzero_flow"]:
        return Fraction(0)
    return signed_trade_rank_report(supports, signs)[
        "nonzero_palette_upper"]


def finite_w32_motif_report():
    """Reproducible order-two probe only; all-s theorem stays symbolic."""
    from hyp105_g5d_affine_weights import w32_supports
    from hyp105_g5c2_density import collision_spectrum, w32_columns
    supports = w32_supports()
    t4, t6 = collision_spectrum(w32_columns())
    c2 = classify_small_split_risk(supports[:8], 6, k=2)
    c3 = classify_small_split_risk(supports[:8], 6, k=3)
    return {
        "model": "GF5 all-nonzero weighted risk, globally split 2+2 W32 m12",
        "original_support_count": len(supports),
        "exact_unit_minimal_T4": len(t4),
        "exact_unit_minimal_T6": len(t6),
        "weighted_exact_R2_floor": str(unit_conflict_risk_floor(t4, 4)),
        "weighted_exact_R3_floor": str(unit_conflict_risk_floor(t6, 6)),
        "capped_first_eight_2v2": {
            k: v for k, v in c2.items() if k != "motif_counts"
        },
        "capped_first_eight_3v3": {
            k: v for k, v in c3.items() if k != "motif_counts"
        },
        "asymptotic_bound_proven": False,
        "uniform_random_expected_certificate_power_no_go": "12/5",
        "no_all_labeling_lower_claim": True,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(finite_w32_motif_report(), indent=2, sort_keys=True))
