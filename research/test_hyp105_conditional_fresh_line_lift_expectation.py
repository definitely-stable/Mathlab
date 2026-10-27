"""AA4-K32LIFT: exact conditional expected original D6 from true line lifts."""
from fractions import Fraction
from itertools import combinations, permutations
import unittest

from hyp105_full_physical_degree_tail import genuine_source
from hyp105_k32_saturated_unit_multiplicity import (
    real_W34_two_disjoint_saturated_blocks,
)
from hyp105_saturated_fresh_extension_zero_w34 import (
    ZERO_OTHER_LINE_PAIR_PERMUTATION,
    true_W34_same_selected_zero_vs_positive_fresh_mass,
)
from hyp105_conditional_fresh_line_lift_expectation import (
    conditional_line_slot_probability,
    expected_fresh_mass_for_fixed_saturated_blocks,
    genuine_source_conditional_saturated_line_lift,
    deterministically_complete_line_labels_by_conditional_expectation,
)


def exact_W34_zero_line_completion(g,flags,ids,a=14):
    """Source-independent freeze-set reconstruction of #665 g_ZERO."""
    selected={flags[i][1] for i in ids}
    available=tuple(z for z in combinations(range(a),2)
                    if z not in {g[l] for l in selected})
    other=tuple(l for l in range(len(g)) if l not in selected)
    if (len(selected),len(other),len(available))!=(12,73,79):
        raise AssertionError("unexpected original W34 frozen line inventory")
    new=list(g)
    for l,j in zip(other,ZERO_OTHER_LINE_PAIR_PERMUTATION):
        new[l]=available[j]
    return tuple(new)


