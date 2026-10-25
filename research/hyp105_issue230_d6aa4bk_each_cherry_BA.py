"""AA4-BK: every SINGLE genuine original SOURCE CHERRY gets positive quenched B/A.

Unlike already-known GLOBAL quenched seven-GF5 expectations (#238/#334/#494),
this is EACH adversarially selected fixed TRUE ORIGINAL cherry α,β,
for ANY complete fixed physical map on its anchored side, ANY fixed
occupied physical support E on the opposite side, and ONE uniformly
random COMPLETE global bijection onto E (NOT independent maps per Q).

The exact conditional mean for the selected original B/A (dual A/B)
rooted event is N_src(αβ;f) * 6! T_A(E)/(V)_6.
Here N_src counts TRUE original fourflag point C4 residuals where
ALL SIX genuine opposite source factors are distinct. T_A(E) is
the number of simple six-edge 2regular sixcoordinate templates on E.

New all-h root-wise (h>=5) lower >= 72(s+1). This holds for EACH
specified ACTUAL original cherry, not just summed over all source
factors. It is STILL a RANDOM OPPOSITE full global map expectation,
not universal positivity for EVERY fully fixed correlated f,g.
"""
from fractions import Fraction
from itertools import combinations,permutations,product
from math import comb

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bj_cherry_hall_defect import _full_four_patterns
from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import _params
from hyp105_issue230_d6aa4be_original_D6_pins import falling


def physical_simple_twofactor_6_count(right_edges,a):
    """Independent exact simple A physical targets on original right E.

    Enumerate every six-coordinate vertex set; 60 connected simple C6
    and 10 unordered two-disjoint-triangle targets per K6 coordinate set.
    Intended for finite genuine original W32/W34 only, not high-h.
    """
    E={tuple(sorted(e)) for e in right_edges}
    if len(E)!=len(tuple(right_edges)) or any(
        len(edge)!=2 or edge[0]==edge[1] or min(edge)<0 or max(edge)>=a
        for edge in E
    ):
        raise ValueError("full fixed occupied typed physical support requires distinct K_a edges")
    cyclic=triangles=0
    for verts in combinations(range(a),6):
        v0=verts[0]
        for tail in permutations(verts[1:]):
            order=(v0,)+tail
            if order[1]>order[5]:continue
            if all(tuple(sorted((order[i],order[(i+1)%6]))) in E
                   for i in range(6)):
                cyclic+=1
        for two in combinations(verts[1:],2):
            tri1=frozenset((v0,)+two)
            tri2=frozenset(verts)-tri1
            if all(tuple(sorted(e)) in E for e in
                   tuple(combinations(sorted(tri1),2))+
                   tuple(combinations(sorted(tri2),2))):
                triangles+=1
    return {"right_connected_C6":cyclic,
            "right_two_disjoint_triangles":triangles,
            "right_simple_twofactor_A_total":cyclic+triangles}


