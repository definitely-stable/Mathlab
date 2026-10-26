"""HYP-105 #230 AA4-K32SAT1: unit-multiplicity D6 transfer.

Theorem for ANY finite simple bipartite selected graph G:

For each physically coordinate-transverse SATURATED K3,2 source block F
(three hubs sharing exactly two common frees, and EACH hub pair has
EXACTLY those two neighbors), let E2(F) denote the accepted ORIGINAL
six-ID radius-two extensions in full true-source physical H. The
existing AA4-K32X2 theorem states all E2(F) are D6 and
|E2(F)| = 2 sum_(hub pairs) fresh_common_neighbors_H.

For distinct saturated parents F1!=F2 in the SAME SELECTED graph G,
E2(F1) and E2(F2) are DISJOINT. Proof: fix their common accepted C6.
Every possible K3,2 parent consists of all three vertices of one
alternating side of C6 and two vertices of the other side. Two different
parents of the same orientation give a third common neighbor to all
hubs. Parents of opposite orientation give a third common neighbor
to a pair of the first parent's hubs. In either case the first
parent is NOT saturated in G, a contradiction.

Hence globally and at the SAME fixed correlated true-source maps:
    D6(H) >= sum_(F in SATURATED_K32(G)) |E2(F)|
          = 2 sum_F sum_(i<j) |W_ij^full_H(F)|.

This is a sharpening from the earlier general factor-6 theorem to
FACTOR ONE. A real W(3,4) source example with two source-disjoint
K3,2 blocks and two extensions for each witnesses strict positivity.
No UNIVERSAL lower bound on fresh common-neighbor mass is proved.
"""
from collections import defaultdict
from itertools import combinations

from hyp105_full_physical_degree_tail import (
    genuine_source,physical,conflict_graph,verify_selected,
)
from hyp105_physical_degree_energy import (
    minimal_alphabet,_verify_typed_injections,
)
from hyp105_k32_radius2_exact_extension_count import (
    one_k32_original_two_exchange,
)


def coherent_coordinate_colors(ids,flags,f,g,axis):
    """Independently certify existence of both strict coordinate 2-cuts."""
    from collections import deque
    edges=[tuple((f if axis==0 else g)[flags[i][axis]]) for i in ids]
    links=defaultdict(set)
    for x,y in edges:
        if x==y:
            raise ValueError("source pair contains loop")
        links[x].add(y)
        links[y].add(x)
    color={}
    for root in sorted(links):
        if root in color:
            continue
        color[root]=0
        q=deque([root])
        while q:
            v=q.popleft()
            for w in sorted(links[v]):
                if w in color:
                    if color[w]==color[v]:
                        raise ValueError("selected original-ID coordinate graph has no 2-cut")
                else:
                    color[w]=1-color[v]
                    q.append(w)
    a=max(max(edge) for edge in edges)+1 if edges else 0
    return tuple(color.get(x,0) for x in range(a))


def saturated_bipartite_k32_list(selected):
    """Enumerate ACTUAL selected-graph saturated K3,2, distinct sixsets.

    A selected physical graph is simple, genuine-source-backed,
    coordinate proper, and strict 2-cut bipartite. Every triple of
    common-neighbor hubs with exactly the same two physical frees is
    visited just once. No generic K3,2 is incorrectly called saturated.
    """
    posts=defaultdict(set)
    for free,ns in selected.items():
        for a,b in combinations(sorted(ns),2):
            posts[a,b].add(free)
    strong=defaultdict(set)
    for (a,b),witnesses in posts.items():
        if len(witnesses)>=2:
            strong[a].add(b)
            strong[b].add(a)
    out=[]
    for a in sorted(strong):
        for b in sorted(v for v in strong[a] if v>a):
            for c in sorted(v for v in (strong[a]&strong[b]) if v>b):
                A=posts[a,b]
                B=posts[b,c]
                C=posts[a,c]
                if len(A)!=2 or A!=B or A!=C:
                    continue
                hubs=(a,b,c)
                frees=tuple(sorted(A))
                if len({v[0] for v in hubs+frees})!=5 or (
                    len({v[1] for v in hubs+frees})!=5):
                    raise AssertionError("genuine selected saturation lost coordinate transversality")
                out.append((hubs,frees))
    return tuple(out)


