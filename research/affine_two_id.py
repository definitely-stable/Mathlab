#!/usr/bin/env python3
"""HYP-002-C index-free affine-STS two-ID codec: proof-oriented laboratory.

IMPORTANT: correctness is restricted to <=2 DISTINCT active IDs and a
trusted update sequence. Raw modulo-3 arithmetic is NOT an error detector.
Both the dense-state read and checked updates take Theta(m) time.

No library API or product GO is implied. Only Python standard library.
"""
from __future__ import annotations

from itertools import combinations
from math import comb

CanonicalID = tuple[int, int]
State = tuple[int, ...]


def size(rank: int) -> int:
    if not isinstance(rank, int) or not 1 <= rank <= 5:
        raise ValueError("rank must be integer in [1,5] (bounded lab only)")
    return 3 ** rank


def third(a: int, b: int, rank: int) -> int:
    """Unique third point on affine F3^rank line, O(rank), no ID table."""
    m = size(rank)
    if not (isinstance(a, int) and isinstance(b, int)
            and 0 <= a < m and 0 <= b < m and a != b):
        raise ValueError("two distinct point indices in range required")
    answer = 0
    place = 1
    x, y = a, b
    for _ in range(rank):
        da, db = x % 3, y % 3
        answer += ((-da - db) % 3) * place
        x //= 3
        y //= 3
        place *= 3
    return answer


def canonical_line(a: int, b: int, rank: int) -> CanonicalID:
    return tuple(sorted((a, b, third(a, b, rank)))[:2])  # type: ignore[return-value]


def line_points(identifier: CanonicalID, rank: int) -> tuple[int, int, int]:
    """Fail closed on non-canonical IDs: the first two indices MUST be lowest."""
    if not isinstance(identifier, tuple) or len(identifier) != 2:
        raise ValueError("ID must be a canonical pair")
    a, b = identifier
    z = third(a, b, rank)
    if not a < b < z:
        raise ValueError("non-canonical line ID (expected first two indices)")
    return a, b, z


def encode(ids: tuple[CanonicalID, ...], rank: int) -> State:
    """Trusted-set snapshot encoder: <=2 distinct canonical IDs only."""
    m = size(rank)
    if len(ids) > 2 or len(set(ids)) != len(ids):
        raise ValueError("capacity exceeded or duplicate active ID")
    state = [0] * m
    for ident in ids:
        for point in line_points(ident, rank):
            state[point] = (state[point] + 1) % 3
    return tuple(state)


def _is_line(points: tuple[int, int, int], rank: int) -> bool:
    return points[0] < points[1] < points[2] and (
        third(points[0], points[1], rank) == points[2]
    )


def decode(snapshot: State, rank: int) -> tuple[CanonicalID, ...] | None:
    """O(m+rank*20) decoding for promised <=2 valid distinct active IDs.

    Returns None for recognizably malformed yet well-formed trit arrays.
    Raises ValueError for invalid input shape/types/range.
    Cannot recognize all >2-ID states; an explicit 3->2 alias exists.
    """
    m = size(rank)
    if len(snapshot) != m or any(
        not isinstance(value, int) or not 0 <= value <= 2
        for value in snapshot
    ):
        raise ValueError("state must contain exactly m trits")
    ones: list[int] = []
    twos: list[int] = []
    for pos, value in enumerate(snapshot):
        if value == 1:
            ones.append(pos)
        elif value == 2:
            twos.append(pos)
        if len(ones) + len(twos) > 6:
            return None

    if not ones and not twos:
        return ()
    if len(ones) == 3 and not twos:
        triple = tuple(ones)
        return ((triple[0], triple[1]),) if _is_line(triple, rank) else None

    candidates: set[tuple[CanonicalID, CanonicalID]] = set()
    if len(ones) == 4 and len(twos) == 1:
        shared = twos[0]
        one_set = set(ones)
        # With two overlapping lines, both contain the shared point.
        # The four nonshared points partition into two pairs.
        for point in ones:
            mate = third(shared, point, rank)
            if mate == point or mate not in one_set:
                continue
            first = tuple(sorted((shared, point, mate)))
            if not _is_line(first, rank):
                continue
            remaining = one_set - {point, mate}
            if len(remaining) != 2:
                continue
            other = tuple(sorted((shared, *remaining)))
            if _is_line(other, rank):
                a, b = sorted(((first[0], first[1]), (other[0], other[1])))
                if a != b:
                    candidates.add((a, b))

    elif len(ones) == 6 and not twos:
        universe = set(ones)
        # At most C(6,3)=20 candidates; independent of V=m(m-1)/6.
        for triple in combinations(ones, 3):
            if not _is_line(triple, rank):
                continue
            other = tuple(sorted(universe - set(triple)))
            if _is_line(other, rank):
                a, b = sorted(((triple[0], triple[1]), (other[0], other[1])))
                if a != b:
                    candidates.add((a, b))
    else:
        return None

    if len(candidates) != 1:
        return None
    answer = tuple(sorted(next(iter(candidates))))
    # Fail closed on any bug in candidate classification.
    return answer if encode(answer, rank) == snapshot else None


