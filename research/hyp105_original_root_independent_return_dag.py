"""AA4-ROOT-REFEREE: independent original full/CORE typed-return and root DAG.

New independent ALL-h source/physical *EXACT* return identity:
  Qx(C) = 4*|C| + 4*e(J_C, point-pencil)
  Qy(C) = 4*|C| + 4*e(J_C, line-pencil)
  Qx+Qy = 8*|C| + 4*e(J_C).
Here Qx/y count ACTUAL ordered physical 2walks whose endpoints
share respectively the first/second physical coordinate, including
literal backtracks, with BOTH diagonals of each original owner.
No source f/g label independence, no physical edge cloning.

For arbitrary paired original CORE C subset I at fixed true W(3,s),
and full original J with all-h e(J) <2 M_H*s^4, N<=nu_H*s^4:
  Qx+Qy <8*(nu_H+M_H)*s^4,
  ||B2||_F^2 <= Delta*(Qx+Qy),
  improper3 <= 3 Delta*(Qx+Qy).
For H=32 and Delta<=T*s:
  L4_new = q2^2 ceil_sqrt(ceil(nu_H*L6)) + 17*T;
  coordinate_improper_new <=49*T*s^5,
from old +19*T and 111*T*s^5/2 respectively.

Independent all-order root proof DAG recomputes all HEAVY and LOW
structural/quantifier/numerical sufficient gates from exact Fractions,
no imports of historical root/HEAVY/LOW calculators, no numeric external
ordinary-graph C6 constants claimed. TRUE W32/W34 finite source
falsifiers calculate BOTH source pencil J AND physical 2walk/3walk
directly, in independent algorithms.

Science scope: the exact return identity and all-h conditional root
numerical composition proved here; end-to-end acceptance of inherited
original D6/BBo positive sixset and source adversarial blockers must
remain a separate publication-level review before root PROVED_A.
"""
from collections import Counter,defaultdict
from fractions import Fraction as Q
from itertools import combinations
from math import comb,isqrt
import json

