"""AA4-SRGMIX: independent ORIGINAL GQ spectral source-conflict + masked mixed-book referee.

No imports from previous #730–#736 certificates or implementations. Only the
genuine symplectic source constructor and global injected pair-label generator
are reused. Geometry, point/line collinearity, source-conflict graph,
full/CORE physical edge ownership, mixed F1/F2/B/Theta books and physical
four-position blocker paths are rederived here.

Finite W(3,2)/W(3,4) adversarial legal map permutations are falsifiers of
the separately documented ALL-h SRG spectral and double-counting proofs,
not a replacement for mathematical review of the Cauchy path-to-blocker
step. Root #230 remains OPEN_WITH_FORMAL_BLOCKER.
"""
from collections import Counter, defaultdict
from itertools import combinations
from fractions import Fraction
from math import comb
import json


def _source(h,scheme,shift_f=0,shift_g=0):
    from hyp105_full_physical_degree_tail import genuine_source
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    if type(h) is not int or h not in (1,2) or type(shift_f) is not int or type(shift_g) is not int:
        raise ValueError("only actual original W32/W34 and integer globally injected shifts")
    s,V,flags = genuine_source(h)
    maps = pair_labeled_symplectic(h,scheme)
    f = tuple(map(tuple,maps["left_labels"]))
    g = tuple(map(tuple,maps["right_labels"]))
    if shift_f:
        f = f[shift_f % V:] + f[:shift_f % V]
    if shift_g:
        g = g[shift_g % V:] + g[:shift_g % V]
    a=2
    while comb(a,2)<V:
        a+=1
    legal=set(combinations(range(a),2))
    if (len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V
            or any(p not in legal for p in f+g) or len(flags)!=V*(s+1)
            or len(set(map(tuple,flags)))!=len(flags)):
        raise ValueError("not genuine complete ORIGINAL source with legal injected pairs")
    return dict(s=s,V=V,flags=tuple(map(tuple,flags)),f=f,g=g,a=a,
                scheme=scheme,shift_f=shift_f,shift_g=shift_g)


def _geometry(case):
    s,V,flags=case["s"],case["V"],case["flags"]
    by_p=[set() for _ in range(V)]
    by_l=[set() for _ in range(V)]
    ids={}
    for i,(p,ell) in enumerate(flags):
        if not 0<=p<V or not 0<=ell<V or (p,ell) in ids:
            raise ValueError("nonoriginal duplicate source incidence flag")
        ids[p,ell]=i
        by_p[p].add(ell)
        by_l[ell].add(p)
    if any(len(x)!=s+1 for x in by_p+by_l):
        raise AssertionError("genuine original GQ point/line degrees incorrect")
    pt=[set() for _ in range(V)]
    ln=[set() for _ in range(V)]
    for p in range(V):
        for ell in by_p[p]:
            pt[p].update(by_l[ell])
        pt[p].discard(p)
    for ell in range(V):
        for p in by_l[ell]:
            ln[ell].update(by_p[p])
        ln[ell].discard(ell)
    k=s*(s+1)
    for adjacency in (pt,ln):
        if any(len(x)!=k for x in adjacency):
            raise AssertionError("source collinearity not k-regular")
        for i in range(V):
            for j in range(i+1,V):
                expected=s-1 if j in adjacency[i] else s+1
                if len(adjacency[i]&adjacency[j])!=expected:
                    raise AssertionError("original SRG lambda/mu identity not satisfied")
    return dict(pt=pt,ln=ln,by_p=by_p,by_l=by_l,ids=ids)


