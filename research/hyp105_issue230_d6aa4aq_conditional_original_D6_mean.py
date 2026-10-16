"""HYP-105 #230 AA4-AQ — ONE-MAP ADVERSARIAL conditional original D6 mean.

NEW quantified all-h theorem (distinct from AA4-AA uniform random f/g):
For ANY genuine original symplectic W(3,s), s=2^h>=4, and ANY
globally COMPLETE injective original point f AND arbitrary globally
occupied original line physical image E_g of V pairs in K_a, randomly
PERMUTE the V ACTUAL original line factors' fixed pair labels among
their original sources (no resampling physical support). For the SAME
global point f and ONE global permuted line map throughout all Q,

  E_permutation S_D6(f, g∘pi)
    = A6(f) * 12 C6(E_g)/(V)_6,

where A6(f) is the TRUE-original number of six-distinct-incidence
SOURCE matching Q whose six distinct ORIGINAL point factors form one
physical connected C6 under fixed f; C6(E_g) is number of simple
undirected six-cycles of globally OCCUPIED physical line pair image.

If m=binom(a,2)-V<=a-2, every K_a subset with V edges obeys
  C6 >= (a)_6/12 - m*(a-2)_4,
by deleting at most (a-2)_4 cycles for each missing physical edge.
And ORIGINAL GQ has any distinct two points sharing at most ONE
line, giving >=d^6-15d^4 source line SDRs per six original points
(d=s+1>=5). Thus for EVERY f and every E_g:
  E_perm S_D6 >=12*Cmin²*d^4*(d²-15)/(V)_6
              >= (2/3)*s^6   for ALL dyadic s>=4.
For s=2 one original matching per physical C6 by regular graph Hall
gives an exact positive weaker bound without claiming 2/3*s6.
Uniform 2/3 proof: s4 direct integer Fraction; s>=8, a>=35:
 Cmin/Cfull>=2/3, (a)_6/a^6>=3/5, d>=9 implies
 (d^6-15d^4)/d^6>=22/27; V<=a²/2. Product
  (16/3)*(2/3)^2*(3/5)^2*(22/27)=1408/2025>2/3.

Consequently for EVERY fixed globally complete point f and any
allowed occupied line physical image, there EXISTS a favorable
permutation of line factor physical edges with D6 >=2*s6/3.
This is a nontrivial one-sided conditional expectation/existence
theorem, NOT the adversarial FOR ALL (f,g) original #230 Branch A.
Counter-witness W32 S68/S72 fixed pairs have D6 ZERO.
Classical union bound, Hall and probabilistic method acknowledged.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations,permutations
from math import comb, isqrt

from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _actual_strict_original_transport,
)


def _falling(n,k):
    if type(n) is not int or type(k) is not int or n<k or k<0:
        raise ValueError("nonnegative falling n>=k integers")
    t=1
    for i in range(k):
        t*=n-i
    return t


def minimal_physical_GQ_parameters(s):
    if type(s) is not int or s<2 or (s&(s-1)):
        raise ValueError("only genuine symplectic GQ W(3,2^h), h>=1")
    V=(s+1)*(s*s+1)
    d=s+1
    a=(1+isqrt(1+8*V))//2
    while comb(a,2)<V:a+=1
    assert comb(a-1,2)<V<=comb(a,2)
    return V,d,a,comb(a,2)-V


def six_cycle_image_lower(s):
    V,d,a,m=minimal_physical_GQ_parameters(s)
    full=_falling(a,6)//12
    removed=m*_falling(a-2,4)
    minimum=full-removed
    assert minimum>=0
    return {
        "s":s,"V":V,"d":d,"a":a,"m":m,
        "complete_Ka_undirected_C6":full,
        "each_missing_physical_edge_C6_deletion_max":_falling(a-2,4),
        "minimum_globally_occupied_C6_by_union_bound":minimum,
        "for_every_V_occupied_physical_pairs":True}


def all_h_one_side_permutation_D6_theorem(s):
    z=six_cycle_image_lower(s)
    V,d,a,m=(z[k] for k in ("V","d","a","m"))
    C=z["minimum_globally_occupied_C6_by_union_bound"]
    q=d**4*(d*d-15) if s>=4 else 1
    assert q>=1
    denominator=_falling(V,6)
    lower=Fraction(12*C*C*q,denominator)
    if s>=4:
        if s==4:
            assert lower>=Fraction(2,3)*s**6
        else:
            assert s>=8 and a>=35 and d>=9
            # Exact elementary inequalities, avoiding numeric
            # asymptotic fitting or fake high-h finite GQ construction.
            assert 3*C>=2*z["complete_Ka_undirected_C6"]
            assert Fraction(_falling(a,6),a**6)>=Fraction(3,5)
            assert Fraction(q,d**6)>=Fraction(22,27)
            assert 2*V<=a*a
            assert Fraction(1408,2025)>Fraction(2,3)
            assert lower>=Fraction(1408,2025)*s**6
    return {
        **z,
        "source_original_six_points_injective_neighbor_choices_at_least":q,
        "conditional_exact_denominator_original_six_line_factor_assignments":
            denominator,
        "any_fixed_point_global_f_and_any_fixed_line_occupied_image_expectation_lower":
            lower,
        "all_complete_original_two_typed_supports_one_sided_mean_at_least_two_thirds_s6":
            s>=4,
        "some_GLOBALLY_complete_line_source_permutation_has_D6_at_least":
            (lower.numerator+lower.denominator-1)//lower.denominator,
        "relative_to_s6_uniform_lower":lower/Fraction(s**6),
        "requires_random_GLOBAL_line_source_factor_assignment":
            True,
        "does_NOT_hold_for_EACH_FIXED_GLOBAL_f_g":True,
        "full_seven_GF5_s6_every_two_global_maps_NOT_PROVED":True,
        "root_issue230_A_B_C_OPEN":True}


def _image_edges_and_inverse(global_labels,a):
    seen={}
    for source,edge in enumerate(global_labels):
        u,v=edge
        if not(0<=u<v<a) or (u,v) in seen:
            raise ValueError("not a global injection into canonical K_a edges")
        seen[(u,v)]=source
    return seen


def independent_occupied_C6_cycle_census(global_labels,a,*,limit_a=6):
    """Finite EXACT physically occupied simple undirected 6cycles:
    an unrelated six-vertex permutation generator, canonical dedup.
    Strict bounded a=6 for all W32 tests; never fake huge W34 census.
    """
    if a>limit_a:
        raise ValueError("full physical C6 enumeration budget exceeded")
    inv=_image_edges_and_inverse(global_labels,a)
    cycles={}
    for vertices in permutations(range(a),6):
        edges=tuple(tuple(sorted((vertices[i],vertices[(i+1)%6])))
                    for i in range(6))
        if not all(e in inv for e in edges):
            continue
        key=tuple(sorted(edges))
        cycles.setdefault(key,tuple(inv[e] for e in edges))
    return cycles


def true_original_six_line_SDR_count(point_source_ids,original_neighbors):
    """Independent of physical g. TRUE original GQ 6-point -> six
    DIFFERENT original line factors count using source regularity.
    Line-major 6-bit dynamic programming, not a cartesian product.
    """
    ps=tuple(point_source_ids)
    if len(ps)!=6 or len(set(ps))!=6:
        raise ValueError("six distinct original point source IDs")
    neighbors=[set(original_neighbors[p]) for p in ps]
    if any(not x for x in neighbors):raise ValueError("incomplete genuine GQ source")
    union=sorted(set().union(*neighbors))
    dp=[0]*64
    dp[0]=1
    for line in union:
        mask=sum(1<<i for i in range(6) if line in neighbors[i])
        for subset in range(63,-1,-1):
            if not dp[subset]:continue
            unused=mask&~subset
            while unused:
                low=unused&-unused
                dp[subset|low]+=dp[subset]
                unused-=low
    return dp[63]


def _original_six_line_SDR_by_distinct_permutation(ps,original_neighbors):
    """Separately enumerates ACTUAL original six-source-line-flag
    assignments via line ID tuples, independent of bitmask DP."""
    good=0
    seen=set()
    for p in ps:
        seen.add(p)
    if len(seen)!=6:raise ValueError("six different source points")
    def explore(i,used):
        if i==6:return 1
        count=0
        for l in original_neighbors[ps[i]]:
            if l not in used:
                count+=explore(i+1,used|{l})
        return count
    return explore(0,set())


def exact_true_original_W32_conditional_D6_mean(model, *,
                                                 direct_source_check=True):
    """Exact conditional mean for fixed arbitrary TRUE original f and
    fixed line-edge OCCUPANCY image, random one permutation of line
    original factors across those very same physical line edges.
    NEVER randomize f or redraw g per Q. Genuine W32 physical K6.
    """
    s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("full finite original source C6 census W32 only")
    fcycles=independent_occupied_C6_cycle_census(f,a)
    gcycles=independent_occupied_C6_cycle_census(g,a)
    point_sdr_weight=0
    checked_source_sets=set()
    for edges,point_order in fcycles.items():
        ps=tuple(point_order)
        if len(set(ps))!=6:raise AssertionError("source physical C6 repeats")
        q=true_original_six_line_SDR_count(ps,np)
        if direct_source_check:
            q2=_original_six_line_SDR_by_distinct_permutation(ps,np)
            if q!=q2:raise AssertionError("independent true ORIGINAL six matching paths mismatch")
        point_sdr_weight+=q
        checked_source_sets.add(tuple(sorted(ps)))
    # Each physical simple C6 contributes one source point *set*.
    if len(checked_source_sets)!=len(fcycles):
        raise AssertionError("globally injected source f simple cycle repeated source set")
    probability=Fraction(12*len(gcycles),_falling(V,6))
    expectation=point_sdr_weight*probability
    lower=all_h_one_side_permutation_D6_theorem(s)[
        "any_fixed_point_global_f_and_any_fixed_line_occupied_image_expectation_lower"]
    if expectation<lower:raise AssertionError("conditional mean global support lower false")
    return {
        "s":s,"V":V,
        "point_global_physically_occupied_C6":len(fcycles),
        "line_FIXED_global_image_physically_occupied_C6":len(gcycles),
        "original_source_six_points_six_distinct_line_Flag_matchings_given_f":
            point_sdr_weight,
        "exact_probability_random_SINGLE_global_line_source_perm_gives_ALIGNED_D6":
            probability,
        "exact_conditional_D6_six_original_FLAG_Q_expectation":expectation,
        "original_source_six_SDR_DP_vs_independent_recursive_permutation_checked":
            bool(direct_source_check),
        "never_redraws_source_line_map_for_different_incidence_Q":True,
        "all_global_f_g_adversarial_lower_NOT_PROVED":True}


def independent_W32_original_source_sixpoint_first_mean(model):
    """Second order-independent ORIGINAL POINT-SET-FIRST oracle:
    iterate ALL C(15,6)=5005 actual original point 6-sets,
    test their physical f six-cycle directly by source factor degree,
    then count genuine line source injections by DP. Never call physical
    6cycle permutation enumerator or D6 source path algorithm.
    """
    s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("strict genuine original W32 only")
    cycles=0;sourcematch=0
    for ps in combinations(range(V),6):
        degrees=Counter(x for p in ps for x in f[p])
        if len(degrees)!=6 or any(n!=2 for n in degrees.values()):
            continue
        adjacent={x:set() for x in degrees}
        for p in ps:
            u,v=f[p]
            adjacent[u].add(v);adjacent[v].add(u)
        reached={min(adjacent)}
        pending=list(reached)
        while pending:
            for v in adjacent[pending.pop()]:
                if v not in reached:
                    reached.add(v);pending.append(v)
        if len(reached)!=6:continue
        cycles+=1
        sourcematch+=true_original_six_line_SDR_count(ps,np)
    line_support_cycles=independent_occupied_C6_cycle_census(g,a)
    return {
        "point_six_source_subset_first_connected_C6":cycles,
        "source_original_six_distinct_line_flag_matchings":sourcematch,
        "conditional_D6_expectation_original_point_subset_first":
            Fraction(12*sourcematch*len(line_support_cycles),
                     _falling(V,6)),
        "source_first_not_physical_C6_enumerator":True}
