"""HYP-105 G5-D: exact GF5 affine-weight signed-trade probability theorem.

For any prescribed signed support incidence, the unconstrained-nonzero
(checksum=4, *zeros allowed*) collision probability is exactly 5^(C-V)
if each component has signed checksum balance, else zero. Explicitly
distinguishes this from the all-nonzero 51-option admissible palette.
"""
from collections import defaultdict
from fractions import Fraction

Q = 5
CHECKSUM = 4


def gf5_rank(rows):
    """Independently computed exact row rank via modular Gaussian elimination."""
    matrix = [list(row) for row in rows]
    if not matrix:
        return 0
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("ragged coefficient matrix")
    if any(not isinstance(x, int) for row in matrix for x in row):
        raise ValueError("integer GF5 coefficients required")
    for row in matrix:
        for j in range(width):
            row[j] %= Q
    rank = 0
    for col in range(width):
        pivot = next((i for i in range(rank, len(matrix))
                      if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inv = pow(matrix[rank][col], Q - 2, Q)
        matrix[rank] = [(x * inv) % Q for x in matrix[rank]]
        for i in range(len(matrix)):
            if i != rank and matrix[i][col]:
                factor = matrix[i][col]
                matrix[i] = [(x - factor*y) % Q
                             for x, y in zip(matrix[i], matrix[rank])]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def trade_linear_system(supports, signs):
    """Matrix of checksum rows and coordinate equality rows.

    Unknown one GF5 coefficient per incidence (column i, coordinate j).
    All t checksum RHS values =4, all coordinate RHS values =0.
    Coordinate equation has sign +-1 depending on the trade side.
    """
    t = len(supports)
    if t == 0 or len(signs) != t or any(x not in (-1, 1) for x in signs):
        raise ValueError("nonempty supports and valid +/-1 signs required")
    if any(len(row) != 4 or len(set(row)) != 4
           or any(not isinstance(x, int) or x < 0 for x in row)
           for row in supports):
        raise ValueError("four distinct nonnegative coordinates per column")
    coords = tuple(sorted(set(c for row in supports for c in row)))
    pos = {coord: k for k, coord in enumerate(coords)}
    r = t + len(coords)
    width = 4 * t
    matrix = [[0] * width for _ in range(r)]
    rhs = [CHECKSUM] * t + [0] * len(coords)
    incidence_degrees = defaultdict(int)
    for i, row in enumerate(supports):
        for j, coord in enumerate(row):
            k = 4*i + j
            matrix[i][k] = 1
            matrix[t+pos[coord]][k] = signs[i] % Q
            incidence_degrees[coord] += 1
    return matrix, rhs, coords, dict(incidence_degrees)


def incidence_components(supports):
    """Independent union-find on column and physical-coordinate nodes."""
    t = len(supports)
    coords = tuple(sorted(set(c for row in supports for c in row)))
    pos = {c: t+i for i, c in enumerate(coords)}
    n = t + len(coords)
    parents = list(range(n))

    def root(x):
        while x != parents[x]:
            x = parents[x]
        return x

    for i, row in enumerate(supports):
        for c in row:
            a, b = root(i), root(pos[c])
            if a != b:
                parents[b] = a
    groups = defaultdict(list)
    for i in range(t):
        groups[root(i)].append(i)
    return tuple(tuple(ids) for ids in sorted(groups.values())), len(coords)


def signed_trade_rank_report(supports, signs):
    matrix, rhs, coords, degrees = trade_linear_system(supports, signs)
    t = len(supports)
    components, v = incidence_components(supports)
    C = len(components)
    rank = gf5_rank(matrix)
    augmented_rank = gf5_rank(tuple(row + [rhs[i]]
                                    for i, row in enumerate(matrix)))
    predicted = t + v - C
    if rank != predicted:
        raise AssertionError("bipartite incidence rank theorem falsified")
    balanced = all(sum(signs[i] for i in group) % Q == 0
                   for group in components)
    if (augmented_rank == rank) != balanced:
        raise AssertionError("affine signed RHS consistency theorem falsified")
    if balanced:
        # Each of t columns chosen uniformly from q^3 checksum-fiber
        # vectors; # solutions = q^(4t-rank), probability q^(t-rank)
        probability = Fraction(1, Q**(v-C))
        solutions = Q**(4*t-rank)
        nonzero_probability_upper = min(
            Fraction(1), probability * Fraction(125, 51)**t)
    else:
        probability = Fraction(0)
        solutions = 0
        nonzero_probability_upper = Fraction(0)
    if any(degree == 1 for degree in degrees.values()):
        # A singleton coordinate equality forces one coefficient to 0,
        # impossible when all t columns must retain support-exact-four.
        nonzero_probability_upper = Fraction(0)
    return {
        "t": t, "v": v, "components": C, "support_components": components,
        "rank": rank, "augmented_rank": augmented_rank,
        "affine_consistent": balanced,
        "affine_solution_count": solutions,
        "full_affine_probability": probability,
        "nonzero_palette_upper": nonzero_probability_upper,
        "has_singleton_coordinate": any(d == 1 for d in degrees.values()),
    }
