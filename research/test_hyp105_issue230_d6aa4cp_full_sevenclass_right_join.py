"""AA4-CP independent true-original accepted historical GF5 sevenclass W32/W34."""
import unittest

from hyp105_issue230_d6aa4cp_full_right_original_sevenclass_join import (
    CLASS_NAMES,WEIGHTS,full_original_sevenclass_right_join,
    independent_W32_sevenclass_reference,
)
from hyp105_issue230_projection import fixture


class AA4CPExactOriginalAllSevenJoin(unittest.TestCase):
    def _reference_W32(self,scheme):
        original=fixture(1,scheme)
        optimized=full_original_sevenclass_right_join(original,timeout_seconds=120)
        reference=independent_W32_sevenclass_reference(original)
        self.assertEqual(optimized["seven_class_motif_counts"],reference["counts"])
        self.assertEqual(optimized["S_unweighted"],reference["S"])
        self.assertEqual(optimized["W_weighted"],reference["W"])
        self.assertEqual((optimized["s"],optimized["V"],optimized["a"]),(2,15,6))
        self.assertEqual(optimized["physical_sixpalettes"],1)
        self.assertGreater(optimized["right_source_Q_candidate_completions_tested"],0)
        self.assertTrue(optimized["one_full_original_source_incidence_host"])
        print("AA4CP_ORIGINAL_W32_ORACLE",scheme,optimized,flush=True)

    def test_01_true_original_W32_lex_all7_vs_completely_independent_left_oracle(self):
        self._reference_W32("lex")

    def test_02_true_original_W32_S72_all7_vs_completely_independent_left_oracle(self):
        self._reference_W32("S72")

    def test_03_true_original_W34_full_historical_all7_lex(self):
        original=fixture(2,"lex")
        z=full_original_sevenclass_right_join(original,timeout_seconds=1500)
        self.assertEqual((z["s"],z["V"],z["a"]),(4,85,14))
        self.assertEqual(z["physical_sixpalettes"],3003)
        self.assertGreater(z["right_line_A_patterns"],0)
        self.assertGreater(z["right_line_B_patterns"],0)
        self.assertGreater(z["right_line_C_patterns"],0)
        self.assertEqual(z["S_unweighted"],sum(z["seven_class_motif_counts"].values()))
        self.assertGreater(z["S_unweighted"],0)
        print("AA4CP_TRUE_W34_FULL_ALL7_LEX",z,flush=True)

    def test_04_true_original_W34_full_historical_all7_random(self):
        original=fixture(2,"random")
        z=full_original_sevenclass_right_join(original,timeout_seconds=1500)
        self.assertEqual((z["s"],z["V"],z["a"]),(4,85,14))
        self.assertEqual(z["physical_sixpalettes"],3003)
        self.assertGreater(z["S_unweighted"],0)
        self.assertGreater(z["W_weighted"],0)
        print("AA4CP_TRUE_W34_FULL_ALL7_RANDOM",z,flush=True)

    def test_05_original_W38_failclosed_scope_and_acceptance_registry(self):
        with self.assertRaises(ValueError):
            full_original_sevenclass_right_join(fixture(3,"lex"),timeout_seconds=1)
        self.assertEqual(len(CLASS_NAMES),7)
        self.assertEqual(WEIGHTS,(5643,45600,45600,43320,49050,51750,45010))
        with self.assertRaises(ValueError):
            full_original_sevenclass_right_join(fixture(1,"lex"),timeout_seconds=0)
        with self.assertRaises(ValueError):
            full_original_sevenclass_right_join(fixture(1,"lex"),timeout_seconds=True)


if __name__=="__main__":
    unittest.main()
