"""AA4-CX: all-h local GQ mixing upgrades multi-anchor RAW leakage to Omega(s^5).

All claims concern REAL original W(3,2^h), one full arbitrary correlated
point/line physical pair injection, six original incidence IDs unchanged.
No source 3x3 permanent/GF5 acceptance lower follows.

The original GQ M incidence nontrivial singular value sqrt(2s)
bounds each RAW physical spoke rectangle by <4s^2 (h>=24), replacing
AA4-CW's 2(k-2)(s+1). Combined with AA4-CW T>=k^2*d*V/512
gives >=s^5/16384 distinct genuine nonincident RAW-positive anchors.

For doubly physical disjoint original P3 anchors, filtering raw spokes
that meet doubled images removes at most FOUR point and FOUR line
spokes; original incidence loss per anchor <=8d. Bad anchors with
a doubled physical overlap number <=2(a-2)*s*(|P|+|L|).
The resulting error budgets exceed the established raw floor:
NO unconditional safe-spoke / physical C4 / perfect matching floor.
"""
from math import comb
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import original_nonincident_threepath
from hyp105_issue230_d6aa4cw_multi_anchor_spoke_leakage import (
    exact_dyadic_cut_leakage_arithmetic,
    original_cut_spoke_leakage_certificate,
)


def allh_local_spectrum_exclusion_arithmetic(h):
    """Integer-only arithmetic falsifier, h1..N; proof is fully symbolic in doc."""
    z=exact_dyadic_cut_leakage_arithmetic(h)
    s,V,a,k,d=(z[x] for x in ("s","V","a","k","d"))
    # Pointwise E(A,B)<= d*|A||B|/V + sqrt(2s)*sqrt(|A||B|),
    # |A|,|B| <=2(k-2). Exact integer sufficiently sharp gates:
    #
    # 4d(k-2)^2 /V < s^2
    # 2(k-2)*sqrt(2s) < 3s^2
    #
    # Sum CW raw source mass >= k^2*d*V/512.
    # Number positive nonincident >= T/(4s^2) - Vd.
    # k^2>=s^3/4,dV>=s^4,s>=2^24 yield >=s^5/16384.
    if h>=24:
        if not (
            k>=8 and 4*d*(k-2)**2 < s*s*V
            and 8*(k-2)**2 < 9*s**3
            and 4*k*k >= s**3 and s>=16384
            and 16384*d*V*(k*k-2048*s*s) >= 2048*s**7
        ):
            raise AssertionError("all-h strengthened local-spectrum/no-loss theorem gate invalid")
    # For any fixed POINT p, at most 2(a-2) original q have f(q)
    # intersecting f(p), each collinear q projects onto exactly s
    # distinct original nonincident l. Dual on fixed original l.
    bad_upper_one_side=2*(a-2)*s*V
    bad_union_upper=2*bad_upper_one_side
    local_loss_per_good_anchor=8*d
    return {"h":h,"s":s,"V":V,"a":a,"k":k,"d":d,
            "positive_raw_nonincident_lower_numerator":s**5,
            "positive_raw_nonincident_lower_denominator":16384,
            "max_raw_source_spoke_incidence_upper":4*s*s,
            "max_excluded_original_spoke_images_per_side":4,
            "max_original_incidence_loss_per_double_disjoint_anchor":local_loss_per_good_anchor,
            "double_overlap_bad_cut_anchor_upper":bad_union_upper,
            "source_spoke_raw_vs_safe_transfer_is_NOT_PROVED":True,
            "allh_gate_h_ge_24":h>=24,
            "root_230":"OPEN_WITH_FORMAL_BLOCKER"}


