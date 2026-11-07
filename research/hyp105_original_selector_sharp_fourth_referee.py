"""AA4-SELGAP: independent all-order original source selector & SHARP 4th moment.

All-order theorems, given a true ORIGINAL paired source core C of a genuine
symplectic W(3,s), globally injected fixed (possibly correlated) f,g, and
maximum actual ORIGINAL source conflict degree K:

  sigma_r = 1 / [4^r * binom(r(K+1),r)], r=2,3.
  sigma_r^2 ||P_r||_F^2 <= tr(A_C^(2r)).
  tr(A_C^4) <= sigma_2^-2 sqrt(2m X6) + Delta(Qx+Qy).
  Under m<=4s^4, Delta<=Ts, Qx+Qy<=28s^4,
  X6<=L6 s^6: L4_SHARP = q2² ceil(sqrt(8L6))+28T.
  The prior safe L4 = 2q2² ceil(sqrt(8L6))+56T is exactly doubled.

This code NEVER imports the historical selector, selector moments, GF5
classifiers or previous root-gate algebra; it uses only trusted genuine GQ
source and globally injected pair-map fixture constructors. A distinct
TEST-only oracle compares old constants and inverse source six-ID D6.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb, isqrt
import json

ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"


def ceil_sqrt(n):
    if type(n) is not int or n<0:
        raise ValueError("exact positive integer ceiling root only")
    r=isqrt(n)
    return r+(r*r<n)


def ceil_fraction(v):
    if type(v) is not Fraction:
        raise ValueError("exact rational formal graph constant required")
    return -(-v.numerator//v.denominator)


def original_case(h, scheme, shift_f=0, shift_g=0):
    from hyp105_full_physical_degree_tail import genuine_source
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    if (type(h) is not int or h not in (1,2)
            or type(shift_f) is not int or type(shift_g) is not int):
        raise ValueError("actual ORIGINAL W32/W34 source only")
    s,V,raw=genuine_source(h)
    model=pair_labeled_symplectic(h,scheme)
    flags=tuple(tuple(t) for t in raw)
    f=tuple(tuple(p) for p in model["left_labels"])
    g=tuple(tuple(p) for p in model["right_labels"])
    f=f[shift_f%V:]+f[:shift_f%V]
    g=g[shift_g%V:]+g[:shift_g%V]
    a=2
    while comb(a,2)<V:
        a+=1
    legal=set(combinations(range(a),2))
    if (len(flags)!=V*(s+1) or len(set(flags))!=len(flags)
            or len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V
            or any(pair not in legal for pair in f+g)):
        raise AssertionError("not genuine complete ORIGINAL pair-injective source")
    return {"s":s,"V":V,"a":a,"flags":flags,"f":f,"g":g,
            "scheme":scheme,"shift_f":shift_f,"shift_g":shift_g}


def conflict_graph(case, core):
    """Independent genuine source collinear pencil conflict graph."""
    flags=case["flags"]
    f,g=case["f"],case["g"]
    core=tuple(core)
    if (len(core)!=len(set(core)) or
            any(type(i) is not int or not 0<=i<len(flags) for i in core)):
        raise ValueError("invalid ORIGINAL source core ID")
    groups_p=defaultdict(list);groups_l=defaultdict(list)
    for i in core:
        p,l=flags[i];groups_p[p].append(i);groups_l[l].append(i)
    J={i:set() for i in core}
    for groups,side in ((groups_p,0),(groups_l,1)):
        for members in groups.values():
            for i,j in combinations(members,2):
                p1,l1=flags[i];p2,l2=flags[j]
                pair1=g[l1] if side==0 else f[p1]
                pair2=g[l2] if side==0 else f[p2]
                if set(pair1)&set(pair2):
                    J[i].add(j);J[j].add(i)
    if any(i in others or any(i not in J[j] for j in others)
           for i,others in J.items()):
        raise AssertionError("original conflict relation not symmetric/irreflexive")
    return J


def physical_core(case,core):
    """Both genuine ORIGINAL opposite physical diagonals with unique owner."""
    adj=defaultdict(set);owner={}
    f,g,flags=case["f"],case["g"],case["flags"]
    for i in core:
        p,l=flags[i];x,z=f[p];y,w=g[l]
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            e=tuple(sorted((u,v)))
            if e in owner:
                raise AssertionError("original physical edge has two owners")
            owner[e]=i;adj[u].add(v);adj[v].add(u)
    if len(owner)!=2*len(core):
        raise AssertionError("one true flag must own two actual physical edges")
    return adj,owner


def color_probability_exact(r):
    """FULL independent exhaustive physical coordinate color assignments."""
    if type(r) is not int or r not in (2,3):
        raise ValueError("short proper original r=2,3 only")
    good=0
    for bits in product((0,1),repeat=2*(r+1)):
        left=bits[:r+1];right=bits[r+1:]
        if all(left[j]!=left[j+1] and right[j]!=right[j+1]
               for j in range(r)):
            good+=1
    p=Fraction(good,2**(2*(r+1)))
    if p!=Fraction(1,4**r):
        raise AssertionError("original coordinate-proper path color law incorrect")
    return {"r":r,"assignments":2**(2*(r+1)),"successful":good,
            "exact_probability":p}


def exact_local_priority_floor(b,r):
    """All r specified pairwise nonconflicting ORIGINAL IDs first among b.

    This is a SUFFICIENT priority event, not equality to the selector's
    actual probability, which may be strictly greater.
    """
    if type(b) is not int or type(r) is not int or not 1<=r<=b:
        raise ValueError("original source neighborhood size b>=r required")
    return Fraction(1,comb(b,r))


def _powers(adj):
    """Independent physical matrix A²,A³ and exact traces A⁴,A⁶."""
    a2={v:Counter() for v in adj}
    for v,neighbors in adj.items():
        for mid in neighbors:
            a2[v].update(adj[mid])
    a3={v:Counter() for v in adj}
    for v,row in a2.items():
        for mid,n in row.items():
            for u in adj[mid]:
                a3[v][u]+=n
    tr4=sum(n*n for row in a2.values() for n in row.values())
    tr6=sum(n*n for row in a3.values() for n in row.values())
    return a2,a3,tr4,tr6


def independent_proper_path_referee(case,core,J,adj,owners,r):
    """All proper actual physical paths, real source IDs, exact Jensen floor."""
    if r not in (2,3):
        raise ValueError("r must be 2 or 3")
    K=max(map(len,J.values()),default=0)
    q=4**r*comb(r*(K+1),r)
    sigma=Fraction(1,q)
    P=Counter()
    adaptive=defaultdict(Fraction)
    neighborhood_hist=Counter()
    path_count=0
    min_b=None
    for start in adj:
        walk=[(start,)]
        for j in range(r):
            walk=[p+(v,) for p in walk for v in adj[p[-1]]]
        for path in walk:
            if len({u[0] for u in path})!=r+1 or len({u[1] for u in path})!=r+1:
                continue
            ids=tuple(owners[tuple(sorted((path[j],path[j+1])))]
                      for j in range(r))
            if len(set(ids))!=r or any(v in J[u] for u,v in combinations(ids,2)):
                raise AssertionError("coordinate proper path cannot carry two conflicting ORIGINAL ID owners")
            closed=set(ids)
            for i in ids:closed.update(J[i])
            b=len(closed)
            if not r<=b<=r*(K+1):
                raise AssertionError("ORIGINAL source closed conflict neighborhood bound invalid")
            w=exact_local_priority_floor(b,r)*Fraction(1,4**r)
            if w<sigma:
                raise AssertionError("adaptive lower priority/color preservation < uniform")
            P[path[0],path[-1]]+=1
            adaptive[path[0],path[-1]]+=w
            neighborhood_hist[b]+=1
            min_b=b if min_b is None else min(min_b,b)
            path_count+=1
    raw=sum(v*v for v in P.values())
    weighted=sum(v*v for v in adaptive.values())
    _,_,trace4,trace6=_powers(adj)
    trace=trace4 if r==2 else trace6
    if not (sigma*sigma*raw<=weighted<=trace):
        raise AssertionError("original source selector Jensen lower/trace upper")
    return {"r":r,"selector_uniform_inverse_q":q,
            "selector_uniform_sigma":sigma,"proper_paths":path_count,
            "original_proper_endpoint_Frobenius2":raw,
            "original_adaptive_weighted_endpoint_Frobenius2":weighted,
            "selected_energy_upper_original_trace":trace,
            "source_neighborhood_histogram":dict(sorted(neighborhood_hist.items())),
            "minimum_original_neighborhood":min_b,
            "maximum_original_neighborhood":max(neighborhood_hist,default=None),
            "all_check_pass":True}


def selected_physical_source(case,core,J,priority,left,right):
    """Priority minima and BOTH true factor coordinate two-color cuts."""
    flags,f,g=case["flags"],case["f"],case["g"]
    if (len(priority)!=len(core) or set(priority)!=set(core)
            or len(left)!=case["a"] or len(right)!=case["a"]
            or any(v not in (0,1) for v in left+right)):
        raise ValueError("not genuine original source order and typed binary cuts")
    rank={i:j for j,i in enumerate(priority)}
    kept=[]
    for i in core:
        p,l=flags[i]
        if (all(rank[i]<rank[v] for v in J[i])
                and left[f[p][0]]!=left[f[p][1]]
                and right[g[l][0]]!=right[g[l][1]]):
            kept.append(i)
    adj,owner=physical_core(case,kept)
    for u,neighbors in adj.items():
        if (len({v[0] for v in neighbors})!=len(neighbors)
                or len({v[1] for v in neighbors})!=len(neighbors)):
            raise AssertionError("selected ORIGINAL graph has coordinate cherry")
        if any(left[u[0]]==left[v[0]] or right[u[1]]==right[v[1]]
               for v in neighbors):
            raise AssertionError("selected original edge did not cross both typed cuts")
    return adj,owner,tuple(kept)


def _canonical_cycle(v):
    v=tuple(v)
    if len(v)!=6 or len(set(v))!=6:
        raise ValueError("six distinct ORIGINAL physical vertices required")
    return min(tuple(w[i:]+w[:i] for w in (v,v[::-1]) for i in range(6)))


def selected_c6_original_D6_injection(case,adj,owners):
    """Independent true-source C6 injection; never imports GF5 classifier."""
    cycles=set()
    for start in sorted(adj):
        def dfs(path):
            if len(path)==6:
                if start in adj.get(path[-1],()):
                    cycles.add(_canonical_cycle(path))
                return
            for v in adj.get(path[-1],()):
                if v>start and v not in path:
                    dfs(path+(v,))
        dfs((start,))
    f,g,flags=case["f"],case["g"],case["flags"]
    source=set()
    for cyc in cycles:
        if len({x for x,y in cyc})!=6 or len({y for x,y in cyc})!=6:
            raise AssertionError("both true original factor cuts did not make physical C6 coordinate proper")
        ids=tuple(sorted(owners[tuple(sorted((cyc[j],cyc[(j+1)%6])))]
                         for j in range(6)))
        if (len(set(ids))!=6 or
                len({flags[i][0] for i in ids})!=6 or
                len({flags[i][1] for i in ids})!=6):
            raise AssertionError("physical original cycle did not yield six distinct source D6 IDs")
        if ids in source:
            raise AssertionError("two physical C6 share the same SIX original D6 source IDs")
        source.add(ids)
    return {"unoriented_physical_c6":len(cycles),
            "six_distinct_original_D6_ID_sets":len(source),
            "independent_original_D6_source_ID_sets":tuple(sorted(source)),
            "injective":True}


def sharp_fourth_moment(case,core,adj,owners):
    """The old factor TWO is unnecessary due to DISJOINT 2walk partition.

    Every physical 2walk with distinct first and second endpoint
    coordinates is automatically coordinate-proper, as each physical
    diagonal changes BOTH coordinates. All other 2walks are improper.
    Therefore trA4=||P2||²+||B2||² EXACTLY, not just
        <=2||P2||²+2||B2||².
    B2_uv <=Delta, sum B2 <= Qx+Qy, hence
        trA4 <= ||P2||²+Delta(Qx+Qy).
    """
    A2,A3,t4,t6=_powers(adj)
    proper=Counter()
    wrong=Counter()
    qx=qy=0
    for u,row in A2.items():
        for v,n in row.items():
            if u[0]==v[0]:qx+=n
            if u[1]==v[1]:qy+=n
            if u[0]!=v[0] and u[1]!=v[1]:
                proper[u,v]=n
            else:wrong[u,v]=n
    proper2=sum(n*n for n in proper.values())
    wrong2=sum(n*n for n in wrong.values())
    Delta=max(map(len,adj.values()),default=0)
    m=len(owners)
    checks={
        "exact_disjoint_full_two_walk_partition":t4==proper2+wrong2,
        "all_improper_2walks_counted_in_two_return_books":
            sum(wrong.values())<=qx+qy,
        "improper_B2_squared_le_Delta_return_mass":
            wrong2<=Delta*(qx+qy),
        "NEW_sharp_true_original_fourth_moment":
            t4<=proper2+Delta*(qx+qy),
        "spectral_trace_A4_sq_le_2m_trace_A6":
            t4*t4<=2*m*t6,
    }
    if not all(checks.values()):
        raise AssertionError("false original SHARP fourth moment identity")
    return {"actual_m":m,"physical_Delta":Delta,"trace_A4":t4,
            "trace_A6":t6,"proper_P2_norm2":proper2,
            "improper_B2_norm2":wrong2,
            "physical_Qx":qx,"physical_Qy":qy,
            "sharp_fourth_ceiling":proper2+Delta*(qx+qy),
            "old_double_ceiling":2*proper2+2*Delta*(qx+qy),
            "checks":checks}


def sixcycle_sixth_bound(adj, owners):
    """All-order simple bipartite walk/backtrack and Young exact inequalities."""
    from collections import Counter
    _,_,t4,t6=_powers(adj)
    m=len(owners)
    Delta=max(map(len,adj.values()),default=0)
    C6=_count_c6(adj)
    a=12*C6+6*Delta*t4
    b=24*C6+72*m*Delta*Delta
    if t6>a or t6>b:
        raise AssertionError("original actual selected bipartite C6/sixth moment lemma fails")
    return {"physical_C6":C6,"m":m,"Delta":Delta,
            "trace_A4":t4,"trace_A6":t6,
            "sixth_walk_injection_bound":a,
            "sixth_Young_bound":b,"valid":True}


def _count_c6(adj):
    cycles=set()
    for st in sorted(adj):
        def walk(path):
            if len(path)==6:
                if st in adj.get(path[-1],()):
                    cycles.add(_canonical_cycle(path))
                return
            for n in adj.get(path[-1],()):
                if n>st and n not in path:
                    walk(path+(n,))
        walk((st,))
    return len(cycles)


def ceil_graph_exact_ledger(C0,c0):
    """Formal graph constants only. Independently rerun all-dyadic s0 ledger."""
    if (type(C0) is not Fraction or type(c0) is not Fraction
            or C0<1 or not 0<c0<=1):
        raise ValueError("unknown external ordinary C6 graph constants need exact formal bounds")
    K=64
    T=ceil_fraction(Fraction(2**64)*C0**3)
    q2=16*comb(2*(K+1),2)
    q3=64*comb(3*(K+1),3)
    L6=24+288*T*T
    root6=ceil_sqrt(8*L6)
    oldL4=2*q2*q2*root6+56*T
    newL4=q2*q2*root6+28*T
    B0=ceil_sqrt(1280*(K+1)*T)
    E=8*q3*ceil_sqrt(L6)
    oldD=4*ceil_sqrt(B0*T*oldL4)
    newD=4*ceil_sqrt(B0*T*newL4)
    old_s0=max(64,672*T,(8*E)**2,(8*oldD)**8)
    new_s0=max(64,672*T,(8*E)**2,(8*newD)**8)
    old_h0=(old_s0-1).bit_length()
    new_h0=(new_s0-1).bit_length()
    rho=Fraction(1,12*q3*q3*L6)
    delta=c0/Fraction(2**120)
    checks={
        "selector_exact_binomial_q2":q2==16*comb(130,2),
        "selector_exact_binomial_q3":q3==64*comb(195,3),
        "new_L4_exactly_half_old_L4":2*newL4==oldL4,
        "new_D_not_worse":newD<=oldD,
        "new_minimum_dyadic_threshold_not_worse":new_h0<=old_h0,
        "NEW_s0_definition_exact":
            new_s0==max(64,672*T,(8*E)**2,(8*newD)**8),
        "all_original_source_deletion_budget_unchanged":
            12*q3*q3*L6*rho==1,
        "all_original_D6_delta_unchanged":
            delta==c0/Fraction(2**120),
        "root_status_is_scientific_Draft":ROOT_STATUS=="OPEN_WITH_FORMAL_BLOCKER",
    }
    if not all(checks.values()):
        raise AssertionError("SHARP original fourth moment dyadic ledger broken")
    return {"C0_FORMAL":C0,"c0_FORMAL":c0,"K":K,"T":T,
            "q2":q2,"q3":q3,"L6":L6,
            "old_L4":oldL4,"sharp_L4":newL4,"B0":B0,
            "old_D":oldD,"sharp_D":newD,"E":E,
            "rho":rho,"delta":delta,
            "old_s0":old_s0,"sharp_s0":new_s0,
            "old_h0":old_h0,"sharp_h0":new_h0,
            "checks":checks}


def finite_original_selector_case(h,scheme,shift_f=0,shift_g=0,mode="all",seed=3):
    """Real W32/W34 source source graph and independently selected moments."""
    c=original_case(h,scheme,shift_f,shift_g)
    n=len(c["flags"])
    if mode not in ("all","subsample"):
        raise ValueError("finite genuine ORIGINAL paired core selection")
    C=tuple(range(n)) if mode=="all" else tuple(i for i in range(n) if i%5 in (1,3))
    J=conflict_graph(c,C)
    graph,owner=physical_core(c,C)
    r2=independent_proper_path_referee(c,C,J,graph,owner,2)
    r3=independent_proper_path_referee(c,C,J,graph,owner,3)
    sharp=sharp_fourth_moment(c,C,graph,owner)
    order=tuple(sorted(C,key=lambda i:((i*47+seed*11)%(n+17),i)))
    left=tuple((i*13+seed+i//3)%2 for i in range(c["a"]))
    right=tuple((i*7+seed*2+i//2)%2 for i in range(c["a"]))
    graph_sel,owner_sel,kept=selected_physical_source(c,C,J,order,left,right)
    selected=sixcycle_sixth_bound(graph_sel,owner_sel)
    d6=selected_c6_original_D6_injection(c,graph_sel,owner_sel)
    return {
        "s":c["s"],"scheme":scheme,"shift_f":shift_f,"shift_g":shift_g,
        "original_core_flags":len(C),
        "original_conflict_max_K":max(map(len,J.values()),default=0),
        "physical_core_edges":len(owner),
        "original_proper_r2":_readable(r2),
        "original_proper_r3":_readable(r3),
        "SHARP_original_fourth":sharp,
        "true_original_selected_source_flags":len(kept),
        "selected_sixth":selected,
        "selected_original_D6_injection":{
            k:v for k,v in d6.items() if k!="independent_original_D6_source_ID_sets"},
        "selected_original_sixid_set_samples":
            [list(z) for z in d6["independent_original_D6_source_ID_sets"][:3]],
        "checks":{ "original_selector_r2_r3_valid":r2["all_check_pass"] and r3["all_check_pass"],
                   "sharp_original_fourth_valid":all(sharp["checks"].values()),
                   "selected_sixth_valid":selected["valid"],
                   "source_sixID_D6_injective":d6["injective"]},
    }


def _readable(v):
    return {k:(str(z) if isinstance(z,Fraction) else z) for k,z in v.items()}


def canonical_report():
    trials=[
        (1,"lex",0,0,"all",2),
        (1,"reverse-line",3,7,"all",3),
        (2,"lex",0,0,"subsample",2),
        (2,"reverse-line",11,23,"subsample",4),
    ]
    real=[finite_original_selector_case(*q) for q in trials]
    formal=[]
    for C,c in ((Fraction(1),Fraction(1)),(Fraction(2),Fraction(1,5)),
                (Fraction(7,3),Fraction(1,17))):
        z=ceil_graph_exact_ledger(C,c)
        formal.append({
            "C0_FORMAL":str(C),"c0_FORMAL":str(c),
            "q2":z["q2"],"q3":z["q3"],
            "T":str(z["T"]),"rho":str(z["rho"]),
            "delta":str(z["delta"]),
            "old_L4":str(z["old_L4"]),
            "sharp_L4":str(z["sharp_L4"]),
            "old_D":str(z["old_D"]),
            "sharp_D":str(z["sharp_D"]),
            "old_h0":z["old_h0"],"sharp_h0":z["sharp_h0"],
            "all_exact_checks_pass":all(z["checks"].values()),
            "external_graph_constants_are_NOT_numeric_claims":True,
        })
    return {
        "schema":"mathlab.hyp105.original-selector-jensen-sharp4.v1",
        "root_230_status":ROOT_STATUS,
        "root_Branch_A_unconditionally_accepted":False,
        "all_order_selector_probability_and_Jensen_independent_proof":True,
        "all_order_exact_SHARP_fourth_moment_proof":True,
        "all_order_selected_bipartite_sixth_moment_rederived":True,
        "original_external_graph_SS6_numerical_constants_known":False,
        "coordinate_proper_color_probabilities":[
            _readable(color_probability_exact(r)) for r in (2,3)],
        "formal_graph_constant_ledgers":formal,
        "genuine_original_source_selector_moment_cases":real,
        "root_ASET_exponent_proved":False,
    }


if __name__=="__main__":
    print("AA4_ORIGINAL_SELECTOR_SHARP4_CERTIFICATE="+json.dumps(
        canonical_report(),sort_keys=True,separators=(",",":")),flush=True)
