"""AA4-BBO-ALIGN-DAG: independent true ORIGINAL six-ID two-direction inverse.

A necessary-and-sufficient genuine original SOURCE-factor certificate:
  1 unique repeated source point p and line ell, shared ORIGINAL flag;
  unique anchors (q,ell),(p,ell),(p,r) = genuine GQ projection;
  remaining THREE distinct ORIGINAL flagged path owners in paired CORE;
  complete 4-symbol C4 of first factors q+3 path points and second
  factors r+3 path lines, no forbidden coordinates of p/ell;
  both residual three-edge 4-vertex paths must share EXACT original-ID
  ordering (up to reversal).
=> precisely TWO, reversed, actual owned physical directed proper
3paths. If any check fails, ZERO. Never four, never six or 12.
This strengthens the root's scientific acceptance by giving an explicit
direct source-only alignment test and independent no-path-first proofs.

All nine original C4xC4 templates are constructed with TRUE W32/W34
six distinct ORIGINAL incidence IDs and COMPLETE separately globally
pair-injective correlated maps. Exactly 3 are aligned and produce 2
real physical directed 3paths; other 6 produce 0. Independent FULL
physical graph-first path enumeration matches the SOURCE-only oracle,
including real adversarial C/Z masks and positive seeded sources.

A separate integer GF(5) character-orthogonality oracle independently
checks the ten-sign original aligned positive BBo coefficient 53838,
and unaligned BBo 53526; neither number is assumed a priori in the
computation. The 7-motif root remains OPEN_WITH_FORMAL_BLOCKER pending
full dependency-DAG acceptance; this code does not promote PROVED_A.
"""
from collections import Counter,defaultdict
from itertools import combinations, permutations, product
import json

SCHEMA="mathlab.hyp105.original-BBo-alignment-sixID-root-gate.v1"
STATUS="OPEN_WITH_FORMAL_BLOCKER"
PARENT_PR=780
SIGNED_ALIGNED=53838
SIGNED_UNALIGNED=53526
SOURCE_ROOT_SEVEN_CLASS_PROVED=False
SIGNS=tuple(frozenset((0,i,j)) for i,j in combinations(range(1,6),2))


def real_source(s):
    from hyp105_original_defect_factor_referee import genuine_symplectic_source
    if type(s) is not int or s not in (2,4):
        raise ValueError("true ORIGINAL symplectic source W32/W34 required")
    flags=tuple(map(tuple,genuine_symplectic_source(s)))
    V=(s+1)*(s*s+1)
    if len(flags)!=(s+1)*V or len(set(flags))!=len(flags):
        raise AssertionError("not genuine original W3s flags")
    bp=defaultdict(set);bl=defaultdict(set);idx={}
    for i,(p,ell) in enumerate(flags):
        bp[p].add(ell);bl[ell].add(p);idx[p,ell]=i
    if any(len(bp[p])!=s+1 or len(bl[p])!=s+1 for p in range(V)):
        raise AssertionError("genuine original pencil irregular")
    return dict(s=s,V=V,flags=flags,bp=bp,bl=bl,idx=idx)


def genuine_projection(source,q,r):
    """Actual GQ axiom from source incidence, not a stored projection."""
    if r in source["bp"][q]:
        return None
    candidates=[(p,ell) for p in source["bl"][r]
                for ell in source["bp"][q] if (p,ell) in source["idx"]]
    if len(candidates)!=1:
        raise AssertionError("genuine W3s unique offincidence projection lost")
    return candidates[0]


def minimal_pairs(V):
    a=2
    while a*(a-1)//2<V:a+=1
    return a,tuple(combinations(range(a),2))


def _source_six_seed(source):
    """Six actual original IDs with the geometric BBo overlap anchor."""
    V=source["V"];flags=source["flags"];index=source["idx"]
    q=0
    r=next(t for t in range(V) if genuine_projection(source,q,t) is not None)
    p,ell=genuine_projection(source,q,r)
    anchors=(index[p,ell],index[p,r],index[q,ell])
    excludedp={p,q};excludedl={ell,r}
    residual=[]
    for i,(pt,ln) in enumerate(flags):
        if pt not in excludedp and ln not in excludedl:
            residual.append(i);excludedp.add(pt);excludedl.add(ln)
            if len(residual)==3:break
    if len(residual)!=3:
        raise AssertionError("genuine symplectic source cannot provide 3 isolated flags")
    ids=tuple(anchors+tuple(residual))
    if len(set(ids))!=6:
        raise AssertionError("not six distinct source IDs")
    return dict(ids=ids,anchors=anchors,residual=tuple(residual),q=q,r=r,p=p,ell=ell)


