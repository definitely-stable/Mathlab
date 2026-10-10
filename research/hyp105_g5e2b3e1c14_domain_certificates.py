"""HYP-105 C14: seven-family sound partial-pair completion certificates.

Finite executable oracle: original W(3,2) (15 GQ points and 15 lines)
with COMPLETE pair-edge K6 physical alphabets on both halves. The
abstract per-witness min/sum inequality works for all incidence hosts,
but this implementation makes NO all-h Omega(s**6) claim.

A candidate original six-incidence set is only evaluated when ALL its
original LEFT points have assigned physical edges. For its touched
unpinned ORIGINAL right lines, enumerate every locally injective
choice of still unused physical edges. Take per-witness MIN over those
choices and sum the nonnegative minima. This lower is valid for EVERY
ONE common global completion; local injections must NOT be mistaken for
a simultaneous attainable global right permutation.
"""
from collections import Counter
from itertools import permutations
from math import factorial

from hyp105_b1_symplectic import symplectic_gq
from hyp105_g5e2b3e1a_fixed_leading import (
    PAIRS, selected_left_six, validated_small_model,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    classify_seven_prechecked, seven_census, R3_CERTIFIED_FLOORS,
)


def _pins(p, side):
    if not hasattr(p, "items"):
        raise ValueError(side+" must be original-index -> physical-index mapping")
    p=dict(p)
    if (any(type(i) is not int or type(j) is not int
            or not 0<=i<15 or not 0<=j<15 for i,j in p.items())
            or len(set(p.values()))!=len(p)):
        raise ValueError(side+" must be injective over exact original/physical IDs")
    return p


def _original_W32(model):
    left,right,edges,_=validated_small_model(model)
    _,points,lines,true_edges=symplectic_gq(1)
    if (len(points)!=15 or len(lines)!=15
            or set(edges)!=set(true_edges)):
        raise ValueError("C14 requires actual original W(3,2) incidences")
    if len(PAIRS)!=15 or tuple(PAIRS)!=tuple(sorted(PAIRS)):
        raise AssertionError("noncanonical K6 physical edge palette")
    return edges


def _filled_model(model,left_pins,right_pins):
    """Canonical full LEGAL completion only for enumerating left templates.

    A filler right map is NEVER used as a presumed universal optimum.
    """
    f=_pins(left_pins,"left pins")
    g=_pins(right_pins,"right pins")
    _original_W32(model)
    def fill(p):
        unused=(j for j in range(15) if j not in p.values())
        ids=dict(p)
        for i in range(15):
            if i not in ids:
                ids[i]=next(unused)
        return tuple(PAIRS[ids[i]] for i in range(15))
    left=fill(f)
    right=fill(g)
    out=dict(model)
    out["left_labels"]=left
    out["right_labels"]=right
    a=model["a"]
    out["supports"]=tuple(
        tuple(sorted(left[i]+tuple(a+x for x in right[j])))
        for i,j in model["incidences"])
    validated_small_model(out)
    return out


