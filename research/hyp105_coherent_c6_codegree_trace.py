"""HYP-105 #230 AA4-C6TRACE: exact source-safe C6 codegree trace.

For every simple undirected bipartite G=(L,R,E), K_{uv}=|N(u)∩N(v)|
for different u,v in L and K_uu=0. Exact identity:

 C6(G)=tr(K^3)/6
       - sum_{r in R} ((deg(r)-2) sum_{{u,v} subset N(r)} K_uv
                       -2*binom(deg(r),3)).

The first term counts 3-distinct-left / 3-not-necessarily-distinct-right
closed six-walks; the correction removes right-coordinate coincidences,
including the all-three-equal case by inclusion-exclusion. Pure combinatorics,
all finite bipartite graphs, independent of f/g randomness.

For a genuine W(3,2^h) ORIGINAL source-ID subset which has been made
pencil-conflict-free, and passed BOTH typed physical-coordinate 2-cuts
as in #659, every simple C6 is physical coordinate-rainbow and maps
bijectively to a historical ORIGINAL GF5-accepted six-ID D6. This provides
a computable same-map D6 lower certificate. A large trace(K^3) alone
is not sufficient; the correction may consume it entirely (source GQ
Levi incidence graphs are exact zero-C6 density-threshold controls).
No universal Omega(s^6) conclusion is asserted.
"""
from collections import Counter,defaultdict,deque
from itertools import combinations
from math import comb


def bipartite_parts(adjacency):
    """Reject loops, missing reverse edges and odd cycles; return bipartition."""
    adj={v:set(ns) for v,ns in adjacency.items()}
    if any(not isinstance(v,tuple) or len(v)!=2 for v in adj):
        raise ValueError("vertices must be typed physical coordinate pairs")
    for v,ns in adj.items():
        if v in ns:
            raise ValueError("self-loop is not an admissible simple graph")
        for w in ns:
            if w not in adj or v not in adj[w]:
                raise ValueError("missing reverse adjacency")
    color={}
    for root in sorted(adj):
        if root in color:
            continue
        color[root]=0
        pending=deque([root])
        while pending:
            v=pending.popleft()
            for w in sorted(adj[v]):
                if w in color:
                    if color[w]==color[v]:
                        raise ValueError("graph is not bipartite")
                else:
                    color[w]=1-color[v]
                    pending.append(w)
    return adj,tuple(sorted(v for v in color if color[v]==0)),tuple(
        sorted(v for v in color if color[v]==1))


def exact_bipartite_codegree_trace(adjacency,*,verify_by_dfs=False,
                                   source_flags=None,source_provenance=None,
                                   original_f=None,original_g=None):
    """Exact integer sextic witness: no sixcycle enumeration in main path.

    If source parameters are given, independent DFS validates that each
    physical 6cycle has six different REAL original source point/line IDs
    and passes historical GF5 classifier. This check is separate from
    the codegree identity itself and not an all-h computational proof.
    """
    adj,L,R=bipartite_parts(adjacency)
    codegree=Counter()
    codegree_neighbors=defaultdict(set)
    for right in R:
        for u,v in combinations(sorted(adj[right]),2):
            codegree[u,v]+=1
            codegree_neighbors[u].add(v)
            codegree_neighbors[v].add(u)

    triangle_mass=0
    triangles_positive=0
    for u in L:
        for v in sorted(w for w in codegree_neighbors[u] if w>u):
            for w in sorted(w for w in (codegree_neighbors[u] &
                                        codegree_neighbors[v]) if w>v):
                triangle_mass += (codegree[u,v]*codegree[v,w]*
                                  codegree[u,w])
                triangles_positive+=1

    correction=0
    correction_triple_sources=0
    for right in R:
        nbr=sorted(adj[right])
        d=len(nbr)
        if d<3:
            continue
        pair_mass=sum(codegree[u,v] for u,v in combinations(nbr,2))
        right_correction=(d-2)*pair_mass-2*comb(d,3)
        if right_correction<0:
            raise AssertionError("right-star collision correction negative")
        correction+=right_correction
        correction_triple_sources+=comb(d,3)
    cycles=triangle_mass-correction
    if cycles<0:
        raise AssertionError("negative source-safe ordinary C6 count")
    e=sum(map(len,adj.values()))//2
    res={
        "bipartite_left_vertices":len(L),
        "bipartite_right_vertices":len(R),
        "edges":e,
        "positive_codegree_pairs":len(codegree),
        "positive_codegree_triangles":triangles_positive,
        "trace_K_cubed":6*triangle_mass,
        "trace_K_cubed_div_six":triangle_mass,
        "exact_right_collision_correction":correction,
        "right_common_triples":correction_triple_sources,
        "exact_ordinary_C6":cycles,
        "all_h_bipartite_trace_identity_proved":True,
        "all_h_universal_seven_class_Omega_s6_proved":False,
    }
    if verify_by_dfs:
        direct,original=independent_simple_C6_DFS(
            adj,source_flags=source_flags,
            source_provenance=source_provenance,
            original_f=original_f,original_g=original_g)
        if direct!=cycles:
            raise AssertionError("independent simple C6 DFS differs from trace")
        res["independent_C6_DFS"]=direct
        res["genuine_original_GF5_D6_checked"]=original
    return res


