"""Independent AA4-K all-h 9/6/3 physical-source / genuine original-GF5 checks."""
import random
import unittest
from fractions import Fraction
from itertools import combinations

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import (
    seven_census,R3_CERTIFIED_FLOORS)
from hyp105_issue230_d6aa4i_original_spectral_coordinate import geometry
from hyp105_issue230_d6aa4k_projection_aware_charge import (
    PATTERN_CAP,TAG_TYPES,six_incidence_projection_capacity,
    conditional_average_transfer,true_original_projection_charge,_ceil,
)


class OriginalProjectionChargeTests(unittest.TestCase):
    def test_001_abstract_true_six_coordinate_projection_A_B_C_exact_cap(self):
        cases=[
            ("A",tuple(range(6)),((0,1),(1,2),(2,3),(3,4),(4,5),(0,5)),9,6),
            ("B",(0,0,1,2,3,4),((0,1),(2,3),(3,4),(4,5),(2,5)),6,5),
            ("C",(0,0,1,1,2,2),((0,1),(2,3),(4,5)),3,3),
        ]
        for kind,endpoints,labels,cap,nfactors in cases:
            # Labels are unique GLOBAL source factor images. All Q six
            # incidences use only those typed-source original factor IDs.
            r=six_incidence_projection_capacity(endpoints,labels,6)
            self.assertEqual(r["true_original_source_projection_kind"],kind)
            self.assertEqual(r["original_distinct_source_factors"],nfactors)
            self.assertEqual(r["ALL_physically_disjoint_original_factor_pairs"],cap)
            self.assertEqual(r["exact_A_B_C_source_pair_disjoint_capacity"],cap)
            self.assertTrue(r["physical_six_coordinate_degree_two"])
            self.assertEqual(sum(r["source_factor_multiplicity_profile"]),6)

    def test_002_fail_closed_non_six_coordinate_and_noninjective_projections(self):
        edges=((0,1),(1,2),(2,3),(3,4),(4,5),(0,5))
        with self.assertRaises(ValueError):
            six_incidence_projection_capacity((0,1,2,3,4),edges,6)
        with self.assertRaises(ValueError):
            six_incidence_projection_capacity(tuple(range(6)),((0,1),)*6,6)
        with self.assertRaises(ValueError):
            six_incidence_projection_capacity(tuple(range(6)),edges[:-1],6)
        with self.assertRaises(ValueError):
            six_incidence_projection_capacity((0,0,0,1,2,3),edges,6)
        with self.assertRaises(ValueError):
            six_incidence_projection_capacity(tuple(range(6)),((0,0),)+edges[1:],6)
        with self.assertRaises(ValueError):
            six_incidence_projection_capacity(tuple(range(6)),edges,5)
        with self.assertRaises(ValueError):
            six_incidence_projection_capacity(tuple(range(6)),edges,True)

    def test_003_all_h_conditional_average_not_per_pair_lower(self):
        for h in range(1,13):
            s=2**h
            zero=conditional_average_transfer(s,0)
            self.assertEqual(zero["conditional_seven_Q_lower_using_sharp_projection_9"],0)
            r=conditional_average_transfer(s,s)
            self.assertTrue(r["conditional_seven_Q_lower_using_sharp_projection_9"]>=
                            r["AA4J_conditional_seven_Q_lower_using_loose_15"])
            self.assertFalse(r["any_global_positive_average_claim_ESTABLISHED"])
            self.assertFalse(r["root_all_h_seven_positive_PROVED"])
            if s>=4:
                self.assertTrue(r["all_h_if_average_at_least_c_s_then_S_at_least_c_s6_over36"])
                self.assertGreaterEqual(
                    r["conditional_seven_Q_lower_using_sharp_projection_9"],
                    _ceil(Fraction(s**6,36)))
        with self.assertRaises(ValueError):
            conditional_average_transfer(4,-1)

    def test_004_all_true_original_W32_baselines_class_oriented_certified_GF5(self):
        known={"lex":259,"reverse":169,"S68":68,"S72":72}
        for scheme,S in known.items():
            m=fixture(1,scheme)
            g=geometry(2,m["incidences"])
            c=seven_census(m,independent_checks=False,witness_sets=True)
            self.assertEqual(c["S_seven"],S)
            r=true_original_projection_charge(g,m,c["sets"])
            self.assertEqual(r["original_seven_Q"],S)
            self.assertEqual(r["selected_GF5_51palette_numerator"],
                             c["GF5_seven_lower_numerator"])
            self.assertEqual(sum(z["count"] for z in
                                 r["true_ORIGINAL_Q_by_class"].values()),S)
            self.assertEqual(sum(r["genuine_original_Q_by_independent_half_projection_kind"].values()),S)
            self.assertEqual(r["independent_AA4J_pair_major_charge_oracle"],"PASS")
            self.assertEqual(r["all_7_classes_in_GF5_numerator_ratio"],7)
            self.assertGreaterEqual(r["source_P_projection_aware_S_floor"],
                                    _ceil(Fraction(r["source_P_charge"],15)))
            self.assertGreaterEqual(r["source_L_projection_aware_S_floor"],
                                    _ceil(Fraction(r["source_L_charge"],15)))
            self.assertGreaterEqual(r["joint_projection_aware_S_floor"],
                                    r["joint_loose_AA4J_S_floor"])
            self.assertLessEqual(r["joint_projection_aware_S_floor"],S)
            self.assertLessEqual(r["selected_GF5_numerator_floor_from_joint_charge"],
                                 c["GF5_seven_lower_numerator"])
            self.assertLessEqual(r["joint_source_pair_to_original_GF5_positive_Q_charge"],
                                 r["joint_A_B_C_projection_disjoint_capacity"])

    def test_005_original_class_per_Q_exact_cap_and_total_by_TAG(self):
        m=fixture(1,"S72")
        g=geometry(2,m["incidences"])
        c=seven_census(m,independent_checks=False,witness_sets=True)
        r=true_original_projection_charge(g,m,c["sets"])
        x=r["true_ORIGINAL_Q_by_class"]
        for tag,stats in x.items():
            self.assertIn(tag,R3_CERTIFIED_FLOORS)
            self.assertEqual(stats["weighted_51floor"],stats["count"]*R3_CERTIFIED_FLOORS[tag])
            allowed=TAG_TYPES[tag]
            allowed_caps={p+"P":PATTERN_CAP[p] for p,l in allowed}
            self.assertLessEqual(stats["P_charge"],stats["P_cap"])
            self.assertLessEqual(stats["L_charge"],stats["L_cap"])
            self.assertLessEqual(stats["P_cap"],
                                 stats["count"]*max(PATTERN_CAP[p] for p,l in allowed))
            self.assertLessEqual(stats["L_cap"],
                                 stats["count"]*max(PATTERN_CAP[l] for p,l in allowed))
        self.assertEqual(sum(z["P_charge"] for z in x.values()),r["source_P_charge"])
        self.assertEqual(sum(z["L_charge"] for z in x.values()),r["source_L_charge"])
        self.assertEqual(sum(z["P_cap"]+z["L_cap"] for z in x.values()),
                         r["joint_A_B_C_projection_disjoint_capacity"])

    def test_006_all_real_W32_random_global_maps_without_physical_P3_surrogate(self):
        m=fixture(1,"lex")
        g=geometry(2,m["incidences"])
        pairs=list(combinations(range(6),2))
        rng=random.Random(2300443)
        for _ in range(4):
            rng.shuffle(pairs)
            left=tuple(pairs)
            rng.shuffle(pairs)
            right=tuple(pairs)
            current={**m,"left_labels":left,"right_labels":right}
            c=seven_census(current,independent_checks=False,witness_sets=True)
            r=true_original_projection_charge(g,current,c["sets"])
            self.assertEqual(r["original_seven_Q"],c["S_seven"])
            self.assertEqual(r["independent_AA4J_pair_major_charge_oracle"],"PASS")
            self.assertLessEqual(r["source_P_charge"],9*r["original_seven_Q"])
            self.assertLessEqual(r["source_L_charge"],9*r["original_seven_Q"])
            self.assertFalse(r["all_h_root_s6_PROVED"])

    def test_007_incompatible_source_class_tag_rejected(self):
        m=fixture(1,"S68")
        g=geometry(2,m["incidences"])
        c=seven_census(m,independent_checks=False,witness_sets=True)
        # Reclassifying a genuine ORIGINAL sixset with a conflicting
        # A/B/C type violates the independent two-half geometry audit.
        Q,tag=next(iter(c["sets"].items()))
        possible=("D6","B-left/A-right","A-left/B-right",
                  "C/A","C/B","B/B-overlap","B/B-disjoint")
        endpoints=tuple(m["incidences"][i] for i in Q)
        from hyp105_g5e2b3e1a_fixed_leading import _half_projection_kind
        k=(_half_projection_kind([p for p,l in endpoints],m["left_labels"]),
           _half_projection_kind([l for p,l in endpoints],m["right_labels"]))
        bad=next(x for x in possible if k not in TAG_TYPES[x])
        with self.assertRaises(AssertionError):
            true_original_projection_charge(g,m,{Q:bad})
        with self.assertRaises(ValueError):
            true_original_projection_charge(g,m,{(0,1,2,3,4):"D6"})
        with self.assertRaises(ValueError):
            true_original_projection_charge(g,m,{Q:"FAKE-SEVEN-CLASS"})

    def test_008_explicit_proper_six_coordinate_necessity(self):
        m=fixture(1,"S68")
        g=geometry(2,m["incidences"])
        q=seven_census(m,independent_checks=False,witness_sets=True)["sets"]
        for Q,tag in list(q.items())[:30]:
            original=tuple(m["incidences"][i] for i in Q)
            for t,slot in (("P",0),("L",1)):
                labels=m["left_labels" if t=="P" else "right_labels"]
                row=six_incidence_projection_capacity(
                    tuple(e[slot] for e in original),labels,6)
                self.assertIn(row["true_original_source_projection_kind"],PATTERN_CAP)
                self.assertEqual(row["ALL_physically_disjoint_original_factor_pairs"],
                                 row["exact_A_B_C_source_pair_disjoint_capacity"])


if __name__=="__main__":
    unittest.main()
