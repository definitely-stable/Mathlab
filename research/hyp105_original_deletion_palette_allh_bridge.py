"""Independent all-h CONDITIONAL interface #674 -> #726 palette Hamming theorem.

Re-derive all explicit formal normalized constants from the algebra,
WITHOUT importing #674's implementation. No numerical value is
claimed for the published external Simonovits/Jiang–Yepremyan SS6
C_graph,c_graph constants. C=1,c=1 inputs are only FORMAL falsifiers,
NOT validated analytic graph supersaturation constants.

When the #674 original all-h deletion theorem and exact original
signed-flow topology are independently accepted, its claimed
rho(C_graph)>0 and s0(C_graph) imply t>rho*s^4/6 ORIGINAL
six-source-ID-disjoint accepted D6/BBo motifs, so #726's rigorously
established ten-sign-exclusive random 51-palette event q=53526/51^6
implies exp(-q*rho*s^4/6) clean scarcity and the sharper exact
binomial stochastic dominance for any found finite packing.

This module audits numerical constants / logical implication, not the
all-h geometry of heavy tails, FULL/CORE mixed blocking or sixset
reconstruction. It CANNOT accept root #230 Branch A.
"""
from fractions import Fraction
from math import isqrt

Q_TEN=Fraction(53526,51**6)


def _ceil_sqrt_exact(n):
    if type(n) is not int or n<0:raise ValueError("integer sqrt only")
    t=isqrt(n)
    return t if t*t==n else t+1


def independent_UDEL_packing_and_exact_GF5_probability_bridge(
        C_graph,c_graph,*,assume_unreviewed_parent_674=False):
    if (type(C_graph) is not int or C_graph<1 or
        not isinstance(c_graph,(Fraction,int)) or
        c_graph<=0 or c_graph>1):
        raise ValueError("formal normalized C>=1, 0<c<=1 required")
    if assume_unreviewed_parent_674 is not True:
        raise ValueError("must not silently promote unaccepted #674 geometry")
    c=Fraction(c_graph)
    k=64; eps=Fraction(1,8)
    T=2**65*C_graph**3
    sig2=64*(k+1)**2
    sig3=64*27*(k+1)**3
    sixth=24+576*T*T
    M3_squared=sig3**2*sixth
    rho=min(Fraction(1,32),Fraction(1,768*M3_squared))
    delta=min(Fraction(1,16),c/Fraction(2**120))
    L4coef=140*sig2**2+56
    L_E=200*sig3*T
    L_B=24*_ceil_sqrt_exact(L4coef)*T*T
    s0=max(64,1008*T,(12*L_E)**2,(48*L_B)**8)
    # Heavy tail proof gate: physical original H loses <=2|Z|
    # full heavy edges; I_Z >= eps*s^4/4 from unique original owner.
    if not (rho<=Fraction(1,32) and
            eps-2*rho>=eps/2 and
            T==2**41*C_graph**3*16**6 and
            c*eps**12/Fraction(2**84)==c/Fraction(2**120)):
        raise AssertionError("formal original heavy tail certificate incorrect")
    # Low-tail: remove original high-core/source conflict/Z IDs
    # but keep both physical diagonals; 2*N0>=s^4.
    if not (
        1-eps-Fraction(3,32)-rho>=Fraction(3,4) and
        rho*768*M3_squared<=1 and
        8*sixth<=4900*T*T and
        2*sig2**2*70+56<=L4coef):
        raise AssertionError("formal mixed source/core/endpoint mask budget incorrect")
    # The 3 path error terms in (21) have the following conservative
    # constraints. s0 >= 1008T, (12 LE)^2, (48 LB)^8.
    # They individually guarantee their error <=s^6/24.
    if not (s0>=1008*T and
            s0>=(12*L_E)**2 and
            s0>=(48*L_B)**8):
        raise AssertionError("nonsextic error exponents gate incomplete")
    if not Q_TEN>10*Fraction(5175,51**6):
        raise AssertionError("ten-sign source event improvement lost")
    pack_rate=rho/Fraction(6)
    clean_rate=Q_TEN*pack_rate
    distance_coefficient=clean_rate/Fraction(2)
    distance_deviation_rate=clean_rate/Fraction(8)
    return {
        "schema":"mathlab.hyp105.AA4-UDEL-to-PALDIST-CONDITIONAL-exact-v1",
        "C_graph_is_only_a_FORMAL_external_SS6_parameter":True,
        "c_graph_is_only_a_FORMAL_external_SS6_parameter":True,
        "C_graph_formal":str(C_graph),
        "c_graph_formal":str(c),
        "graph_SS6_actual_constants_VERIFIED":False,
        "heavy_degree_cap_T":str(T),
        "selected_original_conflict_cap_K":k,
        "original_selector_sigma2_inverse":str(sig2),
        "original_selector_sigma3_inverse":str(sig3),
        "original_physical_sixth_walk_L6":str(sixth),
        "original_proper_path_M3_squared":str(M3_squared),
        "parent_674_original_deletion_rho":str(rho),
        "parent_674_original_sevenmotif_delta":str(delta),
        "parent_674_symbolic_s0":str(s0),
        "parent_674_s0_binary_bit_length":s0.bit_length(),
        "allh_conditional_packing_t_strictly_greater_rho_s4_over_6":True,
        "full_ten_sign_UNION_GF5_original_probability_q10":str(Q_TEN),
        "allh_random_clean_exponential_rate_q10rho_over_6":str(clean_rate),
        "allh_random_recolor_distance_min_coeff_q10rho_over_12":
            str(distance_coefficient),
        "allh_recolor_lower_tail_exponential_rate_q10rho_over_48":
            str(distance_deviation_rate),
        "allh_requires_parent_674_qualified_mathematical_review":True,
        "allh_requires_actual_external_SS6_positive_constants":True,
        "allh_NEW_geometric_obstruction_proved_here":False,
        "root_230_status":"OPEN_WITH_FORMAL_BLOCKER",
        "allh_sufficient_threshold_quantifier":
            "for dyadic s=2^h >= s0(C_graph), if claimed #674 original theorem valid",
        "GF5_uniform_random_source_NOT_arbitrary_deterministic_initial":True,
        "note":"Independent EXACT arithmetic and logic verification ONLY: parent geometric hypotheses not discharged",
    }
