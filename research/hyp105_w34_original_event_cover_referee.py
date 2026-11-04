"""True ORIGINAL 425-flag W(3,4) signed-event / transversal referee.

The #713 independently implemented lossless external GF(5)^28 radix
census enumerates ALL 12,704,100 ORIGINAL triples. This module
extracts ALL true signed six-distinct-source witnesses, independently
checks their complete 28-coordinate GF5 equations and actual R2
source events, then computes explicitly verifiable finite vertex-cover
and disjoint-packing certificates. No all-h conclusion is claimed.
"""
import argparse
import json
from pathlib import Path

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_w34_external_triple_r3_referee import (
    exact_gf5_original_vectors, exact_full_original_external_r3)
from hyp105_w34_projected_source_palette_repair_referee import (
    _two_sum_collision_source_pairs)
from hyp105_original_event_cover import (
    canonical_signed_partition, normalize_edges, covers,
    greedy_cover, greedy_packing, verify_disjoint_packing,
    bounded_exact_cover)


SOURCE_CERT=Path(__file__).with_name(
    "hyp105_w34_zero_incidence_erasure_certificates.json")
PARENT="8bdef0393e197d02b09c56addd55dacff16254d8"
SOURCE_PARENT="bb9378cac271cbfb8f6f446d932fd009178f8d79"
TRIPLES=12_704_100
EXPECTED={"lex":(1,475,54,27),"reverse-line":(0,61,61,29)}


def _source_original_event_lists(scheme):
    if scheme not in EXPECTED:
        raise ValueError("only genuine original fixed W34 lex/reverse-line")
    cert=json.loads(SOURCE_CERT.read_text(encoding="utf-8"))
    if (cert["root_230_status"]!="OPEN_WITH_FORMAL_BLOCKER"
        or cert["all_h_theorem_proved"]
        or cert["all_original_source_column_count"]!=425
        or cert["exact_frozen_parent_SHA"]!=
           "b0be049a0899ec653a36956d363c43eb762426a2"):
        raise AssertionError("source parent governance drift")
    z=cert["scheme_results"][scheme]
    before=tuple(z["original_source_425_legal_palette_indices_before"])
    after=tuple(z["exact_source_425_GF5_legal_palette_indices_after"])
    model=pair_labeled_symplectic(2,scheme)
    r2,d3,r3,edit_count=EXPECTED[scheme]
    if (model["s"],model["N"],model["m"])!=(4,425,28):
        raise AssertionError("not complete genuine original W34 geometry")
    if (len(set(model["incidences"]))!=425 or len(before)!=425
        or len(after)!=425 or
        tuple(z["starting_full_original_D2_D3_TRUE_R3"])!=(r2,d3,r3)
        or tuple(z["final_independently_exact_rehashed_full_original_D2_D3_TRUE_R3"])
              !=(0,0,0)
        or len(z["exact_global_source_palette_edit_trace"])!=edit_count):
        raise AssertionError("wrong fixed original source or risk census")
    ids,columns=exact_gf5_original_vectors(model,before)
    if ids!=tuple(range(425)) or len(set(columns))!=425:
        raise AssertionError("invalid original distinct source columns")
    # This source physical audit enumerates ALL exact complete 28D
    # ORIGINAL source triple signatures without sampling or hashing.
    external=exact_full_original_external_r3(
        model,before,max_triples=TRIPLES,max_witnesses=256)
    risk=(external["R2_signed_2v2_events_exact"],
          external["equal_sum_pairs_of_distinct_ORIGINAL_triples"],
          external["FULL_six_distinct_original_ID_3v3_signed_event_count"])
    if (risk!=(r2,d3,r3)
        or external["all_triples_exact_external_disk_records_processed"]!=TRIPLES
        or external["all_source_triple_count"]!=TRIPLES
        or not external["independent_original_R2_to_R3_overlap_identity_verified"]
        or d3!=r3+421*r2):
        raise AssertionError(("physical source triple census mismatch",risk))
    r3signed=set()
    for w in external["verified_independent_true_source_witnesses"]:
        event=tuple(sorted((tuple(sorted(w["positive_ORIGINAL_three"])),
                            tuple(sorted(w["negative_ORIGINAL_three"])))))
        canonical_signed_partition(event,3)
        if tuple(w["six_distinct_ORIGINAL_flag_IDs"])!=tuple(
                sorted(event[0]+event[1])):
            raise AssertionError("fake true ORIGINAL source witness")
        r3signed.add(event)
    if len(r3signed)!=r3:
        raise AssertionError("missing or duplicate actual signed R3 event")
    r2signed=set()
    for parts in _two_sum_collision_source_pairs(model,before):
        event=tuple(sorted((tuple(sorted(parts[0])),
                            tuple(sorted(parts[1])))))
        canonical_signed_partition(event,2)
        r2signed.add(event)
    if len(r2signed)!=r2:
        raise AssertionError("missing original four-ID R2 event")
    # Independent direct 28D physical coordinate validation of EVERY
    # signed witness emitted by the external signature bucket method.
    for k,events in ((2,r2signed),(3,r3signed)):
        for a,b in events:
            canonical_signed_partition((a,b),k)
            for j in range(28):
                if sum(columns[i][j] for i in a)%5 != sum(
                        columns[i][j] for i in b)%5:
                    raise AssertionError("fake original physical GF5 cancellation")
    original_edits=tuple(
        step["original_source_flag_ID"]
        for step in z["exact_global_source_palette_edit_trace"])
    if len(set(original_edits))!=edit_count:
        raise AssertionError("repeated original source ID in clean erasure")
    r2events=tuple(sorted(r2signed))
    r3events=tuple(sorted(r3signed))
    edges=normalize_edges(tuple(a+b for es in (r2events,r3events)
                                for a,b in es))
    if not covers(edges,original_edits):
        raise AssertionError("W34 full erasure violates initial-source cover")
    return r2events,r3events,edges,original_edits,risk


