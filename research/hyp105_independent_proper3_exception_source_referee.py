"""AA4-P3EXC: independent ORIGINAL proper-three-walk + exceptional END-PAIR referee.

Exact universal finite-graph AND true symplectic W(3,2),W(3,4) checks.
No import of earlier P3/improper/exceptions/BBo/referee modules; only
the genuine original source incidence constructor.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations

from hyp105_full_physical_degree_tail import genuine_source


def _validate_pair_labels(V, labels):
    a=2
    while a*(a-1)//2<V:a+=1
    try: labels=tuple(tuple(x) for x in labels)
    except (TypeError,ValueError):raise ValueError("complete original pair maps required")
    legal=set(combinations(range(a),2))
    if len(labels)!=V or len(set(labels))!=V or any(p not in legal for p in labels):
        raise ValueError("complete separately globally injective typed pair map required")
    return a,labels


def _source_geometry(V, flags):
    pl=[set() for _ in range(V)]
    lp=[set() for _ in range(V)]
    lookup={}
    for i,(p,l) in enumerate(flags):
        pl[p].add(l);lp[l].add(p);lookup[p,l]=i
    C=[set().union(*(lp[l] for l in pl[p]))-{p} for p in range(V)]
    proj={}
    for q in range(V):
        for r in range(V):
            if r in pl[q]:continue
            anchors=C[q]&lp[r]
            if len(anchors)!=1:raise AssertionError("original GQ projection not unique")
            p=next(iter(anchors))
            ell=pl[q]&pl[p]
            if len(ell)!=1:raise AssertionError("original GQ connecting line not unique")
            proj[q,r]=(p,next(iter(ell)))
    return pl,lp,lookup,proj


def _physical_graph(a,flags,f,g,ids):
    graph={(x,y):set() for x in range(a) for y in range(a)}
    provenance={}
    for i in ids:
        p,l=flags[i]; x,z=f[p]; y,w=g[l]
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            e=frozenset((u,v))
            if len(e)!=2 or e in provenance:
                raise AssertionError("physical paired flag edge provenance duplicates")
            provenance[e]=i
            graph[u].add(v);graph[v].add(u)
    if len(provenance)!=2*len(ids):
        raise AssertionError("missing original physical second diagonal")
    return graph,provenance


def _bad_mask(v):
    x=[u[0] for u in v]
    y=[u[1] for u in v]
    # Adjacent coordinate repeats are impossible for legitimate physical edges.
    return sum(1<<i for i,z in enumerate(
        (x[0]==x[2],x[1]==x[3],x[0]==x[3],
         y[0]==y[2],y[1]==y[3],y[0]==y[3])) if z)


def _three_walk_source_free(graph):
    """PHYSICAL walk-forward, independent of endpoint-middle-edge tensor."""
    hits=Counter()
    P3=Counter()
    all_walks=0
    for v0,N0 in graph.items():
        for v1 in N0:
            for v2 in graph[v1]:
                for v3 in graph[v2]:
                    mask=_bad_mask((v0,v1,v2,v3))
                    hits[mask]+=1
                    all_walks+=1
                    if mask==0:P3[v0,v3]+=1
    good=sum(P3.values())
    return all_walks,all_walks-good,hits,P3


def _three_walk_endpoint_tensor(graph):
    """INDEPENDENT endpoint-first constrained middle-edge contraction.

    The opposite of forward DFS: choose v0,v3 first; then choose v1
    from neighbors(v0) and v2 from neighbors(v3), test v1--v2 edge.
    For proper paths only the nonadjacent coordinate equalities matter.
    """
    P3=Counter()
    active=[v for v,N in graph.items() if N]
    for v0 in active:
        for v3 in active:
            if v0[0]==v3[0] or v0[1]==v3[1]:continue
            for v1 in graph[v0]:
                if v1[0]==v3[0] or v1[1]==v3[1]:continue
                for v2 in graph[v3]:
                    if v2[0]==v0[0] or v2[1]==v0[1]:continue
                    if v2 in graph[v1]:
                        P3[v0,v3]+=1
    return P3


def _two_walk_books(graph):
    """EXACT coordinate two-walk return populations (physical-first)."""
    Qx=Qy=bad=0
    for v0,N0 in graph.items():
        for v1 in N0:
            for v2 in graph[v1]:
                a=v0[0]==v2[0]
                b=v0[1]==v2[1]
                Qx+=a;Qy+=b;bad+=a or b
    m=sum(len(N) for N in graph.values())//2
    if bad!=Qx+Qy-2*m:
        raise AssertionError("2-walk inclusion/exclusion lost exact backtracking")
    return {"Qx":Qx,"Qy":Qy,"B2":bad,"edges":m,
            "max_degree":max(map(len,graph.values()),default=0)}


def _finite_endpoint_partition(a, f,g, flags, source):
    """FULL original source endpoint classes, physical first, all 4M² cells."""
    pl,lp,lookup,proj=source
    invf={p:i for i,p in enumerate(f)}
    invg={p:i for i,p in enumerate(g)}
    classes={}
    counts=Counter()
    for u0 in ((x,y) for x in range(a) for y in range(a)):
        for u3 in ((z,w) for z in range(a) for w in range(a)):
            if u0[0]==u3[0] or u0[1]==u3[1]:continue
            q=invf.get(tuple(sorted((u0[0],u3[0]))))
            r=invg.get(tuple(sorted((u0[1],u3[1]))))
            if q is None or r is None:
                label="missing"
            elif r in pl[q]:
                label="incident"
            else:
                p,ell=proj[q,r]
                L=bool(set(f[q])&set(f[p]))
                R=bool(set(g[r])&set(g[ell]))
                label="bad" if L or R else "good"
            classes[u0,u3]=label
            counts[label]+=1
    return classes,counts


def _full_original_bad_books(V,flags,f,g,source):
    pl,lp,_lookup,proj=source
    Mg=Mf=0
    for p in range(V):
        ys=Counter(y for ell in pl[p] for y in g[ell])
        Mg+=sum(k*(k-1)//2 for k in ys.values())
    for ell in range(V):
        xs=Counter(x for p in lp[ell] for x in f[p])
        Mf+=sum(k*(k-1)//2 for k in xs.values())
    L=R=J=0
    for (q,r),(p,ell) in proj.items():
        left=bool(set(f[q])&set(f[p]))
        right=bool(set(g[r])&set(g[ell]))
        L+=left;R+=right;J+=left and right
    return {"Mf":Mf,"Mg":Mg,"original_bad_left":L,
            "original_bad_right":R,"original_bad_joint":J,
            "source_2s_books":(L,R)}


def _inclusion_exclusion_64(mask_hist):
    """Exact Möbius inversion over SIX forbidden coordinate return events."""
    intersections=[sum(ct for mask,ct in mask_hist.items() if mask&b==b)
                   for b in range(64)]
    proper=sum((-1)**b.bit_count()*intersections[b] for b in range(64))
    return {"proper_inclusion_exclusion":proper,
            "improper_inclusion_exclusion":intersections[0]-proper,
            "single_event_sizes":tuple(intersections[1<<i] for i in range(6)),
            "overlap_correction_total":
                sum(intersections[1<<i] for i in range(6))
                -(intersections[0]-proper)}


def _source_sixset_image(graph,edge_owner,flags,source,f,g,classes):
    """Independent ANCHOR/ORIGINAL-ID sixset audit on ACTUAL proper GOOD paths.

    Does not use previous historical BBo path generator or GF5 code.
    All color masks and six source IDs are reconstructed from genuine
    physical three-edge paths and the complete source GQ projection.
    """
    pl,lp,lookup,proj=source
    invf={p:i for i,p in enumerate(f)}
    invg={p:i for i,p in enumerate(g)}
    counts=Counter()
    paths=0
    blocked=Counter()
    for v0,near in graph.items():
        for v1 in near:
            for v2 in graph[v1]:
                for v3 in graph[v2]:
                    v=(v0,v1,v2,v3)
                    if _bad_mask(v) or classes.get((v0,v3))!="good":continue
                    q=invf[tuple(sorted((v0[0],v3[0])))]
                    r=invg[tuple(sorted((v0[1],v3[1])))]
                    p,ell=proj[q,r]
                    flagsbad=(v1[0] in f[p],v2[0] in f[p],
                              v1[1] in g[ell],v2[1] in g[ell])
                    if any(flagsbad):
                        blocked[sum(1<<i for i,z in enumerate(flagsbad) if z)]+=1
                        continue
                    owners=[edge_owner[frozenset((v[i],v[i+1]))] for i in range(3)]
                    anchor=[lookup[q,ell],lookup[p,ell],lookup[p,r]]
                    six=tuple(sorted(owners+anchor))
                    if (len(set(six))!=6 or
                        Counter(flags[i][0] for i in six).most_common(1)[0][1]!=2 or
                        Counter(flags[i][1] for i in six).most_common(1)[0][1]!=2):
                        raise AssertionError("not six distinct ORIGINAL BBo source flags")
                    counts[six]+=1
                    paths+=1
    if any(v!=2 for v in counts.values()) or 2*len(counts)!=paths:
        raise AssertionError("original BBo image must have 2 directed paths per sixset")
    return {"unblocked_original_paths":paths,
            "produced_original_BBo_sixsets":len(counts),
            "directed_paths_per_original_sixset":
                tuple(sorted(set(counts.values()))),
            "internal_blocker_exact_union":sum(blocked.values()),
            "sixsets":tuple(sorted(counts))}


def exact_original_proper3_exceptional_referee(power,f,g,core_ids=None):
    if type(power) is not int or power not in (1,2):
        raise ValueError("finite original symplectic source oracle only W32/W34")
    s,V,flags=genuine_source(power)
    a,f=_validate_pair_labels(V,f)
    b,g=_validate_pair_labels(V,g)
    if b!=a:raise AssertionError("source factor physical alphabets differ")
    ids=tuple(range(len(flags))) if core_ids is None else tuple(core_ids)
    if any(type(i) is not int or i<0 or i>=len(flags) for i in ids) or len(set(ids))!=len(ids):
        raise ValueError("core must have unique real ORIGINAL incidence IDs")
    src=_source_geometry(V,flags)
    graph,owner=_physical_graph(a,flags,f,g,ids)
    allwalk,improper,mask_hist,p3=_three_walk_source_free(graph)
    tensor=_three_walk_endpoint_tensor(graph)
    if p3!=tensor:
        raise AssertionError("independent proper-three tensor and walk DFS disagree")
    ie=_inclusion_exclusion_64(mask_hist)
    if (ie["proper_inclusion_exclusion"]!=sum(p3.values()) or
        ie["improper_inclusion_exclusion"]!=improper):
        raise AssertionError("exact 64-event return-set inclusion/exclusion disagrees")
    two=_two_walk_books(graph)
    book= _full_original_bad_books(V,flags,f,g,src)
    classes,pop=_finite_endpoint_partition(a,f,g,flags,src)
    M=a*(a-1)//2;N=len(flags)
    expected={
        "missing":4*(M*M-V*V),
        "incident":4*N,
        "bad":4*(2*s*(book["Mf"]+book["Mg"])-book["original_bad_joint"]),
        "good":4*(V*V-N-2*s*(book["Mf"]+book["Mg"])+book["original_bad_joint"])
    }
    if dict(pop)!= {k:v for k,v in expected.items() if v}:
        raise AssertionError(("physical 4M² end partition vs ORIGINAL books",pop,expected))
    if (book["original_bad_left"]!=2*s*book["Mf"] or
        book["original_bad_right"]!=2*s*book["Mg"]):
        raise AssertionError("original GQ 2s times pencil collision identity fails")
    R0=Counter((p,y) for i in ids for p,ell in (flags[i],) for y in g[ell])
    L0=Counter((ell,x) for i in ids for p,ell in (flags[i],) for x in f[p])
    Mg0=sum(k*(k-1)//2 for k in R0.values())
    Mf0=sum(k*(k-1)//2 for k in L0.values())
    if two["Qx"]!=4*len(ids)+4*Mg0 or two["Qy"]!=4*len(ids)+4*Mf0:
        raise AssertionError("original CORE exact improper two-walk book failed")
    Delta=two["max_degree"]
    if improper>2*Delta*two["B2"]+Delta*(two["Qx"]+two["Qy"]):
        raise AssertionError("published ALL-h 3-walk improper union cap false")
    total_three= sum(len(graph[v])*len(graph[w]) for v,ns in graph.items() for w in ns)
    if total_three!=allwalk:
        raise AssertionError("independent core degree product 3-walk total disagrees")
    # Blakley-Roy / homomorphism Sidorenko for P4: ALL undirected graphs,
    # includes physical isolates in the n=a*a vertex denominator.
    e=two["edges"];nn=a*a
    if Fraction(allwalk)<Fraction((2*e)**3,nn**2):
        raise AssertionError("universal length-three walk density lower failed")
    weights=Counter()
    norms=Counter()
    for (v0,v3),k in p3.items():
        weights[classes[v0,v3]]+=k
        norms[classes[v0,v3]]+=k*k
    Wexc=sum(weights[x] for x in ("missing","incident","bad"))
    Eexc=sum(pop[x] for x in ("missing","incident","bad"))
    normall=sum(k*k for k in p3.values())
    if Wexc*Wexc>Eexc*sum(norms[x] for x in ("missing","incident","bad")):
        raise AssertionError("adaptive actual exceptional-endpoint CS failed")
    source_six=_source_sixset_image(graph,owner,flags,src,f,g,classes)
    if source_six["unblocked_original_paths"]+source_six["internal_blocker_exact_union"]!=weights["good"]:
        raise AssertionError("exact original-end-good proper path partition fails")
    if (allwalk-improper-Wexc-source_six["internal_blocker_exact_union"]
        !=source_six["unblocked_original_paths"]):
        raise AssertionError("original source-admissible path subtraction not exact")
    return {
        "s":s,"V":V,"a":a,"original_core_flag_count":len(ids),
        "physical_core_edges":two["edges"],"physical_degree_cap":Delta,
        "all_directed_three_walks":allwalk,
        "improper_directed_three_walks":improper,
        "proper_directed_three_walks":sum(p3.values()),
        "proper_endpoint_pair_cells_nonzero":len(p3),
        "proper_frobenius_squared":normall,
        "exact_six_event_return_mobius":ie,
        "two_walk_full_books":two,"original_core_Mf":Mf0,"original_core_Mg":Mg0,
        "source_full_Mf":book["Mf"],"source_full_Mg":book["Mg"],
        "original_bad_joint_J":book["original_bad_joint"],
        "full_original_four_class_endpoint_counts":expected,
        "proper_three_walk_mass_by_endpoint_class":dict(weights),
        "proper_three_frobenius_by_endpoint_class":dict(norms),
        "exceptional_endpoint_proper_mass":Wexc,
        "exceptional_endpoint_count":Eexc,
        "exceptional_adaptive_cauchy_upper_squared":
            Eexc*sum(norms[x] for x in ("missing","incident","bad")),
        "original_BBo_image":source_six,
        "independent_endpoint_tensor_equal_forward_walk":True,
        "original_sixID_path_bookkeeping_exact":True
    }
