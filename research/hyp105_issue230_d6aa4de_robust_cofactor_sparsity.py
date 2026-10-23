"""AA4-DE: UNCONDITIONAL original BBo Hall defect is large; small-D strategy NO-GO.

For all dyadic h>=96, every genuine original symplectic W(3,s) and EVERY
complete arbitrary-correlated globally injective typed ORIGINAL point f /
line g into the same minimal K_a, in EVERY two physical halfcuts:

D_BBo >= D_light >= s^10 / 2^18,
max of four dual Hall-vacancy classes >=s^10/2^20.

Here D_BBo is a C4-PAIR-MULTIPLICITY-weighted failed 2x2 cofactor mark
of the EXACT original source incidence 3x3 (AA4-DC/DD). Not a count of
distinct six-incidence-ID GF5 positive motifs. No universal lower bound
on ORIGINAL accepted U_BBo or all-seven S_s follows.

Proof uses (a) parent AA4-DA guaranteed true original SAFE crossflags
on double-disjoint genuine P3; (b) <=16 heavy physical coordinates per
typed map with missing degree >=(a-5)/4; (c) per genuine anchored
light source flag >=m=floor((a-5)/2)+1 actual occupied C4 completions
on EACH side; (d) for a fixed point C4 completion, at most 2d line
C4 completions can EXTEND its marked true original source flag because
each has a DISTINCT ORIGINAL LINE other-spoke factor in the union of
the two remaining ORIGINAL POINT neighborhoods (size<=2d).

No random independent source maps, no synthetic GQ source geometry.
"""
from collections import Counter,defaultdict
from itertools import combinations
from math import comb,isqrt

from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original
from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import (
    c4_completions_from_single_and_doubled,
    original_nonincident_threepath,
)
from hyp105_issue230_d6aa4dd_dual_hall_vacancy import (
    allh_original_vacancy_dichotomy_arithmetic,
    original_marked_true_source_vacancy_certificate,
    SOURCE_VACANCY_CLASSES,
)


