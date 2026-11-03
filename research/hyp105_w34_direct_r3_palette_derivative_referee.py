"""HYP-105 AA4-W34-R3DERIV: exact 51-palette DIRECT signed R3 descent.

For any set of N DIFFERENT fixed physical GF(5)^m source vectors,
D3 = R3(six distinct IDs) + (N-4)*D2.
A one-source legal GF5 palette change has exactly computable
D3(t)-D3(old) via a 24D outside/4D inside pair-triple projection,
and D2(t)-D2(old) via the same support projection on outside
singles versus other-original pair sums. Therefore

  R3(t)-R3(old) =
    [D3_cross(t)-D3_cross(old)]
    -(N-4)*[D2_cross(t)-D2_cross(old)].

This is the TRUE full R3 signed event count, NOT raw duplicated triples
or seven leading classes. The selector refuses to increase R2,
and changes a palette only on strict decrease of R3.

All REAL W34 source IDs and physical maps remain constant. Every
accepted change is independently validated by a FRESH complete
12,704,100-triple original 28D external radix census with all true
R2/3+3 signed counts and complete direct 28D event witnesses.
A bounded hotspot search is NOT proof of global optimality nor all h.
"""
from collections import Counter,defaultdict
from itertools import combinations
from pathlib import Path
import json
import math

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_original_gf5_deterministic_extraction_referee import PALETTES
from hyp105_w34_external_triple_r3_referee import (
    BASE,_add_four_digit_table,_packed_four_groups,
    exact_gf5_original_vectors,exact_full_original_external_r3,
)
from hyp105_w34_projected_source_palette_repair_referee import (
    _gf5_four_support_projection,_subtract_to_gf5_palette,
    source_palette_51_exact_cross_histogram,_two_sum_collision_source_pairs,
)


def all_51_exact_original_source_D2_cross_cost(model,indices,source_id):
    """Exact 51-way FULL D2 local derivative with only 424+89676 source sums.

    Let U be all ORIGINAL pairs not containing source ID i, and let
    A_i be pairs {i,j}. Pairs within U/U are invariant; A_i/A_i equal
    only if two distinct ORIGINAL singleton physical vectors equal,
    impossible for separately pair-injective real source f,g.
    A_i/U equality is
      c_i + c_j = c_a+c_b,
      iff outside_i(c_j) == outside_i(c_a+c_b)
      and 4D-inside palette_i = inside_i(c_a+c_b)-inside_i(c_j).
    For each outside projection match, exactly one legal palette may
    satisfy it. Count every match ONCE for its exact required palette.
    This yields precise global D2(t)-D2(old) for all 51 choices,
    with NO sampling, non-exact fingerprint or 51 full scans.
    """
    ids,vectors=exact_gf5_original_vectors(model,indices)
    n=len(ids)
    if type(source_id) is not int or not 0<=source_id<n:
        raise ValueError("real original source ID must exist")
    if n not in (45,425):
        raise ValueError("only complete genuine W32/W34 source experiments")
    parts=_packed_four_groups(vectors)
    add=_add_four_digit_table()
    subtract=_subtract_to_gf5_palette()
    out_luts,in_luts,outcoords,support=_gf5_four_support_projection(
        model,source_id)
    ng=len(out_luts)
    other=tuple(i for i in range(n) if i!=source_id)
    # Full true 424 other ORIGINAL singleton sums with their complete
    # 24D outside and exact four original support-coordinate values.
    singles=defaultdict(Counter)
    for i in other:
        outside=inside=0
        for k,limb in enumerate(parts[i]):
            outside+=out_luts[k][limb]
            inside+=in_luts[k][limb]
        singles[outside][inside]+=1
    if sum(sum(z.values()) for z in singles.values())!=n-1:
        raise AssertionError("one ORIGINAL source singleton missing")

    hist=[0]*51
    matched_outside=0
    forced_legal=0
    pair_count=0
    for u,v in combinations(other,2):
        a=parts[u];b=parts[v]
        outside=inside=0
        for k in range(ng):
            limb=add[BASE*a[k]+b[k]]
            outside+=out_luts[k][limb]
            inside+=in_luts[k][limb]
        pair_count+=1
        options=singles.get(outside)
        if options is None:continue
        for single_inside,multiplicity in options.items():
            matched_outside+=multiplicity
            pal=subtract[BASE*inside+single_inside]
            if pal>=0:
                hist[pal]+=multiplicity
                forced_legal+=multiplicity
    if pair_count!=math.comb(n-1,2):
        raise AssertionError("not all other original 2-subsets processed")
    if any(x<0 for x in hist):
        raise AssertionError("invalid negative exact D2 cross")
    return {
        "real_original_source_id":source_id,
        "real_original_four_support":support,
        "outside_original_GF5_coordinates":len(outcoords),
        "other_original_single_source_processed":n-1,
        "other_original_pair_source_processed":pair_count,
        "all_51_legal_source_D2_cross_counts":tuple(hist),
        "current_original_palette":indices[source_id],
        "current_exact_D2_cross_count":hist[indices[source_id]],
        "projected_outside_matches":matched_outside,
        "projected_matches_with_legal_nonzero_checksum4_GF5_palette":
            forced_legal,
        "exact_no_sampling":True,
    }


