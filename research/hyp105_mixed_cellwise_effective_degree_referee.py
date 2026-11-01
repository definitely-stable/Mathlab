"""AA4-CELLREF: independent all-h cell-support/effective-degree blocker referee.

NEW exact deterministic all-h inequality for a finite simple graph H0,
arbitrary candidate first-edge triples T (including original W(3,s) ones):
  W^2 <= Xi * Theta_T <= B * Theta <= B*Delta*tr(A^4),
where
  B=|T|, m(u,w)=#{v0:(v0,u,w) in T}, d(u)=deg_H0(u),
  Xi=sum_{m>0} m(u,w)^2/d(u),
  Theta_T=sum_{m>0} d(u)*(A²[u,w])²,
  Theta=sum_u d(u)*(A^4)[u,u].
No independence, choice of f,g, or external SS6 is required.
Includes physically independent original-source and full-original-book
record enumeration on true W(3,2),W(3,4) only as FINITE falsifiers.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations

from hyp105_full_physical_degree_tail import genuine_source


def _typed(V,labels):
    if type(labels) not in (list,tuple) or len(labels)!=V:
        raise ValueError("complete original factor labeling required")
    a=2
    while a*(a-1)//2<V:a+=1
    pairset=set(combinations(range(a),2))
    labels=tuple(tuple(z) for z in labels)
    if len(set(labels))!=V or any(z not in pairset for z in labels):
        raise ValueError("original factor pair assignment not legal/injective")
    return a,labels


def _source(V,flags):
    point_lines=[set() for _ in range(V)]
    line_points=[set() for _ in range(V)]
    for p,l in flags:
        point_lines[p].add(l)
        line_points[l].add(p)
    projections={}
    collinear=[]
    for q in range(V):
        collinear.append(set().union(*(line_points[l] for l in point_lines[q]))-{q})
    for q in range(V):
        for r in range(V):
            if r in point_lines[q]:continue
            common=line_points[r]&collinear[q]
            if len(common)!=1:
                raise AssertionError("genuine original GQ projection not unique")
            p=next(iter(common))
            connecting=point_lines[p]&point_lines[q]
            if len(connecting)!=1:
                raise AssertionError("missing unique original connecting source line")
            projections[q,r]=(p,next(iter(connecting)))
    return point_lines,collinear,projections


def _paired(flags,f,g,ids):
    adjacency=defaultdict(set)
    owner={}
    for i in ids:
        p,l=flags[i]
        x,z=f[p];y,w=g[l]
        for v,t in (((x,y),(z,w)),((x,w),(z,y))):
            edge=frozenset((v,t))
            if len(edge)!=2 or edge in owner:
                raise AssertionError("two diagonal actual ORIGINAL edge ownership invalid")
            owner[edge]=i
            adjacency[v].add(t);adjacency[t].add(v)
    return dict(adjacency),owner


def _candidate_physical(adjacency, f,g, projections):
    """Physical-first extraction: do NOT use source pencil K_pu tensor."""
    sx=defaultdict(list)
    sy=defaultdict(list)
    for q,pair in enumerate(f):
        for v in pair:sx[v].append(q)
    for r,pair in enumerate(g):
        for v in pair:sy[v].append(r)
    out=set()
    for v0,near in adjacency.items():
        x,y=v0
        for v1 in near:
            k=v1[0]
            for q in sx[x]:
                z=f[q][0] if f[q][1]==x else f[q][1]
                for r in sy[y]:
                    anchor=projections.get((q,r))
                    if anchor is None or k not in f[anchor[0]]:
                        continue
                    w=g[r][0] if g[r][1]==y else g[r][1]
                    out.add((v0,v1,(z,w)))
    return out


def _candidate_original(flags,ids,f,g,source):
    """SOURCE-first: full original p,r incidence records, even outside core."""
    pencils,collinear,projections=source
    sx=defaultdict(set)
    for p,pair in enumerate(f):
        for x in pair:sx[x].add(p)
    phi=psi=0
    triples=set()
    for i in ids:
        u,lam=flags[i]
        for x,k in ((f[u][0],f[u][1]),(f[u][1],f[u][0])):
            for y,t in ((g[lam][0],g[lam][1]),(g[lam][1],g[lam][0])):
                for p in sx[k]:
                    for q in sx[x]&collinear[p]:
                        z=f[q][0] if f[q][1]==x else f[q][1]
                        for r in pencils[p]:
                            if y not in g[r]:continue
                            phi+=1
                            if r in pencils[q]:
                                psi+=1
                                continue
                            if projections[q,r][0]!=p:
                                raise AssertionError("wrong original projection counted")
                            w=g[r][0] if g[r][1]==y else g[r][1]
                            triples.add(((x,y),(k,t),(z,w)))
    if phi-psi!=len(triples):
        raise AssertionError("full-original Phi-Psi not injective to physical triples")
    return phi,psi,triples


def arbitrary_graph_cellwise_certificate(adjacency,triples):
    """ALL finite simple graphs, ALL candidate oriented first-edge triples.

    Independent exact rational weighted Cauchy: alpha_t=m(u,w)/d(u),
    Xi=sum m²/d, Theta_T=sum_{m>0} d*(A²)².
    """
    graph={v:set(nears) for v,nears in adjacency.items()}
    if any(v in nears or any(w not in graph or v not in graph[w] for w in nears)
           for v,nears in graph.items()):
        raise ValueError("input must be undirected simple graph with both endpoints")
    triples=tuple(triples)
    if len(set(triples))!=len(triples):
        raise ValueError("ordered candidate triples must be distinct")
    cells=Counter()
    for v0,u,w in triples:
        if v0 not in graph or u not in graph[v0] or u not in graph:
            raise ValueError("each triple begins with a directed actual graph edge")
        cells[u,w]+=1
    a2=defaultdict(Counter)
    for u,near in graph.items():
        for v in near:
            a2[u].update(graph[v])
    degrees={u:len(near) for u,near in graph.items()}
    B=len(triples)
    W=sum(mult*a2[u][w] for (u,w),mult in cells.items())
    Xi=sum((Fraction(mult*mult,degrees[u]) for (u,w),mult in cells.items()),Fraction())
    theta_supported=sum(degrees[u]*a2[u][w]**2 for u,w in cells)
    theta=sum(degrees[u]*sum(v*v for v in a2[u].values()) for u in graph)
    trace4=sum(sum(v*v for v in a2[u].values()) for u in graph)
    delta=max(degrees.values(),default=0)
    ordinary_cell_energy=sum(mult*a2[u][w]**2 for (u,w),mult in cells.items())
    if (any(mult>degrees[u] for (u,w),mult in cells.items()) or
        not (Fraction(W*W)<=Xi*theta_supported<=Fraction(B*theta)
             <=Fraction(B*delta*trace4))):
        raise AssertionError("new support-weighted Cauchy and fourth-moment chain fails")
    return {
        "triples":B,"physical_cell_count":len(cells),
        "weighted_completions":W,"Xi_effective_first_edge":Xi,
        "supported_degree_weighted_moment":theta_supported,
        "full_degree_weighted_moment":theta,"traceA4":trace4,
        "max_physical_degree":delta,
        "ordinary_cell_energy":ordinary_cell_energy,
        "old_cauchy_bound":Fraction(B*theta),
        "new_cauchy_bound":Xi*theta_supported,
        "new_never_worse":True,
        "strict_improvement":Xi*theta_supported<Fraction(B*theta),
        "exact_cell_multiplicities":tuple(sorted(cells.items(),key=lambda e:repr(e[0]))),
    }


def independent_original_cell_referee(power, f,g,core_ids=None):
    """TRUE source FIRST and PHYSICAL FIRST audits, including four positions.

    Finite only for W32/W34; the mathematical inequality above is all-h.
    """
    if type(power) is not int or power not in (1,2):
        raise ValueError("finite original symplectic oracle supports powers 1,2")
    s,V,flags=genuine_source(power)
    a,f=_typed(V,f)
    b,g=_typed(V,g)
    if a!=b:raise AssertionError("typed physical pair alphabets differ")
    ids=tuple(range(len(flags))) if core_ids is None else tuple(core_ids)
    if (any(type(i) is not int or i<0 or i>=len(flags) for i in ids)
        or len(set(ids))!=len(ids)):
        raise ValueError("duplicate/unknown ORIGINAL incidence flag IDs")
    graph,owners=_paired(flags,f,g,ids)
    src=_source(V,flags)
    phys=_candidate_physical(graph,f,g,src[2])
    phi,psi,original=_candidate_original(flags,ids,f,g,src)
    if phys!=original:
        raise AssertionError("independent full-source and physical blocked triples disagree")
    left=arbitrary_graph_cellwise_certificate(graph,phys)
    dual_flags=tuple((l,p) for p,l in flags)
    dgraph,downer=_paired(dual_flags,g,f,ids)
    dsrc=_source(V,dual_flags)
    dphys=_candidate_physical(dgraph,g,f,dsrc[2])
    dphi,dpsi,doriginal=_candidate_original(dual_flags,ids,g,f,dsrc)
    if dphys!=doriginal:
        raise AssertionError("source/physical dual mixed blockers disagree")
    right=arbitrary_graph_cellwise_certificate(dgraph,dphys)
    if (left["full_degree_weighted_moment"]!=right["full_degree_weighted_moment"]
        or left["traceA4"]!=right["traceA4"] or len(owners)!=len(downer)):
        raise AssertionError("dual original source transpose failed")
    # Directly count four blocked positions on ALL PHYSICAL proper
    # three-paths; no book or cell m counts used to select these paths.
    invf={pair:p for p,pair in enumerate(f)}
    invg={pair:l for l,pair in enumerate(g)}
    positions=[0,0,0,0]
    union=0
    proper=0
    for v0,near in graph.items():
        for v1 in near:
            for v2 in graph[v1]:
                for v3 in graph[v2]:
                    if (len({v[0] for v in (v0,v1,v2,v3)})!=4 or
                        len({v[1] for v in (v0,v1,v2,v3)})!=4):
                        continue
                    q=invf.get(tuple(sorted((v0[0],v3[0]))))
                    r=invg.get(tuple(sorted((v0[1],v3[1]))))
                    anchor=src[2].get((q,r))
                    if anchor is None:continue
                    p,l=anchor
                    checks=(v1[0] in f[p],v2[0] in f[p],
                            v1[1] in g[l],v2[1] in g[l])
                    proper+=1
                    union+=any(checks)
                    for j,flag in enumerate(checks):positions[j]+=flag
    if not (positions[0]==positions[1]<=left["weighted_completions"]
            and positions[2]==positions[3]<=right["weighted_completions"]
            and union<=2*(left["weighted_completions"]+right["weighted_completions"])):
        raise AssertionError("four internal positions contradiction")
    return {
        "s":s,"original_core_ids":len(ids),
        "original_core_physical_edges":len(owners),
        "left":left,"right":right,
        "original_full_core_phi":phi,"original_incident_defect":psi,
        "original_dual_full_core_phi":dphi,"original_dual_incident_defect":dpsi,
        "four_physical_blocked_positions":tuple(positions),
        "proper_original_end_decoded_paths":proper,
        "four_position_union":union,
        "four_position_support_weighted_upper":
            2*(left["weighted_completions"]+right["weighted_completions"]),
        "source_physical_identity_verified":True,
    }
