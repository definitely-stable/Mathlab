"""AA4-ROOT-ENDTOEND: a mathematically independent K-free Z=empty Branch A budget.

This script checks exact algebra and independently reconstructs true ORIGINAL
W(3,2)/W(3,4) flags, J conflicts and physical core/walk identities. It does
NOT claim to machine-prove the separately inherited all-h low/high lemmas,
original six-ID inverses, or ordinary C6 supersaturation. Root issue #230
remains OPEN_WITH_FORMAL_BLOCKER.

NEW: a deterministic K>=5 high-J pruning + adjustable LOW-error allocations
instead of the inherited arbitrary K=64 and uniform s^6/8 budgets. Combine
with the ALL-ORDER Harris selector q_r=4^r(K+1)^r from predecessor #771.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb,isqrt
import json

SCHEMA="mathlab.hyp105.root-endtoend-kfree-optimized.v1"
STATUS="OPEN_WITH_FORMAL_BLOCKER"
R_Z0=93312
K_OLD=64
K_NEW=11
ERROR_ALLOC=(Fraction(1,64),Fraction(1,64),Fraction(15,16))
EXTERNAL_GRAPH_CONSTANTS_NUMERICALLY_UNKNOWN=True

def _ceil(q):
    if not isinstance(q,Fraction):
        raise TypeError("exact Fraction required")
    return -(-q.numerator//q.denominator)

def _ceil_sqrt(n):
    if type(n) is not int or n<0:
        raise ValueError("nonnegative exact integer required")
    x=isqrt(n)
    return x+(x*x<n)

def _dyadic_h(s0):
    if type(s0) is not int or s0<1:
        raise ValueError("positive integer s0 required")
    return (s0-1).bit_length()

def _fraction(x):
    return [x.numerator,x.denominator]

def normalized_constant_inputs(C0,c0):
    if not isinstance(C0,Fraction) or not isinstance(c0,Fraction):
        raise TypeError("exact formal fractions required")
    if C0<1 or not 0<c0<=1:
        raise ValueError("formal existential C0>=1 and 0<c0<=1")
    return C0,c0

def _energy_budget(K,C0,c0,errors=ERROR_ALLOC):
    """Exact root Z0 inequalities parametrized by a genuine J cap K.

    All-h proof logic: e(J)<=5s^4/2; deleting FULL J-degree >K
    removes <=5s^4/(K+1) distinct ORIGINAL source owners. Removing
    actual Q_T touching source owners removes <s^4/8. No Z.
    """
    normalized_constant_inputs(C0,c0)
    if type(K) is not int or K<5:
        raise ValueError("original LOW core positive only for K>=5 under the all-h J bound")
    if (not isinstance(errors,(tuple,list)) or len(errors)!=3
            or any(not isinstance(x,Fraction) or x<=0 for x in errors)
            or sum(errors)>=1):
        raise ValueError("three positive exact LOW error fractions sum <1 required")
    c=Fraction(7,8)-Fraction(5,K+1)
    if c<=0:
        raise AssertionError("pruning loses every source owner")
    # True physical graph: n=a^2<=9s^3/4, m=2|C|.
    walk=Fraction(16,81)*(4*c)**3
    # A heavy physical edge belongs to one actual ORIGINAL owner.
    # R_Z0 and T are exactly the inherited source no-clone HEAVY theorem.
    T=_ceil(Fraction(17*R_Z0**3,2)*C0**3)
    delta=c0/Fraction(R_Z0**6)
    L6=24+153*T*T
    q2=16*(K+1)**2
    q3=64*(K+1)**3
    L4=q2*q2*_ceil_sqrt(_ceil(Fraction(17*L6,4)))+19*T
    B0=_ceil_sqrt(360*(K+1)*T)
    E=5*q3*_ceil_sqrt(L6)
    D=4*_ceil_sqrt(B0*T*L4)
    a_coord,a_endpoint,a_blocker=errors
    # Coordinate improper <= (111/2)T s^5
    # Original endpoint error <= E s^(11/2)
    # Four real ORIGINAL blocker union <= D s^(47/8).
    coord_s=_ceil(Fraction(111*T,2)/(a_coord*walk))
    endpoint_s=_ceil((Fraction(E)/(a_endpoint*walk))**2)
    blocker_s=_ceil((Fraction(D)/(a_blocker*walk))**8)
    s0=max(64,coord_s,endpoint_s,blocker_s)
    residue=walk*(1-sum(errors))
    bbo=residue/2
    if not bbo>=delta:
        raise AssertionError("root LOW has inadequate source BBo floor for HEAVY delta")
    # Exact inequalities at the sufficient cutoff s0; no floating sqrt.
    if Fraction(111*T,2)>a_coord*walk*s0:
        raise AssertionError("physical coordinate-return envelope wrong")
    if Fraction(E**2)>(a_endpoint*walk)**2*s0:
        raise AssertionError("FULL original endpoint error envelope wrong")
    if Fraction(D**8)>(a_blocker*walk)**8*s0:
        raise AssertionError("mixed source Cauchy four-blocker envelope wrong")
    if not Fraction(5,K+1)<Fraction(7,8):
        raise AssertionError("K choice fails physical core positivity")
    if not Fraction(1,R_Z0**6)<bbo:
        raise AssertionError("Z0 root delta not uniform in unknown c0")
    return dict(
        K=K,
        true_original_FULL_J_high_degree_strictly_above_K=K+1,
        original_source_J_global_edge_envelope=_fraction(Fraction(5,2)),
        original_low_CORE_fraction_floor=_fraction(c),
        original_Blackley_Roy_W3_fraction_floor=_fraction(walk),
        original_HEAVY_R_zero=R_Z0,
        source_owner_selected_moment_harris_q2=q2,
        source_owner_selected_moment_harris_q3=q3,
        original_LOW_L6=L6,
        original_LOW_L4=L4,
        original_LOW_B0=B0,
        original_LOW_E=E,
        original_LOW_D=D,
        error_fractions=[_fraction(x) for x in errors],
        coordinate_threshold=coord_s,
        endpoint_threshold=endpoint_s,
        mixed_four_blocker_threshold=blocker_s,
        all_h_sufficient_integer_s0=s0,
        all_h_sufficient_dyadic_h0=_dyadic_h(s0),
        at_least_original_produced_BBo_coefficient=_fraction(bbo),
        heavy_original_D6_delta=_fraction(delta),
        exact_Z_empty_no_GF5_or_B75=False,
        original_ALL_h_precursor_proof_requirements_still_inherited=True,
        root_PROVED_A=False)

def prior_fixed_K64_Harris_budget(C0,c0):
    """Independent recreation of #771 fixed 64 / error 1/8 root h0."""
    normalized_constant_inputs(C0,c0)
    T=_ceil(Fraction(17*R_Z0**3,2)*C0**3)
    L6=24+153*T*T
    K=K_OLD
    q2=16*(K+1)**2
    q3=64*(K+1)**3
    L4=q2*q2*_ceil_sqrt(_ceil(Fraction(17*L6,4)))+19*T
    B0=_ceil_sqrt(360*(K+1)*T)
    E=5*q3*_ceil_sqrt(L6)
    D=4*_ceil_sqrt(B0*T*L4)
    s0=max(64,444*T,(8*E)**2,(8*D)**8)
    return dict(K=K,q2=q2,q3=q3,h0=_dyadic_h(s0),
                s0=s0,root_PROVED_A=False)