def all_51_direct_R3_derivative(model,indices,source_id,*
                               baseline_D2,baseline_D3,
                               max_other_triples=12_614_424):
    """Exact all-51 true six-distinct-original-ID R3 derivative.

    Independent full D2/D3 is the pinned caller baseline, not recomputed
    from cross histograms. Every candidate is charged EXACTLY the
    source-local change of D3 minus (N-4) times change of D2.
    """
    n=model["N"]
    if n not in (45,425) or len(indices)!=n:
        raise ValueError("full true original source scope only")
    if (type(baseline_D2) is not int or type(baseline_D3) is not int
        or min(baseline_D2,baseline_D3)<0):
        raise ValueError("finite exact nonnegative integer risk inputs only")
    baseline_R3=baseline_D3-(n-4)*baseline_D2
    if baseline_R3<0:
        raise ValueError("baseline violates exact all-N original R2/R3 identity")
    d2=all_51_exact_original_source_D2_cross_cost(
        model,indices,source_id)
    d3=source_palette_51_exact_cross_histogram(
        model,indices,source_id,max_other_triples=max_other_triples)
    if d2["real_original_four_support"]!=d3["original_source_support"]:
        raise AssertionError("D2 and D3 source coordinates disagree")
    cur=indices[source_id]
    result=[]
    for t in range(51):
        change2=d2["all_51_legal_source_D2_cross_counts"][t]-d2[
            "current_exact_D2_cross_count"]
        change3=d3["all_51_exact_cross_counts"][t]-d3[
            "cross_collision_count_current_palette"]
        candidate_D2=baseline_D2+change2
        candidate_D3=baseline_D3+change3
        candidate_R3=candidate_D3-(n-4)*candidate_D2
        if min(candidate_D2,candidate_D3,candidate_R3)<0:
            raise AssertionError(("not full true source GF5 derivative",
                                  source_id,t,candidate_D2,candidate_D3,
                                  candidate_R3))
        if t==cur and (candidate_D2,candidate_D3,candidate_R3)!=(
                baseline_D2,baseline_D3,baseline_R3):
            raise AssertionError("unchanged original source palette cost incorrect")
        result.append({
            "palette":t,"delta_full_D2":change2,"delta_full_D3":change3,
            "delta_true_six_distinct_original_R3":change3-(n-4)*change2,
            "predicted_exact_D2":candidate_D2,
            "predicted_exact_D3":candidate_D3,
            "predicted_exact_true_R3":candidate_R3,
            "R2_guardrail_no_increase":candidate_D2<=baseline_D2,
        })
    allowed=tuple(z for z in result if z["R2_guardrail_no_increase"])
    selected=min(allowed,key=lambda z:(
        z["predicted_exact_true_R3"],
        z["predicted_exact_D2"],z["predicted_exact_D3"],
        z["palette"]))
    return {
        "source_id":source_id,
        "initial_original_palette":cur,
        "baseline_exact_D2":baseline_D2,
        "baseline_exact_D3":baseline_D3,
        "baseline_exact_true_R3":baseline_R3,
        "exact_all_51_source_palette_candidates":tuple(result),
        "best_R2_nonincrease_candidate":selected,
        "strict_true_R3_improvement":baseline_R3-selected[
            "predicted_exact_true_R3"],
        "other_original_triples_counted_once":d3[
            "source_other_triples_processed"],
        "other_original_pair_sums_for_D3":d3[
            "source_other_pair_count"],
        "other_original_pair_sums_for_D2":d2[
            "other_original_pair_source_processed"],
        "full_source_exact_no_sampling_or_proxy":True,
    }


