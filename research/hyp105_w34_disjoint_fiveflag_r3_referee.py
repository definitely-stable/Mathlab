"""HYP-105 AA4-W34-DISJOINT5: exact DIRECT full original signed R3 delta.

For one real ORIGINAL source flag i and one legal GF5 palette t, define
 H_i(t) = #((P,T): P subset other flags, |P|=2,
                    T subset other flags, |T|=3, P cap T=empty,
                    c_i(t)+sum(P)==sum(T) in full physical GF(5)^m).
Every six-distinct-ORIGINAL-flag 3+3 signed event containing i has a
UNIQUE orientation with i positive, so full R3(t)-full R3(old)
equals H_i(t)-H_i(old) EXACTLY. Events avoiding i are invariant.

Source-local 24D complement projection and exact 4D GF5 difference
classify each disjoint matching (pair, triple) into at most one of the
51 allowed nonzero checksum4 palettes. One pass over C(424,3) genuine
other triples and one ID-preserving C(424,2)-pair index give ALL 51
exact TRUE R3 costs, with NO use of the D3-(N-4)D2 identity.

Independent R2 guard uses the all-51 physical-source R2 histogram from
AA4-W34-R3DERIV (#715). Every selected 425-source W34 palette edit is
checked by an entirely fresh full 12,704,100-triple external GF5
six-distinct-flag signed-R3 audit. No theorem beyond finite W34 is
claimed by a bounded deterministic local search.
"""
from collections import Counter,defaultdict
from itertools import combinations
from pathlib import Path
import json
import math

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_w34_external_triple_r3_referee import (
    BASE, _add_four_digit_table, _packed_four_groups,
    exact_gf5_original_vectors, exact_full_original_external_r3,
)
from hyp105_w34_projected_source_palette_repair_referee import (
    _gf5_four_support_projection, _subtract_to_gf5_palette,
    _two_sum_collision_source_pairs,
)
from hyp105_w34_direct_r3_palette_derivative_referee import (
    all_51_exact_original_source_D2_cross_cost,
    _read_frozen_r2first_original_certificates,
)
from hyp105_w34_direct_r3_palette_derivative_referee import (
    _all_current_actual_signed_witnesses,
)


def all_51_direct_disjoint_original_R3_costs(
        model, indices, source_id, *, max_other_triples=12_614_424):
    """Exact H_i(t) histogram for all 51, using only 6-DISTINCT-ID events.

    The key difference from #714's D3 cross histogram:
    PRESERVE the actual two other-original-source IDs in pair index.
    For each triple T, count only indexed source pairs P with P
    DISJOINT from T. All overlapping P/T combinations would be
    R2 shadows, and are intentionally excluded from true R3.

    No six-source sign event involving i is missed: orient the
    unordered sign partition so i is positive, choose exactly
    the other positive pair P and three negative flags T.
    """
    ids,vectors=exact_gf5_original_vectors(model,indices)
    n=len(ids)
    if (n not in (45,425) or len(indices)!=n
        or type(source_id) is not int or not 0<=source_id<n):
        raise ValueError("complete TRUE W32/W34 original source and flag ID required")
    if type(max_other_triples) is not int or max_other_triples<0:
        raise ValueError("nonnegative complete source three-subset budget required")
    required=math.comb(n-1,3)
    if required>max_other_triples:
        raise ValueError("full original disjoint-triples budget exceeded: fail closed")
    parts=_packed_four_groups(vectors)
    add=_add_four_digit_table()
    subtract=_subtract_to_gf5_palette()
    out_luts,in_luts,outcoords,support=_gf5_four_support_projection(
        model,source_id)
    ng=len(out_luts)
    other=tuple(j for j in range(n) if j!=source_id)
    if len(other)!=n-1 or ng!=len(parts[0]):
        raise AssertionError("not a global original source/physical projection")

    # Store ACTUAL source IDs, not just multiplicity counters:
    # exact pair/triple SOURCE DISJOINTNESS is required for true R3.
    by_outside=defaultdict(list)
    pairs=0
    for a_pos in range(n-2):
        ia=other[a_pos]
        a=parts[ia]
        for b_pos in range(a_pos+1,n-1):
            ib=other[b_pos]
            b=parts[ib]
            outside=inside=0
            for k in range(ng):
                limb=add[BASE*a[k]+b[k]]
                outside+=out_luts[k][limb]
                inside+=in_luts[k][limb]
            by_outside[outside].append((inside,ia,ib))
            pairs+=1
    if pairs!=math.comb(n-1,2):
        raise AssertionError("source pair projection did not index ALL originals")

    hist=[0]*51
    trios=0
    projected_matches=0
    overlapping_pairs_rejected=0
    truly_disjoint_projected_matches=0
    legal_palette_matches=0
    for a_pos in range(n-3):
        ia=other[a_pos]
        a=parts[ia]
        for b_pos in range(a_pos+1,n-2):
            ib=other[b_pos]
            b=parts[ib]
            partial=tuple(add[BASE*a[k]+b[k]] for k in range(ng))
            for c_pos in range(b_pos+1,n-1):
                ic=other[c_pos]
                c=parts[ic]
                outside=0
                limbs=[]
                for k in range(ng):
                    limb=add[BASE*partial[k]+c[k]]
                    outside+=out_luts[k][limb]
                    limbs.append(limb)
                trios+=1
                potential=by_outside.get(outside)
                if potential is None:continue
                inside=sum(in_luts[k][limbs[k]] for k in range(ng))
                for pair_inside,ip,iq in potential:
                    projected_matches+=1
                    if ip in (ia,ib,ic) or iq in (ia,ib,ic):
                        overlapping_pairs_rejected+=1
                        continue
                    truly_disjoint_projected_matches+=1
                    forced=subtract[BASE*inside+pair_inside]
                    if forced>=0:
                        hist[forced]+=1
                        legal_palette_matches+=1
    if (trios!=required or projected_matches!=
        overlapping_pairs_rejected+truly_disjoint_projected_matches
        or sum(hist)!=legal_palette_matches):
        raise AssertionError("source-complete disjoint six-original-ID histogram lost cases")
    if any(type(z) is not int or z<0 for z in hist):
        raise AssertionError("invalid negative true original signed-event risk")
    return {
        "original_source_ID":source_id,
        "physical_four_GF5_support":support,
        "outside_GF5_dimensions":len(outcoords),
        "original_2subsets_indexed":pairs,
        "original_3subsets_processed":trios,
        "projected_GF5_pair_triple_matches":projected_matches,
        "overlapping_original_pair_triple_matches_correctly_excluded":
            overlapping_pairs_rejected,
        "disjoint_original_pair_triple_matches":
            truly_disjoint_projected_matches,
        "legal_palette_disjoint_sixsource_matches":legal_palette_matches,
        "current_source_palette_index":indices[source_id],
        "current_source_TRUE_R3_incidence":hist[indices[source_id]],
        "all_51_exact_TRUE_R3_incidence_counts":tuple(hist),
        "no_D3_or_R2_shadow_used_for_R3":True,
    }


