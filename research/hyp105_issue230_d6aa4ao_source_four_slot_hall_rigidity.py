"""HYP-105 #230 AA4-AO: GENUINE original source 4-slot Hall rigidity.

NEW all-h: four true original point incidence factor slots and four
line factor slots, each either A=1+1+1+1 or B=2+1+1, specify exactly
four DISTINCT source incidence flags matching slot multiplicities.
If either slot type is B, AT MOST ONE genuine original 4-edge subset
can realize both multisets; if both A, at most TWO, with equality
only when the eight distinct actual GQ source factors induce C8.

Reason: two DISTINCT 4-edge source matchings on the SAME vertex degree
profiles have red/blue balanced symmetric difference, and hence an
alternating source cycle. Original W(3,s) incidence girth EIGHT rules
out cycles on <8 edges; so all 4 edges of each matching must differ,
their union is a C8 on FOUR DISTINCT original points/lines. This is
impossible whenever a source factor appears twice in either profile.
The A/A <=2 and genuine C8 classification PREEXIST in AA4-AE #512.
The NEW result is the strict <=1 rigidity when one residual physical
port half-template contains the twice-used ORIGINAL source factor,
and its GLOBAL port-template weighted consequence.

For ANY globally complete separately injected point/line f,g and a
genuine D anchor, the occupied physical port fourfactor templates have
point A_P/B_P and line A_L/B_L counts (from sibling #533). The actual
TRUE original bilateral two-regular D-anchored source extension charge
H(D) is universally <= 2*A_P*A_L + A_P*B_L + B_P*A_L + B_P*B_L.
For FULL K_a the limit is exactly the analytic upper 149*C(a-3,3)^2
(compared to older crude 2400*C(a-3,3)^2=24*100*t^2).

Every SOURCE-Hall count is EXACTLY the number of valid ordered slot
permutations (no repeated incidence flags) divided by the stabilizer
product of 4-slot repeated-factor multiplicity factorials: 1,2 or4.
No synthetic GQ, per-Q physical relabeling, or independence assumed.
This is an upper, NOT a positive all-map seven GF5 lower.
"""
from collections import Counter
from itertools import combinations,permutations
from math import comb,factorial

from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _actual_strict_original_transport,
)
from hyp105_issue230_d6aa4an_port_completion_hall_funnel import (
    true_original_D_physical_ports,_strict_occupied_half_patterns,
    _original_four_flag_completions,
)


def _profile(slots):
    slots=tuple(slots)
    if len(slots)!=4 or any(type(i) is not int or i<0 for i in slots):
        raise ValueError("four actual nonnegative original source factor IDs")
    mult=Counter(slots)
    vals=tuple(sorted(mult.values()))
    if vals==(1,1,1,1):return "A",1
    if vals==(1,1,2):return "B",2
    raise ValueError("source factor slot profile must be A or B")


def _girth8_local_source_matrix(point_sources,line_sources,incidence_index):
    """Fail CLOSED when a 4- or 6-cycle occurs among actual factors.

    Does not replace authentic W(3,s) source validation. This local
    necessary condition makes synthetic invalid 4x4 tests adversarial.
    """
    pp=tuple(sorted(set(point_sources)))
    ll=tuple(sorted(set(line_sources)))
    N={p:{l for l in ll if (p,l) in incidence_index} for p in pp}
    for p,q in combinations(pp,2):
        if len(N[p]&N[q])>=2:
            raise ValueError("original incidence C4: not genuine GQ")
    for p,q,t in combinations(pp,3):
        # Three different pairwise source common lines would form C6.
        shared=[N[p]&N[q],N[q]&N[t],N[t]&N[p]]
        if all(shared):
            l0=next(iter(shared[0]))
            l1=next(iter(shared[1]))
            l2=next(iter(shared[2]))
            if len({l0,l1,l2})==3:
                raise ValueError("original incidence C6: not genuine GQ")
    return N


