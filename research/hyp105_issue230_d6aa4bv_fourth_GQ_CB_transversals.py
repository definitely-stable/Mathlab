"""HYP-105 #230 AA4-BV: FOURTH Walsh ORIGINAL GQ C/B source bound.

ALL s=2^h, h>=1; any COMPLETE correlated globally injected ORIGINAL
typed f,g and any FOUR pairwise DISJOINT WHOLE-original-LINE-factor
image swap packets. A true six-DISTINCT-original-incidence Q that can
contribute to fourth Walsh must hit all four source LINE packets.

If source POINT profile is C=(2,2,2), source LINE profile B=(2,1,1,1,1),
its FIVE genuinely different original LINE IDs include one from EACH
packet and a fifth either INSIDE a packet or OUTSIDE all 4 packets.

All-inside <= 960 genuine Q.
Outside repeated LINE <= 96d by the ORIGINAL GQ transversal lemma.
Outside singleton LINE <= 192(2d-1)(d-1).
Thus N4,C/B <= 960+96d+192(2d-1)(d-1), and
|hat S_C/B([4])| <= half this capacity for EVERY fixed f,g.
It refines t=6 zero, t=5 960 (AA4-BU) into t=4 O(d^2).
NOT a lower on the UNCHANGED center / root Branch A/B/C.
"""
from collections import Counter
from itertools import combinations,product
from fractions import Fraction
from math import comb