def fixed_K_referee(C0,c0):
    """A transparent K=5..64 scan; no global-optimum assertion for real C0."""
    normalized_constant_inputs(C0,c0)
    rows=[]
    for K in range(5,65):
        q=_energy_budget(K,C0,c0)
        rows.append((K,q["all_h_sufficient_dyadic_h0"]))
    best=min(h for k,h in rows)
    winners=[k for k,h in rows if h==best]
    chosen=_energy_budget(K_NEW,C0,c0)
    baseline=prior_fixed_K64_Harris_budget(C0,c0)
    if (K_NEW not in winners or
        chosen["all_h_sufficient_dyadic_h0"]>=baseline["h0"]):
        raise AssertionError("formal K=11 optimized no-Z root not an actual improvement")
    q=chosen
    return dict(
        FORMAL_C0_NOT_PUBLISHED=str(C0),
        FORMAL_c0_NOT_PUBLISHED=str(c0),
        winning_integer_K_in_examined_range_5_through_64=winners,
        best_formal_h0_over_K_5_through_64=best,
        fixed_K11_optimized_h0=q["all_h_sufficient_dyadic_h0"],
        previous_K64_Harris_uniform_h0=baseline["h0"],
        dyadic_h0_gain_from_fixed64=baseline["h0"]-q["all_h_sufficient_dyadic_h0"],
        fixed_K11_sharp_core_floor=q["original_low_CORE_fraction_floor"],
        fixed_K11_walk_floor=q["original_Blackley_Roy_W3_fraction_floor"],
        fixed_K11_positive_BBo_floor=q["at_least_original_produced_BBo_coefficient"],
        new_K11_q2=q["source_owner_selected_moment_harris_q2"],
        new_K11_q3=q["source_owner_selected_moment_harris_q3"],
        old_K64_q2=baseline["q2"],
        old_K64_q3=baseline["q3"],
        external_C6_constants_remain_existential=True,
        unchanged_HEAVY_delta=q["heavy_original_D6_delta"],
        root_PROVED_A=False)

