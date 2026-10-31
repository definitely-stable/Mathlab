"""HYP-105 AA4-UDEL: unconditional six-ORIGINAL-ID deletion-robust Branch A.

This supplies an explicit SAME-fixed-f,g two-case proof certificate,
conditional only on the already proved #659 balanced C6 SS6 input and
#672/#673 original-source exact combinatorics. No finite test proves
the asymptotic claim. The pure integer/rational arithmetic below audits
the all-h universal constants and threshold without sampling models.

For *every* allowed legal correlated complete original W(3,2^h)
pair-label map and EVERY adversarial original-flag set Z with
|Z|<=rho*s^4, even with NO small-D6 assumption:
     D6_avoid(Z) + U_BB_overlap_avoid(Z) >= delta*s^6.
The tail side retains original non-Z paired flags before applying
the #659 coherent selector; the low-tail side selects *only* core
non-Z flags, so its sixth moment is charged to D6_avoid, then #673
bounds the full original three-flag anchor exposure to Z.

The stronger asymptotic stability if D6_avoid=o(s^6) and Z=o(s^4)
follows, even when the unpruned D6 is NOT known to be small.
"""
from fractions import Fraction
from math import isqrt

from hyp105_bbo_resilience import avoidance_certificate, checked_ids
from hyp105_full_physical_degree_tail import (
    genuine_source, physical,
)
from hyp105_physical_degree_energy import (
    minimal_alphabet, _verify_typed_injections,
)
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
from hyp105_physical_rainbow_c6 import build_original_physical_graph


def exact_unconditional_constants(C_graph=1, c_graph=Fraction(1)):
    """Exact algebraic sufficient constants for the new two-case theorem.

    Positive C_graph and c_graph are the EXISTING mathematical SS6
    constants (not determined numerically by these tests). The defaults
    are ONLY formal unit placeholders to audit inequalities. Do NOT
    claim the external supersaturation theorem has C=c=1.
    Increasing C_graph to >=1 and decreasing c_graph to <=1
    preserves the external SS6 property, if it held beforehand.

    Use epsilon=1/8; if E_T(full)>=epsilon*s^4, remove <=rho*s^4
    original IDs. At most two heavy edges per deleted ID are lost.
    Since rho<=1/32, at least (epsilon/2)*s^4 original heavy
    physical witness edges survive in ORIGINAL paired H\\Z. Their
    distinct source flags have |I|>=(epsilon/4)*s^4, so #659 applies
    with epsilon_eff=1/16 to this still-dense ORIGINAL subset.
    Therefore D6_avoid(Z)>=c_graph*2^-120*s^6.

    Otherwise the full heavy edge tail is <s^4/8: remove heavy
    flags, conflict degree>K=64 and Z. At least 3/4*s^4
    original IDs remain, 2*N0>=s^4, max physical degree T*s,
    max ORIGINAL conflict degree K. On this Z-free core #672's
    path selector is charged to D6_avoid(Z), NOT unpruned D6.
    If D6_avoid<delta*s^6<=s^6, the same path moments apply.
    #673's 12*s^2*|Z| physical endpoint mask removes <=s^6/8
    proper paths at rho<=1/(768*M3^2), so BBo_avoid>=s^6/16.

    All large s thresholds are explicit enormous upper integers,
    never experimentally evaluated all-h sample sizes.
    """
    if (type(C_graph) is not int or C_graph<1 or
            not isinstance(c_graph,(int,Fraction)) or
            c_graph<=0 or c_graph>1):
        raise ValueError("normalized external SS6 constants must have C>=1, 0<c<=1")
    c=Fraction(c_graph)
    eps=Fraction(1,8)
    K=64
    # 2^41*C^3*(epsilon_eff)^(-6), epsilon_eff=epsilon/2=1/16.
    T=(1<<65)*C_graph**3
    sigma2_inverse=64*(K+1)**2
    sigma3_inverse=64*27*(K+1)**3
    L6=24+576*T*T
    M3_squared=sigma3_inverse**2*L6
    rho=min(Fraction(1,32),Fraction(1,768*M3_squared))
    delta=min(Fraction(1,16),c/Fraction(1<<120))

    # Enlarged exact INTEGER envelopes dominate the constants in
    # the #672 path inequality (21). T>=1:
    # sqrt(L6)<=25*T, sqrt(8L6)<=70*T,
    # B0=64 sqrt(65T)<=576*T.
    LE_upper=200*sigma3_inverse*T
    L4_coefficient=140*sigma2_inverse**2+56
    sq=isqrt(L4_coefficient)
    ceil_sqrt_L4_coefficient=sq+(sq*sq<L4_coefficient)
    Lblock_upper=24*ceil_sqrt_L4_coefficient*T*T
    # each #672 U_BBo error <=s^6/24
    s0=max(
        64,1008*T,(12*LE_upper)**2,(48*Lblock_upper)**8
    )
    assert eps-2*rho>=eps/2
    assert eps+Fraction(3,32)+rho<=Fraction(1,4)
    assert rho*768*M3_squared<=1
    assert T >= (1<<41)*C_graph**3*16**6
    assert 24+576*T*T<=600*T*T
    assert 8*L6<=4900*T*T
    assert delta<=Fraction(1,16)
    return {
        "external_balanced_SS6_constants_are_inputs_not_proved":True,
        "C_graph_formal_normalized":C_graph,
        "c_graph_formal_normalized":str(c),
        "heavy_full_graph_tail_epsilon":eps,
        "heavy_witness_remaining_effective_epsilon":Fraction(1,16),
        "heavy_degree_cap_T":T,
        "source_conflict_degree_cap_K":K,
        "selected_sigma2_inverse":sigma2_inverse,
        "selected_sigma3_inverse":sigma3_inverse,
        "selected_graph_sixth_walk_envelope_L6":L6,
        "endpoint_proper_third_path_Frobenius_bound_squared_M3":M3_squared,
        "allowed_original_flag_deletion_density_rho":rho,
        "accepted_sixset_all_map_floor_delta":delta,
        "sufficient_s0_integer":s0,
        "sufficient_s0_bit_length":s0.bit_length(),
        "high_tail_pruned_D6_floor":c/Fraction(1<<120),
        "low_tail_pruned_BBo_floor":Fraction(1,16),
        "low_tail_Z_free_original_core_density_floor":Fraction(3,4),
        "unconditional_original_sixset_packing_lower_multiple":
            rho/Fraction(6),
        "new_stability_if_D6_avoiding_Z_is_o_s6":
            "liminf BBo_avoid(Z)/s^6>=8 when |Z|=o(s^4)",
        "claim_root_branch_A_parent_already_proved_in_Draft":True,
        "external_mathematical_referee_not_supplied":True,
        "full_ASET_exponent_proved":False,
    }


