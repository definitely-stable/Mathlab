"""HYP-105 E1-K3-D: mixed-coordinate GQ compatibility / girth-eight certificates.

One GLOBAL original point-pair injection f and line-pair injection g is used.
For two Kikuchi vertices with both coordinates different, their common
neighbors form a simple bipartite compatibility graph H. H is a subgraph of
the ORIGINAL W(3,s) incidence graph, so it has no C4 and no C6.

This module proves/checks exact local capacities and a very coarse all-h
aggregate book upper. It does NOT prove the seven-family Omega(s^6)
obstruction, a usable uniform mixed book saving, or any ASET exponent.
"""
from collections import Counter
from math import comb, isqrt
import json

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model, kikuchi_graph
from hyp105_g5e2b3e1k3_local_collisions import star_degree_tensor
from hyp105_g5e2b3e1k3c_book_packing import book_moments


def _choose2(n):
    return n * (n - 1) // 2


def _choose3(n):
    return n * (n - 1) * (n - 2) // 6 if n >= 3 else 0


def c4_free_edge_cap(r):
    """Largest integer m allowed by m*(m-r) <= r^2*(r-1)."""
    if type(r) is not int or r < 1:
        raise ValueError("positive integer side capacity required")
    discriminant = r * r * (4 * r - 3)
    bound = (r + isqrt(discriminant)) // 2
    if bound * (bound - r) > r * r * (r - 1):
        raise AssertionError("C4-free capacity rounding invalid")
    return bound


def girth8_moore_edge_cap(r):
    """Rigorous all-graph C4/C6-free bipartite Moore-cap, integer only.

    Let H have two sides of size r and m edges, girth>=8. When average
    degree m/r >=3, K1's all-graph NB3 bound with degree<=1 peeling
    yields 2*m*(m/r-1)^2 <= NB3(H). Every oriented 3-path uses an
    opposite-side nonedge and is unique, so NB3(H)<=2*(r*r-m).
    Thus m*((m-r)^2+r^2)<=r^4 in the >=3 regime. In the other
    regime m<=3*r-1. No inequality for the low-degree regime is
    silently assumed. The combined cap is max(3r-1, integer root),
    also capped by the r*r available edges.
    """
    if type(r) is not int or r < 1:
        raise ValueError("positive integer side capacity required")
    lo, hi = 0, r*r+1
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid*((mid-r)**2+r*r)<=r**4:
            lo=mid
        else:
            hi=mid
    return min(r*r,max(3*r-1,lo))


def source_inverses(model):
    """Physical pair inverses; zero for absent host pair labels."""
    if type(model.get("a")) is not int or type(model.get("s")) is not int:
        raise ValueError("physical alphabet and GQ order required")
    points = {tuple(sorted(p)): i for i, p in enumerate(model["left_labels"])}
    lines = {tuple(sorted(e)): j for j, e in enumerate(model["right_labels"])}
    if len(points) != len(model["left_labels"]) or len(lines) != len(model["right_labels"]):
        raise ValueError("globally injective point/line labels required")
    return points, lines, frozenset(model["incidences"])


