"""HYP-105 #230 / AA4-BV-C/A: true-original GQ fourth-order anchor identity.

Complement to parallel fourth-order original C/B PR #594. At any four
disjoint whole original LINE factor image swap-packets, every historical
true ORIGINAL six-distinct-incidence Q contributing to fourth Walsh
order must touch each genuine two-LINE-factor packet. If its original
POINT profile is C=(2,2,2), picking one flag per packet yields precisely
point profiles 2+1+1 or 2+2; no other profile can be completed by TWO
unanchored original incidence flags to three point-pairs.

A rigorous all-h original GQ line-uniqueness upper is
 N4_POINT_C <= 96*d²*(d-1)² + 48*(V-2)*C(d,2);
 where d=s+1, V=(s+1)(s²+1).
Hence |hat S_C/A(T)| <= N4_POINT_C/2.
True source LINE right-C is impossible at order four (>=4 distinct).
The exact sum over all genuine anchor quadruples, completions, and
inverse packet-anchor multiplicity counts EVERY source Q ONCE, even
when a sixflag uses two or three LINE images in a selected packet.

These are source spectral MAGNITUDES on corrected global maps. They
do not prove initial unchanged-map positivity for root issue #230.
"""
from collections import Counter
from itertools import product, combinations
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


def fourth_order_true_original_POINT_C_certificate(s):
    """A valid uniform all-h REAL W3 original C/A coefficient bound."""
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("actual genuine symplectic W(3,2^h), h>=1")
    V,_,_,_=_params(s)
    if V<8:raise ValueError("four disjoint source LINE factor pairs need 8 LINES")
    d=s+1
    anchored_211=6*4*(2*d)**2
    anchored_22=3*4**2
    completion_211=(d-1)**2
    completion_22=(V-2)*comb(d,2)
    bound_211=anchored_211*completion_211
    bound_22=anchored_22*completion_22
    return {
      "s":s,"d_original_LINE_and_POINT_degree":d,
      "V_original_POINT_factors":V,
      "four_original_LINE_swap_packets":4,
      "original_POINT_profile_211_anchors_upper":anchored_211,
      "original_POINT_profile_22_anchors_upper":anchored_22,
      "completion_per_211_anchor":completion_211,
      "completion_per_22_anchor":completion_22,
      "POINT_C_true_original_sixflag_upper_by_211":bound_211,
      "POINT_C_true_original_sixflag_upper_by_22":bound_22,
      "POINT_C_true_original_sixflag_upper_total":bound_211+bound_22,
      "historical_GF5_C_A_fourth_Walsh_abs_upper":
          Fraction(bound_211+bound_22,2),
      "right_SOURCE_LINE_C_impossible_at_fourth_order":True,
      "hist_GF5_original_unchanged_center_lower_NOT_PROVED":True,
      "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def actual_original_four_packet_C_anchor_identity(model,pairs):
    """Enumerate genuine ORIGINAL C profile SIX-flags via 4 true source anchors.

    Each one of four actual source two-LINE-factor packets contributes
    exactly one ANCHOR flag. A selected genuine Q may contain multiple
    flags from packet i; it is intentionally produced prod_i n_i(Q)
    times. A Fraction(1,prod_i n_i(Q)) per anchor occurrence yields the
    exact true-original six-Q count; no false unique-anchor assumption.

    Genuine original W32 and W34 finite fixtures ONLY. All-h proof is
    symbolic and does not enumerate fabricated high-order geometries.
    """
    s,V,a,inc,f,g,_,_=_original_source(model)
    if s not in (2,4):
        raise ValueError("finite anchor enumerator restricted to true W32/W34")
    pairs=validate_disjoint_factor_swaps(V,pairs)
    if len(pairs)!=4:raise ValueError("four pairwise disjoint ORIGINAL LINE source pairs")
    byline=[[] for _ in range(V)]
    bypoint=[[] for _ in range(V)]
    for fid,(p,l) in enumerate(inc):
        byline[l].append(fid);bypoint[p].append(fid)
    if any(len(row)!=s+1 for row in byline) or any(len(row)!=s+1 for row in bypoint):
        raise ValueError("not authentic regular GQ point/line incidence")
    packets=[tuple(j for l in (u,v) for j in byline[l]) for u,v in pairs]
    if any(len(row)!=2*(s+1) for row in packets):
        raise AssertionError("source packet size wrong")
    anchors211=anchors22=0
    occurrences=Counter()
    source_classes=Counter()
    eligible=set()
    for anchor in product(*packets):
        points=[inc[j][0] for j in anchor]
        counts=Counter(points)
        profile=tuple(sorted(counts.values()))
        if profile==(1,1,2):
            anchors211+=1
            singles=[p for p,n in counts.items() if n==1]
            # One distinct original flag at EACH of two singly-used points,
            # excluding the already chosen original anchor flags.
            remaining=(
                tuple(j for j in bypoint[singles[0]] if j not in anchor),
                tuple(j for j in bypoint[singles[1]] if j not in anchor))
            for x,y in product(*remaining):
                Q=tuple(sorted(anchor+(x,y)))
                if len(set(Q))!=6:raise AssertionError("repeated original flag ID")
                occurrences[Q]+=1
        elif profile==(2,2):
            anchors22+=1
            # Both double-used source POINTs already have their two flags.
            # Select a third DIFFERENT original point and two true flags.
            for p in range(V):
                if p in counts:continue
                for x,y in combinations(bypoint[p],2):
                    Q=tuple(sorted(anchor+(x,y)))
                    if len(set(Q))!=6:raise AssertionError("repeated source flag ID")
                    occurrences[Q]+=1
    unique=set(occurrences)
    exact_weighted=Fraction(0)
    left_eligible=Counter()
    all_source_class=Counter()
    packet_multiplicity_profile=Counter()
    for Q,seen in occurrences.items():
        src_point=Counter(inc[j][0] for j in Q)
        if tuple(sorted(src_point.values()))!=(2,2,2):
            raise AssertionError("completed original source Q is not POINT-C")
        packet_counts=tuple(sum(inc[j][1] in pair for j in Q) for pair in pairs)
        if any(z==0 for z in packet_counts):
            raise AssertionError("source Q failed actual original LINE packets")
        multiplicity=1
        for z in packet_counts:multiplicity*=z
        if seen!=multiplicity:
            raise AssertionError("source Q anchor count does not equal prod packet loads")
        exact_weighted+=Fraction(seen,multiplicity)
        packet_multiplicity_profile[packet_counts]+=1
        tag=immutable_original_sixflag_class(Q,inc)
        if tag not in ("C/A","C/B",None):
            raise AssertionError("original POINT-C flag entered impossible GF5 class")
        all_source_class[tag if tag is not None else "NOT_GF5"]+=1
        if len({coordinate for p in src_point for coordinate in f[p]})==6:
            eligible.add(Q)
            left_eligible[tag if tag is not None else "NOT_GF5"]+=1
    if exact_weighted!=len(unique):
        raise AssertionError("weighted anchor count did not equal true UNIQUE original Q")
    bound=fourth_order_true_original_POINT_C_certificate(s)
    if len(unique)>bound["POINT_C_true_original_sixflag_upper_total"]:
        raise AssertionError("genuine original GQ point-C four-packet bound false")
    if anchors211>bound["original_POINT_profile_211_anchors_upper"]:
        raise AssertionError("GQ point 2/1/1 anchored match cap false")
    if anchors22>bound["original_POINT_profile_22_anchors_upper"]:
        raise AssertionError("GQ point 2/2 anchored match cap false")
    return {
      "s":s,"V":V,"pairs":pairs,
      "genuine_original_POINT_C_source_Q":frozenset(unique),
      "fixed_LEFT_physically_eligible_original_POINT_C_Q":frozenset(eligible),
      "original_anchor_profile_211_count":anchors211,
      "original_anchor_profile_22_count":anchors22,
      "multiplicity_corrected_original_Q_count":exact_weighted,
      "actual_original_packet_load_shapes":dict(packet_multiplicity_profile),
      "source_right_class_counts":dict(all_source_class),
      "physical_left_C_original_source_right_class_counts":dict(left_eligible),
      "historical_C_A_fourth_Walsh_source_cap_from_actual_f":
          Fraction(left_eligible["C/A"],2),
      "original_W3_all_h_center_lower_NOT_PROVED":True,
    }


def true_original_W32_fourth_CA_GF5_Walsh(model,pairs):
    """Historical same-six-ID C/A and C/B fifth? FOURTH Walsh on 16 full maps."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("finite true ORIGINAL W32 historical oracle only")
    pairs=validate_disjoint_factor_swaps(V,pairs)
    if len(pairs)!=4:raise ValueError("FOUR disjoint true original LINE source pairs")
    geometric=actual_original_four_packet_C_anchor_identity(model,pairs)
    states=tuple(apply_disjoint_factor_swaps(g,pairs,
         tuple(i for i in range(4) if mask>>i&1)) for mask in range(16))
    numerator=Counter()
    for Q in geometric["fixed_LEFT_physically_eligible_original_POINT_C_Q"]:
        static=immutable_original_sixflag_class(Q,inc)
        for mask,state in enumerate(states):
            tag=classify_seven_prechecked(Q,f,state,inc)
            if tag is not None and tag!=static:
                raise AssertionError("same ORIGINAL Q changed positive historical GF5 class")
            numerator[static]+=(-1 if mask.bit_count()%2 else 1)*int(tag is not None)
    for c in ("C/A","C/B"):
        if abs(numerator[c])>8*geometric[
             "physical_left_C_original_source_right_class_counts"].get(c,0):
            raise AssertionError("per-class original GF5 Walsh coefficient >1/2 of source Q")
    cert=fourth_order_true_original_POINT_C_certificate(s)
    if abs(numerator["C/A"])>16*cert["historical_GF5_C_A_fourth_Walsh_abs_upper"]:
        raise AssertionError("fourth C/A Walsh exceeds all-h original GQ bound")
    return {
      "four_original_source_LINE_swap_pairs":pairs,
      "16_COMPLETE_globally_injected_original_right_maps":16,
      "historical_original_C_A_fourth_Walsh_numerator":numerator["C/A"],
      "historical_original_C_B_fourth_Walsh_numerator":numerator["C/B"],
      "historical_original_C_A_fourth_Walsh":Fraction(numerator["C/A"],16),
      "historical_original_C_B_fourth_Walsh":Fraction(numerator["C/B"],16),
      "source_genuine_original_C_Q_geometry":geometric,
      "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }
