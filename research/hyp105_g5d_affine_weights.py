"""HYP-105 G5-D: affine checksum-constrained GF5 weighted sparse ASET.

Elementary all-m checksum/cardinality theorem plus EXACT FINITE constructive
45-column W(3,2) witness at m=12. This does NOT prove a new asymptotic
bound or the scientific originality of an extremal theorem.
"""
from itertools import product
from random import Random
import json

from test_hyp105_g5b_graph_realization import (
    canonical_pair_embedding, quadrangle_w32
)
from test_hyp105_g5c_signed_oracles import direct_aset_collision

P = 5
M = 12
RADICES = tuple(P**i for i in range(M))
CHECKSUM = 4


def checksum_pattern_palette():
    """Every support4 nonzero coefficient tuple with sum=4 (mod 5)."""
    result = tuple(w for w in product(range(1, P), repeat=4)
                   if sum(w) % P == CHECKSUM)
    if len(result) != 51:
        raise AssertionError("GF5 affine palette should have 51 members")
    return result


def w32_supports():
    _, edges = quadrangle_w32()
    result = canonical_pair_embedding(edges, 15, 15, 6, 6)
    if len(result) != 45 or len(set(result)) != 45:
        raise AssertionError("expected simple W32 with 45 support4 edges")
    return result


def encode_support(support, pattern):
    """Base-five field vector encoding, not ordinary integer sum arithmetic."""
    if len(support) != 4 or len(set(support)) != 4:
        raise ValueError("support must have four distinct coordinates")
    if len(pattern) != 4 or any(x not in range(1, P) for x in pattern):
        raise ValueError("GF5 pattern must have four nonzero values")
    if sum(pattern) % P != CHECKSUM:
        raise ValueError("GF5 pattern violates constant affine checksum")
    if any(c < 0 or c >= M for c in support):
        raise ValueError("coordinate out of bounds")
    return sum(w * RADICES[c] for c, w in zip(support, pattern))


def add_field_encoded(a, b):
    """Exact digitwise GF5 addition with modular reduction (NO integer carry)."""
    if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
        raise ValueError("nonnegative field encoding required")
    if a >= P**M or b >= P**M:
        raise ValueError("encoded vector outside GF5^12")
    result = 0
    for power in RADICES:
        ai, a = a % P, a // P
        bi, b = b % P, b // P
        result += ((ai + bi) % P) * power
    return result


def decode_field(encoded):
    if not isinstance(encoded, int) or not 0 <= encoded < P**M:
        raise ValueError("encoded field vector outside GF5^12")
    result = []
    for _ in range(M):
        result.append(encoded % P)
        encoded //= P
    return tuple(result)


def finite_weighted_greedy(seed=20261009, max_attempts=4):
    """Exact incremental 0..3-subset-sum validator and deterministic search.

    Invariant: old k-subset signatures are unique for each k=0,1,2,3.
    For new x, new k-sums are x + old(k-1)-sums; they are mutually
    distinct by injectivity of group translation. Need only check their
    DISJOINTNESS from all old k-sums. Different sizes cannot collide
    because every selected x has constant nonzero coordinate checksum.
    """
    if max_attempts < 1:
        raise ValueError("at least one attempt required")
    rng = Random(seed)
    supports = w32_supports()
    palette = checksum_pattern_palette()
    best = None
    for attempt in range(max_attempts):
        order = list(range(len(supports)))
        rng.shuffle(order)
        old = [set([0]), set(), set(), set()]
        assignments = {}
        for colid in order:
            choices = list(palette)
            rng.shuffle(choices)
            accepted = None
            for pattern in choices:
                encoded = encode_support(supports[colid], pattern)
                if encoded in old[1]:
                    continue
                new_two = tuple(add_field_encoded(encoded, x) for x in old[1])
                if any(x in old[2] for x in new_two):
                    continue
                new_three = tuple(add_field_encoded(encoded, x) for x in old[2])
                if any(x in old[3] for x in new_three):
                    continue
                accepted = encoded, pattern, new_two, new_three
                break
            if accepted is None:
                break
            encoded, pattern, new_two, new_three = accepted
            assignments[colid] = pattern
            # Precomputed new k-sums only involve old signatures, not
            # this candidate twice. Safe to mutate after both checks.
            old[3].update(new_three)
            old[2].update(new_two)
            old[1].add(encoded)
        if best is None or len(assignments) > len(best[1]):
            best = (attempt, assignments.copy(), order)
        if len(assignments) == len(supports):
            break
    attempt, assignments, order = best
    vectors = tuple(
        decode_field(encode_support(supports[i], assignments[i]))
        for i in sorted(assignments))
    return {
        "seed": seed, "attempt": attempt, "m": M,
        "input_supports": len(supports),
        "accepted_columns": len(vectors),
        "checksum": CHECKSUM,
        "palette_size": len(palette),
        "column_ids": tuple(sorted(assignments)),
        "patterns": tuple(tuple(assignments[i]) for i in sorted(assignments)),
        "vectors": vectors,
        "collision": direct_aset_collision(vectors, P, 3),
        "asymptotic_improvement_proven": False,
    }


def verify_independent_full_sums(vectors):
    """Separate complete 12-coordinate GF5 vector-sum oracle, all k<=3."""
    if len(set(vectors)) != len(vectors):
        return False
    if any(len(v) != M or sum(x != 0 for x in v) != 4
           or sum(v) % 5 != CHECKSUM for v in vectors):
        return False
    seen = {}
    n = len(vectors)
    from itertools import combinations
    for k in range(4):
        for subset in combinations(range(n), k):
            summed = tuple(sum(vectors[i][j] for i in subset) % 5
                           for j in range(M))
            if summed in seen:
                return False
            seen[summed] = subset
    return len(seen) == sum(__import__("math").comb(n, k) for k in range(4))


def summary(seed=20261009):
    result = finite_weighted_greedy(seed)
    return {
        "model": "45 W(3,2) 2+2 fixed supports, GF5 weighted affine checksum4, m12",
        "seed": result["seed"],
        "accepted": result["accepted_columns"],
        "source_columns": result["input_supports"],
        "attempt": result["attempt"],
        "checksum": result["checksum"],
        "patterns": result["patterns"],
        "column_ids": result["column_ids"],
        "independent_full_sum_oracle_pass":
            verify_independent_full_sums(result["vectors"]),
        "old_oracle_no_collision": result["collision"] is None,
        "scientific_novelty_unverified": True,
        "new_asymptotic_exponent_proven": False,
    }


if __name__ == "__main__":
    print(json.dumps(summary(), sort_keys=True, indent=2))
