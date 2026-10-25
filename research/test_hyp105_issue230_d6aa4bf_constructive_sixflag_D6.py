"""AA4-BF independent exact whole-permutation and TRUE ORIGINAL D6 falsifiers."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import permutations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4bf_constructive_sixflag_D6 import (
    sixcycle_vertex_orders, oriented_right_sixcycles,
    true_W32_original_D6_sixline_weights, ExactOriginalD6ConditionalPotential,
    all_h_original_D6_constructive_guarantee,
)
from hyp105_issue230_d6aa4be_original_D6_pins import (
    original_W32_true_source_candidate_and_physical_cycle_census,
)


def literal_rainbow_on_true_original_line_positions(edges):
    """Independent six original incidence position condition, no right target table."""
    if len(set(edges))!=6:
        return False
    shared=[]
    for i in range(6):
        cross=set(edges[i])&set(edges[(i+1)%6])
        if len(cross)!=1:
            return False
        shared.append(next(iter(cross)))
    return len(set(shared))==6


def independent_exact_720_permutations_mean(E):
    q=tuple(range(6))
    values=[]
    for im in permutations(E):
        values.append(int(literal_rainbow_on_true_original_line_positions(im)))
    return Fraction(sum(values),len(values)),values


class AA4BFConstructiveOriginalSixflagTests(unittest.TestCase):
    def test_01_global_sixline_full_720_permutations_adaptive_order_and_tower(self):
        E=tuple(tuple(sorted((i,(i+1)%6))) for i in range(6))
        base,v=independent_exact_720_permutations_mean(E)
        self.assertEqual(base,Fraction(1,60))
        self.assertEqual(sum(v),12)
        engine=ExactOriginalD6ConditionalPotential(6,E,6,{(0,1,2,3,4,5):1})
        self.assertEqual(len(engine.targets),12)
        self.assertEqual(engine.potential({}),base)
        self.assertEqual(engine.maximize_one_source_line({},5)[
            "mean_of_all_next_potentials"],base)
        order=(5,3,1,4,0,2)
        result=engine.greedy_complete({},choose_next=lambda psi,remaining:(
            next(j for j in order if j in remaining)))
        self.assertTrue(result["complete_original_global_line_map"])
        self.assertEqual(result["final_literal_original_D6_count"],1)
        self.assertEqual(result["current_conditional_original_D6_potential"],1)
        self.assertEqual([x["source_line"] for x in result["trace"]],list(order))
        self.assertEqual(result["initial_conditional_original_D6_mean"],base)
        self.assertTrue(result["no_per_source_Q_resampling"])
        for trace in result["trace"]:
            self.assertGreaterEqual(trace["next_potential"],trace["old_potential"])

    def test_02_independent_true_original_W32_sixflag_pool_and_mean(self):
        for scheme in ("lex","reverse","S68","S72"):
            model=fixture(1,scheme)
            w=true_W32_original_D6_sixline_weights(model)
            oracle=original_W32_true_source_candidate_and_physical_cycle_census(
                model,{})
            self.assertEqual(sum(w.values()),
                oracle["original_pointC6_six_distinct_lineID_source_Q_count"])
            self.assertEqual(sum(w.values()),
                21186 if scheme.startswith("S") else 18716)
            engine=ExactOriginalD6ConditionalPotential(
                15,model["right_labels"],6,w)
            self.assertEqual(len(engine.targets),720)
            self.assertEqual(engine.potential({}),
                oracle["exact_ONE_complete_original_LINE_permutation_conditional_D6_mean"])
            actual={i:tuple(model["right_labels"][i]) for i in range(15)}
            # Direct fixed SAME ORIGINAL f,g literal positional cycle,
            # not independent random source six-Q maps.
            brute=sum(cnt for ids,cnt in w.items() if
                literal_rainbow_on_true_original_line_positions(
                    tuple(tuple(actual[i]) for i in ids)))
            self.assertEqual(engine.literal_full_D6_count(actual),brute)

    def test_03_original_W32_adversarial_single_PIN_global_conditional_mean(self):
        for scheme in ("lex","S68"):
            model=fixture(1,scheme)
            right=tuple(map(tuple,model["right_labels"]))
            pin={0:right[3]}  # pin non-identity actual original LINE edge
            w=true_W32_original_D6_sixline_weights(model,{0})
            engine=ExactOriginalD6ConditionalPotential(15,right,6,w)
            independent=original_W32_true_source_candidate_and_physical_cycle_census(
                model,pin)
            self.assertEqual(engine.potential(pin),
                independent["exact_ONE_complete_original_LINE_permutation_conditional_D6_mean"])
            self.assertEqual(sum(w.values()),
                independent["original_sixflag_candidates_avoiding_pinned_lines"])
            selected=engine.maximize_one_source_line(pin,14)
            self.assertEqual(selected["old_potential"],engine.potential(pin))
            self.assertEqual(selected["mean_of_all_next_potentials"],
                             engine.potential(pin))
            self.assertGreaterEqual(selected["next_potential"],
                                    selected["old_potential"])
            result=engine.greedy_complete(pin,
                choose_next=lambda psi,free: max(free),max_steps=2)
            self.assertFalse(result["complete_original_global_line_map"])
            self.assertTrue(result["all_initial_actual_LINE_pins_preserved"])
            self.assertEqual(len(result["trace"]),2)
            self.assertGreaterEqual(result["current_conditional_original_D6_potential"],
                                    result["initial_conditional_original_D6_mean"])

    def test_04_full_TRUE_original_W32_global_D6_derandomization(self):
        model=fixture(1,"lex")
        source=true_W32_original_D6_sixline_weights(model)
        engine=ExactOriginalD6ConditionalPotential(15,model["right_labels"],6,source)
        initial=engine.potential({})
        result=engine.greedy_complete({},choose_next=lambda psi,free: max(free))
        self.assertTrue(result["complete_original_global_line_map"])
        self.assertEqual(result["final_literal_original_D6_count"],
                         result["current_conditional_original_D6_potential"])
        self.assertGreaterEqual(result["final_literal_original_D6_count"],initial)
        self.assertEqual(set(result["line_image_mapping"]),set(range(15)))
        self.assertEqual(len(set(result["line_image_mapping"].values())),15)
        self.assertTrue(result["all_initial_actual_LINE_pins_preserved"])

    def test_05_all_dyadic_h5_to80_sixflag_root_scope_without_fake_source(self):
        for h in tuple(range(5,36))+(40,48,64,80):
            s=1<<h
            V=(s+1)*(s*s+1)
            for k in (0,1,V//16):
                z=all_h_original_D6_constructive_guarantee(s,k)
                self.assertGreaterEqual(z["parent_verified_expected_original_D6_floor"],
                                        Fraction(27,25)*(s+1)**6)
                self.assertEqual(z["constructed_selected_original_GF5_D6_floor"],s**6)
                self.assertTrue(z["any_adaptive_order_of_unassigned_original_LINE_IDs"])
                self.assertTrue(z["all_given_fully_fixed_original_f_g_lower_NOT_PROVED"])
                self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")

    def test_06_reject_invalid_images_duplicate_source_factor_pins_and_partial_final(self):
        E=tuple(tuple(sorted((i,(i+1)%6))) for i in range(6))
        with self.assertRaises(ValueError):
            ExactOriginalD6ConditionalPotential(6,E,6,{(0,0,2,3,4,5):1})
        with self.assertRaises(ValueError):
            ExactOriginalD6ConditionalPotential(6,E[:-1]+(E[0],),6,
                                               {(0,1,2,3,4,5):1})
        z=ExactOriginalD6ConditionalPotential(6,E,6,{(0,1,2,3,4,5):1})
        for bad in ({0:E[0],1:E[0]}, {6:E[0]}, {0:(0,3)}):
            with self.assertRaises(ValueError):
                z.potential(bad)
        with self.assertRaises(ValueError):
            z.literal_full_D6_count({0:E[0]})
        with self.assertRaises(ValueError):
            z.maximize_one_source_line({},8)
        with self.assertRaises(ValueError):
            z.greedy_complete({0:E[0]},max_steps=0)
        for s in (2,4,16,33):
            with self.assertRaises(ValueError):
                all_h_original_D6_constructive_guarantee(s,0)

if __name__=="__main__":
    unittest.main()
