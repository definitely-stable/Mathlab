"""TOM-001-C: exact one-edit certificate-state oracle.

NOT a novel theorem. This implements the elementary distinction-profile
quotient for zero old-input probes and one bit-replacement query.

The verifier receives old output f(x), a retained metadata label h(x),
the edit index and new bit. Preprocessing/metadata maintenance is NOT
accounted for in this deliberately narrow finite calibration.
"""

from itertools import product


def input_states(n: int):
    if not 1 <= n <= 3:
        raise ValueError("finite reference oracle supports 1 <= n <= 3")
    return tuple(product((0, 1), repeat=n))


def index_of(x):
    position = 0
    for bit in x:
        position = 2 * position + bit
    return position


def output(table: int, x):
    n = len(x)
    if not 0 <= table < (1 << (1 << n)):
        raise ValueError("truth table out of range")
    return (table >> index_of(x)) & 1


def replace(x, index: int, value: int):
    if not 0 <= index < len(x) or value not in (0, 1):
        raise ValueError("invalid update")
    y = list(x)
    y[index] = value
    return tuple(y)


def response_profile(table: int, x):
    return tuple(
        output(table, replace(x, i, b))
        for i in range(len(x))
        for b in (0, 1)
    )


def exact_min_labels(table: int, n: int):
    """Exact quotient count, free old f(x) can distinguish output fibers."""
    if not 1 <= n <= 3:
        raise ValueError("reference bound: n<=3")
    fibers = {0: set(), 1: set()}
    for x in input_states(n):
        fibers[output(table, x)].add(response_profile(table, x))
    return max(len(fibers[0]), len(fibers[1]), 1)


def labels_are_sufficient(table: int, states, labels):
    """Independent exhaustive verifier (does not use quotient formula)."""
    if len(states) != len(labels):
        raise ValueError("one label per baseline input is required")
    for a in range(len(states)):
        for b in range(a + 1, len(states)):
            x, y = states[a], states[b]
            if output(table, x) != output(table, y):
                continue  # old output is available for free
            if labels[a] != labels[b]:
                continue
            for i in range(len(x)):
                for value in (0, 1):
                    if (output(table, replace(x, i, value))
                            != output(table, replace(y, i, value))):
                        return False
    return True


def exhaustive_min_labels(table: int, n: int = 2):
    """Brute-force ALL label assignments, independent of profile counting."""
    if n != 2:
        raise ValueError("bounded exhaustive cross-check deliberately uses n=2")
    states = input_states(n)
    for m in range(1, len(states) + 1):
        for labels in product(range(m), repeat=len(states)):
            if labels_are_sufficient(table, states, labels):
                return m
    raise AssertionError("n state labels always suffice")


def minimum_extra_bits(m: int):
    if m < 1:
        raise ValueError("at least one metadata label is needed")
    return (m - 1).bit_length()


def self_check():
    # All 16 Boolean functions on two bits are checked, no sampling.
    results = []
    for table in range(16):
        theoretical = exact_min_labels(table, 2)
        exhaustive = exhaustive_min_labels(table, 2)
        if theoretical != exhaustive:
            raise AssertionError((table, theoretical, exhaustive))
        results.append(theoretical)
    if exact_min_labels(0b1110, 2) != 3:
        raise AssertionError("OR must require three labels")
    if exact_min_labels(0b1000, 2) != 3:
        raise AssertionError("AND must require three labels")
    if exact_min_labels(0b1100, 2) != 1:
        raise AssertionError("first-bit projection must require one label")
    print("TOM_C_EXACT_PROFILE_QUOTIENT_PASS")
    print("TOM_C_FULL_16_FUNCTION_BRUTE_FORCE_PASS")
    print("TOM_C_NO_NOVELTY_CLAIM")
    return tuple(results)


if __name__ == "__main__":
    self_check()
