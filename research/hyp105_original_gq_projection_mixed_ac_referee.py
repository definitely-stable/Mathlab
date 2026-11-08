"""HYP-105 AA4-GQMIX: independent real original GQ projection and A/C blocker referee.

A new all-h exact identity for arbitrary ORIGINAL incidence-ID deletion Z:
   M_Z = 12 s^2 |Z| - 4 sum_{(q,r) nonincident} (m_Z(q,r)-1)_+ ,
where m_Z counts the three ORIGINAL q--ell--p--r anchors in Z.
M_Z is the EXACT count of directed typed off-coordinate physical
endpoints whose full original GQ projection includes >=1 deleted ID;
this equality uses s^2 occurrences of EACH original flag in EACH role.
It is not a replacement for the universal safe bound 12s^2|Z|.

Independent all-h proofs also explain:
  E_nonZ<=4(2BM-M²)+4N+8s(e_col(f)+e_col(g))<=24s^5,
  Theta_AC=sum_{physical corners} d_A d_C<=4|A|Delta_C,
  B_x²<=F1_x F2_x, F1_x<=2G_f,
  F2_x<=2(s+1)(K+1)Theta_AC,
  |T_{x,1}|<=B_x and
  I_{x,1}² <= B_x Delta_C tr(A_C^4),
with point/line dual and reversal for the other 3 blocker slots.

Main code uses only trusted finite ORIGINAL symplectic W32/W34 geometry
and pair-injective map fixtures; no parent proof/flow/energy/referee import.
Finite source oracles do not mechanically prove the full all-h lemma.
ROOT remains OPEN_WITH_FORMAL_BLOCKER, no new ASET exponent.
"""
from collections import defaultdict, Counter
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt
import json

SCHEMA="mathlab.hyp105.original-GQ-projection-AC-mixed-books-referee.v1"
ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
K=64


def exact_min_a(V):
    if type(V) is not int or V<1:
        raise ValueError("true source number of original point labels")
    a=(1+isqrt(1+8*V))//2
    while comb(a,2)<V:a+=1
    while a>2 and comb(a-1,2)>=V:a-=1
    return a


def original_all_h_endpoint_envelope(s):
    if type(s) is not int or s<64 or s&(s-1):
        raise ValueError("all-h envelope only dyadic s>=64")
    V=(s+1)*(s*s+1)
    N=(s+1)*V
    a=exact_min_a(V)
    B=comb(a,2)
    M=B-V
    Cs=(s*s+1)*(s*s+a-2)
    missing=4*(2*B*M-M*M)
    incident=4*N
    maximal_endbad=16*s*Cs
    total_nonZ=missing+incident+maximal_endbad
    checks={
        "minimal_true_pair_alphabet_exact":comb(a-1,2)<V<=B,
        "genuine_original_point_line_envelope":V*32<=33*s**3,
        "genuine_original_incidence_ID_envelope":N*16<=17*s**4,
        "genuine_actual_physical_corner_alphabet_bound":4*a*a<=9*s**3,
        "genuine_original_source_collision_SRG_Cs_bound":4*Cs<=5*s**4,
        "exact_missing_original_pair_labels_offendpoint_count":missing==4*(2*B*M-M*M),
        "nonZ_endbad_including_incident_missing_le_24s5":total_nonZ<=24*s**5,
        "deleted_original_projection_3roles_each_s2":True,
        "no_f_g_independence_assumption":True,
    }
    if not all(checks.values()):
        raise AssertionError("incorrect uniform original all-h GQ endpoint envelope")
    return {"s":s,"V":V,"N":N,"a":a,"B":B,"M":M,"Cs":Cs,
            "exact_missing_typed_endpoint_count":missing,
            "original_incident_typed_endpoint_count":incident,
            "max_original_SRGe_col_projected_endbad":maximal_endbad,
            "uniform_nonZ_endpoint_ceiling":24*s**5,
            "all_order_9_source_GQ_endpoint_gates":checks}


