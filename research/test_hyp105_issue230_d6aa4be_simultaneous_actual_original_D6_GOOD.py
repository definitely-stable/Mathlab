"""AA4-BE: independent historical seven GF5 D6 + globally same-map GOOD tests."""
import unittest
from itertools import combinations
from fractions import Fraction

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
from hyp105_issue230_d6aa4aw_sharp_original_twoport_marginals import (
    exact_TRUE_original_twoport_marginal_repair_frontier,
)
from hyp105_issue230_d6aa4be_simultaneous_actual_original_D6_GOOD import (
    six_clique_in_minimal_occupied_original_support,
    actual_true_original_sixflag_left_cycle_order,
    choose_genuine_original_Q_from_any_complete_point_f,
    pin_original_D6_and_construct_global_good,
    all_h_original_sixpin_D6_GOOD_math_certificate,
    all_alphabet_original_sixflag_D6_positional_pattern,
)


def independent_literal_selected_d6_original_sixflags(model,Q,g):
    """Physical original-six-flag cycle EXACTLY, no GF5 classifier.

    Pairwise positional intersection graphs on f(point of flag) and
    g(original line of flag) must be identical connected C6; original
    six source factor IDs of each type distinct.
    """
    inc=tuple(tuple(e) for e in model["incidences"])
    f=model["left_labels"]
    pts=tuple(inc[i][0] for i in Q)
    lines=tuple(inc[i][1] for i in Q)
    if len(set(pts))!=6 or len(set(lines))!=6:return False
    adj=[]
    for data,items in ((f,pts),(g,lines)):
        edges=tuple(data[x] for x in items)
        if len({v for e in edges for v in e})!=6:return False
        graph=set()
        for i,j in combinations(range(6),2):
            if set(edges[i])&set(edges[j]):graph.add((i,j))
        if len(graph)!=6 or any(
                sum(k in e for e in graph)!=2 for k in range(6)):
            return False
        seen={0};todo=[0]
        while todo:
            i=todo.pop()
            for x,y in graph:
                n=y if x==i else x if y==i else None
                if n is not None and n not in seen:
                    seen.add(n);todo.append(n)
        if len(seen)!=6:return False
        adj.append(graph)
    return adj[0]==adj[1]


def independent_same_original_global_GOOD_3flag_count(model,g):
    """Existing original GOOD four-port adjacent actual TRUE GQ audit,
    not the exact source-weight+conditional expectation calculation."""
    m=dict(model,right_labels=tuple(g))
    t=exact_TRUE_original_twoport_marginal_repair_frontier(m)
    return t["physically_opposite_ACTUAL_original_GOOD_D_centered_3flag_wedges"]


