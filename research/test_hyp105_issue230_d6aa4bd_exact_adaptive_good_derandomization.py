"""HYP-105 #230 AA4-BD: actual and independent deterministic global GOOD completion."""
import unittest
from fractions import Fraction
from itertools import combinations, permutations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4az_quenched_allD_variance import (
    original_line_triple_weights,
)
from hyp105_issue230_d6aa4bc_robust_pins import (
    actual_original_pinned_completion_certificate,
    certified_robust_pins_envelope,
)
from hyp105_issue230_d6aa4bd_exact_adaptive_good_derandomization import (
    exact_global_completion_conditional_GOOD_expectation,
    independent_literal_final_global_GOOD_charge,
    physically_clean_opposite_ordered_edge_indices,
    choose_one_adaptive_original_line_image,
    constructive_true_original_GOOD_partial_line_completion,
)


def independent_literal_physical_good(g,occupied,a,l,k0,k1):
    """Different physical clean source from MISSING EDGE enumeration.
    Avoids use of the new physically-clean ordered triple helper."""
    occupied={tuple(sorted(x)) for x in occupied}
    missing=set(combinations(range(a),2))-occupied
    bad={v for v in range(a) if 16*sum(v in e for e in missing)>=a}
    e,x,y=(tuple(sorted(g[i])) for i in (l,k0,k1))
    if any(set(z)&bad for z in (e,x,y)):return False
    P=set(e)&set(x);L=set(e)&set(y)
    return len(P)==len(L)==1 and P!=L


def independent_brute_full_GLOBAL_conditional_distribution(w,E,a,pins):
    E=tuple(tuple(sorted(e)) for e in E)
    free_lines=tuple(i for i in range(len(E)) if i not in pins)
    locked={tuple(sorted(e)) for e in pins.values()}
    free_edges=tuple(e for e in E if e not in locked)
    if len(free_lines)>7:
        raise ValueError("independent exhaustive full global enumeration only small")
    values=[]
    for edge_perm in permutations(free_edges):
        global_map=dict(pins);global_map.update(zip(free_lines,edge_perm))
        values.append(sum(weight for (l,k0,k1),weight in w.items()
                          if independent_literal_physical_good(
                            global_map,E,a,l,k0,k1)))
    return (Fraction(sum(values),len(values)),tuple(values))


