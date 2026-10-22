"""AA4-CV: all-h adversarial original-GQ complete maps with ZERO local BBo energy.

For EVERY genuine W(3,2^h) h>=4 and EVERY chosen true original
nonincident point/line anchor p,l, construct ONE complete globally
injected typed f,g into the minimal physical K_a with:
  * f(p)=g(l)=(0,1), f(q)=g(l0)=(2,3) (q,l0 on unique true P3);
  * EVERY possible N=(a-4)(a-5) original C4 completion occupied
    on both sides, even though each injection omits H<=a-2 labels;
  * NO true original incidence between ANY source factor mapped to
    physical spokes (0,z)/(1,z) on the two sides.
Thus all N*N genuine 3x3 original minors/permanents vanish.
This is an all-h *single-anchor proof-method no-go*, not Branch B
or a bound on full sevenclass S and not even a whole-cut BBo no-go.
"""
from itertools import combinations
from math import comb, isqrt

from hyp105_issue230_d6aa4cr_exact_BBo_three_matching_transfer import original_nonincident_threepath


def minimal_physical_alphabet(V):
    if type(V) is not int or V < 1:
        raise ValueError("positive original factor count required")
    a=(1+isqrt(1+8*V))//2
    while comb(a,2)<V:
        a+=1
    while a>2 and comb(a-1,2)>=V:
        a-=1
    return a


def allh_zero_spoke_arithmetic(h):
    """Exact finite falsifier of an independently proved symbolic h>=4 theorem."""
    if type(h) is not int or h<1:
        raise ValueError("dyadic integer h >=1 required")
    s=1<<h
    V=(s+1)*(s*s+1)
    a=minimal_physical_alphabet(V)
    H=comb(a,2)-V
    t=2*(a-4)
    n=a-4
    N=n*(n-1)
    source_spoke_capacity=V-t*(s+1)-2
    if h>=4:
        if not (a>=6 and H<=2*n and source_spoke_capacity>=t and
                a-2<3*s**1.5/2):
            raise AssertionError("all-h constructive adversarial source spoke budget failed")
    return {"h":h,"s":s,"V":V,"a":a,"H":H,
            "spoke_source_factors_per_side":t,
            "C4_completions_each_side":N,
            "physically_occupied_completion_pairs":N*N,
            "spoke_source_capacity_after_line_neighborhood":source_spoke_capacity,
            "constructive_local_zero_thm_all_h_ge_4":h>=4,
            "root_230":"OPEN_WITH_FORMAL_BLOCKER"}


