"""HYP-105 #230 AA4-K32X2: exact ORIGINAL two-ID radius-two compensation.

For ANY TRUE original symplectic W(3,2^h), complete separately globally
injective typed f,g, and a *coordinate-transverse source-ID* physical
K_{3,2} with six distinct source point and line factors:

  (A) An accepted original GF5 sixset differing in exactly two source
      IDs MUST be the historical class D6; the two discarded K3,2
      edges MUST form a size-2 matching (different hubs and frees).
      The two new flags MUST be physical edges from those two deficient
      hubs to one NEW physical corner w whose first AND second physical
      symbols are not among the five K3,2 physical symbols.
      If instead the two removed edges share a hub, both new point
      labels and both new line labels would have to coincide, forcing
      two distinct original incidences to have the SAME original point
      AND the SAME original line -- impossible in the TRUE simple GQ
      source incidence graph.

  (B) For distinct hub indices i<j let W_ij be the ACTUAL full physical
      common neighbors N(h_i)∩N(h_j) with both typed coordinates outside
      the initial five. Then **exactly**
        |E2(F) intersect historical seven-GF5| =
            2 * sum_{i<j} |W_ij|,
      and EVERY accepted member is ORIGINAL D6. For each w, choose
      the two possible matching deletions touching different frees.
      Each resulting sixset has six distinct genuine source point and
      line IDs and is verified by the historical GF5 classifier.

  (C) For a FAMILY of DISTINCT coordinate-transverse source K3,2
      sixsets F in the SAME full map, sum_F |E2(F)| <= 6 * D6(f,g).
      Proof: each accepted original D6 corresponds to exactly ONE
      unoriented physical coordinate-rainbow C6; it has six choices
      of its NEW vertex w. Once w is removed, its remaining four
      physical edges are a four-edge path, whose UNIQUE K3,2 completion
      (if the missing genuine incidence edges exist) recovers F.
      Therefore each accepted D6 has at most six parent K3,2 sixsets.

This yields the global same-map **conditional** certificate
        D6(f,g) >= (1/3) sum_F sum_{i<j} |W_ij(F)|.
It is NOT a universal lower bound on |W_ij| or on S_seven.
Finite sources W32/W34 only; mathematical theorem is all h.
"""
from collections import defaultdict
from itertools import combinations

from hyp105_full_physical_degree_tail import physical,genuine_source
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked


def edge_key(v,w):
    return tuple(sorted((v,w)))


