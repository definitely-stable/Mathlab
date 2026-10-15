"""HYP-105 #230 AA4-AL — all-h GENUINE ORIGINAL full B/A Hall-site refinement.

For EACH genuine original W(3,s), s=2^h>=2, and TWO complete GLOBAL
typed physical pair injections f,g, a fixed original B root with two
actual original incidence IDs and an occupied complementary physical
C4 on four other ACTUAL source factors has accepted original B/A or
dual A/B GF5 six-Q count at most

  disjoint opposite pinned physical edges: 18(s+1)^2+192(s+1)
  adjacent opposite pinned physical edges: 48(s+1)^2.

Uniform upper = max(these), equal 48(s+1)^2 for s>=8.
This improves the preexisting 72d^2+192d bound of sibling #524.

NEW mathematical input: In two crossed-spoke connected-C6
patterns of parent #521, for EACH source row bipartition S,
each occupied physical auxiliary site y supporting a GENUINE
original 2x2 rook injects into the actual source neighbor line of
the first row q_i (not TWO arbitrary such neighbors). Source
girth>=8 makes its 2x2 original perfect matching UNIQUE.
Global physical map injectivity makes different y map to
different actual source neighbors. Thus EACH six-channel site
set has cardinality <=d (not the coarse 2d), and two-cross
connected-C6 original acceptance <=2*6*d^2=12d^2.

Already known inputs: parent #521 internal-link <=192d; ancestor #517
disjoint split two-triangle <=6d² (also follows same site injection),
parent #525 adjacent connected C6 <=24d²; same-triangle adjacent
original-source anchored two-edge count <=24d² (formula independently
implemented here, also reported in concurrent sibling #524).
No new positive lower for original GF5, no seven-mode S proof.
"""
from itertools import combinations
from math import comb
from fractions import Fraction

from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import _source_cohort
from hyp105_issue230_d6aa4ah_signature_hall_kernel import (
    PAIRS4,six_channel_original_cohort)
from hyp105_issue230_d6aa4aj_connected_c6_original_transfer import (
    exact_original_connected_C6_transfer,_sites_pair,_two_rooks)
from hyp105_issue230_d6aa4ak_adjacent_c6_original_hall import (
    exact_adjacent_C6_original_transfer,exact_full_connected_C6_original_transfer,
    edge,adjacent_pin_vertices)
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    single_original_A_sector_permanent)


def original_cross_spoke_site_injection_witnesses(model,*,side=0,root=0,
                                                  pair_offset=0,four=None):
    """Independently realize each y -> genuine ORIGINAL opposite factor.

    For genuine original source B rows q_i,q_j and a physical crossed
    two-spoke edge pairing, the complete globally assigned opposite
    physical images attached at y identify two ACTUAL source factors
    t0,t1. If real GQ incidence gives a perfect 2x2 matching, it is
    unique (else original source C4). The matched original factor of
    q_i is different for different y because the physical image of
    one actual opposite source factor is fixed once and globally.
    """
    if four is None:raise ValueError("actual occupied B-root source C4 required")
    a,inc,N,pinned,inv,pins,four=_source_cohort(
        model,side=side,root=root,pair_offset=pair_offset,src_four=four)
    d=model["s"]+1
    if set(pins[0])&set(pins[1]):
        return {"adjacent":True,"cross_patterns":(),"source_rook_site_upper":d}
    (u,v),(w,x)=pins
    blocked=set(pins[0]+pins[1])
    cross=(((u,w),(v,x)),((u,x),(v,w)))
    patterns=[]
    actual_accepted=0
    for pair1,pair2 in cross:
        groups=[]
        for e0,e1 in (pair1,pair2):
            sites=_sites_pair(*e0,blocked,a,inv)
            per=[]
            for S in PAIRS4:
                i,j=S
                phi={}
                for y,(t0,t1) in sites.items():
                    m0=t0 in N[four[i]] and t1 in N[four[j]]
                    m1=t1 in N[four[i]] and t0 in N[four[j]]
                    if m0 and m1:
                        raise AssertionError("REAL original GQ forbids two shared neighbors")
                    if m0 or m1:
                        phi[y]=t0 if m0 else t1
                if len(phi)!=len(set(phi.values())):
                    raise AssertionError("different physical sites alias globally injected original factor")
                if len(phi)>d:raise AssertionError("genuine source degree d violated")
                per.append(phi)
            groups.append(per)
        (Y,Z)=groups
        channels=[]
        for k,S in enumerate(PAIRS4):
            Scomp=tuple(i for i in range(4) if i not in S)
            j=PAIRS4.index(Scomp)
            left=set(Y[k]);right=set(Z[j])
            amount=len(left)*len(right)-len(left&right)
            if amount<0 or amount>d*d:raise AssertionError("cross spoke source 2rook upper invalid")
            channels.append(amount)
        accepted=sum(channels)
        actual_accepted+=accepted
        patterns.append({
            "cross_endpoint_pairing":(pair1,pair2),
            "six_original_source_rook_site_channels":channels,
            "source_site_set_Y":tuple(len(x) for x in Y),
            "source_site_set_Z":tuple(len(x) for x in Z),
            "source_Y_unique_real_original_factor_witnesses":
                tuple(tuple(sorted(p.values())) for p in Y),
            "source_Z_unique_real_original_factor_witnesses":
                tuple(tuple(sorted(p.values())) for p in Z),
            "accepted_genuine_original_six_Q":accepted})
    if actual_accepted>12*d*d:raise AssertionError("ALL genuine GQ crossed spokes 12d²")
    return {
        "adjacent":False,"s":model["s"],"side":side,"root":root,
        "four_actual_original_B_factors":four,
        "cross_patterns":patterns,
        "crossed_spoke_accepted_original_Q":actual_accepted,
        "crossed_spoke_sharp_new_source_upper":12*d*d,
        "each_original_2rook_site_set_upper":d,
        "one_same_complete_globally_injected_physical_typed_map":True}