def _four_slot_certificate(point_slots,line_slots,incidence_index,
                           *,pinned=(),independent_direct=False):
    """Hot internal original factor FOUR-slot local Hall verifier.

    source incidence_index maps REAL unique original (point,line) IDs
    to actual flag IDs. Distinct source physical factor slots may repeat,
    but repeated original (p,l) incidence flag IDs are FORBIDDEN.
    """
    p_kind,p_den=_profile(point_slots)
    l_kind,l_den=_profile(line_slots)
    pins=set(pinned)
    if any(i in pins for i in incidence_index.values() if
           False): # explicit no per-call heavy source traversal
        raise AssertionError("unreachable pinned verification")
    _girth8_local_source_matrix(point_slots,line_slots,incidence_index)
    denominator=p_den*l_den
    slot_permutations=0
    distinct=set()
    P=tuple(point_slots);L=tuple(line_slots)
    for sigma in permutations(range(4)):
        src=tuple((P[i],L[sigma[i]]) for i in range(4))
        ids=tuple(incidence_index.get(e) for e in src)
        if (None in ids or len(set(ids))!=4 or
                any(k in pins for k in ids)):
            continue
        slot_permutations+=1
        distinct.add(tuple(sorted(ids)))
    if slot_permutations%denominator:
        raise AssertionError("source slot permutation orbit quotient nonintegral")
    exact=slot_permutations//denominator
    if exact!=len(distinct):
        raise AssertionError("genuine source 4-incidence orbit quotient disagrees")
    cap=2 if p_kind==l_kind=="A" else 1
    if exact>cap:raise AssertionError("genuine GQ incidence girth8 Hall rigidity")
    if independent_direct:
        independent=set()
        edge_ids=tuple((p,l,i) for (p,l),i in incidence_index.items()
                       if p in P and l in L and i not in pins)
        for chosen in combinations(edge_ids,4):
            rows=Counter(p for p,l,i in chosen)
            cols=Counter(l for p,l,i in chosen)
            if rows==Counter(P) and cols==Counter(L):
                independent.add(tuple(sorted(i for p,l,i in chosen)))
        if independent!=distinct:
            raise AssertionError("source-first direct 4-edge subset oracle disagrees")
    return {
        "point_four_slot_kind":p_kind,"line_four_slot_kind":l_kind,
        "slot_permutation_orbit_denominator":denominator,
        "valid_source_permutations_with_DISTINCT_actual_incidence_IDs":
            slot_permutations,
        "exact_DISTINCT_true_original_four_incidence_Q_completions":exact,
        "new_GQ_repeated_source_factor_matching_rigidity_upper":cap,
        "actual_source_four_incidence_ID_sets":tuple(sorted(distinct)),
        "independent_source_EDGE_FIRST_check":"PASS" if independent_direct
            else "NOT_RUN",
        "old_AA_original_four_by_four_permanent_at_most_two_not_new":True,
        "positive_full_seven_GF5_lower_NOT_PROVED":True,
    }


def exact_true_original_four_slot_Hall_certificate(model,point_slots,
                                                     line_slots,*,pinned=(),
                                                     independent_direct=True):
    """Externally strict true W3s original source model validator."""
    s,V,d,a,P,L,inc,np,nl=_actual_strict_original_transport(model)
    if any(x>=V for x in (*point_slots,*line_slots)):
        raise ValueError("source original point/line factor out of bounds")
    idx={tuple(e):i for i,e in enumerate(inc)}
    result=_four_slot_certificate(point_slots,line_slots,idx,
                    pinned=pinned,independent_direct=independent_direct)
    return {"s":s,**result}


