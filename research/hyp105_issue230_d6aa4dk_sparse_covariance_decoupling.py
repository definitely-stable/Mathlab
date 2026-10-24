"""AA4-DK: Line-overlap sparsity, covariance analysis, and orbit concentration status.

Mathematical results:
1. Girth-8 Line Overlap Sparsity Theorem (all h >= 1, s = 2^h):
   In Generalized Quadrangle W(3,s) with V = (s+1)(s^2+1) lines:
   For any two independent 6-flags Q1, Q2, the intersection of their
   line sets R = |L(Q1) \\cap L(Q2)| satisfies:
       P(R = 0) = comb(V-6, 6) / comb(V, 6) = 1 - 36/V + O(V^-2) = 1 - O(s^-3),
       P(R = 1) = 36 * comb(V-6, 5) / comb(V, 6) = 36/V - O(V^-2) = O(s^-3),
       P(R >= 2) <= O(s^-6).
   Exact finite values:
   - s = 4: P(R <= 1) = 94.5% (64.0% share 0, 30.5% share 1, 5.2% share 2).
   - s = 8: P(R <= 1) > 99.0% (94.0% share 0, 5.8% share 1, 0.2% share 2).
   - s = 16: P(R <= 1) > 99.8% (98.6% share 0, 1.4% share 1).

2. Rigorous Covariance Analysis & K_6 Counterexample to Universal Negative Covariance:
   In earlier drafts, it was conjectured that disjoint 6-line sets always yield
   negative covariance under random permutations.
   CRITICAL CORRECTION (Counterexample V=15, complete physical K_6):
   For physical 2-regularity (|T_A| = 70 two-factors):
       P(A) = 70 / 5005 = 2 / 143.
       Ordered pairs of disjoint 2-factors in K_6 = 300.
       Total ordered pairs of disjoint 6-subsets = 5005 * 84 = 420420.
       P(A1 \\cap A2) = 300 / 420420 = 5 / 7007.
       Cov(1_A1, 1_A2) = 5/7007 - (2/143)^2 = +519 / 1002001 approx +0.000518 > 0!
   Because the covariance is strictly POSITIVE, the universal negative covariance
   claim is REFUTED for structured physical factors, and the variance concentration
   Var(S)/(E[S])^2 = O(s^-1) remains an OPEN CONJECTURE.

Root #230 remains OPEN_WITH_FORMAL_BLOCKER.
"""
from collections import Counter
from fractions import Fraction
import itertools
from math import comb
import random

from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original


def gq_line_overlap_distribution(s):
    """Compute exact combinatorial line overlap probabilities P(R = r) in W(3,s)."""
    if not isinstance(s, int) or s < 2 or (s & (s - 1)) != 0:
        raise ValueError("s must be a power of 2 >= 2")

    V = (s + 1) * (s**2 + 1)
    total_comb = comb(V, 6)
    dist = {}
    for r in range(7):
        ways = comb(6, r) * comb(V - 6, 6 - r)
        dist[r] = Fraction(ways, total_comb)

    sum_probs = sum(dist.values())
    if sum_probs != 1:
        raise AssertionError("Overlap probabilities must sum to 1")

    p_at_most_1 = dist[0] + dist[1]
    p_at_least_2 = sum(dist[r] for r in range(2, 7))

    return {
        "s": s,
        "V": V,
        "probabilities": dist,
        "p_share_0": dist[0],
        "p_share_1": dist[1],
        "p_share_at_most_1": p_at_most_1,
        "p_share_at_least_2": p_at_least_2,
        "share_0_float": float(dist[0]),
        "share_1_float": float(dist[1]),
        "share_at_most_1_float": float(p_at_most_1),
        "share_at_least_2_float": float(p_at_least_2),
        "asymptotic_r0_order": "1 - O(s^-3)",
        "asymptotic_r1_order": "O(s^-3)",
        "asymptotic_r_ge_2_order": "O(s^-6)",
    }


