"""HYP-105 B3.1-B2-A: first nonmatching original-factor forest GF5 census.

Exactly six distinct factor incidences; two share ONE left factor vertex,
and all other point vertices and ALL six right factor vertices are distinct.
Restrict to leafless projections touching six physical coordinates EACH.
Left: two parallel dual column edges between columns 0 and 1 plus a C4
on columns 2..5. Right: a simple two-factor, C6 or C3+C3.

The theorem is exact on this restricted stratum, for every s=2^h:
all ten balanced signed events are GF5-positive for each actual occurrence.
Neither repeated-endpoint forests outside this slice nor any fixed-label
upper R2/R3 bound is claimed. The finite GF5 computation reuses the
previously independently tested prescribed-boundary flow identity.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import comb
import json

from hyp105_g5e2b3b1_critical_flows import (
    SIGNS, two_factors, exact_nowherezero_signed_flow,
)

N = 6
ALL_MASK = (1 << N) - 1
LEFT = tuple(sorted(((0, 1), (0, 1), (2, 3), (3, 4),
                     (4, 5), (2, 5))))
RIGHT = two_factors()
FLOW_DENOMINATOR = 51**6
EXPECTED_ORBITS = 66
EXPECTED_WEIGHT_SUM = 3902064
EXPECTED_SIGNED_COEFFICIENT = 11706192
MIN_GF5_WEIGHT = 4560


def _relabel_graph(graph, perm):
    return tuple(sorted(tuple(sorted((perm[u], perm[v]))) for u,v in graph))


def _relabel_sign(mask, perm):
    image = sum(1 << perm[i] for i in range(6) if mask & (1 << i))
    return image if image & 1 else ALL_MASK ^ image


def left_automorphisms():
    """Full S2 x D8 stabilizer, preserving TWO parallel colored coordinates."""
    group = tuple(p for p in permutations(range(6))
                  if _relabel_graph(LEFT, p) == LEFT)
    if len(group) != 16:
        raise AssertionError("incorrect parallel-edge and C4 stabilizer")
    return group


def signed_orbits():
    """70 right 2-factors x 10 unordered sign splits / fixed LEFT automorphisms.

    Correctly retain repeated left parallel edges; do not apply old
    simple-six-matching orbit normalization.
    """
    group = left_automorphisms()
    weight = Counter()
    for right in RIGHT:
        for mask in SIGNS:
            representative = min(
                (_relabel_graph(right, perm), _relabel_sign(mask, perm))
                for perm in group)
            weight[representative] += 1
    if len(weight) != EXPECTED_ORBITS or sum(weight.values()) != 700:
        raise AssertionError("cherry matching/right sign orbit mass changed")
    return tuple(sorted(weight.items()))


def supports_for_edges(left, right):
    """Physical coordinate per colored GRAPH EDGE, parallel edges distinct.

    The left factor pair label of columns 0 and 1 coincides because they
    share one original factor endpoint, not because original columns
    coincide. Each column has two distinct physical coordinates per half.
    """
    if len(left) != 6 or len(right) != 6:
        raise ValueError("two six-coordinate projected multigraphs required")
    supports = [[] for _ in range(6)]
    for block, graph in enumerate((left, right)):
        for index, (u,v) in enumerate(graph):
            if not (0 <= u < v < 6):
                raise ValueError("invalid dual column adjacency edge")
            supports[u].append(6*block+index)
            supports[v].append(6*block+index)
    result = tuple(tuple(sorted(row)) for row in supports)
    if any(len(row) != 4 or len(set(row)) != 4 for row in result):
        raise AssertionError("not a valid 2+2 four-coordinate column")
    if len(set(result)) != 6:
        raise AssertionError("different factor incidences must have different supports")
    return result


@lru_cache(maxsize=1)
def census():
    """Exact GF5 inclusion-exclusion on every signed S2 x D8 orbit."""
    stats = Counter()
    orbit_stats = Counter()
    right_type = Counter()
    total_weight = 0
    minimum = None
    maximum = 0
    witnesses = []
    for ((right, mask), mass) in signed_orbits():
        n = exact_nowherezero_signed_flow(LEFT, right, mask)
        if not isinstance(n,int) or not 0 <= n <= FLOW_DENOMINATOR:
            raise AssertionError("invalid exact GF5 flow coefficient")
        kind = "C6" if _connected(right) else "2C3"
        # Connectivity of the right graph is exactly its C6 / 2C3 type.
        stats["positive" if n else "zero"] += mass
        orbit_stats["positive" if n else "zero"] += 1
        right_type[(kind, "mass")] += mass
        right_type[(kind, "weighted")] += mass*n
        total_weight += mass*n
        minimum = n if minimum is None else min(minimum, n)
        maximum = max(maximum, n)
        if len(witnesses) < 3 or n in (MIN_GF5_WEIGHT, 6786):
            if len(witnesses) < 8:
                witnesses.append((right,mask,n,mass))
    if (stats != Counter({"positive":700}) or minimum != MIN_GF5_WEIGHT
            or maximum != 6786 or total_weight != EXPECTED_WEIGHT_SUM
            or right_type[("C6","mass")] != 600
            or right_type[("2C3","mass")] != 100
            or right_type[("C6","weighted")] != 3354936
            or right_type[("2C3","weighted")] != 547128):
        raise AssertionError("complete GF5 cherry-classification certificate changed")
    # Three C4 patterns on the four named nonrepeated columns.
    # Fifteen choices of original repeated column pair are independent
    # combinatorial positions; physical realizations are treated below.
    return {
        "original_factor_shape":"one repeated left point, six distinct right lines",
        "physical_shape":"left double-edge plus C4, right C6 or 2C3",
        "left_fixed_projected_C4_types":3,
        "right_dual_2_factors":len(RIGHT),
        "sign_partitions":len(SIGNS),
        "signed_cases_fixed_left":700,
        "signed_symmetry_orbits_fixed_left":len(signed_orbits()),
        "positive_signed_cases_fixed_left":stats["positive"],
        "zero_signed_cases_fixed_left":stats["zero"],
        "flow_min":minimum,"flow_max":maximum,
        "sum_weights_fixed_left":total_weight,
        "sum_weights_all_three_left_C4":3*total_weight,
        "right_C6_weight_total":right_type[("C6","weighted")],
        "right_2C3_weight_total":right_type[("2C3","weighted")],
        "witnesses":tuple(witnesses),
        "all_nonmatching_factor_forests_classified":False,
        "full_R3_upper_proved":False,
        "new_ASET_exponent":False,
    }


def _connected(graph):
    """Classify right simple 2-factor by connectivity, independent of flow."""
    seen={0}
    queue=[0]
    while queue:
        u=queue.pop()
        for a,b in graph:
            neighbor = b if a == u else (a if b == u else None)
            if neighbor is not None and neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return len(seen) == 6


def falling(n,k):
    if not isinstance(n,int) or not isinstance(k,int) or n<k or k<0:
        raise ValueError("falling factorial requires integer n>=k>=0")
    out=1
    for i in range(k):
        out *= n-i
    return out


def all_h_cherry66_expectation(s):
    """Exact expected cherry/6/6 R3 identity and explicit positive lower.

    M_cherry: actual count of original factor six-edge forests with one
    unique repeated LEFT point and all six distinct RIGHT lines.
    E[R3_cherry66] =
      M_cherry * 11706192 * (a)_6^2 /
        (2 * 51^6 * (K)_5 * (K)_6).
    Factor 1/2 is ESSENTIAL: two physical left coordinates have the
    identical incidence mask {0,1}, so each physical configuration has
    (a)_6 / 2 ordered coordinate realizations, not (a)_6.
    The greedy matching construction gives a strict uniform-in-s
    M_cherry lower, and both lower/upper are Theta(s^21).
    """
    if not isinstance(s,int) or s<2 or s & (s-1):
        raise ValueError("s=2^h with h>=1 required")
    V=(s+1)*(s*s+1)
    delta=s+1
    N=V*delta
    a=2
    while comb(a,2)<V:
        a+=1
    K=comb(a,2)
    # Choose unique cherry center and its two incident original edges.
    cherry_centers=V*comb(delta,2)
    greedy=Fraction(cherry_centers,1)
    for j in range(4):
        greedy *= Fraction(N-(3+2*j)*delta,j+1)
    if greedy<=0:
        raise AssertionError("greedy six-edge factor forest count failed")
    upper=cherry_centers*comb(N,4)
    if greedy>upper:
        raise AssertionError("factor forest matching lower exceeds upper")
    # The sum over balanced sign splits and three LEFT C4 patterns.
    numerator=EXPECTED_SIGNED_COEFFICIENT*falling(a,6)**2
    denominator=2*FLOW_DENOMINATOR*falling(K,5)*falling(K,6)
    expected_per_cherry=Fraction(numerator,denominator)
    return {
        "s":s,"V":V,"N":N,"a":a,"K":K,
        "count_lower":greedy,
        "count_upper":upper,
        "exact_expected_R3_identity":
            "M_cherry * 11706192*(a)_6^2/(2*51^6*(K)_5*(K)_6)",
        "expected_R3_lower":greedy*expected_per_cherry,
        "expected_R3_upper":upper*expected_per_cherry,
        "asymptotic":"E[R3_cherry66]=Theta(s^6) for independent uniform labels",
        "per_label_R3_lower":
            "R3 >= 45600*(U_left_cherry66+U_right_cherry66)/51^6",
        "uniform_fixed_label_U_lower":False,
        "strict_R3_upper_proved":False,
    }


def report():
    c=census()
    c["all_h_examples"]=tuple({
        k:str(v) if isinstance(v,Fraction) else v
        for k,v in all_h_cherry66_expectation(s).items()
    } for s in (2,4))
    return c


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