class TestConditionalFreshLineLiftExpectation(unittest.TestCase):
    def test_exact_toy_all_injective_line_completions_without_replacement(self):
        # Pure finitely enumerable probabilistic identity, not a GQ
        # source claim. Two unfrozen real-source line IDs are injected
        # into fourteen labels, with SIX original physical coords.
        a=6
        f=((0,5),(1,5),(2,5),(3,5))
        flags=((0,1),(1,2),(2,1))
        fixed={0:(0,4)}
        hubs=((0,0),(1,1),(2,2))
        frees=((3,3),(4,4))
        t=expected_fresh_mass_for_fixed_saturated_blocks(
            a,flags,f,fixed,((hubs,frees),),source_line_count=3)
        self.assertEqual(t["unfixed_original_source_lines"],2)
        self.assertEqual(t["available_unused_pair_labels"],14)
        self.assertEqual(t["expected_total_fresh_common_neighbor_mass"],
                         Fraction(2,14*13))
        self.assertEqual(t["expected_saturated_parent_original_D6_sector"],
                         Fraction(4,14*13))
        # SECOND oracle enumerates ALL 14*13 legal injections,
        # independently recovering original source rectangle incidences.
        available=tuple(z for z in combinations(range(a),2)
                        if z!=(0,4))
        exhaustive=0
        for pair1,pair2 in permutations(available,2):
            g={0:(0,4),1:pair1,2:pair2}
            for i,j in combinations(range(3),2):
                pi,pj=i,j
                li=next((l for l,z in g.items()
                         if z==(i,5)),None)
                lj=next((l for l,z in g.items()
                         if z==(j,5)),None)
                if li is not None and lj is not None and (
                        (pi,li) in flags and (pj,lj) in flags):
                    exhaustive+=1
        self.assertEqual(Fraction(exhaustive,14*13),
                         t["expected_total_fresh_common_neighbor_mass"])
        self.assertEqual(exhaustive,2)

    def test_exact_mixed_frozen_free_and_both_frozen_cases(self):
        incidence={(0,0),(1,1),(1,2)}
        fixed={(0,5):0,(1,5):1}
        degrees=[0,1]
        common={}
        self.assertEqual(conditional_line_slot_probability(
            0,1,(0,5),(1,5),fixed,degrees,common,13,incidence),
            Fraction(1))
        self.assertEqual(conditional_line_slot_probability(
            0,1,(0,5),(2,5),fixed,degrees,common,13,incidence),
            Fraction(1,13))
        self.assertEqual(conditional_line_slot_probability(
            1,0,(2,5),(1,5),fixed,degrees,common,13,incidence),
            Fraction(0))
        self.assertEqual(conditional_line_slot_probability(
            0,1,(2,5),(3,5),fixed,[1,2],{},13,incidence),
            Fraction(2,13*12))
        with self.assertRaises(ValueError):
            conditional_line_slot_probability(
                0,1,(2,5),(2,5),fixed,degrees,common,13,incidence)

    def test_true_W34_two_complete_g_maps_have_IDENTICAL_expectation(self):
        positive,f,g_positive,flags,ids=(
            real_W34_two_disjoint_saturated_blocks(return_inputs=True))
        g_zero=exact_W34_zero_line_completion(g_positive,flags,ids)
        pos=genuine_source_conditional_saturated_line_lift(
            2,f,g_positive,ids)
        zero=genuine_source_conditional_saturated_line_lift(
            2,f,g_zero,ids)
        for key in (
            "source_saturated_blocks","selected_original_source_IDs",
            "block_pair_expected_fresh_mass",
            "expected_total_fresh_common_neighbor_mass",
            "expected_saturated_parent_original_D6_sector",
            "at_least_one_complete_line_injection_original_D6_lower",
            "probability_components",
        ):
            self.assertEqual(pos[key],zero[key])
        self.assertEqual(pos["s"],4)
        self.assertEqual(pos["source_points"],85)
        self.assertEqual(pos["source_lines"],85)
        self.assertEqual(pos["source_flags"],425)
        self.assertEqual(pos["available_unused_pair_labels"],79)
        self.assertEqual(pos["unfixed_original_source_lines"],73)
        self.assertEqual(pos["source_saturated_blocks"],2)
        self.assertEqual(pos["selected_original_diagonal_edges"],24)
        self.assertGreater(pos["expected_total_fresh_common_neighbor_mass"],0)
        self.assertGreater(
            pos["at_least_one_complete_line_injection_original_D6_lower"],0)
        self.assertFalse(pos["pointwise_for_every_completion_positive_proved"])
        self.assertFalse(pos["root_sevenclass_Omega_s6_proved"])
        # The two ACTUAL completions have different, fully source
        # classified local masses, while the conditional expectation
        # given their identical frozen source labels is the SAME.
        direct=true_W34_same_selected_zero_vs_positive_fresh_mass()
        self.assertEqual(
            direct["positive"]["independent_original_source_rectangle_count"],4)
        self.assertEqual(
            direct["zero"]["independent_original_source_rectangle_count"],0)
        self.assertEqual(direct["same_saturated_selected_K32_blocks"],2)
        self.assertEqual(pos["source_saturated_blocks"],2)

    def test_true_W34_conditional_expectation_deterministic_derandomization(self):
        initial,f,g,flags,ids=(
            real_W34_two_disjoint_saturated_blocks(return_inputs=True))
        report=deterministically_complete_line_labels_by_conditional_expectation(
            2,f,g,ids)
        expected=genuine_source_conditional_saturated_line_lift(
            2,f,g,ids)
        self.assertEqual(report["source_selected_saturated_blocks"],2)
        self.assertEqual(
            report["line_assignments_chosen_deterministically"],73)
        self.assertEqual(report["all_source_incidence_flags"],425)
        self.assertEqual(report["initial_exact_expected_fresh_mass"],
                         expected["expected_total_fresh_common_neighbor_mass"])
        self.assertGreaterEqual(
            report["final_actual_fresh_mass"],
            report["initial_exact_expected_fresh_mass"])
        self.assertGreaterEqual(
            report["final_two_swap_original_GF5_accepted_D6"],
            2*report["initial_exact_expected_fresh_mass"])
        self.assertEqual(
            len(set(report["fully_injective_completed_original_line_pairs"])),
            85)
        self.assertTrue(
            report["method_of_conditional_expectations_verified"])
        # Selection labels NEVER change; these two complete g maps
        # may differ on all other true original lines.
        for i in ids:
            line=flags[i][1]
            self.assertEqual(
                report["fully_injective_completed_original_line_pairs"][line],
                g[line])
        self.assertFalse(report["root_sevenclass_Omega_s6_proved"])

    def test_incomplete_source_or_noninjective_frozen_lines_fail_closed(self):
        a=6
        f=((0,5),(1,5),(2,5),(3,5))
        flags=((0,1),(1,2),(2,1))
        block=(((0,0),(1,1),(2,2)),((3,3),(4,4)))
        with self.assertRaises(ValueError):
            expected_fresh_mass_for_fixed_saturated_blocks(
                a,flags,f,{0:(0,4),1:(0,4)},(block,),source_line_count=3)
        with self.assertRaises(ValueError):
            expected_fresh_mass_for_fixed_saturated_blocks(
                a,flags,f,{},(block,),source_line_count=1)
        with self.assertRaises(ValueError):
            expected_fresh_mass_for_fixed_saturated_blocks(
                a,flags,((0,5),(0,5),(2,5),(3,5)),{},(block,),
                source_line_count=3)
        model,f0,g0,flags0,ids=(
            real_W34_two_disjoint_saturated_blocks(return_inputs=True))
        bad=list(g0)
        bad[0]=bad[1]
        with self.assertRaises(ValueError):
            genuine_source_conditional_saturated_line_lift(2,f0,bad,ids)


if __name__=="__main__":
    unittest.main()