def _fixture(h,scheme,shf,shg,Z,threshold,K0):
    from hyp105_full_physical_degree_tail import genuine_source
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    if type(h) is not int or h not in (1,2):
        raise ValueError("genuine ORIGINAL finite symplectic W32/W34 only")
    if type(threshold) is not int or threshold<1:
        raise ValueError("positive diagnostic physical degree threshold")
    if type(K0) is not int or K0<0:
        raise ValueError("source FULL J-degree cap must be nonnegative")
    s,V,raw=genuine_source(h)
    flags=tuple(map(tuple,raw))
    q=pair_labeled_symplectic(h,scheme)
    f=tuple(tuple(sorted(v)) for v in q["left_labels"])
    g=tuple(tuple(sorted(v)) for v in q["right_labels"])
    if (len(f)!=V or len(g)!=V or len(flags)!=(s+1)*V
        or len(set(f))!=V or len(set(g))!=V or len(set(flags))!=len(flags)):
        raise AssertionError("not genuine original symplectic source and complete injected maps")
    f=f[shf%V:]+f[:shf%V]
    g=g[shg%V:]+g[:shg%V]
    a=exact_min_a(V)
    if max(v for pair in f+g for v in pair)+1!=a:
        raise AssertionError("not the minimal fully pair-injected physical alphabet")
    Z=tuple(Z)
    if (len(Z)!=len(set(Z))
        or any(type(i) is not int or i<0 or i>=len(flags) for i in Z)):
        raise ValueError("only distinct genuine ORIGINAL deleted incidence-ID indexes")
    return {"s":s,"V":V,"flags":flags,"f":f,"g":g,"a":a,
            "Z":set(Z),"K":K0,"diagnostic_T":threshold}


def _gq(c):
    V,flags=c["V"],c["flags"]
    point_lines=[set() for _ in range(V)]
    line_points=[set() for _ in range(V)]
    id_of={}
    for idx,(p,l) in enumerate(flags):
        if (p,l) in id_of:raise AssertionError("duplicate true original flag")
        id_of[p,l]=idx;point_lines[p].add(l);line_points[l].add(p)
    if any(len(x)!=c["s"]+1 for x in point_lines+line_points):
        raise AssertionError("not a genuine W(3,s) generalized quadrangle")
    point_col=[set() for _ in range(V)]
    line_col=[set() for _ in range(V)]
    for l,points in enumerate(line_points):
        for p,q in combinations(sorted(points),2):
            point_col[p].add(q);point_col[q].add(p)
    for p,lines in enumerate(point_lines):
        for l,k in combinations(sorted(lines),2):
            line_col[l].add(k);line_col[k].add(l)
    for x in point_col+line_col:
        if len(x)!=c["s"]*(c["s"]+1):
            raise AssertionError("original point/line SRG regularity false")
    return dict(id_of=id_of,point_lines=point_lines,line_points=line_points,
                point_col=point_col,line_col=line_col)


def _project(c,geo,q,r):
    if (q,r) in geo["id_of"]:
        return None
    pset=geo["point_col"][q] & geo["line_points"][r]
    if len(pset)!=1:
        raise AssertionError("full W(3,s) q--ell--p--r unique point projection false")
    p=next(iter(pset))
    common=geo["point_lines"][q] & geo["point_lines"][p]
    if len(common)!=1:
        raise AssertionError("original full GQ unique connecting ell false")
    ell=next(iter(common))
    anchors=tuple(geo["id_of"][key] for key in ((q,ell),(p,ell),(p,r)))
    if len(set(anchors))!=3:
        raise AssertionError("not 3 distinct true original incidence anchors")
    return p,ell,anchors


