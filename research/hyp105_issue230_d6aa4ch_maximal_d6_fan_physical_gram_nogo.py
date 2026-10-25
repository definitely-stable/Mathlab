"""HYP-105 #230 AA4-CH: maximal coaccepted original D6 fan and physical-only Gram no-go.

For ALL dyadic s=2^h, h>=2, construct ONE globally injected
complete original f,g and exactly s+1 distinct ORIGINAL sixflag Q_j
with exactly four common source incidence IDs, all historical D6 at
the SAME unchanged full original f,g. This attains the sharp source
LINE-star cap s+1 for a fan on fixed six original POINT factors.

A SINGLE GLOBAL POINT-factor image transposition f(p0)<->f(p2)
preserves each of these SAME original Q's six-coordinate physical
left/right 2factors and the ENTIRE actual right-side 256-global-g-map
twofamily physical Gram, but destroys historical D6 acceptance of
ALL s+1 fan Q at the unchanged original g.

All claims are about a fixed original fan, NOT the total selected
seven-GF5 count S_s and NOT Branch A/B/C.
"""
from itertools import combinations
from collections import Counter

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    classify_seven_all_a_original_Q,
    physical_overlapping_eight_masks, mixed_8cube_gram,
)
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    apply_disjoint_factor_swaps,
)
from hyp105_issue230_d6aa4by_original_independent_2factor_kernel import (
    physical_right_is_six_vertex_two_regular,
)
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS

SIX_CYCLE=((0,1),(1,2),(2,3),(3,4),(4,5),(0,5))
COMMON_RIGHT=((0,1),(1,2),(2,3),(3,4))


def _full_pair_injection(V,a,selected):
    """One WHOLE original typed image injection; all edge images in K_a."""
    chosen=tuple(tuple(sorted(e)) for e in selected.values())
    if len(set(chosen))!=len(chosen) or any(
        len(e)!=2 or e[0]==e[1] or min(e)<0 or max(e)>=a for e in chosen
    ):
        raise ValueError("selected complete-map pinned physical pairs invalid")
    if not all(type(i) is int and 0<=i<V for i in selected):
        raise ValueError("pinned ORIGINAL source factor IDs out of range")
    other=iter(e for e in combinations(range(a),2) if e not in set(chosen))
    full=tuple(tuple(sorted(selected[i])) if i in selected else next(other)
               for i in range(V))
    if len(full)!=V or len(set(full))!=V:
        raise AssertionError("whole globally injected f/g map not complete")
    return full


def _match_unique(candidates):
    """Independent deterministic augmenting-path SDR for the FOUR anchor POINTs."""
    owned={};slot_to_line={}
    def aug(slot,seen):
        for l in candidates[slot]:
            if l in seen:continue
            seen.add(l)
            previous=owned.get(l)
            if previous is None or aug(previous,seen):
                owned[l]=slot
                slot_to_line[slot]=l
                return True
        return False
    for i in range(len(candidates)):
        if not aug(i,set()):
            raise AssertionError("original four-point residual LINE star Hall theorem falsified")
    if len(set(slot_to_line.values()))!=len(candidates):
        raise AssertionError("source LINE star SDR repeated factor")
    return tuple(slot_to_line[i] for i in range(len(candidates)))