def source_cover_report(scheme, max_nodes=250000):
    r2events,r3events,edges,edits,risk=_source_original_event_lists(scheme)
    candidates=(
        greedy_cover(edges,seed_cover=edits),
        greedy_cover(edges))
    upper=min(candidates,key=lambda ids:(len(ids),ids))
    packing=greedy_packing(edges,restarts=256)
    result=bounded_exact_cover(edges,upper_cover=upper,max_nodes=max_nodes)
    if (not covers(edges,result["cover"])
        or verify_disjoint_packing(edges,packing)!=len(packing)
        or result["lower"]<len(packing)
        or result["upper"]>len(edits)):
        raise AssertionError("unproved original hypergraph cover bound")
    return {
        "schema":"mathlab.hyp105.original-w34-event-cover.v1",
        "scheme":scheme,
        "scientific_parent_HEAD":PARENT,
        "zero_source_parent_719_SHA":SOURCE_PARENT,
        "source":"true original W(3,4) global fixed pair-injective point/line f/g",
        "original_flag_count":425,
        "complete_GF5_physical_dimension":28,
        "all_original_triples_exactly_audited":TRIPLES,
        "initial_complete_D2_D3_TRUE_R3":list(risk),
        "initial_R2_true_original_signed_partitions":
            [[list(a),list(b)] for a,b in r2events],
        "initial_R3_true_original_signed_partitions":
            [[list(a),list(b)] for a,b in r3events],
        "distinct_original_ID_hyperedges":len(edges),
        "existing_719_safe_erasure_edit_count":len(edits),
        "existing_719_true_original_source_edits":list(edits),
        "vertex_disjoint_original_event_packing":
            [list(e) for e in packing],
        "packing_certified_lower":len(packing),
        "explicit_original_ID_hitting_set":list(result["cover"]),
        "hitting_set_certified_upper":result["upper"],
        "transversal_certified_lower":result["lower"],
        "bounded_exact_search_status":result["status"],
        "bounded_exact_search_visited_nodes":result["nodes"],
        "exhaustively_refuted_cardinalities":
            list(result["exhausted_depths"]),
        "full_original_event_witness_count":
            len(r2events)+len(r3events),
        "cover_is_NOT_a_proven_clean_GF5_palette_schedule":True,
        "no_asymptotic_exponent":True,
        "root_230_status":"OPEN_WITH_FORMAL_BLOCKER",
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--scheme",required=True,choices=tuple(EXPECTED))
    parser.add_argument("--max-nodes",type=int,default=250000)
    parser.add_argument("--out",required=True,type=Path)
    args=parser.parse_args()
    report=source_cover_report(args.scheme,max_nodes=args.max_nodes)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",
                        encoding="utf-8")
    # The complete source signed hypergraph is compact (<20KB) and
    # separately saved as an Actions artifact plus exact job-log line.
    print("AA4_ORIGINAL_EVENT_COVER_CERTIFICATE="+
          json.dumps(report,sort_keys=True,separators=(",",":")))
    print("AA4_W34_FINITE_ONLY__ROOT_230_OPEN_WITH_FORMAL_BLOCKER")


if __name__=="__main__":
    main()
