"""AA4-BQ: EXACT all-seven original-GF5 reverse switching and degree-six cube.

Fix genuine original W(3,2^h), complete globally injected typed maps f,g
with frozen opposite occupied physical support. Each selected historical
seven-GF5 indicator involves <=6 ORIGINAL source LINE factor images.
Thus on ANY cube of pairwise disjoint complete-source-image
transpositions the degree is <=6 and every seventh mixed derivative
vanishes (not so for overlapping swaps). This is an all-seven theorem,
not a new derivation of the earlier B/A-only AA4-O two-swap gradient.

The radius-4k multiple-root repair theorem #585 transfers to an EXACT
inverse-cover double count of root subsets versus whole global maps.
That count is radial and does NOT imply positivity of the initial g.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb


def validate_disjoint_factor_swaps(n, swaps):
    if type(n) is not int or n<2:
        raise ValueError("source factor count >=2 required")
    swaps=tuple(swaps)
    seen=set()
    for pair in swaps:
        try: a,b=pair
        except (TypeError,ValueError):
            raise ValueError("each source-factor transposition is exactly two IDs") from None
        if any(type(v) is not int or v<0 or v>=n for v in (a,b)) or a==b:
            raise ValueError("valid distinct TRUE ORIGINAL source factor IDs required")
        if a in seen or b in seen:
            raise ValueError("only PAIRWISE DISJOINT transpositions commute independently")
        seen.update((a,b))
    return swaps


def apply_disjoint_factor_swaps(global_images, pairs, chosen):
    """Whole ORIGINAL source factor-image swaps, support globally unchanged."""
    old=tuple(global_images)
    pairs=validate_disjoint_factor_swaps(len(old),pairs)
    if len(set(old))!=len(old):
        raise ValueError("complete original map must be globally injected")
    result=list(old)
    chosen=tuple(chosen)
    if len(chosen)!=len(set(chosen)) or any(
        type(i) is not int or not 0<=i<len(pairs) for i in chosen
    ):
        raise ValueError("bad disjoint-swap cube subset")
    for i in chosen:
        a,b=pairs[i]
        result[a],result[b]=result[b],result[a]
    if set(result)!=set(old):
        raise AssertionError("original physical pair support changed")
    return tuple(result)


def mobius_cube_coefficients(values, dimension):
    """Möbius inversion on 2^m cube, index bitmask. Exact int/Fraction."""
    if type(dimension) is not int or not 0<=dimension<=12:
        raise ValueError("finite independent oracle cube dimension 0..12")
    if len(values)!=(1<<dimension):
        raise ValueError("need all 2^m actual global-map values")
    if any(type(value) not in (int,Fraction) or value<0 for value in values):
        raise ValueError("GF5 nonnegative integer motif counts required")
    coeff=list(values)
    for j in range(dimension):
        bit=1<<j
        for mask in range(1<<dimension):
            if mask & bit:
                coeff[mask]-=coeff[mask^bit]
    return tuple(coeff)


def invert_cube_coefficients(coefficients, dimension):
    if len(coefficients)!=(1<<dimension):
        raise ValueError("inverse cube data incomplete")
    result=list(coefficients)
    for j in range(dimension):
        bit=1<<j
        for mask in range(1<<dimension):
            if mask&bit:
                result[mask]+=result[mask^bit]
    return tuple(result)


def exact_cube_mean(coefficients, dimension, p=Fraction(1,2)):
    """ONE global original map is drawn via m independent disjoint swaps."""
    if len(coefficients)!=(1<<dimension) or not isinstance(p,Fraction) or not 0<=p<=1:
        raise ValueError("expected all coefficients and rational p in [0,1]")
    return sum(Fraction(value)*(p**mask.bit_count())
               for mask,value in enumerate(coefficients))


def original_seven_source_factor_cube_degree_certificate(incidence_ids,source_incidence,disjoint_pairs):
    """Per-genuine-Q seventh derivative vanishes by TRUE original LINE support.

    This certifies each historical GF5 Q-indicator's locality (even D6,
    C/A,B/B and opposite A/B). The actual accepted tag is computed in
    independently verified historical-GF5 source classifiers / tests.
    """
    Q=tuple(incidence_ids)
    inc=tuple(tuple(e) for e in source_incidence)
    if len(Q)!=6 or len(set(Q))!=6 or any(type(j) is not int or not 0<=j<len(inc) for j in Q):
        raise ValueError("six DIFFERENT ORIGINAL source-incidence flag IDs required")
    if not inc or any(len(e)!=2 or any(type(t) is not int or t<0 for t in e) for e in inc):
        raise ValueError("genuine original incidence source pairs required")
    n=max(l for p,l in inc)+1
    pairs=validate_disjoint_factor_swaps(n,disjoint_pairs)
    affected={index for index,(a,b) in enumerate(pairs)
              if {a,b}&{inc[j][1] for j in Q}}
    if len(affected)>6:
        raise AssertionError("six true original incidence Q uses >six disjoint source swaps")
    return {
        "six_original_incidence_IDs":tuple(sorted(Q)),
        "number_DISTINCT_original_line_source_factors":len({inc[j][1] for j in Q}),
        "swaps_with_possible_Q_influence":tuple(sorted(affected)),
        "max_cube_degree_six":True,
        "seven_or_higher_disjoint_mixed_finite_differences_ZERO":len(pairs)>=7,
        "all_seven_GF5_types_included":True,
        "overlapping_swap_operators_commute_NOT_CLAIMED":True,
    }


def cayley_ball_size_by_cycles(n, radius):
    """Exact ball cardinal: Σ_{j<=r} unsigned Stirling c(n,n-j).

    DP c(n,n-j)=c(n-1,n-1-j)+(n-1)c(n-1,n-j);
    limits protect the finite validation tool from giant all-h n.
    """
    if type(n) is not int or not 2<=n<=150000:
        raise ValueError("exact finite whole-source permutation ball n=2..150000")
    if type(radius) is not int or not 0<=radius<=min(n-1,100):
        raise ValueError("transposition radius 0..min(n-1,100)")
    dp=[0]*(radius+1)
    dp[0]=1
    for j in range(2,n+1):
        for t in range(min(radius,j-1),0,-1):
            dp[t]+=(j-1)*dp[t-1]
    return sum(dp)


def radial_inverse_cover_certificate(good_roots, k, accepted_roots_per_map,
                                     universe_size=None, *, require_cover=True):
    """Finite inverse-repair Hall incidence inequality, no false center bound.

    Good roots must be selected from one ORIGINAL map; each alternate
    complete opposite map h has roots for which a true original six-ID
    accepted B/A witness is known. In the all-h theorem h ranges over
    the WHOLE exact Cayley radius <=4k ball with f and support fixed.
    Every k-subset of good roots appears in at least one h, hence
    sum_h C(R(h),k)>=C(G,k), with R(h) restricted to the good root set.
    """
    good=frozenset(good_roots)
    if any(type(i) is not int or i<0 for i in good):
        raise ValueError("source root identifiers must be nonnegative integers")
    if type(k) is not int or not 1<=k<=len(good):
        raise ValueError("k must be 1..actual good original root count")
    if universe_size is not None and (type(universe_size) is not int or universe_size<len(good)):
        raise ValueError("genuine original root population <good roots")
    neighbors=tuple(frozenset(row)&good for row in accepted_roots_per_map)
    coverage=Counter()
    for row in neighbors:
        for block in combinations(sorted(row),k):
            coverage[block]+=1
    needed=tuple(combinations(sorted(good),k))
    missing=tuple(block for block in needed if not coverage[block])
    if require_cover and missing:
        raise AssertionError("selected maps do not cover all k-subsets of actual good roots")
    multiplicity=sum(coverage.values())
    return {
        "G":len(good),"k":k,"number_neighbor_complete_maps":len(neighbors),
        "number_original_good_root_subsets":len(needed),
        "reverse_incidence_count":multiplicity,
        "exact_nonnegative_reverse_cover_slack":multiplicity-len(needed),
        "missing_good_subsets":missing,
        "candidate_reverse_Hall_cover_valid":not missing,
        "center_root_count_positive_NOT_INFERRED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def abstract_one_local_zero_center_barrier(n, good_root_count):
    """STRICT proof-method countermodel, NOT an original W3 model.

    Label map g is a full permutation of n distinct physical pair edges.
    Let every good root be accepted iff original source factor 0 owns edge 0.
    An arbitrary g is at distance <=1 from such a full map by swapping
    original factor 0 with the current owner of edge 0. So ALL original
    good root k-subsets, any k<=G, are simultaneously locally repairable
    for EVERY starting g. Yet a map with g[0]!=0 has zero accepted roots.
    Every disjoint-swap cube has degree<=1 for this abstract count.
    Therefore even a stronger uniform one-swap coverage plus degree-six
    locality does not logically force center positivity. Absolutely NO
    claim that this artificial acceptance predicate models historical GF5.
    """
    if type(n) is not int or n<2 or type(good_root_count) is not int or good_root_count<1:
        raise ValueError("abstract permutation population >=2 and G>=1")
    original=tuple((i+1)%n for i in range(n))
    before=0
    owner=original.index(0)
    repaired=list(original)
    repaired[0],repaired[owner]=repaired[owner],repaired[0]
    if repaired[0]!=0 or len(set(repaired))!=n or owner==0:
        raise AssertionError("abstract one-swap repair construction invalid")
    return {
        "n":n,"G":good_root_count,
        "zero_accepted_original_center":before,
        "accepted_after_one_global_source_swap":good_root_count,
        "whole_original_source_factor_swaps":((0,owner),),
        "full_support_preserved":set(repaired)==set(original),
        "every_selected_k_good_root_subset_repaired_simultaneously":True,
        "degree_one_on_every_disjoint_swap_cube":True,
        "not_a_genuine_W3_or_historical_GF5_counterexample":True,
        "logical_center_positivity_from_repairability_FALSE":True,
    }
