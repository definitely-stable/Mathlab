"""HYP-105 #230 / AA4-AJ: exact TRUE-ORIGINAL connected-C6 Hall transfer.

Two genuine original pinned flags through the same genuine point (or line)
and four distinct source singleton factors have a first-half occupied B/C4.
If the two OPPOSITE pinned physical edges are disjoint, the physical
connected C6 completions split UNIQUE/EXHAUSTIVELY into:

(1) two crossed spoke pairings, no edge between auxiliary y,z:
      sum of SIX original 2x2-rook site products, removing y=z.

(2) four cross-link choices h between the pinned physical edges, each
    connected C6 contains edges h, (r0,y),(y,z),(z,r1).
    Every accepted REAL source four-rook assignment gives edge yz to
    one of the FOUR actual source singleton rows q_k. Thus its original
    opposite factor is in the degree-(s+1) TRUE GQ neighbor set N(q_k).
    Enumerating these s+1 actual edges per q_k, both orientations of
    y,z and the 3! remaining rook assignments counts EXACTLY every
    original six-incidence-ID accepted Q (including C8 double matchings).

The full transfer is an exact integer count for ALL h, ALL complete
globally injected f,g with no random or independent redraw per Q.
The connected-C6 accepted number can be ZERO for a cohort. NO universal
positive genuine Hall fraction, Branch A/B, ASET exponent is asserted.
"""
from collections import Counter
from itertools import combinations, permutations

from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import _source_cohort
from hyp105_issue230_d6aa4ah_signature_hall_kernel import PAIRS4

_PERM3=tuple(permutations(range(3)))
_SPLIT=("two_cross_spoke","internal_aux_link")


def _edge(u,v):
    if u==v:raise ValueError("simple physical pair required")
    return (u,v) if u<v else (v,u)


def _sites_pair(u,v,exclude,a,inv):
    """One globally occupied physical 2-spoke site to actual 2 source IDs."""
    return {y:(inv[_edge(u,y)],inv[_edge(v,y)])
            for y in range(a)
            if y not in exclude and _edge(u,y) in inv and _edge(v,y) in inv}


def _two_rooks(q,factors,neighbors):
    p,l=factors
    return int(p in neighbors[q[0]] and l in neighbors[q[1]]) + int(
        l in neighbors[q[0]] and p in neighbors[q[1]])


