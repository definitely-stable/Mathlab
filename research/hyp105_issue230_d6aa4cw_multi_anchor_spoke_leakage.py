"""AA4-CW: uniformly many genuine GQ NONINCIDENT anchors escape one CV zero mechanism.

For arbitrary complete correlated global typed pair embeddings f,g into
the MINIMAL physical K_a, and EVERY pair of k=floor(a/2) physical cuts,
there are > s^(9/2)/4096 nonincident original source (p,l) anchors
whose RAW in-cut physical spoke-source factor neighborhoods contain
at least one TRUE original incidence (h>=24).

This *only* defeats a 2x2 completely incidence-free spoke-rectangle
obstruction simultaneously at all anchors. It does not certify
disjointness from the doubled images f(q),g(l0), occupied C4 centers,
a 3x3 matching/permanent, historical GF5-positive Q, or sevenclass S.
"""
from math import comb, isqrt
from hyp105_issue230_d6aa4cq_original_macro_path_cut_gate import _validated_original


def minimal_a(V):
    if type(V) is not int or V < 1:
        raise ValueError("positive original source factor count")
    a=(1+isqrt(1+8*V))//2
    while comb(a,2)<V:a+=1
    while a>2 and comb(a-1,2)>=V:a-=1
    return a


def exact_dyadic_cut_leakage_arithmetic(h):
    """Integer-only falsifier for an analytically proved ALL h>=24 theorem."""
    if type(h) is not int or h<1:
        raise ValueError("dyadic original h>=1 required")
    s=1<<h
    V=(s+1)*(s*s+1)
    d=s+1
    a=minimal_a(V)
    k=a//2
    H=comb(a,2)-V
    m=comb(k,2)-H
    if not (comb(a-1,2)<V<=comb(a,2) and 0<=H<=a-2):
        raise AssertionError("minimal original physical alphabet invalid")
    if h>=24:
        # H can concentrate adversarially at physical coordinate vertices.
        # At most 8H original pair-images in a cut touch vertices of
        # missing-degree >= k/4. No individual image is assumed typical.
        if not (k>=8 and m*8>=V and V>=128*(a-2)
                and d*d>=2048*s and k>=2048*d
                and k*k >= 0):
            raise AssertionError("all-h CW source/physical/spectral gate invalid")
        # Necessary to infer V*k/2048 > s^(9/2)/4096.
        if not (4*k*k > s*s*s):
            raise AssertionError("uniform source anchor exponent 9/2 not justified")
    return {"h":h,"s":s,"V":V,"a":a,"k":k,"H":H,"m":m,
            "d":d,"halfcut_good_source_lower":V//16,
            "allh_nonincident_raw_spoke_positive_lower_numerator":V*k,
            "allh_nonincident_raw_spoke_positive_lower_denominator":2048,
            "allh_gate_h_ge_24":h>=24,
            "NOT_a_GF5_accepted_matching":True,
            "root_230":"OPEN_WITH_FORMAL_BLOCKER"}


def _cut_factors(labels, cut):
    X=frozenset(cut)
    return tuple(i for i,e in enumerate(labels) if set(e)<=X)


def _physical_spoke_neighborhoods(labels, source_ids):
    """Use ONE unchanged complete original embedding; no per-P3 redraw."""
    edge_sets={i:frozenset(labels[i]) for i in source_ids}
    reverse={}
    for i,e in edge_sets.items():
        for vertex in e:
            reverse.setdefault(vertex,[]).append(i)
    return {i:frozenset(set(reverse[e0])|set(reverse[e1]))-{i}
            for i,(e0,e1) in ((i,tuple(e)) for i,e in edge_sets.items())}


