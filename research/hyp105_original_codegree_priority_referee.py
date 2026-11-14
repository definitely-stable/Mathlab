"""HYP-105 #230 AA4-CODEGSEL: exact two-owner ORIGINAL priority codegree.

SOURCE first: genuine W(3,s), independent original owner flags of each
actual 3-edge coordinate-proper physical path, one globally shared source
priority permutation, two genuinely typed physical symbol cuts.

An independent pair (i,j) of original J conflict graph owner vertices with
degrees d_i,d_j, and common-neighbor count c=|J(i) intersect J(j)| has
exact simultaneous strict priority minimum probability
  [1/(d_j-c+1)]*[1/(d_i+1)-1/(d_i+d_j-c+2)] +
  [1/(d_i-c+1)]*[1/(d_j+1)-1/(d_i+d_j-c+2)].
Neither independence of owners' local-minimum EVENTS nor randomness of
physical pair labelings f,g is assumed.

For three mutually J-independent named ORIGINAL owners S, a stronger
all-order SOURCE selector bound:
  max_{i<j in S} P(A_i and A_j)/(1+d_k) <= P(all three minima)
       <= min_{i<j in S} P(A_i and A_j).
The lower uses positive association of transformed independent priorities;
the upper uses intersection containment. When all three original J
neighborhoods are pairwise disjoint, equality is the singleton product.

Composed with previously independently tested exact three-owner true
physical port paths and nonnegative ORIGINAL middle-source compatible
second moments, this gives tight, source-verified M/G/B envelopes,
without claiming global B/M < 3/4 or root six-motif obstruction.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import json

from hyp105_original_full_w34_weighted_risk_referee import _source
from hyp105_original_three_owner_joint_ports_referee import (
    CASES, _joint_original_three_owner_ports,
    _true_original_joint_middle_moment,
)

SCHEMA="mathlab.hyp105.original-codegree-priority-b75.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
THRESHOLD=Fraction(3,4)


def _exact_original_pair_local_minimum(a,b,J):
    """Exact two-owner shared ORIGINAL uniform-priority probability.

    Integrating over the two independent continuous owner ranks, the
    shared outsider priorities must exceed max(rank_a,rank_b); private
    neighbors exceed their respective owner. Original J is symmetric.
    """
    if a==b or b in J[a] or a in J[b]:
        raise ValueError("requires two distinct J-independent original owners")
    da=len(J[a]);db=len(J[b]);common=len(J[a]&J[b])
    if not 0<=common<=min(da,db):
        raise AssertionError("invalid genuine original source J codegree")
    den=da+db-common+2
    ans=(Fraction(1,db-common+1) *
         (Fraction(1,da+1)-Fraction(1,den)) +
         Fraction(1,da-common+1) *
         (Fraction(1,db+1)-Fraction(1,den)))
    singleton_a=Fraction(1,da+1)
    singleton_b=Fraction(1,db+1)
    if not singleton_a*singleton_b<=ans<=min(singleton_a,singleton_b):
        raise AssertionError("exact original two-owner Harris/product or containment false")
    if common==0 and ans!=singleton_a*singleton_b:
        raise AssertionError("disjoint J neighborhoods must give independent minima")
    return ans


def _original_three_owner_codegree_selector_envelope(owners,J,pair_cache=None):
    """Sharper common-source priority envelope; 1/64 typed cut factor.

    Returns (new lower w, new upper w, all-source-neighborhood-disjoint),
    where w is the exact marginal of one ACTUAL proper physical P3.
    """
    key=tuple(sorted(owners))
    if len(key)!=3 or len(set(key))!=3:
        raise ValueError("requires exactly THREE unique original source flags")
    if any(j in J[i] or i in J[j] for i,j in combinations(key,2)):
        raise ValueError("original three owner flags must be J-independent")
    singleton={i:Fraction(1,1+len(J[i])) for i in key}
    product=singleton[key[0]]*singleton[key[1]]*singleton[key[2]]
    pairs=[]
    common_any=False
    for i,j in combinations(key,2):
        k=next(z for z in key if z!=i and z!=j)
        edge=(i,j)
        if pair_cache is not None and edge in pair_cache:
            p=pair_cache[edge]
        else:
            p=_exact_original_pair_local_minimum(i,j,J)
            if pair_cache is not None:
                pair_cache[edge]=p
        if J[i]&J[j]:
            common_any=True
        pairs.append((p,p*singleton[k]))
    lower=max(v for _,v in pairs)
    upper=min(p for p,_ in pairs)
    if not common_any:
        # Stronger all-h EXACT branch: each owner minimum depends on
        # its own rank and its J neighbors. Pairwise disjoint
        # neighborhoods and pairwise J-independence make these THREE
        # coordinate sets disjoint, hence the minima genuinely independent.
        # A pair-event containment bound alone does NOT give equality.
        if lower!=product:
            raise AssertionError("disjoint genuine original J cannot amplify product")
        upper=product
    if not product<=lower<=upper<=min(singleton.values()):
        raise AssertionError("original codegree selector envelope not nested")
    return lower/64,upper/64,not common_any


def _original_codegree_one_case(s,scheme,core):
    """All TRUE original physical paths, exact codegree-risk certificates.

    Source paths are the inherited independent original middle-port JOIN,
    not a random/fitted factor-graph shadow or sampled P3 paths.
    """
    c=_source(s,scheme,core)
    bins,rank_n=_joint_original_three_owner_ports(c)
    pair_cache={}
    triple_cache={}
    moments=defaultdict(Fraction)
    counts=defaultdict(int)
    max_pointwise=None

    for ends,group in bins.items():
        new_group=[]
        old_hi=Fraction(0)
        new_hi=Fraction(0)
        for path,owners,exact_w,old_lo,old_up in group:
            key=tuple(sorted(owners))
            if key not in triple_cache:
                triple_cache[key]=_original_three_owner_codegree_selector_envelope(
                    key,c["J"],pair_cache)
            new_lo,new_up,is_disjoint=triple_cache[key]
            if not old_lo<=new_lo<=exact_w<=new_up<=old_up:
                raise AssertionError("true common PRIORITY exact weight outside new codegree bounds")
            if is_disjoint and not (old_lo==new_lo==exact_w):
                raise AssertionError("disjoint three ORIGINAL neighborhoods require exact product")
            if new_lo>old_lo:
                counts["paths_with_STRICT_improved_Harris_lower"]+=1
            if new_up<old_up:
                counts["paths_with_STRICT_improved_owner_minimum_upper"]+=1
            if new_lo>old_lo or new_up<old_up:
                counts["paths_with_either_improved_selector_envelope"]+=1
            new_group.append((path,owners,exact_w,old_lo,old_up,new_lo,new_up))
            old_hi+=old_up
            new_hi+=new_up
        # Independently inherited exact ORIGINAL second moment is built
        # from source midflag identity, not pairwise path compatibility.
        exact=_true_original_joint_middle_moment(new_group,c,2)
        old_lower=_true_original_joint_middle_moment(new_group,c,3)
        new_lower=_true_original_joint_middle_moment(new_group,c,5)
        if not 0<old_lower["G"]<=new_lower["G"]<=exact["G"]<=exact["M"]:
            raise AssertionError("nonnegative true compatible original paths not monotone")
        if not new_hi<=old_hi:
            raise AssertionError("codegree bound cannot increase original M upper")
        moments["M_exact"]+=exact["M"]
        moments["G_exact"]+=exact["G"]
        moments["B_exact"]+=exact["B"]
        moments["D_exact"]+=exact["D"]
        moments["G00_exact"]+=exact["G00"]
        moments["G11tail_exact"]+=exact["G11_tail"]
        moments["G11head_exact"]+=exact["G11_head"]
        moments["G_lower_old"]+=old_lower["G"]
        moments["G_lower_new"]+=new_lower["G"]
        moments["M_upper_old"]+=old_hi*old_hi
        moments["M_upper_new"]+=new_hi*new_hi
        moments["M_upper_rankless"]+=Fraction(len(group)**2,4096)
        moments["M_lower_new"]+=new_lower["M"]
        counts["true_physical_endpoint_bins"]+=1
        counts["real_proper_source_threepaths"]+=len(group)
        if exact["B"]>THRESHOLD*exact["M"]:
            counts["actual_strict_local_bad_B75_bins"]+=1
        if 4*new_lower["G"]>new_hi*new_hi:
            counts["codegree_envelope_STRICT_local_safe_B75_bins"]+=1
        elif 4*old_lower["G"]>old_hi*old_hi:
            raise AssertionError("strict previous safe bin became unsafe with stronger bounds")
        if max_pointwise is None or len(group)>max_pointwise["count"]:
            max_pointwise={"ordered_physical_endpoints":[list(ends[0]),list(ends[1])],
                           "count":len(group),
                           "exact_original_B_over_M":str(exact["B"]/exact["M"]),
                           "old_M_upper":str(old_hi*old_hi),
                           "new_M_upper":str(new_hi*new_hi)}

    M=moments["M_exact"];G=moments["G_exact"];B=moments["B_exact"]
    old_u=moments["M_upper_old"];new_u=moments["M_upper_new"]
    old_l=moments["G_lower_old"];new_l=moments["G_lower_new"]
    if not (0<M and 0<G<=M and G+B==M):
        raise AssertionError("true original M/G/B energy conservation failed")
    if not (0<old_l<=new_l<=G and
            0<moments["M_lower_new"]<=M<=new_u<=old_u<=moments["M_upper_rankless"]):
        raise AssertionError("pair-codegree original global selector inequality false")
    old_cert=1-old_l/old_u
    new_cert=1-new_l/new_u
    if not B/M<=new_cert<=old_cert<1:
        raise AssertionError("three-owner codegree B75 certificate incorrectly promoted")
    disjoint=sum(1 for x in triple_cache.values() if x[2])
    return {
        "s":s,"scheme":scheme,"retained_original_CORE":core,
        "original_genuine_source_flag_count":len(c["flags"]),
        "original_retained_source_flag_count":len(c["ids"]),
        "original_rank_exact_three_owner_sets":rank_n,
        "original_pair_source_J_codegree_probability_sets":len(pair_cache),
        "original_three_owner_DISJOINT_J_neighborhood_sets":disjoint,
        "exact_original_M":str(M),"exact_original_G":str(G),"exact_original_B":str(B),
        "exact_original_B_over_M":str(B/M),
        "original_Harris_lower_G_old":str(old_l),
        "original_CODEGREE_lower_G_new":str(new_l),
        "original_singleton_degree_M_upper_old":str(old_u),
        "original_CODEGREE_M_upper_new":str(new_u),
        "original_rankless_M_upper":str(moments["M_upper_rankless"]),
        "original_CODEGREE_M_lower_new":str(moments["M_lower_new"]),
        "old_common_original_B_over_M_upper":str(old_cert),
        "new_CODEGREE_common_original_B_over_M_upper":str(new_cert),
        "M_upper_STRICT_improvement_over_parent":new_u<old_u,
        "G_lower_STRICT_improvement_over_parent":new_l>old_l,
        "codegree_certified_strict_global_B75":4*new_l>new_u,
        "exact_local_source_population_not_sampled":True,
        "all_h_NEW_codegree_priority_bounds_are_pointwise_valid":True,
        "counts":dict(sorted(counts.items())),
        "max_true_physical_endpoint_path_bin":max_pointwise,
        "root_PROVED_A":False,
    }


def canonical_report():
    rows=[_original_codegree_one_case(*case) for case in CASES]
    required=[1346,1154,838,83892,82846,79404,9966,66418]
    if [x["counts"]["real_proper_source_threepaths"] for x in rows]!=required:
        raise AssertionError("full genuine original W32/W34 P3 census drift")
    return {
        "schema":SCHEMA,"issue":230,"status":ROOT_STATUS,
        "all_h_ORIGINAL_two_owner_shared_J_codegree_exact_rank":True,
        "all_h_ORIGINAL_three_owner_positive_association_pair_lower":True,
        "all_h_ORIGINAL_three_owner_pair_event_containment_upper":True,
        "all_h_ROOT_seven_motif_obstruction_proved":False,
        "all_h_strict_global_B75_all_fixed_correlated_maps_proved":False,
        "ASET_exponent_claimed":False,
        "eight_complete_genuine_original_source_cases":rows,
    }


if __name__=="__main__":
    print("AA4_CODEGSEL_CERTIFICATE="+json.dumps(
        canonical_report(),sort_keys=True,separators=(",",":")))