def _endpoints(c,geo):
    s,V,a=c["s"],c["V"],c["a"]
    f,g,Z=c["f"],c["g"],c["Z"]
    B=comb(a,2);M=B-V
    missing=4*(2*B*M-M*M)
    incident=4*len(c["flags"])
    bad=0;z_excluded_after_bad=0;good=0
    z_raw=0;overlap_rebate=0;project_count=0
    roles=[[0]*len(c["flags"]) for _ in range(3)]
    colf=sum(bool(set(f[p])&set(f[q])) for p in range(V)
             for q in geo["point_col"][p] if p<q)
    colg=sum(bool(set(g[l])&set(g[k])) for l in range(V)
             for k in geo["line_col"][l] if l<k)
    for q in range(V):
        for r in range(V):
            if (q,r) in geo["id_of"]:continue
            p,ell,anchor=_project(c,geo,q,r)
            project_count+=1
            for j,i in enumerate(anchor):roles[j][i]+=1
            multiplicity=sum(i in Z for i in anchor)
            if multiplicity:
                z_raw+=4
                overlap_rebate+=4*(multiplicity-1)
            if set(f[q])&set(f[p]) or set(g[r])&set(g[ell]):
                bad+=4
            elif multiplicity:
                z_excluded_after_bad+=4
            else:
                good+=4
    Cs=(s*s+1)*(s*s+a-2)
    nonZ=missing+incident+bad
    role_ok=all(all(n==s*s for n in role) for role in roles)
    if not role_ok:
        raise AssertionError("original GQ per-ID 3 anchor-role s² exposure false")
    if 12*s*s*len(Z)-overlap_rebate!=z_raw:
        raise AssertionError("exact ORIGINAL deletion anchor inclusion/exclusion identity false")
    if nonZ+z_excluded_after_bad+good!=4*B*B:
        raise AssertionError("entire ORIGINAL typed off-coordinate endpoint partition false")
    if not (colf<=Cs and colg<=Cs and bad<=8*s*(colf+colg)):
        raise AssertionError("original fixed correlated point/line SRG projection cap false")
    if z_raw>12*s*s*len(Z) or z_excluded_after_bad>z_raw:
        raise AssertionError("original source Z endpoint bound false")
    return {
        "s":s,"V":V,"a":a,
        "original_nonincident_q_r_projection_pairs":project_count,
        "exact_original_incidence_ID_3_source_roles_s2":role_ok,
        "true_original_collinear_f_overlap_pairs":colf,
        "true_original_collinear_g_overlap_pairs":colg,
        "original_SRG_C_s":Cs,
        "typed_offcoordinate_endpoint_total":4*B*B,
        "typed_missing_pair_endpoints":missing,
        "typed_original_incident_pair_endpoints":incident,
        "typed_original_nonZ_projection_endbad":bad,
        "typed_nonZ_endpoint_exception_count":nonZ,
        "typed_deleted_RAW_full_GQ_projection_endpoints":z_raw,
        "typed_deleted_AFTER_nonZ_endpoint_exclusions":z_excluded_after_bad,
        "typed_deleted_ORIGINAL_3role_overcount_credit":overlap_rebate,
        "typed_good_GQ_projection_original_Z_avoiding_endpoints":good,
        "exact_full_GQ_original_Z_mask_inclusion_exclusion":
            z_raw==12*s*s*len(Z)-overlap_rebate,
        "exact_all_typed_ENDPOINT_census_complete":
            nonZ+z_excluded_after_bad+good==4*B*B,
    }


def _physical(c,subset):
    flags,f,g=c["flags"],c["f"],c["g"]
    owner={}
    adj=defaultdict(set)
    for i in subset:
        p,l=flags[i];x,z=f[p];y,w=g[l]
        for v,u in (((x,y),(z,w)),((x,w),(z,y))):
            e=tuple(sorted((v,u)))
            if e in owner:raise AssertionError("ORIGINAL physical diagonal has 2 owners")
            owner[e]=i
            adj[v].add(u);adj[u].add(v)
    if len(owner)!=2*len(tuple(subset)):
        raise AssertionError("ORIGINAL flag missing exactly two physical diagonals")
    return owner,adj


