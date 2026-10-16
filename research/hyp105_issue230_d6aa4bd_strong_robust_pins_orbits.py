"""HYP-105 #230 AA4-BD: 4x more arbitrary true original LINE pins.

Parent AA4-BC holds for k<=floor(V/1024) at mean >=s6/512.
NEW robust partial-map source/physical theorem for h>=5:
  k<=floor(V/256) of the V=(s+1)(s²+1) genuine ORIGINAL LINE
  factors may be pinned to arbitrary distinct physical right images
  of the one fixed occupied K_a right support E.
  For ANY true original globally injected physical point map f:
   E_(ONE UNIFORM COMPLETE GLOBAL g | all pins) R_GOOD_free
                                        >=s6/1024
   Var_g(R_GOOD_free)/(E R_GOOD_free)^2 <= eta<=3*10^10/V.
 Hence some legal full g preserving EVERY adversarial pin has
 R_GOOD>=s6/1024, and conditional failure to reach s6/2048
 is at most min(1,4eta).

NEW complete-map orbit theorem, no re-randomized source event:
 For any PRESELECTED m free-physical-edge permutations T_j,
 each acts on an ENTIRE full g while keeping pinned original LINE
 images fixed. Since T_j is a bijection of the uniform completion
 fiber, the UNION bound says at least 1-4*m*eta fraction of all full
 completions g have R_GOOD(T_j*g)>=s6/2048 SIMULTANEOUSLY for
 every j, IF 4*m*eta<1. m=2 with identity plus any complete
 derangement is guaranteed for h>=13 via eta<=3e10/V, since
 V(2^13)>2.4e11. Thus TWO coherent good global completions
 can differ at ALL V-k free original line images (Hamming n),
 yet agree on arbitrary k pins. Original source f/g fixed
 per full g; NO per-flag or per-six-Q label redraw.

This is NOT for every fully adversarial g; not accepted historical
seven-class GF5 SIX distinct ORIGINAL incidence ID Q; root #230 OPEN.
"""
from fractions import Fraction

from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import _params
from hyp105_issue230_d6aa4az_quenched_good_opposite import (
    universal_original_clean_twoport_support_floor)
from hyp105_issue230_d6aa4bc_robust_pins import (
    _falling,certified_robust_pins_envelope)


def strengthened_original_robust_pin_envelope(s,k):
    """EXACT all-h>=5 same-global original GQ partial LINE map certificate.

    No genuine W(3,s) incidence matrix materialization at large h:
    depends on previously proved CLEAN original source+physical
    s-uniform support lower and pin union-deletion bounds.
    """
    old=universal_original_clean_twoport_support_floor(s)
    if not old["uniform_clean_T_ge_V_squared_over_16_proved"]:
        raise ValueError("genuine original dyadic s=2^h>=32 required")
    V,a,_,_=_params(s)
    if type(k) is not int or not 0<=k<=V//256:
        raise ValueError("up to floor(V/256) distinct arbitrarily pinned ORIGINAL LINE image factors")
    n=V-k
    d=s+1
    t=a-2
    T0=Fraction(V*V,16)
    B0=d*(d-1)*(d-2)*T0
    M1=5*d**3*t*t
    M2=8*d**3*t
    M3=6*d**3
    Bstar=B0-k*M1
    Astar=2*T0-6*k*t*t
    # Universal analytic inequalities, NOT empirical high-h
    # approximations. The real GQ has d=s+1>=33 and
    # d^2/((d-1)(d-2)) <=11/10, minimal a gives (a-2)^2<2V.
    if not (
        t*t<2*V and
        10*d*d<=11*(d-1)*(d-2) and
        Bstar>=Fraction(5,16)*B0 and
        Astar>=Fraction(5,4)*T0 and
        n>=Fraction(255,256)*V
    ):
        raise AssertionError("AA4-BD stronger all-h <=V/256 SOURCE/PHYSICAL independent pin deletion lemma")
    p=Fraction(Astar,_falling(n,3))
    expectation=Bstar*p
    universal_lower=Fraction(s**6,1024)
    # Stronger exact elementary product d(d-1)(d-2)V>=s^6.
    sharp_product=d*(d-1)*(d-2)*V
    if not (
        sharp_product>=s**6 and
        expectation>=Fraction(25,16384)*s**6 and
        expectation>=universal_lower and
        p>=Fraction(5,64*V)
    ):
        raise AssertionError("AA4-BD fourfold wider pinned completion s6/1024 mean proof")

    q=Fraction(_falling(n-3,3),_falling(n,3))
    P1=Fraction(4*t**4,_falling(n-1,4))
    P2=Fraction(16*n*t**3,_falling(n,4))
    eta=(1/q-1
         +Fraction(3*M1,Bstar)*P1/(p*p)
         +Fraction(3*M2,Bstar)*P2/(p*p)
         +Fraction(M3,Bstar)/p)
    # The eight deliberately loose analytic BC upper factors STILL
    # hold with the larger k. For the three SOURCE overlaps:
    # M1/Bstar <= 563.2/V <640/V,
    # M2/Bstar <638/V^(3/2) <1024/V^(3/2),
    # M3/Bstar <338/V^2 <384/V^2.
    # For IMAGE probabilities N>=255V/256 ensures the same
    # P1,P2,q numerical majorants used in parent AA4-BC.
    if not (
        Fraction(M1,Bstar)<=Fraction(640,V) and
        Fraction(M2,Bstar)**2 <= Fraction(1024**2,V**3) and
        Fraction(M3,Bstar)<=Fraction(384,V*V) and
        P1<=Fraction(4096,V*V) and
        P2*P2 <= Fraction(32768**2,V**3) and
        1/p <=16*V and
        1/q-1 <=Fraction(60,V) and
        eta<=Fraction(30000000000,V)
    ):
        raise AssertionError("AA4-BD old all-h 30-billion/V variance proof survives 4x more pins")
    predecessor=None
    if k<=V//1024:
        predecessor=certified_robust_pins_envelope(s,k)
        if expectation!=predecessor[
                "conditional_mean_of_unpinned_GOOD_wedges_lower"] or (
                eta!=predecessor["conditional_relative_variance_upper"]):
            raise AssertionError("AA4-BD must be literally identical to independent AA4-BC exact rational formula on shared domain")

    return dict(
        s=s,h=s.bit_length()-1,V=V,a=a,k=k,
        pinned_fraction_capacity_denominator=256,
        arbitrary_pinned_actual_original_LINE_factor_limit=V//256,
        freely_completed_original_LINE_factor_count=n,
        original_source_after_any_adversarial_pins_weight_floor=Bstar,
        same_FULL_support_clean_physical_free_threeedge_floor=Astar,
        exact_rational_uniform_conditional_GOOD_mean_lower=expectation,
        original_GOOD_mean_universal_s6_over1024=True,
        universal_conditional_GOOD_mean_lower=universal_lower,
        exact_rational_conditional_GOOD_relative_variance_upper=eta,
        universal_relative_variance_le_30000000000_over_V=True,
        failure_probability_below_s6_over2048_upper=min(Fraction(1),4*eta),
        some_GLOBAL_completion_with_GOOD_at_least_s6_over1024=True,
        parent_exact_overlap_checked=(predecessor is not None),
        no_arbitrary_FULL_original_g_good_wedges_lower=True,
        no_original_six_ID_seven_GF5_lower=True,
        root_230="OPEN_WITH_FORMAL_BLOCKER",
    )


