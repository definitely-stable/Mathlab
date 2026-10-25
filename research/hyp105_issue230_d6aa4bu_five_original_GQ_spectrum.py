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
    """Correct all-h five-packet split: sixth Q-flag MAY BE OUTSIDE packets."""
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("genuine symplectic dyadic W3 s>=2")
    V,_,_,_=_params(s)
    d=s+1;b=2*d;M=V*d
    outside=M-10*d
    inside=5*comb(b,2)*b**4
    outside_case=outside*b**5
    H=inside+outside_case
    rightB=10*comb(d,2)*b**4
    rightA=5*d*d*b**4+outside_case
    if H!=rightA+rightB or H!=exact_original_sixflag_packet_hit_count(s,5):
        raise AssertionError("correct all-original-flag inclusion-exclusion split failed")
    insideC=min(inside,4800)
    outsideC=min(outside_case,480*d*d)
    allC=insideC+outsideC
    insideB=min(inside,300*b**4)
    outsideB=min(outside_case,40*b**3*outside+10*d*d*b**4)
    allB=insideB+outsideB
    caps={
      "D6":Fraction(rightA,2),
      "B-left/A-right":Fraction(min(rightA,allB),2),
      "C/A":Fraction(min(rightA,allC),2),
      "A-left/B-right":Fraction(rightB,2),
      "C/B":Fraction(min(rightB,insideC),2),
      "B/B-overlap":Fraction(min(rightB,insideB),2),
      "B/B-disjoint":Fraction(min(rightB,insideB),2)}
    if set(caps)!=set(R3_CERTIFIED_FLOORS):
        raise AssertionError("historical seven source classes changed")
    return {
      "s":s,"d":d,"M_original_sixflag_population":M,
      "five_packet_TOTAL_original_sixflag_sets":H,
      "case_inside_sixth_original_flag":inside,
      "case_OUTSIDE_sixth_original_flag":outside_case,
      "right_A_original_source_sixflag_sets":rightA,
      "right_B_original_source_sixflag_sets":rightB,
      "source_right_C_impossible":True,
      "POINT_C_inside_source_upper":insideC,
      "POINT_C_outside_source_upper":outsideC,
      "POINT_C_total_source_upper":allC,
      "POINT_B_inside_source_upper":insideB,
      "POINT_B_outside_source_upper":outsideB,
      "per_seven_historical_GF5_fifth_Walsh_bound":caps,
      "fifth_Walsh_C_B_uniform_bound":2400,
      "fifth_Walsh_C_A_bound_quadratic_in_original_degree":
          Fraction(allC,2),
      "selected_GF5_floor_weighted_fifth_Walsh_bound":
          sum(R3_CERTIFIED_FLOORS[c]*caps[c] for c in caps),
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

def genuine_original_five_packet_C_OUTSIDE_geometry(model,pairs):
    """Three source-point matches with ONE truly external ORIGINAL LINE flag.

    Five source packet slots plus one OUTSIDE source LINE slot. Exactly
    15 matchings; two internal packet-packet pairs each <=4 original
    line-point intersections, one selected-packet/external match <=2*d².
    Therefore original source POINT-C outside capacity <=480*d².
    """
    s,V,a,inc,f,g,_,_=_original_source(model)
    pairs=validate_disjoint_factor_swaps(V,pairs)
    if len(pairs)!=5:raise ValueError("five source LINE packets required")
    src=genuine_original_five_packet_C_geometry(model,pairs)
    chosenlines={l for pair in pairs for l in pair}
    byline=[{} for _ in range(V)]
    bypoint=[{} for _ in range(V)]
    for j,(p,l) in enumerate(inc):
        byline[l][p]=j;bypoint[p][l]=j
    external={}
    for k in range(5):
        options=[]
        for line in pairs[k]:
            for point,flag in byline[line].items():
                for L,extflag in bypoint[point].items():
                    if L not in chosenlines:
                        options.append((point,flag,extflag))
        if len(options)>2*(s+1)**2:
            raise AssertionError("original selected-packet/external incidence budget exceeded")
        external[k]=tuple(options)
    C=set();leftC=set()
    for matching in _perfect_packet_pairings(range(6)):
        choices=[]
        for i,j in matching:
            if j==5:
                opts=external[i]
            else:
                opts=src["meetings"][(i,j)]
            choices.append(opts)
        for candidate in product(*choices):
            points=[p for p,u,v in candidate]
            if len(set(points))!=3:continue
            Q=tuple(sorted(flag for p,u,v in candidate for flag in (u,v)))
            if len(set(Q))!=6:continue
            if any(sum(inc[q][1] in linepair for q in Q)!=1 for linepair in pairs):
                continue
            if sum(inc[q][1] not in chosenlines for q in Q)!=1:
                continue
            C.add(Q)
            if len({x for p in points for x in f[p]})==6:leftC.add(Q)
    if len(C)>480*(s+1)**2 or not leftC<=C:
        raise AssertionError("original GQ packet-outside source POINT C bound violated")
    return {"source_C_OUTSIDE":frozenset(C),
            "physical_LEFT_C_OUTSIDE":frozenset(leftC),
            "source_C_OUTSIDE_count":len(C),
            "physical_LEFT_C_OUTSIDE_count":len(leftC),
            "outside_original_point_C_bound":480*(s+1)**2,
            "original_packet_external_point_choices":external}

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
    external_geom=genuine_original_five_packet_C_OUTSIDE_geometry(model,pairs)
    if source["C/A"]+source["C/B"]!=(
        geom["physically_left_C_count"]+
        external_geom["physical_LEFT_C_OUTSIDE_count"]):
        raise AssertionError("true original fifth-order physical C-source split mismatch")
    cert=fifth_order_original_GQ_certificate(s)
    for c in R3_CERTIFIED_FLOORS:
        if abs(nums[c])>32*cert["per_seven_historical_GF5_fifth_Walsh_bound"][c]:
            raise AssertionError("original W3 fifth class coefficient >all-h cap")
    if abs(nums["C/A"])+abs(nums["C/B"])>16*(
        geom["physically_left_C_count"]+
        external_geom["physical_LEFT_C_OUTSIDE_count"]):
        raise AssertionError("original point-C total signed cap violated")
    if abs(nums["C/B"])>16*geom["physically_left_C_count"]:
        raise AssertionError("right-B historical original Q cannot use an outside LINE")
    return {"numerators":{c:nums[c] for c in R3_CERTIFIED_FLOORS},
       "coefficients":{c:Fraction(nums[c],32) for c in R3_CERTIFIED_FLOORS},
       "five_source_packet_eligible_left_Q_by_class":dict(source),
       "geometry":geom,"OUTSIDE_geometry":external_geom,
       "number_actual_complete_global_right_maps":32,
       "weighted_selected_GF5_floor_coefficient":Fraction(sum(
           R3_CERTIFIED_FLOORS[c]*nums[c] for c in R3_CERTIFIED_FLOORS),32),
       "root_230":"OPEN_WITH_FORMAL_BLOCKER"}