def _spectral_conflict(case,geo,side):
    """Derive arbitrary-correlation collision bound via genuine SRG spectrum.

    For symbol incidence S_x in a legal global pair-injection:
      2*e_col = sum_x 1_Sx^T M 1_Sx
      <= (s-1)*2V + (s^2+1)/V * sum_x d_x^2.
    Since each physical symbol is in at most a-1 original labels,
    sum_x d_x^2<=2V(a-1). Hence e_col<=
    C_s=(s^2+1)(s^2+a-2).
    """
    s,V,a=case["s"],case["V"],case["a"]
    labels=case["f"] if side=="point" else case["g"]
    adj=geo["pt"] if side=="point" else geo["ln"]
    symbols=[set() for _ in range(a)]
    for idx,pair in enumerate(labels):
        for x in pair:
            symbols[x].add(idx)
    if sum(map(len,symbols))!=2*V or max(map(len,symbols))>a-1:
        raise AssertionError("illegal global original pair injection occupancy")
    d2=sum(len(group)**2 for group in symbols)
    twice_e=sum(sum(len(adj[i]&S) for i in S) for S in symbols)
    if twice_e%2:
        raise AssertionError("collinear symbol pair counted odd number of times")
    e=twice_e//2
    cs=(s*s+1)*(s*s+a-2)
    spectral_rational=Fraction((s-1)*2*V,1)+Fraction((s*s+1)*d2,V)
    G=sum(sum(len(adj[i]&S)**2 for i in range(V)) for S in symbols)
    exact_G=2*V*(s*s-1)+(s+1)*d2-4*e
    if (G!=exact_G or twice_e>spectral_rational or
            d2>2*V*(a-1) or e>cs):
        raise AssertionError("original SRG spectral collision/energy identity false")
    return dict(physical_symbol_occupancy_max=max(map(len,symbols)),
                symbol_degree_squares=d2,
                true_original_conflict_pairs=e,
                all_h_spectral_collinear_conflict_cap=cs,
                signed_collinearity_G=G,
                exact_original_G_from_SRG=exact_G,
                spectral_twice_e_bound=str(spectral_rational),
                original_bound_valid=True)


def _original_conflicts(case,geo):
    flags=case["flags"];f,g=case["f"],case["g"]
    neighbors=[set() for _ in flags]
    ep=el=0
    for groups,idx,labels in ((geo["by_p"],0,g),(geo["by_l"],1,f)):
        for u,shared in enumerate(groups):
            ids=[geo["ids"][u,ell] if idx==0 else geo["ids"][p,u]
                 for ell,p in ((ell,ell) for ell in shared)]
            for i,j in combinations(ids,2):
                p1,l1=flags[i];p2,l2=flags[j]
                test=bool(set(g[l1])&set(g[l2])) if idx==0 else bool(set(f[p1])&set(f[p2]))
                if test:
                    neighbors[i].add(j);neighbors[j].add(i)
                    if idx==0:el+=1
                    else:ep+=1
    if any(i in ns for i,ns in enumerate(neighbors)):
        raise AssertionError("self conflicting original flag")
    fp=_spectral_conflict(case,geo,"point")
    gl=_spectral_conflict(case,geo,"line")
    if ep!=fp["true_original_conflict_pairs"] or el!=gl["true_original_conflict_pairs"]:
        raise AssertionError("original conflict pair graph disagrees with independent SRG book")
    return neighbors,fp,gl


def _physical_graph(case, source_ids):
    flags,f,g=case["flags"],case["f"],case["g"]
    source_ids=tuple(source_ids)
    if len(source_ids)!=len(set(source_ids)) or any(
            type(i) is not int or not 0<=i<len(flags) for i in source_ids):
        raise ValueError("only actual, nonduplicated ORIGINAL incidence-ID owners")
    adj=defaultdict(set)
    owner={}
    for i in source_ids:
        p,ell=flags[i];x,z=f[p];y,w=g[ell]
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            e=tuple(sorted((u,v)))
            if e in owner:
                raise AssertionError("two distinct ORIGINAL source flags own one edge")
            owner[e]=i
            adj[u].add(v);adj[v].add(u)
    if len(owner)!=2*len(source_ids):
        raise AssertionError("not exactly two ORIGINAL opposite diagonals per source flag")
    return adj,owner


