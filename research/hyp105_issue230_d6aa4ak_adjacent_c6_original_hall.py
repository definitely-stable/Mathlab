"""HYP-105 #230 AA4-AK: genuine-ORIGINAL adjacent-pinned connected C6.

If opposite physical pins uv and uw share u, every connected six-vertex
C6 has the UNIQUE oriented path v-u-w-a-b-c-v. Assign internal physical
edges ab,bc to distinct original B singleton source rows qk,ql, anchor
the corresponding two opposite actual original source factors to their
genuine GQ neighbors (at most d²), and test both assignments of the
remaining two original B singleton rows to outer physical edges
w-a,c-v. Counts exact same original six-distinct-incidence Q under
arbitrary separately complete globally injected typed point/line maps.
GQ per-root C4 upper T<=24(s+1)²; no positive Hall bound.

Physical occupancy conditional on D(v),D(w)<a/16 and a>=94:
occupied C6 >= (a-3)(a-4)(a-5)
  -(a/8)(a-4)(a-5)-4m(a-5) >= a³/2.
Then Hall-positive fraction <=48(s+1)²/a³ = O(s^-5/2),
not a proof of nonzero accepted original GF5.
"""
from itertools import combinations
from fractions import Fraction
from math import comb
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    _source_cohort,classify_physical_A_twofactor)
from hyp105_issue230_d6aa4ad_opposite_a_hall_transfer import pinned_twofactor_completions
from hyp105_issue230_d6aa4ae_gq_girth8_sharp_rook import true_gq_four_rook
from hyp105_issue230_d6aa4ag_deterministic_triangle_hall import minimal_alphabet

def edge(u,v):
    if u==v: raise ValueError("simple physical pair required")
    return (u,v) if u<v else (v,u)

def adjacent_pin_vertices(pins):
    a,b=pins
    common=set(a)&set(b)
    if len(common)!=1 or a==b:raise ValueError("genuine adjacent distinct physical pins required")
    u=next(iter(common))
    v=next(x for x in a if x!=u)
    w=next(x for x in b if x!=u)
    return u,v,w

def exact_adjacent_C6_original_transfer(model,*,side=0,root=0,pair_offset=0,four=None):
    """All-h original accepted Q: 12 original ordered internal row pairs,
    d² real neighbor-pairs, at most two remaining original-row matches.
    O(24d²) source incidence tests, not O(a³) physical path listing."""
    if four is None:raise ValueError("occupied actual original B-C4 quartet required")
    a,inc,neighbors,pinned,inv,pins,four=_source_cohort(
        model,side=side,root=root,pair_offset=pair_offset,src_four=four)
    d=model["s"]+1
    if not set(pins[0])&set(pins[1]):
        return {"adjacent":False,"accepted_actual_original_six_Q":0,
                "original_degree_upper":24*d*d}
    u,v,w=adjacent_pin_vertices(pins)
    endpoints={u,v,w}
    labels=tuple(tuple(x) for x in model[
        "right_labels" if side==0 else "left_labels"])
    tally=0;rows=[]
    for k in range(4):
        for ell in range(4):
            if ell==k:continue
            remaining=tuple(i for i in range(4) if i not in (k,ell))
            subtotal=0
            for ab_src in neighbors[four[k]]:
                ab=labels[ab_src]
                if set(ab)&endpoints:continue
                for bc_src in neighbors[four[ell]]:
                    if bc_src==ab_src:continue
                    bc=labels[bc_src]
                    intersection=set(ab)&set(bc)
                    if len(intersection)!=1:continue
                    mid=next(iter(intersection))
                    alpha=next(x for x in ab if x!=mid)
                    gamma=next(x for x in bc if x!=mid)
                    if len({alpha,mid,gamma})!=3 or endpoints&{alpha,mid,gamma}:continue
                    first=inv.get(edge(w,alpha))
                    last=inv.get(edge(gamma,v))
                    if first is None or last is None:continue
                    subtotal+=int(first in neighbors[four[remaining[0]]] and
                                  last in neighbors[four[remaining[1]]])
                    subtotal+=int(last in neighbors[four[remaining[0]]] and
                                  first in neighbors[four[remaining[1]]])
            if subtotal>2*d*d:raise AssertionError("original GQ two-source degree bound failed")
            rows.append({"original_internal_row_pair_ab_bc":(k,ell),
                         "accepted_six_distinct_actual_original_Q":subtotal})
            tally+=subtotal
    if len(rows)!=12 or tally>24*d*d:raise AssertionError("original C6 degree upper invalid")
    return {"s":model["s"],"side":side,"root":root,"four_actual_original_B_factors":four,
            "actual_two_pinned_original_opposite_factors":pinned,
            "opposite_physical_pins":pins,
            "adjacent":True,"oriented_unique_physical_C6_path":"v-u-w-a-b-c-v",
            "channel_results":rows,
            "accepted_actual_original_six_Q":tally,
            "original_degree_upper":24*d*d,
            "all_h_exact_true_original_six_Q_transfer":True,
            "root_issue230_all_f_g_lower_NOT_PROVED":True}

