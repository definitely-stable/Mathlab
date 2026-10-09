#!/usr/bin/env python3
"""ALG-001 G0: exact finite-field rank oracle; no asymptotic speed claim."""
from itertools import product

from dag002_oracle import min_fixed_bits_for_states


def _prime(field):
    if not isinstance(field, int) or isinstance(field, bool) or field < 2:
        return False
    for d in range(2, int(field ** 0.5) + 1):
        if field % d == 0:
            return False
    return True


def rank_mod_prime(matrix, prime):
    """Independent textbook Gaussian elimination over a SMALL prime field."""
    if not _prime(prime):
        raise ValueError("modulus must be prime")
    rows = [list(row) for row in matrix]
    if not rows:
        return 0
    cols = len(rows[0])
    if any(len(row) != cols for row in rows):
        raise ValueError("ragged matrix")
    work = [[int(x) % prime for x in row] for row in rows]
    pivot_row = 0
    for col in range(cols):
        pivot = next((i for i in range(pivot_row, len(work))
                      if work[i][col] != 0), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][col], -1, prime)
        work[pivot_row] = [(x * inverse) % prime for x in work[pivot_row]]
        for i in range(len(work)):
            if i == pivot_row:
                continue
            factor = work[i][col]
            if factor:
                work[i] = [(x - factor * y) % prime for x, y
                           in zip(work[i], work[pivot_row])]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def all_matrices(prime, rows, cols):
    if not _prime(prime) or not 0 <= rows or not 0 <= cols:
        raise ValueError("invalid finite matrix family")
    for values in product(range(prime), repeat=rows * cols):
        yield tuple(tuple(values[i * cols:(i + 1) * cols])
                    for i in range(rows))


def entry_update(matrix, row, col, value):
    if not matrix:
        raise ValueError("empty matrix")
    if not 0 <= row < len(matrix) or not 0 <= col < len(matrix[0]):
        raise ValueError("out of bounds")
    clone = [list(x) for x in matrix]
    clone[row][col] = value
    return tuple(tuple(x) for x in clone)


def fixed_rank_one_rows(n, prime=2):
    """All nonzero 1-by-n rows have rank one (over any prime field)."""
    if not isinstance(n, int) or n < 1 or not _prime(prime):
        raise ValueError("invalid n/field")
    for values in product(range(prime), repeat=n):
        if any(values):
            yield (tuple(values),)


def rank_one_observation_lower_bits(n, prime=2):
    """Endpoint-only bit capacity for coordinate outputs, NOT a rank query."""
    if not isinstance(n, int) or n < 1 or not _prime(prime):
        raise ValueError("invalid n/field")
    return min_fixed_bits_for_states(prime ** n - 1)
