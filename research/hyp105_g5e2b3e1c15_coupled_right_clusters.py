"""HYP-105 C15: coupled right-witness clusters for ONE common residual g.

This is a finite W(3,2) exact hosted oracle, not an all-h seven-motif
lower. Original left-pinned witnesses partition by touched unpinned
ORIGINAL right-line support. Cluster minimization uses ONE common
physical injection within each cluster; global eligible-witness bound
uses ONE common right bijection for ALL left-pinned candidates.
"""
from collections import Counter
from itertools import permutations
from math import factorial

from hyp105_g5e2b3e1a_fixed_leading import PAIRS,selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import (
    classify_seven_prechecked,R3_CERTIFIED_FLOORS,seven_census,
)
from hyp105_g5e2b3e1c14_domain_certificates import (
    _pins,_filled_model,_original_W32,independent_exact_completion_audit,
    seven_local_completion_lower,
)


def coupled_right_witness_certificate(
        model,left_pins,right_pins,*,max_unassigned_right=3,
        max_motif_evaluations=500000):
    """Exact hierarchy: independent-C14 <= right-signature <= shared-right.

    Fix a TRUE partial original-left/right GQ-to-K6 injection. Consider
    exactly the ORIGINAL six-incidence witnesses whose original left
    endpoints are ALL pinned. All other (possibly positive) sixsets
    are omitted, yielding a legitimate nonnegative universal lower
    on EACH true full joint descendant (f,g).

    Let P be ALL complete bijections of currently unpinned ORIGINAL
    right lines to currently unused PHYSICAL right pair edges.
    For every eligible sixset J and EVERY common rho in P, evaluate
    accepted class chi_J(rho) and GF5 necessary floor w_J(rho).

    C14 independent:  SUM_J min_P chi_J.
    Cluster by support M_J of ORIGINAL right lines in J that are
    unpinned: SUM_M min_P SUM_(J:M_J=M) chi_J.
    Fully shared:      min_P SUM_J chi_J.

    Identical chain for nonnegative classwise GF5 floor numerators.
    The signature clusters partition the witnesses (NO double-count).
    A local injection on M_J always extends to a full rho in P,
    making the first level EXACTLY C14 for these eligible sixsets.

    Subsequence monotonicity under left/right partial-map extension:
    eligible witness set only expands, and full right assignments
    become restricted; all witness costs nonnegative. For any fixed
    legal descendant the true common g is one rho from current P.
    """
    f=_pins(left_pins,"original left pins")
    g=_pins(right_pins,"original right pins")
    _original_W32(model)
    if (type(max_unassigned_right) is not int or max_unassigned_right<0
            or type(max_motif_evaluations) is not int
            or max_motif_evaluations<1):
        raise ValueError("invalid exhaustive right coupling budgets")
    free_orig=tuple(i for i in range(15) if i not in g)
    free_phys=tuple(i for i in range(15) if i not in g.values())
    k=len(free_orig)
    if k>max_unassigned_right:
        raise ValueError("residual original-right dimension exceeds exact cap")
    base=_filled_model(model,f,g)
    inc=base["incidences"]
    left=base["left_labels"]
    pinned_left=set(f)
    original_right=base["right_labels"]
    completions=[]
    for physical_tail in permutations(free_phys):
        r=list(original_right)
        for i,j in zip(free_orig,physical_tail):
            r[i]=PAIRS[j]
        completions.append(tuple(r))
    if len(completions)!=factorial(k):
        raise AssertionError("missing or duplicate full common right completion")
    spectrum={}
    singletonS=singletonRisk=0
    eligible=0
    excluded=0
    evaluations=0
    frozen=0
    for six,_ in selected_left_six(base):
        if any(inc[e][0] not in pinned_left for e in six):
            excluded+=1
            continue
        eligible+=1
        if evaluations+len(completions)>max_motif_evaluations:
            raise ValueError("incomplete local motif evaluation budget")
        missing=tuple(sorted({inc[e][1] for e in six if inc[e][1] not in g}))
        pair=spectrum.get(missing)
        if pair is None:
            pair=([0]*len(completions),[0]*len(completions),0)
            spectrum[missing]=pair
        values=[]
        weights=[]
        for j,right in enumerate(completions):
            tag=classify_seven_prechecked(six,left,right,inc)
            positive=int(tag is not None)
            w=R3_CERTIFIED_FLOORS[tag] if tag is not None else 0
            pair[0][j]+=positive
            pair[1][j]+=w
            values.append(positive)
            weights.append(w)
        evaluations+=len(completions)
        singletonS+=min(values)
        singletonRisk+=min(weights)
        frozen+=int(not missing and bool(values[0]))
        spectrum[missing]=(pair[0],pair[1],pair[2]+1)
    if eligible+excluded!=62370:
        raise AssertionError("original left A/B/C candidate count changed")
    rows=[]
    clusteredS=clusteredRisk=0
    allS=[0]*len(completions)
    allRisk=[0]*len(completions)
    for signature,(sv,rv,count) in sorted(spectrum.items()):
        lowS=min(sv)
        lowRisk=min(rv)
        clusteredS+=lowS
        clusteredRisk+=lowRisk
        for j in range(len(completions)):
            allS[j]+=sv[j]
            allRisk[j]+=rv[j]
        rows.append({
            "original_unpinned_right_line_signature":signature,
            "original_six_incidence_witnesses":count,
            "single_signature_common_S_lower":lowS,
            "single_signature_common_GF5_numerator_lower":lowRisk,
        })
    sharedS=min(allS)
    sharedRisk=min(allRisk)
    if not (0<=frozen<=singletonS<=clusteredS<=sharedS
            and 0<=singletonRisk<=clusteredRisk<=sharedRisk):
        raise AssertionError("invalid coupling monotone lower hierarchy")
    return {
        "scope":"ORIGINAL_W32_COMPLETE_PHYSICAL_K6_BOTH_HALVES",
        "pinned_left_original":len(f),
        "pinned_right_original":len(g),
        "unassigned_right_original":k,
        "actual_one_common_right_completions":len(completions),
        "all_original_left_source_candidates":62370,
        "eligible_all_left_pinned_candidates":eligible,
        "excluded_left_unpinned_candidates":excluded,
        "real_evaluated_witness_right_pairs":evaluations,
        "separately_inevitable_frozen_witnesses":frozen,
        "C14_independent_single_seven_lower":singletonS,
        "C15_support_cluster_seven_lower":clusteredS,
        "C15_one_shared_right_seven_lower":sharedS,
        "C14_independent_single_GF5_necessary_numerator_lower":singletonRisk,
        "C15_support_cluster_GF5_necessary_numerator_lower":clusteredRisk,
        "C15_one_shared_right_GF5_necessary_numerator_lower":sharedRisk,
        "right_signature_cluster_count":len(rows),
        "signature_cluster_certificates":tuple(rows),
        "whole_eligible_witness_counts_by_actual_common_right_map":tuple(allS),
        "whole_eligible_GF5_numerators_by_actual_common_right_map":tuple(allRisk),
        "one_full_right_permutation_used_per_sixset_census":True,
        "not_exact_all_f_g_or_all_h_universal_S_lower":True,
    }


