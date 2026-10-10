#!/usr/bin/env python3
"""UCT-005 D1-A: narrowly scoped one-probe interval-parity proof and falsifiers.

This does NOT prove the UCT-005 root. All costs are *logical remote bit cells*;
there is no Byzantine authentication, proof transmission, physical page I/O or
paid trusted checkpoint. Never transfer an honest Fenwick upper to F1 directly.
"""
from __future__ import annotations

import json
from dataclasses import dataclass


def intervals(n: int):
    if n < 1:
        raise ValueError("n must be positive")
    return tuple((left, right) for left in range(n)
                 for right in range(left + 1, n + 1))


def interval_parity(word: tuple[int, ...], left: int, right: int) -> int:
    if not 0 <= left < right <= len(word):
        raise ValueError("invalid half-open interval")
    return sum(word[left:right]) % 2


def one_probe_certificate(n: int) -> dict:
    """Exact optimal m and worst changed remote cells for honest, fixed 1-probe.

    No trusted state, no query-specific stored advice, no proof bytes; every
    possible binary initial word must be supported. Public query may select a
    single fixed address and then apply an arbitrary Boolean function to that
    single bit; such functions are constant, identity or complement.
    """
    itv = intervals(n)
    degree = tuple(sum(left <= i < right for left, right in itv)
                   for i in range(n))
    max_changed = (n + 1) ** 2 // 4
    assert max(degree) == max_changed
    return {
        "n": n,
        "queries": len(itv),
        "minimum_remote_bits": n * (n + 1) // 2,
        "minimum_worst_changed_bits": max_changed,
        "per_flip_minimum_changed_bits": degree,
        "construction": "explicit full interval-parity table",
        "model": "honest exact stateless fixed one-probe GF2; not F1",
    }


def encode_interval_table(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(interval_parity(word, a, b) for a, b in intervals(len(word)))


def table_flip(before: tuple[int, ...], n: int, coordinate: int) -> tuple[int, ...]:
    if not 0 <= coordinate < n or len(before) != n * (n + 1) // 2:
        raise ValueError("invalid state or coordinate")
    return tuple(value ^ int(a <= coordinate < b)
                 for value, (a, b) in zip(before, intervals(n)))


@dataclass(frozen=True)
class OperationCost:
    remote_reads: int
    remote_writes: int


class HonestFenwickSet:
    """Untrusted *logical* raw array + Fenwick tree, no authentication.

    raw[] and tree[] are both charged remote cells (2n total). SET must read
    old raw bit (charged) before changing Fenwick cells. Published proofs,
    authenticated roots, trusted memory and physical page packing absent.
    """

    def __init__(self, word: tuple[int, ...]):
        if not word or any(x not in (0, 1) for x in word):
            raise ValueError("nonempty binary input required")
        self.n = len(word)
        self.raw = list(word)
        self.tree = [0] * (self.n + 1)
        for pos, bit in enumerate(word):
            if bit:
                j = pos + 1
                while j <= self.n:
                    self.tree[j] ^= 1
                    j += j & -j

    def set(self, pos: int, bit: int) -> OperationCost:
        if not 0 <= pos < self.n or bit not in (0, 1):
            raise ValueError("invalid SET")
        previous = self.raw[pos]  # one paid remote bit read
        if previous == bit:
            return OperationCost(1, 0)
        self.raw[pos] = bit  # one paid remote bit write
        writes = 1
        j = pos + 1
        while j <= self.n:
            self.tree[j] ^= 1
            writes += 1
            j += j & -j
        return OperationCost(1, writes)

    def _prefix(self, length: int) -> tuple[int, int]:
        result, reads = 0, 0
        while length:
            result ^= self.tree[length]
            reads += 1
            length -= length & -length
        return result, reads

    def query(self, left: int, right: int) -> tuple[int, OperationCost]:
        if not 0 <= left < right <= self.n:
            raise ValueError("invalid RANGE_PARITY")
        a, ar = self._prefix(left)
        b, br = self._prefix(right)
        return a ^ b, OperationCost(ar + br, 0)


def fenwick_overstrong_candidate_falsifier(power: int = 12) -> dict:
    """Counterexample to the *honest bit-cell* universal Wmax*Qmax >= n.

    It is NOT an F1/Byzantine counterexample: authentication/proof costs are
    completely unaccounted, and both raw values and tree are remote.
    """
    if not 7 <= power <= 24:
        raise ValueError("power must be between 7 and 24")
    n = 1 << power
    # For n=2^k: each SET flips at most (k+1) Fenwick cells plus raw bit;
    # a range query visits at most k nodes in each prefix (k>=1).
    w_upper = power + 2
    q_upper = 2 * power
    product = w_upper * q_upper
    if not product < n:
        raise AssertionError("incorrect falsification parameter")
    return {
        "n": n,
        "max_remote_writes_upper": w_upper,
        "max_remote_query_reads_upper": q_upper,
        "product_upper": product,
        "false_universal_candidate": "Wmax*Qmax >= n",
        "semantic_scope": "honest binary SET/RANGE_PARITY with remote raw+Fenwick bit cells",
        "does_not_refute": "authenticated F1; physical page costs; known cell-probe lower bounds",
    }


def report() -> dict:
    return {
        "scientific_status": "RESTRICTED_CLASSICAL_ONE_PROBE_LEMMA_AND_FALSE_GENERAL_PRODUCT",
        "n6": one_probe_certificate(6),
        "fenwick": fenwick_overstrong_candidate_falsifier(12),
        "UCT005_ROOT": "OPEN_UNPROVED",
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, ensure_ascii=False))