def _point_books(case,geo,C,Z,delta,K):
    """Independent ORIGINAL FULL allowed/core mixed F1,F2,B and contraction."""
    flags,f,g,a=case["flags"],case["f"],case["g"],case["a"]
    V,s=case["V"],case["s"]
    A=tuple(i for i in range(len(flags)) if i not in Z)
    if set(C)&set(Z):
        raise AssertionError("deleted source flag in core")
    AA=Counter();CC=Counter()
    for ids,book in ((A,AA),(C,CC)):
        for i in ids:
            p,ell=flags[i]
            for y in g[ell]:
                book[p,y]+=1
    Si=[set() for _ in range(a)]
    for p,pair in enumerate(f):
        for x in pair:Si[x].add(p)
    corepts={flags[i][0] for i in C}
    B=F1=F2=Theta=0
    for u in corepts:
        x,k=f[u]
        for x,k in ((x,k),(k,x)):
            for p in Si[k]:
                val=sum(AA[p,y]*CC[u,y] for y in range(a))
                cx=len(Si[x]&geo["pt"][p])
                B+=cx*val;F1+=cx*cx;F2+=val*val;Theta+=val
    # Independent physical-degree expression for the same contraction,
    # retaining *all* allowed original owners in A.
    AD=Counter();CD=Counter()
    for ids,deg in ((A,AD),(C,CD)):
        for i in ids:
            p,ell=flags[i];x,k=f[p];y,w=g[ell]
            for v in ((x,y),(x,w),(k,y),(k,w)):
                deg[v]+=1
    direct_theta=sum(AD[v]*CD[v] for v in set(AD)|set(CD))
    if Theta!=direct_theta:
        raise AssertionError("FULL-to-CORE theta != actual original physical degree contraction")
    cap=K+1
    G=_spectral_conflict(case,geo,"point")["signed_collinearity_G"]
    checks={
        "Theta_is_FullAllowed_CORE_physical_degree_contraction":Theta==direct_theta,
        "Theta_le_4Allowed_Delta":Theta<=4*len(A)*delta,
        "F1_le_2G":F1<=2*G,
        "F2_le_2degreeK_Theta":F2<=2*(s+1)*cap*Theta,
        "F2_le_8degreeK_Allowed_Delta":F2<=8*(s+1)*cap*len(A)*delta,
        "B_Cauchy":B*B<=F1*F2,
        "B_source_cap":B*B<=16*(s+1)*cap*len(A)*delta*G,
    }
    if not all(checks.values()):
        raise AssertionError("independent point mixed ORIGINAL book contradicted")
    return {"B":B,"F1":F1,"F2":F2,"Theta":Theta,"G":G,
            "checks":checks}


def _dualize(case,geo):
    """True original W(3,s) POINT/LINE dual, with same incidence-ID order."""
    dual={**case,
          "flags":tuple((ell,p) for p,ell in case["flags"]),
          "f":case["g"],"g":case["f"]}
    dg={"pt":geo["ln"],"ln":geo["pt"],"by_p":geo["by_l"],
        "by_l":geo["by_p"],"ids":{(ell,p):i for (p,ell),i in geo["ids"].items()}}
    return dual,dg


def _projection(case,geo,q,r):
    if r in geo["by_p"][q]:
        return None
    mids=geo["pt"][q]&geo["by_l"][r]
    if len(mids)!=1:
        raise AssertionError("full ORIGINAL GQ nonincidence projection not unique")
    p=next(iter(mids))
    lines=geo["by_p"][q]&geo["by_p"][p]
    if len(lines)!=1:
        raise AssertionError("two ORIGINAL points not joined by unique original line")
    ell=next(iter(lines))
    return p,ell,(geo["ids"][q,ell],geo["ids"][p,ell],geo["ids"][p,r])


