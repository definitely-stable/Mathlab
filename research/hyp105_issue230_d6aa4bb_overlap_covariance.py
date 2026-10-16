"""HYP-105 #230 AA4-BB: separate 0/1/2/3 ORIGINAL line overlaps.

Variance of real ORIGINAL physically opposite GOOD threeflag wedges, under
ONE uniform complete original LINE bijection g onto a FIXED physical
support. Fixed original point map f remains arbitrary and globally
injected. This is NOT a fixed-(f,g) GF(5) minimax theorem.
"""
from collections import Counter
from fractions import Fraction
from math import comb

from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import (
    _params, physical_edge_port_energy
)
from hyp105_issue230_d6aa4az_quenched_allD_variance import (
    original_line_triple_weights, source_influences
)
from hyp105_issue230_d6aa4az_quenched_good_opposite import (
    support_bad_clean_energy, universal_original_clean_twoport_support_floor
)


def all_three_source_line_overlap(weights, V):
    """Maximum source weight with one fixed UNORDERED 3-element LINE set."""
    B, M1, M2 = source_influences(weights, V)
    c = Counter()
    for triple, mass in weights.items():
        c[tuple(sorted(triple))] += mass
    if not c:
        raise ValueError("nonempty genuine original weighted triple family needed")
    M3 = max(c.values())
    if M3 > M2 or M2 > M1 or M1 > B:
        raise AssertionError("source overlap hierarchy impossible")
    return B, M1, M2, M3


def four_overlap_probability_certificate(V, a, physical_port_energy):
    """Purely physical image joint bounds for 0/1/2/3 shared SOURCE LINE IDs.

    The outer two physical pair images meet distinct center endpoints.
    Bounds are valid for any subset of unordered K_a edges of size V,
    including AA4-AO clean-induced support filtering, since filtering
    can only DELETE allowable triples or physical image completions.
    """
    if type(V) is not int or type(a) is not int or V < 6 or a < 4 or V > comb(a, 2):
        raise ValueError("valid full distinct physical right edge support required")
    if type(physical_port_energy) is not int or physical_port_energy <= 0:
        raise ValueError("positive rooted physical port energy required")
    t = a-2
    p = Fraction(2*physical_port_energy, V*(V-1)*(V-2))
    if p > 1:
        raise ValueError("port energy cannot describe physical ordered 3-edge probability")
    q = Fraction((V-3)*(V-4)*(V-5), V*(V-1)*(V-2))
    one = Fraction(4*t**4, (V-1)*(V-2)*(V-3)*(V-4))
    two = Fraction(16*V*t**3, V*(V-1)*(V-2)*(V-3))
    return {"p":p,"q":q,"zero_joint_upper":p*p/q,
            "one_joint_upper":one,"two_joint_upper":two,
            "three_joint_upper":p}


def exact_weighted_global_permutation_second_moment_bound(weights, right_edges, a, clean=False):
    """All 3-source-LINE overlap cases, exact Fraction, no independence fiction."""
    E = tuple(tuple(sorted(e)) for e in right_edges)
    V = len(E)
    if len(set(E)) != V:
        raise ValueError("right image must be a globally injected support")
    if clean:
        port = support_bad_clean_energy(E, a)[
            "CLEAN_physical_two_opposite_port_root_energy"]
    else:
        port = physical_edge_port_energy(E, a)
    x = four_overlap_probability_certificate(V, a, port)
    B, M1, M2, M3 = all_three_source_line_overlap(weights,V)
    p, q = x["p"], x["q"]
    eta = (1/q-1 +
           Fraction(3*M1, B)*x["one_joint_upper"]/(p*p) +
           Fraction(3*M2, B)*x["two_joint_upper"]/(p*p) +
           Fraction(M3, B)/p)
    return {"V":V,"B":B,"M1":M1,"M2":M2,"M3":M3,
            "p":p,"mean":B*p,"relative_variance_upper":eta,
            "probability_below_half_mean_upper":min(Fraction(1),4*eta),
            "physical_zero_joint_upper":x["zero_joint_upper"],
            "physical_one_joint_upper":x["one_joint_upper"],
            "physical_two_joint_upper":x["two_joint_upper"],
            "physical_three_joint_upper":x["three_joint_upper"],
            "fully_correlated_global_right_map":True,
            "root_230":"OPEN_WITH_FORMAL_BLOCKER"}


