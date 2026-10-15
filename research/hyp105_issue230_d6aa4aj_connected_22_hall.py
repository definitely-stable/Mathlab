"""HYP-105 #230 AA4-AJ: exact true-original Hall transfer for BOTH 2+2 C6 bridges.

Research-only partial theorem. Six distinct genuine original incidence IDs and ONE
fixed globally injected map on each typed side; no stochastic independence.
No unconditional positive GF(5) count is asserted.
"""
from itertools import combinations, permutations
from math import comb

from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    _source_cohort, classify_physical_A_twofactor,
)
from hyp105_issue230_d6aa4ad_opposite_a_hall_transfer import (
    pinned_twofactor_completions,
)

PAIRS = tuple(combinations(range(4), 2))
PERMS = tuple(permutations(range(4)))


def edge(u, v):
    return (u, v) if u < v else (v, u)


def two_bridge_pairings(e0, e1):
    """Two (2,2) paths between disjoint pinned edges; no double counting."""
    if len(set(e0 + e1)) != 4:
        return ()
    u, v = e0
    w, x = e1
    return (((v, w), (x, u)), ((v, x), (w, u)))


def sites(a, inv, ends, forbidden):
    x, z = ends
    return {
        t: (inv[edge(x, t)], inv[edge(z, t)])
        for t in range(a)
        if t not in forbidden
        and edge(x, t) in inv and edge(z, t) in inv
    }


def pair_channels(four, neighbors, left, right):
    """Two independent physical auxiliary sites; exact six Hall channels.

    GQ source girth >=8 makes each 2x2 permanent 0 or 1. The equality
    remains algebraically valid for general bipartite input if integers
    replacing sets track the local 2x2 matching multiplicity.
    """
    left_sets = {S: set() for S in PAIRS}
    right_sets = {S: set() for S in PAIRS}
    for domain, target in ((left, left_sets), (right, right_sets)):
        for t, (a, b) in domain.items():
            for S in PAIRS:
                i, j = S
                ways = int(a in neighbors[four[i]] and b in neighbors[four[j]])
                ways += int(b in neighbors[four[i]] and a in neighbors[four[j]])
                if ways > 1:
                    raise AssertionError("not a genuine GQ (source C4 detected)")
                if ways:
                    target[S].add(t)

    channels = []
    for S in PAIRS:
        comp = tuple(i for i in range(4) if i not in S)
        Y, Z = left_sets[S], right_sets[comp]
        count = len(Y) * len(Z) - len(Y & Z)
        assert count >= 0
        channels.append({
            "rows_left": S, "rows_right": comp, "left_sites": len(Y),
            "right_sites": len(Z), "diagonal_excluded": len(Y & Z),
            "accepted_six_original_incidence_Q": count,
        })
    return channels


def original_connected_22_cohort(model, *, side, root, pair_offset, four,
                                  independent=True):
    """All-h exact accepted GF5 count on one B-C4 / opposite connected-2+2 cohort.

    A cycle has the two pinned actual original source flag edges and four
    remaining opposite edges, with exactly two distinct outside physical
    sites, each joined to one endpoint of EACH pinned edge. Pinned physical
    edges must be disjoint; if adjacent this subfamily is empty.
    """
    a, _, neighbors, pins, inv, (e0, e1), four = _source_cohort(
        model, side=side, root=root, pair_offset=pair_offset, src_four=four
    )
    pairings = two_bridge_pairings(e0, e1)
    forbidden = set(e0 + e1)
    rows = []
    physical_cycles = set()
    total = 0
    for bridge_index, (L, R) in enumerate(pairings):
        Y = sites(a, inv, L, forbidden)
        Z = sites(a, inv, R, forbidden)
        channels = pair_channels(four, neighbors, Y, Z)
        accepted = sum(c["accepted_six_original_incidence_Q"] for c in channels)
        raw = len(Y) * len(Z) - len(set(Y) & set(Z))
        assert raw >= 0
        for y in Y:
            for z in Z:
                if y == z:
                    continue
                H = frozenset((e0, e1, edge(L[0], y), edge(L[1], y),
                               edge(R[0], z), edge(R[1], z)))
                if len(H) != 6 or classify_physical_A_twofactor(
                        H, (e0, e1)) != "connected_C6":
                    raise AssertionError("invalid physical C6 bridge")
                if H in physical_cycles:
                    raise AssertionError("duplicate two-bridge cycle")
                physical_cycles.add(H)
        rows.append({
            "bridge": bridge_index, "endpoint_pairs": (L, R),
            "left_occupied_sites": len(Y), "right_occupied_sites": len(Z),
            "raw_occupied_22_C6": raw, "six_Hall_channels": channels,
            "accepted_original_GF5_Q": accepted,
        })
        total += accepted
    assert len(physical_cycles) == sum(z["raw_occupied_22_C6"] for z in rows)
    result = {
        "s": model["s"], "side": side, "root": root,
        "pinned_original_incidence_other_factors": pins,
        "four_original_source_factors": four,
        "pinned_physical_edges_disjoint": len(pairings) == 2,
        "occupied_connected_22_physical_C6": len(physical_cycles),
        "accepted_original_GF5_connected_22_Q": total,
        "bridge_rows": rows, "original_Hall_lower_all_f_g_NOT_PROVED": True,
    }
    if independent:
        oracle = independent_original_connected_22(
            model, side=side, root=root, pair_offset=pair_offset, four=four
        )
        if (oracle["occupied_H"] != physical_cycles or
                oracle["accepted_Q"] != total):
            raise AssertionError("independent physical-cycle / 24-permutation oracle failed")
    return result