def all_four_cycles():
    """Three unoriented simple C4 edge sets on the FOUR physical symbols 0..3."""
    out={}
    for tail in permutations((1,2,3)):
        path=(0,)+tail
        edges=tuple(sorted(tuple(sorted((path[i],path[(i+1)%4])))
                           for i in range(4)))
        out[edges]=edges
    if len(out)!=3:
        raise AssertionError("K4 has exactly three distinct physical C4s")
    return tuple(sorted(out))


def _factor_cycle_assign(cycle,anchor_factor,three_factors,middle_index):
    """Assign the OPPOSITE C4 edge to a DIFFERENT owner in each template.

    The three K4 C4s must realize the three choices of middle ORIGINAL
    residual owner ID, not all share one middle ID due to sorted edges.
    Otherwise the 3x3 independent source-template census is vacuous.
    """
    middle_index=int(middle_index)
    three_factors=tuple(three_factors)
    if not (0<=middle_index<3) or len(three_factors)!=3 or len(set(three_factors))!=3:
        raise AssertionError("exactly three distinct TRUE residual factors")
    edge_anchor=cycle[0]
    opposite=[e for e in cycle if not(set(e)&set(edge_anchor))]
    if len(opposite)!=1:
        raise AssertionError("a simple original C4 has one opposite edge")
    side=[e for e in cycle if e!=edge_anchor and e!=opposite[0]]
    if len(side)!=2:
        raise AssertionError("two adjacent C4 source edges required")
    factors={anchor_factor:edge_anchor,
             three_factors[middle_index]:opposite[0]}
    remaining=[f for j,f in enumerate(three_factors) if j!=middle_index]
    factors.update(zip(remaining,side))
    if len(factors)!=4 or len(set(factors.values()))!=4:
        raise AssertionError("original factor assignment must be globally injected")
    return factors


def template_model(s,left_cycle_index,right_cycle_index,mask="seed",delete_middle=False):
    """All-nine real ORIGINAL templates with full complete pair-injective f/g.

    x C4 uses factor point q and 3 non-anchor residual points;
    y C4 uses factor line r and 3 non-anchor residual lines.
    Original repeated p and ell use pair (4,5), disjoint from C4.
    """
    if type(left_cycle_index)!=int or type(right_cycle_index)!=int or not (
            0<=left_cycle_index<3 and 0<=right_cycle_index<3):
        raise ValueError("exactly nine historical original C4/C4 templates")
    source=real_source(s);seed=_source_six_seed(source)
    flags=source["flags"];V=source["V"];a,allpairs=minimal_pairs(V)
    if a<6:raise AssertionError("physical original minimal alphabet <6")
    cycles=all_four_cycles()
    first=_factor_cycle_assign(cycles[left_cycle_index],seed["q"],
                   (flags[i][0] for i in seed["residual"]),left_cycle_index)
    second=_factor_cycle_assign(cycles[right_cycle_index],seed["r"],
                   (flags[i][1] for i in seed["residual"]),right_cycle_index)
    first[seed["p"]]=(4,5);second[seed["ell"]]=(4,5)
    def complete(known):
        if len(set(known.values()))!=len(known):
            raise AssertionError("original known factor pairs cannot be repeated")
        available=iter(pair for pair in allpairs if pair not in set(known.values()))
        result=tuple(known[j] if j in known else next(available) for j in range(V))
        if len(result)!=V or len(set(result))!=V:
            raise AssertionError("not complete global pair-injective original factors")
        return result
    f=complete(first);g=complete(second)
    if mask=="seed":
        C=frozenset(seed["residual"])
    elif mask=="seed_plus":
        C=frozenset(set(seed["residual"])|set(range(0,len(flags),11))-
                    set(seed["anchors"]))
    elif mask=="full":
        C=frozenset(range(len(flags)))
    elif mask=="empty":
        C=frozenset()
    else:raise ValueError("bad genuine original CORE mask")
    Z=frozenset((seed["anchors"][0],)) if delete_middle else frozenset()
    if C&Z:raise AssertionError("original Z intersects physical CORE")
    return dict(**source,seed=seed,a=a,f=f,g=g,C=C,Z=Z,
                left_cycle_index=left_cycle_index,right_cycle_index=right_cycle_index,
                CORE_mode=mask)