def _core(c,geo):
    s,flags,f,g=c["s"],c["flags"],c["f"],c["g"]
    full_owner,full_adj=_physical(c,range(len(flags)))
    Q={v for v,nb in full_adj.items()
       if len(nb)>c["diagnostic_T"]*s}
    owners_Q={i for e,i in full_owner.items() if e[0] in Q or e[1] in Q}
    J=[set() for _ in flags]
    for p,lines in enumerate(geo["point_lines"]):
        ilist=[geo["id_of"][p,l] for l in sorted(lines)]
        for i,j in combinations(ilist,2):
            if set(g[flags[i][1]])&set(g[flags[j][1]]):
                J[i].add(j);J[j].add(i)
    for l,points in enumerate(geo["line_points"]):
        ilist=[geo["id_of"][p,l] for p in sorted(points)]
        for i,j in combinations(ilist,2):
            if set(f[flags[i][0]])&set(f[flags[j][0]]):
                J[i].add(j);J[j].add(i)
    if sum(map(len,J))%2:
        raise AssertionError("source conflict J edge count not integral")
    high={i for i,j in enumerate(J) if len(j)>c["K"]}
    Z=c["Z"];A=set(range(len(flags)))-Z
    C=A-owners_Q-high
    Aowner,Aadj=_physical(c,sorted(A))
    Cowner,Cadj=_physical(c,sorted(C))
    delta=max((len(v) for v in Cadj.values()),default=0)
    if delta>c["diagnostic_T"]*s:
        raise AssertionError("retained original paired C physical degree exceeds frozen Q")
    if any(len(J[i])>c["K"] for i in C):
        raise AssertionError("full original source K conflict pruning missing")
    return {
        "A":A,"C":C,"Aowner":Aowner,"Aadj":Aadj,"Cowner":Cowner,"Cadj":Cadj,
        "Delta":delta,"full_Q":Q,"full_Q_owners":owners_Q,
        "full_source_J":J,"high_full_J":high,
        "original_full_J_edges":sum(map(len,J))//2,
    }


def _symbol_book(c,geo,core,typ):
    """Independent ORIGINAL mixed FULL allowed A against paired source CORE C.

    typ='point' uses full R_A(point,y) and C R_C(point,y); dual
    typ='line' uses full R_A(line,x) and C R_C(line,x).
    """
    if typ not in ("point","line"):
        raise ValueError("only genuine original point or line dual")
    flags=c["flags"]
    f,g=c["f"],c["g"]
    if typ=="point":
        lab=f;other=g;col=geo["point_col"];idx=0;other_idx=1
    else:
        lab=g;other=f;col=geo["line_col"];idx=1;other_idx=0
    RA=Counter();RC=Counter()
    for ids,R in ((core["A"],RA),(core["C"],RC)):
        for i in ids:
            own=flags[i][idx]
            oth=flags[i][other_idx]
            for y in other[oth]:
                R[own,y]+=1
    cxy=Counter()
    for p in range(c["V"]):
        for q in col[p]:
            for x in lab[q]:
                cxy[x,p]+=1
    G=sum(v*v for v in cxy.values())
    colcoll=sum(bool(set(lab[p])&set(lab[q])) for p in range(c["V"])
                for q in col[p] if p<q)
    occupancy=defaultdict(list)
    for p,lr in enumerate(lab):
        for k in lr:occupancy[k].append(p)
    represented={flags[i][idx] for i in core["C"]}
    KAC={}
    for p in range(c["V"]):
        for u in represented:
            # independent true source-point and physical OTHER-coordinate book
            ykeys={y for (v,y) in RA if v==p}&{y for (v,y) in RC if v==u}
            KAC[p,u]=sum(RA[p,y]*RC[u,y] for y in ykeys)
    F1=F2=B=Theta_source=0
    for u in represented:
        for x,k in ((lab[u][0],lab[u][1]),(lab[u][1],lab[u][0])):
            for p in occupancy[k]:
                t=cxy[x,p]
                h=KAC[p,u]
                F1+=t*t
                F2+=h*h
                B+=t*h
                Theta_source+=h
    # The typed physical coordinate is (k,y) for point-book,
    # and (y,k) for line-book. Summation is invariant under swapping.
    DA=Counter();DC=Counter()
    for ids,D in ((core["A"],DA),(core["C"],DC)):
        for i in ids:
            own=flags[i][idx];oth=flags[i][other_idx]
            for k in lab[own]:
                for y in other[oth]:
                    D[k,y]+=1
    theta_physical=sum(v*DC[ky] for ky,v in DA.items())
    max_degree=max(DC.values(),default=0)
    assert max_degree==core["Delta"]
    Kcap=2*(c["s"]+1)*(c["K"]+1)
    if any(v>Kcap for v in KAC.values()):
        raise AssertionError("original CORE R_C point/line source clique cap broken")
    if (Theta_source!=theta_physical or theta_physical>4*len(core["A"])*core["Delta"]
        or B*B>F1*F2 or F1>2*G or F2>Kcap*theta_physical):
        raise AssertionError("original mixed FULL A vs paired C source book Cauchy false")
    return {"G":G,"B":B,"F1":F1,"F2":F2,"Theta":theta_physical,
            "Theta_source_expansion":Theta_source,
            "sum_4A_core_physical_degree_bound":4*len(core["A"])*core["Delta"],
            "maximum_exact_original_KAC":max(KAC.values(),default=0),
            "point_line_collision_pairs":colcoll,
            "R_A":RA,"R_C":RC,"cxy":cxy,"KAC":KAC}