class TrueOriginalSimultaneousD6AndGood(unittest.TestCase):
    def test_01_all_dyadic_h5_to80_actual_SOURCE_GQ_parameters_and_six_pins(self):
        for h in range(5,81):
            s=1<<h
            cert=all_h_original_sixpin_D6_GOOD_math_certificate(s)
            self.assertEqual(cert["V"],(s+1)*(s*s+1))
            self.assertEqual(cert["a"]*(cert["a"]-1)//2-cert["missing_E_Ka_edges"],
                             cert["V"])
            self.assertTrue(cert["six_ORIGINAL_LINE_image_pins_satisfy_parent_budget"])
            self.assertTrue(cert["one_GLOBAL_completed_original_g_constructive_D6_Q_and_GOOD"])
            self.assertGreaterEqual(
                cert["source_original_GOOD_3flag_lower"],Fraction(s**6,512))
            self.assertEqual(
                cert["historic_GF5_D6_positive_six_ID_count_at_least_ONE_only"],1)
            self.assertTrue(cert["source_good_3flag_to_seven_GF5_count_s6_NOT_proved"])
            if h in (5,6,16,24,40,80):
                print("AA4BE DYADIC ALL-H",h,
                      "physical-a",cert["a"],
                      "missing-pairs",cert["missing_E_Ka_edges"],
                      "ONE_GLOBAL_D6_GF5_AND_GOOD",True)
        for bad in (2,4,16,33,0,-1,True):
            with self.assertRaises(ValueError):
                all_h_original_sixpin_D6_GOOD_math_certificate(bad)

    def test_02_adversarial_original_physical_E_K261_near_complete_s32_clique(self):
        s=32
        V=(s+1)*(s*s+1)
        a=261
        self.assertEqual((a*(a-1)//2)-V,105)
        all_edges=set(combinations(range(a),2))
        missing_star=set(combinations(range(106),2)) # replace below
        # 105 missing star edges, still 33825 globally occupied.
        missing_star={(0,i) for i in range(1,106)}
        missing_spread={(2*i,2*i+1) for i in range(105)}
        for holes in (missing_star,missing_spread):
            E=tuple(sorted(all_edges-holes))
            self.assertEqual(len(E),V)
            six=six_clique_in_minimal_occupied_original_support(E,a)
            self.assertEqual(len(six),6)
            self.assertTrue(all(tuple(sorted(e)) in set(E)
                                for e in combinations(six,2)))
            self.assertTrue(all(tuple(sorted((six[j],six[(j+1)%6])))
                                in E for j in range(6)))

    def test_03_true_original_W32_selected_AUTO_Q_and_one_GLOBAL_g_both_properties(self):
        for scheme in ("lex","reverse","S68","S72"):
            m=fixture(1,scheme)
            Q=choose_genuine_original_Q_from_any_complete_point_f(m)
            self.assertEqual(len(Q),6)
            self.assertEqual(len(set(Q)),6)
            order=actual_true_original_sixflag_left_cycle_order(m,Q)
            self.assertEqual(set(order),set(Q))
            z=pin_original_D6_and_construct_global_good(
                m,Q,verify_universal_guarantee=False)
            self.assertTrue(z["complete_original_line_g_realized"])
            self.assertEqual(z["historical_seven_GF5_original_six_incidence_Q_class"],"D6")
            self.assertEqual(len(z["six_original_LINE_images_always_pinned_to_ONE_D6_C6"]),6)
            g=z["actual_global_LINE_factor_images"]
            self.assertEqual(set(g),set(tuple(e) for e in m["right_labels"]))
            self.assertTrue(independent_literal_selected_d6_original_sixflags(m,Q,g))
            self.assertTrue(all_alphabet_original_sixflag_D6_positional_pattern(m,Q,g))
            self.assertFalse(z["all_h_s_greater_2_legacy_K6_classifier_NOT_called"])
            self.assertEqual(classify_seven_prechecked(
                Q,m["left_labels"],g,m["incidences"]),"D6")
            self.assertEqual(z["complete_GLOBAL_original_GOOD_charge"],
                             independent_same_original_global_GOOD_3flag_count(m,g))
            self.assertGreaterEqual(z["complete_GLOBAL_original_GOOD_charge"],
                                    z["complete_GLOBAL_unpinned_original_GOOD_charge"])
            self.assertGreaterEqual(z["complete_GLOBAL_unpinned_original_GOOD_charge"],
                                    z["initial_PINNED_original_GOOD_conditional_mean"])
            print("AA4BE TRUE ORIGINAL W32",scheme,
                  "exact_six_flag_source_IDs_Q",Q,
                  "historical_selected_tag",z[
                      "historical_seven_GF5_original_six_incidence_Q_class"],
                  "source_GOOD_threeflag_charge",z[
                      "complete_GLOBAL_original_GOOD_charge"],
                  "source_free_GOOD_charge",z[
                      "complete_GLOBAL_unpinned_original_GOOD_charge"],
                  "initial_mean",z["initial_PINNED_original_GOOD_conditional_mean"])

    def test_04_true_original_W32_TWO_frozen_independent_six_source_flag_Q(self):
        frozen={"S68":(2,19,22,35,36,42),
                "S72":(10,15,23,29,30,33)}
        for scheme,Q in frozen.items():
            m=fixture(1,scheme)
            z=pin_original_D6_and_construct_global_good(
                m,Q,verify_universal_guarantee=False)
            g=z["actual_global_LINE_factor_images"]
            self.assertTrue(independent_literal_selected_d6_original_sixflags(m,Q,g))
            self.assertEqual(z["historical_seven_GF5_original_six_incidence_Q_class"],"D6")
            self.assertEqual(independent_same_original_global_GOOD_3flag_count(m,g),
                             z["complete_GLOBAL_original_GOOD_charge"])
            self.assertTrue(z["root_230_A_B_C_OPEN"])

    def test_05_true_original_W34_K14_nononto_six_D6_pins_TWO_steps_only(self):
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            Q=choose_genuine_original_Q_from_any_complete_point_f(m)
            z=pin_original_D6_and_construct_global_good(
                m,Q,max_steps=2,verify_universal_guarantee=False)
            self.assertFalse(z["complete_original_line_g_realized"])
            self.assertIsNone(z["actual_global_LINE_factor_images"])
            self.assertIsNone(z["historical_seven_GF5_original_six_incidence_Q_class"])
            self.assertEqual(len(z["six_original_LINE_images_always_pinned_to_ONE_D6_C6"]),6)
            self.assertTrue(z["independent_PROVISIONAL_full_original_D6_witness"])
            self.assertTrue(z["all_h_s_greater_2_legacy_K6_classifier_NOT_called"])
            self.assertTrue(z["all_alphabet_original_D6_sixflag_pattern_prechecked"])
            self.assertTrue(all_alphabet_original_sixflag_D6_positional_pattern(
                m,Q,z["provisional_GLOBAL_original_LINE_images_structural_D6"]))
            self.assertGreaterEqual(
                z["initial_PINNED_original_GOOD_conditional_mean"],0)
            self.assertTrue(z["right_global_occupied_physical_edge_support_preserved"])
            print("AA4BE TRUE ORIGINAL W34",scheme,"SIX_Q",Q,
                  "provisional_GLOBAL_D6_only_and_GOOD_two_step",True)

    def test_06_independent_historical_GF5_reject_noneligible_source_Q_and_fake_maps(self):
        m=fixture(1,"S68")
        Q=choose_genuine_original_Q_from_any_complete_point_f(m)
        for badQ in ((Q[0],)*6, Q[:5],(-1,)+Q[1:],
                     (Q[0],Q[0],*Q[2:])):
            with self.assertRaises(ValueError):
                actual_true_original_sixflag_left_cycle_order(m,badQ)
        f=tuple(m["left_labels"])
        badm=dict(m,left_labels=(f[0],)*len(f))
        with self.assertRaises(ValueError):
            choose_genuine_original_Q_from_any_complete_point_f(badm)
        badr=dict(m,right_labels=(m["right_labels"][0],)*15)
        with self.assertRaises(ValueError):
            pin_original_D6_and_construct_global_good(badr,Q,
                                                      verify_universal_guarantee=False)
        with self.assertRaises(ValueError):
            six_clique_in_minimal_occupied_original_support(
                tuple(combinations(range(6),2))[:10],6)


if __name__=="__main__":unittest.main()