def root_cherry_BA_quenched_all_h_lower(s):
    """Every fixed true-original POINT root cherry; LINE dual too."""
    if type(s) is not int or s<32 or s&(s-1):
        raise ValueError("explicit root-wise theorem requires dyadic s>=32")
    V,a,K,m=_params(s)
    d=s+1
    n=a-2
    full_C4=3*comb(n,4)
    C4_floor=full_C4-m*(n-2)*(n-3)
    C6_full=Fraction(falling(a,6),12)
    C6_floor=C6_full-m*falling(a-2,4)
    orig_distinct_opposite_min=(d-2)*(d-3)*(d-4)*(d-5)
    src=orig_distinct_opposite_min*C4_floor
    p_connected=Fraction(720*C6_floor,falling(V,6))
    mean_lower=src*p_connected
    if a<261 or m>a-2:
        raise AssertionError("minimal physical palette all-h assumptions")
    if C4_floor<Fraction(a**4,10):
        raise AssertionError("root-complement C4 >=a4/10 physical hole lemma")
    if C6_floor<Fraction(a**6,16):
        raise AssertionError("physical right connected C6 >=a6/16 lemma")
    if orig_distinct_opposite_min<Fraction(d**4,2):
        raise AssertionError("original GQ source four-neighbor distinct-line lower")
    if V*2>a*a or V>d**3:
        raise AssertionError("minimal physical support to source degree inequalities")
    if mean_lower<72*d:
        raise AssertionError("strong universal each-true-source-cherry quenched expectation floor")
    return {
        "s":s,"h":s.bit_length()-1,"V":V,"a":a,"m":m,"d":d,
        "original_true_source_two_flags_cherry_root_quantifier":"EVERY single actual source point (or dual LINE) cherry",
        "physical_root_complement_C4_min":C4_floor,
        "physical_occupied_right_C6_min":C6_floor,
        "per_physical_C4_TRUE_opposite_distinct_original_source_line_choices_min":
            orig_distinct_opposite_min,
        "source_original_six_ID_BA_candidates_min":src,
        "one_global_right_random_connected_C6_target_probability_lower":p_connected,
        "one_global_complete_opposite_map_accepted_original_BA_mean_lower":mean_lower,
        "all_h_each_original_source_cherry_mean_ge_72s_plus72":72*d,
        "exists_a_complete_opposite_global_map_extending_fixed_occupied_support_with_root_BA_ge_72d":True,
        "every_individually_fixed_full_original_f_g_bound_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def genuine_original_root_BA_source_pool(model,side,source_factor,source_flag_ids,
                                        *,vertex_foursets=None):
    """Build genuine original C4 root Q WITHOUT preselected GF5 Q ledger.

    C4 on fixed source-root side; each of remaining 4 TRUE source factors
    chooses actual original flag, preserving TWO anchored source flags
    and requiring SIX DISTINCT genuine OPPOSITE factor IDs.
    Distinct original incidence Q counted once. Fixed opposite typed
    map is used ONLY for an independent literal score / support.
    """
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    if type(side) is not int or side not in (0,1):
        raise ValueError("root fixed original source type 0=POINT or 1=LINE")
    if type(source_factor) is not int or not 0<=source_factor<V:
        raise ValueError("actual fixed root factor ID required")
    source_by=(byP,byL)[side]
    ids=tuple(source_flag_ids)
    if len(ids)!=2 or len(set(ids))!=2 or any(
        type(j) is not int or j not in source_by[source_factor]
        for j in ids
    ):
        raise ValueError("two distinct true source flags at SAME source factor")
    first=(f,g)[side]; opposite=(g,f)[side]
    occupied=set(first)
    anchor=first[source_factor]
    others=tuple(v for v in range(a) if v not in anchor)
    if vertex_foursets is None:
        vertices=tuple(combinations(others,4))
    else:
        vertices=tuple(tuple(sorted(t)) for t in vertex_foursets)
        if len(set(vertices))!=len(vertices) or any(
            len(v)!=4 or len(set(v))!=4 or
            any(type(x) is not int or x not in others for x in v)
            for v in vertices
        ):
            raise ValueError("valid different four physical coordinates, disjoint from root")
    inv={e:p for p,e in enumerate(first)}
    root_opposite={inc[j][1-side] for j in ids}
    if len(root_opposite)!=2:
        raise AssertionError("two ORIGINAL source flags through same true factor require opposite distinct")
    candidates=set()
    physical_C4=0
    accepted_BA=0
    for four in vertices:
        _,_,patterns=_full_four_patterns(four,occupied)
        for kind,edges in patterns:
            if kind!="C4":continue
            physical_C4+=1
            ps=tuple(inv[e] for e in edges)
            if len(set(ps))!=4 or source_factor in ps:
                raise AssertionError("C4 root four genuine distinct other source factors")
            for slot in product(*(source_by[p] for p in ps)):
                Q=tuple(sorted(ids+slot))
                if len(set(Q))!=6:
                    raise AssertionError("actual original six source flag IDs must be distinct")
                src_ids=[inc[j][1-side] for j in Q]
                if len(set(src_ids))!=6:
                    continue
                if Q in candidates:
                    raise AssertionError("same original source 6-Q generated by two C4")
                candidates.add(Q)
                degrees={}
                for j in Q:
                    for col in opposite[inc[j][1-side]]:
                        degrees[col]=degrees.get(col,0)+1
                if len(degrees)==6 and all(q==2 for q in degrees.values()):
                    accepted_BA+=1
    targets=physical_simple_twofactor_6_count(opposite,a)
    probability=Fraction(720*targets["right_simple_twofactor_A_total"],falling(V,6))
    connected_only=Fraction(720*targets["right_connected_C6"],falling(V,6))
    return {
        "s":s,"a":a,"V":V,"side":"POINT_B/LINE_A" if side==0 else "LINE_B/POINT_A",
        "root_actual_original_source_factor":source_factor,
        "root_actual_two_incidence_IDs":tuple(ids),
        "physical_C4_root_residuals":physical_C4,
        "original_six_distinct_incidence_and_opposite_source_factor_Q_count":
            len(candidates),
        "fixed_pair_original_BA_accepted_count":accepted_BA,
        "occupied_opposite_physical_simple_twofactor_counts":targets,
        "one_globally_uniform_opposite_map_exact_BA_probability_for_each_true_original_Q":probability,
        "ONE_global_opposite_map_expected_original_BA_accepted_count":
            len(candidates)*probability,
        "ONE_global_opposite_map_connected_only_expected_BA_lower":
            len(candidates)*connected_only,
        "retains_true_same_six_original_source_incidence_IDs":True,
        "same_given_fully_fixed_opposite_map_is_NOT_guaranteed_positive":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
