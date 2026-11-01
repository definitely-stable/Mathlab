"""R5: source-first squarefree cubic certificate for all FOUR true ORIGINAL blockers.

Unlike historical physical-walk/mixed-book referees this module builds its
first count from oriented ORIGINAL flag edge IDs, not an adjacency walk.
A second, independent method builds the physical CORE adjacency from scratch.
Both use genuine W(3,2)/W(3,4) source geometry only. The cubic identity itself
is proven for all dyadic orders, independently of finite experiments.

No result about external C6 supersaturation or new ASET powers is implied.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb, isqrt

from hyp105_full_physical_degree_tail import genuine_source


def minimal_alphabet(v):
    if type(v) is not int or v < 15:
        raise ValueError("true generalized-quadrangle vertex population required")
    a=(1+isqrt(1+8*v))//2
    while a*(a-1)//2 < v:
        a+=1
    while a>2 and (a-1)*(a-2)//2>=v:
        a-=1
    return a


def _source(power, f, g, ids):
    if type(power) is not int or power not in (1,2):
        raise ValueError("finite referee is restricted to genuine W32/W34")
    s,v,flags=genuine_source(power)
    a=minimal_alphabet(v)
    legal=set(combinations(range(a),2))
    try:
        f=tuple(tuple(p) for p in f)
        g=tuple(tuple(p) for p in g)
    except (TypeError, ValueError) as ex:
        raise ValueError("missing true source pair labels") from ex
    if len(f)!=v or len(g)!=v or any(pair not in legal for pair in f+g):
        raise ValueError("illegal or incomplete original pair-label alphabet")
    if len(set(f))!=v or len(set(g))!=v:
        raise ValueError("source f/g must be complete global injections")
    ids=tuple(range(len(flags))) if ids is None else tuple(ids)
    if (any(type(i) is not int or not 0<=i<len(flags) for i in ids)
        or len(ids)!=len(set(ids))):
        raise ValueError("CORE/universe must contain unique real ORIGINAL IDs")
    return s,v,flags,f,g,ids


def _oriented_source_edges(flags, f, g, ids):
    """Four oriented physical edges per ORIGINAL ID, never clone owners."""
    edges=[]
    owner={}
    for i in ids:
        p,ell=flags[i]
        x,z=f[p];y,w=g[ell]
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            e=frozenset((u,v))
            if e in owner:
                raise AssertionError("two distinct true ORIGINAL owners")
            owner[e]=i
            edges.append((u,v,i))
            edges.append((v,u,i))
    if len(owner)!=2*len(ids):
        raise AssertionError("original paired-diagonal cardinality")
    return edges,owner


def _full_projection_A(flags, v):
    """Source-first projection: nonincident (q,r) via points on r."""
    pencil=[set() for _ in range(v)]
    through=[set() for _ in range(v)]
    idx={}
    for i,(p,ell) in enumerate(flags):
        pencil[p].add(ell)
        through[ell].add(p)
        idx[p,ell]=i
    result={}
    for q in range(v):
        for r in range(v):
            if r in pencil[q]:
                continue
            candidates=[(p,ell) for p in through[r]
                        for ell in pencil[p]&pencil[q]]
            if len(candidates)!=1:
                raise AssertionError("full ORIGINAL GQ projection uniqueness")
            p,ell=candidates[0]
            result[q,r]=(p,ell,(idx[q,ell],idx[p,ell],idx[p,r]))
    return result


def _full_projection_B(flags, v):
    """Independent physical-first source closure: follow q's line pencil."""
    pencil=[set() for _ in range(v)]
    through=[set() for _ in range(v)]
    idx={}
    for i,(p,ell) in enumerate(flags):
        pencil[p].add(ell)
        through[ell].add(p)
        idx[p,ell]=i
    result={}
    for q in range(v):
        for r in range(v):
            if r in pencil[q]:
                continue
            candidates=[(p,ell) for ell in pencil[q]
                        for p in through[ell]&through[r]]
            if len(candidates)!=1:
                raise AssertionError("different FULL source closure oracle disagrees")
            p,ell=candidates[0]
            result[q,r]=(p,ell,(idx[q,ell],idx[p,ell],idx[p,r]))
    return result


