"""GIO-003 G6-C2: FULL-A/CORE-C mixed books, partial projection inverse.

Works on ANY simple (s,t)-biregular girth>=8 source, without a GQ
witness or full projection completeness. Uses G6-C1 on stacked base.
This is a proof of local A5/A6 and endpoint A3 gates; NOT full T3.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb
from pathlib import Path
import argparse
import json

from gio_t3c_intrinsic_defect import (
    source_graph, typed_maps, doubled_gq, defect_matrices,
    typed_conflicts_and_gram, coarse_linear_excess_ledger,
)
from gio_generalized_gq import geometry
from hyp105_aa4_branch_a_integrated_referee import (
    actual_edges, historical_bbo, source_bbo_inverse, physical_d6,
)
from gio_resilience import physical_bbo, source_first_bbo, anchor_ids

SCHEMA="mathlab.gio003.g6c2.partial-book-inverse.v1"
PARENT_G6C1="8932e4c76c2d04c3e1c15f7f56f15a50a7d8f918"


def make_model(name="W32",scheme="lex"):
    if name in ("doubleW32","switchedDoubleW32"):
        lines,P,s,t=doubled_gq("W32",name=="switchedDoubleW32")
    else:
        g=geometry(name)
        lines,s,t=g["lines"],g["s"],g["t"]
        P=(s+1)*(s*t+1)
    m=source_graph(lines,P,s,t)
    z=typed_maps(m,scheme)
    projections={}
    for (q,r),anchor in m["projected"].items():
        assert anchor[0][0]==q and anchor[2][1]==r
        projections[q,r]=(anchor[1][0],anchor[1][1])
    flags=m["flags"]
    old=dict(m,**z,projection=projections,
             flag_to_id={flag:i for i,flag in enumerate(flags)})
    assert len(old["flag_to_id"])==len(flags)
    return old


def selected_mask(m,which):
    full=frozenset(range(len(m["flags"])))
    if which=="full":
        return full,full
    if which=="delete":
        deleted=set(range(0,len(full),11))
        A=full-deleted
        return frozenset(A),frozenset(A)
    if which=="mixed":
        deleted=set(range(0,len(full),13))
        A=full-deleted
        C=A-{i for i in A if i%5==0}
        return frozenset(A),frozenset(C)
    if which=="empty_core":
        return full,frozenset()
    if which=="delete_anchors":
        # Removes source flags, not factors or newly recomputed projections.
        A=full-{0,1}
        return frozenset(A),frozenset(A-{2,3})
    raise ValueError("unknown deterministic adversarial mask")


def point_neighbors(m):
    return m["neighbors_point"]


def original_source_conflict_degrees(m,C):
    """Literal original owner J_C, independently from physical H_C."""
    fs=m["flags"]
    by_point=defaultdict(list);by_line=defaultdict(list)
    for i in C:
        p,l=fs[i]
        by_point[p].append(i)
        by_line[l].append(i)
    d=Counter({i:0 for i in C})
    conflicts=set()
    for p,items in by_point.items():
        for a,b in combinations(items,2):
            l1,l2=fs[a][1],fs[b][1]
            if set(m["g"][l1]) & set(m["g"][l2]):
                conflicts.add((min(a,b),max(a,b)))
    for l,items in by_line.items():
        for a,b in combinations(items,2):
            p1,p2=fs[a][0],fs[b][0]
            if set(m["f"][p1]) & set(m["f"][p2]):
                conflicts.add((min(a,b),max(a,b)))
    for a,b in conflicts:
        d[a]+=1;d[b]+=1
    return d,max(d.values(),default=0),len(conflicts)


def full_core_book(m,A,C,side="point"):
    """Exact original FULL/CORE book B, two Cauchy factors, source Gram.

    C subset A subset original flag IDs; the full side MUST be A, not C.
    For line-side book, swap original typed source factors and dual
    collinearity graph independently, preserving the old full flag set.
    """
    if not set(C)<=set(A):
        raise ValueError("CORE must be a subset of available original flags")
    if side not in ("point","line"):
        raise ValueError("two typed factor sides only")
    fs=m["flags"]
    if side=="point":
        factors=m["f"];other=m["g"]
        V=m["points"];degree=m["t"]+1
        neighbors=m["neighbors_point"]
        flag_coordinates=lambda i:fs[i]
    else:
        factors=m["g"];other=m["f"]
        V=len(m["lines"]);degree=m["s"]+1
        neighbors=m["neighbors_line"]
        flag_coordinates=lambda i:fs[i][::-1]

    RA=defaultdict(int);RC=defaultdict(int)
    for i in A:
        p,l=flag_coordinates(i)
        for y in other[l]:
            RA[p,y]+=1
    for i in C:
        p,l=flag_coordinates(i)
        for y in other[l]:
            RC[p,y]+=1
    d, K, eJ=original_source_conflict_degrees(m,C)
    for n in RC.values():
        assert n<=K+1
    for p in range(V):
        assert sum(RA[p,y] for y in range(max(max(z) for z in other)+1))<=2*degree

    by_symbol=defaultdict(set)
    for p,pair in enumerate(factors):
        for x in pair:
            by_symbol[x].add(p)
    c={}
    for p in range(V):
        for x in by_symbol:
            c[p,x]=len(neighbors[p] & by_symbol[x])
    G=sum(n*n for n in c.values())
    assert G==sum(sum(len(neighbors[p]&by_symbol[x])**2 for p in range(V))
                  for x in by_symbol)
    # Construct a literal book, including the multiplicity of FULL-A and
    # CORE-C flag choices under a shared other-factor symbol.
    Aflags=defaultdict(list);Cflags=defaultdict(list)
    for i in A:
        p,l=flag_coordinates(i)
        for y in other[l]:
            Aflags[p,y].append(i)
    for i in C:
        p,l=flag_coordinates(i)
        for y in other[l]:
            Cflags[p,y].append(i)
    index=[]; book_count=0; F1=0; F2=0; sumK=0
    concrete_book_keys=set()
    for j in range(V):
        a,b=factors[j]
        for x,k in ((a,b),(b,a)):
            for p in by_symbol[k]:
                y_common={y for jj,y in Cflags if jj==j}
                Ky=sum(len(Aflags.get((p,y),()))*len(Cflags[j,y])
                       for y in y_common)
                cx=c[p,x]
                index.append((j,x,k,p,Ky,cx))
                F1+=cx*cx
                F2+=Ky*Ky
                sumK+=Ky
                book_count+=cx*Ky
                if cx*Ky:
                    qs=neighbors[p] & by_symbol[x]
                    for y in y_common:
                        for a_flag in Aflags.get((p,y),()):
                            for c_flag in Cflags[j,y]:
                                for q in qs:
                                    key=(j,x,k,p,q,a_flag,c_flag,y)
                                    assert key not in concrete_book_keys
                                    concrete_book_keys.add(key)
    assert len(concrete_book_keys)==book_count
    assert F1<=2*G
    boundK=2*degree*(K+1)
    assert all(z[4]<=boundK for z in index)
    assert F2<=boundK*sumK
    H,_=actual_edges(m,A)
    HC,_=actual_edges(m,C)
    theta=sum(len(H.get(v,()))*len(HC.get(v,())) for v in set(H)|set(HC))
    assert theta==sumK
    Delta=max(map(len,HC.values()),default=0)
    assert theta<=4*len(A)*Delta
    assert book_count**2<=F1*F2
    bound=16*degree*(K+1)*len(A)*Delta*G
    assert book_count**2<=bound
    return dict(side=side,N_full=len(A),N_core=len(C),
                max_J_core_degree=K,edges_J_core=eJ,
                physical_max_degree_core=Delta,
                source_full_core_theta=theta,source_book=B_to_int(book_count),
                book_term_count=len(concrete_book_keys),
                F1=F1,F2=F2,G=G,
                exact_F1_le_2G=True,
                exact_F2_le_2degree_K_Theta=True,
                exact_theta_equals_product_degrees=True,
                exact_source_book_squared_bound=bound,
                book_keys=concrete_book_keys)


def B_to_int(n):
    assert type(n) is int and n>=0
    return n


def manual_produced_bbo(m,A,C):
    """Physical 3walk census without importing the historical BBo classifier.

    Acceptance uses original surviving unique projections only. Missing
    projections are kept missing; no completion or GQ retrofit occurs.
    """
    if not set(C)<=set(A):
        raise ValueError("CORE not subset of FULL")
    adj,owner=actual_edges(m,C)
    out=defaultdict(set)
    for v0 in sorted(adj):
        for v1 in sorted(adj[v0]):
            for v2 in sorted(adj[v1]):
                for v3 in sorted(adj[v2]):
                    v=(v0,v1,v2,v3)
                    if len({z[0] for z in v})!=4 or len({z[1] for z in v})!=4:
                        continue
                    q=m["point_by_pair"].get(tuple(sorted((v0[0],v3[0]))))
                    r=m["line_by_pair"].get(tuple(sorted((v0[1],v3[1]))))
                    if q is None or r is None:
                        continue
                    if (q,r) not in m["projection"]:
                        continue
                    p,ell=m["projection"][q,r]
                    # Do NOT fetch missing anchors from a GQ completion.
                    aa=(m["flag_to_id"].get((q,ell)),
                        m["flag_to_id"].get((p,ell)),
                        m["flag_to_id"].get((p,r)))
                    if None in aa or not set(aa)<=set(A):
                        continue
                    if set(m["f"][p])&{z[0] for z in v}:
                        continue
                    if set(m["g"][ell])&{z[1] for z in v}:
                        continue
                    resid=tuple(owner[tuple(sorted((x,y)))]
                                for x,y in zip(v,v[1:]))
                    if len(set(resid))!=3:
                        continue
                    ids=aa+resid
                    if len(set(ids))!=6:
                        continue
                    key=tuple(sorted(ids))
                    out[key].add(v)
    for k,paths in out.items():
        assert len(paths)==2 and any(v[::-1] in paths for v in paths)
    return dict(out)


def inverse_certificate(m,A,C):
    """Three independent algorithms for original six-ID aligned BBo."""
    first=manual_produced_bbo(m,A,C)
    published_phys=physical_bbo(m,A,C)
    source=source_first_bbo(m,A,C)
    assert first==published_phys==source
    for k,paths in first.items():
        assert historical_bbo(m,k)
        assert len(k)==6 and len(set(k))==6
        assert set(k)<=A
        assert source_bbo_inverse(m,k)==paths
        assert len(paths)==2 and next(iter(paths))[::-1] in paths
    return dict(original_source_motifs=len(first),
                manual_physical_first_equals_published=True,
                manual_physical_first_equals_source_owner_join=True,
                exact_original_six_ID_nontrivial_inverse=True,
                missing_projections_not_completed=True)


def endpoint_mask(m,A):
    """Independent concrete off-coordinate physical endpoint masks.

    Union decomposition is for FULL original source projections, not for a
    presumed GQ completion; A is deletion-only subset of original flags.
    """
    if not set(A)<=set(range(len(m["flags"]))):
        raise ValueError("only original flags can be kept")
    AP=m["aP"];AL=m["aL"]
    goodP=m["point_by_pair"];goodL=m["line_by_pair"]
    bad=defaultdict(set)
    for x0 in range(AP):
        for x3 in range(AP):
            if x0==x3:
                continue
            qp=goodP.get(tuple(sorted((x0,x3))))
            for y0 in range(AL):
                for y3 in range(AL):
                    if y0==y3:
                        continue
                    pair=((x0,y0),(x3,y3))
                    rl=goodL.get(tuple(sorted((y0,y3))))
                    if qp is None or rl is None:
                        bad["unlabelled"].add(pair)
                    elif (qp,rl) in m["flag_to_id"]:
                        bad["incident"].add(pair)
                    elif (qp,rl) not in m["projection"]:
                        bad["unprojected"].add(pair)
                    else:
                        p,ell=m["projection"][qp,rl]
                        if set(m["f"][qp])&set(m["f"][p]) or set(m["g"][rl])&set(m["g"][ell]):
                            bad["factor_overlap"].add(pair)
                        else:
                            anchor=(m["flag_to_id"][(qp,ell)],
                                    m["flag_to_id"][(p,ell)],
                                    m["flag_to_id"][(p,rl)])
                            if not set(anchor)<=A:
                                bad["deleted_anchors"].add(pair)
    mask=set().union(*(x for x in bad.values()))
    d=len(m["flags"])-len(A)
    vp=m["points"];vl=len(m["lines"])
    MP=comb(AP,2)-vp;ML=comb(AL,2)-vl
    eP=typed_e_col(m,"point")
    eL=typed_e_col(m,"line")
    parts=dict(
       unlabelled=4*(MP*vl+ML*vp+MP*ML),
       incident=4*len(m["flags"]),
       unprojected=4*vp*m["excess_lines"],
       factor_overlap=8*m["t"]*eP+8*m["s"]*eL,
       deleted_anchors=12*m["s"]*m["t"]*d)
    for k,v in bad.items():
        assert len(v)<=parts[k],(k,len(v),parts[k])
    assert len(mask)==sum(len(x) for x in bad.values())  # precedence partition
    assert len(mask)<=sum(parts.values())
    return dict(parts={k:len(bad[k]) for k in parts},
                conservative_caps=parts,
                total_bad=len(mask),
                total_conservative_cap=sum(parts.values()),
                no_GQ_projection_completion=True,
                all_nonincident_projections_unique_where_present=True,
                deleted_original_source_flags=d)


def typed_e_col(m,side):
    if side=="point":
        neighbors=m["neighbors_point"];labels=m["f"]
    elif side=="line":
        neighbors=m["neighbors_line"];labels=m["g"]
    else:
        raise ValueError("point or line required")
    return sum(bool(set(labels[i])&set(labels[j]))
               for i,adj in enumerate(neighbors) for j in adj if j>i)


def source_finite_case(name,scheme="lex",mask="full"):
    m=make_model(name,scheme)
    A,C=selected_mask(m,mask)
    point_book=full_core_book(m,A,C)
    line_book=full_core_book(m,A,C,"line")
    inverse=inverse_certificate(m,A,C)
    endpoints=endpoint_mask(m,A)
    # Independent original source Gram from C1, without GQ SRG formula.
    Dp,Dl,_=defect_matrices(m)
    pdata=typed_conflicts_and_gram(m,m["f"],m["neighbors_point"],Dp,
                                    m["s"],m["t"])
    ldata=typed_conflicts_and_gram(m,m["g"],m["neighbors_line"],Dl,
                                    m["t"],m["s"])
    assert point_book["G"]==pdata["gram"]
    assert line_book["G"]==ldata["gram"]
    return dict(kind=name,scheme=scheme,mask=mask,
                s=m["s"],t=m["t"],
                source_lines=len(m["lines"]),source_points=m["points"],
                source_flags=len(m["flags"]),
                source_excess_lines=m["excess_lines"],
                missing_original_3paths=len(m["missing"]),
                surviving_full_flags=len(A),core_flags=len(C),
                point_book={k:v for k,v in point_book.items() if k!="book_keys"},
                line_book={k:v for k,v in line_book.items() if k!="book_keys"},
                produced_inverse=inverse,
                endpoint_mask=endpoints,
                no_external_GQ_template_used=True,
                finite_falsifier_only=True)


def certificate():
    selected=[
      ("W32","lex","full"),
      ("W32","lex","delete"),
      ("W32","lex","mixed"),
      ("W32","correlated","mixed"),
      ("W33","lex","mixed"),
      ("Qminus24","lex","mixed"),
      ("dualQminus42","lex","mixed"),
      ("doubleW32","lex","full"),
      ("switchedDoubleW32","lex","mixed"),
      ("switchedDoubleW32","correlated","mixed"),
      ("W32","lex","empty_core"),
      ("W32","lex","delete_anchors"),
    ]
    cases=[source_finite_case(*x) for x in selected]
    return dict(schema=SCHEMA,parent_issue=793,meta_issue=790,
       parent_G6C1_HEAD=PARENT_G6C1,
       claim="PROVED_INTRINSIC_A5_BOOK_AND_PARTIAL_A6_INVERSE_NOT_FULL_T3",
       selected_cases=cases,
       source_first_equals_physical_first_for_partial_nonGQ=True,
       full_A_core_C_never_conflated=True,
       exact_mixed_book_Cauchy_and_Theta_bound=True,
       no_abstract_T3_full_obstruction_claim=True,
       no_intrinsic_A4_LOW_sixset_supersaturation=True,
       no_Lean_or_external_independent_referee=True,
       no_unrestricted_ASET_exponent=True)


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--out",default="gio003-g6c2-partial-books.json")
    a=p.parse_args()
    cert=certificate()
    Path(a.out).write_text(json.dumps(cert,sort_keys=True,indent=2)+"\n",
                           encoding="utf-8")
    print("PASS_GIO003_G6C2_MIXED_BOOK_PARTIAL_INVERSE_CERTIFICATE")
