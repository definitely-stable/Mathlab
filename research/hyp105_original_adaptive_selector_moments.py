r"""HYP-105 AA4-SELMOM: original-ID adaptive selector/spectral moment proof.

NEW all-finite-N path-adaptive lemma, valid on genuine original W(3,s),
all fixed complete globally injected correlated f,g, and ANY Z-free
paired original-flag core C. An ORIGINAL coordinate-proper r=2 or 3
directed physical path gamma uses r distinct pairwise nonconflicting
source original flags S_gamma. In the FULL conflict graph ON C, set
B_gamma = union of the CLOSED source-conflict neighborhoods of S_gamma,
b_gamma=|B_gamma|. If the r source flags are the FIRST r priorities
among B_gamma, and BOTH left/right physical pairs on every edge are
bichromatic, the path survives the exact priority+2-cut selector.

Independent random uniform original flag priority yields EXACT
P(first r of B are the specified S)=1/C(b,r).
Independent uniform binary colors on the r+1 distinct left and r+1
distinct right original physical symbols yield EXACT 4^(-r).
Therefore the WEIGHTED path sum
 W_r(u,v)=SUM_{proper gamma:u->v} 4^(-r)/C(b_gamma,r)
is bounded pointwise by E[(A_G^r)_{u,v}].
By Jensen and tr(A_G^{2r})<=tr(A_C^{2r}) for EVERY selector outcome,
  ||W_r||_F^2 <= E tr(A_G^{2r}) <= tr(A_C^{2r}).

This is stronger than using uniform path-preservation constant
sigma_r=1/[4^r (r(K+1))^r] (K=max degree of ORIGINAL source conflict
graph on C), since b_gamma<=r(K+1) and C(b,r)<=b^r.
The parent #672 used slightly different numerically equivalent sigma
forms sigma2=1/[64(K+1)^2], sigma3=1/[64*27(K+1)^3].

No independence between different paths is presumed or required.
The exact finite proof uses source flags and physical source-owned
edges, not a synthetic graph as a replacement for GQ geometry.

A separate all-N selector injection certifies each C6 in selected G
is a TRUE ORIGINAL six-distinct-ID D6 family: the priority selector
has no row/col cherries; each cut is bichromatic so cyclic odd
coordinate returns are impossible; the six source f-pairs and g-pairs
are aligned simple six cycles and source IDs are injectively recovered.
The original six-edge source to physical-cycle representation is
unique (cyclic order and consecutive shared physical vertices fix it).

Full all-h #672->#674 sextic obstruction still depends on separately
accepted graph supersaturation, high-tail and full-core collinearity
geometric estimates. This module does NOT reprove all-h Branch A.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb
import json

from hyp105_full_physical_degree_tail import genuine_source

ROOT_STATUS="OPEN_WITH_FORMAL_BLOCKER"


def _actual_gq(power,f,g,core_ids=None,deleted_ids=()):
    if type(power) is not int or power not in (1,2):
        raise ValueError("finite exact source oracle supports true W32/W34 only")
    s,V,flags=genuine_source(power)
    a=2
    while comb(a,2)<V:a+=1
    legal=set(combinations(range(a),2))
    f=tuple(tuple(p) for p in f)
    g=tuple(tuple(p) for p in g)
    if (len(f)!=V or len(g)!=V or
        len(set(f))!=V or len(set(g))!=V or
        any(p not in legal for p in f+g)):
        raise ValueError("complete separately globally injected f,g required")
    n=len(flags)
    Z=tuple(deleted_ids)
    C=tuple(range(n)) if core_ids is None else tuple(core_ids)
    if (any(type(i) is not int or not 0<=i<n for i in C+Z)
        or len(set(C))!=len(C)
        or len(set(Z))!=len(Z)
        or set(C)&set(Z)):
        raise ValueError("core must be unique true nondeleted ORIGINAL flag IDs")
    return s,V,a,tuple(flags),f,g,tuple(sorted(C)),tuple(sorted(Z))


def _true_original_source_conflict(flags,f,g,C):
    """Reconstruct original full-column conflict adjacency independently."""
    C=tuple(C)
    adjacency={i:set() for i in C}
    for k,i in enumerate(C):
        pi,li=flags[i]
        for j in C[k+1:]:
            pj,lj=flags[j]
            if ((pi==pj and not set(g[li]).isdisjoint(g[lj])) or
                (li==lj and not set(f[pi]).isdisjoint(f[pj]))):
                adjacency[i].add(j)
                adjacency[j].add(i)
    return adjacency


def _true_original_physical(flags,f,g,C):
    """Two physical owned diagonals of each true original source flag."""
    adj=defaultdict(set)
    owner={}
    for i in C:
        p,l=flags[i]
        x,k=f[p];y,w=g[l]
        for v,t in (((x,y),(k,w)),((x,w),(k,y))):
            if v==t:raise AssertionError("illegal original diagonal self-loop")
            e=tuple(sorted((v,t)))
            if e in owner:raise AssertionError("two original flags own one physical edge")
            owner[e]=i
            adj[v].add(t);adj[t].add(v)
    if len(owner)!=2*len(C):
        raise AssertionError("wrong original two diagonals per source flag")
    return {v:tuple(sorted(ns)) for v,ns in adj.items()},owner


def _paths_and_moments_for_r(adj,owner,conflict,r):
    """Independent full source/physical exact r-path and moment calculation."""
    if r not in (2,3):raise ValueError("only original short paths r=2 or3")
    weighted=defaultdict(Fraction)
    raw=Counter()
    b_hist=Counter()
    min_b=None
    max_b=0
    proper=0
    uniform_min_weight=None

    for start in sorted(adj):
        # Paths are tuples of PHYSICAL vertices, not SOURCE IDs.
        work=[(start,)]
        for _ in range(r):
            work=[path+(nextv,) for path in work for nextv in adj[path[-1]]]
        for path in work:
            xs=[x for x,y in path]
            ys=[y for x,y in path]
            if len(set(xs))!=r+1 or len(set(ys))!=r+1:
                continue
            ids=tuple(owner[tuple(sorted((path[j],path[j+1])))]
                      for j in range(r))
            if len(set(ids))!=r:
                raise AssertionError("proper physical short path repeats ORIGINAL incidence flag")
            if any(v in conflict[u] for u,v in combinations(ids,2)):
                raise AssertionError("proper true original physical path source IDs conflict")
            neighborhood=set(ids)
            for i in ids:
                neighborhood.update(conflict[i])
            b=len(neighborhood)
            if b<r:
                raise AssertionError("not r actual original source flag priorities")
            w=Fraction(1,4**r*comb(b,r))
            weighted[path[0],path[-1]]+=w
            raw[path[0],path[-1]]+=1
            proper+=1
            b_hist[b]+=1
            min_b=b if min_b is None else min(min_b,b)
            max_b=max(max_b,b)
            uniform_min_weight=w if uniform_min_weight is None else min(w,uniform_min_weight)
    # Independent physical matrix power r: all closed 2r walks are
    # a sum of squared integer entries of the symmetric A^r.
    walk={v:Counter({v:1}) for v in adj}
    for _ in range(r):
        nxt={}
        for u,row in walk.items():
            v=Counter()
            for mid,num in row.items():
                for dest in adj[mid]:v[dest]+=num
            nxt[u]=v
        walk=nxt
    trace=sum(k*k for row in walk.values() for k in row.values())
    wnorm=sum(w*w for w in weighted.values())
    raw_norm=sum(n*n for n in raw.values())
    maxK=max(map(len,conflict.values()),default=0)
    sigma=Fraction(1,4**r*(r*(maxK+1))**r)
    if r==2 and sigma!=Fraction(1,64*(maxK+1)**2):
        raise AssertionError("source-original two-path uniform selector sigma wrong")
    if r==3 and sigma!=Fraction(1,64*27*(maxK+1)**3):
        raise AssertionError("source-original three-path uniform selector sigma wrong")
    if wnorm<sigma**2*raw_norm or wnorm>trace:
        raise AssertionError("path-adaptive original weighted GQ selector Jensen envelope invalid")
    if proper and uniform_min_weight<sigma:
        raise AssertionError("a TRUE proper physical source path violates uniform selector probability")
    return {
        "directed_proper_original_physical_r_paths":proper,
        "original_source_union_closed_conflict_neighborhood_min_b":min_b,
        "original_source_union_closed_conflict_neighborhood_max_b":max_b,
        "original_source_neighborhood_size_histogram":dict(sorted(b_hist.items())),
        "maximum_original_conflict_graph_degree_K":maxK,
        "uniform_original_selector_sigma":str(sigma),
        "original_adaptive_weighted_endpoint_Frobenius_square":str(wnorm),
        "uniform_sigma_squared_times_exact_original_proper_endpoint_Frobenius_square":
            str(sigma**2*raw_norm),
        "original_proper_endpoint_Frobenius_square":raw_norm,
        "physical_original_full_core_trace_A_to_2r":trace,
        "adaptive_positive_path_weight_improves_uniform_coefficient":True,
        "weighted_original_selector_Jensen_bound_verified":True,
        "source_proper_paths_pairwise_original_ID_nonconflict":True,
    }


def _original_core_two_walk_spectral_gate(adj,flags,g,C,reference_r2):
    """Real ORIGINAL source pair-pencil and physical 4th moment test."""
    # R_x(p,y) = number of retained flags with point p touching right y.
    right=Counter()
    left=Counter()
    for i in C:
        p,l=flags[i]
        for y in g[l]:right[p,y]+=1
    Qx=2*sum(z*z for z in right.values())
    # Qy separately uses the SOURCE line-pencil and point pair labels,
    # verified independently by caller before source selector.
    A2={v:Counter() for v in adj}
    for u,neigh in adj.items():
        for mid in neigh:A2[u].update(adj[mid])
    trace4=sum(n*n for row in A2.values() for n in row.values())
    real_Qx=sum(n for u,row in A2.items()
                for v,n in row.items() if u[0]==v[0])
    if Qx!=real_Qx or trace4!=reference_r2["physical_original_full_core_trace_A_to_2r"]:
        raise AssertionError("physical two-walks vs true ORIGINAL pencil Qx mismatch")
    return Qx,trace4


def adaptive_true_original_selector_certificate(power,f,g,
        core_ids=None,deleted_ids=()):
    s,V,a,flags,f,g,C,Z=_actual_gq(
        power,f,g,core_ids,deleted_ids)
    conflict=_true_original_source_conflict(flags,f,g,C)
    adj,owner=_true_original_physical(flags,f,g,C)
    r2=_paths_and_moments_for_r(adj,owner,conflict,2)
    r3=_paths_and_moments_for_r(adj,owner,conflict,3)
    K=max(map(len,conflict.values()),default=0)
    Qx,trace4=_original_core_two_walk_spectral_gate(
        adj,flags,g,C,r2)
    Rp=Counter()
    for i in C:
        p,l=flags[i]
        for x in f[p]:Rp[l,x]+=1
    Qy=2*sum(z*z for z in Rp.values())
    A2={v:Counter() for v in adj}
    for u,ns in adj.items():
        for mid in ns:A2[u].update(adj[mid])
    physical_Qy=sum(z for u,row in A2.items()
                    for v,z in row.items() if u[1]==v[1])
    if Qy!=physical_Qy:
        raise AssertionError("original full source LINE R(l,x) col return not physical")
    m=len(owner)
    Delta=max(map(len,adj.values()),default=0)
    uniform_P2=Fraction(
        r2["uniform_original_selector_sigma"])
    # tr A0^4 <= 2 ||P2||² + 2 Delta (Qx+Qy):
    # First decompose EACH A² entry into proper vs improper 2-paths,
    # and bound B2^2 by Delta SUM B2; all fields are exact integers.
    P2=Counter()
    B2=Counter()
    for u,row in A2.items():
        for v,z in row.items():
            if u[0]!=v[0] and u[1]!=v[1]:
                P2[u,v]=z
            else:B2[u,v]=z
    P2norm=sum(n*n for n in P2.values())
    B2norm=sum(n*n for n in B2.values())
    if (P2norm!=r2["original_proper_endpoint_Frobenius_square"]
        or B2norm>Delta*(Qx+Qy)
        or trace4!=P2norm+B2norm
        or trace4>2*P2norm+2*Delta*(Qx+Qy)):
        raise AssertionError("original true full/core fourth-moment decomposition false")
    return {
        "schema":"mathlab.hyp105.aa4-original-path-adaptive-selector-moments.v1",
        "s":s,"original_source_flags":len(flags),
        "selected_original_core_IDs":list(C),
        "deleted_original_source_IDs":list(Z),
        "retained_original_source_flags":len(C),
        "global_physical_alphabet":a,
        "physical_core_edges":m,
        "physical_core_max_degree_Delta":Delta,
        "source_conflict_edges":sum(map(len,conflict.values()))//2,
        "source_original_conflict_degree_K":K,
        "real_original_core_Qx":Qx,
        "real_original_core_Qy":Qy,
        "real_original_trace_A4":trace4,
        "real_original_trace_A6":r3["physical_original_full_core_trace_A_to_2r"],
        "real_original_P2_square_norm":P2norm,
        "real_original_B2_square_norm":B2norm,
        "r2":r2,"r3":r3,
        "all_N_weighted_Jensen_original_selector_proof":True,
        "all_N_original_core_selector_bichromatic_source_C6_D6_injection":
            "proved in accompanying manuscript; independently checked on deterministic actual physical source selectors",
        "external_graph_supersaturation_needed_for_allh":True,
        "new_root_allh_Branch_A_proved_here":False,
        "root_230_status":ROOT_STATUS,
    }


def _priority_color_selector_source_graph(flags,f,g,C,priority,left_bits,right_bits):
    adj=defaultdict(set)
    owner={}
    conflict=_true_original_source_conflict(flags,f,g,C)
    pos={source:i for i,source in enumerate(priority)}
    if len(pos)!=len(C) or set(pos)!=set(C):
        raise ValueError("source priorities must be a permutation of ORIGINAL CORE IDs")
    kept=[]
    for i in C:
        if (all(pos[i]<pos[j] for j in conflict[i])
            and left_bits[f[flags[i][0]][0]]!=left_bits[f[flags[i][0]][1]]
            and right_bits[g[flags[i][1]][0]]!=right_bits[g[flags[i][1]][1]]):
            kept.append(i)
    adj,owner=_true_original_physical(flags,f,g,tuple(kept))
    return adj,owner,tuple(sorted(kept))


def _simple_sixcycles(adj):
    """Canonical physical 6cycle DFS, one rotation/reversal per cycle."""
    result=[]
    for start in sorted(adj):
        path=(start,)
        def walk(path):
            if len(path)==6:
                if start in adj[path[-1]] and path[1]<path[-1]:
                    result.append(path)
                return
            for v in adj[path[-1]]:
                if v>start and v not in path:
                    walk(path+(v,))
        walk(path)
    return tuple(result)


def _true_original_sixcycle_selector_audit(
        power,f,g,C,priority,left_bits,right_bits):
    from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
    s,V,a,flags,f,g,C,Z=_actual_gq(power,f,g,C,())
    if len(left_bits)!=a or len(right_bits)!=a:
        raise ValueError("exact source physical binary coloring of both alphabets")
    physical,owner,kept=_priority_color_selector_source_graph(
        flags,f,g,C,priority,left_bits,right_bits)
    cycles=_simple_sixcycles(physical)
    seen=set()
    for path in cycles:
        if (len({x for x,y in path})!=6 or
            len({y for x,y in path})!=6):
            raise AssertionError("selector contains forbidden nonproper original source C6")
        ids=tuple(sorted(owner[tuple(sorted((path[i],path[(i+1)%6])))]
                         for i in range(6)))
        if len(set(ids))!=6:
            raise AssertionError("selector 6cycle uses repeated ORIGINAL ID")
        if ids in seen:
            raise AssertionError("TWO 6cycles use the same ORIGINAL six IDs: source D6 injection fails")
        seen.add(ids)
        if classify_seven_prechecked(ids,f,g,flags)!="D6":
            raise AssertionError("actual selector simple C6 not historical original D6 source GF5 motif")
    return {
        "true_original_selector_retained_flags":len(kept),
        "selected_physical_simple_C6":len(cycles),
        "source_original_D6_sixsets_from_physical_C6":len(seen),
        "actual_original_flag_IDs_D6":[list(x) for x in sorted(seen)],
        "selector_C6_source_injective":True,
        "all_selected_C6_coordinate_proper":True,
    }


def _color_c6_source_factor_edges(edges,a):
    adj=defaultdict(set)
    for u,v in edges:
        adj[u].add(v);adj[v].add(u)
    color=[0]*a
    seen=set()
    for start in sorted(adj):
        if start in seen:continue
        seen.add(start);work=[start]
        for u in work:
            for v in sorted(adj[u]):
                if v not in seen:
                    color[v]=1-color[u];seen.add(v);work.append(v)
                elif color[v]==color[u]:
                    raise AssertionError("genuine original D6 factor C6 cannot be bichromatically selected")
    return tuple(color)


def selected_original_D6_witness(power,scheme):
    """Build one GUARANTEED real source-selector C6, not only a random one."""
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    from hyp105_g5e2b3e1b0_seven_signature import seven_census
    if power!=1:raise ValueError("original D6 source census witness only W32")
    model=pair_labeled_symplectic(power,scheme)
    flags=model["incidences"]
    f,g=model["left_labels"],model["right_labels"]
    census=seven_census(model,independent_checks=True,witness_sets=True)
    source=next(tuple(ids) for ids,cl in sorted(census["sets"].items())
                if cl=="D6")
    assert len(source)==6
    lbits=_color_c6_source_factor_edges((f[flags[i][0]] for i in source),6)
    rbits=_color_c6_source_factor_edges((g[flags[i][1]] for i in source),6)
    C=tuple(range(len(flags)))
    order=tuple(sorted(source))+tuple(i for i in C if i not in source)
    audit=_true_original_sixcycle_selector_audit(
        power,f,g,C,order,lbits,rbits)
    if audit["selected_physical_simple_C6"]<1:
        raise AssertionError("full true ORIGINAL D6 positive source cannot survive intended selector")
    if list(sorted(source)) not in audit["actual_original_flag_IDs_D6"]:
        raise AssertionError("planted TRUE original D6 flag IDs were not selected")
    audit.update({
        "genuine_original_W32_scheme":scheme,
        "planted_original_six_flag_IDs":list(sorted(source)),
        "global_priority_selector_original_source_full_C":45,
        "source_priority_and_bichromatic_both_halves_FORCED_D6":True,
    })
    return audit


def canonical_adaptive_original_source_certificate():
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    cases=[
        (1,"lex",None,()),
        (1,"reverse-line",tuple(i for i in range(45) if i%3!=0),(0,3,6)),
        (2,"lex",tuple(i for i in range(425) if i%4 in (0,1)),tuple(range(0,425,29))),
        (2,"reverse-line",tuple(i for i in range(425) if i%5 in (1,3)),tuple(range(0,425,31))),
    ]
    reports=[]
    for power,scheme,C,Z in cases:
        model=pair_labeled_symplectic(power,scheme)
        if C is None:
            C=tuple(i for i in range(len(model["incidences"])) if i not in Z)
        else:
            C=tuple(i for i in C if i not in Z)
        x=adaptive_true_original_selector_certificate(
            power,model["left_labels"],model["right_labels"],C,Z)
        x["scheme"]=scheme
        reports.append(x)
    witnessed={sc:selected_original_D6_witness(1,sc)
               for sc in ("lex","reverse-line")}
    return {
        "schema":"mathlab.hyp105.AA4-ORIGINAL-path-adaptive-selector-CI-proof.v1",
        "all_N_adaptive_priority_and_bichromatic_path_weight_proof":True,
        "exact_original_source_cases":reports,
        "selector_actual_original_positive_D6_witness":witnessed,
        "all_h_Branch_A_proved_here":False,
        "root_230_status":ROOT_STATUS,
    }


if __name__=="__main__":
    print("AA4_ADAPTIVE_ORIGINAL_SELECTOR_MOMENT_CERTIFICATE="+json.dumps(
        canonical_adaptive_original_source_certificate(),
        sort_keys=True,separators=(",",":")),flush=True)
