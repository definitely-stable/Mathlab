"""HYP-105 #230 AA4-BU: fifth Walsh order authentic GQ C/A and C/B bounds.

ALL dyadic h>=1, arbitrary completely fixed correlated injective f,g.
Five disjoint original LINE-factor image-swap packets, six DISTINCT
original source incidence IDs; a Walsh-sensitive Q must hit each packet.
TRUE GQ distinct LINE intersection at most one actual POINT forces:

- original source C/A (three doubly-used original POINT factors and
  six distinct original LINE factors) at most 480*d*(d-1) true Q,
  where d=s+1. Hence |fifth Walsh S_C/A|<=240*d*(d-1).
- original source C/B (three double POINT factors, one double LINE
  factor and four singleton LINE factors) at most 960 TRUE Q.
  Hence |fifth Walsh S_C/B|<=480 independent of s.

C/B source IDs have an EXACT constructive enumeration over five
genuine two-line packets: pick the one packet with the repeated actual
LINE, two other packets meeting it at two DIFFERENT original POINTs,
and intersect the two remaining packets at a THIRD original POINT.
Five * two * C(4,2) * 2^4 =960 upper.

These source-profile Walsh estimates are partial fixed-map SENSITIVITY
results, not a lower bound on initial unchanged S(f,g) and not #230 A/B/C.
"""
from itertools import combinations,product
from collections import Counter
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


