"""AA4-BM: TRUE-ORIGINAL rooted B/A REPAIR in ≤4 global source swaps.

ALL h>=5, genuine W(3,s), EVERY fully fixed source point f and
EVERY fully fixed source LINE g. For EVERY source POINT cherry pair
whose two original LINE images have local physical hole-degree <=
floor((a-4)/8), an explicit ≤4 original LINE-factor IMAGE
transposition path (not random re-completion) fixes source f,
right occupied support E, BOTH originally pinned LINE source
factor images, and SIX TRUE original incidence IDs and reaches g'
with at least ONE accepted historical positive GF5 B/A sixflag
containing the original root. This holds for >3/4 ORIGINAL source
POINT cherries by AA4-BL, but the repaired g' DEPENDS on root.

Previously #545/#547/#550 prove local ≤5 swaps for a DIFFERENT
D6 event, not this 4-swap root B/A repair preserving 2 images.
Root #230 demands the UNCHANGED arbitrary g positive: NOT PROVED.
"""
from itertools import combinations, permutations,product
from collections import Counter

from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bj_cherry_hall_defect import _full_four_patterns
from hyp105_issue230_d6aa4bl_two_pin_conditional_BA import (
    every_fixed_original_g_good_root_pin_majority,
)
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
from hyp105_issue230_d6aa4q_two_sided_seven_join import independent_joint_classify


def _edge(a,b):
    return (a,b) if a<b else (b,a)


def missing_endpoint_degrees(labels,a):
    """Missing degrees of TRUE complete globally injective physical pair support."""
    occupied=set(labels)
    out=[0]*a
    for u in range(a):
        out[u]=sum(_edge(u,v) not in occupied for v in range(a) if v!=u)
    return tuple(out)


def _root_flags(inc,originals,side,p,flags):
    if type(side) is not int or side not in (0,1):
        raise ValueError("side 0 true source POINT, side 1 true source LINE")
    if type(p) is not int or not 0<=p<len(originals):
        raise ValueError("true original source point/LINE ID invalid")
    if len(flags)!=2 or len(set(flags))!=2 or any(
        type(j) is not int or j not in originals[p] for j in flags
    ):
        raise ValueError("two distinct ACTUAL original incidence flag IDs in same original source factor")
    return tuple(flags)


def find_genuine_source_root_C4_sixflags(model,side,p,flags):
    """Return ONE genuine original B/A source Q without inspecting target.

    Enumerate physical first-side occupied C4 and TRUE original source
    incidence flags, with SIX DISTINCT opposite genuine source factors.
    TRUE source LINE/POINT neighborhoods remain frozen. FINITE
    constructive algorithm, no complexity claim for large s.
    """
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    if type(side) is not int or side not in (0,1):
        raise ValueError("true original source side must be exactly POINT=0 or LINE=1")
    by=(byP,byL)[side]
    flags=_root_flags(inc,by,side,p,flags)
    first=(f,g)[side]
    inv={edge:id for id,edge in enumerate(first)}
    banned=set(first[p])
    root_opposite={inc[j][1-side] for j in flags}
    if len(root_opposite)!=2:raise AssertionError("original source anchor has two distinct opposite factors")
    vertices=tuple(x for x in range(a) if x not in banned)
    for four in combinations(vertices,4):
        _,_,patterns=_full_four_patterns(four,set(inv))
        for name,ed in patterns:
            if name!="C4":continue
            source_factors=tuple(inv[edge] for edge in ed)
            if len(set(source_factors))!=4 or p in source_factors:
                raise AssertionError("true globally injected source root residual invalid")
            # A deterministic greedily chosen FOUR actual ORIGINAL source
            # incidences is possible for d>=6, but enumerate/backtrack
            # here so tiny genuine W32/W34 also furnish legal examples.
            neighbors=tuple(by[x] for x in source_factors)
            for chosen in product(*neighbors):
                Q=tuple(sorted(flags+chosen))
                if len(set(Q))!=6:
                    raise AssertionError("repeated actual original incidence flag")
                opp=(inc[i][1-side] for i in Q)
                if len(set(opp))!=6:
                    continue
                return Q
    return None


