"""JPKC-004: TRUE ORIGINAL-incidence sixset transport of endpoint-blocked collisions.

The mathematical J9 obstruction and J10 <=768 disjoint-sixset witness cap
are ALL-h statements (see companion proof). Executable census is EXACT
finite and fail-closed: no model-free image proxy is promoted to seven-GF5.
"""
from collections import Counter, defaultdict
from itertools import combinations
from functools import lru_cache
import json
import argparse

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_issue230_jpkc002_path_collision_taxonomy import (
    _path_fibers, BLOCKED, collision_certificate,
)
from hyp105_issue230_jpkc003_anchor_channel_concentration import (
    anchor_concentration_certificate,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    classify_seven_prechecked, seven_census,
)

KINDS=("shared_internal","improper_C6","proper_C6")
STATES=("original_incidence_repeat","left_not_2reg",
        "right_not_2reg","seven_selected","two_reg_nonseven",
        "two_reg_unresolved")


def _degrees(ctx,ids,side):
    labels=ctx.f if side==0 else ctx.g
    deg=Counter()
    for i in ids:
        factor=ctx.edges[i][side]
        u,v=labels[factor]
        deg[u]+=1
        deg[v]+=1
    return deg


def _two_regular(deg):
    return len(deg)==6 and all(v==2 for v in deg.values())


def _closure_obstruction(ctx,q,r,ids):
    """J9: 3 ORIGINAL GQ completion incidences + 3 physical path incidences.

    Six POSITIONS are retained even when original IDs are repeated.
    """
    p,l=ctx.projection[q,r]
    left=bool(set(ctx.f[q]) & set(ctx.f[p]))
    right=bool(set(ctx.g[r]) & set(ctx.g[l]))
    if not (left or right):
        raise AssertionError("J9 closure scope requires endpoint-bad original anchor")
    closes=(ctx.edge_id[q,l],ctx.edge_id[p,l],ctx.edge_id[p,r])
    six=tuple(ids)+closes
    if len(six)!=6:
        raise AssertionError("original GQ path uses three closing incidence positions")
    L=_degrees(ctx,six,0)
    R=_degrees(ctx,six,1)
    if left and max(L.values())<3:
        raise AssertionError("J9 left triple-concentration obstruction failed")
    if right and max(R.values())<3:
        raise AssertionError("J9 right triple-concentration obstruction failed")
    if _two_regular(L) and _two_regular(R):
        raise AssertionError("endpoint-bad canonical GQ closure falsely GF5 accepted")
    return {"left":left,"right":right,
            "original_six_distinct":len(set(six))==6,
            "left_max_degree":max(L.values()),
            "right_max_degree":max(R.values())}