def _classify(path, f, g, projection, invf, invg):
    """Exactly the original four internal positions in directed P4."""
    if (len({u[0] for u in path})!=4
        or len({u[1] for u in path})!=4):
        return None
    q=invf.get(tuple(sorted((path[0][0],path[3][0]))))
    r=invg.get(tuple(sorted((path[0][1],path[3][1]))))
    if q is None or r is None or (q,r) not in projection:
        return None
    p,ell,anchors=projection[q,r]
    endgood=(set(f[p]).isdisjoint((path[0][0],path[3][0]))
             and set(g[ell]).isdisjoint((path[0][1],path[3][1])))
    mask=sum(1<<k for k,b in enumerate((
        path[1][0] in f[p], path[2][0] in f[p],
        path[1][1] in g[ell], path[2][1] in g[ell]
    )) if b)
    return endgood,mask,anchors


def original_flag_triple_cubic(power,f,g,universe=None):
    """Build coefficients c_{T,endgood,mask} on ORIGINAL oriented flag triples.

    This does NOT invoke the physical adjacency; the allowed joint is the
    equality of consecutive independently sourced oriented edge endpoints.
    """
    _,v,flags,f,g,ids=_source(power,f,g,universe)
    projection=_full_projection_A(flags,v)
    invf={pair:i for i,pair in enumerate(f)}
    invg={pair:i for i,pair in enumerate(g)}
    oriented,owners=_oriented_source_edges(flags,f,g,ids)
    by_start=defaultdict(list)
    for u,w,i in oriented:
        by_start[u].append((w,i))
    coefficients=Counter()
    witnesses={}
    proper=0
    for a,b,i in oriented:
        for c,j in by_start.get(b,()):
            for d,k in by_start.get(c,()):
                path=(a,b,c,d)
                classified=_classify(path,f,g,projection,invf,invg)
                if classified is None:
                    continue
                endgood,mask,anchors=classified
                if len({i,j,k})!=3:
                    raise AssertionError("a coordinate-proper 3-walk reused an original flag")
                support=tuple(sorted((i,j,k)))
                key=(support,endgood,mask)
                coefficients[key]+=1
                witnesses.setdefault(key,(path,(i,j,k),anchors))
                proper+=1
    return {
        "universe":ids,
        "coefficients":coefficients,
        "witnesses":witnesses,
        "original_sourced_proper_projected_walks":proper,
        "full_incidence_count":len(flags),
        "paired_edges_in_universe":len(owners),
    }


def evaluate_original_cubic(polynomial, core_ids):
    """Exact x_i in {0,1} restriction, with no need for anchor IDs in CORE."""
    core=set(core_ids)
    if any(type(i) is not int for i in core):
        raise ValueError("illegal original ID in retention vector")
    if not core.issubset(set(polynomial["universe"])):
        raise ValueError("retained CORE outside polynomial original-ID universe")
    out=Counter()
    for (support,endgood,mask),multiplicity in polynomial["coefficients"].items():
        if set(support).issubset(core):
            out[endgood,mask]+=multiplicity
    return out


