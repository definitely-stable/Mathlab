"""Independent permanent scientific referee for TWO genuine full W34 425-flag GF5 ASETs.

This program does NOT call the new H_i(t) local projection or its
conflict-erasure algorithm to decide the final answer.  It reads the
COMMITTED immutable 425-entry source palette assignment for each fixed
globally injected real symplectic W(3,4) map; independently constructs
all 425 physical GF(5)^28 columns, tests actual source support and
all 1/2 subset sums, and re-enumerates EVERY 12,704,100 complete
physical three-subset sum with the separate established external-disk
referee (#713).  Any duplicate k=1,2,3 subset sum MUST fail.

All source columns have coordinate checksum =4 mod5. Consequently
for k=0,1,2,3 the checksum of a k-subset sum equals 4k mod5:
0,4,3,2 are pairwise distinct. Thus an independent within-k 1/2/3
collision-free census proves full 0-to-3 ASET, including distinct
cardinality subsets, for these TWO particular fixed W34 maps.

A finite s=4 certificate does NOT prove all-h asymptotic HYP-105.
"""
from pathlib import Path
import json
import math

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_original_gf5_deterministic_extraction_referee import PALETTES
from hyp105_w34_external_triple_r3_referee import (
    exact_gf5_original_vectors,exact_full_original_external_r3,
)
from hyp105_w34_projected_source_palette_repair_referee import (
    _two_sum_collision_source_pairs,_real_original_source_support,
)


CURRENT_SCIENTIFIC_PARENT="b0be049a0899ec653a36956d363c43eb762426a2"
ORIGINAL_TRIPLES=12_704_100
RESULTS={
    "lex":(27,1,475,54,13300718437,
           "250bf7f6417561047d74083d01177a50a91b2473bef01b346e447526be85102d"),
    "reverse-line":(29,0,61,61,13301800312,
                    "36d28dd294c283e00a6e46179385fa4d65ac04706f1ceaddc0d66c292c183f7e"),
}