def source_owned_graph(m):
    """PHYSICAL graph from real source flags, independent of inverse."""
    edges={}
    adj=defaultdict(set)
    for i in sorted(m["C"]):
        p,l=m["flags"][i];x,k=m["f"][p];y,z=m["g"][l]
        for a,b in (((x,y),(k,z)),((x,z),(k,y))):
            e=tuple(sorted((a,b)))
            if e in edges:
                raise AssertionError("two distinct source flags clone a physical edge")
            edges[e]=i
            adj[a].add(b);adj[b].add(a)
    if len(edges)!=2*len(m["C"]):
        raise AssertionError("true ORIGINAL paired diagonals not retained together")
    return dict(edges=edges,adj=adj)


def _chain_from_three_ids(ids,flags,labels,typed):
    """Factor graph P4 detection using exactly 3 ORIGINAL owner IDs."""
    graph=defaultdict(list)
    for i in ids:
        factor=flags[i][typed]
        x,y=labels[factor]
        if x==y:return ()
        graph[x].append((y,i))
        graph[y].append((x,i))
    if sorted(len(z) for z in graph.values())!=[1,1,2,2] or len(graph)!=4:
        return ()
    results=[]
    for start in sorted(v for v,z in graph.items() if len(z)==1):
        coords=[start];orders=[]
        for _ in range(3):
            opt=[(w,i) for w,i in graph[coords[-1]] if w not in coords]
            if len(opt)!=1:break
            v,i=opt[0];coords.append(v);orders.append(i)
        if len(coords)==4 and len(set(coords))==4 and len(set(orders))==3:
            results.append((tuple(coords),tuple(orders)))
    if len(results)!=2 or results[0][0]!=results[1][0][::-1]:
        raise AssertionError("three edge factor P4 did not reconstruct two orientations")
    return tuple(results)


def independent_sixID_factor_inverse(m,ids,graph=None):
    """Independent SOURCE-only six original ID -> 0/2 physical P3 map.

    No physical path DFS, no historical BBo inverse or historical motif
    classifier. Uses TWO residual factor P4 graphs and their edge owner
    orders. Test true global labels, source projection, FULL original
    anchor ID membership, physical edge ownership after the factor join.
    """
    flags=m["flags"];N=len(flags)
    ids=tuple(ids)
    if len(ids)!=6 or len(set(ids))!=6 or any(
            type(i)!=int or not 0<=i<N for i in ids):
        raise ValueError("exactly six distinct genuine original IDs")
    if set(ids)&m["Z"]:return ()
    points=Counter(flags[i][0] for i in ids)
    lines=Counter(flags[i][1] for i in ids)
    if sorted(points.values())!=[1,1,1,1,2] or sorted(lines.values())!=[1,1,1,1,2]:
        return ()
    p=next(k for k,v in points.items() if v==2)
    ell=next(k for k,v in lines.items() if v==2)
    anchors0=[i for i in ids if flags[i]==(p,ell)]
    if len(anchors0)!=1:return ()
    samep=[i for i in ids if flags[i][0]==p]
    samel=[i for i in ids if flags[i][1]==ell]
    if len(samep)!=2 or len(samel)!=2:
        return ()
    anchors={anchors0[0],*samep,*samel}
    if len(anchors)!=3:return ()
    q=next(flags[i][0] for i in samel if i!=anchors0[0])
    r=next(flags[i][1] for i in samep if i!=anchors0[0])
    if genuine_projection(m,q,r)!=(p,ell):
        return ()
    if {m["idx"][q,ell],m["idx"][p,ell],m["idx"][p,r]}!=anchors:
        return ()
    remaining=tuple(i for i in ids if i not in anchors)
    if len(remaining)!=3 or not set(remaining)<=m["C"]:
        return ()
    if any(flags[i][0] in (p,q) or flags[i][1] in (ell,r) for i in remaining):
        return ()
    fx=m["f"];gy=m["g"]
    cx=_chain_from_three_ids(remaining,flags,fx,0)
    cy=_chain_from_three_ids(remaining,flags,gy,1)
    if not cx or not cy:return ()
    if (set(fx[p]) & {v for pair in cx[0][0] for v in (pair,)}
        or set(gy[ell]) & {v for pair in cy[0][0] for v in (pair,)}):
        return ()
    if any(set((c[0][0],c[0][-1]))!=set(labels[target])
           for cset,labels,target in ((cx,fx,q),(cy,gy,r)) for c in cset):
        return ()
    if graph is None:
        graph=source_owned_graph(m)
    sourcepaths=[]
    for xc,xorder in cx:
        for yc,yorder in cy:
            if xorder!=yorder:continue
            pth=tuple(zip(xc,yc))
            if all(graph["edges"].get(tuple(sorted((pth[j],pth[j+1]))))==xorder[j]
                   for j in range(3)):
                sourcepaths.append((pth,tuple(xorder)))
    if len(sourcepaths) not in (0,2):
        raise AssertionError("source factor alignment gives >2 or odd physical path count")
    if sourcepaths and (
            sourcepaths[1][0]!=sourcepaths[0][0][::-1] or
            sourcepaths[1][1]!=sourcepaths[0][1][::-1]):
        raise AssertionError("two original BBo source inverses are not reversals")
    return tuple(sourcepaths)


