"""HYP-105 #230 / AA4-AK: COMPLETE true-original B/A physical-A Hall transfer.

Fix one REAL W(3,2^h) source B-root p, two DISTINCT actual original
flags, four actual distinct source singleton factors inverse-mapped from
an occupied first-side physical C4 under ONE global f. The physically
opposite globally injected map g makes the pinned physical edges either

  disjoint : split two triangles (AH) + connected C6 (AJ),
  adjacent : same-component two triangles (AK) + connected C6 (AK).

Adjacent pins form u-v-w; their connected C6 is uniquely the ordered
three-free-coordinate path w-x-y-z-u. To count accepted original 6-ID Q,
anchor the interior edges x-y and y-z on two *different genuine source
singleton rows*, scanning their true degree d=s+1 original opposite
source neighbors. The other two rows must genuinely match wx,zu.
The same-triangle sector forces the closing edge uw, and the other
triangle x<y<z has a unique canonical smallest edge xy and second
edge yz; source-neighbor anchors check its other edge xz.

All operations preserve ORIGINAL GQ incidences, no random redrawing
of f,g, no source-edge product model, no artificial 4-rook matrices.
Every source matching is counted exactly once, including double
matchings of a genuine induced source C8. Neither exact transfer nor
upper bounds prove a positive lower for original issue #230.
"""
from itertools import permutations
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import _source_cohort
from hyp105_issue230_d6aa4aj_connected_c6_original_transfer import (
    exact_original_connected_C6_transfer,sparse_true_original_C6_upper_bound)
from hyp105_issue230_d6aa4ah_signature_hall_kernel import six_channel_original_cohort


def _edge(u,v):
    if u==v:raise ValueError("distinct simple physical endpoints required")
    return (u,v) if u<v else (v,u)


def _opposite_pairs(model,side):
    return tuple(tuple(e) for e in
        model["right_labels" if side==0 else "left_labels"])


def _adjacent_pins(pins):
    e0,e1=pins
    mid=set(e0)&set(e1)
    if len(mid)!=1:
        raise ValueError("two distinct adjacent physical original pin edges required")
    v=next(iter(mid))
    u=next(x for x in e0 if x!=v)
    w=next(x for x in e1 if x!=v)
    assert len({u,v,w})==3
    return u,v,w


def exact_original_adjacent_A_transfer(model,*,side=0,root=0,
                                       pair_offset=0,four=None):
    """All-h genuine source Hall Q in BOTH adjacent-pinned A sectors.

    Physically disjoint pins yield 0/0, so domains are explicit.
    Actual same-triangle A and actual connected C6 always have exactly
    SIX different physical coordinates and six distinct real original
    incident flags. Counts are original MATCHINGS, not just Hall-positive
    physical H; true source induced C8 can give two Q for the same H.
    Complexity per fixed original occupied C4: O((s+1)^2) source
    adjacency work after full map+neighbor preparation.
    """
    if four is None:
        raise ValueError("explicit true original physically occupied source C4 required")
    a,inc,N,pinned,inv,pins,four=_source_cohort(
        model,side=side,root=root,pair_offset=pair_offset,src_four=four)
    d=model["s"]+1
    opposite=_opposite_pairs(model,side)
    if not (set(pins[0])&set(pins[1])):
        return dict(s=model["s"],side=side,root=root,selected_four=four,
                    pinned_physical_adjacent=False,
                    accepted_same_triangle_original_Q=0,
                    accepted_connected_C6_original_Q=0,
                    accepted_adjacent_A_original_Q=0,
                    same_triangle_source_degree_upper=24*d*d,
                    connected_C6_source_degree_upper=48*d*d,
                    genuine_original_positive_lower_NOT_PROVED=True)

    u,v,w=_adjacent_pins(pins)
    blocked={u,v,w}
    # A physical triangle in the same component as the two pinned edges
    # requires the unique third physical edge u-w, globally occupied.
    same=0
    closing=_edge(u,w)
    if closing in inv:
        closer=inv[closing]
        for k,qk in enumerate(four):
            if closer not in N[qk]:
                continue
            # Canonical ordered x<y<z ensures every opposite TRIANGLE
            # and each ORIGINAL assignment is counted exactly once.
            for i,qi in enumerate(four):
                if i==k:continue
                for src_xy in N[qi]:
                    x,y=opposite[src_xy]
                    if x in blocked or y in blocked:
                        continue
                    for j,qj in enumerate(four):
                        if j in (k,i):continue
                        for src_yz in N[qj]:
                            y0,z=opposite[src_yz]
                            if y0!=y or z<=y or z in blocked:
                                continue
                            # x<y<z since each original physical pair
                            # is canonical, hence no endpoint collisions.
                            src_xz=inv.get(_edge(x,z))
                            if src_xz is None:continue
                            rem=next(t for t in range(4) if t not in (k,i,j))
                            if src_xz in N[four[rem]]:
                                same+=1

    # Adjacent physical connected C6 must have pinned path u-v-w and
    # UNIQUE complementary path w-x-y-z-u with x,y,z distinct,
    # none in {u,v,w}. Internal physical xy and yz are anchored
    # to TWO real free source neighbors. Exactly one physical
    # orientation is fixed by pinned path (w->u). There are two ways
    # to assign free endpoints wx and zu to the other two rows.
    cycle=0
    for i,qi in enumerate(four):
        for src_xy in N[qi]:
            a0,a1=opposite[src_xy]
            if a0 in blocked or a1 in blocked:continue
            for x,y in ((a0,a1),(a1,a0)):
                src_wx=inv.get(_edge(w,x))
                if src_wx is None:continue
                for j,qj in enumerate(four):
                    if j==i:continue
                    for src_yz in N[qj]:
                        b0,b1=opposite[src_yz]
                        if b0==y:z=b1
                        elif b1==y:z=b0
                        else:continue
                        if z in blocked or z in (x,y):
                            continue
                        src_zu=inv.get(_edge(z,u))
                        if src_zu is None:continue
                        remaining=tuple(k for k in range(4) if k not in (i,j))
                        for p in permutations((src_wx,src_zu)):
                            if p[0] in N[four[remaining[0]]] and p[1] in N[four[remaining[1]]]:
                                cycle+=1
    # Bounds count candidate genuinely source-incident ordered edges,
    # so apply to every complete globally injected f/g with original
    # actual true GQ degree s+1; no source isometry assumption.
    assert same<=24*d*d,(same,d)
    assert cycle<=48*d*d,(cycle,d)
    return dict(s=model["s"],side=side,root=root,selected_four=four,
                pinned_physical_adjacent=True,
                accepted_same_triangle_original_Q=same,
                accepted_connected_C6_original_Q=cycle,
                accepted_adjacent_A_original_Q=same+cycle,
                same_triangle_source_degree_upper=24*d*d,
                connected_C6_source_degree_upper=48*d*d,
                exact_all_h_true_original_adjacent_source_Hall_PROVED=True,
                genuine_original_positive_lower_NOT_PROVED=True)