def one_k32_original_two_exchange(hubs,frees,flags,f,g, *,
                                  full_adjacency=None,full_provenance=None,
                                  check_classifier=True):
    """Exact original source GF5 radius-2 positive population of one K3,2.

    Physical graph may be the full map or a SOURCE-ID subset graph; the
    provenance MUST map every listed physical edge to one real source
    incidence ID. Typed globally injected f/g is a precondition.
    """
    hubs=tuple(hubs)
    frees=tuple(frees)
    if len(hubs)!=3 or len(frees)!=2 or len(set(hubs+frees))!=5:
        raise ValueError("requires 3 hubs and 2 free distinct physical corners")
    if (len({v[0] for v in hubs+frees})!=5 or
            len({v[1] for v in hubs+frees})!=5):
        raise ValueError("K3,2 five physical corners must be coordinate transverse")
    if full_adjacency is None or full_provenance is None:
        full_adjacency,full_provenance=physical(
            range(len(flags)),flags,f,g)
    eids={}
    for i,h in enumerate(hubs):
        for j,z in enumerate(frees):
            e=edge_key(h,z)
            if e not in full_provenance:
                raise ValueError("not a TRUE original incidence backed K3,2")
            eids[i,j]=full_provenance[e]
    F=frozenset(eids.values())
    if len(F)!=6 or len({flags[k][0] for k in F})!=6 or (
            len({flags[k][1] for k in F})!=6):
        raise ValueError("K3,2 source incidence IDs/factors must be distinct")
    if check_classifier and classify_seven_prechecked(
            tuple(sorted(F)),f,g,flags) is not None:
        raise AssertionError("old K3,2 sixset cannot be historical GF5 accepted")
    occupied_x={z[0] for z in hubs+frees}
    occupied_y={z[1] for z in hubs+frees}
    new_sixsets={}
    candidates={}
    for i,j in combinations(range(3),2):
        h1,h2=hubs[i],hubs[j]
        common=full_adjacency.get(h1,set()) & full_adjacency.get(h2,set())
        free_new=tuple(sorted(w for w in common
                              if w[0] not in occupied_x and
                                 w[1] not in occupied_y))
        candidates[i,j]=free_new
        for w in free_new:
            p=full_provenance[edge_key(h1,w)]
            q=full_provenance[edge_key(h2,w)]
            if p==q or p in F or q in F:
                raise AssertionError("new coordinate distinctness fails source injection")
            for r,s in ((0,1),(1,0)):
                dropped={eids[i,r],eids[j,s]}
                if len(dropped)!=2:
                    raise AssertionError("not two real old source IDs")
                new=tuple(sorted((F-dropped)|{p,q}))
                if len(new)!=6:
                    raise AssertionError("two replacements not size six")
                if len({flags[k][0] for k in new})!=6 or (
                        len({flags[k][1] for k in new})!=6):
                    raise AssertionError("new flags not six genuine distinct factors")
                if check_classifier and classify_seven_prechecked(
                        new,f,g,flags)!="D6":
                    raise AssertionError("actual physical C6 NOT original GF5 D6")
                if new in new_sixsets:
                    raise AssertionError("local radius-two witness overcount")
                new_sixsets[new]=(i,j,w,r,s)
    expected=2*sum(map(len,candidates.values()))
    if len(new_sixsets)!=expected:
        raise AssertionError("exact two-exchange completion formula broken")
    return {
        "old_original_six_flags":tuple(sorted(F)),
        "hubs":hubs,"frees":frees,
        "candidate_new_common_vertices":candidates,
        "true_new_common_vertices_total":expected//2,
        "two_exchange_accepted_original_D6":len(new_sixsets),
        "source_accepted_sixsets":new_sixsets,
        "all_h_exact_radius_two_extension_formula_proved":True,
        "all_h_root_sevenclass_Omega_s6_proved":False,
    }


