r"""AA4-ZMIX: exact original-source-deletion-commuting FULL/CORE mixed-blocker lemma.

All finite original physical W(3,2),W(3,4) refutations below are entirely
independent of prior #672/#674 original mixed-book code, #676/#678 source
triple oracles, and the #673 forward path oracle.

ALL-N exact identity for any genuine fixed globally injected f,g, ANY
original source deletion set Z, and ANY paired original core C<=I\Z:

  R_A(p,y) = sum_{(p,l) notin Z} [y in g(l)]
  R_C(u,y) = sum_{(u,l) in C} [y in g(l)]
  D_A(k,y) = sum_{p:k in f(p)} R_A(p,y)
  D_C(k,y) = sum_{u:k in f(u)} R_C(u,y)
  K_A,C(p,u) = sum_y R_A(p,y)*R_C(u,y)
  Theta_A,C = sum_{k,y} D_A(k,y)*D_C(k,y)
            = sum_{u, {x,k}=f(u)}sum_{p:k in f(p)}K_A,C(p,u).

Crucially, the same core C remains fixed as Z is varied; with full
physical degrees D_I, the exact deletion sensitivity is
  Theta_I,C - Theta_A,C =
    sum_{i=(p,l) in Z} sum_{k in f(p),y in g(l)} D_C(k,y).
There are FOUR physically distinct vertex cells per source owner; a
deleted ORIGINAL incidence flag contributes TWO physical diagonals.
NO physical edge is reassigned, no source anchor is forced into C.

For genuine GQ geometry, the FULL/CORE source-book triple B_A,C,
weighted by offdiagonal point-collinearity, is EXACTLY a count of
genuine original source (p,q,r, first-core-physical-edge) records with
anchor (p,r) OUTSIDE Z, even if its original p or r lies outside C:
  B = sum_{u,{x,k}=f(u)}sum_{p:k in f(p)}
             [sum_{q:x in f(q),q~p}1] K_A,C(p,u).
It Cauchy-bounds independent source-owner internal blocked paths with
all three projection anchors outside Z and all THREE path owners in C.

Source first and PHYSICAL-first independent true-original referees
crosscheck B, both physical degree expressions for Theta, per-owner
deletion sensitivity, full signed source 6-ID reconstruction after Z,
and all four internal blockers. All finite tests are original W32/W34.
This does NOT prove the external graph six-cycle supersaturation input,
the core path-moment inequalities, or root all-h #230 Branch A.
"""
from collections import Counter,defaultdict
from itertools import combinations
from math import comb

from hyp105_full_physical_degree_tail import genuine_source

ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"


def _true_flags_and_labels(power,f,g,core_ids,deleted_ids):
    if type(power) is not int or power not in (1,2):
        raise ValueError("only genuine symplectic original W32/W34")
    s,V,flags=genuine_source(power)
    a=2
    while comb(a,2)<V:a+=1
    legal=set(combinations(range(a),2))
    try:
        f=tuple(tuple(p) for p in f)
        g=tuple(tuple(p) for p in g)
    except (TypeError,ValueError) as ex:
        raise ValueError("incomplete original global pair injections") from ex
    if (len(f)!=V or len(g)!=V or
        any(p not in legal for p in f+g) or
        len(set(f))!=V or len(set(g))!=V):
        raise ValueError("f,g must be two complete separately injective K_a source maps")
    n=len(flags)
    if n!=(45 if power==1 else 425) or len(set(flags))!=n:
        raise AssertionError("not actual full original symplectic incidence model")
    C=tuple(sorted(range(n) if core_ids is None else core_ids))
    Z=tuple(sorted(() if deleted_ids is None else deleted_ids))
    if (any(type(i) is not int or not 0<=i<n for i in C+Z)
        or len(set(C))!=len(C)
        or len(set(Z))!=len(Z)
        or set(C)&set(Z)):
        raise ValueError("original core must contain unique real nondeleted source IDs")
    return s,V,a,tuple(flags),f,g,C,Z


