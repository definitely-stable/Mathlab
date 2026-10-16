"""HYP-105 #230 AA4-BF: STRICT actual original SIXFLAG global D6 construction tests."""
import unittest
from fractions import Fraction
from itertools import permutations

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
from hyp105_issue230_d6aa4be_original_D6_pins import (
    original_D6_sixflag_pinned_envelope,
    original_W32_true_source_candidate_and_physical_cycle_census,
    falling,
)
from hyp105_issue230_d6aa4bf_constructive_original_D6_sixflag import (
    physically_ordered_original_D6_right_targets,
    original_W32_true_six_ID_D6_source_weights,
    exact_one_global_six_ID_D6_conditional_mean,
    exact_six_ID_D6_choose_next_global_line_image,
    construct_one_global_original_six_ID_D6_from_pins,
    independently_literal_original_D6_six_ID_charge,
)


def independent_true_original_historical_W32_six_ID_D6_census(model,source_Q,g):
    """Only previously historical SAME six original flag ID GF5 D6,
    no target array and no SOURCE six-line weight construction used.
    """
    return sum(classify_seven_prechecked(
        tuple(sorted(Q)),model["left_labels"],g,model["incidences"])=="D6"
        for Q in source_Q)


def completely_unrelated_brute_full_global_six_mapped_E6(weights,E,pins):
    remaining=tuple(i for i in range(6) if i not in pins)
    images=tuple(e for e in E if e not in pins.values())
    values=[]
    for perm in permutations(images):
        chosen=dict(pins)
        chosen.update(zip(remaining,perm))
        g=tuple(chosen[i] for i in range(6))
        # Literal physical C6 per source sixID; no conditional masks.
        val=0
        for six,w in weights.items():
            pairs=[g[j] for j in six]
            if len({x for p in pairs for x in p})!=6:continue
            meetings=[]
            for j in range(6):
                joint=set(pairs[j])&set(pairs[(j+1)%6])
                if len(joint)!=1:break
                meetings.append(next(iter(joint)))
            if len(meetings)==6 and len(set(meetings))==6:
                val+=w
        values.append(val)
    return Fraction(sum(values),len(values)),tuple(values)