def independent_complete_physical_adjacent_C6_oracle(model,*,side,root,pair_offset,four):
    """Independent full original Hall permanent on EVERY occupied C6 H,
    including both original C8 matching multiplicities."""
    a,inc,neighbors,pinned,inv,pins,four=_source_cohort(
        model,side=side,root=root,pair_offset=pair_offset,src_four=four)
    if not set(pins[0])&set(pins[1]):
        return {"adjacent":False,"occupied_C6":0,"accepted_original_Q":0,
                "Hall_positive_C6":0,"real_original_C8_extra":0}
    raw=occupied=accepted=positive=C8=0
    for H in pinned_twofactor_completions(*pins,a):
        if classify_physical_A_twofactor(H,pins)!="connected_C6":continue
        raw+=1
        other=tuple(x for x in H if x not in pins)
        if any(e not in inv for e in other):continue
        occupied+=1
        real_columns=tuple(inv[e] for e in other)
        masks=tuple(sum(1<<j for j,t in enumerate(real_columns)
                        if t in neighbors[q]) for q in four)
        chk=true_gq_four_rook(masks)
        if not chk["gq_girth_eight_eligible"]:raise AssertionError("not genuine original W3s")
        n=chk["true_original_four_rook_permanent"]
        accepted+=n;positive+=int(n>0);C8+=int(n==2)
    if accepted!=positive+C8 or raw!=(a-3)*(a-4)*(a-5):
        raise AssertionError("source girth8 or adjacent physical raw C6 count")
    return {"adjacent":True,"raw_complete_Ka_adjacent_C6":raw,
            "occupied_C6":occupied,"accepted_original_Q":accepted,
            "Hall_positive_C6":positive,"real_original_C8_extra":C8}

def adjacent_low_hole_occupied_C6_all_h(s):
    """ALL complete physical injections g and any adjacent pins whose
    NONSHARED physical endpoint missing-edge degrees are each <a/16.
    The shared physical endpoint's hole-degree is IRRELEVANT for the
    OTHER four physical C6 edges."""
    V,a,m=minimal_alphabet(s)
    d=s+1
    raw=(a-3)*(a-4)*(a-5)
    lower=Fraction(raw)-Fraction(a,8)*(a-4)*(a-5)-4*m*(a-5)
    if s>=16:
        assert a>=94
        assert lower>=Fraction(a**3,2)
        assert 48*d*d<a**3
    return {"s":s,"a":a,"K":comb(a,2),"V":V,"m":m,
            "raw_complete_adjacent_C6":raw,
            "CONDITIONAL_outer_pins_both_missing_degree_lt_a_over_16":True,
            "all_global_opposite_maps_physical_occupied_C6_floor":str(max(0,lower)),
            "genuine_original_C6_accept_upper_per_root_B_C4":24*d*d,
            "Hall_positive_fraction_upper_under_low_holes":
                str(Fraction(48*d*d,a**3)) if s>=16 else "not asserted",
            "all_global_low_holes_Hall_rejected_fraction_ge_1_minus_48d2_a3":
                s>=16,
            "unconditional_positive_Hall_mass_NOT_PROVED":True}

def adjacent_original_rootpair(model,side):
    """Select one ACTUAL original root with two different real flags
    whose assigned opposite physical images are adjacent."""
    inc=tuple(tuple(x) for x in model["incidences"])
    labels=tuple(tuple(x) for x in model[
        "right_labels" if side==0 else "left_labels"])
    v=len(model["left_labels"])
    for root in range(v):
        factors=tuple(sorted(e[1-side] for e in inc if e[side]==root))
        for offset,(i,j) in enumerate(combinations(factors,2)):
            if set(labels[i])&set(labels[j]):return root,offset
    raise ValueError("no ACTUAL original source root physically adjacent flags")


def exact_full_connected_C6_original_transfer(model,*,side=0,root=0,
                                              pair_offset=0,four=None):
    """FULL genuine ORIGINAL connected-C6 accepted Q, ALL global f,g.

    The two distinct actual original opposite pinned factor edge images
    are either physically adjacent (new AK 12-channel theorem) or
    disjoint (prior AJ 2+4 geometric connected-C6 theorem). Cases
    disjoint, exhaustive, same original source 6-ID Q and global maps.
    Counts genuine original matching multiplicities, including C8.
    """
    from hyp105_issue230_d6aa4aj_connected_c6_original_transfer import (
        exact_original_connected_C6_transfer)
    if four is None:raise ValueError("real original B-physical C4 required")
    a,inc,neighbors,pinned,inv,pins,four=_source_cohort(
        model,side=side,root=root,pair_offset=pair_offset,src_four=four)
    if set(pins[0])&set(pins[1]):
        z=exact_adjacent_C6_original_transfer(
            model,side=side,root=root,pair_offset=pair_offset,four=four)
        sector="adjacent";n=z["accepted_actual_original_six_Q"]
        physical=None;cap=24*(model["s"]+1)**2
    else:
        z=exact_original_connected_C6_transfer(
            model,side=side,root=root,pair_offset=pair_offset,four=four)
        sector="disjoint";n=z["accepted_original_connected_C6_Q"]
        physical=z["occupied_physical_connected_C6_H"]
        cap=48*(model["s"]+1)**2+192*(model["s"]+1)
    if n>cap:raise AssertionError("all-h full connected original source cap")
    return {"s":model["s"],"side":side,"root":root,
            "four_actual_original_B_factors":four,
            "pinned_opposite_physical_relation":sector,
            "accepted_full_CONNECTED_C6_actual_original_six_Q":n,
            "occupied_physical_C6_if_disjoint":physical,
            "actual_original_source_degree_upper_for_chosen_sector":cap,
            "adjacent_and_disjoint_exhaust_original_connected_C6":True,
            "same_two_complete_global_typed_maps_used_for_every_original_Q":True,
            "all_seven_GF5_universal_S_lower_NOT_PROVED":True}
