"""Independent permanent EXACT minimum-recolor referee for true W(3,4).

Does NOT import AA4-MULTI CEGAR, native search or its dynamic source
hash. It reads immutable before and COMMITTED after original 425-source
palettes, constructs REAL symplectic point/line W(3,4) with separately
globally pair-injective f,g, directly audits all signed initial R2/R3
source physical events, repeats exact minimum hitting-set proof, and
(in --full mode) replays the original external 12-byte 12,704,100-triple
radix referee BOTH before and after, plus complete original pairs.

The exact minimum number of changed ORIGINAL columns at these TWO
specific maps does not prove root seven-motif all-h HYP-105 #230.
"""
from itertools import combinations
from pathlib import Path
import argparse
import json
import math

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_original_gf5_deterministic_extraction_referee import PALETTES
from hyp105_original_event_cover import (
    normalize_edges,covers,verify_disjoint_packing,
    bounded_exact_cover,canonical_signed_partition)
from hyp105_w34_external_triple_r3_referee import (
    exact_gf5_original_vectors,exact_full_original_external_r3)

ROOT=Path(__file__).parent
PARENT_724="c2354156a23f36e5f3e7b24a104a052c18a6cc55"
MAIN_CERT=ROOT/"hyp105_w34_minimal_source_recolor_certificates.json"
OLD_CERT=ROOT/"hyp105_w34_zero_incidence_erasure_certificates.json"
COVER_CERT=ROOT/"hyp105_w34_original_event_cover_certificates.json"
TRIPLES=12_704_100
PAIRS=90_100
EXPECTED={"lex":(25,27,1,475,54),"reverse-line":(26,29,0,61,61)}


def pair_sum_collisions_direct(vectors):
    """Different direct 28-digit GF5 original pair scan, not C++ CEGAR."""
    bysum={}
    bad=[]
    for i,j in combinations(range(len(vectors)),2):
        signature=tuple((u+v)%5 for u,v in zip(vectors[i],vectors[j]))
        previous=bysum.get(signature)
        if previous is not None:
            if set(previous)&{i,j}:
                raise AssertionError("unexpected repeated original singleton vector")
            bad.append(tuple(sorted((previous,(i,j)))))
        else:
            bysum[signature]=(i,j)
    if len(bysum)+len(bad)!=PAIRS:
        raise AssertionError("missing or duplicate original physical two-sums")
    return tuple(sorted(bad))


