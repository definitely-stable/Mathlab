"""HYP-105 AA4-ERASE0: exact source-preserving R3 conflict-erasure search.

NEW all-N theorem: If changing ONE original flag i to a legal GF(5)
four-coordinate palette t gives H_i(t)=0, where H_i(t) counts
source-disjoint (2 other positives)+(3 negatives) in complete physical
GF(5)^m, then NO NEW six-distinct-original-ID 3+3 signed event exists.
Every previously existing event containing i is deleted; every event
avoiding i is invariant. Consequently E_new = E_old \ {e: i in e}.

The preexisting (independently all-51 real W32 validated) exact
C++ source-local GF5 oracle computes H_i(t) and the separate R2
incident histogram for all 51 palettes in ONE complete pass through
the other C(424,3)=12,614,424 actual source triples. This driver
requires H_i(t)=0, R2 nonincrease, actual physical source validity
and strictly decreasing integer potential (R2+R3).

The initial signed-event hypergraph is obtained by an INDEPENDENT
full 12,704,100-triple physical GF5^28 external census on actual
full 425-original-flag W(3,4) source columns. It is then maintained
by the mathematically exact no-new-event invariant: never infer that
a vague local score implies zero incidents.

At configured checkpoints and final, an INDEPENDENT complete external
disk-based 12.7m source-triple auditor rebuilds all current 28D GF5
sums and compares the exact canonical signed-event hypergraph.
No fake source/independent random flags, no graph-class filtering,
no change to fixed globally separately pair-injective f/g.

If an event cannot be erased by any tested source, report a bounded
STOP, NOT a full source nonexistence or all-h theorem.
"""
import argparse
from collections import Counter
from pathlib import Path
from itertools import chain
import json
import math
import subprocess
import tempfile

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_w34_direct_r3_palette_derivative_referee import (
    _all_current_actual_signed_witnesses,
)
from hyp105_w34_external_triple_r3_referee import (
    exact_full_original_external_r3, exact_gf5_original_vectors,
)
from hyp105_w34_projected_source_palette_repair_referee import (
    _two_sum_collision_source_pairs,
)
from hyp105_w34_oneexchange_exhaustive_referee import (
    construct_exact_source_text,
)
from hyp105_w34_rebased_oneexchange_referee import (
    frozen_complete_W34_sources as _frozen_rebased_source,
)


ALL_TRIPLES=12_704_100
PARENT_SHA="b0be049a0899ec653a36956d363c43eb762426a2"
LIMBS=51


def frozen_current_original_W34(scheme):
    if scheme not in ("lex","reverse-line"):
        raise ValueError("only actual symplectic W(3,4) globally fixed source f/g")
    z=_frozen_rebased_source()["schemes"][scheme]
    c=Path(__file__).with_name(
        "hyp105_w34_rebased_oneexchange_certificates.json")
    cert=json.loads(c.read_text(encoding="utf-8"))
    if (cert["scientific_parent_exact_SHA"]!=
        "81c0ee7149859ec7ac4dbe0e997e4541fb19de7f"
        or not cert["original_source_maps_f_g_unchanged"]
        or not cert["scientific_no_asymptotic_exponent_proved"]
        or set(cert["schemes"])!={"lex","reverse-line"}):
        raise AssertionError("not exact frozen #718 original source witness")
    expected={
        "lex":((1,479,58),(1,475,54),(276,6,0)),
        "reverse-line":((0,65,65),(0,61,61),(285,50,3)),
    }
    old,after,(source,prior,new)=expected[scheme]
    if (tuple(z["after_independently_rehashed_FULL_D2_D3_TRUE_R3"])!=old
        or tuple(cert["schemes"][scheme][
            "before_FULL_D2_D3_TRUE_R3"])!=old
        or tuple(cert["schemes"][scheme][
            "after_independently_rehashed_FULL_D2_D3_TRUE_R3"])!=after):
        raise AssertionError("not exact independently audited 54/61 W34 source")
    previous=tuple(z["full_original_425_GF5_after_source_palette_indices"])
    updated=tuple(cert["schemes"][scheme][
        "full_original_425_GF5_source_palettes_after"])
    change=cert["schemes"][scheme]["optimal_one_source_change"]
    if (len(previous)!=425 or len(updated)!=425
        or {i for i in range(425) if previous[i]!=updated[i]}!={source}
        or (previous[source],updated[source])!=(prior,new)
        or (change["original_source_flag_ID"],
            change["prior_legal_checksum4_palette_index"],
            change["new_legal_checksum4_palette_index"])!=
            (source,prior,new)
        or not cert["schemes"][scheme][
            "independent_full_12704100_original_source_triples_rehashed"]):
        raise AssertionError("actual W34 after #718 source palettes changed")
    return updated,after


