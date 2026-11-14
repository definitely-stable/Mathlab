"""HYP-105 AA4-PATHCHARGE: TRUE ORIGINAL pathwise physical-corner charges.

An all-h genuine W(3,s) ORIGINAL source middle-incidence identity:
For any actual coordinate-proper 3-edge directed physical P3 gamma
sharing ordered physical endpoints (u,v) with its source bin, let i
be its genuine ORIGINAL middle incidence flag (p,l), a and b its
first/last internal physical corners. For arbitrary positive path
weights z, define original weighted middle-overlap neighborhood N_i,
and corner-compatible T_gamma, H_gamma by genuine first/last physical
path ports and ORIGINAL point/line/invariance exclusions. Exactly

 g_gamma(z)=z_gamma + W(z) - N_i(z) + T_gamma(z)+H_gamma(z),
 b_gamma(z)=N_i(z)-z_gamma-T_gamma(z)-H_gamma(z).

The TWO nonnegative sums are the weights of the genuinely compatible
and conflicting paths in that endpoint bin, respectively. Their
weighted sums equal #759/#760 exact ORIGINAL G and B quadratic forms.

Consequently an all-h strict BAD B/M>3/4 forces one TRUE ordered
physical endpoint bin and one ACTUAL three-original-owner P3 such that
N_i > 3W/4 + z_gamma + T_gamma + H_gamma.
This joint 3-owner physical-port/heavy-middle-neighborhood witness
is stronger than treating every middle x/y overlap as a BAD pair.

For intervals ell<=w<=u from #765, rowwise local signed deficits
L_gamma=3*g_gamma(ell)-b_gamma(u) satisfy
 3G(w)-B(w)>= sum_gamma min(ell_gamma*L_gamma,u_gamma*L_gamma).
No random f/g, no independence between path selections, and no
unproved global all-label six-motif theorem are used.
"""
from collections import defaultdict
from fractions import Fraction
import json

from hyp105_original_full_w34_weighted_risk_referee import _source
from hyp105_original_three_owner_joint_ports_referee import (
    CASES,_joint_original_three_owner_ports,_true_original_joint_middle_moment,
)
from hyp105_original_codegree_priority_referee import (
    _original_three_owner_codegree_selector_envelope,
)

SCHEMA="mathlab.hyp105.original-pathwise-corner-physical-charge.v1"
STATUS="OPEN_WITH_FORMAL_BLOCKER"
EXPECTED=(1346,1154,838,83892,82846,79404,9966,66418)
B75=Fraction(3,4)


def _physical_original_pathwise_charges(rows,c,weight_index):
    """All actual ORIGINAL paths, O(n+q²) sparse source path-corner charge.

    Exact Fraction, n number of genuine proper physical 3paths per
    ordered physical endpoint bin, q occupied original middle flag IDs.
    No path-pair iterator; output path-aligned (g_gamma,b_gamma,N_i,
    tail_corner,head_corner). Every original source weight z>0.
    """
    if not rows:
        raise ValueError("nonempty ORIGINAL ordered physical endpoint bin required")
    flags,f,g=c["flags"],c["f"],c["g"]
    ends=(rows[0][0][0],rows[0][0][-1])
    bymid=defaultdict(Fraction)
    first=defaultdict(Fraction);last=defaultdict(Fraction)
    fp=defaultdict(Fraction);fl=defaultdict(Fraction);fi=defaultdict(Fraction)
    lp=defaultdict(Fraction);ll=defaultdict(Fraction);li=defaultdict(Fraction)
    W=Fraction(0)
    source_rows=[]
    for row in rows:
        path,owners=row[:2];z=row[weight_index]
        if z<=0 or not isinstance(z,Fraction):
            raise AssertionError("genuine positive ORIGINAL rational source path weight required")
        if len(path)!=4 or len(owners)!=3 or (path[0],path[-1])!=ends:
            raise AssertionError("not one ordered physical endpoint bin")
        if len({p[0] for p in path})!=4 or len({p[1] for p in path})!=4:
            raise AssertionError("not a genuine coordinate-proper physical P3")
        i=owners[1];p,l=flags[i];a,b=path[1],path[2]
        if tuple(sorted((a[0],b[0])))!=f[p] or tuple(sorted((a[1],b[1])))!=g[l]:
            raise AssertionError("original physical middle port not owned by named flag")
        W+=z;bymid[i]+=z
        first[a]+=z;last[b]+=z
        fp[(p,a)]+=z;fl[(l,a)]+=z;fi[(i,a)]+=z
        lp[(p,b)]+=z;ll[(l,b)]+=z;li[(i,b)]+=z
        source_rows.append((path,owners,z,i,p,l,a,b))

    posted_x=defaultdict(set);posted_y=defaultdict(set)
    for i in bymid:
        p,l=flags[i]
        for x in f[p]:
            posted_x[x].add(i)
        for y in g[l]:
            posted_y[y].add(i)
    occupied={}
    for i in bymid:
        p,l=flags[i]
        neighbors=set().union(*(posted_x[x] for x in f[p]))
        neighbors.update(*(posted_y[y] for y in g[l]))
        if i not in neighbors:
            raise AssertionError("original physical middle owner missing its own conflict neighborhood")
        occupied[i]=sum((bymid[j] for j in neighbors),Fraction(0))

    result=[]
    G=B=Fraction(0)
    sum_N_correction=Fraction(0)
    heavy=None
    for path,owners,z,i,p,l,a,b in source_rows:
        N=occupied[i]
        tail=(first[a]-fp[(p,a)]-fl[(l,a)]+fi[(i,a)])
        head=(last[b]-lp[(p,b)]-ll[(l,b)]+li[(i,b)])
        if tail<0 or head<0:
            raise AssertionError("nonnegative ORIGINAL source corner compatible correction")
        good=z+(W-N)+tail+head
        bad=N-z-tail-head
        if not (z<=good<=W and 0<=bad<=W-z and good+bad==W):
            raise AssertionError("pathwise ORIGINAL good/bad cone inclusion-exclusion broken")
        G+=z*good;B+=z*bad
        sum_N_correction+=z*(N-z-tail-head)
        if heavy is None or bad*heavy[1]>heavy[0]*W:
            # Compare exact ratios across SAME W in this endpoint bin.
            heavy=(bad,W,path,owners,i,tail,head,z,N)
        result.append((good,bad,N,tail,head))
    if not 0<=B<=W*W or not G+B==W*W or B!=sum_N_correction:
        raise AssertionError("source pathwise ORIGINAL G/B conservation false")
    return {"W":W,"M":W*W,"G":G,"B":B,"rows":result,
            "source_middle_occupied":len(bymid),
            "actual_ordered_physical_endpoint_pair":ends,
            "heaviest_bad_fraction_witness":heavy}


