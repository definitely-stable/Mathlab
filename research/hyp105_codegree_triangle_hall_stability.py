"""AA4-HALL2: sharp C6-free strong-codegree triangle stability.

For any simple bipartite G=(L,R,E), and u,v,w distinct left vertices,
the three sets S_uv=N(u)∩N(v), S_vw, S_wu of right witnesses form the
three pairwise common-neighbor lists. Every C6 with these THREE left
vertices is exactly a system of distinct representatives (SDR) for the
lists. If all three q_ij>=2, Hall's theorem and the special incidence
intersection structure imply:

 NO C6 for {u,v,w} <=> all three sets equal the SAME 2 right vertices
 <=> the three left vertices induce K_{3,2} on those two right vertices
      with NO other pair-common right witnesses.

Every other triple with all q>=2 supports >=2 distinct C6.
If all q>=3, it supports >=6 distinct C6 (greedy SDR).
Hence defining T2=#left triples with min q>=2; Sat2=#identical
2-neighbor triple stars; T3=#left triples with min q>=3:

 C6(G) >= 2*(T2-Sat2) + 4*T3.

This is a purely combinatorial deterministic all-graph inequality, not
a universal HYP-105 root lower. In a genuine original-source-selected,
doubly physical-coordinate-cut coherent graph from #659/#660, every
such ordinary C6 is an accepted ORIGINAL six-incidence GF5 D6.
Thus for ANY selected graph, S_seven>=D6>=this nonnegative integer.
If S_seven=o(s^6), necessarily T3=o(s^6) and
T2-Sat2=o(s^6) on EVERY such selected graph. This is a new exact
structural necessary condition for a hypothetical low-S sequence.
"""
from collections import defaultdict
from itertools import combinations

from hyp105_coherent_c6_codegree_trace import (
    bipartite_parts, exact_bipartite_codegree_trace,
)


def exact_double_codegree_triangle_stability(adjacency, *,
                                             verify_full_trace=True):
    """Count saturated vs productive strong-codegree triangles, exact integers.

    The local inclusion-exclusion population is calculated independently
    from #660's aggregate right-collision formula; no C6 enumeration in
    this main algorithm. Each left triple produces disjoint C6 sixsets.
    """
    adj,L,R=bipartite_parts(adjacency)
    q2neighbors=defaultdict(set)
    for u,v in combinations(L,2):
        if len(adj[u]&adj[v])>=2:
            q2neighbors[u].add(v)
            q2neighbors[v].add(u)
    t2=sat2=t3=robust_c6=0
    min_positive=0
    saturated_right_pairs={}
    for u in L:
        for v in sorted(z for z in q2neighbors[u] if z>u):
            for w in sorted(z for z in (
                    q2neighbors[u]&q2neighbors[v]) if z>v):
                A=adj[u]&adj[v]
                B=adj[v]&adj[w]
                C=adj[w]&adj[u]
                aa,bb,cc=len(A),len(B),len(C)
                t=len(A&B&C)
                if min(aa,bb,cc)<2:
                    raise AssertionError("non-double triangle in support")
                t2+=1
                cycles=aa*bb*cc-t*(aa+bb+cc)+2*t
                is_saturated=(aa==bb==cc==2 and t==2)
                if is_saturated:
                    sat2+=1
                    saturated_right_pairs[u,v,w]=tuple(sorted(A))
                elif cycles<2:
                    raise AssertionError("Hall-SDR productive strong triangle has fewer than 2 C6")
                if min(aa,bb,cc)>=3:
                    t3+=1
                    if cycles<6:
                        raise AssertionError("triple 3-codegree supports fewer than 6 C6")
                if (cycles==0)!=is_saturated:
                    raise AssertionError("all-h K3,2 saturation classification fails")
                robust_c6+=cycles
                min_positive+=cycles>0
    lower=2*(t2-sat2)+4*t3
    if robust_c6<lower:
        raise AssertionError("strong-codegree robust positive lower wrong")
    result={
        "left_vertices":len(L),
        "right_vertices":len(R),
        "edges":sum(map(len,adj.values()))//2,
        "double_codegree_triangle_count":t2,
        "saturated_identical_two_right_witness_triangles":sat2,
        "productive_double_codegree_triangles":t2-sat2,
        "triple_codegree_triangle_count":t3,
        "direct_exact_C6_on_double_codegree_left_triples":robust_c6,
        "all_h_stable_C6_lower":lower,
        "saturated_original_right_pairs":saturated_right_pairs,
        "all_h_Hall_SDR_saturation_dichotomy_proved":True,
        "all_h_root_sevenclass_Omega_s6_proved":False,
    }
    if verify_full_trace:
        full=exact_bipartite_codegree_trace(adj)
        if robust_c6>full["exact_ordinary_C6"] or (
                lower>full["exact_ordinary_C6"]):
            raise AssertionError("source strong-codegree lower exceeds ALL ordinary C6")
        result["total_C6_independent_right_collision_trace"]=full["exact_ordinary_C6"]
        result["ordinary_C6_not_from_strong_codegree_triangles"]=(
            full["exact_ordinary_C6"]-robust_c6
        )
    return result


def true_original_source_coherent_Hall_certificate(power, f, g, threshold,
                                                     *,source_subset=None):
    """Certified real W32/W34 source flags under parent exact selector.

    Full source f/g globally injected and may be arbitrarily correlated.
    The parent selector verifies real original ID provenance, two physical
    diagonals per chosen source ID, both 2-cuts, and historic GF5 D6
    for EACH chosen physically simple C6.
    """
    from hyp105_full_physical_degree_tail import (
        genuine_source, finite_tail_selector, physical,
    )
    selected=finite_tail_selector(
        power,f,g,threshold,source_subset=source_subset)
    _,_,flags=genuine_source(power)
    edges,provenance=physical(
        selected["retained_source_ids"],flags,
        tuple(map(tuple,f)),tuple(map(tuple,g)))
    if len(provenance)!=2*selected["retained_original_ids"]:
        raise AssertionError("genuine original source double diagonal lost")
    p=exact_double_codegree_triangle_stability(edges)
    if p["total_C6_independent_right_collision_trace"]!=(
            selected["accepted_original_D6"]):
        raise AssertionError("true original sixflag GF5 D6 census mismatch")
    if p["all_h_stable_C6_lower"]>selected["accepted_original_D6"]:
        raise AssertionError("positive original GF5 certificate violated")
    return {
        "s":1<<power,
        "retained_true_original_source_IDs":selected["retained_original_ids"],
        "original_source_GF5_accepted_D6":selected["accepted_original_D6"],
        "original_source_provenance_verified":True,
        "two_physical_coordinate_cuts_verified":True,
        **p,
    }
