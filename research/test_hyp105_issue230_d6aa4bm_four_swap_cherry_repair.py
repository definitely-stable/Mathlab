"""AA4-BM: independent exact finite repair tests with real original W(3,2/4)."""
import unittest
from collections import Counter
from itertools import combinations, permutations
from math import comb
from fractions import Fraction

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import zero_split_original_W32
from hyp105_issue230_d6aa4bh_local_seven_compensation import _original_source
from hyp105_issue230_d6aa4bl_two_pin_conditional_BA import occupied_A_six_two_pinned_edges
from hyp105_issue230_d6aa4bm_four_swap_cherry_repair import (
    repair_four_prescribed_images,
    first_genuine_original_root_C4_sixflag,
    iter_occupied_two_pin_A_targets,
    repair_genuine_original_cherry,
    all_h_pin_regular_four_swap_certificate,
)


def independent_score(Q, physical, incidence, side):
    counts = Counter(col for j in Q for col in physical[incidence[j][1-side]])
    return len(counts)==6 and set(counts.values())=={2}


class AA4BMFourSwaps(unittest.TestCase):
    def test_01_all_h_exact_theorem_and_majority(self):
        for h in tuple(range(5,36))+(40,48,64,80):
            z=all_h_pin_regular_four_swap_certificate(1<<h)
            self.assertGreater(z["good_actual_original_cherry_root_fraction_lower"], Fraction(3,4))
            self.assertGreaterEqual(z["distinct_global_4swap_repairs_for_EACH_good_root_lower"],
                                    12*(z["a"]-4)*(z["a"]-5))
            self.assertTrue(z["given_entire_input_original_g_actual_accepted_count_NOT_BOUNDED"])
            self.assertTrue(z["same_single_repaired_g_for_all_roots_NOT_PROVED"])

    def test_02_independent_K6_count_and_distinct_all_targets_for_FIXED_Q(self):
        K6=tuple(combinations(range(6),2))
        for x,y,count in (((0,1),(1,2),7),((0,1),(2,3),14)):
            generated=list(iter_occupied_two_pin_A_targets(K6,6,x,y))
            self.assertEqual(len(generated),count)
            self.assertEqual(len(set(generated)),count)
            self.assertEqual(occupied_A_six_two_pinned_edges(K6,6,x,y)[
                "occupied_physical_A_six_twofactor_with_both_pins"],count)
            images=K6
            pins=(images.index(x),images.index(y))
            source_ids=tuple(i for i in range(15) if i not in pins)[:4]
            outputs=set()
            for physical_six in generated:
                other=tuple(sorted(physical_six-{x,y}))
                for assignment in permutations(other):
                    repaired,swaps=repair_four_prescribed_images(
                        images,tuple(zip(source_ids,assignment)),pins)
                    self.assertLessEqual(len(swaps),4)
                    self.assertEqual(tuple(repaired[i] for i in pins), (x,y))
                    outputs.add(repaired)
            self.assertEqual(len(outputs),24*count)

    def test_03_true_original_W32_fixed_f_g_any_root_with_candidate(self):
        schemes=[("dual_zero",zero_split_original_W32())]+[
            (name,fixture(1,name)) for name in ("lex","reverse","S68","S72")]
        across=Counter()
        for name,model in schemes:
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            for side,by in ((0,byP),(1,byL)):
                for p in range(V):
                    for pair in combinations(by[p],2):
                        q=first_genuine_original_root_C4_sixflag(model,side,p,pair)
                        if q is None:
                            continue
                        out=repair_genuine_original_cherry(model,side,p,pair)
                        self.assertIsNotNone(out)
                        self.assertEqual(len(set(out["source_six_original_flag_IDs"])),6)
                        self.assertEqual(len(set(out["source_opposite_six_original_factors"])),6)
                        self.assertLessEqual(len(out["transpositions_of_original_factor_images"]),4)
                        self.assertTrue(independent_score(
                            out["source_six_original_flag_IDs"],
                            out["repaired_complete_opposite_images"],inc,side))
                        self.assertEqual(
                            set(out["repaired_complete_opposite_images"]),
                            set((g,f)[side]))
                        self.assertEqual(tuple(out["repaired_complete_opposite_images"][i]
                                              for i in out["pinned_actual_original_opposite_factor_IDs"]),
                                         tuple((g,f)[side][i]
                                               for i in out["pinned_actual_original_opposite_factor_IDs"]))
                        across[(name,side)]+=1
        self.assertTrue(all(across[(name,side)]>0 for name,_ in schemes for side in (0,1)))

    def test_04_true_original_W34_nononto_type_duality(self):
        for name in ("lex","random"):
            model=fixture(2,name)
            s,V,a,inc,f,g,byP,byL=_original_source(model)
            self.assertEqual((s,V,a),(4,85,14))
            for side,by in ((0,byP),(1,byL)):
                success=0
                for p in range(3):
                    for flags in combinations(by[p],2):
                        out=repair_genuine_original_cherry(model,side,p,flags)
                        if out is None: continue
                        self.assertLessEqual(len(out["transpositions_of_original_factor_images"]),4)
                        self.assertEqual(set(out["repaired_complete_opposite_images"]),
                                         set((g,f)[side]))
                        self.assertTrue(independent_score(
                            out["source_six_original_flag_IDs"],
                            out["repaired_complete_opposite_images"],inc,side))
                        success+=1
                self.assertGreater(success,0)

    def test_05_pendant_physical_no_target_and_adversarial_rejection(self):
        E=tuple(edge for edge in combinations(range(7),2) if 0 not in edge or edge==(0,1))
        self.assertEqual(list(iter_occupied_two_pin_A_targets(E,7,(0,1),(2,3))),[])
        with self.assertRaises(ValueError):
            repair_four_prescribed_images(((0,1),(0,1)),((0,(0,1)),))
        base=tuple(combinations(range(5),2))
        with self.assertRaises(ValueError):
            repair_four_prescribed_images(base,((2,(0,1)),),protected=(0,))
        with self.assertRaises(ValueError):
            repair_four_prescribed_images(base,((2,(10,11)),))
        with self.assertRaises(ValueError):
            repair_four_prescribed_images(base,tuple((i,base[i]) for i in range(5)))
        with self.assertRaises(ValueError):
            all_h_pin_regular_four_swap_certificate(16)


if __name__=="__main__":
    unittest.main()
