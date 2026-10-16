"""Independent original W32/W34 and physical graph adversarial falsifiers."""
import random
import unittest
from collections import Counter
from itertools import combinations, permutations
from math import comb,perm
from fractions import Fraction

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4r_quenched_original_d6 import _params
from hyp105_issue230_d6aa4as_many_five_swap_repairs import (
    all_h_repair_ball_certificate,
    finite_genuine_original_one_Q_repair_ball,
)
from hyp105_issue230_d6aa4ar_five_swap_original_D6 import (
    repair_original_D6_with_at_most_five_line_swaps,
)
from hyp105_g5e2b3e1b0_seven_signature import (
    classify_seven_prechecked,physical_column_dual,is_connected_column_cycle,
)


def independently_count_anchored_physical_C6(a,occupied,anchor):
    """Literal DFS through physical graph, no helper or combinatorial bound."""
    E={tuple(edge) for edge in occupied}
    u,v=anchor
    nbr={w:set() for w in range(a)}
    for x,y in E:
        nbr[x].add(y)
        nbr[y].add(x)
    answer=set()
    def walk(path):
        if len(path)==6:
            if path[-1] in nbr[u]:
                cyc=tuple(tuple(sorted((path[i],path[(i+1)%6]))) for i in range(6))
                answer.add(frozenset(cyc))
            return
        for next_node in nbr[path[-1]]:
            if next_node not in path and next_node!=u:
                walk(path+[next_node])
    walk([u,v])
    return len(answer)