def checked_transition(
    snapshot: State, rank: int, identifier: CanonicalID, add: bool
) -> State:
    """Logical membership correctness; must first decode/scan current state.

    Intentionally Theta(m), not a falsely advertised O(1) write.
    If a raw invalid sequence has aliased a legal state, no local
    checked_transition can discover its history.
    """
    line_points(identifier, rank)
    active = decode(snapshot, rank)
    if active is None:
        raise ValueError("not a valid <=2-ID snapshot")
    active_set = set(active)
    if add:
        if identifier in active_set:
            raise ValueError("duplicate insertion")
        if len(active_set) >= 2:
            raise ValueError("capacity exceeded")
        active_set.add(identifier)
    else:
        if identifier not in active_set:
            raise ValueError("missing deletion")
        active_set.remove(identifier)
    return encode(tuple(sorted(active_set)), rank)


def trusted_raw_update(snapshot: State, rank: int,
                       identifier: CanonicalID, delta: int) -> State:
    """Unsafe laboratory primitive: exactly 3 point writes, NO validity check.

    Preconditions are uncheckable from this function alone. In
    particular 3 distinct insertions can alias a valid 2-ID state.
    """
    m = size(rank)
    if len(snapshot) != m or any(type(v) is not int or v not in (0, 1, 2)
                                 for v in snapshot):
        raise ValueError("invalid trit snapshot")
    if delta not in (-1, 1):
        raise ValueError("delta must be +1 or -1")
    result = list(snapshot)
    for point in line_points(identifier, rank):
        result[point] = (result[point] + delta) % 3
    return tuple(result)


def storage_report(rank: int) -> dict[str, int | float]:
    """Bit-accounting gate: optimistic direct comparator vs dense state.

    Dense counters: >=ceil(m log2 3) theoretical bits, 2m binary-packed
    bits, m bytes in a byte-aligned implementation. Canonical IDs need
    only their first two point coordinates; 2 slots -> 4 ceil(log2 m)
    bits, plus occupancy metadata, with no V-entry lookup table.
    """
    m = size(rank)
    v = m * (m - 1) // 6
    states = 1 + v + comb(v, 2)
    lower_bound_bits = (states - 1).bit_length()
    point_bits = (m - 1).bit_length()
    direct_2id_bits = 4 * point_bits + 2  # two occupancy bits
    # math.ceil could round very large products; pinned rank <=5.
    import math
    ideal_dense_bits = math.ceil(m * math.log2(3))
    binary_dense_bits = 2 * m
    return {
        "rank": rank,
        "m": m,
        "V": v,
        "exact_states": states,
        "info_lower_bits": lower_bound_bits,
        "dense_trit_information_bits": ideal_dense_bits,
        "dense_2bit_bits": binary_dense_bits,
        "dense_byte_bits": 8 * m,
        "direct_two_canonical_ids_bits": direct_2id_bits,
        "trit_vs_direct_bits_ratio": round(ideal_dense_bits / direct_2id_bits, 3),
        "dense_2bit_vs_direct_bits_ratio": round(binary_dense_bits / direct_2id_bits, 3),
    }


def run_decoder_gate() -> None:
    """Finite exhaustive small-grid gate; tests provide fuller coverage."""
    from locality_transition import affine_sts_blocks
    for rank in (1, 2, 3):
        m, lines = affine_sts_blocks(rank)
        ids = tuple((line[0], line[1]) for line in lines)
        assert len(ids) == m * (m-1)//6
        checked = 0
        for family in [()] + [(x,) for x in ids] + list(combinations(ids, 2)):
            state = encode(family, rank)
            expected = tuple(sorted(family))
            assert decode(state, rank) == expected
            checked += 1
        print("HYP002C_EXHAUSTIVE", "rank", rank, "states", checked)

    alias_three = ((0, 1), (0, 3), (0, 4))
    alias_two = ((1, 3), (2, 4))
    zero = encode((), 2)
    over = zero
    for ident in alias_three:
        over = trusted_raw_update(over, 2, ident, +1)
    assert over == encode(alias_two, 2)
    assert decode(over, 2) == alias_two
    print("HYP002C_OVER_CAPACITY_ALIAS_PASS")
    print("HYP002C_EXHAUSTIVE_ORACLE_PASS")
    print("HYP002C_INDEX_FREE_DECODER_PASS")
    print("HYP002C_STORAGE_ACCOUNTING_PASS")
    for rank in (1, 2, 3, 4, 5):
        print("HYP002C_MEMORY", storage_report(rank))
    print("HYP002C_PHASE_A_PASS")


if __name__ == "__main__":
    run_decoder_gate()