def independent_permanent_finite_ASET_referee():
    root=Path(__file__).parent
    cert=json.loads((root/
        "hyp105_w34_zero_incidence_erasure_certificates.json"
    ).read_text(encoding="utf-8"))
    previous=json.loads((root/
        "hyp105_w34_rebased_oneexchange_certificates.json"
    ).read_text(encoding="utf-8"))
    if (cert["exact_frozen_parent_SHA"]!=CURRENT_SCIENTIFIC_PARENT
        or cert["github_scientific_PR"]!=719
        or cert["github_original_initial_complete_runner"]!=41785719789
        or cert["all_original_source_column_count"]!=425
        or cert["full_physical_GF5_dimension"]!=28
        or cert["full_original_3subsets_per_external_referee"]!=ORIGINAL_TRIPLES
        or cert["full_original_2subsets_per_referee"]!=90100
        or not cert["all_1_2_3_original_subset_sum_collisions_zero_for_both_frozen_source_maps"]
        or cert["all_h_theorem_proved"]
        or cert["asymptotic_exponent_improved"]
        or cert["root_230_status"]!="OPEN_WITH_FORMAL_BLOCKER"
        or set(cert["scheme_results"])!=set(RESULTS)
        or len(PALETTES)!=51):
        raise AssertionError("not a frozen 425-ORIGINAL-column GF5 W34 source certificate")
    if (previous["scientific_parent_exact_SHA"]!=
        "81c0ee7149859ec7ac4dbe0e997e4541fb19de7f"
        or set(previous["schemes"])!=set(RESULTS)):
        raise AssertionError("frozen #718 parent source drift")

    report={}
    for scheme,(steps,prior_r2,prior_d3,prior_r3,artifact_id,artifact_hash) in RESULTS.items():
        model=pair_labeled_symplectic(2,scheme)
        if (model["s"],model["N"],model["m"])!=(4,425,28):
            raise AssertionError("not true symplectic W(3,4) source model")
        if len(model["incidences"])!=425 or len(set(model["incidences"]))!=425:
            raise AssertionError("not all 425 genuine ORIGINAL point-line flags")
        z=cert["scheme_results"][scheme]
        initial=tuple(z["original_source_425_legal_palette_indices_before"])
        final=tuple(z["exact_source_425_GF5_legal_palette_indices_after"])
        upstream=tuple(previous["schemes"][scheme][
            "full_original_425_GF5_source_palettes_after"])
        if (initial!=upstream or len(final)!=425 or
            not all(type(x) is int and 0<=x<51 for x in final)
            or tuple(z["starting_full_original_D2_D3_TRUE_R3"])!=
            (prior_r2,prior_d3,prior_r3)
            or tuple(z["final_independently_exact_rehashed_full_original_D2_D3_TRUE_R3"])!=(0,0,0)
            or z["edited_real_original_flags_count"]!=steps
            or z["hosted_complete_source_trace_artifact_id"]!=artifact_id
            or z["hosted_complete_source_trace_uncompressed_SHA256"]!=artifact_hash
            or not z["all_source_edits_form_disjoint_original_ID_set"]
            or not z["all_edits_prove_no_new_source_signed_R3_event"]
            or not z["complete_425_original_source_zero_to_three_ASET"]
            or not z["original_global_maps_f_g_unchanged"]
            or not z["root_all_h_existence_not_established"]):
            raise AssertionError("committed source W34 proof scope mismatch")
        idx=list(initial)
        risks=(prior_r2,prior_d3,prior_r3)
        touched=set()
        trace=z["exact_global_source_palette_edit_trace"]
        if len(trace)!=steps:
            raise AssertionError("missing original source coefficient edit")
        for i,edit in enumerate(trace):
            id=edit["original_source_flag_ID"]
            src_old=edit["legal_palette_before"]
            src_new=edit["legal_palette_after"]
            count=edit["exact_original_signed_R3_events_removed"]
            new_r2=edit["complete_source_risk_after_D2_D3_R3"][0]
            if (edit["step"]!=i or id in touched or
                type(id) is not int or not 0<=id<425 or
                idx[id]!=src_old or src_new==src_old
                or type(src_new) is not int or not 0<=src_new<51
                or count<0 or
                edit["exact_new_signed_six_ID_R3_events_introduced"]!=0
                or tuple(edit["complete_source_risk_before_D2_D3_R3"])!=risks):
                raise AssertionError("source trace not original or not consecutive")
            touched.add(id)
            r3=risks[2]-count
            if r3<0 or new_r2<0 or new_r2>risks[0] or (
                r3>=risks[2] and new_r2>=risks[0]):
                raise AssertionError("source trace claims fake non-decreasing step")
            computed=(new_r2,r3+421*new_r2,r3)
            if tuple(edit["complete_source_risk_after_D2_D3_R3"])!=computed:
                raise AssertionError("incorrect exact original GF5 risk arithmetic")
            idx[id]=src_new
            risks=computed
        if tuple(idx)!=final or risks!=(0,0,0):
            raise AssertionError("complete 425 source coefficient sequence does not end at true zero")
        checks=z["full_12704100_original_3sum_physical_GF5_independent_checkpoints"]
        if (len(checks)!=6 or checks[0]["after_accepted_edits"]!=0
            or checks[-1]["after_accepted_edits"]!=steps):
            raise AssertionError("complete hosted source proof checkpoints missing")
        for c in checks:
            n=c["after_accepted_edits"]
            claimed=tuple(c["independent_full_original_GF5_12704100_triple_risk"])
            predicted=(prior_r2,prior_d3,prior_r3) if n==0 else tuple(
                trace[n-1]["complete_source_risk_after_D2_D3_R3"])
            if (not 0<=n<=steps or claimed!=predicted or
                not c["entire_sixflag_signed_event_set_verified_equal"]):
                raise AssertionError("hosted independent source proof checkpoint falsified")

        # Independent actual W34 425-source physical GF5 construction:
        ids,columns=exact_gf5_original_vectors(model,tuple(final))
        if ids!=tuple(range(425)) or len(set(columns))!=425:
            raise AssertionError("duplicate ORIGINAL source physical GF5 column")
        if len(set(final))<2:
            raise AssertionError("not a genuine 51-coefficient source assignment")
        for i,col in enumerate(columns):
            support=_real_original_source_support(model,i)
            if (len(col)!=28 or len(set(support))!=4
                or sum(bool(x) for x in col)!=4
                or sum(col)%5!=4
                or tuple(col[j] for j in support)!=tuple(PALETTES[final[i]])):
                raise AssertionError("invalid original 2point+2line physical source f/g")
        if len(_two_sum_collision_source_pairs(model,tuple(final)))!=0:
            raise AssertionError("real 90,100 original GF5 2-subset sums not unique")
        # Completely independent #713 exact-on-disk 12-byte signature
        # algorithm: all 12,704,100 ORIGINAL three-source subsets,
        # no hash truncation or source-local derivative input.
        external=exact_full_original_external_r3(
            model,tuple(final),max_triples=ORIGINAL_TRIPLES,
            max_witnesses=8)
        observed=(
            external["R2_signed_2v2_events_exact"],
            external["equal_sum_pairs_of_distinct_ORIGINAL_triples"],
            external["FULL_six_distinct_original_ID_3v3_signed_event_count"])
        if (observed!=(0,0,0)
            or external["all_triples_exact_external_disk_records_processed"]!=ORIGINAL_TRIPLES
            or external["all_source_triple_count"]!=ORIGINAL_TRIPLES
            or external["distinct_complete_GF5_three_source_sums"]!=ORIGINAL_TRIPLES
            or not external["complete_source_GF5_zero_to_three_ASET"]
            or not external["independent_original_R2_to_R3_overlap_identity_verified"]
            or len(external["verified_independent_true_source_witnesses"])!=0
            or not external["no_false_negative_from_hashed_or_sampled_sums"]):
            raise AssertionError("independent full ORIGINAL GF5 1/2/3 census found a collision")
        # Cross-cardinality avoidance is independently forced by
        # exact original source checksum 4 per column in GF5:
        # k=0,1,2,3 have aggregate checksums 0,4,3,2.
        distinct_cardinality_sums=tuple((4*k)%5 for k in range(4))
        if len(set(distinct_cardinality_sums))!=4:
            raise AssertionError("cross-cardinality physical GF5 checksum not unique")
        report[scheme]={
            "full_real_W34_original_425_source_columns":425,
            "complete_original_1subsets_unique":425,
            "complete_original_2subsets_unique":math.comb(425,2),
            "complete_original_3subsets_unique":ORIGINAL_TRIPLES,
            "source_cardinalities_0_to_3_disjoint_checksum_GF5":
                distinct_cardinality_sums,
            "original_GF5_physical_coordinates":28,
            "full_independent_source_D2_D3_TRUE_R3":observed,
            "complete_425_source_0to3_ASET":True,
            "source_f_g_unchanged":True,
            "actual_original_source_edits_independently_replayed":steps,
            "source_trace_checkpoints":len(checks),
            "root_all_h_theorem_still_open":True,
        }
    return report


if __name__=="__main__":
    print(json.dumps(independent_permanent_finite_ASET_referee(),
                     indent=2,sort_keys=True))