def find_target_C6_with_two_original_pinned_edges(occupied,a,e1,e2):
    """Explicit finite undirected physical 6-cycle with BOTH exact pins.

    Enumerate the physical cycle order families used by the rigorous
    AA4-BL missing-degree certificate. On high-h regular pins a cycle
    MUST exist; at s=2,4 physical holes may make an arbitrary pin pair
    fail (the caller must fail closed, not assert a false theorem).
    """
    E=set(occupied)
    if e1==e2 or e1 not in E or e2 not in E:
        raise ValueError("two distinct occupied physical pair pins are required")
    common=set(e1)&set(e2)
    if len(common)==1:
        middle=next(iter(common))
        u=next(x for x in e1 if x!=middle)
        w=next(x for x in e2 if x!=middle)
        rest=[x for x in range(a) if x not in (u,middle,w)]
        for x,y,z in permutations(rest,3):
            candidate=(e1,e2,_edge(w,x),_edge(x,y),_edge(y,z),_edge(z,u))
            if len(set(candidate))==6 and all(edge in E for edge in candidate):
                return tuple(sorted(candidate))
    elif len(common)==0:
        for u,v in ((e1[0],e1[1]),(e1[1],e1[0])):
            for w,x in ((e2[0],e2[1]),(e2[1],e2[0])):
                rest=[j for j in range(a) if j not in (u,v,w,x)]
                for y,z in permutations(rest,2):
                    candidate=(e1,_edge(v,y),_edge(y,w),e2,_edge(x,z),_edge(z,u))
                    if len(set(candidate))==6 and all(edge in E for edge in candidate):
                        return tuple(sorted(candidate))
    else:
        raise AssertionError("two different physical pair edges cannot share two endpoints")
    return None


