"""AA4-CM: strict negative covariance of TWO genuine ORIGINAL D6 sixflags.

For EVERY dyadic s=2^h, h>=2, in actual symplectic W(3,s):
choose EIGHT different original POINT factor IDs and 12 different
original LINE factors (two each at the four shared POINTs, one each
at each of the four exclusive POINTs), via real LINE-star Hall SDR.
Build ONE complete injected original POINT f with left cherry-center
two physical C6 families on 8 genuine POINT factors; ONE complete
injected original LINE g maps their 12 LINE IDs into TWO DISJOINT
physical sixcycles with prescribed six-original-incidence-POSITION
right dual cycles. The right cycles can be chosen so the two
TRUE original six-ID Q_A,Q_B each attain historical A/A D6 on
exactly 4/96 of the SAME global legal 96 f-map orbit, and are NEVER
coaccepted. Their HISTORICAL 5643-weighted named-Q GF5 covariance
is therefore EXACTLY -5643^2/576 for EVERY h>=2.

The two Q share FOUR original POINT factors, but have ZERO common
incidence IDs: their original LINE factors at each shared POINT
are chosen DISTINCT. This is a signed named-sixflag witness, NOT
a negative covariance theorem for their entire original POINT-A
sixflag families and NOT an all-h global S_s counterfamily.
"""
from collections import Counter
from fractions import Fraction

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4ch_maximal_d6_fan_physical_gram_nogo import (
    _full_pair_injection,_match_unique,
)
from hyp105_issue230_d6aa4ci_dual_cycle_orbit_fiber_invariant import (
    _six_position_dual_cycle,W_D,
)
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_seven_all_a_original_Q,
)
from hyp105_issue230_d6aa4cl_shared_four_point_fibers_covariance import (
    ORBIT,FAMILIES,GRAPH_CASES,complete_overlapping_global_f,
    original_two_fiber_same_global_96_orbit,_cov,_mean,
)
from hyp105_issue230_projection import fixture

N_STATES=96
EXPECTED_NAMED_NEGATIVE_COV=Fraction(-W_D*W_D,576)


def _right_physical_edges_for_dual(cycle,physical_vertices):
    """Build an actual connected physical C6 from its labeled position dual.

    Each unordered edge of the six-position dual becomes ONE unique
    physical coordinate; each original incidence position collects
    its TWO incident dual-coordinate vertices. The resulting six
    physical pair edges have exactly the requested original six-column
    dual. Uses NO independent per-source-Q f/g map redraw.
    """
    if not isinstance(cycle,frozenset) or len(cycle)!=6:
        raise ValueError("right Hamiltonian six-position original dual required")
    vertices=tuple(physical_vertices)
    if len(vertices)!=6 or len(set(vertices))!=6 or any(
        type(i) is not int or i<0 for i in vertices
    ):
        raise ValueError("six distinct physical coordinate IDs required")
    dual=tuple(sorted((tuple(sorted(e)) for e in cycle)))
    if any(len(e)!=2 or any(type(i) is not int or not 0<=i<6 for i in e)
           for e in dual):
        raise ValueError("valid true ORIGINAL six-column labeled C6 dual needed")
    at=[[] for _ in range(6)]
    for vertex,(p,q) in zip(vertices,dual):
        at[p].append(vertex);at[q].append(vertex)
    if any(len(x)!=2 for x in at):
        raise ValueError("dual must be 2regular at every original incidence position")
    out=tuple(tuple(sorted(x)) for x in at)
    if len(set(out))!=6 or _six_position_dual_cycle(out)!=cycle:
        raise ValueError("original dual must form connected Hamiltonian sixcycle")
    return out


def _literal_left_cherry_dual_orbit():
    """No original LINE map involved: EXACT physical complete f subgroup."""
    shared,ae,be=GRAPH_CASES["vertex_replacement"]
    images=tuple(shared+ae+be)
    allA={};allB={}
    for state in ORBIT:
        sigma,alpha,beta=state
        mapping=tuple(images[sigma[i]] for i in range(4))+(
            images[4+alpha],images[5-alpha],
            images[6+beta],images[7-beta])
        allA[state]=_six_position_dual_cycle(
            tuple(mapping[i] for i in FAMILIES["A"]))
        allB[state]=_six_position_dual_cycle(
            tuple(mapping[i] for i in FAMILIES["B"]))
        if allA[state] is None or allB[state] is None:
            raise AssertionError("both original left physical C6 must persist")
    return allA,allB


