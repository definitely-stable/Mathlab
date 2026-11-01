"""HYP-105 AA4-CODEGREE: independently exact ordinary bipartite C6 referee.

Two entirely distinct exact finite methods:
 (1) common-neighbor triple intersection / inclusion-exclusion identity;
 (2) direct six-vertex injection via independent triples of left AND right.
Then a THIRD, ORIGINAL source-ID certificate on coherent physical selected
graphs for genuine W32/W34 (not a synthetic source or historical DFS).
No call to historical C6 enumerators, GF5 classifiers or SS6 theorem.
"""
from collections import Counter
from itertools import combinations, permutations

from hyp105_full_physical_degree_tail import genuine_source


def _bit_inputs(rows, nright):
    if type(nright) is not int or nright<0 or type(rows) not in (list,tuple):
        raise ValueError("nonnegative number of right vertices and sequence of row bitsets")
    rows=tuple(rows)
    if any(type(b) is not int or b<0 or b>>nright for b in rows):
        raise ValueError("invalid simple bipartite row neighborhood bitset")
    return rows


def bipartite_c6_codegree(rows,nright):
    """EXACT no-surrogates sum over UNORDERED distinct left triples.

    For x<y<z, let A=N(x)&N(y), B=N(y)&N(z),
    C=N(z)&N(x), t=|N(x)&N(y)&N(z)|.
    All three pairwise intersections A&B, B&C, C&A equal the t-set.
    Thus count distinct right (a,b,c) =
      |A||B||C|-t*(|A|+|B|+|C|)+2*t.
    This is exactly the number of simple unoriented physical C6s whose
    left vertices are {x,y,z}, without an extra division by 6.
    """
    rows=_bit_inputs(rows,nright)
    total=0
    triangle_records=[]
    for x,y,z in combinations(range(len(rows)),3):
        a=rows[x]&rows[y]
        b=rows[y]&rows[z]
        c=rows[z]&rows[x]
        ca,cb,cc=a.bit_count(),b.bit_count(),c.bit_count()
        t=(rows[x]&rows[y]&rows[z]).bit_count()
        n=ca*cb*cc-t*(ca+cb+cc)+2*t
        if n<0:
            raise AssertionError("signed inclusion/exclusion C6 triple negative")
        total+=n
        if n:
            triangle_records.append(((x,y,z),n,(ca,cb,cc),t))
    return {"ordinary_unoriented_C6":total,
            "positive_codegree_triples":tuple(triangle_records),
            "nonzero_triples":len(triangle_records)}


def bipartite_c6_direct_six_vertex_oracle(rows,nright):
    """Completely independent brute force x<y<z and a,b,c all DISTINCT."""
    rows=_bit_inputs(rows,nright)
    result=0
    for x,y,z in combinations(range(len(rows)),3):
        for a,b,c in permutations(range(nright),3):
            if ((rows[x]>>a)&1 and (rows[y]>>a)&1 and
                (rows[y]>>b)&1 and (rows[z]>>b)&1 and
                (rows[z]>>c)&1 and (rows[x]>>c)&1):
                result+=1
    return result


def exact_codegree_clique_certificate(rows,nright,subset):
    """LOCAL, WITHOUT external SS6: if every pair within a specified
    set S of t left vertices has >=k>=3 common right neighbors, then
        #C6 >= binom(t,3) * k(k-1)(k-2).
    A direct greedy proof chooses distinct a,b,c from each pair's
    common-neighbor set, excluding at most 0,1,2 previously used choices.
    No statement that arbitrary fixed maps MUST contain such a clique.
    """
    rows=_bit_inputs(rows,nright)
    subset=tuple(subset)
    if any(type(x) is not int or x<0 or x>=len(rows) for x in subset) or len(set(subset))!=len(subset):
        raise ValueError("subset has invalid or duplicate left vertices")
    if len(subset)<3:return {"min_codegree":0,"guaranteed_C6":0,"subset_size":len(subset)}
    k=min((rows[x]&rows[y]).bit_count() for x,y in combinations(subset,2))
    from math import comb
    floor=comb(len(subset),3)*k*(k-1)*(k-2) if k>=3 else 0
    return {"min_codegree":k,"guaranteed_C6":floor,
            "subset_size":len(subset)}