def _read_frozen_r2first_original_certificates():
    data=json.loads(Path(__file__).with_name(
        "hyp105_w34_r2first_repaired_source_certificates.json"
    ).read_text(encoding="utf-8"))
    if (data["true_ORIGINAL_flags"]!=425 or
        data["physical_GF5_coordinates"]!=28 or
        data["full_source_triples_checked_per_scheme"]!=12704100 or
        data["new_asymptotic_exponent_proved"]):
        raise AssertionError("wrong proven prior true W34 full source baseline")
    return data


def _all_current_actual_signed_witnesses(model,indices,expected):
    """Independently enumerate EVERY currently colliding TRUE 3v3 event.

    The external 12-byte disk oracle is NOT the projected derivative.
    Unlike the initial baseline witness file's 8 example collisions,
    request all true 86/96 non-leading-inclusive signed event pairs
    to rank actual ORIGINAL source flags by current R3 degree.
    """
    full=exact_full_original_external_r3(
        model,indices,max_triples=12704100,max_witnesses=256)
    risk=(full["R2_signed_2v2_events_exact"],
          full["equal_sum_pairs_of_distinct_ORIGINAL_triples"],
          full["FULL_six_distinct_original_ID_3v3_signed_event_count"])
    if risk!=expected:
        raise AssertionError(("source-fixed W34 full original baseline drift",
                              risk,expected))
    ws=full["verified_independent_true_source_witnesses"]
    if len(ws)!=risk[2]:
        raise AssertionError("not ALL true original 3v3 collision witnesses loaded")
    signatures=set()
    for w in ws:
        plus=tuple(w["positive_ORIGINAL_three"])
        minus=tuple(w["negative_ORIGINAL_three"])
        if len(set(plus+minus))!=6:
            raise AssertionError("not a true 6-DISTINCT original flag witness")
        signatures.add((min(plus,minus),max(plus,minus)))
    if len(signatures)!=risk[2]:
        raise AssertionError("duplicate or missing true original R3 witness")
    return full,ws


