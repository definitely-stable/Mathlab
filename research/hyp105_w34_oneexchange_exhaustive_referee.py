"""HYP-105 AA4-W34-ALL1: genuine exhaustive active ORIGINAL one-source audit.

Prepare actual W34 ORIGINAL source and COMPLETE true signed R3 witness
incidence degrees, with a pinned SHA256 source-bound input file for a
fast, exact 51-palette GF5 C++ checker. Validate every original active
flag in disjoint shards; independently aggregate all active sources,
prove none missing, apply only a strict-R3-decreasing R2-safe best edit,
and recheck all 12,704,100 true original 28D GF5 three-subset sums
from scratch with the existing independent external exact referee.

If NONE improves, the exhaustive source set and the all-N zero-incidence
pruning lemma establish *R2-nonincreasing one-original-flag*
local optimality of that ONE fixed finite W34 coefficient assignment.
This is NOT global optimality, multi-source or all-h nonexistence.
"""
from collections import Counter
from pathlib import Path
from itertools import combinations
import argparse
import hashlib
import json
import math

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_original_gf5_deterministic_extraction_referee import PALETTES
from hyp105_w34_external_triple_r3_referee import (
    exact_gf5_original_vectors, exact_full_original_external_r3,
)
from hyp105_w34_direct_r3_palette_derivative_referee import (
    _all_current_actual_signed_witnesses,
)
from hyp105_w34_projected_source_palette_repair_referee import (
    _real_original_source_support,
    _two_sum_collision_source_pairs,
)


SCHEMA="mathlab.hyp105.original-w34-exhaustive-active-oneexchange.v1"
PARENT_SHA="b2d848270980585904fe7c00676dc70bcf7001be"
ALL_ORIGINAL_W34_TRIPLES=12_704_100
SHARDS=8


def frozen_complete_W34_sources():
    p=Path(__file__).with_name(
        "hyp105_w34_disjoint5_repaired_source_certificates.json")
    a=json.loads(p.read_text(encoding="utf-8"))
    if (a["original_source_flags"]!=425 or
        a["physical_GF5_dimensions"]!=28 or
        not a["source_maps_fixed"] or
        a["new_all_h_exponent_proved"] or
        set(a["schemes"])!={"lex","reverse-line"}):
        raise AssertionError("not frozen full W34 original #716 source proof")
    for scheme,z in a["schemes"].items():
        if (tuple(z["final_exact_source_D2_D3_TRUE_R3"])
            !=((1,483,62) if scheme=="lex" else (0,69,69))
            or len(z["all_425_ORIGINAL_ID_ordered_GF5_palette_indices"])!=425):
            raise AssertionError("frozen source risk/425 original IDs drift")
    return a


def construct_exact_source_text(model,indices,full,active):
    """Deterministic source format: values are FULL physical GF5 digits."""
    n=model["N"];m=model["m"]
    d2=full["R2_signed_2v2_events_exact"]
    d3=full["equal_sum_pairs_of_distinct_ORIGINAL_triples"]
    r3=full["FULL_six_distinct_original_ID_3v3_signed_event_count"]
    if ((n,m) not in ((425,28),(45,12))
        or d3!=r3+(n-4)*d2 or r3<0):
        raise AssertionError("wrong complete finite original GF5 source statistics")
    ids,vec=exact_gf5_original_vectors(model,tuple(indices))
    if ids!=tuple(range(n)) or len(set(vec))!=n:
        raise AssertionError("not exact distinct complete original incidence flag IDs")
    if len(PALETTES)!=51:
        raise AssertionError("not exact 51-pattern checksum4 palette")
    if any(not 0<=i<n or not 0<=d<=r3 for i,d in active):
        raise AssertionError("invalid original source signed witness degree")
    lines=[
        f"HYP105_W34_ALL1_V1 {model['scheme']} {n} {m} 51 "
        f"{d2} {d3} {r3} {len(active)}"
    ]
    for i in range(n):
        support=_real_original_source_support(model,i)
        if (len(set(support))!=4 or
            tuple(vec[i][q] for q in support)!=tuple(PALETTES[indices[i]])):
            raise AssertionError("original 2+2 factor support is not globally fixed")
        lines.append(" ".join(str(x) for x in (
            *vec[i],*support,indices[i])))
    for palette in PALETTES:
        lines.append(" ".join(str(x) for x in palette))
    for i,degree in active:
        lines.append(f"{i} {degree}")
    return "\n".join(lines)+"\n"


