"""Independent physical 2-root 2factor and genuine original W32 four-map Hessian tests."""
import unittest
from itertools import combinations, combinations_with_replacement
from collections import Counter
from math import comb,factorial

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4au_two_line_seven_hessian import (
    independent_doubly_rooted_K6_physical_multiset,
    every_original_two_line_seven_hessian_cap,
    genuine_original_W32_two_line_support,
    genuine_original_W32_signed_disjoint_swap_hessian,
    CANONICAL_DISJOINT_PAIRS,
)
from hyp105_g5e2b3e1a_fixed_leading import selected_left_six
from hyp105_g5e2b3e1b0_seven_signature import (
    classify_seven_prechecked, seven_census, R3_CERTIFIED_FLOORS,
)


class TrueOriginalTwoLineSevenHessianTests(unittest.TestCase):
    def test_01_all_5005_physical_twopins_symmetry_and_class_counts(self):
        pairs=tuple(combinations(range(6),2))
        profiles={(1,1,1,1,1,1):"A",(2,1,1,1,1):"B",(2,2,2):"C"}
        patterns=[]
        for multi in combinations_with_replacement(pairs,6):
            d=[0]*6
            for a,b in multi:
                d[a]+=1;d[b]+=1
            if d!=[2]*6:continue
            counts=Counter(multi)
            pattern=tuple(sorted(counts.values(),reverse=True))
            patterns.append((counts,profiles[pattern]))
        self.assertEqual(len(patterns),130)
        for e in pairs:
            # One fixed physical edge counted twice for a required SAME edge.
            same=Counter(ty for counts,ty in patterns if counts[e]>=2)
            self.assertEqual(same,{"B":3,"C":3})
            for other in pairs:
                if other==e:continue
                row=Counter(ty for counts,ty in patterns
                            if counts[e]>=1 and counts[other]>=1)
                if len(set(e)&set(other))==1:
                    self.assertEqual(row,{"A":7,"B":3})
                else:
                    self.assertEqual(row,{"A":14,"B":6,"C":1})
        self.assertEqual(independent_doubly_rooted_K6_physical_multiset(),
                         {"same":{"B":3,"C":3},
                          "adjacent":{"A":7,"B":3},
                          "disjoint":{"A":14,"B":6,"C":1}})

    def test_02_all_dyadic_exact_original_two_line_overlap_and_hessian_gates(self):
        for h in tuple(range(1,33))+(40,48,64,80):
            s=1<<h
            a=every_original_two_line_seven_hessian_cap(s)
            d=s+1
            target=24*d**4*(
                6*comb(a["a"]-2,4)
                +d*d*(10*comb(a["a"]-3,3)+21*comb(a["a"]-4,2)))
            self.assertEqual(a["actual_original_two_distinct_LINE_factor_sixQ_support_upper"],target)
            self.assertEqual(a["absolute_mixed_seven_S_Hessian_upper"],8*target)
            self.assertFalse(a["original_same_full_global_f_g_seven_lower_PROVED"])
            self.assertEqual(a["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
            if s>=4:
                self.assertLessEqual(a["absolute_mixed_seven_S_Hessian_upper"],43200*s**11)
                self.assertLessEqual(a["actual_original_two_distinct_LINE_factor_sixQ_support_upper"],5400*s**11)

    def test_03_real_original_W32_source_line_pair_source_C4free(self):
        for scheme in ("S68","S72","lex","reverse"):
            m=fixture(1,scheme)
            lines=[set() for _ in range(15)]
            for p,l in m["incidences"]:lines[l].add(p)
            self.assertEqual(len(m["incidences"]),45)
            for u,v in combinations(range(15),2):
                self.assertLessEqual(len(lines[u]&lines[v]),1)
            z=genuine_original_W32_two_line_support(scheme)
            self.assertEqual(z["genuine_original_left_candidate_Q"],62370)
            self.assertTrue(z["true_GQ_no_source_C4_verified"])
            c=every_original_two_line_seven_hessian_cap(2)
            for t in z["per_actual_source_line_pair"]:
                self.assertGreater(t["genuine_six_ID_Q_with_both_line_source_factors"],0)
                self.assertLessEqual(t["genuine_six_ID_Q_with_both_line_source_factors"],
                    c["actual_original_two_distinct_LINE_factor_sixQ_support_upper"])
                self.assertLessEqual(t["number_of_actual_shared_original_point_factors"],1)

    def test_04_actual_genuine_W32_S68_and_S72_disjoint_swaps_seven_GF5_Hessian(self):
        for scheme in ("S68","S72"):
            z=genuine_original_W32_signed_disjoint_swap_hessian(scheme)
            self.assertEqual(len(z["mixed_hessian_rows"]),len(CANONICAL_DISJOINT_PAIRS))
            self.assertEqual(z["actual_original_left_Q"],62370)
            self.assertTrue(z["original_global_source_line_pair_injective_all_four_states"])
            expected=68 if scheme=="S68" else 72
            for row in z["mixed_hessian_rows"]:
                self.assertEqual(row["seven_S_before"],expected)
                self.assertTrue(row["independent_sparse_true_Q_Hessian_agrees_with_four_full_maps"])
                self.assertEqual(sum(row["seven_per_tag_signed_Hessian"].values()),
                                 row["signed_mixed_seven_S_Hessian"])
                self.assertGreater(row["source_original_six_ID_Q_with_both_swap_source_support"],0)
                self.assertLessEqual(abs(row["signed_mixed_seven_S_Hessian"]),
                      2*row["source_original_six_ID_Q_with_both_swap_source_support"])

    def test_05_actual_genuine_W32_lex_reverse_mixed_Hessian_sign_and_weight(self):
        for scheme in ("lex","reverse"):
            z=genuine_original_W32_signed_disjoint_swap_hessian(scheme)
            h=259 if scheme=="lex" else 169
            deltas=[]
            for row in z["mixed_hessian_rows"]:
                self.assertEqual(row["seven_S_before"],h)
                self.assertEqual(
                    row["selected_GF5_weighted_necessary_numerator_Hessian"],
                    sum(row["seven_per_tag_signed_Hessian"][k]*w
                        for k,w in R3_CERTIFIED_FLOORS.items()))
                deltas.append(row["signed_mixed_seven_S_Hessian"])
            self.assertTrue(any(v!=0 for v in deltas))
            self.assertFalse(z["root_A_B_C"]=="PROVED_A")

    def test_06_exact_w32_global_coordinate_relabel_class_independent(self):
        for scheme in ("lex","S68"):
            model=fixture(1,scheme)
            inc=tuple(tuple(q) for q in model["incidences"])
            f=tuple(tuple(q) for q in model["left_labels"])
            g=tuple(tuple(q) for q in model["right_labels"])
            lf=lambda u:(u+1)%6
            rg=lambda u:(u+3)%6
            f2=tuple(tuple(sorted(lf(u) for u in e)) for e in f)
            g2=tuple(tuple(sorted(rg(u) for u in e)) for e in g)
            self.assertEqual(len(set(f2)),15)
            self.assertEqual(len(set(g2)),15)
            for ids,kind in selected_left_six(model):
                tag=classify_seven_prechecked(ids,f,g,inc)
                self.assertEqual(tag,classify_seven_prechecked(ids,f2,g2,inc))


if __name__=="__main__":
    unittest.main()
