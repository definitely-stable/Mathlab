"""HYP-105 #230 / AA4-AM: genuine ORIGINAL 3-flag transport and NO GF5 lift.

For EVERY genuine W(3,2^h), h>=1, and separately FULL globally
injective original point/line -> minimal physical K_a unordered pairs
f,g, put M=F^T B G (the earlier AA4-AL two-type transport).
NEW exact globally coupled 3rd *factorial* moment:

  T3 = sum_{x,y} (M[x,y])_3
     = ordered triples of DIFFERENT actual original incidence IDs
       sharing physical point coordinate x AND physical line coord y.

Every ORIGINAL source flag contributes once per chosen coordinate cell,
not a redrawn map. Let R_{p,y}=#{l incident to p:y in g(l)}
and S_{l,x}=#{p incident to l:x in f(p)}. Then

  all_same_original_point = 2 sum_{p,y}(R_{p,y})_3,
  all_same_original_line  = 2 sum_{l,x}(S_{l,x})_3.

They are disjoint subsets of distinct-flag triples. Thus
  T3_mixed = T3 - same_point - same_line
EXACTLY counts ordered THREE distinct actual source flags having
at least 2 different ORIGINAL point factors AND at least 2 different
ORIGINAL line factors while all share BOTH physical coordinate types.
Such a mixed triple has a UNIQUE (x,y) since two distinct original
typed factors have at most one common physical coordinate per side,
from global pair-image injectivity.

NEW all-h Jensen/degeneracy theorem:
  a² <= 12V/5 (s=2,4 direct; s>=8 by minimal physical alphabet)
  µ=4V(s+1)/a² >= 5(s+1)/3 >= 5.
  sum (M)_3 >= a² µ(µ-1)(µ-2)
  same_point + same_line <= 4V(d)_3
so
  T3_mixed >= (64/9)Vd³ - 8Vd² >= 4Vd³ >= 4s^6.
All quantities are integers, bounds exact Fractions.

CRITICAL NONLIFT: every one of these physically coincident triples
has three selected physical B edges incident to one coordinate and
also three selected physical A edges incident to one coordinate
(count multiplicity). Hence NO 6-ID extension containing that triple
can have either side a degree-2 physical graph; specifically none can
directly charge to the selected 2-regular physical A/B or D6 gateway.
This proves a robust order-s6 physically concentrated ORIGINAL triple
phenomenon, NOT root issue #230 Branch A/B/C, NOT a positive GF5
seven-class six-Q lower, and NOT an infinite counterexample family.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _parameters,_actual_strict_original_transport,
    exact_original_global_transport,
)


def falling3(k):
    if type(k) is not int or k<0:
        raise ValueError("nonnegative integral multiplicity required")
    return k*(k-1)*(k-2) if k>=3 else 0


def all_h_mixed_triple_transport_theorem(s):
    """Restricted but positive ALL-h real-source all-map Ω(s^6) theorem.

    Proves actual physical alphabet inequality with exact integers,
    exact Jensen tangent support and source-repeat degeneracy caps,
    not a finite-h fit or a selected GF5 six-source-motif claim.
    """
    V,d,a=_parameters(s)
    if s in (2,4):
        assert (s,V,a) in ((2,15,6),(4,85,14))
    else:
        assert s>=8 and a>=35
        # V > binom(a-1,2); a>=18 gives
        # 12V/5 > 6(a-1)(a-2)/5 >= a^2.
        assert a*a-18*a+12>=0
    assert 5*a*a<=12*V
    total=4*V*d
    mu=Fraction(total,a*a)
    assert mu>=Fraction(5*d,3)>=5
    f_mu=mu*(mu-1)*(mu-2)
    jensen=Fraction(a*a)*f_mu
    repeat_upper=4*V*falling3(d)
    symbolic=Fraction(64,9)*V*d**3-8*V*d*d
    # Use µ lower, product monotone for µ>=2:
    assert jensen-repeat_upper>=symbolic
    assert symbolic>=4*V*d**3>=4*s**6
    return {
        "s":s,"V":V,"d":d,"a":a,
        "physical_K_a_capacity":comb(a,2),
        "unused_global_physical_pair_images":comb(a,2)-V,
        "sharp_uniform_alphabet_square_upper_5a2_le_12V":True,
        "exact_transport_entry_mean_mu":mu,
        "ordered_distinct_original_flag_triples_bicell_Jensen_lower":
            jensen,
        "ordered_all_same_original_point_or_all_same_original_line_upper":
            repeat_upper,
        "ordered_mixed_original_source_triples_uniform_lower":
            jensen-repeat_upper,
        "simple_analytic_mixed_lower":
            symbolic,
        "simple_every_complete_global_f_g_mixed_lower":4*V*d**3,
        "simple_all_h_at_least_4_s6_ordered":4*s**6,
        "mixed_requires_at_least_two_original_points_AND_two_original_lines":True,
        "all_three_original_points_AND_lines_distinct_NOT_PROVED":True,
        "physical_coord_degree_at_least_three_prevents_2regular_GF5_lift":True,
        "selected_seven_GF5_six_Q_Omega_s6_NOT_PROVED":True,
        "root_issue230_Branch_A_B_C_OPEN":True,
    }


def _original_same_source_falling3_exact(f,g,neighbors_p,neighbors_l):
    point=0
    for ls in neighbors_p:
        r=Counter(y for l in ls for y in g[l])
        point+=2*sum(falling3(k) for k in r.values())
    line=0
    for ps in neighbors_l:
        r=Counter(x for p in ps for x in f[p])
        line+=2*sum(falling3(k) for k in r.values())
    return point,line


def exact_mixed_original_triple_transport(model):
    """Actual ONE f/g true source 3rd factorial tensor, no Q relabeling.

    Builds on AA4-AL global transport with original source validation.
    Computes exact mixed source triples, exact Jensen tangent remainder
    and the old ordered original pair count, keeping GF5 caveat.
    """
    s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(model)
    old=exact_original_global_transport(model)
    M=old["cross_physical_coordinate_transport_matrix"]
    total=sum(falling3(v) for row in M for v in row)
    same_p,same_l=_original_same_source_falling3_exact(f,g,np,nl)
    assert 0<=same_p<=2*V*falling3(d)
    assert 0<=same_l<=2*V*falling3(d)
    mixed=total-same_p-same_l
    assert mixed>=0 and mixed%6==0
    th=all_h_mixed_triple_transport_theorem(s)
    assert mixed>=th["ordered_mixed_original_source_triples_uniform_lower"]
    assert mixed>=4*V*d**3
    mu=th["exact_transport_entry_mean_mu"]
    tangent=Fraction(a*a)*mu*(mu-1)*(mu-2)
    remainder=sum((Fraction(v)-mu)**2*(Fraction(v)+2*mu-3)
                  for row in M for v in row)
    assert remainder>=0 and Fraction(total)==tangent+remainder
    # Convex Jensen tangent holds globally for nonnegative INTEGER v
    # because µ>=5 and (v-µ)^2(v+2µ-3)≥0 for every v≥0.
    return {
        "s":s,"V":V,"d":d,"a":a,
        "same_complete_global_original_point_and_line_maps":True,
        "total_four_coordinate_cells_per_actual_source_flag":4*V*d,
        "actual_transport_3rd_factorial_moment_all_original_flags":total,
        "exact_source_all_same_point_ordered_3flag_subtraction":same_p,
        "exact_source_all_same_line_ordered_3flag_subtraction":same_l,
        "exact_ordered_MIXED_true_original_3flag_bilateral_coord_triples":
            mixed,
        "exact_UNORDERED_MIXED_true_original_3flag_bilateral_coord_triples":
            mixed//6,
        "Jensen_3rd_factorial_transport_lower":tangent,
        "exact_nonnegative_Jensen_tangent_remainder":remainder,
        "every_global_map_lower_from_symbolic_proof":
            th["ordered_mixed_original_source_triples_uniform_lower"],
        "simple_all_h_mixed_triple_lower_4Vd3":4*V*d**3,
        "independent_preexisting_original_two_flag_pair_collision":
            old["exact_ordered_DISTINCT_source_flag_pair_bilateral_physical_collision"],
        "genuine_original_two_type_bicell_mixed_triple_unique_center":True,
        "NO_direct_GF5_lift_due_to_degree_3_in_BOTH_physical_types":True,
        "all_three_original_points_and_lines_distinct_NOT_PROVED":True,
        "no_issue230_universal_seven_GF5_lower":True,
    }


def independent_actual_original_triple_oracle(model,*,max_direct_flags=6000):
    """Independent source-first *physical cell* triple enumeration.

    Does NOT use any M tensor, factorial-moment polynomials or
    source-degeneracy identities. Enumerates unordered triples of
    DIFFERENT actual ORIGINAL flag IDs inside each physically
    coincident point-coordinate/line-coordinate cell; retain only
    triples with >=2 DISTINCT actual point AND >=2 actual line factors.
    Mixed triples appear in exactly ONE physical coordinate cell,
    since two distinct original factors on each side cannot share
    two physical coordinates under global edge injection.
    Also reports a FINITE-ONLY stronger 3+3 distinct-root statistic.
    """
    s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(model)
    if len(inc)>max_direct_flags:
        raise ValueError("bounded genuine finite triple oracle only")
    cells={}
    for fid,(p,l) in enumerate(inc):
        for x in f[p]:
            for y in g[l]:
                cells.setdefault((x,y),[]).append(fid)
    mixed=fully_distinct=all_falling=0
    for ids in cells.values():
        n=len(ids)
        all_falling+=falling3(n)
        for i,j,k in combinations(ids,3):
            p0,l0=inc[i];p1,l1=inc[j];p2,l2=inc[k]
            points=len({p0,p1,p2});lines=len({l0,l1,l2})
            if points>=2 and lines>=2:
                mixed+=1
                fully_distinct+=int(points==3 and lines==3)
    return {
        "s":s,"unordered_mixed_actual_original_triples_brute":mixed,
        "ordered_mixed_actual_original_triples_brute":mixed*6,
        "observed_finite_ONLY_all_3_points_and_lines_distinct":
            fully_distinct,
        "all_point_line_physical_coordinate_bicell_ordered_triples":
            all_falling,
        "number_nonempty_coordinate_cells":len(cells),
        "not_from_transport_M_or_source_subtraction":True,
    }


def independent_brute_original_flag_triplets(model,*,max_flags=80):
    """Second independent ORIGINAL source-first all-flag-combination oracle.

    Enumerates each original unordered 3-incidence-Q ONCE, tests both
    physical typed pair intersections DIRECTLY, no coordinate cell
    grouping, no transport/collision formulas. Strict W32 only.
    """
    s,V,d,a,f,g,inc,np,nl=_actual_strict_original_transport(model)
    if len(inc)>max_flags:
        raise ValueError("restrict O(N^3) direct source-triple oracle")
    good=fully_distinct=0
    for inds in combinations(range(len(inc)),3):
        pairs=[inc[i] for i in inds]
        ps={p for p,_ in pairs};ls={l for _,l in pairs}
        if len(ps)<2 or len(ls)<2:
            continue
        p_common=set(f[pairs[0][0]]) & set(f[pairs[1][0]]) & set(f[pairs[2][0]])
        l_common=set(g[pairs[0][1]]) & set(g[pairs[1][1]]) & set(g[pairs[2][1]])
        if p_common and l_common:
            if len(p_common)!=1 or len(l_common)!=1:
                raise AssertionError("complete global pair injectivity grants unique triple center")
            good+=1
            fully_distinct+=int(len(ps)==3 and len(ls)==3)
    return {
        "unordered_mixed_actual_original_triples_brute":good,
        "observed_finite_ONLY_all_3_points_and_lines_distinct":
            fully_distinct,
        "strict_independent_original_source_flag_triple_enumeration":True,
    }
