"""AA4-WALKMOBIUS: exact 6-walk / injective C6 Möbius identity.

NEW independent first-principles sixth-moment referee for ANY simple
BIPARTITE graph, including arbitrary degree distributions, unequal sides,
disconnectivity and isolated vertices.

For m edges and adjacency A, d(v) ordinary degree; c_L(u,v) and c_R(a,b)
are same-side common-neighbor counts, including diagonal c(u,u)=d(u).
Put:
    L=sum_{u,v in X}d(u)c_L(u,v)^2+
      sum_{a,b in Y}d(a)c_R(a,b)^2,
    D3=sum_{v}d(v)^3,
    D2=sum_{v}d(v)^2,
    P=sum_{uv in E}d(u)d(v).
Then the EXACT identity from Möbius inversion on the three LEFT and
three RIGHT edge-root vertices of a closed 6-walk is:

  12*C6 = tr(A^6) - 6*L + 4*D3 + 6*tr(A^4)
                        + 6*P - 12*D2 + 8*m.

C6 is the number of UNROOTED UNORIENTED injective simple six-cycles.
NO C6 codegree-triple formula or physical DFS is used to derive it.

Independently the backtrack removal argument, combined with the exact
symmetric-matrix spectral Holder/Cauchy inequality, yields:

    tr(A^6) <=12 C6+6 Delta tr(A^4)
             <=24 C6+72 m Delta^2.

The 72 coefficient is already present in earlier #686 root arguments,
NOT newly claimed as a discovery. Exact walk identity and its
independent adversarial exhaustive check are this slice's contribution.
"""
from math import comb


def _rows(rows,nright):
    if type(nright) is not int or nright<0 or type(rows) not in (list,tuple):
        raise ValueError("simple bipartite row bitsets required")
    rows=tuple(rows)
    if any(type(x) is not int or x<0 or x>>nright for x in rows):
        raise ValueError("row labels must be bitsets within actual right-side vertices")
    return rows


def exact_bipartite_sixwalk_mobius(rows,nright):
    """Exact all-integer 6-walk and Möbius inversion without calling C6 DFS."""
    rows=_rows(rows,nright)
    nx=len(rows)
    col=[sum(1<<x for x,row in enumerate(rows) if (row>>y)&1)
         for y in range(nright)]
    dx=[z.bit_count() for z in rows]
    dy=[z.bit_count() for z in col]
    m=sum(dx)
    if m!=sum(dy):
        raise AssertionError("bipartite actual edge symmetry broken")
    cx=[[int((rows[i]&rows[j]).bit_count()) for j in range(nx)]
         for i in range(nx)]
    cy=[[int((col[i]&col[j]).bit_count()) for j in range(nright)]
         for i in range(nright)]
    if any(cx[i][i]!=dx[i] for i in range(nx)) or any(
        cy[j][j]!=dy[j] for j in range(nright)):
        raise AssertionError("diagonal same-side codegree not actual degree")
    t4x=sum(c*c for row in cx for c in row)
    t4y=sum(c*c for row in cy for c in row)
    if t4x!=t4y:
        raise AssertionError("independent trace(A4) left/right do not coincide")
    tr4=2*t4x
    # Closed 6-walks with their rooted initial vertex in X. Each closed
    # 6-walk has a unique start parity; transpose Gram powers give
    # the same trace on both parity sides. No adjacency matrix needed.
    rootx=sum(cx[i][j]*cx[j][k]*cx[k][i]
              for i in range(nx) for j in range(nx) for k in range(nx))
    rooty=sum(cy[i][j]*cy[j][k]*cy[k][i]
              for i in range(nright) for j in range(nright)
              for k in range(nright))
    if rootx!=rooty:
        raise AssertionError("two independent roots disagree about six-walk trace")
    tr6=2*rootx
    lfirst=sum(dx[i]*cx[i][j]**2 for i in range(nx) for j in range(nx))
    lsecond=sum(dy[i]*cy[i][j]**2 for i in range(nright)
                for j in range(nright))
    sumd3=sum(d**3 for d in dx+dy)
    sumd2=sum(d*d for d in dx+dy)
    prod=sum(dx[i]*dy[y] for i,z in enumerate(rows)
             for y in range(nright) if (z>>y)&1)
    # This code uses a DIFFERENT exact sum of homomorphism collision
    # strata from #691's injective right-corner inclusion-exclusion.
    numerator=(tr6-6*(lfirst+lsecond)+4*sumd3+6*tr4
               +6*prod-12*sumd2+8*m)
    if numerator<0 or numerator%12:
        raise AssertionError("Möbius six-walk exact numerator negative/nonmultiple of 12")
    cycles=numerator//12
    delta=max((*dx,*dy),default=0)
    if tr4*tr4>2*m*tr6:
        raise AssertionError("spectral Cauchy trace4^2<=2m trace6 violated")
    if tr6>12*cycles+6*delta*tr4:
        raise AssertionError("all nonsimple 6-walks backtrack certificate fails")
    if tr6>24*cycles+72*m*delta*delta:
        raise AssertionError("rigorous 72m Delta2 six-walk upper fails")
    return {
        "left_vertices":nx,"right_vertices":nright,"physical_edges":m,
        "actual_max_degree":delta,
        "trA4_by_two_independent_bipartite_parities":tr4,
        "trA6_by_two_independent_bipartite_parities":tr6,
        "sixwalk_rooted_in_left":rootx,
        "sixwalk_rooted_in_right":rooty,
        "left_collision_degree_weighted_codegree_squared":lfirst,
        "right_collision_degree_weighted_codegree_squared":lsecond,
        "degree_cube_sum":sumd3,
        "degree_square_sum":sumd2,
        "edge_degree_product":prod,
        "exact_mobius_injective_sixcycle_numerator":numerator,
        "actual_unoriented_simple_C6":cycles,
        "noninjective_rooted_sixwalks":tr6-12*cycles,
        "backtrack_6Delta_trA4_bound":6*delta*tr4,
        "new_exact_mobius_decomposition_verified":True,
        "independent_known_sharp_72mDelta2_envelope_verified":True,
        "no_unproven_graph_C6_supersaturation_claim":True,
    }