class EveryOriginalRepairBallTests(unittest.TestCase):
    def test_01_all_h_exact_dyadic_symbolic_and_no_minimax_promotion(self):
        for h in tuple(range(1,36))+(40,48,64,80):
            s=1<<h
            z=all_h_repair_ball_certificate(s)
            self.assertGreaterEqual(
                4*z["distinct_COMPLETE_global_right_maps_positive_D6_within_5_line_swaps_at_least"],
                s**6)
            self.assertGreater(z["occupied_f_C6_avoiding_all_bad_original_points_lower"],0)
            self.assertTrue(z["one_and_same_actual_six_original_incidence_IDs_for_all_repairs"])
            self.assertFalse(z["original_d6_at_given_adversarial_g_lower_proved"])
            self.assertFalse(z["all_seven_class_original_fixed_pair_minimax_proved"])
            self.assertEqual(z["root_230"],"OPEN_WITH_FORMAL_BLOCKER")
            if h>=5:
                self.assertGreater(z["K"],78*z["m"])
                self.assertEqual(z["bad_right_original_LINE_factors_strict_upper"],12*z["m"])
            else:
                self.assertEqual(z["bad_right_original_LINE_factors_strict_upper"],0)

    def test_02_global_physical_C6_6fold_edge_incidence_exact_independent_brute(self):
        for a in range(6,11):
            physical=tuple(combinations(range(a),2))
            cycle_count=0
            per_edge=Counter()
            # Independent cycle enumeration by physical coordinate subset and
            # index-root symmetry, NOT via oriented-edge formula in source.
            for vertex_set in combinations(range(a),6):
                v0=vertex_set[0]
                for order in permutations(vertex_set[1:]):
                    if order[0]>order[-1]:
                        continue
                    vs=(v0,)+order
                    physical_cycle={tuple(sorted((vs[i],vs[(i+1)%6])))
                                    for i in range(6)}
                    cycle_count+=1
                    per_edge.update(physical_cycle)
            self.assertEqual(cycle_count,perm(a,6)//12)
            self.assertEqual(set(per_edge),set(physical))
            self.assertEqual(set(per_edge.values()),{perm(a-2,4)})
            self.assertEqual(sum(per_edge.values()),6*cycle_count)

    def test_03_adversarial_K10_missing_edges_global_loss_mass(self):
        rng=random.Random(230540)
        a=10
        full=set(combinations(range(a),2))
        A=perm(a-2,4)
        for m in range(0,a-1):
            for case in range(10):
                if case==0 and m==a-2:
                    missing={(0,v) for v in range(2,a)}
                else:
                    missing=set(rng.sample(sorted(full),m))
                occupied=full-missing
                deficits={}
                for e in occupied:
                    through=independently_count_anchored_physical_C6(a,occupied,e)
                    self.assertLessEqual(through,A)
                    deficits[e]=A-through
                self.assertLessEqual(sum(deficits.values()),6*m*A)
                bad=[e for e,x in deficits.items() if 2*x>A]
                self.assertLessEqual(len(bad),12*m)
                if case==0 and m==a-2:
                    self.assertEqual((0,1) in bad,True)

    def test_04_real_W32_original_fixed_g_zero_but_many_repaired(self):
        # S68/S72 are genuine FULL ORIGINAL maps with D6=0; test this
        # separately from enumerating many repaired positive witnesses.
        from hyp105_issue230_d6aa4tcyc_fixed_f_d6_pair import (
            genuine_W32_fixed_f_original_connected_left_Q,
        )
        for scheme in ("S68","S72"):
            model=fixture(1,scheme)
            _,rows=genuine_W32_fixed_f_original_connected_left_Q(scheme)
            self.assertEqual(len(rows),21186)
            initial=0
            for ids in rows:
                p=tuple(model["incidences"][i][0] for i in ids)
                l=tuple(model["incidences"][i][1] for i in ids)
                d1=physical_column_dual(model["incidences"],model["left_labels"],p)
                d2=physical_column_dual(model["incidences"],model["right_labels"],l)
                initial+=d1==d2 and is_connected_column_cycle(d1)
            self.assertEqual(initial,0)
            z=finite_genuine_original_one_Q_repair_ball(model)
            self.assertEqual(z["actual_different_full_right_maps_positive_same_original_D6_Q"],48)
            self.assertEqual(z["actual_right_occupied_undirected_C6_through_anchor"],24)
            self.assertGreaterEqual(z["actual_different_full_right_maps_positive_same_original_D6_Q"],16)
            self.assertTrue(z["historical_W32_classifier_full_crosscheck"])
            self.assertLessEqual(z["largest_global_LINE_swap_distance_used"],5)

    def test_05_real_W34_nononto_same_physical_support_and_independent_cycle_DFS(self):
        for scheme in ("lex","random"):
            model=fixture(2,scheme)
            z=finite_genuine_original_one_Q_repair_ball(model)
            self.assertEqual((z["s"],z["physical_a"]),(4,14))
            self.assertEqual(len(model["right_labels"]),85)
            self.assertGreaterEqual(z["actual_different_full_right_maps_positive_same_original_D6_Q"],
                                    perm(12,4))
            independent=independently_count_anchored_physical_C6(
                14,model["right_labels"],z["anchored_global_right_line_physical_edge_kept"])
            self.assertEqual(independent,
                z["actual_right_occupied_undirected_C6_through_anchor"])
            self.assertEqual(2*independent,
                z["actual_different_full_right_maps_positive_same_original_D6_Q"])
            self.assertTrue(z["independent_all_a_six_position_physical_D6_crosscheck"])
            self.assertFalse(z["historical_W32_classifier_full_crosscheck"])

    def test_06_source_genuine_original_6points_Hall_delete_one_line_random(self):
        # Different oracle: source-neighbor DP verifies the Hall deletion
        # argument on true real GQ W32/W34 without relying on swap routine.
        for h,schemes in ((1,("S68","S72")),(2,("lex","random"))):
            for scheme in schemes:
                model=fixture(h,scheme)
                V=len(model["left_labels"])
                degree={p:set() for p in range(V)}
                for p,l in model["incidences"]:
                    degree[p].add(l)
                for p in range(V):
                    self.assertEqual(len(degree[p]),(1<<h)+1)
                rng=random.Random(5401+h)
                for _ in range(12):
                    ps=tuple(rng.sample(range(V),6))
                    removed=rng.randrange(V)
                    # INDEPENDENT subsets and literal Hall matching DP.
                    def match(i,used):
                        if i==6:
                            return True
                        return any(match(i+1,used|{l})
                                   for l in degree[ps[i]]-{removed}
                                   if l not in used)
                    self.assertTrue(match(0,frozenset()))

    def test_07_physical_invalid_and_unproved_original_event_scope(self):
        with self.assertRaises(ValueError):
            all_h_repair_ball_certificate(3)
        with self.assertRaises(ValueError):
            all_h_repair_ball_certificate(1)
        for h in (1,2,4,8,16):
            z=all_h_repair_ball_certificate(1<<h)
            self.assertFalse(z["original_d6_at_given_adversarial_g_lower_proved"])
            self.assertTrue(z["original_fixed_f_and_original_right_physical_support_unchanged"])


if __name__=="__main__":
    unittest.main()