def all_51_independent_direct_R3_candidate_deltas(
        model, indices, source_id, *,
        baseline_D2, baseline_R3,
        max_other_triples=12_614_424):
    """Direct exact full signed 3v3 derivative with independent R2 guard."""
    n=model["N"]
    if (n not in (45,425) or len(indices)!=n
        or type(baseline_D2) is not int or baseline_D2<0
        or type(baseline_R3) is not int or baseline_R3<0):
        raise ValueError("legal full original fixed source and nonnegative exact baseline")
    events=all_51_direct_disjoint_original_R3_costs(
        model,indices,source_id,max_other_triples=max_other_triples)
    d2=all_51_exact_original_source_D2_cross_cost(
        model,indices,source_id)
    if events["physical_four_GF5_support"]!=d2["real_original_four_support"]:
        raise AssertionError("independent R2/R3 physical supports disagree")
    t0=indices[source_id]
    old_inc=events["current_source_TRUE_R3_incidence"]
    old_d2=d2["current_exact_D2_cross_count"]
    options=[]
    for t,inc in enumerate(events["all_51_exact_TRUE_R3_incidence_counts"]):
        delta_R3=inc-old_inc
        delta_D2=d2["all_51_legal_source_D2_cross_counts"][t]-old_d2
        new_R3=baseline_R3+delta_R3
        new_D2=baseline_D2+delta_D2
        new_D3=new_R3+(n-4)*new_D2
        if min(new_R3,new_D2,new_D3)<0:
            raise AssertionError("source-local disjoint true R3 derivative inconsistent")
        if t==t0 and (delta_R3,delta_D2)!=(0,0):
            raise AssertionError("same legal source palette has nonzero derivative")
        options.append({
            "palette":t,
            "exact_source_six_disjoint_R3_incidence":inc,
            "delta_FULL_TRUE_R3":delta_R3,
            "delta_full_D2":delta_D2,
            "predicted_FULL_TRUE_R3":new_R3,
            "predicted_FULL_D2":new_D2,
            "predicted_FULL_D3_via_independent_identity":new_D3,
            "R2_guardrail_no_increase":new_D2<=baseline_D2,
        })
    selected=min((z for z in options if z["R2_guardrail_no_increase"]),
                 key=lambda z:(z["predicted_FULL_TRUE_R3"],
                               z["predicted_FULL_D2"],
                               z["predicted_FULL_D3_via_independent_identity"],
                               z["palette"]))
    return {
        "original_source_ID":source_id,
        "baseline_full_D2":baseline_D2,
        "baseline_full_TRUE_R3":baseline_R3,
        "baseline_original_R3_incidence":old_inc,
        "all_51_direct_true_R3_and_R2_candidates":tuple(options),
        "best_R2_nonincrease_palette":selected,
        "actual_strict_true_R3_improvement":
            baseline_R3-selected["predicted_FULL_TRUE_R3"],
        "full_original_source_triples_visited_once":
            events["original_3subsets_processed"],
        "source_disjointness_exactly_enforced":True,
        "no_expected_risk_proxy":True,
    }


