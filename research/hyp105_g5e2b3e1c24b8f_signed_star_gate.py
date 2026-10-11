"""HYP-105 C24-B8-F: exact signed-star QAP and certified LOWER relaxation.

FULL physical K_a-edge bijections only. A legal g corresponds to a family of
a stars of size a-1; each original line belongs to two stars, and every two
stars overlap in exactly one original line. Dropping overlap constraints gives
a rigorous lower (not an optimizer / not a seven-score bound).

All arithmetic rational. No scipy, MIP, local searches, independent motifs or
assumption about the nonlinear residual. A finite star certificate is NOT an
all-h Omega(s^6) theorem.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def _valid_weights(influences, a):
    if type(a) is not int or a < 4 or a > 7:
        raise ValueError("bounded exact full-bijection K_a: 4 <= a <= 7")
    n = comb(a, 2)
    pairs = tuple(combinations(range(n), 2))
    if not isinstance(influences, dict) or set(influences) != set(pairs):
        raise ValueError("complete canonical original-pair influence dictionary needed")
    if any(type(influences[p]) not in (int, Fraction) for p in pairs):
        raise ValueError("rational original-pair influences only")
    w = {p: Fraction(influences[p]) for p in pairs}
    for i in range(n):
        if sum((w[min(i,j), max(i,j)] for j in range(n) if j != i),
               Fraction(0)):
            raise ValueError("full physical bijection requires exact zero rows")
    return n, w


def _stars(w, a):
    n = comb(a, 2)
    return tuple(
        (sum(1 << i for i in t),
         sum((w[i,j] for i,j in combinations(t, 2)), Fraction(0)))
        for t in combinations(range(n), a - 1)
    )


def projection_factor(a):
    """Full-bijection row-zero projection: v/lambda_2=(m-3)/(m-1)."""
    if type(a) is not int or a < 4:
        raise ValueError("host a >= 4 required")
    m = comb(a, 2)
    return Fraction(m-3, m-1)


def evaluate_full_star_form(influences, physical_edges, a):
    """One entire g, exact T=sum_u sum_{i<j in star(u)} I_ij."""
    n, w = _valid_weights(influences, a)
    host = set(combinations(range(a), 2))
    if (not isinstance(physical_edges, (tuple, list)) or len(physical_edges) != n
            or any(type(e) is not tuple or e not in host for e in physical_edges)
            or len(set(physical_edges)) != n):
        raise ValueError("all and only distinct canonical host edges required")
    stars = tuple(tuple(i for i,edge in enumerate(physical_edges) if u in edge)
                  for u in range(a))
    if (any(len(t) != a-1 for t in stars)
            or any(len(set(x)&set(y)) != 1 for x,y in combinations(stars,2))
            or any(sum(i in t for t in stars) != 2 for i in range(n))):
        raise AssertionError("complete K_a incidence design lost")
    by_stars = sum(
        (sum((w[i,j] for i,j in combinations(star,2)), Fraction(0))
         for star in stars), Fraction(0))
    # Independent contraction over ALL physical adjacency pairs.
    by_pairs = sum((w[i,j] for i,j in combinations(range(n),2)
                    if set(physical_edges[i]) & set(physical_edges[j])),
                   Fraction(0))
    if by_pairs != by_stars:
        raise AssertionError("signed-star / adjacency contraction mismatch")
    return {"signed_T": by_stars,
            "pair_projection": projection_factor(a)*by_stars,
            "stars": stars, "pairwise_star_intersections_exactly_one": True}


def star_dual_lower_certificate(influences, a=6, sweeps=3):
    """Certified lower for min_g T via ALL |U|=a-1 original-line subsets.

    Any entire g supplies exactly a subsets with each original line occurring
    twice. For arbitrary rational y_i:
       T(g) >= 2 sum_i y_i + a min_{|U|=a-1}(W(U)-sum_{i in U} y_i).
    Coordinate ascent produces one feasible rational dual, NOT the optimum of
    the dual LP or of the assignment problem. Each coordinate is maximized
    analytically using its inside/outside reduced star minimum.
    """
    n,w = _valid_weights(influences, a)
    if type(sweeps) is not int or not 0 <= sweeps <= 20:
        raise ValueError("integer sweeps between 0 and 20 required")
    stars = _stars(w, a)
    masks = tuple(m for m,c in stars)
    costs = tuple(c for m,c in stars)
    reduced = list(costs)
    y = [Fraction(0) for _ in range(n)]
    raw_lower = a*min(costs)
    history = [raw_lower]
    for _ in range(sweeps):
        for i in range(n):
            bit = 1 << i
            # Price with the i-th dual variable deleted; all other prices fixed.
            in_min = min(r + y[i] for mask,r in zip(masks,reduced) if mask & bit)
            out_min = min(r for mask,r in zip(masks,reduced) if not mask & bit)
            new_i = in_min - out_min
            delta = new_i - y[i]
            if delta:
                y[i] = new_i
                reduced = [r-delta if mask & bit else r
                           for mask,r in zip(masks,reduced)]
        value = 2*sum(y, Fraction(0)) + a*min(reduced)
        if value < history[-1]:
            raise AssertionError("exact dual coordinate ascent lost monotonicity")
        history.append(value)
    lower_T = 2*sum(y, Fraction(0)) + a*min(reduced)
    # Revalidate the final certificate independently, rather than trust state.
    reduced_fresh = tuple(c-sum((y[i] for i in range(n) if mask&(1<<i)),
                                Fraction(0))
                          for mask,c in stars)
    if min(reduced_fresh)!=min(reduced) or lower_T < raw_lower:
        raise AssertionError("invalid rational star-dual certificate")
    return {
        "host_coordinates":a, "original_lines":n,
        "star_subset_count":comb(n,a-1),
        "stars_per_global_bijection":a,
        "star_size":a-1, "each_line_star_degree":2,
        "naive_lower_T":raw_lower,
        "dual_y":tuple(y),
        "minimum_reduced_star_cost":min(reduced_fresh),
        "certified_lower_T":lower_T,
        "certified_lower_pair_projection":projection_factor(a)*lower_T,
        "dual_sweep_history":tuple(history),
        "not_an_exact_global_minimum":True,
    }


def conditional_residual_gate(mean, certified_lower_pair_projection):
    """Precise conditional threshold, deliberately NO global R bound claimed.

    If someone INDEPENDENTLY proves R(f,g)>=r for EVERY legal g at this SAME f,
    then S(f,g)>=mean+lower_P+r. A single observed residual cannot serve as r.
    """
    if (type(mean) not in (int,Fraction) or
            type(certified_lower_pair_projection) not in (int,Fraction)):
        raise ValueError("two exact rational inputs required")
    mu, p = Fraction(mean),Fraction(certified_lower_pair_projection)
    return {
        "mean":mu,
        "pair_projection_global_lower":p,
        "residual_lower_needed_for_strict_positive":-mu-p,
        "is_conditional_not_an_accepted_score_lower":True,
        "requires_independent_all_g_pointwise_residual_bound":True,
    }
