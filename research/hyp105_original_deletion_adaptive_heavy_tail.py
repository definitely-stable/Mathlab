r"""AA4-ZTAIL: original-ID deletion-robust, instance-adaptive HEAVY C6 gate.

NEW exact ALL-N deterministic quantitative algebra lemma:
FULL fixed globally injected (possibly correlated) symplectic physical
f,g have 2N original flag owned real edges; freeze physical heavy set
Q_T from FULL H before deleting ANY original source flag IDs Z.
E_A = true physical full-heavy edges still owned by A=I\Z and
L = count of their DISTINCT original source owners.
Then E_A>=E_FULL-2|Z|, L>=ceil(E_A/2), q=|Q_T|.

Let e_J be the ACTUAL number of conflicting pairs among the L TRUE
ORIGINAL heavy flag owners (not synthetic edge/coordinate IDs).
Source-flag Caro-Wei gives a coherent ORIGINAL independent set
J>=L²/(L+2e_J), two independent deterministic conditional-expectation
coordinate cuts retain >= J/4 original flag IDs and BOTH true physical
diagonals. Give one heavy REAL physical witness per retained ORIGINAL
flag (never duplicated). Pigeonhole assigns >= m/2 distinct witnesses
to heavy endpoints on the SAME typed left-color side. Split the actual
opposite side into non-cloned chunks <=r actual heavy side vertices,
choose maximum ORIGINAL-source physical edge count chunk F.

For n=a² FULL physical vertex universe, the resulting ACTUAL simple
bipartite graph F (possibly retaining only one diagonal of source flag)
has e(F)/v(F)>= L²/[32*n*(L+2e_J)], v(F)<=2q.
Thus the following completely DATA-ADAPTIVE external SS6 threshold
is sufficient:
    L^6 >= 2^16 * C_graph^3 * n^3 * q * (L+2e_J)^3.
If true for the ACTUAL published (unknown!) C_graph, then the published
r=2,k=3 theorem gives at least
    c_graph * [ L²/(32*n*(L+2e_J)) ]^6
true ORIGINAL source-ID-disjoint *within each sixset* GF(5)-positive D6.
No claim that C_graph=c_graph=1, no numerical finite-h acceptance
without supplying REAL authoritative bounds on external constants.

NEW robust all-h COROLLARY for ANY arbitrary deleted ORIGINAL Z:
if s>=64, E_FULL>=2|Z|+epsilon*s^4 and
    T>=2^40*C_graph^3*epsilon^-6,
then D6_avoid(Z) >= c_graph*epsilon^12/2^72*s^6.
The T exponent 40 uses already proved #684 improved full physical
|Q|<=8s^3/T (not old #659 16s^3/T). For root #674's
epsilon_full=1/8, |Z|<=rho*s^4<=s^4/32, choose epsilon=1/16:
    T_new=2^64*C_graph^3,
versus frozen #674 conservative 2^65*C_graph^3. This halves the
SOURCE heavy threshold only. Re-deriving all OTHER all-h geometric
low-tail/path dependencies requires independent scientific review;
this is not a proof of root #230 all-h Branch A.

All true original W32/W34 source/correlation and selected physical
graph finite witnesses independently audited with actual original IDs.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_full_physical_degree_tail import genuine_source
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked

ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"


def _complete_true_original(power,f,g,Z,T):
    if type(power) is not int or power not in (1,2):
        raise ValueError("only genuine original symplectic W(3,2) or W(3,4) finite sources")
    s,V,flags=genuine_source(power)
    a=2
    while comb(a,2)<V:a+=1
    legal=set(combinations(range(a),2))
    f=tuple(tuple(p) for p in f)
    g=tuple(tuple(p) for p in g)
    if (len(f)!=V or len(g)!=V or len(set(f))!=V or
        len(set(g))!=V or any(x not in legal for x in f+g)):
        raise ValueError("both typed factor pair maps must be globally complete/injected")
    Z=tuple(Z)
    if (len(set(Z))!=len(Z) or
        any(type(i) is not int or not 0<=i<len(flags) for i in Z)):
        raise ValueError("only distinct true original incidence flag IDs can be deleted")
    T=Fraction(T)
    if T<=0:raise ValueError("positive exact physical heavy degree threshold T")
    return s,V,a,tuple(flags),f,g,tuple(sorted(Z)),T


def _owned_physical(flags,f,g,ids):
    owner={}
    adjacency=defaultdict(set)
    for i in ids:
        p,l=flags[i];x,k=f[p];y,w=g[l]
        for v,u in (((x,y),(k,w)),((x,w),(k,y))):
            if v==u:raise AssertionError("true original physical diagonal has self-loop")
            edge=tuple(sorted((v,u)))
            if edge in owner:raise AssertionError("two ORIGINAL flag owners for same physical edge")
            owner[edge]=i
            adjacency[v].add(u);adjacency[u].add(v)
    if len(owner)!=2*len(ids) or sum(map(len,adjacency.values()))!=4*len(ids):
        raise AssertionError("not TWO genuine original diagonals per source incidence flag")
    return {v:frozenset(ns) for v,ns in adjacency.items()},owner


def _true_source_conflict(flags,f,g,I):
    I=tuple(I)
    J={i:set() for i in I}
    for i,j in combinations(I,2):
        p,l=flags[i];q,r=flags[j]
        if ((p==q and set(g[l])&set(g[r])) or
            (l==r and set(f[p])&set(f[q]))):
            J[i].add(j);J[j].add(i)
    return J


def _caro_wei_original_independent(J):
    weighted=sum((Fraction(1,len(nbs)+1) for nbs in J.values()),Fraction())
    remaining=set(J)
    chosen=[]
    while remaining:
        winner=min(remaining,key=lambda i:(len(J[i]&remaining),i))
        chosen.append(winner)
        remaining.difference_update({winner}|J[winner])
    if len(chosen)<weighted or any(v in J[u] for u,v in combinations(chosen,2)):
        raise AssertionError("true ORIGINAL source min-current-degree selection violated Caro Wei")
    return tuple(sorted(chosen)),weighted


def _two_cut_conditional(flags,labels,I,side,a):
    """Deterministic original whole-flag 1/2 keep via exact conditional expectation."""
    bits=[None]*a
    I=tuple(I)
    def doubled_expectation():
        score=0
        for i in I:
            p=flags[i][side]
            u,v=labels[p]
            if bits[u] is None or bits[v] is None:
                score+=1
            else:
                score+=2*(bits[u]!=bits[v])
        return score
    old=doubled_expectation()
    for x in range(a):
        bits[x]=0;p0=doubled_expectation()
        bits[x]=1;p1=doubled_expectation()
        bits[x]=0 if p0>=p1 else 1
        if max(p0,p1)<old:
            raise AssertionError("loss of original source expected bichromatic cut")
        old=max(p0,p1)
    chosen=tuple(i for i in I if bits[labels[flags[i][side]][0]]!=
                 bits[labels[flags[i][side]][1]])
    if 2*len(chosen)<len(I):
        raise AssertionError("original source physical typed coordinate cut lost >1/2")
    return chosen,tuple(bits)


def _simple_unoriented_physical_C6(adjacency):
    cycles=[]
    for start in sorted(adjacency):
        def visit(path):
            if len(path)==6:
                if start in adjacency[path[-1]] and path[1]<path[-1]:
                    cycles.append(path)
                return
            for nxt in adjacency[path[-1]]:
                if nxt>start and nxt not in path:
                    visit(path+(nxt,))
        visit((start,))
    return tuple(cycles)


def _local_balanced_no_clone(Fgraph,R,Y,physical_n):
    """Independent from existing #684 exact_balanced_chunk for crosscheck."""
    if not R or not Y:
        return None
    r=len(R)
    chunksets=[tuple(sorted(Y))[j:j+r] for j in range(0,len(Y),r)]
    if not chunksets or len(chunksets)*r>2*physical_n:
        raise AssertionError("cannot create true physical no-clone balanced chunk")
    records=[]
    for chunk in chunksets:
        E=tuple(sorted((u,v) for u in sorted(R) for v in chunk
                       if v in Fgraph.get(u,())))
        records.append((len(E),chunk,E))
    _num,win,actual=max(records,key=lambda z:(z[0],tuple(-v[0]*100000-v[1] for v in z[1])))
    E=sum(len(Fgraph.get(u,())&set(Y)) for u in R)
    if len(actual)*2*physical_n<E*r:
        raise AssertionError("true balanced chunk source edge pigeonhole false")
    actual_verts=tuple(sorted(set(R)|set(win)))
    return {
        "heavy_R_original_physical_vertices":len(R),
        "physical_opposite_side_vertices":len(Y),
        "physical_nonclone_original_chunk_count":len(records),
        "edges_between_heavyR_and_Y":E,
        "winner_ordinary_subgraph_edges":len(actual),
        "winner_ordinary_subgraph_vertices":len(actual_verts),
        "winner_original_physical_vertices":[list(v) for v in actual_verts],
        "winner_actual_physical_edges":[[list(u),list(v)] for u,v in actual],
        "no_clone_bipartite_chunk":True,
        "source_chunk_e_over_v":str(Fraction(len(actual),len(actual_verts))),
        "source_chunk_actual_E_to_r_pigeonhole_verified":True,
    }


