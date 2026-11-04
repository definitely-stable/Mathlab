"""Exact 51-palette residue fibers and signed-event transversal lemmas.

A deliberately small-N, independent arithmetic oracle. Large W34 physical
full-original enumeration is handled separately by the certified PR #719 referee.
The oracle does not treat signed events as physical-automorphism orbits.
"""
from itertools import combinations, product

PALETTES = tuple(
    p for p in product(range(1, 5), repeat=4) if sum(p) % 5 == 4
)
assert len(PALETTES) == 51 and len(set(PALETTES)) == 51


def _validate(columns):
    if not columns:
        raise ValueError("nonempty original source required")
    width = len(columns[0])
    if width < 4 or any(len(x) != width or any(v not in range(5) for v in x)
                      for x in columns):
        raise ValueError("invalid complete physical GF5 source vectors")
    return width


def _sum_ids(columns, ids, m):
    return tuple(sum(columns[i][j] for i in ids) % 5 for j in range(m))


def legal_replacements(m, support):
    if len(support) != 4 or len(set(support)) != 4 or any(
        not isinstance(j, int) or not 0 <= j < m for j in support
    ):
        raise ValueError("exact four distinct in-range support coordinates required")
    out = []
    for palette in PALETTES:
        values = [0] * m
        for j, value in zip(support, palette):
            values[j] = value
        out.append(tuple(values))
    return tuple(out)


def signed_events(columns, k):
    """Complete unordered, source-DISJOINT equal-k-sum original event set."""
    m = _validate(columns)
    if k not in (2, 3):
        raise ValueError("only exact R2 or R3")
    bucket = {}
    events = set()
    for ids in combinations(range(len(columns)), k):
        key = _sum_ids(columns, ids, m)
        for before in bucket.get(key, ()):
            if set(before).isdisjoint(ids):
                events.add(tuple(sorted((before, ids))))
        bucket.setdefault(key, []).append(ids)
    return frozenset(events)


def local_palette_fibers(columns, i, support):
    """Compute H2/H3 for all 51 patterns using a separate residual oracle."""
    m = _validate(columns)
    if type(i) is not int or not 0 <= i < len(columns):
        raise ValueError("invalid original source ID")
    legal = legal_replacements(m, support)
    index_by_residue = {p: j for j, p in enumerate(legal)}
    old_index = index_by_residue.get(tuple(columns[i]))
    if old_index is None:
        raise ValueError("old source vector is not a legal checksum4 four-support palette")
    others = tuple(j for j in range(len(columns)) if j != i)
    h2, h3 = [0] * 51, [0] * 51
    for k, hist in ((2, h2), (3, h3)):
        for left in combinations(others, k-1):
            left_set = set(left)
            available = tuple(j for j in others if j not in left_set)
            left_sum = _sum_ids(columns, left, m)
            for right in combinations(available, k):
                right_sum = _sum_ids(columns, right, m)
                residue = tuple((b-a) % 5 for a,b in zip(left_sum, right_sum))
                legal_index = index_by_residue.get(residue)
                if legal_index is not None:
                    hist[legal_index] += 1
    bad_r3 = frozenset(j for j, value in enumerate(h3) if value > 0)
    bad_r2 = frozenset(j for j, value in enumerate(h2)
                       if value > h2[old_index])
    safe = frozenset(range(51)) - bad_r2 - bad_r3
    return {
        "h2": tuple(h2), "h3": tuple(h3),
        "old_palette": old_index,
        "bad_r2": bad_r2, "bad_r3": bad_r3,
        "safe": safe,
        "safe_exact_count": 51-len(bad_r2 | bad_r3),
        "safe_union_lower_bound": max(0,51-len(bad_r2)-len(bad_r3)),
        "legal_columns": legal,
    }


def predicted_remaining(original_events, edited_ids):
    """Composed no-new-event deletion law. Feasibility is a separate gate."""
    touched = set(edited_ids)
    return frozenset(e for e in original_events
                     if touched.isdisjoint(e[0]) and touched.isdisjoint(e[1]))


def exact_hitting_number(event_sets):
    """Tiny independent exact vertex-cover oracle, NOT for full W34 search."""
    edges = [frozenset(e[0]) | frozenset(e[1]) for e in event_sets]
    if not edges:
        return 0
    vertices = sorted(set().union(*edges))
    if len(vertices) > 18:
        raise ValueError("tiny-event exact-cover oracle only (at most 18 IDs)")
    for size in range(len(vertices)+1):
        for chosen in combinations(vertices, size):
            selected = set(chosen)
            if all(not edge.isdisjoint(selected) for edge in edges):
                return size
    raise AssertionError("nonempty finite hypergraph must have a vertex cover")


def greedy_disjoint_witness_lower_bound(event_sets):
    """Any explicit disjoint-edge packing lower-bounds the transversal size."""
    edges = sorted((frozenset(e[0]) | frozenset(e[1]) for e in event_sets),
                   key=lambda x: tuple(sorted(x)))
    taken, count = set(), 0
    for edge in edges:
        if taken.isdisjoint(edge):
            taken.update(edge)
            count += 1
    return count