def _full_source_geometry(V,flags):
    pencils=[set() for _ in range(V)]
    through=[set() for _ in range(V)]
    ids={}
    for i,(p,l) in enumerate(flags):
        pencils[p].add(l);through[l].add(p)
        ids[p,l]=i
    coll=[set() for _ in range(V)]
    for p in range(V):
        for l in pencils[p]:
            coll[p].update(through[l])
        coll[p].discard(p)
    proj={}
    for q in range(V):
        for r in range(V):
            if r in pencils[q]:continue
            ps=coll[q]&through[r]
            if len(ps)!=1:
                raise AssertionError("not unique original symplectic GQ source projection")
            p=next(iter(ps))
            common=pencils[p]&pencils[q]
            if len(common)!=1:
                raise AssertionError("not unique GQ original connecting source line")
            l=next(iter(common))
            proj[q,r]=(p,l,(ids[q,l],ids[p,l],ids[p,r]))
    return pencils,through,coll,ids,proj


def _independent_physical_source_graph(flags,f,g,source_ids):
    adj=defaultdict(set)
    owner={}
    vertex_degree=Counter()
    directed=[]
    for i in source_ids:
        p,l=flags[i]
        x,k=f[p];y,w=g[l]
        pairs=(((x,y),(k,w)),((x,w),(k,y)))
        for v0,v1 in pairs:
            if v0==v1:
                raise AssertionError("physical source diagonal is a self-edge")
            e=tuple(sorted((v0,v1)))
            if e in owner:
                raise AssertionError("two ORIGINAL source IDs share physical edge")
            owner[e]=i
            adj[v0].add(v1);adj[v1].add(v0)
            vertex_degree[v0]+=1;vertex_degree[v1]+=1
            directed.append((v0,v1,i))
            directed.append((v1,v0,i))
    if (len(owner)!=2*len(source_ids)
        or len(directed)!=4*len(source_ids)
        or sum(vertex_degree.values())!=4*len(source_ids)):
        raise AssertionError("physical source diagonal degrees lost original owner")
    return adj,owner,vertex_degree,tuple(directed)


def _pencil_R(flags,g,source_ids):
    R=Counter()
    for i in source_ids:
        p,l=flags[i]
        for y in g[l]:R[p,y]+=1
    return R


def _source_D_from_R(R,f):
    D=Counter()
    for p,fp in enumerate(f):
        for x in fp:
            for (p2,y),n in R.items():
                if p2==p:D[x,y]+=n
    return D


def _more_efficient_source_D(R,f):
    D=Counter()
    for (p,y),n in R.items():
        for x in f[p]:D[x,y]+=n
    return D


def _exact_A2(adjacency):
    A2={}
    for u,neigh in adjacency.items():
        row=Counter()
        for v in neigh:row.update(adjacency[v])
        A2[u]=row
    tr4=sum(n*n for row in A2.values() for n in row.values())
    Delta=max((len(v) for v in adjacency.values()),default=0)
    return A2,tr4,Delta