def _real_original_selector_adaptive_heavy(power,f,g,deleted_ids,T):
    s,V,a,flags,f,g,Z,T=_complete_true_original(power,f,g,deleted_ids,T)
    allids=tuple(range(len(flags)))
    remain=tuple(i for i in allids if i not in set(Z))
    physical,owner=_owned_physical(flags,f,g,allids)
    Q={v for v,neighbors in physical.items() if len(neighbors)>T*s}
    full_tail_edges={edge for edge in owner if any(v in Q for v in edge)}
    nondeleted_tail_edges={edge for edge in full_tail_edges if owner[edge] not in Z}
    # EXACT per-original-source two diagonal deletion loss.
    lost=sum(owner[e] in Z for e in full_tail_edges)
    if lost>2*len(Z) or len(nondeleted_tail_edges)!=len(full_tail_edges)-lost:
        raise AssertionError("deleted original source owner heavy edge count invalid")
    I=tuple(sorted(set(owner[e] for e in nondeleted_tail_edges)))
    if len(I)*2<len(nondeleted_tail_edges):
        raise AssertionError("true heavy original source flags do not cover all heavy edges")
    if not I:
        return {
            "schema":"mathlab.hyp105.original-adaptive-Z-robust-balanced-SS6.v1",
            "s":s,"scheme":None,"original_source_flags":len(allids),
            "deleted_original_flag_IDs":list(Z),
            "full_original_QT_vertices":len(Q),
            "full_original_tail_edges":len(full_tail_edges),
            "original_tail_edges_remaining_after_Z":0,
            "retained_heavy_original_flag_IDs":[],
            "empty_tail":True,
            "root_230_status":ROOT_STATUS,
            "root_allh_Branch_A_proved_here":False,
        }
    J=_true_source_conflict(flags,f,g,I)
    eI=sum(map(len,J.values()))//2
    chosen,CW=_caro_wei_original_independent(J)
    left,lb=_two_cut_conditional(flags,f,chosen,0,a)
    selected,rb=_two_cut_conditional(flags,g,left,1,a)
    seladj,selowner=_owned_physical(flags,f,g,selected)
    if 4*len(selected)*(len(I)+2*eI)<len(I)**2:
        raise AssertionError("source-adaptive exact Caro Wei and two-cut inequality violated")
    selected_witness={}
    for i in selected:
        edges=tuple(e for e in nondeleted_tail_edges if owner[e]==i)
        if not edges:
            raise AssertionError("selected source owner has no ORIGINAL full-Q heavy edge")
        selected_witness[i]=min(edges)
    sides={0:[],1:[]}
    for i,e in selected_witness.items():
        v=min((x for x in e if x in Q))
        sides[lb[v[0]]].append((i,e,v))
    chosen_side=max((0,1),key=lambda x:(len(sides[x]),-x))
    heavyR={v for v in Q if lb[v[0]]==chosen_side}
    oppositeY={v for v in seladj if lb[v[0]]!=chosen_side}
    original_cell_graph={v:set() for v in heavyR|oppositeY}
    for u in heavyR:
        for v in set(seladj.get(u,())) & oppositeY:
            original_cell_graph[u].add(v)
            original_cell_graph[v].add(u)
    win=_local_balanced_no_clone(original_cell_graph,heavyR,oppositeY,a*a)
    if win is None:
        raise AssertionError("retained original heavy source flag lost real physical witness")
    E=win["edges_between_heavyR_and_Y"]
    if E*2<len(selected):
        raise AssertionError("at least half original source heavy flags have wrong physical side")
    winnerEdges=[(tuple(u),tuple(v)) for u,v in win["winner_actual_physical_edges"]]
    winnerAdj=defaultdict(set)
    for u,v in winnerEdges:
        winnerAdj[u].add(v);winnerAdj[v].add(u)
    selectedCycles=_simple_unoriented_physical_C6(seladj)
    finalCycles=_simple_unoriented_physical_C6(winnerAdj)
    actual_sourceD6=[]
    for cycle in selectedCycles:
        if len({v[0] for v in cycle})!=6 or len({v[1] for v in cycle})!=6:
            raise AssertionError("true ORIGINAL source cut selected a nonproper cycle")
        source_ids=tuple(sorted(selowner[tuple(sorted((
            cycle[j],cycle[(j+1)%6])))] for j in range(6)))
        if (len(set(source_ids))!=6 or set(source_ids)&set(Z) or
            classify_seven_prechecked(source_ids,f,g,flags)!="D6"):
            raise AssertionError("simple physical selector C6 is not positive ORIGINAL six distinct source ID D6")
        actual_sourceD6.append(source_ids)
    if len(actual_sourceD6)!=len(set(actual_sourceD6)):
        raise AssertionError("selected physical source C6 maps duplicate original D6 source flags")
    if len(finalCycles)>len(selectedCycles):
        raise AssertionError("uncloned subgraph created new physical C6")
    for cycle in finalCycles:
        if cycle not in selectedCycles:
            # Graph's canonical DFS should produce identical unrooted,
            # unoriented start/direction even after vertices disappear.
            raise AssertionError("final sixcycle not a true ORIGINAL selected physical sixcycle")
    L=len(I);q=len(Q);n=a*a
    adaptive_density=Fraction(L*L,32*n*(L+2*eI))
    worst_cubed=Fraction(L**6,2**16*n**3*q*(L+2*eI)**3)
    vF=win["winner_ordinary_subgraph_vertices"]
    mF=win["winner_ordinary_subgraph_edges"]
    assert q>=1 and vF>=1
    if (Fraction(mF,vF)<adaptive_density or
        2*q<vF or
        Fraction(mF**3,vF**4)<worst_cubed):
        raise AssertionError("exact data-adaptive source ordinary C6 hypothesis not transferred")
    return {
        "schema":"mathlab.hyp105.original-adaptive-Z-robust-balanced-SS6.v1",
        "s":s,"original_source_flags":len(allids),"physical_alphabet":a,
        "full_original_physical_vertices":n,
        "deleted_original_flag_IDs":list(Z),
        "full_original_QT_vertices":q,
        "original_full_physical_degree_sum":4*len(allids),
        "full_original_tail_edges":len(full_tail_edges),
        "actual_original_heavy_edges_removed_by_Z":lost,
        "original_tail_edges_remaining_after_Z":len(nondeleted_tail_edges),
        "retained_heavy_original_flag_IDs":list(I),
        "original_heavy_conflict_edges_actual":eI,
        "original_source_Caro_Wei_exact_weight":str(CW),
        "original_source_Caro_Wei_selected_count":len(chosen),
        "original_left_cut_after_first_count":len(left),
        "original_both_typed_cuts_selected_count":len(selected),
        "original_both_real_diagonals_per_selected_ID":True,
        "actual_original_heavy_witness_endpoint_chosen_side":chosen_side,
        "actual_original_heavy_witnesses_on_chosen_side":len(sides[chosen_side]),
        "actual_uncloned_balanced_chunk":win,
        "exact_adaptive_guaranteed_density":str(adaptive_density),
        "exact_external_C_graph_CUBED_sufficient_data_threshold":str(worst_cubed),
        "actual_winner_eCubed_over_vFourth":str(Fraction(mF**3,vF**4)),
        "actual_physical_selected_C6":len(selectedCycles),
        "actual_winner_uncloned_physical_C6":len(finalCycles),
        "true_original_D6_six_flag_IDs_selected":[list(v) for v in sorted(actual_sourceD6)],
        "source_c6_injects_original_positive_D6_after_Z":True,
        "no_cloned_vertices_or_source_IDs":True,
        "unknown_published_C_graph_c_graph_NOT_guessed":True,
        "root_230_status":ROOT_STATUS,
        "root_allh_Branch_A_proved_here":False,
    }