def _pathwise_one_complete_source(s,scheme,core):
    c=_source(s,scheme,core)
    bins,source_triplets=_joint_original_three_owner_ports(c)
    triple_cache={}
    pair_cache={}
    sums=defaultdict(Fraction)
    counts=defaultdict(int)
    worst=None
    for ends,group in bins.items():
        enriched=[]
        for path,owners,exact,oldlo,oldup in group:
            key=tuple(sorted(owners))
            if key not in triple_cache:
                triple_cache[key]=_original_three_owner_codegree_selector_envelope(
                    key,c["J"],pair_cache)
            lo,up,disjoint=triple_cache[key]
            if not oldlo<=lo<=exact<=up<=oldup:
                raise AssertionError("original fixed source J codegree bound false")
            enriched.append((path,owners,exact,oldlo,oldup,lo,up))
        true=_physical_original_pathwise_charges(enriched,c,2)
        lower=_physical_original_pathwise_charges(enriched,c,5)
        upper=_physical_original_pathwise_charges(enriched,c,6)
        # Prior independent exact source second-moment implementation
        # must agree for all three independent weight assignments.
        for idx,charge in ((2,true),(5,lower),(6,upper)):
            old=_true_original_joint_middle_moment(enriched,c,idx)
            for k in ("M","G","B"):
                if charge[k]!=old[k]:
                    raise AssertionError("genuine pathwise all-h port corner charge differs from original source moment")
        signed_lower=Fraction(0)
        all_local_signs_positive=True
        for ix,row in enumerate(enriched):
            lo=row[5];up=row[6]
            ge,be,Ne,te,he=true["rows"][ix]
            gl,bl,Nl,tl,hl=lower["rows"][ix]
            gu,bu,Nu,tu,hu=upper["rows"][ix]
            if not (0<gl<=ge<=gu and 0<=bl<=be<=bu):
                raise AssertionError("true original pathwise compatible/bad cone not monotone")
            if not (0<=tl<=te<=tu and 0<=hl<=he<=hu and
                    0<Nl<=Ne<=Nu):
                raise AssertionError("source-original heavy neighborhood or positive corner weights not monotone")
            L=3*gl-bu
            signed_lower+=(lo if L>=0 else up)*L
            if L<=0:
                all_local_signs_positive=False
                counts["paths_with_nonpositive_codegree_local_signed_deficit"]+=1
            if be*4>3*true["W"]:
                counts["paths_with_exact_bad_neighbor_fraction_above_75pct"]+=1
            if be*4>3*true["W"] and not Ne>3*true["W"]/4+row[2]+te+he:
                raise AssertionError("missing genuine ORIGINAL first/middle/last heavy-path obstruction")
            counts["true_original_physical_proper_P3"]+=1
        if 3*true["G"]-true["B"]<signed_lower:
            raise AssertionError("new pathwise signed interval margin invalid on actual source")
        if 3*lower["G"]-upper["B"]>3*true["G"]-true["B"]:
            raise AssertionError("parent signed bound not valid on actual source")
        if all_local_signs_positive and signed_lower<=0:
            raise AssertionError("all strictly good actual path rows but no positive bound")
        if signed_lower>0:
            counts["strict_pathwise_row_B75_certified_endpoint_bins"]+=1
        if 3*lower["G"]-upper["B"]>0:
            counts["prior_pair_cone_B75_certified_endpoint_bins"]+=1
        if true["B"]*4>=3*true["M"]:
            counts["true_local_B75_fail_or_equality_endpoint_bins"]+=1
            if not any(4*charge[1]>=3*true["W"] for charge in true["rows"]):
                raise AssertionError("weak endpoint B75 BAD has no LOCAL pathwise real witness")
            if true["B"]*4>3*true["M"] and not any(
                4*charge[1]>3*true["W"] for charge in true["rows"]
            ):
                raise AssertionError("strict endpoint B75 BAD has no LOCAL strict pathwise witness")
        for k in ("M","G","B"):
            sums["exact_"+k]+=true[k]
        sums["parent_G_lower"]+=lower["G"]
        sums["parent_B_upper"]+=upper["B"]
        sums["parent_M_upper"]+=upper["M"]
        sums["new_row_signed_margin_lower"]+=signed_lower
        counts["ordered_true_original_physical_endpoint_bins"]+=1
        if worst is None or signed_lower<worst[0]:
            worst=(signed_lower,ends,len(enriched),true["B"]/true["M"],all_local_signs_positive)
    M=sums["exact_M"];G=sums["exact_G"];B=sums["exact_B"]
    GL=sums["parent_G_lower"];BU=sums["parent_B_upper"]
    MU=sums["parent_M_upper"]
    Lrow=sums["new_row_signed_margin_lower"]
    parent=BU/(BU+GL)
    if not (0<GL<=G and 0<=B<=BU and M==G+B<=MU):
        raise AssertionError("global ORIGINAL exact and interval cone quantities fail")
    if not (Lrow<=3*G-B and 3*GL-BU<=3*G-B):
        raise AssertionError("global pathwise signed source margin not lower")
    if Lrow>=0:
        row_risk=B75-Lrow/(4*MU)
    else:
        # M_lower=G(ell)+B(ell) is obtained below only if needed;
        # do not use wrong-sign M_upper for a negative margin.
        row_risk=Fraction(1)
    final=min(parent,row_risk)
    if not (B/M<=final<=parent and final<1):
        raise AssertionError("pathwise alternate source B75 bound false or deteriorated")
    for key in (
        "paths_with_nonpositive_codegree_local_signed_deficit",
        "paths_with_exact_bad_neighbor_fraction_above_75pct",
        "strict_pathwise_row_B75_certified_endpoint_bins",
        "prior_pair_cone_B75_certified_endpoint_bins",
        "true_local_B75_fail_or_equality_endpoint_bins",
    ):
        counts[key]+=0
    return {
        "s":s,"scheme":scheme,"retained_original_CORE":core,
        "original_SOURCE_priority_triples":source_triplets,
        "exact_original_M":str(M),"exact_original_G":str(G),"exact_original_B":str(B),
        "exact_original_B_over_M":str(B/M),
        "parent_SIGNCHARGE_G_lower":str(GL),
        "parent_SIGNCHARGE_B_upper":str(BU),
        "parent_SIGNCHARGE_B_over_M_bound":str(parent),
        "new_original_pathwise_signed_deficit_global_lower":str(Lrow),
        "new_pathwise_signed_risk_upper_if_positive_else_one":str(row_risk),
        "best_certified_risk_upper_parent_or_pathwise":str(final),
        "new_pathwise_signed_strict_B75_criterion":Lrow>0,
        "true_original_source_all_h_witness_theorem_conditional":True,
        "finite_complete_not_sampling":True,
        "root_PROVED_A":False,
        "counts":dict(sorted(counts.items())),
        "lowest_local_signed_pathwise_margin":{
            "endpoints":[list(worst[1][0]),list(worst[1][1])],
            "real_paths":worst[2],
            "true_B_over_M":str(worst[3]),
            "all_pathwise_codegree_local_deficits_positive":worst[4],
            "signed_margin":str(worst[0]),
        },
    }


def canonical_report():
    z=[_pathwise_one_complete_source(*case) for case in CASES]
    if [row["counts"]["true_original_physical_proper_P3"] for row in z]!=list(EXPECTED):
        raise AssertionError("original true physical P3 path population drift")
    return {
        "schema":SCHEMA,"issue":230,"status":STATUS,
        "universal_all_h_original_pathwise_correction_identity_proved":True,
        "universal_all_h_strict_B75_requires_one_real_heavy_path_proved":True,
        "universal_all_h_B75_for_all_fixed_correlated_f_g_proved":False,
        "root_original_all_label_seven_motif_Omega_s6_proved":False,
        "ASET_exponent_claimed":False,
        "complete_genuine_original_source_cases":z,
    }


if __name__=="__main__":
    print("AA4_PATHCHARGE_CERTIFICATE="+json.dumps(
        canonical_report(),sort_keys=True,separators=(",",":")))
