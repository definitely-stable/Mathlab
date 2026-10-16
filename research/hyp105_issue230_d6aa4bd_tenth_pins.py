"""AA4-BD: 10% adversarially pinned genuine-original LINE images.

Every dyadic h>=5, EVERY complete original point map f, EVERY right
occupied physical support E, and EVERY injected original LINE-label
partial map of k<=floor(V/10) distinct source LINE IDs can be completed
to a true original globally bijective g with >=s**6/80 physically GOOD
opposite three-original-incidence-flag wedges.

This is a PARTIAL-map extension, NOT all fully fixed f,g and NOT six-ID GF5.
"""
from fractions import Fraction

from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import _params
from hyp105_issue230_d6aa4bb_overlap_covariance import (
    all_three_source_line_overlap
)
from hyp105_issue230_d6aa4bc_robust_pins import (
    _falling, actual_original_pinned_completion_certificate
)


def sharp_clean_all_support_floor(s):
    """Independent stronger AA4-AZ energy LOWER from minimal-palette holes.

    For any V-edge support E(K_a) the AA4-AO induced CLEAN physical
    support has rooted opposite two-port T(E_clean)>=9 V^2/8.
    The proof polynomial is NONNEGATIVE for every t=a-31>=230.
    """
    if type(s) is not int or s<32 or s & (s-1):
        raise ValueError("dyadic s=2^h with h>=5 is essential")
    V,a,_,m = _params(s)
    t=a-31
    if t<230 or m>a-2:
        raise AssertionError("minimal physical alphabet arithmetic")
    L=(Fraction(t*(t-1),2)-a)*(t-2)**2-2*a*(t-1)*(t-2)
    u=t-230
    # EXACT polynomial expansion of L - 9(t+31)^4/32, all positive:
    cert=(Fraction(7,32)*u**4+Fraction(1287,8)*u**3+
          Fraction(637949,16)*u**2+Fraction(27384651,8)*u+
          Fraction(737401095,32))
    if L-Fraction(9,32)*a**4!=cert or cert<=0:
        raise AssertionError("symbolic all-h clean physical port certificate failed")
    if L<Fraction(9,8)*V*V:
        raise AssertionError("minimal support clean port floor regression")
    return {
        "s":s,"V":V,"a":a,"m":m,"t":t,
        "uniform_true_original_support_clean_T_floor":Fraction(9,8)*V*V,
        "symbolic_universal_lower_from_a":L,
        "nonnegative_polynomial_all_t_ge_230":cert,
        "clean_good_rule_from_FULL_physical_support":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER"
    }


def tenth_pinned_GOOD_completion(s,k):
    """Worst-case exact Fraction conditional expectation and variance.

    Uniform over EACH legal partial original LINE map phi, all actual
    source W(3,s) original point f, and adversarial full support E.
    Uses accepted parent #561/#562/#563 per-source incidence bounds.
    """
    x=sharp_clean_all_support_floor(s)
    V,a=x["V"],x["a"]
    if type(k) is not int or not 0<=k<=V//10:
        raise ValueError("k must be between 0 and floor(V/10) actual LINE IDs")
    d=s+1
    t=a-2
    n=V-k
    T0=x["uniform_true_original_support_clean_T_floor"]
    B0=d*(d-1)*(d-2)*T0
    M1=5*d**3*t*t
    M2=8*d**3*t
    M3=6*d**3
    Bstar=B0-k*M1
    Astar=2*T0-6*k*t*t
    if Bstar<Fraction(d**3*V*V,80):
        raise AssertionError("adversarial source 10%-pin deletion all-h floor failed")
    if Astar<V*V:
        raise AssertionError("adversarial physical 10%-pin deletion all-h floor failed")
    pstar=Fraction(Astar,_falling(n,3))
    must_mean=Bstar*pstar
    if must_mean<Fraction(s**6,80):
        raise AssertionError("all-h original GOOD completion mean floor failed")
    q=Fraction(_falling(n-3,3),_falling(n,3))
    P1=Fraction(4*t**4,_falling(n-1,4))
    P2=Fraction(16*n*t**3,_falling(n,4))
    eta=(1/q-1 +
         Fraction(3*M1,Bstar)*P1/pstar**2 +
         Fraction(3*M2,Bstar)*P2/pstar**2 +
         Fraction(M3,Bstar)/pstar)
    if eta*V>50000000:
        raise AssertionError("all-h exact rational 50-million/V bound lost")
    return {
        "s":s,"h":s.bit_length()-1,"V":V,"a":a,
        "adversarial_original_LINE_pin_capacity":V//10,
        "pinned":k,"unpinned_original_LINE_factors":n,
        "pinned_fraction_ceiling":Fraction(1,10),
        "clean_complete_full_support_T_floor":T0,
        "true_original_point_source_3flag_unpinned_weight_floor":Bstar,
        "right_good_ordered_free_edge_3tuples_floor":Astar,
        "conditional_mean_unpinned_original_GOOD_lower":must_mean,
        "conditional_relative_variance_upper":eta,
        "uniform_relative_variance_le_50000000_over_V":True,
        "probability_full_GOOD_less_than_s6_over160_upper":
            min(Fraction(1),4*eta),
        "some_complete_g_extending_all_adversarial_line_pins_GOOD_ge_s6_over80":True,
        "ALL_fully_fixed_g_or_six_original_ID_GF5_PROVED":False,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER"
    }


def actual_true_original_tenth_pins_certificate(model,pins):
    """True W32/W34 literal f and E, keeping pre-lock CLEAN coordinates."""
    k=len(pins)
    z=actual_original_pinned_completion_certificate(model,pins)
    s=model["s"]
    if s>=32:
        u=tenth_pinned_GOOD_completion(s,k)
        if z["original_clean_source_3flag_weight_avoiding_pins"]<u[
            "true_original_point_source_3flag_unpinned_weight_floor"]:
            raise AssertionError("true original unpinned source bound failed")
        if z["physical_good_ordered_right_free_edge_triples"]<u[
            "right_good_ordered_free_edge_3tuples_floor"]:
            raise AssertionError("actual physical support energy tenth-pins bound failed")
        if z["mean_unpinned_source_good_wedges"]<u[
            "conditional_mean_unpinned_original_GOOD_lower"]:
            raise AssertionError("actual original conditional mean tenth-pins bound failed")
        if z["relative_variance_unpinned_upper"]>u[
            "conditional_relative_variance_upper"]:
            raise AssertionError("actual original conditioned overlap upper failed")
    return z