def _derive_all_true_signed_original_degrees(witnesses,r3,n):
    seen=set()
    participation=Counter()
    for w in witnesses:
        plus=tuple(w["positive_ORIGINAL_three"])
        minus=tuple(w["negative_ORIGINAL_three"])
        six=tuple(w["six_distinct_ORIGINAL_flag_IDs"])
        if (len(set(six))!=6 or tuple(sorted(plus+minus))!=six
            or not all(type(x) is int and 0<=x<n for x in six)):
            raise AssertionError("not true six-distinct original signed event")
        canonical=(min(plus,minus),max(plus,minus))
        if canonical in seen:
            raise AssertionError("duplicate true original signed GF5 3v3 witness")
        seen.add(canonical)
        participation.update(six)
    if len(seen)!=r3 or sum(participation.values())!=6*r3:
        raise AssertionError("missing actual true-original R3 witness degree")
    return tuple(sorted(participation.items()))


def prepare_real_W34_inputs(folder):
    root=Path(folder)
    root.mkdir(parents=True,exist_ok=True)
    parent=frozen_complete_W34_sources()
    summary={}
    for scheme in ("lex","reverse-line"):
        model=pair_labeled_symplectic(2,scheme)
        if ((model["s"],model["N"],model["m"])!=(4,425,28)
            or len(set(model["incidences"]))!=425):
            raise AssertionError("false actual symplectic W(3,4) geometry")
        z=parent["schemes"][scheme]
        original=tuple(z["all_425_ORIGINAL_ID_ordered_GF5_palette_indices"])
        expected=tuple(z["final_exact_source_D2_D3_TRUE_R3"])
        full,witnesses=_all_current_actual_signed_witnesses(model,original,expected)
        active=_derive_all_true_signed_original_degrees(
            witnesses,expected[2],425)
        if not active or len(active)>425:
            raise AssertionError("no genuine active current signed 3v3 original flag IDs")
        content=construct_exact_source_text(model,original,full,active)
        blob=content.encode("utf-8")
        (root/f"{scheme}.txt").write_bytes(blob)
        manifest={
            "schema":SCHEMA,"source_model":scheme,
            "frozen_source_parent_SHA":PARENT_SHA,
            "all_425_original_flag_IDs_in_scope":True,
            "physical_GF5_dimensions":28,
            "all_original_sixflag_signed_events_independently_enumerated":len(witnesses),
            "original_exact_D2_D3_R3":expected,
            "source_425_palette_indices":original,
            "all_active_original_source_ID_degrees":active,
            "active_source_count":len(active),
            "sum_original_witness_degrees":sum(d for _,d in active),
            "full_original_12_704_100_triple_census_rechecked":True,
            "source_context_sha256":hashlib.sha256(blob).hexdigest(),
            "original_incidence_points_lines_and_f_g_unchanged":True,
            "no_all_h_claim":True,
        }
        (root/f"{scheme}.manifest.json").write_text(
            json.dumps(manifest,indent=2,sort_keys=True)+"\n",encoding="utf-8")
        summary[scheme]={
            "R2_D3_R3":expected,
            "true_active_source_count":len(active),
            "deg_total":manifest["sum_original_witness_degrees"],
            "min_max_degree":(min(d for _,d in active),
                              max(d for _,d in active)),
            "sha256":manifest["source_context_sha256"],
        }
    return summary


def _normalize_exact_shard_source(scheme,header,rows,expected,active):
    """Reject incomplete and manipulated experimental oracle outputs."""
    r2,d3,r3=expected
    if (header["schema"]!="mathlab.hyp105.original-w34-active-oneexchange-v1"
        or header["scheme"]!=scheme or header["n"]!=425
        or header["m"]!=28 or
        (header["original_D2"],header["original_D3"],
         header["original_R3"])!=(r2,d3,r3)
        or header["total_active_original_IDs"]!=len(active)
        or header["shards"]!=SHARDS
        or not 0<=header["shard"]<SHARDS):
        raise AssertionError("wrong exact full original source worker job")
    allowed=dict(active)
    for row in rows:
        i=row["source_ID"]
        if (i not in allowed or i%SHARDS!=header["shard"] or
            row["witness_degree"]!=allowed[i] or
            row["current_true_R3_incidence"]!=allowed[i] or
            row["current_palette"]<0 or row["current_palette"]>=51 or
            len(row["H_R3_all_51"])!=51 or
            len(row["H_R2_all_51"])!=51):
            raise AssertionError("false exact current ORIGINAL R3 witness incidence")
        cur=row["current_palette"]
        h3=row["H_R3_all_51"]
        h2=row["H_R2_all_51"]
        if (h3[cur]!=allowed[i] or
            h2[cur]!=row["current_R2_cross_incidence"] or
            h2[cur]>r2 or
            any(type(x) is not int or x<0 for x in (*h2,*h3))):
            raise AssertionError("false 51 exact source GF5 projected events")
        scores=[]
        for t in range(51):
            new_r3=r3+h3[t]-h3[cur]
            new_r2=r2+h2[t]-h2[cur]
            new_d3=new_r3+421*new_r2
            if min(new_r2,new_r3,new_d3)<0:
                raise AssertionError("negative exact candidate GF5 risk")
            if new_r2<=r2:
                scores.append((new_r3,new_r2,new_d3,t))
        best=min(scores)
        if best!=(row["best_full_R3"],row["best_full_D2"],
                  row["best_full_D3"],row["best_palette"]):
            raise AssertionError("C++ candidate did not choose globally best LEGAL 51-palette single-source move")
        if best[0]>r3:
            raise AssertionError("source unchanged palette should not worsen true R3")
    return rows