def seven_local_completion_lower(
        model,left_pins,right_pins,*,max_unassigned_right=3,
        max_motif_evaluations=500000):
    """Rigorous partial pair (f,g) lower for ALL common full completions.

    For each sixset E with ALL touched original LEFT points assigned:
      min_{injective local right labels on its unassigned lines}
          1[class(E) is one of seven accepted motifs],
    and independently min its already ACCEPTED GF5-floor numerator.
    Summing yields two valid lower bounds on EVERY actual completion.

    Individual minima may use DIFFERENT incompatible local injections,
    so this is explicitly an admissible relaxation, NOT a witness map.
    The left source template enumerator emits exactly 62,370 original
    6-incidence candidates for ANY full legal left labeling. Restrict
    to those whose ORIGINAL left points are already pinned; all these
    candidates are invariant under different filler completions.
    """
    f=_pins(left_pins,"left pins")
    g=_pins(right_pins,"right pins")
    if (type(max_unassigned_right) is not int
            or max_unassigned_right<0
            or type(max_motif_evaluations) is not int
            or max_motif_evaluations<1):
        raise ValueError("invalid exact lookahead limits")
    if 15-len(g)>max_unassigned_right:
        raise ValueError("unassigned right dimension beyond certified lookahead")
    full=_filled_model(model,f,g)
    edges=full["incidences"]
    left=full["left_labels"]
    right=full["right_labels"]
    pinned_left=set(f)
    pinned_right=set(g)
    free_right=tuple(j for j in range(15) if j not in g.values())
    considered=0
    excluded=0
    evals=0
    frozen=0
    class_floor=Counter()
    S_floor=0
    risk_floor=0
    locally_inevitable=0
    for ids,_left_kind in selected_left_six(full):
        touched_left={edges[e][0] for e in ids}
        if not touched_left<=pinned_left:
            excluded+=1
            continue
        considered+=1
        missing=tuple(sorted({edges[e][1] for e in ids}-pinned_right))
        assert len(missing)<=len(free_right)
        cls_seen=set()
        best_s=1
        best_risk=None
        options=0
        for labels in permutations(free_right,len(missing)):
            options+=1
            evals+=1
            if evals>max_motif_evaluations:
                raise ValueError("exact per-motif completion budget exceeded; no certificate")
            local=list(right)
            for src_idx,label_idx in zip(missing,labels):
                local[src_idx]=PAIRS[label_idx]
            tag=classify_seven_prechecked(ids,left,tuple(local),edges)
            cls_seen.add(tag)
            positive=int(tag is not None)
            risk=R3_CERTIFIED_FLOORS[tag] if tag is not None else 0
            best_s=min(best_s,positive)
            best_risk=risk if best_risk is None else min(best_risk,risk)
        if not options or best_risk is None:
            raise AssertionError("all local injections unexpectedly empty")
        if best_s:
            locally_inevitable+=1
        if not missing and best_s:
            frozen+=1
        S_floor+=best_s
        risk_floor+=best_risk
        if len(cls_seen)==1:
            tag=next(iter(cls_seen))
            if tag is not None:
                class_floor[tag]+=1
    if considered+excluded!=62370:
        raise AssertionError("left candidate enumeration incomplete/duplicate")
    if sum(class_floor.values())>S_floor or frozen>S_floor:
        raise AssertionError("inconsistent guaranteed structural class count")
    return {
        "scope":"GENUINE_W32_COMPLETE_K6_LEFT_AND_RIGHT_PHYSICAL",
        "pinned_original_left":len(f),
        "pinned_original_right":len(g),
        "remaining_original_left":15-len(f),
        "remaining_original_right":15-len(g),
        "left_physical_candidate_count":62370,
        "left_pinned_fully_decidable_candidates":considered,
        "left_incomplete_omitted_candidates":excluded,
        "exact_local_classifications":evals,
        "frozen_both_halves_positive_motifs":frozen,
        "locally_inevitable_seven_motifs":locally_inevitable,
        "certified_every_completion_S_seven_lower":S_floor,
        "certified_every_completion_GF5_necessary_numerator_lower":risk_floor,
        "per_class_guaranteed_count_lower":
            {t:class_floor[t] for t in R3_CERTIFIED_FLOORS},
        "all_actual_common_completion_maps_covered":True,
        "local_witness_assignments_need_not_be_jointly_compatible":True,
        "all_f_g_or_all_h_omega_s6_proved":False,
    }