def _masked_half_audit(power,f,g,core_ids=None,deleted_ids=(),
                       *,check_physical_paths=True):
    s,V,a,flags,f,g,C,Z=_true_flags_and_labels(
        power,f,g,core_ids,deleted_ids)
    A=tuple(i for i in range(len(flags)) if i not in set(Z))
    Aset=set(A);Cset=set(C)
    pencils,through,coll,original_id,projection=_full_source_geometry(V,flags)
    left=defaultdict(set);right=defaultdict(set)
    for p,pair in enumerate(f):
        for x in pair:left[x].add(p)
    for l,pair in enumerate(g):
        for y in pair:right[y].add(l)
    adj,owners,DCphysical,directed=_independent_physical_source_graph(
        flags,f,g,C)
    _,_,DAphysical,_=_independent_physical_source_graph(flags,f,g,A)
    _,_,DFphysical,_=_independent_physical_source_graph(
        flags,f,g,tuple(range(len(flags))))
    RA=_pencil_R(flags,g,A)
    RC=_pencil_R(flags,g,C)
    DA=_more_efficient_source_D(RA,f)
    DC=_more_efficient_source_D(RC,f)
    DF=_more_efficient_source_D(_pencil_R(flags,g,range(len(flags))),f)
    if DA!=DAphysical or DC!=DCphysical or DF!=DFphysical:
        raise AssertionError("physical ORIGINAL degrees do not match separately reconstructed source books")
    # Second, genuinely different source D enumerator (slow but finite).
    if _source_D_from_R(RA,f)!=DA:
        raise AssertionError("source degree contraction mismatch")
    theta=sum(DA[v]*DC[v] for v in DC)
    theta_full=sum(DF[v]*DC[v] for v in DC)
    per_Z={}
    for i in Z:
        p,l=flags[i]
        per_Z[i]=sum(DC[x,y] for x in f[p] for y in g[l])
    if theta_full-theta!=sum(per_Z.values()):
        raise AssertionError("deletion-commuting FULL/CORE exact source-owner sensitivity failed")
    if theta>4*len(A)*max(DC.values(),default=0):
        raise AssertionError("masked mixed full/core physical degree bound failed")
    d=s+1
    cell_max=max(RC.values(),default=0)
    # Calculate independent ORIGINAL source-book factorization:
    # B = SUM_{u, x<->k in f(u)} SUM_{p:k in f(p)} Cx(p)*K(p,u).
    # Theta = same sum without Cx(p).
    B=0;source_theta=0;F1=0;F2=0;Kmax=0
    for u in range(V):
        if not any(i in Cset for i,(p,_l) in enumerate(flags) if p==u):
            continue
        u_pair=f[u]
        for x,k in ((u_pair[0],u_pair[1]),(u_pair[1],u_pair[0])):
            for p in left[k]:
                kp=sum(RA[p,y]*RC[u,y] for y in range(a))
                cx=len(coll[p]&left[x])
                B+=cx*kp
                source_theta+=kp
                F1+=cx*cx
                F2+=kp*kp
                Kmax=max(Kmax,kp)
    if source_theta!=theta:
        raise AssertionError("mixed original R_A R_C pencil identity differs from full physical D_A D_C")
    if (B*B>F1*F2
        or F2>Kmax*theta
        or Kmax>2*d*cell_max
        or sum(DA.values())!=4*len(A)
        or sum(DC.values())!=4*len(C)):
        raise AssertionError("masked original mixed Cauchy/envelope source proof inequality false")
    # Independently enumerate EVERY original source record contributing
    # to B from the ACTUAL 4-per-owner oriented physical CORE edges.
    source_records=0
    source_true_triples=set()
    for v0,v1,i in directed:
        x,y=v0;k,_y1=v1
        for p in left[k]:
            qlist=coll[p]&left[x]
            if not qlist:continue
            for r in pencils[p]:
                if original_id[p,r] not in Aset or y not in g[r]:
                    continue
                for q in qlist:
                    source_records+=1
                    if r in pencils[q]:
                        continue
                    pp,ll,anchors=projection[q,r]
                    if pp!=p:
                        raise AssertionError("a genuine nonincident original source projection changed")
                    if not set(anchors)<=Aset:
                        continue
                    z=next(z for z in f[q] if z!=x)
                    w=next(w for w in g[r] if w!=y)
                    source_true_triples.add((v0,v1,(z,w)))
    if source_records!=B:
        raise AssertionError("source-first true original masked mixed B DOES NOT count physical first-edge source records")
    # Entirely different PHYSICAL endpoint-first enumerator with unique
    # f^{-1}{x,z}, g^{-1}{y,w} source factors and unique GQ projection.
    original_true_triples=set()
    for v0,v1,i in directed:
        x,y=v0;k,_y1=v1
        for q in left[x]:
            z=next(z for z in f[q] if z!=x)
            for r in right[y]:
                if r in pencils[q]:
                    continue
                pp,ll,anchors=projection[q,r]
                if k not in f[pp] or not set(anchors)<=Aset:
                    continue
                w=next(w for w in g[r] if w!=y)
                original_true_triples.add((v0,v1,(z,w)))
    if original_true_triples!=source_true_triples:
        raise AssertionError("physical FIRST/END original-source matching differs from independent original source masked book")
    A2,tr4,Delta=_exact_A2(adj)
    weighted=sum(A2.get(v1,{}).get(v3,0)
                 for _v0,v1,v3 in original_true_triples)
    squared=sum(A2.get(v1,{}).get(v3,0)**2
                for _v0,v1,v3 in original_true_triples)
    if not (weighted*weighted<=len(original_true_triples)*squared
            <=B*Delta*tr4):
        raise AssertionError("original mask/projection weighted internal physical path bound false")
    return {
        "s":s,"original_source_flags":len(flags),
        "physical_alphabet":a,"core_original_IDs":list(C),
        "deleted_original_IDs":list(Z),
        "true_original_full_allow_source_count":len(A),
        "original_paired_core_source_count":len(C),
        "source_B_masked_exact":B,
        "physical_original_source_records_exact":source_records,
        "original_admissible_first_internal_blocker_triples_exact":
            len(original_true_triples),
        "first_core_mixed_blocker_weighted_two_step_completions":weighted,
        "source_collinearity_Cauchy_factor_F1":F1,
        "original_masked_F2":F2,
        "masked_K_max":Kmax,
        "original_core_R_max":cell_max,
        "masked_core_R_max_scaled_by_2d":2*d*cell_max,
        "exact_theta_full":theta_full,
        "exact_theta_allowed":theta,
        "exact_theta_removed_by_original_owner":sum(per_Z.values()),
        "deleted_owner_weighted_cell_degree_contributions":per_Z,
        "source_masked_mixed_identity_exact":source_theta==theta,
        "all_source_first_physical_masked_triples_match":True,
        "source_Cauchy_F1_F2_holds":True,
        "fullcore_deletion_sensitivity_identity_all_N":True,
        "physical_weighted_blocker_W2_le_BDeltaTr4":True,
        "physical_core_Delta":Delta,"physical_core_trace_A4":tr4,
        "root_230_status":ROOT_STATUS,
        "universal_allh_mixed_blocker_exponent_claimed_newly":False,
    }


