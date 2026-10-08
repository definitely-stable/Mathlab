"""TOM-006 source-only COPY/ADD: deliberately optimistic proof-model floor.

Not a VCDIFF parser, encoder, runtime library, or production wire certificate.
No claim that computing q-gram membership is free for an actual product.
"""


def absent_windows(base, target, q):
    """Count positions with a target q-window absent from contiguous base."""
    if not isinstance(base, bytes) or not isinstance(target, bytes):
        raise TypeError("base and target must be bytes")
    if not isinstance(q, int) or q < 1:
        raise ValueError("q must be a positive integer")
    if q > len(target):
        return 0
    source = {base[i:i + q] for i in range(len(base) - q + 1)}
    return sum(target[i:i + q] not in source
               for i in range(len(target) - q + 1))


def optimistic_floor(base, target, max_q=2, add_charge=1, copy_charge=2):
    """Safe lower bound in frozen flat-charge toy units, not actual wire bytes.

    Minimize a relaxation over L literal bytes and C source-only COPYs.
    Includes C*len(base)>=len(target)-L and no empty instructions.
    Real ADD cost is L + add_charge * number_of_ADD_instructions,
    so charging just one ADD when L>0 deliberately undercharges.
    """
    if not isinstance(base, bytes) or not isinstance(target, bytes):
        raise TypeError("base and target must be bytes")
    if not isinstance(max_q, int) or max_q < 1:
        raise ValueError("max_q must be a positive integer")
    if (not isinstance(add_charge, int) or add_charge < 1
            or not isinstance(copy_charge, int) or copy_charge < 1):
        raise ValueError("instruction charges must be positive integers")
    n, m = len(target), len(base)
    if n == 0:
        return 0
    missing = [(q, absent_windows(base, target, q))
               for q in range(1, min(n, max_q) + 1)]
    best = None
    for literals in range(n + 1):
        copied = n - literals
        for copies in range(copied + 1):
            if copies == 0 and copied:
                continue
            if copies > 0 and (m == 0 or copies * m < copied):
                continue
            if any(u > q * literals + (q - 1) * max(copies - 1, 0)
                   for q, u in missing):
                continue
            possible_cost = (literals
                             + (add_charge if literals else 0)
                             + copy_charge * copies)
            if best is None or possible_cost < best:
                best = possible_cost
    if best is None:
        raise AssertionError("all-literal admissible relaxation disappeared")
    return best


if __name__ == "__main__":
    for width in (2, 4, 8, 16):
        base = b"a" * width + b"bb" + b"a" * width
        target = b"ab" * width
        assert optimistic_floor(base, target, max_q=2) == 2
    print("TOM-006 toy q<=2 adversarial-floor smoke: PASS")