def selected_original_coherent_provenance(power,f,g,source_flag_ids,left_colors,right_colors):
    """Full true symplectic ORIGINAL six-ID/codegree C6 source referee.

    Checks separately complete injected f,g, all source IDs distinct,
    NO original pencil cherry conflicts, genuine two typed binary cuts,
    BOTH physical diagonals of EVERY source flag, and each exact
    codegree C6 maps INJECTIVELY to one true ORIGINAL D6 sixset.
    """
    s,V,flags=genuine_source(power)
    a=2
    while a*(a-1)//2<V:a+=1
    f=tuple(tuple(z) for z in f)
    g=tuple(tuple(z) for z in g)
    allowed=set(combinations(range(a),2))
    if (len(f)!=V or len(g)!=V or
        len(set(f))!=V or len(set(g))!=V or
        any(z not in allowed for z in f+g)):
        raise ValueError("complete distinct typed physical pair injections required")
    if (len(left_colors)!=a or len(right_colors)!=a or
        any(type(c) is not int or c not in (0,1)
            for c in tuple(left_colors)+tuple(right_colors))):
        raise ValueError("two full binary physical coordinate cuts required")
    ids=tuple(source_flag_ids)
    if (len(set(ids))!=len(ids) or
        any(type(i) is not int or i<0 or i>=len(flags) for i in ids)):
        raise ValueError("unique genuine ORIGINAL source flag IDs required")
    for i,j in combinations(ids,2):
        p,l=flags[i];q,r=flags[j]
        if ((p==q and (set(g[l])&set(g[r]))) or
            (l==r and (set(f[p])&set(f[q])))):
            raise ValueError("source cherry conflict in selected original IDs")
    selected_edges={}
    for i in ids:
        p,l=flags[i]
        x,z=f[p];y,w=g[l]
        if left_colors[x]==left_colors[z] or right_colors[y]==right_colors[w]:
            raise ValueError("source whole-flag pair is not bichromatic on both sides")
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            e=frozenset((u,v))
            if len(e)!=2 or e in selected_edges:
                raise AssertionError("two physical diagonals duplicate or lose ORIGINAL ID")
            selected_edges[e]=i
    if len(selected_edges)!=2*len(ids):
        raise AssertionError("source flag physical paired diagonals missing")
    left=sorted({v for e in selected_edges for v in e if left_colors[v[0]]==0})
    right=sorted({v for e in selected_edges for v in e if left_colors[v[0]]==1})
    lr={v:j for j,v in enumerate(right)}
    rows=[0]*len(left)
    for x,u in enumerate(left):
        for v in right:
            if frozenset((u,v)) in selected_edges:
                rows[x]|=1<<lr[v]
    if sum(x.bit_count() for x in rows)!=len(selected_edges):
        raise AssertionError("physical graph is not a true cut bipartite graph")
    exact=bipartite_c6_codegree(rows,len(right))["ordinary_unoriented_C6"]
    sixsets=set()
    for a0,b0,c0 in combinations(range(len(left)),3):
        pair01=rows[a0]&rows[b0]
        pair12=rows[b0]&rows[c0]
        pair20=rows[c0]&rows[a0]
        for j in range(len(right)):
            if not (pair01>>j)&1:continue
            for k in range(len(right)):
                if k==j or not (pair12>>k)&1:continue
                for h in range(len(right)):
                    if h==j or h==k or not (pair20>>h)&1:continue
                    cycle=(left[a0],right[j],left[b0],right[k],left[c0],right[h])
                    if len(set(cycle))!=6:
                        raise AssertionError("C6 repeats physical vertex")
                    if (len({v[0] for v in cycle})!=6 or
                        len({v[1] for v in cycle})!=6):
                        raise AssertionError("coherent source physical C6 is not coordinate-proper")
                    owners=tuple(selected_edges[frozenset((cycle[t],cycle[(t+1)%6]))]
                                 for t in range(6))
                    if len(set(owners))!=6:
                        raise AssertionError("six physical edges not six original flag IDs")
                    if len({flags[i][0] for i in owners})!=6 or len({flags[i][1] for i in owners})!=6:
                        raise AssertionError("C6 is not original source matching D6")
                    sixset=frozenset(owners)
                    if sixset in sixsets:
                        raise AssertionError("two physical C6 maps to SAME original sixset")
                    sixsets.add(sixset)
    if len(sixsets)!=exact:
        raise AssertionError("independent source six-ID lift disagrees with codegree formula")
    return {"s":s,"original_selected_flags":len(ids),
            "paired_physical_edges":len(selected_edges),
            "bipartite_left_vertices":len(left),"bipartite_right_vertices":len(right),
            "exact_common_neighbor_C6":exact,
            "verified_distinct_original_D6":len(sixsets),
            "source_flag_sets":tuple(sorted(tuple(sorted(z)) for z in sixsets)),
            "independent_direct_six_vertex_check":
                bipartite_c6_direct_six_vertex_oracle(rows,len(right)),
            "clique_local_bound":exact_codegree_clique_certificate(
                rows,len(right),range(len(left)))["guaranteed_C6"]}


def original_independently_greedy_cut_ids(power,f,g,left_colors,right_colors):
    """No call to existing selector; simple source-ID greedy under typed cuts."""
    _,_,flags=genuine_source(power)
    picked=[]
    for i,(p,l) in enumerate(flags):
        if (left_colors[f[p][0]]==left_colors[f[p][1]] or
            right_colors[g[l][0]]==right_colors[g[l][1]]):
            continue
        if any((p==flags[j][0] and set(g[l])&set(g[flags[j][1]])) or
               (l==flags[j][1] and set(f[p])&set(f[flags[j][0]]))
               for j in picked):
            continue
        picked.append(i)
    return tuple(picked)
