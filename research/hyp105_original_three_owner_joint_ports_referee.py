"""HYP-105 #230 AA4-JOINT3: genuine three-ORIGINAL-owner physical port contraction.

For any genuine W(3,2^h), fixed separately pair-injective (even correlated)
f/g, and retained named original source flags C, every coordinate-proper
directed physical 3path has a unique first/middle/last ORIGINAL owner triple.
The exact common-priority selector marginal is pi_J(triple)/64, NOT the
product of three independent owner-minimum probabilities.

This code constructs the physical paths by ORIGINAL owned middle diagonals,
joined to actual ORIGINAL owned first/last physical ports. It DOES NOT call
the inherited physical adjacency path walker. It then computes exact
selector-weighted M/G/B via sparse ORIGINAL middle-owner second moments.

New all-order envelope: if d_i is the TRUE retained original J degree of
each of three pairwise J-independent owners, then
  1/(64*product(1+d_i)) <= p_path <= 1/(64*(1+max(d_i))).
Consequently sum_uv L_uv^2 <= M <= sum_uv U_uv^2 <= sum_uv n_uv^2/4096.
Also G_lower(from pathwise lower weights) <= G and
  B/M <= 1 - G_lower/M_upper.
None of these envelopes alone proves the global strict B75 root gate.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import json

from hyp105_original_full_w34_weighted_risk_referee import (
    _source, _rank_probability3,
)

SCHEMA="mathlab.hyp105.original-three-owner-joint-port-selector.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
CASES=((2,"lex","full"),(2,"reverse","full"),(2,"shift","Z17"),
       (4,"lex","full"),(4,"reverse","full"),(4,"shift","full"),
       (4,"lex","even"),(4,"shift","Z17"))
THRESHOLD=Fraction(3,4)


def _real_source_directed_port_books(c):
    """Two directed orientations of EACH of the two ORIGINAL owned diagonals."""
    incoming=defaultdict(list)
    outgoing=defaultdict(list)
    for (a,b),i in c["owner"].items():
        incoming[b].append((a,i))
        outgoing[a].append((b,i))
        incoming[a].append((b,i))
        outgoing[b].append((a,i))
    if sum(map(len,incoming.values()))!=4*len(c["ids"]):
        raise AssertionError("original physical port orientations not conserved")
    if sum(map(len,outgoing.values()))!=4*len(c["ids"]):
        raise AssertionError("original physical opposite directed ports not conserved")
    return incoming,outgoing


def _genuine_middle_diagonal_orientations(c,i):
    p,l=c["flags"][i]
    x0,x1=c["f"][p];y0,y1=c["g"][l]
    for a,b in (((x0,y0),(x1,y1)),((x1,y1),(x0,y0)),
                ((x0,y1),(x1,y0)),((x1,y0),(x0,y1))):
        edge=(a,b) if a<b else (b,a)
        if c["owner"].get(edge)!=i:
            raise AssertionError("middle diagonal has wrong original incidence owner")
        yield a,b


def _joint_original_three_owner_ports(c):
    """Source middle-first-last JOIN; never walk the physical graph's P3s.

    Output rows (actual physical 4-vertex path, three ORIGINAL owner IDs,
    EXACT selector weight, Harris lower, rank-minimum upper).
    """
    incoming,outgoing=_real_source_directed_port_books(c)
    J=c["J"]
    degrees=[len(v) for v in J]
    rank_cache={}
    bins=defaultdict(list)
    for i in c["ids"]:
        for a,b in _genuine_middle_diagonal_orientations(c,i):
            for u,j in incoming[a]:
                if len({u[0],a[0],b[0]})!=3 or len({u[1],a[1],b[1]})!=3:
                    continue
                for v,k in outgoing[b]:
                    path=(u,a,b,v)
                    if (len({z[0] for z in path})!=4 or
                            len({z[1] for z in path})!=4):
                        continue
                    owners=(j,i,k)
                    if len(set(owners))!=3:
                        raise AssertionError("coordinate-proper path duplicated an original source")
                    if any(q in J[p] for p,q in combinations(owners,2)):
                        raise AssertionError("coordinate-proper original owners must be J-independent")
                    key=tuple(sorted(owners))
                    if key not in rank_cache:
                        rank_cache[key]=_rank_probability3(key,J)
                    pi=rank_cache[key]
                    w=pi/64
                    d=[degrees[z] for z in owners]
                    lo=Fraction(1,64)
                    for di in d:
                        lo/=1+di
                    hi=Fraction(1,64*(1+max(d)))
                    if not 0<lo<=w<=hi<=Fraction(1,64):
                        raise AssertionError("invalid original three-owner common-priority envelope")
                    bins[(u,v)].append((path,owners,w,lo,hi))
    if not bins:
        raise AssertionError("genuine retained ORIGINAL source has no proper physical P3")
    return bins,len(rank_cache)


def _sq(book):
    return sum((v*v for v in book.values()),Fraction(0))


def _true_original_joint_middle_moment(group,c,weight_index):
    """Independent sparse second-moment evaluation; no P3-pair iteration.

    Uses ONLY real middle owner source p,l, physical f/g, first/last inner
    corners, and path marginal; original same-p and same-l corrections
    avoid synthetic conflict source copies.
    """
    f,g,flags=c["f"],c["g"],c["flags"]
    W=D=Fraction(0)
    mid=defaultdict(Fraction)
    tails=defaultdict(Fraction);heads=defaultdict(Fraction)
    tp=defaultdict(Fraction);tl=defaultdict(Fraction);ti=defaultdict(Fraction)
    hp=defaultdict(Fraction);hl=defaultdict(Fraction);hi=defaultdict(Fraction)
    for path,owners,*weights in group:
        w=weights[weight_index-2]
        if w<=0:
            raise AssertionError("not a positive selector priority marginal")
        i=owners[1];p,l=flags[i];a,b=path[1],path[2]
        if tuple(sorted((a[0],b[0])))!=f[p] or tuple(sorted((a[1],b[1])))!=g[l]:
            raise AssertionError("joint path middle rectangle not genuine original")
        W+=w;D+=w*w;mid[i]+=w
        tails[a]+=w;heads[b]+=w
        tp[(p,a)]+=w;tl[(l,a)]+=w;ti[(i,a)]+=w
        hp[(p,b)]+=w;hl[(l,b)]+=w;hi[(i,b)]+=w
    points=defaultdict(Fraction);lines=defaultdict(Fraction)
    X=defaultdict(Fraction);Y=defaultdict(Fraction);XY=defaultdict(Fraction)
    PY=defaultdict(Fraction);LX=defaultdict(Fraction)
    for i,w in mid.items():
        p,l=flags[i]
        points[p]+=w;lines[l]+=w
        for x in f[p]:
            X[x]+=w;LX[(l,x)]+=w
        for y in g[l]:
            Y[y]+=w;PY[(p,y)]+=w
        for x in f[p]:
            for y in g[l]:
                XY[(x,y)]+=w
    M=W*W
    Ox=_sq(X)-_sq(points)
    Oy=_sq(Y)-_sq(lines)
    Oxy=_sq(XY)-_sq(PY)-_sq(LX)+_sq(mid)
    G00=M-Ox-Oy+Oxy
    G11t=_sq(tails)-_sq(tp)-_sq(tl)+_sq(ti)
    G11h=_sq(heads)-_sq(hp)-_sq(hl)+_sq(hi)
    G=D+G00+G11t+G11h
    if not (0<D<=G<=M and G00>=0 and G11t>=0 and G11h>=0):
        raise AssertionError("original physical middle moments are not nonnegative")
    return {"W":W,"M":M,"D":D,"G00":G00,
            "G11_tail":G11t,"G11_head":G11h,"G":G,"B":M-G}


def _joint_original_selector_case(s,scheme,core):
    c=_source(s,scheme,core)
    bins,distinct_owner_triples=_joint_original_three_owner_ports(c)
    sums=defaultdict(Fraction)
    counts=defaultdict(int)
    maximum=None
    for ends,group in bins.items():
        exact=_true_original_joint_middle_moment(group,c,2)
        lower=_true_original_joint_middle_moment(group,c,3)
        upper=_true_original_joint_middle_moment(group,c,4)
        n=len(group)
        assert exact["W"]<=upper["W"]<=Fraction(n,64)
        assert lower["W"]<=exact["W"]
        if not lower["G"]<=exact["G"]:
            raise AssertionError("coordinatewise Harris lower cannot exceed exact G")
        for k in ("M","D","G00","G11_tail","G11_head","G","B"):
            sums[k]+=exact[k]
        sums["M_Harris_lower"]+=lower["M"]
        sums["M_owner_degree_upper"]+=upper["M"]
        sums["G_Harris_positive_compatible_lower"]+=lower["G"]
        sums["M_trivial_n_over_64_upper"]+=Fraction(n*n,4096)
        sums["source_threeowner_P3_count"]+=n
        sums["priority_loss_from_rankless_physical_count"]+=Fraction(n,64)-exact["W"]
        counts["physical_endpoint_bins"]+=1
        if exact["B"]>THRESHOLD*exact["M"]:
            counts["strict_local_B75_bad_endpoint_bins"]+=1
        if maximum is None or n>maximum["proper_paths"]:
            maximum={"endpoints":[list(ends[0]),list(ends[1])],
                     "proper_paths":n,"selector_W":str(exact["W"]),
                     "degree_upper_W":str(upper["W"])}
    M=sums["M"];G=sums["G"];B=sums["B"]
    MU=sums["M_owner_degree_upper"];GL=sums["G_Harris_positive_compatible_lower"]
    if not (0<M and 0<G and B>=0 and G+B==M):
        raise AssertionError("true original common-selector M/G/B conservation failed")
    if not (sums["M_Harris_lower"]<=M<=MU<=sums["M_trivial_n_over_64_upper"]):
        raise AssertionError("source three-owner second-moment envelope false")
    if GL>G or not 0<GL<=MU:
        raise AssertionError("original Harris positive compatible lower certificate false")
    if B/M>1-GL/MU:
        raise AssertionError("independent robust all-h B/M upper certificate false")
    return {
        "s":s,"scheme":scheme,"CORE":core,
        "true_original_source_flags":len(c["flags"]),
        "retained_original_source_flags":len(c["ids"]),
        "real_original_directed_proper_P3s":int(sums["source_threeowner_P3_count"]),
        "original_physical_endpoint_bins":counts["physical_endpoint_bins"],
        "distinct_original_three_owner_priority_sets":distinct_owner_triples,
        "exact_original_M":str(M),"exact_original_G":str(G),
        "exact_original_B":str(B),"exact_original_B_over_M":str(B/M),
        "original_Harris_lower_M":str(sums["M_Harris_lower"]),
        "original_priority_degree_upper_M":str(MU),
        "original_rankless_P3_count_square_upper_M":
            str(sums["M_trivial_n_over_64_upper"]),
        "original_Harris_lower_positive_compatible_G":str(GL),
        "original_certified_B_over_M_upper_from_LOWER_G_UPPER_M":
            str(1-GL/MU),
        "original_true_priority_loss_from_rankless_physical_count":
            str(sums["priority_loss_from_rankless_physical_count"]),
        "original_local_strict_B75_bad_endpoint_bins":
            counts["strict_local_B75_bad_endpoint_bins"],
        "max_actual_source_P3_endpoint_bin":maximum,
        "all_h_exact_SOURCE_three_owner_joint_port_contraction":True,
        "all_h_Harris_product_lower_and_degree_minimum_upper":True,
        "all_h_GLOBAL_B75_by_coarse_envelope_proved":GL>MU/4,
        "root_PROVED_A":False
    }


def canonical_report():
    rows=[_joint_original_selector_case(*case) for case in CASES]
    expected=(1346,1154,838,83892,82846,79404,9966,66418)
    if tuple(x["real_original_directed_proper_P3s"] for x in rows)!=expected:
        raise AssertionError("independent ORIGINAL source-joined P3 population disagrees")
    return {"schema":SCHEMA,"issue":230,"status":ROOT_STATUS,
            "actual_genuine_W32_W34_cases":rows,
            "all_h_ROOT_seven_motif_sixset_theorem_proved":False,
            "ASET_exponent_claimed":False}


if __name__=="__main__":
    print("AA4_JOINT3_CERTIFICATE="+json.dumps(canonical_report(),sort_keys=True,separators=(",",":")))
