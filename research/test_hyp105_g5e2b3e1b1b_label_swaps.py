"""Independent falsification of complete W(3,2) right label-swap landscape."""
import unittest
from itertools import combinations

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1b0_seven_signature import (
    R3_CERTIFIED_FLOORS, seven_census,
)
from hyp105_g5e2b3e1b1b_label_swaps import (
    exact_swap_deltas, swap_line_pair_labels,
)


class CorrelatedRightLabelExchangeTests(unittest.TestCase):
    def test_all_105_exact_swaps_and_independent_full_oracle(self):
        base=pair_labeled_symplectic(1,"reverse-line")
        data=exact_swap_deltas(base)
        self.assertEqual(data["candidate_left_sixsets"],62370)
        self.assertEqual(data["base_S"],169)
        self.assertEqual(data["base_GF5_R3_floor_numerator"],7627209)
        self.assertEqual(len(data["all_105_swaps"]),105)
        self.assertEqual({tuple(x["swap"]) for x in data["all_105_swaps"]},
                         set(combinations(range(15),2)))
        self.assertEqual(data["best"]["new_S"],
                         min(x["new_S"] for x in data["all_105_swaps"]))
        self.assertEqual(data["exact_independent_best_verification"]["full_recount_S"],
                         data["best"]["new_S"])
        self.assertFalse(data["universal_asymptotic_counterexample"])
        self.assertFalse(data["full_R3_minimization"])

        # These three independent full recomputations do not use the
        # incremental touched-sixset delta formula. This is an
        # exhaustive exact full 62,370 original-candidate check each.
        checks={tuple(x["swap"]):x for x in data["all_105_swaps"]}
        for candidate in ((0,1),(2,9),(8,14)):
            changed=swap_line_pair_labels(base,*candidate)
            full=seven_census(changed,independent_checks=True)
            delta=checks[candidate]
            self.assertEqual(full["S_seven"],delta["new_S"])
            self.assertEqual(full["GF5_seven_lower_numerator"],
                             delta["new_GF5_R3_floor_numerator"])
            self.assertEqual(
                sum(R3_CERTIFIED_FLOORS[k]*n
                    for k,n in full["seven_class_motif_counts"].items()),
                delta["new_GF5_R3_floor_numerator"])

    def test_double_swap_involution_and_physical_pair_bijection(self):
        model=pair_labeled_symplectic(1,"reverse-line")
        switched=swap_line_pair_labels(model,3,10)
        reverted=swap_line_pair_labels(switched,3,10)
        self.assertEqual(reverted["right_labels"],model["right_labels"])
        self.assertEqual(reverted["supports"],model["supports"])
        self.assertEqual(len(set(switched["right_labels"])),15)
        self.assertNotEqual(model["right_labels"],switched["right_labels"])
        self.assertEqual(seven_census(reverted,independent_checks=False)["S_seven"],
                         169)
        for i,j in ((-1,1),(0,0),(14,15),(0,True),(False,3)):
            with self.assertRaises(ValueError):
                swap_line_pair_labels(model,i,j)

    def test_right_coordinate_gauge_does_not_change_exact_motif_count(self):
        model=pair_labeled_symplectic(1,"reverse-line")
        p=(3,5,0,2,4,1)
        other=dict(model)
        right=tuple(tuple(sorted(p[x] for x in edge))
                    for edge in model["right_labels"])
        other["right_labels"]=right
        a=model["a"]
        other["supports"]=tuple(tuple(sorted(
            model["left_labels"][pid] +
            tuple(a+z for z in right[line_id])))
            for pid,line_id in model["incidences"])
        prior=seven_census(model)
        gauge=seven_census(other)
        self.assertEqual(gauge["S_seven"],prior["S_seven"])
        self.assertEqual(gauge["Q4"],prior["Q4"])
        self.assertEqual(gauge["GF5_seven_lower"],prior["GF5_seven_lower"])


if __name__=="__main__":
    unittest.main()