def allh_original_robust_defect_arithmetic(h):
    """Exact big-integer analytic gates; does NOT prove by finite extrapolation."""
    z=allh_original_vacancy_dichotomy_arithmetic(h)
    s,V,a,k=(z[t] for t in ("s","V","a","k"))
    d=s+1
    H=comb(a,2)-V
    m=(a-5)//2+1 if a>=5 else 0
    heavy_source_factor_upper=16*(a-1)
    light_flag_loss_upper=256*(a-1)*k*k*d
    if h>=96 and not (
        a>=8 and H<=a-2 and 8*H<=16*(a-5)
        and 32768*light_flag_loss_upper<=s**7
        and (a-5)**2>=s**3
        and 4*m*m>=s**3
        and m>=4*d
        and k*k<=s**3 and a-1<=2*s*isqrt(s) and d<=2*s
    ):
        raise AssertionError("original h>=96 robust LIGHT-HALL domination gate violated")
    return {
        "h":h,"s":s,"V":V,"a":a,"k":k,"d":d,
        "missing_original_physical_pair_images_H":H,
        "max_heavy_coordinates_per_original_typed_map":16,
        "max_source_typed_factors_touching_heavy":heavy_source_factor_upper,
        "max_true_original_SAFE_crossflag_light_filter_loss":light_flag_loss_upper,
        "least_occupied_C4_completions_per_original_LIGHT_marked_spoke":m,
        "original_C4_line_completions_extending_fixed_point_C4_mark_upper":2*d,
        "true_original_SAFE_LIGHT_crossflag_mass_floor_numerator":s**7,
        "true_original_SAFE_LIGHT_crossflag_mass_floor_denominator":1<<15,
        "original_LIGHT_C4_pair_mark_mass_floor_numerator":s**10,
        "original_LIGHT_C4_pair_mark_mass_floor_denominator":1<<17,
        "original_LIGHT_C4_pair_unextendible_cofactor_defect_floor_numerator":s**10,
        "original_LIGHT_C4_pair_unextendible_cofactor_defect_floor_denominator":1<<18,
        "max_original_four_typed_Hall_vacancy_mass_floor_numerator":s**10,
        "max_original_four_typed_Hall_vacancy_mass_floor_denominator":1<<20,
        "allh_gate_h_ge_96":h>=96,
        "NO_proven_other_GF5_class_compensation":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def _original_heavy_pair_sources(labels,a):
    """Actual original source typed factor images; PHYSICAL holes only."""
    if len(set(labels))!=len(labels) or any(
        len(e)!=2 or any(type(u) is not int or u<0 or u>=a for u in e)
        for e in labels
    ):
        raise ValueError("complete valid injected original typed physical pairs required")
    occupied={tuple(sorted(e)) for e in labels}
    missing=Counter()
    for u,v in combinations(range(a),2):
        if (u,v) not in occupied:
            missing[u]+=1;missing[v]+=1
    H=comb(a,2)-len(occupied)
    if sum(missing.values())!=2*H:
        raise AssertionError("missing true-original physical typed source pair ledger corrupted")
    # 4*delta >= a-5; for a>=8 H<=a-2 => at most 16 heavy coords.
    heavy=frozenset(u for u in range(a) if 4*missing[u]>=a-5)
    if a>=8 and H<=a-2 and len(heavy)>16:
        raise AssertionError("full typed physical missing-degree charging bound false")
    bad=frozenset(i for i,e in enumerate(labels) if set(e)&heavy)
    if a>=8 and len(bad)>16*(a-1):
        raise AssertionError("original typed source factor heavy-coordinate count false")
    return {"physical_missing_pair_count":H,
            "physical_missing_degree":tuple(missing[u] for u in range(a)),
            "heavy_physical_coordinates":tuple(sorted(heavy)),
            "bad_original_source_factor_ids":bad}


def original_light_crossflag_robust_defect_certificate(
        model, *, anchor_pairs, point_cut=None, line_cut=None,
        max_triples_per_side=None):
    """Real ORIGINAL source light-marked C4×C4 Hall census, one frozen f,g.

    Explicit anchor list is required, preventing an accidental ALL W38
    claim. No truncation => FULL source C4 completion pair domain for
    those ORIGINAL anchors; cap is explicitly PARTIAL, with no
    analytic lower extension bound attached to capped results.
    """
    s,V,a,f,g,pl,lp=_validated_original(model)
    if anchor_pairs is None:
        raise ValueError("explicit actual nonincident original source anchors required")
    if max_triples_per_side is not None and (
        type(max_triples_per_side) is not int or max_triples_per_side<1):
        raise ValueError("positive optional C4 completion sampling cap required")
    def cut(t):
        if t is None:return None
        t=tuple(t)
        if len(set(t))!=len(t) or any(type(u) is not int or not 0<=u<a for u in t):
            raise ValueError("physical coordinate cut must be valid and injective")
        return frozenset(t)
    X,Y=cut(point_cut),cut(line_cut)
    anchors=tuple(tuple(e) for e in anchor_pairs)
    if len(anchors)!=len(set(anchors)):
        raise ValueError("duplicate genuine original nonincident source anchor")
    for p,l in anchors:
        if (type(p) is not int or type(l) is not int or
            not 0<=p<V or not 0<=l<V or l in pl[p]
            or X is not None and not set(f[p])<=X
            or Y is not None and not set(g[l])<=Y):
            raise ValueError("source anchor is not a true original nonincident P3 in cut")
    invf={tuple(sorted(e)):i for i,e in enumerate(f)}
    invg={tuple(sorted(e)):i for i,e in enumerate(g)}
    hp=_original_heavy_pair_sources(f,a)
    hl=_original_heavy_pair_sources(g,a)
    bp,bl=hp["bad_original_source_factor_ids"],hl["bad_original_source_factor_ids"]
    d=s+1
    count=Counter()
    credits=Counter({kind:0 for kind in SOURCE_VACANCY_CLASSES})
    first_light=None
    first_rejected=None
    witness_ratio=None
    actual_min_point=None
    actual_min_line=None
    for p,l in anchors:
        path=original_nonincident_threepath(p,l,pl,lp)
        q,l0=path[1][0],path[0][1]
        if set(f[p])&set(f[q]) or set(g[l])&set(g[l0]):
            continue
        pts=c4_completions_from_single_and_doubled(f[p],f[q],invf,a)
        lns=c4_completions_from_single_and_doubled(g[l],g[l0],invg,a)
        if max_triples_per_side is not None:
            pts=pts[:max_triples_per_side];lns=lns[:max_triples_per_side]
        def group(completions,labels,base):
            out=defaultdict(list)
            for ids in completions:
                spokes=[v for v in ids if len(set(labels[v])&set(base))==1]
                center=[v for v in ids if not set(labels[v])&set(base)]
                if len(spokes)!=2 or len(center)!=1:
                    raise AssertionError("not an occupied ORIGINAL physical C4 triple")
                for marked in spokes:
                    other=next(i for i in spokes if i!=marked)
                    out[marked].append((other,center[0]))
            return out
        P=group(pts,f,f[p])
        L=group(lns,g,g[l])
        if p in bp or l in bl:
            continue
        for i,point_completions in P.items():
            if i in bp or X is not None and not set(f[i])<=X:
                continue
            for j in pl[i]:
                if j not in L or j in bl or Y is not None and not set(g[j])<=Y:
                    continue
                if set(f[i])&set(f[q]) or set(g[j])&set(g[l0]):
                    raise AssertionError("completed physically occupied original C4 crossed doubled source image")
                lines=L[j]
                mark_weight=len(point_completions)*len(lines)
                count["light_original_anchor_crossflags_with_two_occupied_C4_witnesses"]+=1
                count["light_completed_source_C4_pair_mark_T"]+=mark_weight
                actual_min_point=min(actual_min_point,len(point_completions)) if actual_min_point is not None else len(point_completions)
                actual_min_line=min(actual_min_line,len(lines)) if actual_min_line is not None else len(lines)
                if first_light is None:
                    first_light=(p,l,i,j,len(point_completions),len(lines))
                extendible=0
                rejected=0
                for other_p,center_p in point_completions:
                    successful_line_completions=0
                    for other_l,center_l in lines:
                        c=int(other_l in pl[other_p] and center_l in pl[center_p]) + int(
                            center_l in pl[other_p] and other_l in pl[center_p])
                        if c>1:
                            raise AssertionError("true original GQ source incidence C4 in 2x2")
                        if c:
                            successful_line_completions+=1
                            extendible+=1
                        else:
                            rejected+=1
                            # true original 2x2 zero row/column witness
                            residual=((int(other_l in pl[other_p]),int(center_l in pl[other_p])),
                                      (int(other_l in pl[center_p]),int(center_l in pl[center_p])))
                            if not(any(sum(row)==0 for row in residual) or
                                   any(residual[0][col]+residual[1][col]==0 for col in (0,1))):
                                raise AssertionError("2x2 original Hall failure has no true zero source row or col")
                            roles=(
                                sum(residual[0])==0,sum(residual[1])==0,
                                residual[0][0]+residual[1][0]==0,
                                residual[0][1]+residual[1][1]==0,
                            )
                            n=sum(roles)
                            for typ,yes in zip(SOURCE_VACANCY_CLASSES,roles):
                                if yes:credits[typ]+=12//n
                            if first_rejected is None:
                                first_rejected=(p,l,i,j,other_p,center_p,other_l,center_l,residual)
                    if successful_line_completions>2*d:
                        raise AssertionError("too many true original line C4 3matching cofactor completions per POINT C4")
                    count["maximum_true_original_line_extensions_per_FIXED_point_C4"] = max(
                        count["maximum_true_original_line_extensions_per_FIXED_point_C4"],
                        successful_line_completions)
                if extendible+rejected!=mark_weight:
                    raise AssertionError("light genuine original full C4 point-line cofactor mass partition invalid")
                count["light_genuine_original_cofactor_extendible_mark_E"]+=extendible
                count["light_genuine_original_Hall_cofactor_defect_D"]+=rejected
                if witness_ratio is None or extendible*100 > witness_ratio[0]*mark_weight:
                    witness_ratio=(extendible,mark_weight,p,l,i,j)
    T=count["light_completed_source_C4_pair_mark_T"]
    E=count["light_genuine_original_cofactor_extendible_mark_E"]
    D=count["light_genuine_original_Hall_cofactor_defect_D"]
    if D+E!=T or sum(credits.values())!=12*D:
        raise AssertionError("true original light C4 source cofactor and four-vacancy partition violated")
    if max_triples_per_side is None and actual_min_line is not None:
        m=(a-5)//2+1
        if actual_min_line<m or actual_min_point<m:
            raise AssertionError("light original true source pair does not have global hole-guaranteed C4 extensions")
        if E*m>2*d*T:
            raise AssertionError("original line-degree marked-cofactor sparsity theorem false")
    return {
        "s":s,"V":V,"a":a,"d":d,
        "min_full_occupied_C4_extension_per_light_spoke":(a-5)//2+1,
        "actual_min_POINT_C4_completions_per_light_original_spoke":actual_min_point,
        "actual_min_LINE_C4_completions_per_light_original_spoke":actual_min_line,
        "light_original_anchor_crossflag_count":
            count["light_original_anchor_crossflags_with_two_occupied_C4_witnesses"],
        "light_original_occupied_C4_pair_mark_mass_T":T,
        "light_original_2x2_cofactor_extendible_mark_mass_E":E,
        "light_original_2x2_cofactor_Hall_defect_mark_mass_D":D,
        "max_actual_original_line_ext_per_one_POINT_C4":
            count["maximum_true_original_line_extensions_per_FIXED_point_C4"],
        "actual_SOURCE_point_heavy_physical_coordinates":hp["heavy_physical_coordinates"],
        "actual_SOURCE_line_heavy_physical_coordinates":hl["heavy_physical_coordinates"],
        "light_source_four_vacancy_Hall_credits_in_twelfths":dict(credits),
        "first_genuine_light_crossflag":first_light,
        "first_true_original_light_rejected_3matching_cofactor":first_rejected,
        "source_not_GF5_historical_positive":True,
        "is_explicitly_PARTIAL_if_capped":max_triples_per_side is not None,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