def canonical_event(w):
    p=tuple(sorted(w["positive_ORIGINAL_three"]))
    q=tuple(sorted(w["negative_ORIGINAL_three"]))
    six=tuple(sorted(p+q))
    if len(p)!=3 or len(q)!=3 or len(set(six))!=6 or tuple(
        w["six_distinct_ORIGINAL_flag_IDs"])!=six:
        raise AssertionError("not a true six-distinct original GF5 signed event")
    return tuple(sorted((p,q)))


def _full_independent_checkpoint(model,indices,r2,events,*,stage):
    """Independently rehash ALL triples and exact signed hyperedges."""
    r3=len(events)
    full=exact_full_original_external_r3(
        model,tuple(indices),max_triples=ALL_TRIPLES,
        max_witnesses=max(256,r3+1))
    actual=(
        full["R2_signed_2v2_events_exact"],
        full["equal_sum_pairs_of_distinct_ORIGINAL_triples"],
        full["FULL_six_distinct_original_ID_3v3_signed_event_count"])
    predicted=(r2,r3+421*r2,r3)
    if actual!=predicted or full[
        "all_triples_exact_external_disk_records_processed"]!=ALL_TRIPLES or not full[
        "independent_original_R2_to_R3_overlap_identity_verified"]:
        raise AssertionError(("full physical W34 original GF5 audit refutes "
                              "zero-new-conflict induction",stage,actual,predicted))
    independent=full["verified_independent_true_source_witnesses"]
    if len(independent)!=r3:
        raise AssertionError("independent full signed-event witness budget incomplete")
    old_set={canonical_event(w) for w in events}
    new_set={canonical_event(w) for w in independent}
    if len(old_set)!=r3 or len(new_set)!=r3 or old_set!=new_set:
        raise AssertionError(("new/unreported six-distinct-source 3v3 collision "
                              "despite exact H_i(new)=0",stage,r3))
    return {
        "stage":stage,"full_GF5_original_triples_rehashed":ALL_TRIPLES,
        "source_R2_D3_TRUE_R3":actual,
        "canonical_six_source_event_sets_independently_equal":True,
        "physical_28D_GF5_signed_events_all_verified":True,
        "complete_zero_to_three_ORIGINAL_ASET":full[
            "complete_source_GF5_zero_to_three_ASET"],
    }


def _current_source_physics(model,indices,r2,events,*,validate_each_event):
    """Fast independently reconstructed 28D physical GF5 source checks."""
    idx,cols=exact_gf5_original_vectors(model,tuple(indices))
    if idx!=tuple(range(425)) or len(set(cols))!=425:
        raise AssertionError("missing or duplicate genuine ORIGINAL source ID")
    if any(len(w)!=28 or sum(w)%5!=4 or
           sum(bool(v) for v in w)!=4 for w in cols):
        raise AssertionError("invalid 2+2 physical original GF5 source column")
    if len(_two_sum_collision_source_pairs(model,tuple(indices)))!=r2:
        raise AssertionError("external two-original-source GF5 R2 guard failed")
    if validate_each_event:
        for w in events:
            plus=tuple(w["positive_ORIGINAL_three"])
            minus=tuple(w["negative_ORIGINAL_three"])
            if any(sum(cols[i][j] for i in plus)%5!=
                   sum(cols[i][j] for i in minus)%5 for j in range(28)):
                raise AssertionError("retained true original 28D signed equation invalid")
    return cols