from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import _params
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    validate_disjoint_factor_swaps,apply_disjoint_factor_swaps,
)
from hyp105_issue230_d6aa4br_all_seven_signed_source_flux import (
    immutable_original_sixflag_class,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS,classify_seven_prechecked,
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six


def fourth_GQ_C_B_source_certificate(s):
    """Exact integer all-h SOURCE bound; no fictitious high-h W3 samples."""
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("requires actual dyadic W3 order s=2^h, h>=1")
    V,a,_,_=_params(s)
    if V<8:raise ValueError("four different disjoint original LINE pairs")
    d=s+1
    inside=4*(2**3)*5*6
    outside_repeat=2**4*comb(4,2)*d
    outside_single=2**4*4*(3*(d-1)**2+3*d*(d-1))
    total=inside+outside_repeat+outside_single
    if (inside,outside_repeat,outside_single)!=(960,96*d,
        192*(2*d-1)*(d-1)):
        raise AssertionError("true-original GQ fourth C/B partition formula")
    return {
        "s":s,"h":s.bit_length()-1,"V":V,"a":a,"d":d,
        "four_original_disjoint_LINE_factor_swap_packets":4,
        "max_fourth_source_C_B_all_five_LINEs_INSIDE_four_packets":inside,
        "max_fourth_source_C_B_OUTSIDE_repeated_LINE":outside_repeat,
        "max_fourth_source_C_B_OUTSIDE_singleton_LINE":outside_single,
        "max_fourth_source_C_B_original_Q":total,
        "max_abs_fourth_original_GF5_C_B_Walsh":Fraction(total,2),
        "max_abs_fourth_original_GF5_weighted_C_B":
            R3_CERTIFIED_FLOORS["C/B"]*Fraction(total,2),
        "original_GQ_common_TRANSVERSALS_of_TWO_LINEs_at_most_d":True,
        "original_SOURCE_C_B_six_DISTINCT_flags":True,
        "NOT_a_fixed_center_seven_GF5_lower":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def fourth_original_C_B_true_GQ_geometry(model,line_packets):
    """EXACT C/B source Q through four genuine 2-LINE-factor packets.

    Enumerate FIVE distinct ORIGINAL line factors from four packets,
    with the fifth either a free second member INSIDE the four
    packets or an OUTSIDE original LINE factor. Choose repeated line
    and its two *unordered* intersecting partner lines; the other two
    original lines must meet at a third DISTINCT original POINT.
    True original two-LINE point intersection uniqueness makes Q
    unique and no original sixflag Q can be counted twice.
    """
    s,V,a,inc,f,g,_,_=_original_source(model)
    packets=validate_disjoint_factor_swaps(V,line_packets)
    if len(packets)!=4:raise ValueError("FOUR disjoint original LINE pairs")
    all_packet_lines={l for pair in packets for l in pair}
    byline=[{} for _ in range(V)]
    for j,(p,l) in enumerate(inc):
        if p in byline[l]:
            raise ValueError("original source same POINT-LINE incidence duplicated")
        byline[l][p]=j
    if any(len(z)!=s+1 for z in byline):
        raise ValueError("genuine original W3 line source valency must be d")
    # Explicitly validate the LINE-pair local GQ partial-linearity
    # on EVERY factor used by the original source enumerator.
    for a_id in range(V):
        for b_id in range(a_id+1,V):
            if len(byline[a_id].keys() & byline[b_id].keys())>1:
                raise ValueError("original source two distinct LINEs share >1 POINT")
    Qs=set();physical=set()
    partition=Counter()
    exterior_repeated=0
    # All-INSIDE 5-line sets have TWO possible choices of the
    # "anchored" line in the doubled packet; canonicalize FIRST,
    # otherwise a real source sixflag would appear twice falsely.
    five_line_sets={tuple(sorted((*chosen,fifth)))
        for chosen in product(*packets) for fifth in range(V)
        if fifth not in chosen}
    for line_ids in sorted(five_line_sets):
            exterior=frozenset(line_ids)-all_packet_lines
            if len(exterior)>1:
                raise AssertionError("four packets cannot be met by five lines with two exterior IDs")
            inside=not exterior
            fifth=next(iter(exterior),None)
            for repeated in line_ids:
                others=tuple(x for x in line_ids if x!=repeated)
                if len(others)!=4:raise AssertionError("five distinct original LINE ids")
                for partners in combinations(others,2):
                    residual=tuple(x for x in others if x not in partners)
                    if len(residual)!=2:raise AssertionError("two third-POINT line IDs")
                    pset=(byline[repeated].keys() & byline[partners[0]].keys())
                    qset=(byline[repeated].keys() & byline[partners[1]].keys())
                    rset=(byline[residual[0]].keys() & byline[residual[1]].keys())
                    if not pset or not qset or not rset:continue
                    if len(pset)>1 or len(qset)>1 or len(rset)>1:
                        raise AssertionError("not an original GQ two-LINE intersection")
                    p=next(iter(pset));q=next(iter(qset));r=next(iter(rset))
                    if len({p,q,r})!=3:continue
                    Q=tuple(sorted((
                        byline[repeated][p],byline[repeated][q],
                        byline[partners[0]][p],byline[partners[1]][q],
                        byline[residual[0]][r],byline[residual[1]][r],
                    )))
                    if len(Q)!=6 or len(set(Q))!=6:
                        raise AssertionError("not six DISTINCT ORIGINAL source incidence IDs")
                    if Q in Qs:
                        raise AssertionError("one true original Q has two C/B decompositions")
                    sourcep=tuple(sorted(Counter(inc[j][0] for j in Q).values()))
                    sourcel=tuple(sorted(Counter(inc[j][1] for j in Q).values()))
                    if sourcep!=(2,2,2) or sourcel!=(1,1,1,1,2):
                        raise AssertionError("not ORIGINAL source POINT C / LINE B")
                    Qs.add(Q)
                    case=("inside" if inside else
                          ("outside_repeated" if repeated==fifth else
                           "outside_singleton"))
                    partition[case]+=1
                    if len({u for p_id in (p,q,r) for u in f[p_id]})==6:
                        physical.add(Q)
    cert=fourth_GQ_C_B_source_certificate(s)
    if not (partition["inside"]<=cert["max_fourth_source_C_B_all_five_LINEs_INSIDE_four_packets"]
        and partition["outside_repeated"]<=cert["max_fourth_source_C_B_OUTSIDE_repeated_LINE"]
        and partition["outside_singleton"]<=cert["max_fourth_source_C_B_OUTSIDE_singleton_LINE"]
        and len(Qs)<=cert["max_fourth_source_C_B_original_Q"]
        and len(physical)<=len(Qs)):
        raise AssertionError("true original GQ source C/B fourth cap violated")
    return {
        "s":s,"V":V,"source_LINE_packets":packets,
        "real_original_C_B_six_ID_sets":frozenset(Qs),
        "original_POINT_physical_C_eligible_sets":frozenset(physical),
        "source_fourth_C_B_case_counts":dict(partition),
        "source_fourth_C_B_count":len(Qs),
        "physically_LEFT_C_eligible_count":len(physical),
        "true_GQ_C_B_fourth_source_bound":cert["max_fourth_source_C_B_original_Q"],
        "refined_abs_original_C_B_fourth_Walsh":Fraction(len(physical),2),
        "all_true_source_six_incidence_IDs_UNCHANGED":True,
    }


def exact_W32_fourth_original_GQ_C_B_Walsh(model,packets):
    """Historical GF5 for actual original W32 on 16 globally coherent maps."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    if (s,V,a)!=(2,15,6):raise ValueError("finite exact W32 only")
    pairs=validate_disjoint_factor_swaps(V,packets)
    if len(pairs)!=4:raise ValueError("four original LINE swap packets")
    states=tuple(apply_disjoint_factor_swaps(g,pairs,tuple(
        i for i in range(4) if mask>>i&1)) for mask in range(16))
    geo=fourth_original_C_B_true_GQ_geometry(model,pairs)
    nums=Counter()
    source_counts=Counter()
    count=0
    for Q,_ in selected_left_six(model):
        usedlines={inc[j][1] for j in Q}
        if not all(u in usedlines or v in usedlines for u,v in pairs):
            continue
        count+=1
        tag=immutable_original_sixflag_class(Q,inc)
        if tag is None:continue
        source_counts[tag]+=1
        if tag=="C/B" and Q not in geo["original_POINT_physical_C_eligible_sets"]:
            raise AssertionError("true original source GQ C/B fourpacket intersection enumeration omitted Q")
        for mask,images in enumerate(states):
            actual=classify_seven_prechecked(Q,f,images,inc)
            if actual is not None and actual!=tag:
                raise AssertionError("historical original sixflag changed immutable class")
            nums[tag]+=(-1 if mask.bit_count()%2 else 1)*int(actual is not None)
    if abs(nums["C/B"])>8*geo["physically_LEFT_C_eligible_count"]:
        raise AssertionError("original C/B fourth historic Walsh exceeds exact source physical cap")
    return {
        "real_W32_full_original_global_LINE_maps":16,
        "real_original_Q_hitting_four_packets":count,
        "original_Q_source_class_counts":dict(source_counts),
        "fourth_true_original_GF5_class_Walsh_numerators":
            {c:nums[c] for c in R3_CERTIFIED_FLOORS},
        "fourth_true_original_GF5_class_Walsh_coefficients":
            {c:Fraction(nums[c],16) for c in R3_CERTIFIED_FLOORS},
        "exact_original_source_C_B_intersections":geo,
        "UNCHANGED_original_f_g_GF5_positive_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
