"""UCT-005 G2-B2: elementary GF(2) multi-subscriber broadcast model.

Code is an EXACT finite mathematical oracle. It neither implements nor proves
authenticated broadcasting and must not be treated as a novel theorem.
"""
from itertools import product


def syndrome(rows, delta):
    """Encode all subscribers' output changes as a little-endian bit mask."""
    return sum(((row & delta).bit_count() & 1) << j
               for j, row in enumerate(rows))


def image_set(rows, deltas):
    return frozenset(syndrome(rows, d) for d in deltas)


def min_fixed_broadcast_bits(rows, deltas):
    assert deltas, "the allowed update alphabet must be nonempty"
    distinct = len(image_set(rows, deltas))
    return (distinct - 1).bit_length()


def rank_gf2(rows):
    """Exact GF(2) row rank; integer bit-mask Gaussian elimination."""
    basis = {}
    for word in rows:
        r = word
        while r:
            high = r.bit_length() - 1
            if high in basis:
                r ^= basis[high]
            else:
                basis[high] = r
                break
    return len(basis)


def encode_and_decode(rows, deltas):
    """Canonical nonuniform quotient codebook; setup size MUST be charged."""
    words = sorted(image_set(rows, deltas))
    code = {w: i for i, w in enumerate(words)}
    return code, tuple(words)


def iter_all_binary_matrices(rows, cols):
    for mask in range(1 << (rows * cols)):
        yield tuple((mask >> (i * cols)) & ((1 << cols) - 1)
                    for i in range(rows))


def all_nonempty_update_alphabets(m):
    space = 1 << m
    for mask in range(1, 1 << space):
        yield tuple(d for d in range(space) if mask & (1 << d))


def conflict_colors_exact(rows, deltas, colors):
    """Independent brute-force K-color test; no quotient formula used.

    Contradiction on equal-message pairs with different per-subscriber delta.
    This enumerates all assignments d -> broadcast color.
    """
    words = list(deltas)
    for assign in product(range(colors), repeat=len(words)):
        valid = True
        for i, d in enumerate(words):
            for j in range(i):
                if assign[i] == assign[j]:
                    if any(((row & d).bit_count() ^ (row & words[j]).bit_count()) & 1
                           for row in rows):
                        valid = False
                        break
            if not valid:
                break
        if valid:
            return True
    return False


def apply_message(rows, outputs, message, codewords):
    """One publisher message; independent subscribers keep only their output."""
    changes = codewords[message]
    return tuple(bit ^ ((changes >> i) & 1)
                 for i, bit in enumerate(outputs))


def outputs_for(rows, state):
    return tuple((row & state).bit_count() & 1 for row in rows)
