"""HYP-105 AA4-CWSHARP: independently prove and falsify a stronger
ORIGINAL source-pair conflict / Caro-Wei / heavy-tail balanced chunk bridge.

ALL-h analytical source bound at dyadic s>=64:
  Cs=(s²+1)(s²+a-2) <= (6/5)s^4,
where minimal a* is exact for the true W(3,s), with
a*<=ceil((3/2)*s*sqrt(s))<=97/64*s*sqrt(s).

For 0<epsilon<=4 and E_T>=epsilon*s4, actual heavy original IDs
L>=E_T/2>=epsilon*s4/2. Source conflict edges <=2Cs.
Caro-Wei + TWO typed whole-flag binary cuts retain
  |I_G| >=L²/[4*(4Cs+L)] >= beta_new*s4,
  beta_new=5*epsilon²/(384+40*epsilon),
strictly improving historical beta_old=epsilon²/128.
The actual no-clone F from #684 thus has
  e(F)/v(F)>=beta_new*s/32,
  T>=2^19*C_graph^3/beta_new³
  => D6>=c_graph*(beta_new/32)^6*s6.
C_graph,c_graph are UNKNOWN existential theorem constants.
Never assert new all-h exponent or entire root proof acceptance.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt
from collections import Counter,defaultdict

from hyp105_full_physical_degree_tail import genuine_source


def minimum_original_alphabet(V):
    if type(V) is not int or V<1:raise ValueError("positive original factor count needed")
    a=(1+isqrt(1+8*V))//2
    while comb(a,2)<V:a+=1
    while a>2 and comb(a-1,2)>=V:a-=1
    return a


def true_original_source_book_symbolic(s):
    """Exact source constants, rational all-h UPPER certificate."""
    if type(s) is not int or s<64 or s&(s-1):
        raise ValueError("true dyadic parameter s=2^h>=64 required")
    V=(s+1)*(s*s+1)
    N=(s+1)*V
    a=minimum_original_alphabet(V)
    Cs=(s*s+1)*(s*s+a-2)
    # 1.5s sqrt(s) need no floating point at all:
    # a <= ceil(3*s*sqrt(s)/2) <= (97/64)s sqrt(s).
    # Certificate first inequality via exact squaring of bounds:
    if (2*a-2)**2>9*s**3+4*(2*a-2):
        # Not used as proof; verify with exact rational square separately below.
        pass
    # Bound a <= 97*s*sqrt(s)/64 iff (64*a)^2<=97²*s³.
    if (64*a)**2>97**2*s**3:
        raise AssertionError("minimal alphabet prior #690 envelope violated")
    rho=Fraction(4097*609,4096*512)
    if rho>=Fraction(6,5):
        raise AssertionError("symbolic s=64 envelope must be below 6/5")
    if Fraction(Cs,s**4)>rho:
        raise AssertionError("true original Cs violates certified all-h formula")
    return {
        "s":s,"V":V,"N":N,"a_minimal":a,"Cs_exact":Cs,
        "Cs_over_s4":Fraction(Cs,s**4),
        "uniform_rho_analytic":rho,"all_h_Cs_bound":Fraction(6,5),
        "rho_lt_six_fifths":True,
        "main_n2N_actual_original_paired_physical_edges":2*N,
        "source_spectral_Cs_bound_REQUIRES_true_GQ_incidence":True,
    }


def exact_source_selector_bridge(epsilon,C_graph,c_graph=1):
    """Analytic heavy-tail stronger Caro-Wei beta and conditional graph gate.

    All inputs are EXACT rational hypothetical trial graph constants.
    Real published values C_graph,c_graph are intentionally UNKNOWN.
    """
    vals=(epsilon,C_graph,c_graph)
    if any(type(q) not in (int,Fraction) or Fraction(q)<=0 for q in vals):
        raise ValueError("positive exact rational epsilon,C_graph,c_graph needed")
    eps,C,c=map(Fraction,vals)
    if eps>4:raise ValueError("no heavy premise possible beyond 2N<=4s4")
    rho=Fraction(6,5)
    beta=eps*eps/(64*rho+8*eps)
    old=eps*eps/128
    if not beta>=old:
        raise AssertionError("new original-source selector beta below historical")
    # Rounding up the symbolic threshold to integer is allowed later;
    # preserve exact rational for mathematical truth.
    newT=Fraction(2**19)*C**3/beta**3
    oldT=Fraction(2**19)*C**3/old**3
    newD6=c*(beta/32)**6
    oldD6=c*(old/32)**6
    if newT>oldT or newD6<oldD6:
        raise AssertionError("strengthened source beta fails monotone chunk transfer")
    return {
        "epsilon":eps,"hypothetical_graph_C":C,"hypothetical_graph_c":c,
        "original_uniform_book_rho":rho,
        "old_beta":old,"new_beta":beta,
        "new_to_old_source_retention_factor":beta/old,
        "old_symbolic_T_threshold":oldT,
        "new_symbolic_T_threshold":newT,
        "new_T_over_old_T":newT/oldT,
        "old_original_D6_coefficient":oldD6,
        "new_original_D6_coefficient":newD6,
        "new_D6_over_old_D6":newD6/oldD6,
        "all_h_original_source_lower_requires_actual_full_heavy_E_T":True,
        "graph_constants_are_hypothetical_not_published_values":True,
        "not_a_full_Branch_A_acceptance":True,
    }


def _original_source_full_physical(flags,f,g):
    """Raw true original physical edges; unique ORIGINAL ID ownership."""
    adjacency=defaultdict(set)
    owners={}
    diag={}
    for i,(p,l) in enumerate(flags):
        x,z=f[p];y,w=g[l]
        edges=(frozenset(((x,y),(z,w))),frozenset(((x,w),(z,y))))
        if len(set(edges))!=2:
            raise AssertionError("original source flag diagonals collapse")
        for e in edges:
            if len(e)!=2 or e in owners:
                raise AssertionError("global original source flag owner duplicated")
            owners[e]=i
            u,v=tuple(e)
            adjacency[u].add(v);adjacency[v].add(u)
        diag[i]=edges
    return dict(adjacency),owners,diag


def _independent_conflict_census(ids, flags,f,g):
    """TWO independent ORIGINAL flag conflict definitions, no old helpers."""
    I=tuple(ids)
    graph={i:set() for i in I}
    by_point=defaultdict(list)
    by_line=defaultdict(list)
    for i in I:
        p,l=flags[i];by_point[p].append(i);by_line[l].append(i)
    bucket=Counter()
    for p,idx in by_point.items():
        for i in idx:
            for y in g[flags[i][1]]:bucket[("p",p,y)]+=1
    for l,idx in by_line.items():
        for i in idx:
            for x in f[flags[i][0]]:bucket[("l",l,x)]+=1
    bpoint=sum(comb(n,2) for (kind,_,_),n in bucket.items() if kind=="p")
    bline=sum(comb(n,2) for (kind,_,_),n in bucket.items() if kind=="l")
    point=line=0
    for i,j in combinations(I,2):
        p,l=flags[i];q,m=flags[j]
        a=(p==q and bool(set(g[l])&set(g[m])))
        b=(l==m and bool(set(f[p])&set(f[q])))
        if a and b:raise AssertionError("two different actual original source IDs share entire flag")
        if a or b:graph[i].add(j);graph[j].add(i)
        point+=a;line+=b
    if bpoint!=point or bline!=line:
        raise AssertionError("independent source-flag pair-major and pencil bucket conflicts disagree")
    return graph,point,line


def _min_degree_constructive_cw(conflicts):
    """Greedy min-induced-degree independent source IDs, exact CW guarantee.

    At each iteration chosen minimum induced degree v: the removed
    v+N(v) original weights sum_{u in closed(v)} 1/(d_original(u)+1)
    <=1 by d_original(u)>=d_induced(v). Thus >=CW initially.
    """
    out=[]
    remain=set(conflicts)
    while remain:
        u=min(remain,key=lambda i:(len(conflicts[i]&remain),i))
        out.append(u)
        remain.difference_update({u}|conflicts[u])
    CW=sum((Fraction(1,len(ns)+1) for ns in conflicts.values()),Fraction())
    if len(out)<CW or any(j in conflicts[i] for i,j in combinations(out,2)):
        raise AssertionError("constructive Caro-Wei source independence invalid")
    return tuple(out),CW


def _conditional_typed_cut(ids,flags,labels,side,a):
    """Independent deterministic conditional expectation of each typed cut.

    Expected retained flags =half current flags; classify pair label
    as satisfied if both colored and disagree, else probability=1/2.
    """
    known={}
    for x in range(a):
        def score():
            passed=0
            for i in ids:
                u,v=labels[flags[i][side]]
                if u in known and v in known:
                    passed+=2*(known[u]!=known[v])
                else:
                    passed+=1
            return passed
        known[x]=0;zero=score()
        known[x]=1;one=score()
        known[x]=1 if one>zero else 0
    kept=tuple(i for i in ids if known[labels[flags[i][side]][0]]
                                !=known[labels[flags[i][side]][1]])
    if 2*len(kept)<len(ids):
        raise AssertionError("deterministic original whole-flag half-cut guarantee invalid")
    return kept,tuple(known[x] for x in range(a))


def independent_true_source_heavy_cw_referee(power,f,g,T):
    """TRUE original W32/W34 finite heavy source selector & witness ledger.

    Recomputes from actual original IDs (not old selector outputs).
    The universal s>=64 coefficient is a separate symbolic theorem;
    W32/W34 are falsification checks on exact finite combinatorics.
    """
    if type(power) is not int or power not in (1,2):
        raise ValueError("real finite original GQ only h=1,2")
    if type(T) not in (int,Fraction) or Fraction(T)<=0:
        raise ValueError("positive exact rational original FULL degree threshold")
    s,V,flags=genuine_source(power)
    a=minimum_original_alphabet(V)
    legal=set(combinations(range(a),2))
    try:f=tuple(tuple(p) for p in f);g=tuple(tuple(p) for p in g)
    except (TypeError,ValueError):raise ValueError("invalid typed original maps")
    if (len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V or
        any(x not in legal for x in f+g)):
        raise ValueError("complete separately injected f,g in minimal physical alphabet")
    H,owners,diags=_original_source_full_physical(flags,f,g)
    Q={v for v in H if len(H[v])>Fraction(T)*s}
    heavyedges={e for e in owners if any(v in Q for v in e)}
    flagwitness={i:min((tuple(sorted(e)) for e in pair if e in heavyedges),
                       default=None) for i,pair in diags.items()}
    flagwitness={i:e for i,e in flagwitness.items() if e is not None}
    I=tuple(sorted(flagwitness))
    if 2*len(I)<len(heavyedges):
        raise AssertionError("actual heavy FULL physical edges lost ORIG IDs")
    conflicts,mg,mf=_independent_conflict_census(I,flags,f,g)
    C=(s*s+1)*(s*s+a-2)
    if mg>C or mf>C:
        raise AssertionError("actual ORIGINAL pencil books exceed spectral Cs")
    independent,CW=_min_degree_constructive_cw(conflicts)
    lc_selected,lc=_conditional_typed_cut(independent,flags,f,0,a)
    selected,rc=_conditional_typed_cut(lc_selected,flags,g,1,a)
    L=len(I);E=mg+mf
    exactCWfloor=Fraction(L*L,2*E+L) if L else Fraction()
    sourceCsFloor=Fraction(L*L,4*C+L) if L else Fraction()
    if (len(independent)<exactCWfloor or len(independent)<sourceCsFloor or
        4*len(selected)<len(independent)):
        raise AssertionError("actual source CW / two cuts failed")
    # Everything below uses the selected REAL ORIGINAL IDs and
    # their independently checked one assigned heavy physical witness.
    fullHeavyWitness={}
    for i in selected:
        pair=tuple(sorted(flagwitness[i]))
        e=frozenset(pair)
        if owners[e]!=i or not any(v in Q for v in e):
            raise AssertionError("selected ORIGINAL heavy physical witness not preserved")
        p,l=flags[i]
        if lc[f[p][0]]==lc[f[p][1]] or rc[g[l][0]]==rc[g[l][1]]:
            raise AssertionError("selected source flag is not whole-flag bichromatic")
        fullHeavyWitness[i]=pair
    leftSides={0:[],1:[]}
    for i,e in fullHeavyWitness.items():
        u=min(v for v in e if v in Q)
        leftSides[lc[u[0]]].append((i,e,u))
    side=max((0,1),key=lambda z:(len(leftSides[z]),-z))
    R={v for v in Q if lc[v[0]]==side}
    G,Gowners,Gdiags=_original_source_full_physical(
        tuple(flags[i] for i in selected),
        f,g)
    # Gowners are indexed over the compact retained source list; restore
    # REAL original ID owners when auditing the physical selected F.
    reindexed_owner={edge:selected[j] for edge,j in Gowners.items()}
    if len(reindexed_owner)!=2*len(selected):
        raise AssertionError("selected actual two physical diagonals lost")
    Y={v for v in G if lc[v[0]]!=side}
    Eactual=sum(len(G.get(v,set())&Y) for v in R)
    if Eactual<len(leftSides[side]):
        raise AssertionError("source heavy physical witnesses not inside real selected G[R,Y]")
    if R and Y:
        chunks=[tuple(sorted(Y))[j:j+len(R)] for j in range(0,len(Y),len(R))]
        ec=[sum(len(G.get(v,set())&set(c)) for v in R) for c in chunks]
        winner=max(range(len(chunks)),key=lambda j:(ec[j],j))
        num=ec[winner]
        if 2*a*a*num<Eactual*len(R):
            raise AssertionError("genuine no-clone R/Y opposite chunk pigeonhole failed")
        if 4*a*a*num<Eactual*(len(R)+len(chunks[winner])):
            raise AssertionError("genuine no-clone balanced chunk density false")
        chunk={"heavy_R":len(R),"opposite_Y":len(Y),"winner_vertices":len(R)+len(chunks[winner]),
               "winner_edges":num,"full_R_to_Y_edges":Eactual,
               "number_opposite_actual_chunks":len(chunks)}
    else:
        chunk=None
    return {
        "s":s,"original_full_flags":len(flags),
        "original_full_physical_edges":len(owners),
        "full_original_heavy_vertices":len(Q),
        "full_actual_heavy_physical_edges":len(heavyedges),
        "heavy_actual_ORIGINAL_ID_flags":L,
        "actual_original_source_point_pencil_conflicts":mg,
        "actual_original_source_line_pencil_conflicts":mf,
        "original_full_source_Cs_exact":C,
        "actual_source_Caro_Wei_sum":CW,
        "strong_original_conflict_CW_lower":exactCWfloor,
        "symbolic_source_Cs_CW_lower":sourceCsFloor,
        "independent_original_source_flags":len(independent),
        "selected_original_source_flags_after_two_cuts":len(selected),
        "retained_original_owners_both_physical_diagonals":len(reindexed_owner),
        "actual_original_heavy_witnesses_retained":len(fullHeavyWitness),
        "chosen_side_original_heavy_witnesses":len(leftSides[side]),
        "no_cloned_physical_chunk":chunk,
        "not_an_all_h_numeric_W32_W34_proof":True,
    }
