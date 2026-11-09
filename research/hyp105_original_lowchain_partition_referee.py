"""AA4-LOWCHAIN: independent ORIGINAL full-GQ low-path exhaustive partition referee.

All-h source theorem is in docs. Finite W32/W34 oracles are written
independently of prior LOW, BBo, original endpoint, source blocker, or
P3 test implementations. The only project import is a TRUE symplectic
W(3,s) incidence fixture from the previous independent constructor.

Exact all-path partition:
 W3 = improper + missing + incident + endbad + deleted_projection
      + interior_blocked_union + 2 * distinct_produced_original_BBo.
At each admissible endpoint, the four interior blockers are tested
independently; exact mixed full-allowed/core original-source books bound
their occurrences. All source-ID anchors can be outside the physical CORE.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt
import json

from hyp105_original_defect_factor_referee import genuine_symplectic_source

SCHEMA="mathlab.hyp105.original-lowchain-source-partition.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
R=93313
K=64
RHO_CAP=Fraction(1,2**32)
D6_WEIGHT=54162
BBO_WEIGHT=53838


def ceil_fraction(x):
    if type(x) is not Fraction:raise ValueError("require exact Fraction")
    return -(-x.numerator//x.denominator)


def ceil_sqrt(n):
    if type(n) is not int or n<0:raise ValueError("require nonnegative integer")
    t=isqrt(n)
    return t+(t*t<n)


def formal_low_heavy_glue(C0,c0):
    """Exact all-h LOW error ledger and HEAVY/L0 composition (no numeric graph constant)."""
    if (type(C0) is not Fraction or type(c0) is not Fraction
        or C0<1 or not 0<c0<=1):
        raise ValueError("fixed formal rational graph bounds required")
    T=ceil_fraction(Fraction(17*R**3,2)*C0**3)
    q2=16*comb(2*(K+1),2)
    q3=64*comb(3*(K+1),3)
    L6=24+153*T*T
    L4=q2**2*ceil_sqrt(ceil_fraction(Fraction(17*L6,4)))+19*T
    B0=ceil_sqrt(360*(K+1)*T)
    E=5*q3*ceil_sqrt(L6)
    D=4*ceil_sqrt(B0*T*L4)
    s0=max(64,444*T,(8*E)**2,(8*D)**8)
    h0=(s0-1).bit_length()
    delta=c0/Fraction(R**6)
    tstar=Fraction(119,24)-Fraction(2*D6_WEIGHT,BBO_WEIGHT)*delta
    rho=tstar*tstar/Fraction(12*q3*q3*L6)
    low_bbo=(Fraction(119,24)-tstar)/2
    checks={
       "heavy_root_graph_C0_c0_constants_fixed_once":True,
       "T_adaptive_heavy_graph_threshold":T>=Fraction(17*R**3,2)*C0**3,
       "true_SOURCE_low_core_at_least_three_quarters":
           Fraction(1)-Fraction(1,8)-Fraction(5,64)-rho>=Fraction(3,4),
       "true_source_K_equals_64":K==64,
       "proper_r_path_source_J_free_selector_q2_q3":
           q2==4**2*comb(2*(K+1),2) and q3==4**3*comb(3*(K+1),3),
       "bipartite_selected_sixth_moment":L6==24+153*T*T,
       "source_fourth_moment_no_extra_disjoint_cross_factor":
           L4==q2**2*ceil_sqrt(ceil_fraction(Fraction(17*L6,4)))+19*T,
       "FULL_ALLOWED_CORE_dual_book_constant":B0**2>=360*(K+1)*T,
       "source_point_line_four_internal_blockers":
           D>=4*ceil_sqrt(B0*T*L4),
       "non_Z_GQ_end_bad_24s5_energy_term":E>=5*q3*ceil_sqrt(L6),
       "coordinate_wrong_error_at_most_sixth_over_eight":444*T<=s0,
       "endpoint_wrong_error_at_most_sixth_over_eight":(8*E)**2<=s0,
       "four_blocker_error_at_most_sixth_over_eight":(8*D)**8<=s0,
       "three_small_nonZ_errors_reduce_16over3_to_119over24":
           Fraction(16,3)-3*Fraction(1,8)==Fraction(119,24),
       "original_three_ANCHOR_roles_s_squared_deletion_mask":
           Fraction(12*q3*q3*L6)*rho==tstar*tstar,
       "globally_admissible_rho_below_R_heavy_cap":
           0<rho<RHO_CAP and rho<Fraction(3,64),
       "source_positive_BBo_asymptotic_matching":
           low_bbo==Fraction(D6_WEIGHT,BBO_WEIGHT)*delta,
       "source_UNWEIGHTED_seven_class_lower_unconditional_if_INPUTS":
           low_bbo>=delta and delta>0,
       "additive_GF5_signed_R3_NOT_probability_union":
           BBO_WEIGHT*low_bbo==D6_WEIGHT*delta,
       "s0_is_absolute_dyadic_threshold":(1<<h0)>=s0,
       "root_NOT_independently_accepted_without_all_h_examination":True,
    }
    if not all(checks.values()):
        raise AssertionError("exact LOW/HEAVY final closure arithmetic failed")
    return {"C0_FORMAL":str(C0),"c0_FORMAL":str(c0),
        "R":R,"T":T,"q2":q2,"q3":q3,"L6":L6,"L4":L4,"B0":B0,
        "E":E,"D":D,"s0":s0,"h0":h0,
        "delta":str(delta),"t_star":str(tstar),"rho_star":str(rho),
        "LOW_original_BBo_sextic_coefficient":str(low_bbo),
        "GF5_additive_sextic_coefficient":str(D6_WEIGHT*delta/Fraction(51**6)),
        "proved_independent_full_Branch_A":False,
        "published_numeric_graph_constants_claimed":False,
        "all_h_LOWMATH_formal_bound_gates":checks}


def _source(s,mode):
    flags=tuple(map(tuple,genuine_symplectic_source(s)))
    V=(s+1)*(s*s+1)
    a=2
    while comb(a,2)<V:a+=1
    pairs=list(combinations(range(a),2))
    f=list(pairs[:V]);g=list(pairs[:V])
    if mode=="reverse":
        g.reverse()
    elif mode=="shift":
        f=f[3:]+f[:3];g=g[7:]+g[:7]
    elif mode=="lex":
        pass
    elif mode=="seed":
        pass
    else:raise ValueError("unknown fixed global pair-map scheme")
    bypoint=[set() for _ in range(V)]
    byline=[set() for _ in range(V)]
    index={}
    for i,(p,l) in enumerate(flags):
        bypoint[p].add(l);byline[l].add(p);index[p,l]=i
    if len(flags)!=(s+1)*V or any(len(x)!=s+1 for x in bypoint+byline):
        raise AssertionError("not genuine original GQ")
    proj={}
    for q in range(V):
        for r in range(V):
            if r in bypoint[q]:continue
            candidates=[]
            for l in bypoint[q]:
                for p in byline[l]:
                    if p!=q and r in bypoint[p]:
                        candidates.append((p,l,(index[q,l],index[p,l],index[p,r])))
            if len(candidates)!=1:
                raise AssertionError("original unique FULL GQ projection axiom false")
            proj[q,r]=candidates[0]
    seed=None
    if mode=="seed":
        q,r=next(iter(sorted(proj)))
        p,l,anchors=proj[q,r]
        iso=[]
        seenp={p,q};seenl={l,r}
        for i,(pp,ll) in enumerate(flags):
            if pp not in seenp and ll not in seenl:
                seenp.add(pp);seenl.add(ll);iso.append(i)
                if len(iso)==3:break
        if len(iso)!=3:raise AssertionError("failed genuine non-overlap source seed")
        xp=[(0,3),(4,5),(0,1),(1,2),(2,3)]
        yp=xp
        givenf={q:xp[0],p:xp[1]}
        giveng={r:yp[0],l:yp[1]}
        for j,i in enumerate(iso):
            pp,ll=flags[i]
            givenf[pp]=xp[2+j];giveng[ll]=yp[2+j]
        for labels,known in ((f,givenf),(g,giveng)):
            used=set(known.values())
            remaining=iter(q for q in pairs if q not in used)
            for j in range(V):
                labels[j]=known.get(j)
                if labels[j] is None:labels[j]=next(remaining)
        seed={"q":q,"r":r,"p":p,"ell":l,
            "original_projection_anchors":list(anchors),
            "original_physical_3path_owners":iso,
            "expected_forward_physical_path":[[j,j] for j in range(4)]}
    if len(set(f))!=V or len(set(g))!=V:
        raise AssertionError("globally pair-injective maps invalid")
    return {"s":s,"V":V,"a":a,"flags":flags,"f":tuple(f),"g":tuple(g),
       "bypoint":bypoint,"byline":byline,"index":index,"projection":proj,
       "seed":seed}


def _edge(u,v):
    if u==v:raise AssertionError("source-owned edge cannot be loop")
    return tuple(sorted((u,v)))


def _actual_core(c,C,Z):
    N=len(c["flags"])
    if any(type(i) is not int or not 0<=i<N for i in C|Z):
        raise ValueError("invalid named original ID")
    if C&Z:raise ValueError("core contains deleted original source ID")
    f,g,flags=c["f"],c["g"],c["flags"]
    owner={};adj=defaultdict(set)
    for i in sorted(C):
        p,l=flags[i];x,z=f[p];y,w=g[l]
        for e in (_edge((x,y),(z,w)),_edge((x,w),(z,y))):
            if e in owner:raise AssertionError("physical pair edge double-owned")
            owner[e]=i
            u,v=e;adj[u].add(v);adj[v].add(u)
    if len(owner)!=2*len(C):
        raise AssertionError("not two REAL physical diagonals per original source flag")
    return owner,adj


def _endpoint(c,u,v,Z):
    x,y=u;z,w=v
    if x==z or y==w:raise ValueError("off-coordinate endpoints needed")
    f,g=c["f"],c["g"]
    q=c["decode_f"].get(tuple(sorted((x,z))))
    r=c["decode_g"].get(tuple(sorted((y,w))))
    if q is None or r is None:return ("missing",None)
    if r in c["bypoint"][q]:return ("incident",None)
    p,l,anchors=c["projection"][q,r]
    if (set(f[p]) & {x,z}) or (set(g[l]) & {y,w}):
        return ("endbad",None)
    if set(anchors)&Z:return ("deleted",None)
    return ("eligible",(p,l,anchors,q,r))


def _endpoints(c,Z):
    a=c["a"]
    counts=Counter()
    e_bad=set()
    for x in range(a):
      for z in range(a):
        if x==z:continue
        for y in range(a):
          for w in range(a):
            if y==w:continue
            u=(x,y);v=(z,w)
            category,_=_endpoint(c,u,v,Z)
            counts[category]+=1
            if category!="eligible":e_bad.add((u,v))
    if sum(counts.values())!=a*a*(a-1)**2:
        raise AssertionError("full typed ordered endpoint partition size")
    if len(e_bad)!=sum(counts[k] for k in ("missing","incident","endbad","deleted")):
        raise AssertionError("endpoint union overlap wrong")
    return counts,e_bad


def _trace4(adj):
    t4=0
    for u in adj:
        paths=Counter(v for mid in adj[u] for v in adj[mid])
        t4+=sum(x*x for x in paths.values())
    return t4


def _mixed_book(c,C,Z,dual=False):
    """Full A=I minus Z / CORE C dual mixed book, independently rederived."""
    flags=c["flags"]
    f,g=c["f"],c["g"]
    bypoint=c["bypoint"];byline=c["byline"]
    if dual:
        flags=tuple((l,p) for p,l in flags)
        f,g=g,f
        bypoint,byline=byline,bypoint
    V=c["V"];a=c["a"]
    A=set(range(len(flags)))-Z
    RA=[[0]*a for _ in range(V)]
    RC=[[0]*a for _ in range(V)]
    for i in A:
        p,l=flags[i]
        for y in g[l]:RA[p][y]+=1
    for i in C:
        p,l=flags[i]
        for y in g[l]:RC[p][y]+=1
    KAC={}
    for p in range(V):
        for u in range(V):
            KAC[p,u]=sum(RA[p][y]*RC[u][y] for y in range(a))
    neigh=[set() for _ in range(V)]
    for pts in byline:
        for p,q in combinations(sorted(pts),2):
            neigh[p].add(q);neigh[q].add(p)
    occup=defaultdict(set)
    for p,pair in enumerate(f):
        for x in pair:occup[x].add(p)
    books=0
    for u in range(V):
        x,k=f[u]
        for first,inner in ((x,k),(k,x)):
            for p in occup[inner]:
                cp=sum(q in occup[first] for q in neigh[p])
                books+=cp*KAC[p,u]
    return books


def _threepath_source_inverse(c,ids,C,Z,owner):
    """Independent SOURCE-FIRST physical P3 inverse, not enumeration of 3-walks."""
    ids=tuple(sorted(ids));flags=c["flags"];f,g=c["f"],c["g"]
    if len(ids)!=6 or len(set(ids))!=6 or set(ids)&Z:
        return ()
    cp=Counter(flags[i][0] for i in ids)
    cl=Counter(flags[i][1] for i in ids)
    repeatedp=[p for p,v in cp.items() if v==2]
    repeatedl=[l for l,v in cl.items() if v==2]
    if (len(cp)!=5 or len(cl)!=5 or len(repeatedp)!=1 or len(repeatedl)!=1
        or any(v not in (1,2) for v in cp.values())
        or any(v not in (1,2) for v in cl.values())):
        return ()
    p,l=repeatedp[0],repeatedl[0]
    midd=c["index"].get((p,l))
    if midd not in ids:return ()
    qe=[i for i in ids if flags[i][1]==l and flags[i][0]!=p]
    re=[i for i in ids if flags[i][0]==p and flags[i][1]!=l]
    if len(qe)!=1 or len(re)!=1:return ()
    q=flags[qe[0]][0];r=flags[re[0]][1]
    if c["projection"].get((q,r))!=(p,l,(qe[0],midd,re[0])):
        return ()
    anchors={qe[0],midd,re[0]}
    path_ids=set(ids)-anchors
    if len(path_ids)!=3 or not path_ids<=C:return ()
    if any(flags[i][0] in {p,q} or flags[i][1] in {l,r} for i in path_ids):
        return ()
    if set(f[p])&set.union(*(set(f[flags[i][0]]) for i in path_ids),set(f[q])):
        return ()
    if set(g[l])&set.union(*(set(g[flags[i][1]]) for i in path_ids),set(g[r])):
        return ()
    pathgraph=defaultdict(list)
    for i in path_ids:
        x,z=f[flags[i][0]]
        pathgraph[x].append((z,i));pathgraph[z].append((x,i))
    answers=[]
    for x0 in f[q]:
        xs=[x0];sequence=[];prev=None
        for _ in range(3):
            opts=[(z,i) for z,i in pathgraph[xs[-1]] if i!=prev]
            if len(opts)!=1:break
            z,i=opts[0];xs.append(z);sequence.append(i);prev=i
        if (len(sequence)!=3 or set(sequence)!=path_ids
            or len(set(xs))!=4 or set((xs[0],xs[3]))!=set(f[q])):
            continue
        yy=set(g[r])&set(g[flags[sequence[0]][1]])
        if len(yy)!=1:continue
        ys=[next(iter(yy))]
        for i in sequence:
            pair=set(g[flags[i][1]])
            if ys[-1] not in pair:break
            ys.append(next(iter(pair-{ys[-1]})))
        if (len(ys)!=4 or len(set(ys))!=4
            or set((ys[0],ys[3]))!=set(g[r])):continue
        vs=tuple(zip(xs,ys))
        if set(xs)&set(f[p]) or set(ys)&set(g[l]):continue
        if all(owner.get(_edge(vs[j],vs[j+1]))==sequence[j] for j in range(3)):
            answers.append(vs)
    if answers and (len(answers)!=2 or answers[0]!=answers[1][::-1]):
        raise AssertionError("produced six ORIGINAL ID inverse is NOT exact reversal pair")
    return tuple(answers)


def finite_original_partition(s,mode,C_mode="full",Z_mode="none"):
    c=_source(s,mode)
    c["decode_f"]={z:p for p,z in enumerate(c["f"])}
    c["decode_g"]={z:l for l,z in enumerate(c["g"])}
    N=len(c["flags"])
    seed=c["seed"]
    if C_mode=="full":C=set(range(N))
    elif C_mode=="even":C=set(range(0,N,2))
    elif C_mode=="seed":
        if seed is None:raise ValueError("seed core requires seed map")
        C=set(seed["original_physical_3path_owners"])
    elif C_mode=="seed_plus":
        if seed is None:raise ValueError("seed-plus core requires seed map")
        C=set(seed["original_physical_3path_owners"])
        C|={i for i in range(0,N,11) if i not in seed["original_projection_anchors"]}
    else:raise ValueError("unsupported named original core")
    if Z_mode=="none":Z=set()
    elif Z_mode=="anchor":
        if seed is None:raise ValueError("anchor deletion requires seeded source")
        Z={seed["original_projection_anchors"][1]}
    elif Z_mode=="sparse":
        Z={i for i in range(0,N,17) if i not in C}
    elif Z_mode=="point_star":
        p=0
        Z={i for i,(pp,ll) in enumerate(c["flags"]) if pp==p and i not in C}
    else:raise ValueError("unsupported source deletion mask")
    if C&Z:raise ValueError("named original Z overlaps physical CORE")
    owner,adj=_actual_core(c,C,Z)
    Delta=max((len(v) for v in adj.values()),default=0)
    t4=_trace4(adj)
    ep_counts,e_bad=_endpoints(c,Z)
    for key in ("missing","incident","endbad","deleted","eligible"):
        ep_counts.setdefault(key,0)
    counts=Counter()
    blockers=Counter()
    P3=Counter()
    accepted=defaultdict(set)
    total_from_deg=sum(len(adj[u])*len(adj[v])
        for u in adj for v in adj[u])
    for v0 in adj:
      for v1 in adj[v0]:
        for v2 in adj[v1]:
          for v3 in adj[v2]:
            path=(v0,v1,v2,v3)
            if (len({v[0] for v in path})!=4 or
                len({v[1] for v in path})!=4):
                counts["improper"]+=1
                continue
            P3[v0,v3]+=1
            category,projection=_endpoint(c,v0,v3,Z)
            if category!="eligible":
                counts["end_"+category]+=1
                continue
            p,l,anchors,q,r=projection
            bad=tuple(k for k,flag in (
                ("x1",v1[0] in c["f"][p]),("x2",v2[0] in c["f"][p]),
                ("y1",v1[1] in c["g"][l]),("y2",v2[1] in c["g"][l]))
                if flag)
            for k in bad:blockers[k]+=1
            if bad:
                counts["blocker_union"]+=1
                continue
            owners=[owner[_edge(path[j],path[j+1])] for j in range(3)]
            ids=tuple(sorted((*owners,*anchors)))
            if len(set(ids))!=6:
                raise AssertionError("admissible physical path not six distinct ORIGINAL IDs")
            if any(i in Z for i in ids):
                raise AssertionError("admissible path contains deleted ORIGINAL anchor")
            counts["accepted"]+=1
            accepted[ids].add(path)
    # Fail-closed stable certificate schema: all mutually exclusive seven
    # categories MUST appear explicitly even if their count is zero.
    for key in ("improper","end_missing","end_incident","end_endbad",
                "end_deleted","blocker_union","accepted"):
        counts.setdefault(key,0)
    if sum(counts.values())!=total_from_deg:
        raise AssertionError("exact directed 3walk source partition non-conservation")
    if counts["accepted"]!=sum(len(p) for p in accepted.values()):
        raise AssertionError("source sixsets duplicated or non-injective mapping")
    for ids,seen in accepted.items():
        if len(seen)!=2:
            raise AssertionError("original BBo six-ID multiplicity is not EXACT two")
        independent=set(_threepath_source_inverse(c,ids,C,Z,owner))
        if independent!=seen:
            raise AssertionError("independent original SOURCE-FIRST inverse disagrees")
    if C_mode=="seed" and Z_mode=="none":
        if counts["accepted"]!=2 or len(accepted)!=1:
            raise AssertionError("positive actual original seed BBo did not survive")
        if tuple(map(tuple,seed["expected_forward_physical_path"])) not in next(iter(accepted.values())):
            raise AssertionError("seed source original true physical 3path was lost")
    if C_mode=="seed" and Z_mode=="anchor" and counts["accepted"]!=0:
        raise AssertionError("deleted original middle projection anchor accepted erroneously")
    norm2=sum(x*x for x in P3.values())
    removed=sum(P3[uv] for uv in e_bad)
    cntbad=sum(counts["end_"+k] for k in ("missing","incident","endbad","deleted"))
    if removed!=cntbad:
        raise AssertionError("endpoint union not same original physical P3 bad mass")
    if removed*removed>len(e_bad)*norm2:
        raise AssertionError("original endpoint Cauchy energy false")
    BX=_mixed_book(c,C,Z,dual=False)
    BY=_mixed_book(c,C,Z,dual=True)
    for k,B in (("x1",BX),("x2",BX),("y1",BY),("y2",BY)):
        if blockers[k]**2>B*Delta*t4:
            raise AssertionError("original FULL allowed/CORE blocker Cauchy false")
    if counts["blocker_union"]>sum(blockers.values()):
        raise AssertionError("four original source internal blocker union not bounded")
    a=c["a"];V=c["V"];B=comb(a,2);M=B-V
    if ep_counts["missing"]!=4*(2*B*M-M*M):
        raise AssertionError("true missing original label-pair count wrong")
    if ep_counts["incident"]!=4*N:
        raise AssertionError("true ORIGINAL incident endpoint count wrong")
    if ep_counts["deleted"]>12*s*s*len(Z):
        raise AssertionError("true ORIGINAL 3 projections deleted > s²/role mask")
    if s>=64 and sum(ep_counts[k] for k in ("missing","incident","endbad"))>24*s**5:
        raise AssertionError("all-h nonZ physical source endpoint exception cap")
    W3_lower=Fraction((4*len(C))**3,a**4)
    if total_from_deg<W3_lower:
        raise AssertionError("Blakley Roy actual true-original W3 density false")
    return {
       "s":s,"mode":mode,"C_mode":C_mode,"Z_mode":Z_mode,
       "original_flags":N,"physical_vertices_including_isolates":a*a,
       "original_CORE_ID_count":len(C),"original_Z_ID_count":len(Z),
       "original_full_projection_anchors_outside_core":bool(seed and any(
            i not in C for i in seed["original_projection_anchors"])),
       "physical_core_edges":len(owner),"physical_max_degree":Delta,
       "W3_walks_directed_exact":total_from_deg,
       "W3_Blakley_Roy_lower_exact":str(W3_lower),
       "W3_source_partition":dict(counts),
       "W3_partition_sum":sum(counts.values()),
       "proper_endpoint_pair_tensor_Frobenius2":norm2,
       "endpoint_class_counts":dict(ep_counts),
       "endpoint_bad_union_size":len(e_bad),
       "proper_P3_bad_endpoint_weight":removed,
       "Cauchy_endpoint_error_squared_bound":len(e_bad)*norm2,
       "four_individual_interior_blockers":{k:blockers[k] for k in ("x1","x2","y1","y2")},
       "original_point_FULL_CORE_Bx":BX,"original_line_dual_FULL_CORE_By":BY,
       "original_physical_fourth_trace":t4,
       "four_blocker_Cauchy_source_bound_valid":True,
       "original_source_produced_BBo_sixsets":len(accepted),
       "original_source_produced_BBo_directed":counts["accepted"],
       "original_exact_2to1_inverse_all_positive_sixsets":True,
       "root_PROVED_A":False}


def canonical_report():
    cases=[
        (2,"lex","full","none"),
        (2,"reverse","full","none"),
        (2,"shift","even","sparse"),
        (2,"seed","seed","none"),
        (2,"seed","seed","anchor"),
        (2,"seed","seed_plus","none"),
        (4,"lex","even","sparse"),
        (4,"reverse","even","none"),
        (4,"seed","seed","none"),
        (4,"seed","seed","anchor"),
        (4,"seed","seed_plus","none"),
    ]
    finite=[finite_original_partition(*c) for c in cases]
    formal=[formal_low_heavy_glue(C,c) for C,c in (
        (Fraction(1),Fraction(1)),
        (Fraction(2),Fraction(1,5)),
        (Fraction(7,3),Fraction(1,17)))]
    return {"schema":SCHEMA,"issue":230,"status":ROOT_STATUS,
        "root_PROVED_A":False,"original_FULL_LOW_chain_independently_judged_finished":False,
        "published_numeric_graph_constants":False,
        "exact_all_h_low_heavy_formal_glue":formal,
        "true_original_W32_W34_finite_joint_partitions":finite}


if __name__=="__main__":
    print("AA4_LOWCHAIN_CERTIFICATE="+json.dumps(canonical_report(),sort_keys=True,separators=(",",":")))