def complete_zero_anchor_source_pairmaps(s, point_lines, line_points, p, l):
    """Construct complete legal *typed* injective maps for a REAL original GQ.

    Caller must supply original incidence adjacency of genuine W(3,s).
    Proves all positive statements from source incidence only; neither
    random f/g nor independence of factor/source labels is invoked.
    Supports h>=4, where the closed-form budget always holds.
    """
    if type(s) is not int or s<16 or s&(s-1):
        raise ValueError("original dyadic s>=16 required")
    params=allh_zero_spoke_arithmetic(s.bit_length()-1)
    V,a,H,t=params["V"],params["a"],params["H"],params["spoke_source_factors_per_side"]
    if len(point_lines)!=V or len(line_points)!=V:
        raise ValueError("complete genuine original point/line factor arrays required")
    pl=tuple(frozenset(row) for row in point_lines)
    lp=tuple(frozenset(row) for row in line_points)
    if not(type(p) is int and type(l) is int and 0<=p<V and 0<=l<V and l not in pl[p]):
        raise ValueError("genuine source nonincident anchor required")
    if (any(len(row)!=s+1 for row in pl) or
            any(len(row)!=s+1 for row in lp)):
        raise ValueError("all original source factors must have GQ degree s+1")
    original_path=original_nonincident_threepath(p,l,pl,lp)
    q,l0=original_path[1][0],original_path[0][1]
    if (p==q or l==l0):
        raise AssertionError("source nonincident path must have distinct factors")

    # Choose t REAL original LINE factors outside the anchor path.
    spoke_lines=tuple(j for j in range(V) if j not in (l,l0))[:t]
    if len(spoke_lines)!=t:
        raise AssertionError("line factor spoke budget failed")
    # Exclude the entire TRUE original GQ neighborhood of these lines.
    excluded={p,q}
    for line_id in spoke_lines:
        excluded.update(lp[line_id])
    spoke_points=tuple(i for i in range(V) if i not in excluded)[:t]
    if len(spoke_points)!=t:
        raise AssertionError("actual original POINT spoke factors insufficient")
    if any(x in pl[i] for i in spoke_points for x in spoke_lines):
        raise AssertionError("actual source spoke POINT×LINE incidence free property false")

    z=range(4,a)
    physical_spokes=tuple((u,j) for u in (0,1) for j in z)
    physical_centers=tuple(combinations(range(4,a),2))
    # Deliberately OMIT ONLY edges involving doubled physical endpoint 2 or3;
    # no physical C4 template uses any of these edges.
    unprotected=tuple((u,j) for u in (2,3) for j in z)
    if H>len(unprotected):
        raise AssertionError("insufficient removable physical pair labels")
    holes=frozenset(unprotected[:H])
    occupied=tuple(e for e in combinations(range(a),2) if e not in holes)
    if len(occupied)!=V or len(physical_spokes)!=t:
        raise AssertionError("physical occupancy/injection budget invalid")
    occupied_set=set(occupied)
    if not ({(0,1),(2,3)}|set(physical_spokes)).issubset(occupied_set):
        raise AssertionError("actual anchor/spoke physical images removed")
    if any(e not in occupied_set for e in combinations(range(4,a),2)):
        raise AssertionError("any missing middle edge destroys maximum physical C4")

    def inject(single, double, spoke_ids):
        assigned={single:(0,1),double:(2,3)}
        for source_id,physical_edge in zip(spoke_ids, physical_spokes):
            if source_id in assigned:
                raise AssertionError("true original source spoke collided with anchor")
            assigned[source_id]=physical_edge
        used=set(assigned.values())
        rest=iter(e for e in occupied if e not in used)
        labels=tuple(assigned[i] if i in assigned else next(rest) for i in range(V))
        if len(set(labels))!=V or set(labels)!=occupied_set:
            raise AssertionError("full original typed source injection invalid")
        return labels

    f=inject(p,q,spoke_points)
    g=inject(l,l0,spoke_lines)
    return {"s":s,"V":V,"a":a,"H":H,
            "anchor":(p,l),"true_original_source_P3":original_path,
            "point_labels":f,"line_labels":g,
            "source_POINT_spokes":spoke_points,
            "source_LINE_spokes":spoke_lines,
            "physical_spokes":physical_spokes,
            "hole_edges":tuple(sorted(holes)),
            "all_physical_C4_completions_per_side":params["C4_completions_each_side"],
            "all_physical_C4_pairs":params["physically_occupied_completion_pairs"],
            "all_true_original_3x3_permanents_zero_PROVED_BY_CROSS_NONINCIDENCE":True,
            "local_only_no_global_S_conclusion":True,
            "root_230":"OPEN_WITH_FORMAL_BLOCKER"}


def verify_combinatorial_zero_without_enumerating_quartic_pairs(w, point_lines):
    """Independent SOURCE incidence witness: every 3x3 matching needs spoke×spoke."""
    s,V,a=w["s"],w["V"],w["a"]
    p,l=w["anchor"]
    path=w["true_original_source_P3"]
    q,l0=path[1][0],path[0][1]
    f,g=w["point_labels"],w["line_labels"]
    assert f[p]==g[l]==(0,1) and f[q]==g[l0]==(2,3)
    f_inv={e:i for i,e in enumerate(f)}
    g_inv={e:i for i,e in enumerate(g)}
    physical_centers=tuple(combinations(range(4,a),2))
    for z in range(4,a):
        for u in (0,1):
            edge=(u,z)
            assert f_inv[edge] in w["source_POINT_spokes"]
            assert g_inv[edge] in w["source_LINE_spokes"]
    assert all(edge in f_inv and edge in g_inv for edge in physical_centers)
    assert all(line not in point_lines[point] for point in w["source_POINT_spokes"]
               for line in w["source_LINE_spokes"])
    N=(a-4)*(a-5)
    assert N==w["all_physical_C4_completions_per_side"]
    return {"s":s,"a":a,"true_nonincident_source_anchor":(p,l),
            "point_spoke_count":len(w["source_POINT_spokes"]),
            "line_spoke_count":len(w["source_LINE_spokes"]),
            "physical_completions_each_side":N,
            "all_physical_pairs_with_zero_true_source_permanent":N*N,
            "root_230":"OPEN_WITH_FORMAL_BLOCKER"}
