"""Independent finite checks of incidence-matching aligned all-h no-go."""
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3b2_coincident_cycles import (
    physical_six_cycles, exact_coincident_c6, independent_brute_small_incidence,
)
from hyp105_g5e2b3b3_incidence_nogo import (
    forced_sixcycles_lower, canonical_incidence_perfect_matching,
    incidence_matched_labeling,
)


def direct_GF5_alternating_witness(model, column_ids):
    a = model["a"]
    coordinate_sum=[0]*(2*a)
    for j,eid in enumerate(column_ids):
        p,l=model["incidences"][eid]
        for i in model["left_labels"][p]:
            coordinate_sum[i] += 1 if j%2==0 else -1
        for i in model["right_labels"][l]:
            coordinate_sum[a+i] += 1 if j%2==0 else -1
    return all(x%5==0 for x in coordinate_sum)


class IncidencePerfectMatchingNoGoTests(unittest.TestCase):
    def test_all_h_explicit_union_bound_and_minimal_pair_alphabet(self):
        result2=forced_sixcycles_lower(2)
        result4=forced_sixcycles_lower(4)
        self.assertEqual(result2["a"],6)
        self.assertEqual(result2["missing_pairs"],0)
        self.assertEqual(result2["unconditional_C6_lower"],60)
        self.assertEqual(result4["a"],14)
        self.assertEqual(result4["missing_pairs"],6)
        self.assertEqual(result4["all_Ka_C6"],180180)
        self.assertEqual(result4["C6_containing_given_pair"],11880)
        self.assertEqual(result4["unconditional_C6_lower"],108900)
        for s in (2,4,8,16,32):
            result=forced_sixcycles_lower(s)
            self.assertGreater(result["unconditional_C6_lower"],0)
            self.assertLess(result["missing_pairs"],result["a"]-1)
            self.assertEqual(
                result["fixed_label_R3_lower_numerator"],
                5643*result["unconditional_C6_lower"])
            self.assertFalse(result["excludes_all_correlated_labels"])
        with self.assertRaises(ValueError):
            forced_sixcycles_lower(3)

    def test_geometry_incidence_perfect_matching_and_cycle_injection_GF2(self):
        base=pair_labeled_symplectic(1,"lex")
        pi=canonical_incidence_perfect_matching(base)
        self.assertEqual(set(pi),set(range(base["v"])))
        incidences=set(base["incidences"])
        self.assertTrue(all((p,l) in incidences
                            for l,p in enumerate(pi)))
        aligned=incidence_matched_labeling(base)
        self.assertEqual(len(set(aligned["right_labels"])),base["v"])
        self.assertEqual(
            aligned["right_labels"],
            tuple(base["left_labels"][pi[l]] for l in range(base["v"])))
        actual=exact_coincident_c6(aligned)
        left_cycle_count=sum(1 for _ in physical_six_cycles(
            base["left_labels"],base["a"]))
        self.assertEqual(left_cycle_count,60)
        self.assertEqual(actual["exact_coincident_C6_factor_matchings_D"],69)
        self.assertGreaterEqual(
            actual["exact_coincident_C6_factor_matchings_D"],left_cycle_count)
        for witness in actual["witness_column_ids_in_canonical_left_cycle_order"]:
            self.assertTrue(direct_GF5_alternating_witness(aligned,witness))
        # Direct subset oracle must agree with the join even when the
        # special matched incidence columns are included.
        pi_inverse={p:l for l,p in enumerate(pi)}
        six_points=next(physical_six_cycles(base["left_labels"],base["a"]))
        ix={pair:i for i,pair in enumerate(base["incidences"])}
        aligned_ids=[ix[(p,pi_inverse[p])] for p in six_points]
        self.assertEqual(len(set(aligned_ids)),6)
        chosen=aligned_ids + [i for i in range(base["N"])
                              if i not in aligned_ids][:6]
        sample=dict(aligned)
        sample["incidences"]=tuple(base["incidences"][i] for i in chosen)
        sample["N"]=len(chosen)
        self.assertEqual(
            independent_brute_small_incidence(sample)["D"],
            exact_coincident_c6(sample)["exact_coincident_C6_factor_matchings_D"])

    def test_GF4_exact_count_at_least_mathematical_s9_bound(self):
        base=pair_labeled_symplectic(2,"lex")
        aligned=incidence_matched_labeling(base)
        actual=exact_coincident_c6(aligned)
        bound=forced_sixcycles_lower(4)
        self.assertEqual(actual["left_physical_C6_cycles_examined"],121320)
        self.assertEqual(actual["exact_coincident_C6_factor_matchings_D"],157251)
        self.assertGreaterEqual(actual["exact_coincident_C6_factor_matchings_D"],
                                121320)
        self.assertGreaterEqual(
            actual["exact_coincident_C6_factor_matchings_D"],
            bound["unconditional_C6_lower"])
        self.assertFalse(actual["new_ASET_exponent_proved"])


if __name__=="__main__":
    unittest.main()