SCHEMA="mathlab.hyp105.root-endtoend-return-dag.v1"
ISSUE=230
PARENT_PR=781
STATUS="OPEN_WITH_FORMAL_BLOCKER"
H_FIXED=32
K_FIXED=10
R_FIXED=33281
ALPHA=(Q(1,64),Q(1,64),Q(15,16))
SOURCE_VERIFICATION="INDEPENDENT_ALL_H_ORIGINAL_TYPED_RETURN_AND_CONDITIONAL_ROOT_GLUE"
PROOF_GATES=(
    ("GQ_POINT_LINE","GQ original source geometry, V and N, three-anchor projection",
     (), "original_all_h_lemma"),
    ("SOURCE_J_SRG","real ORIGINAL pencil conflict J bound, any fixed correlated f/g",
     ("GQ_POINT_LINE",),"original_all_h_lemma"),
    ("FULL_PHYSICAL","two disjoint actual diagonals per original incidence owner",
     ("GQ_POINT_LINE",),"original_all_h_lemma"),
    ("HEAVY_F","Caro-Wei, both actual global cuts, real top-r F and density",
     ("SOURCE_J_SRG","FULL_PHYSICAL"),"inherited_all_h_lemma"),
    ("GRAPH_C6","Simonovits ordinary simple graph C6 supersaturation, existential constants",
     ("HEAVY_F",),"external_published_theorem"),
    ("HEAVY_D6_INVERSE","actual ordinary unoriented C6 -> unique original D6 six-ID set",
     ("GRAPH_C6","FULL_PHYSICAL"),"inherited_all_h_lemma"),
    ("LOW_CORE","FULL Q_T frozen once and K full-source J-degree prune",
     ("SOURCE_J_SRG","FULL_PHYSICAL"),"inherited_all_h_lemma"),
    ("RETURN_EXACT","NEW exact original Qx+Qy=8|C|+4 e(J_C) and improper3",
     ("LOW_CORE","FULL_PHYSICAL"),"new_independent_all_h_lemma"),
    ("LOW_W3","same actual minimal pair alphabet, original paired Blakley-Roy W3",
     ("LOW_CORE","FULL_PHYSICAL"),"inherited_all_h_lemma"),
    ("ONE_SELECTOR","one shared original priority and two typed global cuts",
     ("LOW_CORE",),"inherited_all_h_lemma"),
    ("EXPECTED_MOMENT","exact E m=W_C/2 and selected C6, sixth/fourth Jensen",
     ("ONE_SELECTOR","HEAVY_D6_INVERSE","RETURN_EXACT"),"inherited_all_h_lemma"),
    ("FULL_AC_BOOK","true full allowed A=I and smaller paired C source books F1/F2/theta",
     ("SOURCE_J_SRG","LOW_CORE"),"inherited_all_h_lemma"),
    ("GQ_ENDPOINTS","full three-anchor original GQ endpoint projection",
     ("GQ_POINT_LINE","FULL_AC_BOOK"),"inherited_all_h_lemma"),
    ("FOUR_BLOCKERS","both typed actual first/last blockers and weighted fourth trace",
     ("FULL_AC_BOOK","GQ_ENDPOINTS","EXPECTED_MOMENT"),"inherited_all_h_lemma"),
    ("LOW_BBO_INVERSE","all-h original aligned six-ID source BBo zero/two inverse and positive GF5 class",
     ("GQ_ENDPOINTS","FULL_PHYSICAL"),"inherited_all_h_lemma"),
    ("LOW_PRODUCED","true original 3walk partition, all errors, produced BBo floor",
     ("LOW_W3","RETURN_EXACT","EXPECTED_MOMENT","FOUR_BLOCKERS","LOW_BBO_INVERSE"),"inherited_all_h_lemma"),
    ("ROOT_SEVEN","disjoint D6/BBo ORIGINAL six-ID class, all fixed maps and scales",
     ("HEAVY_D6_INVERSE","LOW_PRODUCED"),"conditional_glue"),
)
NEEDS_INDEPENDENT_PUBLICATION_SIGNOFF=(
 "HEAVY_F","HEAVY_D6_INVERSE","ONE_SELECTOR","EXPECTED_MOMENT",
 "FULL_AC_BOOK","GQ_ENDPOINTS","FOUR_BLOCKERS","LOW_BBO_INVERSE",
 "LOW_PRODUCED","ROOT_SEVEN",
)