def _min_pairs(V):
    a=2
    while comb(a,2)<V:
        a+=1
    return a,tuple(combinations(range(a),2))[:V]

def genuine_original_source(s,scheme):
    """Original symplectic source fixture, independently rebuilt physical model."""
    from hyp105_original_defect_factor_referee import genuine_symplectic_source
    if s not in (2,4):
        raise ValueError("only true finite W32/W34 source tests")
    flags=tuple(map(tuple,genuine_symplectic_source(s)))
    V=(s+1)*(s*s+1)
    if len(flags)!=(s+1)*V or len(set(flags))!=len(flags):
        raise AssertionError("not the genuine original symplectic point/line flags")
    a,pairs=_min_pairs(V)
    f=pairs
    if scheme=="lex":
        g=pairs
    elif scheme=="reverse":
        g=tuple(reversed(pairs))
    elif scheme=="shift":
        g=pairs[7:]+pairs[:7]
    else:
        raise ValueError("unrecognized fixed correlated globally injected maps")
    if len(set(f))!=V or len(set(g))!=V:
        raise AssertionError("source pair map not separately globally injected")
    return dict(s=s,V=V,N=len(flags),a=a,flags=flags,f=f,g=g,
                source_scheme=scheme)

def _edge(u,v):
    if u==v:
        raise AssertionError("physical diagonal is loop")
    return tuple(sorted((u,v)))

def source_model(c):
    """Independent exact original pencil J and full physical edge ownership."""
    flags,f,g=c["flags"],c["f"],c["g"]
    byp=defaultdict(list)
    byl=defaultdict(list)
    for i,(p,l) in enumerate(flags):
        byp[p].append(i)
        byl[l].append(i)
    if len(byp)!=c["V"] or len(byl)!=c["V"]:
        raise AssertionError("original factor coverage incomplete")
    nbr=[set() for _ in flags]
    for groups,other,other_ix in ((byp,g,1),(byl,f,0)):
        for ids in groups.values():
            for i,j in combinations(ids,2):
                if set(other[flags[i][other_ix]])&set(other[flags[j][other_ix]]):
                    nbr[i].add(j)
                    nbr[j].add(i)
    # Completely separate original GQ collinearity count:
    # collinear p,q iff source point pencils share one original line.
    col_f=0
    col_g=0
    for p,q in combinations(range(c["V"]),2):
        if set(byp[p]) and set(byp[q]):
            if any(flags[i][1]==flags[j][1]
                   for i in byp[p] for j in byp[q]):
                col_f+=bool(set(f[p])&set(f[q]))
        if any(flags[i][0]==flags[j][0]
               for i in byl[p] for j in byl[q]):
            col_g+=bool(set(g[p])&set(g[q]))
    if sum(map(len,nbr))%2:
        raise AssertionError("undirected original J asymmetric")
    eJ=sum(map(len,nbr))//2
    if eJ!=col_f+col_g:
        raise AssertionError("ORIGINAL J not equal to two independent collinearity-overlap sums")
    ownership={}
    per_source={}
    deg=Counter()
    for i,(p,l) in enumerate(flags):
        x0,x1=f[p]
        y0,y1=g[l]
        for u,v in (((x0,y0),(x1,y1)),((x0,y1),(x1,y0))):
            edge=_edge(u,v)
            if edge in ownership:
                raise AssertionError("two true original ID owners of physical edge")
            ownership[edge]=i
            deg[u]+=1
            deg[v]+=1
            per_source.setdefault(i,[]).append(edge)
    if len(ownership)!=2*c["N"] or sum(deg.values())!=4*c["N"]:
        raise AssertionError("true source physical two-diagonal identity false")
    if any(len(v)!=2 or set(v[0])&set(v[1]) for v in per_source.values()):
        raise AssertionError("a named ORIGINAL flag two diagonals share a physical corner")
    return dict(**c,
                source_J_neighbors=nbr,
                source_J_edge_count=eJ,
                collinear_point_conflicts=col_f,
                collinear_line_conflicts=col_g,
                physical_owner=ownership,
                physical_per_original_id=per_source,
                actual_original_full_physical_degree=deg)

