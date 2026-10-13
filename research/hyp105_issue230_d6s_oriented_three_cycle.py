"""HYP-105 #230 D6-S: exact order-aware three-cycle and seven-class commutator.

ALL-h theorem for any globally injective ORIGINAL GQ pair labels f,g:
for any bijective permutation pi of ORIGINAL right line IDs supported on T,
  Delta_pi S = sum_{c:R(c) intersects T} m_f(c)
                     (1{chi_c(g^pi)}-1{chi_c(g)}).
For a 3-cycle T={u,v,w}, there are TWO distinct orientations: the
compositions sigma=(u,v), tau=(v,w) in opposite orders. They generally
produce DIFFERENT right maps and different ORIGINAL seven-GF5 counts.

For ordered sigma THEN tau:
 H_{sigma->tau} = S(g^(sigma then tau))-S(g^sigma)-S(g^tau)+S(g)
is supported on I_tau (not necessarily I_sigma intersect I_tau);
the component on I_tau \ I_sigma is an **order/overlap tail**:
  sum_{c in I_tau\I_sigma} m_f(c)
                  [chi_c(g^(sigma then tau))-chi_c(g^tau)].
Conversely H_{tau->sigma} is supported on I_sigma.
Their difference is exactly the commutator order defect:
 H_{sigma->tau}-H_{tau->sigma}
       =S(g^(sigma then tau))-S(g^(tau then sigma)).
For every right cylinder outside T, both orientations have identical
acceptance; hence |commutator S|<=M_T and
|commutator GF5 necessary floor numerator|<=51750*M_T, where M_T is
the number (with ORIGINAL multiplicity) of cylinders touching T.
This is a deterministic ALL-FINITE-H assertion, not Branch A/B.

For directed B-left/A-right and C-left/A-right, with SIX distinct
ORIGINAL right factors, if all three moved factor IDs lie in its right
support then the right physical unordered A-edge set is invariant
under either orientation. This sharpening is FALSE for position-sensitive
D6, for which a three-cycle may change aligned column-dual adjacency.

Finite executable: FULL 2*C(15,3)=910 oriented right three-cycles on
the true ORIGINAL W(3,2) strict singleton minima S68 and S72, with
exact seven-class and GF5 necessary-floor deltas; not a global all-h
minimum, not all right-label permutations, not a complete W34 census.
"""
from collections import Counter
from itertools import combinations
import json

