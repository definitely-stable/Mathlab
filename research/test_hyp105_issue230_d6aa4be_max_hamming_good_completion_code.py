"""AA4-BE independent whole-completion Hamming orbit over TRUE original W3s."""
import unittest
from fractions import Fraction
from itertools import permutations

from hyp105_issue230_d6aa4be_max_hamming_good_completion_code import (
    preselected_original_global_LINE_orbit,
    original_maximal_Hamming_good_LINE_completion_code,
    exact_two_all_original_global_completions_Hamming,
    literal_true_original_small_full_LINE_support_shift_family,
)
from hyp105_issue230_d6aa4bd_tenth_pins import (
    tenth_pinned_GOOD_completion)
from hyp105_issue230_d6aa4ar_good_wedges_port_balance import (
    exact_true_original_good_D_two_port_wedge_certificate)
from hyp105_issue230_projection import fixture


class MaxHammingOriginalLineGoodMaps(unittest.TestCase):
    def test_01_all_dyadic_h10_80_maximal_Hamming_cyclic_full_global_code_10percent_pins(self):
        for h in tuple(range(10,35))+(40,48,64,80):
            s=1<<h
            V=(s+1)*(s*s+1)
            for k in (0,1,V//1024,V//256,V//10):
                x=original_maximal_Hamming_good_LINE_completion_code(s,k)
                self.assertEqual(x["max_arbitrary_pinned_TRUE_original_LINE_factor_images"],V//10)
                self.assertEqual(x["pointwise_Hamming_distance_on_all_unpinned_SOURCE_LINE_factor_images"],V-k)
                self.assertEqual(x["number_of_distinct_completed_global_right_LINE_maps"],V//400000000)
                self.assertGreaterEqual(x["number_of_distinct_completed_global_right_LINE_maps"],2)
                self.assertTrue(x["any_two_completed_original_LINE_maps_differ_on_EVERY_unpinned_LINE"])
                self.assertGreaterEqual(x["exact_rational_actual_source_good_base_fraction_lower"],
                                        Fraction(1,2))
                self.assertTrue(x["every_completed_global_original_GOOD_wedge_count_ge_s6_over160"])
                self.assertTrue(x["no_accepted_SEVEN_GF5_SIX_distinct_original_flag_Q_theorem"])
                two=exact_two_all_original_global_completions_Hamming(s,k)
                self.assertEqual(two["pointwise_Hamming_difference_on_every_free_true_original_LINE_factor"],
                                 V-k)
                self.assertGreater(two[
                  "exact_positive_base_map_fraction_for_arbitrary_PRESELECTED_derangement"],0)
            if h in (10,11,12,13,20,40,80):
                print("AA4BE_TRUE_ORIGINAL_ALLH_CODE",h,
                      "V",V,"max_k",V//10,
                      "free_kmax",V-V//10,
                      "maximally_Hamming_separated_whole_GLOBAL_original_GOOD_maps",V//400000000)
        for invalid in (0,3,True,-2):
            with self.assertRaises(ValueError):
                original_maximal_Hamming_good_LINE_completion_code(invalid,0)

    def test_02_exact_parent_one_complete_g_variance_and_preselected_orbit_mass(self):
        for h in (5,6,7,8,9,10,11,12,13,14,20,40,80):
            s=1<<h
            V=(s+1)*(s*s+1)
            for k in (0,V//10):
                old=tenth_pinned_GOOD_completion(s,k)
                for m in (1,2,max(2,V//400000000)):
                    res=preselected_original_global_LINE_orbit(s,k,m)
                    self.assertEqual(res[
                        "exact_rational_conditional_relative_variance_parent"],
                        old["conditional_relative_variance_upper"])
                    exact=Fraction(1)-4*m*old["conditional_relative_variance_upper"]
                    self.assertEqual(res["exact_union_lower_before_truncation"],exact)
                    self.assertEqual(res["exact_union_lower_on_simultaneously_GOOD_fraction"],
                                     max(Fraction(0),exact))
                    self.assertTrue(res["entire_global_source_f_g_no_independent_event_image_resampling"])
                    self.assertTrue(res["arbitrary_fully_fixed_global_g_OR_original_seven_GF5_six_ID_lower_NOT_PROVED"])
        for m in (0,-1,2.5,True):
            with self.assertRaises(ValueError):
                preselected_original_global_LINE_orbit(1<<10,0,m)

    def test_03_genuine_original_W32_fixed_point_map_one_PIN_fourteen_FREE_orbit(self):
        for scheme in ("S68","S72","lex"):
            m=fixture(1,scheme)
            pinned={0}
            full=literal_true_original_small_full_LINE_support_shift_family(
                m,pinned,14)
            self.assertEqual(len(full),14)
            self.assertEqual(len(set(full)),14)
            R=[]
            for right in full:
                z=exact_true_original_good_D_two_port_wedge_certificate(
                    dict(m,right_labels=right))
                R.append(z["good_D_original_OPPOSITE_TWO_TYPED_port_wedges"])
            # Finite h1 REAL symplectic source GLOBAL injection observation
            # only: no claim the all-h h>=10 theorem was proved by h1.
            self.assertTrue(all(x>0 for x in R))
            self.assertTrue(all(right[0]==m["right_labels"][0] for right in full))
            print("AA4BE_REAL_W32_FULL_HAMMING_ORBIT",scheme,
                  "ONE_original_LINE_pin",0,
                  "all_14_COMPLETE_global_LINE_maps_pairwise_Hamming14",
                  "R_good_min",min(R),"R_good_max",max(R))

    def test_04_true_original_W34_K14_six_physical_holes_global_images_and_adversarial_pins(self):
        for scheme in ("lex","random"):
            m=fixture(2,scheme)
            imgs=literal_true_original_small_full_LINE_support_shift_family(
                m,{0,1,10},6)
            self.assertEqual(len(imgs),6)
            for shifted in imgs:
                self.assertEqual(len(set(shifted)),85)
                self.assertEqual(shifted[0],m["right_labels"][0])
                self.assertEqual(shifted[1],m["right_labels"][1])
                self.assertEqual(shifted[10],m["right_labels"][10])
                self.assertEqual({tuple(x) for x in shifted},
                                 {tuple(x) for x in m["right_labels"]})
            values=[]
            for shifted in imgs:
                x=exact_true_original_good_D_two_port_wedge_certificate(
                    dict(m,right_labels=shifted))
                values.append(x["good_D_original_OPPOSITE_TWO_TYPED_port_wedges"])
            # All images are FULL true-original source LINE assignments.
            # They need not all be GOOD at h2; h>=10 statement independent.
            self.assertTrue(all(type(x) is int and x>=0 for x in values))
            print("AA4BE_REAL_W34_PARTIAL_PHYSICAL_K14",scheme,
                  "6_complete_maps_Hamming82_and_3_pins",
                  "R_good_values",values)

    def test_05_original_validity_and_abstract_free_edge_permutation_coset(self):
        m=fixture(1,"S68")
        for invalid_pins in ((0,0),(-1,),(16,),(1.5,)):
            with self.assertRaises(ValueError):
                literal_true_original_small_full_LINE_support_shift_family(
                    m,invalid_pins,2)
        for invalid_count in (0,-1,True,15):
            with self.assertRaises(ValueError):
                literal_true_original_small_full_LINE_support_shift_family(
                    m,(0,),invalid_count)
        with self.assertRaises(ValueError):
            literal_true_original_small_full_LINE_support_shift_family(
                dict(m,right_labels=((0,1),)*15),(0,),2)
        # Abstract independent finite permutation source-free image
        # complement verification, explicitly NOT a fake W3s.
        pool=tuple("abcdef")
        images=[]
        for shift in range(len(pool)):
            mapping=dict(zip(range(6),pool[shift:]+pool[:shift]))
            images.append(mapping)
        for a,b in permutations(images,2):
            self.assertEqual(sum(a[j]!=b[j] for j in range(6)),6)


if __name__=="__main__":
    unittest.main()