def physical_core_referee(model,K,Tdiag):
    """Finite original K-pruning and fixed full-Q_T; diagnostic T, not all-h."""
    if type(K)!=int or K<0 or type(Tdiag)!=int or Tdiag<0:
        raise ValueError("integer K and diagnostic T>=0")
    s=model["s"]
    deg=model["actual_original_full_physical_degree"]
    Q={v for v,n in deg.items() if n>Tdiag*s}
    touched={i for e,i in model["physical_owner"].items()
             if e[0] in Q or e[1] in Q}
    high={i for i,ns in enumerate(model["source_J_neighbors"])
          if len(ns)>K}
    core=set(range(model["N"]))-touched-high
    phys={}
    d=Counter()
    for i in core:
        for e in model["physical_per_original_id"][i]:
            if e in phys:
                raise AssertionError("physical owner repeated in retained CORE")
            phys[e]=i
            d[e[0]]+=1
            d[e[1]]+=1
    if len(phys)!=2*len(core):
        raise AssertionError("original paired core lost one of two diagonals")
    Delta=max(d.values(),default=0)
    if Delta>Tdiag*s:
        raise AssertionError("frozen original heavy Q_T failed LOW physical-degree cap")
    if any(len(model["source_J_neighbors"][i]&core)>K for i in core):
        raise AssertionError("J-pruned ORIGINAL CORE exceeds requested local degree")
    if len(high)* (K+1)>2*model["source_J_edge_count"]:
        raise AssertionError("genuine original J handshaking bound false")
    if len(core)<model["N"]-len(high)-len(touched):
        raise AssertionError("wrong source union bound")
    # Independent exact original REAL physical directed 3walk count:
    W3=2*sum(d[u]*d[v] for u,v in phys)
    if W3*model["a"]**4 < (4*len(core))**3:
        raise AssertionError("true physical Blakley-Roy W3 violates exact arithmetic")
    return dict(
        s=s,scheme=model["source_scheme"],K=K,diagnostic_T_not_HEAVY_all_h=Tdiag,
        actual_original_N=model["N"],
        original_full_J_edges=model["source_J_edge_count"],
        original_collinear_point_J_edges=model["collinear_point_conflicts"],
        original_collinear_line_J_edges=model["collinear_line_conflicts"],
        genuine_FULL_Q_vertices=len(Q),
        original_full_Q_touching_physical_edges=sum(
            e[0] in Q or e[1] in Q for e in model["physical_owner"]),
        original_flags_removed_by_FULL_Q=len(touched),
        original_flags_removed_by_J_gt_K=len(high),
        original_pruned_CORE_flags=len(core),
        original_CORE_real_edges=2*len(core),
        original_CORE_max_physical_degree=Delta,
        original_CORE_max_J_degree=max((len(model["source_J_neighbors"][i]&core)
                                         for i in core),default=0),
        original_full_3walk_count=W3,
        Blakley_Roy_exact_true_actual_physical_graph_verified=True)

def genuine_case(s,scheme):
    m=source_model(genuine_original_source(s,scheme))
    # Diagnostic T values are NOT the astronomical all-h published
    # supersaturation threshold. Scan all integer physical-degree bands
    # to find a truly NONEMPTY Q with a genuinely retained paired CORE.
    trial=[physical_core_referee(m,11,t) for t in range(0,11)]
    partial=[z for z in trial if
             0<z["genuine_FULL_Q_vertices"] and
             0<z["original_pruned_CORE_flags"]<m["N"]]
    return dict(s=s,scheme=scheme,
                no_Q_K11=physical_core_referee(m,11,10),
                low_Q_K11=physical_core_referee(m,11,1),
                test_nontrivial_K3_pruning=physical_core_referee(m,3,10),
                actual_partial_Q_nonempty_CORE_case=partial[0] if partial else None,
                tested_exact_original_physical_T_grid_count=len(trial))

