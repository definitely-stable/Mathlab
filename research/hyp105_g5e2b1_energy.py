"""HYP-105 G5-E2-B1: exact GF5 weighted additive energy / overlap inversion.

All-m theorem: a signed k-vs-k trade risk is the disjoint-pair component
of the squared distribution of independent k-column weighted sums.
Möbius inversion on intersections gives it EXACTLY; these identities are
classical inclusion-exclusion, not a novel ASET exponent.

Executable counts are strictly finite and work within fixed budgets.
GF5 coordinate vectors are byte strings, NOT integer sums with carries.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb

from hyp105_g5d_affine_weights import checksum_pattern_palette

DEFAULT_PALETTE = checksum_pattern_palette()


def checked_supports(supports, dimension):
    if not isinstance(dimension, int) or dimension < 4:
        raise ValueError("ambient GF5 dimension must be >=4")
    supports = tuple(tuple(s) for s in supports)
    for s in supports:
        if (len(s) != 4 or len(set(s)) != 4 or
            any(not isinstance(c, int) or c < 0 or c >= dimension for c in s)):
            raise ValueError("each support must contain four distinct valid coordinates")
    if len(set(tuple(sorted(s)) for s in supports)) != len(supports):
        raise ValueError("supports must be physically distinct")
    return supports


def checked_palette(palette):
    palette = tuple(tuple(w) for w in palette)
    if not palette or len(set(palette)) != len(palette):
        raise ValueError("palette must be nonempty and without duplicate weights")
    if any(len(w) != 4 or any(not isinstance(x, int) or not 1 <= x <= 4
                              for x in w) or sum(w) % 5 != 4
           for w in palette):
        raise ValueError("only nonzero GF5 4-tuples with checksum4 allowed")
    return palette


def vector_for_support(support, weights, dimension):
    output = bytearray(dimension)
    for coord, weight in zip(support, weights):
        output[coord] = weight
    return bytes(output)


def add_gf5_vectors(a, b):
    if len(a) != len(b):
        raise ValueError("different ambient dimensions")
    return bytes((x+y) % 5 for x,y in zip(a,b))


def _sum_histogram(columns, k_subset, palette, cap):
    """Count EXACT per-GF5-signature independent local weight assignments."""
    n_choices = len(palette)**len(k_subset)
    if n_choices > cap:
        raise ValueError("enumeration would exceed explicitly stated budget")
    histogram = {bytes(len(columns[0][0])): 1}
    for colid in k_subset:
        updated = defaultdict(int)
        for base, multiplicity in histogram.items():
            for column in columns[colid]:
                updated[add_gf5_vectors(base,column)] += multiplicity
        histogram = updated
    if sum(histogram.values()) != n_choices:
        raise AssertionError("some weighted assignments were lost")
    return histogram


def single_signed_trade_mitm(supports, signs, dimension,
                             palette=DEFAULT_PALETTE, max_side_assignments=150000):
    """Exact event flow count via GF5 signed subset-sum meet-in-middle.

    For t=2k (k=2 or 3), enumerate k-side distributions O(51^k)
    rather than the published 2^(4t) b-flow inclusion-exclusion oracle
    or brute 51^(2k). It computes the SAME nowhere-zero flow count,
    but does not yet count how many motifs occur at all m.
    """
    supports = checked_supports(supports, dimension)
    palette = checked_palette(palette)
    k = len(supports)//2
    if (len(supports) not in (4,6) or len(signs) != len(supports) or
        signs.count(1) != k or signs.count(-1) != k or
        any(s not in (-1,1) for s in signs)):
        raise ValueError("expected a balanced 2v2 or 3v3 sign assignment")
    if len(palette)**k > max_side_assignments:
        raise ValueError("meet-in-middle side assignment limit exceeded")
    columns = tuple(tuple(vector_for_support(s,w,dimension) for w in palette)
                    for s in supports)
    plus = tuple(i for i,v in enumerate(signs) if v==1)
    minus = tuple(i for i,v in enumerate(signs) if v==-1)
    a = _sum_histogram(columns, plus, palette, max_side_assignments)
    b = _sum_histogram(columns, minus, palette, max_side_assignments)
    numerator = sum(c*b.get(key,0) for key,c in a.items())
    denominator = len(palette)**(2*k)
    if not 0 <= numerator <= denominator:
        raise AssertionError("invalid exact signed GF5 risk")
    return {
        "t": 2*k, "k": k, "weighted_flow_count": numerator,
        "total_assignments": denominator,
        "exact_probability": Fraction(numerator,denominator),
        "plus_distinct_sums":len(a), "minus_distinct_sums":len(b),
        "algorithm": "two independent exact GF5 k-subset sum histograms",
        "new_exponent_proved":False,
    }


def disjoint_energy_mobius(histograms, k):
    """Exact inclusion-exclusion numerator for unordered disjoint k-sets.

    histograms: dict {sorted k-subset column IDs: Counter(signature->count)}.
    All nonnegative counts, each local histogram uses independent columns.
    For each signature sigma and all S of size r<=k let
    B_S(sigma)=sum_{T superset S, |T|=k} H_T(sigma).
    Then total disjoint unordered pair weighted count =
      1/2 * sum_sigma sum_{r=0}^k (-1)^r sum_{|S|=r} B_S(sigma)^2.
    Includes r=0. Self-pairs disappear since (1-1)^k=0.
    """
    if k not in (2,3):
        raise ValueError("only equal 2v2 / 3v3 risks expected")
    groups = defaultdict(list)
    for subset, hist in histograms.items():
        if (len(subset) != k or tuple(sorted(set(subset))) != subset or
            any(not isinstance(x,int) or x < 0 for x in subset)):
            raise ValueError("invalid k-column subset")
        if any(not isinstance(v,int) or v < 0 for v in hist.values()):
            raise ValueError("nonnegative exact signature counts required")
        for signature,count in hist.items():
            if count:
                groups[signature].append((subset,count))
    numerator_twice = 0
    for entries in groups.values():
        moments = [defaultdict(int) for _ in range(k+1)]
        for subset,count in entries:
            for r in range(k+1):
                for common in combinations(subset,r):
                    moments[r][common] += count
        value = sum((-1)**r * sum(x*x for x in moments[r].values())
                    for r in range(k+1))
        if value < 0 or value % 2:
            raise AssertionError("negative / odd disjoint Möbius energy")
        numerator_twice += value
    if numerator_twice < 0 or numerator_twice % 2:
        raise AssertionError("invalid total disjoint pair count")
    return numerator_twice//2


def risk_from_pair_energy(supports, dimension, palette=DEFAULT_PALETTE,
                          max_local_assignments=160000):
    """Exact R2 for finite small N without enumerating N-choose-4 events.

    Work ~ binom(N,2)*palette_size^2, rather than ~ N^4*palette^4.
    Does NOT imply an improved asymptotic exponent for GQ(s,s).
    """
    supports = checked_supports(supports, dimension)
    palette = checked_palette(palette)
    n = len(supports)
    local = comb(n,2)*len(palette)**2 if n>=2 else 0
    if local > max_local_assignments:
        raise ValueError("requested exact pair enumeration exceeds budget")
    columns = tuple(tuple(vector_for_support(s,w,dimension) for w in palette)
                    for s in supports)
    histograms={}
    for pair in combinations(range(n),2):
        histograms[pair] = _sum_histogram(
            columns,pair,palette,max_local_assignments)
    numerator = disjoint_energy_mobius(histograms,2)
    denom = len(palette)**4
    return {
        "n":n,"k":2,"local_weighted_pair_samples":local,
        "distinct_pair_sum_signatures":len(set().union(
            *(set(h) for h in histograms.values()))) if histograms else 0,
        "exact_disjoint_weight_assignments":numerator,
        "denominator_per_trade":denom,
        "R2":Fraction(numerator,denom),
        "method":"GF5 2-sum-energy with vertex-overlap correction",
        "uniform_GQ_power_proved":False,
    }


def risk_from_energy_finite(supports, dimension, k, palette,
                            max_local_assignments=160000):
    """Generic tiny-N exact R2/R3 verification with bounded palette.

    k=3 with full 51-element palette is deliberately size-capped:
    exact R3 for N=425 requires a new theorem, not a 51^3*N^3 run.
    """
    supports = checked_supports(supports, dimension)
    palette = checked_palette(palette)
    n = len(supports)
    if k not in (2,3):
        raise ValueError("only k2/k3")
    local = comb(n,k)*len(palette)**k if n>=k else 0
    if local > max_local_assignments:
        raise ValueError("exact local signed k-sum computation exceeds cap")
    columns = tuple(tuple(vector_for_support(s,w,dimension) for w in palette)
                    for s in supports)
    histograms={}
    for chosen in combinations(range(n),k):
        histograms[chosen]=_sum_histogram(
            columns,chosen,palette,max_local_assignments)
    numer=disjoint_energy_mobius(histograms,k)
    return {
        "n":n, "k":k, "signature_assignments":local,
        "numerator":numer,
        "denominator_per_trade":len(palette)**(2*k),
        "Rk":Fraction(numer,len(palette)**(2*k)),
        "new_exponent_proved":False
    }
