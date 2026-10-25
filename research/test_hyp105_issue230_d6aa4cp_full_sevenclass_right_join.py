"""AA4-CP independent true-original accepted historical GF5 sevenclass W32/W34."""
import unittest

from hyp105_issue230_d6aa4cp_full_right_original_sevenclass_join import (
    CLASS_NAMES,WEIGHTS,full_original_sevenclass_right_join,
    independent_W32_sevenclass_reference,swap_actual_original_GQ_dual,
    assert_genuine_original_dual_swap_sevenclass_involution,
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

    def _independent_full_W34_dual_falsifier(self,original,scheme):
        from collections import Counter
        from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
        from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
            classify_seven_all_a_original_Q)
        _,_,_,inc,f,g,_,_=_original_source(original)
        z=full_original_sevenclass_right_join(original,timeout_seconds=1500,
                                              dump_physical_Q=True)
        mirror=full_original_sevenclass_right_join(
            swap_actual_original_GQ_dual(original),timeout_seconds=1500,
            dump_physical_Q=True)
        self.assertTrue(assert_genuine_original_dual_swap_sevenclass_involution(z,mirror))
        qa=set(z["physical_Q_ID_sets"])
        qb=set(mirror["physical_Q_ID_sets"])
        self.assertEqual(len(qa),z["BOTH_physical_Q"])
        self.assertEqual(len(qb),mirror["BOTH_physical_Q"])
        self.assertEqual(qa,qb,"entire original W34 BOTH physical source-sixflag Q must be same under typed GQ dual")
        def physically_valid(q):
            from collections import Counter
            left=Counter(v for j in q for v in f[inc[j][0]])
            right=Counter(v for j in q for v in g[inc[j][1]])
            return (len(q)==6 and len(set(q))==6 and len(left)==len(right)==6
                    and set(left.values())==set(right.values())=={2})
        self.assertTrue(all(physically_valid(q) for q in qa))
        independent=Counter(classify_seven_all_a_original_Q(q,f,g,inc) for q in qa)
        accepted={k:independent[k] for k in CLASS_NAMES}
        self.assertEqual(accepted,z["seven_class_motif_counts"])
        self.assertEqual(sum(accepted.values()),z["S_unweighted"])
        self.assertEqual(sum(accepted[k]*w for k,w in zip(CLASS_NAMES,WEIGHTS)),
                         z["W_weighted"])
        self.assertEqual(z["physical_sixpalettes"],3003)
        self.assertEqual((z["s"],z["V"],z["a"]),(4,85,14))
        self.assertEqual(len(qa),sum(z["BOTH_physical_by_RIGHT_source"].values()))
        expected={
            "lex":{
                "D6":8481,"B-left/A-right":181793,
                "A-left/B-right":171203,"C/A":22913,"C/B":3973,
                "B/B-overlap":22111,"B/B-disjoint":23051},
            "random":{
                "D6":7295,"B-left/A-right":164462,
                "A-left/B-right":162557,"C/A":20351,"C/B":4356,
                "B/B-overlap":24168,"B/B-disjoint":18222},
        }[scheme]
        self.assertEqual(z["seven_class_motif_counts"],expected)
        self.assertEqual((z["S_unweighted"],z["W_weighted"],
                          z["BOTH_physical_Q"]),
                         {"lex":(433525,19513712453,1036770),
                          "random":(401411,18119365425,981639)}[scheme])
        self.assertGreater(z["right_line_A_patterns"],0)
        self.assertGreater(z["right_line_B_patterns"],0)
        self.assertGreater(z["right_line_C_patterns"],0)
        print("AA4CP_FULL_TRUE_ORIGINAL_W34",scheme,
              {k:v for k,v in z.items() if k!="physical_Q_ID_sets"},
              "DUAL", {k:v for k,v in mirror.items() if k!="physical_Q_ID_sets"},
              "INDEPENDENT_HISTORIC_REAL_Q",dict(independent),flush=True)
        return z

    def test_03_true_original_W34_full_historical_all7_lex(self):
        self._independent_full_W34_dual_falsifier(fixture(2,"lex"),"lex")

    def test_04_true_original_W34_full_historical_all7_random(self):
        self._independent_full_W34_dual_falsifier(fixture(2,"random"),"random")

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
