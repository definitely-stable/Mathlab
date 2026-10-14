"""HYP-105 #230 D6-AA4-K: projection-aware ORIGINAL source pair charges.

NEW all-h exact structural CAP of physically disjoint source factor pairs
within each genuine accepted six-incidence seven-GF5 Q: A=9, B=6, C=3,
vs AA4-J's unconditional combinatorial 15. A/B/C are the verified
6-physical-coordinate 2-regular projections, not independent Q labels.
Full original W32 positional GF5 data; ROOT Branch A/B still OPEN.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_d6aa4i_original_spectral_coordinate import (
    all_h_source_disjoint_theorem,geometry)
from hyp105_issue230_d6aa4j_source_pair_gf5_charge import (
    charge_original_sixsets,_ceil,_eligible_pairs)

PATTERN_CAP={"A":9,"B":6,"C":3}
ALL_TAGS=frozenset((
    "D6","B-left/A-right","A-left/B-right","C/A","C/B",
    "B/B-overlap","B/B-disjoint"))
TAG_TYPES={
    "D6":frozenset({("A","A")}),
    "B-left/A-right":frozenset({("B","A")}),
    "A-left/B-right":frozenset({("A","B")}),
    "C/A":frozenset({("C","A"),("A","C")}),
    "C/B":frozenset({("C","B"),("B","C")}),
    "B/B-overlap":frozenset({("B","B")}),
    "B/B-disjoint":frozenset({("B","B")}),
}


def six_incidence_projection_capacity(incidence_endpoints,labels,a):
    """Independent abstract 6-coordinate 2-regular physical multigraph check.

    Six TRUE ORIGINAL incidence endpoints need not be six distinct source
    factors. Each source factor has ONE injected pair label, repeated as
    often as the same factor occurs among six original incidences.
    """
    if len(incidence_endpoints)!=6 or type(a) is not int or a<6:
        raise ValueError("exactly six original source incidence endpoints required")
    sources=Counter(incidence_endpoints)
    profile=tuple(sorted(sources.values(),reverse=True))
    kind={tuple([1]*6):"A",(2,1,1,1,1):"B",
          (2,2,2):"C"}.get(profile)
    if kind is None:
        raise ValueError("not one accepted A/B/C original source projection")
    coords=Counter()
    touched={}
    for p,count in sources.items():
        if type(p) is not int or p<0 or p>=len(labels):
            raise ValueError("original source factor ID invalid")
        e=tuple(labels[p])
        if (len(e)!=2 or any(type(x) is not int for x in e)
                or not 0<=e[0]<e[1]<a):
            raise ValueError("invalid canonical physical source-factor image")
        touched[p]=frozenset(e)
        coords.update({e[0]:count,e[1]:count})
    if len(set(touched.values()))!=len(touched):
        raise ValueError("original source factors do not have injective physical labels")
    if len(coords)!=6 or any(v!=2 for v in coords.values()):
        raise ValueError("not an accepted degree-two six-coordinate projection")
    physical_disjoint=sum(not (touched[u]&touched[v])
                          for u,v in combinations(sorted(touched),2))
    cap=PATTERN_CAP[kind]
    if physical_disjoint!=cap:
        raise AssertionError("A/B/C six-coordinate exact physical disjoint cap false")
    return {
        "true_original_source_projection_kind":kind,
        "original_distinct_source_factors":len(touched),
        "physical_six_coordinate_degree_two":True,
        "ALL_physically_disjoint_original_factor_pairs":physical_disjoint,
        "exact_A_B_C_source_pair_disjoint_capacity":cap,
        "source_factor_multiplicity_profile":profile,
    }


def conditional_average_transfer(s,minimum_average_multiplicity):
    """All-h CONDITIONAL average positive-Q multiplicity (not per-pair).

    With D_t>=s^5/4 for s>=4 and I_t=D_t*average,
    true accepted original six-Q charges <=9*S, so S>=cs^6/36
    whenever the actual average >=c*s across globally forced pairs.
    """
    s0=all_h_source_disjoint_theorem(s)
    c=Fraction(minimum_average_multiplicity)
    if c<0:
        raise ValueError("nonnegative average positive-Q multiplicity required")
    D=max(0,s0["uniform_forced_physically_disjoint_collinear_lower"])
    return {
        "s":s,
        "hypothesized_average_actual_positive_Q_multiplicity":str(c),
        "source_disjoint_original_pair_lower":D,
        "conditional_seven_Q_lower_using_sharp_projection_9":_ceil(c*D/9),
        "AA4J_conditional_seven_Q_lower_using_loose_15":_ceil(c*D/15),
        "all_h_if_average_at_least_c_s_then_S_at_least_c_s6_over36":
            s>=4 and D*4>=s**5,
        "any_global_positive_average_claim_ESTABLISHED":False,
        "root_all_h_seven_positive_PROVED":False,
    }


def true_original_projection_charge(g,model,accepted):
    """Class-sensitive ORIGINAL-Q charges, both source types, exact independent audit.

    Re-evaluates A/B/C structure from ACTUAL physical labels, NOT from
    class tags as a surrogate. Accepting historical seven_census tags is
    necessary but the source/physical pattern gets rechecked separately.
    """
    from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS
    accepted=dict(accepted)
    if any(not isinstance(Q,tuple) or len(Q)!=6 or len(set(Q))!=6
           or any(type(i) is not int or not 0<=i<len(g["original_incidences"])
                  for i in Q) or tag not in ALL_TAGS for Q,tag in accepted.items()):
        raise ValueError("accepted positive Q must be six distinct ORIGINAL IDs and valid 7-class tag")
    orig=tuple(g["original_incidences"])
    labels={
        "P":tuple(tuple(x) for x in model["left_labels"]),
        "L":tuple(tuple(x) for x in model["right_labels"]),
    }
    pair_sets={}
    paircharge={"P":Counter(),"L":Counter()}
    for t in ("P","L"):
        pair_sets[t],_= _eligible_pairs(g,labels[t],source_type=t)
    classes=defaultdict(lambda:{"count":0,"weighted_51floor":0,
                  "P_cap":0,"L_cap":0,"P_charge":0,"L_charge":0})
    orientations=Counter()
    total_caps={"P":0,"L":0}
    total_charges={"P":0,"L":0}
    max_single={"P":0,"L":0}
    positive_Q_without_any_pair=0
    for Q,tag in sorted(accepted.items()):
        endpoints=tuple(orig[i] for i in Q)
        side={}
        touched={}
        for t,j in (("P",0),("L",1)):
            side[t]=six_incidence_projection_capacity(
                tuple(edge[j] for edge in endpoints),labels[t],g["a"])
            touched[t]=frozenset(edge[j] for edge in endpoints)
        kind=(side["P"]["true_original_source_projection_kind"],
              side["L"]["true_original_source_projection_kind"])
        if kind not in TAG_TYPES[tag]:
            raise AssertionError("true seven GF5 tag incompatible with independently rechecked A/B/C")
        orientations[kind]+=1
        stats=classes[tag]
        stats["count"]+=1
        stats["weighted_51floor"]+=R3_CERTIFIED_FLOORS[tag]
        q_total=0
        for t in ("P","L"):
            c=side[t]["exact_A_B_C_source_pair_disjoint_capacity"]
            this=frozenset((u,v) for u,v in combinations(sorted(touched[t]),2)
                           if (u,v) in pair_sets[t])
            if len(this)>c:
                raise AssertionError("actual positive Q exceeds source physical disjoint capacity")
            # Independent source-label direct count of ALL physically
            # disjoint source-factor pairs inside Q (without GQ adjacency).
            direct=sum(not(set(labels[t][u])&set(labels[t][v]))
                       for u,v in combinations(sorted(touched[t]),2))
            if direct!=c:
                raise AssertionError("independent physical disjoint factor count not A/B/C structural cap")
            for pair in this:paircharge[t][pair]+=1
            total_caps[t]+=c
            total_charges[t]+=len(this)
            max_single[t]=max(max_single[t],len(this))
            stats[t+"_cap"]+=c
            stats[t+"_charge"]+=len(this)
            q_total+=len(this)
        positive_Q_without_any_pair+=q_total==0
    S=len(accepted)
    W=sum(R3_CERTIFIED_FLOORS[tag] for tag in accepted.values())
    if S!=sum(v["count"] for v in classes.values()) or W!=sum(
            v["weighted_51floor"] for v in classes.values()):
        raise AssertionError("ORIGINAL seven-Q class partition or GF5 weight lost")
    if (total_caps["P"]>9*S or total_caps["L"]>9*S or
          sum(total_caps.values())>18*S):
        raise AssertionError("all-h A/B/C two-sided physical disjoint capacity violated")
    for t in ("P","L"):
        if total_charges[t]>total_caps[t]:
            raise AssertionError("true source GQ charge exceeds physical-disjoint A/B/C upper")
        if sum(paircharge[t].values())!=total_charges[t]:
            raise AssertionError("Q-to-source pair incidence conservation failed")
        # Independently iterate all ORIGINAL eligible source pairs and
        # all historical positive Q via AA4-J (pair-major verification).
        independent=charge_original_sixsets(
            g,model,accepted,source_type=t)
        if independent["all_genuine_original_pair_to_positive_Q_weak_charges"]!=total_charges[t]:
            raise AssertionError("AA4-J fully independent pair-major ORIGINAL GF5 charge disagreed")
        if len(paircharge[t])!=independent["original_pairs_covered_by_any_positive_sixset"]:
            raise AssertionError("independent original pair coverage disagreed")
        if max_single[t]>9:
            raise AssertionError("even one accepted Q exceeds all-h 9 bound")
    numerator_ratio=min(
        (Fraction(R3_CERTIFIED_FLOORS[tag],v["P_cap"]+v["L_cap"])
         for tag,v in classes.items() if v["count"]),default=None)
    # The universal numerical w/cap ratio is from each permitted tag's
    # worst side orientation, not guessed from whichever class happened
    # to occur in the 24-state finite fiber.
    ratios={}
    for tag in ALL_TAGS:
        cap=max(PATTERN_CAP[p]+PATTERN_CAP[l] for p,l in TAG_TYPES[tag])
        ratios[tag]=Fraction(R3_CERTIFIED_FLOORS[tag],cap)
    universal_GF5_ratio=min(ratios.values())
    all_charge=sum(total_charges.values())
    certified_GF5_from_charge=_ceil(universal_GF5_ratio*all_charge)
    if certified_GF5_from_charge>W:
        raise AssertionError("selected 51 palette GF5 numerator weak dual broken")
    return {
        "original_seven_Q":S,
        "selected_GF5_51palette_numerator":W,
        "true_ORIGINAL_Q_by_class":dict(sorted((k,dict(v)) for k,v in classes.items())),
        "genuine_original_Q_by_independent_half_projection_kind":{
            p+"/"+l:n for (p,l),n in sorted(orientations.items())},
        "source_P_charge":total_charges["P"],
        "source_L_charge":total_charges["L"],
        "joint_source_pair_to_original_GF5_positive_Q_charge":all_charge,
        "source_P_projection_disjoint_capacity":total_caps["P"],
        "source_L_projection_disjoint_capacity":total_caps["L"],
        "joint_A_B_C_projection_disjoint_capacity":sum(total_caps.values()),
        "all_h_unconditional_P_and_L_capacity_per_positive_Q":9,
        "all_h_unconditional_joint_capacity_per_positive_Q":18,
        "loose_AA4J_15_Q_single_type_capacity":15,
        "class_sensitive_exact_charges_conserved":True,
        "independent_AA4J_pair_major_charge_oracle":"PASS",
        "source_P_projection_aware_S_floor":_ceil(Fraction(total_charges["P"],9)),
        "source_L_projection_aware_S_floor":_ceil(Fraction(total_charges["L"],9)),
        "joint_projection_aware_S_floor":_ceil(Fraction(all_charge,18)),
        "joint_loose_AA4J_S_floor":_ceil(Fraction(all_charge,30)),
        "GF5_selected_numerator_per_joint_charge_rational_floor":
            str(universal_GF5_ratio),
        "selected_GF5_numerator_floor_from_joint_charge":
            certified_GF5_from_charge,
        "true_positive_original_Q_with_zero_P_and_L_eligible_pair_charge":
            positive_Q_without_any_pair,
        "all_7_classes_in_GF5_numerator_ratio":len(ratios),
        "all_h_root_s6_PROVED":False,
    }


def genuine_original_W32_projection_charge_fiber(scheme):
    """Historical exact complete original 24-state four-point GF5 audit."""
    from hyp105_issue230_projection import fixture
    from hyp105_g5e2b3e1b0_seven_signature import (
        seven_census,R3_CERTIFIED_FLOORS)
    from hyp105_issue230_d6aa4c_edit_transversal import (
        genuine_original_positive_hypergraph,incidence_cover_bits)
    from hyp105_issue230_d6aa4d_mixed_transversal_fibers import (
        finite_source_support_partition)
    from hyp105_issue230_d6aa4g_overlap_capacity import (
        complete_fixed_image_states)
    if scheme not in ("S68","S72"):
        raise ValueError("true ORIGINAL pinned W32 only")
    model=fixture(1,scheme)
    g=geometry(2,model["incidences"])
    records=genuine_original_positive_hypergraph(model)["records"]
    bits,weights,mask=incidence_cover_bits(records)
    p=finite_source_support_partition(bits,weights,mask)
    if p["number_transversal_blocks"]!={"S68":53,"S72":119}[scheme]:
        raise AssertionError("true original critical source transversals changed")
    block=next((tuple(b) for b in p["transversal_original_factor_blocks"]
               if len(b)==4 and all(0<=i<15 for i in b)),None)
    if block is None:
        raise AssertionError("true source four-point critical block missing")
    initial=tuple(tuple(model["left_labels"][i]) for i in block)
    states=complete_fixed_image_states(("P",)*4,initial)
    fixed_right=tuple(tuple(x) for x in model["right_labels"])
    all_complete=[]
    for assignment in states:
        left=list(tuple(tuple(e) for e in model["left_labels"]))
        for i,label in zip(block,assignment):left[i]=label
        complete={**model,"left_labels":tuple(left),"right_labels":fixed_right}
        census=seven_census(complete,independent_checks=False,witness_sets=True)
        if len(census["sets"])!=census["S_seven"] or census[
               "GF5_seven_lower_numerator"]!=sum(
               R3_CERTIFIED_FLOORS[t] for t in census["sets"].values()):
            raise AssertionError("full actual ORIGINAL GF5 seven classifier mass invalid")
        charge=true_original_projection_charge(g,complete,census["sets"])
        if charge["original_seven_Q"]!=census["S_seven"] or charge[
              "selected_GF5_51palette_numerator"]!=census[
              "GF5_seven_lower_numerator"]:
            raise AssertionError("lost complete true ORIGINAL seven-GF5 Q")
        all_complete.append(charge)
    baseline={"S68":68,"S72":72}[scheme]
    if len(all_complete)!=24 or all_complete[0]["original_seven_Q"]!=baseline:
        raise AssertionError("actual 24 complete source map baseline changed")
    if min(x["original_seven_Q"] for x in all_complete)!=baseline:
        raise AssertionError("AA4-J exact S68/S72 four-point minimum regression")
    fields=(
        "original_seven_Q",
        "source_P_charge","source_L_charge",
        "joint_source_pair_to_original_GF5_positive_Q_charge",
        "source_P_projection_aware_S_floor",
        "source_L_projection_aware_S_floor",
        "joint_projection_aware_S_floor",
        "joint_loose_AA4J_S_floor",
        "selected_GF5_numerator_floor_from_joint_charge",
        "joint_A_B_C_projection_disjoint_capacity",
        "true_positive_original_Q_with_zero_P_and_L_eligible_pair_charge",
    )
    ranges={k:{"min":min(q[k] for q in all_complete),
               "max":max(q[k] for q in all_complete)}
             for k in fields}
    return {
        "scheme":scheme,
        "original_four_point_source_block":block,
        "complete_globally_injected_source_states":24,
        "complete_original_six_candidate_sets_per_state":62370,
        "all_24_complete_original_GF5_results":all_complete,
        "exact_ranges":ranges,
        "strictly_one_true_original_Q_classification_per_state":True,
        "source_pair_Q_projection_charge_all_h_theorem_not_GF5_root":True,
        "root_A":"OPEN","root_B":"OPEN",
    }


def report(scheme=None):
    r={
        "slice":"HYP105-ISSUE230-D6-AA4-K-PROJECTION-AWARE-PAIR-CHARGE",
        "A_B_C_original_six_coordinate_exact_disjoint_cap":{"A":9,"B":6,"C":3},
        "all_h_original_P_or_L_charge_le_9S":True,
        "all_h_joint_P_plus_L_charge_le_18S":True,
        "all_h_conditional_average_multiplicity":conditional_average_transfer(4,4),
        "universal_GF5_risk_ratio_for_certified_class_floors_only":True,
        "all_h_nonzero_total_charge_lower_proved":False,
        "root_A":"OPEN","root_B":"OPEN",
        "full_R3_proved":False,"ASET_exponent_proved":False,
    }
    if scheme is not None:
        r["true_original_W32"]=genuine_original_W32_projection_charge_fiber(scheme)
    return r


if __name__=="__main__":
    import argparse,json
    a=argparse.ArgumentParser()
    a.add_argument("--scheme",choices=("S68","S72"))
    p=a.parse_args()
    print(json.dumps(report(p.scheme),indent=2,sort_keys=True))