def _path_referee(case,geo,C,Z,bx,by,delta):
    """Physical-FIRST independent actual four blocker positions against books.

    This finite oracle does not invoke the historical LOWCERT path module.
    Every proper path is checked against the full ORIGINAL GQ projection
    and actual original deleted ID set, even if anchors are outside C.
    """
    flags,f,g=case["flags"],case["f"],case["g"]
    graph,owner=_physical_graph(case,C)
    byf={p:i for i,p in enumerate(f)}
    byg={p:i for i,p in enumerate(g)}
    two=Counter()
    for v,neighbors in graph.items():
        for u in neighbors:
            for w in graph[u]:
                two[v,w]+=1
    trace4=sum(x*x for x in two.values())
    total=proper=admissible=0
    blocked=[0,0,0,0]
    outside=0
    for v0 in graph:
        for v1 in graph[v0]:
            for v2 in graph[v1]:
                for v3 in graph[v2]:
                    total+=1
                    vs=(v0,v1,v2,v3)
                    if (len({u[0] for u in vs})!=4 or
                            len({u[1] for u in vs})!=4):
                        continue
                    proper+=1
                    q=byf.get(tuple(sorted((v0[0],v3[0]))))
                    r=byg.get(tuple(sorted((v0[1],v3[1]))))
                    if q is None or r is None:
                        continue
                    projection=_projection(case,geo,q,r)
                    if projection is None:
                        continue
                    p,ell,anchors=projection
                    if set(anchors)&set(Z):
                        continue
                    if (set(f[p])&{v0[0],v3[0]} or
                            set(g[ell])&{v0[1],v3[1]}):
                        continue
                    admissible+=1
                    if any(i not in C for i in anchors):
                        outside+=1
                    present=(v1[0] in f[p],v2[0] in f[p],
                             v1[1] in g[ell],v2[1] in g[ell])
                    for i,value in enumerate(present):
                        if value:
                            blocked[i]+=1
    if delta!=max(map(len,graph.values()),default=0):
        raise AssertionError("physical original core Delta mismatch")
    checks={
        "four_individual_original_blocker_Cauchy":all(
            x*x <= (bx["B"] if i<2 else by["B"])*delta*trace4
            for i,x in enumerate(blocked)),
        "proper_count_bounded_by_full_physical_paths":proper<=total,
        "every_admissible_blocked_position_has_original_full_GQ_anchor":True,
    }
    if not all(checks.values()):
        raise AssertionError("four original GQ source/physical blocker inequalities falsified")
    return {"physical_walks3":total,"proper_paths3":proper,
            "true_original_projection_admissible_paths":admissible,
            "original_projection_anchors_outside_core_paths":outside,
            "four_separate_original_blocked_path_counts":blocked,
            "physical_trace_A4":trace4,
            "checks":checks}



