"""Independent exact original-source 45-column GF5 full-R3 descent tests."""
from fractions import Fraction
import unittest

from hyp105_w32_sevenclass_global_deterministic_gf5_referee import (
    true_original_w32_seven_hypergraph,
)
from hyp105_w32_complete_r3_triple_sum_referee import (
    committed_sevenclass_indices,true_original_source_vectors,
    _sums_by_cardinality,full_original_r3_triple_hash_census,
)
from hyp105_w32_exact_triple_sum_local_repair_referee import (
    _replacement_source_vector,
    _collision_owners,
    exact_one_original_source_palette_repair,
    deterministic_full_original_45flag_repair,
    repair_saved_full_W32_certificates,
)


class OriginalW32ExactCompleteGF5Repair(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source={s:true_original_w32_seven_hypergraph(s)
                    for s in ("lex","reverse-line")}
        cls.original=committed_sevenclass_indices()

    def test_all_real_source_target_palettes_are_nonzero_checksum4(self):
        for scheme,family in self.source.items():
            original=self.original[scheme]
            vec=true_original_source_vectors(family["source"],original)
            for source_id in (0,3,7,17,32,44):
                with self.subTest(scheme=scheme,id=source_id):
                    self.assertEqual(
                        _replacement_source_vector(
                            family["source"],source_id,original[source_id]),
                        vec[source_id])
                    for t in range(51):
                        v=_replacement_source_vector(family["source"],source_id,t)
                        self.assertEqual(sum(v)%5,4)
                        self.assertEqual(sum(bool(x) for x in v),4)
                        self.assertEqual(len(v),12)

    def test_one_variable_cross_repair_is_mathematically_exact(self):
        for scheme,family in self.source.items():
            current=self.original[scheme]
            before=_sums_by_cardinality(
                true_original_source_vectors(family["source"],current),3)[1]
            self.assertEqual(before,7 if scheme=="lex" else 4)
            owners=_collision_owners(
                true_original_source_vectors(family["source"],current))
            self.assertGreater(len(owners),0)
            self.assertTrue(all(0<=i<45 for i in owners))
            changed_any=False
            for source_id in owners[:5]:
                z=exact_one_original_source_palette_repair(
                    family["source"],current,source_id)
                self.assertTrue(z["all_51_candidates_checked"])
                self.assertGreaterEqual(z["improvement"],0)
                after=_sums_by_cardinality(
                    true_original_source_vectors(family["source"],z["indices"]),3)[1]
                self.assertEqual(after,before-z["improvement"])
                if z["changed"]:
                    changed_any=True
                    self.assertLess(after,before)
            self.assertTrue(changed_any)

    def test_saved_original_45_flag_full_R3_strict_descent_and_independent_census(self):
        results=repair_saved_full_W32_certificates()
        self.assertEqual(set(results),{"lex","reverse-line"})
        for scheme,family in self.source.items():
            with self.subTest(scheme=scheme):
                z=results[scheme]
                self.assertEqual(z["previous_equal_triple_pairs"],
                                 7 if scheme=="lex" else 4)
                self.assertLessEqual(z["final_equal_triple_pairs"],
                                     z["previous_equal_triple_pairs"])
                self.assertEqual(len(z["final_complete_original_45_flag_palette_indices"]),45)
                verified=full_original_r3_triple_hash_census(
                    family["source"],
                    z["final_complete_original_45_flag_palette_indices"],
                    leading_original_sixsets=(m["ids"] for m in family["motifs"]))
                self.assertEqual(
                    z["independently_checked_true_full_R3"],
                    verified["FULL_original_distinct_sixflag_3v3_signed_events"])
                self.assertEqual(
                    z["full_0_to_3_original_subset_sums_unique"],
                    verified["all_45_original_source_0_to_3_subset_sums_unique"])
                self.assertEqual(z["exact_global_zero_0_to_3_achieved"],
                                 z["final_equal_triple_pairs"]==0)
                self.assertFalse(z["no_asymptotic_claim"] is False)

    def test_strict_fail_closed_source_and_budget_cases(self):
        m=self.source["lex"]["source"]
        c=self.original["lex"]
        for idx,pal in ((-1,0),(45,0),(0,-1),(0,51),(0,1.0)):
            with self.assertRaises(ValueError):
                _replacement_source_vector(m,idx,pal)
        with self.assertRaises(ValueError):
            exact_one_original_source_palette_repair(m,c[:44],0)
        with self.assertRaises(ValueError):
            deterministic_full_original_45flag_repair(m,c,max_sweeps=-1)
        with self.assertRaises(ValueError):
            deterministic_full_original_45flag_repair(m,c,max_sweeps=1.5)


if __name__=="__main__":
    unittest.main()
