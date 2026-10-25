"""AA4-DB: actual original W3 SAFE cross-flags with BOTH occupied physical C4s.

All dyadic h>=96: for every complete global correlated typed original
POINT/LINE injection into a common MINIMAL physical K_a and any two
halfcuts, >=s^7/2^15 immutable ORIGINAL source incidence flags are
counted (with their genuine nonincident unique P3 anchor multiplicity)
such that both associated SAFE spoke factors belong to actual occupied
physical C4 completion triples avoiding doubled images.

The C4 completions are ORIGINAL factor IDs, but their three-point by
three-line ORIGINAL incidence permanent may be ZERO. Do NOT promote
this theorem to accepted historical 6-flag GF(5) B/B-overlap or
all-seven S_s. Root #230 stays OPEN_WITH_FORMAL_BLOCKER.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations
from math import comb, isqrt

from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    original_nonincident_threepath,
)
from hyp105_issue230_d6aa4cx_local_spectrum_doubled_exclusion import (
    original_cut_doubled_exclusion_certificate,
)
from hyp105_issue230_d6aa4da_bridge_gram_safe_source_flags import (
    allh_original_bridge_gram_safe_arithmetic,
)


def allh_original_occupied_c4_arithmetic(h):
    """Exact dyadic infinite theorem gates; no finite-h proof extrapolation."""
    z=allh_original_bridge_gram_safe_arithmetic(h)
    s,V,a,k,d=(z[t] for t in ("s","V","a","k","d"))
    H=comb(a,2)-V
    # Missing physical pair labels H<=a-2. Each heavy physical
    # coordinate has missing degree >=(a-5)/2. For a>=8,
    # count heavy <=4H/(a-5) <=8.
    # <=8(a-1) true original typed source factor images touch one.
    # Each bad POINT/LINE source factor can occur as an anchor or
    # an original source SPOKE factor in SAFE physical source flags
    # with mass <=4k²d per role, independently on each typed side.
    loss=128*(a-1)*k*k*d
    if h>=96:
        if not (
            a>=8 and 0<=H<=a-2 and
            4*H <= 8*(a-5) and
            (a-1)*(a-1)<=4*s**3 and k*k<=s**3 and
            d<=2*s and 4*k*k>=s**3 and
            32768*loss<=s**7 and
            # Full source Q global from AA4-CY <=128s^(17/2).
            k*k*k<=s**4*isqrt(s)
        ):
            raise AssertionError("all-h original physical C4 hole-extension gate invalid")
    return {
        "h":h,"s":s,"V":V,"a":a,"k":k,"d":d,"H":H,
        "max_heavy_missing_degree_physical_coordinates":8,
        "max_original_bad_occupied_pair_source_factors_per_typed_map":8*(a-1),
        "raw_safe_to_both_occupied_C4_original_flag_mass_loss_upper":
            loss,
        "allh_both_occupied_c4_original_flag_mass_lower_numerator":s**7,
        "allh_both_occupied_c4_original_flag_mass_lower_denominator":1<<15,
        "allh_both_occupied_c4_true_original_positive_P3_lower_squared_numerator":s**11,
        "allh_both_occupied_c4_true_original_positive_P3_lower_squared_denominator":1<<74,
        "allh_both_occupied_c4_true_original_positive_P3_floor":isqrt(s**11)//(1<<37),
        "allh_gate_h_ge_96":h>=96,
        "occupied_C4_has_NOT_proved_source_original_3x3_matching":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def _physical_pair_holes_and_heavy(labels,a):
    """No synthetic SOURCE geometry: inspect missing physical image pairs only."""
    if len(labels)!=len(set(labels)):
        raise ValueError("complete globally injected typed original image labels required")
    occupied=frozenset(tuple(sorted(edge)) for edge in labels)
    H=comb(a,2)-len(occupied)
    missing_degree=[0]*a
    for edge in combinations(range(a),2):
        if edge not in occupied:
            u,v=edge;missing_degree[u]+=1;missing_degree[v]+=1
    if H!=sum(missing_degree)//2:
        raise AssertionError("complete original physical factor hole census invalid")
    heavy=frozenset(u for u,h in enumerate(missing_degree)
                    if 2*h >=a-5)
    if a>=8 and len(heavy)>8:
        raise AssertionError("theorem hole-heavy global coordinate counting failed")
    bad=frozenset(i for i,e in enumerate(labels) if any(u in heavy for u in e))
    if len(bad)>8*(a-1):
        raise AssertionError("bad original source physical factor charging failed")
    return {"H":H,"holes_by_coordinate":tuple(missing_degree),
            "heavy_physical_coordinates":heavy,
            "bad_original_source_factor_ids":bad,"occupied":occupied}


def occupied_C4_completion_containing_original_SAFE_spoke(
        single,double,spoke,physical_inverse,a):
    """Return one ACTUAL three-source-factor physical C4 completion witness.

    A single original SOURCE factor image (u,v), a doubled original
    SOURCE factor image disjoint from it, and a SAFE spoke original
    source factor image (u,z), z outside the 4 excluded coordinates.
    The occupied physical C4 needs real source factors at
    (u,z), (z,w), (w,v) with w outside p,q,z.
    """
    e,d,t=map(frozenset,(single,double,spoke))
    if not e.isdisjoint(d) or len(e)!=2 or len(d)!=2 or len(t)!=2:
        return ()
    shared=t&e
    if len(shared)!=1 or not t.isdisjoint(d) or t==e:
        return ()
    u=next(iter(shared))
    v=next(iter(e-{u}))
    z=next(iter(t-{u}))
    i=physical_inverse.get(tuple(sorted(t)))
    if i is None:
        raise AssertionError("original physical spoke image not occupied")
    for w in range(a):
        if w in e or w in d or w==z:
            continue
        center=physical_inverse.get(tuple(sorted((z,w))))
        other=physical_inverse.get(tuple(sorted((w,v))))
        if center is not None and other is not None:
            witness=(i,center,other)
            if len(set(witness))!=3:
                raise AssertionError("physical C4 source factor collision")
            return witness
    return ()


def original_cut_occupied_c4_source_flag_certificate(model,X=None,Y=None):
    """Exact finite ORIGINAL W3 test of SAFE->both physical C4 extension loss."""
    s,V,a,f,g,pl,lp=_validated_original(model)
    k=a//2
    X=tuple(range(k)) if X is None else tuple(X)
    Y=tuple(range(a-k,a)) if Y is None else tuple(Y)
    # Validate independent source-map/cut contracts before local work.
    prior=original_cut_doubled_exclusion_certificate(model,X,Y)
    P=tuple(p for p in range(V) if set(f[p])<=set(X))
    L=tuple(l for l in range(V) if set(g[l])<=set(Y))
    pf={p:frozenset(i for i in P if i!=p and bool(set(f[i])&set(f[p])))
        for p in P}
    gl={l:frozenset(j for j in L if j!=l and bool(set(g[j])&set(g[l])))
        for l in L}
    inv_f={tuple(sorted(edge)):i for i,edge in enumerate(f)}
    inv_g={tuple(sorted(edge)):j for j,edge in enumerate(g)}
    holes_f=_physical_pair_holes_and_heavy(f,a)
    holes_g=_physical_pair_holes_and_heavy(g,a)
    if len(inv_f)!=V or len(inv_g)!=V:
        raise AssertionError("complete original typed pair embedding violated")
    @lru_cache(None)
    def left(p,q,i):
        return occupied_C4_completion_containing_original_SAFE_spoke(
            f[p],f[q],f[i],inv_f,a)
    @lru_cache(None)
    def right(l,l0,j):
        return occupied_C4_completion_containing_original_SAFE_spoke(
            g[l],g[l0],g[j],inv_g,a)
    safe_mass=both_mass=unextended=positive_original_anchors=0
    positive_both_nonincident=0
    all_original_P3=0
    example=None
    witness=None
    for p in P:
        for l in L:
            if l in pl[p]:
                continue
            path=original_nonincident_threepath(p,l,pl,lp)
            q,l0=path[1][0],path[0][1]
            if set(f[p])&set(f[q]) or set(g[l])&set(g[l0]):
                continue
            all_original_P3+=1
            A=tuple(i for i in pf[p] if not set(f[i])&set(f[q]))
            B=frozenset(j for j in gl[l] if not set(g[j])&set(g[l0]))
            if not A or not B:
                continue
            Bc={j for j in B if right(l,l0,j)}
            zsafe=sum(len(pl[i]&B) for i in A)
            zboth=sum(len(pl[i]&Bc) for i in A if left(p,q,i))
            safe_mass+=zsafe
            both_mass+=zboth
            unextended+=zsafe-zboth
            positive_original_anchors+=zsafe>0
            positive_both_nonincident+=zboth>0
            if zsafe>zboth and example is None:
                example=(p,l,zsafe,zboth)
            if zboth and witness is None:
                for i in A:
                    wp=left(p,q,i)
                    if not wp:continue
                    for j in (pl[i]&Bc):
                        wl=right(l,l0,j)
                        if wl:
                            witness=(p,l,i,j,wp,wl)
                            break
                    if witness:break
    if safe_mass!=prior["SAFE_original_source_incidence_mass_double_disjoint"]:
        raise AssertionError("genuine immutable SOURCE SAFE flag census disagrees with AA4-CX")
    if positive_original_anchors!=prior["double_disjoint_SAFE_spoke_positive_anchors"]:
        raise AssertionError("original SAFE-positive anchor support mismatches independent census")
    if unextended<0 or unextended>safe_mass or safe_mass!=both_mass+unextended:
        raise AssertionError("original SAFE occupied-C4 extension partition mismatch")
    bound=128*(a-1)*k*k*(s+1)
    if unextended>bound:
        raise AssertionError("universal original SAFE->occupied C4 heavy-hole loss bound false")
    if s>=1<<96:
        theory=allh_original_occupied_c4_arithmetic(s.bit_length()-1)
        if both_mass*(1<<15)<s**7 or (
            positive_both_nonincident**2*(1<<74)<s**11):
            raise AssertionError("universal true original both physically occupied C4 theorem false")
    return {
        "s":s,"V":V,"a":a,"k":k,
        "real_original_nonincident_double_disjoint_3path_anchors":all_original_P3,
        "safe_actual_original_source_incidence_mass":safe_mass,
        "both_occupied_physical_C4_TRUE_original_cross_source_flag_mass":both_mass,
        "SAFE_to_occupied_C4_original_flag_mass_loss":unextended,
        "original_SAFE_positive_nonincident_P3":positive_original_anchors,
        "original_both_occupied_C4_positive_nonincident_P3":positive_both_nonincident,
        "actual_original_source_POINT_bad_factor_ids":len(holes_f["bad_original_source_factor_ids"]),
        "actual_original_source_LINE_bad_factor_ids":len(holes_g["bad_original_source_factor_ids"]),
        "POINT_heavy_hole_physical_coordinates":tuple(sorted(holes_f["heavy_physical_coordinates"])),
        "LINE_heavy_hole_physical_coordinates":tuple(sorted(holes_g["heavy_physical_coordinates"])),
        "allh_original_SAFE_to_both_occupied_C4_loss_upper":bound,
        "first_real_original_SAFE_but_non_C4_extendible_anchor":example,
        "first_real_original_cross_FLAG_with_both_occupied_C4_triplets":witness,
        "these_are_NOT_original_3x3_matching_flags":True,
        "does_NOT_prove_historical_sevenclass_GF5":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