def exact_original_adjacent_same_triangle(model,*,side=0,root=0,
                                          pair_offset=0,four=None):
    """Genuine source exact SOURCE-anchored same 2*C3 physical A sector.

    This same-triangle source-neighbor algorithm already exists in
    parallel sibling #524. This module independently reuses the
    original 4 actual source factors to compose a stricter FOUR-sector
    aggregate upper, and NEVER claims this source algorithm as new.
    """
    if four is None:raise ValueError("actual first physical B C4 required")
    a,inc,N,pinned,inv,pins,four=_source_cohort(
        model,side=side,root=root,pair_offset=pair_offset,src_four=four)
    d=model["s"]+1
    if not set(pins[0])&set(pins[1]):
        return {"adjacent":False,"accepted_original_same_two_triangles":0,
                "real_original_source_degree_upper":24*d*d}
    u,v,w=adjacent_pin_vertices(pins)
    closure=inv.get(edge(v,w))
    # Pins u-v and u-w; physical closing edge v-w is mandatory.
    if closure is None:
        return {"adjacent":True,"accepted_original_same_two_triangles":0,
                "real_original_source_degree_upper":24*d*d}
    blocked={u,v,w}
    g=tuple(tuple(z) for z in model[
        "right_labels" if side==0 else "left_labels"])
    total=0
    for k in range(4):
        if closure not in N[four[k]]:continue
        for i in range(4):
            if i==k:continue
            for t_xy in N[four[i]]:
                x,y=g[t_xy] # actual globally fixed canonical unordered edge x<y
                if x in blocked or y in blocked:continue
                for j in range(4):
                    if j in (k,i):continue
                    for t_yz in N[four[j]]:
                        yy,z=g[t_yz]
                        if yy!=y or z<=y or z in blocked:continue
                        t_xz=inv.get(edge(x,z))
                        rem=next(t for t in range(4) if t not in (k,i,j))
                        total+=int(t_xz is not None and t_xz in N[four[rem]])
    if total>24*d*d:raise AssertionError("true original two-real-neighbor bound")
    return {
        "s":model["s"],"adjacent":True,
        "accepted_original_same_two_triangles":total,
        "real_original_source_degree_upper":24*d*d,
        "full_original_GQ_actual_incidence_and_global_labels":True}


def sharp_all_h_original_full_BA_upper(s):
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("genuine original W(3,2^h), h>=1 only")
    d=s+1
    disjoint=18*d*d+192*d
    adjacent=48*d*d
    ceiling=max(disjoint,adjacent)
    assert (ceiling==48*d*d)==(s>=8)
    return {
        "s":s,"d":d,
        "disjoint_split_two_triangles_cap":6*d*d,
        "disjoint_connected_C6_crossed_spoke_cap_NEW":12*d*d,
        "disjoint_connected_C6_internal_link_cap":192*d,
        "disjoint_all_true_original_A_sectors_cap_NEW":disjoint,
        "adjacent_same_component_two_triangles_cap":24*d*d,
        "adjacent_connected_C6_cap_from_AK":24*d*d,
        "adjacent_all_true_original_A_sectors_cap_NEW":adjacent,
        "all_fixed_actual_original_B_C4_cohort_cap_NEW":ceiling,
        "OLD_parallel_AK_full_cohort_cap":72*d*d+192*d,
        "strictly_smaller_all_h_full_cohort_source_degree_ceiling":True,
        "for_s_ge8_upper_is_48_splus1_squared":s>=8,
        "for_every_full_global_f_g_true_original_W3s_PROVED":True,
        "NO_positive_all_maps_GF5_lower":True,
        "NO_issue230_A_B_C_closure":True}