def _completion_pairs(model,left_pins,right_pins,max_full_maps):
    f=_pins(left_pins,"left pins")
    g=_pins(right_pins,"right pins")
    _original_W32(model)
    left_unassigned=tuple(i for i in range(15) if i not in f)
    right_unassigned=tuple(i for i in range(15) if i not in g)
    remaining_left=tuple(i for i in range(15) if i not in f.values())
    remaining_right=tuple(i for i in range(15) if i not in g.values())
    N=factorial(len(left_unassigned))*factorial(len(right_unassigned))
    if (type(max_full_maps) is not int or max_full_maps<1 or N>max_full_maps):
        raise ValueError("full completion oracle budget exceeded")
    for left_labels in permutations(remaining_left):
        fnew={**f,**dict(zip(left_unassigned,left_labels))}
        for right_labels in permutations(remaining_right):
            gnew={**g,**dict(zip(right_unassigned,right_labels))}
            yield fnew,gnew


def independent_exact_completion_audit(
        model,left_pins,right_pins,*,max_full_maps=100):
    """Independent full seven_census on EVERY bounded true f,g completion."""
    histogram=Counter()
    best=None
    tried=0
    for f,g in _completion_pairs(model,left_pins,right_pins,max_full_maps):
        full=_filled_model(model,f,g)
        result=seven_census(full,independent_checks=False)
        score=(result["S_seven"],result["GF5_seven_lower_numerator"])
        histogram[score]+=1
        tried+=1
        if best is None or score<best[0]:
            best=(score,tuple(f[i] for i in range(15)),
                  tuple(g[i] for i in range(15)))
    if not tried:
        raise AssertionError("finite original W32 completion box empty")
    return {
        "complete_joint_maps_checked":tried,
        "true_minimum_S_seven_in_box":min(x[0] for x in histogram),
        "true_minimum_GF5_floor_numerator_in_box":min(x[1] for x in histogram),
        "S_and_GF5_joint_score_histogram":
            tuple(sorted((S,risk,n) for (S,risk),n in histogram.items())),
        "lexicographically_best_map_S_then_GF5":best,
        "NOT_global_all_f_g_W32_minimum":True,
    }


def bounded_exact_joint_branch_search(
        model,left_pins,right_pins,*,max_full_maps=100,
        max_nodes=300,max_motif_evaluations=500000,
        objective="S_seven"):
    """Sound joint prefix BnB; actual full-map oracle at every leaf.

    Existing upper incumbent is the exact full census of an explicit
    canonical legal map. At each node a bound >= incumbent may prune
    WITHOUT excluding a strictly better solution. Equality is safe
    because an incumbent achieving it already exists.

    This is a finite bounded box search, NOT a general all-W32 optimizer.
    """
    if objective not in ("S_seven","GF5_floor_numerator"):
        raise ValueError("unsupported exact branch objective")
    f=_pins(left_pins,"left pins")
    g=_pins(right_pins,"right pins")
    remaining=(15-len(f),15-len(g))
    N=factorial(remaining[0])*factorial(remaining[1])
    if type(max_full_maps) is not int or max_full_maps<1 or N>max_full_maps:
        raise ValueError("finite branch completion box beyond budget")
    if type(max_nodes) is not int or max_nodes<1:
        raise ValueError("max_nodes must be a positive exact hard cap")
    full=_filled_model(model,f,g)
    init=seven_census(full,independent_checks=False)
    attr="S_seven" if objective=="S_seven" else "GF5_seven_lower_numerator"
    bound_attr=("certified_every_completion_S_seven_lower" if objective=="S_seven"
                else "certified_every_completion_GF5_necessary_numerator_lower")
    best=init[attr]
    best_witness=(
        tuple(PAIRS.index(e) for e in full["left_labels"]),
        tuple(PAIRS.index(e) for e in full["right_labels"]))
    counts=Counter()
    trace=[]
    def visit(fp,gp):
        nonlocal best,best_witness
        counts["nodes"]+=1
        if counts["nodes"]>max_nodes:
            raise ValueError("tree node budget exceeded; no exact search result")
        if len(fp)==len(gp)==15:
            counts["leaves"]+=1
            candidate=_filled_model(model,fp,gp)
            census=seven_census(candidate,independent_checks=False)
            value=census[attr]
            if value<best:
                best=value
                best_witness=(
                    tuple(fp[i] for i in range(15)),
                    tuple(gp[i] for i in range(15)))
            return
        b=seven_local_completion_lower(
            model,fp,gp,max_motif_evaluations=max_motif_evaluations)
        lower=b[bound_attr]
        trace.append((len(fp),len(gp),lower,best))
        if lower>=best:
            counts["pruned_subtrees"]+=1
            return
        # Complete the LEFT physical map before assigning more right
        # labels, so candidate template eligibility grows monotonically.
        if len(fp)<15:
            v=min(set(range(15))-set(fp))
            for physical in range(15):
                if physical not in fp.values():
                    visit({**fp,v:physical},gp)
        else:
            v=min(set(range(15))-set(gp))
            for physical in range(15):
                if physical not in gp.values():
                    visit(fp,{**gp,v:physical})
    visit(f,g)
    return {
        "objective":objective,
        "exact_minimum_within_fixed_joint_completion_box":best,
        "best_complete_original_left_and_right_physical_index_maps":
            best_witness,
        "nodes_visited":counts["nodes"],
        "leaves_explicitly_evaluated":counts["leaves"],
        "strictly_sound_pruned_subtrees":counts["pruned_subtrees"],
        "original_box_full_completion_count":N,
        "partial_lower_traces":tuple(trace),
        "incomplete_or_early_budget_result":False,
        "all_f_g_global_optimum_proved":False,
    }