def _candidate_source_priority(events,r2_source_events):
    """Try all true R2-collision endpoints first, then R3 hottest source."""
    degree=Counter(i for w in events for i in
                   w["six_distinct_ORIGINAL_flag_IDs"])
    if sum(degree.values())!=6*len(events):
        raise AssertionError("incorrect exact source signed incidence degrees")
    two=sorted(set(chain.from_iterable(
        chain.from_iterable(pair) for pair in r2_source_events)),
        key=lambda i:(-degree[i],i))
    active=sorted(degree,key=lambda i:(-degree[i],i))
    return tuple(dict.fromkeys((*two,*active))),degree


def _compile_cpp_oracle(binary):
    cpp=Path(__file__).with_name("hyp105_w34_oneexchange_exact.cpp")
    p=subprocess.run([
        "g++","-O3","-std=c++17","-Wall","-Wextra","-pedantic",
        str(cpp),"-o",str(binary)],
        capture_output=True,text=True,timeout=120)
    if p.returncode!=0:
        raise AssertionError(("independent exact C++ GF5 compilation failed",
                              p.stderr[-6000:]))
    return str(binary)


def _all_51_for_real_source(model,indices,source_id,degree,r2,r3,binary,
                            temporary,*,step):
    """One independent complete 12,614,424-triple source H_i(t) census."""
    d3=r3+421*r2
    mock_full={
        "R2_signed_2v2_events_exact":r2,
        "equal_sum_pairs_of_distinct_ORIGINAL_triples":d3,
        "FULL_six_distinct_original_ID_3v3_signed_event_count":r3,
    }
    source=Path(temporary)/"current-original-source.txt"
    result=Path(temporary)/"current-original-source.json"
    source.write_text(construct_exact_source_text(
        model,tuple(indices),mock_full,((source_id,degree),)),encoding="utf-8")
    p=subprocess.run([binary,str(source),"0","1",str(result)],
                     capture_output=True,text=True,timeout=240)
    if p.returncode!=0:
        raise AssertionError(("source-local exact GF5 51-palette audit failed",
                              step,source_id,p.stderr[-6500:]))
    data=json.loads(result.read_text(encoding="utf-8"))
    if (data["schema"]!="mathlab.hyp105.original-w34-active-oneexchange-v1"
        or data["scheme"]!=model["scheme"] or data["n"]!=425
        or data["m"]!=28
        or (data["original_D2"],data["original_D3"],
            data["original_R3"])!=(r2,d3,r3)
        or data["total_active_original_IDs"]!=1
        or len(data["results"])!=1):
        raise AssertionError("C++ original GF5 source evidence missing")
    row=data["results"][0]
    old=indices[source_id]
    if (row["source_ID"]!=source_id or row["current_palette"]!=old
        or row["witness_degree"]!=degree or
        row["current_true_R3_incidence"]!=degree
        or len(row["H_R3_all_51"])!=LIMBS
        or len(row["H_R2_all_51"])!=LIMBS
        or row["H_R3_all_51"][old]!=degree
        or row["H_R2_all_51"][old]!=row["current_R2_cross_incidence"]):
        raise AssertionError("exact source H_i(current) disagrees with actual E")
    return row


