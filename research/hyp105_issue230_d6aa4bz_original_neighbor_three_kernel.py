"""HYP-105 #230 AA4-BZ: true-original k=6 physical 2-factor neighbor cap THREE.

Every genuine original W(3,2^h), h>=1, arbitrary completely globally
injected potentially correlated POINT f and LINE g physical pair labels.
If six DISTINCT original source incidence flags Q hit six disjoint
whole-original-LINE-factor image-swap packets, precisely one original
LINE factor image per packet occurs in Q.

If I_Q(x) means the original RIGHT physical six-edge projection has
six physical vertices of degree two, its SIX adjacent cube states
contain at most THREE accepted states. This follows from degree-one
vertices and the DISTINCTNESS of ALL 12 original physical LINE factor
images. It holds for *all* sixcube vertices x and all physical K_a.

Elementary radial Fourier layer inequalities imply
  -264/5 <= sum_{x:I_Q(x)=1} K6(x) <= 139/2,
  K6(j)=(22,-10,2,2,-2,-2,10),
  so eta6(physical right 2-factor) <=139/128 <45/32.

Refines parent AA4-BY #599's original f-only ALL SEVEN historical GF5
necessary risk numerator sixcube center-certificate by 41/128 times
the actual sixth-packet f-eligible weighted ORIGINAL source-sixflag mass.

Do NOT call eta6=139/128 'sharp' for physically realizable
2-factors (the rational LP relaxation is not an indicator of a W3 Q).
Not root issue #230 Branch A/B/C.
"""
from collections import Counter
from fractions import Fraction

from hyp105_issue230_d6aa4by_original_independent_2factor_kernel import (
    CUBE6_INDEPENDENT_HIGH_PASS,
    original_six_packet_source_line_A,
    physical_right_is_six_vertex_two_regular,
    refined_original_W32_f_only_all_seven_kernel,
    refined_original_W32_all64_center_certificate,
)
from hyp105_issue230_d6aa4bx_all_seven_center_kernel import (
    high_degree_boolean_kernel,
)
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    apply_disjoint_factor_swaps,validate_disjoint_factor_swaps,
)
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source

CUBE6_NEIGHBOR_THREE_HIGH_PASS=Fraction(139,128)
CUBE6_INDEPENDENT_TO_NEIGHBOR_THREE_SAVING=Fraction(41,128)
CUBE6_RADIAL_KERNEL=(22,-10,2,2,-2,-2,10)

def exact_sixcube_neighbor_three_kernel_certificate():
    """Fully explicit 7-variable rational LP DUAL; NO solver dependency.

    For any physically accepted k6 original-Q right 2-factor indicator
    b(x), put p_j = mean_{|x|=j} b(x).
    Edge exclusion -> p_2 + p_3 <= 1, p_4 + p_5 <= 1.
    Neighborhood-at-most-three -> 6 p_1 <= 3,
       2 p_1 + 4 p_3 <= 3, 5 p_4 + p_6 <= 3.
    As 0<=p_j<=1 and the exact 6cube high-pass signed sum is
       T=22p0-60p1+30p2+40p3-30p4-12p5+10p6,
    its positive part is bounded by
       22 +30(p2+p3)+(5/2)(2p1+4p3)+10 <=139/2.
    Its negative part bounded by
       -10*(6p1) -12*(p4+p5)
       -(18/5)*(5p4+p6) >= -264/5.
    Hence |T|<=139/2; divide by 64.
    The 139/2 LP relaxation need NOT be achievable by physical Q.
    """
    k=6
    vals=high_degree_boolean_kernel(k)
    radial=tuple(vals[1<<j and (1<<j)-1] for j in range(7))
    if radial!=CUBE6_RADIAL_KERNEL:
        raise AssertionError("historical sixcube radial Walsh kernel drift")
    if not (Fraction(139,2)>Fraction(264,5) and
            CUBE6_NEIGHBOR_THREE_HIGH_PASS==Fraction(139,2*64) and
            CUBE6_INDEPENDENT_HIGH_PASS-CUBE6_NEIGHBOR_THREE_HIGH_PASS==
            CUBE6_INDEPENDENT_TO_NEIGHBOR_THREE_SAVING):
        raise AssertionError("incorrect exact rational signed dual coefficients")
    # A FRACTIONAL 7-LAYER certificate witnesses the precise UPPER
    # of the stated averaged-LP relaxation. Not an actual independent
    # Boolean vertex subset, and NOT a physical 2-factor realization.
    p=(Fraction(1),Fraction(0),Fraction(1,4),Fraction(3,4),
       Fraction(0),Fraction(0),Fraction(1))
    assert_radial_relaxation(p)
    score=sum(Fraction(6*5*4*3*2*1,1) /
              Fraction(__import__("math").factorial(j)*__import__("math").factorial(6-j))
              * radial[j]*p[j] for j in range(7))
    if score!=Fraction(139,2):
        raise AssertionError("explicit dual/relaxation witness failed")
    return {
        "radial_degree_ge4_Walsh_kernel":radial,
        "all_h_six_original_LINE_source_packets":6,
        "maximum_true_physical_neighbor_acceptances":3,
        "signed_highpass_numerator_upper":Fraction(139,2),
        "signed_highpass_numerator_lower":Fraction(-264,5),
        "true_original_sixcube_eta_upper":CUBE6_NEIGHBOR_THREE_HIGH_PASS,
        "parent_only_independent_eta":CUBE6_INDEPENDENT_HIGH_PASS,
        "strict_eta6_saving":CUBE6_INDEPENDENT_TO_NEIGHBOR_THREE_SAVING,
        "fractional_radial_upper_witness_not_actual_GF5":p,
        "eta_upper_NOT_sharp_realizability":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }

def assert_radial_relaxation(p):
    """Independent direct integer/Fraction check for proof inequalities."""
    p=tuple(Fraction(x) for x in p)
    if len(p)!=7 or any(not 0<=x<=1 for x in p):
        raise ValueError("7 radial layer fractions 0..1 expected")
    if any(p[i]+p[i+1]>1 for i in range(6)):
        raise ValueError("layerwise edge independence violated")
    if any(i*p[i-1] if i else 0 for i in []):
        raise AssertionError("unreachable")
    if any((i*p[i-1] if i else Fraction(0))+
           ((6-i)*p[i+1] if i<6 else Fraction(0))>3
           for i in range(7)):
        raise ValueError("neighbor maximum three per cube vertex violated")
    return True

def original_Q_sixcube_physical_neighbor_three(model,Q,pairs):
    """TRUE source ID Q evaluated at 64 complete globally injected g^x.

    Parent #599 already proved edge-wise independence. This NEW
    guard certifies the stronger at-most-three accepted NEIGHBORS at
    EACH of all 64 cube vertices, without any independence of Qs.
    """
    s,V,a,inc,f,g,_,_=_original_source(model)
    pairs=validate_disjoint_factor_swaps(V,pairs)
    if len(pairs)!=6 or not original_six_packet_source_line_A(
        Q,inc,pairs,V):
        raise ValueError("genuine original Q must hit six disjoint LINE packets")
    maps=tuple(apply_disjoint_factor_swaps(g,pairs,tuple(
       j for j in range(6) if x>>j&1)) for x in range(64))
    valid=tuple(int(physical_right_is_six_vertex_two_regular(
        Q,inc,images)) for images in maps)
    neigh=tuple(sum(valid[x^(1<<j)] for j in range(6)) for x in range(64))
    if max(neigh)>3:
        raise AssertionError("four neighbors physically 2regular contradicts unique globally injected EDGE images")
    if any(valid[x]*valid[x^(1<<j)] for x in range(64) for j in range(6)):
        raise AssertionError("one-edge replacement cannot preserve physical degree2")
    radial=tuple(Fraction(sum(valid[x] for x in range(64)
               if x.bit_count()==j),__import__("math").comb(6,j))
                 for j in range(7))
    assert_radial_relaxation(radial)
    K=high_degree_boolean_kernel(6)
    signed=sum(valid[x]*K[x] for x in range(64))
    if not Fraction(-264,5)<=signed<=Fraction(139,2):
        raise AssertionError("exact true-original physical indicator broke 7-layer rational proof")
    return {
        "original_six_incidence_source_IDs":tuple(Q),
        "physical_2factor_global_right_map_indicator":valid,
        "max_accepted_neighbors_in_sixcube":max(neigh),
        "exact_K6_highpass_signed_numerator":signed,
        "radial_physical_acceptance_layer_fraction":radial,
        "original_global_right_maps":64,
        "six_true_original_LINE_source_packets_distinct":True,
    }

def original_W32_f_only_all_seven_neighbor_three_envelope(model,pairs):
    """Strict f-only original ALL SEVEN center error improvement over #599."""
    old=refined_original_W32_f_only_all_seven_kernel(model,pairs)
    weighted=old["exact_source_line_A_six_packet_weighted_GF5_support"]
    new=old["sharpened_true_original_2factor_independent_f_quenched_E"] - (
        CUBE6_INDEPENDENT_TO_NEIGHBOR_THREE_SAVING*weighted)
    if new<0:
        raise AssertionError("physical true-Q error envelope cannot be negative")
    return {
        "parent_f_only_ALL_SEVEN_kernel_eta6":CUBE6_INDEPENDENT_HIGH_PASS,
        "new_f_only_ALL_SEVEN_kernel_eta6":CUBE6_NEIGHBOR_THREE_HIGH_PASS,
        "parent_all_seven_f_only_E":old[
            "sharpened_true_original_2factor_independent_f_quenched_E"],
        "new_original_f_only_ALL_SEVEN_error_upper":new,
        "weighted_six_source_packet_original_Q_mass":weighted,
        "strict_saving":CUBE6_INDEPENDENT_TO_NEIGHBOR_THREE_SAVING*weighted,
        "complete_original_right_map_g_UNRESTRICTED":True,
        "original_CENTER_seven_GF5_positive_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }

def original_W32_all64_true_center_neighbor_three(model,pairs):
    """Falsify new η6 bound against the FULL 64-map GF5 all-seven scores."""
    old=refined_original_W32_all64_center_certificate(model,pairs)
    env=original_W32_f_only_all_seven_neighbor_three_envelope(model,pairs)
    E=env["new_original_f_only_ALL_SEVEN_error_upper"]
    highs=old["original_center_actual_signed_highpass"]
    # parent only exposes center highpass and full W32 center score;
    # the complete all64 source model was tested in parent #599.
    if abs(highs)>E:
        raise AssertionError("true ORIGINAL all-seven weighted center exceeds neighbor-three envelope")
    low=old["original_center_low_degree_Walsh_value"]
    true=old["original_center_true_weighted_GF5"]
    if low-E>true:
        raise AssertionError("physical neighbor-three original center lower falsely excludes actual score")
    return {
        "original_seven_GF5_unchanged_center":true,
        "original_zero_through_third_Walsh_at_unchanged_center":low,
        "original_center_actual_degree4_through6_signed":highs,
        "new_f_only_ALL_SEVEN_kernel_E":E,
        "original_center_certified_nonnegative_lower":max(Fraction(0),low-E),
        "strict_E_reduction_over_parent":env["strict_saving"],
        "original_COMPLETE_right_map_g_arbitrary":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