DEPENDENCY_GATE=(
    ("ROOT_GOAL", "root issue #230 seven disjoint named ORIGINAL 6-ID classes",
     "S_s >= D6 + produced BBo", "INHERITED_SCOPE"),
    ("GQ_SRG", "true W(3,s) original collinearity and source J",
     "e(J)<=5s^4/2 for all s>=64, fixed correlated pair-injective maps", "INHERITED_PROOF_REVIEW"),
    ("HEAVY_OWNER", "frozen full physical Q_T, distinct heavy named ORIGINAL owners",
     "HEAVY yields genuine no-clone simple F, m/v>=s/93312, v<=17s^3/(2T)", "INHERITED_PROOF_REVIEW"),
    ("EXT6", "ordinary simple-graph Jiang-Yepremyan 2020 r=2 k=3",
     "unknown fixed existential C_graph,c_graph; copies unoriented C6", "EXTERNAL_SOURCE_PROVENANCE"),
    ("C6_D6", "source independent J plus both cuts and original dual inverse",
     "each true physical C6 maps injectively into D6 named ORIGINAL 6sets", "PREDECESSOR_772_REVIEW"),
    ("LOW_CORE", "FULL J-degree >K and full pre-Z heavy-touching owners removed",
     "K>=5, |C|>=(7/8-5/(K+1))s^4 with actual paired original flags", "NEW_ALL_ORDER_DERIVATION"),
    ("LOW_WALK", "actual paired CORE physical graph on full a^2 corners",
     "W3>=w_K s^6 by Blakley-Roy", "NEW_ALL_ORDER_DERIVATION"),
    ("LOW_COORD", "original coordinate-return physical matrices",
     "improper<=111 Ts^5/2", "INHERITED_PROOF_REVIEW"),
    ("LOW_SELECTOR", "one shared original source random priority and both cuts",
     "Harris q_r=4^r(K+1)^r for r=2,3", "PREDECESSOR_771_REVIEW"),
    ("LOW_MOMENT", "selected bipartite C6/no-clone sixth walk + fourth moment",
     "L6=24+153 T^2, L4=q2^2 sqrtceil +19 T", "INHERITED_PROOF_REVIEW"),
    ("LOW_ENDPOINT", "full original GQ projected physical endpoint geometry",
     "bad endpoints<=24s^5; error<=E s^(11/2)", "INHERITED_PROOF_REVIEW"),
    ("LOW_BLOCKERS", "full A=I, selected smaller CORE C mixed original books",
     "four blocker union<=D s^(47/8)", "PREDECESSOR_770_REVIEW"),
    ("LOW_BBO", "proper accepted original 3path and its inverse",
     "2 directed proper P3 per produced named original BBo sixset", "PREDECESSOR_751_REVIEW"),
    ("QUANTIFIERS", "C0,c0 chosen once; HEAVY and LOW use identical T",
     "s0 finite independent of s,f,g, delta=c0/93312^6", "NEW_ALL_ORDER_DERIVATION"),
)

def certificate():
    probes=( (Fraction(1),Fraction(1)),
             (Fraction(2),Fraction(1,5)),
             (Fraction(7,3),Fraction(1,17)) )
    formal=[fixed_K_referee(C0,c0) for C0,c0 in probes]
    K11=[_energy_budget(K_NEW,C0,c0) for C0,c0 in probes]
    actual=[genuine_case(s,scheme)
            for s,scheme in ((2,"lex"),(2,"reverse"),(4,"lex"),
                             (4,"reverse"),(4,"shift"))]
    return dict(
        schema=SCHEMA,issue=230,parent_pr=772,status=STATUS,
        source_modification_branch_only=True,
        closed_root_PROVED_A=False,
        standalone_all_h_conditional_root_implication_proved_in_manuscript=True,
        all_h_genuine_original_K_free_pruning_proved_in_manuscript=True,
        all_h_asymmetric_error_budget_gluing_proved_in_manuscript=True,
        all_h_K_minimum_from_source_J_bound=5,
        all_h_K11_valid_one_fixed_choice_before_maps=True,
        all_h_unknown_graph_constants_not_numeric=True,
        all_h_GQ_and_source_inverses_inherited_not_newly_accepted=True,
        GF5_or_B75_required_for_ROOT=False,
        general_ASET_exponent_claimed=False,
        genuine_original_W32_W34_pruning_and_Blackley_Roy_falsifiers=actual,
        formal_graph_constant_probe_K_optimization=formal,
        formal_graph_constant_probe_complete_K11_ledger=K11,
        dependency_gate=[
           dict(id=i,statement=j,needed_implication=k,proof_status=l)
           for i,j,k,l in DEPENDENCY_GATE],
    )

if __name__=="__main__":
    print("AA4_ROOT_ENDTOEND_KFREE_CERTIFICATE="+json.dumps(
        certificate(),sort_keys=True,separators=(",",":")))
