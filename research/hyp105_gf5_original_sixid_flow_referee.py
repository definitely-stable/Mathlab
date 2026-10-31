"""AA4-GF5REF: independent full 51-palette flow referee on ORIGINAL six IDs.

Two mathematically different EXACT coefficient oracles:
  (1) inclusion-exclusion over all 2^12 subsets of coordinate edges;
  (2) nonzero chord enumeration plus uniquely solved tree-edge currents.
All cases use six *named* ORIGINAL columns, two colored coordinate halves,
ten global-sign-unordered 3+3 partitions and six distinct original flags.
NO historical GF5 classifier, Fourier oracle or precomputed flow table used.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from math import comb

from hyp105_full_physical_degree_tail import genuine_source

COLUMNS=6
PHYSICAL_EDGES=12
SIGNS=tuple(frozenset((0,)+other) for other in combinations(range(1,6),2))


def c4_edge_sets(columns):
    """All three distinct SIMPLE four-cycles on four named column vertices."""
    columns=tuple(sorted(columns))
    if len(columns)!=4 or len(set(columns))!=4:
        raise ValueError("four distinct named columns required")
    out=set()
    for tail in permutations(columns[1:]):
        path=(columns[0],)+tail
        out.add(tuple(sorted(tuple(sorted((path[i],path[(i+1)%4])))
                             for i in range(4))))
    result=tuple(sorted(out))
    if len(result)!=3:
        raise AssertionError("exactly three C4s required")
    return result


def bb_overlap_templates():
    """Nine 2C2/C4 configurations; repeated ORIGINAL pairs share ID 0."""
    for a in c4_edge_sets((2,3,4,5)):
        for b in c4_edge_sets((1,3,4,5)):
            yield (((0,1),(0,1))+a+((0,2),(0,2))+b)


def coincident_c6_template():
    cycle=tuple(tuple(sorted((i,(i+1)%6))) for i in range(6))
    return cycle+cycle


def _check_flow_input(edges,plus):
    edges=tuple(tuple(pair) for pair in edges)
    plus=frozenset(plus)
    if len(edges)!=PHYSICAL_EDGES or len(plus)!=3 or 0 not in plus:
        raise ValueError("12 colored coordinate edges and canonical 3+3 signs required")
    if any(len(e)!=2 or any(type(v) is not int or v<0 or v>=6 for v in e)
           or e[0]==e[1] for e in edges):
        raise ValueError("every physical coordinate must connect two distinct named columns")
    if any(sum(v in edge for edge in edges[:6])!=2 for v in range(6)):
        raise ValueError("each column must have two left coordinates")
    if any(sum(v in edge for edge in edges[6:])!=2 for v in range(6)):
        raise ValueError("each column must have two right coordinates")
    return edges,plus


def gf5_flow_inclusion_exclusion(edges,plus):
    """Direct 4096-subset original-graph rank formula; arbitrary parallel edges."""
    edges,plus=_check_flow_input(edges,plus)
    demands=tuple(4 if i in plus else -4 for i in range(6))
    total=0
    for mask in range(1<<12):
        parent=list(range(6))
        def root(v):
            while parent[v]!=v:
                parent[v]=parent[parent[v]]
                v=parent[v]
            return v
        for j,(u,v) in enumerate(edges):
            if mask & (1<<j):
                ru,rv=root(u),root(v)
                parent[rv]=ru
        balance=[0]*6
        vertices=[0]*6
        for i,d in enumerate(demands):
            r=root(i)
            balance[r]+=d
            vertices[r]+=1
        if any(balance[i]%5 for i in range(6) if vertices[i]):
            continue
        components=sum(v>0 for v in vertices)
        dimension=mask.bit_count()-6+components
        if dimension<0:
            raise AssertionError("incidence rank dimension negative")
        total+=(-1 if (12-mask.bit_count())%2 else 1)*5**dimension
    if total<0 or total>51**6:
        raise AssertionError("invalid signed full-palette coefficient count")
    return total


def gf5_flow_spanning_tree(edges,plus):
    """Independent direct primal oracle: 4^7 nowhere-zero chord assignments.

    Each selected chord is nonzero; tree edge variables are uniquely
    determined by leaf-to-root balance and rejected if zero. No IE or
    contraction rank theorem is used to count the returned solutions.
    """
    edges,plus=_check_flow_input(edges,plus)
    adjacency=[[] for _ in range(6)]
    for k,(u,v) in enumerate(edges):
        adjacency[u].append((v,k))
        adjacency[v].append((u,k))
    parent=[-1]*6;parent_edge=[-1]*6
    parent[0]=0
    bfs=[0]
    for v in bfs:
        for w,j in adjacency[v]:
            if parent[w]<0:
                parent[w]=v
                parent_edge[w]=j
                bfs.append(w)
    if len(bfs)!=6:
        raise ValueError("direct tree solver requires connected six-column graph")
    tree_edges=set(parent_edge[1:])
    chords=tuple(j for j in range(12) if j not in tree_edges)
    if len(chords)!=7:
        raise AssertionError("connected 6-vertex 12-edge graph needs 7 chords")
    demand=tuple(4 if i in plus else -4 for i in range(6))
    valid=0
    for currents in product(range(1,5),repeat=7):
        residual=list(demand)
        for j,x in zip(chords,currents):
            u,v=edges[j]
            residual[u]=(residual[u]-x)%5
            residual[v]=(residual[v]+x)%5
        for v in reversed(bfs[1:]):
            parent_v=parent[v]
            edge=edges[parent_edge[v]]
            forced=(residual[v] if edge[0]==v else -residual[v])%5
            if forced==0:
                break
            residual[parent_v]=(residual[parent_v]+residual[v])%5
        else:
            if residual[0]%5==0:
                valid+=1
    return valid


def complete_bb_overlap_census(*, direct_crosscheck=False):
    """All 90 named signed cases; 3*53838+6*53526 = 482670."""
    profiles=[]
    min_flow=51**6;max_flow=0;positive=0
    for j,edges in enumerate(bb_overlap_templates()):
        coeff=tuple(gf5_flow_inclusion_exclusion(edges,sign) for sign in SIGNS)
        if direct_crosscheck:
            # All ten independent primal counts on first C4/C4 profile;
            # one representative on each other profile.
            targets=range(10) if j==0 else (0,)
            for k in targets:
                if gf5_flow_spanning_tree(edges,SIGNS[k])!=coeff[k]:
                    raise AssertionError("independent direct GF5 tree flow differs")
        min_flow=min(min_flow,*coeff)
        max_flow=max(max_flow,*coeff)
        positive+=sum(c>0 for c in coeff)
        profiles.append({"c4_left":edges[:6],"c4_right":edges[6:],
                         "signed_flows":coeff,"total":sum(coeff)})
    total=sum(p["total"] for p in profiles)
    return {"profiles":tuple(profiles),"signed_cases":90,
            "positive_cases":positive,"min":min_flow,"max":max_flow,
            "total_all_nine_and_ten":total,"all_positive":positive==90}


def _minimal_alphabet(V):
    a=2
    while comb(a,2)<V:a+=1
    return a


def _fill_f_g(V,a,seed_point,seed_line):
    all_pairs=tuple(combinations(range(a),2))
    f=[None]*V;g=[None]*V
    for labels,seeds in ((f,seed_point),(g,seed_line)):
        if len(set(seeds.values()))!=len(seeds):
            raise AssertionError("duplicate planted typed physical pairs")
        if any(not 0<=p<V or pair not in all_pairs for p,pair in seeds.items()):
            raise AssertionError("invalid planted original factor")
        for p,pair in seeds.items():labels[p]=pair
        unused=(pair for pair in all_pairs if pair not in seeds.values())
        for p in range(V):
            if labels[p] is None:labels[p]=next(unused)
        if len(set(labels))!=V:
            raise AssertionError("globally injected typed physical pair map failed")
    return tuple(f),tuple(g)


def original_projected_column_edges(flags,source_ids,f,g):
    """Create real 12 physical coordinate incidences directly from ORIGINAL IDs."""
    ids=tuple(source_ids)
    if len(ids)!=6 or len(set(ids))!=6 or any(
            type(i) is not int or i<0 or i>=len(flags) for i in ids):
        raise ValueError("six distinct valid ORIGINAL incidence IDs required")
    columns=[flags[i] for i in ids]
    physical=[]
    for typed,side in ((f,0),(g,1)):
        starts=defaultdict(list)
        for j,flag in enumerate(columns):
            label=typed[flag[side]]
            if len(label)!=2 or label[0]==label[1]:
                raise ValueError("each source factor must map to a proper pair")
            for coord in label:
                starts[coord].append(j)
        if len(starts)!=6 or any(len(v)!=2 for v in starts.values()):
            raise ValueError("selected ORIGINAL sixset not 6-coordinate leafless")
        physical.extend(tuple(sorted(starts[x])) for x in sorted(starts))
    return tuple(physical)


def planted_original_bb_overlap(power):
    """True W(3,2), W(3,4): q--ell--p--r plus 3 independent source IDs.

    f(q),f(u1..u3) and g(r),g(lambda1..lambda3) are each a physical
    C4 on 0,1,2,3; f(p) and g(ell) are the disjoint 4,5 double pairs.
    The six source flags are never invented synthetic incidences.
    """
    if type(power) is not int or power not in (1,2):
        raise ValueError("genuine ORIGINAL test source only W32/W34")
    s,V,flags=genuine_source(power)
    a=_minimal_alphabet(V)
    pencils=[set() for _ in range(V)]
    on_line=[set() for _ in range(V)]
    flag_id={flag:i for i,flag in enumerate(flags)}
    for q,r in flags:
        pencils[q].add(r);on_line[r].add(q)
    q=0
    r=next(r for r in range(V) if r not in pencils[q])
    friends=set().union(*(on_line[ell] for ell in pencils[q]))-{q}
    anchors=on_line[r]&friends
    if len(anchors)!=1:
        raise AssertionError("genuine GQ projection not unique")
    p=next(iter(anchors))
    linking=pencils[q]&pencils[p]
    if len(linking)!=1:
        raise AssertionError("unique original connecting line absent")
    ell=next(iter(linking))
    match=[];used_p={p,q};used_l={ell,r}
    for i,(u,lam) in enumerate(flags):
        if u not in used_p and lam not in used_l:
            match.append(i);used_p.add(u);used_l.add(lam)
            if len(match)==3:break
    if len(match)!=3:
        raise AssertionError("three disjoint original flags unavailable")
    triples=tuple(flags[i] for i in match)
    around=((0,1),(1,2),(2,3))
    fs={q:(0,3),p:(4,5)}
    gs={r:(0,3),ell:(4,5)}
    for (u,lam),pair in zip(triples,around):
        fs[u]=pair;gs[lam]=pair
    f,g=_fill_f_g(V,a,fs,gs)
    ids=(flag_id[q,ell],flag_id[p,ell],flag_id[p,r],*match)
    if len(set(ids))!=6:
        raise AssertionError("original flag ID overlap")
    edges=original_projected_column_edges(flags,ids,f,g)
    counts_p=Counter(flags[i][0] for i in ids)
    counts_l=Counter(flags[i][1] for i in ids)
    if sorted(counts_p.values())!=[1,1,1,1,2] or sorted(counts_l.values())!=[1,1,1,1,2]:
        raise AssertionError("original B/B repeated factor profile invalid")
    repeated_p={i for i,j in enumerate(ids) if flags[j][0]==p}
    repeated_l={i for i,j in enumerate(ids) if flags[j][1]==ell}
    if len(repeated_p&repeated_l)!=1:
        raise AssertionError("historical ORIGINAL B/B overlap not exactly one ID")
    if any(gf5_flow_inclusion_exclusion(edges,sig)<5175 for sig in SIGNS):
        raise AssertionError("planted ORIGINAL B/B overlap loses GF5 positivity")
    return {"s":s,"V":V,"ids":ids,"flags":tuple(flags),
            "f":f,"g":g,"edges":edges}


def planted_original_d6(power):
    """Genuine matching flags + two coincident coordinate C6 projections."""
    if type(power) is not int or power not in (1,2):
        raise ValueError("genuine ORIGINAL test source only W32/W34")
    s,V,flags=genuine_source(power)
    a=_minimal_alphabet(V)
    matching=[];points=set();lines=set()
    for i,(p,ell) in enumerate(flags):
        if p not in points and ell not in lines:
            matching.append(i);points.add(p);lines.add(ell)
            if len(matching)==6:break
    if len(matching)!=6:
        raise AssertionError("six source matching flags not available")
    sixcycle=tuple(tuple(sorted((i,(i+1)%6))) for i in range(6))
    fs={flags[i][0]:pair for i,pair in zip(matching,sixcycle)}
    gs={flags[i][1]:pair for i,pair in zip(matching,sixcycle)}
    f,g=_fill_f_g(V,a,fs,gs)
    edges=original_projected_column_edges(flags,matching,f,g)
    if gf5_flow_inclusion_exclusion(edges,SIGNS[5])!=5643:
        # SIGNS[5] is {0,2,4} for the standard combinations order.
        raise AssertionError("ORIGINAL planted D6 alternating coefficient differs")
    return {"s":s,"ids":tuple(matching),"flags":tuple(flags),
            "f":f,"g":g,"edges":edges}
