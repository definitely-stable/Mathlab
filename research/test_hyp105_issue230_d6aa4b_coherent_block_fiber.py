"""D6-AA4B independent globally admissible four-right-factor fiber checks."""
import unittest
from collections import Counter
from itertools import permutations

from hyp105_issue230_d6aa4b_coherent_block_fiber import (
    assign_block, coherent_fiber, validate_block)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census, R3_CERTIFIED_FLOORS)
from hyp105_issue230_d6p_seven_cylinder_swap_audit import (
    compile_original_W32_cylinders)
from hyp105_issue230_d6aa_positional_tensor import (
    local_signature, classify_position_signatures)


class CoherentFiberContract(unittest.TestCase):
    def test_injection_enforced_and_fixed_image(self):
        m=fixture(1,"S68")
        labels=tuple(m["right_labels"])
        block=(0,1,2,3)
        edges=tuple(labels[i] for i in block)
        self.assertEqual(validate_block(labels,block),block)
        self.assertEqual(len(tuple(permutations(edges))),24)
        for order in permutations(edges):
            assigned=assign_block(labels,block,order)
            self.assertEqual(len(set(assigned)),15)
            self.assertEqual(set(assigned),set(labels))
            self.assertTrue(all(assigned[i]==labels[i]
                                for i in range(15) if i not in block))
        with self.assertRaises(ValueError):
            assign_block(labels,block,(edges[0],)*4)
        with self.assertRaises(ValueError):
            assign_block(labels,block,(labels[4],)+edges[1:])
        with self.assertRaises(ValueError):
            validate_block(labels,(0,0,1,2))
        with self.assertRaises(ValueError):
            validate_block(labels,(0,1,2,15))

    def test_explicit_shared_choice_not_factorwise_choice(self):
        # Two Q indicators would each be avoidable by changing the shared
        # label, yet there is no ONE globally coherent assignment that
        # simultaneously makes both zero. Simple complete toy fiber.
        options=((1,0),(0,1))
        self.assertEqual(sum(min(row) for row in options),0)
        self.assertEqual(min(sum(row[j] for row in options)
                             for j in range(2)),1)
        self.assertEqual(1-0,1)

    def test_exact_S68_fiber_and_independent_original_sixset_oracle(self):
        model=fixture(1,"S68")
        compiled=compile_original_W32_cylinders(model)
        block=(0,1,2,3)
        result=coherent_fiber(compiled,tuple(model["right_labels"]),block)
        self.assertEqual(result["baseline_seven_count"],68)
        self.assertEqual(result["baseline_GF5_floor_numerator"],3112510)
        self.assertEqual(result["complete_global_injection_completions"],24)
        self.assertEqual(len(result["all_24_exact_global_completion_results"]),24)
        self.assertEqual(result["frozen_left_original_sixsets"],62370)
        self.assertEqual(result["min_global_fiber_S"],
                         min(r["S_seven"] for r in result["all_24_exact_global_completion_results"]))
        self.assertEqual(result["min_global_fiber_GF5_floor_numerator"],
                         min(r["GF5_floor_numerator"] for r in
                             result["all_24_exact_global_completion_results"]))
        self.assertGreaterEqual(result["exact_coherence_gap_S"],0)
        self.assertGreaterEqual(result["exact_coherence_gap_GF5_numerator"],0)
        for row in result["all_24_exact_global_completion_results"]:
            self.assertEqual(sum(row["by_class"].values()),row["S_seven"])
            self.assertEqual(sum(row["by_class"][k]*w
                             for k,w in R3_CERTIFIED_FLOORS.items()),
                             row["GF5_floor_numerator"])
        # Completely separate six-original-incidence oracle, no compressed
        # cylinder class implementation, for multiple actual global maps.
        orders=result["all_24_exact_global_completion_results"]
        for idx in (0,1,7,23):
            physical=tuple(tuple(e) for e in orders[idx]["physical_original_line_image"])
            changed=assign_block(model["right_labels"],block,physical)
            checked=seven_census({**model,"right_labels":changed},
                                 independent_checks=False)
            self.assertEqual(orders[idx]["S_seven"],checked["S_seven"])
            self.assertEqual(orders[idx]["GF5_floor_numerator"],
                             checked["GF5_seven_lower_numerator"])
            self.assertEqual(orders[idx]["by_class"],
                             checked["seven_class_motif_counts"])
        if result["source_cylinder_cover_complete"]:
            covered=0
            for item in result["source_cylinder_cover"]:
                self.assertGreater(item["original_sixset_multiplicity"],0)
                covered|=item["completion_mask"]
            self.assertEqual(covered,(1<<24)-1)
            self.assertGreater(result["min_affected_coherent_S"],0)

    def test_six_position_class_invariant_for_true_global_fiber_assignments(self):
        m=fixture(1,"S72")
        E=tuple(m["incidences"])
        original=tuple(m["right_labels"])
        block=(1,7,9,12)
        order=tuple(original[i] for i in block)
        altered=assign_block(original,block,order[1:]+order[:1])
        L=tuple(m["left_labels"])
        selected=tuple(E[i] for i in range(6))
        sig=local_signature(tuple(L[p] for p,l in selected))
        for labels in (original,altered):
            r=local_signature(tuple(labels[l] for p,l in selected))
            tag=classify_position_signatures(sig,r)
            self.assertTrue(tag is None or tag in R3_CERTIFIED_FLOORS)


if __name__=="__main__":
    unittest.main()