def independent_physical_core_histogram(power,f,g,core_ids):
    """Direct PHYSICAL adjacency walk census and DIFFERENT full source closure."""
    _,v,flags,f,g,ids=_source(power,f,g,core_ids)
    projection=_full_projection_B(flags,v)
    invf={pair:i for i,pair in enumerate(f)}
    invg={pair:i for i,pair in enumerate(g)}
    graph=defaultdict(set)
    owners={}
    for i in ids:
        p,ell=flags[i]
        x,z=f[p];y,w=g[ell]
        for a,b in (((x,y),(z,w)),((x,w),(z,y))):
            key=frozenset((a,b))
            if key in owners:
                raise AssertionError("duplicate physical edge owner")
            owners[key]=i
            graph[a].add(b);graph[b].add(a)
    counts=Counter()
    blocked_by_position=Counter()
    unique_anchors_outside=Counter()
    for a,neighbors in graph.items():
        for b in neighbors:
            for c in graph[b]:
                for d in graph[c]:
                    path=(a,b,c,d)
                    # Deliberately independent physical-first classification:
                    # no call to the ORIGINAL oriented-flag oracle _classify.
                    xs=(a[0],b[0],c[0],d[0])
                    ys=(a[1],b[1],c[1],d[1])
                    if len(set(xs))!=4 or len(set(ys))!=4:
                        continue
                    q=invf.get(tuple(sorted((xs[0],xs[3]))))
                    rr=invg.get(tuple(sorted((ys[0],ys[3]))))
                    if q is None or rr is None:
                        continue
                    closure=projection.get((q,rr))
                    if closure is None:
                        continue
                    p,ell,anchors=closure
                    endgood=(xs[0] not in f[p] and xs[3] not in f[p]
                             and ys[0] not in g[ell] and ys[3] not in g[ell])
                    mask=(int(xs[1] in f[p]) + 2*int(xs[2] in f[p])
                          + 4*int(ys[1] in g[ell])
                          + 8*int(ys[2] in g[ell]))
                    counts[endgood,mask]+=1
                    for j in range(4):
                        if mask & (1<<j):
                            blocked_by_position[endgood,j]+=1
                    if any(anchor not in ids for anchor in anchors):
                        unique_anchors_outside[endgood,mask]+=1
    return {
        "histogram":counts,
        "position_counts":blocked_by_position,
        "outside_core_anchors":unique_anchors_outside,
        "core_flags":len(ids),
        "paired_physical_edges":len(owners),
        "physical_vertices_with_degree":len(graph),
    }


def audit_original_four_blocker_cubic(power,f,g,universe,core_ids):
    polynomial=original_flag_triple_cubic(power,f,g,universe)
    expected=evaluate_original_cubic(polynomial,core_ids)
    physical=independent_physical_core_histogram(power,f,g,core_ids)
    if expected!=physical["histogram"]:
        raise AssertionError(
            ("genuine original triple CUBIC vs independent physical walk",
             expected-physical["histogram"], physical["histogram"]-expected))
    if polynomial["paired_edges_in_universe"]!=2*len(polynomial["universe"]):
        raise AssertionError("source diagonals disappeared")
    for good in (False,True):
        for j in range(4):
            got=sum(n for (is_good,mask),n in expected.items()
                    if is_good==good and mask & (1<<j))
            if got != physical["position_counts"][good,j]:
                raise AssertionError("original four-position event mismatch")
        blocked=sum(n for (is_good,mask),n in expected.items()
                    if is_good==good and mask!=0)
        if blocked > sum(physical["position_counts"][good,j] for j in range(4)):
            raise AssertionError("four-position union bound false")
    return {
        "source_original_triple_coefficients":len(polynomial["coefficients"]),
        "source_original_all_walks":polynomial["original_sourced_proper_projected_walks"],
        "physical_original_core_flags":physical["core_flags"],
        "physical_paired_edges":physical["paired_physical_edges"],
        "full_source_anchor_absent_from_core":sum(physical["outside_core_anchors"].values()),
        "projected_endgood":sum(n for (good,_),n in expected.items() if good),
        "endgood_unblocked":expected[True,0],
        "endgood_blocked_union":sum(n for (good,m),n in expected.items() if good and m),
        "four_position_counts":tuple(physical["position_counts"][True,j] for j in range(4)),
        "full_source_projections_independently_recomputed":True,
        "exact_cubic_for_this_core":True,
    }