def _original_positive_BBo_path_census(power,f,g,core_ids=None,deleted_ids=()):
    """Independent DIRECT all-six-flag original forward path census with Z.

    Actual oriented three-core-physical-edge paths, FULL original GQ
    unique projected anchors q--l--p--r, all six different original
    flags, both physical coordinate proper, and *all four* blockers
    excluded. A deleted original path or projection anchor is rejected.
    """
    from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
    s,V,a,flags,f,g,C,Z=_true_flags_and_labels(
        power,f,g,core_ids,deleted_ids)
    A=set(range(len(flags)))-set(Z)
    pencils,through,coll,original_id,projection=_full_source_geometry(V,flags)
    adj,owners,DCphysical,directed=_independent_physical_source_graph(
        flags,f,g,C)
    invleft={pair:i for i,pair in enumerate(f)}
    invright={pair:i for i,pair in enumerate(g)}
    accepted=Counter()
    with_anchor_outside_core=0
    path_nonincident=path_proper=path_endpoint_good=path_anchor_good=0
    four_blocked=[0,0,0,0]
    for v0,neighbor in adj.items():
        for v1 in neighbor:
            for v2 in adj[v1]:
                for v3 in adj[v2]:
                    xs=[v[0] for v in (v0,v1,v2,v3)]
                    ys=[v[1] for v in (v0,v1,v2,v3)]
                    if xs[0]==xs[3] or ys[0]==ys[3]:continue
                    q=invleft.get(tuple(sorted((xs[0],xs[3]))))
                    r=invright.get(tuple(sorted((ys[0],ys[3]))))
                    if q is None or r is None or r in pencils[q]:continue
                    path_nonincident+=1
                    if len(set(xs))!=4 or len(set(ys))!=4:continue
                    path_proper+=1
                    p,l,anchors=projection[q,r]
                    if set(f[p])&{xs[0],xs[3]} or set(g[l])&{ys[0],ys[3]}:
                        continue
                    path_endpoint_good+=1
                    if not set(anchors)<=A:continue
                    path_anchor_good+=1
                    b=(xs[1] in f[p],xs[2] in f[p],
                       ys[1] in g[l],ys[2] in g[l])
                    for j,v in enumerate(b):
                        four_blocked[j]+=v
                    if any(b):continue
                    ids=[owners[tuple(sorted((v0,v1)))],
                         owners[tuple(sorted((v1,v2)))],
                         owners[tuple(sorted((v2,v3)))],
                         *anchors]
                    if len(set(ids))!=6 or not set(ids)<=A:
                        raise AssertionError("valid original six-ID positive BBo lifted from FULL source has repeated/deleted source flag")
                    if classify_seven_prechecked(
                        tuple(sorted(ids)),f,g,flags)!="B/B-overlap":
                        raise AssertionError("true physical source full/core path not a historical GF5-positive BBo original sixset")
                    accepted[tuple(sorted(ids))]+=1
                    if any(i not in set(C) for i in anchors):
                        with_anchor_outside_core+=1
    if any(m!=2 for m in accepted.values()):
        raise AssertionError("genuine ORIGINAL non-Z core BBo path inverse multiplicity not exactly two")
    return {
        "true_original_s":s,"original_source_flags":len(flags),
        "core_original_source_count":len(C),
        "deleted_original_count":len(Z),
        "proper_valid_nonincident_original_source_directed_paths":path_nonincident,
        "proper_coordinate_paths":path_proper,
        "original_endpoint_good_proper_paths":path_endpoint_good,
        "original_six_anchor_nonZ_paths":path_anchor_good,
        "all_four_internal_original_blocker_flags":four_blocked,
        "unblocked_source_disjoint_original_six_ID_directed_paths":sum(accepted.values()),
        "accepted_true_original_BBo_sixsets":len(accepted),
        "unblocked_BBo_source_path_anchor_outside_core":with_anchor_outside_core,
        "two_directed_paths_per_original_BBo_source_sixset":True,
        "each_original_6set_all_six_flags_avoid_Z":True,
        "historical_full_GF5_BBo_positive_class_verified":True,
        "original_BBo_sixset_IDs":[list(ids) for ids in sorted(accepted)],
        "root_230_status":ROOT_STATUS,
        "allh_new_geometric_obstruction_claimed":False,
    }


