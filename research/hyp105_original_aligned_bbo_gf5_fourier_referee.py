"""R6 AA4-ALIGNGF5: exact aligned ORIGINAL B/B-overlap signed-mass theorem.

All-h theorem (not inferred from finite fixture):
a produced ORIGINAL B/B sixset has the SAME center among its three
non-anchor source IDs in the left and right C4 column incidence cycles.
Precisely three of nine C4/C4 templates are compatible, and those have
ten-sign GF(5) total 53838 rather than the general BBo floor 53526.

Independent exact third GF(5) oracle uses character orthogonality over
5^5 potentials with INTEGER values (no complex/float arithmetic), not
prior inclusion-exclusion over edge subsets or spanning-tree currents.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, isqrt

from hyp105_full_physical_degree_tail import genuine_source

PALETTE=51
PALETTE_SIX=PALETTE**6
SIGNED_D6=54162
SIGNED_ALIGNED_BBO=53838
SIGNED_UNALIGNED_BBO=53526
SIGNS=tuple(frozenset((0,i,j)) for i,j in combinations(range(1,6),2))


def _cycles(four):
    four=tuple(sorted(four))
    if len(four)!=4 or len(set(four))!=4:
        raise ValueError("four distinct ORIGINAL column positions required")
    allcycles=set()
    for tail in permutations(four[1:]):
        walk=(four[0],)+tail
        allcycles.add(tuple(sorted(tuple(sorted((walk[j],walk[(j+1)%4])))
                                   for j in range(4))))
    if len(allcycles)!=3:
        raise AssertionError("each named four-column side has precisely three C4 structures")
    return tuple(sorted(allcycles))


def _opposite(cycle,anchor):
    neighbours=defaultdict(set)
    for u,v in cycle:
        neighbours[u].add(v)
        neighbours[v].add(u)
    if set(neighbours)!=set(range(1,6))-{1 if anchor==2 else 2}:
        raise ValueError("invalid canonical ORIGINAL BBo four-vertex cycle")
    if anchor not in neighbours or any(len(z)!=2 for z in neighbours.values()):
        raise ValueError("not a simple four-cycle")
    opposite=set(neighbours)-{anchor}-neighbours[anchor]
    if len(opposite)!=1:
        raise AssertionError("unique non-anchor opposite original column missing")
    return next(iter(opposite))


def aligned_template_types():
    """Canonical ORIGINAL columns:
       0=(p,ell), 1=(p,r), 2=(q,ell), 3..5=actual path owners.
       Left C4 on 2,3,4,5; right C4 on 1,3,4,5.
    """
    out=[]
    for left in _cycles((2,3,4,5)):
        for right in _cycles((1,3,4,5)):
            lcenter=_opposite(left,2)
            rcenter=_opposite(right,1)
            out.append({
                "left":left,"right":right,"left_middle_owner":lcenter,
                "right_middle_owner":rcenter,
                "aligned":lcenter==rcenter,
                "edges":((0,1),(0,1))+left+((0,2),(0,2))+right
            })
    if len(out)!=9 or sum(x["aligned"] for x in out)!=3:
        raise AssertionError("nine types / three original aligned BBo types")
    return tuple(out)


def gf5_fourier_potential_oracle(edges, plus):
    """EXACT GF(5) nowhere-zero current count via finite Fourier inversion.

    Let edge current x!=0, Bx=b with b_i=4 sigma_i. Character
    orthogonality gives count = 5^-5 sum_{phi_0=0, phi_1..5 in GF5}
       omega^(-b.phi) PROD_edges (4 if phi_u==phi_v else -1).
    The 4 nonzero root coefficients coincide by phi->t*phi, t!=0.
    Thus result=(C0-C1)/3125 in INTEGER arithmetic, no complex roots.
    """
    edges=tuple(tuple(e) for e in edges)
    plus=frozenset(plus)
    if (len(edges)!=12 or len(plus)!=3 or 0 not in plus
        or any(len(e)!=2 or e[0]==e[1] or
               any(type(i) is not int or i not in range(6) for i in e)
               for e in edges)):
        raise ValueError("twelve true coordinate edges and valid canonical signs required")
    if any(sum(v in e for e in edges[:6])!=2 or
           sum(v in e for e in edges[6:])!=2 for v in range(6)):
        raise ValueError("each ORIGINAL column must have two coordinates per factor")
    b=tuple(4 if i in plus else -4 for i in range(6))
    if sum(b)!=0:
        raise AssertionError("balanced signed six-column demand required")
    bucket=[0]*5
    for other in product(range(5),repeat=5):
        phi=(0,)+other
        w=1
        for u,v in edges:
            w*=4 if phi[u]==phi[v] else -1
        exponent=(-sum(b[i]*phi[i] for i in range(6)))%5
        bucket[exponent]+=w
    if len(set(bucket[1:]))!=1:
        raise AssertionError("nonzero fifth-root Fourier bucket symmetry broken")
    difference=bucket[0]-bucket[1]
    if difference%5**5:
        raise AssertionError("GF5 Fourier root expression not exact integer")
    result=difference//5**5
    if not 0<=result<=PALETTE_SIX:
        raise AssertionError("outside 51^6 original palette")
    return result


def source_six_original_ids(power):
    """Construct genuine q-ell-p-r + three disjoint genuine source flags.

    No fake ORIGINAL flags or independent physical edge IDs.
    """
    s,v,flags=genuine_source(power)
    pencil=[set() for _ in range(v)]
    through=[set() for _ in range(v)]
    owner={}
    for i,(p,r) in enumerate(flags):
        pencil[p].add(r)
        through[r].add(p)
        owner[p,r]=i
    q=0
    r=next(x for x in range(v) if x not in pencil[q])
    collinear=set().union(*(through[line] for line in pencil[q]))-{q}
    ps=through[r]&collinear
    if len(ps)!=1:
        raise AssertionError("true original GQ nonincident projection failed")
    p=next(iter(ps))
    connecting=pencil[q]&pencil[p]
    if len(connecting)!=1:
        raise AssertionError("source anchor line not unique")
    ell=next(iter(connecting))
    matching=[]
    used_p={p,q};used_l={ell,r}
    for i,(u,l) in enumerate(flags):
        if u not in used_p and l not in used_l:
            matching.append(i)
            used_p.add(u);used_l.add(l)
            if len(matching)==3:
                break
    if len(matching)!=3:
        raise AssertionError("true original W32/W34 matching missing")
    ids=(owner[p,ell],owner[p,r],owner[q,ell],*matching)
    if len(set(ids))!=6:
        raise AssertionError("six original IDs not distinct")
    return s,v,tuple(flags),ids


def _complete_map(v,seeds):
    a=(1+isqrt(1+8*v))//2
    while comb(a,2)<v:
        a+=1
    labels=tuple(combinations(range(a),2))
    if len(set(seeds.values()))!=len(seeds):
        raise AssertionError("noninjective planted pair labels")
    if any(not 0<=i<v or pair not in labels for i,pair in seeds.items()):
        raise AssertionError("planted original pair outside minimal alphabet")
    remaining=iter(pair for pair in labels if pair not in set(seeds.values()))
    out=tuple(seeds[i] if i in seeds else next(remaining) for i in range(v))
    if len(out)!=v or len(set(out))!=v:
        raise AssertionError("incomplete true original f/g injection")
    return out


def _factor_from_cycle(cycle):
    """Original factor/column as two physical coordinate edge IDs."""
    return {col:tuple(j for j,e in enumerate(cycle) if col in e)
            for col in sorted({x for e in cycle for x in e})}


def lift_template(power, typ):
    """Nine types on the SAME true ORIGINAL six flags and complete f,g."""
    s,v,flags,ids=source_six_original_ids(power)
    left=_factor_from_cycle(typ["left"])
    right=_factor_from_cycle(typ["right"])
    fs={flags[ids[0]][0]:(4,5)}
    gs={flags[ids[0]][1]:(4,5)}
    for j in left:
        fs[flags[ids[j]][0]]=left[j]
    for j in right:
        gs[flags[ids[j]][1]]=right[j]
    f=_complete_map(v,fs)
    g=_complete_map(v,gs)
    if len({flags[i][0] for i in ids})!=5 or len({flags[i][1] for i in ids})!=5:
        raise AssertionError("not actual BBo repeated ORIGINAL point/line")
    return s,v,flags,ids,f,g


def source_coordinate_edges(flags,ids,f,g):
    """Independently reconstruct column multigraph from ORIGINAL six IDs."""
    if len(ids)!=6 or len(set(ids))!=6:
        raise ValueError("six distinct actual original source IDs required")
    edges=[]
    for side,labels in ((0,f),(1,g)):
        buckets=defaultdict(list)
        for j,i in enumerate(ids):
            for coordinate in labels[flags[i][side]]:
                buckets[coordinate].append(j)
        if len(buckets)!=6 or any(len(z)!=2 for z in buckets.values()):
            raise AssertionError("original sixset is not degree-two six-coordinate on both factors")
        edges.extend(tuple(sorted(z)) for coord,z in sorted(buckets.items()))
    return tuple(edges)


def classify_original_six_alignment(flags,ids,f,g):
    """Canonicalize an arbitrary unordered original BBo sixset, not a template."""
    if len(ids)!=6 or len(set(ids))!=6:
        raise ValueError("exact six distinct true original source flags")
    seq=tuple(flags[i] for i in ids)
    pc=Counter(p for p,_ in seq);lc=Counter(ell for _,ell in seq)
    if sorted(pc.values())!=[1,1,1,1,2] or sorted(lc.values())!=[1,1,1,1,2]:
        raise ValueError("not ORIGINAL B/B repeated factor profile")
    p=next(k for k,n in pc.items() if n==2)
    ell=next(k for k,n in lc.items() if n==2)
    root=[i for i in ids if flags[i]==(p,ell)]
    if len(root)!=1:
        raise ValueError("not ORIGINAL B/B-overlap repeated-source intersection")
    second=[i for i in ids if flags[i][0]==p and i!=root[0]]
    third=[i for i in ids if flags[i][1]==ell and i!=root[0]]
    if len(second)!=1 or len(third)!=1:
        raise AssertionError("BBo anchors not unique")
    rest=tuple(sorted(set(ids)-{root[0],second[0],third[0]}))
    ordered=(root[0],second[0],third[0])+rest
    edges=source_coordinate_edges(flags,ordered,f,g)
    left=tuple(sorted(edges[:6][2:])) if False else tuple(sorted(e for e in edges[:6] if e!=(0,1)))
    right=tuple(sorted(e for e in edges[6:] if e!=(0,2)))
    if (edges[:6].count((0,1))!=2 or edges[6:].count((0,2))!=2
        or len(left)!=4 or len(right)!=4):
        raise ValueError("not physical BBo doubled pair plus C4")
    lc=_opposite(left,2);rc=_opposite(right,1)
    return {"ordered_original_ids":ordered,"left_middle_owner":lc,
            "right_middle_owner":rc,"aligned":lc==rc,"edges":edges}


def count_actual_physical_owner_paths(flags,ids,f,g):
    """For exactly three non-anchor owners, independently count P4 routes
       closing to original q,r; FULL anchor IDs are NOT in physical CORE.
    """
    anchor=classify_original_six_alignment(flags,ids,f,g)
    ordered=anchor["ordered_original_ids"]
    core=ordered[3:]
    q=flags[ordered[2]][0]
    r=flags[ordered[1]][1]
    p=flags[ordered[0]][0]
    ell=flags[ordered[0]][1]
    graph=defaultdict(set)
    for i in core:
        u,line=flags[i];x,z=f[u];y,w=g[line]
        for a,b in (((x,y),(z,w)),((x,w),(z,y))):
            graph[a].add(b);graph[b].add(a)
    found=[]
    for a in graph:
        for b in graph[a]:
            for c in graph[b]:
                for d in graph[c]:
                    path=(a,b,c,d)
                    if len({u[0] for u in path})!=4 or len({u[1] for u in path})!=4:
                        continue
                    if (set((path[0][0],path[-1][0]))!=set(f[q]) or
                        set((path[0][1],path[-1][1]))!=set(g[r]) or
                        set(f[p])&{u[0] for u in path} or
                        set(g[ell])&{u[1] for u in path}):
                        continue
                    found.append(path)
    return len(found)


def exact_aligned_signed_certificate(power):
    """True original all-nine-source-templates and independent GF5 Fourier."""
    result=[]
    for typ in aligned_template_types():
        s,v,flags,ids,f,g=lift_template(power,typ)
        source=classify_original_six_alignment(flags,ids,f,g)
        if source["aligned"]!=typ["aligned"]:
            raise AssertionError("true original alignment disagrees with combinatorial center")
        # Name order of six source IDs in this construction is already canonical.
        if source["ordered_original_ids"]!=ids:
            raise AssertionError("canonical genuine original source IDs modified")
        if Counter(source["edges"])!=Counter(typ["edges"]):
            raise AssertionError("original-coordinate incidence differs from template")
        paths=count_actual_physical_owner_paths(flags,ids,f,g)
        if paths!=(2 if typ["aligned"] else 0):
            raise AssertionError("actual paired-diagonal ORIGINAL 0/2 path inverse failed")
        flowvec=tuple(gf5_fourier_potential_oracle(source["edges"],sign) for sign in SIGNS)
        total=sum(flowvec)
        if total!=(SIGNED_ALIGNED_BBO if typ["aligned"] else SIGNED_UNALIGNED_BBO):
            raise AssertionError("the proposed aligned signed mass theorem is false")
        result.append({"s":s,"source_six_original_ids":ids,
                       "aligned":typ["aligned"],"middle_owner":typ["left_middle_owner"],
                       "original_produced_directed_paths":paths,"ten_signs":flowvec,
                       "exact_signed_mass":total})
    if (Counter((r["aligned"],r["exact_signed_mass"]) for r in result)
        !=Counter({(True,53838):3,(False,53526):6})):
        raise AssertionError("3 aligned and 6 unaligned ORIGINAL sixsets required")
    return tuple(result)


def sharpened_original_r3_floor(D6, produced_aligned, other_bbo=0):
    """Lower bound on SUM of signed 3+3 event expectations, NOT union probability."""
    if any(type(x) is not int or x<0 for x in (D6,produced_aligned,other_bbo)):
        raise ValueError("nonnegative original sixset counts required")
    floor=SIGNED_D6*D6+SIGNED_ALIGNED_BBO*produced_aligned+SIGNED_UNALIGNED_BBO*other_bbo
    return Fraction(floor, PALETTE_SIX)


if __name__=="__main__":
    import json
    print(json.dumps([{"power":power,
                       "templates":[{"aligned":r["aligned"],
                                     "signed_mass":r["exact_signed_mass"],
                                     "paths":r["original_produced_directed_paths"]}
                                    for r in exact_aligned_signed_certificate(power)]}
                      for power in (1,2)],indent=2))