def checked_inputs(scheme):
    if scheme not in EXPECTED:raise ValueError("only true fixed W34 source maps")
    c=json.loads(MAIN_CERT.read_text(encoding="utf-8"))
    old=json.loads(OLD_CERT.read_text(encoding="utf-8"))
    low=json.loads(COVER_CERT.read_text(encoding="utf-8"))
    if (c["schema"]!="mathlab.hyp105.W34-exact-source-recolor-minima.v1"
        or c["parent_scientific_exact_SHA"]!=PARENT_724
        or c["original_root_status"]!="OPEN_WITH_FORMAL_BLOCKER"
        or c["all_h_existence_or_asymptotic_exponent_claimed"]
        or not c["finite_original_W34_both_optimizers_independently_fully_certified"]
        or set(c["schemes"])!=set(EXPECTED)
        or old["root_230_status"]!="OPEN_WITH_FORMAL_BLOCKER"
        or low["root_status"]!="OPEN_WITH_FORMAL_BLOCKER"):
        raise AssertionError("scientific root/parent source provenance changed")
    z=c["schemes"][scheme];lz=low["schemes"][scheme]
    seed=old["scheme_results"][scheme]
    tau,prior,r2,d3,r3=EXPECTED[scheme]
    before=tuple(seed["original_source_425_legal_palette_indices_before"])
    after=tuple(z["exact_425_original_GF5_after_palettes"])
    changed=tuple(i for i in range(425) if before[i]!=after[i])
    if (len(before)!=425 or len(after)!=425 or
        any(type(x) is not int or not 0<=x<51 for x in before+after)
        or changed!=tuple(lz["explicit_original_ID_hitting_set"])
        or changed!=tuple(z["minimum_support_original_IDs"])
        or len(changed)!=tau
        or z["exact_minimal_original_source_changes"]!=tau
        or z["upper_bound_actual_original_changed_source_IDs"]!=tau
        or z["lower_bound_original_source_transversal"]!=tau
        or tuple(z["original_source_before_palettes"])!=before
        or tuple(z["edited_legal_palettes_on_support"])!=tuple(after[i] for i in changed)
        or z["root_original_hypothesis_230_A_B_C_proved"]
        or z["source_hosted_original_CEGAR_run_id"]!=41878874102
        or z["source_hosted_original_CEGAR_job_id"]!=(
            126745909421 if scheme=="lex" else 126745909376)
        or z["host_CEGAR_rounds"]!=1
        or z["host_CEGAR_verified_hypernogoods"]!=0
        or z["complete_actual_source_GF5_R2_D3_signed_R3_after"]!=[0,0,0]
        or z["independent_full_original_triples_reprocessed"]!=TRIPLES
        or z["independent_full_original_pairs_reprocessed"]!=PAIRS
        or lz["transversal_certified_lower"]!=tau
        or lz["hitting_set_certified_upper"]!=tau
        or lz["bounded_exact_search_status"]!="EXACT"
        or lz["existing_719_safe_erasure_edit_count"]!=prior
        or lz["initial_complete_D2_D3_TRUE_R3"]!=[r2,d3,r3]
        or z["exact_initial_r2_d3_r3"]!=[r2,d3,r3]
        or lz["all_original_triples_exactly_audited"]!=TRIPLES):
        raise AssertionError("new optimal 425-original-W34 source certificate drift")
    model=pair_labeled_symplectic(2,scheme)
    if ((model["s"],model["N"],model["m"])!=(4,425,28)
        or len(model["incidences"])!=425
        or len(set(model["incidences"]))!=425):
        raise AssertionError("not the true complete original W34 incidence geometry")
    before_ids,before_vectors=exact_gf5_original_vectors(model,before)
    after_ids,after_vectors=exact_gf5_original_vectors(model,after)
    if before_ids!=tuple(range(425)) or after_ids!=before_ids:
        raise AssertionError("not original global 425 source IDs")
    for vectors,indices in ((before_vectors,before),(after_vectors,after)):
        if (len(vectors)!=425 or len(set(vectors))!=425
            or any(len(v)!=28 or sum(v)%5!=4 or
                   sum(q!=0 for q in v)!=4 for v in vectors)):
            raise AssertionError("original GF5^28 column support/checksum/injection invalid")
        a=model["a"]
        for id,(point,line) in enumerate(model["incidences"]):
            support=tuple(model["left_labels"][point]) + tuple(
                a+x for x in model["right_labels"][line])
            if (len(support)!=4 or len(set(support))!=4
                or tuple(vectors[id][coord] for coord in support)!=PALETTES[indices[id]]):
                raise AssertionError("physical coefficients did not preserve globally fixed source f/g")
    for i in range(425):
        if i not in changed and before_vectors[i]!=after_vectors[i]:
            raise AssertionError("frozen ORIGINAL source vector changed")
        if i in changed and before_vectors[i]==after_vectors[i]:
            raise AssertionError("fake changed original source palette")
    return model,before,after,before_vectors,after_vectors,lz,z,changed


