"""HYP-105 #230 AA4-K32ZERO genuine source-only zero-extension falsifiers."""
from itertools import combinations
import unittest

from hyp105_full_physical_degree_tail import genuine_source,physical
from hyp105_k32_saturated_unit_multiplicity import (
    real_W34_two_disjoint_saturated_blocks,
    saturated_bipartite_k32_list,
)
from hyp105_saturated_fresh_extension_zero_w34 import (
    ZERO_OTHER_LINE_PAIR_PERMUTATION,
    source_incidence_rectangle_counts,
    true_W34_same_selected_zero_vs_positive_fresh_mass,
)


class TestSaturatedFreshZeroW34(unittest.TestCase):
    def test_exact_same_selected_graph_zero_vs_positive_extension(self):
        r=true_W34_same_selected_zero_vs_positive_fresh_mass()
        self.assertEqual((r["s"],r["V"],r["original_source_incidence_flags"]),
                         (4,85,425))
        self.assertEqual(r["selected_source_ID_count"],12)
        self.assertEqual(r["same_saturated_selected_K32_blocks"],2)
        self.assertEqual(r["selected_ordinary_C6_both"],0)
        self.assertTrue(r["globally_injected_point_pair_labels_identical"])
        self.assertTrue(r["all_selected_original_line_pairs_identical"])
        self.assertTrue(r["same_selected_physical_adjacency_and_source_provenance"])
        self.assertTrue(r["full_maps_both_source_GQ_and_complete"])
        self.assertEqual(
            r["positive"]["independent_original_source_rectangle_count"],4)
        self.assertEqual(
            r["positive"]["full_map_original_D6_radius_two_extensions"],8)
        self.assertEqual(
            r["zero"]["independent_original_source_rectangle_count"],0)
        self.assertEqual(
            r["zero"]["full_map_original_D6_radius_two_extensions"],0)
        self.assertEqual(r["positive"]["selected_true_original_GF5_D6"],0)
        self.assertEqual(r["zero"]["selected_true_original_GF5_D6"],0)
        self.assertFalse(r["infinite_asymptotic_HYP105_counterexample"])
        self.assertTrue(r["finite_W34_selected_structure_cannot_force_fresh_mass"])
        self.assertEqual(
            len(r["positive"]["per_source_block_per_hub_pair_fresh"]),2)
        self.assertEqual(
            len(r["zero"]["per_source_block_per_hub_pair_fresh"]),2)
        self.assertTrue(all(
            not w for block in r["zero"]["per_source_block_per_hub_pair_fresh"]
            for _,w in block[1]
        ))

    def test_frozen_permutation_is_79_bijection_not_stochastic_assumption(self):
        p=ZERO_OTHER_LINE_PAIR_PERMUTATION
        self.assertEqual(len(p),79)
        self.assertEqual(set(p),set(range(79)))
        self.assertNotEqual(tuple(p),tuple(range(79)))

    def test_source_rectangle_genuine_W34_independent_full_physical_H(self):
        parent,f,g,flags,selected=real_W34_two_disjoint_saturated_blocks(
            return_inputs=True)
        self.assertEqual(len(selected),12)
        selected_physical,_=physical(selected,flags,f,g)
        blocks=saturated_bipartite_k32_list(selected_physical)
        self.assertEqual(len(blocks),2)
        full,_=physical(range(len(flags)),flags,f,g)
        total=0
        for hubs,frees in blocks:
            oracle=source_incidence_rectangle_counts(hubs,frees,flags,f,g)
            used_x={v[0] for v in hubs+frees}
            used_y={v[1] for v in hubs+frees}
            for (i,j),candidates in oracle.items():
                direct=tuple(sorted(
                    w for w in full[hubs[i]] & full[hubs[j]]
                    if w[0] not in used_x and w[1] not in used_y))
                self.assertEqual(candidates,direct)
                total+=len(candidates)
        self.assertEqual(total,4)
        self.assertEqual(total,parent["full_H_fresh_common_neighbor_mass"])

    def test_source_rectangle_rejects_illegal_global_injection(self):
        parent,f,g,flags,selected=real_W34_two_disjoint_saturated_blocks(
            return_inputs=True)
        graph,_=physical(selected,flags,f,g)
        hubs,frees=saturated_bipartite_k32_list(graph)[0]
        wrong=list(g)
        wrong[1]=wrong[0]
        with self.assertRaises(ValueError):
            source_incidence_rectangle_counts(hubs,frees,flags,f,wrong)
        wrong_f=list(f)
        wrong_f[1]=wrong_f[0]
        with self.assertRaises(ValueError):
            source_incidence_rectangle_counts(hubs,frees,flags,wrong_f,g)


if __name__=="__main__":
    unittest.main()
