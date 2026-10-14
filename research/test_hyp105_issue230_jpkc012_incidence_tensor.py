"""JPKC-012 direct ORIGINAL incidence-tensor exactness, independent W32 oracle."""
import unittest
from collections import Counter

from hyp105_issue230_projection import fixture
from hyp105_issue230_jpkc012_incidence_tensor import (
    physical_twofactor_multigraphs, compile_incidence_tensor,
    contract_incidence_tensor, independent_comparison,
    coherent_right_fiber_tensor, source_multiplicity_type,
    _same_global_labels, _connected_dual,
)
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS


class JPKC012Tests(unittest.TestCase):
    def test_complete_130_multigraph_exact_covers_without_original_path_proxy(self):
        patterns=physical_twofactor_multigraphs(tuple(range(6)))
        counts=Counter(tuple(sorted(Counter(x).values(), reverse=True)) for x in patterns)
        self.assertEqual(dict(counts),{
            (1,1,1,1,1,1):70,(2,1,1,1,1):45,(2,2,2):15})
        self.assertEqual(len(patterns),len(set(patterns)))
        for p in patterns:
            self.assertEqual(len(p),6)
            self.assertEqual(Counter(x for edge in p for x in edge),
                             Counter({i:2 for i in range(6)}))
        with self.assertRaises(ValueError):
            physical_twofactor_multigraphs((0,1,2,3,4,4))

    def test_all_original_W32_models_complete_source_profile_tensor_vs_independent_GF5(self):
        expected={"lex":259,"reverse":169,"S68":68,"S72":72}
        for scheme,s in expected.items():
            with self.subTest(scheme=scheme):
                model=fixture(1,scheme)
                compiled=compile_incidence_tensor(model)
                self.assertEqual(compiled["candidate_original_Q"],62370)
                self.assertEqual(compiled["original_point_profile_histogram"],
                                 {"A":51030,"B":10935,"C":405})
                self.assertEqual(compiled["physical_twofactor_pattern_histogram"],
                    {"left_pattern_A":70,"left_pattern_B":45,"left_pattern_C":15})
                self.assertGreater(compiled["source_line_profile_count"],0)
                self.assertGreater(compiled["distinct_sparse_right_profile_cylinder_rows"],0)
                self.assertGreater(compiled["distinct_source_line_AA_dual_rows"],0)
                # Precise SOURCE-line tensor dimensions from independent hosted oracle:
                expected_profiles, expected_rows, expected_duals = (
                    (21950,29523,20317) if scheme in ("lex","reverse")
                    else (17890,25032,21369))
                self.assertEqual(compiled["source_line_profile_count"],expected_profiles)
                self.assertEqual(compiled["distinct_sparse_right_profile_cylinder_rows"],expected_rows)
                self.assertEqual(compiled["distinct_source_line_AA_dual_rows"],expected_duals)
                self.assertTrue(compiled["independent_no_P3_left_generator"])
                result=independent_comparison(model,compiled)
                self.assertEqual(result["complete_W32_true_original_S"],s)
                self.assertTrue(result["independent_original_seven_census_confirmed"])
                self.assertTrue(result["J41_non_D6_source_multiset_contraction_exact"])
                self.assertTrue(result["J42_D6_original_line_named_dual_contraction_exact"])
                self.assertEqual(result["GF5_51_column_certified_floor_numerator"],
                                 sum(n*R3_CERTIFIED_FLOORS[k] for k,n in
                                     result["original_seven_classes"].items()))
                self.assertFalse(result["Root_A_proved"])

    def test_original_sixfactor_tensor_reuse_under_global_right_line_relabel(self):
        model=fixture(1,"S68")
        compiled=compile_incidence_tensor(model)
        right=list(model["right_labels"])
        right[0],right[1]=right[1],right[0]
        changed=dict(model)
        changed["right_labels"]=tuple(right)
        previous=contract_incidence_tensor(compiled,model["right_labels"])
        perturbed=contract_incidence_tensor(compiled,changed["right_labels"])
        control=independent_comparison(changed,compiled)
        self.assertEqual(previous["complete_W32_true_original_S"],68)
        self.assertEqual(perturbed["original_seven_classes"],
                         control["original_seven_classes"])
        self.assertTrue(perturbed["one_global_right_factor_assignment_shared_by_all_original_Q"])

    def test_true_W32_pinned_fiber_exact_two_coherent_states_guard(self):
        for scheme in ("S68","S72"):
            with self.subTest(scheme=scheme):
                row=coherent_right_fiber_tensor(scheme,states=2)
                self.assertEqual(row["actual_globally_injective_right_maps"],2)
                self.assertFalse(row["complete_24_state_global_fiber"])
                self.assertEqual(row["all_states"][0]["S"],{"S68":68,"S72":72}[scheme])
                self.assertEqual(row["exact_global_source_profile_coherence_gap"],
                                 row["exact_min_full_seven_S"]-
                                 row["sum_of_independent_right_source_profile_minima"])
                self.assertGreaterEqual(row["exact_global_source_profile_coherence_gap"],0)
                self.assertTrue(row["all_results_one_global_g_per_state"])
                self.assertTrue(row["greedy_profile_cover_exactly_covers_examined_global_states"])
                self.assertFalse(row["greedy_profile_cover_optimality_claimed"])
                self.assertEqual(sum(p["new_globally_legal_fiber_states_covered"]
                                     for p in row["greedy_all_global_states_positive_source_profile_cover"]),
                                 2)

    def test_fail_closed_input_global_injection_and_exact_population_budget(self):
        model=fixture(1,"S72")
        tensor=compile_incidence_tensor(model)
        with self.assertRaisesRegex(ValueError,"budget"):
            compile_incidence_tensor(model,max_original_candidates=1)
        with self.assertRaisesRegex(ValueError,"W32"):
            compile_incidence_tensor(fixture(2,"lex"))
        corrupt=list(model["right_labels"])
        corrupt[0]=corrupt[1]
        with self.assertRaisesRegex(ValueError,"globally injective"):
            contract_incidence_tensor(tensor,tuple(corrupt))
        with self.assertRaises(ValueError):
            contract_incidence_tensor(tensor,model["right_labels"][:-1])
        for bad in (0,-1,25,True):
            with self.subTest(states=bad):
                with self.assertRaises(ValueError):
                    coherent_right_fiber_tensor("S68",states=bad)
        with self.assertRaises(ValueError):
            coherent_right_fiber_tensor("lex",states=1)
        self.assertFalse(_connected_dual(((0,1),)*6))
        self.assertIsNone(source_multiplicity_type((0,0,0,1,2,3)))


if __name__=="__main__":
    unittest.main()