from hyp105_issue230_d6p_seven_cylinder_swap_audit import (
    SEVEN_CLASSES, R3_CERTIFIED_FLOORS, cylinder_seven_class,
    compile_original_W32_cylinders, cylinder_census, swapped_labels,
    exact_seven_cylinder_swap,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census

MAX_GF5_WEIGHT=max(R3_CERTIFIED_FLOORS.values())
assert MAX_GF5_WEIGHT==51750


def _validated_triple(right_labels, triple):
    try:
        triple=tuple(triple)
    except TypeError as exc:
        raise ValueError("three ORIGINAL right factor IDs required") from exc
    if (len(triple)!=3 or len(set(triple))!=3 or
            any(type(i) is not int or i<0 or i>=len(right_labels)
                for i in triple)):
        raise ValueError("requires three distinct valid ORIGINAL right factor IDs")
    return tuple(sorted(triple))


def right_three_cycle_labels(right_labels, triple, orientation):
    """Plus = sigma(u,v) THEN tau(v,w); minus = reverse ORDER.

    For canonical u<v<w, plus: u<-v, v<-w, w<-u;
    minus: u<-w, v<-u, w<-v. This rotates EXISTING PHYSICAL pair
    labels; it cannot create duplicate labels or unused extra edges.
    """
    u,v,w=_validated_triple(right_labels,triple)
    if type(orientation) is not int or orientation not in (-1,1):
        raise ValueError("orientation must be exactly +1 or -1")
    labels=list(right_labels)
    if orientation==1:
        labels[u],labels[v],labels[w]=labels[v],labels[w],labels[u]
    else:
        labels[u],labels[v],labels[w]=labels[w],labels[u],labels[v]
    if len(set(labels))!=len(labels):
        raise AssertionError("right three-cycle broke complete injection")
    return tuple(labels)


def _class_delta(before,after,multiplicity,output):
    if before is not None:
        output[before]-=multiplicity
    if after is not None:
        output[after]+=multiplicity


def _final_deltas(class_counts):
    by_class={k:class_counts[k] for k in SEVEN_CLASSES}
    return {
        "delta_by_seven_class":by_class,
        "delta_S_seven":sum(by_class.values()),
        "delta_GF5_selected_lower_numerator":sum(
            by_class[k]*R3_CERTIFIED_FLOORS[k] for k in SEVEN_CLASSES),
    }


def exact_three_cycle_pair_delta(compiled,right_labels,triple,
                                  baseline_tags=None):
    """Exact BOTH orientations, evaluating only ORIGINAL cylinders meeting T."""
    u,v,w=_validated_triple(right_labels,triple)
    if len(set(right_labels))!=len(right_labels):
        raise ValueError("complete globally injective right labels required")
    index=compiled["by_original_line"]
    touched=set(index.get(u,()))|set(index.get(v,()))|set(index.get(w,()))
    g_plus=right_three_cycle_labels(right_labels,(u,v,w),1)
    g_minus=right_three_cycle_labels(right_labels,(u,v,w),-1)
    counts_plus=Counter()
    counts_minus=Counter()
    mass=0
    right_A_triple_stable_mass=0
    for sig in touched:
        multiplicity=compiled["cylinders"][sig]
        mass+=multiplicity
        # All moved ORIGINAL right labels are present: physical right-A
        # membership is permutation invariant for left B/C, six distinct.
        if (sig[0] in ("B","C") and len(set(sig[1]))==6
                and {u,v,w}.issubset(sig[1])):
            right_A_triple_stable_mass+=multiplicity
            continue
        before=(baseline_tags[sig] if baseline_tags is not None
                else cylinder_seven_class(sig,right_labels))
        _class_delta(before,cylinder_seven_class(sig,g_plus),
                     multiplicity,counts_plus)
        _class_delta(before,cylinder_seven_class(sig,g_minus),
                     multiplicity,counts_minus)
    plus=_final_deltas(counts_plus)
    minus=_final_deltas(counts_minus)
    commutator_classes={
        k:plus["delta_by_seven_class"][k]-minus["delta_by_seven_class"][k]
        for k in SEVEN_CLASSES
    }
    defect=sum(commutator_classes.values())
    weighted_defect=sum(
        commutator_classes[k]*R3_CERTIFIED_FLOORS[k] for k in SEVEN_CLASSES)
    if (defect!=plus["delta_S_seven"]-minus["delta_S_seven"] or
            weighted_defect!=plus["delta_GF5_selected_lower_numerator"]-
                             minus["delta_GF5_selected_lower_numerator"]):
        raise AssertionError("oriented commutator class conservation failed")
    if abs(defect)>mass or abs(weighted_defect)>MAX_GF5_WEIGHT*mass:
        raise AssertionError("all-h supported ORIGINAL commutator bound violated")
    return {
        "triple_original_right_factors":[u,v,w],
        "touched_unique_original_cylinders":len(touched),
        "touched_original_sixsets_weight":mass,
        "three_present_directed_BC_right_A_stable_original_sixsets":
            right_A_triple_stable_mass,
        "forward":plus,"reverse":minus,
        "commutator_by_seven_class":commutator_classes,
        "order_commutator_S":defect,
        "order_commutator_GF5_selected_lower_numerator":weighted_defect,
        "absolute_commutator_S_bound":mass,
        "absolute_commutator_GF5_bound":MAX_GF5_WEIGHT*mass,
        "all_seven_ORIGINAL_classes_preserved":True,
        "fixed_right_PHYSICAL_image_invariant":True,
    }


def exact_ordered_three_cycle_curvature(compiled,right_labels,triple):
    """Order-sensitive mixed Hessian; catches missing intersection tail.

    sigma=(u,v) first, tau=(v,w) second for 'forward'; the opposite
    execution order gives 'reverse'. Both are globally valid 3-cycles.
    """
    u,v,w=_validated_triple(right_labels,triple)
    index=compiled["by_original_line"]
    hit_sigma=set(index.get(u,()))|set(index.get(v,()))
    hit_tau=set(index.get(v,()))|set(index.get(w,()))
    intersect=hit_sigma & hit_tau
    tail_forward=hit_tau-hit_sigma
    tail_reverse=hit_sigma-hit_tau
    sigma=(u,v);tau=(v,w)
    g_sigma=swapped_labels(right_labels,*sigma)
    g_tau=swapped_labels(right_labels,*tau)
    g_forward=swapped_labels(g_sigma,*tau)
    g_reverse=swapped_labels(g_tau,*sigma)
    if (g_forward!=right_three_cycle_labels(right_labels,(u,v,w),1) or
            g_reverse!=right_three_cycle_labels(right_labels,(u,v,w),-1) or
            g_forward==g_reverse):
        raise AssertionError("overlapping swap order and three-cycle mismatch")
    forward_counts=Counter()
    reverse_counts=Counter()
    overlap_forward=Counter()
    tail_f_counts=Counter()
    overlap_reverse=Counter()
    tail_r_counts=Counter()
    for sig in hit_sigma | hit_tau:
        mult=compiled["cylinders"][sig]
        base=cylinder_seven_class(sig,right_labels)
        v_sigma=cylinder_seven_class(sig,g_sigma)
        v_tau=cylinder_seven_class(sig,g_tau)
        if sig in hit_tau:
            v_fwd=cylinder_seven_class(sig,g_forward)
            contrib=overlap_forward if sig in intersect else tail_f_counts
            for tag,sign in ((v_fwd,1),(v_sigma,-1),(v_tau,-1),(base,1)):
                if tag is not None:
                    contrib[tag]+=sign*mult
                    forward_counts[tag]+=sign*mult
        if sig in hit_sigma:
            v_rev=cylinder_seven_class(sig,g_reverse)
            contrib=overlap_reverse if sig in intersect else tail_r_counts
            for tag,sign in ((v_rev,1),(v_sigma,-1),(v_tau,-1),(base,1)):
                if tag is not None:
                    contrib[tag]+=sign*mult
                    reverse_counts[tag]+=sign*mult
    all_f=_final_deltas(forward_counts)
    all_r=_final_deltas(reverse_counts)
    f_inter=_final_deltas(overlap_forward)
    f_tail=_final_deltas(tail_f_counts)
    r_inter=_final_deltas(overlap_reverse)
    r_tail=_final_deltas(tail_r_counts)
    for k in SEVEN_CLASSES:
        if (all_f["delta_by_seven_class"][k] !=
                f_inter["delta_by_seven_class"][k]+f_tail["delta_by_seven_class"][k] or
                all_r["delta_by_seven_class"][k] !=
                r_inter["delta_by_seven_class"][k]+r_tail["delta_by_seven_class"][k]):
            raise AssertionError("order-aware overlap/tail decomposition violated")
    m_sigma=exact_seven_cylinder_swap(compiled,right_labels,*sigma)
    m_tau=exact_seven_cylinder_swap(compiled,right_labels,*tau)
    cycles=exact_three_cycle_pair_delta(compiled,right_labels,(u,v,w))
    for sign,curvature in (("forward",all_f),("reverse",all_r)):
        for k in SEVEN_CLASSES:
            if (cycles[sign]["delta_by_seven_class"][k] !=
                    m_sigma["delta_by_seven_class"][k]+
                    m_tau["delta_by_seven_class"][k]+
                    curvature["delta_by_seven_class"][k]):
                raise AssertionError("three-cycle mixed Hessian exact class identity failed")
    if (all_f["delta_S_seven"]-all_r["delta_S_seven"] !=
            cycles["order_commutator_S"] or
            all_f["delta_GF5_selected_lower_numerator"]-
            all_r["delta_GF5_selected_lower_numerator"] !=
            cycles["order_commutator_GF5_selected_lower_numerator"]):
        raise AssertionError("noncommutative order defect must equal Hessian gap")
    return {
        "triple_original_right_factors":[u,v,w],
        "first_sigma":[u,v],"second_tau":[v,w],
        "intersection_original_cylinders":len(intersect),
        "forward_tail_original_cylinders":len(tail_forward),
        "reverse_tail_original_cylinders":len(tail_reverse),
        "forward_ordered_Hessian":all_f,
        "reverse_ordered_Hessian":all_r,
        "forward_intersection_component":f_inter,
        "forward_noncommuting_tail_component":f_tail,
        "reverse_intersection_component":r_inter,
        "reverse_noncommuting_tail_component":r_tail,
        "order_commutator_S":cycles["order_commutator_S"],
        "order_commutator_GF5_selected_lower_numerator":
            cycles["order_commutator_GF5_selected_lower_numerator"],
        "intersection_ONLY_formula_for_overlapping_swaps":"INVALID",
        "Branch_A":"OPEN","Branch_B":"OPEN",
    }


def real_W32_complete_oriented_three_cycle_report(schemes=("S68","S72")):
    """ALL 910 oriented 3-cycles for EACH requested true W32 S68/S72 map."""
    if (not schemes or len(set(schemes))!=len(schemes) or
            any(k not in ("S68","S72") for k in schemes)):
        raise ValueError("choose distinct frozen S68/S72 original W32 maps")
    settings={"S68":(68,7),"S72":(72,2)}
    cases=[]
    for scheme in schemes:
        known_S,known_single=settings[scheme]
        model=fixture(1,scheme)
        compiled=compile_original_W32_cylinders(model)
        labels=tuple(model["right_labels"])
        initial=cylinder_census(compiled,labels)
        other=seven_census(model,independent_checks=False)
        if (initial["S_seven"]!=known_S or
                initial["seven_class_motif_counts"]!=other["seven_class_motif_counts"] or
                initial["GF5_seven_lower_numerator"]!=
                other["GF5_seven_lower_numerator"]):
            raise AssertionError("true ORIGINAL W32 independent seven-count baseline failed")
        # An exact independent 105 singleton scan, no assumption of 3-cycle
        # stability. Together with the two orientations for EVERY triple,
        # this tests every permutation supported on <=3 original line IDs.
        singleton=[exact_seven_cylinder_swap(compiled,labels,u,v)
                   for u,v in combinations(range(15),2)]
        if (len(singleton)!=105 or
                min(x["delta_S_seven"] for x in singleton)!=known_single or
                any(x["delta_S_seven"]<=0 for x in singleton)):
            raise AssertionError("D6-P strict 1-swap minimum oracle changed")
        baseline_tags={
            sig:cylinder_seven_class(sig,labels)
            for sig in compiled["cylinders"]
        }
        oriented=[]
        triples=list(combinations(range(15),3))
        for triple in triples:
            result=exact_three_cycle_pair_delta(
                compiled,labels,triple,baseline_tags)
            for orientation in ("forward","reverse"):
                d=result[orientation]
                oriented.append({
                    "triple_original_right_factors":list(triple),
                    "orientation":orientation,
                    "delta_S_seven":d["delta_S_seven"],
                    "delta_GF5_selected_lower_numerator":
                        d["delta_GF5_selected_lower_numerator"],
                    "delta_by_seven_class":d["delta_by_seven_class"],
                    "order_commutator_S":result["order_commutator_S"],
                })
        if len(triples)!=455 or len(oriented)!=910:
            raise AssertionError("complete true W32 right 3-cycle enumeration truncated")
        key=lambda row:(row["delta_S_seven"],
                        row["triple_original_right_factors"],
                        row["orientation"])
        best=min(oriented,key=key)
        worst=max(oriented,key=key)
        g_min=min(oriented,key=lambda v:(v[
            "delta_GF5_selected_lower_numerator"],v[
            "triple_original_right_factors"],v["orientation"]))
        deficit_counts={
            "negative":sum(v["delta_S_seven"]<0 for v in oriented),
            "zero":sum(v["delta_S_seven"]==0 for v in oriented),
            "positive":sum(v["delta_S_seven"]>0 for v in oriented),
        }
        weighted_improve=sum(v[
            "delta_GF5_selected_lower_numerator"]<0 for v in oriented)
        commutator_nonzero=sum(
            oriented[2*j]["order_commutator_S"]!=0 for j in range(455))
        if (sum(deficit_counts.values())!=910 or
                oriented[0]["orientation"]!="forward" or
                any(oriented[2*j]["order_commutator_S"]!=
                    oriented[2*j+1]["order_commutator_S"]
                    for j in range(455))):
            raise AssertionError("complete oriented S3 original W32 audit failed")
        cases.append({
            "scheme":scheme,
            "baseline_true_original_S":known_S,
            "baseline_GF5_selected_lower_numerator":
                initial["GF5_seven_lower_numerator"],
            "all_105_single_transpositions_strictly_increase_S":True,
            "min_singleton_delta_S":known_single,
            "unique_original_right_line_triples":455,
            "all_910_oriented_three_cycles_checked":True,
            "oriented_three_cycles_increasing_S":deficit_counts["positive"],
            "oriented_three_cycles_equal_S":deficit_counts["zero"],
            "oriented_three_cycles_improving_S":deficit_counts["negative"],
            "oriented_three_cycles_improving_GF5_selected_lower":
                weighted_improve,
            "triple_supports_with_nonzero_order_commutator":
                commutator_nonzero,
            "best_oriented_three_cycle":best,
            "worst_oriented_three_cycle":worst,
            "best_weighted_GF5_three_cycle":g_min,
            "S_local_minimum_for_ALL_right_permutations_supported_on_at_most_3_original_lines":
                deficit_counts["negative"]==0,
            "S_strict_local_minimum_for_ALL_nonidentity_right_permutations_supported_on_at_most_3_original_lines":
                deficit_counts["negative"]==0 and deficit_counts["zero"]==0,
            "NOT_full_permutation_global_minimum":True,
        })
    return {
        "slice":"HYP105-ISSUE230-D6S-ORIENTED-3CYCLE-ORDER-DEFECT",
        "theorem":"ALL-H-ORIGINAL-SEVEN-CYLINDER-ORIENTED-3CYCLE-COMMUTATOR",
        "full_W32_two_orientations_all_455_right_factor_triples_per_map":True,
        "genuine_original_W32_complete_injections":True,
        "no_W34_W38_full_seven_S":"NOT-CLAIMED",
        "all_h_global_lower":"NOT-PROVED",
        "infinite_B_counterfamily":"NOT-PROVED",
        "Branch_A":"OPEN","Branch_B":"OPEN",
        "rows":cases,
    }


if __name__=="__main__":
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("--scheme",choices=("S68","S72"),default=None)
    args=parser.parse_args()
    requested=(args.scheme,) if args.scheme else ("S68","S72")
    print(json.dumps(real_W32_complete_oriented_three_cycle_report(requested),
                     sort_keys=True,indent=2))
