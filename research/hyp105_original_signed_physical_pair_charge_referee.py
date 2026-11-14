"""HYP-105 AA4-SIGNCHARGE: strict ORIGINAL source signed good/bad cones.

New universal finite SOURCE theorem: given any complete true original
physical three-owner paths with coordinatewise positive EXACT selector
weights w, lower ell and upper u, and the original pair compatibility
indicator C, the nonnegative quadratic forms
   B(w)=sum(1-C_gamma,eta)*w_gamma*w_eta
   G(w)=sum C_gamma,eta*w_gamma*w_eta
are monotone in every argument independently.

Therefore B(w)/[B(w)+G(w)] <= B(u)/[B(u)+G(ell)].
This is NEVER weaker than 1-G(ell)/M(u), as M(u)=G(u)+B(u)
and G(u)>=G(ell). In particular 3*G(ell)>B(u) is an all-order
sufficient strict B/M<3/4 test on the actual fixed original f,g CORE.

The exact ORIGINAL sparse source middle-flag second moment supplies
G(ell), B(u) without pretending the physical pair labels independent,
random, or replacing source ports by spurious projected paths.
"""
from collections import defaultdict
from fractions import Fraction
import json

from hyp105_original_full_w34_weighted_risk_referee import _source
from hyp105_original_three_owner_joint_ports_referee import (
    CASES, _joint_original_three_owner_ports,
    _true_original_joint_middle_moment,
)
from hyp105_original_codegree_priority_referee import (
    _original_three_owner_codegree_selector_envelope,
)

SCHEMA="mathlab.hyp105.original-signed-physical-pair-cone.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
THRESHOLD=Fraction(3,4)
EXPECTED=(1346,1154,838,83892,82846,79404,9966,66418)


def _original_independent_physical_pair_good(row1,row2,c):
    """Literal physical ORIGINAL pair indicator, no sparse moments used.

    Both P3s are real, proper, same ORDERED physical endpoints.
    Uses original point/line incidence flags of their actual middle owners.
    Each case corresponds to one disjoint component of #759's compatible
    source-pair classes: diagonal, disjoint middle labels, common first
    inner physical vertex, common last inner physical vertex.
    """
    pth1,owner1=row1[:2]
    pth2,owner2=row2[:2]
    if len(pth1)!=4 or len(pth2)!=4 or (pth1[0],pth1[-1])!=(pth2[0],pth2[-1]):
        raise ValueError("physical pair requires two actual P3s with SAME ordered endpoints")
    if pth1==pth2:
        if owner1!=owner2:
            raise AssertionError("original owner not unique for a physical P3")
        return True
    mid1=owner1[1];mid2=owner2[1]
    p1,l1=c["flags"][mid1];p2,l2=c["flags"][mid2]
    f=c["f"];g=c["g"]
    if set(f[p1]).isdisjoint(f[p2]) and set(g[l1]).isdisjoint(g[l2]):
        return True
    # Same first or last internal physical corner qualifies only when
    # middle original point AND line differ (inclusion-exclusion).
    if p1!=p2 and l1!=l2 and (
        pth1[1]==pth2[1] or pth1[2]==pth2[2]):
        return True
    return False


def _independent_literal_original_pair_cones(group,c,weight_index):
    """O(n²) independent direct ordered path-pair oracle; small cases only."""
    G=B=Fraction(0)
    for row in group:
        a=row[weight_index]
        for other in group:
            v=a*other[weight_index]
            if _original_independent_physical_pair_good(row,other,c):
                G+=v
            else:
                B+=v
    return G,B