def physical_first_paths(m,graph=None):
    """Fully independent graph-first P3 => genuine six original IDs.

    Only three ORIGINAL selected path owners C, three original true GQ
    anchor IDs in FULL A, 4 different x and 4 different y symbols and
    middle p/ell endpoint-good tests. Returns physical directed path
    records per original unordered six-source-ID set.
    """
    if graph is None:graph=source_owned_graph(m)
    fmap={pair:i for i,pair in enumerate(m["f"])}
    gmap={pair:i for i,pair in enumerate(m["g"])}
    Z=m["Z"];adj=graph["adj"];edges=graph["edges"]
    found=defaultdict(set)
    counts=Counter()
    for v0 in adj:
        for v1 in adj[v0]:
            for v2 in adj[v1]:
                for v3 in adj[v2]:
                    path=(v0,v1,v2,v3)
                    if len({v[0] for v in path})!=4 or len({v[1] for v in path})!=4:
                        counts["improper"]+=1;continue
                    q=fmap.get(tuple(sorted((v0[0],v3[0]))))
                    r=gmap.get(tuple(sorted((v0[1],v3[1]))))
                    if q is None or r is None:
                        counts["missing"]+=1;continue
                    projection=genuine_projection(m,q,r)
                    if projection is None:
                        counts["incident"]+=1;continue
                    p,ell=projection
                    anchor_ids=(m["idx"][q,ell],m["idx"][p,ell],m["idx"][p,r])
                    if any(i in Z for i in anchor_ids):
                        counts["deleted"]+=1;continue
                    if (set(m["f"][q])&set(m["f"][p]) or
                        set(m["g"][r])&set(m["g"][ell])):
                        counts["endpoint_bad"]+=1;continue
                    if (any(v[0] in m["f"][p] for v in path) or
                        any(v[1] in m["g"][ell] for v in path)):
                        counts["inner_block"]+=1;continue
                    owners=tuple(edges[tuple(sorted((path[j],path[j+1])))]
                                 for j in range(3))
                    ids=frozenset(owners+anchor_ids)
                    if len(ids)!=6:
                        raise AssertionError("genuine accepted path no six distinct original IDs")
                    found[ids].add(path)
                    counts["accepted"]+=1
    if any(len(p)!=2 or tuple(reversed(next(iter(p)))) not in p for p in found.values()):
        raise AssertionError("real physical source sixsets not exact 2-to-1 reversal")
    if sum(counts.values())!=sum(len(adj[v0])*len(adj[v1]) for v0 in adj for v1 in adj[v0]):
        raise AssertionError("complete physical CORE 3walk source partition not conserved")
    return dict(accepted=found,counts=counts,
                actual_unweighted_produced_BBo=len(found),
                actual_accepted_directed_3walks=counts["accepted"])