def _frozen_W34_true_R3_certificates():
    data=json.loads(Path(__file__).with_name(
        "hyp105_w34_direct_r3_repaired_source_certificates.json"
    ).read_text(encoding="utf-8"))
    if (not data["source_geometry_unchanged"] or
        data["new_asymptotic_ASET_exponent_proved"] or
        set(data["schemes"])!={"lex","reverse-line"}):
        raise AssertionError("wrong frozen parent #715 finite W34 certificates")
    for scheme,source in data["schemes"].items():
        if (len(source["repaired_all_original_425_palettes"])!=425 or
            tuple(source["final_exact_original_R2_D3_R3"])!=
                ((1,497,76) if scheme=="lex" else (0,83,83))):
            raise AssertionError("source-fixed original parent #715 risk mismatch")
    return data


def exact_W34_direct_disjoint_source_descent(
        scheme,*,max_candidates_per_round=4,max_updates=3):
    """Finite three-round true ORIGINAL six-distinct event R3 descent.

    All actual R3 witnesses are fully reconstructed from the prior
    exact W34 external oracle at each round. Only source IDs in a
    current genuine collision can possibly strictly improve R3
    by a single-palette edit: every event avoiding the edited
    source ID is invariant, and negative event count is impossible.

    Select highest-degree current real source hotspots, but never
    claim bounded top-K search proves an all-source local optimum.
    """
    if scheme not in ("lex","reverse-line"):
        raise ValueError("true original W34 fixed source scheme required")
    if (type(max_candidates_per_round) is not int
        or not 1<=max_candidates_per_round<=425
        or type(max_updates) is not int or not 1<=max_updates<=8):
        raise ValueError("bounded positive original-source search budgets only")
    model=pair_labeled_symplectic(2,scheme)
    if (model["s"],model["N"],model["m"])!=(4,425,28):
        raise AssertionError("wrong true symplectic original W34 fixed map")
    pinned=_frozen_W34_true_R3_certificates()["schemes"][scheme]
    indices=list(pinned["repaired_all_original_425_palettes"])
    init=tuple(pinned["final_exact_original_R2_D3_R3"])
    if init[1]!=init[2]+421*init[0]:
        raise AssertionError("parent full R2/R3 model not exact")
    current=init
    selected_edits=[]
    checked_hotspots=[]
    final_full=None
    for round_id in range(max_updates):
        full,witnesses=_all_current_actual_signed_witnesses(
            model,tuple(indices),current)
        final_full=full
        if current[2]==0:break
        degree=Counter(src for w in witnesses
                       for src in w["six_distinct_ORIGINAL_flag_IDs"])
        if not degree:
            raise AssertionError("true positive full signed R3 has no actual source")
        # Exact prune theorem: source not in current R3 witness cannot
        # strictly reduce R3 by changing that one source coefficient.
        if sum(degree.values())!=6*current[2]:
            raise AssertionError("missing/duplicated actual six-source signed witnesses")
        ranked=tuple(sorted(degree,key=lambda src:(-degree[src],src)))
        shortlisted=ranked[:max_candidates_per_round]
        possible=[]
        for source_id in shortlisted:
            candidate=all_51_independent_direct_R3_candidate_deltas(
                model,tuple(indices),source_id,
                baseline_D2=current[0],baseline_R3=current[2])
            if candidate["baseline_original_R3_incidence"]!=degree[source_id]:
                raise AssertionError(
                    "DISJOINT source-local GF5 exact incidence disagree with independent ALL 3v3 event oracle")
            best=candidate["best_R2_nonincrease_palette"]
            checked_hotspots.append({
                "round":round_id,
                "original_source_ID":source_id,
                "current_exact_source_R3_event_degree":degree[source_id],
                "all_51_source_options_verified":len(candidate[
                    "all_51_direct_true_R3_and_R2_candidates"]),
                "best_true_R3":best["predicted_FULL_TRUE_R3"],
                "best_R2":best["predicted_FULL_D2"],
                "best_palette":best["palette"],
                "all_51_TRUE_R3_deltas":tuple(z["delta_FULL_TRUE_R3"]
                    for z in candidate["all_51_direct_true_R3_and_R2_candidates"]),
            })
            if (best["predicted_FULL_TRUE_R3"]<current[2]
                and best["predicted_FULL_D2"]<=current[0]
                and best["palette"]!=indices[source_id]):
                possible.append((
                    best["predicted_FULL_TRUE_R3"],
                    best["predicted_FULL_D2"],
                    best["predicted_FULL_D3_via_independent_identity"],
                    source_id,best,candidate))
        if not possible:
            break
        after_R3,after_R2,after_D3,source_id,best,choice=min(
            possible,key=lambda q:q[:4])
        old_palette=indices[source_id]
        before=current
        indices[source_id]=best["palette"]
        current=(after_R2,after_D3,after_R3)
        if (current[2]>=before[2] or current[0]>before[0] or
            current[1]!=current[2]+421*current[0]):
            raise AssertionError("not exact strict TRUE original R3 source descent")
        # NONNEGOTIABLE: FULL independent 12,704,100 physical original
        # GF5 triples after EACH accepted source palette edit.
        final_full,new_witnesses=_all_current_actual_signed_witnesses(
            model,tuple(indices),current)
        if (final_full["all_triples_exact_external_disk_records_processed"]!=
            12704100 or len(new_witnesses)!=current[2]):
            raise AssertionError("source-local current W34 3+3 certificate incomplete")
        selected_edits.append({
            "round":round_id,
            "ORIGINAL_source_ID":source_id,
            "prior_original_palette_index":old_palette,
            "new_original_palette_index":indices[source_id],
            "full_D2_D3_R3_before":before,
            "full_D2_D3_R3_after":current,
            "true_signed_sixflag_R3_improvement":before[2]-current[2],
            "exact_all_51_TRUE_R3_delta_vector":tuple(z["delta_FULL_TRUE_R3"]
                 for z in choice["all_51_direct_true_R3_and_R2_candidates"]),
            "exact_all_51_R2_delta_vector":tuple(z["delta_full_D2"]
                 for z in choice["all_51_direct_true_R3_and_R2_candidates"]),
            "complete_12704100_original_triple_external_check":True,
            "independent_true_R3_events_after_edit":len(new_witnesses),
        })
    if final_full is None:
        raise AssertionError("zero full original source independent checks")
    if (final_full["FULL_six_distinct_original_ID_3v3_signed_event_count"]!=
            current[2] or
        final_full["R2_signed_2v2_events_exact"]!=current[0] or
        final_full["equal_sum_pairs_of_distinct_ORIGINAL_triples"]!=current[1]):
        raise AssertionError("final full independent signed GF5 source risk disagreement")
    return {
        "fixed_original_W34_scheme":scheme,
        "original_source_flag_count":425,
        "original_GF5_physical_dimension":28,
        "source_parent_715_full_D2_D3_R3":init,
        "exact_source_flag_hotspots_examined":tuple(checked_hotspots),
        "accepted_real_source_coefficient_edits":tuple(selected_edits),
        "num_source_edits":len(selected_edits),
        "all_425_ORIGINAL_ID_ordered_GF5_palette_indices":tuple(indices),
        "final_exact_source_D2_D3_TRUE_R3":current,
        "TRUE_original_sixflag_R3_strictly_decreased":current[2]<init[2],
        "full_source_GF5_0to3_ASET":current[0]==current[2]==0,
        "all_accepted_edits_fully_12_704_100_triples_checked":True,
        "single_source_zero_incidence_pruning_theorem_used":True,
        "source_point_line_maps_unchanged":True,
        "bounded_K_hotspot_search_not_all_425_optimality":True,
        "no_all_h_exponent_or_universal_zero_claim":True,
    }


def report(*,scheme="lex",candidates=4,updates=3):
    return {
        "research":"HYP105 true disjoint 5flag source local GF5 51-palette signed R3",
        "data":exact_W34_direct_disjoint_source_descent(
            scheme,max_candidates_per_round=candidates,max_updates=updates),
        "new_asymptotic_exponent_proved":False,
    }


if __name__=="__main__":
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("--scheme",choices=("lex","reverse-line"),default="lex")
    parser.add_argument("--candidates",type=int,default=4)
    parser.add_argument("--updates",type=int,default=3)
    a=parser.parse_args()
    print(json.dumps(report(scheme=a.scheme,candidates=a.candidates,
                            updates=a.updates),indent=2,sort_keys=True))