def transport_certificate(model,*,compare_seven=False,max_paths=2_000_000,
                          max_ordered_pairs=8_000_000,
                          max_unique_sixsets=3_000_000,
                          include_witnesses=False):
    """All ordered endpoint-bad BLOCKED P3 collision pairs on SAME f,g."""
    ctx=ProjectionClosure(model)
    if compare_seven and ctx.s!=2:
        raise ValueError("original seven-class oracle exact only for W32")
    if type(max_ordered_pairs)!=int or max_ordered_pairs<=0:
        raise ValueError("positive endpoint collision pair budget required")
    if type(max_unique_sixsets)!=int or max_unique_sixsets<=0:
        raise ValueError("positive source sixset cache budget required")
    _,fibers,_=_path_fibers(ctx,max_paths)
    counted=0
    moment=Counter()
    provenance=Counter()
    gf5_tagged=Counter()
    source_seen=defaultdict(set)
    separate_cycles_by_sixset=Counter()
    closure=Counter()
    source_tag_cache={}
    examples={}

    # Every true ORIGINAL nonincident anchor has exactly four oriented
    # graph endpoint pairs; physical pair injections fix a unique anchor.
    for (u,v),paths in fibers.items():
        q=ctx.fi.get(tuple(sorted((u//ctx.a,v//ctx.a))))
        r=ctx.gi.get(tuple(sorted((u%ctx.a,v%ctx.a))))
        if q is None or r is None or (q,r) not in ctx.projection:
            continue
        p,l=ctx.projection[q,r]
        eleft=bool(set(ctx.f[q]) & set(ctx.f[p]))
        eright=bool(set(ctx.g[r]) & set(ctx.g[l]))
        if not(eleft or eright):
            continue
        candidates=[(b,c,ids) for b,c,tag,ids in paths if tag in BLOCKED]
        for b,c,ids in candidates:
            x=_closure_obstruction(ctx,q,r,ids)
            closure["original_paths_endpoint_bad"]+=1
            closure["original_six_distinct"]+=int(x["original_six_distinct"])
            closure["bad_left"]+=int(x["left"])
            closure["bad_right"]+=int(x["right"])
            closure["left_max_degree_at_least_3"]+=int(x["left_max_degree"]>=3)
            closure["right_max_degree_at_least_3"]+=int(x["right_max_degree"]>=3)
        n=len(candidates)
        counted+=n*(n-1)
        if counted>max_ordered_pairs:
            raise ValueError("complete endpoint-only collision pair budget exceeded")

        for i,(b,c,ids) in enumerate(candidates):
            for d,e,ids2 in candidates[i+1:]:
                kind="shared_internal" if (b in (d,e) or c in (d,e)) else (
                    "proper_C6" if (
                        len({z//ctx.a for z in (u,b,c,v,d,e)})==6
                        and len({z%ctx.a for z in (u,b,c,v,d,e)})==6
                    ) else "improper_C6")
                moment[kind]+=2
                source=tuple(sorted(set(ids+ids2)))
                if len(source)!=6:
                    state="original_incidence_repeat"
                else:
                    if source not in source_tag_cache:
                        if len(source_tag_cache)>=max_unique_sixsets:
                            raise ValueError("complete distinct original sixset cache budget exceeded")
                        L=_two_regular(_degrees(ctx,source,0))
                        R=_two_regular(_degrees(ctx,source,1))
                        if not L:
                            meta=("left_not_2reg",None)
                        elif not R:
                            meta=("right_not_2reg",None)
                        elif compare_seven:
                            tag=classify_seven_prechecked(source,ctx.f,ctx.g,ctx.edges)
                            meta=("seven_selected" if tag is not None else "two_reg_nonseven",tag)
                        else:
                            meta=("two_reg_unresolved",None)
                        source_tag_cache[source]=meta
                    state,tag=source_tag_cache[source]
                    source_seen[(kind,state)].add(source)
                    if kind!="shared_internal":
                        separate_cycles_by_sixset[source]+=2
                        if separate_cycles_by_sixset[source]>768:
                            raise AssertionError("all-h 2^6*12 disjoint original sixset cap violated")
                    if kind=="proper_C6":
                        if not _two_regular(_degrees(ctx,source,0)) or not _two_regular(_degrees(ctx,source,1)):
                            raise AssertionError("proper physical C6 must have two 2regular ORIGINAL projections")
                        if compare_seven and tag!="D6":
                            raise AssertionError("proper physical C6 not certified original seven D6")
                    if compare_seven and kind=="improper_C6" and tag is not None:
                        raise AssertionError("improper graph C6 cannot be accepted GF5 original seven motif")
                    if state=="seven_selected":
                        gf5_tagged[(kind,tag)]+=2
                provenance[(kind,state)]+=2
                key=(kind,state)
                if include_witnesses and key not in examples:
                    examples[key]={"q":q,"r":r,"path1_original":ids,
                                   "path2_original":ids2,"original_six":source,
                                   "path1_grid":(u,b,c,v),
                                   "path2_grid":(u,d,e,v)}
    if sum(moment.values())!=counted or sum(provenance.values())!=counted:
        raise AssertionError("endpoint-only ordered collision ledger incomplete")
    if sum(closure[k] for k in ("bad_left","bad_right"))<closure["original_paths_endpoint_bad"]:
        raise AssertionError("each original endpoint-bad path fails J9 on at least one side")
    if compare_seven:
        originals=seven_census(model,independent_checks=False,witness_sets=True)
        accepted=originals["sets"]
        for (kind,state),wits in source_seen.items():
            if state=="seven_selected":
                for source in wits:
                    if source not in accepted:
                        raise AssertionError("selected GF5 sixset absent from full original W32 census")
        for (kind,tag),num in gf5_tagged.items():
            if tag not in originals["seven_class_motif_counts"]:
                raise AssertionError("unknown ORIGINAL seven motif class")
            if num<0:
                raise AssertionError("negative original sixset witness multiplicity")
    previous=anchor_concentration_certificate(model,max_paths=max_paths)
    if counted!=previous["J7_endpoint_region_collisions"]:
        raise AssertionError("JPKC003 exact endpoint collision moment does not reconcile")
    if closure["original_paths_endpoint_bad"]!=previous["J7_endpoint_E"]:
        raise AssertionError("JPKC003 exact endpoint path mass does not reconcile")
    if compare_seven:
        old=collision_certificate(model,max_paths=max_paths,compare_seven=True)
        if old["true_original_seven_S"]!=originals["S_seven"]:
            raise AssertionError("independent ORIGINAL seven-class census mismatch")
    by_kind={k:moment[k] for k in KINDS}
    by_state={k:{s:provenance[(k,s)] for s in STATES} for k in KINDS}
    by_GF5={kind:{motif:n for (category,motif),n in gf5_tagged.items()
                  if category==kind} for kind in KINDS}
    if sum(sum(row.values()) for row in by_state.values())!=counted:
        raise AssertionError("typed source partition lost paths")
    result={
        "s":ctx.s,"a":ctx.a,
        "same_original_global_f_g":True,
        "endpoint_bad_original_path_count":closure["original_paths_endpoint_bad"],
        "endpoint_bad_ordered_collisions":counted,
        "physical_collision_kinds":by_kind,
        "original_sixset_provenance_partition":by_state,
        "original_sixset_distinct_counts":{
            k:{st:len(source_seen[(k,st)]) for st in STATES} for k in KINDS},
        "max_disjoint_cycle_ordered_witnesses_per_original_sixset":
            max(separate_cycles_by_sixset.values(),default=0),
        "J10_universal_disjoint_per_sixset_cap":768,
        "J9_direct_GQ_closure_no_GF5_2reg":True,
        "J9_closure_original_six_distinct_paths":closure["original_six_distinct"],
        "J9_endpoint_bad_left_paths":closure["bad_left"],
        "J9_endpoint_bad_right_paths":closure["bad_right"],
        "JPKC003_endpoint_moment_independently_reconciled":True,
        "GF5_seven_W32_exact_accepted_witnesses":
            by_GF5 if compare_seven else None,
        "GF5_seven_all_h_classifier_available":False,
        "Root_A_PROVED":False,"Root_B_CONSTRUCTED":False,
    }
    if compare_seven:
        result["original_W32_true_seven_S"]=originals["S_seven"]
    if include_witnesses:
        result["original_witness_examples"]={
            "|".join(k):v for k,v in examples.items()}
    return result


def report(*,spread=False):
    records=[]
    for scheme in ("lex","reverse","S68","S72"):
        records.append({"scheme":scheme,**transport_certificate(
            fixture(1,scheme),compare_seven=True)})
    for scheme in ("lex","random"):
        records.append({"scheme":scheme,**transport_certificate(
            fixture(2,scheme))})
    if spread:
        from hyp105_issue230_jpkc_spread_adversary import spread_adversary_model
        model,cert=spread_adversary_model(2)
        records.append({"scheme":"D4-true-original-symplectic-spread",
                        "original_Mf":cert["M_f_original_exact"],
                        **transport_certificate(model)})
    return {
        "scope":"true ORIGINAL GQ endpoint-bad blocked collisions source sixset transport",
        "all_h_J9_closure_no_go":True,
        "all_h_J10_disjoint_sixset_cap":768,
        "no_all_h_S_lower_proof":True,
        "records":records}


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--spread",action="store_true")
    args=parser.parse_args()
    print(json.dumps(report(spread=args.spread),indent=2,sort_keys=True))