def original_fixed_pair_repair_cherry_four_swaps(model,side,p,flags,
                                                *,require_regular=True):
    """Build one FULL legal physical original map g' within <=4 source swaps.

    The two original opposite source factor images represented by the
    genuine root flags are PINNED to their PREVIOUS physical images.
    This works for EACH TRUE root with a valid C4 source candidate
    and physical C6 target. If a supposed high-h 'regular' root fails,
    raises rather than silently treating a constructed example as proof.
    """
    s,V,a,inc,f,g,byP,byL=_original_source(model)
    if type(side) is not int or side not in (0,1):
        raise ValueError("true original source side must be exactly POINT=0 or LINE=1")
    by=(byP,byL)[side]
    flags=_root_flags(inc,by,side,p,flags)
    first=(f,g)[side]
    second=(g,f)[side]
    original_second=tuple(second)
    pins=tuple(inc[i][1-side] for i in flags)
    e1,e2=(second[t] for t in pins)
    miss=missing_endpoint_degrees(second,a)
    t=(a-4)//8
    regular=max(miss[u] for u in set(e1+e2))<=t
    if require_regular and s>=32 and not regular:
        raise ValueError("given genuine root does not satisfy exact physical pin-regularity precondition")
    Q=find_genuine_source_root_C4_sixflags(model,side,p,flags)
    if Q is None:
        if require_regular and s>=32:
            raise AssertionError("all-h source true original C4 with six distinct opposite factors missing")
        return None
    target=find_target_C6_with_two_original_pinned_edges(second,a,e1,e2)
    if target is None:
        if require_regular and s>=32:
            raise AssertionError("all-h physically pinned C6 from right hole-degree certificate missing")
        return None
    Q_opp={inc[i][1-side] for i in Q}
    free_orig=sorted(Q_opp-set(pins))
    wanted=tuple(sorted(set(target)-{e1,e2}))
    if len(free_orig)!=4 or len(wanted)!=4:
        raise AssertionError("true root six source factors / target missing 4 unique extras")
    new=list(second)
    owner={edge:j for j,edge in enumerate(new)}
    swaps=[]
    for src,dest in zip(free_orig,wanted):
        if new[src]==dest:continue
        donor=owner[dest]
        if donor in pins:
            raise AssertionError("source root image pin cannot donate an unpinned physical edge")
        before=new[src]
        new[src],new[donor]=new[donor],new[src]
        owner[dest]=src
        owner[before]=donor
        swaps.append((src,donor))
    if any(new[j]!=original_second[j] for j in pins):
        raise AssertionError("changed physical pair image of fixed actual original source factor")
    if len(swaps)>4 or len(new)!=V or len(set(new))!=V or set(new)!=set(second):
        raise AssertionError("original global physical pair injectivity/support or swap budget violated")
    rebuilt=dict(model)
    rebuilt["right_labels" if side==0 else "left_labels"]=tuple(new)
    # Independent HISTORICAL seven-GF5 classifier on SAME six ORIGINAL
    # source incidence IDs, not physical cycle count alone.
    # Check BOTH physical projections, actual original source factor
    # multiplicities, and the positive historical GF5 source class.
    # The old seven_census classifier is deliberately W32-K6-specific:
    # for real W34 nononto K14 use the existing true-original
    # full-alphabet independent joint-source classifier instead.
    profiles=[]
    for typ,images in ((0,rebuilt["left_labels"]),(1,rebuilt["right_labels"])):
        degrees=Counter(col for j in Q for col in images[inc[j][typ]])
        if len(degrees)!=6 or any(degree!=2 for degree in degrees.values()):
            raise AssertionError("six SAME true original source incidence flags fail actual physical degree-two")
        multiplicities=tuple(sorted(Counter(inc[j][typ] for j in Q).values()))
        profiles.append({
            (1,1,1,1,1,1):"A",
            (1,1,1,1,2):"B",
            (2,2,2):"C"
        }.get(multiplicities))
    want="B-left/A-right" if side==0 else "A-left/B-right"
    tag=independent_joint_classify(
        Q,profiles[0],profiles[1],tuple(inc),
        tuple(rebuilt["left_labels"]),tuple(rebuilt["right_labels"]))
    if s==2:
        historic=classify_seven_prechecked(
            Q,tuple(rebuilt["left_labels"]),tuple(rebuilt["right_labels"]),tuple(inc))
        if historic!=tag:
            raise AssertionError("independent historical W32 and original structural class disagree")
    if tag!=want:
        raise AssertionError(f"true original seven-GF5 classification {tag} != {want}")
    if not all(new[src]==dst for src,dst in zip(free_orig,wanted)):
        raise AssertionError("global right physical 4-edge target wasn't reached")
    return {
        "s":s,"V":V,"a":a,"side":side,"original_source_factor":p,
        "original_source_root_two_incidence_IDs":flags,
        "same_six_REAL_original_incidence_IDs":Q,
        "initial_actual_physical_root_pin_images":(e1,e2),
        "both_initial_original_source_factor_pin_images_unchanged":True,
        "original_global_opposite_map_before":original_second,
        "original_global_opposite_map_after":tuple(new),
        "repaired_full_true_original_model":rebuilt,
        "exact_original_source_line_swap_transpositions":tuple(swaps),
        "number_global_source_FACTOR_swaps":len(swaps),
        "accepted_historical_seven_GF5_tag":tag,
        "physical_root_pin_regular":regular,
        "certified_any_h_ge5_good_root_four_swap_theorem":s>=32 and regular,
        "four_swaps_repair_many_roots_on_ONE_IDENTICAL_unchanged_map_NOT_PROVED":True,
        "original_unmodified_full_f_g_positive_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def original_genuine_root_pin_majority_four_swap_cert(s):
    """Formal ALL-h theorem; no constructed fake large W3 geometry."""
    if type(s) is not int or s<32 or s&(s-1):
        raise ValueError("source GQ h>=5 only")
    z=every_fixed_original_g_good_root_pin_majority(s)
    if z["fraction_true_original_cherries_with_regular_two_pinned_images_lower"]<=3/4:
        raise AssertionError("all-h root majority must be strict")
    return {
        **z,
        "quantifier":"for EVERY fully fixed genuine-original f,g, each good source root has SOME globally injective g_prime of transposition distance <=4",
        "number_original_source_cherries_with_a_repair_witness_lower":
            z["number_true_original_cherries_with_regular_two_pinned_images_lower"],
        "fixes_all_ORIGINAL_source_point_labels_and_occupied_opposite_support":True,
        "fixes_two_REAL_original_LINE_factor_image_pins":True,
        "six_real_original_source_incidence_IDs_immutable":True,
        "positive_GF5_class":"B-left/A-right",
        "allowed_source_LINE_image_transpositions_max":4,
        "one_repaired_map_simultaneously_for_all_roots_NOT_PROVED":True,
        "unmodified_arbitrary_full_original_f_g_positive_NOT_PROVED":True,
        "root_230":"OPEN_WITH_FORMAL_BLOCKER",
    }


def four_external_donors_swap_lower_bound():
    """Exact abstract target-specific four-swap lower; NOT a GF5 optimum.

    Fixed TWO source factor pins, four eligible source line IDs q0..q3
    and four external donors r0..r3. The four target images are all
    initially owned by EXTERNAL sources, so a swap can bring at most
    one desired target to the four original source Q labels. Exactly
    FOUR transpositions are required to realize THAT PARTICULAR
    four-assignment target; perhaps another accepted GF5 target
    is reachable in fewer swaps, which is expressly NOT claimed.
    """
    names=("pin0","pin1","q0","q1","q2","q3","r0","r1","r2","r3")
    initial=tuple(range(10))
    desired={2:6,3:7,4:8,5:9}
    paths=[(2,6),(3,7),(4,8),(5,9)]
    vals=list(initial)
    for x,y in paths: vals[x],vals[y]=vals[y],vals[x]
    assert all(vals[x]==y for x,y in desired.items())
    return {
        "source_original_factor_names":names,
        "pinned_source_IDs":(0,1),
        "targeted_four_source_IDs":(2,3,4,5),
        "target_images_initially_owned_by_external_four_IDs":(6,7,8,9),
        "source_transposition_lower_for_THIS_SPECIFIC_TARGET":4,
        "explicit_repair_path":tuple(paths),
        "claim_all_GF5_BA_targets_need_four_swaps":False,
        "not_a_true_W3_source_fixture":True,
    }