def aggregate_exhaustive_active_oneexchange(inputs,parts,outfile):
    """All active originals + 51 legal palettes; one independent full W34 check."""
    input_dir=Path(inputs);parts_dir=Path(parts)
    root=frozen_complete_W34_sources()
    outcome={
        "schema":"mathlab.hyp105.true-W34-ALL-active-51-oneexchange-CI.v1",
        "source_frozen_parent_SHA":PARENT_SHA,
        "all_original_f_g_geometry_unchanged":True,
        "all_425_original_source_ids_scoped":True,
        "all_original_source_0to3_constraints_are_G5":True,
        "same_source_global_palette_in_every_signed_event":True,
        "new_all_h_asymptotic_exponent_proved":False,
        "CI_shards_per_actual_source_model":SHARDS,
        "schemes":{},
    }
    for scheme in ("lex","reverse-line"):
        manifest=json.loads(
            (input_dir/f"{scheme}.manifest.json").read_text(encoding="utf-8"))
        raw=(input_dir/f"{scheme}.txt").read_bytes()
        expected=tuple(manifest["original_exact_D2_D3_R3"])
        active=tuple(tuple(pair) for pair in
                     manifest["all_active_original_source_ID_degrees"])
        if (manifest["source_model"]!=scheme or
            manifest["schema"]!=SCHEMA or
            manifest["frozen_source_parent_SHA"]!=PARENT_SHA or
            not manifest["all_425_original_flag_IDs_in_scope"] or
            len(active)!=manifest["active_source_count"] or
            len(set(i for i,d in active))!=len(active) or
            sum(d for i,d in active)!=6*expected[2] or
            len(active)==0 or
            hashlib.sha256(raw).hexdigest()!=manifest[
                "source_context_sha256"]):
            raise AssertionError("incomplete TRUE original witness preparation")
        old=tuple(root["schemes"][scheme][
            "all_425_ORIGINAL_ID_ordered_GF5_palette_indices"])
        if tuple(manifest["source_425_palette_indices"])!=old:
            raise AssertionError("frozen original #716 coefficients changed")
        seen={}
        for shard in range(SHARDS):
            p=parts_dir/f"{scheme}-{shard}.json"
            packet=json.loads(p.read_text(encoding="utf-8"))
            if packet["shard"]!=shard:
                raise AssertionError("missing/out-of-order signed ORIGINAL shard")
            rows=_normalize_exact_shard_source(
                scheme,packet,packet["results"],expected,active)
            for row in rows:
                i=row["source_ID"]
                if i in seen or old[i]!=row["current_palette"]:
                    raise AssertionError("duplicate source flag or counterfeit original coefficient")
                seen[i]=row
        if set(seen)!=set(i for i,d in active):
            raise AssertionError("EXHAUSTIVE active one-source GF5 signed R3 audit not complete")
        if len(seen)!=len(active):
            raise AssertionError("source activity/worker coverage mismatch")
        legal_options=[
            (row["best_full_R3"],row["best_full_D2"],
             row["best_full_D3"],i,row["best_palette"])
            for i,row in seen.items()]
        optimum=min(legal_options)
        strict=optimum[0]<expected[2]
        if strict:
            r3,r2,d3,source_id,palette=optimum
            next_idx=list(old)
            if palette==old[source_id]:
                raise AssertionError("claimed strict true-R3 improvement without source edit")
            next_idx[source_id]=palette
            selected={"original_source_ID":source_id,
                      "old_source_palette":old[source_id],
                      "new_source_palette":palette,
                      "predicted_full_D2_D3_TRUE_R3":(r2,d3,r3)}
        else:
            next_idx=list(old)
            selected=None
        model=pair_labeled_symplectic(2,scheme)
        if (model["s"],model["N"],model["m"])!=(4,425,28):
            raise AssertionError("not real original W34 symplectic source")
        # Independent 12.7m original GF5 physical exact source census,
        # NOT based on this C++ or Python active-source derivative.
        full=exact_full_original_external_r3(
            model,tuple(next_idx),max_triples=ALL_ORIGINAL_W34_TRIPLES,
            max_witnesses=16)
        observed=(
            full["R2_signed_2v2_events_exact"],
            full["equal_sum_pairs_of_distinct_ORIGINAL_triples"],
            full["FULL_six_distinct_original_ID_3v3_signed_event_count"])
        expected_final=(optimum[1],optimum[2],optimum[0]) if strict else expected
        if observed!=expected_final or not full[
            "independent_original_R2_to_R3_overlap_identity_verified"] or full[
            "all_triples_exact_external_disk_records_processed"]!=ALL_ORIGINAL_W34_TRIPLES:
            raise AssertionError("full original 12.7m source GF5 oracle refuted one-exchange candidate")
        if len(_two_sum_collision_source_pairs(model,tuple(next_idx)))!=observed[0]:
            raise AssertionError("independent true ORIGINAL 2source GF5 audit disagreed")
        # Exact physical coordinates and all immutable source supports.
        _,vec=exact_gf5_original_vectors(model,tuple(next_idx))
        if len(vec)!=425 or len(set(vec))!=425 or any(
                sum(c)%5!=4 or sum(bool(v) for v in c)!=4 for c in vec):
            raise AssertionError("not 425 real legal original source GF5 columns")
        for witness in full["verified_independent_true_source_witnesses"]:
            positive=witness["positive_ORIGINAL_three"]
            negative=witness["negative_ORIGINAL_three"]
            if (len(set(positive+negative))!=6 or
                any(sum(vec[i][j] for i in positive)%5 !=
                    sum(vec[k][j] for k in negative)%5 for j in range(28))):
                raise AssertionError("actual 28D signed GF5 original source witness refuted")
        outcome["schemes"][scheme]={
            "scheme":scheme,
            "before_full_D2_D3_TRUE_R3":expected,
            "active_source_count":len(active),
            "active_source_degrees":active,
            "all_active_sources_with_all_51_legal_GF5_palettes_checked":True,
            "all_remaining_425_minus_active_can_be_mathematically_pruned":
                True,
            "all_original_flag_source_results":tuple(
                seen[i] for i in sorted(seen)),
            "best_exact_oneexchange_nonincreasing_R2":{
                "candidate_FULL_TRUE_R3":optimum[0],
                "candidate_FULL_D2":optimum[1],
                "candidate_FULL_D3":optimum[2],
                "source_ID":optimum[3],
                "palette":optimum[4]},
            "strict_improving_single_original_source_exists":strict,
            "R2_guarded_oneexchange_local_optimum_proved_for_fixed_assignment":
                not strict,
            "independently_verified_applied_edit":selected,
            "all_425_original_ID_ordered_final_legal_GF5_palettes":tuple(next_idx),
            "final_full_D2_D3_TRUE_R3":observed,
            "independent_full_12704100_original_triple_rehash_verified":True,
            "full_original_28D_GF5_signed_witnesses":
                full["verified_independent_true_source_witnesses"],
            "not_global_or_all_h_optimality":True,
        }
    dest=Path(outfile)
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(outcome,indent=2,sort_keys=True)+"\n",
                    encoding="utf-8")
    return {
        s:{"active":z["active_source_count"],
           "baseline":z["before_full_D2_D3_TRUE_R3"],
           "new":z["final_full_D2_D3_TRUE_R3"],
           "selected":z["independently_verified_applied_edit"],
           "one_exchange_local_optimum":z[
               "R2_guarded_oneexchange_local_optimum_proved_for_fixed_assignment"]}
        for s,z in outcome["schemes"].items()
    }


def cli():
    parser=argparse.ArgumentParser()
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--prepare",metavar="OUTDIR")
    group.add_argument("--aggregate",metavar="OUTFILE")
    parser.add_argument("--inputs",default="inputs")
    parser.add_argument("--shards",default="shards")
    args=parser.parse_args()
    if args.prepare:
        print(json.dumps(prepare_real_W34_inputs(args.prepare),
                         sort_keys=True,indent=2))
    else:
        print(json.dumps(aggregate_exhaustive_active_oneexchange(
            args.inputs,args.shards,args.aggregate),sort_keys=True,indent=2))


if __name__=="__main__":
    cli()
