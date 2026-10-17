"""AA4-BU: exact genuine original GQ five-line-packet source-GF5 spectra."""
from collections import Counter
from itertools import combinations,product
from fractions import Fraction
from math import comb
from hyp105_issue230_d6aa4ay_quenched_allD_opposite_mean import _params
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import validate_disjoint_factor_swaps,apply_disjoint_factor_swaps
from hyp105_issue230_d6aa4br_all_seven_signed_source_flux import immutable_original_sixflag_class
from hyp105_issue230_d6aa4bt_gq_sixth_order_intersections import exact_original_sixflag_packet_hit_count,_perfect_packet_pairings
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS,classify_seven_prechecked
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six

def fifth_order_original_GQ_certificate(s):
    if type(s) is not int or s<2 or s&(s-1):raise ValueError("actual dyadic W3 s>=2")
    V,_,_,_=_params(s)
    d=s+1;b=2*d
    H=5*comb(b,2)*b**4
    A=5*d*d*b**4
    B=10*comb(d,2)*b**4
    if H!=A+B or H!=exact_original_sixflag_packet_hit_count(s,5):
        raise AssertionError("five original line-packet source A/B count wrong")
    pointB=min(H,300*b**4)
    pointC=min(H,4800)
    caps={
      "D6":Fraction(A,2),
      "B-left/A-right":Fraction(min(A,pointB),2),
      "C/A":Fraction(min(A,pointC),2),
      "A-left/B-right":Fraction(B,2),
      "C/B":Fraction(min(B,pointC),2),
      "B/B-overlap":Fraction(min(B,pointB),2),
      "B/B-disjoint":Fraction(min(B,pointB),2)}
    if set(caps)!=set(R3_CERTIFIED_FLOORS):raise AssertionError("seven-class scope changed")
    return {"s":s,"d":d,"total_genuine_sixflag_five_packet_sets":H,
      "exact_original_RIGHT_source_A":A,"exact_original_RIGHT_source_B":B,
      "RIGHT_source_C_impossible":True,
      "original_POINT_source_B_upper":pointB,
      "original_POINT_source_C_upper":pointC,
      "source_POINT_C_uniform_cap":4800,
      "per_seven_historical_GF5_fifth_Walsh_bound":caps,
      "selected_GF5_floor_weighted_fifth_Walsh_bound":sum(
         R3_CERTIFIED_FLOORS[c]*caps[c] for c in caps),
      "unchanged_original_global_positive_NOT_PROVED":True,
      "root_230":"OPEN_WITH_FORMAL_BLOCKER"}

def genuine_original_five_packet_C_geometry(model,pairs):
    """Genuine original line intersections over 75 source point-C matchings."""
    s,V,a,inc,f,g,_,_=_original_source(model)
    pairs=validate_disjoint_factor_swaps(V,pairs)
    if len(pairs)!=5:raise ValueError("FIVE pairwise disjoint true line packets")
    byline=[{} for _ in range(V)]
    for fid,(p,l) in enumerate(inc):byline[l][p]=fid
    if any(len(m)!=s+1 for m in byline):raise ValueError("not original W3 line degree")
    meets={}
    for i in range(5):
        for j in range(i,5):
            a=[]
            for l in pairs[i]:
                for r in pairs[j]:
                    if l==r:continue
                    inter=set(byline[l])&set(byline[r])
                    if len(inter)>1:raise AssertionError("two original GQ lines meet twice")
                    for p in inter:a.append((p,byline[l][p],byline[r][p]))
            if len(a)>4:raise AssertionError("two original two-line packets meet >four ways")
            meets[(i,j)]=tuple(a)
    C=set();leftC=set()
    for doubled in range(5):
        slots=(doubled,doubled)+tuple(i for i in range(5) if i!=doubled)
        for matching in _perfect_packet_pairings(range(6)):
            choices=[]
            for x,y in matching:
                i,j=slots[x],slots[y]
                z=meets[(min(i,j),max(i,j))]
                if i>j:z=tuple((p,v,u) for p,u,v in z)
                choices.append(z)
            for result in product(*choices):
                ps=[p for p,u,v in result]
                if len(set(ps))!=3:continue
                Q=tuple(sorted(q for p,u,v in result for q in (u,v)))
                if len(set(Q))!=6:continue
                if any(sum(inc[q][1] in pair for q in Q)!=
                       (2 if j==doubled else 1)
                       for j,pair in enumerate(pairs)):continue
                C.add(Q)
                if len({x for p in ps for x in f[p]})==6:leftC.add(Q)
    if not len(leftC)<=len(C)<=4800:raise AssertionError("all-h GQ fifth point-C cap")
    return {"source_C":frozenset(C),"physically_left_C":frozenset(leftC),
      "source_C_count":len(C),"physically_left_C_count":len(leftC),
      "meetings":meets,"five_times_fifteen_source_C_matchings":75,
      "exact_physical_C_fifth_Walsh_bound":Fraction(len(leftC),2)}

def true_original_W32_fifth_historical_GF5(model,pairs):
    s,V,a,inc,f,g,_,_=_original_source(model)
    if (s,V,a)!=(2,15,6):raise ValueError("finite historical oracle W32 only")
    pairs=validate_disjoint_factor_swaps(V,pairs)
    if len(pairs)!=5:raise ValueError("five original line source packets needed")
    states=tuple(apply_disjoint_factor_swaps(g,pairs,tuple(
        i for i in range(5) if mask>>i&1)) for mask in range(32))
    nums=Counter();source=Counter()
    for Q,_ in selected_left_six(model):
        lines={inc[q][1] for q in Q}
        if any(not (u in lines or v in lines) for u,v in pairs):continue
        tag=immutable_original_sixflag_class(Q,inc)
        if tag is None:continue
        source[tag]+=1
        for mask,h in enumerate(states):
            actual=classify_seven_prechecked(Q,f,h,inc)
            if actual is not None and actual!=tag:
                raise AssertionError("historical original GF5 source type switched")
            nums[tag]+=(-1 if mask.bit_count()%2 else 1)*int(actual is not None)
    geom=genuine_original_five_packet_C_geometry(model,pairs)
    if source["C/A"]+source["C/B"]!=geom["physically_left_C_count"]:
        raise AssertionError("original left physical C source set mismatch")
    cert=fifth_order_original_GQ_certificate(s)
    for c in R3_CERTIFIED_FLOORS:
        if abs(nums[c])>32*cert["per_seven_historical_GF5_fifth_Walsh_bound"][c]:
            raise AssertionError("original W3 fifth class coefficient >all-h cap")
    if abs(nums["C/A"])+abs(nums["C/B"])>16*geom["physically_left_C_count"]:
        raise AssertionError("original point-C signed cap violated")
    return {"numerators":{c:nums[c] for c in R3_CERTIFIED_FLOORS},
       "coefficients":{c:Fraction(nums[c],32) for c in R3_CERTIFIED_FLOORS},
       "five_source_packet_eligible_left_Q_by_class":dict(source),
       "geometry":geom,"number_actual_complete_global_right_maps":32,
       "weighted_selected_GF5_floor_coefficient":Fraction(sum(
           R3_CERTIFIED_FLOORS[c]*nums[c] for c in R3_CERTIFIED_FLOORS),32),
       "root_230":"OPEN_WITH_FORMAL_BLOCKER"}
