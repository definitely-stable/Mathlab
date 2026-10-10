"""HYP-105 B3.2-E1-C7: exact ONE-global-bijection prefix fibers.

A partially pinned injective right map has a single shared uniform
completion, not independently randomized B/A anchor fibers.  This
restricted selector optimizes B-left/A-right ONLY.  It does not compute
the seven-family S or assert an all-correlated lower bound.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import json

from hyp105_g5e2b3e1c5_common_bijection import (
    validate_weighted_sixsets, fixed_map_overlap, physical_occupied_target,
)


def _inputs(source, target, V, pinned):
    source = validate_weighted_sixsets(source, V)
    try:
        target = tuple(target)
        raw = {frozenset(t): 1 for t in target}
    except (TypeError, ValueError) as exc:
        raise ValueError("target must be sixsets") from exc
    if len(raw) != len(target):
        raise ValueError("duplicate target sixsets")
    validate_weighted_sixsets(raw, V)
    if not hasattr(pinned, "items"):
        raise ValueError("partial right map must be a mapping")
    p = dict(pinned)
    if len(p) != len(pinned) or any(
        type(x) is not int or type(y) is not int
        or x < 0 or x >= V or y < 0 or y >= V
        for x, y in p.items()
    ) or len(set(p.values())) != len(p):
        raise ValueError("invalid partial injection of original right lines")
    return source, frozenset(raw), p


def conditional_overlap_mean(source, target, V, pinned):
    """Exact E[U(Pi)|Pi|_D=p] for ONE uniform bijection Pi:[V]->[V].

    For each original source sixset R, A=R intersect D is already pinned.
    Its remaining 6-|A| target labels are a uniform subset of the V-|D|
    unpinned target labels.  Only target sixsets T with
    T intersect p(D) = p(A) are possible.  Therefore

      E[U|p] = sum_A b_p(A)*q_p(p(A))/C(V-|D|,6-|A|),

    b_p(A)=sum_{R:R intersect D=A}m(R), and
    q_p(B)=#{T:T intersect p(D)=B}.

    All arithmetic is rational; no independent per-anchor randomization.
    """
    source, target, p = _inputs(source, target, V, pinned)
    D = frozenset(p)
    I = frozenset(p.values())
    n = V - len(D)
    q = Counter(frozenset(T & I) for T in target)
    b = Counter()
    for R, value in source.items():
        b[frozenset(R & D)] += value
    total = Fraction(0)
    for A, mass in b.items():
        denom = comb(n, 6 - len(A))
        if denom == 0:
            raise AssertionError("impossible residual original sixset")
        total += Fraction(mass * q[frozenset(p[i] for i in A)], denom)
    return total


def greedy_conditional_selector(source, target, V):
    """Deterministically build ONE legal g with U(g) <= floor(E_uniform U).

    Process original factor IDs in increasing order. At every step assign
    the available physical edge label minimizing the *exact conditional
    expectation*, tie-breaking by increasing target index. Tower property
    guarantees a nonincreasing rational sequence. The final conditional
    mean equals the independently recounted integer overlap.
    """
    source, target, _ = _inputs(source, target, V, {})
    p = {}
    mean = conditional_overlap_mean(source, target, V, p)
    initial = mean
    trace = [mean]
    for original in range(V):
        candidates = [
            (conditional_overlap_mean(source, target, V,
                                      {**p, original: candidate}),
             candidate)
            for candidate in range(V) if candidate not in p.values()
        ]
        if not candidates:
            raise AssertionError("no right-label completion")
        best, chosen = min(candidates)
        if sum(x for x, _ in candidates) != (V - original) * mean:
            raise AssertionError("conditional tower identity failed")
        if best > mean:
            raise AssertionError("greedy mean increased")
        p[original] = chosen
        mean = best
        trace.append(mean)
    permutation = tuple(p[i] for i in range(V))
    actual = fixed_map_overlap(source, target, permutation)
    if trace[-1] != actual or actual > initial:
        raise AssertionError("final exact overlap violates conditional selector")
    return {
        "V": V,
        "original_to_occupied_permutation": permutation,
        "initial_uniform_mean": initial,
        "conditional_means": tuple(trace),
        "actual_fixed_BA_overlap": actual,
        "all_one_global_permutation": True,
        "full_seven_family_S_evaluated": False,
        "all_correlated_lower_proved": False,
    }


def W32_report():
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    from hyp105_g5e2b3e1c0_weighted_overlap import source_weighted_BA_hypergraph
    from hyp105_g5e2b3e1c5_common_bijection import fixed_map_overlap
    F = tuple(combinations(range(6), 2))
    target = physical_occupied_target(6, F)
    model = pair_labeled_symplectic(1, "reverse-line")
    source = source_weighted_BA_hypergraph(model)
    original = tuple({e: i for i, e in enumerate(F)}[e]
                     for e in model["right_labels"])
    before = fixed_map_overlap(source, target, original)
    result = greedy_conditional_selector(source, target, 15)
    return {
        "W32_original_reverse_line_BA": before,
        "W32_conditional_greedy_BA": result["actual_fixed_BA_overlap"],
        "W32_exact_random_mean": str(result["initial_uniform_mean"]),
        "W32_greedy_permutation": result["original_to_occupied_permutation"],
        "W32_greedy_under_floor_of_mean": result["actual_fixed_BA_overlap"]
                                      <= result["initial_uniform_mean"],
        "true_GQ_original_source": True,
        "all_correlated_BA_or_seven_family_bound": False,
    }


if __name__ == "__main__":
    print(json.dumps(W32_report(), indent=2, sort_keys=True, default=str))
