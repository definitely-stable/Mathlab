"""HYP-105 #230 AA4-TCN: universal same-fixed-map triple-codegree D6 transfer.

For ANY genuine source W(3,s) with separately complete globally injected
typed physical pair maps f,g (arbitrary correlation), a coordinate-transverse
K_{3,3} in the genuine-source physical corner graph H yields exactly SIX
accepted ORIGINAL six-source-incidence GF(5) D6 motifs.

Let U range over unordered coordinate-injective triples of physical corners;
T(U)=common physical neighbors of all U that avoid ALL first/second
coordinates used by U. Give T(U) the simple bipartite coordinate graph
on first and second physical symbols, and let m3(T) be its 3-matching
count, i.e. unordered triples with pairwise distinct coordinates in BOTH
axes. Each eligible K3,3 is counted twice by U<->T, and each has six
alternating C6, hence 3*sum_U m3(T(U)) exactly counts the K3,3-supported
subset of accepted ORIGINAL D6 motifs. It is <= total D6; NOT equality
in general. No source-free physical edges and no reused source IDs.

For m=|T(U)|, Delta=max coordinate degree among T(U), D=2Delta-1,
m3(T)>=m*[m-D]_+*[m-2D]_+/6.
Thus D6 >= (1/2)*sum_U m*[m-D]_+*[m-2D]_+, all h.

Code below is finite true-source GF2/GF4 certificate; all-h is the proof.
"""
from collections import defaultdict
from itertools import combinations, permutations
from hyp105_physical_degree_energy import minimal_alphabet

from hyp105_b1_symplectic import symplectic_gq
from hyp105_physical_rainbow_c6 import (
    build_original_physical_graph, exact_rainbow_c6_finite,
)


def exact_coordinate_transversal_m3(corners):
    """Return exact three-edge matching count in the physical coordinate graph.

    Corners are unordered pairs (x,y) in a bipartite graph on typed
    first/second alphabet symbols. No equality x!=y is needed: the
    coordinates are TYPED; only within-side noncollision matters.
    """
    corners=tuple(corners)
    if len(set(corners)) != len(corners):
        raise ValueError("physical corner multiset not allowed")
    result=0
    for three in combinations(corners, 3):
        if (len({v[0] for v in three}) == 3 and
                len({v[1] for v in three}) == 3):
            result+=1
    return result


def greedy_matching_three_lower(corners):
    """Rigorous all-h integer numerator of lower bound 6*m3 >= numerator."""
    corners=tuple(corners)
    if len(set(corners))!=len(corners):
        raise ValueError("duplicate coordinate corner")
    m=len(corners)
    if m<3:
        return 0
    dx={}
    dy={}
    for x,y in corners:
        dx[x]=dx.get(x,0)+1
        dy[y]=dy.get(y,0)+1
    delta=max((*dx.values(),*dy.values()))
    D=2*delta-1
    return m*max(0,m-D)*max(0,m-2*D)


def _six_cycles_on_k33(hubs, frees):
    """Exactly SIX undirected alternating simple C6, with fixed hub order."""
    h0,h1,h2=hubs
    for a,b,c in permutations(frees):
        yield (h0,a,h1,b,h2,c)


