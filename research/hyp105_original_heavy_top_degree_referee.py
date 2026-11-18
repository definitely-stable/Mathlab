"""AA4-HEAVY-TOP-DEGREE: independent actual ORIGINAL HEAVY -> simple F.

NEW all-order no-clone physical selection lemma:
For r genuine left heavy physical vertices and Y opposite-bit physical
vertices, select up to r Y vertices with the largest ACTUAL degrees into R.
This retains >= E(R,Y)*r/n genuine edges, without old factor-two loss
from rounding the number of disjoint Y-blocks. Combined with independently
proved source SRG bound e(J)<2*M_H*s^4 for dyadic s>=2^H,
the HEAVY density denominator is
    R_H = ceil(576*(1+64*M_H)).
For H=32, R_H=37441 (prior 93312).

True finite symplectic W(3,2)/W(3,4) flag geometry is imported ONLY from
the original independent incidence constructor. All other Caro-Wei,
source pencils, paired edges, colorings, physical top-degree selection and
C6 source inverses are rebuilt here. Finiteness is a falsifier, never
an all-h proof substitute. The entire ROOT issue remains
OPEN_WITH_FORMAL_BLOCKER pending inherited global LOW acceptance.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb,isqrt
import json

SCHEMA="mathlab.hyp105.original-heavy-top-degree-no-clone.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
H_FIXED=32
K_LOW_FIXED=10
OLD_R=93312
ERROR_ALLOC=(Fraction(1,64),Fraction(1,64),Fraction(15,16))


def ceil_fraction(q):
    if not isinstance(q,Fraction):
        raise TypeError("exact Fraction required")
    return -(-q.numerator//q.denominator)


def ceil_root(n):
    if type(n)!=int or n<0:
        raise ValueError("nonnegative integer root required")
    k=isqrt(n)
    return k+(k*k<n)


def positive_dyadic_h(x):
    if type(x)!=int or x<=0:
        raise ValueError("strict positive integer")
    return (x-1).bit_length()


def source_M(H):
    if type(H)!=int or H<8 or H%2:
        raise ValueError("fixed even H>=8, before maps and s")
    return (1+Fraction(1,2**(2*H)))*(1+Fraction(23,16*2**(H//2)))


def improved_R(H=H_FIXED):
    """Precise all-order source/physical density, no arbitrary rounding."""
    M=source_M(H)
    return ceil_fraction(576*(1+64*M))


def formal_heavy_low_root(C0,c0,H=H_FIXED,K=K_LOW_FIXED,old=False):
    """All-h conditional root with a common, fixed HEAVY/LOW T and R.

    C0,c0 are NOT known numerical constants of the published graph C6
    theorem. The source/sixset/moment prerequisites are separately
    stated, not inferred from this arithmetic checker.
    """
    if (not isinstance(C0,Fraction) or not isinstance(c0,Fraction)
            or C0<1 or not 0<c0<=1):
        raise ValueError("only formal exact rational C0>=1, 0<c0<=1")
    if type(K)!=int or K<4:
        raise ValueError("K must preserve a strictly positive original CORE")
    M=source_M(H)
    R=OLD_R if old else improved_R(H)
    c=Fraction(7,8)-4*M/Fraction(K+1)
    if c<=0:
        raise ValueError("original source core does not survive")
    w=Fraction(16,81)*(4*c)**3
    T=ceil_fraction(Fraction(17*R**3,2)*C0**3)
    delta=c0/Fraction(R**6)
    L6=24+153*T*T
    q2=16*(K+1)**2
    q3=64*(K+1)**3
    L4=q2*q2*ceil_root(ceil_fraction(Fraction(17*L6,4)))+19*T
    B0=ceil_root(360*(K+1)*T)
    E=5*q3*ceil_root(L6)
    D=4*ceil_root(B0*T*L4)
    a1,a2,a3=ERROR_ALLOC
    s_coord=ceil_fraction(Fraction(111*T,2)/(a1*w))
    s_endpoint=ceil_fraction((Fraction(E)/(a2*w))**2)
    s_blocker=ceil_fraction((Fraction(D)/(a3*w))**8)
    s0=max(2**H,64,s_coord,s_endpoint,s_blocker)
    bbo=w*(1-sum(ERROR_ALLOC))/2
    if not bbo>delta:
        raise AssertionError("retained genuine produced BBo below HEAVY delta")
    if not (Fraction(111*T,2)<=a1*w*s0
            and E*E<=(a2*w)**2*s0
            and D**8<=(a3*w)**8*s0):
        raise AssertionError("three inherited physical LOW error bounds do not fit")
    return dict(
        H=H,K=K,M_H=str(M),R=R,
        actual_heavy_delta=str(delta),
        original_CORE_lower=str(c),original_W3_lower=str(w),
        original_produced_BBo_lower=str(bbo),
        source_J_degree_cut_above=K+1,
        selected_Harris_q2=q2,selected_Harris_q3=q3,
        fixed_T=str(T),L6=str(L6),L4=str(L4),B0=str(B0),
        E=str(E),D=str(D),
        cutoff_coordinate=str(s_coord),
        cutoff_endpoint=str(s_endpoint),
        cutoff_original_mixed_blockers=str(s_blocker),
        exact_s0=str(s0),exact_h0=positive_dyadic_h(s0),
        published_graph_constants_not_numerically_identified=True,
        inherited_original_LOW_and_sixID_gates_still_open=True,
        root_PROVED_A=False)


def exact_formal_comparison(C0,c0):
    old=formal_heavy_low_root(C0,c0,old=True)
    new=formal_heavy_low_root(C0,c0,old=False)
    if not (new["R"]==37441 and old["R"]==93312
            and int(new["fixed_T"])<int(old["fixed_T"])
            and int(new["exact_s0"])<int(old["exact_s0"])
            and new["exact_h0"]<old["exact_h0"]
            and Fraction(new["actual_heavy_delta"])>
                Fraction(old["actual_heavy_delta"])):
        raise AssertionError("top-degree no-clone HEAVY did not improve true root")
    return dict(
        FORMAL_C0_NOT_PUBLISHED=str(C0),FORMAL_c0_NOT_PUBLISHED=str(c0),
        previous_R=old["R"],new_R=new["R"],
        previous_h0=old["exact_h0"],new_h0=new["exact_h0"],
        improved_dyadic_orders=old["exact_h0"]-new["exact_h0"],
        previous_T=str(old["fixed_T"]),new_T=str(new["fixed_T"]),
        heavy_delta_multiplier=str(Fraction(OLD_R,improved_R(H_FIXED))**6),
        previous_ROOT_delta=old["actual_heavy_delta"],
        NEW_ROOT_delta=new["actual_heavy_delta"],
        exact_and_conditional_only=True,
        original_ROOT_PROVED_A=False)


def _pairs(V):
    a=2
    while comb(a,2)<V:
        a+=1
    pairs=tuple(combinations(range(a),2))
    return a,pairs[:V]


def genuine_source(s,mode):
    from hyp105_original_defect_factor_referee import genuine_symplectic_source
    if s not in (2,4):
        raise ValueError("genuine finite W32/W34 only")
    flags=tuple(map(tuple,genuine_symplectic_source(s)))
    V=(s+1)*(s*s+1)
    if len(flags)!=(s+1)*V or len(set(flags))!=len(flags):
        raise AssertionError("not true W3s ORIGINAL named flags")
    a,pairs=_pairs(V)
    f=pairs
    if mode=="lex":
        g=pairs
    elif mode=="reverse":
        g=pairs[::-1]
    elif mode=="shift":
        g=pairs[1:]+pairs[:1]
    else:
        raise ValueError("unknown fixed map correlation")
    if len(set(f))!=V or len(set(g))!=V:
        raise AssertionError("global pair injection lost")
    return dict(s=s,V=V,a=a,flags=flags,f=f,g=g,mode=mode)


def _edge(u,v):
    if u==v:
        raise ValueError("no actual physical loops")
    return tuple(sorted((u,v)))


def source_j_and_physical(m):
    """Two physically true diagonals for EVERY original flag, no copies."""
    f,g,flags=m["f"],m["g"],m["flags"]
    byp=defaultdict(list)
    byl=defaultdict(list)
    for i,(p,l) in enumerate(flags):
        byp[p].append(i)
        byl[l].append(i)
    J=[set() for _ in flags]
    for groups,pairs,ix in ((byp,g,1),(byl,f,0)):
        for ids in groups.values():
            for i,j in combinations(ids,2):
                if set(pairs[flags[i][ix]])&set(pairs[flags[j][ix]]):
                    J[i].add(j)
                    J[j].add(i)
    eJ=sum(len(x) for x in J)//2
    pc=lc=0
    for p,q in combinations(range(m["V"]),2):
        if any(flags[i][1]==flags[j][1]
               for i in byp[p] for j in byp[q]):
            pc+=bool(set(f[p])&set(f[q]))
        if any(flags[i][0]==flags[j][0]
               for i in byl[p] for j in byl[q]):
            lc+=bool(set(g[p])&set(g[q]))
    if eJ!=pc+lc:
        raise AssertionError("original conflict J and dual collinear counts disagree")
    physical={}
    per_owner={}
    deg=Counter()
    for i,(p,l) in enumerate(flags):
        x,k=f[p]
        y,z=g[l]
        diagonal=(_edge((x,y),(k,z)),_edge((x,z),(k,y)))
        if diagonal[0]==diagonal[1] or set(diagonal[0])&set(diagonal[1]):
            raise AssertionError("true original rectangle diagonals wrong")
        per_owner[i]=diagonal
        for e in diagonal:
            if e in physical:
                raise AssertionError("two distinct ORIGINAL owners of same real edge")
            physical[e]=i
            deg[e[0]]+=1
            deg[e[1]]+=1
    if len(physical)!=2*len(flags) or sum(deg.values())!=4*len(flags):
        raise AssertionError("physical original two-diagonal degree sum lost")
    return dict(**m,J=J,eJ=eJ,point_overlaps=pc,line_overlaps=lc,
                physical=physical,per_owner=per_owner,degree=deg)


def independent_caro_wei(source_J,vertex_ids):
    """Constructive min-degree ORIGINAL owner selector and potential proof."""
    S=set(vertex_ids)
    if len(S)!=len(tuple(vertex_ids)) or any(
            type(i)!=int or i<0 or i>=len(source_J) for i in S):
        raise ValueError("distinct original source IDs required")
    edges=sum(len(source_J[i]&S) for i in S)//2
    lower=Fraction(len(S)**2,len(S)+2*edges) if S else Fraction(0)
    potential=sum((Fraction(1,1+len(source_J[i]&S)) for i in S),Fraction(0))
    result=[]
    potentials=[]
    while S:
        before=sum((Fraction(1,1+len(source_J[i]&S)) for i in S),Fraction(0))
        i=min(S,key=lambda j:(len(source_J[j]&S),j))
        result.append(i)
        S-={i}|source_J[i]
        after=sum((Fraction(1,1+len(source_J[j]&S)) for j in S),Fraction(0))
        if before-after>1:
            raise AssertionError("Caro-Wei min-degree potential decreases by >1")
        potentials.append(str(before-after))
    if len(result)<lower or len(result)<potential:
        raise AssertionError("constructive independent set below original Caro-Wei")
    if any(j in source_J[i] for i,j in combinations(result,2)):
        raise AssertionError("retained actual original source flags conflict")
    return dict(owners=tuple(result),lower=lower,potential=potential,
                potential_steps=potentials)


def derandomize_typed_bits(owner_ids,model,typ):
    """Genuine whole-original-flag pair cuts by conditional expectation."""
    flags=model["flags"]
    pairs=model["f"] if typ=="x" else model["g"]
    factors=[flags[i][0 if typ=="x" else 1] for i in owner_ids]
    a=model["a"]
    bits={}
    def doubled_expected():
        total=0
        for factor in factors:
            u,v=pairs[factor]
            if u in bits and v in bits:
                total+=2*(bits[u]!=bits[v])
            else:
                total+=1
        return total
    previous=doubled_expected()
    for symbol in range(a):
        bits[symbol]=0
        zero=doubled_expected()
        bits[symbol]=1
        one=doubled_expected()
        if zero+one!=2*previous:
            raise AssertionError("actual full-source color expectation changed")
        if zero>=one:
            bits[symbol]=0
            current=zero
        else:
            current=one
        if current<previous:
            raise AssertionError("source pair-cut conditional expectation decreased")
        previous=current
    retained=tuple(i for i in owner_ids
                   if bits[pairs[flags[i][0 if typ=="x" else 1]][0]] !=
                      bits[pairs[flags[i][0 if typ=="x" else 1]][1]])
    if 2*len(retained)<len(tuple(owner_ids)):
        raise AssertionError("whole-flag two-color cut below half")
    if previous!=2*len(retained):
        raise AssertionError("conditional expectation and actual flags mismatch")
    return bits,retained


def physical_heavy_top_degree_referee(model,Tdiag):
    """True ORIGINAL W32/W34, frozen Q, Caro Wei, two cuts, real F."""
    if type(Tdiag)!=int or Tdiag<0:
        raise ValueError("diagnostic finite T>=0 integer")
    s=model["s"]
    Q={v for v,d in model["degree"].items() if d>Tdiag*s}
    heavy={e:i for e,i in model["physical"].items() if e[0] in Q or e[1] in Q}
    L=set(heavy.values())
    if not L:
        return dict(s=s,mode=model["mode"],Tdiag=Tdiag,HEAVY_nonvacuous=False,
                    full_physical_Q=len(Q),original_full_heavy_edges=0,
                    root_PROVED_A=False)
    selection=independent_caro_wei(model["J"],sorted(L))
    source_I=selection["owners"]
    bx,Cx=derandomize_typed_bits(source_I,model,"x")
    by,S=derandomize_typed_bits(Cx,model,"y")
    if not S:
        raise AssertionError("nonempty original heavy source disappeared")
    # Every owner has at least one ACTUAL heavy edge, even after cuts;
    # both original diagonals are bichromatic in BOTH typed alphabets.
    physical_sel={e:i for i in S
                  for e in model["per_owner"][i]}
    for e in physical_sel:
        u,v=e
        if not (bx[u[0]]!=bx[v[0]] and by[u[1]]!=by[v[1]]):
            raise AssertionError("selected original diagonal does not cross BOTH cuts")
    witness={}
    for i in S:
        candidates=[e for e in model["per_owner"][i] if e in heavy]
        if not candidates:
            raise AssertionError("selected source owner lost actual frozen heavy edge")
        e=min(candidates)
        possible=sorted(q for q in e if q in Q)
        witness[i]=(e,possible[0])
    by_side=Counter(bx[v[0]] for e,v in witness.values())
    bit=max((0,1),key=lambda k:(by_side[k],-k))
    RQ={v for v in Q if bx[v[0]]==bit}
    r=len(RQ)
    if r<=0:
        raise AssertionError("source heavy endpoint majority has no real vertices")
    n=model["a"]**2
    Y=tuple((x,y) for x in range(model["a"]) for y in range(model["a"])
            if bx[x]!=bit)
    if not Y:
        raise AssertionError("selected true heavy witness has no opposite-bit corner")
    Ry=Counter()
    real_cross={}
    for e,i in physical_sel.items():
        u,v=e
        if u in RQ and v in Y:
            Ry[v]+=1
            real_cross[e]=i
        elif v in RQ and u in Y:
            Ry[u]+=1
            real_cross[e]=i
    majority_count=sum(bx[v[0]]==bit for e,v in witness.values())
    if len(real_cross)<majority_count or 2*majority_count<len(S):
        raise AssertionError("majority of original full-heavy witnesses lost")
    Ytop=set(sorted(Y,key=lambda v:(-Ry[v],v))[:min(r,len(Y))])
    F={e:i for e,i in real_cross.items() if e[0] in Ytop or e[1] in Ytop}
    # The improvement is the UNROUNDED prefix-degree average.
    # r<=n, |Y|<=n, |Ytop|=min(r,|Y|).
    if not Fraction(len(F),1)>=Fraction(len(real_cross)*r,n):
        raise AssertionError("top-r true physical Y vertices violate mean-degree bound")
    if not Fraction(len(F),1)>=Fraction(majority_count*r,n):
        raise AssertionError("new source heavy top-r lower bound false")
    if not (len(RQ)<=n and len(Ytop)<=r and
            len(RQ|Ytop)<=2*r and
            Fraction(len(F),len(RQ|Ytop))>=Fraction(len(S),4*n)):
        raise AssertionError("real physical no-clone F density lower bound false")
    if not set(F).issubset(model["physical"]) or not set(F).issubset(physical_sel):
        raise AssertionError("non-original physical F edge materialized")
    if len({e for e,_ in witness.values()})!=len(S):
        raise AssertionError("two named ORIGINAL witness IDs share one physical edge")
    if len(physical_sel)!=2*len(S):
        raise AssertionError("selected original whole flags did not own both diagonals")
    for e,i in F.items():
        if model["physical"][e]!=i or i not in S:
            raise AssertionError("F edge has wrong ORIGINAL source owner")
    return dict(
        s=s,mode=model["mode"],Tdiag=Tdiag,HEAVY_nonvacuous=True,
        original_named_flags=len(model["flags"]),
        original_pencil_J_edges=model["eJ"],
        original_point_collinear_J=model["point_overlaps"],
        original_line_collinear_J=model["line_overlaps"],
        full_physical_Q=len(Q),original_full_heavy_edges=len(heavy),
        original_heavy_distinct_source_owners=len(L),
        original_CaroWei_source_lower=str(selection["lower"]),
        original_CaroWei_source_potential=str(selection["potential"]),
        original_independent_owners=len(source_I),
        after_original_x_cut=len(Cx),after_original_y_cut=len(S),
        actual_original_heavy_witness_majority=majority_count,
        actual_physical_majority_Q_R=r,
        true_opposite_Y_vertices=len(Y),
        selected_original_true_two_diagonal_edges=len(physical_sel),
        original_true_cross_edges=len(real_cross),
        selected_true_top_r_Y=len(Ytop),
        true_no_clone_F_real_vertices=len(RQ|Ytop),
        true_no_clone_F_real_edges=len(F),
        actual_F_edge_per_vertex_density=str(Fraction(len(F),len(RQ|Ytop))),
        physical_top_r_density_lower=str(Fraction(len(S),4*n)),
        sharp_top_r_average_lower=str(Fraction(len(real_cross)*r,n)),
        previous_chunk_proof_uses_at_most_half_of_new_lower=True,
        all_selected_source_flags_doubly_bichromatic=True,
        all_F_edges_have_unique_original_owner=True,
        all_source_J_independence_verified=True,
        direct_C6_all_original_six_ID_inverse_proper=_source_cycle_check(F,model),
        root_PROVED_A=False)


def _canonical(v):
    v=tuple(v)
    if len(v)!=6 or len(set(v))!=6:
        raise ValueError("not a simple physical six-cycle")
    return min(tuple(w[i:]+w[:i]) for w in (v,v[::-1]) for i in range(6))


def _source_cycle_check(F,model):
    """Graph-first REAL C6, exact source sixset uniqueness (may be empty)."""
    adj=defaultdict(set)
    for u,v in F:
        adj[u].add(v);adj[v].add(u)
    seen=set()
    for start in sorted(adj):
        stack=[(start,)]
        while stack:
            path=stack.pop()
            if len(path)==6:
                if start in adj[path[-1]]:
                    seen.add(_canonical(path))
                continue
            for v in adj[path[-1]]:
                if v not in path and v>=start:
                    stack.append(path+(v,))
    original_sixsets=set()
    for walk in seen:
        if len({v[0] for v in walk})!=6 or len({v[1] for v in walk})!=6:
            raise AssertionError("C6 in source-J-free twice-cut F not coordinate proper")
        ids=tuple(model["physical"][_edge(walk[j],walk[(j+1)%6])]
                  for j in range(6))
        if len(set(ids))!=6 or len(
                {model["flags"][i][0] for i in ids})!=6 or len(
                {model["flags"][i][1] for i in ids})!=6:
            raise AssertionError("physical C6 is not SIX different ORIGINAL flags")
        ss=frozenset(ids)
        if ss in original_sixsets:
            raise AssertionError("two REAL F-C6 collapse onto same ORIGINAL sixset")
        original_sixsets.add(ss)
    return dict(real_F_simple_unoriented_C6=len(seen),
                corresponding_distinct_original_D6_sixsets=len(original_sixsets))


def weighted_bipartite_top_r_falsifier():
    """Abstract worst-case graph-average equality, SEPARATE from GQ."""
    R=[("heavy",i) for i in range(2)]
    Y=[("other",i) for i in range(4)]
    # Four actual unique physical edges, one per Y with exact equal weights.
    edges={(R[i%2],Y[i]) for i in range(4)}
    deg=Counter(y for _,y in edges)
    chosen=sorted(Y,key=lambda y:(-deg[y],y))[:2]
    surviving=sum(y in chosen for _,y in edges)
    if surviving!=2 or Fraction(surviving,len(edges))!=Fraction(len(R),len(Y)):
        raise AssertionError("unrounded weighted prefix top-r sharpness lost")
    # General exhaustive EVERY 2x4 simple bipartite edge set; proof input
    # only uses degree nonnegativity, never symplectic geometry here.
    verified=0
    for mask in range(1,1<<(len(R)*len(Y))):
        E={(R[i],Y[j]) for i in range(2) for j in range(4)
           if mask&(1<<(i*4+j))}
        d=Counter(y for _,y in E)
        winners=sorted(Y,key=lambda y:(-d[y],y))[:2]
        kept=sum(y in winners for _,y in E)
        if kept*len(Y)<len(E)*len(R):
            raise AssertionError("direct top-r graph averaging inequality false")
        verified+=1
    return dict(abstract_bipartite_graphs_exhausted=verified,
                exact_equality_witness_2_by_4=True,
                extra_half_from_old_chunk_bound_not_required=True)


def certificate():
    formal=[exact_formal_comparison(*v) for v in (
        (Fraction(1),Fraction(1)),
        (Fraction(2),Fraction(1,5)),
        (Fraction(7,3),Fraction(1,17)))]
    real=[]
    for s,mode in ((2,"lex"),(2,"reverse"),(2,"shift"),
                   (4,"lex"),(4,"reverse"),(4,"shift")):
        model=source_j_and_physical(genuine_source(s,mode))
        trial=[physical_heavy_top_degree_referee(model,T)
               for T in (0,1,2,3)]
        positive=[x for x in trial if x["HEAVY_nonvacuous"]]
        if not positive:
            raise AssertionError("original GQ case has no genuine heavy witnesses")
        real.append(dict(s=s,mode=mode,
                         original_flag_count=len(model["flags"]),
                         all_original_source_edges=len(model["physical"]),
                         real_full_J_edges=model["eJ"],
                         true_original_heavy_cases=trial))
    return dict(schema=SCHEMA,issue=230,parent_pr=775,status=ROOT_STATUS,
                independently_derived_all_h_original_heavy_top_r_no_clone=True,
                new_all_h_top_r_without_old_chunk_ceil_factor_2=True,
                precise_fixed_H32_R=improved_R(H_FIXED),
                previous_source_R=OLD_R,
                new_exact_improvement_in_heavy_delta=str(
                    Fraction(OLD_R,improved_R(H_FIXED))**6),
                all_h_source_J_bound_from_parent_775_used_with_explicit_scope=True,
                all_h_full_original_HEAVY_owner_and_selected_F_lemma_PROVED_in_manuscript=True,
                all_h_external_C6_application_only_with_unknown_existential_constants=True,
                all_h_selected_C6_to_original_D6_requires_parent_772=True,
                full_ROOT_PROVED_A=False,ASET_exponent_claimed=False,
                original_BBo_LOW_global_moment_prerequisites_STILL_OPEN=True,
                abstract_source_free_bipartite_prefix_counterfactual=weighted_bipartite_top_r_falsifier(),
                real_original_W32_W34_heavy_true_physical_cases=real,
                formal_ROOT_H32_K10_same_low_with_better_heavy_top_r=formal)


if __name__=="__main__":
    print("AA4_HEAVY_TOP_R_CERTIFICATE="+json.dumps(
        certificate(),sort_keys=True,separators=(",",":")))
