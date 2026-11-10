"""HYP-105 AA4-FULL-W34: exact source-first FULL symplectic W(3,4) P3 risk.

NEW all-h risk certificate: let p_gamma be strictly positive source-priority
plus TWO typed original-cut marginal for each real coordinate-proper P3,
and let endpoint family Gamma_uv have M_uv=(sum p)^2, D_uv=sum p^2,
incompatibility graph clique omega_uv, true incompatible weight B_uv.

For every source, no independence assumptions:
    G_uv=M_uv-B_uv >= max(M_uv/omega_uv, D_uv).
This combines weighted Motzkin-Straus with the physical PATH DIAGONAL
and strengthens either bound whenever effective path multiplicity
n_eff=M_uv/D_uv is below omega_uv.

Hence exact non-asymptotic all-h:
    B/M <= 1 - sum_uv max(M_uv/omega_uv,D_uv)/M.
A local strict bad ratio B_uv/M_uv>3/4 requires BOTH omega_uv>=5
and n_eff>4. Even omega>=5 ALONE is not a source risk witness.

Separately: every true ORIGINAL physical P3 determines a single oriented
middle physical edge, whose unique named owner ID corresponds exactly to
its f(point) and g(line) pair labels. For fixed ordered endpoints and
one oriented middle edge there is at most one such path; one ORIGINAL
middle flag has at most FOUR oriented physical diagonals, hence at most
four paths per endpoint family. This is an all-order genuine source
middle-anchor inversion and is verified on ALL physical paths.

The research artifact independently constructs genuine W(3,2), W(3,4)
symplectic original named point-line incidence flags, fixed complete
separately globally pair-injective f/g (arbitrary deterministic cross-
correlation), BOTH owned physical diagonals, exact original J pencils,
and FULL coordinate-proper real physical P3s; NO finite path sample for
any case marked complete. Main module imports ONLY the canonical genuine
symplectic incidence generator from #748, not earlier path/covariance/
motif or weighted-source programs. Tests may independently compare old
frozen exact W32/W34 census for regression. All weights are Fractions.
The root scientific status remains OPEN_WITH_FORMAL_BLOCKER.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import comb
import json

from hyp105_original_defect_factor_referee import genuine_symplectic_source

SCHEMA="mathlab.hyp105.original-full-W34-risk-effective-multiplicity.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
K=64
Q=16*(K+1)**3
THRESHOLD=Fraction(3,4)


def _source(s,scheme="lex",core="full"):
    if s not in (2,4) or type(s)!=int:
        raise ValueError("genuine symplectic W32/W34 only")
    V=(s+1)*(s*s+1)
    flags=tuple(map(tuple,genuine_symplectic_source(s)))
    if len(flags)!=(s+1)*V or len(set(flags))!=len(flags):
        raise AssertionError("not the genuine original symplectic point-line flags")
    a=2
    while comb(a,2)<V:a+=1
    pairs=list(combinations(range(a),2))
    x=list(pairs[:V]);y=list(pairs[:V])
    if scheme=="reverse":
        y.reverse()
    elif scheme=="shift":
        x=x[3:]+x[:3]
        y=y[7:]+y[:7]
    elif scheme!="lex":
        raise ValueError("fixed globally pair-injective label scheme")
    if len(set(x))!=V or len(set(y))!=V:
        raise AssertionError("original source label pair injection violated")
    if core=="full":
        ids=tuple(range(len(flags)))
    elif core=="even":
        ids=tuple(range(0,len(flags),2))
    elif core=="Z17":
        ids=tuple(i for i in range(len(flags)) if i%17)
    else:
        raise ValueError("must name original retained incidence core")
    pbook=defaultdict(list)
    lbook=defaultdict(list)
    for i in ids:
        p,l=flags[i]
        pbook[p].append(i);lbook[l].append(i)
    J=[set() for _ in flags]
    for kind,books in (("p",pbook),("l",lbook)):
        for members in books.values():
            for i,j in combinations(members,2):
                pi,li=flags[i];pj,lj=flags[j]
                u=y[li] if kind=="p" else x[pi]
                v=y[lj] if kind=="p" else x[pj]
                if u[0] in v or u[1] in v:
                    J[i].add(j);J[j].add(i)
    maxJ=max((len(J[i]) for i in ids),default=0)
    if maxJ>K:raise AssertionError("not a true original LOW-eligible source core")
    owner={};adj=defaultdict(set)
    for i in ids:
        p,l=flags[i]
        x0,x1=x[p];y0,y1=y[l]
        for u,v in (((x0,y0),(x1,y1)),((x0,y1),(x1,y0))):
            e=(u,v) if u<v else (v,u)
            if e in owner:raise AssertionError("one REAL physical edge has two ORIGINAL owners")
            owner[e]=i
            adj[u].add(v);adj[v].add(u)
    if len(owner)!=2*len(ids):
        raise AssertionError("each named ORIGINAL flag must own exactly TWO diagonals")
    return {"s":s,"a":a,"V":V,"flags":flags,"f":tuple(x),"g":tuple(y),
            "ids":ids,"J":J,"owner":owner,"adj":adj,
            "source_J_max_degree":maxJ,"scheme":scheme,"core":core,
            "original_deleted_Z_flags":len(flags)-len(ids)}


def _true_original_proper_P3(c):
    """No sampling. Each four-coordinate valid path and its real 3 source owners."""
    adj=c["adj"];edges=c["owner"];J=c["J"]
    for u in sorted(adj):
        for a in sorted(adj[u]):
            for b in sorted(adj[a]):
                if b[0]==u[0] or b[0]==a[0] or b[1]==u[1] or b[1]==a[1]:
                    continue
                for v in sorted(adj[b]):
                    p=(u,a,b,v)
                    if len({z[0] for z in p})!=4 or len({z[1] for z in p})!=4:
                        continue
                    owners=tuple(edges[(p[i],p[i+1]) if p[i]<p[i+1]
                        else (p[i+1],p[i])] for i in range(3))
                    if len(set(owners))!=3 or any(j in J[i] for i,j in combinations(owners,2)):
                        raise AssertionError("not a proper original J-free physical path")
                    middle=owners[1]
                    point,line=c["flags"][middle]
                    if tuple(sorted((a[0],b[0])))!=c["f"][point] or tuple(
                        sorted((a[1],b[1])))!=c["g"][line]:
                        raise AssertionError("middle source flag inverse physical labels fail")
                    yield p,owners


def _rank_probability3(owners,J):
    """Independent exact original priority event integration, 3! orders."""
    S=tuple(sorted(owners))
    if len(set(S))!=3 or any(j in J[i] for i,j in combinations(S,2)):
        raise ValueError("not original J-independent THREE owner IDs")
    extras=set().union(*(J[i] for i in S))-set(S)
    requirements={z:tuple(i for i in S if z in J[i]) for z in extras}
    total=Fraction(0)
    for order in permutations(S):
        place={i:z for z,i in enumerate(order)}
        counts=[0,0,0]
        for req in requirements.values():
            counts[max(place[i] for i in req)]+=1
        t=0;den=1
        for j in (2,1,0):
            t+=1+counts[j]
            den*=t
        total+=Fraction(1,den)
    if not Fraction(1,(K+1)**3)<=total<=1:
        raise AssertionError("true all-h Harris original product priority floor failed")
    return total


def _pair_bad(path1,owners1,path2,owners2,J):
    """Three disjoint false-color/source original covariance causes."""
    S=set(owners1);S.update(owners2)
    for i in S:
        if not J[i].isdisjoint(S):
            return "original_J_conflict"
    if path1[1][0]==path2[2][0] or path1[2][0]==path2[1][0]:
        return "first_typed_opposite_depth"
    if path1[1][1]==path2[2][1] or path1[2][1]==path2[1][1]:
        return "second_typed_opposite_depth"
    return "compatible"


def _exact_clique(adj):
    """Exact independent bit-mask pivot recursion, small true source endpoint graph."""
    n=len(adj)
    if n==0:return 0
    if n==1:return 1
    bitnbr=[sum((1<<j for j in nei)) for nei in adj]
    best=1
    def search(size,P,X):
        nonlocal best
        if not P and not X:
            if size>best:best=size
            return
        if size+P.bit_count()<=best:return
        U=P|X
        if U:
            opts=U
            pv=-1;pvdeg=-1
            while opts:
                t=opts&-opts;i=t.bit_length()-1;opts-=t
                deg=(P&bitnbr[i]).bit_count()
                if deg>pvdeg:pv=i;pvdeg=deg
            cand=P&~bitnbr[pv]
        else:cand=P
        while cand:
            t=cand&-cand;i=t.bit_length()-1
            search(size+1,P&bitnbr[i],X&bitnbr[i])
            P-=t;X|=t;cand-=t
            if size+P.bit_count()<=best:return
    search(0,(1<<n)-1,0)
    return best


def _full_exact_case(s,scheme,core):
    c=_source(s,scheme,core)
    binpaths=defaultdict(list)
    rank_cache={}
    middle_anchor_max=0
    full_path_count=0
    for vertices,owners in _true_original_proper_P3(c):
        os=tuple(sorted(owners))
        if os not in rank_cache:
            rank_cache[os]=_rank_probability3(os,c["J"])/64
        binpaths[(vertices[0],vertices[-1])].append(
            (vertices,owners,rank_cache[os]))
        full_path_count+=1
    if full_path_count==0:raise AssertionError("empty genuine original full source proper P3 set")
    J=c["J"]
    M=Fraction(0);B=Fraction(0);G=Fraction(0)
    raw_diag=Fraction(0);motz=Fraction(0);hybrid=Fraction(0)
    rank_high=0;rank_low=0
    M_high=Fraction(0);M_low=Fraction(0)
    M_risk_eff=Fraction(0)
    loc_gt75=0
    extreme=None
    max_clique=0;max_family=0
    last_row=None
    hist=Counter();cls=Counter()
    owned_middle_max=0
    mid_flags_duplicate_bin=0
    pairs_count=0
    num_unsafe_eff=0
    for ends,group in binpaths.items():
        n=len(group)
        max_family=max(max_family,n)
        middle_directed=set()
        middle_by_id=Counter()
        for path,os,w in group:
            key=(path[1],path[2])
            if key in middle_directed:
                raise AssertionError("unique oriented middle physical edge determines full source 3path at fixed endpoints")
            middle_directed.add(key)
            middle_by_id[os[1]]+=1
        owned_middle_max=max(owned_middle_max,max(middle_by_id.values()))
        if max(middle_by_id.values())>4:
            raise AssertionError("one ORIGINAL middle flag has >4 directed diagonals for same ordered endpoints")
        mid_flags_duplicate_bin+=sum(v>1 for v in middle_by_id.values())
        weights=[w for _,_,w in group]
        W=sum(weights,Fraction(0))
        localM=W*W
        localDiag=sum((w*w for w in weights),Fraction(0))
        localBad=Fraction(0)
        edges=[set() for _ in range(n)]
        for i in range(n):
            path1,owner1,p1=group[i]
            for j in range(i+1,n):
                path2,owner2,p2=group[j]
                reason=_pair_bad(path1,owner1,path2,owner2,J)
                if reason!="compatible":
                    localBad+=2*p1*p2
                    edges[i].add(j);edges[j].add(i)
                    cls[reason]+=2
                else:cls["compatible"]+=2
        cls["compatible"]+=n
        pairs_count+=n*n
        k=_exact_clique(edges)
        if not (1<=k<=Q):
            raise AssertionError("original all-h clique bound and source local risk invalid")
        localMot=localM/k
        localHybrid=max(localMot,localDiag)
        localG=localM-localBad
        if localG<localHybrid:
            raise AssertionError("all-h diagonal+Motzkin independent exact hybrid source bound violated")
        if localG+localBad!=localM:
            raise AssertionError("genuine W34 full source risk M conservation failed")
        if k>=5:
            rank_high+=1;M_high+=localM
        if k<=3:
            rank_low+=1;M_low+=localM
        if k>=5 and 4*localDiag<localM:
            num_unsafe_eff+=1;M_risk_eff+=localM
        if localBad*4>3*localM:
            loc_gt75+=1
            if not (k>=5 and 4*localDiag<localM):
                raise AssertionError("all-h necessary joint tail criterion violated")
        if extreme is None or Fraction(localBad,localM)>Fraction(
                extreme["local_B"],extreme["local_M"]):
            extreme={"endpoints":[list(ends[0]),list(ends[1])],
                "local_B":str(localBad),"local_M":str(localM),
                "local_ratio":str(localBad/localM),
                "clique":k,"paths":n,
                "effective_multiplicity":str(localM/localDiag),
                "source_midflags":dict(sorted(middle_by_id.items())),
                "real_path_owners":[list(os) for _,os,_ in group],
                "real_path_vertices":[[list(v) for v in path] for path,_,_ in group],
                "source_marginals":[str(w) for _,_,w in group]}
        max_clique=max(k,max_clique)
        hist[k]+=1
        M+=localM;B+=localBad;G+=localG
        raw_diag+=localDiag;motz+=localMot;hybrid+=localHybrid
    if sum(cls.values())!=pairs_count or M!=B+G:
        raise AssertionError("full original P3 weighted source tensor or class partition inconsistent")
    if not G>=hybrid>=motz>=M/Fraction(Q):
        raise AssertionError("universal source hybrid risk lower certificate invalid")
    if not G>=hybrid>=raw_diag:
        raise AssertionError("universal diagonal physical path lower failed")
    if not 0<=M_risk_eff<=M_high<=M:
        raise AssertionError("high-clique source tail weights not monotone")
    return {
        "original_s":s,"original_scheme":scheme,"original_CORE":core,
        "source_GQ_point_count":c["V"],"source_GQ_line_count":c["V"],
        "source_original_flag_ID_count":len(c["flags"]),
        "source_retained_original_flags":len(c["ids"]),
        "source_deleted_original_IDs":c["original_deleted_Z_flags"],
        "true_source_physical_edges":len(c["owner"]),
        "actual_physical_pair_alphabet_size":c["a"],
        "original_J_max_degree":c["source_J_max_degree"],
        "full_true_coordinate_proper_P3_count":full_path_count,
        "full_source_complete_census":True,
        "exact_unique_original_source_priority_threeowner_triples":len(rank_cache),
        "true_original_ordered_endpoint_bins":len(binpaths),
        "true_original_ordered_same_endpoint_path_pairs":pairs_count,
        "max_physical_paths_per_endpoint_bin":max_family,
        "max_same_original_middle_flag_P3_per_bin":owned_middle_max,
        "same_middle_flag_repeated_in_bin_count":mid_flags_duplicate_bin,
        "max_incompatibility_clique_over_all_real_endpoints":max_clique,
        "exact_clique_histogram":dict(sorted(hist.items())),
        "full_disjoint_actual_path_pair_source_classes":dict(sorted(cls.items())),
        "M":str(M),"B":str(B),"G":str(G),
        "B_over_M":str(B/M),
        "G_over_M":str(G/M),
        "diagonal_source_path_weight":str(raw_diag),
        "weighted_Motzkin_only_source_G_lower":str(motz),
        "new_weighted_hybrid_Motzkin_diagonal_G_lower":str(hybrid),
        "new_certified_B_over_M_hybrid_upper":str(1-hybrid/M),
        "hybrid_improvement_above_motzkin_G_lower":str(hybrid-motz),
        "bins_with_omega_at_least_5":rank_high,
        "bins_with_omega_at_most_3":rank_low,
        "M_share_omega_at_least_5":str(M_high/M),
        "M_share_omega_at_most_3":str(M_low/M),
        "bins_jointly_omega_at_least_5_and_n_eff_gt_4":num_unsafe_eff,
        "M_share_jointly_omega_at_least_5_and_n_eff_gt_4":str(M_risk_eff/M),
        "bins_with_actually_local_B_over_M_gt_3_over_4":loc_gt75,
        "top_actual_bad_local_endpoint_witness":extreme,
        "source_rho_small_Z_admissibility_NOT_claimed":True,
        "root_PROVED_A":False,
    }


def canonical_report():
    cases=[]
    for s,scheme,core in (
        (2,"lex","full"),
        (2,"reverse","full"),
        (2,"shift","Z17"),
        (4,"lex","full"),
        (4,"reverse","full"),
        (4,"shift","full"),
        (4,"lex","even"),
        (4,"shift","Z17"),
    ):
        cases.append(_full_exact_case(s,scheme,core))
    if [c["full_true_coordinate_proper_P3_count"] for c in cases[:3]] !=[1346,1154,838]:
        raise AssertionError("independent genuine W32 3P source baseline mismatch")
    if [c["full_true_coordinate_proper_P3_count"] for c in cases[3:5]] !=[83892,82846]:
        raise AssertionError("independent genuine W34 FULL source P3 anchor mismatch")
    return {
        "schema":SCHEMA,"issue":230,"status":ROOT_STATUS,
        "root_PROVED_A":False,
        "all_h_new_source_hybrid_diagonal_plus_weighted_Motzkin_theorem":True,
        "all_h_nonvacuous_risk_requires_omega5_AND_effective_multiplicity_gt4":True,
        "all_h_unique_oriented_middle_physical_edge_and_max_four_paths_per_original_midflag":True,
        "complete_independently_verified_original_W32_W34_source_census":cases,
        "all_h_global_B_over_M_below_3_over_4_PROVED":False,
        "numerical_external_C6_graph_constants_claimed":False,
        "ASET_exponent_claimed":False,
        "local_s2_counterexample_to_global_B_over_M_claimed":False,
    }


if __name__=="__main__":
    print("AA4_FULL_W34_RISK_CERTIFICATE="+json.dumps(canonical_report(),sort_keys=True,separators=(",",":")))