def original_cut_doubled_exclusion_certificate(model,X=None,Y=None):
    """Finite actual-GQ audit of AA4-CX RAW->SAFE lost original flags.

    SAFE refers only to physical doubled-factor exclusions; middle C4
    occupancy and two other actual ORIGINAL incidence IDs are NOT checked.
    """
    s,V,a,f,g,pl,lp=_validated_original(model)
    k=a//2
    X=tuple(range(k)) if X is None else tuple(X)
    Y=tuple(range(a-k,a)) if Y is None else tuple(Y)
    cw=original_cut_spoke_leakage_certificate(model,X,Y)
    xset,yset=frozenset(X),frozenset(Y)
    P=tuple(p for p in range(V) if set(f[p])<=xset)
    L=tuple(l for l in range(V) if set(g[l])<=yset)
    pf={p:frozenset(i for i in P if i!=p and
                    not frozenset(f[i]).isdisjoint(f[p])) for p in P}
    gl={l:frozenset(j for j in L if j!=l and
                    not frozenset(g[j]).isdisjoint(g[l])) for l in L}
    good=bad_left=bad_right=bad_either=raw_pos=safe_pos=raw_pos_good=0
    raw_total=raw_good=safe_good=lost_total=0
    max_raw=max_loss=0
    first_witness=None
    first_bad=None
    for p in P:
        for l in L:
            if l in pl[p]:
                continue
            path=original_nonincident_threepath(p,l,pl,lp)
            q,l0=path[1][0],path[0][1]
            bleft=not frozenset(f[p]).isdisjoint(f[q])
            bright=not frozenset(g[l]).isdisjoint(g[l0])
            bad_left+=bleft
            bad_right+=bright
            bad_either+=bleft or bright
            if (bleft or bright) and first_bad is None:
                first_bad=(p,l,bleft,bright)
            A=pf[p];C=gl[l]
            raw=sum(len(pl[i]&C) for i in A)
            raw_total+=raw
            raw_pos+=raw>0
            max_raw=max(max_raw,raw)
            if bleft or bright:
                continue
            good+=1
            raw_good+=raw
            raw_pos_good+=raw>0
            A_safe=frozenset(i for i in A if frozenset(f[i]).isdisjoint(f[q]))
            C_safe=frozenset(j for j in C if frozenset(g[j]).isdisjoint(g[l0]))
            dropped_left=len(A)-len(A_safe)
            dropped_right=len(C)-len(C_safe)
            if dropped_left>4 or dropped_right>4:
                raise AssertionError("physical doubled image can delete at most four spokes")
            safe=sum(len(pl[i]&C_safe) for i in A_safe)
            if safe>raw or raw-safe>8*(s+1):
                raise AssertionError("original source incidence loss budget violated")
            loss=raw-safe
            lost_total+=loss
            max_loss=max(max_loss,loss)
            safe_good+=safe
            safe_pos+=safe>0
            if raw>0 and safe==0 and first_witness is None:
                first_witness=(p,l,raw,dropped_left,dropped_right)
    if good+bad_either!=cw["source_original_nonincident_P3_anchors"]:
        raise AssertionError("all genuine source nonincident anchors partition invalid")
    if raw_pos!=cw["positive_spoke_NONINCIDENT_P3_anchors"]:
        raise AssertionError("independent original spoke method disagrees with AA4-CW")
    if (bad_left>2*(a-2)*s*len(P) or bad_right>2*(a-2)*s*len(L)):
        raise AssertionError("exact source GQ projection bad-anchor source-factor charging")
    if raw_good-safe_good!=lost_total:
        raise AssertionError("physical doubled-factor raw/safe exact loss decomposition")
    return {"s":s,"V":V,"a":a,"k":k,
            "source_POINT_cut_original_factor_count":len(P),
            "source_LINE_cut_original_factor_count":len(L),
            "original_nonincident_3path_anchors":good+bad_either,
            "double_disjoint_good_source_3path_anchors":good,
            "bad_left_physical_doubled_source_overlap_anchors":bad_left,
            "bad_right_physical_doubled_source_overlap_anchors":bad_right,
            "bad_either_physical_doubled_source_overlap_anchors":bad_either,
            "raw_original_spoke_positive_source_3path_anchors":raw_pos,
            "double_disjoint_raw_spoke_positive_anchors":raw_pos_good,
            "double_disjoint_SAFE_spoke_positive_anchors":safe_pos,
            "raw_original_source_incidence_mass_all_nonincident":raw_total,
            "raw_original_source_incidence_mass_double_disjoint":raw_good,
            "SAFE_original_source_incidence_mass_double_disjoint":safe_good,
            "exact_original_source_incidence_loss":lost_total,
            "max_original_spoke_rectangle_incidence":max_raw,
            "max_original_incidence_loss_one_good_anchor":max_loss,
            "first_actual_raw_positive_safe_zero_witness":first_witness,
            "first_actual_doubled_overlap_bad_anchor":first_bad,
            "not_an_original_3x3_matching":True,
            "not_a_GF5_accepted_motif":True,
            "root_230":"OPEN_WITH_FORMAL_BLOCKER"}
