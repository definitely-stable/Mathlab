"""AA4-MOM6: exact bipartite 6-walk collision decomposition and 2x gain.

PURE GRAPH ALL-h THEOREM (all finite simple bipartite graphs, not just GQ):
For left vertices U, d_u=degree(u), c_uv=|N(u) cap N(v)|,
t_uvw=|N(u) cap N(v) cap N(w)|, and C6 simple unoriented cycles:

  C6 = SUM_{u<v<w in U}
       [c_uv*c_vw*c_wu - t_uvw*(c_uv+c_vw+c_wu-2)].

  tr(A^6) = 12*C6 + 2*SUM_u d_u^3
            +6*SUM_{u<v}(d_u+d_v)*c_uv^2
            +12*SUM_{u<v<w} t_uvw*(c_uv+c_vw+c_wu-2).

The three noncycle summands count ALL NON-INJECTIVE 6-closed-walks,
without using the original #672 six-walk/backtrack inequality.
This is exact with vertices/edges of the actual physical graph.

For any simple bipartite graph maximum degree D, m edges,
tr(A6) <=12*C6 +6*D*tr(A4) (backtrack injection/union bound),
tr(A4)^2 <=2*m*tr(A6) (eigenvalue/Cauchy).
Young at theta=1/2 then gives the rigorously sharper universal
  tr(A6) <=24*C6 + 72*m*D^2
(old #672 used 24*C6+144*m*D^2).

Under the original #672 selected physical G with 2m<=8s4,
m<=4s4, D<=T*s, and C6(G)<=D6(f,g)<s6, its sixth moment
has the better all-h uniform coefficient
  tr(A_G^6) <= (24+288*T^2)*s6,
versus the original L6=24+576*T^2. Coupling with AA4-SELPLUS
sigma2/sigma3 sharpens Jensen bounds on proper core paths.

Finite TRUE ORIGINAL W32/W34 adversarial selector graphs verify:
- selected flags come from original source flag IDs, both physical
  diagonals retained or both deleted, row/column cherries excluded;
- selected physical graph is bipartite and simple;
- every physical C6 is coordinate-proper and is a historical ORIGINAL
  D6 sixset on six DISTINCT original source incidence IDs;
- three INDEPENDENT sixth-moment algorithms (left/right codegree,
  direct length-three walk squaring, independently enumerated cycles)
  agree, and the tightened bound holds.
Finite checks do NOT establish #672's all-map global theorem.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations


def _bipartition(graph, left=None, right=None):
    """Deterministic bipartition, including isolates and disconnected graph."""
    nodes=set(graph)
    if any(v in ns or not set(ns)<=nodes for v,ns in graph.items()):
        raise ValueError("graph must be simple with all endpoint keys")
    if any(v not in graph[u] for v,ns in graph.items() for u in ns):
        raise ValueError("graph adjacency must be symmetric")
    if (left is None)!=(right is None):
        raise ValueError("supply both typed bipartition sides or neither")
    if left is not None:
        U=set(left);W=set(right)
        if U&W or U|W!=nodes or any(v in U for u in U for v in graph[u]) or (
            any(v in W for u in W for v in graph[u])):
            raise ValueError("not a typed simple bipartite graph")
    else:
        colors={}
        for v in sorted(nodes):
            if v in colors:continue
            colors[v]=0
            queue=[v]
            for u in queue:
                for w in graph[u]:
                    if w not in colors:
                        colors[w]=1-colors[u]
                        queue.append(w)
                    elif colors[w]==colors[u]:
                        raise ValueError("not bipartite")
        U={v for v,c in colors.items() if c==0}
        W=nodes-U
    return tuple(sorted(U)),tuple(sorted(W))


def _direct_sixcycles(graph):
    """Independent rooted simple physical cycle DFS, canonical reverse."""
    result=set()
    for root in sorted(graph):
        def visit(path):
            if len(path)==6:
                if root not in graph[path[-1]]:return
                if path[1]<path[-1]:
                    result.add(tuple(path))
                return
            for w in sorted(graph[path[-1]]):
                if w>root and w not in path:
                    visit(path+(w,))
        visit((root,))
    return result


def _direct_trace_even(graph,length):
    """Independent actual adjacency walk dynamic programming (no spectra)."""
    if length not in (4,6):
        raise ValueError("length=4 or 6")
    trace=0
    for root in graph:
        row={root:1}
        for _ in range(length):
            nextrow=Counter()
            for u,amount in row.items():
                for v in graph[u]:
                    nextrow[v]+=amount
            row=nextrow
        trace+=row.get(root,0)
    return trace


def _degree_codegree_moments(graph,left):
    U=tuple(sorted(left))
    adj={u:set(graph[u]) for u in U}
    deg={u:len(adj[u]) for u in U}
    c={(u,v):len(adj[u]&adj[v]) for u,v in combinations(U,2)}
    def co(u,v):
        if u==v:return deg[u]
        return c[tuple(sorted((u,v)))]
    three=0
    collision=0
    simple_cycles=0
    for u,v,w in combinations(U,3):
        uv,vw,wu=co(u,v),co(v,w),co(w,u)
        prod=uv*vw*wu
        t=len(adj[u]&adj[v]&adj[w])
        defective=t*(uv+vw+wu-2)
        if defective<0 or defective>prod:
            raise AssertionError("distinct right matching inclusion/exclusion invalid")
        simple_cycles+=prod-defective
        collision+=defective
        three+=prod
    degree_cube=sum(z**3 for z in deg.values())
    paircode=sum((deg[u]+deg[v])*c[(u,v)]**2 for u,v in c)
    nonsimple=2*degree_cube+6*paircode+12*collision
    sixth_trace=12*simple_cycles+nonsimple
    if sixth_trace!=2*(degree_cube+3*paircode+6*three):
        raise AssertionError("matrix B B^T cubic trace and primitive partition differ")
    return {
        "simple_C6":simple_cycles,
        "primitive_injective_C6_rooted_count":12*simple_cycles,
        "noninjective_closed_six_walk_count":nonsimple,
        "sixth_trace":sixth_trace,
        "degree_cube_collision_term":2*degree_cube,
        "repeated_left_pair_collision_term":6*paircode,
        "repeated_right_with_three_distinct_left_term":12*collision,
    }


def exact_bipartite_sixwalk_certificate(graph,left=None,right=None,
                                       *,exhaustive=False):
    """Exact integer 6walk classification; optional INDEPENDENT DFS referee.

    left/right are typed graph vertex subsets, NOT original source
    factor IDs, and may be disconnected, sparse or empty.
    """
    U,W=_bipartition(graph,left,right)
    l=_degree_codegree_moments(graph,U)
    r=_degree_codegree_moments(graph,W)
    if l["simple_C6"]!=r["simple_C6"] or (
        l["sixth_trace"]!=r["sixth_trace"]):
        raise AssertionError("left/right bipartite codegree sixth moments differ")
    tr6=l["sixth_trace"]
    m=sum(map(len,graph.values()))//2
    delta=max(map(len,graph.values()),default=0)
    # tr A4 = sum_(u,v) (A^2_uv)^2; exact local codegree formula.
    trace4=0
    for side in (U,W):
        for u in side:
            trace4+=len(graph[u])**2
        for u,v in combinations(side,2):
            trace4+=2*len(graph[u]&graph[v])**2
    if trace4**2>2*m*tr6:
        raise AssertionError("fourth-to-sixth spectral Cauchy failed")
    if tr6>12*l["simple_C6"]+6*delta*trace4:
        raise AssertionError("backtrack-to-fourth closed-walk union bound failed")
    improved=24*l["simple_C6"]+72*m*delta**2
    older=24*l["simple_C6"]+144*m*delta**2
    if tr6>improved or improved>older:
        raise AssertionError("improved all-h sixth moment Young bound failed")
    if exhaustive:
        if len(_direct_sixcycles(graph))!=l["simple_C6"]:
            raise AssertionError("direct physical C6 DFS and codegree differ")
        if _direct_trace_even(graph,6)!=tr6 or (
            _direct_trace_even(graph,4)!=trace4):
            raise AssertionError("independent physical 4/6 closed walk DFS differs")
    return {
        "vertices":len(graph),
        "edges":m,"max_degree":delta,
        "left_vertices":len(U),"right_vertices":len(W),
        "simple_physical_C6":l["simple_C6"],
        "trace_A4":trace4,
        "trace_A6":tr6,
        "noninjective_sixwalks":l["noninjective_closed_six_walk_count"],
        "left_collision_decomposition":l,
        "right_collision_decomposition":r,
        "tighter_all_h_Young_upper":improved,
        "old_672_all_h_upper":older,
        "all_h_Young_degree_error_coefficient_old":144,
        "all_h_Young_degree_error_coefficient_new":72,
        "full_exact_independent_6walk_DFS_checked":exhaustive,
    }


def improved_allh_selected_sixth_moment_envelopes(K,T):
    """Strict all-h L6 improvement under #672's genuine core assumptions.

    Positive real-graph bound holds without source assumptions; this
    helper merely propagates source s6 normalization m<=4s4,
    Delta<=T*s and #679 Jensen sigma2/3 improved probabilities.
    """
    from hyp105_selector_positive_correlation import improved_path_selector_sigma
    if type(T) is not int or T<1:
        raise ValueError("source physical core T>=1 integer")
    sig=improved_path_selector_sigma(K)
    oldL6=24+576*T*T
    newL6=24+288*T*T
    oldsig3=sig["old_sigma3"]
    newsig3=sig["new_sigma3"]
    oldsig2=sig["old_sigma2"]
    newsig2=sig["new_sigma2"]
    # Bound fourth moment from sixth by Cauchy, selected 2m<=8s4.
    # sqrt(8 L6) exact symbolic integer/rational bound; use exact
    # coefficients of radicals via squared-ratio records.
    return {
        "K":K,"T":T,
        "old_L6_s6":oldL6,
        "new_L6_s6":newL6,
        "strict_L6_gain":288*T*T,
        "new_sigma2":newsig2,
        "new_sigma3":newsig3,
        "old_P3_frobenius_coefficient":oldsig3**(-2)*oldL6,
        "new_P3_frobenius_coefficient":newsig3**(-2)*newL6,
        "P3_frobenius_exact_strict_ratio":
            (oldsig3**(-2)*oldL6)/(newsig3**(-2)*newL6),
        "P2_frobenius_square_coefficient_ratio":
            (oldsig2**(-2)/newsig2**(-2)),
        "old_sixth_graph_inequality": "24*C6+144*m*Delta^2",
        "new_sixth_graph_inequality": "24*C6+72*m*Delta^2",
        "full_Branch_A_root_scientific_acceptance":False,
    }


def genuine_source_selected_graph_moment_certificates(
        power,f,g,core_ids=None,seeds=(1,3,7,11)):
    """Fixed actual W32/W34 f,g, source flag priorities and typed cuts.

    Deterministic priority ranks are used ONLY for falsifying the exact
    graph moment identities. No stochastic experiment is extrapolated
    to prove the all-h probability theorem.
    """
    from hyp105_full_physical_degree_tail import (
        genuine_source,physical,conflict_graph,
    )
    from hyp105_physical_degree_energy import (
        minimal_alphabet,_verify_typed_injections,
    )
    from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked

    if type(power) is not int or power not in (1,2):
        raise ValueError("genuine W32/W34 source required")
    s,V,flags=genuine_source(power)
    a=minimal_alphabet(V)
    f=tuple(map(tuple,f));g=tuple(map(tuple,g))
    _verify_typed_injections(a,V,f,g)
    ids=(tuple(range(len(flags))) if core_ids is None else tuple(core_ids))
    if len(set(ids))!=len(ids) or any(type(i) is not int or not 0<=i<len(flags)
                                      for i in ids):
        raise ValueError("genuine distinct original source core IDs required")
    C,_,_=conflict_graph(ids,flags,f,g)
    rows=[]
    for seed in seeds:
        if type(seed) is not int:
            raise ValueError("priority/color deterministic seed must be int")
        # For any seed, this sorting assigns a COMPLETE deterministic
        # priority order on genuine core ORIGINAL incidence IDs.
        order=sorted(ids,key=lambda i:((i*6364136223846793005+seed*1442695040888963407)%
                                       18446744073709551557,i))
        rank={i:j for j,i in enumerate(order)}
        independent=[i for i in ids if all(rank[i]<rank[j] for j in C[i])]
        if any(j in C[i] for i,j in combinations(independent,2)):
            raise AssertionError("true original conflict selector not independent")
        # Deterministic binary cuts on ORIGINAL point- and line-label
        # physical alphabets; both diagonals of kept flags remain.
        def color(v,part):
            return ((v*1664525+1013904223+(seed+part*700001)*2246822519) >> 
                    (seed%11+1))&1
        kept=tuple(i for i in independent
                   if color(f[flags[i][0]][0],0)!=color(f[flags[i][0]][1],0)
                   and color(g[flags[i][1]][0],1)!=color(g[flags[i][1]][1],1))
        graph,owner=physical(kept,flags,f,g)
        for i in kept:
            if sum(j==i for j in owner.values())!=2:
                raise AssertionError("original source flag does not preserve BOTH diagonals")
        left={v for v in graph if color(v[0],0)==0}
        right=set(graph)-left
        cert=exact_bipartite_sixwalk_certificate(
            graph,left,right,exhaustive=True)
        C6sets=set()
        for cyc in _direct_sixcycles(graph):
            if len({v[0] for v in cyc})!=6 or len({v[1] for v in cyc})!=6:
                raise AssertionError("selected physical C6 not coordinate-proper")
            ids6=tuple(sorted(owner[tuple(sorted((cyc[j],cyc[(j+1)%6])))]
                              for j in range(6)))
            if len(set(ids6))!=6 or (
                len({flags[i][0] for i in ids6})!=6 or
                len({flags[i][1] for i in ids6})!=6):
                raise AssertionError("selected physical C6 not six ORIGINAL D6 IDs")
            if classify_seven_prechecked(ids6,f,g,flags)!="D6":
                raise AssertionError("selected physical C6 historical ORIGINAL GF5 class not D6")
            C6sets.add(ids6)
        if len(C6sets)!=cert["simple_physical_C6"]:
            raise AssertionError("physical C6 to ORIGINAL D6 sixset map not injective")
        rows.append({
            "seed":seed,
            "original_core_flag_count":len(ids),
            "original_conflict_selected_flag_count":len(independent),
            "original_bichromatic_selected_flag_count":len(kept),
            "accepted_original_D6_C6_subcount":len(C6sets),
            "physical_moment":cert,
        })
    return {
        "s":s,"original_V":V,"physical_a":a,
        "all_selected_graphs_from_true_original_flags":True,
        "certificates":tuple(rows),
        "finite_real_original_source_not_all_h_root_proof":True,
    }
