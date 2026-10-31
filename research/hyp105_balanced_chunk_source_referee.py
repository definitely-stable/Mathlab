"""HYP-105 AA4-CHUNKREF — independent balanced-heavy-chunk and D6 referee.

ALL-h source tail theorem refinement for TRUE W(3,s), every dyadic s>=64,
and EVERY full fixed globally injected (arbitrarily correlated) f,g.

Full physical graph has exactly 2N distinct edges (two diagonals per
ORIGINAL flag) and 4N total degree. Therefore for
Q_T={v: deg_full(v)>T*s}, |Q_T|*T*s<4N<=8s^4, whence

    |Q_T| <= 8 s^3/T.

The old #659 used the needlessly weak |Q_T|<=16s^3/T. For the
same beta=epsilon²/2^7 original-flag coherent selector and the
same selected bipartite graph G, choose the half of the chosen heavy
physical witness edges with their original heavy endpoints on the
same typed left-color side X. These are E>=beta*s^4/2 DISTINCT physical
edges from R=Q_T∩X to the opposite color Y.
Set r=|R|>0, n=a²<=4s³. Divide Y into consecutive disjoint chunks
of size <=r. There are <=ceil(|Y|/r)<=2n/r chunks (no clone).
One genuine subgraph F=G[R,chunk] satisfies

    e(F)>=E*r/(2n)>=beta*r*s/16,
    v(F)<=2r<=16s^3/T,
    e(F)/v(F)>=beta*s/32.

Hence if T>=2^19*C_graph³*beta^-3, i.e.
T>=2^40*C_graph³*epsilon^-6,
then e(F)>=C_graph*v(F)^(4/3). By the PUBLISHED
balanced graph sixcycle supersaturation lemma,
#C6(F)>=c_graph*(beta/32)^6*s^6
       =c_graph*epsilon^12*s^6/2^72.
Every actual physical simple C6(F) is in coherent + two-color cut G,
hence coordinate-proper, has six distinct ORIGINAL flag IDs and is a
historically accepted ORIGINAL GF5 D6. The injection is part of #652
and checked independently on true W32/W34.

The earlier #659 2^41 and #683 T>=2^59*C³ remain valid/conservative.
This NEW all-h proof sharpens the sufficient threshold to 2^40 and
epsilon=1/8 threshold to 2^58*C³ without modifying the parent.

FINITE falsifiers independently select original heavy-source flags,
Caro-Wei original conflict independent flags, and both typed coordinate
binary cuts. They compute a real physical un-cloned balanced chunk,
direct cycle census and exact ORIGINAL D6 six-ID provenance. Finite
W32/W34 calculations do not prove the cited asymptotic external theorem.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb,isqrt


def exact_balanced_chunk(graph, left, right, heavy_left, physical_n=None):
    """Independent balanced chunk pigeonhole, exact edge list and rational check.

    This is a pure ordinary undirected bipartite graph lemma: no GQ.
    R is a nonempty subset of LEFT vertices; Y can include isolates.
    For every such graph, some real, noncloned F=G[R,chunk] satisfies
        e(F)>=E*|R|/(2*n), v(F)<=2|R|,
    where E is number of actual edges between R and Y, n>=|V(G)|.
    When E=0, the lemma still holds (but no SS6 is applied).
    """
    verts=set(graph)
    L,Rside=set(left),set(right)
    heavy=set(heavy_left)
    if not L.isdisjoint(Rside) or L|Rside!=verts or not heavy or not heavy<=L:
        raise ValueError("proper exhaustive typed bipartition and nonempty R required")
    for u,ns in graph.items():
        if u in ns or not set(ns)<=verts or any(u not in graph[v] for v in ns):
            raise ValueError("graph must be simple symmetric closed")
        if any((u in L)==(v in L) for v in ns):
            raise ValueError("graph must be truly bipartite")
    if not Rside:
        raise ValueError("opposite color side Y must have vertices")
    n=len(verts) if physical_n is None else physical_n
    if type(n) is not int or n<len(verts):
        raise ValueError("physical n must bound actual universe")
    r=len(heavy)
    Y=tuple(sorted(Rside))
    R=tuple(sorted(heavy))
    if not r<=n or not len(Y)<=n:
        raise AssertionError("pigeonhole partition preconditions")
    chunks=tuple(Y[k:k+r] for k in range(0,len(Y),r))
    ec=lambda chunk:sum(len(graph[u]&set(chunk)) for u in R)
    counts=tuple(ec(chunk) for chunk in chunks)
    if not counts:
        raise AssertionError("Y side improperly empty")
    winner=max(range(len(chunks)),key=lambda k:(counts[k],tuple(chunks[k])))
    chunk=chunks[winner];edges=counts[winner]
    E=sum(len(graph[u]&Rside) for u in R)
    if sum(counts)!=E:
        raise AssertionError("some REAL heavy edges disappeared or duplicated in chunking")
    if (len(chunks)>-(-len(Y)//r) or len(chunks)*r>2*n or
        2*n*edges<E*r):
        raise AssertionError("genuine no-clone balance pigeonhole failed")
    v=len(R)+len(chunk)
    if not v<=2*r or 4*n*edges<E*v:
        raise AssertionError("balanced chunk density transfer failed")
    return {
        "physical_universe_n":n,
        "heavy_left_size_r":r,"opposite_size_y":len(Y),
        "E_original_distinct_heavy_to_opposite_edges":E,
        "number_actual_chunks":len(chunks),
        "winner_opposite_vertices":tuple(chunk),
        "winner_heavy_vertices":R,
        "winner_actual_edges":edges,
        "winner_actual_vertices":v,
        "winner_edge_density":Fraction(edges,v),
        "source_free_pigeonhole_eF_ge_Er_over_2n":True,
        "source_free_pigeonhole_eF_over_v_ge_E_over_4n":True,
        "no_cloning_of_original_physical_vertices":True,
    }


def strengthened_tail_constants(C,c,epsilon):
    """EXACT conditional arithmetic of improved all-h #659 source tail.

    Inputs C,c are HYPOTHETICAL positive rational stress inputs, never
    asserted actual published C6 supersaturation constants.
    """
    try:
        C,c,epsilon=Fraction(C),Fraction(c),Fraction(epsilon)
    except (TypeError,ValueError,ZeroDivisionError):
        raise ValueError("positive rational inputs required")
    if any(v<=0 for v in (C,c,epsilon)):
        raise ValueError("positive rational inputs required")
    beta=epsilon*epsilon/Fraction(2**7)
    oldthreshold=Fraction(2**41)*C**3/epsilon**6
    newthreshold=Fraction(2**40)*C**3/epsilon**6
    delta=c*epsilon**12/Fraction(2**72)
    # Compute via the true beta and physical chunk, independently of
    # old/new simplified epsilon exponents.
    geometricthreshold=Fraction(2**19)*C**3/beta**3
    if newthreshold!=geometricthreshold or 2*newthreshold!=oldthreshold:
        raise AssertionError("balanced source chunk T coefficient is wrong")
    if Fraction(2**40)*C**3/epsilon**6!=newthreshold or delta<=0:
        raise AssertionError("original D6 supersaturation denominator wrong")
    root_old=Fraction(2**59)*C**3
    root_new=Fraction(2**58)*C**3
    if epsilon==Fraction(1,8) and (
        newthreshold!=root_new or oldthreshold!=root_old):
        raise AssertionError("epsilon=1/8 tail normalization error")
    return {
        "hypothetical_graph_C":str(C),"hypothetical_graph_c":str(c),
        "epsilon":str(epsilon),"beta":beta,
        "old_T_threshold":oldthreshold,
        "new_T_threshold":newthreshold,
        "T_threshold_improvement_exact_factor":Fraction(2),
        "old_original_D6_lower":delta,
        "new_original_D6_lower_unchanged":delta,
        "root_eps_eighth_old_T_threshold":root_old,
        "root_eps_eighth_new_T_threshold":root_new,
        "graph_theorem_constants_are_not_estimated":True,
    }


def _direct_simple_C6(graph):
    """Independent physical unrooted/unoriented simple 6cycle enumerator."""
    found=set()
    for root in sorted(graph):
        def walk(path):
            if len(path)==6:
                if root in graph[path[-1]] and path[1]<path[-1]:
                    found.add(tuple(path))
                return
            for w in sorted(graph[path[-1]]):
                if w>root and w not in path:walk(path+(w,))
        walk((root,))
    return found


def _cut_half_source_ids(ids,flags,labels,source_side,a):
    """Independent conditional-expectation nonrandom typed binary cut."""
    color={}
    def score():
        val=0
        for i in ids:
            x,y=labels[flags[i][source_side]]
            if x in color and y in color:
                val+=2*(color[x]!=color[y])
            else:val+=1
        return val
    for x in range(a):
        color[x]=0;s0=score()
        color[x]=1;s1=score()
        color[x]=int(s1>s0)
    kept=tuple(i for i in ids if
               color[labels[flags[i][source_side]][0]]!=
               color[labels[flags[i][source_side]][1]])
    if len(kept)*2<len(ids):
        raise AssertionError("half-expectation original source ID cut failed")
    return kept,tuple(color[i] for i in range(a))


def independent_true_original_chunk(power,f,g,T,source_subset=None):
    """Independent W32/W34 original-heavy source selector + physical chunk.

    Does NOT invoke #659's finite_tail_selector, coordinate_cut,
    min_degree_independent, verify_selected, or expected JSON fixtures.
    Original geometry and physical edge assembly are shared primitives
    only; conflict and selection are reimplemented source-ID FIRST.
    """
    from hyp105_full_physical_degree_tail import genuine_source,physical,diagonals
    from hyp105_physical_degree_energy import minimal_alphabet,_verify_typed_injections
    from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
    if type(power) is not int or power not in (1,2):
        raise ValueError("true original W32/W34 finite oracle only")
    T=Fraction(T)
    if T<=0:raise ValueError("positive full physical threshold")
    s,V,flags=genuine_source(power)
    a=minimal_alphabet(V)
    f,g=tuple(map(tuple,f)),tuple(map(tuple,g))
    _verify_typed_injections(a,V,f,g)
    full,full_owner=physical(range(len(flags)),flags,f,g)
    Q={v for v in full if len(full[v])>T*s}
    affected={i:tuple(e for e in diagonals(flags[i],f,g)
                      if set(e)&Q) for i in range(len(flags))}
    affected={i:e for i,e in affected.items() if e}
    original_tail_physical_edges={
        e for e in full_owner if set(e)&Q
    }
    if source_subset is None:
        I=tuple(sorted(affected))
    else:
        I=tuple(source_subset)
        if (len(set(I))!=len(I) or
            any(type(i) is not int or i not in affected for i in I)):
            raise ValueError("source subset must be distinct REAL heavy original flags")
    if source_subset is None and 2*len(I)<len(original_tail_physical_edges):
        raise AssertionError("original full physical heavy tail witness capacity broken")
    if not I:
        return {
            "s":s,"original_heavy_flags":0,
            "original_full_heavy_vertices":len(Q),
            "empty_source_tail":True,
            "full_source_physical_degree_sum":sum(len(ns) for ns in full.values()),
        }
    # Independently construct EXACT source conflict graph from ID pairs.
    conflict={i:set() for i in I}
    for i,j in combinations(I,2):
        p,ell=flags[i];q,r=flags[j]
        if ((p==q and bool(set(g[ell])&set(g[r]))) or
            (ell==r and bool(set(f[p])&set(f[q])))):
            conflict[i].add(j);conflict[j].add(i)
    # MIN-DEGREE CURRENT SOURCE GRAPH greedy independent set with Caro--Wei.
    cw=sum((Fraction(1,len(conflict[i])+1) for i in I),Fraction(0))
    rem=set(I);J=[]
    while rem:
        i=min(rem,key=lambda v:(len(conflict[v]&rem),v))
        J.append(i);rem.difference_update({i}|(conflict[i]&rem))
    if Fraction(len(J))<cw:
        raise AssertionError("independent original Caro--Wei guarantee false")
    for i,j in combinations(J,2):
        if j in conflict[i]:
            raise AssertionError("two chosen original flags physically conflict")
    L,lc=_cut_half_source_ids(J,flags,f,0,a)
    selected,rc=_cut_half_source_ids(L,flags,g,1,a)
    if 4*len(selected)*(4*((s*s+1)*(s*s+a-2))+len(I))<len(I)**2:
        raise AssertionError("Caro--Wei and 2 typed cuts root lower failed")
    selected_graph,owner=physical(selected,flags,f,g)
    if len(owner)!=2*len(selected):
        raise AssertionError("original selected flag diagonals not paired")
    # Distinct selected ORIGINAL witness physical edges, each in full Q.
    witnesses={i:min(affected[i]) for i in selected}
    for i,e in witnesses.items():
        if owner[e]!=i or not (set(e)&Q):
            raise AssertionError("some chosen ORIGINAL heavy physical witness lost")
    sides={0:[],1:[]}
    for i,e in witnesses.items():
        v=min(set(e)&Q)
        sides[lc[v[0]]].append((i,e,v))
    chosen=max((0,1),key=lambda side:(len(sides[side]),-side))
    if 2*len(sides[chosen])<len(selected):
        raise AssertionError("one physical left-color side misses half witnesses")
    R={v for v in Q if lc[v[0]]==chosen}
    Y={v for v in selected_graph if lc[v[0]]!=chosen}
    if not R or not Y:
        raise AssertionError("positive selected true-heavy witness lost a bipartition")
    gridgraph={v:set() for v in R|Y}
    for v in R:
        gridgraph[v]=selected_graph.get(v,set())&Y
        for w in gridgraph[v]:gridgraph[w].add(v)
    chunk=exact_balanced_chunk(
        gridgraph,R,Y,heavy_left=R,physical_n=a*a)
    if chunk["E_original_distinct_heavy_to_opposite_edges"]<len(sides[chosen]):
        raise AssertionError("true original selected heavy witness not in source chunk")
    if 2*len(Q)*T*s>=8*s**4:
        # This coarse #659/#684 bound only guaranteed s>=64,
        # not at the small W32/W34 direct falsifier sizes.
        pass
    r=chunk["heavy_left_size_r"];E=chunk["E_original_distinct_heavy_to_opposite_edges"]
    if not Fraction(E,1)>=Fraction(len(selected),2):
        raise AssertionError("genuine selected source heavy witness side count false")
    # Independent direct C6 census of whole selected graph, then of
    # the REAL UNCLONED balanced F, preserving original flag labels.
    realF={v:set() for v in chunk["winner_heavy_vertices"]+
                             chunk["winner_opposite_vertices"]}
    for v in chunk["winner_heavy_vertices"]:
        for w in selected_graph.get(v,set())&set(chunk["winner_opposite_vertices"]):
            realF[v].add(w);realF[w].add(v)
    cwhole=_direct_simple_C6(selected_graph)
    cF=_direct_simple_C6(realF)
    seen=set()
    for cycle in cwhole:
        if len({v[0] for v in cycle})!=6 or len({v[1] for v in cycle})!=6:
            raise AssertionError("coherent plus typed cut cycle not coordinate-proper")
        original=tuple(sorted(owner[tuple(sorted((cycle[j],cycle[(j+1)%6])))]
                              for j in range(6)))
        if (len(set(original))!=6 or
            len({flags[i][0] for i in original})!=6 or
            len({flags[i][1] for i in original})!=6):
            raise AssertionError("physical cycle not six ORIGINAL source factors")
        if original in seen:
            raise AssertionError("physical C6 maps noninjectively to ORIGINAL D6")
        seen.add(original)
        if classify_seven_prechecked(original,f,g,flags)!="D6":
            raise AssertionError("physical C6 not accepted historical original D6")
    if len(cF)>len(cwhole):
        raise AssertionError("physical chunk creates cycles not in selected original G")
    return {
        "s":s,"V":V,"a":a,"full_original_flag_count":len(flags),
        "original_full_heavy_vertices":len(Q),
        "original_full_heavy_physical_edges":len(original_tail_physical_edges),
        "original_heavy_flags":len(I),
        "original_Caro_Wei_expectation":cw,
        "original_independent_flag_count":len(J),
        "after_first_typed_cut":len(L),
        "after_second_typed_cut":len(selected),
        "selected_both_original_diagonals":True,
        "independent_source_witness_count":len(witnesses),
        "heavy_original_source_witnesses_side":len(sides[chosen]),
        "balanced_chunk":chunk,
        "actual_selected_physical_C6":len(cwhole),
        "actual_selected_ORIGINAL_D6_unique_sixsets":len(seen),
        "actual_balanced_F_C6":len(cF),
        "actual_balanced_F_v":len(realF),
        "actual_balanced_F_e":sum(map(len,realF.values()))//2,
        "real_original_W3_source_not_all_h_proof":True,
    }