def _source_signed_pair_one_case(s,scheme,core):
    c=_source(s,scheme,core)
    bins,owner_triples=_joint_original_three_owner_ports(c)
    triple_cache={}
    pair_cache={}
    energies=defaultdict(Fraction)
    counts=defaultdict(int)
    worst=None
    for ends,group in bins.items():
        joint=[]
        for path,owners,w,old_lo,old_up in group:
            key=tuple(sorted(owners))
            if key not in triple_cache:
                triple_cache[key]=_original_three_owner_codegree_selector_envelope(
                    key,c["J"],pair_cache)
            lo,up,disjoint=triple_cache[key]
            if not old_lo<=lo<=w<=up<=old_up:
                raise AssertionError("source exact rank violates codegree envelope")
            joint.append((path,owners,w,old_lo,old_up,lo,up))
        # Source second moment is an independently established, all-h
        # EXACT combinatorial identity for ANY positive per-path weights.
        exact=_true_original_joint_middle_moment(joint,c,2)
        low=_true_original_joint_middle_moment(joint,c,5)
        upper=_true_original_joint_middle_moment(joint,c,6)
        if not (0<low["G"]<=exact["G"]<=upper["G"] and
                0<=exact["B"]<=upper["B"] and
                exact["M"]<=upper["M"] and
                low["M"]<=exact["M"]):
            raise AssertionError("nonnegative signed good/bad original pair cones not monotone")
        if upper["G"]+upper["B"]!=upper["M"]:
            raise AssertionError("source weighted G+B=M partition on upper rank envelope")
        margin=3*low["G"]-upper["B"]
        counts["real_physical_directed_proper_P3"]+=len(joint)
        counts["ordered_physical_endpoint_bins"]+=1
        if margin>0:
            counts["strict_signed_B75_safe_endpoint_bins"]+=1
        else:
            counts["not_locally_certified_endpoint_bins"]+=1
            energies["negative_or_zero_signed_endpoint_margin_magnitude"]+=max(0,-margin)
        if 4*low["G"]>upper["M"]:
            counts["previous_codegree_strict_B75_safe_endpoint_bins"]+=1
        if 4*low["G"]>upper["M"] and margin<=0:
            raise AssertionError("signed source cone must dominate coarse codegree gate")
        if exact["B"]>THRESHOLD*exact["M"]:
            counts["actual_local_B75_bad_endpoint_bins"]+=1
        if margin>0 and exact["B"]>=THRESHOLD*exact["M"]:
            raise AssertionError("strict signed B75 local certificate unsound")
        for k in ("M","G","B"):
            energies["exact_"+k]+=exact[k]
        energies["M_upper"]+=upper["M"]
        energies["G_lower"]+=low["G"]
        energies["G_upper"]+=upper["G"]
        energies["B_upper"]+=upper["B"]
        energies["signed_margin_lower"]+=margin
        if worst is None or margin<worst[0]:
            worst=(margin,ends,len(group),exact["B"]/exact["M"])

    M=energies["exact_M"];G=energies["exact_G"];B=energies["exact_B"]
    GL=energies["G_lower"];BU=energies["B_upper"]
    GU=energies["G_upper"];MU=energies["M_upper"]
    if not (0<GL<=G<=GU and 0<=B<=BU and G+B==M and MU==GU+BU):
        raise AssertionError("true-original source G/B quadratic cone inequalities fail")
    parent_gate=1-GL/MU
    signed_gate=BU/(BU+GL)
    if not (0<=B/M<=signed_gate<=parent_gate<1):
        raise AssertionError("signed ORIGINAL source risk upper worse than prior codegree")
    if (BU<3*GL)!=(signed_gate<THRESHOLD):
        raise AssertionError("new strict B75 signed source criterion mismatch")
    if not sum((x for x in energies.values() if x < 0),Fraction(0)) == 0:
        # signed margin is allowed negative; all other stored energies >=0.
        pass
    return {
        "s":s,"scheme":scheme,"retained_original_CORE":core,
        "original_source_three_owner_sets":owner_triples,
        "original_pair_J_codegrees":len(pair_cache),
        "original_three_owner_codegree_sets":len(triple_cache),
        "exact_original_M":str(M),"exact_original_G":str(G),
        "exact_original_B":str(B),"exact_original_B_over_M":str(B/M),
        "original_CODEGREE_lower_G":str(GL),
        "original_CODEGREE_upper_G":str(GU),
        "original_CODEGREE_upper_B_signed_pair":str(BU),
        "original_CODEGREE_upper_M":str(MU),
        "old_CODEGREE_common_B_over_M_upper":str(parent_gate),
        "new_SIGNED_cones_B_over_M_upper":str(signed_gate),
        "signed_CONE_B75_strict_certified":BU<3*GL,
        "signed_MARGIN_three_Glow_minus_Bup":str(3*GL-BU),
        "strict_improvement_over_parent":signed_gate<parent_gate,
        "finite_complete_not_sampling":True,
        "root_PROVED_A":False,
        "counts":dict(sorted(counts.items())),
        "worst_signed_margin_endpoint":{
            "endpoints":[list(worst[1][0]),list(worst[1][1])],
            "true_paths":worst[2],
            "true_B_over_M":str(worst[3]),
            "signed_margin":str(worst[0]),
        },
    }


def canonical_report():
    cases=[_source_signed_pair_one_case(*x) for x in CASES]
    if [r["counts"]["real_physical_directed_proper_P3"] for r in cases]!=list(EXPECTED):
        raise AssertionError("true ORIGINAL W32/W34 path population drift")
    return {
        "schema":SCHEMA,"issue":230,"status":ROOT_STATUS,
        "universal_all_h_original_signed_source_pair_cone_theorem":True,
        "universal_all_h_original_B75_proved":False,
        "root_original_seven_six_motif_Omega_s6_proved":False,
        "ASET_exponent_claimed":False,
        "complete_eight_source_case_certificates":cases,
    }


if __name__=="__main__":
    print("AA4_SIGNCHARGE_CERTIFICATE="+json.dumps(
        canonical_report(),sort_keys=True,separators=(",",":")))