def exact_allh_robust_source_tail_constants(C_graph,c_graph,epsilon):
    """Strictly FORMAL actual published external C,c, never invent values."""
    C=Fraction(C_graph);c=Fraction(c_graph);eps=Fraction(epsilon)
    if min(C,c,eps)<=0:
        raise ValueError("external graph constants and residual tail epsilon must be positive")
    beta=eps*eps/128
    T_old=Fraction(2**41)*C**3/eps**6
    T_improved=Fraction(2**40)*C**3/eps**6
    D_lower=c*eps**12/Fraction(2**72)
    if T_old!=2*T_improved or D_lower!=c*(beta/Fraction(32))**6:
        raise AssertionError("SS6 original epsilon-beta constant normalized incorrectly")
    T_root_new=2**64*C**3
    T_root_old=2**65*C**3
    if T_root_new!=Fraction(2**40)*C**3/Fraction(1,16)**6:
        raise AssertionError("root original deletion robust threshold incorrect")
    return {
        "schema":"mathlab.hyp105.original-SS6-Z-resilient-allh-constants.v1",
        "published_graph_C_is_only_unfixed_symbolic_trial":str(C),
        "published_graph_c_is_only_unfixed_symbolic_trial":str(c),
        "residual_original_tail_epsilon":str(eps),
        "original_minimum_selected_fraction_beta":str(beta),
        "old_659_heavy_threshold_T":str(T_old),
        "improved_684_AND_adversarial_original_deletion_T":str(T_improved),
        "original_D6_after_ANY_deletion_lower_multiplier_of_sixpower":str(D_lower),
        "root_674_old_T_for_full_tail_eighth_original_deletion_at_most_1over32":str(T_root_old),
        "root_674_NEW_T_for_same_full_tail_deletion_hypothesis":str(T_root_new),
        "actual_published_graph_constants_numerical_values_VERIFIED":False,
        "new_root_allh_geometric_Branch_A_proved":False,
        "root_230_status":ROOT_STATUS,
    }