def original_maximal_D6_fan(power):
    """Finite original s=4/8 witness to ALL-h structural Hall theorem.

    The proof is for all s=2^h>=4, and requires an actual true
    symplectic W3 incidence graph rather than a fabricated host.
    """
    if type(power) is not int or power not in (2,3):
        raise ValueError("finite certified symplectic oracle h=2,3; proof all h>=2")
    model=fixture(power,"lex")
    s,V,a,inc,f0,g0,_,_=_original_source(model)
    if a<s+6:
        raise AssertionError("minimal original physical K_a lacks s+1 cherry centers")
    stars=[set() for _ in range(V)]
    flag_id={}
    for i,(p,l) in enumerate(inc):
        stars[p].add(l)
        flag_id[p,l]=i
    if any(len(st)!=s+1 for st in stars):
        raise AssertionError("true original W3 POINT stars not s+1")
    p4=0
    p5=next((q for q in range(1,V) if not stars[p4]&stars[q]),None)
    if p5 is None:
        raise AssertionError("W3 needs noncollinear original POINT factors")
    anchors=tuple(p for p in range(V) if p not in (p4,p5))[:4]
    if len(anchors)!=4:
        raise AssertionError("need four other actual ORIGINAL POINT factors")
    points=anchors+(p4,p5)
    heavyA=tuple(sorted(stars[p4]))
    heavyB=tuple(sorted(stars[p5]))
    if len(set(heavyA+heavyB))!=2*(s+1):
        raise AssertionError("two chosen original noncollinear POINT stars overlap")
    taken=set(heavyA+heavyB)
    candidate=tuple(tuple(sorted(stars[p]-taken)) for p in anchors)
    if any(len(c)<s-1 for c in candidate):
        raise AssertionError("original GQ pairwise LINE-star intersection at most one")
    common=_match_unique(candidate)
    all_line_ids=common+heavyA+heavyB
    if len(set(all_line_ids))!=2*s+6:
        raise AssertionError("all fan source LINE IDs must be genuinely different")
    target_f={p:e for p,e in zip(points,SIX_CYCLE)}
    f=_full_pair_injection(V,a,target_f)
    requested={l:e for l,e in zip(common,COMMON_RIGHT)}
    fan=[]
    for j in range(s+1):
        center=5+j
        requested[heavyA[j]]=(4,center)
        requested[heavyB[j]]=(0,center)
        Q=tuple(sorted((
            flag_id[anchors[0],common[0]],
            flag_id[anchors[1],common[1]],
            flag_id[anchors[2],common[2]],
            flag_id[anchors[3],common[3]],
            flag_id[p4,heavyA[j]],
            flag_id[p5,heavyB[j]],
        )))
        if len(set(Q))!=6:
            raise AssertionError("actual original sixflag IDs not all different")
        fan.append(Q)
    g=_full_pair_injection(V,a,requested)
    scrambled=list(f)
    scrambled[anchors[0]],scrambled[anchors[2]]=scrambled[anchors[2]],scrambled[anchors[0]]
    f_bad=tuple(scrambled)
    if set(f)!=set(f_bad):
        raise AssertionError("adversarial point swap changed occupied physical labels")
    for Q in fan:
        if classify_seven_all_a_original_Q(Q,f,g,inc)!="D6":
            raise AssertionError("maximal true ORIGINAL D6 fan construction failed")
        if classify_seven_all_a_original_Q(Q,f_bad,g,inc) is not None:
            raise AssertionError("one global f-transposition did NOT erase original fan D6")
        left_before=Counter(v for j in Q for v in f[inc[j][0]])
        left_after=Counter(v for j in Q for v in f_bad[inc[j][0]])
        if left_before!=left_after or len(left_before)!=6 or set(left_before.values())!={2}:
            raise AssertionError("same left physical 2factor eligibility was NOT preserved")
        if not physical_right_is_six_vertex_two_regular(Q,inc,g):
            raise AssertionError("same full g must physically accept ALL original fan Q")
    for i,Q in enumerate(fan):
        if any(len(set(Q)&set(other))!=4 for other in fan[:i]):
            raise AssertionError("fan original sixflags must share EXACTLY four same IDs")
    if len(fan)!=s+1:
        raise AssertionError("maximal star fan cardinality drift")
    normal=dict(model,left_labels=f,right_labels=g)
    adversarial=dict(model,left_labels=f_bad,right_labels=g)
    return {"s":s,"V":V,"a":a,"original_inc":inc,
      "point_ids":points,"line_ids":all_line_ids,
      "four_shared_original_flags":tuple(sorted(flag_id[p,l] for p,l in zip(anchors,common))),
      "fan":tuple(fan),"normal_model":normal,"scrambled_model":adversarial,
      "fan_size":len(fan),"baseline_historical_D6_positive":len(fan),
      "scrambled_historical_selected_seven_positive":0,
      "fan_weighted_original_GF5_baseline":R3_CERTIFIED_FLOORS["D6"]*len(fan),
      "fan_weighted_original_GF5_scrambled":0,
      "root_230":"OPEN_WITH_FORMAL_BLOCKER"}