def mixed_compatibility(model, u, v, inverses=None):
    """Construct exact mixed common-neighbor graph H from ORIGINAL I(p,l).

    H left vertices z not in {x,x'}, right vertices t not in {y,y'}.
    Edge (z,t) iff I(F_xz,G_yt)*I(F_x'z,G_y't) = 1. This fixes
    one coherent pair f,g; no motifwise relabeling or independence.
    """
    a, s = model["a"], model["s"]
    if (type(u) is not int or type(v) is not int or
            not 0 <= u < a * a or not 0 <= v < a * a or u == v):
        raise ValueError("two distinct valid Kikuchi vertices required")
    x, y = divmod(u, a)
    xx, yy = divmod(v, a)
    if x == xx or y == yy:
        raise ValueError("only mixed-coordinate vertex pairs supported")
    points, lines, incidence = source_inverses(model) if inverses is None else inverses
    r = a - 2
    remaining_z = tuple(z for z in range(a) if z != x and z != xx)
    remaining_t = tuple(t for t in range(a) if t != y and t != yy)
    rows = {}
    counts_t = Counter()
    for z in remaining_z:
        p = points.get((min(x,z),max(x,z)))
        pp = points.get((min(xx,z),max(xx,z)))
        neighbors = set()
        if p is not None and pp is not None:
            for t in remaining_t:
                l = lines.get((min(y,t),max(y,t)))
                ll = lines.get((min(yy,t),max(yy,t)))
                if (l is not None and ll is not None and
                        (p,l) in incidence and (pp,ll) in incidence):
                    neighbors.add(t)
                    counts_t[t] += 1
        rows[z] = frozenset(neighbors)
    m = sum(map(len, rows.values()))
    left_degree = tuple(len(rows[z]) for z in remaining_z)
    right_degree = tuple(counts_t[t] for t in remaining_t)
    max_degree = max((*left_degree,*right_degree))
    if max_degree > s+1:
        raise AssertionError("source incidence degree exceeds s+1")
    # A C4 would be a pair of original points sharing TWO GQ lines.
    for za, zb in __import__("itertools").combinations(remaining_z, 2):
        if len(rows[za] & rows[zb]) > 1:
            raise AssertionError("GQ original incidence C4 violation")
    left_wedges = sum(_choose2(d) for d in left_degree)
    right_wedges = sum(_choose2(d) for d in right_degree)
    if left_wedges > _choose2(r) or right_wedges > _choose2(r):
        raise AssertionError("C4-free opposite side pair packing violation")
    if m * (m-r) > r*r*(r-1):
        raise AssertionError("C4-free Jensen bound violation")
    c4_cap = c4_free_edge_cap(r)
    moore_cap = girth8_moore_edge_cap(r)
    if m > min(c4_cap,moore_cap):
        raise AssertionError("girth-eight integer edge cap violation")
    # Number of oriented nonbacktracking 3-paths left->right. With no
    # C4 they never connect adjacent endpoints. With no C6 there is
    # at most one for any (left,right) pair.
    paths3 = sum((len(rows[z])-1)*(counts_t[t]-1)
                 for z in remaining_z for t in rows[z])
    if paths3 > r*r-m:
        raise AssertionError("GQ girth-eight 3-path injection violation")
    return {
        "u":u,"v":v,"x":x,"y":y,"xx":xx,"yy":yy,
        "r":r,"m":m,"source_girth_at_least":8,
        "max_degree":max_degree,"max_degree_bound":s+1,
        "left_wedges":left_wedges,"right_wedges":right_wedges,
        "opposite_pair_capacity":_choose2(r),
        "C4_free_edge_cap":c4_cap,
        "C6_free_Moore_edge_cap":moore_cap,
        "combined_girth8_edge_cap":min(c4_cap,moore_cap,r*(s+1)),
        "degree_cap":r*(s+1),
        "path3_left_to_right":paths3,
        "path3_pair_capacity":r*r-m,
        "rows":rows,
    }