def simultaneously_robust_whole_global_completions(s,k,number_of_preselected_maps):
    """Conditional on ANY pinned right partial source-factor injection.

    The m caller-specified permutations of WHOLE FREE physical edge
    images may be arbitrary, do NOT need to be coordinate automorphisms.
    Each T_j maps the whole full-completion fiber into itself and
    preserves the UNIFORM law. Applying union bound to m events all
    with same pinned-g failure upper 4eta yields a positive existence
    count if strictly m*4eta<1. All source triple images in each T_j*g
    belong to ONE globally coherent full right map.
    """
    z=strengthened_original_robust_pin_envelope(s,k)
    m=number_of_preselected_maps
    if type(m) is not int or m<1:
        raise ValueError("at least one PRESELECTED whole-right-map support permutation, including identity")
    eta=z["exact_rational_conditional_GOOD_relative_variance_upper"]
    fail=4*m*eta
    if fail>=1:
        return dict(
            s=s,k=k,m=m,successful_simultaneous_orbit_NOT_CERTIFIED=True,
            analytic_GOOD_whole_map_fraction_lower=Fraction(0),
            strict_original_f_g_global_no_redraw=True,
            fixed_adversarial_fully_completed_g_UNPROVED=True,
        )
    return dict(
        s=s,k=k,m=m,
        analytic_GOOD_whole_map_fraction_lower=1-fail,
        for_ANY_preselected_m_FREE_edge_image_permutations_EXISTS_one_base_completion_good_for_ALL=True,
        each_full_map_GOOD_at_least_s6_over2048=True,
        strict_original_f_g_global_no_redraw=True,
        no_original_seven_GF5_six_ID_Q_claim=True,
    )


def fully_deranged_two_original_completions_all_large_h(s,k):
    """TWO successful fully-genuine ORIGINAL global line maps distance V-k.

    For h>=13: V>240e9 so even the worst-case eta<=30e9/V
    gives 8eta<1. Take preselected identity and ANY derangement of
    ALL free physical edge images; such a derangement exists since
    n=V-k>=2. Uniform-space inclusion/exclusion forces one base map
    good under both transformations. Both extend ALL arbitrary pins.
    """
    z=strengthened_original_robust_pin_envelope(s,k)
    if z["h"]<13:
        raise ValueError("independent universal all-h>=13 distant-two-global-map theorem")
    if not z["V"]>240000000000 or z["freely_completed_original_LINE_factor_count"]<2:
        raise AssertionError("V dyadic h>=13 threshold / free Hamming distance")
    orbit=simultaneously_robust_whole_global_completions(s,k,2)
    if "for_ANY_preselected_m_FREE_edge_image_permutations_EXISTS_one_base_completion_good_for_ALL" not in orbit:
        raise AssertionError("pair of fully deranged pinned-completion good maps not proved")
    return dict(
        s=s,k=k,V=z["V"],
        two_fully_globally_injected_original_LINE_maps_extend_same_adversarial_pins=True,
        each_map_genuine_original_GOOD_opposite_threeflag_wedges_at_least_s6_over2048=True,
        original_source_LINE_image_Hamming_distance_between_two_maps=z[
            "freely_completed_original_LINE_factor_count"],
        Hamming_changes_EVERY_free_original_LINE_factor=True,
        ALL_same_original_point_f_and_FULL_right_physical_support=True,
        success_base_completions_fraction_lower=orbit[
            "analytic_GOOD_whole_map_fraction_lower"],
        selected_six_DISTINCT_source_ID_seven_GF5_NOT_PROVED=True,
    )