def exact_original_negative_named_dual_choice():
    """Entire 96-map original dual cycle compatibility: exact negative pair.

    Deterministically select first ORIGINAL right sixposition C6 pair
    with BOTH positive support and DISJOINT accepted map supports.
    """
    allA,allB=_literal_left_cherry_dual_orbit()
    binsA=tuple(sorted(set(allA.values()),key=lambda z:tuple(
        sorted(tuple(sorted(e)) for e in z))))
    binsB=tuple(sorted(set(allB.values()),key=lambda z:tuple(
        sorted(tuple(sorted(e)) for e in z))))
    if len(binsA)!=24 or len(binsB)!=24:
        raise AssertionError("cherry-original A/B source f dual orbit must each have 24 cycles")
    candidates=0
    negative=0
    chosen=None
    for ca in binsA:
        statesA={st for st,cy in allA.items() if cy==ca}
        if len(statesA)!=4:
            raise AssertionError("each reachable right dual has exactly 4 legal original f states")
        for cb in binsB:
            statesB={st for st,cy in allB.items() if cy==cb}
            if len(statesB)!=4:
                raise AssertionError("each reachable B right dual has 4 legal original f states")
            candidates+=1
            if not statesA&statesB:
                negative+=1
                if chosen is None:chosen=(ca,cb,statesA,statesB)
    if chosen is None or negative==0:
        raise AssertionError("negative covariance original all-h physical orientation no-go failed")
    ca,cb,statesA,statesB=chosen
    qa=tuple(W_D*int(allA[st]==ca) for st in ORBIT)
    qb=tuple(W_D*int(allB[st]==cb) for st in ORBIT)
    cov=_cov(qa,qb)
    if cov!=EXPECTED_NAMED_NEGATIVE_COV:
        raise AssertionError("noncoaccepted original named D6 covariance expected -5643²/576")
    return {"original_f_A_labeled_right_cycle":ca,
            "original_f_B_labeled_right_cycle":cb,
            "right_dual_orientation_pairs_examined":candidates,
            "right_dual_pairs_with_strictly_negative_named_covariance":negative,
            "selected_A_accepting_complete_original_f_states":frozenset(statesA),
            "selected_B_accepting_complete_original_f_states":frozenset(statesB),
            "each_true_original_D6_named_Q_positive_states":4,
            "both_TRUE_original_Q_D6_coaccepted_states":0,
            "named_historical_weighted_GF5_covariance":cov,
            "weighted_named_mean_each":Fraction(W_D,24),
            "all_h_ge_2_original_realizability_proved_by_Hall":True}


