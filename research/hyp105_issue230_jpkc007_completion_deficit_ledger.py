"""JPKC-007: exact true ORIGINAL source/PALLETE completion-deficit ledger.

J22 and J23 are all-h finite equalities, not a positive S lower theorem.
All GF5 source-positive Q are independently checked against the JPKC006
constructive per-seed oracle and (W32 only) exhaustive seven-class index.
"""
from collections import Counter
from itertools import permutations
from math import comb
import argparse
import json

from hyp105_issue230_projection import ProjectionClosure,fixture
from hyp105_issue230_jpkc002_path_collision_taxonomy import _path_fibers
from hyp105_issue230_jpkc005_alternate_three_completion import (
    _bad_seed_paths,general_seven_original,
)
from hyp105_issue230_jpkc006_source_topology_sharp_charge import (
    _a_sides,_path_source,_other_source_completion,
)
from hyp105_g5e2b3e1b0_seven_signature import seven_census

KINDS=("D6","B-left/A-right","A-left/B-right")


def _physical_half_palette(ctx,path,side):
    """All-h J22 *exact* sequential absent-Ka-edge budget for an A half."""
    a=ctx.a
    coords=[(v//a if side==0 else v%a) for v in path]
    if len(set(coords))!=4:
        raise AssertionError("physical source P3 is not coordinate proper")
    available=ctx.fi if side==0 else ctx.gi
    outside=set(range(a))-set(coords)
    initial=len(outside)*(len(outside)-1)
    entry=exit_=middle=0
    valid=set()
    F={z for z in outside if tuple(sorted((coords[3],z))) in available}
    L={z for z in outside if tuple(sorted((coords[0],z))) in available}
    missing_inside={tuple(sorted(p)) for p in __import__("itertools").combinations(outside,2)
                    if tuple(sorted(p)) not in available}
    for z4 in outside:
        for z5 in outside:
            if z4==z5:
                continue
            if z4 not in F:
                entry+=1
            elif z5 not in L:
                exit_+=1
            elif tuple(sorted((z4,z5))) in missing_inside:
                middle+=1
            else:
                ids=(
                    available[tuple(sorted((coords[3],z4)))],
                    available[tuple(sorted((z4,z5)))],
                    available[tuple(sorted((z5,coords[0])))],
                )
                if len(set(ids))!=3:
                    raise AssertionError("physical six-cycle complement repeats an original factor")
                valid.add(ids)
    full=initial-entry-exit_-middle
    if full!=len(valid):
        raise AssertionError("J22 hole partition not an exact disjoint decomposition")
    if len(valid)!=len(_a_sides(ctx,path,side)):
        raise AssertionError("J22 independently reconstructed true occupied physical A completions disagree")
    direct=len(F)*len(L)-len(F&L)-sum(
        1 for x in F for y in L if x!=y and tuple(sorted((x,y))) in missing_inside)
    if direct!=full:
        raise AssertionError("J22 independent bipartite complement-edge availability identity failed")
    missing=comb(a,2)-ctx.v
    if len(missing_inside)>missing:
        raise AssertionError("J22 physical missing Ka edges exceed global deficit")
    # For each missing undirected interior edge there are at most TWO
    # oriented (z4,z5) assignments. This is a legitimate all-h
    # palette-only lower bound, never an ORIGINAL GF5 witness.
    guaranteed=max(0,len(F)*len(L)-len(F&L)-2*missing)
    if full<guaranteed:
        raise AssertionError("J24 original global physical pair deficit inequality failed")
    regular_endpoints=(len(F)==len(outside) and len(L)==len(outside))
    if regular_endpoints:
        universal_regular=max(0,initial-2*missing)
        if full<universal_regular:
            raise AssertionError("J24 regular-endpoint physical palette guarantee failed")
    return {
        "all_physical_A_half_candidates":initial,
        "missing_first_chord":entry,
        "missing_last_chord_after_first":exit_,
        "missing_internal_chord_after_both":middle,
        "available_A_half":full,
        "J22_closed_form_A_half":direct,
        "physical_endpoint_neighborhood_F":len(F),
        "physical_endpoint_neighborhood_L":len(L),
        "physical_missing_edges_inside_P4_complement":len(missing_inside),
        "physical_global_missing_Ka_edges":missing,
        "J24_local_palette_guaranteed_A_half":guaranteed,
        "J24_P4_endpoints_have_no_missing_outside_chord":regular_endpoints,
        "J24_regular_endpoint_guaranteed_A_half":
            max(0,initial-2*missing) if regular_endpoints else None,
    }


def _source_wedge_stages(ctx,path,side_A):
    """Exact candidate accounting at original point/line and pair-image stages.

    side_A=0: left A, right B; side_A=1: right A, left B.
    Every A-half candidate yields three distinguishable endpoint/wedge choices.
    """
    q=ctx.fi.get(tuple(sorted((path[0]//ctx.a,path[-1]//ctx.a))))
    r=ctx.gi.get(tuple(sorted((path[0]%ctx.a,path[-1]%ctx.a))))
    if q is None or r is None or (q,r) not in ctx.projection:
        raise ValueError("eligible ORIGINAL nonincident endpoint labels required")
    original_source=set(_path_source(ctx,path))
    results=set()
    histogram=Counter()
    for ids in _a_sides(ctx,path,side_A):
        for solo_index in range(3):
            solo=ids[solo_index]
            u,v=[ids[i] for i in range(3) if i!=solo_index]
            histogram["source_wedge_proposals"]+=1
            if side_A==0:
                # A-left/B-right; solo source point must lie on r.
                if (solo,r) not in ctx.edge_id:
                    histogram["missing_original_endpoint_incidence"]+=1
                    continue
                common=ctx.point_lines[u]&ctx.point_lines[v]
                if not common:
                    histogram["missing_original_collinearity"]+=1
                    continue
                if len(common)>1:
                    raise AssertionError("original point pair has more than one common line")
                center=next(iter(common))
                if set(ctx.g[center])&{p%ctx.a for p in path}:
                    histogram["global_physical_pair_interference"]+=1
                    continue
                U=(ctx.edge_id[solo,r],ctx.edge_id[u,center],
                   ctx.edge_id[v,center])
                expected="A-left/B-right"
            else:
                # B-left/A-right; solo line incident with q, other two
                # lines concurrent at unique original point.
                if (q,solo) not in ctx.edge_id:
                    histogram["missing_original_endpoint_incidence"]+=1
                    continue
                common=ctx.lines[u]&ctx.lines[v]
                if not common:
                    histogram["missing_original_collinearity"]+=1
                    continue
                if len(common)>1:
                    raise AssertionError("original line pair has two common points")
                center=next(iter(common))
                if set(ctx.f[center])&{p//ctx.a for p in path}:
                    histogram["global_physical_pair_interference"]+=1
                    continue
                U=(ctx.edge_id[q,solo],ctx.edge_id[center,u],
                   ctx.edge_id[center,v])
                expected="B-left/A-right"
            if len(set(U))!=3 or set(U)&original_source:
                raise AssertionError("wedge source physical disjointness failed after complete geometry cuts")
            Q=tuple(sorted(original_source|set(U)))
            if general_seven_original(ctx,Q)!=expected:
                raise AssertionError("wedge source geometry passed but true ORIGINAL seven-class rejected")
            if tuple(sorted(U)) in results:
                raise AssertionError("wedge original source-positive candidate duplicate")
            results.add(tuple(sorted(U)))
            histogram["source_positive_wedges"]+=1
    if histogram["source_wedge_proposals"]!=sum(
            histogram[k] for k in (
                "missing_original_endpoint_incidence","missing_original_collinearity",
                "global_physical_pair_interference","source_positive_wedges")):
        raise AssertionError("J23 original source-wedge rejection telescope violated")
    return histogram,results


def _source_matching_stages(ctx,path):
    """All-h exact matching/incident/nonaligned D6 opportunity telescope."""
    src=set(_path_source(ctx,path))
    left=_a_sides(ctx,path,0)
    right=_a_sides(ctx,path,1)
    hist=Counter()
    positives=set()
    for ps in left:
        for ls in right:
            for perm in permutations(ls):
                hist["raw_matching_bijections"]+=1
                U=[]
                for p,l in zip(ps,perm):
                    index=ctx.edge_id.get((p,l))
                    if index is None:
                        break
                    U.append(index)
                if len(U)<3:
                    hist["missing_original_incidence_matching"]+=1
                    continue
                if len(set(U))!=3 or set(U)&src:
                    raise AssertionError("physical A/A matching reused an ORIGINAL incidence")
                Q=tuple(sorted(src|set(U)))
                if general_seven_original(ctx,Q)=="D6":
                    if Q in positives:
                        raise AssertionError("one true D6 complement from two different physical paths")
                    positives.add(Q)
                    hist["source_positive_D6"]+=1
                else:
                    hist["nonaligned_AA_original_duals"]+=1
    if hist["raw_matching_bijections"]!=sum(hist[k] for k in (
        "missing_original_incidence_matching","nonaligned_AA_original_duals",
        "source_positive_D6")):
        raise AssertionError("J23 exact ORIGINAL matching and dual alignment telescope violated")
    return hist,positives


def _stratified_indices(n,k):
    if type(k) is not int or k<1:
        raise ValueError("positive exact selected source seed limit required")
    if n<=k:
        return tuple(range(n))
    if k==1:
        return (n//2,)
    return tuple((i*(n-1))//(k-1) for i in range(k))


def deficit_certificate(model,*,limit_seeds=None,exact_W32=True,
                        max_paths=2_000_000,max_accepted=20000):
    ctx=ProjectionClosure(model)
    if exact_W32 and ctx.s!=2:
        raise ValueError("full seven-class exact reference restricted to W32")
    _,fibers,_=_path_fibers(ctx,max_paths)
    seeds=list(_bad_seed_paths(ctx,fibers))
    selected=[seeds[i] for i in _stratified_indices(len(seeds),
              len(seeds) if limit_seeds is None else limit_seeds)]
    totals=Counter()
    byclass=Counter()
    complete=0
    individual=[]
    if exact_W32:
        oracle=seven_census(model,independent_checks=False,witness_sets=True)
        if len(oracle["sets"])>max_accepted:
            raise ValueError("accepted original sixset oracle budget exceeded")
    for path,T,qr in selected:
        left=_physical_half_palette(ctx,path,0)
        right=_physical_half_palette(ctx,path,1)
        for side,ledger in (("L",left),("R",right)):
            for field,value in ledger.items():
                totals[side+"_"+field]+=value
        match,mp=_source_matching_stages(ctx,path)
        wedge_l,wp_l=_source_wedge_stages(ctx,path,0)
        wedge_r,wp_r=_source_wedge_stages(ctx,path,1)
        for prefix,row in (("match",match),("A_left",wedge_l),("A_right",wedge_r)):
            for field,v in row.items():
                totals[prefix+"_"+field]+=v
        actual={tuple(sorted(set(T)|set(U))):name
                for U,name in (
                  *((U,"D6") for U in mp),
                  *((U,"A-left/B-right") for U in wp_l),
                  *((U,"B-left/A-right") for U in wp_r),
                )}
        if len(actual)!=len(mp)+len(wp_l)+len(wp_r):
            raise AssertionError("J23 positive original source Q counted by multiple classes")
        from hyp105_issue230_jpkc006_source_topology_sharp_charge import _other_source_completion
        if actual!=_other_source_completion(ctx,path,T,qr):
            raise AssertionError("J23 independent stage oracle mismatches source-positive Q")
        if exact_W32:
            expected={Q:tag for Q,tag in oracle["sets"].items()
                      if set(T).issubset(Q)}
            if expected!=actual:
                raise AssertionError("J23 true full W32 seven-census source completion mismatch")
        complete+=bool(actual)
        totals["genuine_original_positive_PQ"]+=len(actual)
        for name in actual.values():
            byclass[name]+=1
        if not actual and left["available_A_half"] and right["available_A_half"]:
            totals["isolation_despite_both_physical_A_halves"]+=1
        if not actual:
            totals["isolated_physical_P3"]+=1
    if totals["genuine_original_positive_PQ"]!=sum(byclass.values()):
        raise AssertionError("J23 all-h class-completion sum failed")
    if totals["isolated_physical_P3"]+complete!=len(selected):
        raise AssertionError("J23 exact isolated/covered seed complement failed")
    if totals["match_raw_matching_bijections"]!=sum(totals["match_"+k] for k in (
       "missing_original_incidence_matching","nonaligned_AA_original_duals",
       "source_positive_D6")):
        raise AssertionError("J23 aggregated matching deficits do not telescope")
    for kind in ("A_left","A_right"):
        if totals[kind+"_source_wedge_proposals"]!=sum(totals[kind+"_"+field] for field in (
            "missing_original_endpoint_incidence","missing_original_collinearity",
            "global_physical_pair_interference","source_positive_wedges")):
            raise AssertionError("J23 aggregated original wedge deficits do not telescope")
    return {
        "s":ctx.s,"a":ctx.a,"complete_global_source_injections":True,
        "true_full_endpoint_bad_seed_population":len(seeds),
        "exact_selected_endpoint_bad_seeds":len(selected),
        "complete_endpoint_seed_census":len(selected)==len(seeds),
        "seeds_with_positive_true_source_Q":complete,
        "isolated_true_source_seeds":len(selected)-complete,
        "actual_source_positive_Q_class_counts":dict(byclass),
        "J22_exact_A_half_palette_hole_identity":True,
        "J23_exact_geometry_matching_wedge_dual_deficit_telescope":True,
        "J24_palette_only_A_half_lower_verified":True,
        "J24_palette_only_all_h_positive_extension_proved":False,
        "full_original_W32_seven_GF5_index_compared":bool(exact_W32),
        "scope_no_full_W34_seven_S":not exact_W32,
        "loss_budget":dict(sorted(totals.items())),
        "root_A_proved":False,"root_B_constructed":False,
    }


def report():
    rows=[]
    for name in ("lex","reverse","S68","S72"):
        rows.append({"name":name,**deficit_certificate(fixture(1,name))})
    for name in ("lex","random"):
        rows.append({"name":name,**deficit_certificate(
            fixture(2,name),limit_seeds=32,exact_W32=False)})
    from hyp105_issue230_jpkc_spread_adversary import spread_adversary_model
    model,proof=spread_adversary_model(2)
    rows.append({"name":"D4 true symplectic spread",
                 "original_Mf":proof["M_f_original_exact"],
                 **deficit_certificate(model,limit_seeds=32,exact_W32=False)})
    return {"all_h_J22_J23_exact":True,
            "no_universal_S_lower":True,"records":rows}

if __name__=="__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))