def canonical_original_deleted_adaptive_heavy_report():
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    cases=[
        (1,"lex","1/2",(0,)),
        (1,"reverse-line","3/4",(1,13,33)),
        (2,"lex","1",(0,10,100,200)),
        (2,"reverse-line","5/4",(0,25,26,33,34)),
    ]
    rows=[]
    for h,scheme,T,Z in cases:
        m=pair_labeled_symplectic(h,scheme)
        x=_real_original_selector_adaptive_heavy(
            h,m["left_labels"],m["right_labels"],Z,T)
        x["scheme"]=scheme
        x["full_physical_degree_cap_T"]=T
        rows.append(x)
    return {
        "schema":"mathlab.hyp105.AA4-true-original-deletion-robust-heavy-SS6.v1",
        "genuine_source_cases":rows,
        "formal_constants":[exact_allh_robust_source_tail_constants(
            C,c,Fraction(1,16)) for C,c in (
                (Fraction(1),Fraction(1)),
                (Fraction(7,3),Fraction(2,101)))],
        "allh_ss6_external_C_c_required_NOT_numeric":True,
        "root_allh_Branch_A_proved_here":False,
        "root_230_status":ROOT_STATUS,
    }


if __name__=="__main__":
    import json
    print("AA4_ORIGINAL_ADAPTIVE_ZTAIL_CERTIFICATE="+json.dumps(
        canonical_original_deleted_adaptive_heavy_report(),
        sort_keys=True,separators=(",",":")),flush=True)
