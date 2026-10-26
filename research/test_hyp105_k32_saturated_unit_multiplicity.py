"""AA4-K32SAT1: sharp saturated-only 1-parent positive original GF5 D6 transfer."""
from itertools import combinations, permutations
import unittest

from hyp105_saturated_k32_original_sixset_radius2 import (
    genuine_W34_protected_k32_radius_two,
)
from hyp105_k32_saturated_unit_multiplicity import (
    genuine_source_saturated_unit_transfer,
    real_W34_two_disjoint_saturated_blocks,
)


class TestSaturatedUnitMultiplicity(unittest.TestCase):
    def test_all_512_K33_simple_bipartite_subgraphs_no_two_saturated_parents(self):
        # Independent physical combinatorial falsifier: for EVERY G subset
        # of K3,3, enumerate each of its possible saturated K3,2 parents
        # for all SIX distinct C6 in the full K3,3. If two parents
        # pointed to the SAME C6 the proposed bound would be false.
        L=(0,1,2)
        R=(3,4,5)
        all_edges=tuple((u,v) for u in L for v in R)
        cycles=set()
        for perm in permutations(R):
            cyc=frozenset(
                (min(u,v),max(u,v))
                for i in range(3)
                for u,v in ((L[i],perm[i]),
                            (L[(i+1)%3],perm[i]))
            )
            cycles.add(cyc)
        self.assertEqual(len(cycles),6)
        n_saturated=n_nonempty=0
        for mask in range(1<<9):
            edges={edge for k,edge in enumerate(all_edges) if mask>>k&1}
            saturated=[]
            for absent in R:
                parent={(u,v) for u in L for v in R if v!=absent}
                if parent<=edges and all(
                        len({z for z in R if (u,z) in edges and
                             (v,z) in edges})==2
                        for u,v in combinations(L,2)):
                    saturated.append(parent)
            for absent in L:
                parent={(u,v) for u in L for v in R if u!=absent}
                if parent<=edges and all(
                        len({z for z in L if (z,u) in edges and
                             (z,v) in edges})==2
                        for u,v in combinations(R,2)):
                    saturated.append(parent)
            n_saturated+=len(saturated)
            for cyc in cycles:
                compatible=sum(
                    1 for parent in saturated
                    if len(parent-cyc)==2 and len(cyc-parent)==2
                )
                self.assertLessEqual(compatible,1)
                n_nonempty+=(compatible>0)
        self.assertGreater(n_saturated,0)
        self.assertGreater(n_nonempty,0)

    def test_true_W34_existing_one_saturated_parent_many_full_extensions(self):
        result,f,g,flags,_,_=genuine_W34_protected_k32_radius_two(
            return_inputs=True)
        ids=result["true_original_protected_ids"]
        z=genuine_source_saturated_unit_transfer(2,f,g,ids)
        self.assertEqual(z["saturated_original_source_K32_blocks"],1)
        self.assertGreaterEqual(z["full_H_fresh_common_neighbor_mass"],1)
        self.assertEqual(z["two_swap_D6_extension_memberships"],
                         2*z["full_H_fresh_common_neighbor_mass"])
        self.assertEqual(z["two_swap_D6_extension_memberships"],
                         z["distinct_accepted_original_D6_from_saturated_blocks"])
        self.assertEqual(z["max_original_D6_saturated_parent_multiplicity"],1)
        self.assertEqual(z["selected_ordinary_C6"],0)
        self.assertEqual(z["selected_original_double_diagonal_edges"],12)
        self.assertTrue(z["all_h_saturated_only_unit_multiplicity_proved"])

    def test_true_W34_two_disjoint_source_factor_saturated_parents(self):
        z=real_W34_two_disjoint_saturated_blocks()
        self.assertEqual(z["s"],4)
        self.assertEqual(z["saturated_original_source_K32_blocks"],2)
        self.assertEqual(z["selected_original_double_diagonal_edges"],24)
        self.assertEqual(z["selected_ordinary_C6"],0)
        self.assertGreaterEqual(z["full_H_fresh_common_neighbor_mass"],2)
        self.assertGreaterEqual(z["two_swap_D6_extension_memberships"],4)
        self.assertEqual(z["two_swap_D6_extension_memberships"],
                         z["distinct_accepted_original_D6_from_saturated_blocks"])
        self.assertEqual(z["max_original_D6_saturated_parent_multiplicity"],1)
        self.assertFalse(z["root_sevenclass_Omega_s6_proved"])

    def test_incomplete_and_repeated_genuine_selected_source_rejected(self):
        report,f,g,_,_,_=genuine_W34_protected_k32_radius_two(
            return_inputs=True)
        old=report["true_original_protected_ids"]
        with self.assertRaises(ValueError):
            genuine_source_saturated_unit_transfer(2,f,g,old+old[:1])
        g_bad=list(g)
        g_bad[1]=g_bad[0]
        with self.assertRaises(ValueError):
            genuine_source_saturated_unit_transfer(2,f,g_bad,old)
        with self.assertRaises(ValueError):
            genuine_source_saturated_unit_transfer(3,f,g,old)


if __name__=="__main__":
    unittest.main()
