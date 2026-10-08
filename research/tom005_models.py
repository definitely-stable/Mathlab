#!/usr/bin/env python3
"""TOM-005: seven elementary cross-domain theorem models, all non-novel.

Every result has a separate quantified paper proof in
docs/research/TOM-005-SEVEN-THEOREM-AUDIT.md. The functions below are
small, pure algorithmic specifications. Finite tests are *regressions*,
not formal verification of universally quantified proofs.

T05 A: independent intervals, certified exact best evaluated candidate
T05 B: nondecreasing separable objective, Pareto candidate pruning
T05 C: additive switching-cost route, Bellman optimal substructure
T05 D: independent fail-fast tests, cost/rejection exchange rule
T05 E: immutable new data flushed before atomic durable root switch
T05 F: fixed-bit exact fingerprint pigeonhole impossibility
T05 G: fully materialized fanout output change lower bound
"""
from __future__ import annotations

from fractions import Fraction


def interval_certificate(
    intervals: tuple[tuple[int, int], ...],
    observed: dict[int, int],
) -> tuple[int, bool]:
    """Return best exact cost among evaluated candidates and global certificate.

    Assumptions: all candidates independent; each unknown exact integer cost
    may lie anywhere in its closed interval. An evaluated candidate is needed
    as the returned concrete witness (not just a speculative upper bound).
    """
    if not intervals or not observed:
        raise ValueError("at least one candidate and one evaluation required")
    for low, high in intervals:
        if type(low) is not int or type(high) is not int or low > high:
            raise ValueError("invalid candidate cost interval")
    for i, cost in observed.items():
        if type(i) is not int or not 0 <= i < len(intervals):
            raise ValueError("observed candidate index invalid")
        low, high = intervals[i]
        if type(cost) is not int or not low <= cost <= high:
            raise ValueError("observed cost outside frozen bounds")
    best = min(observed.values())
    return best, all(low >= best for i, (low, _) in
                     enumerate(intervals) if i not in observed)


def pareto_indices(vectors: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    """Prune weakly dominated independent complete choices.

    Identical vectors retain the lowest-index representative.
    This is NOT valid with cross-candidate switching or shared setup costs.
    """
    if not vectors:
        raise ValueError("empty choices")
    dim = len(vectors[0])
    if not dim or any(len(v) != dim for v in vectors):
        raise ValueError("vectors must have equal positive dimension")
    if any(type(x) is not int or x < 0 for v in vectors for x in v):
        raise ValueError("nonnegative integer costs required")
    winners = []
    for i, item in enumerate(vectors):
        if any(
            all(a <= b for a, b in zip(other, item))
            and (any(a < b for a, b in zip(other, item)) or j < i)
            for j, other in enumerate(vectors) if j != i
        ):
            continue
        winners.append(i)
    return tuple(winners)


def routed_cost(
    local: tuple[tuple[int, ...], ...], switch: int
) -> int:
    """Minimize sum_t cost[t][base_t] + switch*[base_t != base_(t-1)]."""
    if not local or not local[0]:
        raise ValueError("nonempty periods/bases required")
    k = len(local[0])
    if type(switch) is not int or switch < 0:
        raise ValueError("nonnegative fixed switching charge")
    if any(len(row) != k or any(type(v) is not int or v < 0 for v in row)
           for row in local):
        raise ValueError("fixed base universe and nonnegative costs required")
    previous = tuple(local[0])
    for row in local[1:]:
        previous = tuple(
            row[j] + min(previous[i] + (switch if i != j else 0)
                         for i in range(k)) for j in range(k)
        )
    return min(previous)


def expected_cost(
    tests: tuple[tuple[int, Fraction], ...],
    order: tuple[int, ...],
) -> Fraction:
    """One-sided reject ends chain; rejection events are independent."""
    if tuple(sorted(order)) != tuple(range(len(tests))):
        raise ValueError("order must be a permutation of all tests")
    survival = Fraction(1)
    total = Fraction(0)
    for i in order:
        price, reject = tests[i]
        if type(price) is not int or price < 0 or not 0 <= reject <= 1:
            raise ValueError("nonnegative cost and 0<=p<=1")
        total += survival * price
        survival *= 1 - reject
    return total


def reject_first_order(tests: tuple[tuple[int, Fraction], ...]) -> tuple[int, ...]:
    """Nonincreasing p_i / c_i, zero-cost tests before positive-cost tests.

    For zero price/rejection tie, any placement is optimal.  Use strict
    comparator without floating point; reject=0 is last for positive costs.
    """
    if not tests:
        raise ValueError("empty test cascade")
    if any(type(c) is not int or c < 0 or not 0 <= p <= 1 for c, p in tests):
        raise ValueError("bad reject test")
    def ratio(i: int) -> tuple[int, Fraction, int]:
        c, p = tests[i]
        return (1 if c == 0 else 0, Fraction(0) if c == 0 else p/c, -i)
    return tuple(sorted(range(len(tests)), key=ratio, reverse=True))


def generation_crash_prefix(
    actions: tuple[str, ...], stop: int,
) -> tuple[str, bool, bool]:
    """Abstract durable atomic switch; no real disk fsync semantics.

    actions use: prepare (write volatile new data), flush (new data durable),
    publish (durable atomic pointer switch).  Prefix crash discards volatile.
    """
    if tuple(sorted(actions)) != ("flush", "prepare", "publish"):
        raise ValueError("one of each action required")
    if type(stop) is not int or not 0 <= stop <= len(actions):
        raise ValueError("invalid crash cut")
    volatile = False
    durable = False
    root = "old"
    for action in actions[:stop]:
        if action == "prepare":
            volatile = True
        elif action == "flush":
            durable |= volatile
        else:
            root = "new"
    return root, durable, root == "old" or durable


def exact_fingerprint_possible(domain_states: int, retained_bits: int) -> bool:
    """Pigeonhole necessary-and-sufficient cardinality for arbitrary injective map.

    Assumes all domain_states are distinct and *must* be exactly distinguished
    with no external context or further probes.
    """
    if (type(domain_states) is not int or domain_states < 1 or
            type(retained_bits) is not int or retained_bits < 0):
        raise ValueError("bad finite summary cardinality")
    return domain_states <= 1 << retained_bits


def materialized_fanout_changes(fanout: int, old: int, new: int) -> int:
    """Each independent materialized output y_j = x AND 1 must be rewritten."""
    if (type(fanout) is not int or fanout < 0 or
            old not in (0, 1) or new not in (0, 1)):
        raise ValueError("bad fanout or source bits")
    return fanout if old != new else 0


def main() -> None:
    print("TOM005_SEVEN_THEOREM_MODELS_DEFINED")
    print("TOM005_A_INTERVAL", interval_certificate(((0, 4), (3, 8)), {0: 2}))
    print("TOM005_B_PARETO", pareto_indices(((2, 1), (3, 2), (1, 4))))
    print("TOM005_C_ROUTE", routed_cost(((0, 1), (1, 0)), 3))
    print("TOM005_D_TEST_ORDER",
          reject_first_order(((2, Fraction(1, 2)), (1, Fraction(1, 4)))))
    print("TOM005_E_DURABLE", generation_crash_prefix(
          ("prepare", "flush", "publish"), 3))
    print("TOM005_F_SUMMARY", exact_fingerprint_possible(4, 1))
    print("TOM005_G_FANOUT", materialized_fanout_changes(16, 0, 1))


if __name__ == "__main__":
    main()
