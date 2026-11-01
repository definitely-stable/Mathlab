"""HYP-105 AA4-BOOKBUD: independent all-h EXACT original-source budget referee.

This is NOT the 'maximal epsilon' in #689's deliberately COARSE bound
Cs<=3s4/2. Instead use the actual symplectic GQ formulas for N and Cs
and an independent rational ALL-h analytic majorant.
NO changed f/g maps; NO claim of a new exponent or human peer review.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb,isqrt

from hyp105_full_physical_degree_tail import genuine_source

K=64
EPS_689=Fraction(13,32)
EPS_NEW=Fraction(1787,4096)
B=Fraction(97,64)
ANALYTIC_PENALTY=Fraction(38245,33554432)
LOWER_BUDGET=Fraction(7,16)-ANALYTIC_PENALTY


def ceil_rat(q):
    return -(-q.numerator//q.denominator)


def ceil_sqrt(n):
    t=isqrt(n)
    return t+int(t*t<n)


def exact_pos(x):
    if type(x) not in (int,Fraction) or Fraction(x)<=0:
        raise ValueError("positive exact rational constant required; no float/bool")
    return Fraction(x)


def true_minimal_alphabet(V):
    if type(V) is not int or V<1:
        raise ValueError("V must be a positive integer")
    a=(1+isqrt(1+8*V))//2
    while a*(a-1)<2*V:a+=1
    while a>2 and (a-1)*(a-2)>=2*V:a-=1
    return a


def original_core_budget(s,epsilon=EPS_NEW):
    """NO sample-based asymptotic extrapolation.

    Exact source bound: m0>2*(N-eps*s4-4Cs/64).
    The s-independent lower is proved analytically from minimal alphabet.
    """
    if type(s) is not int or s<64 or s&(s-1):
        raise ValueError("power-of-two original source order >=64 required")
    epsilon=exact_pos(epsilon)
    V=(s+1)*(s*s+1)
    N=(s+1)*V
    a=true_minimal_alphabet(V)
    Cs=(s*s+1)*(s*s+a-2)
    density_budget=Fraction(N,s**4)-Fraction(1,2)-Fraction(Cs,16*s**4)
    if not (a*(a-1)>=2*V and (a-1)*(a-2)<2*V):
        raise AssertionError("minimal original label alphabet failed")
    if not (epsilon<=LOWER_BUDGET<=density_budget):
        if epsilon>LOWER_BUDGET:
            raise ValueError("epsilon not certified by universal bound")
        raise AssertionError("proved original-source lower budget violated")
    return {
        "s":s,"V":V,"N":N,"a":a,"Cs":Cs,
        "exact_max_epsilon_for_m0_ge_s4":density_budget,
        "independent_analytic_all_s_lower":LOWER_BUDGET,
        "chosen_epsilon":epsilon,
        "paired_core_lower":2*(N-epsilon*s**4-Fraction(Cs,16)),
        "above_s4":2*(N-epsilon*s**4-Fraction(Cs,16))>=s**4,
    }


def universal_analytic_certificate():
    """Algebraic inequality for every real s>=64, no finite fitting.

    Let t=1/sqrt(s)<=1/8, b=97/64 and a<=b*s*sqrt(s).
    N/s4 >=1+2t²;
    Cs/s4 <=(1+t^4)*(1+b*t).
    Hence budget >=7/16+2t²-b*t/16-t^4/16-b*t^5/16.
    Complete square 2t²-b*t/16 >= -b²/2048,
    and t^4<=1/4096, t^5<=1/32768.
    """
    independent=Fraction(7,16)-B*B/2048-Fraction(1,65536)-B/Fraction(524288)
    if independent!=LOWER_BUDGET:
        raise AssertionError("exact rational budget constant drift")
    if not (EPS_689<EPS_NEW<LOWER_BUDGET<Fraction(7,16)):
        raise AssertionError("claimed larger epsilon not certified")
    return {
        "s_all_dyadic_at_least":64,
        "epsilon_prior":EPS_689,
        "epsilon_improved":EPS_NEW,
        "epsilon_analytic_upper_certificate":LOWER_BUDGET,
        "strict_margin":LOWER_BUDGET-EPS_NEW,
        "full_book_bound_used_exactly":"Cs=(s^2+1)(s^2+a-2)",
        "original_N":"(s+1)^2*(s^2+1)",
        "proven_a_upper":"a<=(97/64)*s*sqrt(s)",
    }


def root_symbolic(C,c,epsilon=EPS_NEW):
    """Entire #686 loss stack recomputed independently for chosen epsilon.

    Published balanced C6 SS6 graph C,c are EXISTENTIAL real constants.
    Rational values are test inputs ONLY, NOT actual published constants.
    """
    C,c,epsilon=map(exact_pos,(C,c,epsilon))
    if epsilon>LOWER_BUDGET:
        raise ValueError("epsilon lacks all-h exact-source budget certificate")
    T=max(1,ceil_rat(Fraction(2**40)*C**3/epsilon**6))
    alpha=c*epsilon**12/Fraction(2**72)
    delta=min(Fraction(1,8),alpha)
    sig2_inv=16*65**2
    sig3_inv=64*65**3
    L6=24+288*T*T
    L4ceil=2*sig2_inv**2*ceil_sqrt(8*L6)+40*T
    B0ceil=64*ceil_sqrt(65*T)
    thresholds={
        "original_source_ge64":64,
        "proper_three_path":816*T,
        "exceptional_source_endpoints":144*21*sig3_inv**2*L6,
        "four_true_original_internal_blockers":48**8*(B0ceil*T*L4ceil)**4,
    }
    s0=max(thresholds.values())
    h0=max(1,(s0-1).bit_length())
    assert (1<<h0)>=s0 and (h0==1 or (1<<(h0-1))<s0)
    return {
        "epsilon":epsilon,"T":T,"alpha_heavy":alpha,
        "delta_original_sixsets":delta,
        "s0_sufficient":s0,"h0_sufficient":h0,
        "critical_thresholds":thresholds,
        "exact_signed_GF5_R3_lower_coefficient":min(
            Fraction(54162)*delta,Fraction(53526,8))/51**6,
        "interpretation":"symbolic; C,c only test placeholders, not known graph constants"
    }


def independent_true_source_books(power,shift=0):
    """Check ORIGINAL source conflicts and both source pencil books by
    independent explicit flag pairs for genuine W32 and W34.
    """
    if type(power) is not int or power not in (1,2):
        raise ValueError("finite genuine source oracle supports h=1,2")
    if type(shift) is not int:
        raise ValueError("integer permutation shift required")
    s,V,flags=genuine_source(power)
    a=true_minimal_alphabet(V)
    pairs=tuple(combinations(range(a),2))
    f=pairs[:V]
    g=tuple(pairs[(i+shift)%V] for i in range(V))
    if len(set(f))!=V or len(set(g))!=V:
        raise AssertionError("source pair maps must be globally injected")
    # Source books by true ORIGINAL pencil-coordinate populations.
    right=Counter((p,y) for p,ell in flags for y in g[ell])
    left=Counter((ell,x) for p,ell in flags for x in f[p])
    Mg=sum(v*(v-1)//2 for v in right.values())
    Mf=sum(v*(v-1)//2 for v in left.values())
    # Completely independent ORIGINAL-ID unordered conflict scan.
    conflicts=0
    for i,(p,ell) in enumerate(flags):
        for q,r in flags[i+1:]:
            if ((p==q and bool(set(g[ell])&set(g[r]))) or
                (ell==r and bool(set(f[p])&set(f[q])))):
                conflicts+=1
    Cs=(s*s+1)*(s*s+a-2)
    if conflicts!=Mf+Mg or Mf>Cs or Mg>Cs:
        raise AssertionError("true source original-book spectral bound mismatch")
    return {"s":s,"original_flags":len(flags),
            "a":a,"Mf":Mf,"Mg":Mg,
            "direct_original_conflicts":conflicts,
            "Cs_all_h":Cs,
            "original_source_identity_verified":True}