def fifth_order_original_GQ_C_certificate(s):
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("genuine original symplectic s=2^h h>=1")
    V,_,_,_=_params(s)
    if V<10:
        raise ValueError("five disjoint actual original LINE pairs require 10 LINE IDs")
    d=s+1
    c_a=480*d*(d-1)
    c_b=960
    raw=480*d*(d-1)+960
    return {
        "s":s,"V":V,"original_LINE_degree":d,
        "number_disjoint_whole_LINE_factor_swap_pairs":5,
        "max_actual_original_C_A_Q_touching_ALL_five_packets":c_a,
        "max_actual_original_C_B_Q_touching_ALL_five_packets":c_b,
        "max_abs_fifth_Walsh_original_C_A":Fraction(c_a,2),
        "max_abs_fifth_Walsh_original_C_B":Fraction(c_b,2),
        "max_abs_fifth_Walsh_original_C_A_plus_C_B":
             Fraction(raw,2),
        "max_abs_fifth_Walsh_weighted_two_C_classes":
             (R3_CERTIFIED_FLOORS["C/A"]*Fraction(c_a,2)
              +R3_CERTIFIED_FLOORS["C/B"]*Fraction(c_b,2)),
        "true_original_POINT_source_C_profile":(2,2,2),
        "true_original_LINE_source_A_profile":(1,1,1,1,1,1),
        "true_original_LINE_source_B_profile":(1,1,1,1,2),
        "original_GQ_two_different_LINEs_meet_in_AT_MOST_one_POINT":True,
        "source_class_CAP_is_not_a_FIXED_MAP_acceptance_lower":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def original_five_packet_C_B_geometry(model,line_pairs):
    """Enumerate ALL C/B true sixflag Q meeting five real disjoint 2-line packets.

    No use of GF5 classifier or of physical RIGHT image g during source
    enumeration. The original source of a double-LINE factor is UNIQUE.
    A C/B sixflag that meets five disjoint packets has its 6th actual
    incidence from the SAME line in one packet: otherwise its source
    right multiplicities would all be singleton (source A).
    """
    s,V,a,inc,f,g,_,_=_original_source(model)
    pairs=validate_disjoint_factor_swaps(V,line_pairs)
    if len(pairs)!=5:
        raise ValueError("five disjoint authentic original LINE factor packets required")
    byline=[{} for _ in range(V)]
    for j,(p,l) in enumerate(inc):
        if p in byline[l]:
            raise ValueError("repeated original POINT-LINE incidence")
        byline[l][p]=j
    d=s+1
    if any(len(x)!=d for x in byline):
        raise ValueError("true original LINE valency invalid")
    # Independently check original GQ uniqueness for precisely all
    # packet line-pairs used by the constructive C/B point matching.
    chosen_lines={l for pair in pairs for l in pair}
    for l,r in combinations(sorted(chosen_lines),2):
        if len(byline[l].keys() & byline[r].keys())>1:
            raise ValueError("not a genuine partial-linear original GQ")
    Qs=set()
    eligible_left=set()
    seen_paths=0
    for dup_packet in range(5):
        others=tuple(i for i in range(5) if i!=dup_packet)
        for repeated_line in pairs[dup_packet]:
            for meets in combinations(others,2):
                rest=tuple(i for i in others if i not in meets)
                # Each OTHER packet contributes precisely one actual
                # LINE factor; at most 2^4 choices. Two must intersect
                # the repeated LINE at different source POINTs; the
                # other two must intersect each other at a third point.
                for lines in product(*(pairs[i] for i in others)):
                    owners=dict(zip(others,lines))
                    a_line,b_line=(owners[j] for j in meets)
                    c_line,e_line=(owners[j] for j in rest)
                    left=set(byline[repeated_line])&set(byline[a_line])
                    right=set(byline[repeated_line])&set(byline[b_line])
                    common=set(byline[c_line])&set(byline[e_line])
                    if not left or not right or not common:
                        continue
                    if len(left)>1 or len(right)>1 or len(common)>1:
                        raise AssertionError("original GQ two lines meet in more than one point")
                    pa=next(iter(left));pb=next(iter(right))
                    pc=next(iter(common))
                    if len({pa,pb,pc})!=3:
                        continue
                    Q=tuple(sorted((
                        byline[repeated_line][pa],
                        byline[repeated_line][pb],
                        byline[a_line][pa],
                        byline[b_line][pb],
                        byline[c_line][pc],
                        byline[e_line][pc],
                    )))
                    if len(Q)!=6 or len(set(Q))!=6:
                        raise AssertionError("constructed Q violates six true original incidence IDs")
                    pprof=tuple(sorted(Counter(inc[j][0] for j in Q).values()))
                    lprof=tuple(sorted(Counter(inc[j][1] for j in Q).values()))
                    if (pprof,lprof)!=((2,2,2),(1,1,1,1,2)):
                        raise AssertionError("true-original C/B source projection malformed")
                    if Q in Qs:
                        raise AssertionError("nonunique repeated ORIGINAL line or two matching pairs")
                    Qs.add(Q)
                    if len({u for p in (pa,pb,pc) for u in f[p]})==6:
                        eligible_left.add(Q)
                    seen_paths+=1
    if len(Qs)!=seen_paths or len(Qs)>960 or len(eligible_left)>len(Qs):
        raise AssertionError("fifth original C/B incidence packet source cap false")
    return {
        "s":s,"V":V,"five_original_LINE_source_packets":pairs,
        "original_C_B_Q_source_flag_sets":frozenset(Qs),
        "original_C_B_fixed_POINT_physical_eligible_sets":frozenset(eligible_left),
        "number_source_C_B":len(Qs),
        "number_FIXED_LEFT_physical_eligible_C_B":len(eligible_left),
        "all_h_source_C_B_upper":960,
        "refined_fifth_C_B_Walsh_upper":Fraction(len(eligible_left),2),
        "one_GENUINE_double_LINE_factor_per_C_B_Q":True,
    }


def independent_fifth_original_W32_GF5(model,pairs):
    """Historical original W32 32-map fifth class Walsh, no Q redraw."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("W32 original 32-map historical exhaustive checker only")
    pairs=validate_disjoint_factor_swaps(V,pairs)
    if len(pairs)!=5:raise ValueError("exactly five disjoint genuine LINE source packets")
    states=tuple(apply_disjoint_factor_swaps(g,pairs,tuple(
        i for i in range(5) if mask>>i&1)) for mask in range(32))
    geom=original_five_packet_C_B_geometry(model,pairs)
    numerator=Counter()
    source_support=Counter()
    selected_count=0
    for Q,_ in selected_left_six(model):
        lines={inc[j][1] for j in Q}
        if not all(u in lines or v in lines for u,v in pairs):
            continue
        selected_count+=1
        source_tag=immutable_original_sixflag_class(Q,inc)
        if source_tag is None:continue
        source_support[source_tag]+=1
        if source_tag=="C/B" and Q not in geom["original_C_B_fixed_POINT_physical_eligible_sets"]:
            raise AssertionError("source GQ five-packet C/B matching oracle omitted accepted candidate")
        for mask,state in enumerate(states):
            tag=classify_seven_prechecked(Q,f,state,inc)
            if tag is not None and tag!=source_tag:
                raise AssertionError("source class changed across whole LINE-factor image swaps")
            numerator[source_tag]+=(-1 if mask.bit_count()%2 else 1)*int(tag is not None)
    bound=fifth_order_original_GQ_C_certificate(s)
    if abs(numerator["C/A"])>32*bound["max_abs_fifth_Walsh_original_C_A"]:
        raise AssertionError("historical original C/A fifth coefficient violates GQ")
    if abs(numerator["C/B"])>32*geom["refined_fifth_C_B_Walsh_upper"]:
        raise AssertionError("historical original C/B fifth coefficient violates refined source bound")
    return {
        "true_W32_original_32_complete_LINE_maps":32,
        "five_packet_source_sensitive_left_sixflag_Q":selected_count,
        "original_sixflag_source_class_counts":dict(source_support),
        "original_fifth_class_Walsh_numerators":
            {c:numerator[c] for c in R3_CERTIFIED_FLOORS},
        "original_fifth_class_Walsh_coefficients":
            {c:Fraction(numerator[c],32) for c in R3_CERTIFIED_FLOORS},
        "exact_true_original_GQ_C_B_line_matching":geom,
        "unchanged_original_full_f_g_positive_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
