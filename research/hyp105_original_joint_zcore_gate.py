"""AA4-JOINTZCORE: independently certified ORIGINAL dense-core and dyadic gate.

Every source flag is a REAL incidence ID of symplectic W(3,2^h).
The exact global bound is conditional on explicit #730 heavy and #731
six-original-ID B/B-overlap lifting lemmas. Formal input graph constants
are NOT certified numerical values of published C_graph,c_graph.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt


def ceil_root2(n):
    if type(n) is not int or n < 0:
        raise ValueError("nonnegative integer needed")
    root=isqrt(n)
    return root+(root*root<n)


def ceil_fraction(t):
    return -(-t.numerator//t.denominator)


def _norm_graph_constants(C_upper, c_lower):
    if type(C_upper) is not Fraction or type(c_lower) is not Fraction:
        raise ValueError("use EXACT rational formal graph constants")
    if C_upper<1 or not 0<c_lower<=1:
        raise ValueError("normalize formal graph constants C>=1, 0<c<=1")
    return C_upper,c_lower


def uniform_original_joint_gate(C_upper, c_lower):
    """All-h conditional proof ledger, no use of floating point or random f/g."""
    C,c=_norm_graph_constants(C_upper,c_lower)
    K=64
    T=ceil_fraction(Fraction(2**64)*C**3)
    q2=16*comb(2*(K+1),2)
    q3=64*comb(3*(K+1),3)
    L6=24+288*T*T
    L4=2*q2*q2*ceil_root2(8*L6)+56*T
    B0=ceil_root2(1280*(K+1)*T)
    E=8*q3*ceil_root2(L6)
    D=4*ceil_root2(B0*T*L4)
    # NEW use of the TRUE original low-core |C|>=3s^4/4:
    # W3 >= ((4*3s^4/4)^3)/(16s^6) = 27s^6/16.
    # Reserve s^6 for arbitrary ORIGINAL Z projection and 3*s^6/8
    # for the other errors. Then 2*BBo>=5s^6/16.
    rho=Fraction(1,12*q3*q3*L6)
    delta=c/Fraction(2**120)
    if not (rho<=Fraction(1,32) and delta<=Fraction(5,32)):
        raise AssertionError("heavy/core sufficient constant budget invalid")
    s0=max(64,672*T,(8*E)**2,(8*D)**8)
    h0=(s0-1).bit_length()
    if 2**h0<s0 or (h0 and 2**(h0-1)>=s0):
        raise AssertionError("invalid least dyadic exponent")
    if (Fraction(27,16)-1-3*Fraction(1,8)
            !=Fraction(5,16)):
        raise AssertionError("original dense-core leading arithmetic failed")
    old_q3=64*27*(K+1)**3
    old_T=ceil_fraction(Fraction(2**65)*C**3)
    old_L6=24+576*old_T**2
    old_rho=Fraction(1,768*old_q3**2*old_L6)
    if rho<=old_rho:
        raise AssertionError("old deletion radius unexpectedly dominates")
    return {
        "K":K,"T":T,"q2":q2,"q3":q3,"L6":L6,"L4":L4,
        "B0":B0,"E":E,"D":D,"rho":rho,"delta":delta,
        "old_rho":old_rho,"s0":s0,"h0":h0,
        "heavy_graph_constant_upper_formal":C,
        "heavy_graph_constant_lower_formal":c,
        "dense_core_flag_coefficient":Fraction(3,4),
        "physical_core_edge_coefficient":Fraction(3,2),
        "lowtail_W3_coefficient":Fraction(27,16),
        "lowtail_BBo_coefficient":Fraction(5,32),
        "root_230_mathematical_acceptance":False
    }


def verify_at_dyadic_h(ledger,h):
    """Exact sufficient threshold, preserving all fractional s-exponents."""
    if type(h) is not int or h<1:
        raise ValueError("positive dyadic h required")
    s=1<<h
    T,E,D=ledger["T"],ledger["E"],ledger["D"]
    checks={
        "heavy_original_T":T>=2**64*ledger["heavy_graph_constant_upper_formal"]**3,
        "low_original_core":Fraction(1)-Fraction(1,8)-Fraction(3,32)-Fraction(1,32)==Fraction(3,4),
        "density":Fraction(27,16)-Fraction(3,8)-1==Fraction(5,16),
        "improper":s>=672*T,
        "original_nonZ_endpoint":s>=(8*E)**2,
        "four_original_blockers":s>=(8*D)**8,
        "original_Z_mask":12*ledger["rho"]*ledger["q3"]**2*ledger["L6"]==1,
        "original_heavy_deletion":ledger["rho"]<=Fraction(1,32),
        "root_still_draft":ledger["root_230_mathematical_acceptance"] is False,
    }
    return {"h":h,"all_sufficient":all(checks.values()),
            "checks":checks}


def _physical_owned_source(s,flags,f,g,a):
    edges_by_flag=[]
    owner={}
    degree=Counter()
    for i,(p,ell) in enumerate(flags):
        x,k=f[p]
        y,w=g[ell]
        actual=[]
        for v,z in (((x,y),(k,w)),((x,w),(k,y))):
            edge=tuple(sorted((v,z)))
            if edge in owner or v==z:
                raise ValueError("noninjective physical edge/source owner")
            owner[edge]=i
            actual.append(edge)
            degree[v]+=1
            degree[z]+=1
        edges_by_flag.append(tuple(actual))
    if len(owner)!=2*len(flags):
        raise AssertionError("not two physical original diagonals per flag")
    return edges_by_flag,owner,degree


def _original_conflict_degrees(flags,f,g):
    degree=[0]*len(flags)
    points=defaultdict(list)
    lines=defaultdict(list)
    for i,(p,ell) in enumerate(flags):
        points[p].append(i)
        lines[ell].append(i)
    conflicts=0
    for pop,labels,project in (
        (points,g,lambda i: flags[i][1]),
        (lines,f,lambda i: flags[i][0])
    ):
        for ids in pop.values():
            for i,j in combinations(ids,2):
                if set(labels[project(i)])&set(labels[project(j)]):
                    degree[i]+=1
                    degree[j]+=1
                    conflicts+=1
    return degree,conflicts


def _returns(flags,f,g,core):
    Rpoint=Counter()
    Rline=Counter()
    for i in core:
        p,ell=flags[i]
        for y in g[ell]:
            Rpoint[p,y]+=1
        for x in f[p]:
            Rline[ell,x]+=1
    return 2*sum(v*v for v in Rpoint.values()),2*sum(v*v for v in Rline.values())


def prune_genuine_original_source(power,scheme,T,K,Z):
    """Independent actual original flag-level full-Q lowcore pruning certificate.

    T may be small to exercise the heavy deletion code on W32/W34.
    Such finite fixtures are NOT claimed to satisfy all-h hypotheses.
    """
    from hyp105_full_physical_degree_tail import genuine_source
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    if type(power) is not int or power not in (1,2):
        raise ValueError("finite genuine original W32/W34 only")
    if type(T) is not Fraction or T<=0 or type(K) is not int or K<0:
        raise ValueError("exact positive physical threshold and integer K")
    s,V,flags=genuine_source(power)
    a=2
    while comb(a,2)<V:
        a+=1
    maps=pair_labeled_symplectic(power,scheme)
    f=tuple(map(tuple,maps["left_labels"]))
    g=tuple(map(tuple,maps["right_labels"]))
    if len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V:
        raise ValueError("not complete separately injected original maps")
    Z=set(Z)
    if any(type(i) is not int or i<0 or i>=len(flags) for i in Z):
        raise ValueError("original deleted flag IDs invalid")
    per,owner,full_deg=_physical_owned_source(s,flags,f,g,a)
    original_K,conflicts=_original_conflict_degrees(flags,f,g)
    fullQ={v for v in full_deg if Fraction(full_deg[v])>T*s}
    heavy_edges={e for e in owner if set(e)&fullQ}
    heavy_ids={i for i,edges in enumerate(per) if any(e in heavy_edges for e in edges)}
    highconf={i for i,d in enumerate(original_K) if d>K}
    core=tuple(i for i in range(len(flags)) if i not in heavy_ids|highconf|Z)
    cowners={edge:i for i in core for edge in per[i]}
    surviving_heavy=sum(1 for e,i in owner.items() if e in heavy_edges and i not in Z)
    actual_heavy_loss=len(heavy_edges)-surviving_heavy
    core_degree=Counter()
    for e in cowners:
        for v in e:
            core_degree[v]+=1
    delta=max(core_degree.values(),default=0)
    Qx,Qy=_returns(flags,f,g,core)
    C_s=(s*s+1)*(s*s+a-2)
    assert len(flags)==(s+1)**2*(s*s+1)
    assert conflicts<=2*C_s
    assert len(heavy_ids)<=len(heavy_edges)
    assert actual_heavy_loss<=2*len(Z)
    assert len(core)>=len(flags)-len(heavy_edges)-len(highconf)-len(Z)
    assert delta<=T*s
    assert max((original_K[i] for i in core),default=0)<=K
    assert Qx+Qy<=8*len(flags)+8*C_s
    return {
        "s":s,"scheme":scheme,
        "source_original_count":len(flags),"physical_alphabet":a,
        "full_edges":len(owner),"full_high_vertices":len(fullQ),
        "full_heavy_physical_edges":len(heavy_edges),
        "original_full_heavy_flag_ids":len(heavy_ids),
        "original_conflict_edges":conflicts,
        "original_full_high_conflict_flags":len(highconf),
        "original_source_deleted_ids":len(Z),
        "original_surviving_heavy_edges":surviving_heavy,
        "original_heavy_owner_deletion_loss":actual_heavy_loss,
        "original_core_flag_count":len(core),
        "core_physical_edge_count":len(cowners),
        "core_max_physical_degree":delta,
        "core_max_original_conflict":max((original_K[i] for i in core),default=0),
        "original_Qx":Qx,"original_Qy":Qy,
        "original_core_budget_exact":len(flags)-len(heavy_ids|highconf|Z),
        "verified":True,
    }


def projection_anchor_exposure(power):
    """A fixed ORIGINAL W(3,s) flag is an anchor in each of 3 roles s² times.

    The factor 4 ordered physical endpoint orientations gives the
    at-most 12*s²*|Z| original projection-mask union bound.
    No physical maps or independent-label assumptions are needed.
    """
    from hyp105_full_physical_degree_tail import genuine_source
    s,V,flags=genuine_source(power)
    lookup={tuple(flag):i for i,flag in enumerate(flags)}
    incident=defaultdict(set)
    linepoints=defaultdict(set)
    for p,ell in flags:
        incident[p].add(ell)
        linepoints[ell].add(p)
    col=defaultdict(set)
    for p in range(V):
        for ell in incident[p]:
            col[p].update(linepoints[ell])
        col[p].discard(p)
    role=[[0]*len(flags) for _ in range(3)]
    for q in range(V):
        for r in range(V):
            if r in incident[q]:
                continue
            mids=col[q]&linepoints[r]
            if len(mids)!=1:
                raise AssertionError("not genuine original GQ unique projection")
            p=next(iter(mids))
            midlines=incident[p]&incident[q]
            if len(midlines)!=1:
                raise AssertionError("not genuine original GQ joint line")
            ell=next(iter(midlines))
            for j,flag in enumerate(((q,ell),(p,ell),(p,r))):
                role[j][lookup[flag]]+=1
    if any(z!=s*s for row in role for z in row):
        raise AssertionError("exact original flag anchor exposure failed")
    return {"s":s,"original_flags":len(flags),
            "projection_nonincident_pairs":V*(V-(s+1)),
            "three_roles_each_exact":s*s,"four_orientations":4,
            "one_original_deleted_flag_endpoint_cap":12*s*s}


def _as_readable(ledger):
    return {k:(str(v) if isinstance(v,Fraction) else v)
            for k,v in ledger.items() if k not in ("s0",) } | {
                "s0_decimal_digits":len(str(ledger["s0"])),
                "s0_is_explicit_integer":True}


def canonical_joint_original_certificates():
    formal=[]
    for C,c in ((Fraction(1),Fraction(1)),(Fraction(2),Fraction(1,5)),
                (Fraction(7,3),Fraction(1,17))):
        v=uniform_original_joint_gate(C,c)
        assert verify_at_dyadic_h(v,v["h0"])["all_sufficient"]
        assert not verify_at_dyadic_h(v,v["h0"]-1)["all_sufficient"]
        formal.append(_as_readable(v))
    rows=[]
    for p in (1,2):
        for scheme in ("lex","reverse-line"):
            Z=(0,) if p==1 else tuple(range(1,425,31))
            for T,K in ((Fraction(1,2),2),(Fraction(20),64)):
                rows.append(prune_genuine_original_source(p,scheme,T,K,Z))
    anchors=[projection_anchor_exposure(1),projection_anchor_exposure(2)]
    mixed=[]
    for scheme in ("lex","reverse-line"):
        for threshold in (Fraction(4),Fraction(17,4),Fraction(9,2),
                          Fraction(19,4),Fraction(5),Fraction(21,4),
                          Fraction(11,2)):
            v=prune_genuine_original_source(2,scheme,threshold,64,range(1,425,31))
            if (0<v["full_heavy_physical_edges"]<v["full_edges"] and
                    0<v["original_core_flag_count"]<411):
                v["diagnostic_T"]=str(threshold)
                v["both_full_heavy_and_paired_core_nonempty"]=True
                mixed.append(v)
                break
    if not mixed:
        raise AssertionError("no genuine original mixed heavy/low source witness")
    return {
        "schema":"mathlab.hyp105.original-JOINTZCORE.v1",
        "formal_graph_constants_only":True,
        "root_230_status":"OPEN_WITH_FORMAL_BLOCKER",
        "root_A_unconditionally_accepted":False,
        "conditional_exact_allh_ledgers":formal,
        "genuine_original_source_pruning_cases":rows,
        "exact_original_source_projection_anchor_exposures":anchors,
        "genuine_original_nonvacuous_mixed_tail_core_witnesses":mixed,
    }


if __name__=="__main__":
    import json
    print("AA4_TRUE_ORIGINAL_JOINTZCORE_CERTIFICATE="+json.dumps(
        canonical_joint_original_certificates(),
        sort_keys=True,separators=(",",":")),flush=True)
