"""JPKC-002: ORIGINAL-incidence-preserving typed 3-path collision ledger.

All count identities are finite-graph statements; the conditional all-h
proper-path collision theorem is in companion JPKC-002 note. ALL oriented
simple physical 3-paths are classified by the same COMPLETE original f/g,
and ALL ORDERED pairs with identical oriented endpoints are accounted once.

Does NOT prove root A/B or a cross-defect compensation inequality.
"""
from collections import Counter, defaultdict
from fractions import Fraction
import argparse
import json

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_issue230_jpkc_joint_defect_gate import (
    _path3_and_theta, _cycles_independent, _graph,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    classify_seven_prechecked, seven_census,
)

STATUS = (
    "coordinate_repeat", "missing", "incident",
    "blocked_left_only", "blocked_right_only", "blocked_both",
    "unblocked",
)
GOOD = frozenset(STATUS[1:])
BLOCKED = frozenset(("blocked_left_only","blocked_right_only","blocked_both"))
KINDS = ("identical", "shared_internal", "proper_C6", "improper_C6")


def _edge_incidence_map(ctx):
    """Exactly one ORIGINAL incidence ID per physical graph edge."""
    a=ctx.a
    out={}
    for i,(p,l) in enumerate(ctx.edges):
        x,xp=ctx.f[p]
        y,yp=ctx.g[l]
        for u,v in ((x*a+y,xp*a+yp),(x*a+yp,xp*a+y)):
            key=(min(u,v),max(u,v))
            if key in out:
                raise AssertionError("two different original incidences on one physical edge")
            out[key]=i
    if len(out)!=2*len(ctx.edges):
        raise AssertionError("incomplete two-diagonal original incidence map")
    return out