def global_mixed_book_certificate(model, *,
                                  max_pairs=40_000, max_book_witnesses=2500):
    """All-h computable deterministic but generally WEAK cubic book cap.

    For mixed pair multiplicities c_uv:
        M1=sum_mixed c_uv, M3=sum_mixed choose(c_uv,3),
        Bmixed=3*M3 <= ((Cmax-1)*(Cmax-2)/2)*M1,
    with Cmax=min(C4-free extremal edge cap, r*(s+1)).
    M1 is independently constrained by
        sum_(all unordered u,v) c_uv = sum_w choose(deg(w),2).
    There is no assertion this cap is o(s^6), or improves K2/K3-C.
    """
    a, s = model["a"], model["s"]
    graph = kikuchi_graph(model)
    n = len(graph)
    if type(max_pairs) is not int or max_pairs < 0 or n*(n-1)//2 > max_pairs:
        raise RuntimeError("Kikuchi pair budget exceeded (fail closed)")
    if type(max_book_witnesses) is not int or max_book_witnesses < 0:
        raise ValueError("nonnegative book witness budget required")
    invert = source_inverses(model)
    mixed_m1=mixed_m2=mixed_m3=0
    aligned_m1=aligned_m3=0
    book_witnesses=0
    witness_max_path3=0
    max_c=0
    high_pairs=[]
    for u in range(n):
        nu = graph[u]
        for v in range(u+1,n):
            c = len(nu & graph[v])
            if (u//a == v//a) or (u%a == v%a):
                aligned_m1 += c
                aligned_m3 += _choose3(c)
                continue
            mixed_m1 += c
            mixed_m2 += _choose2(c)
            mixed_m3 += _choose3(c)
            max_c = max(max_c,c)
            if c >= 3:
                high_pairs.append((u,v,c))
    if len(high_pairs)>max_book_witnesses:
        raise RuntimeError("mixed book witness budget exceeded (fail closed)")
    for u,v,c in high_pairs:
        h = mixed_compatibility(model,u,v,inverses=invert)
        if h["m"] != c:
            raise AssertionError("original GQ tensor vs Kikuchi codegree mismatch")
        book_witnesses+=1
        witness_max_path3=max(witness_max_path3,h["path3_left_to_right"])
    degree_from_original=star_degree_tensor(model)
    if degree_from_original != tuple(map(len,graph)):
        raise AssertionError("independent original GQ degree tensor mismatch")
    total_codegree_by_stars=sum(_choose2(d) for d in degree_from_original)
    if mixed_m1+aligned_m1 != total_codegree_by_stars:
        raise AssertionError("all-graph codegree first moment identity failed")
    cap = min(c4_free_edge_cap(a-2),girth8_moore_edge_cap(a-2),
              (a-2)*(s+1))
    if max_c > cap:
        raise AssertionError("mixed original GQ pointwise girth cap exceeded")
    # 3*choose(c,3)=c*(c-1)*(c-2)/2, monotone in c.
    book_bound = mixed_m1*max(0,cap-1)*max(0,cap-2)//2
    actual_book = 3*mixed_m3
    if actual_book > book_bound:
        raise AssertionError("global mixed-book cap violated")
    check=book_moments(graph,a)
    if check["book_mixed"] != actual_book:
        raise AssertionError("independent K3-C book moment mismatch")
    if check["book_same_x"]+check["book_same_y"] != 3*aligned_m3:
        raise AssertionError("aligned source book decomposition mismatch")
    return {
        "s":s,"a":a,"r":a-2,"Kikuchi_vertices":n,
        "mixed_M1":mixed_m1,"mixed_M2":mixed_m2,
        "mixed_M3":mixed_m3,"B_mixed":actual_book,
        "B_aligned":3*aligned_m3,
        "B_total":actual_book+3*aligned_m3,
        "B_mixed_fraction":str(__import__("fractions").Fraction(actual_book,
            actual_book+3*aligned_m3)) if actual_book+3*aligned_m3 else "0",
        "total_codegree_M1_from_original_stars":total_codegree_by_stars,
        "aligned_M1":aligned_m1,
        "mixed_max_codegree":max_c,
        "universal_mixed_codegree_cap":cap,
        "C4_free_cap":c4_free_edge_cap(a-2),
        "C6_free_Moore_cap":girth8_moore_edge_cap(a-2),
        "B_mixed_upper_via_first_moment":book_bound,
        "book_witnesses_checked_against_original_GQ":book_witnesses,
        "max_witness_3paths":witness_max_path3,
        "uniform_o_s6_proved":False,
        "branch_A_or_B_proved":False,
    }


def report():
    result={"slice":"HYP-105-B3.2-E1-K3-D",
            "scientific_verdict":"RESTRICTED_THEOREM_C",
            "all_h_mixed_book_saving_proved":False,
            "models":{}}
    for power,scheme,seed in ((1,"lex",None),
                              (1,"reverse-line",None),
                              (2,"random",20261011)):
        model=gq_pair_model(power,scheme,seed)
        result["models"]["s%s-%s"%(model["s"],scheme)]=global_mixed_book_certificate(model)
    return result


if __name__=="__main__":
    print(json.dumps(report(),sort_keys=True,indent=2))