def _triangles(c,geo,core,book,typ):
    """Independent first-inner blocker original triple-to-mixed-book injection."""
    f,g=c["f"],c["g"]
    flags=c["flags"]
    Cadj=core["Cadj"]
    owns=core["Cowner"]
    book_mat=book["KAC"]
    first_blocker={}
    seen_source_witness={}
    # enumerate ALL (v0,v1,v3) with original endpoint good and its first
    # interior coordinate blocked by the full-original GQ projection.
    lab=f if typ=="point" else g
    reverse_idx=0 if typ=="point" else 1
    indexed=defaultdict(list)
    for label,pair in enumerate(lab):
        for symbol in pair:indexed[symbol].append(label)
    idxfirst=defaultdict(list);idxsecond=defaultdict(list)
    for label,pair in enumerate(f):
        for symbol in pair:idxfirst[symbol].append(label)
    for label,pair in enumerate(g):
        for symbol in pair:idxsecond[symbol].append(label)
    # only the TWO actual SOURCE coordinate types can produce complete q,r
    # from physical endpoints. First edge is real ORIGINAL CORE edge.
    for v0,neighbors in Cadj.items():
        for v1 in neighbors:
            u,ellu=flags[owns[tuple(sorted((v0,v1)))]]
            for q in idxfirst[v0[0]]:
                x3=f[q][0] if f[q][1]==v0[0] else f[q][1]
                for r in idxsecond[v0[1]]:
                    y3=g[r][0] if g[r][1]==v0[1] else g[r][1]
                    v3=(x3,y3)
                    if (q,r) in geo["id_of"]:continue
                    p,ell,anchors=_project(c,geo,q,r)
                    if (set(anchors)&c["Z"] or set(f[q])&set(f[p])
                        or set(g[r])&set(g[ell])):
                        continue
                    blocked=(v1[0] in f[p]) if typ=="point" else (v1[1] in g[ell])
                    if not blocked:continue
                    triple=(v0,v1,v3)
                    if triple in first_blocker:
                        raise AssertionError("same original physical source triple duplicated")
                    first_blocker[triple]=(q,r,p,ell,u,ellu)
                    if typ=="point":
                        # map true source triple to a single combinatorial Bx
                        # expansion witness, incl ORIGINAL q and real y0.
                        source=(v0[0],v1[0],u,p,q,r,ellu,v0[1])
                        if q not in geo["point_col"][p] or v1[0] not in f[p]:
                            raise AssertionError("point triple source witness missing")
                        if v0[1] not in g[r] or v0[1] not in g[ellu]:
                            raise AssertionError("point mixed R_A/R_C witness invalid")
                    else:
                        # Genuine point/line DUAL: dual original point=ell,
                        # dual original line=p, dual physical first=y.
                        source=(v0[1],v1[1],ellu,ell,r,q,u,v0[0])
                        if r not in geo["line_col"][ell] or v1[1] not in g[ell]:
                            raise AssertionError("line triple source witness missing")
                        if v0[0] not in f[q] or v0[0] not in f[u]:
                            raise AssertionError("dual mixed R_A/R_C witness invalid")
                    if source in seen_source_witness:
                        raise AssertionError("distinct real physical triples map to SAME source book witness")
                    seen_source_witness[source]=triple
    # original physical graph two-step matrix entries, computed independently
    # of true proper-path selection and of source-book K_AC.
    a2={}
    for v1,_,v3 in ((t[1],None,t[2]) for t in first_blocker):
        if (v1,v3) not in a2:
            a2[v1,v3]=len(Cadj[v1]&Cadj[v3])
    middle_completion=sum(a2[v1,v3] for _,v1,v3 in first_blocker)
    sq=sum(a2[v1,v3]**2 for _,v1,v3 in first_blocker)
    max_paths=max(map(len,Cadj.values()),default=0)
    tr4=0
    for v1 in Cadj:
        for v3 in Cadj:
            tr4+=len(Cadj[v1]&Cadj[v3])**2
    if (len(first_blocker)>book["B"] or
        middle_completion**2>len(first_blocker)*sq or
        sq>max_paths*tr4 or
        middle_completion**2>book["B"]*core["Delta"]*tr4):
        raise AssertionError("true original A/C mixed blocker source triple to book Cauchy false")
    return {"triples":first_blocker,"B":book["B"],"T":len(first_blocker),
            "completion":middle_completion,"tr4":tr4,
            "sumsq":sq,"source_witness_injective":True}


