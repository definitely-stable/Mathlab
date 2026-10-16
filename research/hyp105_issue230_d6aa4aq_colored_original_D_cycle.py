"""HYP-105 #230 AA4-AQ: EXACT original D6 = colored-rainbow 6-cycles.

For TRUE original W(3,2^h), arbitrary fully globally injected typed
point/line physical unordered-edge maps f,g, build graph G_D whose
VERTICES are actual original incidence-flag IDs (p,l). Its UNDIRECTED
edge {i,j} exists iff original p_i!=p_j and l_i!=l_j AND the pair
images f(p_i),f(p_j) meet at one physical POINT coordinate and
g(l_i),g(l_j) meet at one physical LINE coordinate. These are EXACT
AA4-AL genuine original D pairs, not free source-factor pairs.

Color each D edge by the UNIQUE shared physical point coordinate
and unique shared physical line coordinate. Then:

    selected original D6 six-ID Q
    <==> UNIQUE simple length-six cycle on Q in G_D for which ALL
          six POINT edge colors are distinct and ALL six LINE
          edge colors are distinct.

As an EXACT all-h ordered-walk identity:
    12 * S_D6(f,g) = #{directed rooted simple length-6 cycles of
                       G_D rainbow in BOTH physical color types}.
"12" counts 6 starting vertices * 2 orientations. If a rainbow cycle
exists, the original point and line image pair of each flag MUST be
the two differently colored incident cycle edges; this FORCES
aligned connected physical A/A six-factors and TRUE source D6. A
selected D6 has precisely its six positional physical-column overlaps
(AA4-AM), giving precisely that one cycle up to 12 orientations.
This is a novel *reformulation of the already researched AA4-T
positional D6 tensor*; classical cycle graph counting is not claimed
a novel combinatorial theorem or a source-Hall GF5 lower.

Each nonbacktracking typed directed D arc i->j can be followed ONLY
by j->k whose physical point shared coordinate equals the OTHER
endpoint of f(p_j), AND whose line shared coordinate equals the OTHER
endpoint of g(l_j). Thus each next flag k lies in one ACTUAL ORIGINAL
incidence-cell fiber M[c,e]=(F^T B G)[c,e]. Its outdegree is bounded
by the AA4-AP actual GQ spectral cell cap K. Rainbow simple cycle
closure adds strict global six-color injectivity.

Crucially, AA4-AP's GOOD D>=s^5/10 is an EDGE-count statement and
does not force even an UNCOLORED six-cycle under general graph
extremal principles: for all h>=48 an ABSTRACT C6-free GQ incidence
graph can be padded to N=V(s+1) vertices with >=s^5 edges. This
abstract graph is NOT an actual globally mapped original D graph.
The exact colored D6 cycle lower is still OPEN. Other six GF5 tags
are NOT represented by this D6-only rainbow transfer.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_d6aa4al_global_original_coordinate_transport import (
    _actual_strict_original_transport)
from hyp105_issue230_d6aa4am_genuine_pair_sixcharge import (
    original_D_pair_index)
from hyp105_issue230_d6aa4ap_uniform_good_original_D_spectral import (
    global_good_original_D_spectral_certificate)
from hyp105_issue230_d6aa4q_two_sided_seven_join import (
    independent_joint_classify)


def original_bicolored_D_flag_graph(model):
    """The REAL AA4-AL original D-pair graph, with unique TWO typed colors.

    Retains full global source incidence flag IDs, globally injected
    physical factor map and both source-factor inequality guards.
    """
    s,V,d,a,left,right,inc,np,nl=_actual_strict_original_transport(model)
    source_pairs=original_D_pair_index(model)
    neighbors=[[] for _ in inc]
    colors={}
    for i,j in source_pairs:
        p,l=inc[i];q,m=inc[j]
        pc=set(left[p])&set(left[q])
        lc=set(right[l])&set(right[m])
        if p==q or l==m or len(pc)!=1 or len(lc)!=1:
            raise AssertionError("one true original bilateral D edge per pair")
        cp,cl=next(iter(pc)),next(iter(lc))
        colors[i,j]=(cp,cl)
        neighbors[i].append((j,cp,cl))
        neighbors[j].append((i,cp,cl))
    return dict(s=s,V=V,a=a,inc=inc,left=left,right=right,
                D_edges=frozenset(source_pairs),edge_colors=colors,
                neighbors=tuple(tuple(sorted(row)) for row in neighbors),
                original_source_flag_vertices=len(inc),
                actual_source_global_two_typed_injections=True)


def _other_endpoint(edge,shared):
    if shared==edge[0]:return edge[1]
    if shared==edge[1]:return edge[0]
    raise AssertionError("incoming ORIGINAL D physical shared coordinate missing")


def original_D_arc_transition_spectral_audit(model):
    """Exact directed D arc allowed-next source transitions.

    A valid D6 rainbow cycle can use only these 2-typed port
    complementary moves. For every directed arc (i,j) the allowed
    next genuine ORIGINAL flag k lies in the ACTUAL original point
    and line coordinate cell M[other_f(j),other_g(j)] and is bounded
    by classical GQ source spectral upper K, not a lower.
    """
    G=original_bicolored_D_flag_graph(model)
    s=G["s"];a=G["a"]
    K=global_good_original_D_spectral_certificate(s)[
        "original_coordinate_cell_incidence_uniform_upper"]
    per_arc=Counter()
    max_step=0
    for i,row in enumerate(G["neighbors"]):
        for j,cp,cl in row:
            p,l=G["inc"][j]
            xp=_other_endpoint(G["left"][p],cp)
            xl=_other_endpoint(G["right"][l],cl)
            allowed=sum(u!=i and cp2==xp and cl2==xl
                        for u,cp2,cl2 in G["neighbors"][j])
            if allowed>K:
                raise AssertionError("true source GQ spectral cell bound violated")
            per_arc[allowed]+=1
            max_step=max(max_step,allowed)
    assert sum(per_arc.values())==2*len(G["D_edges"])
    return dict(s=s,original_flag_vertices=len(G["inc"]),
                D_undirected_original_edges=len(G["D_edges"]),
                directed_original_D_arc_count=sum(per_arc.values()),
                forward_original_typed_legal_port_count_histogram=dict(sorted(per_arc.items())),
                maximum_valid_original_two_typed_one_step=max_step,
                classical_original_source_incidence_cell_upper=K,
                AA4_AP_good_D_lower_not_promoted_to_D6=True)


def _plain_any_six_cycle(G):
    """One literal ordinary simple 6-cycle, without ANY rainbow constraints.

    Finite W32 only: the counterexample is a SIX-CYCLE in the SAME
    true-original D graph but NOT selected positive original D6.
    """
    adjacency=tuple({j for j,_,_ in row} for row in G["neighbors"])
    def dfs(root,path):
        if len(path)==6:
            return tuple(path) if root in adjacency[path[-1]] else None
        for j in sorted(adjacency[path[-1]]):
            if j<=root or j in path:continue
            z=dfs(root,path+[j])
            if z is not None:return z
        return None
    for root in range(len(adjacency)):
        ans=dfs(root,[root])
        if ans is not None:return ans
    return None


def exact_original_rainbow_D6_cycle_transfer(model,*,roots=None,
                                             max_rainbow_sixcycles=None):
    """Original six-ID TRUE D6 ↔ rainbow undirected simple C6.

    roots=None => exhaustive full original D6 certificate, practical
    W32 only; roots=(0,...,) => an explicitly labelled partial
    minimum-original-flag-root sample for W34, never full census.
    max_rainbow_sixcycles is an optional cap that TRUNCATES with a
    clear status rather than claiming a complete S_D6.
    """
    G=original_bicolored_D_flag_graph(model)
    inc=G["inc"];adj=G["neighbors"]
    if roots is None:
        if len(inc)>60:
            raise ValueError("full rainbow D6 enumeration is certified W32 only; select roots")
        roots=tuple(range(len(inc)))
        full=True
    else:
        roots=tuple(roots)
        if any(type(i)!=int or i<0 or i>=len(inc) for i in roots):
            raise ValueError("genuine original source flag root IDs required")
        if len(set(roots))!=len(roots):
            raise ValueError("source flag roots must be distinct")
        full=len(roots)==len(inc)
    if max_rainbow_sixcycles is not None and (
            type(max_rainbow_sixcycles)!=int or max_rainbow_sixcycles<1):
        raise ValueError("positive partial rainbow witness budget")
    witnesses={}
    one_step=0
    exhausted=True

    class ReachedBudget(Exception):pass

    def dfs(root,path,point_colors,line_colors):
        nonlocal one_step
        last=path[-1]
        if len(path)==6:
            for j,cp,cl in adj[last]:
                if j!=root or cp in point_colors or cl in line_colors:
                    continue
                if path[1]>=path[-1]:continue
                Q=tuple(sorted(path))
                if Q in witnesses:
                    raise AssertionError("same genuine ORIGINAL D6 Q has two 6-cycles")
                tag=independent_joint_classify(
                    Q,"A","A",inc,G["left"],G["right"])
                if tag!="D6":
                    raise AssertionError("rainbow true ORIGINAL D 6-cycle is not aligned D6")
                witnesses[Q]=tuple(path)
                if (max_rainbow_sixcycles is not None and
                        len(witnesses)>=max_rainbow_sixcycles):
                    raise ReachedBudget()
            return
        for j,cp,cl in adj[last]:
            if j<=root or j in path or cp in point_colors or cl in line_colors:
                continue
            one_step+=1
            dfs(root,path+[j],point_colors+(cp,),line_colors+(cl,))

    try:
        for root in roots:
            dfs(root,[root],(),())
    except ReachedBudget:
        exhausted=False
    return dict(
        s=G["s"],a=G["a"],
        D_original_undirected_pair_count=len(G["D_edges"]),
        original_source_flag_vertices=len(inc),
        minimum_flag_roots_tested=len(roots),
        global_root_scan_complete=full and exhausted,
        scan_truncated_by_explicit_witness_budget=not exhausted,
        double_rainbow_D6_original_Q_count=len(witnesses),
        exact_true_original_six_ID_D6_Q_to_unique_cycle=witnesses,
        canonical_undirected_cycles_from_12_oriented_rooted_walks=True,
        examined_D_flag_path_extensions=one_step,
        all_h_theorem_12_oriented_rainbow_walks_per_D6=True,
        accepted_original_full_seven_GF5_lower_NOT_PROVED=True,
        all_h_uniform_positive_D6_lower_NOT_PROVED=True)


def all_h_abstract_plain_C6_edgecount_nogo(s):
    """For h>=48: explicit ABSTRACT C6-free graph on no more than
    original N=Vd flag vertices with at least s^5 edges.

    Use the actual mathematical existence of a generalized quadrangle
    W(3,q), q=2^(floor(4h/3)-3), whose incidence graph is bipartite
    girth-eight, hence ordinary C6-free. This construction is NOT an
    actual AA4-AL D graph for W(3,s) global factor injections; it
    only refutes a proposed generic graph-edge-count⇒C6 inference.
    """
    if type(s) is not int or s<2 or s&(s-1):
        raise ValueError("original parameter s=2^h>=2")
    h=s.bit_length()-1
    if h<48:
        raise ValueError("symbolic graph threshold for general h>=48 only")
    t=(4*h)//3-3
    q=1<<t
    n=2*(q+1)*(q*q+1)
    E=(q+1)**2*(q*q+1)
    N=(s+1)**2*(s*s+1)
    assert 4*t>=5*h
    assert n<=N and E>=s**5
    assert n<=4*q**3<=N
    return dict(
        s=s,h=h,q=q,
        original_source_flag_vertex_budget=N,
        abstract_generalized_quadrangle_incidence_graph_vertices=n,
        abstract_C6_free_incidence_graph_edges=E,
        at_least_s5_edges=E>=s**5,
        has_any_ordinary_C6=False,
        padding_to_original_flag_vertex_count_possible=True,
        NOT_an_actual_original_D_f_g_compatibility_graph=True,
        no_all_map_D6_counterexample_proved=True,
        edge_count_lower_alone_does_NOT_force_ordinary_C6=True)
