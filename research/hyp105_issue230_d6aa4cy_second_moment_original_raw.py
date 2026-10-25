"""AA4-CY: genuine ORIGINAL GQ second-moment raw-spoke floor, every halfcut.

All-h h>=24, every complete arbitrary correlated globally injective
original POINT f / LINE g into minimal physical K_a, EVERY two physical
halfcuts X,Y: >= s^(11/2)/2^26 distinct true ORIGINAL nonincident
point-line source anchors have a genuine raw-spoke crossing incidence.

This is a SECOND-MOMENT improvement over AA4-CX's Omega(s^5),
using ||A_f M A_g^T||_F, genuine source incidence M, two actual
occupied physical line-graph adjacency matrices A_f,A_g,
and the source singular-value bound sqrt(2s).

RAW source spoke crossings != physical doubled-disjoint C4 completion,
!= actual original 3x3 matching, != accepted sixflag GF5 motif.
"""
from collections import defaultdict
from itertools import combinations
from math import comb, isqrt

from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cw_multi_anchor_spoke_leakage import (
    exact_dyadic_cut_leakage_arithmetic,
    original_cut_spoke_leakage_certificate,
)


def allh_raw_frobenius_arithmetic(h):
    """Exact-integer necessary gates; analytic all-h proof in the Markdown."""
    z=exact_dyadic_cut_leakage_arithmetic(h)
    s,V,a,k,d=(z[j] for j in ("s","V","a","k","d"))
    # ||C||_F² <= 32d²k⁴ + 32sVk³.
    # For h>=24, d²k<=sV, k>s^(3/2)/2,
    # T>=k²dV/512, hence
    # # positive any >= k*d²*V/(2^24*s).
    # Discard <=Vd original INCIDENT endpoints.
    # k*s>=2^25*d grants positive nonincident >= k*s*V/2^25
    # >=s^(11/2)/2^26.
    if h>=24:
        if not (4*k < s*s
                and d*d*k <= s*V
                and 4*k*k >= s*s*s
                and k*s >= (1<<25)*d
                and 4*k*k > s*s*s
                and k>=8):
            raise AssertionError("all-h raw second-moment spectral gate invalid")
    return {
        "h":h,"s":s,"V":V,"a":a,"k":k,"d":d,
        "original_source_incidence_flags":V*d,
        "spectral_frobenius_second_moment_upper":
             32*d*d*k**4 + 32*s*V*k**3,
        "raw_positive_genuine_nonincident_lower_s11_half_squared_numerator":s**11,
        "raw_positive_genuine_nonincident_lower_s11_half_squared_denominator":1<<52,
        "raw_positive_integer_floor_at_least":isqrt(s**11)//(1<<26),
        "original_interacting_double_disjoint_anchors_NOT_PROVED":True,
        "historical_GF5_sixflag_lower_NOT_PROVED":True,
        "allh_gate_h_ge_24":h>=24,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def original_cut_frobenius_second_moment(model,X=None,Y=None,independent_flag_pair_oracle=True):
    """Exact true-original C=A_f M A_g^T, T=sum(C), Q=sum(C²).

    Occupied physical pair graph neighbors A_f and A_g live on
    ORIGINAL source POINT and LINE factor IDs, not synthetic sources.
    The optional independent *flag-pair-first* Q oracle uses
    ∑_{e,e' true source flags}|N_f(i)∩N_f(i')| |N_g(j)∩N_g(j')|.
    Only finite true original W32/W34/W38 fixtures are enumerated.
    """
    s,V,a,f,g,pl,lp=_validated_original(model)
    k=a//2
    X=tuple(range(k)) if X is None else tuple(X)
    Y=tuple(range(a-k,a)) if Y is None else tuple(Y)
    cw=original_cut_spoke_leakage_certificate(model,X,Y)
    xx,yy=frozenset(X),frozenset(Y)
    P=tuple(i for i in range(V) if set(f[i])<=xx)
    L=tuple(j for j in range(V) if set(g[j])<=yy)
    pset,lset=set(P),set(L)
    def neighbors(ids,labels):
        mapped={i:set(labels[i]) for i in ids}
        return {i:frozenset(j for j in ids if j!=i
                            and bool(mapped[i]&mapped[j])) for i in ids}
    pf=neighbors(P,f)
    gl=neighbors(L,g)
    if any(len(x)>2*(k-2) for x in tuple(pf.values())+tuple(gl.values())):
        raise AssertionError("physical K_k line-graph degree bound false")

    flags=tuple((i,j) for i in P for j in pl[i] if j in lset)
    C=defaultdict(int)
    for i,j in flags:
        for p in pf[i]:
            for l in gl[j]:
                C[p,l]+=1
    T=sum(C.values())
    Q=sum(value*value for value in C.values())
    positive_source_anchors=sum(l not in pl[p] for p,l in C)
    incident_positive=len(C)-positive_source_anchors
    if T!=cw["true_original_flag_mass_through_incut_physical_spokes"]:
        raise AssertionError("first source moment disagrees with independently frozen CW")
    if len(C)!=cw["positive_spoke_anchors_including_incident"]:
        raise AssertionError("true original RAW source spoke supports mismatch")
    if positive_source_anchors!=cw["positive_spoke_NONINCIDENT_P3_anchors"]:
        raise AssertionError("real ORIGINAL nonincident anchor count mismatch")
    if max(C.values(),default=0)!=cw["max_original_spoke_cross_incidence_at_one_anchor"]:
        raise AssertionError("original source local peak mismatch")
    if T*T>len(C)*Q:
        raise AssertionError("exact source Cauchy-Schwarz inequality violated")

    independent=None
    if independent_flag_pair_oracle:
        independent=sum(
            len(pf[i]&pf[ii])*len(gl[j]&gl[jj])
            for i,j in flags for ii,jj in flags
        )
        if Q!=independent:
            raise AssertionError("real original two-source-incidence flag-pair Gram identity false")

    # M=d/V J+M0, ||M0||op=sqrt(2s).
    # ||A_f||F²<=2k V, ||A_g||op<=2k.
    # signal²<=16d²k⁴, residual²<=16sVk³,
    # ||C||F²<=2signal²+2residual².
    cap=32*(s+1)**2*k**4+32*s*V*k**3
    if Q>cap:
        raise AssertionError("all-original singular-value Frobenius bound violated")
    return {
        "s":s,"V":V,"a":a,"k":k,
        "true_original_cut_point_factors":len(P),
        "true_original_cut_line_factors":len(L),
        "genuine_original_flags_between_two_cut_factor_sets":len(flags),
        "original_raw_spoke_first_moment_T":T,
        "original_raw_spoke_second_moment_Q":Q,
        "independent_original_source_flag_pair_Gram_Q":independent,
        "raw_spoke_positive_original_endpoint_pairs":len(C),
        "raw_spoke_positive_original_NONINCIDENT_P3":positive_source_anchors,
        "raw_spoke_positive_original_INCIDENT_pairs":incident_positive,
        "actual_source_peak_raw_incidence":max(C.values(),default=0),
        "source_spectral_absolute_Frobenius_Q_upper":cap,
        "Cauchy_positive_support_necessary_ceiling":
             (T*T+Q-1)//Q if Q else 0,
        "actual_original_second_moment_support_no_GF5_transfer":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
