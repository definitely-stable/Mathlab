"""AA4-LOW-FORMAL: original source-book witness injection and weighted blocker.

The mathematical local theorem is valid for ANY finite typed incidence system
and ANY partial single-valued 3-anchor projection (not just W(3,s)).
No heavy/low/root certificate evaluator is imported. W32/W34 tests reuse only
an independently generated original symplectic incidence fixture.

Z, A and C are ORIGINAL named flag-ID sets. Every physical original flag
owns TWO opposite diagonals. Complete fixed f/g pair injections are mandatory.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from fractions import Fraction
import json

SCHEMA = "mathlab.hyp105.original-low-formal-weighted-source-witness.v1"
ROOT_STATUS = "OPEN_WITH_FORMAL_BLOCKER"


def minimal_labels(n):
    if type(n) is not int or n < 2:
        raise ValueError("at least two typed original factors required")
    a = 2
    while a*(a-1)//2 < n:
        a += 1
    return a, tuple(combinations(range(a), 2))[:n]


def _edge(u, v):
    if u == v:
        raise ValueError("original physical diagonals cannot be loops")
    return tuple(sorted((u, v)))


def _other(pair, contained):
    if contained == pair[0]:
        return pair[1]
    if contained == pair[1]:
        return pair[0]
    raise AssertionError("physical source witness symbol not in unique factor pair")


def source_model(flags, f, g, *, require_GQ=False):
    """Independently construct a finite typed ORIGINAL flag source."""
    flags = tuple(map(tuple, flags))
    f = tuple(map(tuple, f))
    g = tuple(map(tuple, g))
    if not f or not g or len(set(flags)) != len(flags):
        raise ValueError("duplicate or empty original incidence source")
    if len(set(f)) != len(f) or len(set(g)) != len(g):
        raise ValueError("pair labeling must be separately globally injective")
    a = max((v for pair in f+g for v in pair), default=-1)+1
    if a < 2 or any(len(pair)!=2 or pair[0]>=pair[1] or pair[0]<0 or
                     pair[1]>=a for pair in f+g):
        raise ValueError("physical labels must be distinct canonical pairs")
    flagid = {}
    bp = defaultdict(list)
    bl = defaultdict(list)
    for i, (p, l) in enumerate(flags):
        if not 0<=p<len(f) or not 0<=l<len(g):
            raise ValueError("invalid point/line named ORIGINAL flag")
        flagid[p,l] = i
        bp[p].append(i)
        bl[l].append(i)
    np = [set() for _ in f]
    nl = [set() for _ in g]
    for l, ids in bl.items():
        for i,j in combinations(ids,2):
            p,q=flags[i][0],flags[j][0]
            np[p].add(q)
            np[q].add(p)
    for p, ids in bp.items():
        for i,j in combinations(ids,2):
            l,r=flags[i][1],flags[j][1]
            nl[l].add(r)
            nl[r].add(l)
    proj={}
    multiple=0
    for q in range(len(f)):
        for r in range(len(g)):
            if (q,r) in flagid:
                continue
            triples=[]
            for ir in bl[r]:
                p=flags[ir][0]
                for iq in bp[q]:
                    ell=flags[iq][1]
                    if (p,ell) in flagid and p!=q:
                        triples.append((p,ell))
            if require_GQ and len(triples)!=1:
                raise AssertionError("true original generalized quadrangle lost unique projection")
            if len(triples)>1:
                multiple+=1
            if triples:
                # For a generic incidence system use a fixed SINGLE projection;
                # no ambiguous multivalued choice can enter the witness theorem.
                proj[q,r] = min(triples)
    return dict(flags=flags, f=f, g=g, a=a, flagid=flagid, byp=bp, byl=bl,
                p_neighbors=np, l_neighbors=nl, projection=proj,
                competing_abstract_projections=multiple, strict_GQ=require_GQ)


def _physical_edges(m, ids):
    edges={}
    for i in sorted(ids):
        p,l=m["flags"][i]
        x0,x1=m["f"][p]
        y0,y1=m["g"][l]
        for u,v in (((x0,y0),(x1,y1)),((x0,y1),(x1,y0))):
            e=_edge(u,v)
            if e in edges:
                raise AssertionError("physical edge has two original flag owners")
            edges[e]=i
    if len(edges)!=2*len(ids):
        raise AssertionError("a retained ORIGINAL flag lost one of its paired diagonals")
    return edges


def _neighbors(edges):
    adj=defaultdict(set)
    for u,v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def _book_source_keys(m, A, C, side):
    """Literal source witness expansion, with ALL original source IDs.

    Each book term is named by projected collinear q/r, projected allowed
    original flag and first-core original flag, plus the shared symbol.
    """
    f,g,flags=m["f"],m["g"],m["flags"]
    bypA=defaultdict(list)
    bylA=defaultdict(list)
    bypC=defaultdict(list)
    bylC=defaultdict(list)
    for i in A:
        p,l=flags[i]
        bypA[p].append(i)
        bylA[l].append(i)
    for i in C:
        p,l=flags[i]
        bypC[p].append(i)
        bylC[l].append(i)
    keys=set()
    if side=="x":
        inv=defaultdict(list)
        for p,pair in enumerate(f):
            for k in pair: inv[k].append(p)
        for u, retained_ids in bypC.items():
            for x,k in ((f[u][0],f[u][1]),(f[u][1],f[u][0])):
                for p in inv[k]:
                    for q in m["p_neighbors"][p]:
                        if x not in f[q]:
                            continue
                        for first in retained_ids:
                            ell_u=flags[first][1]
                            for projected in bypA[p]:
                                r=flags[projected][1]
                                for y in set(g[ell_u])&set(g[r]):
                                    keys.add((u,ell_u,x,k,p,q,r,y))
    elif side=="y":
        inv=defaultdict(list)
        for l,pair in enumerate(g):
            for k in pair: inv[k].append(l)
        for u, retained_ids in bylC.items():
            for y,k in ((g[u][0],g[u][1]),(g[u][1],g[u][0])):
                for ell in inv[k]:
                    for r in m["l_neighbors"][ell]:
                        if y not in g[r]:
                            continue
                        for first in retained_ids:
                            p_u=flags[first][0]
                            for projected in bylA[ell]:
                                q=flags[projected][0]
                                for x in set(f[p_u])&set(f[q]):
                                    keys.add((u,p_u,y,k,ell,r,q,x))
    else:
        raise ValueError("only x or y physical source")
    return keys


def _book_contraction(m,A,C,side):
    """Independent multiplicity sum using c_x and K_AC, no source-key calls."""
    f,g,flags=m["f"],m["g"],m["flags"]
    if side=="x":
        outer,inner=f,g
        by_outer=m["byp"]
        neighbors=m["p_neighbors"]
        first_idx, second_idx=0,1
    elif side=="y":
        outer,inner=g,f
        by_outer=m["byl"]
        neighbors=m["l_neighbors"]
        first_idx, second_idx=1,0
    else:
        raise ValueError("unknown factor")
    inv=defaultdict(list)
    for i, pair in enumerate(outer):
        for k in pair: inv[k].append(i)
    R_A=Counter()
    R_C=Counter()
    active=set()
    for j, (p,l) in enumerate(flags):
        o=(p,l)[first_idx]
        t=(p,l)[second_idx]
        for y in inner[t]:
            if j in A: R_A[o,y]+=1
            if j in C:
                R_C[o,y]+=1
                active.add(o)
    B=Theta=F1=F2=0
    for u in active:
        for x,k in ((outer[u][0],outer[u][1]),(outer[u][1],outer[u][0])):
            for p in inv[k]:
                c=sum(1 for q in neighbors[p] if x in outer[q])
                Kac=sum(R_A[p,y]*R_C[u,y] for y in range(m["a"]))
                B+=c*Kac
                Theta+=Kac
                F1+=c*c
                F2+=Kac*Kac
    if B*B>F1*F2:
        raise AssertionError("original mixed source book Cauchy inequality")
    return dict(B=B,Theta=Theta,F1=F1,F2=F2,
                source_Kmax=max((R_C[u,y] for u in active
                                 for y in range(m["a"])),default=0))


def _source_witness_triples(m,A,C,edge_C,book_keys,side):
    """ALL physical edge-first triples and their explicitly inverted keys."""
    f,g=m["f"],m["g"]
    fx=defaultdict(list)
    gy=defaultdict(list)
    for q,pair in enumerate(f):
        for x in pair: fx[x].append(q)
    for r,pair in enumerate(g):
        for y in pair: gy[y].append(r)
    result={}
    for edge,owner in edge_C.items():
        u,ell_u=m["flags"][owner]
        for v0,v1 in (edge,(edge[1],edge[0])):
            x0,y0=v0
            x1,y1=v1
            for q in fx[x0]:
                x3=_other(f[q],x0)
                for r in gy[y0]:
                    y3=_other(g[r],y0)
                    projection=m["projection"].get((q,r))
                    if projection is None:
                        continue
                    p,ell=projection
                    if any(m["flagid"][(pp,ll)] not in A
                           for pp,ll in ((q,ell),(p,ell),(p,r))):
                        continue
                    # deliberately NO endpoint-good, interior propriety or
                    # second core walk is required for a SOURCE triple.
                    if side=="x":
                        if x1 not in f[p]:
                            continue
                        key=(u,ell_u,x0,x1,p,q,r,y0)
                        rebuilt=((x0,y0),
                                 (x1,_other(g[ell_u],y0)),
                                 (_other(f[q],x0),_other(g[r],y0)))
                    elif side=="y":
                        if y1 not in g[ell]:
                            continue
                        key=(ell_u,u,y0,y1,ell,r,q,x0)
                        rebuilt=((x0,y0),
                                 (_other(f[u],x0),y1),
                                 (_other(f[q],x0),_other(g[r],y0)))
                    else:
                        raise ValueError("factor")
                    triple=(v0,v1,(x3,y3))
                    if rebuilt!=triple:
                        raise AssertionError("physical triple cannot be inverted from original source witness")
                    if key not in book_keys:
                        raise AssertionError("physical blocker triple has no FULL/CORE original source-book witness")
                    if triple in result and result[triple]!=key:
                        raise AssertionError("noninjective physical triple-to-original witness")
                    result[triple]=key
    if len(set(result.values()))!=len(result):
        raise AssertionError("two physical triples collide in one source-book witness")
    return result


def _physical_moments(m,edge_A,edge_C):
    adjA=_neighbors(edge_A)
    adjC=_neighbors(edge_C)
    vertices=list(product(range(m["a"]),repeat=2))
    degree=lambda v:len(adjC[v])
    t4=weighted4=0
    for v in vertices:
        dv=degree(v)
        for w in vertices:
            two=len(adjC[v]&adjC[w])
            t4+=two*two
            weighted4+=dv*two*two
    Delta=max((degree(v) for v in vertices),default=0)
    theta=sum(len(adjA[v])*len(adjC[v]) for v in vertices)
    assert weighted4<=Delta*t4
    assert theta<=4*len(edge_A)//2*Delta
    return dict(adjC=adjC,Delta=Delta,t4=t4,
                weighted4=weighted4,theta=theta)


def _literal_first_blocks(m,A,adjC):
    """Direct actual ORIGINAL proper P3 census, unrelated to book expansion."""
    f,g=m["f"],m["g"]
    qmap={pair:i for i,pair in enumerate(f)}
    rmap={pair:i for i,pair in enumerate(g)}
    blocked=Counter()
    proper=good=0
    for v0 in adjC:
        for v1 in adjC[v0]:
            for v2 in adjC[v1]:
                for v3 in adjC[v2]:
                    path=(v0,v1,v2,v3)
                    if len({v[0] for v in path})!=4 or len(
                        {v[1] for v in path})!=4:
                        continue
                    proper+=1
                    q=qmap.get(_edge(v0[0],v3[0]))
                    r=rmap.get(_edge(v0[1],v3[1]))
                    if q is None or r is None:
                        continue
                    proj=m["projection"].get((q,r))
                    if proj is None:
                        continue
                    p,ell=proj
                    if any(m["flagid"][(pp,ll)] not in A
                           for pp,ll in ((q,ell),(p,ell),(p,r))):
                        continue
                    if set(f[q]) & set(f[p]) or set(g[r]) & set(g[ell]):
                        continue
                    good+=1
                    blocked["x1"]+=int(v1[0] in f[p])
                    blocked["x2"]+=int(v2[0] in f[p])
                    blocked["y1"]+=int(v1[1] in g[ell])
                    blocked["y2"]+=int(v2[1] in g[ell])
    if blocked["x1"]!=blocked["x2"] or blocked["y1"]!=blocked["y2"]:
        raise AssertionError("true physical reversal fails for ORIGINAL blockers")
    return dict(blocked=blocked,proper=proper,endpoint_good=good)


def witness_certificate(m, *, zmod=None, coremod=5):
    """Fully independent physical/source/weighted certificates on a legal source."""
    if type(coremod)!=int or coremod<2:
        raise ValueError("bad core partition")
    N=len(m["flags"])
    Z={i for i in range(N) if zmod is not None and i%zmod==0}
    A=set(range(N))-Z
    C={i for i in A if i%coremod not in (0,1)}
    if not C or C==A:
        raise AssertionError("must exercise proper paired original CORE")
    edge_A=_physical_edges(m,A)
    edge_C=_physical_edges(m,C)
    moment=_physical_moments(m,edge_A,edge_C)
    bx=_book_source_keys(m,A,C,"x")
    by=_book_source_keys(m,A,C,"y")
    ax=_book_contraction(m,A,C,"x")
    ay=_book_contraction(m,A,C,"y")
    if ax["B"]!=len(bx) or ay["B"]!=len(by):
        raise AssertionError("literal original source book and multiplicity contraction disagree")
    if ax["Theta"]!=moment["theta"] or ay["Theta"]!=moment["theta"]:
        raise AssertionError("FULL/CORE mixed source theta and physical contraction disagree")
    if not ax["B"]>=0 or not ay["B"]>=0:
        raise AssertionError("negative actual source book")
    p3=_literal_first_blocks(m,A,moment["adjC"])
    data={}
    for side,sourcebook,book in (("x",bx,ax),("y",by,ay)):
        triples=_source_witness_triples(m,A,C,edge_C,sourcebook,side)
        T=len(triples)
        W=Phi=0
        for v0,v1,v3 in triples:
            a2=len(moment["adjC"][v1] & moment["adjC"][v3])
            W+=a2
            Phi+=a2*a2
        actual=p3["blocked"][side+"1"]
        if not (0<=actual<=W and T<=book["B"] and
                W*W<=T*Phi<=book["B"]*moment["weighted4"]<=
                book["B"]*moment["Delta"]*moment["t4"]):
            raise AssertionError("exact source-weighted physical blocker inequality failed")
        data[side]=dict(
            genuine_first_blockers=actual,
            original_book_witnesses=book["B"],
            distinct_reconstructible_source_triples=T,
            direct_source_triple_two_walk_weight=W,
            direct_source_triple_two_walk_square=Phi,
            degree_weighted_physical_fourth_trace=moment["weighted4"],
            ordinary_physical_fourth_trace=moment["t4"],
            Delta=moment["Delta"],
            original_source_book_surplus=book["B"]-T,
            exact_source_book_count_verified=True,
            all_source_triples_have_unique_reversible_witness=True,
            physical_path_charging_all_steps_pass=True)
    return dict(
        flags=N,deleted_original_Z=len(Z),full_allowed_A=len(A),
        paired_original_CORE_C=len(C),A_not_equal_C=C!=A,
        distinct_original_diagonals_full=2*len(A),
        distinct_original_diagonals_core=2*len(C),
        physical_mixed_degree_theta=moment["theta"],
        point_source_book_theta=ax["Theta"],
        line_source_book_theta=ay["Theta"],
        proper_original_P3=p3["proper"],
        endpoint_good_original_P3=p3["endpoint_good"],
        original_first_equals_last_by_reversal=True,
        x=data["x"], y=data["y"],
        original_source_projection_single_valued=True,
        abstract_nonGQ_projection_competitions=m["competing_abstract_projections"],
    )


def true_original_case(s,mode,zmod=None):
    from hyp105_original_defect_factor_referee import genuine_symplectic_source
    flags=genuine_symplectic_source(s)
    V=(s+1)*(s*s+1)
    a,pairs=minimal_labels(V)
    f=pairs
    if mode=="lex":
        g=pairs
    elif mode=="reverse":
        g=tuple(reversed(pairs))
    elif mode=="shift":
        g=tuple(pairs[(i*7+3)%V] for i in range(V)) if V%7 else tuple(
            pairs[(i+1)%V] for i in range(V))
    else:
        raise ValueError("unrecognized fixed label adversary")
    m=source_model(flags,f,g,require_GQ=True)
    c=witness_certificate(m,zmod=zmod)
    c.update(s=s,mode=mode,genuine_symplectic_W3s=True,
             canonical_original_flags=len(flags),
             original_label_alphabet=a)
    return c


def abstract_adversarial_case(seed):
    """Finite NON-GQ bipartite incidence redteam for the general local lemma."""
    if type(seed)!=int or seed not in (1,2,3):
        raise ValueError("known adversarial fixtures only")
    n=5
    a,pairs=minimal_labels(n)
    f=pairs
    g=tuple(pairs[(i*2+seed)%n] for i in range(n))
    flags=tuple((p,l) for p in range(n) for l in range(n)
                if (p+2*l+seed)%4!=0)
    m=source_model(flags,f,g,require_GQ=False)
    c=witness_certificate(m,zmod=5 if seed!=3 else None,coremod=3)
    c.update(seed=seed,strict_GQ=False,
             source_projection_is_canonical_single_valued=True)
    return c


def certificate():
    cases=[true_original_case(2,"lex",None),
           true_original_case(2,"reverse",7),
           true_original_case(4,"lex",None),
           true_original_case(4,"reverse",17),
           true_original_case(4,"shift",None)]
    adversarial=[abstract_adversarial_case(i) for i in (1,2,3)]
    assert any(c["x"]["genuine_first_blockers"]>0
               or c["y"]["genuine_first_blockers"]>0 for c in cases)
    assert all(c["x"]["physical_path_charging_all_steps_pass"] and
               c["y"]["physical_path_charging_all_steps_pass"]
               for c in cases+adversarial)
    return {
        "schema":SCHEMA,"issue":230,"parent_pr":769,
        "status":ROOT_STATUS,
        "all_h_source_witness_proof_in_manuscript":True,
        "all_h_general_typed_incidence_local_extension_proved_in_manuscript":True,
        "all_h_weighted_fourth_trace_bound_proved_in_manuscript":True,
        "all_h_any_original_Z_and_C_subset_A_in_local_theorem":True,
        "all_h_GQ_spectral_and_ROOT_dependencies_not_accepted_by_this_code":True,
        "true_original_W32_W34_correlated_fixed_map_cases":cases,
        "non_GQ_partial_projection_falsifier_cases":adversarial,
        "root_PROVED_A":False,
        "all_h_B75_proved":False,
        "general_ASET_exponent_claimed":False
    }


if __name__=="__main__":
    print("AA4_LOW_FORMAL_WEIGHTED_CERTIFICATE="+json.dumps(
        certificate(),sort_keys=True,separators=(",",":")))