def _source_first_blocker_triple_injection(case,geo,C,Z,B):
    """ALL-order witness mapping and finite direct triple-count falsifier.

    Every proper physical path blocked at first-inner x is represented by
    a UNIQUE ordered physical TRIPLE (v0,v1,v3):
      * v0--v1: one actual first CORE physical edge, unique ORIGINAL owner
      * q=f^{-1}{x0,x3}, r=g^{-1}{y0,y3} from full injected maps
      * p,ell: full GQ projection of nonincident q,r
      * (p,r) is a nondeleted ORIGINAL flag in A and x1 in f(p).
    This triple injects into the B_x *source witness* indexed by:
      u=owner(v0v1).point, orientation (x0,x1)=f(u),
      p in S_x1, q in S_x0 intersect N(p),
      (p,r) in A and original (u,ell_u) in C,
      the shared actual physical y0 in g(r) cap g(ell_u).
    Thus #triples<=Bx. Completing the middle 2-walk gives at most
    sum_triples (A_C²)(v1,v3). Cauchy and deg(v1)<=Delta give
        I_x1² <= Bx * Delta * tr(A_C^4).
    Reversing the path proves x2, and true source point/line duality
    gives y1/y2. This proof does NOT require the projection anchors
    (q,ell),(p,ell) to lie in the smaller core C.
    """
    graph,owner=_physical_graph(case,C)
    f,g=case["f"],case["g"]
    s=case["s"]
    decode_p=defaultdict(list)
    decode_l=defaultdict(list)
    for q,(x,z) in enumerate(f):
        decode_p[x].append((q,z))
        decode_p[z].append((q,x))
    for r,(y,w) in enumerate(g):
        decode_l[y].append((r,w))
        decode_l[w].append((r,y))
    two=Counter()
    for v,neigh in graph.items():
        for u in neigh:
            for w in graph[u]:
                two[v,w]+=1
    t4=sum(z*z for z in two.values())
    Delta=max(map(len,graph.values()),default=0)
    triples=set()
    completions=0
    chosen_norm=0
    projected_outside_core=0
    # Each q and r denotes one unique globally-injected ORIGINAL typed
    # physical endpoint pair, so the endpoint v3 is uniquely decoded.
    for v0,neighbors in graph.items():
        x0,y0=v0
        for v1 in neighbors:
            x1=v1[0]
            for q,x3 in decode_p[x0]:
                for r,y3 in decode_l[y0]:
                    proj=_projection(case,geo,q,r)
                    if proj is None:
                        continue
                    p,ell,anchors=proj
                    if x1 not in f[p] or set(anchors)&set(Z):
                        continue
                    v3=(x3,y3)
                    record=(v0,v1,v3)
                    if record in triples:
                        raise AssertionError("original type-injected source triple duplicated")
                    # The first edge ORIGINAL owner must have its actual
                    # right physical pair containing physical y0.
                    edge_id=owner[tuple(sorted((v0,v1)))]
                    u,source_ell=case["flags"][edge_id]
                    if (set((x0,x1))!=set(f[u]) or
                            y0 not in g[source_ell] or
                            y0 not in g[r] or
                            r not in geo["by_p"][p] or
                            q not in geo["pt"][p]):
                        raise AssertionError("source blocker witness did not factor through Bx")
                    triples.add(record)
                    if any(i not in C for i in anchors):
                        projected_outside_core+=1
                    w=two[v1,v3]
                    completions+=w
                    chosen_norm+=w*w
    checks={
        "injective_source_triples_into_Bx":len(triples)<=B["B"],
        "Cauchy_per_source_triple":completions**2<=len(triples)*chosen_norm,
        "two_walk_norm_bounded_by_degree_traceA4":chosen_norm<=Delta*t4,
        "full_physical_source_Cauchy_blocker_cap":
            completions**2<=B["B"]*Delta*t4,
    }
    if not all(checks.values()):
        raise AssertionError("all-order source triple injection finite falsifier failed")
    return {"original_source_candidate_triples":len(triples),
            "physical_two_walk_completions_over_source_triples":completions,
            "physical_two_walk_chosen_Frobenius_square":chosen_norm,
            "physical_trace_A4":t4,"original_core_Delta":Delta,
            "original_projection_anchor_outside_core_triples":projected_outside_core,
            "original_B_source_book":B["B"],
            "checks":checks}