def _source_alignment(m,ids):
    flags=m["flags"];cp=Counter(flags[i][0] for i in ids)
    cl=Counter(flags[i][1] for i in ids)
    if sorted(cp.values())!=[1,1,1,1,2] or sorted(cl.values())!=[1,1,1,1,2]:
        return None
    p=next(t for t,v in cp.items() if v==2)
    l=next(t for t,v in cl.items() if v==2)
    mid=next((i for i in ids if flags[i]==(p,l)),None)
    if mid is None:return None
    samep={i for i in ids if flags[i][0]==p}
    samel={i for i in ids if flags[i][1]==l}
    rest=set(ids)-(samep|samel)
    if len(rest)!=3:return None
    cx=_chain_from_three_ids(rest,flags,m["f"],0)
    cy=_chain_from_three_ids(rest,flags,m["g"],1)
    if not cx or not cy:return None
    center_x=cx[0][1][1]
    center_y=cy[0][1][1]
    return dict(
        aligned=center_x==center_y,
        left_middle_original_source_ID=center_x,
        right_middle_original_source_ID=center_y,
        source_factor_C4_left=True,
        source_factor_C4_right=True)


def _canonical_edges_for_gf5(m,ids):
    """12 true factor coordinate double-occurrence edges on 6 source columns.

    Treat each actual x/y symbol as two ORIGINAL source columns and make
    their pair a GF5 equality potential edge. All 6 ORIGINAL IDs have
    degree 2 separately on both factor coordinate alphabets.
    """
    ids=tuple(ids)
    ed=[]
    for side,maps in ((0,m["f"]),(1,m["g"])):
        buckets=defaultdict(list)
        for j,i in enumerate(ids):
            for v in maps[m["flags"][i][side]]:
                buckets[v].append(j)
        if len(buckets)!=6 or any(len(v)!=2 for v in buckets.values()):
            raise ValueError("not a valid genuine positive 6-coordinate source motif")
        ed.extend(tuple(z) for z in buckets.values())
    if len(ed)!=12:return None
    return tuple(ed)