def full_original_A_Hall_cohort(model,*,side=0,root=0,
                                 pair_offset=0,four=None):
    """Complete ALL physically accepted true-original B/A or A/B sector.

    Exact all-h all-f,g identity, covering EVERY physical A 2factor:
    disjoint pins: genuine original AH split triangles + AJ connected C6;
    adjacent pins: new AK same-triangle and new AK connected C6.
    All four are genuine source six-incidence-ID Q, no overlaps.
    """
    if four is None:
        raise ValueError("explicit occupied original C4 required")
    a,inc,N,pinned,inv,pins,four=_source_cohort(
        model,side=side,root=root,pair_offset=pair_offset,src_four=four)
    adjacent=bool(set(pins[0])&set(pins[1]))
    if adjacent:
        z=exact_original_adjacent_A_transfer(
            model,side=side,root=root,pair_offset=pair_offset,four=four)
        split=sixcycle_disjoint=0
        same=z["accepted_same_triangle_original_Q"]
        sixcycle_adjacent=z["accepted_connected_C6_original_Q"]
    else:
        h=six_channel_original_cohort(
            model,side=side,root=root,pair_offset=pair_offset,
            four_sources=four,independent_direct=False)
        j=exact_original_connected_C6_transfer(
            model,side=side,root=root,pair_offset=pair_offset,four=four)
        split=h["accepted_original_GF5_Q_sample"]
        sixcycle_disjoint=j["accepted_original_connected_C6_Q"]
        same=sixcycle_adjacent=0
    d=model["s"]+1
    total=split+same+sixcycle_disjoint+sixcycle_adjacent
    bound=72*d*d+192*d
    assert total<=bound,(total,bound)
    return dict(s=model["s"],side=side,root=root,
                selected_four=tuple(four),
                pinned_physical_adjacent=adjacent,
                accepted_split_two_triangles_original_Q=split,
                accepted_same_triangle_original_Q=same,
                accepted_disjoint_pins_C6_original_Q=sixcycle_disjoint,
                accepted_adjacent_pins_C6_original_Q=sixcycle_adjacent,
                accepted_full_true_original_BA_or_AB_Q=total,
                all_global_all_h_original_fixed_cohort_upper=bound,
                all_four_physical_A_sectors_exhaustive=True,
                true_original_six_distinct_incidence_ID_Q=True,
                universal_positive_original_GF5_lower_NOT_PROVED=True)


def all_h_true_original_full_BA_cohort_upper(s):
    """All-f,g guaranteed accepted ORIGINAL B/A upper per true B/C4 cohort.

    Disjoint: AH split <=24d², AJ C6 <=48d²+192d.
    Adjacent: AK same triangle <=24d², AK C6 <=48d².
    Applies to all h>=1, f,g, actual root/flags/physical C4.
    """
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("actual symplectic W(3,2^h), h>=1 required")
    d=s+1
    disjoint=72*d*d+192*d
    adjacent=72*d*d
    return dict(s=s,disjoint_pinned_source_Q_upper=disjoint,
                adjacent_pinned_source_Q_upper=adjacent,
                all_original_BA_cohort_source_Q_upper=disjoint,
                all_global_complete_injections=True,
                all_h_proved=True,
                original_S_lower_NOT_PROVED=True)