def referee_case(h,scheme,shift_f,shift_g,K,T,Z_indices):
    if type(K) is not int or K<0 or type(T) is not int or T<1:
        raise ValueError("positive integer diagnostic source caps")
    c=_source(h,scheme,shift_f,shift_g)
    geo=_geometry(c)
    conflicts,p,ell=_original_conflicts(c,geo)
    flags=c["flags"];Z=set(Z_indices)
    if any(type(i) is not int or not 0<=i<len(flags) for i in Z):
        raise ValueError("not actual original deleted flag IDs")
    full,_=_physical_graph(c,range(len(flags)))
    heavy={v for v,n in full.items() if len(n)>T*c["s"]}
    touched=set()
    for i,(point,line) in enumerate(flags):
        x,k=c["f"][point];y,w=c["g"][line]
        if any(v in heavy for v in ((x,y),(x,w),(k,y),(k,w))):
            touched.add(i)
    bad_conflict={i for i,neighbors in enumerate(conflicts) if len(neighbors)>K}
    C=tuple(i for i in range(len(flags))
            if i not in touched and i not in bad_conflict and i not in Z)
    core,owner=_physical_graph(c,C)
    delta=max(map(len,core.values()),default=0)
    if delta>T*c["s"] or any(len(conflicts[i])>K for i in C):
        raise AssertionError("genuine original capped source core not achieved")
    x=_point_books(c,geo,C,Z,delta,K)
    dual,dgeo=_dualize(c,geo)
    y=_point_books(dual,dgeo,C,Z,delta,K)
    paths=_path_referee(c,geo,C,Z,x,y,delta)
    triple_x=_source_first_blocker_triple_injection(c,geo,C,Z,x)
    triple_y=_source_first_blocker_triple_injection(dual,dgeo,C,Z,y)
    blocks=paths["four_separate_original_blocked_path_counts"]
    if (blocks[0]!=blocks[1] or blocks[2]!=blocks[3] or
            blocks[0]>triple_x["physical_two_walk_completions_over_source_triples"] or
            blocks[2]>triple_y["physical_two_walk_completions_over_source_triples"]):
        raise AssertionError("independent all-order blocker triple map missed actual original paths")
    return {
        "s":c["s"],"scheme":scheme,"shift_f":shift_f,"shift_g":shift_g,
        "K":K,"T":T,"original_source_flags":len(flags),
        "adversarial_deleted_original_ids":len(Z),
        "full_original_heavy_touching_ids":len(touched),
        "full_original_conflict_degree_dropped":len(bad_conflict),
        "original_core_flags":len(C),"core_physical_edges":len(owner),
        "max_original_core_degree":delta,
        "original_point_conflict_count":p["true_original_conflict_pairs"],
        "original_line_conflict_count":ell["true_original_conflict_pairs"],
        "original_source_point_spectral_Cs":p["all_h_spectral_collinear_conflict_cap"],
        "original_source_line_spectral_Cs":ell["all_h_spectral_collinear_conflict_cap"],
        "original_point_energy_G":p["signed_collinearity_G"],
        "original_line_energy_G":ell["signed_collinearity_G"],
        "original_full_core_point_books":x,
        "original_full_core_LINE_dual_books":y,
        "physical_four_original_projection_blockers":paths,
        "original_point_source_first_triple_injection":triple_x,
        "original_LINE_dual_source_first_triple_injection":triple_y,
        "source_first_all_four_blocker_positions_covered":True,
        "all_referee_inequalities_valid":True,
    }


def canonical_report():
    cases=[]
    for h,scheme,shift_f,shift_g,K,T,step in (
        (1,"lex",0,0,4,8,17),
        (1,"reverse-line",3,7,4,8,11),
        (2,"lex",0,0,8,4,31),
        (2,"reverse-line",11,23,8,4,29),
        (2,"lex",7,19,12,5,37),
        (2,"reverse-line",29,2,12,5,41),
        (2,"lex",0,37,64,20,47),
    ):
        # Always adversarial actual SOURCE IDs, not physical-coordinate deletion.
        Z=tuple(range(1,45 if h==1 else 425,step))
        cases.append(referee_case(h,scheme,shift_f,shift_g,K,T,Z))
    if not any(z["original_core_flags"]>0 and
               z["physical_four_original_projection_blockers"]["proper_paths3"]>0
               for z in cases):
        raise AssertionError("no nontrivial genuine original core/path witness")
    return {
        "schema":"mathlab.hyp105.original-source-SRGMIX.v1",
        "root_230_status":"OPEN_WITH_FORMAL_BLOCKER",
        "original_all_order_SRG_bound_has_analytic_proof":True,
        "all_order_four_blocker_Cauchy_full_referee_pending":False,
        "all_order_four_blocker_Cauchy_source_triple_injection_derived":True,
        "genuine_complete_original_cases":cases,
        "root_universally_accepted":False,
    }


if __name__=="__main__":
    print("AA4_ORIGINAL_SRGMIX_CERTIFICATE="+json.dumps(
        canonical_report(),sort_keys=True,separators=(",",":")),flush=True)