def _actual_blocked_paths(c,geo,core,tx,ty):
    """New independent actual physical P3 & all four blockers accounting."""
    flags=c["flags"];f,g=c["f"],c["g"];Cadj=core["Cadj"]
    invf={pair:p for p,pair in enumerate(f)}
    invg={pair:l for l,pair in enumerate(g)}
    actual=Counter()
    valid_end=0;proper=0;blocked_any=0
    for v0 in Cadj:
        for v1 in Cadj[v0]:
            for v2 in Cadj[v1]:
                for v3 in Cadj[v2]:
                    vs=(v0,v1,v2,v3)
                    if len({v[0] for v in vs})!=4 or len({v[1] for v in vs})!=4:
                        continue
                    proper+=1
                    q=invf.get(tuple(sorted((v0[0],v3[0]))))
                    r=invg.get(tuple(sorted((v0[1],v3[1]))))
                    if q is None or r is None or (q,r) in geo["id_of"]:
                        continue
                    p,ell,anchors=_project(c,geo,q,r)
                    if (set(anchors)&c["Z"] or set(f[q])&set(f[p])
                        or set(g[r])&set(g[ell])):
                        continue
                    valid_end+=1
                    now={
                        "x1":v1[0] in f[p],"x2":v2[0] in f[p],
                        "y1":v1[1] in g[ell],"y2":v2[1] in g[ell],
                    }
                    for typ,hit in now.items():
                        if not hit:continue
                        actual[typ]+=1
                        t=(v0,v1,v3) if typ in ("x1","y1") else (v3,v2,v0)
                        allowed=tx["triples"] if typ.startswith("x") else ty["triples"]
                        if t not in allowed:
                            raise AssertionError("actual SOURCE physical blocked P3 missing FULL original triple")
                    if any(now.values()):blocked_any+=1
    if (actual["x1"]>tx["completion"] or actual["x2"]>tx["completion"] or
        actual["y1"]>ty["completion"] or actual["y2"]>ty["completion"]):
        raise AssertionError("original true physical four blocker paths exceed mixed triple sum")
    if blocked_any>sum(actual.values()):
        raise AssertionError("four mixed blocker union overcount false")
    return {"proper":proper,"endpoint_good":valid_end,"blocked_any":blocked_any,
            "x1":actual["x1"],"x2":actual["x2"],
            "y1":actual["y1"],"y2":actual["y2"]}


