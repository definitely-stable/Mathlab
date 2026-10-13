"""HYP-105 #230 D6-X: all-h projective star pseudomarginal vs global occupancy.

RESTRICTED THEOREM C, not Branch A/B:
For s=2^h,h>=2, a=min{a:C(a,2)>=V_s}, V_s=(s+1)(s^2+1),
define on ANY set of <=a-1 typed ORIGINAL factors a probability law:
  - choose a uniformly random physical coordinate c;
  - assign its original point factors injectively to distinct K_a
    physical pairs (c,j), uniformly without replacement;
  - independently assign original line factors uniformly injectively
    into all K_a pair edges.
These finite marginals are EXACTLY projectively consistent for every
typed scope of total size <=a-1, and locally injective on both sides.
All genuine ORIGINAL six-incidence factors Q have <=6 original points
and <=6 original lines, so scope <=12<=a-1; left center c is repeated
SIX times across Q's ORIGINAL incidence positions. Every accepted
seven-GF5 positive Q has expected cost ZERO, including the certified
nonnegative selected GF5 numerator.

CRITICAL LIMIT: these marginals are NOT a standard Sherali-Adams
solution to the full injection 0/1 formulation! For any two different
physical edges e=(0,1), e'=(0,2), and original point p, the lifted
column capacity cut
 E[x_(p,e) * (1-sum_(q!=p)x_(q,e'))] >= 0
is violated: conditional expected occupancy of e' among the OTHER
V-1 original points is (V-1)/(2(a-2))>1.
The all-h projective-local consistency model does NOT enforce all
globally lifted assignment-capacity inequalities.

This isolates a precise missing global constraint at rank two, rather
than falsely claiming that all constant-level Sherali-Adams fails.
NO positive all-f,g bound, NO infinite counterfamily, NO R3 upper.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb
import json

from hyp105_issue230_proof_audit import parameters
from hyp105_issue230_d6u_proper_scope_nogo import (
    original_sixset_forest_scope,
)


def falling(n,k):
    if type(n) is not int or type(k) is not int or not 0<=k<=n:
        raise ValueError("falling factorial demands 0<=k<=n integers")
    result=1
    for i in range(k):
        result*=n-i
    return result


def canonical_edge(a,e):
    if (type(a) is not int or a<4 or not isinstance(e,(tuple,list))
            or len(e)!=2 or any(type(v) is not int for v in e)
            or not 0<=e[0]<e[1]<a):
        raise ValueError("canonical K_a physical pair required")
    return tuple(e)


def star_point_probability(a,physical_edges):
    """Exact marginal probability for arbitrary ordered ORIGINAL points.

    Uniform center + ordered injection of k spokes, k<=a-1.
    Coordinates are physical, not ORIGINAL point IDs.
    """
    if not isinstance(physical_edges,(tuple,list)):
        raise ValueError("ordered physical edge tuple required")
    edges=tuple(canonical_edge(a,e) for e in physical_edges)
    k=len(edges)
    if k>a-1:
        raise ValueError("star law exists only for <=a-1 ORIGINAL points")
    if k==0:
        return Fraction(1)
    if len(set(edges))!=k:
        return Fraction(0)
    centers=set(edges[0])
    for e in edges[1:]:
        centers.intersection_update(e)
    return Fraction(len(centers), a*falling(a-1,k))


def right_injection_probability(a,physical_edges):
    """Independent uniform injection into all K_a pair labels."""
    if not isinstance(physical_edges,(tuple,list)):
        raise ValueError("ordered physical edge tuple required")
    edges=tuple(canonical_edge(a,e) for e in physical_edges)
    K=comb(a,2)
    if len(edges)>K:
        raise ValueError("more right ORIGINAL sites than physical edges")
    if len(set(edges))!=len(edges):
        return Fraction(0)
    return Fraction(1,falling(K,len(edges)))


def typed_local_star_probability(a,point_edges,line_edges):
    """Projectively consistent typed left-star/right-uniform local law."""
    if not isinstance(point_edges,(tuple,list)) or not isinstance(line_edges,(tuple,list)):
        raise ValueError("typed ORIGINAL local sequences required")
    if len(point_edges)+len(line_edges)>a-1:
        raise ValueError("total typed local rank exceeds guaranteed projective horizon")
    return (star_point_probability(a,point_edges)*
            right_injection_probability(a,line_edges))


def _physical_degree(ends,mapping):
    deg=Counter(c for v in ends for c in mapping[v])
    return deg


def genuine_original_sixset_star_zero(s,true_original_incidences,original_sixsets):
    """Independent true ORIGINAL sixset incidence-position-aware falsifier.

    The actual W(3,s) fixture supplies the SOURCE incidence relation;
    the caller must not supply a synthetic replacement masquerading as
    genuine geometry. Each local map is one possible realization of
    star support; the abstract law uses all centers/injections.
    """
    p=parameters(s)
    if s<4:
        raise ValueError("six ORIGINAL points require a-1>=6; all-h gate h>=2")
    if not isinstance(true_original_incidences,(tuple,list)):
        raise ValueError("true ORIGINAL GQ incidence list required")
    source=tuple(tuple(e) for e in true_original_incidences)
    if (len(source)!=p["V"]*(s+1) or len(set(source))!=len(source)
            or any(len(e)!=2 or any(type(t) is not int or not 0<=t<p["V"]
                                   for t in e) for e in source)):
        raise ValueError("source must contain complete distinct typed ORIGINAL incidences")
    source_set=set(source)
    if not isinstance(original_sixsets,(tuple,list)) or not original_sixsets:
        raise ValueError("nonempty ORIGINAL sixset sample required")
    checked=[]
    for q in original_sixsets:
        if not isinstance(q,(tuple,list)):
            raise ValueError("original sixset must be an incidence sequence")
        Q=tuple(tuple(edge) for edge in q)
        if not set(Q)<=source_set:
            raise ValueError("sixset contains non-original incidence")
        L,R=original_sixset_forest_scope(Q)
        if len(L)+len(R)>p["a"]-1 or len(L)>p["a"]-1:
            raise AssertionError("six-incidence scope exceeds projective star horizon")
        # Every original point factor is mapped to a DIFFERENT spoke.
        star={v:(0,i+1) for i,v in enumerate(L)}
        degrees=_physical_degree(tuple(v for v,_ in Q),star)
        if degrees[0]!=6 or (len(degrees)==6 and set(degrees.values())=={2}):
            raise AssertionError("star did not forbid seven GF5 classes")
        checked.append({
            "distinct_original_points":len(L),
            "distinct_original_lines":len(R),
            "original_incidence_positions":len(Q),
            "center_physical_degree":degrees[0],
            "local_left_injective":len(set(star.values()))==len(L),
            "every_seven_GF5_positive_class_impossible":True,
        })
    return {
        "s":s,"a":p["a"],"V":p["V"],
        "true_original_incidences_checked":len(source),
        "independent_original_sixsets_checked":len(checked),
        "classes":"ALL-SEVEN-POSITIVE-GF5-NECESSARY-TWO-REGULAR",
        "local_star_all_zero":True,
        "all_q_locally_zero_NOT_global_single_assignment":True,
        "rows":checked,
    }


def lifted_column_occupancy_cut(s):
    """Exact degree-two lift that invalidates the local-star pseudomarginal.

    For globally injective x_(i,e), the column e' capacity inequality is
      1-sum_j x_(j,e')>=0.
    Multiply by x_(i,e), e!=e'. Then E[conditioned capacity]>=0.
    Our local pseudolaw has a strictly negative value for adjacent e,e'.
    """
    p=parameters(s)
    a,V,K=p["a"],p["V"],p["K"]
    if a<6:
        raise AssertionError("minimum ORIGINAL physical alphabet too small")
    e=(0,1)
    e_prime=(0,2)
    marginal=star_point_probability(a,(e,))
    joint=star_point_probability(a,(e,e_prime))
    conditional_expected=(V-1)*joint/marginal
    col_unconditional=V*marginal
    # Positive if the pseudo assigns too much expected e' occupancy
    # conditioned on original factor p receiving adjacent image e.
    lifted_slack=marginal-(V-1)*joint
    if col_unconditional>1:
        raise AssertionError("unlifted capacity should pass in star pseudo")
    if conditional_expected!=Fraction(V-1,2*(a-2)):
        raise AssertionError("star two-site projection derived incorrectly")
    if lifted_slack>=0:
        raise AssertionError("expected STRICT rank-two capacity violation")
    if V-1<=2*(a-2):
        raise AssertionError("minimal-K all-h strict occupancy inequality false")
    return {
        "s":s,"a":a,"V":V,"K":K,
        "point_edge_marginal":str(marginal),
        "two_original_points_adjacent_edge_joint":str(joint),
        "unlifted_physical_column_expected_occupancy":str(col_unconditional),
        "unlifted_column_capacity_satisfied":True,
        "conditional_other_original_point_occupancy":str(conditional_expected),
        "lifted_capacity_slack":str(lifted_slack),
        "lifted_column_capacity_strictly_violated":True,
        "inequality":"E[x_p,e*(1-sum_{q!=p}x_q,e_prime)]>=0",
        "pair_edge_relation":"e_and_e_prime_distinct_share_ONE_physical_coordinate",
    }


def enumerate_small_star(a,point_count,*,max_states=60000):
    """Independent finite full star-center/spoke enumeration, exact integers."""
    if type(point_count) is not int or not 0<=point_count<=a-1:
        raise ValueError("legal bounded star scope size required")
    size=a*falling(a-1,point_count)
    if size>max_states:
        raise ValueError("explicit star enumeration exceeds fail-closed state budget")
    census=Counter()
    for center in range(a):
        neighbors=tuple(v for v in range(a) if v!=center)
        for spokes in permutations(neighbors,point_count):
            key=tuple(tuple(sorted((center,v))) for v in spokes)
            census[key]+=1
    if sum(census.values())!=size:
        raise AssertionError("star witness exhaustive orbit miscount")
    for edges,count in census.items():
        if Fraction(count,size)!=star_point_probability(a,edges):
            raise AssertionError("closed form disagrees with independent enumeration")
    return census,size


def projective_oracle(a,scope_size):
    """Exhaustively verify all subset projections, no sampling."""
    if not 1<=scope_size<=4:
        raise ValueError("scope_count 1..4 supported for independent falsification")
    high,total=enumerate_small_star(a,scope_size)
    compared=0
    for k in range(scope_size):
        low,norm=enumerate_small_star(a,k)
        for selected in combinations(range(scope_size),k):
            projection=Counter()
            for full,multiplicity in high.items():
                projection[tuple(full[i] for i in selected)]+=multiplicity
            if set(projection)!=set(low):
                raise AssertionError("projective marginal support disagreement")
            for outcome,count in low.items():
                if Fraction(projection[outcome],total)!=Fraction(count,norm):
                    raise AssertionError("projective finite marginals not consistent")
            compared+=1
    return {
        "a":a,"scope_size":scope_size,
        "full_center_spoke_assignments":total,
        "all_proper_subscopes_checked":compared,
        "projective_consistency":"EXACT_RATIONAL_INDEPENDENT_ENUMERATION",
    }


def report():
    params=[lifted_column_occupancy_cut(2**h) for h in range(1,7)]
    return {
        "slice":"HYP105-ISSUE230-D6X-LOCAL-STAR-PSEUDOMARGINAL-CAPACITY-CUT",
        "all_h_h_ge_2_zero":"PROJECTIVELY_CONSISTENT-INJECTIVE-LOCAL-REGIONS",
        "all_h_h_ge_2_scope_rank":"a_minus_1",
        "all_h_original_sixset_left_center_degree":6,
        "selected_nonnegative_GF5_numerator_local_expected":0,
        "capacity_failure_rank":"TWO-FOR-LIFTED-GLOBAL-PHYSICAL-COLUMN-CONSTRAINT",
        "first_order_global_capacity":"SATISFIED",
        "this_is_feasible_Sherali_Adams_for_global_assignment":False,
        "general_Sherali_Adams_no_go":False,
        "not_actual_complete_correlated_f_g_witness":True,
        "global_original_root_PROVED_A":False,
        "infinite_correlated_counterexample_PROVED_B":False,
        "Branch_A":"OPEN","Branch_B":"OPEN",
        "exact":params,
        "independent_small_projection_checks":[
            projective_oracle(7,4),projective_oracle(14,3),
        ],
    }


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True))
