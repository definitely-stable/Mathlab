"""HYP-105 E2-B3.0: exact six-column projection 2-core catalog.

For W(3,2^h) factor edges, any SIX distinct incidences form a forest
(girth eight). Independent uniform injective pair labels can be analyzed
using finite weighted simple graphs on at most six physical coordinates.
The resulting necessary-only leafless upper is O(s^6), NOT o(s^6).
No GF(5) positive-flow classification or correlated labeling is claimed.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import comb, factorial
import json


def integer_partitions(total, maximum=None):
    """All nonincreasing positive partitions, deterministically."""
    if not isinstance(total, int) or total < 0:
        raise ValueError("partition target must be nonnegative")
    if total == 0:
        yield ()
        return
    cap = min(total, total if maximum is None else maximum)
    for first in range(cap, 0, -1):
        for rest in integer_partitions(total - first, first):
            yield (first,) + rest


def falling(n, k):
    if not isinstance(n, int) or not isinstance(k, int) or n < 0 or k < 0:
        raise ValueError("falling factorial requires nonnegative integers")
    if k > n:
        return 0
    value = 1
    for j in range(k):
        value *= n - j
    return value


@lru_cache(maxsize=None)
def six_projection_coefficients(multiplicities):
    """Exact numerator in the falling-factorial basis for 6 occurrences.

    For a profile lambda of r DISTINCT factor endpoints, uniformly inject
    each endpoint into an edge of K_a. If G has v touched coordinate
    vertices, leaflessness demands v<=6. For each v<=6 enumerate all
    distinct unordered graph-edge sets, all distinct placements of the
    multiset of endpoint multiplicities, and then label equal-weight
    edges by their distinct endpoint IDs. Dividing by v! removes the
    auxiliary ordering of the physical coordinate vertices.

    Returns tuple of (v, coefficient Fraction) so the exact probability
    is sum_v c_v*(a)_v / (binom(a,2))_r.
    """
    profile = tuple(multiplicities)
    if not profile or tuple(sorted(profile, reverse=True)) != profile:
        raise ValueError("canonical nonincreasing endpoint profile expected")
    if any(not isinstance(x, int) or x <= 0 for x in profile) or sum(profile) != 6:
        raise ValueError("six positive edge occurrences required")
    r = len(profile)
    placements = set(permutations(profile))
    equal_id_factor = 1
    for count in Counter(profile).values():
        equal_id_factor *= factorial(count)
    result = []
    for v in range(2, 7):
        palette = tuple(combinations(range(v), 2))
        if len(palette) < r:
            continue
        assignments = 0
        for edge_set in combinations(palette, r):
            if len({x for edge in edge_set for x in edge}) != v:
                continue
            for weights in placements:
                degrees = [0] * v
                for (x, y), weight in zip(edge_set, weights):
                    degrees[x] += weight
                    degrees[y] += weight
                if min(degrees) >= 2:
                    assignments += equal_id_factor
        if assignments:
            result.append((v, Fraction(assignments, factorial(v))))
    return tuple(result)


def leafless_projection_probability(a, multiplicities):
    """Exact rational uniform-injective projection probability, a>=4."""
    if not isinstance(a, int) or a < 4:
        raise ValueError("six distinct factor edges require at least K4")
    profile = tuple(sorted(multiplicities, reverse=True))
    coeffs = six_projection_coefficients(profile)
    denominator = falling(comb(a, 2), len(profile))
    if denominator == 0:
        raise ValueError("insufficient distinct coordinate-pair labels")
    numerator = sum((coef * falling(a, v) for v, coef in coeffs), Fraction())
    return numerator / denominator


def projection_power_loss(profile):
    """Power of s lost when a=Theta(s^(3/2)), or None if impossible."""
    coeffs = six_projection_coefficients(tuple(profile))
    if not coeffs:
        return None
    vmax = max(v for v, _ in coeffs)
    return Fraction(3, 2) * (2 * len(profile) - vmax)


def restricted_growth_partitions(t=6):
    """All Bell(t) partitions of named factor-edge endpoints."""
    if t != 6:
        raise ValueError("only six factor edges in this proof slice")

    def visit(sequence):
        if len(sequence) == t:
            yield tuple(sequence)
        else:
            for next_id in range(max(sequence) + 2):
                yield from visit(sequence + [next_id])
    return tuple(visit([0]))


def is_six_factor_forest(left, right):
    """True abstract factor graph cycle test; NOT projected pair graph."""
    if len(left) != 6 or len(right) != 6:
        raise ValueError("six paired incidence edges required")
    if len(set(zip(left, right))) != 6:
        return False
    left_count = max(left) + 1
    parent = list(range(left_count + max(right) + 1))

    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v

    for u, v in zip(left, right):
        x, y = root(u), root(left_count + v)
        if x == y:
            return False
        parent[x] = y
    return True


def profile_for(partition):
    return tuple(sorted(Counter(partition).values(), reverse=True))


def six_forest_power_report():
    """Complete 203^2 factor partition audit, no 425-choose-6 scan.

    Each six-edge factor subgraph is a forest by girth eight. With c
    components, V=(s+1)(s^2+1)=Theta(s^3), Delta=s+1=Theta(s),
    a fixed abstract forest has O(V^c Delta^6) embeddings.
    Independent injective pair labels give two projection losses.
    Bound concerns necessary leaflessness, not GF5 flow positivity.
    """
    shapes = restricted_growth_partitions()
    if len(shapes) != 203 or len(set(shapes)) != 203:
        raise AssertionError("Bell(6) catalog mismatch")
    count = 0
    exponents = Counter()
    example = {}
    for left in shapes:
        left_profile = profile_for(left)
        loss_left = projection_power_loss(left_profile)
        if loss_left is None:
            continue
        for right in shapes:
            right_profile = profile_for(right)
            loss_right = projection_power_loss(right_profile)
            if loss_right is None or not is_six_factor_forest(left, right):
                continue
            components = len(left_profile) + len(right_profile) - 6
            if components < 1:
                raise AssertionError("forest component count invalid")
            exponent = Fraction(3 * components + 6) - loss_left - loss_right
            count += 1
            exponents[exponent] += 1
            example.setdefault(exponent, (left_profile, right_profile))
    if not exponents:
        raise AssertionError("empty forest catalog")
    maximum = max(exponents)
    if maximum != 6:
        raise AssertionError("necessary-only six-trade upper exponent changed")
    return {
        "named_factor_endpoint_partitions_per_side": len(shapes),
        "admissible_leafless_factor_forest_shapes": count,
        "max_leafless_expected_count_power_in_s": str(maximum),
        "shape_exponents": {str(k): exponents[k]
                            for k in sorted(exponents, reverse=True)},
        "one_max_profile_pair": example[maximum],
        "conclusion": "E_label[R3] = O(s^6) necessary-core bound only",
        "strict_R3_exponent_proved": False,
        "positive_GF5_flow_classification_done": False,
        "new_ASET_power_proved": False,
    }


def proof_report():
    catalog = {}
    for part in integer_partitions(6):
        catalog["+".join(map(str, part))] = {
            "coefficients": {str(v): str(c)
                             for v, c in six_projection_coefficients(part)},
            "s_projection_loss": (None if projection_power_loss(part) is None
                                  else str(projection_power_loss(part))),
        }
    return {"projection_profiles": catalog,
            "factor_forest": six_forest_power_report()}


if __name__ == "__main__":
    print(json.dumps(proof_report(), sort_keys=True, indent=2))