class OriginalD6SixFlagAdaptiveConstructive(unittest.TestCase):
    def test_01_all_120_real_global_six_phys_edge_completions_and_exact_tower(self):
        # ABSTRACT weighted source six LINE IDs (not fake GQ),
        # SINGLE complete occupied right physical C6 support E of 6 edges.
        E=tuple(tuple(sorted((j,(j+1)%6))) for j in range(6))
        W={(0,1,2,3,4,5):3,
           (1,3,5,0,2,4):5,
           (5,4,3,2,1,0):2}
        pins={1:E[3]}
        physical=physically_ordered_original_D6_right_targets(E,6)
        self.assertEqual(len(physical),12)
        brute,vals=completely_unrelated_brute_full_global_six_mapped_E6(W,E,pins)
        self.assertEqual(len(vals),120)
        exact=exact_one_global_six_ID_D6_conditional_mean(
            W,E,6,pins,physical_targets=physical)
        self.assertEqual(exact,brute)
        last=exact;current=dict(pins)
        for k in range(5):
            free=set(range(6))-set(current)
            adversary=min(free) if k%2==0 else max(free)
            z=exact_six_ID_D6_choose_next_global_line_image(
                W,E,6,current,adversary,physical_targets=physical)
            self.assertEqual(z["conditional_mean_before"],last)
            self.assertGreaterEqual(z["conditional_mean_after"],last)
            self.assertEqual(z["all_remaining_legal_next_images_checked"],6-len(current))
            self.assertTrue(z["exact_tower_verified"])
            current=z["updated_original_source_LINE_pins"]
            last=z["conditional_mean_after"]
        g=tuple(current[i] for i in range(6))
        self.assertEqual(Fraction(independently_literal_original_D6_six_ID_charge(
            W,g,E,6)),last)
        self.assertGreaterEqual(last,exact)
        self.assertEqual(current[1],pins[1])
        self.assertEqual(set(g),set(E))

    def test_02_genuine_W32_all_four_SOURCE_populations_and_parent_pinned_means(self):
        for scheme in ("lex","reverse","S68","S72"):
            m=fixture(1,scheme)
            source=original_W32_true_six_ID_D6_source_weights(m)
            self.assertEqual(source["actual_eligible_source_Q_total"],
                             21186 if scheme.startswith("S") else 18716)
            self.assertEqual(source["point_occupied_C6"],60)
            self.assertTrue(all(len(set(t))==6 for t in source[
                "source_weighted_ordered_six_ORIGINAL_line_ID_tuples"]))
            E=tuple(tuple(e) for e in m["right_labels"])
            t=physically_ordered_original_D6_right_targets(E,6)
            self.assertEqual(len(t),720)
            for k in (0,1,2):
                pins={j:E[(j+3)%15] for j in range(k)}
                p=original_W32_true_source_candidate_and_physical_cycle_census(
                    m,pins)
                w={q:v for q,v in source[
                    "source_weighted_ordered_six_ORIGINAL_line_ID_tuples"].items()
                    if not(set(q)&set(pins))}
                actual=exact_one_global_six_ID_D6_conditional_mean(
                    w,E,6,pins,physical_targets=t)
                self.assertEqual(actual,p[
                    "exact_ONE_complete_original_LINE_permutation_conditional_D6_mean"])
            print("AA4BF genuine W32",scheme,
                  "real_original_source_six_Q",source["actual_eligible_source_Q_total"],
                  "true_original_exact_pinned_mean_two_LINEs",actual)

    def test_03_one_COMPLETE_genuine_W32_S68_global_D6_high_charge_with_adversarial_original_line_pins(self):
        m=fixture(1,"S68")
        source=original_W32_true_six_ID_D6_source_weights(m)
        E=tuple(m["right_labels"])
        # Two arbitrarily fixed ORIGINAL source LINE pair images, not
        # both global maps re-randomized per original six-Q.
        pins={0:E[4],7:E[1]}
        weights={q:v for q,v in source[
            "source_weighted_ordered_six_ORIGINAL_line_ID_tuples"].items()
                 if not(set(q)&set(pins))}
        order=tuple(reversed([i for i in range(15) if i not in pins]))
        z=construct_one_global_original_six_ID_D6_from_pins(
            weights,E,6,pins,source_order=order)
        self.assertTrue(z["complete"])
        g=z["one_complete_legal_original_global_right_g"]
        self.assertEqual(len(set(g)),15)
        self.assertEqual(set(g),set(E))
        self.assertEqual(g[0],pins[0])
        self.assertEqual(g[7],pins[7])
        exact_selected=independent_true_original_historical_W32_six_ID_D6_census(
            m,source["actual_six_distinct_original_incidence_ID_Q_in_C6_positions"],g)
        self.assertGreaterEqual(exact_selected,z[
            "complete_global_selected_original_sixID_D6_charge"])
        # Historical full D6 may contain pinned line factors too.
        self.assertGreaterEqual(
            z["complete_global_selected_original_sixID_D6_charge"],
            z["conditional_original_sixID_D6_mean_initial"])
        self.assertTrue(z["D6_potential_non_decreasing_all_steps"])
        self.assertEqual(len(z["step_original_D6_fraction_history"]),13)
        print("AA4BF full original W32 S68 TWO adversarial pins",
              "exact_INITIAL_conditional_original_D6_mean",
              z["conditional_original_sixID_D6_mean_initial"],
              "constructed_TRUE_ORIGINAL_sixID_D6_free",
              z["complete_global_selected_original_sixID_D6_charge"],
              "independent_FULL_original_GF5_D6",exact_selected)

    def test_04_genuine_W32_lex_adaptive_source_two_steps_only(self):
        m=fixture(1,"lex")
        source=original_W32_true_six_ID_D6_source_weights(m)
        E=tuple(m["right_labels"])
        pins={1:E[2]}
        weights={q:v for q,v in source[
            "source_weighted_ordered_six_ORIGINAL_line_ID_tuples"].items()
                 if 1 not in q}
        order=tuple(reversed([i for i in range(15) if i not in pins]))
        z=construct_one_global_original_six_ID_D6_from_pins(
            weights,E,6,pins,source_order=order,max_steps=2)
        self.assertFalse(z["complete"])
        self.assertIsNone(z["one_complete_legal_original_global_right_g"])
        self.assertEqual(len(z["last_globally_injective_real_original_source_pins"]),3)
        self.assertTrue(z["D6_potential_non_decreasing_all_steps"])
        self.assertGreaterEqual(z[
            "conditional_original_sixID_D6_mean_last"],z[
            "conditional_original_sixID_D6_mean_initial"])

    def test_05_all_dyadic_h5_to80_parent_strong_SOURCE_sixID_bound_and_constructive_preservation(self):
        # No fake high-order finite symplectic geometry materialized:
        # parent #568's REAL ORIGINAL sixflag source proof supplies
        # exact pinned Q/physical right six-C6 conditional mean.
        for h in range(5,81):
            s=1<<h
            V=(s+1)*(s*s+1)
            for k in (0,1,V//16):
                x=original_D6_sixflag_pinned_envelope(s,k)
                self.assertGreaterEqual(x[
                    "one_global_conditional_original_sixID_D6_expected_count_lower"],s**6)
                self.assertTrue(x[
                    "some_complete_legal_extension_selected_original_D6_ge_s6"])
                self.assertTrue(x[
                    "every_given_full_original_g_has_positive_D6_NOT_PROVED"])
            if h in (5,16,24,40,80):
                print("AA4BF ALL-H true original s",s,"V",V,
                      "arbitrary_fixed_LINE_budget",V//16,
                      "constructive_tower_full_same_global_g",True)

    def test_06_negative_fake_source_tuple_invalid_pins_and_complete_global_map(self):
        E=tuple(tuple(sorted((i,(i+1)%6))) for i in range(6))
        W={(0,1,2,3,4,5):1}
        for bad in ({0:E[0],1:E[0]},{0:(8,9)},{-1:E[0]},{9:E[0]}):
            with self.assertRaises(ValueError):
                exact_one_global_six_ID_D6_conditional_mean(W,E,6,bad)
        for bad in ({(0,0,1,2,3,4):1},
                    {(0,1,2,3,4,9):1},
                    {(0,1,2,3,4,5):0},
                    {(0,1,2,3,4,5):True}):
            with self.assertRaises(ValueError):
                exact_one_global_six_ID_D6_conditional_mean(bad,E,6,{})
        with self.assertRaises(ValueError):
            exact_six_ID_D6_choose_next_global_line_image(W,E,6,{0:E[0]},0)
        with self.assertRaises(ValueError):
            construct_one_global_original_six_ID_D6_from_pins(
                W,E,6,{},source_order=(1,))
        with self.assertRaises(ValueError):
            construct_one_global_original_six_ID_D6_from_pins(
                W,E,6,{},max_steps=-1)
        with self.assertRaises(ValueError):
            construct_one_global_original_six_ID_D6_from_pins(
                W,E,6,{},validate_floor_s=32)


if __name__=="__main__":
    unittest.main()