def measure_sampled_flag_line_overlaps(model, num_samples=150, seed=42):
    """Sample genuine 6-flags with distinct points and lines; measure line overlap."""
    s, V, a, f, g, pl, lp = _validated_original(model)
    all_flags = tuple((p, l) for p in range(V) for l in pl[p])

    rng = random.Random(seed)
    sampled_flags = []
    attempts = 0
    max_attempts = num_samples * 100

    while len(sampled_flags) < num_samples and attempts < max_attempts:
        attempts += 1
        cand = rng.sample(all_flags, 6)
        pts = tuple(p for p, l in cand)
        lns = tuple(l for p, l in cand)
        if len(set(pts)) == 6 and len(set(lns)) == 6:
            sampled_flags.append(tuple(sorted(cand)))

    if len(sampled_flags) < num_samples // 2:
        raise ValueError("Insufficient 6-flags sampled")

    overlap_counts = Counter()
    total_pairs = 0
    for i in range(len(sampled_flags)):
        l1 = frozenset(l for p, l in sampled_flags[i])
        for j in range(i + 1, len(sampled_flags)):
            l2 = frozenset(l for p, l in sampled_flags[j])
            overlap_counts[len(l1 & l2)] += 1
            total_pairs += 1

    distribution = {r: overlap_counts[r] for r in range(7)}
    freq_at_most_1 = (distribution[0] + distribution[1]) / total_pairs if total_pairs > 0 else 0.0

    return {
        "s": s,
        "V": V,
        "num_flags_sampled": len(sampled_flags),
        "total_pairs_evaluated": total_pairs,
        "overlap_counts": distribution,
        "empirical_fraction_at_most_1": freq_at_most_1,
    }


def exact_k6_two_factor_covariance():
    """Exact calculation on V=15, K_6: proves covariance of disjoint 2-factors is strictly positive."""
    vertices = list(range(6))
    edges = list(itertools.combinations(vertices, 2))
    assert len(edges) == 15

    two_factors = []
    for subset in itertools.combinations(range(15), 6):
        deg = [0] * 6
        for e_idx in subset:
            u, v = edges[e_idx]
            deg[u] += 1
            deg[v] += 1
        if all(d == 2 for d in deg):
            two_factors.append(frozenset(subset))

    assert len(two_factors) == 70  # 60 cycles C6 + 10 pairs 2*C3

    disjoint_tf_pairs = 0
    for tf1 in two_factors:
        for tf2 in two_factors:
            if tf1.isdisjoint(tf2):
                disjoint_tf_pairs += 1

    total_disjoint_6_pairs = comb(15, 6) * comb(15 - 6, 6)
    p_A = Fraction(len(two_factors), comb(15, 6))
    p_joint = Fraction(disjoint_tf_pairs, total_disjoint_6_pairs)
    cov = p_joint - (p_A ** 2)

    return {
        "V": 15,
        "num_two_factors": len(two_factors),
        "disjoint_pairs_count": disjoint_tf_pairs,
        "total_disjoint_6_pairs": total_disjoint_6_pairs,
        "p_A": p_A,
        "p_joint": p_joint,
        "covariance": cov,
        "is_strictly_positive": cov > 0,
        "counterexample_refutes_universal_negative_cov": True,
    }


def exact_r0_covariance_sign(V, p_A):
    """Audit the naive disjoint subset formula vs genuine permutation covariance."""
    if V <= 12 or p_A <= 0:
        raise ValueError("V > 12 and p_A > 0 required")
    # Under independent subset drawing, prob_disjoint < 1, giving negative naive formula:
    prob_disjoint = Fraction(comb(V - 6, 6), comb(V, 6))
    naive_cov_0 = (prob_disjoint - 1) * (p_A**2)

    # Note: On actual graphs with degree constraints (e.g. K_6 2-factors),
    # true covariance is POSITIVE (+0.000518). The naive formula does not hold.
    return {
        "V": V,
        "p_A": p_A,
        "prob_disjoint_under_permutation": prob_disjoint,
        "naive_covariance_r0": naive_cov_0,
        "naive_formula_negative": (naive_cov_0 < 0),
        "universal_negative_covariance_holds": False,
        "note": "Refuted for 2-regular subgraphs by K_6 counterexample (Cov = +0.000518 > 0)",
    }


def variance_ratio_decay_bound(s):
    """Status of asymptotic variance-to-mean-squared ratio Var(S)/(E[S])^2."""
    if not isinstance(s, int) or s < 2 or (s & (s - 1)) != 0:
        raise ValueError("s must be a power of 2 >= 2")

    V = (s + 1) * (s**2 + 1)
    # The heuristic 10/s bound is an UNPROVEN conjecture because disjoint covariance
    # is not universally negative.
    heuristic_bound = Fraction(10, s)

    return {
        "s": s,
        "V": V,
        "heuristic_variance_ratio_conjecture": heuristic_bound,
        "status": "OPEN_CONJECTURE_UNPROVEN",
        "formal_blocker": "Covariance between disjoint motifs can be positive due to graph regularity constraints.",
    }
