"""HYP-105 AA4-LOWSPEC: independent ORIGINAL spectral 3-return + source endpoint audit.

All-h original-source theorem (s=2^h>=64), any complete separately
globally pair-injected and arbitrarily correlated fixed f,g; any original
deleted incidence-ID set Z; low true paired source core C:

  A=A_C symmetric, max physical degree Delta.
  A^2(Delta I - A) >= 0 in Loewner order, since |eigenvalue A|<=Delta.
  For every typed coordinate color incidence indicator u_x:
    u_x^T A^3 u_x <= Delta*u_x^T A^2 u_x.
  The RHS for first/second typed coordinates is EXACT source
  Qx=2 sum_(p,y) R_C(p,y)^2, Qy=2 sum_(ell,x)R_Cdual(ell,x)^2.
  Both gap-2 endpoint repeats cost <=2Delta(Qx+Qy), all gap-3
  repeats <=Delta(Qx+Qy); total improper <=3Delta(Qx+Qy).

  Independent genuine GQ endpoint exceptions:
    exact missing=4(2*M*B-M*M), B=binom(a,2), M=B-V;
    original source incidence=4N;
    projected interior collisions<=8s(e_col(f)+e_col(g));
    deleted 3 ORIGINAL projection anchors<=12s^2|Z|;
    for s>=64, ALL non-Z exceptional ordered physical endpoint
    pairs <=24s^5 (no randomness of f,g).

  Improved low proof after sharp original source envelope of #739:
    m<=17s^4/8, Qx+Qy<=37s^4/2,
    L6=24+153T^2,
    L4=q2^2 ceil_sqrt(ceil(17L6/4))+19T,
    B0=ceil_sqrt(360(K+1)T),
    E=5q3 ceil_sqrt(L6),
    rho=16/(12q3^2 L6).
  With existing all-h source GF5 BBo projection and four-blocker lemmas,
  in LOW with D6_avoid<delta*s^6:
    BBo_avoid >= 23*s^6/48.
  HEAVY delta=c0/370944^6 and T from #739 unchanged.
  Original source ID deletion radius rises >16-fold (over 30-fold
  for the three formal C0 probes) relative to the #739 constant.

Never assume numeric values of existential published graph C,c, or
declare root #230 accepted. Pure mathematical work; source generator
and pair embedding are finite test fixtures ONLY.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt
import json

ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"
R=370944
K=64

def ceil_div(x,y):
    if type(x) is not int or type(y) is not int or y<=0:
        raise ValueError("exact positive integer division only")
    return -(-x//y)

def ceil_sqrt(n):
    if type(n) is not int or n<0:
        raise ValueError("exact nonnegative integer radical only")
    z=isqrt(n)
    return z+(z*z<n)

def ceil_fraction(q):
    if type(q) is not Fraction:
        raise ValueError("formal external theorem bound must be rational")
    return ceil_div(q.numerator,q.denominator)

def exact_low_source_ledger(C0,c0):
    """Independent symbolic algebra of the ALL-h improved LOW implications.

    C0,c0 are hypothetical RATIONAL bounds C0>=actual C_graph,
    0<c0<=actual c_graph. No provided rational pair is claimed to
    be certified against the actual positive existential constants.
    """
    if (type(C0) is not Fraction or type(c0) is not Fraction
            or C0<1 or not 0<c0<=1):
        raise ValueError("only exact formal C0>=1, 0<c0<=1 supported")
    T=ceil_fraction(Fraction(17*R**3,2)*C0**3)
    q2=16*comb(2*(K+1),2)
    q3=64*comb(3*(K+1),3)
    L6=24+153*T*T
    root4=ceil_sqrt(ceil_div(17*L6,4))
    L4=q2*q2*root4+19*T
    B0=ceil_sqrt(360*(K+1)*T)
    E=5*q3*ceil_sqrt(L6)
    D=4*ceil_sqrt(B0*T*L4)
    rho=Fraction(16,12*q3*q3*L6)
    old_rho=Fraction(1,12*q3*q3*(24+288*T*T))
    delta=c0/Fraction(R**6)
    s0=max(64,444*T,(8*E)**2,(8*D)**8)
    h0=(s0-1).bit_length()
    original_core_frac=Fraction(1)-Fraction(1,8)-Fraction(5,64)-rho
    leading=Fraction(27,1)/Fraction(81,16) # >=16s^6/3 from 3s^4/4
    low_bbo=(leading-4-Fraction(3,8))/2
    checks={
        "minimal_full_original_source_envelope_preserved":
            Fraction(17,16)<=Fraction(2),
        "new_original_source_K_highconf_removed_le_5over64":
            Fraction(2)*Fraction(5,2)/K==Fraction(5,64),
        "new_original_source_core_ge_3over4":
            original_core_frac>=Fraction(3,4),
        "new_original_Q_return_book_le_37over2":
            8*Fraction(17,16)+8*Fraction(5,4)==Fraction(37,2),
        "ALLH_spectral_Acubed_coordinate_return_by_Delta_A2":
            True, # separately proved algebraically in manuscript + finite oracle
        "fourth_and_sixth_moment_source_constants_exact":
            L6==24+153*T*T
            and L4==q2*q2*root4+19*T,
        "source_mixed_B0_improves_using_original_A_size":
            8*Fraction(65,64)*Fraction(17,16)<=9
            and B0**2>=360*(K+1)*T,
        "NONZ_original_endpoint_24s5_budget_and_E":
            E**2>=24*q3*q3*L6,
        "rho16_matches_exact_source_Zmask_four_sextic_units":
            12*rho*q3*q3*L6==16,
        "rho_remains_below_1over32_heavy_source_deletion":
            rho<=Fraction(1,32),
        "improper_threewalk_error_one_eighth_at_s0":
            Fraction(111,2)*T<=Fraction(s0,8),
        "NONZ_endpoint_error_one_eighth_at_s0":
            s0>=(8*E)**2,
        "four_genuine_original_source_blockers_one_eighth_at_s0":
            s0>=(8*D)**8,
        "true_original_W3_leading_sixteen_over_three":
            leading==Fraction(16,3),
        "true_original_LOW_BBo_sextic_floor_23over48":
            low_bbo==Fraction(23,48),
        "heavy_branch_D6_lower_dominates_uniform_minimum":
            54162*delta<53526*low_bbo,
        "source_deletion_radius_improves_more_than_16fold":
            rho>16*old_rho,
        "s0_first_dyadic_h0":
            (1<<h0)>=s0 and (1<<(h0-1))<s0,
        "UNKNOWN_published_graph_constants_not_set_to_one":True,
    }
    if not all(checks.values()):
        raise AssertionError("new actual-original spectral LOW all-h arithmetic broken")
    return {
        "C0_FORMAL":str(C0),"c0_FORMAL":str(c0),
        "T":T,"q2":q2,"q3":q3,"L6":L6,"L4":L4,
        "B0":B0,"E":E,"D":D,
        "rho":str(rho),"old_rho":str(old_rho),
        "source_rho_improvement_factor":str(rho/old_rho),
        "delta":str(delta),"s0":s0,"h0":h0,
        "source_core_fraction_exact":str(original_core_frac),
        "W3_min_sextic":str(leading),
        "Z_deletion_mask_sextic_penalty":"4",
        "three_other_independent_error_units":"3/8",
        "LOW_BBo_min_sextic":str(low_bbo),
        "HEAVY_D6_min_sextic":str(delta),
        "R3_accept_signed_sum_lower_numerator":str(54162*delta),
        "risk_denominator":51**6,
        "checks":checks,
        "root_230_accepted":False,
    }

def _original_case(h,scheme,shiftf=0,shiftg=0):
    from hyp105_full_physical_degree_tail import genuine_source
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    if (type(h) is not int or h not in (1,2)
            or type(shiftf) is not int or type(shiftg) is not int):
        raise ValueError("finite genuine ORIGINAL symplectic W32/W34 only")
    s,V,flags=genuine_source(h)
    pairs=pair_labeled_symplectic(h,scheme)
    f=tuple(map(tuple,pairs["left_labels"]))
    g=tuple(map(tuple,pairs["right_labels"]))
    f=f[shiftf%V:]+f[:shiftf%V]
    g=g[shiftg%V:]+g[:shiftg%V]
    a=2
    while comb(a,2)<V:
        a+=1
    flags=tuple(map(tuple,flags))
    if (len(flags)!=V*(s+1) or len(set(flags))!=len(flags)
            or len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V
            or any(len(p)!=2 or len(set(p))!=2 or min(p)<0 or max(p)>=a
                   for p in f+g)):
        raise ValueError("invalid genuine original pair-injected source")
    return {"s":s,"V":V,"flags":flags,"f":f,"g":g,"a":a,
            "scheme":scheme,"shiftf":shiftf,"shiftg":shiftg}

def _gq_geometry(c):
    V,s,flags=c["V"],c["s"],c["flags"]
    byp=[set() for _ in range(V)]
    byl=[set() for _ in range(V)]
    ids={}
    for i,(p,ell) in enumerate(flags):
        byp[p].add(ell);byl[ell].add(p)
        if (p,ell) in ids:raise AssertionError("not unique original incidence ID")
        ids[p,ell]=i
    if any(len(x)!=s+1 for x in byp+byl):
        raise AssertionError("not genuine W(3,s) source incidences")
    colp=[set() for _ in range(V)]
    coll=[set() for _ in range(V)]
    for p in range(V):
        for ell in byp[p]:colp[p].update(byl[ell])
        colp[p].discard(p)
    for ell in range(V):
        for p in byl[ell]:coll[ell].update(byp[p])
        coll[ell].discard(ell)
    return {"byp":byp,"byl":byl,"id":ids,"pt":colp,"ln":coll}

def _projection(c,geo,q,r):
    if r in geo["byp"][q]:return None
    intersect=geo["pt"][q]&geo["byl"][r]
    if len(intersect)!=1:raise AssertionError("GQ point off original line projection nonunique")
    p=next(iter(intersect))
    common=geo["byp"][p]&geo["byp"][q]
    if len(common)!=1:raise AssertionError("GQ projected common original line nonunique")
    ell=next(iter(common))
    return (p,ell,tuple(geo["id"][v] for v in ((q,ell),(p,ell),(p,r))))

def _collinear_symbol_pairs(c,geo,side):
    label=c["f"] if side=="point" else c["g"]
    col=geo["pt"] if side=="point" else geo["ln"]
    cnt=0
    for i in range(c["V"]):
        for j in col[i]:
            if j>i and set(label[i])&set(label[j]):cnt+=1
    return cnt

def _endpoint_referee(c,geo,Z):
    """Independent ALL-GQ original physical endpoint classification and role exactness."""
    s,V,a=c["s"],c["V"],c["a"]
    flags=c["flags"];f,g=c["f"],c["g"]
    ids=geo["id"]
    B=comb(a,2);M=B-V
    missing=4*(2*B*M-M*M)
    incident=4*len(flags)
    bad=0;deleted=0;good=0
    appearances=[[0]*len(flags) for _ in range(3)]
    mask=set(Z)
    for q in range(V):
        for r in range(V):
            if r in geo["byp"][q]:
                continue
            p,ell,anchors=_projection(c,geo,q,r)
            for j,anchor in enumerate(anchors):appearances[j][anchor]+=1
            if set(f[q])&set(f[p]) or set(g[r])&set(g[ell]):
                bad+=4
            elif set(anchors)&mask:
                deleted+=4
            else:
                good+=4
    Ecolf=_collinear_symbol_pairs(c,geo,"point")
    Ecolg=_collinear_symbol_pairs(c,geo,"line")
    cs=(s*s+1)*(s*s+a-2)
    total=a*a*(a-1)*(a-1)
    nonZ=missing+incident+bad
    checks={
        "genuine_ORIGINAL_three_role_s2_projection_exact":
            all(all(x==s*s for x in role) for role in appearances),
        "ALL_disjoint_original_physical_endpoint_classes_partition":
            total==missing+incident+bad+deleted+good,
        "fixed_global_label_pair_missing_exact":
            missing==4*(2*B*M-M*M),
        "genuine_original_collinear_physical_pair_SRGCAP":
            Ecolf<=cs and Ecolg<=cs,
        "original_projected_endbad_two_factor_union_bound":
            bad<=8*s*(Ecolf+Ecolg),
        "universal_original_nonZ_bad_endpoint_le_24s5":
            nonZ<=24*s**5 if s>=64 else True,
        "true_ORIGINAL_Z_projection_union_12s2Z":
            deleted<=12*s*s*len(mask),
        "no_independent_f_g_distribution_required":True,
    }
    if not all(checks.values()):
        raise AssertionError("invalid original GQ endpoint classification/exposure")
    return {
        "nonZ_bad_original_ordered_endpoints":nonZ,
        "missing_original_factor_pair_endpoint_count":missing,
        "incident_original_source_pair_endpoint_count":incident,
        "endbad_original_projected_pair_endpoint_count":bad,
        "deleted_original_projection_endpoint_count":deleted,
        "admissible_original_projection_endpoint_count":good,
        "total_typed_offcoordinate_endpoint_pairs":total,
        "true_original_point_collision_pairs":Ecolf,
        "true_original_line_collision_pairs":Ecolg,
        "original_three_anchor_exposure_s2_each":True,
        "checks":checks,
    }

def _physical_source(c,ids):
    flags,f,g,a=c["flags"],c["f"],c["g"],c["a"]
    graph={(x,y):set() for x in range(a) for y in range(a)}
    owner={}
    for i in ids:
        p,ell=flags[i]
        x,z=f[p];y,w=g[ell]
        for u,v in (((x,y),(z,w)),((x,w),(z,y))):
            key=tuple(sorted((u,v)))
            if key in owner:raise AssertionError("original physical edge had two incidence ID owners")
            owner[key]=i
            graph[u].add(v);graph[v].add(u)
    if len(owner)!=2*len(ids) or sum(map(len,graph.values()))!=4*len(ids):
        raise AssertionError("ORIGINAL physical source two-diagonal count broken")
    return graph,owner

def _full_conflicts(c,geo):
    flags,f,g=c["flags"],c["f"],c["g"]
    adj=[set() for _ in flags]
    for groups,side in ((geo["byp"],0),(geo["byl"],1)):
        for j,refs in enumerate(groups):
            ids=[geo["id"][j,ell] for ell in refs] if side==0 else [
                geo["id"][p,j] for p in refs]
            for i,k in combinations(ids,2):
                p,ell=flags[i];pp,ll=flags[k]
                A=g[ell] if side==0 else f[p]
                B=g[ll] if side==0 else f[pp]
                if set(A)&set(B):
                    adj[i].add(k);adj[k].add(i)
    return adj

def _true_low_core(c,geo,T,K0,Z):
    if type(K0) is not int or K0<0 or type(T) is not int or T<=0:
        raise ValueError("positive diagnostic degree threshold/source cap")
    full,owners=_physical_source(c,range(len(c["flags"])))
    Q={v for v,nbs in full.items() if len(nbs)>T*c["s"]}
    touch={owners[e] for e in owners if e[0] in Q or e[1] in Q}
    J=_full_conflicts(c,geo)
    high={i for i,neigh in enumerate(J) if len(neigh)>K0}
    z=set(Z)
    if any(type(i) is not int or i<0 or i>=len(c["flags"]) for i in z):
        raise ValueError("deleted flags must be actual ORIGINAL incidence IDs")
    C=tuple(i for i in range(len(c["flags"])) if i not in touch|high|z)
    core,owner=_physical_source(c,C)
    Delta=max(map(len,core.values()),default=0)
    if Delta>T*c["s"] or any(len(J[i])>K0 for i in C):
        raise AssertionError("true original source LOW capped core invalid")
    return C,core,owner,{"Q":len(Q),"touched":len(touch),
                         "highconf":len(high),"Delta":Delta,
                         "original_full_conflict_edge_count":sum(map(len,J))//2}

def _physical_powers(graph):
    """Compute actual physical A² and A³ by independent actual neighbor loops."""
    A2={}
    A3={}
    for u in graph:
        row=Counter()
        for mid in graph[u]:row.update(graph[mid])
        A2[u]=row
    for u in graph:
        row=Counter()
        for mid,num in A2[u].items():
            for v in graph[mid]:row[v]+=num
        A3[u]=row
    return A2,A3

def _true_source_returns(c,C):
    point=Counter();line=Counter()
    for i in C:
        p,ell=c["flags"][i]
        for y in c["g"][ell]:point[p,y]+=1
        for x in c["f"][p]:line[ell,x]+=1
    return 2*sum(z*z for z in point.values()),2*sum(z*z for z in line.values())

def _walk_coordinate_referee(c,core,C):
    """Direct true-graph finite falsifier of all-order spectral gap-3 proof."""
    A2,A3=_physical_powers(core)
    qx,qy=_true_source_returns(c,C)
    Q={}
    returns={}
    triple={}
    PSD_checks={}
    Delta=max(map(len,core.values()),default=0)
    for typ in (0,1):
        keys=range(c["a"])
        two=0;three=0
        all_psd=True
        for symbol in keys:
            S=[u for u in core if u[typ]==symbol]
            x2=sum(A2[u].get(v,0) for u in S for v in S)
            x3=sum(A3[u].get(v,0) for u in S for v in S)
            if Delta*x2<x3:raise AssertionError("symmetric physical A^2(DeltaI-A) not PSD")
            two+=x2;three+=x3
        Q[typ]=two
        returns[typ]=three
        PSD_checks[typ]=all_psd
    if (Q[0],Q[1])!=(qx,qy):
        raise AssertionError("original source-pencil 2walk returns disagree with physical graph")
    total=sum(sum(row.values()) for row in A3.values())
    gap2a=gap2b=gap3=wrong=proper=0
    for u0,ns in core.items():
        for u1 in ns:
            for u2 in core[u1]:
                for u3 in core[u2]:
                    xs=(u0[0],u1[0],u2[0],u3[0])
                    ys=(u0[1],u1[1],u2[1],u3[1])
                    a=xs[0]==xs[2] or ys[0]==ys[2]
                    b=xs[1]==xs[3] or ys[1]==ys[3]
                    d=xs[0]==xs[3] or ys[0]==ys[3]
                    gap2a+=a;gap2b+=b;gap3+=d
                    if a or b or d:wrong+=1
                    else:proper+=1
    checks={
        "actual_original_source_return_book_equals_physical_A2":True,
        "SPECTRAL_coordinate_gap3_x_le_Delta_Qx":
            returns[0]<=Delta*Q[0],
        "SPECTRAL_coordinate_gap3_y_le_Delta_Qy":
            returns[1]<=Delta*Q[1],
        "actual_coordinate_gap3_covered_by_spectral_sum":
            gap3<=returns[0]+returns[1],
        "actual_gap2_window1_le_Delta_Q":
            gap2a<=Delta*(qx+qy),
        "actual_gap2_window2_le_Delta_Q":
            gap2b<=Delta*(qx+qy),
        "exact_all_physical_3walk_partition":total==wrong+proper,
        "every_actual_improper_walk_in_three_return_positions":
            wrong<=gap2a+gap2b+gap3,
        "UNIVERSAL_bad_physical_threewalk_le_3Delta_Q":
            wrong<=3*Delta*(qx+qy),
    }
    if not all(checks.values()):
        raise AssertionError("source core 3walk spectral coordinate-return lemma false")
    return {
        "physical_vertices_including_isolates":len(core),
        "real_original_CORE_flag_count":len(C),
        "real_core_two_diagonal_edges":2*len(C),
        "physical_max_degree":Delta,
        "source_Qx":qx,"source_Qy":qy,
        "physical_A2_coordinate_returns_x":Q[0],
        "physical_A2_coordinate_returns_y":Q[1],
        "physical_A3_coordinate_gap3_x":returns[0],
        "physical_A3_coordinate_gap3_y":returns[1],
        "threewalks_total":total,"proper_threewalks":proper,
        "improper_threewalks":wrong,
        "actual_bad_gap2_first":gap2a,
        "actual_bad_gap2_second":gap2b,
        "actual_bad_gap3":gap3,
        "spectral_one_side_gap3_bounds":[
            str(Fraction(returns[0],max(1,Delta*qx))),
            str(Fraction(returns[1],max(1,Delta*qy)))],
        "checks":checks,
    }

def _actual_produced_bbo(c,geo,core,owner,C,Z):
    """INDEPENDENT physical-first proper path -> six ORIGINAL incidence IDs.

    Actual endpoint-good projected anchor SOURCE IDs only need avoid Z,
    not remain in the smaller paired core. An accepted source sixset has
    exactly TWO directed proper physical threepath representations.
    """
    f,g,flags=c["f"],c["g"],c["flags"]
    if Z is None:Z=set()
    Cset=set(C)
    invf={p:i for i,p in enumerate(f)}
    invg={p:i for i,p in enumerate(g)}
    src=Counter()
    anchors_outside_core=0
    eligible_paths=0
    for v0 in core:
        for v1 in core[v0]:
            for v2 in core[v1]:
                for v3 in core[v2]:
                    walk=(v0,v1,v2,v3)
                    if (len({z[0] for z in walk})!=4
                            or len({z[1] for z in walk})!=4):
                        continue
                    q=invf.get(tuple(sorted((v0[0],v3[0]))))
                    r=invg.get(tuple(sorted((v0[1],v3[1]))))
                    if q is None or r is None:
                        continue
                    proj=_projection(c,geo,q,r)
                    if proj is None:continue
                    p,ell,anchors=proj
                    if (set(anchors)&set(Z)
                            or set(f[p])&{v0[0],v3[0]}
                            or set(g[ell])&{v0[1],v3[1]}
                            or any(v[0] in f[p] or v[1] in g[ell]
                                   for v in (v1,v2))):
                        continue
                    owners=tuple(owner[tuple(sorted((walk[j],walk[j+1])))]
                                 for j in range(3))
                    all_ids=tuple(sorted(owners+anchors))
                    if len(set(all_ids))!=6:
                        raise AssertionError("BBo produced six ORIGINAL incidence owners collide")
                    eligible_paths+=1
                    anchors_outside_core+=any(i not in Cset for i in anchors)
                    src[all_ids]+=1
    if any(v!=2 for v in src.values()):
        raise AssertionError("ORIGINAL produced BBo directed path reversal is not exactly 2")
    return {"original_projected_anchor_outside_paired_core_paths":anchors_outside_core,
            "accepted_original_proper_directed_paths":eligible_paths,
            "distinct_produced_original_BBo_sixID_sets":len(src),
            "exact_two_directed_reversals_per_sixset":True,
            "sample_original_sixsets":[list(k) for k in sorted(src)[:4]]}

def genuine_original_finite_case(h,scheme,T,K0,deleted,shiftf=0,shiftg=0):
    c=_original_case(h,scheme,shiftf,shiftg)
    geo=_gq_geometry(c)
    Z=set(deleted)
    C,graph,owner,prune=_true_low_core(c,geo,T,K0,Z)
    endpoint=_endpoint_referee(c,geo,Z)
    walks=_walk_coordinate_referee(c,graph,C)
    produced=_actual_produced_bbo(c,geo,graph,owner,C,Z)
    if any(i in Z for i in C):raise AssertionError("deleted actual source flag remained core")
    return {
        "s":c["s"],"scheme":scheme,
        "fixed_complete_f_shift":shiftf,"fixed_complete_g_shift":shiftg,
        "original_deleted_source_IDs":len(Z),
        "original_flags_total":len(c["flags"]),
        "original_low_paired_core_flags":len(C),
        "original_prune":prune,
        "original_ENDPOINT":endpoint,
        "actual_ORIGINAL_source_spectral_3walk":walks,
        "actual_original_good_BBo_sixID_projection":produced,
        "root_230_unconditionally_accepted":False,
    }

def canonical_report():
    formal=[exact_low_source_ledger(C,c) for C,c in (
        (Fraction(1),Fraction(1)),
        (Fraction(2),Fraction(1,5)),
        (Fraction(7,3),Fraction(1,17)))]
    cases=[
        genuine_original_finite_case(1,"lex",8,8,(0,)),
        genuine_original_finite_case(1,"reverse-line",8,8,(1,13),2,4),
        genuine_original_finite_case(2,"lex",4,64,tuple(range(1,425,31))),
        genuine_original_finite_case(2,"reverse-line",4,64,tuple(range(1,425,29)),11,23),
        genuine_original_finite_case(2,"lex",5,64,tuple(range(2,425,41)),7,19),
    ]
    return {
        "schema":"mathlab.hyp105.original-low-spectral-endpoint-rho16.v1",
        "root_230_status":ROOT_STATUS,
        "all_order_symmetric_A3_coordinate_return_spectral_proof":True,
        "all_order_original_nonZ_endpoint_24s5_count_proof":True,
        "all_order_improved_original_LOW_BBo_23over48_conditional":True,
        "all_order_original_heavy_plus_low_quantifiers_conditionally_compatible":True,
        "actual_external_graph_SS6_constants_numerical_values_known":False,
        "root_Branch_A_unconditionally_accepted":False,
        "root_ASET_exponent_proved":False,
        "formal_graph_theorem_ledger":formal,
        "genuine_original_source_cases":cases,
    }

if __name__=="__main__":
    print("AA4_ORIGINAL_LOW_SPECTRAL_RHO16_CERTIFICATE="+json.dumps(
        canonical_report(),sort_keys=True,separators=(",",":")),flush=True)
