"""HYP-105 #230 D6-N: exact correlated C-left/A-right six-line overlap.

All finite s=2**h theorem: fix a complete original GQ left injection f.
For each unordered six-subset L of DISTINCT ORIGINAL right lines let
w_f(L) count original six-incidence sets with left physical C and right
line support L. For any globally injective right physical labeling g,

    U_C/A(f,g) = sum_L w_f(L) * 1{g(L) is physical A}.

This is an exact deterministic *correlation identity*, not an all-g
positive lower bound. A uniformly random complete injection g yields
an exact SECOND moment controlled by the overlap spectrum of the
genuine original line supports:

    E U = p * W,
    E U**2 = sum_{k=0}**6 N_k(f) * q_k(a),

where W=sum_L w_f(L), N_k=sum_{|L intersect M|=k} w_f(L)w_f(M)
(ORDERED pairs), and q_k is a universal rational physical
2-factor overlap kernel. It is NOT valid to replace the q_k by p*p,
even at k=0: right injection is globally without replacement.

For every 0<=k<=6, 0<=t<=6, put T[t,k] the number of ordered
simple 2-factors (F,H) on fixed 6-vertex sets with t common physical
vertices and k common physical edges; sum_k T[t,k]=70**2.
Then with K=binom(a,2) and A_a=70*binom(a,6),

    P_k(a)=binom(a,6)*sum_t binom(6,t)*binom(a-6,6-t)*T[t,k],
    q_k(a)=k!*(6-k)!**2*P_k(a)/(K)_(12-k).

Proof: choose the two physical 6-vertex sets and 2-factors, require
EXACTLY k shared physical pair labels due to global injection; then
match common ORIGINAL line IDs in k! ways and each disjoint complement
in (6-k)! ways. The denominator injects the 12-k ORIGINAL lines.
This formula is exact at every admissible a (including a<12).

The finite-W32 oracle is an exact true-ORIGINAL witness only. Neither
positive conditional mean, variance nor finite discrepancy certifies
Branch A, an infinite Branch B or the full seven-family S.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb, factorial
import json


def _choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def _falling(n, k):
    if k < 0 or k > n:
        return 0
    out = 1
    for i in range(k):
        out *= n - i
    return out


def _factor_edges(vertices):
    """Enumerate the 70 unoriented labelled 2-factors of a fixed K6."""
    vertices = tuple(vertices)
    if len(vertices) != 6 or len(set(vertices)) != 6:
        raise ValueError("requires six distinct physical coordinates")
    pairs = tuple(combinations(vertices, 2))
    answer = []
    for chosen in combinations(pairs, 6):
        deg = Counter(v for uv in chosen for v in uv)
        if len(deg) == 6 and all(n == 2 for n in deg.values()):
            answer.append(frozenset(chosen))
    if len(answer) != 70 or len(set(answer)) != 70:
        raise AssertionError("physical six-coordinate A has exactly 70 factors")
    return tuple(answer)


@lru_cache(maxsize=1)
def local_two_factor_overlap_table():
    """Seven universal 70x70 local enumerations, independent of all GQ."""
    first = _factor_edges(range(6))
    rows = []
    for t in range(7):
        second_vertices = tuple(range(t)) + tuple(range(6, 12 - t))
        second = _factor_edges(second_vertices)
        row = [0] * 7
        for f in first:
            for g in second:
                row[len(f & g)] += 1
        if sum(row) != 70**2 or any(row[k] for k in range(t + 1, 7)):
            raise AssertionError("invalid canonical local intersection table")
        rows.append(tuple(row))
    if rows[0][0] != 4900 or rows[6][6] != 70:
        raise AssertionError("local disjoint/identical extrema violated")
    return tuple(rows)


@lru_cache(maxsize=None)
def exact_right_A_overlap_kernel(a):
    """Exact q_k(a) for TWO six-line events sharing k ORIGINAL lines."""
    if type(a) is not int or a < 6:
        raise ValueError("physical alphabet must be integer a>=6")
    K = comb(a, 2)
    table = local_two_factor_overlap_table()
    physical_pairs_by_shared_edges = []
    for k in range(7):
        n = comb(a, 6) * sum(
            comb(6, t) * _choose(a - 6, 6 - t) * table[t][k]
            for t in range(7)
        )
        physical_pairs_by_shared_edges.append(n)
    total_A = 70 * comb(a, 6)
    if sum(physical_pairs_by_shared_edges) != total_A**2:
        raise AssertionError("every ordered physical A-factor pair miscounted")
    p = Fraction(factorial(6) * total_A, _falling(K, 6))
    q = tuple(
        Fraction(factorial(k) * factorial(6-k)**2
                 * physical_pairs_by_shared_edges[k],
                 _falling(K, 12-k))
        for k in range(7)
    )
    if q[6] != p or not 0 < p <= 1 or any(not 0 <= x <= 1 for x in q):
        raise AssertionError("exact right-overlap kernel invalid")
    return {
        "a": a,
        "K": K,
        "physical_A_sixsets": total_A,
        "ordered_A_pairs_by_common_physical_edge_count":
            tuple(physical_pairs_by_shared_edges),
        "single_A_probability": p,
        "joint_A_probability_by_common_original_line_count": q,
    }


def ca_original_line_weights(model):
    """Finite original-GQ oracle; only W(3,2) full C enumeration.

    The ALL-h mathematical definition is unrestricted. The small exact
    oracle intentionally refuses fake W34 full-positive census.
    """
    from hyp105_issue230_projection import ProjectionClosure
    from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
    core = ProjectionClosure(model)
    if core.s != 2:
        raise ValueError("full sixset support enumeration pinned to W(3,2)")
    weights = Counter()
    for ids, kind in selected_left_six(model):
        if kind != "C":
            continue
        right_lines = tuple(sorted(core.edges[i][1] for i in ids))
        if len(set(right_lines)) != 6:
            continue
        weights[right_lines] += 1
    if not weights or any(len(k) != 6 or w <= 0 for k, w in weights.items()):
        raise AssertionError("original six-line C support malformed")
    return weights


def _is_right_physical_A(six, right_labels):
    degrees = Counter(
        coord for r in six for coord in right_labels[r]
    )
    return len(degrees) == 6 and set(degrees.values()) == {2}


def ca_correlation_moments(weights, right_labels, a):
    """Exact rational moments and fixed-g signed discrepancy.

    weights is a nonnegative integer multiset of ORIGINAL six-line
    supports, not 2-factor physical patterns or orbit representatives.
    The caller must verify genuine original-GQ provenance separately.
    """
    if type(a) is not int or a < 6:
        raise ValueError("requires physical a>=6")
    labels = tuple(tuple(p) for p in right_labels)
    legal = set(combinations(range(a), 2))
    if (len(labels) > len(legal) or len(set(labels)) != len(labels)
            or any(p not in legal for p in labels)):
        raise ValueError("complete right labels must be injective canonical pairs")
    if not weights:
        raise ValueError("nonempty original six-line support required")
    canon = Counter()
    for six, weight in weights.items():
        six = tuple(sorted(six))
        if (len(six) != 6 or len(set(six)) != 6
                or any(type(i) is not int or i < 0 or i >= len(labels)
                       for i in six)
                or type(weight) is not int or weight <= 0):
            raise ValueError("requires positive integer original support weights")
        canon[six] += weight
    kernel = exact_right_A_overlap_kernel(a)
    p = kernel["single_A_probability"]
    q = kernel["joint_A_probability_by_common_original_line_count"]
    supports = [(sum(1 << r for r in lines), weight, lines)
                for lines, weight in canon.items()]
    N = [0] * 7
    for mask, wi, _ in supports:
        for other, wj, _ in supports:
            N[(mask & other).bit_count()] += wi * wj
    W = sum(canon.values())
    if sum(N) != W**2 or N[6] != sum(w*w for w in canon.values()):
        raise AssertionError("ordered original-six-line pair conservation failed")
    observed = sum(w for lines, w in canon.items()
                   if _is_right_physical_A(lines, labels))
    support_intersection = sum(1 for lines in canon
                               if _is_right_physical_A(lines, labels))
    mean = p * W
    second = sum((N[k] * q[k] for k in range(7)), Fraction())
    variance = second - mean**2
    if variance < 0 or second < mean**2:
        raise AssertionError("negative exact conditional variance")
    # Paley-Zygmund at theta=0: conditional random-right positive
    # probability is >= E[U]**2 / E[U**2]; no fixed-g conclusion.
    nonzero_probability_lower = mean**2 / second
    # EXACT deterministic discrepancy of the actually supplied g.
    discrepancy = Fraction(observed) - mean
    return {
        "a": a,
        "original_distinct_right_line_supports": len(canon),
        "original_C_sixsets_six_distinct_right_lines": W,
        "ordered_support_pairs_by_shared_original_line_count": N,
        "right_A_physical_2factor_probability": str(p),
        "right_random_joint_A_probability_by_overlap": [str(x) for x in q],
        "right_random_exact_mean": str(mean),
        "right_random_exact_second_moment": str(second),
        "right_random_exact_variance": str(variance),
        "right_random_P_positive_lower_Paley_Zygmund": str(
            nonzero_probability_lower),
        "actual_fixed_g_positive_original_support_count": support_intersection,
        "actual_fixed_g_Cleft_Aright_sixsets": observed,
        "actual_fixed_g_minus_right_random_mean": str(discrepancy),
        "actual_fixed_g_centered_discrepancy_over_mean": str(
            discrepancy / mean),
        "all_h_moment_identity_scope": "ANY-GENUINE-ORIGINAL-LINE-WEIGHT-SYSTEM",
        "physical_target_right_A_density_ALONE_not_sufficient": True,
        "not_an_all_g_lower_bound": True,
        "Branch_A": "OPEN",
        "Branch_B": "OPEN",
    }


def real_W32_correlation_report():
    from hyp105_issue230_projection import fixture
    from hyp105_g5e2b3e1b1a_one_sided import exact_physical_counts
    from hyp105_issue230_d6m_gq_collinearity_ca_transfer import (
        exact_fixed_left_CA_profile
    )
    rows = []
    for scheme in ("lex", "reverse", "S68", "S72"):
        model = fixture(1, scheme)
        weights = ca_original_line_weights(model)
        row = ca_correlation_moments(weights, model["right_labels"], model["a"])
        parent = exact_fixed_left_CA_profile(model)
        assert row["right_random_exact_mean"] == parent[
            "exact_expected_g_random_Cleft_Aright"]
        assert row["actual_fixed_g_Cleft_Aright_sixsets"] == parent[
            "actual_fixed_global_right_g_Cleft_Aright"]
        row["scheme"] = scheme
        row["complete_right_physical_A_patterns_available"] = (
            exact_physical_counts(model["a"], model["right_labels"])["A"]
        )
        if row["complete_right_physical_A_patterns_available"] != 70:
            raise AssertionError("W32 right physical K6 must have 70 A-factors")
        rows.append(row)
    if not (rows[0]["right_random_exact_mean"] ==
            rows[1]["right_random_exact_mean"] == "38/13"):
        raise AssertionError("identical original W32 left map means violated")
    if [r["actual_fixed_g_Cleft_Aright_sixsets"] for r in rows] != [4, 0, 0, 2]:
        raise AssertionError("fixed right-map directional falsifier changed")
    return {
        "slice": "HYP105-ISSUE230-D6N-EXACT-ORIGINAL-CORRELATED-CA-OVERLAP",
        "theorem": "EXACT-ALL-FINITE-H-ONE-DIRECTION-SECOND-MOMENT-IDENTITY",
        "right_labeling": "GLOBAL-INJECTION-NO-REPLACEMENT",
        "genuine_W32_complete_original_GQ": True,
        "right_A_physical_patterns_present_even_when_actual_CA_zero": True,
        "full_seven_S_for_W34_W38": "NOT-CLAIMED",
        "Branch_A": "OPEN",
        "Branch_B": "OPEN",
        "finite_W32_rows": rows,
    }


if __name__ == "__main__":
    print(json.dumps(real_W32_correlation_report(), indent=2, sort_keys=True))
