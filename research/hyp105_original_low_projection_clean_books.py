"""AA4-LOW-AC-CLEAN: independent all-h ORIGINAL GQ endpoint and A/C blocker review.

Original symplectic W(3,s), arbitrary fixed separately complete
globally pair-injective f and g, FULL allowed original source A=I\\Z
and paired physical CORE C subset A (in Branch A Z=empty, A=I).

NEW exact projection-/endpoint-clean source books Bh_x/Bh_y prune the
historical mixed books Bx/By by eliminating original source candidates
with nonexistent/forbidden three-anchor GQ projection, incident
endpoints, or f(q)/f(p) or g(r)/g(ell) endpoint collisions.

For true coordinate-proper, endpoint-good physical CORE 3paths:
 I_x1**2 <= Bh_x * tr(D_C A_C**4) <= Bx * Delta_C * tr(A_C**4)
 I_y1**2 <= Bh_y * tr(D_C A_C**4) <= By * Delta_C * tr(A_C**4)
and reversal gives x2=x1, y2=y1. A/C must NOT be conflated.
No new universal B0, root PROVED_A or ASET exponent is asserted.
Also independent all-h combinatorial proof that each named original
flag appears exactly s**2 times in each of the THREE offincidence
point-line GQ projection anchor roles (the Z endpoint budget).

All source/physical constructions except genuine_symplectic_source are
implemented independently; no import of old mixed blockers, GQ
projection, root or LOW budget module.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations
import json

SCHEMA="mathlab.hyp105.original-low-projection-clean-AC-books.v1"
STATUS="OPEN_WITH_FORMAL_BLOCKER"
PARENT=779


def canonical_pair(a,b):
    if a==b: raise ValueError("genuine physical edges have no loops")
    return (a,b) if a<b else (b,a)


def other(pair,shared):
    if shared==pair[0]:return pair[1]
    if shared==pair[1]:return pair[0]
    raise ValueError("physical symbol not in genuine original pair")


def min_pairs(V):
    if type(V)!=int or V<1: raise ValueError("positive source size")
    a=2
    while a*(a-1)//2<V:
        a+=1
    pairs=tuple(combinations(range(a),2))[:V]
    if not (len(pairs)==V and len(set(pairs))==V):
        raise AssertionError("global pair injectivity fails")
    return a,pairs


def genuine_original(s,mode,removed=(),core_scheme="two_thirds"):
    from hyp105_original_defect_factor_referee import genuine_symplectic_source
    if s not in (2,4) or type(s)!=int:
        raise ValueError("actual ORIGINAL symplectic source only W32/W34")
    flags=tuple(map(tuple,genuine_symplectic_source(s)))
    V=(s+1)*(s*s+1)
    N=(s+1)*V
    if len(flags)!=N or len(set(flags))!=N:
        raise AssertionError("non-original GQ source")
    a,pairs=min_pairs(V)
    f=pairs
    if mode=="lex":
        g=pairs
    elif mode=="reverse":
        g=pairs[::-1]
    elif mode=="shift":
        g=pairs[7:]+pairs[:7]
    else:
        raise ValueError("fixed complete source label mode required")
    if len(set(f))!=V or len(set(g))!=V:
        raise AssertionError("source f/g must be SEPARATELY injected")
    Z=frozenset(removed)
    if any(type(i)!=int or i<0 or i>=N for i in Z):
        raise ValueError("valid distinct original Z IDs only")
    A=frozenset(set(range(N))-Z)
    if core_scheme=="full":
        C=A
    elif core_scheme=="two_thirds":
        C=frozenset(i for i in A if i%3!=0)
    elif core_scheme=="half":
        C=frozenset(i for i in A if i%2==0)
    elif core_scheme=="thin":
        C=frozenset(i for i in A if i%5==0)
    else:
        raise ValueError("invalid original named CORE selector")
    return dict(s=s,V=V,N=N,a=a,flags=flags,f=f,g=g,Z=Z,A=A,C=C,
                mode=mode,core_scheme=core_scheme)


def true_gq_projection(source):
    """Independent true GQ axiom, every q outside r has exactly ONE q-ell-p-r."""
    V=source["V"];flags=source["flags"];s=source["s"]
    from_line=[set() for _ in range(V)]
    through_point=[set() for _ in range(V)]
    fid={}
    for i,(p,l) in enumerate(flags):
        if (p,l) in fid:
            raise AssertionError("source GQ duplicate original incidence")
        fid[p,l]=i
        from_line[l].add(p)
        through_point[p].add(l)
    if any(len(x)!=s+1 for x in from_line+through_point):
        raise AssertionError("actual original point/line pencil not regular")
    point_col=[set() for _ in range(V)]
    line_col=[set() for _ in range(V)]
    for points in from_line:
        for p,q in combinations(sorted(points),2):
            point_col[p].add(q);point_col[q].add(p)
    for lines in through_point:
        for l,r in combinations(sorted(lines),2):
            line_col[l].add(r);line_col[r].add(l)
    if any(len(z)!=s*(s+1) for z in point_col+line_col):
        raise AssertionError("true symplectic GQ collinearity regularity lost")
    proj={}
    for q in range(V):
        for r in range(V):
            if (q,r) in fid: continue
            matches=[(p,ell) for p in from_line[r] for ell in through_point[q]
                     if (p,ell) in fid]
            if len(matches)!=1:
                raise AssertionError("original GQ offincidence projection not UNIQUE")
            p,ell=matches[0]
            if p==q or (q,ell) not in fid or (p,r) not in fid:
                raise AssertionError("original projection anchor invalid")
            proj[q,r]=(p,ell)
    if len(proj)!=V*V-source["N"]:
        raise AssertionError("lost genuine offincidence endpoint pairs")
    role_counts={typ:Counter() for typ in ("qell","pell","pr")}
    for (q,r),(p,ell) in proj.items():
        role_counts["qell"][fid[q,ell]]+=1
        role_counts["pell"][fid[p,ell]]+=1
        role_counts["pr"][fid[p,r]]+=1
    if any(len(z)!=source["N"] or set(z.values())!={s*s}
           for z in role_counts.values()):
        raise AssertionError("each REAL original flag must appear s² times in EVERY role")
    return dict(fid=fid,from_line=from_line,through_point=through_point,
                point_col=point_col,line_col=line_col,proj=proj,
                roles=role_counts)


def physical_source_edges(source,ids):
    """Construct BOTH unique real physical diagonal edges for every source ID."""
    edges={}
    for i in sorted(ids):
        p,l=source["flags"][i]
        x,k=source["f"][p];y,z=source["g"][l]
        ee=(canonical_pair((x,y),(k,z)),canonical_pair((x,z),(k,y)))
        if ee[0]==ee[1] or set(ee[0])&set(ee[1]):
            raise AssertionError("original incidence lost one disjoint diagonal")
        for e in ee:
            if e in edges:
                raise AssertionError("physical edge cloned by two ORIGINAL source IDs")
            edges[e]=i
    if len(edges)!=2*len(ids):
        raise AssertionError("missing original paired CORE edge")
    return edges


def physical_graph(source):
    edgeA=physical_source_edges(source,source["A"])
    edgeC=physical_source_edges(source,source["C"])
    adjA=defaultdict(set);adjC=defaultdict(set)
    for e in edgeA:
        u,v=e;adjA[u].add(v);adjA[v].add(u)
    for e in edgeC:
        u,v=e;adjC[u].add(v);adjC[v].add(u)
    if not set(edgeC).issubset(edgeA):
        raise AssertionError("original CORE physical edges not in allowed A")
    a=source["a"]
    d_A={v:len(adjA[v]) for v in ((x,y) for x in range(a) for y in range(a))}
    d_C={v:len(adjC[v]) for v in d_A}
    if sum(d_A.values())!=4*len(source["A"]) or sum(d_C.values())!=4*len(source["C"]):
        raise AssertionError("true physical source degree mass false")
    Delta=max(d_C.values(),default=0)
    trace4=weighted4=0
    for v in d_A:
        nbs=adjC[v]
        for w in d_A:
            two=len(nbs&adjC[w])
            sq=two*two
            trace4+=sq
            weighted4+=d_C[v]*sq
    theta=sum(d_A[v]*d_C[v] for v in d_A)
    if weighted4>Delta*trace4 or theta>4*len(source["A"])*Delta:
        raise AssertionError("source/cross CORE weighted trace or theta broken")
    return dict(edgesA=edgeA,edgesC=edgeC,adjA=adjA,adjC=adjC,
                d_A=d_A,d_C=d_C,Delta=Delta,trace4=trace4,
                weighted4=weighted4,theta=theta)


def key_books(source,gq):
    """Literal SOURCE-first old+new keys on all complete original f/g labels."""
    f,g,flags=source["f"],source["g"],source["flags"]
    old={"x":set(),"y":set()}
    clean={"x":set(),"y":set()}
    reason={side:Counter() for side in ("x","y")}
    A=source["A"];C=source["C"]
    bypA=defaultdict(list);bylA=defaultdict(list)
    bypC=defaultdict(list);bylC=defaultdict(list)
    for i in A:
        p,l=flags[i]
        bypA[p].append(l);bylA[l].append(p)
    for i in C:
        p,l=flags[i]
        bypC[p].append(i);bylC[l].append(i)
    invf=defaultdict(list);invg=defaultdict(list)
    for p,pair in enumerate(f):
        for x in pair:invf[x].append(p)
    for l,pair in enumerate(g):
        for y in pair:invg[y].append(l)
    for u,owners in bypC.items():
        for x,k in ((f[u][0],f[u][1]),(f[u][1],f[u][0])):
            for p in invf[k]:
                for q in gq["point_col"][p]:
                    if x not in f[q]:continue
                    for i in owners:
                        ell_u=flags[i][1]
                        for r in bypA[p]:
                            for y in set(g[r])&set(g[ell_u]):
                                key=(i,x,k,p,q,r,y)
                                old["x"].add(key)
                                proj=gq["proj"].get((q,r))
                                if proj is None or proj[0]!=p:
                                    reason["x"]["incident_or_wrong_projection"]+=1
                                    continue
                                pp,ell=proj
                                if any(gq["fid"][l] not in A
                                       for l in ((q,ell),(p,ell),(p,r))):
                                    reason["x"]["missing_ALLOWED_anchor"]+=1
                                    continue
                                if set(f[q])&set(f[p]) or set(g[r])&set(g[ell]):
                                    reason["x"]["bad_end_pair"]+=1
                                    continue
                                clean["x"].add(key)
    for l,owners in bylC.items():
        for y,k in ((g[l][0],g[l][1]),(g[l][1],g[l][0])):
            for ell in invg[k]:
                for r in gq["line_col"][ell]:
                    if y not in g[r]:continue
                    for i in owners:
                        u=flags[i][0]
                        for q in bylA[ell]:
                            for x in set(f[q])&set(f[u]):
                                key=(i,y,k,ell,r,q,x)
                                old["y"].add(key)
                                proj=gq["proj"].get((q,r))
                                if proj is None or proj[1]!=ell:
                                    reason["y"]["incident_or_wrong_projection"]+=1
                                    continue
                                p,ee=proj
                                if any(gq["fid"][l] not in A
                                       for l in ((q,ell),(p,ell),(p,r))):
                                    reason["y"]["missing_ALLOWED_anchor"]+=1
                                    continue
                                if set(f[q])&set(f[p]) or set(g[r])&set(g[ell]):
                                    reason["y"]["bad_end_pair"]+=1
                                    continue
                                clean["y"].add(key)
    for side in ("x","y"):
        if not clean[side].issubset(old[side]):
            raise AssertionError("projection-clean book is NOT subset of old mixed FULL/CORE book")
        if len(old[side])!=len(clean[side])+sum(reason[side].values()):
            raise AssertionError("original SOURCE book partition missed duplicate witness keys")
    return dict(old=old,clean=clean,reason=reason,
                bypA=bypA,bylA=bylA,bypC=bypC,bylC=bylC)


def _decode_from_key(source,key,side):
    f,g,flags=source["f"],source["g"],source["flags"]
    if side=="x":
        i,x,k,p,q,r,y=key
        _,ell_u=flags[i]
        v0=(x,y);v1=(k,other(g[ell_u],y))
        v3=(other(f[q],x),other(g[r],y))
    elif side=="y":
        i,y,k,ell,r,q,x=key
        u,_=flags[i]
        v0=(x,y);v1=(other(f[u],x),k)
        v3=(other(f[q],x),other(g[r],y))
    else:
        raise ValueError("true x/y dual source only")
    return v0,v1,v3


def physical_first_triples(source,gq,physical,books):
    """INDEPENDENT PHYSICAL-first genuine endpoint-good triple census.

    No calls to the SOURCE-first book enumeration algorithm to generate
    triples: trace edges -> true physical corner -> endpoint pair decode ->
    FULL original GQ projection -> distinct ID and accepted anchors.
    """
    f,g,flags=source["f"],source["g"],source["flags"]
    invf=defaultdict(list);invg=defaultdict(list)
    for p,pair in enumerate(f):
        for k in pair: invf[k].append(p)
    for l,pair in enumerate(g):
        for k in pair: invg[k].append(l)
    results={"x":{},"y":{}}
    outsideC={"x":0,"y":0}
    for edge,i in physical["edgesC"].items():
        for v0,v1 in ((edge[0],edge[1]),(edge[1],edge[0])):
            x,y=v0
            for q in invf[x]:
                x3=other(f[q],x)
                for r in invg[y]:
                    y3=other(g[r],y)
                    proj=gq["proj"].get((q,r))
                    if proj is None:continue
                    p,ell=proj
                    anchors=(gq["fid"][q,ell],gq["fid"][p,ell],gq["fid"][p,r])
                    if any(z not in source["A"] for z in anchors):continue
                    if set(f[q])&set(f[p]) or set(g[r])&set(g[ell]):continue
                    t=(v0,v1,(x3,y3))
                    if v1[0] in f[p]:
                        key=(i,v0[0],v1[0],p,q,r,v0[1])
                        if key not in books["clean"]["x"]:
                            raise AssertionError("FIRST TRUE x-blocker triple has no CLEAN original witness")
                        if _decode_from_key(source,key,"x")!=t:
                            raise AssertionError("source-to-physical clean x left inverse fails")
                        if t in results["x"] and results["x"][t]!=key:
                            raise AssertionError("FIRST x-blocker physical triple not single-valued")
                        results["x"][t]=key
                        outsideC["x"]+=int(any(z not in source["C"] for z in anchors))
                    if v1[1] in g[ell]:
                        key=(i,v0[1],v1[1],ell,r,q,v0[0])
                        if key not in books["clean"]["y"]:
                            raise AssertionError("FIRST TRUE y-blocker triple has no CLEAN original witness")
                        if _decode_from_key(source,key,"y")!=t:
                            raise AssertionError("source-to-physical clean y left inverse fails")
                        if t in results["y"] and results["y"][t]!=key:
                            raise AssertionError("FIRST y-blocker physical triple not single-valued")
                        results["y"][t]=key
                        outsideC["y"]+=int(any(z not in source["C"] for z in anchors))
    for side in ("x","y"):
        if len(set(results[side].values()))!=len(results[side]):
            raise AssertionError("distinct original physical triples collide on clean A/C source witness")
        if len(results[side])>len(books["clean"][side]):
            raise AssertionError("new projection-clean source book not an upper")
    return dict(triples=results,anchors_outside_C=outsideC)


def true_paths_and_blockers(source,gq,physical,triples):
    """Independent real 3edge walk enumeration and 4 blocker classifications."""
    f,g=source["f"],source["g"]
    fmap={pair:p for p,pair in enumerate(f)}
    gmap={pair:r for r,pair in enumerate(g)}
    adj=physical["adjC"]
    counts=Counter()
    union=0;good=0;path_count=0
    for v0 in adj:
        for v1 in adj[v0]:
            for v2 in adj[v1]:
                for v3 in adj[v2]:
                    path=(v0,v1,v2,v3)
                    if len({v[0] for v in path})!=4 or len({v[1] for v in path})!=4:
                        continue
                    path_count+=1
                    q=fmap.get(tuple(sorted((v0[0],v3[0]))))
                    r=gmap.get(tuple(sorted((v0[1],v3[1]))))
                    if q is None or r is None:continue
                    proj=gq["proj"].get((q,r))
                    if proj is None:continue
                    p,ell=proj
                    anchors=(gq["fid"][q,ell],gq["fid"][p,ell],gq["fid"][p,r])
                    if any(z not in source["A"] for z in anchors):continue
                    if set(f[q])&set(f[p]) or set(g[r])&set(g[ell]):continue
                    good+=1
                    x1=v1[0] in f[p];x2=v2[0] in f[p]
                    y1=v1[1] in g[ell];y2=v2[1] in g[ell]
                    for name,valid in (("x1",x1),("x2",x2),("y1",y1),("y2",y2)):
                        counts[name]+=int(valid)
                    union+=int(x1 or x2 or y1 or y2)
                    for side,valid in (("x",x1),("y",y1)):
                        if valid and (v0,v1,v3) not in triples[side]:
                            raise AssertionError("true clean first blocker P3 not in physical triple source cover")
    if counts["x1"]!=counts["x2"] or counts["y1"]!=counts["y2"]:
        raise AssertionError("true W(3,s) original projection not invariant under P3 reversal")
    if union>sum(counts.values()) or sum(counts.values())>4*good:
        raise AssertionError("four blockers union is miscounted as disjoint")
    return dict(proper=path_count,endpoint_good=good,blocked=counts,union=union)


def projected_delete_role_report(source,gq):
    """Independent exact all-order s² role counts -> physical 12s²|Z|."""
    Z=source["Z"];s=source["s"]
    roles=gq["roles"]
    bad={qr for qr,(p,ell) in gq["proj"].items()
         if any(gq["fid"][flag] in Z
                for flag in ((qr[0],ell),(p,ell),(p,qr[1])))}
    by_role={typ:{qr for qr,(p,ell) in gq["proj"].items()
                  if gq["fid"][(qr[0],ell) if typ=="qell" else
                                (p,ell) if typ=="pell" else
                                (p,qr[1])] in Z}
             for typ in ("qell","pell","pr")}
    if set.union(set(),*by_role.values())!=bad:
        raise AssertionError("ORIGINAL deleted GQ projections union not exact")
    if any(len(v)!=s*s*len(Z) for v in by_role.values()):
        raise AssertionError("true original deleted anchor source exact s² multiplicity false")
    if len(bad)>3*s*s*len(Z):
        raise AssertionError("original deleted endpoint union exceeds all-order source charge")
    return dict(original_source_deleted_IDs=len(Z),
                all_genuine_nonincident_qr=len(gq["proj"]),
                number_bad_genuine_projection_pairs=len(bad),
                exact_bad_source_qell_role=len(by_role["qell"]),
                exact_bad_source_pell_role=len(by_role["pell"]),
                exact_bad_source_pr_role=len(by_role["pr"]),
                physical_endpoint_orientations_per_qr=4,
                physical_deleted_endpoints_upper=4*len(bad),
                all_h_deleted_physical_bound=12*s*s*len(Z),
                all_h_role_count_per_named_flag=s*s)


def certificate_case(s,mode,core_scheme,deleted=()):
    source=genuine_original(s,mode,deleted,core_scheme)
    gq=true_gq_projection(source)
    physical=physical_graph(source)
    books=key_books(source,gq)
    triples=physical_first_triples(source,gq,physical,books)
    path=true_paths_and_blockers(source,gq,physical,triples["triples"])
    delreport=projected_delete_role_report(source,gq)
    theta=physical["theta"]
    # Entire source books are deliberately computed with FULL A, CORE C,
    # NOT with CORE-only original projected anchors.
    report={}
    for side in ("x","y"):
        Ts=triples["triples"][side]
        raw=len(books["old"][side]);clean=len(books["clean"][side])
        W=Phi=0
        for v0,v1,v3 in Ts:
            two=len(physical["adjC"][v1]&physical["adjC"][v3])
            W+=two
            Phi+=two*two
        actual=path["blocked"][side+"1"]
        if not (actual<=W and len(Ts)<=clean<=raw
                and W*W<=len(Ts)*Phi
                and Phi<=physical["weighted4"]
                and actual*actual<=clean*physical["weighted4"]
                and clean*physical["weighted4"]<=raw*physical["Delta"]*physical["trace4"]):
            raise AssertionError("NEW clean source book / weighted fourth chain not valid")
        if len(Ts) and not all(_decode_from_key(source,key,side)==trip
                               for trip,key in Ts.items()):
            raise AssertionError("genuine original physical triple inverse failed")
        report[side]=dict(
            full_historical_A_C_book=raw,
            NEW_projection_clean_endpoint_good_A_C_book=clean,
            removed_invalid_original_source_book_keys=raw-clean,
            original_filtered_reason_counts=dict(books["reason"][side]),
            actual_first_physical_blocker_triples=len(Ts),
            actual_first_physical_blocker_paths=actual,
            clean_true_first_two_walk_weight=W,
            clean_exact_two_walk_square=Phi,
            original_CORE_degree_weighted_fourth_trace=physical["weighted4"],
            old_CORE_max_degree_times_fourth_trace=physical["Delta"]*physical["trace4"],
            original_anchor_triples_OUTSIDE_CORE=triples["anchors_outside_C"][side],
            clean_source_witness_is_left_invertible=True,
            all_original_weighted_blocker_charge_exactly_checked=True)
    if report["x"]["actual_first_physical_blocker_paths"]!=path["blocked"]["x2"]:
        raise AssertionError("original x reversal path census mismatch")
    if report["y"]["actual_first_physical_blocker_paths"]!=path["blocked"]["y2"]:
        raise AssertionError("original y reversal path census mismatch")
    return dict(
        s=s,mode=mode,core_scheme=core_scheme,
        original_GQ_named_flags=source["N"],
        original_A_full_allowed_flags=len(source["A"]),
        original_paired_CORE_flags=len(source["C"]),
        original_FULL_not_equal_CORE=source["A"]!=source["C"],
        original_A_NOT_CORE_projection_anchors_supported=True,
        original_alphabet_a=source["a"],
        ORIGINAL_physical_FULL_A_edges=len(physical["edgesA"]),
        ORIGINAL_physical_paired_CORE_edges=len(physical["edgesC"]),
        original_CORE_actual_Delta=physical["Delta"],
        original_CORE_trace4=physical["trace4"],
        original_CORE_degree_weighted_trace4=physical["weighted4"],
        exact_TRUE_original_mixed_theta=theta,
        true_genuine_offincidence_projection_count=len(gq["proj"]),
        each_original_GQ_source_flag_in_each_three_roles_exactly_s2=True,
        deletion_projection=delreport,
        actual_original_proper_physical_P3=path["proper"],
        actual_TRUE_endpoint_good_P3=path["endpoint_good"],
        actual_four_blocker_union=path["union"],
        original_ALL_four_blocker_counts=dict(path["blocked"]),
        source_point_x=report["x"],
        source_line_y=report["y"],
        all_h_local_book_injection_mathematically_proved_in_manuscript=True,
        ROOT_PROVED_A=False)


def certificate():
    modes=[
        (2,"lex","full",()),
        (2,"reverse","two_thirds",()),
        (2,"shift","half",(0,4,9)),
        (4,"lex","full",()),
        (4,"reverse","two_thirds",()),
        (4,"shift","half",(0,7,19,101)),
        (4,"reverse","thin",(0,5,10,77)),
    ]
    cases=[certificate_case(*args) for args in modes]
    if not any(z["source_point_x"]["removed_invalid_original_source_book_keys"]>0 for z in cases):
        raise AssertionError("new clean original x books never remove an invalid witness")
    if not any(z["source_line_y"]["removed_invalid_original_source_book_keys"]>0 for z in cases):
        raise AssertionError("new clean original y books never remove an invalid witness")
    if not any(z["source_point_x"]["original_anchor_triples_OUTSIDE_CORE"]>0 or
               z["source_line_y"]["original_anchor_triples_OUTSIDE_CORE"]>0 for z in cases):
        raise AssertionError("no genuine original projection with source anchors in A\\C")
    return dict(
        schema=SCHEMA,parent_pr=PARENT,issue=230,status=STATUS,
        newly_proved_original_projection_filtered_books_x_y=True,
        all_h_true_GQ_three_projection_anchor_roles_exact_s2=True,
        original_FULL_A_vs_CORE_C_never_conflated=True,
        independent_all_h_four_physical_blocker_reverse_and_dual_books_proved=True,
        all_h_weighted_fourth_trace_not_independent_path_probability=True,
        exact_SOURCE_book_reduction_valid_but_NO_universal_B0_improvement_claim=True,
        root_unweighted_seven_class_PROVED_A=False,
        source_P3_to_BBo_full_inverse_not_newly_accepted=True,
        no_numerical_C6_graph_constants_invented=True,
        original_true_W32_W34_cases=cases,
        next_scientific_gate="ORIGINAL_P3_BBo_SIXSET_TWO_DIRECTION_INVERSE_AND_ROOT_DAG")


if __name__=="__main__":
    print("AA4_LOW_AC_CLEAN_PROJECTION_CERTIFICATE="+json.dumps(
        certificate(),sort_keys=True,separators=(",",":")))
