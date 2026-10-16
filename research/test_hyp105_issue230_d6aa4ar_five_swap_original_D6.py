"""Independent test oracles: K10 missing-edge extremal and actual W32/W34 D6 repair."""
import unittest
from itertools import combinations, permutations
from math import comb,perm
import random

from hyp105_issue230_d6aa4ar_five_swap_original_D6 import (
    exceptional_noncycle_edge, complete_physical_C6_with_anchor,
    find_first_physical_C6, repair_original_D6_with_at_most_five_line_swaps,
)
from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import (
    classify_seven_prechecked,physical_column_dual,
    is_connected_column_cycle,
)


def brute_anchored_physical_C6(a,occupied,edge):
    """Definition-level exhaustive genuine physical C6 anchored with edge."""
    E=set(occupied)
    x,y=edge
    for tail in permutations((v for v in range(a) if v not in edge),4):
        path=(x,y)+tail
        edges={tuple(sorted((path[i],path[(i+1)%6]))) for i in range(6)}
        if edges<=E:
            return True
    return False


class DeterministicOriginalFiveSwapD6Tests(unittest.TestCase):
    def test_01_physical_two_edge_joint_C6_counts_independent_brute(self):
        # Explicit independent brute, no #485 inclusion/exclusion reuse.
        for a in (6,7,8,10):
            e=(0,1)
            h_adj=(0,2)
            h_dis=(2,3)
            N=adj=dis=0
            for tail in permutations(range(2,a),4):
                path=(0,1)+tail
                edges={tuple(sorted((path[i],path[(i+1)%6])))
                       for i in range(6)}
                N+=1
                adj+=h_adj in edges
                dis+=h_dis in edges
            self.assertEqual(N,perm(a-2,4))
            self.assertEqual(adj,perm(a-3,3))
            self.assertEqual(dis,6*perm(a-4,2))
        # At actual original s>=4 physical a>=14, adjacent deletions
        # are STRICTLY most destructive for a fixed occupied e.
        self.assertGreater(perm(14-3,3),6*perm(14-4,2))

    def test_02_physical_pendant_is_exact_unique_extremal_exception(self):
        for a in (10,14,35):
            all_edges=set(combinations(range(a),2))
            # Delete a-2 physical edges incident to physical vertex 0,
            # preserving ONLY edge (0,1). It is a real no-C6 edge.
            missing={(0,j) for j in range(2,a)}
            E=all_edges-missing
            self.assertEqual(exceptional_noncycle_edge(a,E),(0,1))
            with self.assertRaises(ValueError):
                complete_physical_C6_with_anchor(a,E,(0,1))
            self.assertIsNotNone(complete_physical_C6_with_anchor(a,E,(1,2)))
            # Removing ONE fewer edge restores an occupied cycle for e.
            E.add((0,2))
            self.assertIsNone(exceptional_noncycle_edge(a,E))
            self.assertTrue(brute_anchored_physical_C6(a,E,(0,1)))

    def test_03_arbitrary_nonstar_missing_palettes_K10_exact_edge_coverage(self):
        a=10
        universe=set(combinations(range(a),2))
        rng=random.Random(23005)
        for m in range(0,a-1):
            for _ in range(8):
                missing=set(rng.sample(sorted(universe),m))
                occupied=universe-missing
                bad=exceptional_noncycle_edge(a,occupied)
                actual_bad={e for e in occupied if not brute_anchored_physical_C6(a,occupied,e)}
                self.assertEqual(actual_bad,{bad} if bad is not None else set())

    def test_04_real_original_W32_bad_full_f_g_repaired_genuine_source(self):
        # S68 and S72 have actual ORIGINAL complete f,g and strict D6=0.
        from hyp105_issue230_d6aa4tcyc_fixed_f_d6_pair import (
            genuine_W32_fixed_f_original_connected_left_Q,
        )
        for scheme in ("S68","S72"):
            model=fixture(1,scheme)
            other_model, original_Q = genuine_W32_fixed_f_original_connected_left_Q(scheme)
            self.assertEqual(len(original_Q),21186)
            # INDEPENDENT original-definition complete 21,186 six-ID D6
            # census of the ORIGINAL (f,g), before any swaps: exactly zero.
            initial_d6=0
            for ids in original_Q:
                source_points=tuple(model["incidences"][i][0] for i in ids)
                source_lines=tuple(model["incidences"][i][1] for i in ids)
                left=physical_column_dual(model["incidences"],model["left_labels"],source_points)
                right=physical_column_dual(model["incidences"],model["right_labels"],source_lines)
                initial_d6+=(left==right and is_connected_column_cycle(left))
            self.assertEqual(initial_d6,0)
            for reverse in (False,True):
                z=repair_original_D6_with_at_most_five_line_swaps(model,reverse=reverse)
                self.assertLessEqual(z["global_line_transposition_distance_upper"],5)
                self.assertEqual(z["historical_original_seven_GF5_class_after"],"D6")
                self.assertEqual(z["right_global_full_injection_before"],
                                 tuple(map(tuple,model["right_labels"])))
                inc=tuple(map(tuple,model["incidences"]))
                ids=z["actual_original_six_incidence_IDs"]
                self.assertEqual(len(set(ids)),6)
                self.assertEqual(len({inc[i][0] for i in ids}),6)
                self.assertEqual(len({inc[i][1] for i in ids}),6)
                self.assertEqual(classify_seven_prechecked(
                    ids,model["left_labels"],
                    z["right_global_full_injection_after"],inc),"D6")
                if reverse:
                    self.assertNotEqual(
                        z["right_global_full_injection_after"],
                        repair_original_D6_with_at_most_five_line_swaps(
                            model,reverse=False)["right_global_full_injection_after"])

    def test_05_full_original_W32_five_layouts_and_change_only_line_labels(self):
        for scheme in ("lex","reverse","S68","S72"):
            model=fixture(1,scheme)
            z=repair_original_D6_with_at_most_five_line_swaps(model)
            final=list(z["right_global_full_injection_before"])
            for u,v in z["swap_list_of_TRUE_original_LINE_factor_labels"]:
                final[u],final[v]=final[v],final[u]
            self.assertEqual(tuple(final),z["right_global_full_injection_after"])
            self.assertEqual(set(final),set(z["right_global_full_injection_before"]))
            self.assertEqual(final[z["anchored_original_line_factor_ID"]],
                             z["anchored_physical_image_preserved"])
            p=tuple(model["incidences"][i][0] for i in z["actual_original_six_incidence_IDs"])
            l=tuple(model["incidences"][i][1] for i in z["actual_original_six_incidence_IDs"])
            d1=physical_column_dual(model["incidences"],model["left_labels"],p)
            d2=physical_column_dual(model["incidences"],final,l)
            self.assertEqual(d1,d2)
            self.assertTrue(is_connected_column_cycle(d1))

    def test_06_real_original_W34_nononto_K14_two_schemes(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            self.assertEqual(model["s"],4)
            self.assertEqual(model["a"],14)
            self.assertEqual(comb(14,2)-len(model["right_labels"]),6)
            z=repair_original_D6_with_at_most_five_line_swaps(model)
            self.assertLessEqual(len(z["swap_list_of_TRUE_original_LINE_factor_labels"]),5)
            self.assertEqual(z["historical_original_seven_GF5_class_after"],"D6")
            self.assertIsNone(z["physical_right_C6_free_exceptional_edge"])
            self.assertEqual(len(set(z["right_global_full_injection_after"])),85)

    def test_07_invalid_fake_original_global_injections_fail_closed(self):
        z=fixture(1,"lex")
        broken=dict(z)
        broken["right_labels"]=tuple(z["right_labels"][:-1])+tuple(z["right_labels"][:1])
        with self.assertRaises(ValueError):
            repair_original_D6_with_at_most_five_line_swaps(broken)
        broken=dict(z)
        broken["incidences"]=tuple(z["incidences"][:-1])+tuple(z["incidences"][:1])
        with self.assertRaises(ValueError):
            repair_original_D6_with_at_most_five_line_swaps(broken)
        with self.assertRaises(ValueError):
            exceptional_noncycle_edge(10,set(combinations(range(10),2))-
                                     {(0,j) for j in range(2,10)}-{(1,2)})

    def test_08_all_h_symbolic_missing_palette_strict_positive_cycles(self):
        from hyp105_issue230_d6aa4r_quenched_original_d6 import _params
        for h in tuple(range(1,21))+(32,64):
            s=1<<h
            V,a,K,m=_params(s)
            self.assertTrue((a==6 and m==0) or (a>=14 and m<=a-2))
            all_cycles=perm(a,6)//12
            lost=m*perm(a-2,4)
            self.assertGreater(all_cycles-lost,0)
            self.assertGreater(V,6)
            self.assertGreaterEqual(s+1,3)


if __name__=="__main__":
    unittest.main()
