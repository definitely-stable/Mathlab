"""HYP-105 / #230 AA4-SEL6WALK: independent source selector and C6 audit.

NEW standalone mathematical referee for two genuinely difficult non-mechanized
interfaces of the root Branch A proof:
(1) exact local priority-permutation probability for a proper physical r-path
    (r=2,3) in true ORIGINAL W(3,2)/W(3,4), computed as linear extensions
    of the ORIGINAL source conflict precedence DAG, NOT estimated via samples;
    two factor bit cuts verified by direct exhaustive 2^(2(r+1)) enumeration.
(2) full enumeration of all 2^(3*3)=512 simple bipartite K_3,3 subgraphs,
    direct closed 4- and 6-walk traces and unoriented C6 census, proof-gated
    tr A^6 <= 12 C6 + 6 Delta tr A^4 and
    tr A^6 <= 24 C6 + 72 m Delta^2;
    and source-first heavy D6 ORIGINAL six-ID seed W(3,4) real two-diagonal
    edge graphs supporting one actual selected coordinate-proper C6.

No historical selector, source inverse, energy, heavy or root calculators
are imported by the MAIN source; only trusted genuine symplectic finite
source and complete pair-injective fixture constructors.

Proof boundaries: a finite exhaustive check is NOT an all-graph proof;
the written manuscript supplies independent elementary injections/
spectral proofs. Correct accepted source Branch A S_s vs additive GF5 R3
is preserved. NO promotion PROVED_A, ASET exponent, numeric external
SS6 constants, parent/main mutation or merge.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial
import json

SCHEMA="mathlab.hyp105.original-selector-sixwalk-independent-referee.v1"
K=64
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
D6_SEEDS=(
    ("lex",(111,116,203,224,383,412)),
    ("lex",(129,146,224,366,412,417)),
    ("reverse-line",(47,224,229,273,300,355)),
)


def _source_data(h,scheme,shift_f=0,shift_g=0):
    from hyp105_full_physical_degree_tail import genuine_source
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    if type(h) is not int or h not in (1,2):
        raise ValueError("only actual ORIGINAL W(3,2) and W(3,4) source")
    s,V,raw=genuine_source(h)
    flags=tuple(map(tuple,raw))
    model=pair_labeled_symplectic(h,scheme)
    f=tuple(tuple(sorted(p)) for p in model["left_labels"])
    g=tuple(tuple(sorted(p)) for p in model["right_labels"])
    f=f[shift_f%V:]+f[:shift_f%V]
    g=g[shift_g%V:]+g[:shift_g%V]
    if (len(flags)!=(s+1)*V or len(flags)!=len(set(flags))
        or len(f)!=len(g)!=V):
        raise AssertionError("not complete genuine original source")
    if len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V:
        raise AssertionError("invalid global pair injection")
    return s,V,flags,f,g


def _source_conflict(flags,f,g):
    n=len(flags)
    nbr=[set() for _ in range(n)]
    bypoint=defaultdict(list)
    byline=defaultdict(list)
    for i,(p,l) in enumerate(flags):
        bypoint[p].append(i)
        byline[l].append(i)
    for by,typ in ((bypoint,"point"),(byline,"line")):
        for ids in by.values():
            for i,j in combinations(ids,2):
                left=g[flags[i][1]] if typ=="point" else f[flags[i][0]]
                right=g[flags[j][1]] if typ=="point" else f[flags[j][0]]
                if set(left)&set(right):
                    nbr[i].add(j)
                    nbr[j].add(i)
    if any(len(row)>K for row in nbr):
        # In a large-h proof this is why we FIRST prune high J-degree;
        # the finite true W32/W34 source fixtures happen not to need it.
        raise AssertionError("finite fixture conflict degree exceeds K=64")
    return nbr


def _physical(flags,f,g):
    owner={}
    adj=defaultdict(set)
    for i,(p,l) in enumerate(flags):
        x,z=f[p];y,w=g[l]
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            e=tuple(sorted((u,v)))
            if e in owner:
                raise AssertionError("ORIGINAL source physical edge owner not unique")
            owner[e]=i
            adj[u].add(v)
            adj[v].add(u)
    if len(owner)!=2*len(flags):
        raise AssertionError("missing genuine opposite physical diagonal")
    return owner,adj


def _source_proper_path_sample(flags,f,g,nbr,r,max_samples=6000):
    if r not in (2,3):
        raise ValueError("only proper two/three step original source path")
    edgeowner,adj=_physical(flags,f,g)
    best=None
    visited=0
    ordered_starts=sorted(adj)
    for start in ordered_starts:
        stack=[(start,)]
        while stack:
            path=stack.pop()
            if len(path)==r+1:
                visited+=1
                owners=tuple(edgeowner[tuple(sorted((path[j],path[j+1])))]
                             for j in range(r))
                if len(set(owners))!=r:
                    raise AssertionError("proper path repeats original source owner")
                if any(o2 in nbr[o1] for o1,o2 in combinations(owners,2)):
                    raise AssertionError("proper original physical path source owners conflict")
                U=set(owners)
                for o in owners:
                    U.update(nbr[o])
                candidate=(len(U),tuple(path),owners,tuple(sorted(U)))
                if best is None or candidate<best:
                    best=candidate
                if visited>=max_samples:
                    break
                continue
            for u in sorted(adj[path[-1]],reverse=True):
                if (u not in path and
                    u[0] not in [v[0] for v in path] and
                    u[1] not in [v[1] for v in path]):
                    stack.append(path+(u,))
        if visited>=max_samples:
            break
    if best is None:
        raise AssertionError("no real ORIGINAL proper path found")
    b,path,owners,U=best
    if b>20:
        raise AssertionError("finite exact source permutation DP would exceed 20 IDs")
    return dict(path=path,owners=owners,closed_conflict_neighborhood=U,
                b=b,scanned=visited)


def _source_rank_linear_extensions(nbr,owners,U):
    """Count EXACT favorable original source priority permutations on U.

    Event is ALL owners precede their actual source J neighbors, not merely
    first-r sufficient event. There are b! uniform relative orderings.
    Precedence constraints are only i<j when i is one of target owners
    and j is an original conflict neighbor. All nonowners are unrestricted.
    """
    U=tuple(sorted(U))
    owners=tuple(owners)
    if len(set(owners))!=len(owners):
        raise ValueError("source owners repeated")
    if not set(owners)<=set(U):
        raise ValueError("owner missing in original closed J-neighborhood")
    if any(other in nbr[i] for i,other in combinations(owners,2)):
        raise ValueError("owners not pairwise source J independent")
    b=len(U)
    if b>20:
        raise ValueError("exact local DP cap b=20")
    idx={u:i for i,u in enumerate(U)}
    prior=[0]*b
    for owner in owners:
        for neighbor in nbr[owner]:
            if neighbor in idx:
                prior[idx[neighbor]] |= 1<<idx[owner]
    dp=[0]*(1<<b)
    dp[0]=1
    full=(1<<b)-1
    for mask in range(full):
        n=dp[mask]
        if not n:continue
        waiting=full^mask
        while waiting:
            low=waiting&-waiting
            j=low.bit_length()-1
            if prior[j]&mask==prior[j]:
                dp[mask|low]+=n
            waiting-=low
    if not dp[full]:
        raise AssertionError("real source rank event impossible")
    p=Fraction(dp[full],factorial(b))
    sufficient=Fraction(1,comb(b,len(owners)))
    if p<sufficient:
        raise AssertionError("actual original rank probability below exact first-r bound")
    return {"actual_priority_probability":str(p),
            "first_r_priority_sufficient":str(sufficient),
            "exact_favorable_permutations":str(dp[full]),
            "all_local_source_priority_permutations":str(factorial(b))}


def _exhaustive_path_color_probability(r):
    """Independent all legal physical cut assignments on 2*(r+1) symbols."""
    if r not in (2,3):
        raise ValueError("only finite original proper path r2/r3")
    n=r+1
    success=0
    for bits in product((0,1),repeat=2*n):
        left=bits[:n]
        right=bits[n:]
        if all(left[i]!=left[i+1] and right[i]!=right[i+1]
               for i in range(r)):
            success+=1
    return success,1<<(2*n)


def genuine_selector_rank_falsifier(h,scheme,r,shift_f=0,shift_g=0):
    s,V,flags,f,g=_source_data(h,scheme,shift_f,shift_g)
    nbr=_source_conflict(flags,f,g)
    q=_source_proper_path_sample(flags,f,g,nbr,r)
    priority=_source_rank_linear_extensions(nbr,q["owners"],
                                           q["closed_conflict_neighborhood"])
    color_good,color_total=_exhaustive_path_color_probability(r)
    color_p=Fraction(color_good,color_total)
    exact_p=Fraction(priority["actual_priority_probability"])*color_p
    sufficient=Fraction(1,4**r*comb(q["b"],r))
    global_sigma=Fraction(1,4**r*comb(r*(K+1),r))
    if (color_p!=Fraction(1,4**r) or exact_p<sufficient or
        sufficient<global_sigma or q["b"]>r*(K+1)):
        raise AssertionError("true ORIGINAL finite source selector rank/color lemma false")
    return {
        "s":s,"scheme":scheme,"r":r,
        "global_f_shift":shift_f,"global_g_shift":shift_g,
        "source_flags_total":len(flags),
        "proper_path_sample_scanned":q["scanned"],
        "actual_physical_path":q["path"],
        "distinct_named_ORIGINAL_source_owners":q["owners"],
        "original_J_closed_neighborhood_size_b":q["b"],
        "exact_source_priority_probability":priority["actual_priority_probability"],
        "first_r_original_priority_sufficient_probability":priority["first_r_priority_sufficient"],
        "exact_original_favorable_relative_rank_permutations":
            priority["exact_favorable_permutations"],
        "all_original_local_relative_rank_permutations":
            priority["all_local_source_priority_permutations"],
        "full_two_coordinate_color_assignment_count":color_total,
        "both_typed_physical_cuts_surviving_assignments":color_good,
        "exact_two_physical_factor_color_probability":str(color_p),
        "exact_actual_priority_times_color_probability":str(exact_p),
        "original_J_FIRST_R_source_selector_probability_floor":str(sufficient),
        "uniform_all_h_q_r_source_selector_probability_floor":str(global_sigma),
        "all_source_owners_true_distinct_and_J_independent":True,
    }


def _matmul(a,b):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def _matrix_traces_4_6(adjacency):
    n=len(adjacency)
    a=[[int(j in adjacency[i]) for j in range(n)] for i in range(n)]
    a2=_matmul(a,a)
    a3=_matmul(a2,a)
    a4=_matmul(a2,a2)
    a6=_matmul(a3,a3)
    return sum(a4[i][i] for i in range(n)),sum(a6[i][i] for i in range(n))


def _undirected_six_cycles(adjacency):
    n=len(adjacency)
    cycles=set()
    def key(c):
        t=tuple(c)
        return min(t[k:]+t[:k] for t in (t,t[::-1]) for k in range(6))
    for a in range(n):
        stack=[(a,)]
        while stack:
            path=stack.pop()
            if len(path)==6:
                if a in adjacency[path[-1]]:
                    cycles.add(key(path))
                continue
            for u in adjacency[path[-1]]:
                if u not in path:
                    stack.append(path+(u,))
    return cycles


def _graph_exact_bipartite_sixwalk_census(nleft,nright):
    if (type(nleft) is not int or type(nright) is not int
        or nleft<=0 or nright<=0 or nleft*nright>9):
        raise ValueError("exhaustive K_ab <=9 edges")
    n=nleft+nright
    pairs=tuple((i,nleft+j) for i in range(nleft) for j in range(nright))
    examined=0
    cycles_positive=0
    bound_tight=0
    maximum_c6=0
    maximum_positive_slack=0
    for bits in range(1<<len(pairs)):
        adj=[set() for _ in range(n)]
        for idx,(i,j) in enumerate(pairs):
            if bits&(1<<idx):
                adj[i].add(j);adj[j].add(i)
        m=bits.bit_count()
        delta=max((len(v) for v in adj),default=0)
        trace4,trace6=_matrix_traces_4_6(adj)
        C6=len(_undirected_six_cycles(adj))
        if C6:cycles_positive+=1
        if trace6>12*C6+6*delta*trace4:
            raise AssertionError("actual ordinary bipartite graph C6/6walk lemma false")
        if trace6>24*C6+72*m*delta*delta:
            raise AssertionError("actual bipartite selected sixth moment Young bound false")
        if trace6==12*C6+6*delta*trace4:
            bound_tight+=1
        examined+=1
        maximum_c6=max(maximum_c6,C6)
        maximum_positive_slack=max(maximum_positive_slack,
                                   12*C6+6*delta*trace4-trace6)
    return {
        "left":nleft,"right":nright,
        "all_bipartite_adjacency_masks":examined,
        "graphs_with_at_least_one_genuine_C6":cycles_positive,
        "max_distinct_unoriented_C6":maximum_c6,
        "graphs_tight_in_raw_sixwalk_upper":bound_tight,
        "max_nonnegative_sixwalk_upper_slack":maximum_positive_slack,
        "all_graphs_respect_12C6_plus_6Delta_traceA4":True,
        "all_graphs_respect_24C6_plus_72mDelta2":True,
    }


def real_original_d6_selected_cycle_case(scheme,original_six_ids):
    """Independent source-first ORIGINAL physical D6 selected graph witness.

    Build TRUE complete W34 f/g, source J, 2 diagonals/flag, actual
    physical graph of exactly six ORIGINAL flags and use direct C6 census.
    """
    s,V,flags,f,g=_source_data(2,scheme)
    nbr=_source_conflict(flags,f,g)
    ids=tuple(original_six_ids)
    if len(ids)!=len(set(ids)) or len(ids)!=6 or any(
        type(i) is not int or not 0<=i<len(flags) for i in ids
    ):
        raise ValueError("six distinct true ORIGINAL W34 flag IDs required")
    if any(j in nbr[i] for i,j in combinations(ids,2)):
        raise AssertionError("REAL original D6 six-source flag owners SOURCE conflict")
    pset={flags[i][0] for i in ids}
    lset={flags[i][1] for i in ids}
    if len(pset)!=len(lset)!=6:
        raise AssertionError("genuine source D6 owners repeat ORIGINAL p/l")
    edges={}
    physical=defaultdict(set)
    for i in ids:
        p,l=flags[i]
        x,z=f[p];y,w=g[l]
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            key=tuple(sorted((u,v)))
            if key in edges:
                raise AssertionError("ORIGINAL D6 source physical edge cloned")
            edges[key]=i
            physical[u].add(v);physical[v].add(u)
    vertices=tuple(sorted(physical))
    ix={v:j for j,v in enumerate(vertices)}
    adj=[{ix[u] for u in physical[v]} for v in vertices]
    cycles=_undirected_six_cycles(adj)
    eligible=[]
    for cy in cycles:
        corners=tuple(vertices[j] for j in cy)
        if (len({q[0] for q in corners})==6
            and len({q[1] for q in corners})==6):
            owners=tuple(edges[tuple(sorted((corners[j],corners[(j+1)%6])))]
                         for j in range(6))
            if set(owners)!=set(ids):
                raise AssertionError("physical proper C6 owns wrong ORIGINAL six flags")
            eligible.append(corners)
    if len(eligible)!=1:
        raise AssertionError("genuine original six D6 flags not unique proper physical C6")
    cutf={corner[0]:j%2 for j,corner in enumerate(eligible[0])}
    cutg={corner[1]:j%2 for j,corner in enumerate(eligible[0])}
    for i in ids:
        p,l=flags[i];x,z=f[p];y,w=g[l]
        if cutf[x]==cutf[z] or cutg[y]==cutg[w]:
            raise AssertionError("source-aligned physical C6 not both literal typed bichromatic")
    trace4,trace6=_matrix_traces_4_6(adj)
    deg=max(len(v) for v in adj)
    m=len(edges)
    if (len(edges)!=12 or trace6>12*len(cycles)+6*deg*trace4
        or trace6>24*len(cycles)+72*m*deg*deg):
        raise AssertionError("genuine original D6 physical selected graph 6walk bound false")
    return {
        "source_scheme":scheme,
        "s":s,"original_six_incidence_ID_set":tuple(sorted(ids)),
        "distinct_original_source_points_and_lines":True,
        "all_real_original_owned_physical_diagonals":len(edges),
        "actual_physical_graph_distinct_vertices":len(vertices),
        "actual_physical_graph_edges":m,
        "real_original_selected_graph_degree_Delta":deg,
        "physical_simple_C6_count":len(cycles),
        "proper_sixdistinct_both_coordinates_C6_count":len(eligible),
        "single_ORIGINAL_sixset_unoriented_physical_C6_multiplicity":1,
        "both_real_original_factor_coordinate_cuts_exist":True,
        "selected_physical_actual_trace_A4":trace4,
        "selected_physical_actual_trace_A6":trace6,
        "signed_C6_12_rooted_orientations":12*len(cycles),
        "all_source_physical_C6_and_sixwalk_gates_pass":True,
    }


def canonical_report():
    finite=tuple(
        genuine_selector_rank_falsifier(h,scheme,r,shf,shg)
        for h,scheme,shf,shg in (
            (1,"lex",0,0),
            (1,"reverse-line",2,4),
            (2,"lex",0,0),
            (2,"reverse-line",11,23),
        ) for r in (2,3)
    )
    census=(
        _graph_exact_bipartite_sixwalk_census(2,3),
        _graph_exact_bipartite_sixwalk_census(3,3),
    )
    heavy=tuple(real_original_d6_selected_cycle_case(k,ids)
                for k,ids in D6_SEEDS)
    return {
        "schema":SCHEMA,
        "root_230_status":ROOT_STATUS,
        "root_all_18_prior_source_lemmas_formally_machine_proved":False,
        "root_Branch_A_s_motif_PROVED_A":False,
        "root_ASET_exponent_proved":False,
        "exact_external_C6_graph_SS6_constants_numerically_verified":False,
        "original_root_target_is_SEVEN_class_unweighted_S_s":True,
        "original_R3_is_separate_additive_GF5_signed_event_SUM":True,
        "new_independent_exact_local_source_priority_probability_audited":True,
        "new_exhaustive_all_K33_bipartite_6walk_graphs_audited":True,
        "new_actual_original_W34_selected_D6_sixflag_inverse_audited":True,
        "source_original_proper_path_rank_and_two_cut_exact_cases":finite,
        "independent_graph_sixwalk_masks_exact_censuses":census,
        "real_original_W34_D6_selected_graph_sixwalk_census":heavy,
    }


if __name__=="__main__":
    print("AA4_ORIGINAL_SELECTOR_6WALK_REFEREE_CERTIFICATE="+json.dumps(
        canonical_report(),sort_keys=True,separators=(",",":")),flush=True)