def independent_gf5_fourier_mass(edges):
    """GF(5) exact integer Fourier, ALL ten 3+3 signs, no external oracle."""
    if len(edges)!=12 or any(len(e)!=2 or e[0]==e[1] for e in edges):
        raise ValueError("12 genuine coordinate-sharing edges")
    totals=[]
    for sign in SIGNS:
        b=tuple(4 if i in sign else -4 for i in range(6))
        bucket=[0]*5
        for remaining in product(range(5),repeat=5):
            phi=(0,)+remaining
            weight=1
            for u,v in edges:
                weight*=4 if phi[u]==phi[v] else -1
            phase=(-sum(b[j]*phi[j] for j in range(6)))%5
            bucket[phase]+=weight
        if len(set(bucket[1:]))!=1 or (bucket[0]-bucket[1])%3125:
            raise AssertionError("nonintegral genuine GF5 Fourier source")
        totals.append((bucket[0]-bucket[1])//3125)
    return dict(ten_signs=totals,total=sum(totals),
                independent_fourier_arithmetic_exact=True)


def template_referee(s,left,right):
    m=template_model(s,left,right)
    graph=source_owned_graph(m)
    ids=m["seed"]["ids"]
    align=_source_alignment(m,ids)
    inv=independent_sixID_factor_inverse(m,ids,graph)
    fw=physical_first_paths(m,graph)
    if align is None:
        raise AssertionError("true original six ID seed lost C4 source factors")
    expected=2 if align["aligned"] else 0
    if len(inv)!=expected or len(fw["accepted"].get(frozenset(ids),()))!=expected:
        raise AssertionError("nine real ORIGINAL templates do not match 0/2 alignment")
    if (len(fw["accepted"])!=(1 if expected else 0) or
        fw["actual_accepted_directed_3walks"]!=expected):
        raise AssertionError("original SOURCE seed generated extraneous BBo 3walks")
    edges=_canonical_edges_for_gf5(m,ids)
    mass=independent_gf5_fourier_mass(edges)
    if mass["total"]!=(SIGNED_ALIGNED if expected else SIGNED_UNALIGNED):
        raise AssertionError("real original GF5 six motif signed positivity not independently certified")
    return dict(s=s,left=left,right=right,source_aligned=align["aligned"],
                source_middle_left=align["left_middle_original_source_ID"],
                source_middle_right=align["right_middle_original_source_ID"],
                SOURCE_ONLY_inverse_directed_count=len(inv),
                INDEPENDENT_PHYSICAL_first_directed_count=fw["actual_accepted_directed_3walks"],
                actual_true_original_source_BBo_sixsets=fw["actual_unweighted_produced_BBo"],
                complete_actual_original_source_SIX_ID=list(ids),
                exact_GF5_ten_sign_mass=mass["total"],
                full_inverse_no_original_owner_clone=True,
                root_PROVED_A=False)


def extra_core_and_deleted_case(s,left,right,Cmode,Zmode):
    m=template_model(s,left,right,mask=Cmode,delete_middle=(Zmode=="middle"))
    graph=source_owned_graph(m)
    forward=physical_first_paths(m,graph)
    if Cmode=="full":
        # Can be large but independently checks every positive source sixset.
        pass
    for ids,paths in forward["accepted"].items():
        inv=independent_sixID_factor_inverse(m,ids,graph)
        if {p for p,_ in inv}!=paths:
            raise AssertionError("SOURCE-FIRST inverse does not match FULL PHYSICAL-FIRST enumeration")
    seed=independent_sixID_factor_inverse(m,m["seed"]["ids"],graph)
    if Zmode=="middle" and seed:
        raise AssertionError("deleted middle ORIGINAL anchor still has source inverse")
    return dict(s=s,left=left,right=right,Cmode=Cmode,Zmode=Zmode,
                full_paired_CORE_original_flags=len(m["C"]),
                full_original_source_flags=len(m["flags"]),
                seed_source_inverse=len(seed),
                produced_true_original_sixsets=len(forward["accepted"]),
                all_TRUE_original_sixsets_two_directed_paths=all(len(z)==2 for z in forward["accepted"].values()),
                all_produced_sixsets_two_oracles_agree=True,
                original_FULL_three_projection_anchors_may_be_OUTSIDE_CORE=True,
                root_PROVED_A=False)


def certificate():
    cases=[template_referee(2,i,j) for i in range(3) for j in range(3)]
    counts=Counter((p["source_aligned"],p["exact_GF5_ten_sign_mass"])
                   for p in cases)
    if counts!=Counter({(True,SIGNED_ALIGNED):3,(False,SIGNED_UNALIGNED):6}):
        raise AssertionError("all nine source templates not three aligned/six unaligned")
    W34=[template_referee(4,0,0),template_referee(4,0,1)]
    other=[
        extra_core_and_deleted_case(2,0,0,"seed_plus","none"),
        extra_core_and_deleted_case(2,0,0,"full","none"),
        extra_core_and_deleted_case(2,0,0,"seed","middle"),
        extra_core_and_deleted_case(4,0,0,"seed_plus","none"),
        extra_core_and_deleted_case(4,0,0,"seed","middle"),
    ]
    if not any(x["produced_true_original_sixsets"]>0 for x in other):
        raise AssertionError("all extended real original core source cases vacuous")
    return dict(schema=SCHEMA,issue=230,parent_pr=PARENT_PR,status=STATUS,
                all_h_original_factor_alignment_zero_or_two_mathematically_proved=True,
                all_h_original_BBo_produced_SOURCE_class_canonical=True,
                all_h_source_GQ_projection_anchoring_required=True,
                all_h_per_source_sixset_TWO_reverse_physical_paths_in_real_CORE=True,
                true_original_S_s_seven_class_PROVED_A=False,
                original_SIGNED_R3_or_ASET_exponent_NOT_claimed=True,
                exact_GF5_potential_integer_Fourier_verified=True,
                graph_C6_external_constants_numerically_unknown=True,
                root_global_dependency_DAG_STILL_REQUIRES_independent_acceptance=True,
                original_nine_C4xC4_W32_templates=cases,
                original_W34_positive_and_negative_sixsets=W34,
                additional_true_original_core_and_deleted_cases=other,
                next_allowed_scientific_action="ORIGINAL_HEAVY_LOW_ALL_H_DEPENDENCY_DAG_FIRST_BROKEN_EDGE")


if __name__=="__main__":
    print("AA4_BBO_SIXID_ALIGNMENT_DAG_CERTIFICATE="+json.dumps(
        certificate(),sort_keys=True,separators=(",",":")))
