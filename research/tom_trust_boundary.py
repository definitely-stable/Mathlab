#!/usr/bin/env python3
"""TOM-003: finite exact overwrite-state equivalence and trusted-delta gate.

No Rust code and no theorem novelty claim. This is a classical Moore/Myhill-
Nerode indistinguishability argument for the declared overwrite machine.

Model U: initialize from any x in {0,1}^n, retain state M(x); future input
write(i, new_bit) and current f(x) output are exact for *every* history.
Model T: old_bit supplied on a trusted/externally validated channel; summary
may use this promise but pays for validation outside its own accounting.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import ceil, log2


def validate_function(n: int, truth_table: int) -> None:
    if type(n) is not int or not 1 <= n <= 10:
        raise ValueError("n must be integer in 1..10")
    if type(truth_table) is not int or not 0 <= truth_table < 1 << (1 << n):
        raise ValueError("truth_table must contain exactly 2^n Boolean outputs")


def value(n: int, truth_table: int, x: int) -> int:
    validate_function(n, truth_table)
    if type(x) is not int or not 0 <= x < 1 << n:
        raise ValueError("initial binary vector is out of range")
    return (truth_table >> x) & 1


def write(n: int, x: int, index: int, bit: int) -> int:
    if (type(n) is not int or not 1 <= n <= 10
            or type(x) is not int or not 0 <= x < 1 << n
            or type(index) is not int or not 0 <= index < n
            or type(bit) is not int or bit not in (0, 1)):
        raise ValueError("invalid bit overwrite")
    return (x & ~(1 << index)) | (bit << index)


def essential_mask(n: int, truth_table: int) -> int:
    """Variable i is essential if a same-context flip of i can change f."""
    validate_function(n, truth_table)
    mask = 0
    for i in range(n):
        for x in range(1 << n):
            if ((truth_table >> x) & 1) != ((truth_table >> (x ^ (1 << i))) & 1):
                mask |= 1 << i
                break
    return mask


def future_equivalence_partition(n: int, truth_table: int) -> tuple[tuple[int, ...], int]:
    """Independent exhaustive Moore-machine partition refinement.

    State = full Boolean input vector x.
    Observation = exact f(x) after every operation.
    Action alphabet = all possible unconditional writes (i,0)/(i,1).
    Compute the coarsest *stable* output-respecting equivalence partition;
    no essential-variable theorem is used inside the algorithm.
    """
    validate_function(n, truth_table)
    size = 1 << n
    # Initial partition: observe f at the current state, before any writes.
    labels = tuple((truth_table >> x) & 1 for x in range(size))
    rounds = 0
    while True:
        signatures = [
            (labels[x],) + tuple(
                labels[write(n, x, i, b)] for i in range(n) for b in (0, 1)
            ) for x in range(size)
        ]
        ids = {sig: k for k, sig in enumerate(sorted(set(signatures)))}
        updated = tuple(ids[s] for s in signatures)
        # Stable partitions may relabel classes; test actual equivalences.
        old_classes = tuple(tuple(y for y in range(size) if labels[y] == labels[x])
                            for x in range(size))
        new_classes = tuple(tuple(y for y in range(size) if updated[y] == updated[x])
                            for x in range(size))
        rounds += 1
        if new_classes == old_classes:
            return updated, rounds
        if rounds > size:
            raise AssertionError("finite partition refinement failed to converge")
        labels = updated


def oracle_report(n: int) -> dict[str, object]:
    """Exhaustively audit all 2^(2^n) Boolean functions, n<=3.

    Larger n has doubly-exponentially many truth tables; fail closed rather
    than misrepresent a partial sample as universal exhaustive evidence.
    """
    if type(n) is not int or not 1 <= n <= 3:
        raise ValueError("full function enumeration pinned to n<=3")
    essential_histogram = [0] * (n + 1)
    max_rounds = 0
    for tt in range(1 << (1 << n)):
        essential = essential_mask(n, tt)
        labels, rounds = future_equivalence_partition(n, tt)
        ess_count = essential.bit_count()
        essential_histogram[ess_count] += 1
        max_rounds = max(max_rounds, rounds)
        if len(set(labels)) != 1 << ess_count:
            raise AssertionError("classical overwrite lower/upper bounds disagreed")
        for x in range(1 << n):
            for y in range(1 << n):
                if (labels[x] == labels[y]) != ((x & essential) == (y & essential)):
                    raise AssertionError("independent Moore quotient != essential-bit quotient")
    return {
        "n": n,
        "truth_tables_checked": 1 << (1 << n),
        "essential_histogram": essential_histogram,
        "max_refinement_rounds": max_rounds,
        "all_full_overwrite_quotients_match": True,
        "claim_status": "FINITE_ORACLE_FOR_CLASSICAL_AUTOMATA_COROLLARY",
    }


def threshold_truth_table(n: int, threshold: int) -> int:
    if (type(n) is not int or not 1 <= n <= 10
            or type(threshold) is not int or not 1 <= threshold <= n):
        raise ValueError("threshold 1..n required")
    return sum(1 << x for x in range(1 << n) if x.bit_count() >= threshold)


@dataclass(frozen=True)
class PromisedOldBitSummary:
    """O(log(n)) stored bits, but NOT an unconditional exact-update API.

    The caller MUST have checked that 'old' equals the actual current bit
    at index i. This object does not store per-index membership and cannot
    detect a false old bit. External validation/state is separately charged.
    """

    length: int
    threshold: int
    ones: int

    def __post_init__(self) -> None:
        if (type(self.length) is not int or not 1 <= self.length <= 1_000_000
                or type(self.threshold) is not int
                or not 1 <= self.threshold <= self.length
                or type(self.ones) is not int or not 0 <= self.ones <= self.length):
            raise ValueError("invalid summary parameters")

    def root(self) -> bool:
        return self.ones >= self.threshold

    def apply_assuming_verified_old(
        self, old_bit: int, new_bit: int
    ) -> tuple[PromisedOldBitSummary, bool]:
        if (type(old_bit) is not int or old_bit not in (0, 1)
                or type(new_bit) is not int or new_bit not in (0, 1)):
            raise ValueError("trusted delta requires two Boolean bit values")
        new_count = self.ones + new_bit - old_bit
        if not 0 <= new_count <= self.length:
            raise ValueError("inconsistent delta violates total count bounds")
        newer = PromisedOldBitSummary(self.length, self.threshold, new_count)
        return newer, newer.root() != self.root()


def full_overwrite_state_bits(n: int, truth_table: int) -> int:
    """Exact *information-theoretic* min state bits in Model U (not time)."""
    return essential_mask(n, truth_table).bit_count()


def trusted_counter_state_bits(n: int) -> int:
    """Sufficient bits for the exact count in Model T, excluding verifier."""
    if type(n) is not int or n < 1:
        raise ValueError("n must be positive integer")
    # n+1 possible counts: use bit_length(n), same as ceil(log2(n+1)).
    return n.bit_length()


def untrusted_count_alias() -> dict[str, object]:
    """Same count state, same overwrite, different exact outcomes."""
    a, b, target = 0b011, 0b101, 2
    if a.bit_count() != b.bit_count() or a == b:
        raise AssertionError("wrong two-state collision")
    i, new_bit = 1, 0
    before = threshold_truth_table(3, target)
    a2, b2 = write(3, a, i, new_bit), write(3, b, i, new_bit)
    if value(3, before, a2) == value(3, before, b2):
        raise AssertionError("no observable divergence")
    return {
        "n": 3,
        "threshold": 2,
        "initial_states": [a, b],
        "same_initial_count": a.bit_count(),
        "same_initial_root": value(3, before, a) == value(3, before, b),
        "same_overwrite": [i, new_bit],
        "post_roots": [value(3, before, a2), value(3, before, b2)],
        "requires_external_old_bit_check": True,
    }


def main() -> None:
    for n in (1, 2, 3):
        result = oracle_report(n)
        print("TOM003_MOORE_QUOTIENT_PASS", result)
    example = untrusted_count_alias()
    print("TOM003_UNTRUSTED_OVERWRITE_ALIAS_PASS", example)
    for n in (3, 8, 64, 1024):
        table_bits = n  # all variables essential for Boolean AND/threshold
        counter_bits = trusted_counter_state_bits(n)
        if counter_bits > n:
            raise AssertionError("conditional count bound should not exceed full input")
        print("TOM003_TRUST_ACCOUNTING", {
            "n": n,
            "untrusted_full_state_lower_bits": table_bits,
            "trusted_count_bits_excluding_old_validation": counter_bits,
            "external_validation_charged": True,
            "product_authorization": "NO_GO_PENDING_FULL_COST",
        })
    print("TOM003_PHASE_A_FINITE_ORACLE_PASS")


if __name__ == "__main__":
    main()
