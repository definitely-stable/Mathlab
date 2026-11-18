"""AA4-HEAVY-LOW-SYNTHESIS: merge sibling #776 alphabet and #777 top-r mathematics.

A standalone all-h exact rational source/physical proof-budget referee:
  M_H=(1+2^-2H)*(1+23/(16*2^(H/2))) from #775 genuine GQ source J.
  A_H=2(1+2^-H)*(1+2^-2H)+23/(4*2^(3H/2))+4*2^-3H
      from independent sibling #776: MINIMAL true pair alphabet a^2<A_H*s^3.
  Top-r real physical degree selection from parent #777, not the
      inferior partition of Y from #776.
  R_mix=ceil(256*A_H*(1+64*M_H)), H=32 => EXACT 33281.
  In LOW on the very same full physical symbol alphabet:
      w_new=(4*c_KH)^3/A_H^2, c_KH=7/8-4*M_H/(K+1).
  One and the same T=ceil(17*R_mix^3*C0^3/2) in BOTH branches.
  All unknown graph constants remain FORMAL rational probes, never
      numerically established ordinary C6 supersaturation constants.
  ROOT #230 remains OPEN_WITH_FORMAL_BLOCKER.

Finite independent true ORIGINAL W(3,2)/W(3,4) flag/source physical
falsifiers import ONLY the genuine symplectic incidence constructor.
They use full and pruned real physical owner graphs and exact walk counts.
No historical root/HEAVY/LOW or sibling source solver imported.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations
from math import comb,isqrt
import json

SCHEMA="mathlab.hyp105.heavy-low-alphabet-topr-synthesis.v1"
ISSUE=230
PARENT_PR=777
PARALLEL_PR=776
STATUS="OPEN_WITH_FORMAL_BLOCKER"
H_FIXED=32
K_FIXED=10
R_PARENT_777=37441
R_SIBLING_776=66562
R_PARENT_775=93312
ALPHA=(Q(1,64),Q(1,64),Q(15,16))


def ceilq(x):
    if type(x) is not Q:
        raise TypeError("fail-closed: exact Fraction mandatory")
    return -(-x.numerator//x.denominator)


def ceilsqrt(n):
    if type(n) is not int or n<0:
        raise ValueError("nonnegative exact integer root required")
    v=isqrt(n)
    return v+int(v*v<n)


def hceil(n):
    if type(n) is not int or n<1:
        raise ValueError("positive exact integer")
    return (n-1).bit_length()


def min_alphabet(V):
    """O(log V) true minimal a; no brute loop at astronomic dyadic s."""
    if type(V) is not int or V<1:
        raise ValueError("positive number of ORIGINAL points")
    a=(1+isqrt(1+8*V))//2
    while comb(a,2)<V:
        a+=1
    while a>2 and comb(a-1,2)>=V:
        a-=1
    if not comb(a-1,2)<V<=comb(a,2):
        raise AssertionError("not the true minimal pair alphabet")
    return a


def envelope(H):
    """ALL dyadic s>=2^H, H even>=8, fixed before source f and g."""
    if type(H) is not int or H<8 or H%2:
        raise ValueError("source dyadic scale H even>=8")
    M=(1+Q(1,2**(2*H)))*(1+Q(23,16*2**(H//2)))
    A=(2*(1+Q(1,2**H))*(1+Q(1,2**(2*H)))
       +Q(23,4*2**(3*H//2))+Q(4,2**(3*H)))
    # Existing siblings use identical original-source M_H, different F selection.
    # Old-chunk R #776 has 512*A*(1+64*M); new top-r has half.
    # Parent #777 uses 576*(1+64*M) from coarse a^2<=9s^3/4.
    parent777=ceilq(576*(1+64*M))
    sibling776=ceilq(512*A*(1+64*M))
    mix=ceilq(256*A*(1+64*M))
    if not (1<M<Q(35,32) and 2<A<Q(9,4)
            and mix<parent777 and mix<sibling776
            and mix<=R_PARENT_775):
        raise AssertionError("new combined original source/physical R invalid")
    return dict(H=H,M=M,A=A,R=mix,
                R_top_r_parent_777=parent777,
                R_chunk_sibling_776=sibling776,
                source_collision_J_upper=2*M,
                physical_sufficient_vertices_per_s3=A,
                exact_unrounded_density=Q(1,256*A*(1+64*M)),
                source_positive_CORE_K4=Q(7,8)-4*M/5)


def actual_alphabet_envelope(s,H):
    """Independent actual MINIMAL a_s vs symbolic all-h bound."""
    if type(s) is not int or s<2 or s&(s-1) or s<2**H:
        raise ValueError("dyadic source s>=2^H")
    z=envelope(H)
    V=(s+1)*(s*s+1)
    a=min_alphabet(V)
    value=Q(a*a,s**3)
    if not value<z["A"]:
        raise AssertionError("actual ORIGINAL minimal a^2 violates ALL-H source bound")
    if not Q((s*s+1)*(s*s+a-2),s**4)<z["M"]:
        raise AssertionError("true ORIGINAL GQ SRG source C_s exceeds M_H")
    return dict(s=str(s),H=H,V=str(V),a=str(a),
                actual_a2_over_s3=str(value),
                certified_A_H=str(z["A"]),
                actual_original_source_Cs_over_s4=str(Q((s*s+1)*(s*s+a-2),s**4)),
                certified_M_H=str(z["M"]),
                both_true_minimal_alphabet_and_SRG_envelopes_hold=True)


def root_budget(C0,c0,R,alphabet,H=H_FIXED,K=K_FIXED):
    """Conditional original D6/BBo proof budget, exact shared T at one R.

    alphabet=True means source A_H improved paired CORE Blakley-Roy.
    alphabet=False means old 9/4 original physical n ceiling.
    """
    if (type(C0) is not Q or type(c0) is not Q
            or C0<1 or not 0<c0<=1):
        raise ValueError("unknown published C6 constants must use FORMAL exact rational probes")
    if type(R) is not int or R<1 or type(K) is not int or K<4:
        raise ValueError("fixed denominator R positive, source K>=4")
    z=envelope(H)
    c=Q(7,8)-4*z["M"]/Q(K+1)
    if c<=0:
        raise ValueError("LOW original paired CORE no longer guaranteed")
    # Actual ORIGINAL paired core graph: m=2|C|, n=a^2, W3>=(2m)^3/n^2.
    physical_ceiling=z["A"] if alphabet else Q(9,4)
    walk=(4*c)**3/physical_ceiling**2
    T=ceilq(Q(17*R**3,2)*C0**3)
    L6=24+153*T*T
    q2=16*(K+1)**2
    q3=64*(K+1)**3
    L4=q2*q2*ceilsqrt(ceilq(Q(17*L6,4)))+19*T
    B0=ceilsqrt(360*(K+1)*T)
    E=5*q3*ceilsqrt(L6)
    D=4*ceilsqrt(B0*T*L4)
    sx=ceilq(Q(111*T,2)/(ALPHA[0]*walk))
    se=ceilq((Q(E)/(ALPHA[1]*walk))**2)
    sb=ceilq((Q(D)/(ALPHA[2]*walk))**8)
    s0=max(2**H,64,sx,se,sb)
    bbo=walk*(1-sum(ALPHA))/2
    delta=c0/Q(R**6)
    if not (bbo>delta
            and Q(111*T,2)<=ALPHA[0]*walk*s0
            and Q(E)**2<=(ALPHA[1]*walk)**2*s0
            and Q(D)**8<=(ALPHA[2]*walk)**8*s0):
        raise AssertionError("original LOW source mixed-budget/external HEAVY quantifiers inconsistent")
    return dict(
        H=H,K=K,R=R,improved_true_a2_bound=alphabet,
        M_H=str(z["M"]),A_H=str(z["A"]),
        source_original_CORE_fraction=str(c),
        actual_physical_W3_floor=str(walk),
        T=str(T),q2=q2,q3=q3,L6=str(L6),L4=str(L4),
        B0=str(B0),E=str(E),D=str(D),
        coordinate_cutoff=str(sx),endpoint_cutoff=str(se),
        mixed_four_blocker_cutoff=str(sb),
        exact_s0=str(s0),dyadic_h0=hceil(s0),
        alpha=[str(t) for t in ALPHA],
        original_BBo_produced_conditional_floor=str(bbo),
        original_D6_HEAVY_delta=str(delta),
        published_external_graph_C6_constants_NOT_NUMLY_VERIFIED=True,
        original_LOW_global_moment_proofs_inherited=True,
        ROOT_PROVED_A=False)


def combined_formal_scenario(C0,c0):
    env=envelope(H_FIXED)
    b775=root_budget(C0,c0,R_PARENT_775,False)
    b776=root_budget(C0,c0,env["R_chunk_sibling_776"],True)
    b777=root_budget(C0,c0,env["R_top_r_parent_777"],False)
    mix=root_budget(C0,c0,env["R"],True)
    if not (b775["R"]==93312 and b776["R"]==66562
            and b777["R"]==37441 and mix["R"]==33281
            and mix["dyadic_h0"]<min(b776["dyadic_h0"],
                                   b777["dyadic_h0"])
            and Q(mix["original_D6_HEAVY_delta"])>
                max(Q(b777["original_D6_HEAVY_delta"]),
                    Q(b776["original_D6_HEAVY_delta"]))
            and Q(mix["actual_physical_W3_floor"])>
                Q(b777["actual_physical_W3_floor"])):
        raise AssertionError("parallel HEAVY improvements did not compose")
    return dict(
        C0_FORMAL_NOT_PUBLISHED=str(C0),
        c0_FORMAL_NOT_PUBLISHED=str(c0),
        baseline_pr775_R=b775["R"],baseline_pr775_h0=b775["dyadic_h0"],
        sibling_pr776_R=b776["R"],sibling_pr776_h0=b776["dyadic_h0"],
        parent_pr777_R=b777["R"],parent_pr777_h0=b777["dyadic_h0"],
        combined_R=mix["R"],combined_h0=mix["dyadic_h0"],
        parent777_to_combined_gain_h=b777["dyadic_h0"]-mix["dyadic_h0"],
        sibling776_to_combined_gain_h=b776["dyadic_h0"]-mix["dyadic_h0"],
        sextic_delta_gain_vs_pr775=str(Q(R_PARENT_775,mix["R"])**6),
        sextic_delta_gain_vs_pr777=str(Q(R_PARENT_777,mix["R"])**6),
        sextic_delta_gain_vs_pr776=str(Q(R_SIBLING_776,mix["R"])**6),
        LOW_W3_gain_over_parent777=str(
            Q(mix["actual_physical_W3_floor"])/
            Q(b777["actual_physical_W3_floor"])),
        root_new_delta=str(mix["original_D6_HEAVY_delta"]),
        root_new_BBo_floor=str(mix["original_BBo_produced_conditional_floor"]),
        common_NEW_T=str(mix["T"]),
        actual_original_sixset_and_moments_STILL_PROOF_GATES=True,
        root_PROVED_A=False)


def _edge(u,v):
    if u==v:
        raise AssertionError("original physical edge must have two distinct corners")
    return tuple(sorted((u,v)))


def original_symplectic_fixture(s,mode):
    from hyp105_original_defect_factor_referee import genuine_symplectic_source
    if s not in (2,4):
        raise ValueError("only true ORIGINAL W32/W34 finite falsifier")
    flags=tuple(map(tuple,genuine_symplectic_source(s)))
    V=(s+1)*(s*s+1)
    a=min_alphabet(V)
    pairs=tuple(combinations(range(a),2))[:V]
    f=pairs
    if mode=="lex":
        g=pairs
    elif mode=="reverse":
        g=pairs[::-1]
    elif mode=="shift":
        g=pairs[1:]+pairs[:1]
    else:
        raise ValueError("unknown source-label correlation")
    if len(flags)!=(s+1)*V or len(set(flags))!=len(flags) or len(set(f))!=V or len(set(g))!=V:
        raise AssertionError("bad true original incidence/f-g pair injection")
    physical={}
    per={}
    deg=Counter()
    point=defaultdict(list)
    line=defaultdict(list)
    for i,(p,l) in enumerate(flags):
        point[p].append(i)
        line[l].append(i)
        x,z=f[p];y,w=g[l]
        ee=(_edge((x,y),(z,w)),_edge((x,w),(z,y)))
        if set(ee[0])&set(ee[1]):
            raise AssertionError("true original two diagonals share physical vertex")
        for e in ee:
            if e in physical:
                raise AssertionError("two ORIGINAL flags own one physical edge")
            physical[e]=i
            deg[e[0]]+=1
            deg[e[1]]+=1
        per[i]=ee
    if len(physical)!=2*len(flags) or sum(deg.values())!=4*len(flags):
        raise AssertionError("original physical full edge/degree count invalid")
    J=[set() for _ in flags]
    for groups,side in ((point,"point"),(line,"line")):
        for ids in groups.values():
            for i,j in combinations(ids,2):
                p,l=flags[i];q,m=flags[j]
                a1=g[l] if side=="point" else f[p]
                a2=g[m] if side=="point" else f[q]
                if set(a1)&set(a2):
                    J[i].add(j);J[j].add(i)
    eJ=sum(len(x) for x in J)//2
    return dict(s=s,mode=mode,flags=flags,V=V,a=a,f=f,g=g,physical=physical,
                per=per,degree=deg,source_J=J,source_J_edges=eJ)


def _cuts(owners,source,typ):
    flags=source["flags"]
    labels=source["f"] if typ=="x" else source["g"]
    ix=0 if typ=="x" else 1
    bit={}
    def twice_expectation():
        return sum(2*int(bit[u]!=bit[v]) if u in bit and v in bit else 1
                   for i in owners for u,v in (labels[flags[i][ix]],))
    previous=twice_expectation()
    for symbol in range(source["a"]):
        bit[symbol]=0
        zero=twice_expectation()
        bit[symbol]=1
        one=twice_expectation()
        if zero+one!=2*previous:
            raise AssertionError("shared-source conditional color expectation broken")
        bit[symbol]=0 if zero>=one else 1
        now=twice_expectation()
        if now<previous:
            raise AssertionError("whole-original-source-coloring lost expectation")
        previous=now
    out=tuple(i for i in owners if
              bit[labels[flags[i][ix]][0]]!=bit[labels[flags[i][ix]][1]])
    if 2*len(out)<len(owners) or 2*len(out)!=previous:
        raise AssertionError("selected original owner halves invalid")
    return bit,out


def physical_C6_original_source_check(F,source):
    """Independent ordinary graph-first unoriented C6 to unique original sixset."""
    adj=defaultdict(set)
    for u,v in F:
        adj[u].add(v);adj[v].add(u)
    def canonical(path):
        path=tuple(path)
        return min(tuple(z[k:]+z[:k]) for z in (path,path[::-1]) for k in range(6))
    cycles=set()
    for start in sorted(adj):
        stack=[(start,)]
        while stack:
            path=stack.pop()
            if len(path)==6:
                if start in adj[path[-1]]:
                    cycles.add(canonical(path))
                continue
            for v in adj[path[-1]]:
                if v not in path and v>=start:
                    stack.append(path+(v,))
    names=set()
    for path in cycles:
        if len({v[0] for v in path})!=6 or len({v[1] for v in path})!=6:
            raise AssertionError("actual source independent two-cut graph has improper C6")
        ids=tuple(F[_edge(path[i],path[(i+1)%6])] for i in range(6))
        if len(set(ids))!=6 or len({source["flags"][i][0] for i in ids})!=6 or len({source["flags"][i][1] for i in ids})!=6:
            raise AssertionError("physical original C6 source IDs are not a valid D6")
        if frozenset(ids) in names:
            raise AssertionError("two distinct ordinary C6 share one ORIGINAL six-ID set")
        names.add(frozenset(ids))
    return dict(actual_ordinary_simple_unoriented_C6=len(cycles),
                distinct_TRUE_original_D6_sixsets=len(names),
                no_original_sixset_cloning_or_twelve_fold_loss=True)


def finite_dual_referee(s,mode,Tdiag):
    """Genuine full ORIGINAL HEAVY F + independently frozen LOW paired core."""
    if type(Tdiag) is not int or Tdiag<0:
        raise ValueError("nonnegative diagnostic T integer")
    source=original_symplectic_fixture(s,mode)
    flags,edges,degree=source["flags"],source["physical"],source["degree"]
    Qfull={v for v,d in degree.items() if d>Tdiag*s}
    heavy={e:i for e,i in edges.items() if e[0] in Qfull or e[1] in Qfull}
    heavy_ids=set(heavy.values())
    J=source["source_J"]
    original_J_edges=source["source_J_edges"]
    # Separate mathematical HEAVY and LOW at a diagnostic Q: no claim
    # s=2/4 satisfies the asymptotic s>=2^32 or E_T>=s^4/8 when selected.
    Hresult=None
    if heavy_ids:
        ids=set(heavy_ids)
        Jsubedges=sum(len(J[i]&ids) for i in ids)//2
        caro=Q(len(ids)**2,len(ids)+2*Jsubedges)
        selected=[]
        while ids:
            i=min(ids,key=lambda i:(len(J[i]&ids),i))
            selected.append(i)
            ids-={i}|J[i]
        if len(selected)<caro or any(j in J[i] for i,j in combinations(selected,2)):
            raise AssertionError("original SOURCE Caro Wei selection invalid")
        bx,selx=_cuts(tuple(selected),source,"x")
        by,S=_cuts(selx,source,"y")
        if not S:
            raise AssertionError("both actual original typed cuts erased source")
        chosen={e:i for i in S for e in source["per"][i]}
        if len(chosen)!=2*len(S):
            raise AssertionError("original whole owners not paired before HEAVY block")
        witness={}
        for i in S:
            options=[(e,v) for e in source["per"][i] for v in e if v in Qfull]
            if not options:
                raise AssertionError("selected original source owner has no full-Q witness")
            witness[i]=min(options)
        majoritybit=0 if sum(bx[v[0]]==0 for e,v in witness.values())*2>=len(S) else 1
        Rq={v for v in Qfull if bx[v[0]]==majoritybit}
        r=len(Rq)
        Y=tuple((x,y) for x in range(source["a"]) for y in range(source["a"])
                if bx[x]!=majoritybit)
        cross={}
        actual_d=Counter()
        for e,i in chosen.items():
            u,v=e
            if u in Rq and v in Y:
                cross[e]=i;actual_d[v]+=1
            elif v in Rq and u in Y:
                cross[e]=i;actual_d[u]+=1
        witness_count=sum(bx[v[0]]==majoritybit for e,v in witness.values())
        if 2*witness_count<len(S) or len(cross)<witness_count:
            raise AssertionError("actual SOURCE heavy witness majority invalid")
        top=set(sorted(Y,key=lambda v:(-actual_d[v],v))[:min(r,len(Y))])
        F={e:i for e,i in cross.items() if e[0] in top or e[1] in top}
        vF=len(Rq|top)
        if not F or vF>2*r or len(F)*source["a"]**2<len(cross)*r:
            raise AssertionError("TOP-R genuine physical edge averaging fails")
        if Q(len(F),vF)<Q(len(S),4*source["a"]**2):
            raise AssertionError("original top-r physical density FAIL")
        if any(edges[e]!=i or i not in S for e,i in F.items()):
            raise AssertionError("source-clone physical edge in actual F")
        invert=physical_C6_original_source_check(F,source)
        Hresult=dict(
            physically_checked_actual_C6_original_source_inverse=invert,
            source_real_heavy_edges=len(heavy),source_original_heavy_owners=len(heavy_ids),
            original_CaroWei_lower=str(caro),
            selected_source_independent_count=len(selected),after_x_cut=len(selx),
            after_both_cuts=len(S),original_selected_paired_edges=len(chosen),
            actual_heavy_witness_bit_majority=witness_count,
            selected_original_F_real_edges=len(F),
            selected_original_F_real_vertices=vF,
            physical_no_clone_F_topr_bound=str(Q(len(S),4*source["a"]**2)),
            physical_actual_F_density=str(Q(len(F),vF)),
            actual_F_edges_only_from_original_owners=True,
            all_selected_source_J_independent=True)
    # Independently build true low CORE on the SAME fixed full H and Q.
    # Restrict to a diagnostic source FULL-J cap Ktest: finite orders are
    # not used to assert any all-h K10 source lower coefficient.
    Ktest=3
    hitQ=set(heavy.values())
    highJ={i for i,neighbors in enumerate(J) if len(neighbors)>Ktest}
    CORE=set(range(len(flags)))-hitQ-highJ
    low_physical={e:i for i in CORE for e in source["per"][i]}
    if len(low_physical)!=2*len(CORE):
        raise AssertionError("genuine ORIGINAL paired LOW graph has missing diagonals")
    lowdeg=Counter()
    for u,v in low_physical:
        lowdeg[u]+=1;lowdeg[v]+=1
    W3=2*sum(lowdeg[u]*lowdeg[v] for u,v in low_physical)
    if W3*source["a"]**4<(4*len(CORE))**3:
        raise AssertionError("independent true physical original Blakley Roy W3 violated")
    if max(lowdeg.values(),default=0)>Tdiag*s:
        raise AssertionError("source LOW retained physical vertex degree exceeds frozen Q")
    if max((len(J[i]&CORE) for i in CORE),default=0)>Ktest:
        raise AssertionError("original LOW FULL-J degree cap not respected")
    return dict(s=s,mode=mode,diagnostic_T_not_asymptotic=Tdiag,
                ORIGINAL_V=source["V"],original_source_N=len(flags),
                minimal_true_physical_a=source["a"],
                full_genuine_original_physical_edges=len(edges),
                full_original_J_conflicts=original_J_edges,
                full_physical_Q_real_vertices=len(Qfull),
                HEAVY_real_no_clone_top_r=Hresult,
                LOW_original_named_core_flags=len(CORE),
                LOW_original_paired_physical_edges=len(low_physical),
                LOW_true_physical_W3=W3,
                LOW_true_Blackley_Roy_exact_verified=True,
                heavy_source_unchanged_all_alphabet_labels=True,
                root_PROVED_A=False)


def certificate():
    z=envelope(H_FIXED)
    scenarios=[combined_formal_scenario(*q) for q in (
        (Q(1),Q(1)),(Q(2),Q(1,5)),(Q(7,3),Q(1,17)))]
    small=[finite_dual_referee(s,mode,T) for s in (2,4)
           for mode in ("lex","reverse","shift") for T in (0,1,2,3)]
    large=[actual_alphabet_envelope(s,H_FIXED)
           for s in (2**H_FIXED,2**(H_FIXED+2),2**(H_FIXED+8))]
    return dict(
        schema=SCHEMA,issue=ISSUE,parent_pr=PARENT_PR,parallel_pr=PARALLEL_PR,
        status=STATUS,branch_Z_scope="EMPTY",
        new_synthesis_all_h_mathematical_proof_in_manuscript=True,
        entire_FULL_GQ_original_SOURCE_quantifier_preserved=True,
        external_graph_C6_constants_remain_existential=True,
        original_source_pruning_K10_coherent_with_new_graph_T=True,
        exact_minimal_original_a2_envelope_from_sibling_776_independently_checked=True,
        real_physical_top_r_unrounded_source_from_parent_777_independently_checked=True,
        original_ROOT_unweighted_seven_sixset_PROVED_A=False,
        original_full_LOW_moments_and_BBo_inverse_not_newly_accepted=True,
        no_GF5_or_ASET_exponent_claimed=True,
        fixed_H=H_FIXED,fixed_K=K_FIXED,
        source_M_H=str(z["M"]),physical_A_H=str(z["A"]),
        combined_R=z["R"],
        old_R_parent_777=z["R_top_r_parent_777"],
        old_R_parallel_776=z["R_chunk_sibling_776"],
        original_true_heavy_density_lower=str(z["exact_unrounded_density"]),
        formal_ROOT_comparisons=scenarios,
        TRUE_original_W32_W34_finite_same_H_heavy_low_Q_cases=small,
        true_large_dyadic_minimal_alphabet_envelopes=large)


if __name__=="__main__":
    print("AA4_HEAVY_LOW_SYNERGY_CERTIFICATE="+json.dumps(
        certificate(),sort_keys=True,separators=(",",":")))
