"""Independent C22 original W32 joint seven-family and all-h mask tests."""
from collections import Counter
from itertools import combinations, combinations_with_replacement
from fractions import Fraction
import unittest

from hyp105_g5e2b3e1a_fixed_leading import PAIRS
from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS
from hyp105_g5e2b3e1c21d_adversarial_right import W32_LEX_RIGHT_ZERO_D6
from hyp105_g5e2b3e1c22_joint_seven_tensor import (
    EDGE_BITS, TAGS, six_edges_degree_two_by_parity,
    all_h_D6_one_global_right_transposition_influence,
    _column_dual_signature,_cycle6_connected,
    compile_original_W32_joint_source,counts_for_global_right_mapping,
    exact_joint_one_swap_neighborhood,
    independently_check_historical_full_W32_global_maps,
    _swap_g,
)


class C22OneGlobalRightJointTensorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.compiled=compile_original_W32_joint_source()
        cls.report=exact_joint_one_swap_neighborhood()

    def test_all_h_six_two_bit_masks_parity_iff_twofactor_bruteforce(self):
        # Independent direct six-coordinate degree oracle, including
        # repeated physical pairs (the ORIGINAL right B/C multiplicities).
        accepted=0
        for ids in combinations_with_replacement(range(15),6):
            edge_masks=tuple(EDGE_BITS[i] for i in ids)
            degrees=[0]*6
            for i in ids:
                u,v=PAIRS[i]
                degrees[u]+=1
                degrees[v]+=1
            expected=degrees==[2]*6
            got=six_edges_degree_two_by_parity(edge_masks)
            self.assertEqual(got,expected,msg=str(ids))
            accepted+=got
        # More than 70 simple factors because original line B/C repeats
        # can give physically repeated edges and a valid degree-two source.
        self.assertGreater(accepted,70)
        # Exact ALL-a mask identity also works on non-K6 symbols.
        simple=tuple((1<<i)|(1<<((i+1)%8)) for i in range(6))
        self.assertEqual(six_edges_degree_two_by_parity(simple),False)
        with self.assertRaises(ValueError):
            six_edges_degree_two_by_parity((1,)*6)

    def test_all_h_global_right_two_line_D6_influence(self):
        for s in (2,4,8,16,32,64,128):
            info=all_h_D6_one_global_right_transposition_influence(s)
            self.assertEqual(
                info["original_left_C6_with_two_swapped_right_lines_upper"],
                2*info["original_left_C6_with_one_fixed_right_line_upper"])
            self.assertLessEqual(info["D6_absolute_transposition_change_upper"],
                                 info["all_original_left_C6_upper"])
            self.assertTrue(info["not_positive_all_g_D6_or_seven_lower"])
        self.assertEqual(
            all_h_D6_one_global_right_transposition_influence(2)[
                "original_left_C6_with_two_swapped_right_lines_upper"],
            34992)
        for s in (0,1,3,True,9,"4"):
            with self.assertRaises(ValueError):
                all_h_D6_one_global_right_transposition_influence(s)

    def test_connected_dual_rejects_two_disjoint_triangles(self):
        from hyp105_g5e2b3e1a_fixed_leading import _two_factors_K6
        sigs=Counter()
        for graph in _two_factors_K6():
            index={p:i for i,p in enumerate(PAIRS)}
            sig=_column_dual_signature(tuple(EDGE_BITS[index[p]] for p in graph))
            sigs[_cycle6_connected(sig)]+=1
        self.assertEqual(sigs,{True:60,False:10})

    def test_all_original_62370_sixsets_and_one_global_baseline(self):
        c=self.compiled
        self.assertEqual(c["full_actual_original_sixsets"],62370)
        self.assertEqual(c["left_source_original_profiles"],
                         {"A":51030,"B":10935,"C":405})
        self.assertEqual(sum(c["original_candidate_class_profiles"].values()),
                         c["eligible_original_sixsets"])
        self.assertTrue(0<c["compressed_source_records"]<=
                        c["eligible_original_sixsets"]<=62370)
        self.assertEqual(sum(t[3] for t in c["records"]),
                         c["eligible_original_sixsets"])
        self.assertEqual(len(c["source_record_ids_touching_original_right_line"]),15)
        from hyp105_g5e2b3e1c21d_adversarial_right import W32_SEVEN_EXPECTED
        self.assertEqual(counts_for_global_right_mapping(
            c,W32_LEX_RIGHT_ZERO_D6),W32_SEVEN_EXPECTED)

    def test_incremental_one_global_right_exact_full_105(self):
        r=self.report
        self.assertEqual(r["source_actual_left_sixsets"],62370)
        self.assertEqual(r["one_swap_full_right_maps"],105)
        self.assertEqual(r["D6_histogram"],{0:40,1:29,2:24,3:6,4:4,5:1,9:1})
        self.assertEqual(sum(r["S_seven_histogram"].values()),105)
        self.assertTrue(r["all_h_swap_affected_original_right_lines_only"])
        self.assertTrue(r["not_global_all_h_seven_Omega_s6_or_ASET_bound"])
        self.assertTrue(r["not_full_15_factorial_right_search"])
        trials=r["all_105_exact_global_right_joint_profiles"]
        self.assertEqual(len(trials),105)
        # Independently re-derived by a second GF(2) W32 incidence
        # generator and full 62,370-source JavaScript oracle, not by
        # serializing this very Python implementation.
        self.assertEqual(r["source_eligible_seven_pattern_sixsets"],52309)
        self.assertEqual(r["source_compiled_weighted_records"],36272)
        self.assertEqual(r["minimum_S_seven_over_only_105_swaps"],122)
        self.assertEqual(r["minimum_GF5_necessary_numerator_over_only_105_swaps"],
                         5623340)
        winner=r["min_S_attaining_global_right_swap"]
        self.assertEqual(tuple(winner["swap_original_right_lines"]),(4,14))
        self.assertEqual(winner["S_seven"],122)
        self.assertEqual(winner["GF5_seven_necessary_numerator"],5623340)
        self.assertEqual(winner["seven_counts"],{
            "D6":0,"B-left/A-right":47,"A-left/B-right":57,
            "C/A":2,"C/B":0,"B/B-overlap":11,"B/B-disjoint":5,
        })
        self.assertEqual(r["min_GF5_attaining_global_right_swap"][
            "swap_original_right_lines"],(4,14))
        self.assertEqual(r["per_D6_level_exact_minima_over_only_105_swaps"][0][
            "min_S"],122)
        self.assertEqual(r["per_D6_level_exact_minima_over_only_105_swaps"][0][
            "min_GF5"],5623340)
        for trial in trials:
            self.assertEqual(sum(trial["seven_counts"].values()),trial["S_seven"])
            self.assertEqual(
                sum(R3_CERTIFIED_FLOORS[k]*v for k,v
                    in trial["seven_counts"].items()),
                trial["GF5_seven_necessary_numerator"])
            self.assertLessEqual(trial["source_records_with_changed_acceptance"],
                                 trial["source_records_touched"])
            self.assertLessEqual(trial["original_sixsets_with_changed_class"],
                                 r["source_eligible_seven_pattern_sixsets"])
        self.assertEqual(min(x["S_seven"] for x in trials),
                         r["minimum_S_seven_over_only_105_swaps"])
        self.assertEqual(min(x["GF5_seven_necessary_numerator"] for x in trials),
                         r["minimum_GF5_necessary_numerator_over_only_105_swaps"])
        for level,stat in r["per_D6_level_exact_minima_over_only_105_swaps"].items():
            eligible=[x for x in trials if x["seven_counts"]["D6"]==level]
            self.assertEqual(stat["min_S"],min(x["S_seven"] for x in eligible))
            self.assertEqual(stat["min_GF5"],
                             min(x["GF5_seven_necessary_numerator"]
                                 for x in eligible))

    def test_three_full_recounts_not_just_incremental(self):
        c=self.compiled
        trials=self.report["all_105_exact_global_right_joint_profiles"]
        for trial in (trials[0],trials[-1],
                      min(trials,key=lambda x:x["S_seven"])):
            i,j=trial["swap_original_right_lines"]
            actual=counts_for_global_right_mapping(
                c,_swap_g(W32_LEX_RIGHT_ZERO_D6,i,j))
            self.assertEqual(actual,trial["seven_counts"])

    def test_independent_historical_all_62370_and_weighted_BA_comparators(self):
        independent=independently_check_historical_full_W32_global_maps(self.report)
        self.assertGreaterEqual(len(independent),2)
        self.assertLessEqual(len(independent),4)
        self.assertTrue(all(x["historical_exact_all_62370_source_census_match"]
                            and x["independent_B_left_A_right_weighted_source_match"]
                            for x in independent))

    def test_right_coordinate_renaming_gauge_same_full_physical_map(self):
        c=self.compiled
        original=W32_LEX_RIGHT_ZERO_D6
        transformed=[]
        sigma=(1,0,3,2,5,4)
        edges_to_index={edge:i for i,edge in enumerate(PAIRS)}
        for idx in original:
            u,v=PAIRS[idx]
            transformed.append(edges_to_index[tuple(sorted((sigma[u],sigma[v])))])
        self.assertEqual(counts_for_global_right_mapping(c,original),
                         counts_for_global_right_mapping(c,tuple(transformed)))
        # A right ORIGINAL source-factor transposition commutes with
        # one uniform RIGHT physical coordinate renaming.
        trans=_swap_g(original,1,12)
        trans_gauge=[]
        for idx in trans:
            u,v=PAIRS[idx]
            trans_gauge.append(edges_to_index[
                tuple(sorted((sigma[u],sigma[v])))])
        self.assertEqual(counts_for_global_right_mapping(c,trans),
                         counts_for_global_right_mapping(c,trans_gauge))

    def test_invalid_incomplete_original_source_and_global_right_fail_closed(self):
        for cap in (0,1,62369,True,"62370",62370.0):
            with self.assertRaises(ValueError):
                compile_original_W32_joint_source(max_original_candidates=cap)
        for invalid in ((),tuple(range(14)),(0,)*15,
                        tuple(range(14))+(15,),
                        tuple(range(14))+(True,)):
            with self.assertRaises(ValueError):
                counts_for_global_right_mapping(self.compiled,invalid)
        with self.assertRaises(ValueError):
            independently_check_historical_full_W32_global_maps(
                self.report, maximum_full_census_checks=0)


if __name__=="__main__":
    unittest.main()