def independent_original_connected_22(model, *, side, root, pair_offset, four):
    """Independent falsifier: enumerate physical full A 2factors, not Y/Z sets.

    Check connected C6, four nonpin physical edges meeting exactly one
    endpoint of the pinned pairs and one of two outside sites. Count
    original 4-rook permanents by literal 24 bijections.
    """
    a, _, neighbors, _, inv, (e0, e1), four = _source_cohort(
        model, side=side, root=root, pair_offset=pair_offset, src_four=four
    )
    pins = (e0, e1)
    P = set(e0 + e1)
    cycles = set()
    accepted = 0
    if len(P) < 4:
        return {"occupied_H": cycles, "accepted_Q": 0}
    for H in pinned_twofactor_completions(e0, e1, a):
        H = frozenset(H)
        remaining = H - set(pins)
        if any(e not in inv for e in remaining):
            continue
        if classify_physical_A_twofactor(H, pins) != "connected_C6":
            continue
        outside = set(v for e in H for v in e) - P
        if len(outside) != 2 or any(
            len(set(e) & P) != 1 or len(set(e) & outside) != 1
            for e in remaining
        ):
            continue
        if H in cycles:
            raise AssertionError("repeated original physical H")
        cycles.add(H)
        cols = [inv[e] for e in sorted(remaining)]
        accepted += sum(
            all(cols[permutation[i]] in neighbors[four[i]] for i in range(4))
            for permutation in PERMS
        )
    return {"occupied_H": cycles, "accepted_Q": accepted}


def complete_22_capacity(a):
    """Raw (all-edges-occupied) two-bridge share of connected C6 is 1/3."""
    if type(a) is not int or a < 6:
        raise ValueError("physical alphabet must be integer >=6")
    return {"each_bridge": (a - 4) * (a - 5),
            "both_bridges": 2 * (a - 4) * (a - 5),
            "all_disjoint_pinned_connected_C6": 6 * (a - 4) * (a - 5)}


def certified_two_bridge_prehall_floor(s):
    """Sibling #518 GQ pencil safety certificate + two distinct #519 bridges.

    Every complete global f,g, genuine W(3,s), s=2^h>=16. PRE-HALL
    physical candidate count only: Hall-positive original Q may be zero.
    Do not confuse this independent closed-form verifier with a new
    proof of the sibling GQ line-pencil lemma.
    """
    if type(s) is not int or s < 2 or s & (s - 1):
        raise ValueError("s must be a power of two >=2")
    V = (s + 1) * (s * s + 1)
    a = 2
    while comb(a, 2) < V:
        a += 1
    m = comb(a, 2) - V
    d = s + 1
    N = V * comb(d, 2)
    H = (32 * m) // a
    safe = max(0, N - a * comb(a - 1, 2) - H * (a - 1) * d * (d - 1))
    C4 = max(0, 3 * comb(a - 2, 4) - m * (a - 4) * (a - 5))
    single = (a * a + 3) // 4
    physical = 2 * safe * C4 * single
    if s >= 16:
        assert 128 * physical >= s ** 14
    return {"s": s, "a": a, "V": V, "missing_physical_edges": m,
            "hot_coordinate_upper": H, "safe_original_rootpairs_lower": safe,
            "occupied_root_C4_lower": C4,
            "connected_22_indexed_preHall_lower": physical,
            "s14_over_128_physical_proved_for_all_global_maps": s >= 16,
            "accepted_original_Hall_positive_lower_NOT_PROVED": True}
