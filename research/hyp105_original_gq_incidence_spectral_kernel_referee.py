"""AA4-GQSPECTRAL — independent true ORIGINAL W(3,s) incidence spectrum
and exact ORIGINAL pencil collision book spectral KERNEL-SLACK identity.

ALL-h mathematics (proved in accompanying document from the generalized
quadrangle axiom), without assuming the published source spectral input:

  A^2=(s^2-1)I-2A+(s+1)J,
  BB^T=(s+1)I+A,
  spec(BB^T)={(s+1)^2,2s,0}, multiplicities 1,
      s(s+1)^2/2, s(s^2+1)/2.

For ANY separately globally injected ORIGINAL factor-to-K_a-pair map,
star populations k_y and FULL source pencil return r_zy,

 M_exact=(s-1)V+(s^2+1)/(2V)*sum_y k_y^2
          -s*sum_y ||P_ker 1_{L_y}||^2;

 C_s-M_exact=(s^2+1)/(2V)*sum_y k_y*(a-1-k_y)
             +s*sum_y ||P_ker 1_{L_y}||^2.

For minimal a, t=binom(a,2)-V missing coordinate pair labels satisfies
  sum k_y*(a-1-k_y) >= 2*t*(a-1-t).
Thus a new strictly improved UNIFORM FULL original collision book upper
when t>0; no f,g independence or fake physical source edges.

The finite oracle reconstructs ONLY genuine original W(3,2)/W(3,4)
geometry and verifies all exact integer/Fraction identities independently.
No previous source spectral, book, conflict or selector modules imported.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb,isqrt

from hyp105_full_physical_degree_tail import genuine_source


def minimum_alphabet(V):
    if type(V) is not int or V<1:
        raise ValueError("positive original factor cardinality required")
    a=max(2,(1+isqrt(1+8*V))//2)
    while comb(a,2)<V:a+=1
    while a>2 and comb(a-1,2)>=V:a-=1
    return a


def allh_original_GQ_spectrum_parameters(s):
    """Pure exact integer identity from axioms, NOT finite-spectrum fitting."""
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("true symplectic source s=2^h>=2 required")
    V=(s+1)*(s*s+1)
    d=s+1
    k=s*(s+1)
    lam=s-1
    mu=s+1
    f=s*(s+1)**2//2
    g=s*(s*s+1)//2
    top=(s+1)**2
    middle=2*s
    if (1+f+g!=V or k+f*(s-1)-g*(s+1)!=0 or
        k*(k-lam-1)!=(V-k-1)*mu or
        top+middle*f!=V*d or
        top*top+middle*middle*f!=V*d*d+V*k):
        raise AssertionError("true GQ strongly regular spectrum multiplicities fail")
    return {
        "s":s,"V":V,"flags":V*d,
        "GQ_point_degree":d,
        "collinearity_degree":k,
        "collinearity_lambda":lam,"collinearity_mu":mu,
        "collinearity_r":s-1,"collinearity_t":-s-1,
        "collinearity_r_mult":f,"collinearity_t_mult":g,
        "incidence_BBt_nonzero_eigenvalues":(top,middle),
        "incidence_BBt_multiplicities":(1,f,g),
        "source_spectral_positive_semidefinite":True,
        "kernel_dimension":g,
    }


def _original_incidence_geometry(power):
    if type(power) is not int or power not in (1,2):
        raise ValueError("only genuine original W32/W34 finite oracle")
    s,V,flags=genuine_source(power)
    point_to_lines=[set() for _ in range(V)]
    line_to_points=[set() for _ in range(V)]
    seen=set()
    for p,l in flags:
        if (p,l) in seen:raise AssertionError("duplicate ORIGINAL incidence flag ID")
        seen.add((p,l));point_to_lines[p].add(l);line_to_points[l].add(p)
    if (len(flags)!=V*(s+1) or
        any(len(z)!=s+1 for z in point_to_lines+line_to_points)):
        raise AssertionError("genuine GQ regular pencils invalid")
    pcol=[set().union(*(line_to_points[l] for l in point_to_lines[p]))-{p}
          for p in range(V)]
    lcol=[set().union(*(point_to_lines[p] for p in line_to_points[l]))-{l}
          for l in range(V)]
    # INDEPENDENT all-pairs strong regular EXACT combinatorial GQ axiom.
    for adjacency in (pcol,lcol):
        for i in range(V):
            if len(adjacency[i])!=s*(s+1):
                raise AssertionError("true original GQ collinearity valency mismatch")
            for j in range(V):
                joint=len(adjacency[i]&adjacency[j])
                expected=(s*(s+1) if i==j else
                          (s-1 if j in adjacency[i] else s+1))
                if joint!=expected:
                    raise AssertionError("GQ strongly regular A^2 identity violated")
    # Independent ORIGINAL GQ projection axiom, not assumed by spectral.
    for p in range(V):
        for l in range(V):
            if l not in point_to_lines[p]:
                if len(pcol[p]&line_to_points[l])!=1:
                    raise AssertionError("true original W3s unique projection fails")
    return s,V,tuple(flags),point_to_lines,line_to_points,pcol,lcol


def _labels(V, raw):
    a=minimum_alphabet(V)
    legal=set(combinations(range(a),2))
    try:
        labels=tuple(tuple(p) for p in raw)
    except (TypeError,ValueError):
        raise ValueError("invalid complete typed original pair labels")
    if len(labels)!=V or len(set(labels))!=V or any(p not in legal for p in labels):
        raise ValueError("complete globally injected ORIGINAL factor pair map required")
    return a,labels


def _one_original_full_book(s,V,source_neighbors,labels,a):
    """Exact independent spectral polynomial projector and two book oracles.

    source_neighbors: for each ORIGINAL opposite factor i, set of factor
    neighbors incident to it (lines through p, or points on ell).
    B has rows opposite factors, columns assigned factor labels.
    """
    if (len(source_neighbors)!=V or
        any(len(ns)!=s+1 for ns in source_neighbors)):
        raise AssertionError("original incidence geometry invalid")
    factor_to_opp=[set() for _ in range(V)]
    for opp,neighbors in enumerate(source_neighbors):
        for fac in neighbors:factor_to_opp[fac].add(opp)
    if any(len(z)!=s+1 for z in factor_to_opp):
        raise AssertionError("dual original regularity invalid")
    label_stars=tuple(tuple(i for i,pair in enumerate(labels) if y in pair)
                      for y in range(a))
    d=(s+1)**2
    u=2*s
    null_mass=Fraction()
    squared_stars=0
    source_pencil_book=0
    per_star=[]
    for y,star in enumerate(label_stars):
        starset=set(star)
        k=len(star)
        if k>a-1:raise AssertionError("globally injected pair labels share >a-1 star")
        # The source incidence map B*1_{L_y}: ORIGINAL opposite-pencil populations.
        r=[len(ns&starset) for ns in source_neighbors]
        dot=sum(t*t for t in r)
        source_pencil_book+=sum(comb(t,2) for t in r)
        if sum(r)!=(s+1)*k:
            raise AssertionError("true full ORIGINAL point/line star first moment")
        # Qv=B^T B v on ORIGINAL labeled factors, computed via incidence.
        qv=[sum(r[p] for p in factor_to_opp[i]) for i in range(V)]
        if sum(qv[i] for i in star)!=dot:
            raise AssertionError("independent incidence quadratic form mismatch")
        # Q^2v=B^TB Qv; required for exact kernel spectral projector.
        qv_opp=[sum(qv[i] for i in ns) for ns in source_neighbors]
        q2v=[sum(qv_opp[p] for p in factor_to_opp[i]) for i in range(V)]
        p0v=[Fraction(q2v[i]-(d+u)*qv[i]+d*u*int(i in starset),d*u)
              for i in range(V)]
        # Q P_ker=0: assert actual source-kernel, not just a numeric eigenvalue.
        if any(sum(p0v[i] for i in ns)!=0 for ns in source_neighbors):
            raise AssertionError("independent original incidence kernel projector not annihilated")
        mass=sum((p0v[i] for i in star),Fraction())
        if mass!=sum((v*v for v in p0v),Fraction()) or mass<0:
            raise AssertionError("source projector not positive orthogonal idempotent")
        # qv^T qv=v^T Q^2 v, independent spectral identity.
        mass_poly=Fraction(
            sum(t*t for t in qv)-(d+u)*dot+d*u*k,d*u)
        if mass_poly!=mass:
            raise AssertionError("source polynomial spectral slack mismatch")
        upper=Fraction(2*s*k)+Fraction(s*s+1,V)*k*k
        if Fraction(dot)!=upper-2*s*mass:
            raise AssertionError("all-h source incidence Rayleigh spectral decomposition wrong")
        null_mass+=mass
        squared_stars+=k*k
        per_star.append((y,k,mass))
    if sum(len(star) for star in label_stars)!=2*V:
        raise AssertionError("true full global original map uses exactly two coordinates")
    # SECOND genuinely different book oracle: unordered original factor
    # pairs that have both source concurrence and pair-label collision.
    pairmajor=0
    for i,j in combinations(range(V),2):
        if set(labels[i])&set(labels[j]) and factor_to_opp[i]&factor_to_opp[j]:
            if len(factor_to_opp[i]&factor_to_opp[j])!=1:
                raise AssertionError("original source concurrence not unique")
            pairmajor+=1
    if pairmajor!=source_pencil_book:
        raise AssertionError("full ORIGINAL pencil-first book != independent pair-major book")
    M=source_pencil_book
    base=Fraction((s-1)*V)+Fraction(s*s+1,2*V)*squared_stars
    C=(s*s+1)*(s*s+a-2)
    slot_def=sum(k*(a-1-k) for _,k,_ in per_star)
    true_slack=Fraction(s*s+1,2*V)*slot_def+s*null_mass
    missing=comb(a,2)-V
    if (base-s*null_mass!=M or Fraction(C-M)!=true_slack or
        slot_def!=2*V*(a-1)-squared_stars or
        slot_def<2*missing*(a-1-missing) or
        M<0 or M>C):
        raise AssertionError("exact source spectral kernel+unused-pair budget identity invalid")
    return {
        "original_full_book_actual_M":M,
        "original_full_book_pair_major_M":pairmajor,
        "spectral_base_before_kernel":base,
        "spectral_kernel_mass":null_mass,
        "label_star_squares":squared_stars,
        "missing_legal_pair_labels":missing,
        "unused_pair_star_defect":slot_def,
        "algebraic_Cs":C,
        "Cs_minus_actual_M_exact":C-M,
        "Cs_minus_actual_spectral_identity":
            Fraction(s*s+1,2*V)*slot_def+s*null_mass,
        "universal_unused_pairs_extra_gap":
            Fraction((s*s+1)*missing*(a-1-missing),V),
        "strict_extra_gap_if_missing":missing>0,
        "individual_coordinate_stars":tuple(per_star),
        "all_source_projectors_are_exact_original_kernel_projections":True,
    }


def genuine_original_dual_spectral_book_referee(power,f,g,core_ids=None):
    """Independently audit the full ORIGINAL point/line books and subset.

    Original source FIRST: original incidence IDs. For each side, verify
    pencil-first and factor-pair-major counts; exact spectral projector
    polynomial; source conflicts restricted to ANY ORIGINAL flag CORE.
    """
    s,V,flags,pencils,linepoints,pcol,lcol=_original_incidence_geometry(power)
    a,f=_labels(V,f)
    b,g=_labels(V,g)
    if a!=b:raise AssertionError("true original typed alphabet mismatch")
    lines=_one_original_full_book(s,V,pencils,g,a)
    points=_one_original_full_book(s,V,linepoints,f,a)
    selected=tuple(range(len(flags))) if core_ids is None else tuple(core_ids)
    if (len(set(selected))!=len(selected)
        or any(type(i) is not int or i<0 or i>=len(flags) for i in selected)):
        raise ValueError("CORE must contain distinct genuine ORIGINAL incidence IDs")
    m_f=m_g=0
    for i,j in combinations(selected,2):
        p,ell=flags[i];q,m=flags[j]
        point_conf=(p==q and bool(set(g[ell])&set(g[m])))
        line_conf=(ell==m and bool(set(f[p])&set(f[q])))
        if point_conf and line_conf:
            raise AssertionError("two distinct original source ID share original factor pair")
        m_g+=point_conf;m_f+=line_conf
    if (m_g>lines["original_full_book_actual_M"] or
        m_f>points["original_full_book_actual_M"]):
        raise AssertionError("CORE conflict exceeds original FULL pencil book")
    spectrum=allh_original_GQ_spectrum_parameters(s)
    return {
        "s":s,"V":V,"minimal_alphabet_a":a,
        "original_full_flag_ID_count":len(flags),
        "original_CORE_flag_ID_count":len(selected),
        "true_original_GQ_srg_axioms_independently_verified":True,
        "source_incidence_spectrum":spectrum,
        "right_g_line_factor_point_pencil_book":lines,
        "left_f_point_factor_line_pencil_book":points,
        "restricted_original_source_pencil_conflicts_Mg":m_g,
        "restricted_original_source_pencil_conflicts_Mf":m_f,
        "restricted_original_SOURCE_conflict_edges":m_g+m_f,
        "all_source_label_maps_are_fixed_and_may_be_correlated":True,
    }
