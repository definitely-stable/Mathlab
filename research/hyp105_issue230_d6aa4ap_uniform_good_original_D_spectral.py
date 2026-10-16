"""HYP-105 #230 AA4-AP: UNIFORM positive good true-original D-pair theorem.

ALL genuine symplectic W(3,s), s=2^h, h>=14; EVERY COMPLETE
globally injected pair of typed physical edge-label maps f,g.
AA4-AL proves >=s^5 unordered genuine original bilateral two-flag
pairs D. AA4-AO identifies physical coordinate "bad" when missing
physical K_a edge degree >=a/16, at most 31 of them per typed map.

NEW: show that D pairs whose FOUR physical ports avoid the bad sets
are >=s^5/10 for EVERY global pair f,g once h>=14. No randomness,
no independence across f,g, no synthetic incidence geometry.

Let B be REAL W(3,s) point-line incidence, and for physical
coordinate c/e, let P_c, L_e be actual ORIGINAL source fiber sets
of point/line factors. Their sizes <=a-1 due to globally injected
unordered edge physical images. The standard original GQ spectral
fact ||B-(d/V)J||_2 = sqrt(2s) implies
    B(P_c,L_e) <= d*(a-1)^2/V + sqrt(2s)*(a-1) = K.
Use the rigorous integer upper ceil(sqrt(2s)).

Let P_bad,L_bad be source point/line factors with ANY physically bad
label endpoint (not only an actual chosen D-pair port). Each set
has <=b(a-1) factors, b=floor(32m/a)<=31,
m=C(a,2)-V. Thus <=2*b*(a-1)*d genuine ORIGINAL flags touch
P_bad or L_bad. Each such flag (p,l) has at most FOUR physical
cell combinations (c,e) in f(p)×g(l); any D partner lies in one
of the four original cell source fiber incidence sets of size <=K.
The number of unordered D pairs with a port bad is therefore <=
    8*b*(a-1)*d*K.
No double-counting lower is used: this is an UPPER by union bounds.
By AA4-AL exact Cauchy/source-degenerate lower,
    |D| >= D0 = 8V²d²/a² - 2Vd² >=s^5,
so good D >= max(0,D0-8*b*(a-1)*d*K).

Proof the rational bound >=s^5/10 for h=14..23 by exact finite
integer calculations of the displayed closed forms (not finite
geometric enumeration); for ALL h>=24 via universal b<=31,
a-1<=2s^(3/2), d<=5s/4,
K<=5s+4s²<=21s²/4, hence bad<=3255s^(9/2)
and good>=s^5(1-3255/sqrt(s))>=841*s^5/4096 >s^5/10.

Combining independently proven AA4-AO per-GOOD D physical lower:
    SUM_(good D) occupied P5(point)*occupied P5(line)
      >= s^5/40 * [n(n-1)(n-2)]², n=a-3, h>=14.
This is a universal ORIGINAL-INDEXED PHYSICAL mass bound, NOT
accepted ORIGINAL six-flag source Hall, NOT selected seven-GF5 E/U,
NOT Branch A S=Omega(s^6).
"""
from fractions import Fraction
from math import comb, isqrt

from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _parameters,_actual_strict_original_transport,exact_original_global_transport)
from hyp105_issue230_d6aa4ao_robust_port_occupancy import (
    globally_bad_physical_coordinates,all_h_robust_original_D_port_physical_theorem)
from hyp105_issue230_d6aa4am_genuine_pair_sixcharge import (
    original_D_pair_index)
from hyp105_issue230_d6aa4an_port_completion_hall_funnel import (
    true_original_D_physical_ports)


