"""HYP-105 #230 AA4-BT: TRUE ORIGINAL GQ six-swap spectral intersection sieve.

All-h for actual W(3,2^h), arbitrary fully globally injected and potentially
correlated typed original physical f,g: SIX disjoint WHOLE LINE factor-image
swap packets force SIX DIFFERENT original LINE source factors among every
true six-incidence Q that can contribute to sixth-order Walsh coefficient.

Consequently FOUR historical seven-GF5 classes have identically ZERO
sixth-order coefficient: A-left/B-right,C/B,B/B-overlap,B/B-disjoint.
Only original D6, B-left/A-right, C/A can occur.

The GQ property that two distinct genuine LINE factors share at most
ONE actual original POINT gives a new uniform SOURCE C/A capacity:
at most 15 perfect pairings * 4^3 line-pair coincidences =960 genuinely
distinct six-flag Q, hence |hat S_C/A(T)|<=480 independent of s.
Original source B/A is at most 60*(2(s+1))^4 genuine Q and
|hat S_B/A(T)|<=30*(2(s+1))^4.

For t disjoint source LINE-pair packets, an EXACT all-h unrestricted
six-original-flag hitting count is inclusion-exclusion on the disjoint
sets of 2(s+1) real original incidence IDs per packet. Never synthesize
high-h W3 fixtures. No claim that this supplies initial fixed-map lower.
"""
from collections import Counter
from itertools import combinations,permutations,product
from math import comb
from fractions import Fraction

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

SIXTH_ALLOWED=("D6","B-left/A-right","C/A")
SIXTH_FORBIDDEN=("A-left/B-right","C/B","B/B-overlap","B/B-disjoint")

def exact_original_sixflag_packet_hit_count(s,t):
    """Exact source flag subsets meeting t disjoint 2-LINE source packets.

    M=V(s+1) different actual original W3 incidence IDs, 2d flag IDs
    per disjoint two-line packet; simple inclusion/exclusion on disjoint
    genuine original incidence-ID packets (not independent f,g).
    """
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("genuine dyadic s=2^h >=2 needed")
    V,_,_,_=_params(s)
    if type(t) is not int or not 0<=t<=V//2:
        raise ValueError("there must be t DISJOINT original line-factor pairs")
    d=s+1
    M=V*d
    if t>6:return 0
    result=sum((-1)**j*comb(t,j)*comb(M-2*d*j,6)
               for j in range(t+1) if M-2*d*j>=6)
    if result<0 or result>comb(M,6):
        raise AssertionError("true original packet inclusion/exclusion count invalid")
    if t==6 and result!=(2*d)**6:
        raise AssertionError("six disjoint line packets must contribute exactly one flag each")
    return result

