"""HYP-105 G5-C2: exact signed-trade conflict spectrum and alteration frontier.

This file proves/implements only a classical first-moment conditional
extraction lemma and enumerates finite GF(5) unit-support-four models.
It does NOT prove a new asymptotic bound for ASET.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import json
import random

from test_hyp105_g5b_graph_realization import (
    canonical_pair_embedding, quadrangle_w32
)
from test_hyp105_g5c_signed_oracles import direct_aset_collision


def bitset(indices):
    out = 0
    for i in indices:
        out |= 1 << i
    return out


def sum_signature(columns, subset):
    """Direct integer sums for unit columns, subsets of size <=3."""
    m = len(columns[0])
    acc = [0] * m
    for i in subset:
        for j, x in enumerate(columns[i]):
            acc[j] += x
    return tuple(acc)


def gf5_unit_four(columns):
    """Certify the restricted unit model required by fast collision census."""
    if len(set(columns)) != len(columns):
        raise ValueError("duplicate columns")
    if columns and len({len(c) for c in columns}) != 1:
        raise ValueError("inconsistent dimensions")
    if any(sum(x == 1 for x in col) != 4 or
           any(x not in (0, 1) for x in col) for col in columns):
        raise ValueError("expected exactly four 1 entries per column")


def collision_spectrum(columns):
    """All inclusion-minimal invalid column supports in GF(5), unit weight 4.

    Cardinalities 0..3 are distinguished by the coordinate-sum functional
    (each column has sum 4, p=5), and uniqueness removes 1-vs-1.
    Hence all collisions reduce to 2-vs-2 or disjoint 3-vs-3.
    A 3-vs-3 collision with an overlapping column reduces to 2-vs-2.
    """
    gf5_unit_four(columns)
    conflict4 = set()
    conflict6 = set()
    pairs = defaultdict(list)
    for pair in combinations(range(len(columns)), 2):
        pairs[sum_signature(columns, pair)].append(bitset(pair))
    for bucket in pairs.values():
        for a, b in combinations(bucket, 2):
            if a & b:
                raise AssertionError("pair sums sharing a column cannot collide")
            conflict4.add(a | b)

    triples = defaultdict(list)
    for triple in combinations(range(len(columns)), 3):
        triples[sum_signature(columns, triple)].append(bitset(triple))
    for bucket in triples.values():
        for a, b in combinations(bucket, 2):
            overlap = a & b
            if overlap:
                # Overlap of size 1 reduces the collision to a 2-vs-2 trade;
                # overlap of size 2 would force duplicated columns.
                rest = (a | b) ^ overlap
                if rest.bit_count() == 4:
                    if rest not in conflict4:
                        raise AssertionError("overlap 3/3 must yield pair collision")
                else:
                    raise AssertionError("unexpected overlapping triple collision")
            else:
                conflict6.add(a | b)

    # Minimal support sets, NOT multiplicities of sign assignments. If a
    # 6-set already contains any 4-set conflict, discard it as nonminimal.
    minimal6 = {s for s in conflict6 if not any((s & t) == t
                                                  for t in conflict4)}
    return tuple(sorted(conflict4)), tuple(sorted(minimal6))


def has_forbidden_core(mask, conflicts):
    return any(mask & core == core for core in conflicts)


def optimize_first_moment(n, conflicts, granularity=128):
    """Finite rational-grid optimum of E[|S|-#present minimal cores]."""
    spectrum = defaultdict(int)
    for mask in conflicts:
        spectrum[mask.bit_count()] += 1
    # Decimal comparison is only for choosing a candidate grid point. The
    # actual certificate and derandomization use exact rational arithmetic.
    best = max(range(granularity + 1),
               key=lambda k: (n * (k/granularity) -
                              sum(t * (k/granularity)**s
                                  for s, t in spectrum.items()),
                              -k))
    p = Fraction(best, granularity)
    expectation = p * n - sum(count * p**size
                            for size, count in spectrum.items())
    return p, expectation


def conditional_expectation_extract(n, conflicts, p):
    """Deterministic conditional-expectation alteration with exact rationals.

    For variable i, including it changes conditional expected score by:
      1 - sum_{H contains i, no prior exclusion} p^{future(H)}.
    This is exact even with overlapping hyperedges.
    Drop one index from each surviving core to obtain an ASET subset.
    """
    if not isinstance(p, Fraction) or not 0 <= p <= 1:
        raise ValueError("expected Fraction probability in [0,1]")
    memberships = [[] for _ in range(n)]
    for edge in conflicts:
        if edge == 0 or edge >> n:
            raise ValueError("invalid hyperedge")
        for i in range(n):
            if edge >> i & 1:
                memberships[i].append(edge)

    selected = 0
    excluded = 0
    for i in range(n):
        delta = Fraction(1)
        for edge in memberships[i]:
            if edge & excluded:
                continue
            # All previous indices in edge must already be selected.
            future = (edge >> (i + 1)).bit_count()
            delta -= p**future
        if delta >= 0:
            selected |= 1 << i
        else:
            excluded |= 1 << i

    original_score = selected.bit_count() - sum(
        selected & edge == edge for edge in conflicts)
    expected = n * p - sum(p**edge.bit_count() for edge in conflicts)
    if original_score < expected:
        raise AssertionError("conditional expectation invariant violated")

    # Deterministic cleaning: remove one endpoint from a surviving conflict,
    # choosing max live forbidden-degree (ties resolved by lower column ID).
    cleaned = selected
    while True:
        present = [c for c in conflicts if cleaned & c == c]
        if not present:
            break
        degrees = [sum(c >> i & 1 for c in present) if cleaned >> i & 1
                   else -1 for i in range(n)]
        removed = max(range(n), key=lambda i: (degrees[i], -i))
        cleaned &= ~(1 << removed)
    return selected, cleaned, expected, original_score


def validate_cleaned(columns, cleaned_mask, conflicts):
    if has_forbidden_core(cleaned_mask, conflicts):
        return False
    chosen = tuple(c for i, c in enumerate(columns)
                   if cleaned_mask >> i & 1)
    return direct_aset_collision(chosen, 5, 3) is None


def w32_columns(seed=None):
    """45 graph edges on GF(5)^12, bijective pair-label permutations."""
    _, edges = quadrangle_w32()
    if seed is not None:
        rng = random.Random(seed)
        left, right = list(range(15)), list(range(15))
        rng.shuffle(left)
        rng.shuffle(right)
        edges = tuple((left[i], right[j]) for i, j in edges)
    return canonical_pair_embedding(edges, 15, 15, 6, 6)


def density_report(seed=None, granularity=128):
    columns = w32_columns(seed)
    c4, c6 = collision_spectrum(columns)
    allcores = c4 + c6
    p, score = optimize_first_moment(len(columns), allcores, granularity)
    initial, cleaned, certified, actual_score = conditional_expectation_extract(
        len(columns), allcores, p)
    if score != certified:
        raise AssertionError("incompatible rational first-moment scores")
    if not validate_cleaned(columns, cleaned, allcores):
        raise AssertionError("extracted family violates ASET")
    return {
        "model": "GF5 unit support4, W(3,2) canonical pair graph (not ASET)",
        "seed": "identity" if seed is None else seed,
        "ambient_m": 12,
        "base_columns": len(columns),
        "minimal_t4": len(c4),
        "minimal_t6": len(c6),
        "grid_probability": str(p),
        "expectation_lower": str(score),
        "selected_before_clean": initial.bit_count(),
        "preclean_score": actual_score,
        "certified_aset_columns": cleaned.bit_count(),
        "selected_column_ids": [i for i in range(len(columns))
                                if cleaned >> i & 1],
        "no_new_exponent_claim": True,
    }


if __name__ == "__main__":
    print(json.dumps([density_report(seed) for seed in (None, 0, 1, 2)],
                     indent=2, ensure_ascii=False, sort_keys=True))