def true_original_negative_D6_pair_fixture(power):
    """Finite actual symplectic original W34/W38 test of the ALL-h construction."""
    if type(power) is not int or power not in (2,3):
        raise ValueError("true-original finite referees W34/W38 only, theorem all h>=2")
    model=fixture(power,"lex")
    s,V,a,inc,f,g,by_p,_=_original_source(model)
    if s<4 or a<12:raise AssertionError("physical alphabet must support 12 disjoint right C6 vertices")
    pts=tuple(range(8))
    left_edges=sum(GRAPH_CASES["vertex_replacement"],())
    f=_full_pair_injection(V,a,dict(zip(pts,left_edges)))
    # Eight unique true ORIGINAL POINT factors with TWELVE true LINE
    # slots: each common POINT appears twice with distinct actual
    # incidence LINE IDs, each exclusive original POINT once.
    slots=tuple((fam,local,i,pts[i]) for fam,inds in FAMILIES.items()
                for local,i in enumerate(inds))
    assert len(slots)==12
    candidates=tuple(tuple(sorted(inc[j][1] for j in by_p[p]))
                     for fam,local,i,p in slots)
    line_ids=_match_unique(candidates)
    if len(line_ids)!=12 or len(set(line_ids))!=12:
        raise AssertionError("actual original W3 12 LINE source ID Hall SDR failed")
    choice=exact_original_negative_named_dual_choice()
    projected={
        "A":_right_physical_edges_for_dual(
            choice["original_f_A_labeled_right_cycle"],range(6)),
        "B":_right_physical_edges_for_dual(
            choice["original_f_B_labeled_right_cycle"],range(6,12))}
    pinned={line_ids[k]:projected[slots[k][0]][slots[k][1]]
            for k in range(len(slots))}
    if len(pinned)!=12 or len(set(pinned.values()))!=12:
        raise AssertionError("actual original g 12 pinned right pair edges not injected")
    g=_full_pair_injection(V,a,pinned)
    incidence_id={(p,l):j for j,(p,l) in enumerate(inc)}
    QA=[];QB=[]
    for k,(fam,local,i,p) in enumerate(slots):
        flag=incidence_id[(p,line_ids[k])]
        (QA if fam=="A" else QB).append(flag)
    QA=tuple(sorted(QA));QB=tuple(sorted(QB))
    if len(QA)!=6 or len(QB)!=6 or len(set(QA))!=6 or len(set(QB))!=6:
        raise AssertionError("six distinct genuine original flag IDs required on each side")
    if set(QA)&set(QB):
        raise AssertionError("different original LINE IDs at four common POINTs yield NO common original incidence IDs")
    out=dict(model,left_labels=f,right_labels=g)
    status={"A":[],"B":[]}
    direct={"A":{},"B":{}}
    for state in ORBIT:
        changed=complete_overlapping_global_f(f,pts,state)
        if set(changed)!=set(f):raise AssertionError("whole map changed occupied original POINT image pairs")
        for fam,Q in (("A",QA),("B",QB)):
            tag=classify_seven_all_a_original_Q(Q,changed,g,inc)
            if tag not in (None,"D6"):
                raise AssertionError("original named Q source right A only may be historically D6")
            direct[fam][state]=W_D*int(tag=="D6")
            if tag=="D6":status[fam].append(state)
    if len(status["A"])!=4 or len(status["B"])!=4 or (
        set(status["A"])&set(status["B"])):
        raise AssertionError("actual globally injected original Q D6 negative covariance supports not as claimed")
    x=tuple(direct["A"][st] for st in ORBIT)
    y=tuple(direct["B"][st] for st in ORBIT)
    if _cov(x,y)!=EXPECTED_NAMED_NEGATIVE_COV:
        raise AssertionError("true original W3 negative named D6 covariance != abstract physical dual construction")
    return {"s":s,"V":V,"a":a,"actual_original_model":out,
            "eight_REAL_original_POINT_source_ids":pts,
            "twelve_distinct_REAL_original_LINE_source_ids":line_ids,
            "QA_six_true_original_incidence_IDs":QA,
            "QB_six_true_original_incidence_IDs":QB,
            "true_original_common_POINT_factor_ids":4,
            "true_original_common_incidence_flag_ids":0,
            "physical_RIGHT_image_coordinates_disjoint":True,
            "one_fixed_complete_original_LINE_g":True,
            "one_same_GLOBAL_complete_original_f_map_per_orbit_state":True,
            "all_96_genuine_original_global_states_classified":96,
            "named_GF5_D6_positive_states_A":len(status["A"]),
            "named_GF5_D6_positive_states_B":len(status["B"]),
            "named_GF5_D6_coaccepted_states":0,
            "named_GF5_historical_weighted_covariance":_cov(x,y),
            "pure_named_negative_pair_not_full_original_fiber":True}


def full_original_fiber_check_negative_named_vs_entire(power):
    """Independent full TRUE original six-POINT-A fibers: NEVER infer the sign."""
    z=true_original_negative_D6_pair_fixture(power)
    full=original_two_fiber_same_global_96_orbit(
        z["actual_original_model"],z["eight_REAL_original_POINT_source_ids"])
    return {"named":z,
            "entire_source_POINT_A_fiber_covariance":
               full["historical_score_covariance_A_B"],
            "entire_source_POINT_A_fiber_mean_A":full["historical_score_mean_A"],
            "entire_source_POINT_A_fiber_mean_B":full["historical_score_mean_B"],
            "entire_source_POINT_A_fiber_right_eligible_Q_A":
               len(full["original_histograms"]["A"]["eligible_actual_original_Q"]),
            "entire_source_POINT_A_fiber_right_eligible_Q_B":
               len(full["original_histograms"]["B"]["eligible_actual_original_Q"]),
            "full_global_seven_GQ_S_NOT_computed":True,
            "root_230":"OPEN_WITH_FORMAL_BLOCKER"}
