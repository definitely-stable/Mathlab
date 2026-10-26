"""AA4-K32R2: accepted-GF5 radius-two exclusion on TRUE W(3,4) original flags."""
import unittest
from itertools import combinations

from hyp105_saturated_k32_original_sixset_radius2 import (
    genuine_W34_protected_k32_radius_two,
)


class TestSaturatedK32OriginalSixsetRadius2(unittest.TestCase):
    def test_genuine_original_W34_sharp_two_source_flag_replacement(self):
        report=genuine_W34_protected_k32_radius_two()
        self.assertEqual((report["s"],report["V"],report["a"]),(4,85,14))
        self.assertEqual(report["old_saturated_K32_triangles"],1)
        self.assertEqual(report["old_primary_K32_edges"],6)
        self.assertEqual(report[
            "old_opposite_parity_companion_matching_edges"],6)
        self.assertEqual(report["old_original_GF5_seven_tag"],None)
        self.assertEqual(report["old_ordinary_C6"],0)
        self.assertEqual(report["new_ordinary_C6"],2)
        self.assertEqual(report["new_accepted_original_D6"],2)
        self.assertEqual(
            report["one_flag_substitution_candidates_checked"],
            6*(425-6))
        self.assertEqual(report["one_flag_substitution_accepted"],0)
        self.assertEqual(
            len(report["sharp_accepted_original_D6_two_replacements"]),2)
        sig=report["old_original_sixset_coordinate_signature"]
        self.assertEqual(sig["point_label_coordinate_symbols"],5)
        self.assertEqual(sig["line_label_coordinate_symbols"],5)
        self.assertEqual(sig["point_label_coordinate_degrees"],
                         (2,2,2,3,3))
        self.assertEqual(sig["line_label_coordinate_degrees"],
                         (2,2,2,3,3))
        self.assertFalse(sig["GF5_six_coordinate_two_regular_necessary"])
        self.assertTrue(report[
            "all_distinct_original_point_and_line_factors"])
        self.assertTrue(report[
            "paired_source_original_diagonals_checked"])
        self.assertTrue(report[
            "all_h_one_flag_accepted_GF5_compensation_excluded"])
        self.assertFalse(report["all_h_root_sevenclass_Omega_s6_proved"])

    def test_generic_coordinate_K32_radius_one_impossible(self):
        # Independent pure-label audit of the ALL-h degree argument.
        # The two 3-valent vertices are nonadjacent in K3,2, so a
        # ONE-edge replacement cannot lower both their degrees.
        H=(0,1,2)
        Z=(3,4)
        edges=tuple((u,v) for u in H for v in Z)
        self.assertEqual(len(edges),6)
        all_pairs=tuple(combinations(range(14),2))
        count=0
        for missing in edges:
            for replacement in all_pairs:
                if replacement in edges:
                    continue
                chosen=tuple(edge for edge in edges if edge!=missing)+(
                    replacement,)
                degrees={}
                for a,b in chosen:
                    degrees[a]=degrees.get(a,0)+1
                    degrees[b]=degrees.get(b,0)+1
                self.assertFalse(
                    len(degrees)==6 and set(degrees.values())=={2})
                count+=1
        self.assertEqual(count,6*(91-6))

    def test_two_edge_replacement_can_form_true_six_coordinate_cycle(self):
        old=tuple((u,v) for u in range(3) for v in (3,4))
        choices=(
            ((0,3),(1,4)),
            ((0,4),(1,3)),
        )
        for discarded in choices:
            remaining=set(old)-set(discarded)
            remaining.update(((0,5),(1,5)))
            degrees={}
            for a,b in remaining:
                degrees[a]=degrees.get(a,0)+1
                degrees[b]=degrees.get(b,0)+1
            self.assertEqual(len(remaining),6)
            self.assertEqual(len(degrees),6)
            self.assertEqual(set(degrees.values()),{2})


if __name__=="__main__":
    unittest.main()
