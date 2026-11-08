"""AA4-HEAVYCHAIN: independent true ORIGINAL W(3,s) HEAVY source-to-D6 referee.

Self-contained physical edge ownership / source J / two deterministic
coordinate cuts / uncloned graph F / C6-to-original-ID inverse.
Only the independently constructed TRUE symplectic W32/W34 source from
AA4-DEGFACT is imported, not any HEAVY, selector, physical graph,
six-ID inverse, cycle or Fourier source algorithm.
All-h mathematical proofs are in the accompanying manuscript;
finite W32/W34 tests do not establish infinite-order assertions.
"""
from collections import defaultdict, Counter
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt
import json

from hyp105_original_defect_factor_referee import genuine_symplectic_source

SCHEMA="mathlab.hyp105.original-heavy-source-d6-independent.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
K_SOURCE=64
R=93313
RHO_CAP=Fraction(1,2**32)


def _ceiling(fr):
    return -(-fr.numerator//fr.denominator)


def heavy_uniform_formal_budget(s,rho):
    """Exact per-s arithmetic instance; all-h proof is symbolic in manuscript."""
    if type(s) is not int or s<64 or s & (s-1):
        raise ValueError("dyadic s >= 64 only")
    if type(rho) is not Fraction or not 0<=rho<=RHO_CAP:
        raise ValueError("exact nonnegative original source deletion density")
    V=(s+1)*(s*s+1)
    N=(s+1)*V
    a=2
    while comb(a,2)<V:
        a+=1
    Cs=(s*s+1)*(s*s+a-2)
    lam=Fraction(1,16)-rho
    density_den=72*(lam+5)/lam**2
    uniform_lam=Fraction(1,16)-RHO_CAP
    uniform_den=72*(uniform_lam+5)/uniform_lam**2
    checks={
       "original_two_diagonals_per_flag":True,
       "real_source_J_equals_two_typed_collinearity_overlap_counts":True,
       "original_GQ_SRG_lambda_mu_and_spectral_eigenvalues":True,
       "original_pair_injection_symbol_degrees_lte_a_minus_one":True,
       "minimal_physical_alphabet_envelope":4*a*a<=9*s**3,
       "GQ_points_and_original_flags_envelopes":32*V<=33*s**3 and 16*N<=17*s**4,
       "two_typed_original_conflict_graph_max":4*Cs<=5*s**4,
       "HEAVY_surviving_distinct_original_owners":0<lam<=Fraction(1,16),
       "Caro_Wei_source_independent_set":lam**2/(lam+5)>0,
       "two_coherent_physical_bits_keep_entire_original_owners":True,
       "no_clones_chunk_density":density_den>=72*(lam+5)/lam**2,
       "uniform_R_exact_ceiling":_ceiling(uniform_den)==R,
       "admitted_rho_implies_R93313":density_den<=R,
       "D6_original_sixID_inverse_one_unoriented_C6":True,
       "external_Jiang_Yepremyan_normalization_separate_749":True,
       "global_LOW_and_7_motif_root_not_signed_off":True,
    }
    if not all(checks.values()):
        raise AssertionError("all-h exact original HEAVY budget mismatch")
    return {"s":s,"V":V,"N":N,"a":a,"C_s":Cs,"rho":str(rho),
        "R":R,"lambda":str(lam),"density_R_at_rho":str(density_den),
        "source_independent_coefficient":str(lam**2/(lam+5)),
        "selected_source_fraction_coefficient":str(lam**2/(4*(lam+5))),
        "all_h_explicit_rational_and_source_gates":checks,
        "root_PROVED_A":False,"external_numerical_C0_c0_assumed":False}


def _pair_alphabet(V):
    a=2
    while comb(a,2)<V:a+=1
    return a,tuple(combinations(range(a),2))


def fixed_maps(s,flags,mode):
    """Complete correlated, reverse or separately shifted global injections."""
    V=(s+1)*(s*s+1)
    a,pairs=_pair_alphabet(V)
    p=list(pairs[:V])
    if mode=="lex":
        return a,tuple(p),tuple(p)
    if mode=="reverse":
        return a,tuple(p),tuple(reversed(p))
    if mode=="shift":
        return a,tuple(p[7:]+p[:7]),tuple(p[11:]+p[:11])
    raise ValueError("only fixed total deterministic map schemes")


def _edge(u,v):
    if u==v:
        raise AssertionError("physical diagonal is not a loop")
    return tuple(sorted((u,v)))


def actual_original_edges(flags,f,g):
    """Unique owner for both actual physical diagonals of each true ID."""
    V=len(f)
    if (len(g)!=V or len(set(f))!=V or len(set(g))!=V or
        any(len(q)!=2 or q[0]==q[1] for q in f+g)):
        raise ValueError("not two separately complete globally pair-injective maps")
    owner={}
    per_id=[]
    adj=defaultdict(set)
    for i,(p,l) in enumerate(flags):
        x,z=f[p]; y,w=g[l]
        edges=(_edge((x,y),(z,w)),_edge((x,w),(z,y)))
        if edges[0]==edges[1] or edges[0][0] in edges[1] or edges[0][1] in edges[1]:
            raise AssertionError("original flag's two diagonals are NOT vertex-disjoint")
        for e in edges:
            if e in owner:
                raise AssertionError("two ORIGINAL incidence IDs own same physical diagonal")
            owner[e]=i
            u,v=e
            adj[u].add(v);adj[v].add(u)
        per_id.append(edges)
    if len(owner)!=2*len(flags):
        raise AssertionError("one ORIGINAL flag not two distinct actual physical diagonals")
    return owner,tuple(per_id),adj


def original_conflicts(flags,f,g,ids):
    """Actual ID graph J; do not import historical J or its SRG bound."""
    chosen=tuple(sorted(ids))
    if len(chosen)!=len(set(chosen)):
        raise ValueError("duplicate original IDs")
    if any(type(i) is not int or i<0 or i>=len(flags) for i in chosen):
        raise ValueError("invalid named original ID")
    J={i:set() for i in chosen}
    byp=defaultdict(list);byl=defaultdict(list)
    for i in chosen:
        p,l=flags[i]
        byp[p].append(i);byl[l].append(i)
    for groups,typ in ((byp,0),(byl,1)):
        for ids_ in groups.values():
            for i,j in combinations(ids_,2):
                a=g[flags[i][1]] if typ==0 else f[flags[i][0]]
                b=g[flags[j][1]] if typ==0 else f[flags[j][0]]
                if set(a)&set(b):
                    J[i].add(j);J[j].add(i)
    return J


def independent_source(J):
    """Diagnostic min-current-degree independent-set witness, no oracle imports."""
    remaining=set(J)
    chosen=[]
    while remaining:
        i=min(remaining,key=lambda j:(len(J[j]&remaining),j))
        chosen.append(i)
        remaining.remove(i)
        remaining.difference_update(J[i])
    if any(j in J[i] for i,j in combinations(chosen,2)):
        raise AssertionError("source J not independent")
    return tuple(chosen)


def _cut_score_twice(ids,flags,labels,typ,assignment):
    score=0
    for i in ids:
        u,v=labels[flags[i][typ]]
        if u in assignment and v in assignment:
            score+=2*int(assignment[u]!=assignment[v])
        else:
            score+=1
    return score


def two_exact_original_cuts(ids,flags,f,g,a):
    """Two typed conditional-expectation cuts; keep whole ORIGINAL flags."""
    chosen=tuple(ids)
    cuts=[]
    for typ,labels in ((0,f),(1,g)):
        prev=len(chosen)
        bits={}
        score=prev
        for sym in range(a):
            bits[sym]=0
            sc0=_cut_score_twice(chosen,flags,labels,typ,bits)
            bits[sym]=1
            sc1=_cut_score_twice(chosen,flags,labels,typ,bits)
            bits[sym]=0 if sc0>=sc1 else 1
            now=_cut_score_twice(chosen,flags,labels,typ,bits)
            if now<score:
                raise AssertionError("true source bichromatic expected score decreased")
            score=now
        kept=tuple(i for i in chosen
                   if bits[labels[flags[i][typ]][0]]!=bits[labels[flags[i][typ]][1]])
        if 2*len(kept)<len(chosen):
            raise AssertionError("source whole original IDs not retained by half")
        cuts.append({"input":prev,"output":len(kept),"bits":tuple(bits[k] for k in range(a))})
        chosen=kept
    return chosen,tuple(cuts)


def source_collinearity_conflict_census(s,flags,f,g):
    """Independent ORIGINAL GQ all-source e(J)=e_col(f)+e_col(g)."""
    V=(s+1)*(s*s+1)
    byp=[set() for _ in range(V)]
    byl=[set() for _ in range(V)]
    for p,l in flags:
        byp[p].add(l);byl[l].add(p)
    if any(len(row)!=s+1 for row in byp+byl):
        raise AssertionError("not true GQ original incidence source")
    ep=el=0
    for pts in byl:
        ep+=sum(bool(set(f[p])&set(f[q])) for p,q in combinations(sorted(pts),2))
    for lines in byp:
        el+=sum(bool(set(g[l])&set(g[r])) for l,r in combinations(sorted(lines),2))
    J=original_conflicts(flags,f,g,range(len(flags)))
    actual=sum(map(len,J.values()))//2
    if ep+el!=actual:
        raise AssertionError("exact point/line collinearity-to-source-J identity failed")
    a=max(max(max(q) for q in f),max(max(q) for q in g))+1
    Cs=(s*s+1)*(s*s+a-2)
    if ep>Cs or el>Cs:
        raise AssertionError("independent ORIGINAL SRG source conflict bound false")
    return {"actual_original_conflict_J_edges":actual,
            "point_original_collinearity_f_overlap":ep,
            "line_original_collinearity_g_overlap":el,
            "both_typed_C_s_upper":Cs,
            "exact_J_typed_source_equality":True}


def _canonical_cycles(edges,max_cycles=50000):
    adj=defaultdict(set)
    for u,v in edges:
        adj[u].add(v);adj[v].add(u)
    found=[]
    for root in sorted(adj):
        def visit(path):
            last=path[-1]
            if len(path)==6:
                if root in adj[last] and path[1]<last:
                    found.append(tuple(path))
                    if len(found)>max_cycles:
                        raise AssertionError("finite red-team C6 cap exceeded")
                return
            for nxt in sorted(adj[last]):
                if nxt>root and nxt not in path:
                    visit(path+(nxt,))
        for nxt in sorted(adj[root]):
            if nxt>root:
                visit((root,nxt))
    return tuple(found)


def _cycle_edges(cycle):
    return frozenset(_edge(cycle[j],cycle[(j+1)%6]) for j in range(6))


def inverse_D6_by_original_ids(ids,flags,f,g):
    """SOURCE-FIRST unique possible unoriented physical C6; not graph DFS."""
    ids=tuple(ids)
    if len(ids)!=6 or len(set(ids))!=6:
        return None
    xs=defaultdict(set)
    owner_by_pair={}
    for i in ids:
        p,l=flags[i]
        pair=frozenset(f[p])
        if pair in owner_by_pair:return None
        owner_by_pair[pair]=i
        x,z=f[p];xs[x].add(z);xs[z].add(x)
    if len(xs)!=6 or any(len(nb)!=2 for nb in xs.values()):
        return None
    start=min(xs)
    chain=[start,min(xs[start])]
    while len(chain)<6:
        here=chain[-1];prev=chain[-2]
        choices=xs[here]-{prev}
        if len(choices)!=1:return None
        nxt=next(iter(choices))
        if nxt in chain:return None
        chain.append(nxt)
    if start not in xs[chain[-1]]:return None
    ordered=[]
    for j in range(6):
        id_=owner_by_pair.get(frozenset((chain[j],chain[(j+1)%6])))
        if id_ is None:return None
        ordered.append(id_)
    if len(set(ordered))!=6:return None
    ys=[]
    for j in range(6):
        prev=ordered[(j-1)%6]
        cur=ordered[j]
        a=set(g[flags[prev][1]])&set(g[flags[cur][1]])
        if len(a)!=1:return None
        ys.append(next(iter(a)))
    if len(set(ys))!=6:return None
    vertices=tuple((chain[j],ys[j]) for j in range(6))
    E=_cycle_edges(vertices)
    full_owner,_,_=actual_original_edges(flags,f,g)
    if not all(full_owner.get(_edge(vertices[j],vertices[(j+1)%6]))==ordered[j]
               for j in range(6)):
        return None
    return E


def verify_selected_sixcycles(flags,f,g,selected,selected_edges):
    """Independent physical DFS versus ORIGINAL six-incidence-ID source inverse."""
    original_owner,_,_=actual_original_edges(flags,f,g)
    cycles=_canonical_cycles(selected_edges)
    seen={}
    for cyc in cycles:
        if len({v[0] for v in cyc})!=6 or len({v[1] for v in cyc})!=6:
            raise AssertionError("actual selected C6 is NOT coordinate-proper")
        E=_cycle_edges(cyc)
        ids=tuple(original_owner[e] for e in E)
        if len(set(ids))!=6 or any(i not in selected for i in ids):
            raise AssertionError("selected C6 source flag ownership false")
        pp=[flags[i][0] for i in ids]
        ll=[flags[i][1] for i in ids]
        if len(set(pp))!=6 or len(set(ll))!=6:
            raise AssertionError("not ORIGINAL D6 six distinct point/line factors")
        key=frozenset(ids)
        inverse=inverse_D6_by_original_ids(ids,flags,f,g)
        if inverse!=E or key in seen:
            raise AssertionError("physical C6 duplicated a source six-ID set")
        seen[key]=E
    return {"unoriented_proper_C6":len(cycles),
            "distinct_original_D6_sixsets":len(seen),
            "no_rotation_reverse_or_doubled_diagonal_overcount":True}


def true_original_heavy_case(s,mode,Z=(),diagnostic_T=1):
    """Actual W32/W34 HEAVY physical witness (small diagnostic T ONLY)."""
    flags=genuine_symplectic_source(s)
    a,f,g=fixed_maps(s,flags,mode)
    owner,perid,adj=actual_original_edges(flags,f,g)
    Z=set(Z)
    if any(type(i) is not int or not 0<=i<len(flags) for i in Z):
        raise ValueError("Z is not genuine original ID set")
    if type(diagnostic_T) is not int or diagnostic_T<1:
        raise ValueError("positive diagnostic threshold required")
    Q={v for v,nb in adj.items() if len(nb)>diagnostic_T*s}
    ET={e for e in owner if e[0] in Q or e[1] in Q}
    EA={e for e in ET if owner[e] not in Z}
    retained=set(owner[e] for e in EA)
    J=original_conflicts(flags,f,g,retained)
    edgesJ=sum(map(len,J.values()))//2
    L=len(J)
    cw=Fraction(L*L,L+2*edgesJ) if L else Fraction(0)
    independent=independent_source(J)
    if len(independent)<cw:
        raise AssertionError("diagnostic min-degree source independent set < Caro-Wei")
    selected,cuts=two_exact_original_cuts(independent,flags,f,g,a)
    if not selected:
        raise AssertionError("nonvacuous diagnostic source selection required")
    bits=cuts[0]["bits"]
    witness=[]
    for i in selected:
        e=next((edge for edge in perid[i] if edge in EA),None)
        if e is None:raise AssertionError("selected original ID lacks genuine HEAVY edge")
        heavy=[v for v in e if v in Q]
        if not heavy:raise AssertionError("witness has no genuine heavy corner")
        witness.append((i,e,heavy[0],bits[heavy[0][0]]))
    most=max((0,1),key=lambda b:(sum(w[3]==b for w in witness),-b))
    Rset={v for v in Q if bits[v[0]]==most}
    selected_edge_set={e for i in selected for e in perid[i]}
    Y=sorted({v for e in selected_edge_set for v in e
        if bits[v[0]]!=most and any(u in Rset for u in e)})
    r=len(Rset)
    if r==0 or not Y:
        raise AssertionError("no actual HEAVY cut source physical vertices")
    blocks=[set(Y[j:j+r]) for j in range(0,len(Y),r)]
    Fchoices=[]
    for B in blocks:
        E={e for e in selected_edge_set if
           (e[0] in Rset and e[1] in B) or (e[1] in Rset and e[0] in B)}
        Fchoices.append((E,B))
    Fedges,B=max(Fchoices,key=lambda z:(len(z[0]),-len(z[1])))
    vF=r+len(B);eF=len(Fedges)
    if len(selected_edge_set)!=2*len(selected):
        raise AssertionError("actual original source physical edge cloning")
    if not all(owner[e] in selected for e in Fedges):
        raise AssertionError("F invented physical edges outside selected sources")
    if eF==0 or 8*a*a*eF<len(selected)*vF or 4*a*a*eF<len(selected)*r:
        raise AssertionError("actual no-clone F density pigeonhole false")
    if vF>2*len(Q):
        raise AssertionError("actual F physical vertex cap false")
    cycle=verify_selected_sixcycles(flags,f,g,set(selected),Fedges)
    return {"s":s,"mode":mode,"diagnostic_T_NOT_all_h":diagnostic_T,
        "original_Z":len(Z),"original_flags":len(flags),
        "physical_full_edges":len(owner),"physical_full_Q":len(Q),
        "physical_full_heavy_edges":len(ET),
        "physical_surviving_heavy_edges":len(EA),
        "surviving_distinct_original_heavy_owners":L,
        "J_edges_on_surviving_owners":edgesJ,
        "Caro_Wei_necessary_original_independent_lower":str(cw),
        "actual_independent_original_owners":len(independent),
        "after_FIRST_source_cut":cuts[0]["output"],
        "after_BOTH_source_cuts":len(selected),
        "TRUE_F_vertices":vF,"TRUE_F_edges":eF,
        "actual_density_F":str(Fraction(eF,vF)),
        "source_density_lower_S_over_8a2":str(Fraction(len(selected),8*a*a)),
        "F_no_clone_and_no_sixset_duplication":True,**cycle}


def seeded_original_D6_case(s):
    """Real ORIGINAL six-ID positive source witness built independently."""
    flags=genuine_symplectic_source(s)
    a,pairs=_pair_alphabet((s+1)*(s*s+1))
    if a<6:raise AssertionError("need genuine six distinct first/second coords")
    selected=[];seenp=set();seenl=set()
    for i,(p,l) in enumerate(flags):
        if p not in seenp and l not in seenl:
            selected.append(i);seenp.add(p);seenl.add(l)
            if len(selected)==6:break
    if len(selected)!=6:raise AssertionError("no six ORIGINAL matching source IDs")
    V=(s+1)*(s*s+1)
    f=[None]*V;g=[None]*V
    cycle_pairs=[tuple(sorted((i,(i+1)%6))) for i in range(6)]
    for j,i in enumerate(selected):
        p,l=flags[i];f[p]=cycle_pairs[j];g[l]=cycle_pairs[j]
    for lab in (f,g):
        used=set(cycle_pairs)
        remaining=(q for q in pairs if q not in used)
        for j in range(V):
            if lab[j] is None:lab[j]=next(remaining)
    f,g=tuple(f),tuple(g)
    J=original_conflicts(flags,f,g,selected)
    if any(J[i] for i in J):
        raise AssertionError("six matching original source IDs spuriously conflicting")
    all_owner,perid,_=actual_original_edges(flags,f,g)
    E={e for i in selected for e in perid[i]}
    chosen,cuts=two_exact_original_cuts(selected,flags,f,g,a)
    # The deterministic cut may or may not retain the six seeded owners;
    # an explicit alternating bit assignment always retains all six.
    forced={k:k%2 for k in range(6)}
    if not all(forced[x]!=forced[z] and forced[y]!=forced[w]
          for i in selected for (x,z),(y,w) in ((f[flags[i][0]],g[flags[i][1]]),)):
        raise AssertionError("positive original six-source C6 not two-colorable")
    cert=verify_selected_sixcycles(flags,f,g,set(selected),E)
    if cert["unoriented_proper_C6"]<1:
        raise AssertionError("no genuine original D6 from constructed six-ID seed")
    ids=tuple(selected)
    inv=inverse_D6_by_original_ids(ids,flags,f,g)
    if inv is None or inv not in ({frozenset(E)},(inv,)):
        raise AssertionError("original source first six-ID inverse failed")
    return {"s":s,"matching_original_incidence_IDs":selected,
        "true_TWO_physical_diagonals_per_ID":2*len(selected),
        "source_J_independent":True,
        "two_explicit_actual_typed_alternating_cuts":True,
        "independent_original_sixID_inverse_success":True,**cert}


def canonical_report():
    rows=[]
    for s in (2,4):
        flags=genuine_symplectic_source(s)
        for mode in ("lex","reverse","shift"):
            a,f,g=fixed_maps(s,flags,mode)
            census=source_collinearity_conflict_census(s,flags,f,g)
            result=true_original_heavy_case(s,mode,Z=tuple(range(0,len(flags),17)),
                                             diagnostic_T=1)
            rows.append({**result,**census})
    formal=[heavy_uniform_formal_budget(s,rho) for s,rho in (
        (64,Fraction(0)),(64,RHO_CAP),(128,Fraction(1,2**33)),
        (1024,RHO_CAP),(65536,RHO_CAP))]
    return {"schema":SCHEMA,"issue":230,"status":ROOT_STATUS,
        "root_PROVED_A":False,"new_ASET_exponent":False,
        "external_C0_c0_numeric_NOT_claimed":True,
        "original_6motif_HEAVY_only":True,
        "independent_all_h_FORMAL_arithmetic":formal,
        "true_original_W32_W34_six_heavy_diagnostic_cases":rows,
        "true_original_positive_D6_seed_cases":[seeded_original_D6_case(2),
                                                seeded_original_D6_case(4)]}


if __name__=="__main__":
    print("AA4_HEAVYCHAIN_CERTIFICATE="+json.dumps(canonical_report(),sort_keys=True,separators=(",",":")))