def independent_original_source_factor_exchange_census(hubs,frees,flags,f,g):
    """Independent ORIGINAL POINT-label indexed two-swap census (not H neighbors).

    Explicitly audits all deletion patterns:
      - two discarded edges on distinct frees and distinct hubs:
        find two new source point label edges to one fresh x-coordinate,
        then independently enumerate their TRUE incident source LINES.
        Invoke full historical seven-class classifier.
      - two edges sharing one hub: any admitted x-candidate needs a
        repeated source point, and y-classification forces same source
        line; no pair of DISTINCT actual original incidence flags can pass.
    Returns actual accepted seven-class sixsets for distance exactly 2.
    """
    hubs=tuple(hubs)
    frees=tuple(frees)
    source_ids={flag:i for i,flag in enumerate(flags)}
    old={}
    fp_to_p={tuple(sorted(pair)):p for p,pair in enumerate(f)}
    by_point=defaultdict(list)
    for idx,(p,l) in enumerate(flags):
        by_point[p].append(idx)
    for i,h in enumerate(hubs):
        for j,z in enumerate(frees):
            xp=tuple(sorted((h[0],z[0])))
            yp=tuple(sorted((h[1],z[1])))
            p=fp_to_p[xp]
            line_idx=next((l for l,q in enumerate(g)
                           if tuple(sorted(q))==yp),None)
            if line_idx is None or (p,line_idx) not in source_ids:
                raise ValueError("input not supported by true original source incidence")
            old[i,j]=source_ids[p,line_idx]
    F=frozenset(old.values())
    oldx={v[0] for v in hubs+frees}
    selected={}
    star_x_population=0
    for deleted in combinations(tuple(old),2):
        (i,k),(j,l)=deleted
        kept=F-{old[i,k],old[j,l]}
        if k==l:
            # One old degree-three free coordinate keeps degree 3.
            continue
        if i==j:
            # The two new first pairs must be an identical pair on
            # two not-yet-degree-two x coordinates. The two new
            # source IDs then have the SAME source point. The
            # symmetrically identical line pair condition requires
            # the SAME source line, impossible for distinct flags.
            # Independently test all actual repeated-source-point
            # candidate pairs against the full GF5 classifier.
            old_remaining_first={f[flags[z][0]][q]
                                 for z in kept for q in (0,1)}
            for p,idxs in by_point.items():
                if set(f[p]) & old_remaining_first:
                    continue
                for c1,c2 in combinations(idxs,2):
                    if c1 in F or c2 in F:
                        continue
                    star_x_population+=1
                    candidate=tuple(sorted(kept|{c1,c2}))
                    if classify_seven_prechecked(
                            candidate,f,g,flags) is not None:
                        raise AssertionError("source-simple star-exchange no-go falsified")
            continue
        for newx in range(max(max(v) for v in f)+1):
            if newx in oldx:
                continue
            p1=fp_to_p.get(tuple(sorted((hubs[i][0],newx))))
            p2=fp_to_p.get(tuple(sorted((hubs[j][0],newx))))
            if p1 is None or p2 is None:
                continue
            for c1 in by_point[p1]:
                if c1 in F:
                    continue
                for c2 in by_point[p2]:
                    if c2 in F or c1==c2:
                        continue
                    candidate=tuple(sorted(kept|{c1,c2}))
                    tag=classify_seven_prechecked(candidate,f,g,flags)
                    if tag is not None:
                        if tag!="D6":
                            raise AssertionError("non-D6 accepted two-swap motif")
                        if candidate in selected:
                            raise AssertionError("independent source two-swap overcount")
                        selected[candidate]=deleted
    return {
        "old_original_six_flags":tuple(sorted(F)),
        "brute_original_source_accepted_two_swaps":set(selected),
        "independent_same_hub_repeated_point_pairs_checked":star_x_population,
        "no_two_exchange_non_D6_sevenclass":True,
    }


def certified_family_k32_extension_mass(k32_pairs,flags,f,g, *,
                                         adjacency=None,provenance=None,
                                         check_classifier=True):
    """Exact positive original D6 count from any distinct K3,2 SOURCE sixsets.

    Sixfold multiplicity bound independent of source size/map statistics.
    Family can be saturated in a selected graph or ANY coordinate-proper
    original-backed physical K3,2 (the latter proves sharpness of 6).
    """
    if adjacency is None or provenance is None:
        adjacency,provenance=physical(range(len(flags)),flags,f,g)
    parents=set()
    accepted_to_parents=defaultdict(set)
    local_sum=0
    for hubs,frees in k32_pairs:
        out=one_k32_original_two_exchange(
            hubs,frees,flags,f,g,full_adjacency=adjacency,
            full_provenance=provenance,check_classifier=check_classifier)
        F=out["old_original_six_flags"]
        if F in parents:
            raise ValueError("same original sixset K3,2 counted twice")
        parents.add(F)
        local_sum+=out["two_exchange_accepted_original_D6"]
        for accepted in out["source_accepted_sixsets"]:
            accepted_to_parents[accepted].add(F)
    if any(len(ps)>6 for ps in accepted_to_parents.values()):
        raise AssertionError("universal six-parent C6 reconstruction bound false")
    if local_sum>6*len(accepted_to_parents):
        raise AssertionError("global positive original D6 multiplicity bound false")
    return {
        "distinct_original_K32_source_sixsets":len(parents),
        "two_exchange_D6_parent_witness_mass":local_sum,
        "distinct_accepted_original_GF5_D6_sixsets":
            len(accepted_to_parents),
        "max_actual_parent_multiplicity":
            max(map(len,accepted_to_parents.values()),default=0),
        "exact_distinct_accepted_D6_source_sixsets":
            tuple(sorted(accepted_to_parents)),
        "all_h_global_sixfold_multiplicity_bound_proved":True,
        "certified_D6_lower_numerator":local_sum,
        "certified_D6_lower_denominator":6,
        "all_h_universal_S_omega_s6_proved":False,
    }
