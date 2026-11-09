"""AA4-DICHOTOMY: all-h same-endpoint ORIGINAL proper-P3 selector covariance sign.

Mathematical theorem:
for ANY dyadic genuine W(3,s), legal independently globally injective fixed
original f/g pair labels (arbitrary mutual correlation), ANY adversarial
named original source-ID deletion Z and paired original core C <= I\Z,
and two ACTUAL directed coordinate-proper physical 3paths with the SAME
physical ordered endpoint vertices:

 If the union of their true ORIGINAL owner flags has a source J edge,
 or either typed original physical pair-label union graph is nonbipartite:
   P(both selected)=0; Cov=-P1*P2<0.
 Otherwise:
   P(both selected)>=4*P1*P2; Cov>=3*P1*P2>0.

The positive rank correlation is by Harris association on independent
source priority uniforms (reverse source-owner coordinates; leave outsider
coordinates unchanged). Each typed cut has at least ONE shared endpoint
parity constraint, so compatible GF2 union rank <=3+3-1=5, and its exact
intersection probability is at least 2*product of two path marginals.
No product-independence hypothesis on the paths is made.

All-h written proof in docs. Finite source oracle independently reconstructs
true symplectic incidence source, J, real paired edges, ORIGINAL paths,
an independent rational owner-priority integral, GF2 two-cut rank and complete
W32 source endpoint-pair covariance ledger. No import from #752 calculations.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import comb
import json

from hyp105_original_defect_factor_referee import genuine_symplectic_source

SCHEMA="mathlab.hyp105.original-compatible-P3-covariance-dichotomy.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"


def actual_source(s,scheme="lex",core="full"):
    if type(s) is not int or s not in (2,4):
        raise ValueError("finite source requires original symplectic W32/W34")
    N=(s+1)*(s*s+1)
    original_flags=tuple(map(tuple,genuine_symplectic_source(s)))
    if len(original_flags)!=(s+1)*N or len(set(original_flags))!=len(original_flags):
        raise AssertionError("invalid named original incidence source")
    a=2
    while comb(a,2)<N:a+=1
    choices=list(combinations(range(a),2))
    f=list(choices[:N]);g=list(choices[:N])
    if scheme=="reverse":
        g.reverse()
    elif scheme=="shift":
        f=f[3:]+f[:3];g=g[7:]+g[:7]
    elif scheme!="lex":
        raise ValueError("invalid fixed physical mapping")
    if core=="full":
        ids=tuple(range(len(original_flags)))
    elif core=="even":
        ids=tuple(range(0,len(original_flags),2))
    elif core=="Z17":
        ids=tuple(i for i in range(len(original_flags)) if i%17!=0)
    else:raise ValueError("invalid source core/deletion experiment")
    Z=tuple(i for i in range(len(original_flags)) if i not in ids)
    J=[set() for _ in original_flags]
    bypoint=defaultdict(list);byline=defaultdict(list)
    for i in ids:
        p,l=original_flags[i]
        bypoint[p].append(i);byline[l].append(i)
    for typ,groups in (("point",bypoint),("line",byline)):
        for flag_ids in groups.values():
            for i,j in combinations(flag_ids,2):
                pi,li=original_flags[i];pj,lj=original_flags[j]
                z1=g[li] if typ=="point" else f[pi]
                z2=g[lj] if typ=="point" else f[pj]
                if set(z1)&set(z2):
                    J[i].add(j);J[j].add(i)
    owner={};adj=defaultdict(set)
    for i in ids:
        p,l=original_flags[i]
        x0,x1=f[p];y0,y1=g[l]
        for u,v in (((x0,y0),(x1,y1)),((x0,y1),(x1,y0))):
            e=tuple(sorted((u,v)))
            if e in owner:raise AssertionError("physical original flag owner not unique")
            owner[e]=i
            adj[u].add(v);adj[v].add(u)
    if len(owner)!=2*len(ids):
        raise AssertionError("true original source not both physical diagonals")
    return {"s":s,"a":a,"flags":original_flags,"f":f,"g":g,
            "ids":ids,"Z":Z,"J":J,"owner":owner,"adj":adj,
            "source_max_J":max((len(J[i]) for i in ids),default=0)}


def true_proper_p3(c,max_paths=None):
    out=[]
    for x0 in sorted(c["adj"]):
        for x1 in sorted(c["adj"][x0]):
            for x2 in sorted(c["adj"][x1]):
                if x2[0] in (x0[0],x1[0]) or x2[1] in (x0[1],x1[1]):
                    continue
                for x3 in sorted(c["adj"][x2]):
                    path=(x0,x1,x2,x3)
                    if len({v[0] for v in path})<4 or len({v[1] for v in path})<4:
                        continue
                    owners=tuple(c["owner"][tuple(sorted((path[j],path[j+1])))]
                                 for j in range(3))
                    if len(set(owners))!=3:raise AssertionError("reused original path owner")
                    if any(j in c["J"][i] for i,j in combinations(owners,2)):
                        raise AssertionError("source J conflict in proper physical path")
                    out.append((path,owners))
                    if max_paths is not None and len(out)>=max_paths:
                        return out
    return out


def _source_priority_exact(owners,J):
    """Independent ALL finite source order-statistic integral on ≤6 owners."""
    S=tuple(sorted(set(owners)))
    if not S:return Fraction(1)
    if any(j in J[i] for i,j in combinations(S,2)):return Fraction(0)
    outer=set()
    for i in S:outer.update(J[i])
    outer-=set(S)
    neighbors={z:tuple(i for i in S if z in J[i]) for z in sorted(outer)}
    total=Fraction(0)
    k=len(S)
    for order in permutations(S):
        where={o:j for j,o in enumerate(order)}
        counts=[0]*k
        for dep in neighbors.values():
            counts[max(where[o] for o in dep)]+=1
        cumulative=0
        q=1
        for j in range(k-1,-1,-1):
            cumulative+=counts[j]+1
            q*=cumulative
        total+=Fraction(1,q)
    if not 0<total<=1:raise AssertionError("rank probability invalid")
    return total


def _constraint_rank(owners,c,typ):
    """If bipartite, rank over GF2 of true x_u XOR x_v=1 equations."""
    f=c["f"] if typ=="x" else c["g"]
    ix=0 if typ=="x" else 1
    graph=defaultdict(set)
    for i in owners:
        a,b=f[c["flags"][i][ix]]
        if a==b:raise AssertionError("not true unordered physical pair")
        graph[a].add(b);graph[b].add(a)
    bits={};components=0
    for seed in graph:
        if seed in bits:continue
        components+=1
        bits[seed]=0
        queue=[seed]
        while queue:
            v=queue.pop()
            for u in graph[v]:
                if u not in bits:
                    bits[u]=1-bits[v]
                    queue.append(u)
                elif bits[u]==bits[v]:
                    return None
    return len(graph)-components


def _probability(owners,c):
    S=tuple(sorted(set(owners)))
    p=_source_priority_exact(S,c["J"])
    if not p:return Fraction(0)
    r1=_constraint_rank(S,c,"x")
    if r1 is None:return Fraction(0)
    r2=_constraint_rank(S,c,"y")
    if r2 is None:return Fraction(0)
    return p*Fraction(1,2**(r1+r2))


def pair_dichotomy(a,b,c,prior_cache=None):
    """For same ordered physical endpoints: negative iff incompatible; otherwise joint>=4p1p2."""
    va,oa=a;vb,ob=b
    if va[0]!=vb[0] or va[-1]!=vb[-1]:
        raise ValueError("the universal factor-four theorem needs SAME endpoints")
    S=tuple(sorted(set(oa+ob)))
    def marginal(owners):
        if prior_cache is None:
            return _probability(owners,c)
        key=tuple(sorted(owners))
        if key not in prior_cache:
            prior_cache[key]=_probability(owners,c)
        return prior_cache[key]
    PA=marginal(oa)
    PB=marginal(ob)
    if not PA>0 or not PB>0:
        raise AssertionError("true proper original P3 survival must be positive")
    if any(j in c["J"][i] for i,j in combinations(S,2)):
        cause="original_J_conflict"
        joint=Fraction(0)
        rankX=rankY=None
        source_ratio=None
    else:
        rx=_constraint_rank(S,c,"x")
        ry=_constraint_rank(S,c,"y")
        if rx is None:
            cause="original_first_factor_odd_cycle"
            joint=Fraction(0)
            rankX=None;rankY=ry
            source_ratio=None
        elif ry is None:
            cause="original_second_factor_odd_cycle"
            joint=Fraction(0)
            rankX=rx;rankY=None
            source_ratio=None
        else:
            cause="compatible"
            rankX=rx;rankY=ry
            assert _constraint_rank(oa,c,"x")==_constraint_rank(oa,c,"y")==3
            assert _constraint_rank(ob,c,"x")==_constraint_rank(ob,c,"y")==3
            # Both 3-paths enforce the SAME typed endpoint parity bit relation.
            # Hence the two 3-edge constraint systems share one GF2 relation.
            if rankX>5 or rankY>5:
                raise AssertionError("shared original physical endpoints must reduce rank")
            pS=_source_priority_exact(S,c["J"])
            pA=_source_priority_exact(oa,c["J"])
            pB=_source_priority_exact(ob,c["J"])
            source_ratio=pS/(pA*pB)
            if source_ratio<1:
                raise AssertionError("Harris original-priority association fails")
            joint=pS*Fraction(1,2**(rankX+rankY))
            if joint<4*PA*PB:
                raise AssertionError("quantitative compatible original path theorem fails")
    covariance=joint-PA*PB
    if cause=="compatible" and covariance<3*PA*PB:
        raise AssertionError("compatible paths must have covariance >=3 marg-product")
    if cause!="compatible" and covariance!=-PA*PB:
        raise AssertionError("incompatible paths must have exactly negative product")
    return {"cause":cause,"p_a":PA,"p_b":PB,"joint":joint,
        "covariance":covariance,"rank_x_union":rankX,
        "rank_y_union":rankY,"original_priority_ratio":source_ratio,
        "minimum_two_typed_color_boost":4 if cause=="compatible" else 0,
        "typed_color_extra_boost":2**(10-rankX-rankY)
            if cause=="compatible" else 0}


def _display_pair(a,b,t):
    return {"original_owner_ids_a":list(a[1]),"original_owner_ids_b":list(b[1]),
            "physical_path_a":[list(v) for v in a[0]],
            "physical_path_b":[list(v) for v in b[0]],
            "cause":t["cause"],"joint":str(t["joint"]),
            "marginal_a":str(t["p_a"]),"marginal_b":str(t["p_b"]),
            "covariance":str(t["covariance"]),
            "rank_first":t["rank_x_union"],"rank_second":t["rank_y_union"],
            "rank_priority_ratio":None if t["original_priority_ratio"] is None
               else str(t["original_priority_ratio"]),
            "typed_color_extra_boost":t["typed_color_extra_boost"]}


def endpoint_pair_audit(c,paths,max_pairs=None):
    """Complete W32; W34 uses explicit bounded same-endpoint witness sample."""
    byend=defaultdict(list)
    for path in paths:
        byend[(path[0][0],path[0][-1])].append(path)
    total=0
    classes=Counter()
    rank_boost_hist=Counter()
    witnesses={}
    weighted_broken=Fraction(0)
    weighted_compatible=Fraction(0)
    mean2=Fraction(0)
    exact2=Fraction(0)
    direct_cov=Fraction(0)
    prob_cache={}
    ordered_pair_count=0
    for ep,group in sorted(byend.items()):
        gm=sum((_probability(p[1],c) for p in group),Fraction(0))
        if max_pairs is None:mean2+=gm*gm
        for i,a in enumerate(group):
            for j,b in enumerate(group):
                if max_pairs is not None and total>=max_pairs:break
                r=pair_dichotomy(a,b,c,prob_cache)
                cls=r["cause"]
                classes[cls]+=1
                weighted= r["p_a"]*r["p_b"]
                if cls=="compatible":
                    weighted_compatible+=weighted
                    rank_boost_hist[r["typed_color_extra_boost"]]+=1
                else:
                    weighted_broken+=weighted
                exact2+=r["joint"]
                direct_cov+=r["covariance"]
                if cls not in witnesses and a!=b:
                    witnesses[cls]=_display_pair(a,b,r)
                total+=1
            if max_pairs is not None and total>=max_pairs:break
        if max_pairs is not None and total>=max_pairs:break
    if max_pairs is None:
        ordered_pair_count=sum(len(x)**2 for x in byend.values())
        if total!=ordered_pair_count:raise AssertionError("full endpoint tensor pair count")
        if weighted_broken+weighted_compatible!=mean2:
            raise AssertionError("full original second-moment weighted pair conservation")
        if exact2-mean2!=direct_cov or direct_cov<0:
            raise AssertionError("original covariance decomposition/Jensen false")
        if exact2<4*weighted_compatible:
            raise AssertionError("universal factor-four lower bound false")
        if classes["compatible"]+sum(n for cause,n in classes.items()
           if cause!="compatible")!=ordered_pair_count:
            raise AssertionError("source class disjointness")
    return {"s":c["s"],"original_flags":len(c["flags"]),
       "original_CORE_ID_count":len(c["ids"]),"original_deleted_Z_ID_count":len(c["Z"]),
       "max_true_J_degree":c["source_max_J"],
       "actual_paired_original_physical_edges":len(c["owner"]),
       "proper_directed_P3_scanned":len(paths),
       "complete_true_original_P3_and_joint_pairs":max_pairs is None,
       "physical_ordered_endpoint_bins":len(byend),
       "same_end_ordered_path_pairs_audited":total,
       "same_end_ordered_path_pair_classes":dict(classes),
       "compatible_extra_physical_color_boost_histogram":{
           str(k):v for k,v in sorted(rank_boost_hist.items())},
       "weighted_compatible_marginal_product":str(weighted_compatible),
       "weighted_incompatible_marginal_product":str(weighted_broken),
       "exact_selected_P3_second_moment":str(exact2),
       "independently_summed_original_pair_covariances":str(direct_cov),
       "exact_mean_selected_P3_norm2":str(mean2) if max_pairs is None else None,
       "quantitative_color_rank_lower4":str(4*weighted_compatible),
       "true_original_first_witnesses":witnesses}


def canonical_report():
    cases=[]
    for s,scheme,core,cap_paths,cap_pairs in (
        (2,"lex","full",None,None),
        (2,"reverse","full",None,None),
        (2,"shift","Z17",None,None),
        (4,"lex","even",1800,160),
        (4,"reverse","even",1800,160),
        (4,"shift","Z17",1800,160),
    ):
        c=actual_source(s,scheme,core)
        paths=true_proper_p3(c,max_paths=cap_paths)
        if not paths:raise AssertionError("original physical path enumeration empty")
        result=endpoint_pair_audit(c,paths,cap_pairs)
        result["scheme"]=scheme
        result["core"]=core
        cases.append(result)
    full=cases[0]
    known={"compatible":2386,"original_J_conflict":1348,
           "original_first_factor_odd_cycle":464,
           "original_second_factor_odd_cycle":172}
    if full["same_end_ordered_path_pair_classes"]!=known:
        raise AssertionError("independent W32 four-class physical theorem census disagrees")
    if full["same_end_ordered_path_pairs_audited"]!=4370:
        raise AssertionError("true original W32 full same-endpoint pair count changed")
    for k in known:
        if k not in full["true_original_first_witnesses"]:
            raise AssertionError("missing physical real-original distinct witness")
    return {"schema":SCHEMA,"issue":230,"status":ROOT_STATUS,
        "root_PROVED_A":False,"same_endpoint_factor_four_all_h_THEOREM":True,
        "negative_iff_SOURCE_or_TYPED_odd_cycle_all_h_THEOREM":True,
        "independent_original_full_W32_and_sample_W34_cases":cases,
        "source_quantifiers":"all dyadic s, fixed globally injected arbitrary correlated f/g, any original Z and paired C",
        "not_claimed":"universal improvement to root Branch A, ASET exponent, numeric external graph constants"}


if __name__=="__main__":
    print("AA4_COMPATIBLE_PAIR_CERTIFICATE="+json.dumps(canonical_report(),sort_keys=True,separators=(",",":")))
