"""HYP-105 AA4-PAIRSEL: exact joint ORIGINAL source-path selector law.

All-h independent finite-graph theorem. For two proper actual physical
paths P,Q, priority source survival of their UNION is zero if any original
source flag pair conflicts; otherwise it has the exact shared-neighbor
r!-simplex rational integral. Binary typed physical-coordinate cuts have
an independent EXACT 2^(components-vertices) parity-CSP probability for
each typed union of source pair labels, or ZERO for an odd cycle.

Result: pairwise PATH survival is NOT positively associated in general,
although independently nonconflicting ORIGINAL local minima are. Gives
exact E[X_uv^2] for the proper-path count X_uv, hence independently
checks Jensen moment transfer without path-to-path independence.

Genuine W32/W34 finite checks are falsifiers, not all-h proof.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations,permutations

from hyp105_full_physical_degree_tail import genuine_source


def exact_source_priorities(graph,target):
    """Exact joint local-minimum probability for any source-target union.

    Graph is finite, UNDIRECTED/simple, explicit vertex set.
    A non-independent target union has zero probability.
    Derivation: condition on target priorities and integrate all shared
    non-target neighbors on each one of the |T|! order simplices.
    """
    if type(graph) is not dict:
        raise ValueError("complete finite source graph dict required")
    n=set(graph)
    if any((v in ns or not set(ns)<=n or
            any(v not in graph[w] for w in ns))
           for v,ns in graph.items()):
        raise ValueError("symmetric simple source conflict graph required")
    T=tuple(target)
    if not T or len(T)!=len(set(T)) or any(t not in graph for t in T):
        raise ValueError("nonempty distinct actual source flag target IDs required")
    if any(t in graph[u] for u,t in combinations(T,2)):
        return Fraction(0)
    tset=set(T)
    neighborhood=set().union(*(set(graph[t]) for t in T))
    value=Fraction(0)
    for pi in permutations(T):
        rank={v:j for j,v in enumerate(pi)}
        last=[0]*len(pi)
        for w in neighborhood:
            latest=max(rank[v] for v in graph[w] if v in tset)
            last[latest]+=1
        integral=Fraction(1)
        suffix=0
        for j in range(len(pi)-1,-1,-1):
            suffix+=last[j]+1
            integral/=suffix
        value+=integral
    if not Fraction(0)<value<=1:
        raise AssertionError("valid independent target source survival impossible")
    return value


def exact_typed_bichromatic_probability(edges):
    """Probability ALL parity constraints c_u != c_v hold, independent bits.

    For arbitrary finite graph of physical source pair labels: each
    connected bipartite component has exactly TWO valid assignments.
    A nonbipartite (odd-cycle) constraint system has probability ZERO.
    Components/vertices count only USED physical coordinate symbols.
    Duplicate constraints do not change probability.
    """
    graph=defaultdict(set)
    for e in edges:
        if type(e) not in (tuple,list) or len(e)!=2:
            raise ValueError("physical pair edge must be length two")
        u,v=e
        if type(u) is not int or type(v) is not int or u<0 or v<0 or u==v:
            raise ValueError("typed coordinate symbols nonnegative distinct ints")
        graph[u].add(v);graph[v].add(u)
    colored={}
    components=0
    for start in graph:
        if start in colored:continue
        components+=1
        colored[start]=0
        q=[start]
        while q:
            v=q.pop()
            for w in graph[v]:
                if w in colored:
                    if colored[w]==colored[v]:return Fraction(0)
                else:
                    colored[w]=1-colored[v]
                    q.append(w)
    return Fraction(1,2**(len(graph)-components))


def _typed_labels(V,labels):
    a=2
    while a*(a-1)//2<V:a+=1
    legal=set(combinations(range(a),2))
    try:pair=tuple(tuple(x) for x in labels)
    except (TypeError,ValueError):raise ValueError("invalid complete physical typed labels")
    if len(pair)!=V or len(set(pair))!=V or any(x not in legal for x in pair):
        raise ValueError("source maps must be complete globally pair-injective")
    return a,pair


def _validate_path(witness, flags,f,g,source_graph):
    """Each path witnesses real actual BOTH-diagonal edge provenance.

    A path is a pair (physical corner sequence, ordered original flag IDs).
    Coordinates separately injective. Every graph edge is specifically
    owned by that original ORIGINAL incidence flag, not just a source
    point/line projection surrogate.
    """
    corners,ids=witness
    corners=tuple(tuple(v) for v in corners)
    ids=tuple(ids)
    if len(ids) not in (2,3) or len(corners)!=len(ids)+1:
        raise ValueError("path length must be two or three real source flags")
    if any(type(i) is not int or i not in source_graph for i in ids):
        raise ValueError("missing original source flag ID from retained CORE")
    if len(set(ids))!=len(ids):
        raise ValueError("proper physical path repeated ORIGINAL source ID")
    if any(not isinstance(v,tuple) or len(v)!=2 or
           any(type(t) is not int or t<0 for t in v) for v in corners):
        raise ValueError("physical path corners invalid")
    if (len({v[0] for v in corners})!=len(corners) or
        len({v[1] for v in corners})!=len(corners)):
        raise ValueError("physical path is not coordinate-proper")
    for j,i in enumerate(ids):
        p,ell=flags[i]
        if (tuple(sorted((corners[j][0],corners[j+1][0])))!=f[p] or
            tuple(sorted((corners[j][1],corners[j+1][1])))!=g[ell]):
            raise ValueError("physical edge is not a true original flag diagonal")
    if any(v in source_graph[u] for u,v in combinations(ids,2)):
        raise ValueError("single proper path flags cannot source-conflict")
    return corners,ids


def exact_joint_path_selector_law(source_graph, flags,f,g,P,Q):
    """Exact P/Q covariance, including negative pair dependence.

    Does not require all union flag IDs to be independent, nor that the
    two physical paths be distinct or have the same endpoint pair.
    Both individually must be coordinate-proper true owner paths.
    """
    _corners_p,ip=_validate_path(P,flags,f,g,source_graph)
    _corners_q,iq=_validate_path(Q,flags,f,g,source_graph)
    union=tuple(sorted(set(ip)|set(iq)))
    priority=exact_source_priorities(source_graph,union)
    left=exact_typed_bichromatic_probability(f[flags[i][0]] for i in union)
    right=exact_typed_bichromatic_probability(g[flags[i][1]] for i in union)
    pair=priority*left*right

    def single(ids):
        prior=exact_source_priorities(source_graph,ids)
        p_left=exact_typed_bichromatic_probability(f[flags[i][0]] for i in ids)
        p_right=exact_typed_bichromatic_probability(g[flags[i][1]] for i in ids)
        if p_left!=Fraction(1,2**len(ids)) or p_right!=Fraction(1,2**len(ids)):
            raise AssertionError("a proper path does not require exactly r alternating cuts")
        return prior*p_left*p_right

    pp=single(ip);pq=single(iq)
    cov=pair-pp*pq
    return {
        "original_source_union_IDs":union,
        "path_flag_ids_P":ip,"path_flag_ids_Q":iq,
        "source_joint_priority":priority,
        "typed_left_color_probability":left,
        "typed_right_color_probability":right,
        "joint_full_path_probability":pair,
        "individual_P_probability":pp,
        "individual_Q_probability":pq,
        "covariance":cov,
        "negative_covariance":cov<0,
        "no_independence_or_positive_pair_association_assumed":True,
    }


def exact_same_endpoints_path_second_moment(source_graph,flags,f,g,witnesses):
    """Exact E[X²] where X counts the surviving supplied proper paths.

    Each supplied path has the SAME ordered endpoints; 2/3 actual flags.
    For arbitrary retained core, witness subfamilies are allowed.
    X<=A_G^r(u,v); (E X)^2 <= E X².
    """
    witnesses=tuple(witnesses)
    if not witnesses:raise ValueError("nonempty real path witness subset required")
    normalized=[_validate_path(w,flags,f,g,source_graph) for w in witnesses]
    if len(set(normalized))!=len(normalized):
        raise ValueError("duplicate directed actual path witness")
    r=len(normalized[0][1])
    start,end=normalized[0][0][0],normalized[0][0][-1]
    if any(len(ids)!=r or corners[0]!=start or corners[-1]!=end
           for corners,ids in normalized):
        raise ValueError("same ordered endpoint and length required")
    pr=[]
    pair=Fraction(0)
    positive=negative=zero=0
    for w in normalized:
        one=exact_joint_path_selector_law(source_graph,flags,f,g,w,w)
        pr.append(one["individual_P_probability"])
    for a in normalized:
        for b in normalized:
            law=exact_joint_path_selector_law(source_graph,flags,f,g,a,b)
            pair+=law["joint_full_path_probability"]
            negative+=law["covariance"]<0
            positive+=law["covariance"]>0
            zero+=law["covariance"]==0
    mean=sum(pr,Fraction(0))
    if mean*mean>pair:
        raise AssertionError("exact second moment Jensen violated")
    return {"proper_path_count":len(witnesses),"r":r,
            "original_ordered_endpoints":(start,end),
            "exact_expected_surviving_paths":mean,
            "exact_expected_surviving_paths_squared":pair,
            "exact_variance":pair-mean*mean,
            "jensen_second_moment_valid":True,
            "ordered_negative_covariance_pairs":negative,
            "ordered_positive_covariance_pairs":positive,
            "ordered_zero_covariance_pairs":zero,
            "upper_moment_relation":"E[X_uv^2] <= E[(A_G^r)_{uv}^2] (pointwise X<=A^r)",
            "no_path_independence_assumed":True}


def independent_genuine_source_path_pair_referee(power,f,g,
                                                 core_ids=None,r=2,
                                                 max_paths=32,max_pairs=12):
    """True ORIGINAL W32/W34: source-conflict graph built from RAW IDs.

    Independently derives actual paired physical diagonals and scans
    coordinate-proper directed paths. Pair law is exact rational,
    bounded by fixed K selector floor. Test samples are NOT a proof
    for arbitrary h, maps or all path pairs.
    """
    if type(power) is not int or power not in (1,2):
        raise ValueError("real GQ finite source oracle only h=1,2")
    if type(r) is not int or r not in (2,3):
        raise ValueError("actual original path lengths r=2,3")
    if type(max_paths) is not int or max_paths<1 or type(max_pairs) is not int or max_pairs<1:
        raise ValueError("positive finite exact rational audit limits")
    s,V,flags=genuine_source(power)
    a,f=_typed_labels(V,f);b,g=_typed_labels(V,g)
    if a!=b:raise AssertionError("physical point/line alphabets mismatch")
    I=tuple(range(len(flags))) if core_ids is None else tuple(core_ids)
    if len(set(I))!=len(I) or any(type(i) is not int or i<0 or i>=len(flags) for i in I):
        raise ValueError("distinct genuine ORIGINAL source core flag IDs required")
    conflict={i:set() for i in I}
    # Source FIRST pair comparison, no import of previous #679 graph.
    fs=list(map(set,f));gs=list(map(set,g))
    for i,j in combinations(I,2):
        p,l=flags[i];q,m=flags[j]
        if ((p==q and gs[l]&gs[m]) or
            (l==m and fs[p]&fs[q])):
            conflict[i].add(j);conflict[j].add(i)
    K=max((len(x) for x in conflict.values()),default=0)
    graph=defaultdict(set)
    owner={}
    for i in I:
        p,l=flags[i]
        x,z=f[p];y,w=g[l]
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            edge=frozenset((u,v))
            if edge in owner:raise AssertionError("noninjective paired physical owner")
            owner[edge]=i;graph[u].add(v);graph[v].add(u)
    if len(owner)!=2*len(I):raise AssertionError("original paired diagonal cardinality wrong")
    paths=[]
    def dfs(corners,ids):
        if len(ids)==r:
            paths.append((corners,ids))
            return
        for nxt in sorted(graph[corners[-1]]):
            if any(nxt[0]==v[0] or nxt[1]==v[1] for v in corners):continue
            new_id=owner[frozenset((corners[-1],nxt))]
            dfs(corners+(nxt,),ids+(new_id,))
            if len(paths)>=max_paths:return
    for v in sorted(graph):
        dfs((v,),())
        if len(paths)>=max_paths:break
    if not paths:
        raise ValueError("no real proper source paths for selected finite test core")
    single_probabilities=[]
    for w in paths:
        law=exact_joint_path_selector_law(conflict,flags,f,g,w,w)
        if law["individual_P_probability"]<Fraction(1,4**r*(K+1)**r):
            raise AssertionError("original #679 path selector sigma violated")
        single_probabilities.append(law["individual_P_probability"])
    negative_example=None
    checked=0
    for i in range(len(paths)):
        for j in range(i+1,len(paths)):
            if checked>=max_pairs:break
            law=exact_joint_path_selector_law(conflict,flags,f,g,paths[i],paths[j])
            if law["negative_covariance"] and negative_example is None:
                negative_example=(i,j,law)
            checked+=1
        if checked>=max_pairs:break
    groups=defaultdict(list)
    for w in paths:
        group=(w[0][0],w[0][-1])
        if len(groups[group])<3:groups[group].append(w)
    nontrivial=next((ws for ws in groups.values() if len(ws)>1),None)
    moment=(exact_same_endpoints_path_second_moment(
        conflict,flags,f,g,nontrivial) if nontrivial else None)
    return {"s":s,"V":V,"original_core_flags":len(I),
            "r":r,"original_source_conflict_cap":K,
            "original_paired_physical_edges":len(owner),
            "actual_proper_paths_sampled":len(paths),
            "actual_distinct_path_pairs_checked":checked,
            "min_original_single_path_survival":min(single_probabilities),
            "single_path_sigma":Fraction(1,4**r*(K+1)**r),
            "negative_covariance_witness":negative_example,
            "same_endpoints_exact_second_moment":moment,
            "all_h_analytic_lemma_requires_the_proof_not_finite_tests":True}