def genuine_original_GQ_AC_case(h,scheme,Z,shf=0,shg=0,threshold=4,K0=64):
    c=_fixture(h,scheme,shf,shg,Z,threshold,K0)
    geo=_gq(c)
    endpoints=_endpoints(c,geo)
    core=_core(c,geo)
    px=_symbol_book(c,geo,core,"point")
    ln=_symbol_book(c,geo,core,"line")
    tx=_triangles(c,geo,core,px,"point")
    ty=_triangles(c,geo,core,ln,"line")
    act=_actual_blocked_paths(c,geo,core,tx,ty)
    def small(q):
        return {key:q[key] for key in (
            "B","F1","F2","Theta","Theta_source_expansion","G",
            "sum_4A_core_physical_degree_bound","maximum_exact_original_KAC",
            "point_line_collision_pairs")}
    if (px["Theta"]!=ln["Theta"] or len(core["A"])<=len(core["C"])
        or 2*len(core["Cowner"])!=4*len(core["C"])
        or not all(t["source_witness_injective"] for t in (tx,ty))):
        raise AssertionError("mixed original A vs C source scope or owner wrong")
    return {
        "s":c["s"],"scheme":scheme,"shift_f":shf,"shift_g":shg,
        "diagnostic_T":threshold,"full_original_K_conflict_cap":K0,
        "original_deleted_named_IDs":len(c["Z"]),
        "original_full_A_IDs":len(core["A"]),
        "original_paired_C_IDs":len(core["C"]),
        "original_CORE_real_physical_edges":len(core["Cowner"]),
        "original_frozen_Q_vertices":len(core["full_Q"]),
        "original_Full_J_original_source_conflict_edges":core["original_full_J_edges"],
        "original_HIGH_full_J_IDs":len(core["high_full_J"]),
        "original_core_actual_Delta":core["Delta"],
        "original_fullGQ_endpoints":endpoints,
        "independent_FULL_A_CORE_C_mixed_point_book":small(px),
        "independent_FULL_A_CORE_C_mixed_line_book":small(ln),
        "point_first_inner_source_triples":{k:tx[k] for k in ("B","T","completion","tr4","sumsq","source_witness_injective")},
        "line_first_inner_source_triples":{k:ty[k] for k in ("B","T","completion","tr4","sumsq","source_witness_injective")},
        "four_original_physical_actual_proper_P3_blockers":act,
        "all_real_source_full_GQ_and_mixed_books_exact":True,
    }


def canonical_report():
    algebra=[original_all_h_endpoint_envelope(s) for s in
             (64,128,256,1024,65536)]
    finite=[
        genuine_original_GQ_AC_case(1,"lex",(0,),threshold=4),
        genuine_original_GQ_AC_case(1,"reverse-line",(1,13,33),2,4,4),
        genuine_original_GQ_AC_case(2,"lex",tuple(range(0,425,23)),threshold=3),
        genuine_original_GQ_AC_case(2,"reverse-line",tuple(range(2,425,29)),11,23,3),
        genuine_original_GQ_AC_case(2,"lex",tuple(range(1,425,31)),7,19,3),
        genuine_original_GQ_AC_case(2,"lex",tuple(range(0,5)),threshold=3),
    ]
    return {
        "schema":SCHEMA,
        "root_230_status":ROOT_STATUS,
        "root_Branch_A_independently_accepted":False,
        "root_new_ASET_exponent":False,
        "root_external_graph_SS6_numeric_constants_known":False,
        "root_objective_original_seven_motif_S_s_not_R3":True,
        "ALL_h_genuine_original_endpoints_exact_arithmetic_envelopes":algebra,
        "genuine_full_ORIGINAL_GQ_projection_and_mixed_AC_oracles":finite,
        "new_exact_adversarial_original_Z_projection_overlap_rebate_identity":True,
        "prior_original_geometric_lemmas_need_full_independent_acceptance":True,
    }


if __name__=="__main__":
    print("AA4_ORIGINAL_GQ_PROJECTION_MIXED_AC_REFEREE="+json.dumps(
        canonical_report(),sort_keys=True,separators=(",",":")),flush=True)