def coupled_right_joint_branch_search(
        model,left_pins,right_pins,*,mode="shared",objective="S_seven",
        max_full_maps=100,max_nodes=300,max_motif_evaluations=500000):
    """Certified joint f,g exact finite box BnB with three nested lower modes.

    Uses the SAME deterministic C14 extension order and initial full
    right/left legal witness. For every mode one fixed objective and ONE
    shared actual global right map per complete leaf are checked by
    the independent accepted seven_census; node lower may use looser
    independent sixsets, compatible original-right-signature clusters,
    or all eligible motifs coupled to ONE common residual right map.
    """
    if mode not in ("single","cluster","shared"):
        raise ValueError("unsupported proved bound type")
    if objective not in ("S_seven","GF5_floor_numerator"):
        raise ValueError("unsupported finite exact motif objective")
    f=_pins(left_pins,"left pins")
    g=_pins(right_pins,"right pins")
    _original_W32(model)
    N=factorial(15-len(f))*factorial(15-len(g))
    if (type(max_full_maps) is not int or max_full_maps<1 or N>max_full_maps
            or type(max_nodes) is not int or max_nodes<1):
        raise ValueError("exact joint box/node budget exceeded")
    full=_filled_model(model,f,g)
    base=seven_census(full,independent_checks=False)
    target="S_seven" if objective=="S_seven" else "GF5_seven_lower_numerator"
    metric={
        ("single","S_seven"):"C14_independent_single_seven_lower",
        ("cluster","S_seven"):"C15_support_cluster_seven_lower",
        ("shared","S_seven"):"C15_one_shared_right_seven_lower",
        ("single","GF5_floor_numerator"):
            "C14_independent_single_GF5_necessary_numerator_lower",
        ("cluster","GF5_floor_numerator"):
            "C15_support_cluster_GF5_necessary_numerator_lower",
        ("shared","GF5_floor_numerator"):
            "C15_one_shared_right_GF5_necessary_numerator_lower",
    }[(mode,objective)]
    best=base[target]
    witness=(
        tuple(PAIRS.index(e) for e in full["left_labels"]),
        tuple(PAIRS.index(e) for e in full["right_labels"]))
    counts=Counter()
    trace=[]
    def walk(fp,gp):
        nonlocal best,witness
        counts["nodes"]+=1
        if counts["nodes"]>max_nodes:
            raise ValueError("tree node cap exceeded; do not certify partial result")
        if len(fp)==len(gp)==15:
            counts["leaves"]+=1
            actual=seven_census(_filled_model(model,fp,gp),
                                independent_checks=False)[target]
            if actual<best:
                best=actual
                witness=(tuple(fp[i] for i in range(15)),
                         tuple(gp[i] for i in range(15)))
            return
        cert=coupled_right_witness_certificate(
            model,fp,gp,max_motif_evaluations=max_motif_evaluations)
        lower=cert[metric]
        trace.append((len(fp),len(gp),lower,best))
        if lower>=best:
            counts["pruned"]+=1
            return
        if len(fp)<15:
            src=min(set(range(15))-set(fp))
            for physical in range(15):
                if physical not in fp.values():
                    walk({**fp,src:physical},gp)
        else:
            src=min(set(range(15))-set(gp))
            for physical in range(15):
                if physical not in gp.values():
                    walk(fp,{**gp,src:physical})
    walk(f,g)
    return {
        "mode":mode,"objective":objective,
        "exact_minimum_in_given_legal_joint_box":best,
        "best_explicit_full_original_left_and_right_maps":witness,
        "total_complete_legal_joint_maps_in_box":N,
        "visited_nodes":counts["nodes"],
        "exact_full_map_leaves_recounted":counts["leaves"],
        "sound_subtrees_pruned":counts["pruned"],
        "certified_partial_lower_trace":tuple(trace),
        "no_incomplete_budget_result":True,
        "not_entire_W32_f_g_or_all_h":True,
    }