def true_original_GOOD_source_second_moment(model):
    """Actual W32/W34 original source flags, exact GOOD clean physical support."""
    V, a, _, _ = _params(model["s"])
    E = tuple(tuple(sorted(e)) for e in model["right_labels"])
    if len(E)!=V:
        raise ValueError("complete original LINE factor right image needed")
    w=original_line_triple_weights(model,clean_only=True)
    z=exact_weighted_global_permutation_second_moment_bound(w,E,a,clean=True)
    d,t=model["s"]+1,a-2
    if z["M1"]>5*d**3*t*t or z["M2"]>8*d**3*t or z["M3"]>6*d**3:
        raise AssertionError("true original source incidence influence cap violated")
    if model["s"]>=32:
        if z["relative_variance_upper"]>uniform_GOOD_variance_envelope(model["s"])[
            "relative_variance_upper"]:
            raise AssertionError("original GOOD uniform bound violated")
    return z


def uniform_GOOD_variance_envelope(s):
    """ALL h>=5 exact arithmetic certificate: Var/mean²=O(s^-3).

    Relies on original true-source degree d and #561 CLEAN port energy
    >=V²/16 for BOTH full globally injected typed physical supports.
    """
    prior=universal_original_clean_twoport_support_floor(s)
    if not prior["uniform_clean_T_ge_V_squared_over_16_proved"]:
        raise ValueError("original clean all-support theorem only for dyadic h>=5")
    V,a,_,_ = _params(s)
    d,t=s+1,a-2
    T0=Fraction(V*V,16)
    B0=d*(d-1)*(d-2)*T0
    p0=Fraction(2*T0,V*(V-1)*(V-2))
    M1=5*d**3*t*t
    M2=8*d**3*t
    M3=6*d**3
    q=Fraction((V-3)*(V-4)*(V-5),V*(V-1)*(V-2))
    P1=Fraction(4*t**4,(V-1)*(V-2)*(V-3)*(V-4))
    P2=Fraction(16*V*t**3,V*(V-1)*(V-2)*(V-3))
    eta=(1/q-1+Fraction(3*M1,B0)*P1/(p0*p0)+
         Fraction(3*M2,B0)*P2/(p0*p0)+Fraction(M3,B0)/p0)
    mean0=B0*p0
    if mean0<Fraction(s**6,128):
        raise AssertionError("parent uniform GOOD mean lower regressed")
    # Analytic ALL-h constant proof in the companion Markdown:
    # V>=30; t²<2V; B0>=d³V²/32; q^-1-1<=30/V;
    # P1<=256/V², P2<=2048/V^(3/2), p0>=1/(8V).
    # Each term bounded via these inequalities by < 220000000/V.
    if eta*V>220000000:
        raise AssertionError("universal rational V^-1 certified constant regressed")
    return {"s":s,"h":s.bit_length()-1,"V":V,"a":a,"d":d,
            "mean_lower":mean0,"M1_upper":M1,"M2_upper":M2,"M3_upper":M3,
            "source_unique_line_three_overlap_capped":True,
            "relative_variance_upper":eta,
            "explicit_all_h_eta_le_220million_over_V":True,
            "probability_R_GOOD_below_s6_over256_upper":min(Fraction(1),4*eta),
            "all_given_adversarial_g_lower_NOT_PROVED":True,
            "selected_seven_original_sixflag_GF5_NOT_PROVED":True,
            "root_230":"OPEN_WITH_FORMAL_BLOCKER"}