def original_fan_common_physical_gram_referee(power):
    """Two true original fan Q, eight original LINE factors, 256 whole g states.

    Source f transposition leaves SAME original sixflag source IDs,
    SAME global g and right physical Gram, and all f-side physical
    six-coordinate eligible Q, yet rejects both historical D6 at x=0.
    """
    z=original_maximal_D6_fan(power)
    s,V,a,inc,f,g,_,_=_original_source(z["normal_model"])
    fan=z["fan"]; A,B=fan[0],fan[1]
    common=z["four_shared_original_flags"]
    if not (set(common)<=set(A)&set(B)):
        raise AssertionError("fan source common original flags missing")
    lsrc=tuple(inc[j][1] for j in common)+tuple(
        inc[j][1] for j in A if j not in common)+tuple(
        inc[j][1] for j in B if j not in common)
    if len(lsrc)!=8 or len(set(lsrc))!=8:
        raise AssertionError("mixed-eight source factors not distinct")
    free=iter(l for l in range(V) if l not in set(z["line_ids"]))
    packets=tuple((l,next(free)) for l in lsrc)
    if len(set(y for pair in packets for y in pair))!=16:
        raise AssertionError("eight original whole source swaps must be disjoint")
    physical=physical_overlapping_eight_masks(g,packets)
    mixed=mixed_8cube_gram(physical)
    if mixed["J"][0][0]<=0:
        raise AssertionError("true original fan two-Q physical coexistence lost")
    f_bad=z["scrambled_model"]["left_labels"]
    historical={"before":[],"after":[]}
    physical_count=0
    for x in range(256):
        changed=apply_disjoint_factor_swaps(
            g,packets,tuple(i for i in range(8) if x>>i&1))
        actual=tuple(physical_right_is_six_vertex_two_regular(Q,inc,changed)
                     for Q in (A,B))
        if tuple(bool(physical[key][x]) for key in ("A","B"))!=actual:
            raise AssertionError("raw true original Q physical masks != one global eightpacket")
        physical_count+=int(all(actual))
        for name,pmap in (("before",f),("after",f_bad)):
            classification=tuple(
                classify_seven_all_a_original_Q(Q,pmap,changed,inc)
                for Q in (A,B))
            if any(tag is not None and tag!="D6" for tag in classification):
                raise AssertionError("source LINE A/A fan may only be positive D6")
            historical[name].append(classification)
    if mixed["J"][0][0]!=physical_count:
        raise AssertionError("independent complete map physical pair overlap != mixed Gram")
    if historical["before"][0]!=("D6","D6") or historical["after"][0]!=(None,None):
        raise AssertionError("same original physical Gram does not distinguish historical D6 erasure")
    return {"s":s,"fan_size":z["fan_size"],
      "shared_physical_Gram_J00":mixed["J"][0][0],
      "independent_literal_original_joint_256_maps":physical_count,
      "physical_A_active":physical["A_active"],"physical_B_active":physical["B_active"],
      "before_original_center_selected_Q_tags":historical["before"][0],
      "scrambled_original_center_selected_Q_tags":historical["after"][0],
      "before_original_256_joint_D6":sum(x==("D6","D6") for x in historical["before"]),
      "after_original_256_joint_D6":sum(x==("D6","D6") for x in historical["after"]),
      "identical_global_g_and_256_right_physical_Gram":True,
      "left_physical_2factor_eligibility_same":True,
      "full_original_seven_GQ_S_NOT_COMPUTED":True,
      "root_230":"OPEN_WITH_FORMAL_BLOCKER"}
