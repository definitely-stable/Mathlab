"""HYP-105 / #230 AA4-T: TRUE ORIGINAL positional D6 tensor and quenched bound.

Proved all-h for W(3,s), s=2^h>=2:
    D6(f,g) = sum_H sum_Q A_f[H,Q] A_g[H,Q],
where Q is one true six-incidence source set, source factor IDs on BOTH
types are distinct, and H is the connected C6 dual graph on the SAME
six incidence positions (60 possible labelled C6 graphs).

For EVERY fixed complete globally point-injective f, uniform independent
complete globally line-injective g gives the EXACT expectation
    E_g[D6(f,g)] = (a)_6/(K)_6 * T_f,  T_f=sum_H,Q A_f[H,Q].
The uniform bound E_g[D6] >= s^6/98304 holds for ALL h>=1.
Neither averaging nor the existence of a good g proves min_{f,g} D6>0.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb, prod

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    _column_physical_dual, _is_single_6cycle_on_incidence_positions,
    exact_ONE_side_original_projection_index, exact_two_sided_original_seven_join,
)
from hyp105_issue230_d6aa4r_original_joint_swap_certificate import (
    strict_true_W32_gq_model,
)
from hyp105_issue230_d6aa4s_root_conditional_frechet import minimal_physical_a


def falling(n, k):
    if type(n) is not int or type(k) is not int or k<0 or n<k:
        raise ValueError("nonnegative exact integer falling factorial required")
    return prod(range(n-k+1,n+1))


def all_h_fixed_point_map_quenched_d6_certificate(s):
    """Rigorous all-h bound, exact rational integer arithmetic.

    Physical C6 count in full K_a is (a)_6/12. Every missing physical
    edge kills at most (a-2)_4 physical C6; m=K-V<=a-2.
    Genuine source bipartite d-regularity gives Hall for ANY six distinct
    points, hence at least ONE distinct-original-line assignment; for
    d>=6 greedy count >= (d)_6 source line assignments.

    The right matching of one fixed LEFT original six-position C6 dual
    has probability (a)_6/(K)_6 under ONE uniform complete injection g.
    """
    a=minimal_physical_a(s)
    V=(s+1)*(s*s+1)
    d=s+1
    K=comb(a,2)
    m=K-V
    all_c6=falling(a,6)//12
    destroyed_per_missing=falling(a-2,4)
    occupied_lower=all_c6-m*destroyed_per_missing
    if occupied_lower<=0 or not 0<=m<=a-2:
        raise AssertionError("complete minimal K_a C6 occupancy lower failed")
    source_assign_lower=falling(d,6) if d>=6 else 1
    T_lower=occupied_lower*source_assign_lower
    p=Fraction(falling(a,6),falling(K,6))
    expectation_lower=T_lower*p
    target=Fraction(s**6,98304)
    if expectation_lower<target:
        raise AssertionError("uniform all-h quenched D6 floor failed")
    if s>=8:
        # For powers of two s>=8, minimal a>=35:
        # occupied C6 >= (a)_6/24, (a)_6>= (a/2)^6,
        # (d)_6>=(s/2)^6, p >=1/a^6.
        if not (a>=35 and 12*m*2<=a*(a-1)
                and 2*(a-5)>=a and d-5>=s//2):
            raise AssertionError("uniform symbolic s>=8 proof gate failed")
        mode="analytic_uniform_s_ge_8"
    else:
        mode="exact_small_orders_s_2_and_4_Hall"
    return {
        "s":s, "V":V, "d":d, "a":a, "K":K,
        "missing_physical_edges":m,
        "physical_complete_Ka_distinct_C6":all_c6,
        "physical_missing_edge_destroyed_C6_cap":destroyed_per_missing,
        "physical_occupied_C6_floor":occupied_lower,
        "true_original_distinct_line_assignments_per_C6_floor":source_assign_lower,
        "T_f_all_fixed_point_maps_floor":T_lower,
        "right_g_uniform_connected_matching_probability_num":p.numerator,
        "right_g_uniform_connected_matching_probability_den":p.denominator,
        "every_f_quenched_D6_expectation_lower_num":expectation_lower.numerator,
        "every_f_quenched_D6_expectation_lower_den":expectation_lower.denominator,
        "universal_s6_floor_den":98304,
        "uniform_all_h_proof_mode":mode,
        "all_h_every_f_conditional_EXPECTATION_omega_s6_PROVED":True,
        "all_h_min_over_both_maps_positive_PROVED":False,
    }


def connected_dual_or_none(Q,inc,labels,side):
    """Full source-factor physical coordinate dual, fail closed except non-A."""
    coords={}
    for position,j in enumerate(Q):
        source=inc[j][side]
        for symbol in labels[source]:
            coords.setdefault(symbol,[]).append(position)
    if len(coords)!=6 or any(len(v)!=2 for v in coords.values()):
        return None
    dual=tuple(sorted(tuple(sorted(v)) for v in coords.values()))
    return dual if _is_single_6cycle_on_incidence_positions(dual) else None


def direct_original_W32_point_source_connected_A_tensor(model):
    """Independent of AA4-Q half enumerator: physical 6-edge K6 cycles
    -> six genuine source-point IDs -> six genuine source-incidence IDs,
    keeping all original lines distinct. No historical seven classifier.
    """
    inc,f,g=strict_true_W32_gq_model(model)
    bypoint=[[] for _ in range(15)]
    for j,(p,l) in enumerate(inc):
        bypoint[p].append(j)
    inv={e:p for p,e in enumerate(f)}
    occupied_edges=tuple(combinations(range(6),2))
    eligible={}
    occupied_cycles=0
    for physical_six in combinations(occupied_edges,6):
        degree=Counter(sym for e in physical_six for sym in e)
        if len(degree)!=6 or any(n!=2 for n in degree.values()):
            continue
        # A K6 simple 2factor can be 6cycle or two 3cycles.
        point_sources=tuple(inv[e] for e in physical_six)
        physical_verts={v:set() for v in range(6)}
        for x,y in physical_six:
            physical_verts[x].add(y)
            physical_verts[y].add(x)
        reached={0}; stack=[0]
        while stack:
            for v in physical_verts[stack.pop()]:
                if v not in reached: reached.add(v);stack.append(v)
        if len(reached)!=6:
            continue
        occupied_cycles+=1
        for selected in product(*(bypoint[p] for p in point_sources)):
            if len({inc[j][1] for j in selected})!=6:
                continue
            Q=tuple(sorted(selected))
            H=connected_dual_or_none(Q,inc,f,0)
            if H is None:
                raise AssertionError("physical source C6 failed positional C6")
            if Q in eligible:
                raise AssertionError("same actual source Q duplicated by physical cycles")
            eligible[Q]=H
    if occupied_cycles!=60:
        raise AssertionError("complete true W32 physical K6 must have 60 C6")
    return eligible,occupied_cycles


def W32_point_first_60_position_D6_tensor(model,*,check_independent=True):
    """Exact genuine ORIGINAL W32, 60 H fibres joined on SAME Q.

    Parallel-independent:
      (i) direct physical K6 C6 -> source matching enumerator,
      (ii) AA4-Q source-half full A/B/C index, then 2factor positional dual,
      (iii) historical GF5 seven classifier, and AA4-Q true two-sided join.
    """
    inc,f,g=strict_true_W32_gq_model(model)
    point,Hcount=direct_original_W32_point_source_connected_A_tensor(model)
    if check_independent:
        other=exact_ONE_side_original_projection_index(model,0)["candidate_sixset_map"]
        independent={}
        for Q,kind in other.items():
            if kind!="A" or len({inc[j][1] for j in Q})!=6:
                continue
            H=_column_physical_dual(Q,inc,f,0)
            if _is_single_6cycle_on_incidence_positions(H):
                independent[Q]=H
        if independent!=point:
            raise AssertionError("two independent genuine-original left C6 tensor methods disagree")
    fibres=Counter(point.values())
    matched={}
    for Q,H in point.items():
        if connected_dual_or_none(Q,inc,g,1)==H:
            matched[Q]="D6"
    if check_independent:
        old=seven_census(model,independent_checks=False,witness_sets=True)
        reference={Q:tag for Q,tag in old["sets"].items() if tag=="D6"}
        if reference!=matched:
            raise AssertionError("true original historical full GF5 D6 mismatch")
        q=exact_two_sided_original_seven_join(model,independent_history=False,
                                             collect=True)
        ref2={Q:tag for Q,tag in q["selected_ORIGINAL_Q_tags"].items()
              if tag=="D6"}
        if ref2!=matched:
            raise AssertionError("independent AA4-Q true-original Q D6 join mismatch")
    p=Fraction(falling(6,6),falling(15,6))
    exp=len(point)*p
    c=all_h_fixed_point_map_quenched_d6_certificate(2)
    if len(point)<c["T_f_all_fixed_point_maps_floor"]:
        raise AssertionError("actual original left source tensor below universal capacity")
    return {
        "scope":"TRUE ORIGINAL W32 same six source-incidence IDs and full point/line K6 maps",
        "T_f_connected_60_position_C6_tensor_total":len(point),
        "physical_full_K6_connected_C6_count":Hcount,
        "occupied_positional_H_fibres":len(fibres),
        "H_positional_Q_fibre_min":min(fibres.values()),
        "H_positional_Q_fibre_max":max(fibres.values()),
        "D6_matched_exact_two_sided_original_count":len(matched),
        "uniform_complete_right_global_injection_D6_expectation_num":exp.numerator,
        "uniform_complete_right_global_injection_D6_expectation_den":exp.denominator,
        "right_positional_C6_matching_probability_num":p.numerator,
        "right_positional_C6_matching_probability_den":p.denominator,
        "independent_original_W32_full_seven_oracles":"PASS" if check_independent else "NOT_RUN",
        "all_h_conditional_every_f_positive_EXPECTATION":True,
        "all_h_deterministic_min_over_f_g_PROVED":False,
    }


def report(schemes=("S68","S72","lex","reverse")):
    return {
        "slice":"HYP105-ISSUE230-D6-AA4-T-QUENCHED-ALIGNED-D6",
        "all_h_exact_positional_tensor_inner_product":True,
        "universal_all_h_every_fixed_point_map_expected_D6_floor_s6_divisor":98304,
        "all_h_sample_orders":[all_h_fixed_point_map_quenched_d6_certificate(1<<h)
                               for h in range(1,8)],
        "cases":{name:W32_point_first_60_position_D6_tensor(fixture(1,name))
                 for name in schemes},
        "root_A":"OPEN", "root_B":"OPEN", "full_R3_or_ASET":False,
    }


if __name__=="__main__":
    import argparse,json
    cli=argparse.ArgumentParser()
    cli.add_argument("--scheme",choices=("S68","S72","lex","reverse"))
    args=cli.parse_args()
    result=(W32_point_first_60_position_D6_tensor(fixture(1,args.scheme))
            if args.scheme else report())
    print(json.dumps(result,sort_keys=True,indent=2))
