"""AA4-BL: exact TWO pinned original-root opposite images, TRUE original B/A.

ALL genuine dyadic s>=32, every actual cherry alpha=(p,l1), beta=(p,l2),
any fully fixed source-side physical injection f, occupied opposite right
support E, and any TWO DISTINCT opposite physical edges e1,e2 IN E
pinned as g(l1)=e1, g(l2)=e2, ONE global uniformly chosen COMPLETE
bijection on remaining V-2 genuine LINE IDs:
 E H_BA = N_BA(alpha,beta;f) * 4! T_A(E;e1,e2)/(V-2)_4.
Not independent g per source Q; this is one globally coherent g.

NEW robust per-root bound E H_BA >=4(s+1) if physical complement
maximum degree Delta(K_a\\E) <=(a-4)/8, a>=261. No such claim if
E has very concentrated holes. The generic abstract pendant-edge
counterexample has m=a-2 holes, and is EXPLICITLY NOT asserted
realizable for any given dyadic s's particular V value.
"""
from fractions import Fraction
from itertools import combinations,permutations
from math import comb

from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import _params
from hyp105_issue230_d6aa4be_original_D6_pins import falling
from hyp105_issue230_d6aa4bk_each_cherry_BA import (
    root_cherry_BA_quenched_all_h_lower,
    genuine_original_root_BA_source_pool,
)


def occupied_A_six_two_pinned_edges(E,a,e1,e2):
    """Exact 70 physical A templates per six-coordinate set, requiring pins.

    Occupied physical E may be NONONTO K_a, original source images may
    have holes. All A targets are UNORDERED edge-subsets: physical 60 C6
    or 10 two-triangles per six-coordinate set. In a rooted original
    B/A sixflag Q, the two pinned actual opposite LINE factor positions
    are distinct, so each target gives 4! assignments of other factors.
    """
    edges=tuple(tuple(sorted(e)) for e in E)
    support=set(edges)
    pins=(tuple(sorted(e1)),tuple(sorted(e2)))
    if len(support)!=len(edges) or any(len(e)!=2 or e[0]==e[1]
                                      or min(e)<0 or max(e)>=a for e in edges):
        raise ValueError("physical occupied edge support must be a simple K_a subgraph")
    if pins[0]==pins[1] or any(pin not in support for pin in pins):
        raise ValueError("two DIFFERENT pinned occupied physical pair edges required")
    if any(len(pin)!=2 or pin[0]==pin[1] for pin in pins):
        raise ValueError("two distinct real physical pair coordinates per pin")
    vertex_union=set(pins[0]+pins[1])
    connected=triangles=0
    for vertices in combinations(range(a),6):
        if not vertex_union<=set(vertices):
            continue
        # One canonical orientation for every undirected 6cycle.
        first=vertices[0]
        for tail in permutations(vertices[1:]):
            order=(first,)+tail
            if order[1]>order[-1]:
                continue
            cycle=frozenset(tuple(sorted((order[i],order[(i+1)%6])))
                            for i in range(6))
            if pins[0] in cycle and pins[1] in cycle and cycle<=support:
                connected+=1
        # Every unordered partition of six coordinates into two triangles
        # has exactly one triangle containing the minimum vertex.
        for other_two in combinations(vertices[1:],2):
            tri1=frozenset((first,)+other_two)
            tri2=frozenset(vertices)-tri1
            doubletri=frozenset(tuple(sorted(pair))
                                for tri in (tri1,tri2)
                                for pair in combinations(sorted(tri),2))
            if pins[0] in doubletri and pins[1] in doubletri and doubletri<=support:
                triangles+=1
    return {"occupied_physical_connected_C6_with_pins":connected,
            "occupied_physical_two_disjoint_C3_with_pins":triangles,
            "occupied_physical_A_six_twofactor_with_both_pins":connected+triangles,
            "pinned_physical_edges_adjacent":len(vertex_union)==3,
            "physical_support_holes":comb(a,2)-len(support)}