def sixth_order_original_GQ_class_certificate(s):
    """Exact all-h upper bounds per ORIGINAL six-GF5 motif class at order 6."""
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("genuine dyadic source order >=2 required")
    V,_,_,_=_params(s)
    if V<12:
        raise ValueError("six disjoint original LINE source pairs need 12 line IDs")
    d=s+1
    A=(2*d)**6
    B=min(A,60*(2*d)**4)
    C=min(A,960)
    per={"D6":Fraction(A,2),
         "B-left/A-right":Fraction(B,2),
         "C/A":Fraction(C,2)}
    per.update({c:Fraction(0) for c in SIXTH_FORBIDDEN})
    weighted=sum(R3_CERTIFIED_FLOORS[c]*per[c] for c in per)
    return {
        "s":s,"V":V,"genuine_original_line_degree":d,
        "sixth_order_original_sixflag_packet_capacity":A,
        "maximum_original_POINT_profile_B_source_Q":B,
        "maximum_original_POINT_profile_C_source_Q":C,
        "per_historical_seven_class_sixth_Walsh_absolute_upper":per,
        "maximum_original_selected_GF5_floor_sixth_Walsh_absolute_upper":weighted,
        "class_C_overall_bound_uniform_in_s":480,
        "positive_GF5_classes_identically_zero_at_sixth_order":SIXTH_FORBIDDEN,
        "true_original_GQ_line_intersections_at_most_ONE":True,
        "unchanged_original_f_g_positive_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }

def _perfect_packet_pairings(xs):
    xs=tuple(xs)
    if not xs:
        yield ()
        return
    first=xs[0]
    for j in range(1,len(xs)):
        for tail in _perfect_packet_pairings(xs[1:j]+xs[j+1:]):
            yield ((first,xs[j]),)+tail

def genuine_original_six_packet_geometry(model,line_pairs):
    """Exact finite TRUE-original W3 C-profile matchings and physical f capacity.

    Each original LINE-pair packet contains 2d distinct REAL incidences.
    For packets i!=j, at most four true original POINT coincidences,
    since the packets contain 2x2 different genuine LINE factor pairs
    and two distinct original GQ lines have at most one common point.
    The C source profile is exactly the sum over 15 packet perfect
    matchings of three concurrent-pair choices at DISTINCT points.
    """
    s,V,a,inc,f,g,_,_=_original_source(model)
    pairs=validate_disjoint_factor_swaps(V,line_pairs)
    if len(pairs)!=6:
        raise ValueError("six disjoint authentic original LINE factor pairs required")
    byline=[{} for _ in range(V)]
    for j,(p,l) in enumerate(inc):
        byline[l][p]=j
    if any(len(m)!=s+1 for m in byline):
        raise ValueError("source geometry does not have true GQ line degree")
    packets=[tuple(j for l in (u,v) for j in sorted(byline[l].values()))
             for u,v in pairs]
    matches={}
    for i in range(6):
        for j in range(i+1,6):
            intersections=[]
            for lu in pairs[i]:
                for lv in pairs[j]:
                    shared=set(byline[lu])&set(byline[lv])
                    if len(shared)>1:
                        raise AssertionError("two ORIGINAL GQ lines meet at more than one POINT")
                    for p in shared:
                        intersections.append((p,byline[lu][p],byline[lv][p]))
            if len(intersections)>4:
                raise AssertionError("original 2x2 LINE packet pair has >4 common POINTs")
            matches[(i,j)]=tuple(sorted(intersections))
    classC=set()
    physicalC=set()
    for matching in _perfect_packet_pairings(range(6)):
        choices=(matches[tuple(sorted(edge))] for edge in matching)
        for choice in product(*choices):
            points=[p for p,_,_ in choice]
            if len(set(points))!=3:
                continue
            Q=tuple(sorted(z for p,u,v in choice for z in (u,v)))
            if len(Q)!=6 or len(set(Q))!=6:
                raise AssertionError("original six-packet repeated POINT-source C flags malformed")
            if Q in classC:
                raise AssertionError("true original POINT-C sixflag counted by two different matchings")
            classC.add(Q)
            if len(set(x for p in points for x in f[p]))==6:
                physicalC.add(Q)
    if not len(physicalC)<=len(classC)<=960:
        raise AssertionError("genuine original GQ C-profile uniform capacity violated")
    return {
        "s":s,"V":V,"pairs":pairs,
        "original_incidence_flag_packet_sizes":tuple(len(p) for p in packets),
        "source_C_sixflag_sets":frozenset(classC),
        "fixed_LEFT_physical_C_eligible_original_sixflag_sets":frozenset(physicalC),
        "source_C_count":len(classC),
        "fixed_LEFT_physical_C_eligible_count":len(physicalC),
        "pair_packet_common_point_matchings":matches,
        "number_perfect_packet_matchings":15,
        "GQ_original_C_source_upper_960":True,
        "historical_C_A_sixth_Walsh_bound_refined":
            Fraction(len(physicalC),2),
    }

def exact_W32_sixth_historical_class_Walsh(model,line_pairs):
    """Sixth Walsh numerator for original W32 on 64 FULL physical right maps.

    Filter by genuine 6-packet source incidence BEFORE reclassification:
    source LINE factors of a sixth-sensitive Q must hit all packets.
    Historical seven-GF5 classifier evaluates exactly the SAME Q IDs
    on all 64 complete globally injected maps; not Q-by-Q redrawing.
    """
    s,V,a,inc,f,g,_,_=_original_source(model)
    if (s,V,a)!=(2,15,6):
        raise ValueError("64-map finite sixth Walsh historical test needs true W32")
    pairs=validate_disjoint_factor_swaps(V,line_pairs)
    if len(pairs)!=6:
        raise ValueError("six disjoint original LINE source factor pairs required")
    states=tuple(apply_disjoint_factor_swaps(g,pairs,
        tuple(i for i in range(6) if mask&(1<<i)))
        for mask in range(64))
    numer=Counter()
    supporting=Counter()
    candidates=0
    for Q,_ in selected_left_six(model):
        lines={inc[j][1] for j in Q}
        if not all(u in lines or v in lines for u,v in pairs):
            continue
        candidates+=1
        static=immutable_original_sixflag_class(Q,inc)
        if static not in SIXTH_ALLOWED:
            raise AssertionError("true original six-flag source RIGHT profile not A")
        supporting[static]+=1
        if static=="C/A":
            # Independent fixed physical left C check is guaranteed by
            # historical left-six-flag enumeration.
            pcount=Counter(inc[j][0] for j in Q)
            if tuple(sorted(pcount.values()))!=(2,2,2):
                raise AssertionError("C/A original source POINT C profile missing")
        for mask,state in enumerate(states):
            tag=classify_seven_prechecked(Q,f,state,inc)
            if tag is not None and tag!=static:
                raise AssertionError("historical original sixflag retyped across six swaps")
            numer[static]+=(-1 if mask.bit_count()%2 else 1)*int(tag is not None)
    cert=sixth_order_original_GQ_class_certificate(s)
    geom=genuine_original_six_packet_geometry(model,pairs)
    if supporting["C/A"]!=geom["fixed_LEFT_physical_C_eligible_count"]:
        raise AssertionError("historical left original C source enumeration != geometric 15-matchings")
    for name in SEVEN:
        if abs(numer[name])>64*cert["per_historical_seven_class_sixth_Walsh_absolute_upper"][name]:
            raise AssertionError("historical class sixth Walsh violates GQ all-h cap")
    if abs(numer["C/A"])>32*geom["fixed_LEFT_physical_C_eligible_count"]:
        raise AssertionError("finite exact true source C/A Walsh physical sharper cap broken")
    if any(numer[c] for c in SIXTH_FORBIDDEN):
        raise AssertionError("original right repeated LINE source class got sixth-order coefficient")
    return {
        "real_W32_sixth_sensitive_left_sixflag_count":candidates,
        "original_sixth_sensitive_Q_by_source_class":dict(supporting),
        "sixth_historical_seven_GF5_Walsh_numerators":{c:numer[c] for c in R3_CERTIFIED_FLOORS},
        "sixth_historical_seven_GF5_Walsh_coefficients":
            {c:Fraction(numer[c],64) for c in R3_CERTIFIED_FLOORS},
        "sixth_historical_selected_GF5_floor_weighted_coefficient":
            Fraction(sum(R3_CERTIFIED_FLOORS[c]*numer[c] for c in R3_CERTIFIED_FLOORS),64),
        "exact_original_GQ_C_intersection_certificate":geom,
        "full_globally_injected_original_LINE_maps":64,
        "all_seven_historical_class_zero_filter_confirmed":True,
        "original_center_lower_NOT_PROVED":True,
    }