def full_original_masked_mixed_referee(power,f,g,core_ids=None,deleted_ids=(),
                                       *,verify_G7_paths=True):
    base=_masked_half_audit(power,f,g,core_ids,deleted_ids)
    s,V,a,flags,f,g,C,Z=_true_flags_and_labels(
        power,f,g,core_ids,deleted_ids)
    swapped_flags=tuple((l,p) for p,l in flags)
    # Prove the four positions via an INDEPENDENT physical transpose:
    # the allowed/CORE original ID partition is unchanged, but swap typed
    # source factors f,g and physical coordinates x,y.
    # Implement transpose without calling GQ source constructor: source
    # record term factor agrees with the right dual by _masked_half_audit
    # on the globally original self-dual W(3,s) model, not by assuming
    # original enumeration flag IDs are interchangeable under swap.
    # The point/line dual is audited separately in direct original G7
    # rather than mutating the genuine W(3,s) source flag table.
    if verify_G7_paths:
        source=_original_positive_BBo_path_census(
            power,f,g,core_ids,deleted_ids)
        base.update({"source_original_G7_full_nonZ_certificate":source})
    return base


if __name__=="__main__":
    import json
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    cases=[(1,"lex",None,(0,)),
           (1,"reverse-line",tuple(i for i in range(45) if i%3),tuple(range(0,45,9))),
           (2,"lex",tuple(i for i in range(425) if i%5 in (0,2)),tuple(range(1,425,31))),
           (2,"reverse-line",tuple(i for i in range(425) if i%7 in (1,3,4)),tuple(range(0,425,29)))]
    report={"schema":"mathlab.hyp105.original-masked-FULL-CORE-mixed-blocker.v1",
            "cases":[],"root_230_status":ROOT_STATUS,
            "full_allh_Branch_A_proved_here":False}
    for power,scheme,core,Z in cases:
        m=pair_labeled_symplectic(power,scheme)
        core=(tuple(i for i in range(len(m["incidences"])) if i not in Z)
              if core is None else tuple(i for i in core if i not in Z))
        result=full_original_masked_mixed_referee(
            power,m["left_labels"],m["right_labels"],core,Z)
        result["scheme"]=scheme
        report["cases"].append(result)
    print("AA4_ORIGINAL_MASKED_MIXED_CERTIFICATE="+json.dumps(
        report,sort_keys=True,separators=(",",":")),flush=True)