def true_original_two_pin_root_conditional_mean(model,side,source_factor,
                                                 source_flag_ids,e1,e2,
                                                 *,vertex_foursets=None):
    """Conditional one-WHOLE-GLOBAL-map mean; fixed-g literal is separate."""
    pool=genuine_original_root_BA_source_pool(
        model,side,source_factor,source_flag_ids,
        vertex_foursets=vertex_foursets)
    physical=(model["right_labels"] if side==0 else model["left_labels"])
    T=occupied_A_six_two_pinned_edges(physical,pool["a"],e1,e2)
    V=pool["V"]
    N=pool["original_six_distinct_incidence_and_opposite_source_factor_Q_count"]
    condp=Fraction(24*T["occupied_physical_A_six_twofactor_with_both_pins"],
                   falling(V-2,4))
    return {
        "s":pool["s"],"V":V,"a":pool["a"],
        "source_original_root_factor":source_factor,
        "source_original_two_actual_incidence_flags":tuple(source_flag_ids),
        "source_sixdistinct_incidence_opposite_factor_Q_pool":N,
        "two_arbitrary_pinned_DISTINCT_global_opposite_physical_edges":
            (tuple(sorted(e1)),tuple(sorted(e2))),
        "right_physical_A_two_pin_templates":T,
        "exact_ONE_whole_global_opposite_completion_two_pin_probability":condp,
        "exact_ONE_whole_global_opposite_completion_expected_BA":
            N*condp,
        "original_given_fixed_other_map_may_be_different_from_these_pins":True,
        "six_actual_original_flag_IDs_always_shared_between_both_sides":True,
        "every_fully_fixed_g_nonzero_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def robust_all_h_two_root_pin_BA_floor(s,missing_max_degree=None):
    """All-h integer/Fraction physical support + genuine source bound.

    Statement: EVERY fixed f,E, and any anchored two opposite physical
    pinned pair-edge images e1,e2∈E; if Delta(K_a\\E)<=floor((a-4)/8),
    mean >=4(s+1). We do NOT manufacture W(3,s) instances for high h.
    """
    if type(s) is not int or s<32 or s&(s-1):
        raise ValueError("all-h robust pinned-root claim only for dyadic s>=32")
    V,a,K,m=_params(s)
    d=s+1
    delta_cap=(a-4)//8
    if missing_max_degree is None:
        Delta=delta_cap
    else:
        Delta=missing_max_degree
    if type(Delta) is not int or Delta<0 or Delta>delta_cap:
        raise ValueError("certified bound requires valid missing-degree Delta≤floor((a-4)/8)")
    C4=3*comb(a-2,4)-m*(a-4)*(a-5)
    N_source=C4*(d-2)*(d-3)*(d-4)*(d-5)
    adj=(a-3)*(a-4)*(a-5)-2*Delta*(a-4)*(a-5)-4*m*(a-5)
    disj=(a-4)*(a-5)-4*Delta*(a-5)
    T_floor=min(adj,disj)
    expectation=Fraction(24*N_source*T_floor,falling(V-2,4))
    if adj*2<(a-3)*(a-4)*(a-5):
        raise AssertionError("adjacent pinned roots conditioned C6 physical floor invalid")
    if disj*2<(a-4)*(a-5):
        raise AssertionError("disjoint pinned roots conditioned C6 physical floor invalid")
    if C4*10<a**4 or (d-2)*(d-3)*(d-4)*(d-5)*2<d**4:
        raise AssertionError("source root actual GQ C4 distinct factor baseline incorrect")
    if 6*(a-4)*(a-5)<5*a*a:
        raise AssertionError("ratio (a-4)(a-5)/a²≥5/6 failed")
    if expectation<4*d:
        raise AssertionError("all-h two-pinned actual source cherry ≥4d conditional mean false")
    return {
        "s":s,"h":s.bit_length()-1,"a":a,"V":V,"m":m,"d":d,
        "allowed_max_missing_degree":Delta,
        "one_source_C4_survivor_count_floor":C4,
        "one_source_original_six_opposite_factors_distinct_pool_floor":N_source,
        "adjacent_pinned_physical_connected_C6_survivor_floor":adj,
        "disjoint_pinned_physical_connected_C6_survivor_floor":disj,
        "both_types_physical_A_with_two_pins_lower":T_floor,
        "exact_one_complete_globally_coherent_conditional_mean_floor":expectation,
        "all_h_each_SOURCE_CHERRY_pinned_mean_ge_4s_plus4":4*d,
        "explicit_extra_max_missing_degree_assumption_REQUIRED":True,
        "all_fully_fixed_correlated_f_g_positive_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def abstract_extreme_holes_two_pin_no_go(a):
    """Sharp physical-support budget warning, not a dyadic W3 family.

    Occupied E=K_a minus ALL (a-2) edges incident to v0 except (0,1).
    Pinned edge (0,1) is pendant, so NO physical degree2 simple A
    template uses it; ANY source root Q with line l1 pinned to it has
    identically zero conditional B/A probability (even if l2 distinct).
    This support has size binom(a-1,2)+1 and DOES NOT necessarily equal
    V=(2^h+1)((2^h)^2+1) for a dyadic h. Never claim otherwise.
    """
    if type(a) is not int or a<6:
        raise ValueError("abstract physical alphabet at least 6 vertices")
    E=tuple((u,v) for u,v in combinations(range(a),2)
            if u!=0 or v==1)
    t=occupied_A_six_two_pinned_edges(E,a,(0,1),(2,3))
    if t["occupied_physical_A_six_twofactor_with_both_pins"]:
        raise AssertionError("physical pendant edge cannot lie in 2regular A")
    return {"a":a,"V_abstract":len(E),"physical_missing_pairs":a-2,
            "pinned_edges":((0,1),(2,3)),
            "all_A_physical_2factors_with_two_pins":0,
            "conditioned_accepted_original_BA_expected_count_for_ANY_source_pool":0,
            "is_NOT_a_proven_dyadic_true_W3_physical_support":True,
            "root_230":"OPEN_WITH_FORMAL_BLOCKER"}