def genuine_W32_C15_report():
    """3!²=36 original W32 legal joint maps; compare THREE proof levels."""
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    m=pair_labeled_symplectic(1,"reverse-line")
    f={i:PAIRS.index(m["left_labels"][i]) for i in range(12)}
    g={i:PAIRS.index(m["right_labels"][i]) for i in range(12)}
    baseline=seven_local_completion_lower(m,f,g)
    cert=coupled_right_witness_certificate(m,f,g)
    if (cert["C14_independent_single_seven_lower"]
            !=baseline["certified_every_completion_S_seven_lower"]
            or cert["C14_independent_single_GF5_necessary_numerator_lower"]
            !=baseline["certified_every_completion_GF5_necessary_numerator_lower"]):
        raise AssertionError("coupled source singleton marginal differs from C14")
    independent=independent_exact_completion_audit(
        m,f,g,max_full_maps=36)
    results={}
    for mode in ("single","cluster","shared"):
        search=coupled_right_joint_branch_search(
            m,f,g,mode=mode,max_full_maps=36,max_nodes=300)
        if search["exact_minimum_in_given_legal_joint_box"]!=independent[
                "true_minimum_S_seven_in_box"]:
            raise AssertionError("coupled seven right solver differs from independent enumeration")
        results[mode]={
            "nodes":search["visited_nodes"],
            "leaves":search["exact_full_map_leaves_recounted"],
            "pruned":search["sound_subtrees_pruned"],
        }
    if not (cert["C15_one_shared_right_seven_lower"]
            <=independent["true_minimum_S_seven_in_box"]
            and cert["C15_one_shared_right_GF5_necessary_numerator_lower"]
            <=independent["true_minimum_GF5_floor_numerator_in_box"]):
        raise AssertionError("root coupled local lower exceeds independent true minimum")
    # Frozen independent GitHub-hosted true W32 C15 benchmark.
    # These are finite comparison statistics, NOT all-f,g lower bounds.
    if (cert["eligible_all_left_pinned_candidates"]!=6723
            or cert["right_signature_cluster_count"]!=8
            or (
                cert["C14_independent_single_seven_lower"],
                cert["C15_support_cluster_seven_lower"],
                cert["C15_one_shared_right_seven_lower"]
            )!=(2,8,12)
            or (
                cert["C14_independent_single_GF5_necessary_numerator_lower"],
                cert["C15_support_cluster_GF5_necessary_numerator_lower"],
                cert["C15_one_shared_right_GF5_necessary_numerator_lower"]
            )!=(91200,370950,513393)
            or results!={"single":{"nodes":73,"leaves":3,"pruned":33},
                         "cluster":{"nodes":46,"leaves":3,"pruned":19},
                         "shared":{"nodes":34,"leaves":3,"pruned":12}}):
        raise AssertionError("verified W32 C15 three-mode baseline changed")
    return {
        "scope":"TRUE_ORIGINAL_W32_REVERSE_LINE_12_LEFT_12_RIGHT_PIN_BOX",
        "full_true_joint_mapping_pairs_in_box":36,
        "certified_root_C14_single_S":cert["C14_independent_single_seven_lower"],
        "certified_root_C15_signature_cluster_S":
            cert["C15_support_cluster_seven_lower"],
        "certified_root_C15_full_shared_right_S":
            cert["C15_one_shared_right_seven_lower"],
        "certified_root_C14_single_GF5":
            cert["C14_independent_single_GF5_necessary_numerator_lower"],
        "certified_root_C15_signature_cluster_GF5":
            cert["C15_support_cluster_GF5_necessary_numerator_lower"],
        "certified_root_C15_full_shared_GF5":
            cert["C15_one_shared_right_GF5_necessary_numerator_lower"],
        "left_eligible_original_six_incidence_candidates":
            cert["eligible_all_left_pinned_candidates"],
        "right_original_signature_clusters":cert["right_signature_cluster_count"],
        "full_right_shared_completions":cert["actual_one_common_right_completions"],
        "independent_exact_36_true_joint_S_min":
            independent["true_minimum_S_seven_in_box"],
        "independent_exact_36_true_GF5_floor_min":
            independent["true_minimum_GF5_floor_numerator_in_box"],
        "comparative_branch_and_bound":results,
        "no_all_f_g_or_all_h_lower_proved":True,
    }


if __name__=="__main__":
    import json
    print(json.dumps(genuine_W32_C15_report(),indent=2,sort_keys=True))
