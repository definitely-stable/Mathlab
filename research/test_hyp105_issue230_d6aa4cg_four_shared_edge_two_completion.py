"""Independent AA4-CG original eightpacket 4-edge dual completion proof oracles."""
import unittest
from collections import Counter
from itertools import combinations

from hyp105_issue230_d6aa4cg_four_shared_edge_two_completion import (
    CUBE, FAMILIES, SHARED_MASK,
    _regular6, classify_four_common_completion, physical_overlapping_eight_masks,
    mixed_8cube_gram, genuine_W34_eightpacket_witness,
    genuine_W34_original_pair_eight_cube,
    classify_seven_all_a_original_Q,
)
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bq_all_seven_reverse_switching import (
    apply_disjoint_factor_swaps,
)
from hyp105_issue230_d6aa4by_original_independent_2factor_kernel import (
    physical_right_is_six_vertex_two_regular,
)

K7=tuple(combinations(range(7),2))


class TestAA4CGTrueOriginalEightpacket(unittest.TestCase):
    def test_01_exhaustive_K7_independent_ALL_four_edge_graphs_and_two_completions(self):
        """5985 K7 four-edge sets × 136 candidate exclusive two-edge sets.

        Independent literal edge degree census, THEN compare to separate
        dichotomy classifier for ALL distinct viable completion pairs.
        """
        cases=Counter()
        common_with_some=0
        for F in combinations(K7,4):
            residual=[e for e in K7 if e not in F]
            solutions=[]
            for E in combinations(residual,2):
                deg=Counter(v for edge in F+E for v in edge)
                direct=(len(deg)==6 and all(z==2 for z in deg.values()))
                self.assertEqual(direct,_regular6(F+E))
                if direct:solutions.append(E)
            if solutions:common_with_some+=1
            for A,B in combinations(solutions,2):
                if set(A)&set(B):continue
                case=classify_four_common_completion(F,A,B)
                independent_support=len({v for e in F for v in e})
                expected={5:"vertex_replacement",6:"four_cycle_switch"}[independent_support]
                self.assertEqual(case,expected)
                cases[case]+=1
        self.assertEqual(common_with_some,3360)
        self.assertEqual(cases["vertex_replacement"],1470)
        self.assertEqual(cases["four_cycle_switch"],3150)
        self.assertEqual(sum(cases.values()),4620)
        print("AA4CG_EXHAUSTIVE_K7",
              "common_fours_with_completion",common_with_some,
              "true_two_completion_cases",dict(cases),flush=True)

    def test_02_nonvacuous_fully_original_W34_both_dichotomy_cases_all_256(self):
        """Real W(3,4), 85 POINT and 85 LINE source factors, 425 flags."""
        for kind in ("four_cycle_switch","vertex_replacement"):
            z=genuine_W34_original_pair_eight_cube(kind)
            self.assertEqual(z["source_W34_original_s"],4)
            self.assertEqual(z["original_LINE_factor_count"],85)
            QA,QB=z["genuine_original_distinct_QA_QB"]
            self.assertEqual(len(QA),6)
            self.assertEqual(len(QB),6)
            self.assertEqual(len(set(QA)),6)
            self.assertEqual(len(set(QB)),6)
            self.assertEqual(len(set(QA)&set(QB)),4)
            self.assertGreater(z["physical_8cube_A_active"],0)
            self.assertGreater(z["physical_8cube_B_active"],0)
            self.assertGreater(z["true_original_both_physical_joint"],0)
            self.assertEqual(
                z["independent_true_original_joint_classification"],
                {kind:z["true_original_both_physical_joint"]})
            self.assertIn("historical_GF5_original_center_QA",z)
            self.assertIn("historical_GF5_original_center_QB",z)
            self.assertGreaterEqual(z["GF5_joint_historical_positive_maps"],0)
            print("AA4CG_TRUE_W34",kind,
                  "A_active",z["physical_8cube_A_active"],
                  "B_active",z["physical_8cube_B_active"],
                  "physical_both",z["true_original_both_physical_joint"],
                  "GF5_both_positive",z["GF5_joint_historical_positive_maps"],
                  "GF5_center_A",z["historical_GF5_original_center_QA"],
                  "GF5_center_B",z["historical_GF5_original_center_QB"],flush=True)

    def test_03_256_map_mixed_Gram_independent_literal_true_original_Q_oracle(self):
        for kind in ("four_cycle_switch","vertex_replacement"):
            model,pairs,source=genuine_W34_eightpacket_witness(kind)
            s,V,a,inc,f,g,_,_=_original_source(model)
            mask=physical_overlapping_eight_masks(g,pairs)
            J=mixed_8cube_gram(mask)
            self.assertGreater(J["same_four_positive_pairs"],0)
            self.assertEqual(J["J"][0][0],
                sum(mask["A"][x]*mask["B"][x] for x in range(CUBE)))
            literal=0
            for x in range(CUBE):
                changed=apply_disjoint_factor_swaps(
                    g,pairs,tuple(j for j in range(8) if x>>j&1))
                right=[]
                for fam in ("A","B"):
                    Q=source["Q"+fam]
                    physical=physical_right_is_six_vertex_two_regular(Q,inc,changed)
                    right.append(int(physical))
                    self.assertEqual(int(physical),mask[fam][x])
                literal+=right[0]*right[1]
            self.assertEqual(literal,J["J"][0][0])
            # Other orientation offsets must NOT be spuriously tied to same
            # four shared source LINE factors.
            for t,u in ((0,0),(1,1),(3,7),(15,15),(63,63),(13,44)):
                shifted=0
                for x in range(CUBE):
                    liftA=sum(1<<k for i,k in enumerate(FAMILIES["A"])
                              if (t>>i)&1)
                    liftB=sum(1<<k for i,k in enumerate(FAMILIES["B"])
                              if (u>>i)&1)
                    shifted+=mask["A"][x^liftA]*mask["B"][x^liftB]
                self.assertEqual(shifted,J["J"][t][u])

    def test_04_exact_old_W32_historic_seven_classifier_full_source_Q_equivalence(self):
        """Independent ALL 62370 source six-incidence Q versus pinned W32 helper.

        This is mandatory evidence before reusing the algebraic seven
        class definition on genuine W34 with a larger physical alphabet.
        """
        from hyp105_issue230_projection import fixture
        from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
        from hyp105_g5e2b3e1b0_seven_signature import classify_seven_prechecked
        from hyp105_g5e2b3e1b0_seven_signature import R3_CERTIFIED_FLOORS
        for scheme in ("lex","S72"):
            model=fixture(1,scheme)
            s,V,a,inc,f,g,_,_=_original_source(model)
            seen=0;hist=Counter()
            for Q,source_kind in selected_left_six(model):
                reference=classify_seven_prechecked(Q,f,g,inc)
                actual=classify_seven_all_a_original_Q(Q,f,g,inc)
                self.assertEqual(actual,reference)
                if actual is not None:
                    self.assertIn(actual,R3_CERTIFIED_FLOORS)
                    hist[actual]+=1
                seen+=1
            self.assertEqual(seen,62370)
            print("AA4CG_W32_GENERALIZED_GF5_EQUIVALENCE",
                  scheme,seen,dict(hist),flush=True)

    def test_05_invalid_and_two_extra_edge_swaps_forbidden(self):
        F=((0,1),(1,2),(2,3),(3,4))
        A=((4,5),(0,5))
        B=((4,6),(0,6))
        self.assertEqual(classify_four_common_completion(F,A,B),
                         "vertex_replacement")
        self.assertEqual(classify_four_common_completion(
            ((0,1),(1,2),(3,4),(4,5)),
            ((0,5),(2,3)),((0,3),(2,5))),"four_cycle_switch")
        self.assertEqual(classify_four_common_completion(
            F,((4,5),(0,5)),((4,7),(1,7))),"not_both")
        for args in [
            (F[:3],A,B),(F,A[:1],B),
            (F,A,((4,6),(4,6))),
            (F,A,((0,5),(4,6))),
            (((0,0),)+F[1:],A,B)
        ]:
            with self.assertRaises(ValueError):
                classify_four_common_completion(*args)
        model,pairs,src=genuine_W34_eightpacket_witness("vertex_replacement")
        g=model["right_labels"]
        with self.assertRaises(ValueError):
            physical_overlapping_eight_masks(g,pairs[:7])
        with self.assertRaises(ValueError):
            physical_overlapping_eight_masks(g,
                ((0,1),(1,2))+pairs[2:])
        bad=list(g);bad[0]=bad[1]
        with self.assertRaises(ValueError):
            physical_overlapping_eight_masks(bad,pairs)


if __name__=="__main__":unittest.main()