def global_good_original_D_spectral_certificate(s):
    """Exact ALL-f,g source-original GOOD bilateral pair floor, h>=14.

    All operations Fraction/integer, no simulated large GQ or floats.
    The closed-form interval proof for h>=24 is built in; h=14..23
    are independently auditable ten exact integer parameter checks.
    """
    V,d,a=_parameters(s)
    h=s.bit_length()-1
    m=comb(a,2)-V
    b=min(31,(32*m)//a)
    assert 0<=b<=31 and m<=a-2
    sigma=isqrt(2*s-1)+1  # exact mathematical ceil sqrt(2s)
    K=Fraction(d*(a-1)**2,V)+sigma*(a-1)
    unordered_D0=Fraction(8*V*V*d*d,a*a)-2*V*d*d
    bad_ub=8*b*(a-1)*d*K
    good_ub_floor=max(Fraction(0),unordered_D0-bad_ub)
    proven=False
    if h>=14:
        if h>=24:
            # a-1 <= 2*s^(3/2), d <= 5s/4 and
            # K <= (21/4)s² for s>=4. This gives
            # bad <= 8*31*2*(5/4)*(21/4)*s^(9/2)
            #     = 3255*s^(9/2).
            assert (a-1)**2<=4*s**3
            assert 4*d<=5*s
            assert sigma*sigma>=2*s
            # sqrt(2s) <=2sqrt(s); exact integer proof uses
            # sigma<=2sqrt(s) for s>=4:
            assert sigma*sigma<=4*s
            assert K<=Fraction(21*s*s,4)
            assert unordered_D0>=s**5
            assert 4096**2<=s
            assert Fraction(841,4096)>Fraction(1,10)
            # Monotone analytic proof, no dependence on specific m:
            assert bad_ub<=Fraction(3255*s**5,4096)
            proven=True
        else:
            # Exactly TEN finite parameter inequalities, a proof for
            # h=14...23, NOT a finite actual GQ construction.
            proven=good_ub_floor>=Fraction(s**5,10)
            assert proven,("exact rational 14..23 failed",h)
    th=all_h_robust_original_D_port_physical_theorem(s)
    n=a-3
    universal_mass=(Fraction(s**5,40)*(
        n*(n-1)*(n-2))**2 if proven else None)
    return dict(
        s=s,h=h,V=V,d=d,a=a,
        globally_missing_physical_edges=m,
        bad_vertex_upper_each_type=b,
        original_B_central_singular_upper_integer=sigma,
        original_coordinate_cell_incidence_uniform_upper=K,
        all_global_unordered_D_lower_exact=unordered_D0,
        globally_port_bad_unordered_D_upper=bad_ub,
        globally_port_good_unordered_D_explicit_lower=good_ub_floor,
        universally_all_f_g_good_D_at_least_s5_over_10=proven,
        original_GOOD_D_uniform_lower=(
            Fraction(s**5,10) if proven else None),
        all_global_GOOD_D_indexed_PHYSICAL_P5_P5_mass_lower=universal_mass,
        conditional_per_good_D_occupied_P5_P5_min=th[
            "conditional_two_side_good_P5_P5_lower"],
        proof_method=("finite_exact_rational_h14_to_h23" if 14<=h<24
                      else "all_larger_h_analytic_3255_over_sqrt_s"
                      if h>=24 else "no_positive_good_D_claim"),
        full_source_Hall_positive_NOT_PROVED=True,
        selected_seven_GF5_E_U_s6_lower_NOT_PROVED=True,
        original_issue230_Branch_A_NOT_PROVED=True,
    )


def finite_genuine_original_good_D_audit(model):
    """ACTUAL source W32/W34: independent D-first port and spectral bounds.

    Computes real globally injected maps, ALL genuine source flags,
    bad physical vertices, and all real original compatible D pairs;
    compares truly GOOD physical ports with the rational all-h bound.
    Never interprets physical mass as accepted 6 original incidences.
    """
    s,V,d,a,left,right,inc,np,nl=_actual_strict_original_transport(model)
    bP=globally_bad_physical_coordinates(a,left)
    bL=globally_bad_physical_coordinates(a,right)
    badP=frozenset(bP["bad_physical_coordinate_indices"])
    badL=frozenset(bL["bad_physical_coordinate_indices"])
    source_badP={p for p in range(V) if badP.intersection(left[p])}
    source_badL={l for l in range(V) if badL.intersection(right[l])}
    assert len(source_badP)<=len(badP)*(a-1)
    assert len(source_badL)<=len(badL)*(a-1)
    good=bad=bad_source_pairs=0
    D=original_D_pair_index(model)
    for pair in D:
        ports=true_original_D_physical_ports(inc,left,right,pair)
        isgood=(ports[0][1] not in badP and ports[0][2] not in badP
                and ports[1][1] not in badL and ports[1][2] not in badL)
        if isgood:
            good+=1
        else:
            bad+=1
        (p,l),(q,m)=(inc[i] for i in pair)
        isbadsource=(p in source_badP or q in source_badP
                     or l in source_badL or m in source_badL)
        bad_source_pairs+=int(isbadsource)
        if not isgood and not isbadsource:
            raise AssertionError("bad physical D PORT not covered by bad ORIGINAL source")
    oracle=exact_original_global_transport(model)
    assert len(D)==oracle[
        "exact_UNORDERED_DISTINCT_source_flag_pair_bilateral_physical_collision"]
    t=global_good_original_D_spectral_certificate(s)
    assert good+bad==len(D)
    assert bad<=bad_source_pairs
    assert bad_source_pairs<=t["globally_port_bad_unordered_D_upper"]
    assert good>=t["globally_port_good_unordered_D_explicit_lower"]
    return dict(
        s=s,a=a,D_unordered_genuine_original=len(D),
        good_D_avoiding_all_four_bad_PHYSICAL_ports=good,
        D_with_at_least_one_bad_physical_port=bad,
        D_touched_by_bad_source_factor_upper_explicit=bad_source_pairs,
        physical_point_bad_vertex_count=len(badP),
        physical_line_bad_vertex_count=len(badL),
        physical_point_bad_source_factor_count=len(source_badP),
        physical_line_bad_source_factor_count=len(source_badL),
        all_global_spectral_certificate=t,
        source_good_D_positive_at_small_s_NOT_ASSERTED=True,
        selected_seven_GF5_acceptance_NOT_PROVED=True,
    )