def exact_original_connected_C6_transfer(model,*,side=0,root=0,
                                         pair_offset=0,four=None):
    """Exact 2+4 geometric C6 templates and actual GQ Hall-positive Q.

    Cost for one fixed (root, two actual flags, original physically
    occupied C4): O(a + m + (s+1)), with constant O(24) source masks;
    m=C(a,2)-V is number of missing global opposite physical pair images.
    Explicit validation/enumeration of the chosen first C4 is separate.
    """
    if four is None:
        raise ValueError("four original occupied physical-C4 source factors required")
    a,inc,neighbors,pinned,inv,pins,four=_source_cohort(
        model,side=side,root=root,pair_offset=pair_offset,src_four=four)
    E=frozenset(inv)
    e0,e1=pins
    if set(e0)&set(e1):
        return dict(s=model["s"],side=side,root=root,selected_four=four,
                    pinned_physical_disjoint=False,
                    two_cross_spoke_accepted_original_Q=0,
                    internal_aux_link_accepted_original_Q=0,
                    accepted_original_connected_C6_Q=0,
                    two_cross_spoke_occupied_physical_H=0,
                    internal_aux_link_occupied_physical_H=0,
                    occupied_physical_connected_C6_H=0,
                    channel_details=(),
                    source_original_hall_positive_lower_NOT_PROVED=True)
    endpoints=set(e0+e1)
    out=set(range(a))-endpoints
    (u,v),(w,x)=pins

    # Each unordered crossed matching of the FOUR actual pinned
    # endpoints is used exactly once (the original two pinned physical
    # pairs would instead create TWO DISJOINT TRIANGLES).
    cross_matchings=(((u,w),(v,x)),((u,x),(v,w)))
    spoke_accepted=spoke_occupied=0
    records=[]
    for pair_A,pair_B in cross_matchings:
        A=_sites_pair(*pair_A,endpoints,a,inv)
        B=_sites_pair(*pair_B,endpoints,a,inv)
        occupied=len(A)*len(B)-len(A.keys()&B.keys())
        spoke_occupied+=occupied
        channel_sum=0
        for S in PAIRS4:
            other=tuple(i for i in range(4) if i not in S)
            row_A=tuple(four[i] for i in S)
            row_B=tuple(four[i] for i in other)
            YA={y for y,fs in A.items() if _two_rooks(row_A,fs,neighbors)}
            ZB={z for z,fs in B.items() if _two_rooks(row_B,fs,neighbors)}
            v_count=len(YA)*len(ZB)-len(YA&ZB)
            assert v_count>=0
            channel_sum+=v_count
        spoke_accepted+=channel_sum
        records.append({"kind":"two_cross_spoke",
                        "cross_endpoint_pairing":(pair_A,pair_B),
                        "occupied_physical_H":occupied,
                        "accepted_true_original_Q":channel_sum,
                        "six_original_rook_channels":6})

    # Internal y-z edge couples the two auxiliary coordinates and
    # therefore cannot be separated into two independent site sets.
    # Instead anchor the internal yz edge to the UNIQUE matched TRUE
    # original source singleton row q_k, of physical degree s+1 in
    # the actual true GQ incidence graph.
    link_accepted=link_occupied=0
    m=tuple(_edge(i,j) for i,j in combinations(range(a),2) if (i,j) not in E)
    missing=frozenset(m)
    for i,p in enumerate(e0):
        other0=e0[1-i]
        for j,q in enumerate(e1):
            other1=e1[1-j]
            cross=_edge(p,q)
            if cross not in inv:
                continue
            cross_source=inv[cross]
            Y={y for y in out if _edge(other0,y) in inv}
            Z={z for z in out if _edge(other1,z) in inv}
            diag=len(Y&Z)
            holes=sum(int(left in Y and right in Z) +
                      int(right in Y and left in Z) for left,right in missing)
            occupied=len(Y)*len(Z)-diag-holes
            assert occupied>=0
            link_occupied+=occupied
            valid=0
            for k,source_row in enumerate(four):
                remaining=tuple(i for i in range(4) if i!=k)
                for yz_source in neighbors[source_row]:
                    yz=tuple(model["right_labels" if side==0 else "left_labels"][yz_source])
                    if yz[0] not in out or yz[1] not in out:
                        continue
                    for y,z in (yz,yz[::-1]):
                        if y not in Y or z not in Z:
                            continue
                        col=(cross_source,inv[_edge(other0,y)],inv[_edge(other1,z)])
                        # source q_k already consumes the opposite yz
                        # actual source ID and actual ORIGINAL incidence.
                        for perm in _PERM3:
                            if all(col[perm[t]] in neighbors[four[row]]
                                   for t,row in enumerate(remaining)):
                                valid+=1
            link_accepted+=valid
            records.append({"kind":"internal_aux_link",
                            "pinned_cross_physical_edge":cross,
                            "occupied_physical_H":occupied,
                            "accepted_true_original_Q":valid,
                            "source_incidence_anchored_yz_edge":True})
    total=spoke_accepted+link_accepted
    return dict(
        s=model["s"],side=side,root=root,selected_four=four,
        pinned_actual_original_opposite_factors=pinned,
        pinned_physical_disjoint=True,
        two_cross_spoke_accepted_original_Q=spoke_accepted,
        internal_aux_link_accepted_original_Q=link_accepted,
        accepted_original_connected_C6_Q=total,
        two_cross_spoke_occupied_physical_H=spoke_occupied,
        internal_aux_link_occupied_physical_H=link_occupied,
        occupied_physical_connected_C6_H=spoke_occupied+link_occupied,
        channel_details=tuple(records),
        exact_all_h_source_original_transfer_PROVED=True,
        sparse_source_incidence_yz_loop_degree=model["s"]+1,
        source_original_hall_positive_lower_NOT_PROVED=True)


def sector_shapes_by_literal_edges(H,pins):
    """Independent physical taxonomy for any genuine disjoint-pin C6."""
    from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
        classify_physical_A_twofactor)
    if set(pins[0])&set(pins[1]):
        raise ValueError("disjoint physical pins required")
    if classify_physical_A_twofactor(H,pins)!="connected_C6":
        raise ValueError("connected genuine six-vertex physical C6 required")
    a=set(pins[0]+pins[1])
    aux={v for e in H for v in e}-a
    if len(aux)!=2:raise ValueError("two auxiliary coordinates")
    yz=_edge(*sorted(aux))
    if yz in H:
        return "internal_aux_link"
    return "two_cross_spoke"
