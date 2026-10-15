"""AA4-AI independent true-original W32 two-orientation zero/C6 restoration."""
import unittest
from itertools import combinations
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    TAGS,ZERO_SPLIT_POINT,ZERO_SPLIT_LINE,zero_split_original_W32,
    classify_physical_A_twofactor,exact_physical_A_sector_capacities,
    full_original_W32_sector_certificate,independent_literal_original_W32_sector_census,
    single_original_A_sector_permanent)
from hyp105_issue230_d6aa4ad_opposite_a_hall_transfer import pinned_twofactor_completions
from hyp105_issue230_d6aa4af_rootpair_robust_quench import occupied_root_C4_source_factors
from hyp105_issue230_d6aa4q_two_sided_seven_join import exact_two_sided_original_seven_join
from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ab_minimax_orbit_normalform import (
    _valid_original_model,transform_model,symplectic_transvection_source)


class CompleteOriginalTriangleCounterexample(unittest.TestCase):
    def test_01_all_pair_complete_K6_K7_K8_physical_1_to_6_sectors(self):
        for a in (6,7,8):
            E=tuple(combinations(range(a),2))
            for pins in combinations(E,2):
                adjacent=bool(set(pins[0])&set(pins[1]))
                expect=exact_physical_A_sector_capacities(a,adjacent=adjacent)
                from collections import Counter
                found=Counter(classify_physical_A_twofactor(H,pins)
                              for H in pinned_twofactor_completions(*pins,a))
                for tag in TAGS:
                    self.assertEqual(found[tag],expect[tag])
                self.assertEqual(sum(found.values()),expect["total_A_twofactors"])
                self.assertEqual(expect["connected_C6"],
                                 6*(expect["same_triangle_pins"]+
                                     expect["split_two_triangles"]))

    def test_02_concrete_global_injective_true_symplectic_W32_witness(self):
        m=zero_split_original_W32()
        V,a,_=_valid_original_model(m)
        self.assertEqual((V,a,m["s"]),(15,6,2))
        self.assertEqual(set(ZERO_SPLIT_POINT),set(range(15)))
        self.assertEqual(set(ZERO_SPLIT_LINE),set(range(15)))
        self.assertEqual(len(set(m["incidences"])),45)
        self.assertEqual(tuple(m["left_labels"][0]),(0,5))
        self.assertNotEqual(m["left_labels"],m["right_labels"])

    def test_03_both_orientations_zero_split_but_original_C6_or_same_tris(self):
        m=zero_split_original_W32()
        for side in (0,1):
            z=full_original_W32_sector_certificate(m,side=side)
            self.assertEqual(z["complete_actual_original_roots"],15)
            self.assertEqual(z["real_original_root_flag_pairs"],45)
            self.assertEqual(z["original_B_root_C4_cohorts"],135)
            self.assertEqual(z["original_GF5_A_accepted_by_sector"]["split_two_triangles"],0)
            self.assertGreater(z["occupied_opposite_A_physical_H_by_sector"]["split_two_triangles"],0)
            self.assertGreater(z["full_original_BA_or_AB_accepted"],0)
            self.assertEqual(z["full_original_BA_or_AB_accepted"],
                             sum(z["original_GF5_A_accepted_by_sector"].values()))
            self.assertEqual(z["full_original_BA_or_AB_accepted"],
                             sum(z["original_Hall_positive_by_sector"].values())+
                             sum(z["induced_original_C8_charge_by_sector"].values()))

    def test_04_independent_literal_original_six_ID_exact_sector_join(self):
        m=zero_split_original_W32()
        for side in (0,1):
            Hall=full_original_W32_sector_certificate(m,side=side)
            literal=independent_literal_original_W32_sector_census(m,side=side)
            self.assertEqual(literal,Hall["original_GF5_A_accepted_by_sector"])
            self.assertEqual(literal["split_two_triangles"],0)

    def test_05_historical_full_62370_seven_GF5_original_S_stays_positive(self):
        m=zero_split_original_W32()
        historical=exact_two_sided_original_seven_join(m,independent_history=True)
        left=full_original_W32_sector_certificate(m,side=0)
        right=full_original_W32_sector_certificate(m,side=1)
        seven=historical["accepted_seven_GF5_original_Q_by_tag"]
        self.assertEqual(left["full_original_BA_or_AB_accepted"],seven["B-left/A-right"])
        self.assertEqual(right["full_original_BA_or_AB_accepted"],seven["A-left/B-right"])
        self.assertGreater(historical["accepted_seven_GF5_original_S"],0)
        self.assertGreater(historical["selected_GF5_51palette_certified_numerator"],0)

    def test_06_existing_original_S68_and_lex_subset_calibration(self):
        expected={"S68":((1,0),(44,21)),"lex":((3,12),(98,110))}
        for scheme,(tris,full) in expected.items():
            m=fixture(1,scheme)
            for side in (0,1):
                z=full_original_W32_sector_certificate(m,side=side)
                self.assertEqual(z["original_GF5_A_accepted_by_sector"]["split_two_triangles"],
                                 tris[side])
                self.assertEqual(z["full_original_BA_or_AB_accepted"],full[side])

    def test_07_actual_source_automorphism_and_independent_physical_relabels(self):
        m=zero_split_original_W32()
        p,l=symplectic_transvection_source(m,1)
        changed=transform_model(
            m,point_sources=p,line_sources=l,
            point_coordinates=tuple(reversed(range(6))),
            line_coordinates=tuple((i+2)%6 for i in range(6)))
        for side in (0,1):
            original=full_original_W32_sector_certificate(m,side=side)
            transformed=full_original_W32_sector_certificate(changed,side=side)
            self.assertEqual(original["original_GF5_A_accepted_by_sector"],
                             transformed["original_GF5_A_accepted_by_sector"])
            self.assertEqual(original["occupied_opposite_A_physical_H_by_sector"],
                             transformed["occupied_opposite_A_physical_H_by_sector"])

    def test_08_invalid_physical_original_and_pinned_domains(self):
        for a,b in ((5,True),(6,1),(6,None),(True,True)):
            with self.assertRaises(ValueError):
                exact_physical_A_sector_capacities(a,adjacent=b)
        with self.assertRaises(ValueError):
            classify_physical_A_twofactor(((0,1),)*6,((0,1),(0,2)))
        with self.assertRaises(ValueError):
            classify_physical_A_twofactor(tuple(combinations(range(4),2)),((0,1),(0,2)))
        m=zero_split_original_W32()
        for bad in (2,-1,True):
            with self.assertRaises(ValueError):
                full_original_W32_sector_certificate(m,side=bad)
        four=occupied_root_C4_source_factors(m,side=0,root=0)[0]
        with self.assertRaises(ValueError):
            single_original_A_sector_permanent(
                m,side=0,root=0,pair_offset=3,four=four)
        with self.assertRaises(ValueError):
            single_original_A_sector_permanent(
                m,side=0,root=0,pair_offset=0,four=(0,1,2,3))
        with self.assertRaises(ValueError):
            full_original_W32_sector_certificate(dict(m,left_labels=((0,1),)*15),side=0)


if __name__=="__main__":
    unittest.main()
