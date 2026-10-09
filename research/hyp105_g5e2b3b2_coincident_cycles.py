"""HYP-105 G5-E2-B3.2: EXACT deterministic coincident C6 obstruction D_s.

Proof-scoped algorithm: enumerate 6-cycles in the LEFT physical K_a pair
graph of distinct factor point labels; attach each point's incident
factor line, checking the RIGHT physical pair labels form a six-cycle
with the SAME column-edge adjacency order. Distinct line endpoints are
enforced. Counts all matching six-sets exactly ONCE, avoiding C(N,6).

This is a finite h=1,2 checker for the strengthened, EXACT motif
fixed-label bound R3(B_s) >= 5643*D_s(B_s)/51^6, with flow coefficient
verified independently in the existing E2-B3.1 source. No new all-h
R3 upper or ASET power.
"""
from collections import Counter
from itertools import combinations
import json

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic, SCHEMES
from hyp105_g5e2b3b1_critical_flows import (CYCLE, exact_nowherezero_signed_flow)


def exact_alternating_cycle_weight():
    """E0/E2-B3.1's exact GF5 3v3 count for coincident colored C6.

    The alternating partition is unique up to reversing all signs.
    A physical relabeling of coordinate symbols does not change the
    signed incidence motif or this exact nowhere-zero flow count.
    """
    mask = (1 << 0) | (1 << 2) | (1 << 4)
    value = exact_nowherezero_signed_flow(CYCLE, CYCLE, mask)
    if value != 5643:
        raise AssertionError("exact GF5 signed C6/C6 flow weight changed")
    return value


def _labels_ok(labels, alphabet_size):
    return (len(set(labels)) == len(labels)
            and all(len(p) == 2 and 0 <= p[0] < p[1] < alphabet_size
                    for p in labels))


def check_input(model):
    """Validate exact graph/physical boundary (no silent multi-edges)."""
    a = model["a"]
    left = tuple(tuple(p) for p in model["left_labels"])
    right = tuple(tuple(p) for p in model["right_labels"])
    edges = tuple(tuple(e) for e in model["incidences"])
    if (not isinstance(a, int) or a < 6 or
            not _labels_ok(left, a) or not _labels_ok(right, a)):
        raise ValueError("two injective pair labels in a>=6 required")
    if (len(set(edges)) != len(edges) or
            any(len(edge) != 2 or
                not (0 <= edge[0] < len(left)) or
                not (0 <= edge[1] < len(right))
                for edge in edges)):
        raise ValueError("distinct valid factor incidence edges required")
    if len(edges) != model["N"]:
        raise ValueError("incidence cardinality metadata inconsistent")
    return a, left, right, edges


def physical_six_cycles(labels, a):
    """Enumerate each undirected physical simple C6 ONCE, with edge IDs.

    Canonicalization: the smallest physical vertex is first, and its
    smaller C6 neighbor is second (rather than last). Unused physical
    pair edges in K_a are simply absent. No GF5 arithmetic here.
    """
    if not _labels_ok(tuple(labels), a):
        raise ValueError("physical K_a pair-edge injection required")
    adjacency = [[] for _ in range(a)]
    for edge_id, (u, v) in enumerate(labels):
        adjacency[u].append((v, edge_id))
        adjacency[v].append((u, edge_id))
    for neighbors in adjacency:
        neighbors.sort()

    for start in range(a):
        coordinates = [start]
        visited = {start}
        edge_ids = []

        def walk(cur):
            if len(edge_ids) == 5:
                for nxt, edge_id in adjacency[cur]:
                    if nxt == start and coordinates[1] < cur:
                        yield tuple(edge_ids + [edge_id])
                return
            for nxt, edge_id in adjacency[cur]:
                if nxt <= start or nxt in visited:
                    continue
                visited.add(nxt)
                coordinates.append(nxt)
                edge_ids.append(edge_id)
                yield from walk(nxt)
                edge_ids.pop()
                coordinates.pop()
                visited.remove(nxt)

        yield from walk(start)


def _single_overlap(a, b):
    """Shared physical symbol for DISTINCT pair-edges; None otherwise."""
    if a == b:
        return None
    if a[0] == b[0] or a[0] == b[1]:
        return a[0]
    if a[1] == b[0] or a[1] == b[1]:
        return a[1]
    return None


def _aligned_right_cycles(left_cycle_points, options, right_pairs,
                          incidence_to_column):
    """Exact closure of the right physical C6, in left column order.

    Both physical cycles being aligned is equivalent to matching
    column-adjacency C6 graphs, and yields one unordered alternating
    signed 3v3 event. Repeated line factor vertices are prohibited.
    Distinct successive shared coordinates force the entire right
    pair graph to be a simple 6-cycle, not a star/triangle.
    """
    candidates = tuple(options[point] for point in left_cycle_points)
    if any(not row for row in candidates):
        return
    selected = []
    used_line_ids = set()
    used_shared_coordinates = set()

    def walk(depth, previous_pair):
        if depth == 6:
            closing = _single_overlap(previous_pair, right_pairs[selected[0]])
            if closing is not None and closing not in used_shared_coordinates:
                # The closing physical coordinate is the sixth distinct
                # shared symbol; each of the six pair-edges is already
                # forced to consist of two different cycle-neighbor symbols.
                yield tuple(
                    incidence_to_column[(point, line)]
                    for point, line in zip(left_cycle_points, selected))
            return

        for line in candidates[depth]:
            if line in used_line_ids:
                continue
            pair = right_pairs[line]
            shared = None if depth == 0 else _single_overlap(previous_pair, pair)
            if depth and (shared is None or shared in used_shared_coordinates):
                continue
            selected.append(line)
            used_line_ids.add(line)
            if depth:
                used_shared_coordinates.add(shared)
            yield from walk(depth + 1, pair)
            if depth:
                used_shared_coordinates.remove(shared)
            used_line_ids.remove(line)
            selected.pop()

    yield from walk(0, None)