def genuine_source_saturated_unit_transfer(power,f,g,selected_ids):
    """Finite TRUE W32/W34 test of the all-h unit multiplicity theorem.

    Exactly one fixed globally injected completed f/g is used for
    selection and for full-H new common-neighbor extensions.
    """
    s,V,flags=genuine_source(power)
    f,g=tuple(map(tuple,f)),tuple(map(tuple,g))
    a=minimal_alphabet(V)
    _verify_typed_injections(a,V,f,g)
    ids=tuple(sorted(selected_ids))
    if len(ids)!=len(set(ids)) or any(type(i)is not int or
            i<0 or i>=len(flags) for i in ids):
        raise ValueError("must select distinct genuine original incidence IDs")
    conflict,mf,mg=conflict_graph(ids,flags,f,g)
    if mf or mg or any(conflict.values()):
        raise ValueError("selected real-source IDs violate pencil conflict-free requirement")
    colors_x=coherent_coordinate_colors(ids,flags,f,g,0)
    colors_y=coherent_coordinate_colors(ids,flags,f,g,1)
    colors_x=colors_x+(0,)*(a-len(colors_x))
    colors_y=colors_y+(0,)*(a-len(colors_y))
    selected,source_edges,checked=verify_selected(
        ids,flags,f,g,colors_x,colors_y)
    if len(source_edges)!=2*len(ids):
        raise AssertionError("paired original physical diagonals not retained")
    candidates=saturated_bipartite_k32_list(selected)
    full,provenance=physical(range(len(flags)),flags,f,g)
    parent_original_sets=set()
    accepted_to_parent={}
    local_sum=0
    local_neighborhood_sum=0
    for hubs,frees in candidates:
        result=one_k32_original_two_exchange(
            hubs,frees,flags,f,g,
            full_adjacency=full,full_provenance=provenance,
            check_classifier=True)
        old=result["old_original_six_flags"]
        if old in parent_original_sets:
            raise AssertionError("different selected saturation representations share sixset")
        parent_original_sets.add(old)
        additions=result["two_exchange_accepted_original_D6"]
        neighbors=result["true_new_common_vertices_total"]
        if additions!=2*neighbors:
            raise AssertionError("parent exact AA4-K32X2 theorem mismatch")
        local_sum+=additions
        local_neighborhood_sum+=neighbors
        for accepted in result["source_accepted_sixsets"]:
            if accepted in accepted_to_parent:
                raise AssertionError("TWO saturated blocks in SAME selected graph share original D6")
            accepted_to_parent[accepted]=old
    if len(accepted_to_parent)!=local_sum:
        raise AssertionError("saturated-only UNIT multiplicity broken")
    return {
        "s":s,"V":V,"a":a,
        "true_source_selected_incidence_ids":ids,
        "selected_ordinary_C6":checked["ordinary_C6"],
        "selected_original_GF5_D6":checked["accepted_original_D6"],
        "selected_original_double_diagonal_edges":len(source_edges),
        "saturated_original_source_K32_blocks":len(candidates),
        "saturated_source_sixsets":tuple(sorted(parent_original_sets)),
        "full_H_fresh_common_neighbor_mass":local_neighborhood_sum,
        "two_swap_D6_extension_memberships":local_sum,
        "distinct_accepted_original_D6_from_saturated_blocks":
            len(accepted_to_parent),
        "max_original_D6_saturated_parent_multiplicity":
            1 if accepted_to_parent else 0,
        "exact_source_sixset_to_saturated_parent":
            tuple(sorted(accepted_to_parent.items())),
        "all_h_saturated_only_unit_multiplicity_proved":True,
        "root_sevenclass_Omega_s6_proved":False,
    }


def real_W34_two_disjoint_saturated_blocks():
    """Two independent physical K3,2 blocks from 16 GENUINE W34 source flags.

    Full completed maps include 4 extra source flags, each group has 2
    fresh physical edges. Selected graph uses only 12 old flags and is
    source-conflict free and has two valid coordinate 2-cuts.
    """
    s,V,flags=genuine_source(2)
    if (s,V)!=(4,85):
        raise AssertionError("wrong genuine symplectic W34 source")
    by_point=[[] for _ in range(V)]
    for p,l in flags:
        by_point[p].append(l)
    owner={}
    def augment(p,visited):
        for l in by_point[p]:
            if l in visited:
                continue
            visited.add(l)
            if l not in owner or augment(owner[l],visited):
                owner[l]=p
                return True
        return False
    for p in range(16):
        if not augment(p,set()):
            raise AssertionError("cannot find 16 pairwise original-factor disjoint flags")
    matched=sorted((p,l) for l,p in owner.items())
    if len(matched)!=16 or len({p for p,l in matched})!=16 or (
            len({l for p,l in matched})!=16):
        raise AssertionError("genuine W34 matching lost original factor uniqueness")
    K0=((0,3),(0,4),(1,3),(1,4),(2,3),(2,4))
    K1=((6,9),(6,10),(7,9),(7,10),(8,9),(8,10))
    ext0=((0,5),(1,5))
    ext1=((6,11),(7,11))
    arrangement=K0+ext0+K1+ext1
    if len(set(arrangement))!=16:
        raise AssertionError("typed K14 labels repeated")
    f=[None]*V
    g=[None]*V
    indices={pair:i for i,pair in enumerate(flags)}
    for (x,y),(p,l) in zip(arrangement,matched):
        f[p]=(x,y)
        g[l]=(x,y)
    pairs=tuple(combinations(range(minimal_alphabet(V)),2))
    for labels in (f,g):
        used={q for q in labels if q is not None}
        rest=iter(q for q in pairs if q not in used)
        for i in range(V):
            if labels[i] is None:
                labels[i]=next(rest)
    _verify_typed_injections(minimal_alphabet(V),V,f,g)
    allids=tuple(indices[z] for z in matched)
    protected_ids=tuple(allids[i] for i in tuple(range(6))+tuple(range(8,14)))
    report=genuine_source_saturated_unit_transfer(
        2,f,g,protected_ids)
    if report["saturated_original_source_K32_blocks"]!=2 or (
            report["two_swap_D6_extension_memberships"]<4 or
            report["distinct_accepted_original_D6_from_saturated_blocks"]<4):
        raise AssertionError("two real disjoint K3,2 sharp positive example failed")
    return report
