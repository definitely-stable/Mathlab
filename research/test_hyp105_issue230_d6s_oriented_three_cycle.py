"""Independent D6-S tests of genuine ORIGINAL W32 oriented three-cycles.

External acceptance oracle: original seven_census scans each original
six-incidence subset, not the new right cylinder classifier. Synthetic
counterexample isolates genuinely noncommuting support-tail loss.
"""
from collections import Counter
from itertools import combinations
import unittest

from hyp105_issue230_d6s_oriented_three_cycle import (
    right_three_cycle_labels, exact_three_cycle_pair_delta,
    exact_ordered_three_cycle_curvature,
)
from hyp105_issue230_d6p_seven_cylinder_swap_audit import (
    compile_original_W32_cylinders, cylinder_census, cylinder_seven_class,
    SEVEN_CLASSES, R3_CERTIFIED_FLOORS, swapped_labels,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census


def original_full_recount(model, labels):
    newer=dict(model)
    newer["right_labels"]=labels
    return seven_census(newer,independent_checks=False)


def synthetic_overlap_tail_instance():
    # A single legal six-column B-left/A-right incidence-POSITION
    # cylinder with right ORIGINAL factors 2..7. sigma=(0,1) misses
    # the support, tau=(1,2) touches it. Ordered sigma-then-tau
    # changes physical image at ORIGINAL line 2 from g(1) to g(0).
    # g(0)=(0,1) completes a physical C6; g(1)=(0,2) does not.
    g=((0,1),(0,2),(1,3),(1,2),(2,3),(3,4),(4,5),(0,5))
    signature=("B",(2,3,4,5,6,7),(),(0,1))
    compiled={
        "cylinders":Counter({signature:1}),
        "by_original_line":{
            i:([signature] if 2<=i<=7 else []) for i in range(8)},
        "original_lines":8,
    }
    return compiled,g,signature


class OrientedThreeCycleTests(unittest.TestCase):
    def test_true_original_W32_independent_global_three_cycle_GF5_recounts(self):
        probes={
            "lex":((0,1,2),(1,7,9)),
            "S68":((0,1,2),(8,9,12),(3,7,10)),
            "S72":((0,1,2),(1,7,14),(3,7,10)),
        }
        for scheme,triples in probes.items():
            model=fixture(1,scheme)
            compiled=compile_original_W32_cylinders(model)
            source=original_full_recount(model,model["right_labels"])
            base=cylinder_census(compiled,model["right_labels"])
            self.assertEqual(base["seven_class_motif_counts"],
                             source["seven_class_motif_counts"])
            for t in triples:
                with self.subTest(scheme=scheme,triple=t):
                    result=exact_three_cycle_pair_delta(
                        compiled,model["right_labels"],t)
                    recount={}
                    for sign,flag in (("forward",1),("reverse",-1)):
                        actual=original_full_recount(
                            model,right_three_cycle_labels(
                                model["right_labels"],t,flag))
                        recount[sign]=actual
                        observed={
                            k:actual["seven_class_motif_counts"][k]-
                              source["seven_class_motif_counts"][k]
                            for k in SEVEN_CLASSES}
                        self.assertEqual(
                            result[sign]["delta_by_seven_class"],observed)
                        self.assertEqual(result[sign]["delta_S_seven"],
                                         actual["S_seven"]-source["S_seven"])
                        self.assertEqual(
                            result[sign]["delta_GF5_selected_lower_numerator"],
                            actual["GF5_seven_lower_numerator"]-
                            source["GF5_seven_lower_numerator"])
                    self.assertEqual(
                        result["order_commutator_S"],
                        recount["forward"]["S_seven"]-
                        recount["reverse"]["S_seven"])
                    self.assertLessEqual(
                        abs(result["order_commutator_S"]),
                        result["absolute_commutator_S_bound"])

    def test_true_W32_ordered_mixed_Hessian_classwise_and_GF5(self):
        for scheme,triple in (("lex",(0,1,2)),
                              ("S68",(8,9,12)),("S72",(1,7,14))):
            with self.subTest(scheme=scheme):
                model=fixture(1,scheme)
                compiled=compile_original_W32_cylinders(model)
                u,v,w=triple
                g=model["right_labels"]
                sigma=swapped_labels(g,u,v)
                tau=swapped_labels(g,v,w)
                first_then_second=swapped_labels(sigma,v,w)
                second_then_first=swapped_labels(tau,u,v)
                recount=[original_full_recount(model,labels) for labels in (
                    g,sigma,tau,first_then_second,second_then_first)]
                got=exact_ordered_three_cycle_curvature(compiled,g,triple)
                for orientation,idx in (("forward",3),("reverse",4)):
                    expected={
                        k:(recount[idx]["seven_class_motif_counts"][k]-
                            recount[1]["seven_class_motif_counts"][k]-
                            recount[2]["seven_class_motif_counts"][k]+
                            recount[0]["seven_class_motif_counts"][k])
                        for k in SEVEN_CLASSES}
                    self.assertEqual(
                        got[orientation+"_ordered_Hessian"][
                            "delta_by_seven_class"],expected)
                    self.assertEqual(
                        got[orientation+"_ordered_Hessian"]["delta_S_seven"],
                        sum(expected.values()))
                    self.assertEqual(
                        got[orientation+"_ordered_Hessian"][
                            "delta_GF5_selected_lower_numerator"],
                        sum(expected[k]*R3_CERTIFIED_FLOORS[k]
                            for k in SEVEN_CLASSES))
                self.assertEqual(
                    got["order_commutator_S"],
                    recount[3]["S_seven"]-recount[4]["S_seven"])
                self.assertEqual(
                    got["intersection_ONLY_formula_for_overlapping_swaps"],
                    "INVALID")

    def test_synthetic_order_tail_counters_false_intersection_formula(self):
        compiled,g,sig=synthetic_overlap_tail_instance()
        self.assertIsNone(cylinder_seven_class(sig,g))
        forward=right_three_cycle_labels(g,(0,1,2),1)
        reverse=right_three_cycle_labels(g,(0,1,2),-1)
        self.assertEqual(cylinder_seven_class(sig,forward),"B-left/A-right")
        self.assertIsNone(cylinder_seven_class(sig,reverse))
        result=exact_ordered_three_cycle_curvature(compiled,g,(0,1,2))
        self.assertEqual(result["intersection_original_cylinders"],0)
        self.assertEqual(result["forward_tail_original_cylinders"],1)
        self.assertEqual(result["forward_noncommuting_tail_component"][
            "delta_S_seven"],1)
        self.assertEqual(result["forward_intersection_component"][
            "delta_S_seven"],0)
        self.assertEqual(result["forward_ordered_Hessian"]["delta_S_seven"],1)
        self.assertEqual(result["order_commutator_S"],1)
        self.assertEqual(result["forward_ordered_Hessian"][
            "delta_GF5_selected_lower_numerator"],45600)

    def test_both_present_right_A_directed_BC_invariant(self):
        for scheme in ("S68","S72"):
            model=fixture(1,scheme)
            compiled=compile_original_W32_cylinders(model)
            labels=model["right_labels"]
            sampled=0
            for signature in compiled["cylinders"]:
                if signature[0] not in ("B","C") or len(set(signature[1]))!=6:
                    continue
                t=tuple(sorted(set(signature[1])))[:3]
                old=cylinder_seven_class(signature,labels)
                expected=("B-left/A-right" if signature[0]=="B" else "C/A")
                for direction in (-1,1):
                    after=cylinder_seven_class(
                        signature,right_three_cycle_labels(labels,t,direction))
                    self.assertEqual(old==expected,after==expected)
                sampled+=1
                if sampled>=250:
                    break
            self.assertEqual(sampled,250)

    def test_one_three_cycle_changes_only_original_triple_shadow(self):
        model=fixture(1,"S68")
        compiled=compile_original_W32_cylinders(model)
        triple=(0,1,2)
        result=exact_three_cycle_pair_delta(compiled,model["right_labels"],triple)
        affected={
            sig for sig in compiled["cylinders"]
            if set(sig[1]).intersection(triple)
        }
        self.assertEqual(result["touched_unique_original_cylinders"],
                         len(affected))
        self.assertEqual(result["touched_original_sixsets_weight"],
                         sum(compiled["cylinders"][sig] for sig in affected))
        self.assertLessEqual(abs(result["order_commutator_S"]),
                             result["touched_original_sixsets_weight"])
        self.assertLessEqual(abs(
            result["order_commutator_GF5_selected_lower_numerator"]),
            result["absolute_commutator_GF5_bound"])
        self.assertEqual(
            result["forward"]["delta_S_seven"]-
            result["reverse"]["delta_S_seven"],
            result["order_commutator_S"])

    def test_bad_and_overlapping_cycles_fail_closed(self):
        model=fixture(1,"lex")
        for triple,orientation in (((0,0,1),1),
                                   ((0,1,15),1),
                                   ((-1,0,1),1),
                                   ((0,1,2),0),
                                   ((0,1,2),2),
                                   ((0,1,2),False)):
            with self.subTest(triple=triple,orientation=orientation):
                with self.assertRaises(ValueError):
                    right_three_cycle_labels(model["right_labels"],
                                             triple,orientation)
        labels=model["right_labels"]
        t=(0,1,2)
        self.assertEqual(len(set(right_three_cycle_labels(labels,t,1))),
                         len(labels))
        self.assertNotEqual(right_three_cycle_labels(labels,t,1),
                            right_three_cycle_labels(labels,t,-1))
        compiled,g,sig=synthetic_overlap_tail_instance()
        with self.assertRaises(ValueError):
            exact_three_cycle_pair_delta(compiled,g,(1,1,2))


if __name__=="__main__":
    unittest.main()