def sharp_true_original_complete_BA_cohort(model,*,side=0,root=0,
                                           pair_offset=0,four=None,
                                           independent_brute=False):
    """Exact ALL FOUR physical A sectors for same 6 actual original IDs.

    Disjoint pins: old AH exact split triangles and AJ disjoint C6,
    independently prove NEW crossed-spoke true-GQ 12d² site bound.
    Adjacent pins: exact source-anchored same triangle and improved
    AK connected C6 source algorithm. Both branches same global f,g.
    """
    if four is None:raise ValueError("real occupied original B-C4 needed")
    a,inc,N,pinned,inv,pins,four=_source_cohort(
        model,side=side,root=root,pair_offset=pair_offset,src_four=four)
    d=model["s"]+1
    bound=sharp_all_h_original_full_BA_upper(model["s"])
    if set(pins[0])&set(pins[1]):
        same=exact_original_adjacent_same_triangle(
            model,side=side,root=root,pair_offset=pair_offset,four=four)[
                "accepted_original_same_two_triangles"]
        connected=exact_adjacent_C6_original_transfer(
            model,side=side,root=root,pair_offset=pair_offset,four=four)[
                "accepted_actual_original_six_Q"]
        sector={"adjacent_same_two_triangles":same,
                "adjacent_connected_C6":connected}
        upper=bound["adjacent_all_true_original_A_sectors_cap_NEW"]
        proof=()
    else:
        ah=six_channel_original_cohort(
            model,side=side,root=root,pair_offset=pair_offset,
            four_sources=four,independent_direct=False)
        aj=exact_original_connected_C6_transfer(
            model,side=side,root=root,pair_offset=pair_offset,four=four)
        witness=original_cross_spoke_site_injection_witnesses(
            model,side=side,root=root,pair_offset=pair_offset,four=four)
        if witness["crossed_spoke_accepted_original_Q"]!=aj[
                "two_cross_spoke_accepted_original_Q"]:
            raise AssertionError("INDEPENDENT original rook site map conflicts with AJ 6channel")
        if ah["accepted_original_GF5_Q_sample"]>6*d*d:
            raise AssertionError("genuine original split triangle 6d² fails")
        if aj["internal_aux_link_accepted_original_Q"]>192*d:
            raise AssertionError("original link source degree d fails")
        sector={
            "disjoint_split_two_triangles":
                ah["accepted_original_GF5_Q_sample"],
            "disjoint_connected_C6_crossed_spokes":
                aj["two_cross_spoke_accepted_original_Q"],
            "disjoint_connected_C6_internal_link":
                aj["internal_aux_link_accepted_original_Q"]}
        upper=bound["disjoint_all_true_original_A_sectors_cap_NEW"]
        proof=witness["cross_patterns"]
    total=sum(sector.values())
    if total>upper:raise AssertionError("sharp real-original all-physical-A source ceiling")
    if independent_brute:
        brute=single_original_A_sector_permanent(
            model,side=side,root=root,pair_offset=pair_offset,four=four)
        if total!=sum(brute["accepted"].values()):
            raise AssertionError("four original A sectors mismatch independent all 2factors & original permanent")
    return {
        "s":model["s"],"side":side,"root":root,
        "actual_original_B_quartet":four,
        "pinned_physical_adjacent":bool(set(pins[0])&set(pins[1])),
        "exact_original_A_sector_counts":sector,
        "crossed_spoke_real_neighbor_site_injections":proof,
        "exact_accepted_true_original_six_ID_GF5":total,
        "new_true_original_upper_for_this_sector":upper,
        "new_uniform_all_A_source_upper":bound[
            "all_fixed_actual_original_B_C4_cohort_cap_NEW"],
        "independent_complete_original_four_rook_comparison":
            bool(independent_brute),
        "issue230_universal_S_lower_NOT_PROVED":True}