def verify_minimum_theorem(scheme):
    model,before,after,initial,final,lz,z,T=checked_inputs(scheme)
    r2,d3,r3=EXPECTED[scheme][2:]
    events=[]
    for k,name in ((2,"initial_R2_true_original_signed_partitions"),
                   (3,"initial_R3_true_original_signed_partitions")):
        source=lz[name]
        if len(source)!=(r2 if k==2 else r3):
            raise AssertionError("original signed event counts altered")
        signed=tuple(canonical_signed_partition(x,k) for x in source)
        if len(set(signed))!=len(signed):
            raise AssertionError("duplicate signed original source event")
        for a,b in signed:
            if len(set(a+b))!=2*k or not set(a+b)&set(T):
                raise AssertionError("original event not hit by new minimal source T")
            for coord in range(28):
                if sum(initial[i][coord] for i in a)%5 != sum(
                        initial[i][coord] for i in b)%5:
                    raise AssertionError("not an initial physical GF5 signed source event")
        events.extend(signed)
    if pair_sum_collisions_direct(initial)!=tuple(sorted(
            canonical_signed_partition(x,2) for x in
            lz["initial_R2_true_original_signed_partitions"])):
        raise AssertionError("independently complete initial original 2v2 census disagrees")
    edges=normalize_edges(a+b for a,b in events)
    if (len(edges)!=lz["distinct_original_ID_hyperedges"]
        or not covers(edges,T)
        or z["original_event_hypergraph_count"]!=lz["full_original_event_witness_count"]):
        raise AssertionError("initial true original event hypergraph or cover drift")
    packed=tuple(tuple(x) for x in lz["vertex_disjoint_original_event_packing"])
    if verify_disjoint_packing(edges,packed)!=lz["packing_certified_lower"]:
        raise AssertionError("invalid lower-packing original signed source witness")
    # The all-N hitting-set necessity applies to ANY final legal palette
    # assignment, even simultaneous nonmonotone recoloring.
    if scheme=="reverse-line":
        if len(packed)!=26:
            raise AssertionError("missing 26 pairwise original source event packing")
        lower_proof="26 source-disjoint physical signed events"
    else:
        exact=bounded_exact_cover(
            edges,upper_cover=T,max_nodes=250000)
        if (exact["status"],exact["lower"],exact["upper"])!=("EXACT",25,25):
            raise AssertionError("complete lex k<25 hitting-set UNSAT was not proved")
        if exact["exhausted_depths"]!=(23,24):
            raise AssertionError("missing independently exhaustive lex 23/24 refutations")
        lower_proof="exact original 74-source incidence-dominance kernel, exhaustive k=23,24 refutation"
    if pair_sum_collisions_direct(final):
        raise AssertionError("new candidate contains complete original 2v2 physical collisions")
    return {
        "scheme":scheme,
        "true_original_W34_flag_count":425,
        "full_physical_GF5_dimension":28,
        "before_original_R2_D3_true_R3":[r2,d3,r3],
        "independently_revalidated_original_initial_signed_events":len(events),
        "exact_original_initial_event_hyperedges":len(edges),
        "independently_reproven_universal_to_this_fixed_source_min_changes":len(T),
        "independent_lower_proof":lower_proof,
        "new_constructive_source_edits":len(T),
        "changed_original_source_IDs":list(T),
        "all_90_100_final_original_pairs_independently_collision_free":True,
        "complete_0_to_3_ASET_after_full_triple_census":None,
        "root_230_status":"OPEN_WITH_FORMAL_BLOCKER"
    }


def verify_complete_physical(scheme):
    result=verify_minimum_theorem(scheme)
    model,before,after,*unused=checked_inputs(scheme)
    for kind,indices in (("before",before),("after",after)):
        z=exact_full_original_external_r3(
            model,indices,max_triples=TRIPLES,max_witnesses=4)
        expected=EXPECTED[scheme][2:] if kind=="before" else (0,0,0)
        data=(z["R2_signed_2v2_events_exact"],
              z["equal_sum_pairs_of_distinct_ORIGINAL_triples"],
              z["FULL_six_distinct_original_ID_3v3_signed_event_count"])
        if (data!=expected
            or z["all_triples_exact_external_disk_records_processed"]!=TRIPLES
            or z["all_source_triple_count"]!=TRIPLES
            or z["all_425_original_flags_in_scope"] is not True
            or z["no_false_negative_from_hashed_or_sampled_sums"] is not True
            or z["independent_original_R2_to_R3_overlap_identity_verified"] is not True
            or z["complete_source_GF5_zero_to_three_ASET"] is not (kind=="after")):
            raise AssertionError("incomplete source GF5^28 independent original 3sum census")
        result["complete_original_GF5_"+kind+"_census"]=list(data)
    result["complete_0_to_3_ASET_after_full_triple_census"]=True
    result["all_12_704_100_original_three_subsets_independently_audited_BEFORE_AND_AFTER"]=True
    # Each source has coefficient sum 4 mod5: k=0,1,2,3 sums have
    # distinct GF5 checksums 0,4,3,2; no cross-size collisions exist.
    result["cross_cardinality_subset_sums_distinct_mod5_checksum"]=True
    result["exact_minimum_recolors_theorem_for_this_fixed_W34_map"]=True
    return result


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--scheme",choices=tuple(EXPECTED),required=True)
    parser.add_argument("--full",action="store_true")
    args=parser.parse_args()
    result=(verify_complete_physical(args.scheme) if args.full else
            verify_minimum_theorem(args.scheme))
    print("AA4_FINITE_W34_EXACT_MINIMUM_CERTIFICATE_PASS="+json.dumps(
        result,sort_keys=True,separators=(",",":")),flush=True)

if __name__=="__main__":
    main()
