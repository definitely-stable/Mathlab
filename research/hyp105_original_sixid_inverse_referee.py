"""AA4-SIXINV: independent ORIGINAL six-incidence-ID inverse/referee.

No import of historical GF5 classifier or old lowtail/heavy implementations.
The finite source constructor is reused; all physical inversions are new.
BBo: 0/2 oriented core paths, NOT surjective onto the complete BBo class.
D6: 0/1 unoriented simple physical C6 per six-ORIGINAL-ID source sixset.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb
from pathlib import Path
import json

ROOT_STATUS = "OPEN_WITH_FORMAL_BLOCKER"


def source_case(h, scheme, shift=0):
    from hyp105_full_physical_degree_tail import genuine_source
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    if type(h) is not int or h not in (1, 2) or type(shift) is not int:
        raise ValueError("only actual W32/W34 sources and integer line permutations")
    s, V, flags = genuine_source(h)
    m = pair_labeled_symplectic(h, scheme)
    f = tuple(map(tuple, m["left_labels"]))
    g = tuple(map(tuple, m["right_labels"]))
    if shift:
        g = g[shift % V:] + g[:shift % V]
    a = 2
    while comb(a, 2) < V:
        a += 1
    legal = set(combinations(range(a), 2))
    if (len(f) != V or len(g) != V or len(set(f)) != V
            or len(set(g)) != V or any(z not in legal for z in f+g)):
        raise ValueError("invalid ORIGINAL complete globally injected labels")
    return dict(s=s, V=V, a=a, flags=tuple(flags), f=f, g=g)


def geometry(c):
    v = c["V"]
    pl = [set() for _ in range(v)]
    lp = [set() for _ in range(v)]
    lookup = {}
    for i, (p, ell) in enumerate(c["flags"]):
        if not 0 <= p < v or not 0 <= ell < v or (p, ell) in lookup:
            raise ValueError("not a genuine unique ORIGINAL point-line incidence")
        pl[p].add(ell)
        lp[ell].add(p)
        lookup[p, ell] = i
    if any(len(z) != c["s"]+1 for z in pl+lp):
        raise ValueError("invalid genuine GQ pencil size")
    col = [set() for _ in range(v)]
    for p in range(v):
        for ell in pl[p]:
            col[p].update(lp[ell])
        col[p].discard(p)
    return dict(pl=pl, lp=lp, lookup=lookup, col=col)


def projection(geo, q, r):
    if r in geo["pl"][q]:
        return None
    mid = geo["col"][q] & geo["lp"][r]
    if len(mid) != 1:
        raise AssertionError("no unique original GQ point projection")
    p = next(iter(mid))
    lines = geo["pl"][p] & geo["pl"][q]
    if len(lines) != 1:
        raise AssertionError("no unique original GQ line projection")
    ell = next(iter(lines))
    return p, ell, (geo["lookup"][q,ell],
                    geo["lookup"][p,ell], geo["lookup"][p,r])


def owned_graph(c, ids):
    flags, f, g = c["flags"], c["f"], c["g"]
    ids = tuple(ids)
    if (len(set(ids)) != len(ids) or
            any(type(i) is not int or not 0 <= i < len(flags) for i in ids)):
        raise ValueError("invalid duplicate or absent ORIGINAL source ID")
    adj = defaultdict(set)
    owner = {}
    for i in ids:
        p, ell = flags[i]
        x, z = f[p]
        y, w = g[ell]
        for u, v in (((x,y),(z,w)),((x,w),(z,y))):
            edge = tuple(sorted((u,v)))
            if edge in owner:
                raise AssertionError("two ORIGINAL owners of one physical edge")
            owner[edge] = i
            adj[u].add(v); adj[v].add(u)
    if len(owner) != 2*len(ids):
        raise AssertionError("each ORIGINAL flag must own two diagonals")
    return adj, owner


def _c4(pairs):
    if len(pairs) != 4 or len(set(pairs)) != 4:
        return False
    g = defaultdict(set)
    for u,v in pairs:
        g[u].add(v);g[v].add(u)
    if len(g) != 4 or any(len(n) != 2 for n in g.values()):
        return False
    seen = {next(iter(g))}
    queue = list(seen)
    while queue:
        for w in g[queue.pop()]:
            if w not in seen:
                seen.add(w);queue.append(w)
    return len(seen) == 4


def bbo_structure(ids, c, geo, Z=()):
    flags, f, g = c["flags"], c["f"], c["g"]
    ids = tuple(ids)
    if (len(ids) != 6 or len(set(ids)) != 6 or
            any(type(i) is not int or not 0 <= i < len(flags) for i in ids)):
        raise ValueError("SIX distinct actual original incidence IDs required")
    if set(ids) & set(Z):
        return None
    cp = Counter(flags[i][0] for i in ids)
    cl = Counter(flags[i][1] for i in ids)
    pp = [p for p,k in cp.items() if k == 2]
    ll = [ell for ell,k in cl.items() if k == 2]
    if (len(cp) != 5 or len(cl) != 5 or len(pp) != 1 or len(ll) != 1
            or any(k not in (1,2) for k in list(cp.values())+list(cl.values()))):
        return None
    p,ell = pp[0],ll[0]
    middle = [i for i in ids if flags[i] == (p,ell)]
    q_edge = [i for i in ids if flags[i][1] == ell and flags[i][0] != p]
    r_edge = [i for i in ids if flags[i][0] == p and flags[i][1] != ell]
    if len(middle)!=1 or len(q_edge)!=1 or len(r_edge)!=1:
        return None
    q,r = flags[q_edge[0]][0], flags[r_edge[0]][1]
    anchors = (q_edge[0],middle[0],r_edge[0])
    iso = tuple(i for i in ids if i not in anchors)
    if len(iso)!=3 or any(flags[i][0] in (p,q) or flags[i][1] in (ell,r)
                          for i in iso):
        return None
    if projection(geo,q,r) != (p,ell,anchors):
        return None
    left = [f[q]]+[f[flags[i][0]] for i in iso]
    right = [g[r]]+[g[flags[i][1]] for i in iso]
    if not _c4(left) or not _c4(right):
        return None
    if set(f[p]) & {v for e in left for v in e}:
        return None
    if set(g[ell]) & {v for e in right for v in e}:
        return None
    return dict(p=p,ell=ell,q=q,r=r,anchors=anchors,iso=iso)


def inverse_bbo(ids,c,geo,C,Z=(),owner=None):
    d = bbo_structure(ids,c,geo,Z)
    if d is None or not set(d["iso"]) <= set(C):
        return ()
    flags,f,g = c["flags"],c["f"],c["g"]
    edges = defaultdict(list)
    for i in d["iso"]:
        u,v = f[flags[i][0]]
        edges[u].append((v,i));edges[v].append((u,i))
    out=[]
    for x0 in f[d["q"]]:
        xs=[x0];order=[];last=None
        for _ in range(3):
            options=[(u,i) for u,i in edges[xs[-1]] if i!=last]
            if len(options)!=1:
                break
            x,i=options[0]
            xs.append(x);order.append(i);last=i
        if (len(order)!=3 or set(order)!=set(d["iso"])
                or len(set(xs))!=4 or xs[-1] not in f[d["q"]]
                or xs[-1]==x0):
            continue
        y0=set(g[d["r"]]) & set(g[flags[order[0]][1]])
        if len(y0)!=1:
            continue
        ys=[next(iter(y0))];valid=True
        for i in order:
            pair=set(g[flags[i][1]])
            if ys[-1] not in pair:
                valid=False;break
            ys.append(next(iter(pair-{ys[-1]})))
        if not valid or len(set(ys))!=4 or set((ys[0],ys[3]))!=set(g[d["r"]]):
            continue
        if set(xs)&set(f[d["p"]]) or set(ys)&set(g[d["ell"]]):
            continue
        vs=tuple(zip(xs,ys))
        for j,i in enumerate(order):
            u,v=vs[j],vs[j+1]
            if (set((u[0],v[0]))!=set(f[flags[i][0]]) or
                    set((u[1],v[1]))!=set(g[flags[i][1]]) or
                    (owner is not None and owner.get(tuple(sorted((u,v))))!=i)):
                valid=False;break
        if valid:
            out.append(vs)
    if out and (len(out)!=2 or out[0]!=out[1][::-1]):
        raise AssertionError("ORIGINAL BBo inverse multiplicity not exactly reversal pair")
    return tuple(out)


def canonical_cycle(v):
    v=tuple(v)
    if len(v)!=6 or len(set(v))!=6:
        raise ValueError("not a simple six-vertex physical cycle")
    return min(tuple(q[k:]+q[:k] for q in (v,v[::-1]) for k in range(6)))


def inverse_d6(ids,c,Z=(),owner=None):
    flags,f,g=c["flags"],c["f"],c["g"]
    ids=tuple(ids)
    if (len(ids)!=6 or len(set(ids))!=6 or
            any(type(i) is not int or not 0<=i<len(flags) for i in ids)):
        raise ValueError("SIX distinct actual original incidence IDs required")
    if set(ids)&set(Z):
        return ()
    if (len({flags[i][0] for i in ids})!=6 or
            len({flags[i][1] for i in ids})!=6):
        return ()
    xadj=defaultdict(list)
    for i in ids:
        u,v=f[flags[i][0]]
        xadj[u].append(i);xadj[v].append(i)
    if len(xadj)!=6 or any(len(z)!=2 for z in xadj.values()):
        return ()
    start=min(xadj);accepted=set()
    for first_id in xadj[start]:
        xs=[start];order=[];current=start;previous=None
        for j in range(6):
            options=[i for i in xadj[current] if i!=previous]
            if j==0:
                i=first_id
            elif len(options)==1:
                i=options[0]
            else:
                break
            if i not in options:
                break
            pair=f[flags[i][0]]
            if current not in pair:
                break
            nxt=pair[0] if pair[1]==current else pair[1]
            order.append(i);previous=i;current=nxt
            if j<5:
                xs.append(nxt)
        if (len(order)!=6 or set(order)!=set(ids) or
                len(set(xs))!=6 or current!=start):
            continue
        ys=[];valid=True
        for j in range(6):
            pre=set(g[flags[order[j-1]][1]])
            now=set(g[flags[order[j]][1]])
            same=pre&now
            if len(same)!=1:
                valid=False;break
            ys.append(next(iter(same)))
        if not valid or len(set(ys))!=6:
            continue
        vs=tuple(zip(xs,ys))
        for j,i in enumerate(order):
            u,v=vs[j],vs[(j+1)%6]
            if (set((u[0],v[0]))!=set(f[flags[i][0]]) or
                    set((u[1],v[1]))!=set(g[flags[i][1]]) or
                    (owner is not None and owner.get(tuple(sorted((u,v))))!=i)):
                valid=False;break
        if valid:
            accepted.add(canonical_cycle(vs))
    if len(accepted)>1:
        raise AssertionError("one original D6 sixset has multiple physical C6")
    return tuple(sorted(accepted))


def independent_cycles(adj,limit=40000):
    cycles=set()
    for start in sorted(adj):
        def dfs(path):
            if len(path)==6:
                if start in adj.get(path[-1],()):
                    cycles.add(canonical_cycle(path))
                    if len(cycles)>limit:
                        raise AssertionError("too many physical C6 for finite referee")
                return
            for v in adj.get(path[-1],()):
                if v>start and v not in path:
                    dfs(path+(v,))
        dfs((start,))
    return cycles


def physical_first_bbo(c,geo,C,Z):
    flags,f,g=c["flags"],c["f"],c["g"]
    C=tuple(C);Z=set(Z)
    if set(C)&Z:
        raise ValueError("original deleted source ID in physical core")
    adj,owner=owned_graph(c,C)
    ifa={pair:p for p,pair in enumerate(f)}
    iga={pair:ell for ell,pair in enumerate(g)}
    images=defaultdict(set)
    proper=0;outside=0
    for v0 in adj:
        for v1 in adj[v0]:
            for v2 in adj[v1]:
                for v3 in adj[v2]:
                    path=(v0,v1,v2,v3)
                    if (len({v[0] for v in path})!=4 or
                            len({v[1] for v in path})!=4):
                        continue
                    proper+=1
                    q=ifa.get(tuple(sorted((v0[0],v3[0]))))
                    r=iga.get(tuple(sorted((v0[1],v3[1]))))
                    if q is None or r is None:
                        continue
                    projection_data=projection(geo,q,r)
                    if projection_data is None:
                        continue
                    p,ell,anchors=projection_data
                    if set(anchors)&Z:
                        continue
                    if (set(f[p])&{v[0] for v in path} or
                            set(g[ell])&{v[1] for v in path}):
                        continue
                    pathids=tuple(owner[tuple(sorted((path[j],path[j+1])))]
                                  for j in range(3))
                    ids=tuple(sorted(pathids+anchors))
                    if len(set(ids))!=6 or bbo_structure(ids,c,geo,Z) is None:
                        raise AssertionError("physical original path failed six-ID BBo structure")
                    images[ids].add(path)
                    if any(i not in C for i in anchors):
                        outside+=1
    if any(len(z)!=2 for z in images.values()):
        raise AssertionError("not two physical directed BBo paths per original sixset")
    for ids,seen in images.items():
        if set(inverse_bbo(ids,c,geo,C,Z,owner))!=seen:
            raise AssertionError("independent source-first inverse and physical-first BBo disagree")
    return dict(sets=set(images),proper=proper,
                produced_directed=sum(len(z) for z in images.values()),
                original_anchors_outside_core_directed=outside)


def original_seeded_d6(c,seed,Z=()):
    """Independently extend source D6 seed via whole-flag coherent typed cuts."""
    flags,f,g=c["flags"],c["f"],c["g"]
    lift=inverse_d6(seed,c,Z)
    if len(lift)!=1:
        raise ValueError("not a genuine original aligned D6 sixset")
    v=lift[0]
    a=c["a"]
    color_f={v[j][0]:j%2 for j in range(6)}
    color_g={v[j][1]:j%2 for j in range(6)}
    for x in range(a):
        color_f.setdefault(x,x%2)
        color_g.setdefault(x,x%2)
    selected=set(seed);Z=set(Z)
    for i,(p,ell) in enumerate(flags):
        if i in selected or i in Z:
            continue
        x,z=f[p];y,w=g[ell]
        if color_f[x]==color_f[z] or color_g[y]==color_g[w]:
            continue
        if any((p==flags[j][0] and set(g[ell])&set(g[flags[j][1]]))
               or (ell==flags[j][1] and set(f[p])&set(f[flags[j][0]]))
               for j in selected):
            continue
        selected.add(i)
    adj,owner=owned_graph(c,selected)
    for v,neighbors in adj.items():
        if (len({u[0] for u in neighbors})!=len(neighbors)
                or len({u[1] for u in neighbors})!=len(neighbors)):
            raise AssertionError("original no-cherry selector violated")
        if any(color_f[v[0]]==color_f[u[0]] or color_g[v[1]]==color_g[u[1]]
               for u in neighbors):
            raise AssertionError("original coordinate cuts violated")
    sixsets=set()
    physical=independent_cycles(adj)
    for cycle in physical:
        if len({v[0] for v in cycle})!=6 or len({v[1] for v in cycle})!=6:
            raise AssertionError("physical C6 not coordinate proper")
        ids=tuple(sorted(owner[tuple(sorted((cycle[j],cycle[(j+1)%6])))]
                         for j in range(6)))
        if len(set(ids))!=6 or set(ids)&Z:
            raise AssertionError("original D6 source IDs repeated or deleted")
        if inverse_d6(ids,c,Z,owner)!=(cycle,):
            raise AssertionError("source-original inverse does not recover physical C6")
        if ids in sixsets:
            raise AssertionError("two unoriented physical C6 use same six ORIGINAL IDs")
        sixsets.add(ids)
    if tuple(sorted(seed)) not in sixsets:
        raise AssertionError("actual original six-ID D6 seed lost by extension")
    return dict(selected_source=len(selected),physical_edges=len(owner),
                physical_C6=len(physical),sixsets=sixsets)



def exhaustive_original_W32_BBo_left_B_scan(scheme):
    """Original source-first 10,935-candidate exhaustive LEFT-B scan.

    Does not invoke prior seven-family classifier or previous physical path
    enumerator. The genuine fixed W32 point mapping is a K6 pair bijection.
    The LEFT B motif is one doubled original point factor and a 4-cycle on
    the FOUR remaining coordinates. Enumerate all 15*3*3*3^4 = 10935
    ORIGINAL six-ID candidate sets with named source line-flag choices.
    Compare source-only BBo topology with its independent 0/2 inverse.
    """
    from itertools import permutations, product
    c=source_case(1,scheme)
    geo=geometry(c)
    a=c["a"]
    if a!=6 or c["V"]!=15:
        raise AssertionError("not full original W32 physical K6 pair alphabet")
    flags,f=c["flags"],c["f"]
    by_p=defaultdict(list)
    for i,(p,ell) in enumerate(flags):
        by_p[p].append(i)
    invf={pair:p for p,pair in enumerate(f)}
    if len(invf)!=15 or len(by_p)!=15 or any(len(ids)!=3 for ids in by_p.values()):
        raise AssertionError("not complete original 15 point 3-line pencil source")
    n=0
    accepted=set()
    in_image=set()
    no_image=[]
    for p in range(15):
        rest=tuple(sorted(set(range(a))-set(f[p])))
        if len(rest)!=4:
            raise AssertionError("original doubled f(p) does not leave four symbols")
        u=rest[0]
        cycles=set()
        for permutation in permutations(rest[1:]):
            vs=(u,)+permutation
            e=tuple(sorted(tuple(sorted((vs[j],vs[(j+1)%4])))
                           for j in range(4)))
            cycles.add(e)
        if len(cycles)!=3:
            raise AssertionError("not precisely three genuine four-coordinate cycles")
        for cyc in cycles:
            other_points=tuple(invf[pair] for pair in cyc)
            if len(set(other_points))!=4 or p in other_points:
                raise AssertionError("source point factor duplicated outside doubled f")
            for doubled in combinations(by_p[p],2):
                for isolated in product(*(by_p[q] for q in other_points)):
                    ids=tuple(sorted(doubled+isolated))
                    if len(set(ids))!=6:
                        raise AssertionError("left B source candidate repeats original ID")
                    n+=1
                    topo=bbo_structure(ids,c,geo)
                    if topo is None:
                        continue
                    if ids in accepted:
                        raise AssertionError("original left-B sixset enumerated twice")
                    accepted.add(ids)
                    paths=inverse_bbo(ids,c,geo,range(len(flags)))
                    if paths:
                        if len(paths)!=2 or paths[0]!=paths[1][::-1]:
                            raise AssertionError("original BBo image not reverse pair")
                        in_image.add(ids)
                    else:
                        no_image.append(ids)
    if n!=10935:
        raise AssertionError("failed exhaustive W32 LEFT B true source census")
    if len(in_image)>len(accepted):
        raise AssertionError("source image exceeded complete true original BBo")
    return {
        "s":2,"scheme":scheme,
        "complete_original_LEFT_B_source_candidates":n,
        "all_original_BBo_sixsets":len(accepted),
        "original_BBo_sixsets_with_physical_3path":len(in_image),
        "original_BBo_source_sixsets_without_aligned_physical_3path":
            len(no_image),
        "first_nonimage_six_original_IDs":
            list(no_image[0]) if no_image else None,
        "original_BBo_inverse_0_or_2_for_ALL_full_source_sixsets":True,
    }


def canonical_referee():
    root=Path(__file__).parent
    low=json.loads((root/"hyp105_original_lowtail_alln_energy_certificates.json").read_text())
    heavy=json.loads((root/"hyp105_original_deletion_adaptive_heavy_tail_certificates.json").read_text())
    low_rows=[]
    for z in low["genuine_true_original_cases"]:
        c=source_case({2:1,4:2}[z["s"]],z["scheme"])
        geo=geometry(c)
        C=z["original_core_source_IDs"];Z=z["deleted_original_flag_IDs"]
        obs=physical_first_bbo(c,geo,C,Z)
        frozen={tuple(ids) for ids in z["real_positive_original_BBo_six_IDs"]}
        if obs["sets"]!=frozen or obs["proper"]!=z["physical_proper_ordered_3paths"]:
            raise AssertionError("independent source sixset inverse differs from historic actual frozen source")
        low_rows.append(dict(s=z["s"],scheme=z["scheme"],
                             original_BBo_sixsets=len(frozen),
                             proper_physical_directed3=obs["proper"],
                             independently_inverted_directed3=obs["produced_directed"],
                             anchors_outside_CORE_directed=obs["original_anchors_outside_core_directed"]))
    heavy_rows=[]
    for z in heavy["genuine_source_cases"]:
        if z.get("empty_tail"):
            continue
        c=source_case({2:1,4:2}[z["s"]],z["scheme"])
        for seed in z["true_original_D6_six_flag_IDs_selected"]:
            obs=original_seeded_d6(c,seed,z["deleted_original_flag_IDs"])
            heavy_rows.append(dict(s=z["s"],scheme=z["scheme"],original_seed=seed,
                                   selected_original_source=obs["selected_source"],
                                   physical_edges=obs["physical_edges"],
                                   physical_D6_C6=obs["physical_C6"]))
    if not any(z["original_BBo_sixsets"]>0 for z in low_rows) or not heavy_rows:
        raise AssertionError("nonvacuous original source positive controls missing")
    return dict(schema="mathlab.hyp105.original-sixID-inverse-referee.v1",
                root_230_status=ROOT_STATUS,
                root_Branch_A_unconditionally_accepted=False,
                BBo_inverse_is_not_all_class_surjectivity=True,
                genuine_original_lowtail=low_rows,
                genuine_original_heavy=heavy_rows,
        exhaustive_W32_original_BBo_source_vs_image=[
            exhaustive_original_W32_BBo_left_B_scan(z)
            for z in ("lex","reverse-line")])


if __name__=="__main__":
    print("AA4_TRUE_ORIGINAL_SIXID_INVERSE_CERTIFICATE="+json.dumps(
        canonical_referee(),sort_keys=True,separators=(",",":")),flush=True)