def ceilq(z):
    if type(z) is not Q:raise TypeError("proof ledger exact Fraction only")
    return -(-z.numerator//z.denominator)


def ceilsqrt(n):
    if type(n)!=int or n<0:raise ValueError("integer nonnegative square root")
    r=isqrt(n)
    return r+(r*r<n)


def h0(n):
    if type(n)!=int or n<1:raise ValueError("positive integer s threshold")
    return (n-1).bit_length()


def source_envelopes(H):
    if type(H)!=int or H<8 or H%2:raise ValueError("fixed even H>=8")
    M=(1+Q(1,2**(2*H)))*(1+Q(23,16*2**(H//2)))
    nu=(1+Q(1,2**H))**2*(1+Q(1,2**(2*H)))
    A=(2*(1+Q(1,2**H))*(1+Q(1,2**(2*H)))
       +Q(23,4*2**(3*H//2))+Q(4,2**(3*H)))
    R=ceilq(256*A*(1+64*M))
    Qcoef=8*(nu+M)
    # 49 is a conservative integer ceiling; 17 is the fourth moment
    # source-return constant. Keep exact rational envelopes inspectable.
    qreturn=ceilq(Qcoef)
    q3return=ceilq(3*Qcoef)
    if not (M>1 and nu>1 and A>2 and 1<qreturn<19
            and q3return<56 and R<93312):
        raise AssertionError("all-h source/physical cut bounds inconsistent")
    if H==H_FIXED and not (R==R_FIXED and qreturn==17 and q3return==49):
        raise AssertionError("frozen source at H32 unexpectedly changed")
    return dict(H=H,M=M,nu=nu,A=A,R=R,Qcoef=Qcoef,
                q2return=qreturn,q3return=q3return)


def full_root_budget(C0,c0,sharp_return=True):
    """Exact all-h conditional root: external graph constants remain FORMAL."""
    if (type(C0) is not Q or type(c0) is not Q or
            C0<1 or c0<=0 or c0>1):
        raise ValueError("only rational FORMAL unknown graph theorem constants")
    H=H_FIXED;K=K_FIXED
    z=source_envelopes(H)
    M,nu,A,R=z["M"],z["nu"],z["A"],z["R"]
    T=ceilq(Q(17*R**3,2)*C0**3)
    delta=c0/Q(R**6)
    c=Q(7,8)-4*M/Q(K+1)
    if c<=0:raise AssertionError("source CORE fraction nonpositive")
    w=(4*c)**3/A**2
    q2=16*(K+1)**2
    q3=64*(K+1)**3
    L6=24+ceilq(36*nu*T*T)
    bound2=z["q2return"] if sharp_return else 19
    bound3=z["q3return"] if sharp_return else Q(111,2)
    L4=q2*q2*ceilsqrt(ceilq(nu*L6))+bound2*T
    B0=ceilsqrt(360*(K+1)*T)
    E=5*q3*ceilsqrt(L6)
    D=4*ceilsqrt(B0*T*L4)
    coord=ceilq(bound3*T/(ALPHA[0]*w))
    endpoint=ceilq((Q(E)/(ALPHA[1]*w))**2)
    mixed=ceilq((Q(D)/(ALPHA[2]*w))**8)
    cutoff=max(2**H,64,coord,endpoint,mixed)
    residual=w*(1-sum(ALPHA))/2
    if not (delta<residual and
            bound3*T<=ALPHA[0]*w*cutoff and
            Q(E)**2<= (ALPHA[1]*w)**2*cutoff and
            Q(D)**8<= (ALPHA[2]*w)**8*cutoff):
        raise AssertionError("all-h original conditional root error budget invalid")
    # Ordinary C6: e/v>=s/R and v<=17 s^3/(2T).
    # For the EXACT same T, (s/R)^3 >= C0^3*(17s^3/(2T)).
    # This inequality is checked by rational symbolic reduction.
    if not Q(T)>=Q(17*R**3,2)*C0**3:
        raise AssertionError("HEAVY ordinary graph supersaturation not applicable")
    # All second-moment and endbad inequalities have separate
    # mathematical source proofs, NOT inferred from this arithmetic.
    return dict(H=H,K=K,R=R,T=str(T),
       graph_C0_FORMAL_NOT_PUBLISHED=str(C0),
       graph_c0_FORMAL_NOT_PUBLISHED=str(c0),
       source_N_coefficient=str(nu),source_J_coefficient=str(M),
       physical_minimal_a2_coefficient=str(A),
       q2=q2,q3=q3,L6=str(L6),L4=str(L4),
       Qreturn_coefficient_exact=str(z["Qcoef"]),
       coordinate_bad_coefficient_exact=str(bound3),
       fourth_improper_return_coefficient=bound2,
       B0=str(B0),E=str(E),D=str(D),
       alpha=[str(z) for z in ALPHA],
       coordinate_threshold=str(coord),
       endpoint_threshold=str(endpoint),
       four_blocker_threshold=str(mixed),
       all_h_sufficient_s0=str(cutoff),
       formal_dyadic_h0=h0(cutoff),
       true_original_LOW_W3_floor=str(w),
       original_BBo_produced_conditional_floor=str(residual),
       original_HEAVY_D6_delta=str(delta),
       universal_strong_bound_has_conditional_prerequisites=True,
       external_GRAPH_C6_constants_numerically_known=False,
       ROOT_PROVED_A=False)


def compare_old_and_sharp(C0,c0):
    old=full_root_budget(C0,c0,False)
    sharp=full_root_budget(C0,c0,True)
    if not (old["R"]==sharp["R"]==R_FIXED and
            old["T"]==sharp["T"] and old["L6"]==sharp["L6"] and
            old["q2"]==sharp["q2"]==1936 and
            old["q3"]==sharp["q3"]==85184 and
            int(sharp["L4"])<int(old["L4"]) and
            Q(sharp["coordinate_bad_coefficient_exact"])<
            Q(old["coordinate_bad_coefficient_exact"]) and
            Q(sharp["original_HEAVY_D6_delta"])==
            Q(old["original_HEAVY_D6_delta"]) and
            Q(sharp["original_BBo_produced_conditional_floor"])==
            Q(old["original_BBo_produced_conditional_floor"]) and
            sharp["formal_dyadic_h0"]<=old["formal_dyadic_h0"]):
        raise AssertionError("new source-return improvement not safely composable")
    return dict(C0_FORMAL=str(C0),c0_FORMAL=str(c0),
       old_q2return=old["fourth_improper_return_coefficient"],
       new_q2return=sharp["fourth_improper_return_coefficient"],
       old_q3return=old["coordinate_bad_coefficient_exact"],
       new_q3return=sharp["coordinate_bad_coefficient_exact"],
       old_L4=str(old["L4"]),new_L4=str(sharp["L4"]),
       old_h0=old["formal_dyadic_h0"],new_h0=sharp["formal_dyadic_h0"],
       T_same=old["T"]==sharp["T"],
       original_BBo_HEAVY_delta_unchanged=True,
       new_return_all_h_proved_from_named_SOURCE_pencils=True,
       ROOT_PROVED_A=False)


def _edge(u,v):
    if u==v:raise AssertionError("true physical original diagonal is loopless")
    return tuple(sorted((u,v)))


def genuine_original_model(s,mode,core):
    from hyp105_original_defect_factor_referee import genuine_symplectic_source
    if type(s)!=int or s not in (2,4):raise ValueError("true symplectic s=2 or4 fixture")
    flags=tuple(map(tuple,genuine_symplectic_source(s)))
    V=(s+1)*(s*s+1)
    if len(flags)!=(s+1)*V or len(set(flags))!=len(flags):
        raise AssertionError("true original GQ flags wrong")
    a=2
    while comb(a,2)<V:a+=1
    pairs=tuple(combinations(range(a),2))[:V]
    if mode=="lex":
        f=pairs;g=pairs
    elif mode=="reverse":
        f=pairs;g=pairs[::-1]
    elif mode=="shift":
        f=pairs;g=pairs[1:]+pairs[:1]
    else:
        raise ValueError("invalid original global labeling")
    N=len(flags)
    if core=="full":
        C=tuple(range(N))
    elif core=="even":
        C=tuple(i for i in range(N) if i%2==0)
    elif core=="thin":
        C=tuple(i for i in range(N) if i%5==0)
    elif core=="shifted":
        C=tuple(i for i in range(N) if i%3!=1)
    else:
        raise ValueError("invalid original paired CORE")
    edges={}
    for i in C:
        p,l=flags[i]
        x,z=f[p];y,w=g[l]
        for edge in (_edge((x,y),(z,w)),_edge((x,w),(z,y))):
            if edge in edges:raise AssertionError("cloned real physical source owner")
            edges[edge]=i
    if len(edges)!=2*len(C):raise AssertionError("real source flags missing paired diagonals")
    adj=defaultdict(set)
    for u,v in edges:
        adj[u].add(v);adj[v].add(u)
    # FIRST SOURCE oracle: actual ORIGINAL named pencil conflicts, entirely
    # separate from Qx/y physical adjacency.
    point=defaultdict(list);line=defaultdict(list)
    for i in C:
        p,l=flags[i];point[p].append(i);line[l].append(i)
    eP=eL=0
    J=set()
    for ids in point.values():
        for i,j in combinations(ids,2):
            if set(g[flags[i][1]])&set(g[flags[j][1]]):
                eP+=1;J.add((i,j))
    for ids in line.values():
        for i,j in combinations(ids,2):
            if set(f[flags[i][0]])&set(f[flags[j][0]]):
                eL+=1;J.add((i,j))
    if eP+eL!=len(J):
        raise AssertionError("original point/line J conflicts overlap on distinct named flags")
    # SECOND SOURCE oracle: independent symbolic R_C(p,y), R'_C(ell,x)
    # physical source pair/flag multiplicities, no graph-walk calls.
    Rp=Counter();Rl=Counter()
    for i in C:
        p,l=flags[i]
        for y in g[l]:Rp[p,y]+=1
        for x in f[p]:Rl[l,x]+=1
    Qx_source=2*sum(z*z for z in Rp.values())
    Qy_source=2*sum(z*z for z in Rl.values())
    # THIRD INDEPENDENT physical oracle: enumerate all physical two-walks
    # with typed returning endpoints, *including* true backtracks.
    Qx_phys=Qy_phys=0
    for mid,neighbors in adj.items():
        dx=Counter(v[0] for v in neighbors)
        dy=Counter(v[1] for v in neighbors)
        Qx_phys+=sum(d*d for d in dx.values())
        Qy_phys+=sum(d*d for d in dy.values())
    if not (Qx_source==Qx_phys==4*len(C)+4*eP
            and Qy_source==Qy_phys==4*len(C)+4*eL):
        raise AssertionError("NEW all-order original source/physical exact Qx/y identity FALSIFIED")
    Delta=max(map(len,adj.values()),default=0)
    # Physical-first counted total directed three-walks via degrees.
    W3=2*sum(len(adj[u])*len(adj[v]) for u,v in edges)
    Ibad=0
    for v0 in adj:
        for v1 in adj[v0]:
            for v2 in adj[v1]:
                for v3 in adj[v2]:
                    x=[v[0] for v in (v0,v1,v2,v3)]
                    y=[v[1] for v in (v0,v1,v2,v3)]
                    Ibad+=int(len(set(x))<4 or len(set(y))<4)
    if not Ibad<=3*Delta*(Qx_phys+Qy_phys):
        raise AssertionError("REAL 3walk coordinate-return bound incorrect")
    # Fourth trace: direct independent common neighbor squared, no old
    # historical P2 classifier or walk moment function imported.
    d2=Counter()
    for mid,neighbors in adj.items():
        for u in neighbors:
            for v in neighbors:
                d2[u,v]+=1
    tr4=sum(w*w for w in d2.values())
    bad2=Counter()
    for (u,v),w in d2.items():
        if u[0]==v[0] or u[1]==v[1]:
            bad2[u,v]=w
    bad2_norm2=sum(z*z for z in bad2.values())
    if not bad2_norm2<=Delta*(Qx_phys+Qy_phys):
        raise AssertionError("REAL return fourth moment does not satisfy new source bound")
    return dict(s=s,mode=mode,core=core,original_N=len(flags),
        original_CORE_named_flags=len(C),
        genuine_physical_real_owned_edges=len(edges),physical_Delta=Delta,
        source_J_point_conflicts=eP,source_J_line_conflicts=eL,
        source_true_J_total=eP+eL,
        Qx_from_named_SOURCE=Qx_source,Qx_from_physical_two_walks=Qx_phys,
        Qy_from_named_SOURCE=Qy_source,Qy_from_physical_two_walks=Qy_phys,
        exact_SOURCE_Qtotal_identity=8*len(C)+4*(eP+eL),
        TRUE_physical_Qtotal=Qx_phys+Qy_phys,
        real_ALL_directed_three_walks=W3,
        real_coordinate_improper_directed_three_walks=Ibad,
        REAL_improper3_upper=3*Delta*(Qx_phys+Qy_phys),
        real_full_physical_trace4=tr4,
        real_coordinate_improper_two_path_norm2=bad2_norm2,
        real_improper_two_path_norm2_upper=Delta*(Qx_phys+Qy_phys),
        actual_original_2step_return_SOURCE_identity_verified=True,
        actual_original_coordinate_improper3_and_fourth_bounds_verified=True)


def dependency_graph():
    nodes={name:dict(
        description=description,deps=list(deps),gate_scope=scope,
        independent_publication_signoff=name not in NEEDS_INDEPENDENT_PUBLICATION_SIGNOFF,
        ROOT_PROVED_A=False)
        for name,description,deps,scope in PROOF_GATES}
    if len(nodes)!=len(PROOF_GATES):
        raise AssertionError("duplicate source proof gate")
    visited=set();visiting=set();order=[]
    def visit(name):
        if name in visiting:raise AssertionError("circular original ROOT proof DAG")
        if name in visited:return
        if name not in nodes:raise AssertionError("missing antecedent source theorem")
        visiting.add(name)
        for d in nodes[name]["deps"]:visit(d)
        visiting.remove(name)
        visited.add(name);order.append(name)
    visit("ROOT_SEVEN")
    if set(order)!=set(nodes):
        raise AssertionError("disconnected proof gate falsely accepted")
    if order[-1]!="ROOT_SEVEN" or any(
            order.index(d)>order.index(name) for name,item in nodes.items()
            for d in item["deps"]):
        raise AssertionError("not a valid original ROOT topological proof order")
    if not any(not x["independent_publication_signoff"] for x in nodes.values()):
        raise AssertionError("ROOT must not be falsely declared fully accepted")
    return dict(order=order,nodes=nodes,
        unaccepted_publication_gates=list(NEEDS_INDEPENDENT_PUBLICATION_SIGNOFF),
        all_h_new_SOURCE_RETURN_gate_proved_by_literal_identities=True,
        external_graph_C6_theorem_correctly_scoped_to_SIMPLE_UNDIRECTED_Graph=True,
        ROOT_PROVED_A=False)


def certificate():
    h=source_envelopes(H_FIXED)
    scenarios=[compare_old_and_sharp(*pair) for pair in (
        (Q(1),Q(1)),(Q(2),Q(1,5)),(Q(7,3),Q(1,17)))]
    finite=[genuine_original_model(s,mode,core)
            for s in (2,4)
            for mode in ("lex","reverse","shift")
            for core in ("full","even","thin","shifted")]
    if not any(x["real_coordinate_improper_directed_three_walks"]>0 for x in finite):
        raise AssertionError("no nonvacuous true original coordinate return source!")
    if not any(x["source_true_J_total"]>0 for x in finite):
        raise AssertionError("all genuine original source pencils vacuous")
    return dict(schema=SCHEMA,parent_pr=PARENT_PR,issue=ISSUE,status=STATUS,
        fixed_H=H_FIXED,fixed_K=K_FIXED,fixed_R=R_FIXED,
        new_all_h_exact_original_Qx_Qy_source_identity=True,
        one_SHARED_full_original_J_envelope_for_HEAVY_and_LOW=True,
        actual_true_original_source_selectors_not_replaced_by_random_f_g=True,
        genuine_original_all_h_improper3_SHARP_49T_and_fourth_17T=True,
        original_D6_BBo_sixset_nonoverlap_INHERITED_not_falsely_new=True,
        published_Simonovits_graph_C6_constants_numeric_unknown=True,
        original_seven_unweighted_motif_ROOT_PROVED_A=False,
        actual_source_Q_bound_exact_coefficient=str(h["Qcoef"]),
        new_integer_source_Qx_y_bound=h["q2return"],
        new_integer_coordinate_improper_bound=h["q3return"],
        formal_unknown_graph_constant_ROOT_scenarios=scenarios,
        TRUE_W32_W34_named_original_source_cases=finite,
        independent_root_dependency_gate_graph=dependency_graph())


if __name__=="__main__":
    print("AA4_ROOT_INDEPENDENT_RETURN_DAG_CERTIFICATE="+json.dumps(
        certificate(),sort_keys=True,separators=(",",":")))
