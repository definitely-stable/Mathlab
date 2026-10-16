"""AA4-BC: adversarially PINNED original line labels, good completion theorem.

Every fixed complete original point f, full right occupied support E,
and EVERY injected partial original LINE->physical-edge assignment of up to
floor(V/1024) original lines admits a complete original line bijection with
>=s^6/512 genuinely original GOOD physically opposite 3-flag wedges
(h>=5). Conditional whole-completion concentration is O(1/V).

This does NOT prove a positive count for the given adversarial FULL g,
nor selected historical seven GF5 six-original-ID motifs.
"""
from fractions import Fraction

from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import (
    _params, physical_edge_port_energy,
)
from hyp105_issue230_d6aa4az_quenched_allD_variance import (
    original_line_triple_weights,
)
from hyp105_issue230_d6aa4bb_overlap_covariance import (
    all_three_source_line_overlap, four_overlap_probability_certificate,
)
from hyp105_issue230_d6aa4az_quenched_good_opposite import (
    support_bad_clean_energy, universal_original_clean_twoport_support_floor,
)


def _falling(n,k):
    if k<0 or n<k:
        raise ValueError("not enough complete-global free source factors")
    out=1
    for i in range(k):
        out*=n-i
    return out


def certified_robust_pins_envelope(s,k):
    """Pure exact all-h rational worst-case; not an imagined large W3 census."""
    prior=universal_original_clean_twoport_support_floor(s)
    if not prior["uniform_clean_T_ge_V_squared_over_16_proved"]:
        raise ValueError("genuine dyadic h>=5 clean port support floor required")
    V,a,_,_= _params(s)
    if type(k) is not int or not 0<=k<=V//1024:
        raise ValueError("arbitrary locked original LINE assignments: k<=floor(V/1024)")
    d,t=s+1,a-2
    n=V-k
    T0=Fraction(V*V,16)
    B0=d*(d-1)*(d-2)*T0
    M1=5*d**3*t*t
    M2=8*d**3*t
    M3=6*d**3
    B_min=B0-k*M1
    favorable_min=2*T0-6*k*t*t
    if B_min < B0/2 or favorable_min < V*V/16:
        raise AssertionError("uniform arbitrary pinned line/edge deletion bound")
    p0=Fraction(favorable_min,_falling(n,3))
    mean_min=B_min*p0
    if mean_min < Fraction(s**6,512):
        raise AssertionError("all-injections constrained completion lower lost")
    q=Fraction(_falling(n-3,3),_falling(n,3))
    P1=Fraction(4*t**4,_falling(n-1,4))
    P2=Fraction(16*n*t**3,_falling(n,4))
    eta=1/q-1+Fraction(3*M1,B_min)*P1/(p0*p0) + (
        Fraction(3*M2,B_min)*P2/(p0*p0)) + Fraction(M3,B_min)/p0
    if eta*V>30000000000:
        raise AssertionError("symbolic uniform 30-billion/V variance bound fails")
    return {
        "s":s,"h":s.bit_length()-1,"V":V,"a":a,
        "arbitrary_pinned_source_LINE_factor_limit":V//1024,
        "actually_pinned":k,"free_original_LINE_factors":n,
        "original_clean_source_weight_floor_after_pins":B_min,
        "physical_GOOD_ordered_right_triples_floor_after_pins":favorable_min,
        "conditional_mean_of_unpinned_GOOD_wedges_lower":mean_min,
        "conditional_relative_variance_upper":eta,
        "eta_le_30000000000_over_V":True,
        "probability_unpinned_GOOD_below_s6_over1024_upper":
            min(Fraction(1),4*eta),
        "existence_of_some_completion_with_GOOD_ge_s6_over512":True,
        "ALL_fully_fixed_g_or_six_ID_GF5_PROVED":False,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER"
    }


def actual_original_pinned_completion_certificate(model,pins):
    """Exact true W32/W34 weighted original 3flag conditional probability.

    pins maps ACTUAL original LINE factor IDs to distinct occupied physical
    edges. Preserve the BAD coordinate set of the FULL occupied E, rather
    than erroneously reclassifying the FREE graph as a new minimal support.
    """
    V,a,_,_=_params(model["s"])
    E=tuple(tuple(sorted(e)) for e in model["right_labels"])
    if len(E)!=V or len(set(E))!=V:
        raise ValueError("not a complete original typed LINE injection")
    if not isinstance(pins,dict) or any(type(i) is not int or i<0 or i>=V
                                     for i in pins):
        raise ValueError("pin original distinct LINE IDs")
    pinned_edges=[]
    for e in pins.values():
        pair=tuple(sorted(e))
        if len(pair)!=2 or pair not in E:
            raise ValueError("pinned edge not a member of complete right support")
        pinned_edges.append(pair)
    if len(set(pinned_edges))!=len(pinned_edges):
        raise ValueError("pinned edges must be globally distinct")
    k=len(pins)
    if V-k<6:
        raise ValueError("at least six free source LINE factors required")
    point_w=original_line_triple_weights(model,clean_only=True)
    free_w={key:value for key,value in point_w.items()
            if not any(x in pins for x in key)}
    B,M1,M2,M3=all_three_source_line_overlap(free_w,V)
    free_E=tuple(e for e in E if e not in set(pinned_edges))
    original_clean=set(support_bad_clean_energy(E,a)[
        "clean_induced_occupied_edges"])
    free_clean=tuple(e for e in free_E if e in original_clean)
    favorable=2*physical_edge_port_energy(free_clean,a)
    n=V-k
    p=Fraction(favorable,_falling(n,3))
    q=Fraction(_falling(n-3,3),_falling(n,3))
    t=a-2
    P1=Fraction(4*t**4,_falling(n-1,4))
    P2=Fraction(16*n*t**3,_falling(n,4))
    eta=1/q-1+Fraction(3*M1,B)*P1/(p*p)+Fraction(3*M2,B)*P2/(p*p)+Fraction(M3,B)/p
    if model["s"]>=32 and k<=V//1024:
        x=certified_robust_pins_envelope(model["s"],k)
        if B<x["original_clean_source_weight_floor_after_pins"] or (
            favorable<x["physical_GOOD_ordered_right_triples_floor_after_pins"]
        ) or eta>x["conditional_relative_variance_upper"]:
            raise AssertionError("original source pinned conditional uniform bound wrong")
    return {
        "s":model["s"],"V":V,"a":a,"pinned":k,"free":n,
        "original_clean_source_3flag_weight_avoiding_pins":B,
        "physical_good_ordered_right_free_edge_triples":favorable,
        "mean_unpinned_source_good_wedges":B*p,
        "relative_variance_unpinned_upper":eta,
        "bad_coordinates_depend_on_FULL_right_support_not_free_support":True,
        "NOT_entire_original_good_event_if_pins_are_used":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER"
    }
