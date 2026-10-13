"""HYP-105 issue230 D6-B: *literal* PR394 coherent original-incidence pruning.

Input: ONE original W(3,s) geometry, ONE complete globally injective f,g.
Each original incidence (p,l) has TWO true physical diagonal edges, which
are always kept/deleted together, including in vertex peeling.

PR394 thresholds are compared by EXACT INTEGER powers:
 kappa=floor(s^(1/16)), big block b iff b^10>s,
 peel low vertex degree d iff d^32 < s^31.
They may DESTROY the entire tiny finite s=2,4 graph; the PR394 guarantee
is asymptotic, not a finite-h survival guarantee.

A separate explicitly labeled finite-calibration mode relaxes thresholds
and IS NOT the literal theorem construction. No universal seven-S bound.
"""
from collections import Counter, defaultdict
from heapq import heappop, heappush
import json

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_issue230_endpoint_mixedbook_d2 import _chord_ledger
from hyp105_issue230_d5_retained_energy import (
    true_spread_global_model, selected_anchor_edge_oracle,
    retained_original_energy,
)
from hyp105_issue230_d6_joint_blocking_audit import joint_record


def _edge(u,v):
    if u==v:
        raise AssertionError("true original physical G edges must be loopless")
    return (u,v) if u<v else (v,u)


def original_diagonals(core):
    """Complete, independent original incidence -> exactly two physical edges."""
    a=core.a
    result=[]
    owner={}
    for eid,(p,l) in enumerate(core.edges):
        u,v=core.f[p]
        x,y=core.g[l]
        edges=(_edge(u*a+x,v*a+y),_edge(u*a+y,v*a+x))
        if len(set(edges))!=2:
            raise AssertionError("original incidence diagonals coincident")
        for e in edges:
            if e in owner:
                raise AssertionError("two different original incidences share physical edge")
            owner[e]=eid
        result.append(edges)
    full={_edge(v,w) for v,row in enumerate(core.adj) for w,_ in row}
    if set(owner)!=full or len(owner)!=2*core.v*core.delta:
        raise AssertionError("original incidence -> physical edge bijection invalid")
    return result,owner


def _root_floor(s,p):
    # floor(s^(1/p)) using integer arithmetic, no float rounding.
    lo,hi=1,s+1
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid**p<=s:
            lo=mid
        else:
            hi=mid
    return lo