def independent_simple_C6_DFS(adjacency,*,source_flags=None,
                               source_provenance=None,
                               original_f=None,original_g=None):
    """Independently enumerate unoriented unorooted simple 6cycles.

    If original inputs supplied: verify all six TRUE original source
    incidence IDs, point/line distinctness and historic GF5 D6 acceptance.
    """
    adj={v:set(ns) for v,ns in adjacency.items()}
    verify_source=source_flags is not None
    if verify_source:
        if (source_provenance is None or original_f is None or
                original_g is None):
            raise ValueError("source verifier requires all source inputs")
        from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
    cycles=0
    seen_source_ids=set()
    def walk(path):
        nonlocal cycles
        if len(path)==6:
            if path[0] not in adj[path[-1]] or not(path[1]<path[-1]):
                return
            cycles+=1
            if verify_source:
                cids=tuple(sorted(source_provenance[tuple(sorted((
                    path[i],path[(i+1)%6]))) ] for i in range(6)))
                if (len(set(cids))!=6 or
                        len({source_flags[i][0] for i in cids})!=6 or
                        len({source_flags[i][1] for i in cids})!=6):
                    raise AssertionError("repeated original source incidence/factor")
                if (len({v[0] for v in path})!=6 or
                        len({v[1] for v in path})!=6):
                    raise AssertionError("not physical coordinate-rainbow")
                if classify_seven_prechecked(
                        cids,original_f,original_g,source_flags)!="D6":
                    raise AssertionError("not accepted historical original GF5 D6")
                if cids in seen_source_ids:
                    raise AssertionError("different cycles mapped to same source sixset")
                seen_source_ids.add(cids)
            return
        for v in sorted(adj[path[-1]]):
            if v>path[0] and v not in path:
                walk(path+(v,))
    for root in sorted(adj):
        walk((root,))
    return cycles,verify_source and len(seen_source_ids)==cycles


def source_selected_codegree_certificate(power,f,g,threshold,
                                         *,source_subset=None):
    """TRUE W32/W34 complete injected maps, prior #659 selector vs new trace.

    No artificial edges; source IDs and both physical diagonals persist.
    The #659 independent source-C6 DFS/classifier output is crosschecked.
    """
    from hyp105_full_physical_degree_tail import (
        genuine_source, finite_tail_selector, physical,
    )
    previous=finite_tail_selector(
        power,f,g,threshold,source_subset=source_subset)
    _,_,flags=genuine_source(power)
    ids=tuple(previous["retained_source_ids"])
    adjacency,provenance=physical(ids,flags,tuple(map(tuple,f)),
                                  tuple(map(tuple,g)))
    result=exact_bipartite_codegree_trace(
        adjacency,verify_by_dfs=True,
        source_flags=flags,source_provenance=provenance,
        original_f=f,original_g=g)
    if (result["exact_ordinary_C6"]!=previous["ordinary_C6"] or
            result["exact_ordinary_C6"]!=previous["accepted_original_D6"]):
        raise AssertionError("source-ID selector accepted D6 discrepancy")
    return {
        "source_s":1<<power,
        "complete_original_source_ID_count":len(ids),
        "both_original_diagonals_retained":len(provenance)==2*len(ids),
        "prior_accepted_original_D6":previous["accepted_original_D6"],
        **result,
    }
