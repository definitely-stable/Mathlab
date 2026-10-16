"""HYP-105 #230 AA4-BF2 INDEPENDENT MATHEMATICAL REFEREE of parallel PR #570.

Two different genuine-original D6 global-permutation conditional algorithms:
#570 works event-by-event using a positional fixed-edge inverted index
and physical occupied-edge integer bit masks; this branch independently
aggregates all source and physically oriented six-target patterns into
64-bit positional subset masks with independent actual ORIGINAL Q6
literal source ID derivation and terminal historical GF5 oracle.

This is NOT a second novel constructive theorem; it is a rigorously
separate agreement/falsifier suite on two concrete algorithms.
"""
import unittest
from fractions import Fraction

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
from hyp105_issue230_d6aa4bf_constructive_sixflag_D6 import (
    true_W32_original_D6_sixline_weights,
    oriented_right_sixcycles,
    ExactOriginalD6ConditionalPotential,
)
from hyp105_issue230_d6aa4bf_constructive_original_D6_sixflag import (
    original_W32_true_six_ID_D6_source_weights,
    physically_ordered_original_D6_right_targets,
    exact_one_global_six_ID_D6_conditional_mean,
    independently_literal_original_D6_six_ID_charge,
    construct_one_global_original_six_ID_D6_from_pins,
)


class IndependentSixflagD6SourceMapReferee(unittest.TestCase):
    def test_01_both_independent_PHYSICAL_sixcycle_target_sets_exactly_equal(self):
        for scheme in ("lex","reverse","S68","S72"):
            m=fixture(1,scheme)
            E=tuple(tuple(e) for e in m["right_labels"])
            owned={tuple(e):i for i,e in enumerate(E)}
            first=set(physically_ordered_original_D6_right_targets(E,6))
            second={tuple(owned[tuple(e)] for e in row)
                    for row in oriented_right_sixcycles(E,6)}
            self.assertEqual(first,second)
            self.assertEqual(len(first),720)

    def test_02_ALL_four_genuine_original_W32_and_zero_one_two_locked_LINE_source_IDs(self):
        for scheme in ("lex","reverse","S68","S72"):
            m=fixture(1,scheme)
            E=tuple(tuple(e) for e in m["right_labels"])
            other_source=original_W32_true_six_ID_D6_source_weights(m)
            expected=other_source[
                "actual_eligible_source_Q_total"]
            self.assertEqual(expected,21186 if scheme.startswith("S") else 18716)
            for k in (0,1,2):
                pins={j:E[(j+3)%15] for j in range(k)}
                # #570 SOURCE enumeration via canonical physical SIX
                # vertex order; our SOURCE via independent Q-first
                # explicit ORIGINAL INCIDENCE sixflag ID arrays.
                parent_source=true_W32_original_D6_sixline_weights(
                    m,initially_pinned_lines=tuple(pins))
                our_source={
                    q:w for q,w in other_source[
                        "source_weighted_ordered_six_ORIGINAL_line_ID_tuples"].items()
                    if not(set(q)&set(pins))
                }
                self.assertEqual(sum(our_source.values()),
                                 sum(parent_source.values()))
                parent_engine=ExactOriginalD6ConditionalPotential(
                    15,E,6,parent_source)
                first=parent_engine.potential(pins)
                second=exact_one_global_six_ID_D6_conditional_mean(
                    our_source,E,6,pins)
                self.assertEqual(first,second)
                if k==0:
                    self.assertEqual(sum(parent_source.values()),expected)
                print("AA4BF2 TRUE ORIGINAL INDEPENDENT",
                      scheme,"locked_LINEl_factor_IDs",k,
                      "six_Q_source_pool",sum(parent_source.values()),
                      "exact_#570_PER_EVENT_AND_#571_BITMASK_MEAN",first)

    def test_03_two_arbitrary_ORIGINAL_LINE_pins_final_one_g_both_engines_and_historical_GF5(self):
        m=fixture(1,"S68")
        E=tuple(tuple(e) for e in m["right_labels"])
        source=original_W32_true_six_ID_D6_source_weights(m)
        pins={0:E[4],7:E[1]}
        weights={
            q:w for q,w in source[
                "source_weighted_ordered_six_ORIGINAL_line_ID_tuples"].items()
            if not(set(q)&set(pins))
        }
        parent_w=true_W32_original_D6_sixline_weights(
            m,initially_pinned_lines=tuple(pins))
        parent=ExactOriginalD6ConditionalPotential(15,E,6,parent_w)
        order=tuple(reversed([i for i in range(15) if i not in pins]))
        ours=construct_one_global_original_six_ID_D6_from_pins(
            weights,E,6,pins,source_order=order)
        self.assertTrue(ours["complete"])
        g=ours["one_complete_legal_original_global_right_g"]
        literal_ours=independently_literal_original_D6_six_ID_charge(
            weights,g,E,6)
        literal_parent=parent.literal_full_D6_count(dict(enumerate(g)))
        conditional_parent=parent.potential(dict(enumerate(g)))
        self.assertEqual(literal_ours,literal_parent)
        self.assertEqual(Fraction(literal_ours),conditional_parent)
        self.assertEqual(literal_ours,ours[
            "complete_global_selected_original_sixID_D6_charge"])
        total_historical=sum(
            classify_seven_prechecked(
                tuple(sorted(Q)),m["left_labels"],g,m["incidences"])=="D6"
            for Q in source[
                "actual_six_distinct_original_incidence_ID_Q_in_C6_positions"])
        self.assertGreaterEqual(total_historical,literal_parent)
        self.assertEqual(g[0],pins[0])
        self.assertEqual(g[7],pins[7])
        print("AA4BF2 FROZEN TRUE ORIGINAL S68",
              "constructed_sixflag_D6_free",literal_ours,
              "independent_PR570_literal",literal_parent,
              "historical_GF5_D6_total",total_historical,
              "original_all_LINE_image_support_count",len(set(g)))

    def test_04_parent_and_independent_sixflag_adversarial_NEXT_source_ID_tower(self):
        m=fixture(1,"lex")
        E=tuple(tuple(e) for e in m["right_labels"])
        pins={0:E[4]}
        ours0=original_W32_true_six_ID_D6_source_weights(m)[
            "source_weighted_ordered_six_ORIGINAL_line_ID_tuples"]
        our_w={q:w for q,w in ours0.items() if 0 not in q}
        parent_w=true_W32_original_D6_sixline_weights(
            m,initially_pinned_lines=(0,))
        parent=ExactOriginalD6ConditionalPotential(15,E,6,parent_w)
        now=dict(pins)
        for line in (14,3):
            baseline=parent.potential(now)
            candidate=exact_one_global_six_ID_D6_conditional_mean(
                our_w,E,6,now)
            self.assertEqual(baseline,candidate)
            decision=parent.maximize_one_source_line(now,line)
            now[line]=decision["physical_edge"]
            after_parent=parent.potential(now)
            after_ours=exact_one_global_six_ID_D6_conditional_mean(
                our_w,E,6,now)
            self.assertEqual(after_parent,after_ours)
            self.assertGreaterEqual(after_ours,candidate)
            self.assertEqual(decision["next_potential"],after_parent)
            self.assertEqual(decision["mean_of_all_next_potentials"],candidate)
        self.assertEqual(now[0],pins[0])


if __name__=="__main__":
    unittest.main()