def original_cut_spoke_leakage_certificate(model, X=None, Y=None):
    """Full TRUE original GQ source-spoke C(p,l) on EVERY cut anchor.

    C(p,l) counts TRUE original incidence IDs (i,j) with i different
    from p, f(i) touching f(p), both inside X; j different from l,
    g(j) touching g(l), both inside Y. Does NOT use q,l0 C4 gates.
    """
    s,V,a,f,g,pl,lp=_validated_original(model)
    k=a//2
    X=tuple(range(k)) if X is None else tuple(X)
    Y=tuple(range(a-k,a)) if Y is None else tuple(Y)
    for cut in (X,Y):
        if (len(cut)!=k or len(set(cut))!=k or any(
                type(v) is not int or not 0<=v<a for v in cut)):
            raise ValueError("exact k coordinate cut with no duplicates required")
    P=_cut_factors(f,X)
    L=_cut_factors(g,Y)
    Pset,Lset=set(P),set(L)
    pf=_physical_spoke_neighborhoods(f,P)
    lg=_physical_spoke_neighborhoods(g,L)
    if any(len(ns)>2*(k-2) for ns in list(pf.values())+list(lg.values())):
        raise AssertionError("physical pair-line graph overlap degree cap violated")
    # Independent missing-coordinate graph hole calculation for each typed map.
    def heavy_and_good(labels,source,cut):
        occupied=frozenset(labels)
        missing=tuple(edge for edge in __import__("itertools").combinations(range(a),2)
                      if edge not in occupied)
        if len(missing)!=comb(a,2)-V:
            raise AssertionError("globally typed image not minimally occupied")
        physical_holes=[0]*a
        for u,v in missing:
            physical_holes[u]+=1
            physical_holes[v]+=1
        heavy=frozenset(u for u in cut if 4*physical_holes[u]>=k)
        excluded=tuple(i for i in source if set(labels[i])&heavy)
        good=tuple(i for i in source if not set(labels[i])&heavy)
        if len(excluded)>8*len(missing):
            raise AssertionError("heavy vertex occupied-original-factor charging false")
        # every good factor i has at least k distinct physical overlapping
        # in-cut images (NOT necessarily valid physical C4 completions).
        neighbors=pf if labels is f else lg
        if k>=8 and any(len(neighbors[i])<k for i in good):
            raise AssertionError("all source typed good cut spoke-degree lower false")
        return heavy,good,excluded
    heavy_p,I,excluded_p=heavy_and_good(f,P,X)
    heavy_l,J,excluded_l=heavy_and_good(g,L,Y)
    Jset=set(J)
    original_good_flags=sum(len(pl[i]&Jset) for i in I)
    all_source_flag_mass=0
    nonincident_positive=0
    any_positive=0
    incident_anchors=0
    nonincident_anchors=0
    maxC=0
    # Independently tally C(p,l) by original POINT spoke incidence path.
    # All h>=24 mathematical theorem is symbolic; actual GQ finite oracle
    # limited by external fixture sizes W32/W34/W38.
    for p in P:
        intermediate={}
        for i in pf[p]:
            for j in pl[i]:
                if j in Lset:
                    intermediate[j]=intermediate.get(j,0)+1
        for l in L:
            c=sum(intermediate.get(j,0) for j in lg[l])
            all_source_flag_mass+=c
            maxC=max(maxC,c)
            any_positive+=c>0
            if l in pl[p]:
                incident_anchors+=1
            else:
                nonincident_anchors+=1
                nonincident_positive+=c>0
    # Independent SOURCE-flag-first double count: each real original
    # (i,j) contributes degree_X(i)*degree_Y(j) anchor pairs.
    degree_f={i:len(pf[i]) for i in P}
    degree_g={j:len(lg[j]) for j in L}
    independent_mass=sum(degree_f[i]*degree_g[j]
                         for i in P for j in pl[i] if j in Lset)
    if all_source_flag_mass!=independent_mass:
        raise AssertionError("original point-first and flag-first spoke mass differ")
    if maxC>2*(k-2)*(s+1):
        raise AssertionError("original GQ degree source-C peak cap violated")
    if nonincident_anchors+incident_anchors!=len(P)*len(L):
        raise AssertionError("all original cut source point-line anchors omitted")
    if s>=1<<24:
        z=exact_dyadic_cut_leakage_arithmetic(s.bit_length()-1)
        if len(I)*16<V or len(J)*16<V:
            raise AssertionError("all-h strong good-cut source supply fails")
        if original_good_flags*512<(s+1)*V:
            raise AssertionError("original GQ mixing lower, genuine incidence flags")
        if all_source_flag_mass*512 < k*k*(s+1)*V:
            raise AssertionError("all-h GQ weighted cut leakage source bound false")
        if 2048*nonincident_positive<V*k:
            raise AssertionError("all-h many NONINCIDENT source spoke escape fails")
        if 4096**2*nonincident_positive**2 <= s**9:
            raise AssertionError("original s^4.5 positive raw spoke anchors false")
    return {
        "s":s,"V":V,"a":a,"k":k,"X":X,"Y":Y,
        "real_original_point_cut_source_factors":len(P),
        "real_original_line_cut_source_factors":len(L),
        "source_original_nonincident_P3_anchors":nonincident_anchors,
        "source_original_incident_pairs":incident_anchors,
        "true_original_flag_mass_through_incut_physical_spokes":all_source_flag_mass,
        "independent_flag_first_source_mass":independent_mass,
        "max_original_spoke_cross_incidence_at_one_anchor":maxC,
        "positive_spoke_anchors_including_incident":any_positive,
        "positive_spoke_NONINCIDENT_P3_anchors":nonincident_positive,
        "original_heavy_vertices_on_POINT_cut":len(heavy_p),
        "original_heavy_vertices_on_LINE_cut":len(heavy_l),
        "original_point_factors_removed_for_heavy":len(excluded_p),
        "original_line_factors_removed_for_heavy":len(excluded_l),
        "original_actual_good_source_flags":original_good_flags,
        "not_the_doubled_factor_avoiding_C4_completion":True,
        "does_NOT_imply_matching_or_GF5":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER"}