def true_source_triple_codegree_d6(power, f, g, *, verify_gf5=True,
                                    verify_full_d6=True):
    """Complete physical K3,3-positive D6 sector on genuine W32/W34.

    Efficient triple-neighbor *inverse posting* enumerates only hub
    triples with at least one common physical neighbor, rather than all
    O(a^6) corner triples. Every accepted sixset source ID checked
    once even for graphs with extra internal hub/free edges.
    """
    if type(power) is not int or power not in (1,2):
        raise ValueError("finite source certificate restricted to h=1,2")
    s=1<<power
    _,points,lines,flags=symplectic_gq(power)
    V=(s+1)*(s*s+1)
    if len(points)!=V or len(lines)!=V:
        raise AssertionError("non-genuine W(3,s) source")
    f=tuple(map(tuple,f))
    g=tuple(map(tuple,g))
    adj,arc_id=build_original_physical_graph(s,f,g,flags)
    if verify_gf5:
        from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked

    # Every candidate hub U is posted by the vertices in N(U).
    by_three_hubs=defaultdict(list)
    for free,neighbors in adj.items():
        for hubs in combinations(sorted(neighbors),3):
            by_three_hubs[hubs].append(free)
    oriented_m3=0
    greedy_numerator=0
    hub_triples_with_coordinate_transverse_three_neighbors=0
    max_eligible_triple_codegree=0
    unique_K33={}
    seen_six_source_sets=set()

    for hubs,common in by_three_hubs.items():
        used_x={v[0] for v in hubs}
        used_y={v[1] for v in hubs}
        if len(used_x)!=3 or len(used_y)!=3:
            continue
        free=tuple(sorted(v for v in common
                          if v[0] not in used_x and v[1] not in used_y))
        if len(free)<3:
            continue
        max_eligible_triple_codegree=max(
            max_eligible_triple_codegree,len(free))
        m3=exact_coordinate_transversal_m3(free)
        local_bound_num=greedy_matching_three_lower(free)
        if 6*m3<local_bound_num:
            raise AssertionError("all-h coordinate-degree three-matching lower failed")
        greedy_numerator+=local_bound_num
        oriented_m3+=m3
        if m3:
            hub_triples_with_coordinate_transverse_three_neighbors+=1
        for free_three in combinations(free,3):
            if (len({v[0] for v in free_three})!=3 or
                    len({v[1] for v in free_three})!=3):
                continue
            # The hub/free bipartition is unique only up to SWAP.
            # Within-part physical chords are allowed and irrelevant.
            name=tuple(sorted((hubs,free_three)))
            if name in unique_K33:
                continue
            unique_K33[name]=(hubs,free_three)
            for cyc in _six_cycles_on_k33(hubs,free_three):
                if len({v[0] for v in cyc})!=6 or len(
                        {v[1] for v in cyc})!=6:
                    raise AssertionError("not a coordinate-rainbow C6")
                if any(cyc[(i+1)%6] not in adj[cyc[i]]
                       for i in range(6)):
                    raise AssertionError("some purported K3,3 edge is synthetic")
                ids=tuple(sorted(arc_id[cyc[i],cyc[(i+1)%6]]
                                 for i in range(6)))
                if len(set(ids))!=6 or (
                        len({flags[k][0] for k in ids})!=6 or
                        len({flags[k][1] for k in ids})!=6):
                    raise AssertionError("not six DISTINCT original source factors")
                if ids in seen_six_source_sets:
                    raise AssertionError("K3,3 D6 sixset overcount across bipartitions")
                seen_six_source_sets.add(ids)
                if verify_gf5 and classify_seven_prechecked(
                        ids,f,g,flags)!="D6":
                    raise AssertionError("not accepted ORIGINAL GF5 D6")
    if oriented_m3!=2*len(unique_K33):
        raise AssertionError("exact K3,3 bipartition factor-two broken")
    d6_sector=6*len(unique_K33)
    if d6_sector!=3*oriented_m3 or d6_sector!=len(seen_six_source_sets):
        raise AssertionError("K3,3 source-sixset normalization broken")
    if 2*d6_sector<greedy_numerator:
        raise AssertionError("greedy lower bound exceeds actual K3,3 positive sector")
    total_d6=None
    if verify_full_d6:
        total_d6=exact_rainbow_c6_finite(
            power,f,g,verify_GF5=verify_gf5)["D6_original_sixsets"]
        if d6_sector>total_d6:
            raise AssertionError("positive K3,3 subclass exceeded total D6")
    return {
        "s":s,"V":V,"a":minimal_alphabet(V),
        "candidate_hub_triples":len(by_three_hubs),
        "admissible_hub_triples_with_positive_three_matchings":
            hub_triples_with_coordinate_transverse_three_neighbors,
        "max_admissible_triple_codegree":max_eligible_triple_codegree,
        "oriented_transversal_three_matchings":oriented_m3,
        "unique_coordinate_transverse_K33":len(unique_K33),
        "accepted_original_D6_from_K33":d6_sector,
        "all_accepted_original_D6":total_d6,
        "non_K33_accepted_original_D6":
            None if total_d6 is None else total_d6-d6_sector,
        "greedy_bound_two_times_D6_numerator":greedy_numerator,
        "all_h_K33_to_D6_exact_subsector_proved":True,
        "all_h_D6_Omega_s6_proved":False,
        "root_sevenclass_Omega_s6_proved":False,
    }