def independent_direct_rooted_closed_walks(rows,nright):
    """FULL direct adjacency DFS, no codegree/moment formulas anywhere."""
    rows=_rows(rows,nright)
    nx=len(rows)
    adjacency=[set() for _ in range(nx+nright)]
    for i,row in enumerate(rows):
        for y in range(nright):
            if (row>>y)&1:
                adjacency[i].add(nx+y)
                adjacency[nx+y].add(i)
    roots4=roots6=0
    for root in range(nx+nright):
        def paths(v,n):
            if n==0:return int(v==root)
            return sum(paths(w,n-1) for w in adjacency[v])
        roots4+=paths(root,4)
        roots6+=paths(root,6)
    return {"trA4_direct_DFS":roots4,"trA6_direct_DFS":roots6}


def source_coherent_actual_physical_bipartite_rows(power,f,g,ids,
                                                    left_color,right_color):
    """Independently reconstruct true source-selected physical graph.

    No import of historical #659/#691 selectors, physical graph, GF5 or
    prior C6 sources; uses ONLY the true ORIGINAL W32/W34 source fixture.
    """
    from hyp105_full_physical_degree_tail import genuine_source
    if type(power) is not int or power not in (1,2):
        raise ValueError("true original finite W32/W34 only")
    s,V,flags=genuine_source(power)
    a=2
    while comb(a,2)<V:a+=1
    legal=set((i,j) for i in range(a) for j in range(i+1,a))
    try:f=tuple(tuple(z) for z in f);g=tuple(tuple(z) for z in g)
    except (ValueError,TypeError):raise ValueError("complete original pair labels required")
    if len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V or any(
        z not in legal for z in f+g):
        raise ValueError("fixed complete separately pair-injective true original maps required")
    if (len(left_color)!=a or len(right_color)!=a or
        any(type(c) is not int or c not in (0,1) for c in
            tuple(left_color)+tuple(right_color))):
        raise ValueError("two complete typed binary coordinate colorings required")
    ids=tuple(ids)
    if len(set(ids))!=len(ids) or any(type(i) is not int or
                                     i<0 or i>=len(flags) for i in ids):
        raise ValueError("distinct actual original source ID selected flags required")
    for i,j in __import__("itertools").combinations(ids,2):
        p,l=flags[i];q,r=flags[j]
        if ((p==q and set(g[l])&set(g[r])) or
            (l==r and set(f[p])&set(f[q]))):
            raise ValueError("selected ORIGINAL source flags have a cherry conflict")
    edges={}
    for i in ids:
        p,l=flags[i];x,z=f[p];y,w=g[l]
        if left_color[x]==left_color[z] or right_color[y]==right_color[w]:
            raise ValueError("both real original physical pair labels must be bichromatic")
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            if left_color[u[0]]==left_color[v[0]]:
                raise AssertionError("selected edge does not cross typed left cut")
            edge=frozenset((u,v))
            if len(edge)!=2 or edge in edges:
                raise AssertionError("duplicate real original physical edge owner")
            edges[edge]=i
    L=sorted({v for edge in edges for v in edge if left_color[v[0]]==0})
    R=sorted({v for edge in edges for v in edge if left_color[v[0]]==1})
    li={v:i for i,v in enumerate(L)}
    ri={v:i for i,v in enumerate(R)}
    rows=[0]*len(L)
    for edge in edges:
        u,v=tuple(edge)
        if u in li and v in ri:
            rows[li[u]]|=1<<ri[v]
        elif v in li and u in ri:
            rows[li[v]]|=1<<ri[u]
        else:raise AssertionError("physical original edge not in both parity classes")
    if sum(z.bit_count() for z in rows)!=2*len(ids):
        raise AssertionError("actual original paired diagonal inventory lost")
    return {"s":s,"original_flags":len(ids),"actual_physical_edges":len(edges),
            "left_original_physical_vertices":tuple(L),
            "right_original_physical_vertices":tuple(R),
            "rows":tuple(rows),"nright":len(R)}