def _physical_status(ctx,u,b,c,v):
    """Definition-level ORIGINAL GQ endpoint projection with subtypes."""
    a=ctx.a
    rows={u//a,b//a,c//a,v//a}
    cols={u%a,b%a,c%a,v%a}
    if len(rows)!=4 or len(cols)!=4:
        return "coordinate_repeat"
    q=ctx.fi.get(tuple(sorted((u//a,v//a))))
    r=ctx.gi.get(tuple(sorted((u%a,v%a))))
    if q is None or r is None:
        return "missing"
    if (q,r) in ctx.edge_id:
        return "incident"
    p,l=ctx.projection[q,r]
    left=bool(set(ctx.f[p])&rows)
    right=bool(set(ctx.g[l])&cols)
    if left and right:
        return "blocked_both"
    if left:
        return "blocked_left_only"
    if right:
        return "blocked_right_only"
    return "unblocked"


def _path_fibers(ctx,max_paths):
    if type(max_paths) is not int or max_paths<=0:
        raise ValueError("positive exact oriented-path budget required")
    a=ctx.a
    adj=_graph(ctx)
    incidence=_edge_incidence_map(ctx)
    # Count oriented simple P3 without materializing, then fail closed.
    bound=sum((len(adj[u])-1)*(len(adj[v])-1)
              for u in range(len(adj)) for v in adj[u])
    if bound>max_paths:
        raise ValueError("complete oriented path budget exceeded")
    fibers=defaultdict(list)
    labels=Counter()
    for u,neighbors in enumerate(adj):
        for b in neighbors:
            for c in adj[b]:
                if c==u:
                    continue
                for v in adj[c]:
                    if v==b or v==u:
                        continue
                    name=_physical_status(ctx,u,b,c,v)
                    ids=tuple(incidence[min(x,y),max(x,y)]
                              for x,y in ((u,b),(b,c),(c,v)))
                    fibers[(u,v)].append((b,c,name,ids))
                    labels[name]+=1
    # The degree-product count is NB3, which also includes 6*C3
    # triangular closed three-walks. Simple paths are a subset.
    if sum(labels.values())>bound:
        raise AssertionError("oriented simple paths exceed nonbacktracking walk cap")
    return adj,fibers,labels


def _ordered_add(counter,t1,t2,kind):
    counter[(kind,t1,t2)]+=1
    counter[(kind,t2,t1)]+=1


def collision_certificate(model,*,max_paths=2_000_000,
                          max_ordered_pairs=8_000_000,
                          compare_seven=False):
    """Exact ORIGINAL GQ path-pair collision partition, never sample/reweight."""
    ctx=ProjectionClosure(model)
    adj,fibers,labels=_path_fibers(ctx,max_paths)
    energy=_path3_and_theta(adj)
    if sum(labels.values())!=energy["P3"]:
        raise AssertionError("independent all-P3 counter disagrees")
    projection=ctx.census(max_paths=max_paths)
    good_total=sum(labels[s] for s in GOOD)
    if projection["proper_P3"]!=good_total:
        raise AssertionError("independent ORIGINAL projection good-P3 total mismatch")
    for name,expected in (
        ("missing",labels["missing"]),
        ("incident",labels["incident"]),
        ("unblocked",labels["unblocked"]),
        ("blocked",sum(labels[t] for t in (
            "blocked_left_only","blocked_right_only","blocked_both"))),
    ):
        if projection[name]!=expected:
            raise AssertionError("independent ORIGINAL projection subclass "+name+" mismatch")
    total_ordered=sum(len(paths)**2 for paths in fibers.values())
    if type(max_ordered_pairs) is not int or max_ordered_pairs<=0 or total_ordered>max_ordered_pairs:
        raise ValueError("complete endpoint collision-pair budget exceeded")
    bykind=Counter()
    matrix=Counter()
    orig_repeated=Counter()
    by_goodgood=Counter()
    by_blockedblocked=Counter()
    six_candidates=Counter()
    for (u,v),paths in fibers.items():
        for (b,c,tag,ids) in paths:
            bykind["identical"]+=1
            matrix[("identical",tag,tag)]+=1
        for j,(b,c,tag,ids) in enumerate(paths):
            for d,e,other,ids2 in paths[j+1:]:
                if b in (d,e) or c in (d,e):
                    kind="shared_internal"
                else:
                    grid=(u,b,c,v,d,e)
                    if len({z//ctx.a for z in grid})==6 and len({z%ctx.a for z in grid})==6:
                        kind="proper_C6"
                        if tag not in GOOD or other not in GOOD:
                            raise AssertionError("proper C6 must consist of two good P3")
                    else:
                        kind="improper_C6"
                    if kind in ("proper_C6","improper_C6"):
                        repeated=len(set(ids+ids2))<6
                        orig_repeated[kind]+=2*int(repeated)
                        six_candidates[kind]+=2
                        if kind=="proper_C6" and repeated:
                            raise AssertionError("proper C6 uses repeated ORIGINAL incidence")
                        if compare_seven and len(set(ids+ids2))==6:
                            tag_Q=classify_seven_prechecked(
                                tuple(sorted(ids+ids2)),ctx.f,ctx.g,ctx.edges)
                            if kind=="proper_C6" and tag_Q!="D6":
                                raise AssertionError("ORIGINAL sixset D6 classifier disagreement")
                            if kind=="improper_C6" and tag_Q is not None:
                                raise AssertionError("coordinate-improper graph cycle accepted as GF5 seven motif")
                bykind[kind]+=2
                _ordered_add(matrix,tag,other,kind)
                if tag in GOOD and other in GOOD:
                    by_goodgood[kind]+=2
                if tag in BLOCKED and other in BLOCKED:
                    by_blockedblocked[kind]+=2

    if bykind["identical"]!=energy["P3"]:
        raise AssertionError("diagonal path pairs not exactly P3")
    if bykind["shared_internal"]!=energy["Theta"]:
        raise AssertionError("shared internal collision != exact K2 Theta")
    if bykind["proper_C6"]+bykind["improper_C6"]!=12*energy["C6_from_K2"]:
        raise AssertionError("disjoint path-pair cycles != 12*C6")
    if sum(bykind.values())!=total_ordered or sum(matrix.values())!=total_ordered:
        raise AssertionError("ordered endpoint collision matrix incomplete")
    if six_candidates["proper_C6"] != bykind["proper_C6"]:
        raise AssertionError("proper witness cycle ledger lost incidence mapping")
    if orig_repeated["proper_C6"]:
        raise AssertionError("proper cycle repeated original incidence")
    Pgood=sum(labels[t] for t in GOOD)
    diag_good=Counter()
    diag_blocked=Counter()
    for (_, _),paths in fibers.items():
        ng=sum(t in GOOD for _,_,t,_ in paths)
        diag_good["sum_good_sq"]+=ng*ng
        diag_good["sum_good_falling2"]+=ng*(ng-1)
        nb=sum(t in BLOCKED for _,_,t,_ in paths)
        diag_blocked["sum_blocked_sq"]+=nb*nb
        diag_blocked["sum_blocked_falling2"]+=nb*(nb-1)
    collision_good=sum(by_goodgood[k] for k in KINDS[1:])
    if collision_good!=diag_good["sum_good_falling2"]:
        raise AssertionError("all-h J3 good-good endpoint falling factorial identity fails")
    if sum(by_blockedblocked[k] for k in KINDS[1:])!=diag_blocked["sum_blocked_falling2"]:
        raise AssertionError("all-h J4 blocked-blocked endpoint falling factorial identity fails")
    proper=by_goodgood["proper_C6"]
    if proper!=bykind["proper_C6"]:
        raise AssertionError("all proper-C6 collisions must be good-good")
    if (collision_good != 12*(proper//12)
            +by_goodgood["shared_internal"]+by_goodgood["improper_C6"]):
        raise AssertionError("J3 exact 12 D6 + Theta_goodgood + I_goodgood fails")
    if bykind["proper_C6"]%12 or bykind["improper_C6"]%12:
        raise AssertionError("every simple C6 must yield 12 ordered witnesses")
    if Pgood < 0 or Fraction(diag_good["sum_good_sq"])<Fraction(Pgood*Pgood,ctx.a**4):
        raise AssertionError("proper-only Cauchy-Schwarz inequality violated")
    if sum(labels[t] for t in GOOD)!=sum(
        len([1 for _,_,tag,_ in paths if tag in GOOD]) for paths in fibers.values()):
        raise AssertionError("status histogram inconsistent with actual path fibers")

    B=sum(labels[t] for t in BLOCKED)
    if Fraction(diag_blocked["sum_blocked_sq"])<Fraction(B*B,ctx.a**4):
        raise AssertionError("blocked-only Cauchy-Schwarz inequality violated")
    # J5: every blocked endpoint fiber has exactly ONE ORIGINAL GQ
    # nonincident anchor pair (q,r), hence one projection q-l-p-r.
    # Each such (q,r) has exactly FOUR possible ORIENTED physical
    # endpoint pairs: two incidence diagonals and both orientations.
    nonincident_anchor_capacity=4*(ctx.v*ctx.v-len(ctx.edges))
    blocked_anchor_hist=Counter()
    blocked_active_endpoint_fibers=0
    for (u,v),paths in fibers.items():
        n_block=sum(tag in BLOCKED for _,_,tag,_ in paths)
        if not n_block:
            continue
        q=ctx.fi.get(tuple(sorted((u//ctx.a,v//ctx.a))))
        r=ctx.gi.get(tuple(sorted((u%ctx.a,v%ctx.a))))
        if q is None or r is None or (q,r) in ctx.edge_id:
            raise AssertionError("blocked endpoint lacks a unique ORIGINAL nonincident anchor")
        if (q,r) not in ctx.projection:
            raise AssertionError("blocked endpoint projection not unique or incomplete")
        if sum(tag in BLOCKED for _,_,tag,_ in fibers[(v,u)])!=n_block:
            raise AssertionError("physical three-path reversal changes ORIGINAL blocker count")
        blocked_anchor_hist[(q,r)]+=n_block
        blocked_active_endpoint_fibers+=1
    if sum(blocked_anchor_hist.values())!=B:
        raise AssertionError("ORIGINAL nonincident anchor masses omit blocked paths")
    if blocked_active_endpoint_fibers>nonincident_anchor_capacity:
        raise AssertionError("more blocked endpoint fibers than four per ORIGINAL anchor")
    if Fraction(diag_blocked["sum_blocked_sq"])<Fraction(B*B,nonincident_anchor_capacity):
        raise AssertionError("J5 ORIGINAL anchor-improved Cauchy floor violated")
    classes={
        "proper_P3_status_counts":{s:labels[s] for s in STATUS},
        "P3_all":energy["P3"],"P3_good_coordinate_proper":Pgood,
        "endpoint_fibers_nonempty":len(fibers),
        "ordered_pair_count":total_ordered,
        "collision_kinds":{k:bykind[k] for k in KINDS},
        "goodgood_ordered_distinct":{
            "proper_C6":by_goodgood["proper_C6"],
            "improper_C6":by_goodgood["improper_C6"],
            "shared_internal":by_goodgood["shared_internal"],
        },
        "J3_goodgood_falling2":diag_good["sum_good_falling2"],
        "J3_proper_only_CS_floor":str(
            Fraction(Pgood*Pgood,ctx.a**4)-Pgood),
        "J3_goodgood_endpoint_variance":str(
            Fraction(diag_good["sum_good_sq"])-Fraction(Pgood*Pgood,ctx.a**4)),
        "J3_exact_identity_verified":True,
        "J4_blocked_original_P3":B,
        "J4_blocked_only_falling2":diag_blocked["sum_blocked_falling2"],
        "J4_blocked_only_CS_floor":str(Fraction(B*B,ctx.a**4)-B),
        "J5_original_nonincident_qr_anchors":ctx.v*ctx.v-len(ctx.edges),
        "J5_possible_oriented_endpoint_fibers":nonincident_anchor_capacity,
        "J5_active_blocked_endpoint_fibers":blocked_active_endpoint_fibers,
        "J5_original_anchors_with_blockers":len(blocked_anchor_hist),
        "J5_max_original_anchor_blocked_paths":max(blocked_anchor_hist.values(),default=0),
        "J5_anchored_CS_floor_exact":str(Fraction(B*B,nonincident_anchor_capacity)-B),
        "J5_single_original_projection_anchor_verified":True,
        "J4_blockedblocked_ordered_distinct":{
            k:by_blockedblocked[k] for k in KINDS[1:]},
        "J4_exact_blocked_only_identity_verified":True,
        "full_K2_Theta_checked":True,
        "proper_D6_from_collision":bykind["proper_C6"]//12,
        "improper_C6_from_collision":bykind["improper_C6"]//12,
        "cycle_ordered_repeated_original_incidences":{
            k:orig_repeated[k] for k in ("proper_C6","improper_C6")},
        "ordered_collision_tensor":{
            "|".join((kind,t1,t2)):count
            for (kind,t1,t2),count in sorted(matrix.items())},
        "universal_S_lower_PROVED_A":False,
        "root_B_counterexample_proved":False,
    }
    if compare_seven:
        if ctx.s!=2:
            raise ValueError("complete seven-census cross-check is W32 only")
        actual=seven_census(model,independent_checks=False)
        if classes["proper_D6_from_collision"]!=actual["seven_class_motif_counts"]["D6"]:
            raise AssertionError("original D6 exact seven-count mismatch")
        classes["true_original_seven_S"]=actual["S_seven"]
        classes["true_original_seven_GF5_numerator"]=actual["GF5_seven_lower_numerator"]
    return classes


def report():
    records=[]
    for scheme in ("lex","reverse","S68","S72"):
        records.append({"s":2,"scheme":scheme,**collision_certificate(
            fixture(1,scheme),compare_seven=True)})
    for scheme in ("lex","random"):
        records.append({"s":4,"scheme":scheme,**collision_certificate(
            fixture(2,scheme))})
    return {
        "scope":"same-map original-injective full graph 3-path endpoint collision taxonomy",
        "J3_all_h_exact_identity":True,
        "J4_all_h_asymptotic_conditional_necessity_in_docs":True,
        "JPKC_Branch_A_proved":False,
        "records":records,
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--full",action="store_true",
                        help="include full O(status^2) ordered collision tensor")
    args=parser.parse_args()
    record=report()
    if not args.full:
        for row in record["records"]:
            row.pop("ordered_collision_tensor")
    print(json.dumps(record,sort_keys=True,indent=2))
