"""HYP-105 B3.2-E0-C: leading random six-forest GF5 risk coefficient.

Independently combine accepted #224 exact per-forest signed flow weights
with elementary embeddings of any bounded bipartite forest in the
Delta-regular two-color W(3,s) host. Computes exact rational finite-h
sandwiches and the LEADING RANDOM-INJECTION asymptotic coefficient.
These estimates are not fixed-map lower bounds or strict ASET powers.
"""
from fractions import Fraction
from math import comb, factorial
import json

# name, numbered two-color factor endpoint-partition pairs, rL, rR,
# abstract forest components c, physical coordinate divisor,
# GF5 signed per ORIGINAL six-edge factor-forest numerator.
CLASSES = (
    ("C/A", 30, 3, 6, 3, 8, 4243968),
    ("C/B", 360, 3, 5, 2, 16, 173682),
    ("B/B-intersect", 120, 5, 5, 4, 4, 482670),
    ("B/B-disjoint", 90, 5, 5, 4, 4, 558080),
)
EXPECTED_LEADING_NUMERATORS = {
    "C/A": 1414656, "C/B": 347364,
    "B/B-intersect": 1287120, "B/B-disjoint": 1116160,
}
TOTAL_EXPECTED_LEADING_NUMERATOR = 4165300
DENOM = 51**6


def falling(n, k):
    if not isinstance(n, int) or not isinstance(k, int) or k < 0:
        raise ValueError("nonnegative integer falling factorial")
    if n < k:
        return 0
    out = 1
    for j in range(k):
        out *= n-j
    return out


def checked_classes():
    """Prove all 600 new leading named factor endpoint partition pairs."""
    if sum(x[1] for x in CLASSES) != 600:
        raise AssertionError("leading forest abstract shape mass changed")
    for name, named, rL, rR, c, divisor, coefficient in CLASSES:
        if c != rL+rR-6 or not all(
                isinstance(x, int) and x > 0
                for x in (named, rL, rR, c, divisor, coefficient)):
            raise AssertionError("invalid two-color six-forest class")
        if c not in (2, 3, 4):
            raise AssertionError("not a leading new forest class")
        if name not in EXPECTED_LEADING_NUMERATORS:
            raise AssertionError("missing normalized GF5 coefficient")
    return True


def asymptotic_weight_coefficients():
    """Exact leading E[R3_class]/s^6 = rational + o(1).

    Each of the 'named' RGF factor endpoint partition pairs corresponds
    to exactly V^c Delta^6*(1+O(1/s)) ORDERED six-edge embeddings.
    An unordered six-incidence edge set has exactly 6! orderings; divide
    the aggregate of the numbered types by 720, not by factor-graph
    automorphisms or physical coordinate relabelings again.

    Uniform pair-label projected six-coordinate probability is
      (a)_6^2/[d*(K)_rL*(K)_rR].
    Since a^2/V -> 2 and K/V -> 1, multiplying by V^c Delta^6
    cancels V powers (rL+rR=c+6), leaving 2^6=64 and Delta^6~s^6.
    """
    checked_classes()
    numerators = {}
    for name, named, rL, rR, c, divisor, coefficient in CLASSES:
        q = Fraction(64*named*coefficient, factorial(6)*divisor)
        if q != EXPECTED_LEADING_NUMERATORS[name]:
            raise AssertionError("exact leading GF5 coefficient mismatch")
        numerators[name] = q
    total = sum(numerators.values(), Fraction())
    if total != TOTAL_EXPECTED_LEADING_NUMERATOR:
        raise AssertionError("new forest GF5 leading intensity disagrees")
    return {"by_class": numerators, "total": total,
            "GF5_denominator": DENOM,
            "limit_total_over_s6": total/DENOM,
            "all_h_fixed_label_lower": False,
            "strict_ASET_improvement": False}


def embedding_sandwich(s):
    """For s>=16, bounds random R3 for each of four NEW classes.

    A chosen bipartite six-edge FOREST has c rooted components and six
    tree edges. Choose typed root vertex at least V-12 ways for each
    component, then distinct child from >=Delta-12 neighbors each step.
    Upper choose V per root and Delta per edge. All vertex images
    injective; extraneous incidence edges don't affect the chosen forest.
    For a fixed named partition-pair, each embedding yields precisely
    one ORDERED six-edge factor tuple. Divide named total by 6! to get
    unordered original column sets. Avoid falsely assuming EXACT
    M_class = leading expression at finite s.
    """
    if not isinstance(s, int) or s < 16 or s & (s-1):
        raise ValueError("s=2^h with h>=4 for positive greedy floor")
    V = (s+1)*(s*s+1)
    Delta = s+1
    a = 2
    while comb(a, 2) < V:
        a += 1
    K = comb(a, 2)
    report = {}
    for name, named, rL, rR, c, divisor, coefficient in CLASSES:
        lower_M = (Fraction(named, factorial(6))
                   * (V-12)**c * (Delta-12)**6)
        upper_M = (Fraction(named, factorial(6))
                   * V**c * Delta**6)
        if not 0 < lower_M <= upper_M:
            raise AssertionError("invalid forest injection sandwich")
        probability_weight = Fraction(
            coefficient*falling(a, 6)**2,
            divisor*DENOM*falling(K, rL)*falling(K, rR))
        if probability_weight <= 0:
            raise AssertionError("GF5 random weight must be strictly positive")
        report[name] = {
            "M_lower": lower_M,
            "M_upper": upper_M,
            "expected_R3_lower": lower_M*probability_weight,
            "expected_R3_upper": upper_M*probability_weight,
        }
    return {"s": s, "a": a, "V": V, "Delta": Delta,
            "by_class": report,
            "finite_bound_only": True,
            "universal_fixed_label_bound": False}


def report():
    certified = asymptotic_weight_coefficients()
    examples = []
    for s in (16, 32, 64):
        data = embedding_sandwich(s)
        examples.append({
            "s":s,"a":data["a"],
            "normalized_lower": str(
                sum((v["expected_R3_lower"] for v in data["by_class"].values()),
                    Fraction()) / s**6),
            "normalized_upper": str(
                sum((v["expected_R3_upper"] for v in data["by_class"].values()),
                    Fraction()) / s**6),
        })
    return {
        "new_600_leading_nonmatching_forest_shapes": True,
        "GF5_exact_named_class_coefficient_numerators":
            {k:str(v) for k,v in certified["by_class"].items()},
        "total_leading_independent_uniform_R3":
            f"({TOTAL_EXPECTED_LEADING_NUMERATOR}/{DENOM})*s^6*(1+o(1))",
        "limit_coefficient": str(certified["limit_total_over_s6"]),
        "asymptotic_h_consequence_only": True,
        "examples":examples,
        "no_per_label_lower_or_strict_ASET": True,
    }


if __name__ == "__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