class ExactAdaptiveTrueOriginalGlobalGoodCompletion(unittest.TestCase):
    def test_01_independent_all_120_FULL_GLOBAL_line_maps_one_locked_abstract_weights(self):
        # Pure abstract positive source weights: validates exact global
        # permutation theorem, not falsely presented as genuine W3s.
        E=tuple(combinations(range(4),2))
        a=4
        weights={(0,1,2):2,(2,3,4):3,(1,4,5):5,(3,0,5):7}
        pins={0:E[1]}
        f=physically_clean_opposite_ordered_edge_indices(E,a)
        expected=exact_global_completion_conditional_GOOD_expectation(
            weights,E,a,pins,physical_triples=f)
        brute,distribution=independent_brute_full_GLOBAL_conditional_distribution(
            weights,E,a,pins)
        self.assertEqual(len(distribution),120)
        self.assertEqual(expected,brute)
        current=dict(pins);prev=expected
        # Dynamically/adversarially choose which still-free original
        # source line arrives next, AFTER prior edge was selected.
        for step in range(5):
            remaining=set(range(6))-set(current)
            chosen=min(remaining) if step%2==0 else max(remaining)
            z=choose_one_adaptive_original_line_image(
                weights,E,a,current,chosen,physical_triples=f)
            self.assertEqual(z["prefix_exact_conditional_expectation"],prev)
            self.assertGreaterEqual(z["after_exact_conditional_expectation"],prev)
            self.assertEqual(
                sum(v for _,v in z["candidate_expected_values"]),
                len(z["candidate_expected_values"])*prev)
            current=z["complete_global_source_line_map_pins_after_step"]
            prev=z["after_exact_conditional_expectation"]
        self.assertEqual(len(current),6)
        result=independent_literal_final_global_GOOD_charge(
            weights,tuple(current[i] for i in range(6)),E,a)
        self.assertEqual(Fraction(result),prev)
        self.assertGreaterEqual(prev,expected)
        self.assertEqual(len(set(current.values())),6)
        self.assertEqual(current[0],E[1])

    def test_02_true_original_W32_full_global_greedy_TWO_different_original_maps(self):
        for scheme in ("S68","S72"):
            m=fixture(1,scheme)
            E=tuple(tuple(sorted(e)) for e in m["right_labels"])
            pins={0:E[(2 if scheme=="S68" else 5)]}
            original=actual_original_pinned_completion_certificate(m,pins)
            w=original_line_triple_weights(m,clean_only=True)
            w={key:v for key,v in w.items() if 0 not in key}
            # Deliberately reverse original source LINE factor order:
            # the algorithm cannot exploit original input ordering.
            order=tuple(reversed([j for j in range(15) if j not in pins]))
            z=constructive_true_original_GOOD_partial_line_completion(
                m,pins,source_order=order,verify_all_h_floor=False)
            self.assertTrue(z["is_COMPLETE_legal_global_original_LINE_map"])
            self.assertEqual(z[
                "conditional_good_wedge_source_3flag_initial_mean"],
                original["mean_unpinned_source_good_wedges"])
            self.assertEqual(z[
                "conditional_good_wedge_source_3flag_final_potential"],
                z["completed_true_original_FREE_good_opposite_threeflag_charge"])
            self.assertGreaterEqual(
                z["completed_true_original_ALL_good_opposite_threeflag_charge"],
                z["completed_true_original_FREE_good_opposite_threeflag_charge"])
            self.assertEqual(z[
                "completed_GLOBAL_original_line_source_factor_images"][0],pins[0])
            self.assertEqual(set(z[
                "completed_GLOBAL_original_line_source_factor_images"]),set(E))
            literal=independent_brute_original_full_good_source_census(
                m,z["completed_GLOBAL_original_line_source_factor_images"])
            self.assertEqual(literal,z[
                "completed_true_original_ALL_good_opposite_threeflag_charge"])
            self.assertEqual(
                tuple(x["source_original_line_ID"] for x in z["steps"]),order)
            self.assertTrue(all(x["after"]>=x["before"] for x in z["steps"]))
            self.assertTrue(z["arbitrary_fully_FIXED_g_positive_not_proved"])
            self.assertTrue(z["selected_seven_GF5_six_original_incidence_ID_Q_NOT_PROVED"])
            print("AA4BD_TRUE_ORIGINAL_W32",scheme,
                  "one_adversarial_INITIAL_PIN",pins,
                  "exact_INITIAL_MEAN",z[
                    "conditional_good_wedge_source_3flag_initial_mean"],
                  "CONSTRUCTED_actual_FREE_GOOD",z[
                    "completed_true_original_FREE_good_opposite_threeflag_charge"],
                  "CONSTRUCTED_ALL_GOOD",literal,
                  "whole_global_factor_choices",len(z["steps"]))

    def test_03_true_original_W34_nononto_both_typed_physical_support_first_steps(self):
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            E=tuple(tuple(sorted(e)) for e in m["right_labels"])
            pins={0:E[2],4:E[8]}
            parent=actual_original_pinned_completion_certificate(m,pins)
            z=constructive_true_original_GOOD_partial_line_completion(
                m,pins,source_order=tuple(
                  reversed(tuple(j for j in range(85) if j not in pins))),
                max_steps=2,verify_all_h_floor=False)
            self.assertFalse(z["is_COMPLETE_legal_global_original_LINE_map"])
            self.assertEqual(len(z["steps"]),2)
            self.assertEqual(z[
                "conditional_good_wedge_source_3flag_initial_mean"],
                parent["mean_unpinned_source_good_wedges"])
            self.assertGreaterEqual(z[
                "conditional_good_wedge_source_3flag_final_potential"],
                z["conditional_good_wedge_source_3flag_initial_mean"])
            self.assertEqual(len(z[
                "all_real_original_source_global_line_pins_after_steps"]),4)
            self.assertTrue(z[
                "fixed_original_line_physically_occupied_E_unchanged"])
            self.assertIsNone(z[
                "completed_true_original_FREE_good_opposite_threeflag_charge"])
            self.assertFalse(z[
                "s_ge32_initial_k_le_V_over1024_implies_constructed_GOOD_ge_s6_over512"])
            print("AA4BD_TRUE_ORIGINAL_W34_NONONTO",scheme,
                  "TRUE_Q_source_k",len(pins),
                  "exact_PINNED_MEAN",parent["mean_unpinned_source_good_wedges"],
                  "after_two_deterministic_decisions",z[
                    "conditional_good_wedge_source_3flag_final_potential"])

    def test_04_independent_original_W32_source_threeflag_literal_FULL_oracle(self):
        for scheme in ("lex","reverse"):
            m=fixture(1,scheme)
            original_line_map=tuple(m["right_labels"])
            w=original_line_triple_weights(m,clean_only=True)
            full=independent_literal_final_global_GOOD_charge(
                w,original_line_map,original_line_map,6)
            literal=independent_brute_original_full_good_source_census(
                m,original_line_map)
            self.assertEqual(full,literal)
            # At NO PINS old conditional mean is the parent one-GLOBAL-
            # permutation expectation; no per-threeflag image redraw.
            parent=actual_original_pinned_completion_certificate(m,{})
            mean=exact_global_completion_conditional_GOOD_expectation(
                w,original_line_map,6,{})
            self.assertEqual(mean,parent["mean_unpinned_source_good_wedges"])

    def test_05_all_h_parent_any_adversarial_partial_pins_and_constructive_tower(self):
        # This checks actual parent's all-h rigorous *input condition*;
        # our math proves existence of a deterministic algorithm for
        # every such input via a symbolic conditional-expectation
        # invariant, not via fake large synthetic symplectic fixtures.
        for h in (*range(5,27),32,40,60,80):
            s=1<<h
            V=(s+1)*(s*s+1)
            for k in (0,1,V//1024):
                q=certified_robust_pins_envelope(s,k)
                self.assertGreaterEqual(
                    q["conditional_mean_of_unpinned_GOOD_wedges_lower"],
                    Fraction(s**6,512))
                self.assertTrue(q[
                    "existence_of_some_completion_with_GOOD_ge_s6_over512"])
                self.assertTrue(q["ALL_fully_fixed_g_or_six_ID_GF5_PROVED"] is False)
                self.assertTrue(q["eta_le_30000000000_over_V"])
            if h in (5,16,24,80):
                print("AA4BD_SYMBOLIC_REAL_ORIGINAL_GQ_ALL_PINS",
                      "h",h,"V",V,
                      "adversarial_pin_limit",V//1024,
                      "DERANDOMIZATION_VIA_EXACT_TOWER",True)

    def test_06_input_guard_and_distinguish_pinned_from_fully_fixed_original_g(self):
        E=tuple(combinations(range(4),2))
        w={(0,1,2):1}
        for pins in (
            {0:E[0],1:E[0]},
            {0:(8,9)},
            {-1:E[0]},
            {88:E[0]},
        ):
            with self.assertRaises(ValueError):
                exact_global_completion_conditional_GOOD_expectation(
                    w,E,4,pins)
        for bad in (
            {(0,0,2):1},
            {(0,1,2):-1},
            {(0,1,2):True},
            {(0,1,99):1},
        ):
            with self.assertRaises(ValueError):
                exact_global_completion_conditional_GOOD_expectation(
                    bad,E,4,{})
        with self.assertRaises(ValueError):
            choose_one_adaptive_original_line_image(w,E,4,{},100)
        with self.assertRaises(ValueError):
            choose_one_adaptive_original_line_image(w,E,4,{0:E[0]},0)
        m=fixture(1,"lex")
        with self.assertRaises(ValueError):
            constructive_true_original_GOOD_partial_line_completion(
                m,{},source_order=(0,),verify_all_h_floor=False)
        with self.assertRaises(ValueError):
            constructive_true_original_GOOD_partial_line_completion(
                m,{},max_steps=-1,verify_all_h_floor=False)


def independent_brute_original_full_good_source_census(model,g):
    """TRUE ORIGINAL threeflag witness enumerated directly from
    genuine incidence list and exact physical f/g source factors:
    no weighted triple helper, no conditional expectation helper."""
    inc=tuple(map(tuple,model["incidences"]))
    f=tuple(tuple(sorted(e)) for e in model["left_labels"])
    Eleft=set(f)
    a=model["a"]
    missing=set(combinations(range(a),2))-Eleft
    bad_point={u for u in range(a)
               if 16*sum(u in e for e in missing)>=a}
    Eright={tuple(sorted(e)) for e in g}
    missing_right=set(combinations(range(a),2))-Eright
    bad_line={u for u in range(a)
              if 16*sum(u in e for e in missing_right)>=a}
    degree=0
    for p,l in inc:
        if set(f[p])&bad_point or set(g[l])&bad_line:continue
        for q0,k0 in inc:
            if len({p,q0})!=2 or len({l,k0})!=2:continue
            if set(f[q0])&bad_point or set(g[k0])&bad_line:continue
            left=set(f[p])&set(f[q0])
            right=set(g[l])&set(g[k0])
            if len(left)!=1 or len(right)!=1:continue
            for q1,k1 in inc:
                if len({p,q0,q1})!=3 or len({l,k0,k1})!=3:continue
                if set(f[q1])&bad_point or set(g[k1])&bad_line:continue
                pother=set(f[p])&set(f[q1])
                lother=set(g[l])&set(g[k1])
                # GOOD source triples are UNORDERED in their two
                # outer true-original flags; the source weight oracle
                # chooses the orientation of point ports in canonical
                # ascending physical order. Without this canonical
                # point-side convention the literal triple loop
                # counts every actual GOOD wedge TWICE.
                u,v=sorted(f[p])
                if (len(pother)==len(lother)==1 and
                        left=={u} and pother=={v} and right!=lother):
                    degree+=1
    return degree


if __name__=="__main__":
    unittest.main()