def exact_coincident_c6(model, cycle_limit=300000, witness_limit=3):
    """Exact D_s count for supplied finite labeled incidence model.

    This is an output-sensitive join over LEFT physical six-cycles and
    6-step constrained RIGHT incidence choices. Does not scan C(N,6).
    'cycle_limit' is a failure-only CI resource guard: if exceeded the
    function raises rather than returning an incomplete count.
    """
    a, left, right, incidence = check_input(model)
    if not isinstance(cycle_limit, int) or cycle_limit < 1:
        raise ValueError("positive resource guard needed")
    options = [[] for _ in left]
    incidence_to_column = {}
    for colid, (pid, lid) in enumerate(incidence):
        options[pid].append(lid)
        incidence_to_column[(pid, lid)] = colid
    for row in options:
        row.sort()
    cycles = 0
    risk_sixsets = 0
    witnesses = []
    for left_cycle in physical_six_cycles(left, a):
        cycles += 1
        if cycles > cycle_limit:
            raise RuntimeError("exceeded exact left-cycle enumeration budget")
        for column_ids in _aligned_right_cycles(
                left_cycle, options, right, incidence_to_column):
            risk_sixsets += 1
            if len(witnesses) < witness_limit:
                witnesses.append(column_ids)
    if risk_sixsets < len(witnesses):
        raise AssertionError("invalid cycle count")
    flow_weight = exact_alternating_cycle_weight()
    return {
        "h": model.get("h"), "s": model.get("s"),
        "scheme": model.get("scheme"), "m": model.get("m"),
        "N": len(incidence),
        "left_physical_C6_cycles_examined": cycles,
        "exact_coincident_C6_factor_matchings_D": risk_sixsets,
        "witness_column_ids_in_canonical_left_cycle_order": witnesses,
        "exact_GF5_flow_weight_per_agreeing_cycle": flow_weight,
        "fixed_label_R3_lower_exact": "%s/51^6" % (
            flow_weight * risk_sixsets),
        "search": "left physical simple C6 DFS + constrained right factor-incidence join",
        "enumerated_N_choose_6": False,
        "all_h_upper_bound_proved": False,
        "strict_R3_exponent_proved": False,
        "new_ASET_exponent_proved": False,
    }


def _physical_dual_column_edges(support_half):
    """Independent tiny 6-column validation of physical 2-regular graph."""
    coordinate_occurrences = {}
    for index, pair in enumerate(support_half):
        for symbol in pair:
            coordinate_occurrences.setdefault(symbol, []).append(index)
    if len(coordinate_occurrences) != 6:
        return None
    if any(len(ids) != 2 for ids in coordinate_occurrences.values()):
        return None
    edges = tuple(sorted(tuple(ids) for ids in coordinate_occurrences.values()))
    adjacency = [set() for _ in range(6)]
    for i, j in edges:
        if i == j:
            return None
        adjacency[i].add(j)
        adjacency[j].add(i)
    if any(len(x) != 2 for x in adjacency):
        return None
    seen = {0}
    stack = [0]
    while stack:
        for neighbor in adjacency[stack.pop()]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    return edges if len(seen) == 6 else None


def independent_brute_small_incidence(model, max_n=14):
    """Brute all SIX-subsets of a small physical incidence candidate set.

    Independently test exact factor matching, TWO physical six-coordinate
    projections and equal dual column-adjacency edge sets. This does
    not reuse canonical physical C6 enumeration or right DFS join.
    """
    a, left, right, incidence = check_input(model)
    n = len(incidence)
    if n > max_n:
        raise ValueError("independent C(n,6) oracle intentionally capped")
    result = 0
    witnesses = []
    for subset in combinations(range(n), 6):
        endpoints = [incidence[i] for i in subset]
        if (len({x for x, _ in endpoints}) != 6 or
                len({y for _, y in endpoints}) != 6):
            continue
        l = _physical_dual_column_edges([left[x] for x, _ in endpoints])
        if l is None:
            continue
        r = _physical_dual_column_edges([right[y] for _, y in endpoints])
        if r == l:
            result += 1
            if len(witnesses) < 3:
                witnesses.append(subset)
    return {"D": result, "witnesses": witnesses, "n": n}


def bounded_report():
    """Full finite GF2/GF4 model controls; no across-h exponent fitting."""
    cases = []
    for h in (1, 2):
        for scheme in SCHEMES:
            model = pair_labeled_symplectic(h, scheme)
            case = exact_coincident_c6(model)
            case.pop("witness_column_ids_in_canonical_left_cycle_order")
            cases.append(case)
    return {
        "cases": cases,
        "meaning": "finite exact D_s necessary obstruction, NOT total GF5 R3",
        "reference_all_h_expected_risk_floor":
            "matching factor class Omega(s^6) under independently random injected labels",
        "unproved": ["fixed-label R3 upper", "joint R2 control",
                     "correlated all-h strictly improved ASET exponent"],
    }


if __name__ == "__main__":
    print(json.dumps(bounded_report(), indent=2, sort_keys=True))