def erasure_source_descent(scheme,*,max_steps=72,checkpoint_every=8):
    """True ORIGINAL W34 physical conflict-erasure with NO NEW R3 events."""
    if (type(max_steps) is not int or max_steps<1 or max_steps>100
        or type(checkpoint_every) is not int or checkpoint_every<1
        or checkpoint_every>64):
        raise ValueError("positive bounded original source step/checkpoint budget")
    model=pair_labeled_symplectic(2,scheme)
    if (model["s"],model["N"],model["m"])!=(4,425,28):
        raise AssertionError("not real symplectic original W(3,4) fixed source")
    old,initial=frozen_current_original_W34(scheme)
    idx=list(old)
    r2,d3,r3=initial
    _,signed=_all_current_actual_signed_witnesses(model,tuple(idx),initial)
    events=list(signed)
    if len(events)!=r3 or len({canonical_event(w) for w in events})!=r3:
        raise AssertionError("not complete ORIGINAL initial 3v3 collision hypergraph")
    evidence=[_full_independent_checkpoint(
        model,idx,r2,events,stage="before")]
    accepted=[]
    attempts=0
    rejected_no_zero=0
    last_independent_step=0
    status="MAX_STEPS_WITH_EVENTS"
    with tempfile.TemporaryDirectory(prefix="hyp105-real-w34-clean-") as work:
        binary=_compile_cpp_oracle(Path(work)/"hyp105-exact-51")
        for step in range(max_steps):
            before=(r2,r3+421*r2,len(events))
            if not events and r2==0:
                status="FULL_ZERO_GF5_0to3_ORIGINAL_ASET"
                break
            _current_source_physics(
                model,idx,r2,events,validate_each_event=True)
            twos=_two_sum_collision_source_pairs(model,tuple(idx))
            source_priority,degree=_candidate_source_priority(events,twos)
            if not source_priority:
                status="STOP_NO_R3_AND_NO_R2_SOURCE_TO_EDIT"
                break
            choice=None
            trials=0
            for source_id in source_priority:
                trials+=1
                row=_all_51_for_real_source(
                    model,idx,source_id,degree.get(source_id,0),
                    r2,len(events),binary,work,step=step)
                cur=idx[source_id]
                hi=row["H_R3_all_51"]
                ki=row["H_R2_all_51"]
                permitted=[]
                for palette in range(51):
                    next_r2=r2+ki[palette]-ki[cur]
                    # For erasure, not merely strict local-R3 decrease:
                    # guarantee no NEW signed 3+3 event uses this source.
                    if hi[palette]!=0 or not 0<=next_r2<=r2:
                        continue
                    reduction=degree.get(source_id,0)
                    if reduction==0 and next_r2==r2:continue
                    permitted.append((next_r2,-reduction,palette))
                if permitted:
                    selected=min(permitted)
                    choice=(source_id,row,selected[2],selected[0])
                    # Exhaust all currently present R2 endpoints
                    # before moving on: priority then lex first.
                    if r2==0 or selected[0]<r2 or
                       source_id not in set(chain.from_iterable(
                           chain.from_iterable(pair) for pair in twos)):
                        break
                else:
                    rejected_no_zero+=1
            if choice is None:
                status="STOP_NO_SAFE_ZERO_INCIDENCE_FOR_CURRENT_ACTIVE_OR_R2_SOURCE"
                break
            source_id,row,palette,new_r2=choice
            current=idx[source_id]
            eliminated=degree.get(source_id,0)
            old_len=len(events)
            next_events=[w for w in events
                         if source_id not in w["six_distinct_ORIGINAL_flag_IDs"]]
            if len(next_events)!=old_len-eliminated or row[
                "H_R3_all_51"][palette]!=0:
                raise AssertionError("zero-incidence original source deletion invalid")
            idx[source_id]=palette
            events=next_events
            r2=new_r2
            new_r3=len(events)
            if (new_r3>before[2] or r2>before[0] or
                not (new_r3<before[2] or r2<before[0])):
                raise AssertionError("source physical erasure did not strictly descend")
            # Source W34 risk and EVERY surviving physical signed event
            # are independently checked after EACH accepted edit.
            _current_source_physics(model,idx,r2,events,
                                    validate_each_event=True)
            accepted.append({
                "step":step,
                "real_ORIGINAL_source_ID":source_id,
                "old_source_GF5_palette":current,
                "new_source_GF5_palette":palette,
                "before_full_D2_D3_TRUE_R3":before,
                "after_full_D2_D3_TRUE_R3":(
                    r2,new_r3+421*r2,new_r3),
                "source_R3_current_incidence":eliminated,
                "H_i_new_exact_all_51_disjoint_GF5_incidence_zero":True,
                "new_R3_events_introduced":0,
                "old_events_deleted":eliminated,
                "candidate_source_IDs_checked_in_this_step":trials,
                "all_51_patterns_counted_on_full_other_12614424_triples":True,
                "complete_source_R2_90100_pairs_rechecked":True,
                "physical_28D_GF5_equations_survive":True,
            })
            if ((step+1)%checkpoint_every==0 or
                not events):
                evidence.append(_full_independent_checkpoint(
                    model,idx,r2,events,stage=f"after-{step+1}"))
                last_independent_step=step+1
            if not events and r2==0:
                status="FULL_ZERO_GF5_0to3_ORIGINAL_ASET"
                break
        if (not evidence or last_independent_step!=len(accepted)):
            evidence.append(_full_independent_checkpoint(
                model,idx,r2,events,stage="final"))
    if not events and r2==0:
        status="FULL_ZERO_GF5_0to3_ORIGINAL_ASET"
    final=(r2,len(events)+421*r2,len(events))
    if final[2]>initial[2] or final[0]>initial[0]:
        raise AssertionError("source no-new-event monotone potential increased")
    result={
        "schema":"mathlab.hyp105.real-W34-425-original-flags-zero-new-signed-R3-erasure-v1",
        "scheme":scheme,
        "scientific_parent_exact_SHA":PARENT_SHA,
        "original_W34_flag_count":425,
        "complete_source_GF5_coordinates":28,
        "legal_source_GF5_palettes":51,
        "source_maps_f_g_and_original_point_line_flags_unchanged":True,
        "full_425_original_source_palettes_before":old,
        "full_425_original_source_palettes_after":tuple(idx),
        "initial_full_D2_D3_TRUE_R3":initial,
        "final_independently_rechecked_D2_D3_TRUE_R3":final,
        "status":status,
        "accepted_source_cleaning_edits":tuple(accepted),
        "accepted_edit_count":len(accepted),
        "complete_independent_full_12704100_triple_checkpoints":tuple(evidence),
        "independent_full_GF5_audits_before_and_final":True,
        "each_step_full_source_R2_G5_pairs_and_surviving_signed_events_checked":True,
        "all_new_original_six_ID_signed_R3_events_proved_absent_each_step":True,
        "R2_nonincrease_hard_guardrail":True,
        "finite_monotone_integer_potential_strictly_decreased":True,
        "tested_single_original_source_H_i_zero_only_not_all_local_optima":True,
        "sufficient_source_cleaning_theorem_all_N_conditional_not_universal":True,
        "complete_425_original_source_zero_to_three_ASET":
            r2==0 and len(events)==0,
        "root_all_h_ASET_theorem_proved":False,
        "no_asymptotic_exponent_proved":True,
        "number_source_attempts_without_clean_pattern":rejected_no_zero,
    }
    return result


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--scheme",choices=("lex","reverse-line"),required=True)
    parser.add_argument("--max-steps",type=int,default=72)
    parser.add_argument("--checkpoint-every",type=int,default=8)
    parser.add_argument("--out",required=True)
    args=parser.parse_args()
    output=erasure_source_descent(
        args.scheme,max_steps=args.max_steps,
        checkpoint_every=args.checkpoint_every)
    dest=Path(args.out)
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(output,indent=2,sort_keys=True)+"\n",
                    encoding="utf-8")
    print(json.dumps({
        "scheme":output["scheme"],
        "status":output["status"],
        "accepted":output["accepted_edit_count"],
        "initial":output["initial_full_D2_D3_TRUE_R3"],
        "final":output["final_independently_rechecked_D2_D3_TRUE_R3"],
        "all_28D_physical_rechecks":len(output[
            "complete_independent_full_12704100_triple_checkpoints"]),
        "full_zero_SOURCE_ASET":output[
            "complete_425_original_source_zero_to_three_ASET"],
        "no_all_h_claim":output["root_all_h_ASET_theorem_proved"],
    },indent=2,sort_keys=True))


if __name__=="__main__":
    main()