def genuine_W32_C14_report():
    """Actual 12+12 pinned W32 joint box; independently certify against 36 maps."""
    from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
    m=pair_labeled_symplectic(1,"reverse-line")
    left={i:PAIRS.index(m["left_labels"][i]) for i in range(12)}
    right={i:PAIRS.index(m["right_labels"][i]) for i in range(12)}
    b=seven_local_completion_lower(m,left,right)
    audit=independent_exact_completion_audit(
        m,left,right,max_full_maps=36)
    search=bounded_exact_joint_branch_search(
        m,left,right,max_full_maps=36,max_nodes=200)
    if not (b["certified_every_completion_S_seven_lower"]
            <=audit["true_minimum_S_seven_in_box"]
            ==search["exact_minimum_within_fixed_joint_completion_box"]):
        raise AssertionError("joint W32 C14 bound/exact solver independently disagrees")
    if b["certified_every_completion_GF5_necessary_numerator_lower"]>audit[
            "true_minimum_GF5_floor_numerator_in_box"]:
        raise AssertionError("necessary GF5 numerator conditional bound invalid")
    return {
        "true_original_geometry":"W(3,2) symplectic",
        "fixed_left_original_points":12,
        "fixed_right_original_lines":12,
        "all_true_full_joint_mapping_pairs_in_box":36,
        "locally_inevitable_7_motifs_lower":
            b["certified_every_completion_S_seven_lower"],
        "frozen_both_halves_7_motifs_lower":
            b["frozen_both_halves_positive_motifs"],
        "locally_inevitable_GF5_numerator_lower":
            b["certified_every_completion_GF5_necessary_numerator_lower"],
        "independent_true_box_S_min":
            audit["true_minimum_S_seven_in_box"],
        "independent_true_box_GF5_floor_numerator_min":
            audit["true_minimum_GF5_floor_numerator_in_box"],
        "branch_exact_same_S_min":
            search["exact_minimum_within_fixed_joint_completion_box"],
        "branch_nodes_visited":search["nodes_visited"],
        "branch_leaves":search["leaves_explicitly_evaluated"],
        "branch_pruned_subtrees":search["strictly_sound_pruned_subtrees"],
        "not_global_W32_or_all_h_result":True,
    }


if __name__=="__main__":
    import json
    print(json.dumps(genuine_W32_C14_report(),indent=2,sort_keys=True))
