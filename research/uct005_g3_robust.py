#!/usr/bin/env python3
"""UCT-005 G3-A: robust observable-state packing and exact sparse near-trades.

Mathematically proved classical composition; finite static witnesses only.
No cryptographic security, physical IO or asymptotic originality asserted.
"""
from functools import lru_cache
from itertools import combinations, product
from math import comb


def _nonnegative(value):
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def volume(q, cells, radius):
    """q-ary Hamming ball cardinality, clipping radius to cell count."""
    if not (_nonnegative(q) and q >= 2 and _nonnegative(cells)
            and _nonnegative(radius)):
        raise ValueError("q>=2, cells>=0, radius>=0 required")
    return sum(comb(cells, i) * (q - 1) ** i
               for i in range(min(cells, radius) + 1))


def potential_query_nodes(q, probes):
    """All possible addresses in a depth-P q-ary adaptive query tree."""
    if not (_nonnegative(q) and q >= 2 and _nonnegative(probes)):
        raise ValueError("bad alphabet or probe count")
    return sum(q ** i for i in range(probes))


def possible_probe_support(q, cells, query_count, probes):
    if not (_nonnegative(cells) and _nonnegative(query_count)
            and query_count >= 1):
        raise ValueError("nonempty query suite and valid cells required")
    return min(cells, query_count * potential_query_nodes(q, probes))


def robust_packing_bound(q, cells, update_depth, max_edge_changes,
                         error_symbols, query_count, probes, trusted_bits):
    """ROST-A bound, integer exact. Necessary, not an achievable capacity."""
    if not all(map(_nonnegative, (update_depth, max_edge_changes,
                                  error_symbols, trusted_bits))):
        raise ValueError("bad update, error or trusted-bit budget")
    m = possible_probe_support(q, cells, query_count, probes)
    radius = update_depth * max_edge_changes
    return (1 << trusted_bits) * max(
        volume(q, size, radius + error_symbols) //
        volume(q, size, error_symbols)
        for size in range(m + 1)
    )


def hamming(a, b):
    if len(a) != len(b):
        raise ValueError("unequal-length words")
    return sum(x != y for x, y in zip(a, b))


def ball_words(q, cells, radius):
    if not (_nonnegative(q) and q >= 2 and _nonnegative(cells)
            and _nonnegative(radius)):
        raise ValueError("invalid ball parameters")
    return tuple(word for word in product(range(q), repeat=cells)
                 if sum(value != 0 for value in word) <= radius)


def exact_ball_packing(q, cells, radius, error_symbols):
    """Exact max error-correcting code contained in ball, small instances.

    Maximum clique search on pairwise distance>=2e+1 compatibility graph.
    Exponential and guarded intentionally. This is an ORACLE, not an algorithm.
    """
    if not (_nonnegative(error_symbols) and _nonnegative(cells)
            and _nonnegative(radius)):
        raise ValueError("invalid error or dimensions")
    words = ball_words(q, cells, radius)
    if len(words) > 22:
        raise ValueError("finite clique oracle restricts candidate count <=22")
    n = len(words)
    neighbors = []
    for i in range(n):
        bits = 0
        for j in range(n):
            if i != j and hamming(words[i], words[j]) >= 2 * error_symbols + 1:
                bits |= 1 << j
        neighbors.append(bits)

    @lru_cache(None)
    def maximum_clique(mask):
        if not mask:
            return 0
        lowbit = mask & -mask
        vertex = lowbit.bit_length() - 1
        without = mask ^ lowbit
        return max(maximum_clique(without),
                   1 + maximum_clique(without & neighbors[vertex]))

    return maximum_clique((1 << n) - 1)


def sparse_masks(items, max_support):
    if not (_nonnegative(items) and _nonnegative(max_support)):
        raise ValueError("bad sparse update model")
    return tuple(sum(1 << i for i in chosen)
                 for size in range(min(items, max_support) + 1)
                 for chosen in combinations(range(items), size))


def field_is_prime(q):
    if not (isinstance(q, int) and not isinstance(q, bool) and q >= 2):
        return False
    return all(q % i for i in range(2, int(q ** 0.5) + 1))


def encode_subset(columns, row_count, q, mask):
    """GF(p) field for PRIME p only; q-prime-powers need real GF arithmetic."""
    if not field_is_prime(q) or not _nonnegative(row_count):
        raise ValueError("only GF(prime) oracle is implemented")
    if not (_nonnegative(mask) and mask < (1 << len(columns))):
        raise ValueError("bad subset mask")
    if any(len(col) != row_count for col in columns):
        raise ValueError("invalid matrix column size")
    return tuple(sum(columns[i][j] for i in range(len(columns))
                     if mask & (1 << i)) % q for j in range(row_count))


def near_trade_witness(columns, row_count, q, max_support, errors):
    """Return pair of distinct sparse subsets whose syndromes differ <=2e."""
    if not _nonnegative(errors):
        raise ValueError("errors must be nonnegative")
    subsets = sparse_masks(len(columns), max_support)
    syndromes = {
        subset: encode_subset(columns, row_count, q, subset)
        for subset in subsets
    }
    for i, first in enumerate(subsets):
        for second in subsets[i + 1:]:
            dist = hamming(syndromes[first], syndromes[second])
            if dist <= 2 * errors:
                return (first, second, dist)
    return None


def sparse_code_capacity_bound(q, rows, columns, max_support,
                               per_column_support, error_symbols):
    """Necessity only when all sparse subsets are distinguished."""
    if not (_nonnegative(columns) and _nonnegative(rows) and
            _nonnegative(max_support) and _nonnegative(per_column_support)
            and _nonnegative(error_symbols)):
        raise ValueError("invalid dimensions")
    left = sum(comb(columns, i) for i in
               range(min(columns, max_support) + 1))
    return (left * volume(q, rows, error_symbols),
            volume(q, rows, max_support * per_column_support
                   + error_symbols))


def nearest_unique_decode(codebook, observed, radius):
    """Error-tolerant exact decoder; None for no hit or ambiguous hit."""
    if not _nonnegative(radius):
        raise ValueError("invalid decoder radius")
    possible = [key for key, word in codebook.items()
                if hamming(word, observed) <= radius]
    return possible[0] if len(possible) == 1 else None