def _config(core,mode):
    if mode=="literal-pr394":
        return {
            "mode":mode,
            "missing_star_cap":_root_floor(core.s,16),
            "block_threshold":"b^10 <= s (equiv. b <= s^(1/10))",
            "peel_degree_threshold":"d^32 >= s^31",
            "block_allowed":lambda b:b**10<=core.s,
            "vertex_allowed":lambda d:d**32>=core.s**31,
        }
    if mode=="finite-calibration":
        # Engineering control, NEVER PR394's actual theorem thresholds.
        t=max(2,(core.s+1)//2)
        return {
            "mode":mode,
            "missing_star_cap":core.a-1,
            "block_threshold":f"b <= {t} (RELAXED finite diagnostic)",
            "peel_degree_threshold":"d >= 2 (RELAXED finite diagnostic)",
            "block_allowed":lambda b:b<=t,
            "vertex_allowed":lambda d:d>=2,
        }
    raise ValueError("only literal PR394 or explicitly relaxed finite calibration")


def prune_original_incidences(core,mode="literal-pr394"):
    """Deterministic faithful PR394 three-stage pruning, preserving diagonals.

    Stage 2 uses neighbor blocks in the ORIGINAL full G (not a rebuilt
    surrogate after stage 1). Removing a superset of large ORIGINAL blocks
    is exactly the stated PR394 procedure. Stage 3 is deterministic
    lowest-grid-vertex-index peeling, and always removes both diagonals.
    """
    diag,owner=original_diagonals(core)
    n=core.a**2
    cfg=_config(core,mode)
    fstar=Counter(x for pair in core.f for x in pair)
    gstar=Counter(x for pair in core.g for x in pair)
    kappa=cfg["missing_star_cap"]
    badrow={u for u in range(core.a) if core.a-1-fstar[u]>kappa}
    badcol={x for x in range(core.a) if core.a-1-gstar[x]>kappa}
    stage1={
        eid for eid,(p,l) in enumerate(core.edges)
        if any(u in badrow for u in core.f[p])
        or any(x in badcol for x in core.g[l])
    }

    # Block size of ORIGINAL G at (u,x), pinned OTHER row or OTHER col.
    # Note each core.adj item carries its unique true original incidence id.
    stage2=set()
    for v,row in enumerate(core.adj):
        by_first=defaultdict(list)
        by_second=defaultdict(list)
        for w,eid in row:
            by_first[w//core.a].append(eid)
            by_second[w%core.a].append(eid)
        for blocks in (by_first,by_second):
            for members in blocks.values():
                if not cfg["block_allowed"](len(members)):
                    stage2.update(members)
    stage2-=stage1
    live=set(range(len(core.edges)))-(stage1|stage2)
    incident=[set() for _ in range(n)]
    degree=[0]*n
    for eid in live:
        vertices=set(z for e in diag[eid] for z in e)
        if len(vertices)!=4:
            raise AssertionError("the two physical diagonals must have four grid endpoints")
        for z in vertices:
            incident[z].add(eid)
            degree[z]+=1
    # Peeling is performed at the *grid vertex* level, but each affected
    # original incidence is removed atomically with its other diagonal.
    todo=[]
    for z,d in enumerate(degree):
        if d>0 and not cfg["vertex_allowed"](d):
            heappush(todo,z)
    stage3=set()
    while todo:
        z=heappop(todo)
        if degree[z]==0 or cfg["vertex_allowed"](degree[z]):
            continue
        for eid in tuple(sorted(incident[z])):
            if eid not in live:
                continue
            live.remove(eid)
            stage3.add(eid)
            for e in diag[eid]:
                for vertex in e:
                    incident[vertex].remove(eid)
                    degree[vertex]-=1
                    if degree[vertex]<0:
                        raise AssertionError("negative retained physical degree")
                    if degree[vertex] and not cfg["vertex_allowed"](degree[vertex]):
                        heappush(todo,vertex)

    if (stage1&stage2 or stage1&stage3 or stage2&stage3
            or len(stage1)+len(stage2)+len(stage3)+len(live)!=len(core.edges)):
        raise AssertionError("original incidence deletion stages must partition E")
    return _make_retention(core,diag,owner,live,
                          ("PR394-EXACT-AS-WRITTEN" if mode=="literal-pr394"
                           else "CALIBRATION-NOT-PR394"),
                          {"missing_star_cap":kappa,
                           "max_missing_original_f_star":max(core.a-1-fstar[u]
                                                              for u in range(core.a)),
                           "max_missing_original_g_star":max(core.a-1-gstar[x]
                                                              for x in range(core.a)),
                           "bad_rows":len(badrow),"bad_columns":len(badcol),
                           "block_threshold":cfg["block_threshold"],
                           "peel_degree_threshold":cfg["peel_degree_threshold"],
                           "deleted_stage1_orig_incidences":len(stage1),
                           "deleted_stage2_orig_incidences":len(stage2),
                           "deleted_stage3_orig_incidences":len(stage3)},
                          check_config=cfg)


def _make_retention(core,diag,owner,live,policy,stages,check_config=None):
    n=core.a**2
    adj=[set() for _ in range(n)]
    selected=set()
    for eid in live:
        for u,v in diag[eid]:
            if v in adj[u]:
                raise AssertionError("duplicate retained physical diagonal")
            adj[u].add(v)
            adj[v].add(u)
            selected.add((u,v))
    remaining=set(owner)-selected
    if any((e in selected)!=(diag[owner[e]][0] in selected)
           for e in owner):
        raise AssertionError("retention broke original incidence diagonal pairing")
    if any((e in selected)!=(diag[owner[e]][1] in selected)
           for e in owner):
        raise AssertionError("coherence of both original diagonals broken")
    if len(selected)!=2*len(live) or len(remaining)!=2*(len(core.edges)-len(live)):
        raise AssertionError("physical edge vs original incidence accounting")
    degrees=[len(neighbors) for neighbors in adj]
    max_block=0
    for row in adj:
        first=Counter(v//core.a for v in row)
        second=Counter(v%core.a for v in row)
        max_block=max(max_block,max(first.values(),default=0),
                      max(second.values(),default=0))
        if check_config is not None and any(
            not check_config["block_allowed"](b)
            for b in tuple(first.values())+tuple(second.values())
        ):
            raise AssertionError("PR394 retained coordinate-neighbor block exceeds T")
    positive=[d for d in degrees if d>0]
    minimum=min(positive,default=0)
    if check_config is not None and any(
        not check_config["vertex_allowed"](d) for d in positive
    ):
        raise AssertionError("retained PR394 graph has forbidden positive low-degree vertex")
    if check_config is not None and any(
        core.a-1-Counter(x for pair in core.f for x in pair)[u]>check_config["missing_star_cap"]
        for v,d in enumerate(degrees) if d for u in (v//core.a,)
    ):
        raise AssertionError("retained PR394 graph uses a bad original f row")
    if check_config is not None and any(
        core.a-1-Counter(x for pair in core.g for x in pair)[x]>check_config["missing_star_cap"]
        for v,d in enumerate(degrees) if d for x in (v%core.a,)
    ):
        raise AssertionError("retained PR394 graph uses a bad original g column")
    return {
        "policy":policy,
        "live_incidence_ids":frozenset(live),
        "adj":adj,
        "deleted_physical_edges":frozenset(remaining),
        "full_original_incidences":len(core.edges),
        "retained_original_incidences":len(live),
        "removed_original_incidences":len(core.edges)-len(live),
        "retained_physical_edges":len(selected),
        "removed_physical_edges":len(remaining),
        "max_retained_coordinate_block":max_block,
        "min_positive_retained_degree":minimum,
        "retained_nonisolated_vertices":len(positive),
        **stages,
    }


def full_retention(core):
    diag,owner=original_diagonals(core)
    return _make_retention(core,diag,owner,set(range(len(diag))),
                           "FULL-TRUE-ORIGINAL-G",{})


def coherent_selected_first(core,selected_physical_edges=None,period=19):
    """Coherent adversarial D5 selected-witness-first OR every-nth source.

    Both diagonals of selected ORIGINAL incidence are always removed.
    Never misreport D5's individual-edge deletion as a coherent policy.
    """
    diag,owner=original_diagonals(core)
    if selected_physical_edges is None:
        if type(period) is not int or period<2:
            raise ValueError("period >=2 expected")
        dropped=set(range(0,len(diag),period))
        policy=f"COHERENT-EVERY-{period}-ORIGINAL-INCIDENCE"
    else:
        keys=set(selected_physical_edges)
        if not keys or not keys<=set(owner):
            raise ValueError("selected must be nonempty actual full original physical edges")
        target=max(1,(len(keys)+4)//5)
        dropped={owner[e] for e in sorted(keys)[:target]}
        policy="COHERENT-D5-SELECTED-WITNESS-FIRST-20PCT"
    return _make_retention(core,diag,owner,set(range(len(diag)))-dropped,
                           policy,{"deleted_adversarial_original_incidences":len(dropped)})


def _bits_from_original_endpoints(core,q,r,coords):
    # Separate reconstruction; independent of D1's _bits implementation.
    p,l=core.projection[q,r]
    x,y=coords
    left_anchor=set(core.f[p])
    right_anchor=set(core.g[l])
    return (
        (1 if left_anchor.intersection((x[0],x[3])) else 0) |
        (2 if left_anchor.intersection((x[1],x[2])) else 0) |
        (4 if right_anchor.intersection((y[0],y[3])) else 0) |
        (8 if right_anchor.intersection((y[1],y[2])) else 0)
    )


def retained_path_census(core,retention,*,max_walks=70_000_000,independent_endpoints=False):
    """Exhaust ALL proper retained P3; classify EXACT original 16 atoms."""
    a=core.a
    H=retention["adj"]
    deg=[len(row) for row in H]
    walk_cap=sum((deg[v]-1)*(deg[w]-1)
                 for v,row in enumerate(H) for w in row)
    if type(max_walks) is not int or max_walks<0 or walk_cap>max_walks:
        raise ValueError("exact finite full oriented 3walk budget exceeded")
    masks=[0]*16
    missing=incident=proper=0
    for v0,row in enumerate(H):
        x0,y0=divmod(v0,a)
        for v1 in row:
            x1,y1=divmod(v1,a)
            for v2 in H[v1]:
                x2,y2=divmod(v2,a)
                if x2 in (x0,x1) or y2 in (y0,y1):
                    continue
                for v3 in H[v2]:
                    x3,y3=divmod(v3,a)
                    if x3 in (x0,x1,x2) or y3 in (y0,y1,y2):
                        continue
                    proper+=1
                    q=core.fi.get(_edge(x0,x3))
                    r=core.gi.get(_edge(y0,y3))
                    if q is None or r is None:
                        missing+=1
                    elif (q,r) in core.edge_id:
                        incident+=1
                    else:
                        masks[_bits_from_original_endpoints(
                            core,q,r,((x0,x1,x2,x3),(y0,y1,y2,y3)))]+=1
    nonincident=sum(masks)
    e=sum(value for mask,value in enumerate(masks) if mask&5)
    i=sum(value for mask,value in enumerate(masks) if mask&5==0 and mask&10)
    c=e+i
    if proper!=missing+incident+nonincident or nonincident!=c+masks[0]:
        raise AssertionError("retained P3 partition into ORIGINAL GQ atoms failed")
    if any(v%2 for v in masks):
        raise AssertionError("each actual retained oriented path must have reversal")
    result={
        "oriented_walk_budget":walk_cap,
        "proper_P3":proper,
        "missing":missing,"incident":incident,
        "nonincident_endpoint_complete":nonincident,
        "exact_sixteen_mask_histogram":masks,
        "E_endpoint_bad_proper_P3":e,
        "I_safe_endpoint_internal_only_proper_P3":i,
        "C_joint_blocked_proper_P3":c,
        "BB_sync_accepted_sixsets":masks[0]//2,
    }
    if independent_endpoints:
        # Different enumeration: original (q,r) endpoints first; choose
        # neighbors at each end and check the middle physical H edge.
        other=[0]*16
        for (q,r),(p,l) in core.projection.items():
            u,v=core.f[q];x,y=core.g[r]
            for (x0,y0),(x3,y3) in (
                ((u,x),(v,y)),((u,y),(v,x)),
                ((v,x),(u,y)),((v,y),(u,x))
            ):
                v0=x0*a+y0;v3=x3*a+y3
                for v1 in H[v0]:
                    x1,y1=divmod(v1,a)
                    if x1 in (x0,x3) or y1 in (y0,y3):
                        continue
                    for v2 in H[v3]:
                        x2,y2=divmod(v2,a)
                        if (v2 not in H[v1] or
                            x2 in (x0,x1,x3) or y2 in (y0,y1,y3)):
                            continue
                        other[_bits_from_original_endpoints(
                            core,q,r,((x0,x1,x2,x3),(y0,y1,y2,y3)))]+=1
        if masks!=other:
            raise AssertionError("ORIGINAL endpoint-first vs 3walk 16-atom enumeration differ")
        result["independent_original_endpair_enumeration"]=True
    return result


def _one_case(core,retention,baseline,*,check_independent=True):
    row=retained_path_census(core,retention,
                             independent_endpoints=check_independent)
    led=_chord_ledger(core,retention["adj"])
    row["W_retained_original_endpoint_energy"]=led["W"]
    row["t_retained"] = led["max_block"]
    if row["t_retained"]!=retention["max_retained_coordinate_block"]:
        raise AssertionError("independent coordinate-block bound disagrees")
    for key,old in (
        ("proper_P3","proper_P3"),
        ("E_endpoint_bad_proper_P3","E_endpoint_bad_proper_P3"),
        ("I_safe_endpoint_internal_only_proper_P3","I_safe_endpoint_internal_only_proper_P3"),
        ("C_joint_blocked_proper_P3","C_joint_blocked_proper_P3"),
        ("BB_sync_accepted_sixsets","BB_sync_accepted_sixsets"),
    ):
        if row[key]>baseline[old]:
            raise AssertionError("removing genuine physical edges created new ORIGINAL proper paths")
    if row["W_retained_original_endpoint_energy"]>baseline["D2_exact_bad_endpoint_energy_W"]:
        raise AssertionError("nonnegative original degree energy grew after deletions")
    row.update({
        k:v for k,v in retention.items()
        if k not in ("adj","live_incidence_ids","deleted_physical_edges")
    })
    row["full_global_original_seven_S"]=baseline["full_seven_S"]
    row["full_global_original_seven_S_scope"]=(
        "COMPLETE-W32-SEVEN" if core.s==2 else "UNKNOWN-NOT-REPLACED-BY-BB"
    )
    return row


def finite_instance(model,scheme,*,selected_edges=None,verify_independent=True):
    core=ProjectionClosure(model)
    baseline=joint_record(model,scheme,compute_full_seven=(core.s==2),
                          independent_paths=verify_independent)
    full=full_retention(core)
    literal=prune_original_incidences(core,"literal-pr394")
    calibrated=prune_original_incidences(core,"finite-calibration")
    adversarial=coherent_selected_first(core,selected_edges)
    policies=(full,literal,calibrated,adversarial)
    rows=[]
    for retention in policies:
        row=_one_case(core,retention,baseline,check_independent=verify_independent)
        if (selected_edges is not None and
                retention["policy"]=="PR394-EXACT-AS-WRITTEN"):
            # Independently invoke D5's verified ORIGINAL projected chord
            # and spread-witness Cauchy lower for retained genuine edges.
            # The caller passes actual D5 selected group data separately below.
            pass
        rows.append(row)
    if rows[0]["proper_P3"]!=baseline["proper_P3"]:
        raise AssertionError("new retained scanner disagrees with D6A full graph")
    if rows[0]["W_retained_original_endpoint_energy"]!=baseline["D2_exact_bad_endpoint_energy_W"]:
        raise AssertionError("new D6B full energy disagrees with D6A")
    if rows[0]["exact_sixteen_mask_histogram"]!=baseline["sixteen_exact_blocking_atoms"]:
        raise AssertionError("independent D6B full sixteen-mask histogram disagrees with D6A")
    return rows


def report():
    entries=[]
    for scheme in ("lex","S68"):
        m=fixture(1,scheme)
        entries.extend(finite_instance(m,"W32-"+scheme))
    for mode in ("balanced","reverse"):
        m,selected,group,spec=true_spread_global_model(2,mode)
        core=ProjectionClosure(m)
        _,selected_edges=selected_anchor_edge_oracle(core,selected,group,spec)
        cases=finite_instance(m,"W34-D5-spread-"+mode,
                              selected_edges=selected_edges)
        # Independent D5 robustness theorem for actual PR394-literal retained H.
        literal=prune_original_incidences(core,"literal-pr394")
        d5=retained_original_energy(m,selected,group,spec,
                    deleted_edges=tuple(literal["deleted_physical_edges"]),
                    assert_new_oracle=False)
        if cases[1]["W_retained_original_endpoint_energy"] != d5["exact_original_bad_chord_energy_W_H"]:
            raise AssertionError("PR394 retained H energy disagrees with D5 independent spread proof")
        cases[1]["D5_selected_kept_original_spread_witness_edges"]=d5[
            "selected_kept_TRUE_physical_edges"]
        cases[1]["D5_robust_lower_numerator"]=d5["robust_removed_edges_lower_num"]
        cases[1]["D5_robust_lower_denominator"]=d5["robust_removed_edges_lower_den"]
        entries.extend(cases)
    return {
        "slice":"ISSUE230-D6-B-TRUE-ORIGINAL-COHERENT-PR394-RETENTION",
        "exact_PR394_integer_thresholds":True,
        "finite_pruning_survival_NOT_asymptotic_theorem":True,
        "calibrated_and_selected_first_NOT_theorem_PR394":True,
        "all_h_original_seven_S_lower":"OPEN",
        "all_h_C_compensation":"OPEN",
        "branch_B_infinite_small_S":"OPEN",
        "same_complete_original_global_maps":entries,
    }


if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
