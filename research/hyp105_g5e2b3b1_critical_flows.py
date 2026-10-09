"""HYP-105 E2-B3.1-A: EXACT GF(5) signed flows in the leading 6+6 core.

Scope: six distinct original factor endpoints on EACH side; injective pair
labels induce a simple 2-regular physical pair graph on SIX coordinates in
EACH color block. Each physical coordinate then belongs to exactly two
columns. The dual column adjacency graph is a 2-factor on six columns:
C6 or C3+C3. All such two-colored pairs and unordered balanced +/- 3v3
events are classified up to a simultaneous permutation of column IDs.

Only the top-degree 6+6 leafless subcase is proved here. Other E2-B3
profiles, actual W(3,s) motif multiplicities and new ASET power stay OPEN.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import comb
import json

N = 6
ALL = (1 << N) - 1
VERTICES = tuple(range(N))
PAIRS = tuple(combinations(VERTICES, 2))
SIGNS = tuple(sum(1 << i for i in (0,) + rest)
              for rest in combinations(range(1, N), 2))


def _normalized_edges(edges):
    return tuple(sorted(tuple(sorted(edge)) for edge in edges))


def _factor_type(edges):
    adj = {i: set() for i in VERTICES}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    todo = set(VERTICES)
    cycles = []
    while todo:
        seed = min(todo)
        seen = {seed}
        stack = [seed]
        while stack:
            for q in adj[stack.pop()]:
                if q not in seen:
                    seen.add(q)
                    stack.append(q)
        todo -= seen
        cycles.append(len(seen))
    return tuple(sorted(cycles))


def two_factors():
    """Exhaustively list all simple 2-regular graphs on six named columns."""
    answer = []
    for chosen in combinations(PAIRS, 6):
        degree = Counter(v for uv in chosen for v in uv)
        if all(degree[i] == 2 for i in VERTICES):
            answer.append(chosen)
    if len(answer) != 70 or Counter(map(_factor_type, answer)) != {
        (6,): 60, (3, 3): 10,
    }:
        raise AssertionError("2-factor census must be C6:60 + 2C3:10")
    return tuple(answer)


CYCLE = _normalized_edges(((0, 1), (1, 2), (2, 3), (3, 4),
                           (4, 5), (5, 0)))
TRIANGLES = _normalized_edges(((0, 1), (1, 2), (2, 0),
                               (3, 4), (4, 5), (5, 3)))
REPRESENTATIVES = ((CYCLE, 60), (TRIANGLES, 10))


def _relabel_edges(edges, perm):
    return _normalized_edges((perm[u], perm[v]) for u, v in edges)


def _relabel_mask(mask, perm):
    image = sum(1 << perm[i] for i in VERTICES if mask & (1 << i))
    return image if image & 1 else ALL ^ image


def _automorphisms(left):
    return tuple(p for p in permutations(VERTICES)
                 if _relabel_edges(left, p) == left)


def _canonical_right_sign(right, mask, autos):
    return min((_relabel_edges(right, p), _relabel_mask(mask, p))
               for p in autos)


def critical_orbits():
    """49,000 labeled cases into exact S6+global-sign orbits.

    Left/right coordinate colors are distinguished; swapping them is NOT
    a symmetry used here. For each left-graph isomorphism type choose a
    representative and quotient its (70 right-graphs)*(10 unordered sign
    partitions) by the full automorphism group of that left representative.
    Multiplying per-representative frequencies by 60 or 10 accounts
    EXACTLY for all 70 choices of left graph.
    """
    cases = {}
    total = 0
    for left, nleft in REPRESENTATIVES:
        autos = _automorphisms(left)
        if len(autos) != (12 if nleft == 60 else 72):
            raise AssertionError("incorrect cycle graph automorphism group")
        groups = Counter()
        for right in two_factors():
            for mask in SIGNS:
                key = _canonical_right_sign(right, mask, autos)
                groups[key] += 1
        if sum(groups.values()) != 70 * 10:
            raise AssertionError("missed potential unordered signed event")
        for (right, mask), count in groups.items():
            case = (left, right, mask)
            if case in cases:
                raise AssertionError("canonical orbit listed twice")
            cases[case] = count * nleft
            total += count * nleft
    if total != 70 * 70 * 10:
        raise AssertionError("signed color-preserving event mass mismatch")
    return cases


def connected_contracted_column_graph(left, right):
    """Independent O(E+V) component oracle on the contracted 6-vertex graph."""
    adjacency = {i: set() for i in VERTICES}
    for u, v in tuple(left) + tuple(right):
        adjacency[u].add(v)
        adjacency[v].add(u)
    reached = {0}
    todo = [0]
    while todo:
        for j in adjacency[todo.pop()]:
            if j not in reached:
                reached.add(j)
                todo.append(j)
    return len(reached) == N


def critical_supports(left, right):
    """Recover actual GF5 support4 columns from physical degree-two slots."""
    result = [[] for _ in VERTICES]
    for block, graph in enumerate((left, right)):
        if len(graph) != N or _factor_type(graph) not in ((6,), (3, 3)):
            raise ValueError("each projection needs a six-edge 2-factor")
        for coord, (u, v) in enumerate(graph):
            result[u].append(block * N + coord)
            result[v].append(block * N + coord)
    supports = tuple(tuple(sorted(c)) for c in result)
    if any(len(row) != 4 or len(set(row)) != 4 for row in supports):
        raise AssertionError("not valid split 2+2 distinct supports")
    if len(set(supports)) != N:
        raise AssertionError("six support4 columns must be distinct")
    return supports


def exact_nowherezero_signed_flow(left, right, mask):
    """Exact count by GF5 inclusion-exclusion over 12 contracted edges.

    Each physical coordinate has degree 2 in the column-coordinate
    incidence graph, so its balance equation eliminates one nonzero
    variable, leaving a signed directed edge in a 4-regular multigraph
    on SIX column vertices. Column boundary demand = 4*sign_i in GF5.

    By inclusion-exclusion over the edges forced to zero:
      F = sum_{A subset 12 edges} (-1)^(12-|A|) *
            [b balanced on EVERY component of (V,A)] * 5^(|A|-6+c(A)).
    This is exact even with L/R parallel edges and isolated vertices.
    """
    if mask not in SIGNS and not (mask.bit_count() == 3 and 0 <= mask <= ALL):
        raise ValueError("exactly three positive and three negative columns")
    edges = tuple(left) + tuple(right)
    if len(edges) != 12:
        raise AssertionError("twelve contracted physical coordinates")
    result = 0
    for included in range(1 << 12):
        parent = list(range(N))

        def root(v):
            while parent[v] != v:
                v = parent[v]
            return v

        nactive = included.bit_count()
        for j, (u, v) in enumerate(edges):
            if included & (1 << j):
                parent[root(u)] = root(v)
        groups = defaultdict(int)
        for v in VERTICES:
            sign = 1 if mask & (1 << v) else -1
            groups[root(v)] += sign
        if any(value % 5 for value in groups.values()):
            continue
        dim = nactive - N + len(groups)
        if dim < 0:
            raise AssertionError("negative GF5 cycle-space dimension")
        term = 5 ** dim
        result += term if (12 - nactive) % 2 == 0 else -term
    if not 0 <= result <= 5**12:
        raise AssertionError("invalid GF5 flow inclusion-exclusion count")
    return result


def proved_matching_r3_lower(s):
    """Uniform-in-s unconditional expected R3 FLOOR from actual factor matchings.

    Choose six DISTINCT, vertex-disjoint GQ incidence edges. There are at
    least prod_{j=0..5}(E-2*j*Delta)/6! unordered such six-sets:
    after j selected edges, <=2*j*Delta graph edges meet an endpoint.

    For each six-set use the UNIQUE alternating balanced 3+3 partition
    whenever the two physical column-adjacency graphs coincide as a C6.
    There are 6!/12=60 labeled C6 on the six named columns. Their
    simultaneous two-block outcomes are mutually exclusive.
    Under independent uniform pair injections, each fixed C6 graph
    appears in one physical half with probability (a)_6/(K)_6.

    All-one coefficients (one of 51 patterns independently per column)
    realize a signed trade: each coordinate occurs once with each
    sign. Thus a matching contributes >=60*P_C6^2/51^6 in expectation.
    The deterministic necessary condition is R3(B_s)>=D_s/51^6,
    where D_s counts six-factor matchings whose two colored C6
    column-adjacency edge sets COINCIDE (one event per six-set).
    This all-h result uses NO assumed flow positivity census.
    """
    if not isinstance(s, int) or s < 2 or (s & (s - 1)):
        raise ValueError("classical theorem requires s=2^h, h>=1")
    v = (s + 1) * (s * s + 1)
    e = (s + 1) ** 2 * (s * s + 1)
    delta = s + 1
    a = 2
    while comb(a, 2) < v:
        a += 1
    k = comb(a, 2)
    matching_lower = Fraction(1)
    for j in range(6):
        matching_lower *= Fraction(e - 2 * j * delta, j + 1)
    if matching_lower <= 0:
        raise AssertionError("six-factor matching lower not positive")
    numerator = 1
    denominator = 1
    for j in range(6):
        numerator *= a - j
        denominator *= k - j
    probability_one_projection = Fraction(numerator, denominator)
    risk_floor = matching_lower * 60 * probability_one_projection**2 / (51**6)
    return {
        "s": s, "m": 2*a, "N": e, "factor_matchings_lower": matching_lower,
        "designated_C6_probability_each_half": probability_one_projection,
        "coincident_labeled_C6_types": 60,
        "expected_coincident_C6_matching_lower":
            matching_lower * 60 * probability_one_projection**2,
        "proved_expected_R3_lower": risk_floor,
        "fixed_label_obstruction": "R3(B_s) >= D_s/51^6 for coincident alternating C6 factor-matching six-sets",
        "scale":"Omega(s^6) for uniform independent injections",
        "universal_individual_label_lower": False,
        "improved_ASET_bound": False,
    }


def critical_flow_census():
    """Exact positivity classification of all dominant degree-two cases."""
    orbits = critical_orbits()
    classes = Counter()
    weighted = Counter()
    min_positive = None
    max_count = 0
    positive_example = None
    zero_example = None
    count_labeled_events = 0
    for (left, right, mask), weight in orbits.items():
        value = exact_nowherezero_signed_flow(left, right, mask)
        if (value > 0) != connected_contracted_column_graph(left, right):
            raise AssertionError("finite GF5 positivity iff contracted connectivity fails")
        status = "positive" if value > 0 else "zero"
        kind = ("%s/%s" % ("C6" if _factor_type(left) == (6,) else "2C3",
                           "C6" if _factor_type(right) == (6,) else "2C3"))
        classes[(kind, status)] += 1
        weighted[(kind, status)] += weight
        count_labeled_events += weight
        if value:
            if min_positive is None or value < min_positive:
                min_positive = value
            max_count = max(max_count, value)
            if positive_example is None:
                positive_example = (left, right, mask, value)
        elif zero_example is None:
            zero_example = (left, right, mask, value)
    if count_labeled_events != 49000:
        raise AssertionError("loss of normalized signed potential events")
    if sum(weighted.values()) != count_labeled_events:
        raise AssertionError("weighted event counts inconsistent")
    if (len(orbits) != 110 or classes.get(("2C3/2C3", "zero")) != 2 or
            weighted.get(("2C3/2C3", "zero")) != 100 or
            sum(v for (kind, status), v in weighted.items()
                if status == "zero") != 100):
        raise AssertionError("exact six-core positive-flow census changed")

    return {
        "model": "all-distinct factor endpoints / v_left=v_right=6 / split 2+2",
        "coordinate_degree_in_each_projection": 2,
        "left_right_2_factors": 70 * 70,
        "unordered_3v3_sign_partitions_per_pair": 10,
        "total_labeled_signed_cases": count_labeled_events,
        "colored_signed_isomorphism_orbits": len(orbits),
        "orbits_by_kind_and_sign": {"/".join(key): value
                                   for key, value in sorted(classes.items())},
        "labeled_cases_by_kind_and_sign": {
            "/".join(key): value for key, value in sorted(weighted.items())
        },
        "min_positive_flow_count": min_positive,
        "max_flow_count": max_count,
        "positive_example": positive_example,
        "zero_example": zero_example,
        "exact_GF5_computation": "prescribed-boundary component-balanced inclusion-exclusion on 12 edges",
        "proved_critical_flow_iff_connected": True,
        "zero_flow_labeled_cases": 100,
        "positive_flow_labeled_cases": 48900,
        "zero_cases_sole_obstruction": "same 3+3 partition on both two-triangle factors",
        "all_11663_leafless_forest_shapes_classified": False,
        "actual_W3s_event_multiplicities_bounded": False,
        "strict_R3_power_proved": False,
        "new_ASET_exponent_proved": False,
    }


if __name__ == "__main__":
    print(json.dumps(critical_flow_census(), sort_keys=True, indent=2))