def exact_true_original_D_anchor_slot_upper(model,pair,
                                              *,independent_all_templates=False):
    """All original physical D port template pairs, exact source-four-ID
    Hall charge without ever using PRE-ACCEPTED seven sixsets.

    Unlike the parent #533, the per-template Hall rigidity assertion
    is checked BEFORE any selected-seven physical alignment filter.
    """
    s,V,d,a,left,right,inc,np,nl=_actual_strict_original_transport(model)
    idx={tuple(e):i for i,e in enumerate(inc)}
    ports=true_original_D_physical_ports(inc,left,right,pair)
    both=[]
    A=[];B=[]
    for side in (0,1):
        labels=(left,right)[side]
        inv={tuple(e):i for i,e in enumerate(labels)}
        entries,formal,occupied=_strict_occupied_half_patterns(
            ports[side],a,inv)
        partition={"A":[],"B":[]}
        for pat in entries:
            kind,_=_profile(pat[1])
            partition[kind].append(pat)
        A.append(partition["A"]);B.append(partition["B"])
        both.append(entries)
    formula=2*len(A[0])*len(A[1])+len(A[0])*len(B[1])+(
        len(B[0])*len(A[1]))+len(B[0])*len(B[1])
    true_H=0
    true_twice=0
    kind_hist=Counter()
    direct_checked=0
    for left_p in both[0]:
        for right_p in both[1]:
            check=_four_slot_certificate(left_p[1],right_p[1],idx,
                pinned=pair,independent_direct=independent_all_templates)
            got=check["exact_DISTINCT_true_original_four_incidence_Q_completions"]
            true_H+=got
            true_twice+=int(got==2)
            kind_hist[check["point_four_slot_kind"]+"/"+
                      check["line_four_slot_kind"]]+=got
            direct_checked+=int(independent_all_templates)
            if independent_all_templates:
                # Independent parent has entirely separate source
                # physical template Q generation; compare SETS.
                from_parent=_original_four_flag_completions(
                    idx,pair,left_p,right_p)
                expected={tuple(sorted(tuple(pair)+tuple(ids))) for ids in
                          check["actual_source_four_incidence_ID_sets"]}
                if from_parent!=expected:
                    raise AssertionError("parent physical-template original Q major disagrees")
    if true_H>formula:
        raise AssertionError("source-Hall exceeds girth8 four-slot cap")
    return {
        "s":s,"anchor_original_two_incidence_IDs":tuple(pair),
        "point_A_occupied_port_templates":len(A[0]),
        "point_B_occupied_port_templates":len(B[0]),
        "line_A_occupied_port_templates":len(A[1]),
        "line_B_occupied_port_templates":len(B[1]),
        "number_occupied_true_original_both_typed_port_template_pairs":
            len(both[0])*len(both[1]),
        "NEW_universal_true_original_port_template_Hall_charge_upper":
            formula,
        "exact_true_original_Hall_source_six_ID_Q_extensions":true_H,
        "original_source_C8_double_match_template_count":true_twice,
        "source_four_slot_class_Hall_charge":dict(kind_hist),
        "independent_PARENT_physical_port_six_Q_oracle_check":
            "PASS" if independent_all_templates else "NOT_RUN",
        "independently_checked_template_pairs":direct_checked,
        "original_positive_selected_GF5_lower_not_proved":True,
    }


def all_h_complete_palette_port_four_slot_Hall_upper(s):
    from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
        _parameters,
    )
    V,d,a=_parameters(s)
    t=comb(a-3,3)
    if t<1:raise AssertionError("physical a>=6 required")
    return {
        "s":s,"V":V,"d":d,"a":a,"new_triples_t":t,
        "full_Ka_per_side_A_port_template_count":7*t,
        "full_Ka_per_side_B_port_template_count":3*t,
        "new_ALL_typed_full_Ka_source_Hall_template_charge_upper":
            149*t*t,
        "old_naive_parent_twentyfour_source_per_template_upper":
            2400*t*t,
        "old_genuine_original_AA_four_rook_at_most_two_from_pr512":True,
        "new_repeated_factor_source_Hall_unique_or_zero":True,
        "universally_positive_all_D_anchor_selected_seven_NOT_PROVED":True,
        "issue230_A_B_C_open":True,
    }
