"""HYP-105 G3: exhaustive finite core configuration and integer minor certificate.

For a minimal dependence among <=6 unit incidence columns of a *linear*
3-uniform hypergraph, every row has >=2 nonzero entries. Enumerate row
patterns up to permutation of rows (vertex relabeling), keeping edge IDs
labelled. Check maximal integer minor gcds; gcd mod p controls rank.

This is a small fully reproducible computer-assisted proof, not a novelty
claim and not an asymptotic graph-construction implementation.
"""
from collections import Counter
from itertools import combinations
from math import gcd


def used_columns(mask, columns):
    return tuple(j for j in range(columns) if mask & (1 << j))


def core_patterns(columns):
    """Enumerate every row-unlabelled min-degree-2 linear triple core.

    A row describes the set of selected edges incident to one hypergraph
    vertex. Every selected edge has exactly three vertices, and no pair of
    edges can meet at more than one vertex. Rows are strictly increasing
    bitmasks: no vertex labels are relevant for field-linear dependence.
    """
    if not 1 <= columns <= 6:
        raise ValueError("finite certificate restricted to 1..6 edges")
    options = []
    for mask in range(1, 1 << columns):
        ids = used_columns(mask, columns)
        if len(ids) < 2:
            continue
        pairmask = sum(1 << (i * columns + j) for i, j in combinations(ids, 2))
        options.append((mask, ids, pairmask))
    counts = [0] * columns
    chosen = []

    def generate(start, used_pairs):
        if all(deg == 3 for deg in counts):
            yield tuple(chosen)
            return
        for idx in range(start, len(options)):
            mask, ids, pairs = options[idx]
            if pairs & used_pairs or any(counts[j] == 3 for j in ids):
                continue
            for j in ids:
                counts[j] += 1
            chosen.append(mask)
            yield from generate(idx + 1, used_pairs | pairs)
            chosen.pop()
            for j in ids:
                counts[j] -= 1

    yield from generate(0, 0)


def determinant_bareiss(square):
    """Exact fraction-free integer determinant, including row-pivot sign."""
    n = len(square)
    if any(len(row) != n for row in square):
        raise ValueError("expected a square matrix")
    if n == 0:
        return 1
    a = [list(row) for row in square]
    previous = 1
    sign = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            j = next((j for j in range(k + 1, n) if a[j][k] != 0), None)
            if j is None:
                return 0
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                if numerator % previous:
                    raise AssertionError("Bareiss exact-division invariant failed")
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[n - 1][n - 1]


def maximal_minor_gcd(rows, columns):
    """Exact gcd of every columns×columns integral incidence minor."""
    if len(rows) < columns:
        return 0
    vectors = [[int(bool(mask & (1 << c))) for c in range(columns)]
               for mask in rows]
    result = 0
    for positions in combinations(range(len(rows)), columns):
        result = gcd(result, determinant_bareiss([vectors[i] for i in positions]))
        if result == 1:
            break
    return result


def is_grid(rows, columns):
    """Independent combinatorial 3×3 detector on the core's edge incidence."""
    if columns != 6 or len(rows) != 9 or any(mask.bit_count() != 2 for mask in rows):
        return False
    # A grid has a bipartition of six edges, with each pair (L,R)
    # appearing in exactly one of its nine degree-two vertex rows.
    for left in combinations(range(columns), 3):
        left_mask = sum(1 << i for i in left)
        if all((mask & left_mask).bit_count() == 1 for mask in rows):
            return True
    return False


def rank_mod_prime(rows, columns, prime):
    """Independent modular Gaussian elimination, no integer minors involved."""
    if prime < 2:
        raise ValueError("invalid prime")
    a = [[(mask >> j) & 1 for j in range(columns)] for mask in rows]
    rank = 0
    for col in range(columns):
        pivot = next((i for i in range(rank, len(a)) if a[i][col] % prime), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, prime)
        for j in range(col, columns):
            a[rank][j] = a[rank][j] * inv % prime
        for i in range(rank + 1, len(a)):
            x = a[i][col] % prime
            if x:
                for j in range(col, columns):
                    a[i][j] = (a[i][j] - x * a[rank][j]) % prime
        rank += 1
    return rank


def classification():
    return {t: Counter(maximal_minor_gcd(rows, t) for rows in core_patterns(t))
            for t in range(1, 7)}


if __name__ == "__main__":
    for t, hist in classification().items():
        print("t=", t, "minor_gcd_counts=", dict(sorted(hist.items())))
