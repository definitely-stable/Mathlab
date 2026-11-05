r"""AA4-LOWCERT: all-N exact ORIGINAL source deletion-aware LOW-tail inequality.

For any genuine symplectic W(3,s), any complete separately globally
injected and ARBITRARILY CORRELATED fixed f,g, any deleted ORIGINAL
incidence flag IDs Z and any paired core C<=I\Z, let H_C have BOTH real
physical diagonals per retained source flag.

NEW independent finite-N inequality (no external balanced SS6 needed):
  2 * (#accepted original surviving B/B-overlap sixsets)
  >= max(0, (4|C|)^3/a^4 -3 Delta (Qx+Qy)
       -sqrt(Ebad * ||P3||_F^2)
       -2 sqrt(Bx Delta tr(A_C^4))
       -2 sqrt(By Delta tr(A_C^4))).
Here Ebad is the EXACT number of ordered first/last physical
coordinates corresponding to missing original point/line factor pairs,
incident original (q,r), endpoint bad source GQ projection or any of
its THREE genuinely deleted original projection IDs. P3 is the true
ordered coordinate-proper physical core 3-path endpoint tensor.

Bx is the masked ORIGINAL point-collinearity FULL-allowed/CORE
mixed source book using ORIGINAL nondeleted flags I\Z as the full
anchor population; By is its TRUE SOURCE POINT/LINE DUAL. No source
projection anchor is forced into C, and all 3 path edge owners are
ALREADY in the Z-free paired core.

All quantities are exact rational / integer, and the theorem holds
without a random selector, any graph supersaturation input, a
numerical published C_graph or a small-D6 hypothesis. It is a
low-tail SOURCE certificate, NOT itself a positive lower bound for
EVERY map in all-h #230. To force Omega(s^6), the source core caps,
original selected-graph moment and source collinearity bounds must
separately show the right side positive. Existing #672/#674 provide
a claimed all-h route, which remains scientific Draft.

Finite referee independently reconstructs ORIGINAL W32/W34 source
geometry, both physical diagonals, true 3-edge physical walks,
source projection (q--ell--p--r), properness, 4 internal blockers,
all SIX source incidence IDs, historical GF5-positive BBo class,
the EXACT disjoint exceptional/mask source-endpoint partition,
both DUAL fullcore original masked source B books, Qx/Qy and tr A4.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb,isqrt

from hyp105_full_physical_degree_tail import genuine_source
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked

ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"


def _ceil_sqrt(x):
    if type(x) is not int or x<0:
        raise ValueError("only nonnegative exact integer physical energy")
    z=isqrt(x)
    return z+(z*z<x)


def _source(power,f,g,C,Z):
    if type(power) is not int or power not in (1,2):
        raise ValueError("finite physical proof only REAL original W32/W34")
    s,V,flags=genuine_source(power)
    a=2
    while comb(a,2)<V:a+=1
    legal=set(combinations(range(a),2))
    try:
        f=tuple(tuple(u) for u in f)
        g=tuple(tuple(u) for u in g)
    except (TypeError,ValueError) as ex:
        raise ValueError("typed global source pair maps missing") from ex
    if len(f)!=V or len(g)!=V or len(set(f))!=V or len(set(g))!=V or any(
            q not in legal for q in f+g):
        raise ValueError("both global ORIGINAL maps must be separately pair-injective and complete")
    C=tuple(range(len(flags))) if C is None else tuple(C)
    Z=tuple(() if Z is None else Z)
    if (len(C)!=len(set(C)) or len(Z)!=len(set(Z)) or
        any(type(i) is not int or not 0<=i<len(flags) for i in C+Z) or
        set(C)&set(Z)):
        raise ValueError("CORE ORIGINAL flags and deleted ORIGINAL IDs must be disjoint and unique")
    return s,V,a,tuple(flags),f,g,tuple(sorted(C)),tuple(sorted(Z))


def _original_geometry(flags,V):
    pt=[set() for _ in range(V)]
    ln=[set() for _ in range(V)]
    lookup={}
    for i,(p,l) in enumerate(flags):
        pt[p].add(l);ln[l].add(p);lookup[p,l]=i
    col=[]
    for q in range(V):
        ps=set()
        for l in pt[q]:ps.update(ln[l])
        ps.discard(q)
        col.append(ps)
    projected={}
    for q in range(V):
        for r in range(V):
            if r in pt[q]:continue
            meeting=col[q]&ln[r]
            if len(meeting)!=1:
                raise AssertionError("genuine original GQ source projection not unique")
            p=next(iter(meeting))
            ell=pt[p]&pt[q]
            if len(ell)!=1:
                raise AssertionError("genuine original source GQ connecting line absent")
            ell=next(iter(ell))
            projected[q,r]=(p,ell,(lookup[q,ell],lookup[p,ell],lookup[p,r]))
    return pt,ln,lookup,col,projected


def _true_physical(flags,f,g,C,a):
    graph={(x,y):set() for x in range(a) for y in range(a)}
    owner={}
    for i in C:
        p,l=flags[i];x,k=f[p];y,w=g[l]
        for v,u in (((x,y),(k,w)),((x,w),(k,y))):
            e=tuple(sorted((v,u)))
            if v==u or e in owner:
                raise AssertionError("duplicate physical edge owner or invalid original diagonal")
            owner[e]=i
            graph[v].add(u);graph[u].add(v)
    if len(owner)!=2*len(C) or sum(map(len,graph.values()))!=4*len(C):
        raise AssertionError("source must own exactly two physical diagonals")
    return graph,owner


def _pencil_return(flags,f,g,C,a):
    rpoint=Counter()
    rline=Counter()
    for i in C:
        p,l=flags[i]
        for y in g[l]:rpoint[p,y]+=1
        for x in f[p]:rline[l,x]+=1
    Qx=2*sum(v*v for v in rpoint.values())
    Qy=2*sum(v*v for v in rline.values())
    return Qx,Qy


def _mixed_original_B(flags,f,g,C,Z,V,a):
    """FULL=I\\Z, paired CORE=C; actual source collinearity weighted B.

    This argument is symmetric under TRUE source GQ point/line
    dualization; applying with swapped genuine typed factors computes
    the independent other physical coordinate blocker family.
    """
    A=tuple(i for i in range(len(flags)) if i not in set(Z))
    pt,ln,lookup,col,proj=_original_geometry(flags,V)
    S=[set() for _ in range(a)]
    for p,fp in enumerate(f):
        for x in fp:S[x].add(p)
    RA=Counter();RC=Counter()
    for ids,book in ((A,RA),(C,RC)):
        for i in ids:
            p,l=flags[i]
            for y in g[l]:book[p,y]+=1
    corepts={flags[i][0] for i in C}
    B=0
    theta=0
    F1=0
    F2=0
    for u in corepts:
        x,k=f[u]
        for x,k in ((x,k),(k,x)):
            for p in S[k]:
                K=sum(RA[p,y]*RC[u,y] for y in range(a))
                cx=len(S[x]&col[p])
                B+=cx*K
                theta+=K
                F1+=cx*cx
                F2+=K*K
    return {"B":B,"Theta":theta,"F1":F1,"F2":F2,
            "source_mixed_book_Cauchy":B*B<=F1*F2}


def _physical_trace_and_three_walks(graph):
    degrees={v:len(ns) for v,ns in graph.items()}
    Delta=max(degrees.values(),default=0)
    A2={v:Counter() for v in graph}
    for u in graph:
        for mid in graph[u]:
            A2[u].update(graph[mid])
    trace4=sum(n*n for row in A2.values() for n in row.values())
    walks3=sum(degrees[u]*degrees[v] for u in graph for v in graph[u])
    return Delta,trace4,walks3,A2


def _endpoint_mask(a,flags,f,g,Z,V):
    """Exactly classify ALL off-row/off-col ordered physical endpoints."""
    pt,ln,lookup,col,projected=_original_geometry(flags,V)
    invf={pair:p for p,pair in enumerate(f)}
    invg={pair:l for l,pair in enumerate(g)}
    sets={kind:set() for kind in
          ("missing","incident","source_end_bad","deleted_projection","admissible")}
    projected_meta={}
    for x in range(a):
        for z in range(a):
            if x==z:continue
            q=invf.get(tuple(sorted((x,z))))
            for y in range(a):
                for w in range(a):
                    if y==w:continue
                    r=invg.get(tuple(sorted((y,w))))
                    endpoints=((x,y),(z,w))
                    if q is None or r is None:
                        kind="missing"
                    elif r in pt[q]:
                        kind="incident"
                    else:
                        p,ell,anchors=projected[q,r]
                        if set(f[p])&{x,z} or set(g[ell])&{y,w}:
                            kind="source_end_bad"
                        elif any(i in Z for i in anchors):
                            kind="deleted_projection"
                        else:
                            kind="admissible"
                            projected_meta[endpoints]=(p,ell,anchors)
                    sets[kind].add(endpoints)
    expected=a*a*(a-1)*(a-1)
    if sum(map(len,sets.values()))!=expected:
        raise AssertionError("complete ordered real original source endpoint partition not disjoint")
    bad=set().union(*(sets[k] for k in (
        "missing","incident","source_end_bad","deleted_projection")))
    if len(bad)+len(sets["admissible"])!=expected:
        raise AssertionError("original source projected endpoint mask not exhaustive")
    return sets,bad,projected_meta


def full_original_lowtail_source_energy_certificate(power,f,g,core_ids=None,deleted_ids=()):
    s,V,a,flags,f,g,C,Z=_source(power,f,g,core_ids,deleted_ids)
    graph,owner=_true_physical(flags,f,g,C,a)
    Delta,trace4,walk3,A2=_physical_trace_and_three_walks(graph)
    Qx,Qy=_pencil_return(flags,f,g,C,a)
    sets,bad,meta=_endpoint_mask(a,flags,f,g,set(Z),V)
    Bx=_mixed_original_B(flags,f,g,C,Z,V,a)
    Bdual=_mixed_original_B(
        tuple((l,p) for p,l in flags),g,f,C,Z,V,a)
    if not Bx["source_mixed_book_Cauchy"] or not Bdual["source_mixed_book_Cauchy"]:
        raise AssertionError("source dual masked FULL/CORE mixed Cauchy false")
    # Distinct exact physical source short-path endpoint P3 tensor.
    P3=Counter()
    blocked=[0,0,0,0]
    actually_admissible=0
    genuine_BBo=Counter()
    actual3=0
    for v0 in graph:
        for v1 in graph[v0]:
            for v2 in graph[v1]:
                for v3 in graph[v2]:
                    actual3+=1
                    path=(v0,v1,v2,v3)
                    if (len({v[0] for v in path})!=4 or
                        len({v[1] for v in path})!=4):
                        continue
                    endpoints=(v0,v3)
                    P3[endpoints]+=1
                    if endpoints in bad:continue
                    actually_admissible+=1
                    p,ell,anchors=meta[endpoints]
                    bs=(v1[0] in f[p],v2[0] in f[p],
                        v1[1] in g[ell],v2[1] in g[ell])
                    for j,b in enumerate(bs):
                        if b:blocked[j]+=1
                    if any(bs):continue
                    ids=tuple(sorted([
                        owner[tuple(sorted((v0,v1)))],
                        owner[tuple(sorted((v1,v2)))],
                        owner[tuple(sorted((v2,v3)))],
                        *anchors]))
                    if (len(set(ids))!=6 or set(ids)&set(Z)
                        or classify_seven_prechecked(ids,f,g,flags)!="B/B-overlap"):
                        raise AssertionError("actual physical unblocked original path did NOT reconstruct historical positive six-ID BBo source motif")
                    genuine_BBo[ids]+=1
    if actual3!=walk3:
        raise AssertionError("independent true physical 3-walk census differs from direct degree convolution")
    if any(n!=2 for n in genuine_BBo.values()):
        raise AssertionError("original positive six-ID BBo path representation multiplicity not exactly 2")
    for v,j in ((1,0),(2,1),(3,2),(4,3)):
        # Original ordinary physical 2-step middle completions upper:
        # each single blocked position admits at most
        # sqrt(Bx/y * Delta * tr(A_C^4)) physical 3-walks.
        book=Bx["B"] if v<=2 else Bdual["B"]
        if blocked[j]**2>book*Delta*trace4:
            raise AssertionError("original full/core masked geometric 4-blocker physically falsified")
    normP3=sum(z*z for z in P3.values())
    bad_mass=sum(P3[e] for e in bad)
    if bad_mass**2>len(bad)*normP3:
        raise AssertionError("original bad projected endpoint Cauchy energy invalid")
    if actually_admissible!=sum(P3.values())-bad_mass:
        raise AssertionError("source original endpoint mask/actual core P3 mass mismatch")
    good=2*len(genuine_BBo)
    blocked_union=actually_admissible-good
    if blocked_union<0 or blocked_union>sum(blocked):
        raise AssertionError("unblocked historical six-ID BBo source path count inconsistent")
    if (len(P3)!=len(set(P3)) or
        sum(P3.values())>actual3 or
        actual3-sum(P3.values())>3*Delta*(Qx+Qy)):
        raise AssertionError("original full/core proper third-walk coordinate-return bound false")
    energy_ceiling=2*_ceil_sqrt(Bx["B"]*Delta*trace4)+2*_ceil_sqrt(
        Bdual["B"]*Delta*trace4)
    if blocked_union>energy_ceiling:
        raise AssertionError("independent dual source-masked FULL/CORE 4 blockers do not cover internal invalid paths")
    bad_ceiling=_ceil_sqrt(len(bad)*normP3)
    BlakleyRoy=Fraction((4*len(C))**3,a**4)
    if actual3<BlakleyRoy:
        raise AssertionError("all-N positive adjacency A^3 density floor false")
    improper_ceiling=3*Delta*(Qx+Qy)
    proper=len(P3) and sum(P3.values()) or 0
    lower_raw=BlakleyRoy-improper_ceiling-bad_ceiling-energy_ceiling
    direct_lower=proper-bad_mass-energy_ceiling
    if good<lower_raw or good<direct_lower:
        raise AssertionError("all-N original source lowtail six-ID BBo energy inequality falsified")
    # Stronger fully OBSERVABLE one-sided certificate with actual masses:
    # good = proper - bad_mass - blocked_union, exact source IDs.
    if good!=proper-bad_mass-blocked_union:
        raise AssertionError("original positive source BBo exact path partition false")
    # Decoupled source/dual book F1*F2 guards:
    if (Bx["B"]**2>Bx["F1"]*Bx["F2"]
        or Bdual["B"]**2>Bdual["F1"]*Bdual["F2"]):
        raise AssertionError("point/line full/core physical original energy Cauchy false")
    return {
        "schema":"mathlab.hyp105.original-lowtail-allN-Z-masked-energy.v1",
        "s":s,"scheme":None,"original_source_flags":len(flags),
        "original_core_source_IDs":list(C),
        "deleted_original_flag_IDs":list(Z),
        "physical_alphabet":a,
        "original_core_source_count":len(C),
        "physical_real_edge_count":len(owner),
        "physical_full_graph_ordered_3walks":actual3,
        "physical_proper_ordered_3paths":proper,
        "physical_improper_3walks":actual3-proper,
        "physical_improper_3walks_max_3DeltaQ":improper_ceiling,
        "physical_original_core_max_Delta":Delta,
        "original_source_Qx":Qx,"original_source_Qy":Qy,
        "physical_trace_A4":trace4,
        "original_exact_exception_endpoint_partition":
            {k:len(v) for k,v in sets.items()},
        "original_bad_endpoint_union_size":len(bad),
        "actual_original_bad_endpoint_path_mass":bad_mass,
        "exact_original_proper3_endpoint_Frobenius_square":normP3,
        "bad_endpoint_Cauchy_integer_upper":bad_ceiling,
        "original_masked_POINT_source_B":Bx,
        "original_masked_LINE_dual_source_B":Bdual,
        "physical_four_separate_internal_original_blocker_paths":blocked,
        "physical_internal_original_blocked_path_union":blocked_union,
        "source_dual_four_blocker_Cauchy_integer_upper":energy_ceiling,
        "exact_original_admissible_endpoint_proper3_path_mass":
            actually_admissible,
        "actual_original_good_unblocked_directed3":good,
        "real_positive_original_BBo_sixsets":len(genuine_BBo),
        "real_positive_original_BBo_six_IDs":[list(x) for x in sorted(genuine_BBo)],
        "physical_three_walk_Blackley_Roy_density_fraction":
            str(BlakleyRoy),
        "all_N_fully_observable_good3_lower":str(direct_lower),
        "all_N_abstract_energy_good3_lower":str(lower_raw),
        "all_N_complete_original_source_path_partition":True,
        "all_N_symmetric_original_masked_four_blocker_bound":True,
        "all_N_TRUE_ORIGINAL_lowtail_condition_valid_even_if_negative":True,
        "allh_positive_root_Branch_A_proved_here":False,
        "root_230_status":ROOT_STATUS,
    }


def canonical_original_lowtail_allN():
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    cases=[
        (1,"lex",tuple(i for i in range(45) if i%3!=0),(0,)),
        (1,"reverse-line",tuple(i for i in range(45) if i%4 in (0,1,3)),(2,)),
        (2,"lex",tuple(i for i in range(425) if i%5 in (0,2,4)),tuple(range(1,425,31))),
        (2,"reverse-line",tuple(i for i in range(425) if i%7 in (0,1,4)),tuple(range(0,425,29))),
    ]
    results=[]
    for h,scheme,C,Z in cases:
        source=pair_labeled_symplectic(h,scheme)
        C=tuple(i for i in C if i not in Z)
        r=full_original_lowtail_source_energy_certificate(
            h,source["left_labels"],source["right_labels"],C,Z)
        r["scheme"]=scheme
        results.append(r)
    return {"schema":"mathlab.hyp105.original-LOWTAIL-allN-energy-source.v1",
            "genuine_true_original_cases":results,
            "allh_unconditional_ROOT_230_claim":False,
            "root_230_status":ROOT_STATUS}


if __name__=="__main__":
    import json
    print("AA4_TRUE_ORIGINAL_ALLN_LOWTAIL_CERTIFICATE="+json.dumps(
        canonical_original_lowtail_allN(),
        sort_keys=True,separators=(",",":")),flush=True)