def finite_original_D6_avoiding_flags(power,f,g,forbidden=()):
    """Finite TRUE original source-provenance D6 sixset DFS after deletion.

    Every physical C6 is enumerated exactly once and decoded into six
    distinct ORIGINAL incidence IDs. The historical original GF5 D6
    classifier independently referees each counted source sixset.
    This verifies the *operation* D6_avoid(Z) = D6(H\\Z), not any
    large-h tail lower bound or external graph theorem.
    """
    if type(power) is not int or power not in (1,2):
        raise ValueError("original-source finite D6 oracle supports h=1,2")
    s,V,flags=genuine_source(power)
    a=minimal_alphabet(V)
    f=tuple(map(tuple,f));g=tuple(map(tuple,g))
    _verify_typed_injections(a,V,f,g)
    Z=checked_ids(forbidden,len(flags))
    retained=[i for i in range(len(flags)) if i not in Z]
    graph,provenance=physical(retained,flags,f,g)
    original_sixsets=set()
    def visit(path):
        if len(path)==6:
            if path[0] not in graph[path[-1]] or path[1]>=path[-1]:
                return
            if (len({v[0] for v in path})!=6 or
                    len({v[1] for v in path})!=6):
                return
            ids=tuple(sorted(
                provenance[tuple(sorted((path[j],path[(j+1)%6])))]
                for j in range(6)))
            if len(set(ids))!=6 or Z.intersection(ids):
                raise AssertionError("not six distinct retained ORIGINAL source flags")
            if classify_seven_prechecked(ids,f,g,flags)!="D6":
                raise AssertionError("physical cycle not genuine historical GF5 D6")
            if ids in original_sixsets:
                raise AssertionError("physical C6 to ORIGINAL sixset not injective")
            original_sixsets.add(ids)
            return
        for w in graph[path[-1]]:
            if w>path[0] and w not in path:
                visit(path+(w,))
    for root in graph:visit((root,))
    return {
        "s":s,"V":V,"original_flags":len(flags),
        "forbidden_original_flag_ids":tuple(sorted(Z)),
        "retained_original_flag_count":len(retained),
        "accepted_original_D6_avoiding_Z":len(original_sixsets),
        "accepted_original_D6_sixsets":tuple(sorted(original_sixsets)),
        "finite_oracle_not_all_h_proof":True,
    }


def finite_true_original_sixset_deletion_certificate(power,f,g,forbidden=(),core_ids=None):
    """Check both accepted original source families separately after Z.

    The source all-h theorem is mathematical; finite W32/W34 may lie
    vastly below its explicit (astronomical) sufficient threshold.
    """
    D=finite_original_D6_avoiding_flags(power,f,g,forbidden)
    B=avoidance_certificate(power,f,g,forbidden,core_ids)
    if any(set(ids).intersection(forbidden) for ids in
           D["accepted_original_D6_sixsets"]):
        raise AssertionError("original D6 sixset contains deleted ID")
    A=set(D["accepted_original_D6_sixsets"])
    Bids=set(map(tuple,B["produced_sixsets"]))
    if A&Bids:
        raise AssertionError("D6 and B/B-overlap ORIGINAL classes intersect")
    return {
        "s":D["s"],
        "forbidden_original_flag_count":len(D["forbidden_original_flag_ids"]),
        "retained_original_flag_count":D["retained_original_flag_count"],
        "D6_avoid":len(A),
        "BBo_avoid_produced_source_subcount":len(Bids),
        "two_disjoint_historical_GF5_class_sixset_lower":len(A)+len(Bids),
        "full_7_class_S_avoid_computed":False,
        "BBo_subcount_comes_from_source_verified_directed_paths":True,
        "strict_six_original_IDs_all_avoiding_Z":True,
        "finite_case_does_not_claim_s_greater_than_s0":True,
    }