def exact_W34_direct_R3_local_descent(
        scheme,*,max_source_candidates_per_round=4,max_updates=2):
    """Pick actual R3 hotspot original IDs, optimize actual R3 (NOT D3).

    Independent complete full original 12.7m triple-sum scans before
    selection and after EACH accepted source change. A candidate is
    accepted only on strict true R3 decrease AND no R2 increase.
    Bounded trials are finite experiments, not global optimum proofs.
    """
    if scheme not in ("lex","reverse-line"):
        raise ValueError("genuine true W34 original source scheme required")
    if (type(max_source_candidates_per_round) is not int
        or not 1<=max_source_candidates_per_round<=425
        or type(max_updates) is not int or max_updates<0):
        raise ValueError("positive bounded source hotspot/candidate budgets required")
    model=pair_labeled_symplectic(2,scheme)
    if (model["s"],model["N"],model["m"])!=(4,425,28):
        raise AssertionError("not genuine complete original W34 425/28 source")
    parent=_read_frozen_r2first_original_certificates()[
        "schemes"][scheme]
    indices=list(parent["all_425_ORIGINAL_flag_palette_indices"])
    initial=(parent["new_exact_full_source_R2"],
             parent["new_exact_full_source_D3"],
             parent["new_exact_full_source_signed_R3"])
    if initial[1]-421*initial[0]!=initial[2]:
        raise AssertionError("frozen full original source R2/R3 identity broken")

    history=[]
    candidate_audit=[]
    current=initial
    if max_updates==0:
        return {
            "scheme":scheme,
            "exact_source_baseline":current,
            "repaired_all_original_425_palettes":tuple(indices),
            "accepted_changes":(),
            "final_exact_original_R2_D3_R3":current,
            "zero_full_0to3_GF5_ASET":False,
            "no_search_performed":True,
            "no_asymptotic_statement":True,
        }

    for round_id in range(max_updates):
        full,ws=_all_current_actual_signed_witnesses(
            model,tuple(indices),current)
        if current[2]==0:
            break
        # Rank only those REAL source IDs that occur in genuine six
        # distinct original 3v3 events; not proxy D3 overlap pairs.
        hotspot=Counter(x for w in ws
                         for x in w["six_distinct_ORIGINAL_flag_IDs"])
        ranked=tuple(sorted(hotspot,key=lambda x:(-hotspot[x],x)))
        if len(ranked)>425 or not ranked:
            raise AssertionError("invalid real W34 true-R3 hotspot ranking")
        selected=ranked[:max_source_candidates_per_round]
        options=[]
        for source_id in selected:
            derivative=all_51_direct_R3_derivative(
                model,tuple(indices),source_id,
                baseline_D2=current[0],baseline_D3=current[1])
            best=derivative["best_R2_nonincrease_candidate"]
            candidate_audit.append({
                "round":round_id,"source_ID":source_id,
                "actual_original_R3_event_degree":hotspot[source_id],
                "candidate_51_count":len(derivative[
                    "exact_all_51_source_palette_candidates"]),
                "best_repaired_palette":best["palette"],
                "best_candidate_R2":best["predicted_exact_D2"],
                "best_candidate_D3":best["predicted_exact_D3"],
                "best_candidate_TRUE_R3":best["predicted_exact_true_R3"],
                "true_R3_improvement":derivative[
                    "strict_true_R3_improvement"],
            })
            if (best["palette"]!=indices[source_id]
                and best["predicted_exact_true_R3"]<current[2]
                and best["predicted_exact_D2"]<=current[0]):
                options.append((best["predicted_exact_true_R3"],
                                best["predicted_exact_D2"],
                                best["predicted_exact_D3"],
                                source_id,best,derivative))
        if not options:
            break
        _r3,_r2,_d3,source_id,best,derivative=min(
            options,key=lambda q:q[:4])
        prev_idx=indices[source_id]
        before=current
        indices[source_id]=best["palette"]
        predicted=(best["predicted_exact_D2"],
                   best["predicted_exact_D3"],
                   best["predicted_exact_true_R3"])
        # NONNEGOTIABLE independent complete original GF5 proof
        # gate after EVERY source edit, not just after all rounds.
        next_full,next_witnesses=_all_current_actual_signed_witnesses(
            model,tuple(indices),predicted)
        if (predicted[2]>=before[2] or predicted[0]>before[0]
            or predicted[1]-421*predicted[0]!=predicted[2]):
            raise AssertionError("not a strict true R3 source improvement")
        current=predicted
        history.append({
            "round":round_id,"source_ID":source_id,
            "old_original_palette":prev_idx,
            "new_original_palette":best["palette"],
            "before_D2_D3_true_R3":before,
            "after_exact_D2_D3_true_R3":current,
            "true_R3_drop":before[2]-current[2],
            "all_51_exact_candidate_delta_D2_D3_TRUE_R3":
                tuple((
                    z["palette"],z["delta_full_D2"],z["delta_full_D3"],
                    z["delta_true_six_distinct_original_R3"])
                    for z in derivative[
                        "exact_all_51_source_palette_candidates"]),
            "fresh_full_true_ORIGINAL_12_704_100_triples_verified":
                next_full["all_triples_exact_external_disk_records_processed"]==12704100,
            "fresh_complete_true_R3_witnesses":len(next_witnesses),
        })
    # If no source change was made, at least prove the frozen baseline
    # via one independent full audit (first loop already did it).
    if not history:
        _all_current_actual_signed_witnesses(model,tuple(indices),current)
    return {
        "scheme":scheme,
        "all_original_425_flag_count":425,
        "physical_GF5_coordinates":28,
        "exact_source_baseline_D2_D3_TRUE_R3":initial,
        "candidate_source_audit":tuple(candidate_audit),
        "accepted_changes":tuple(history),
        "changed_original_source_flag_count":len(history),
        "repaired_all_original_425_palettes":tuple(indices),
        "final_exact_original_R2_D3_R3":current,
        "final_true_six_original_flag_R3_strictly_decreased":
            current[2]<initial[2],
        "zero_full_0to3_GF5_ASET":current==(0,0,0),
        "source_original_pair_maps_unchanged":True,
        "all_accepted_steps_independently_12704100_rechecked":True,
        "bounded_hotspot_is_not_universal_optimality":True,
        "no_asymptotic_statement":True,
    }


def report(scheme="lex",*,max_source_candidates_per_round=4,
           max_updates=2):
    return {
        "research":"AA4-W34 direct TRUE signed R3 exact 51 GF5 local derivative",
        "data":exact_W34_direct_R3_local_descent(
            scheme,max_source_candidates_per_round=
            max_source_candidates_per_round,max_updates=max_updates),
        "new_ASET_asymptotic_exponent_proved":False,
    }


if __name__=="__main__":
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("--scheme",choices=("lex","reverse-line"),
                        default="lex")
    parser.add_argument("--candidates",type=int,default=4)
    parser.add_argument("--updates",type=int,default=2)
    a=parser.parse_args()
    print(json.dumps(report(
        a.scheme,max_source_candidates_per_round=a.candidates,
        max_updates=a.updates),indent=2,sort_keys=True))
