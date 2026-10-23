"""AA4-CZ: genuine GQ collinearity controls BOTH physical doubled-overlap bad paths.

All dyadic h>=60, every genuine original W(3,s), and every fully
complete globally injected arbitrarily correlated typed f,g:
  bad true-original nonincident P3 anchors <=8*s*(s+1)*V,
  TRUE original RAW spoke mass on doubly-physically-disjoint
  nonincident P3 anchors >=k*k*(s+1)*V/2048,
  number of those with a TRUE original RAW spoke incidence
       >= (s+1)^2*V*k/(2^28*s) >s^(11/2)/2^29.
These are RAW ORIGINAL flags; no safe crossed spokes, complete physical
C4s, SOURCE 3x3 matching, GF5 or sevenclass S lower asserted.
"""
from itertools import combinations
from math import comb, isqrt

from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    original_nonincident_threepath,
)
from hyp105_issue230_d6aa4cy_second_moment_original_raw import (
    original_cut_frobenius_second_moment,
    allh_raw_frobenius_arithmetic,
)


def allh_original_collinearity_badpath_arithmetic(h):
    """Exact big integers: all-h proof is separately given in Markdown."""
    z=allh_raw_frobenius_arithmetic(h)
    s,V,a,k,d=(z[x] for x in ("s","V","a","k","d"))
    holes=comb(a,2)-V
    # The source POINT and dual LINE original collinearity graphs have
    # nontrivial eigenvalues s-1 and -(s+1). The occupied physical K_a
    # coordinate stars each have at most a-1 TRUE source factor IDs.
    #
    # For each typed factor map:
    #   # ordered SOURCE-collinear, physically pair-overlapping (p,q)
    #       <=2*d*(V+s*(a-1)).
    # For every (p,q) with genuine SOURCE collinearity exactly s
    # original nonincident lines l project to q from source point p.
    # Dual for original LINEs.
    bad_exact_envelope=4*s*d*(V+s*(a-1))
    bad_simple_envelope=8*s*d*V
    Qcap=64*s*V*k**3
    Tlower_num=d*V*k*k
    Tlower_den=512
    if h>=60:
        if not (s*(a-1)<=V and k*d >= (1<<29)*s*s
                and k*k>=8192*s*s and
                k*k>=s**3//4 and k*s >= (1<<25)*d
                and V>s**3 and 2*k>s*isqrt(s)
                and bad_exact_envelope<=bad_simple_envelope):
            raise AssertionError("all-h source collinearity large-h robust mass gate false")
        # Ratio squared: (T_bad/T_lower)^2
        # <= (8sdV)*(64sVk^3) / ((dVk²/512)^2)
        # =2^27*s²/(d*k) <= 1/4.
        assert (1<<29)*s*s <=d*k
        # Incident-original source anchors <=Vd, every C<4s².
        # 4s²Vd <= T_lower/4 when k²>=8192s².
        assert k*k>=8192*s*s
    return {
        "h":h,"s":s,"V":V,"a":a,"k":k,"d":d,"physical_holes":holes,
        "typed_collinear_overlap_oriented_pair_upper":2*d*(V+s*(a-1)),
        "both_typed_nonincident_bad_P3_upper":bad_exact_envelope,
        "simple_both_typed_bad_P3_upper":bad_simple_envelope,
        "raw_first_moment_lower_numerator":Tlower_num,
        "raw_first_moment_lower_denominator":Tlower_den,
        "raw_second_moment_Q_upper":Qcap,
        "double_disjoint_nonincident_raw_mass_lower_numerator":d*V*k*k,
        "double_disjoint_nonincident_raw_mass_lower_denominator":2048,
        "double_disjoint_raw_positive_source_P3_lower_numerator":d*d*V*k,
        "double_disjoint_raw_positive_source_P3_lower_denominator":(1<<28)*s,
        "simplified_exponent_floor_s11half_integer":isqrt(s**11)//(1<<29),
        "proven_for_all_h_ge_60":h>=60,
        "does_not_guarantee_safe_original_incidence":True,
        "does_not_guarantee_true_original_3x3_matching":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def original_collinear_overlap_from_actual_source_flags(labels,pl,lp):
    """Enumerate all genuine ORIGINAL ordered collinear factor-ID pairs.

    For POINTs, pl[i] are actual original LINE IDs, lp[j] are original
    point neighborhoods; for LINEs, swap the typed roles. Never deduce
    original collinearity from physical pair intersections.
    """
    V=len(labels)
    if len(pl)!=V or len(lp)!=V or len(set(labels))!=V:
        raise ValueError("full globally injective ORIGINAL typed factors required")
    occupied=tuple(frozenset(edge) for edge in labels)
    total=0
    degree=tuple(0 for _ in range(V))
    counts=[]
    for i in range(V):
        unique=set()
        for j in pl[i]:
            unique.update(lp[j])
        unique.discard(i)
        if len(unique)!=len(pl[i])*(len(lp[pl[i][0]])-1):
            raise AssertionError("genuine GQ point graph collinear uniqueness violation")
        count=sum(not occupied[i].isdisjoint(occupied[ii]) for ii in unique)
        counts.append(count)
        total+=count
    return {"ordered_true_original_collinear_physical_overlap":total,
            "per_source_factor_collinear_overlap":tuple(counts)}


def _cut_raw_flags(model, X, Y):
    """One TRUE original source incidence pushforward, fixed complete f,g."""
    s,V,a,f,g,pl,lp=_validated_original(model)
    PX=tuple(p for p in range(V) if set(f[p])<=set(X))
    LY=tuple(l for l in range(V) if set(g[l])<=set(Y))
    PXset,LYset=set(PX),set(LY)
    pf={i:tuple(j for j in PX if j!=i and bool(set(f[i])&set(f[j])))
        for i in PX}
    lg={j:tuple(l for l in LY if l!=j and bool(set(g[j])&set(g[l])))
        for j in LY}
    # ORIGINAL source flag-first pushforward, actual source factors only
    mass={}
    for i in PX:
        for j in pl[i]:
            if j in LYset:
                for p in pf[i]:
                    for l in lg[j]:
                        mass[p,l]=mass.get((p,l),0)+1
    return PX,LY,mass


def original_cut_badpath_mass_certificate(model,X=None,Y=None):
    """Finite ORIGINAL source geometry checks AA4-CZ's bad-path identity.

    Enumerates every ORIGINAL nonincident source p/l in cut once.
    A positive surviving RAW spoke flag is deliberately NOT promoted
    to a SAFE spoke flag or a true ORIGINAL source three-matching.
    """
    s,V,a,f,g,pl,lp=_validated_original(model)
    k=a//2
    X=tuple(range(k)) if X is None else tuple(X)
    Y=tuple(range(a-k,a)) if Y is None else tuple(Y)
    prior=original_cut_frobenius_second_moment(
        model,X,Y,independent_flag_pair_oracle=False)
    PX,LY,C=_cut_raw_flags(model,X,Y)
    if sum(C.values())!=prior["original_raw_spoke_first_moment_T"] or (
            sum(x*x for x in C.values())!=prior["original_raw_spoke_second_moment_Q"]):
        raise AssertionError("original-source-first and independent flag-first T/Q disagree")
    col_f=original_collinear_overlap_from_actual_source_flags(
        f,pl,lp)
    col_g=original_collinear_overlap_from_actual_source_flags(
        g,lp,pl)
    for z in (col_f,col_g):
        if z["ordered_true_original_collinear_physical_overlap"]>2*(s+1)*(V+s*(a-1)):
            raise AssertionError("original GQ point/dual collinearity spectral star bound violated")

    nonincident=bad_left=bad_right=bad_either=bad_mass=incident_mass=good_mass=0
    original_nonincident_good_with_positive_raw=0
    good_with_zero_raw=0
    sample_good=None
    sample_bad=None
    for p in PX:
        for l in LY:
            c=C.get((p,l),0)
            if l in pl[p]:
                incident_mass+=c
                continue
            nonincident+=1
            path=original_nonincident_threepath(p,l,pl,lp)
            q,l0=path[1][0],path[0][1]
            bleft=bool(set(f[p])&set(f[q]))
            bright=bool(set(g[l])&set(g[l0]))
            bad_left+=bleft
            bad_right+=bright
            bad_either+=bleft or bright
            if bleft or bright:
                bad_mass+=c
                if sample_bad is None and c:
                    sample_bad=(p,l,c,bleft,bright)
            else:
                good_mass+=c
                original_nonincident_good_with_positive_raw+=c>0
                good_with_zero_raw+=c==0
                if sample_good is None and c:
                    sample_good=(p,l,c)
    T=prior["original_raw_spoke_first_moment_T"]
    Q=prior["original_raw_spoke_second_moment_Q"]
    if incident_mass+bad_mass+good_mass!=T:
        raise AssertionError("all true original source flag mass partitions invalid")
    if nonincident+prior["raw_spoke_positive_original_INCIDENT_pairs"]<0:
        raise AssertionError("invalid source anchor tally")
    if bad_left>s*col_f["ordered_true_original_collinear_physical_overlap"] or (
            bad_right>s*col_g["ordered_true_original_collinear_physical_overlap"]):
        raise AssertionError("original projection collinearity charged overlap upper violated")
    if bad_either>4*s*(s+1)*(V+s*(a-1)):
        raise AssertionError("uniform original GQ collinearity bad-P3 bound false")
    if bad_mass*bad_mass>bad_either*Q:
        raise AssertionError("bad-path mass violates original second-moment Cauchy")
    if s>=1<<60:
        z=allh_original_collinearity_badpath_arithmetic(s.bit_length()-1)
        if 2048*good_mass < (s+1)*V*k*k:
            raise AssertionError("all-h double-disjoint nonincident raw mass floor false")
        if (1<<28)*s*original_nonincident_good_with_positive_raw < (s+1)**2*V*k:
            raise AssertionError("all-h double-disjoint original raw-support floor false")
    return {
        "s":s,"V":V,"a":a,"k":k,"h":s.bit_length()-1,
        "original_source_incidence_count":V*(s+1),
        "actual_genuine_original_nonincident_cut_P3":nonincident,
        "source_collinear_physical_overlap_ordered_POINT":col_f["ordered_true_original_collinear_physical_overlap"],
        "source_collinear_physical_overlap_ordered_LINE":col_g["ordered_true_original_collinear_physical_overlap"],
        "source_genuine_projection_bad_anchor_upper_from_collinearity":
           s*(col_f["ordered_true_original_collinear_physical_overlap"]+
              col_g["ordered_true_original_collinear_physical_overlap"]),
        "actual_bad_left_P3":bad_left,"actual_bad_right_P3":bad_right,
        "actual_bad_union_nonincident_P3":bad_either,
        "actual_original_raw_bad_path_mass":bad_mass,
        "actual_original_raw_incident_path_mass":incident_mass,
        "actual_original_raw_good_nonincident_double_disjoint_mass":good_mass,
        "actual_original_double_disjoint_nonincident_raw_positive_P3":original_nonincident_good_with_positive_raw,
        "actual_original_double_disjoint_nonincident_raw_zero_P3":good_with_zero_raw,
        "all_original_raw_T":T,"all_original_raw_Q":Q,
        "first_bad_original_path_with_raw_flag":sample_bad,
        "first_good_original_path_with_raw_flag":sample_good,
        "ALL_H_SAFE_FLAG_MATCHING_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
