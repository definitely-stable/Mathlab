"""Independent all-W32 six-incidence fixed-label motif falsification."""
import unittest
from collections import Counter
from itertools import combinations

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1a_fixed_leading import (
    PAIRS, CASES, MIN_GF5, GF5_DENOM, classify_six,
    selected_left_six, finite_census, exact_witness_GF5,
    validated_small_model,
)


class FixedLabelLeadingW32Tests(unittest.TestCase):
    def test_left_enumerator_unique_complete_62370(self):
        model=pair_labeled_symplectic(1,"lex")
        counts=Counter()
        unique=set()
        for ids,kind in selected_left_six(model):
            self.assertEqual(len(ids),6)
            self.assertEqual(len(set(ids)),6)
            self.assertNotIn(ids,unique)
            unique.add(ids)
            counts[kind]+=1
        self.assertEqual(counts,Counter({"A":51030,"B":10935,"C":405}))
        self.assertEqual(len(unique),62370)

    def test_independent_ten_edge_bruteforce_agrees_with_selected_generator(self):
        """On every 6-subset of a witness-enriched TEN original columns.

        Uses raw original-incidence subsets, not the optimized physical
        projection constructors, to crosscheck absence of missed motifs.
        Witness enrichment is declared; NOT a full-family empirical rate.
        """
        model=pair_labeled_symplectic(1,"lex")
        full=finite_census(model,collect_sets=True)
        self.assertEqual(full["candidate_left_2factor_sets"],62370)
        observed=full["sets"]
        for name, ids in full["witnesses"].items():
            selected=list(ids)
            selected += [i for i in range(model["N"])
                         if i not in ids][:4]
            self.assertEqual(len(selected),10)
            for subset in combinations(selected,6):
                tag=classify_six(model,subset)
                self.assertEqual(tag,observed.get(tuple(sorted(subset))))
        self.assertEqual(set(full["new_motif_counts"]),set(CASES))
        self.assertEqual(sum(full["new_motif_counts"].values()),
                         len(observed))
        self.assertEqual(full["new_total_original_six_sets"],len(observed))

    def test_exact_full_GF5_ten_balanced_signed_events(self):
        for name in ("lex","reverse-line"):
            model=pair_labeled_symplectic(1,name)
            result=finite_census(model)
            self.assertGreater(result["new_total_original_six_sets"],0)
            self.assertEqual(result["candidate_left_2factor_sets"],62370)
            expected=sum(10*MIN_GF5[tag]*count for tag,count in
                         result["new_motif_counts"].items())
            self.assertEqual(result["GF5_exact_restricted_R3_lower_numerator"],
                             expected)
            self.assertEqual(result["GF5_exact_restricted_R3_lower"].numerator *
                             GF5_DENOM,
                             result["GF5_exact_restricted_R3_lower"].denominator *
                             expected)
            for tag,ids in result["witnesses"].items():
                cert=exact_witness_GF5(model,ids)
                self.assertEqual(cert["class"],tag)
                self.assertGreaterEqual(cert["min"],MIN_GF5[tag])
                self.assertGreater(cert["sum"],0)
                self.assertEqual(cert["GF5_positive_signed_events"],10)
            self.assertFalse(result["all_h_fixed_label_Omega_s6"])
            self.assertFalse(result["not_full_R3"] is False)

    def test_global_coordinate_permutation_gauge(self):
        original=pair_labeled_symplectic(1,"reverse-line")
        p=(1,3,5,0,2,4)
        rename=lambda e:tuple(sorted((p[e[0]],p[e[1]])))
        model=dict(original)
        model["left_labels"]=tuple(rename(e) for e in original["left_labels"])
        model["right_labels"]=tuple(rename(e) for e in original["right_labels"])
        a=finite_census(original)
        b=finite_census(model)
        self.assertEqual(a["new_motif_counts"],b["new_motif_counts"])
        self.assertEqual(a["GF5_exact_restricted_R3_lower_numerator"],
                         b["GF5_exact_restricted_R3_lower_numerator"])

    def test_reject_noninjective_and_non_w32(self):
        model=pair_labeled_symplectic(1,"lex")
        bad=dict(model)
        bad["left_labels"]=(model["left_labels"][0],)*15
        with self.assertRaises(ValueError):
            validated_small_model(bad)
        with self.assertRaises(ValueError):
            finite_census(pair_labeled_symplectic(2,"lex"))
        with self.assertRaises(ValueError):
            classify_six(model,[0,0,1,2,3,4])
        with self.assertRaises(ValueError):
            classify_six(model,[0,1,2,3,4,45])


if __name__=="__main__":
    unittest.main()
