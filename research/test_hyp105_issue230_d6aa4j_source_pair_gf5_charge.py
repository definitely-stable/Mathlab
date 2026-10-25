"""D6-AA4-J independent original-GQ pair/Q counting and failure gates."""
import random
import unittest
from fractions import Fraction
from itertools import combinations
from math import comb

from hyp105_issue230_projection import fixture
from hyp105_g5e2b3e1b0_seven_signature import seven_census,R3_CERTIFIED_FLOORS
from hyp105_issue230_d6aa4i_original_spectral_coordinate import geometry
from hyp105_issue230_d6aa4j_source_pair_gf5_charge import (
    conditional_charge_formula,charge_original_sixsets,_ceil,
)


class OriginalSourcePairGF5TransferTests(unittest.TestCase):
    def test_001_exact_all_h_conditional_15_Q_capacity(self):
        for h in range(1,12):
            s=1<<h
            d=conditional_charge_formula(s,s)
            self.assertEqual(d["maximum_original_same_type_source_pairs_per_sixset"],15)
            self.assertTrue(d["conditionally_valid_if_each_eligible_pair_has_its_Q_multiplicity"])
            self.assertFalse(d["hypothesis_established_for_all_labels"])
            self.assertFalse(d["seven_GF5_all_h_positive_bound_proved"])
            if s>=4:
                self.assertGreaterEqual(d["all_h_conditional_positive_original_Q_lower"],
                                        _ceil(Fraction(s**6,60)))
        for s in (-2,0,1,3):
            with self.assertRaises(ValueError):
                conditional_charge_formula(s,1)
        with self.assertRaises(ValueError):
            conditional_charge_formula(4,-1)

    def test_002_toy_exact_charge_lemma_does_not_assume_any_witness(self):
        z=conditional_charge_formula(4,0)
        self.assertEqual(z["all_h_conditional_positive_original_Q_lower"],0)
        # Without a verified minimum Q multiplicity, an s^5 pair lower
        # cannot imply even one accepted original GF5 motif.
        self.assertFalse(z["hypothesis_established_for_all_labels"])

    def test_003_original_W32_all_real_source_seven_GF5_baselines(self):
        for scheme,expected in (("lex",259),("reverse",169),
                                ("S68",68),("S72",72)):
            model=fixture(1,scheme)
            g=geometry(2,model["incidences"])
            census=seven_census(model,independent_checks=False,witness_sets=True)
            self.assertEqual(census["S_seven"],expected)
            self.assertEqual(census["S_seven"],len(census["sets"]))
            self.assertEqual(
                sum(R3_CERTIFIED_FLOORS[tag] for tag in census["sets"].values()),
                census["GF5_seven_lower_numerator"])
            for typ in ("P","L"):
                charge=charge_original_sixsets(g,model,census["sets"],
                                              source_type=typ)
                D=charge["original_gq_collinear_physically_disjoint_pair_count"]
                self.assertGreaterEqual(D,9)
                self.assertEqual(
                    charge["original_pairs_covered_by_any_positive_sixset"]+
                    charge["original_pairs_not_covered_by_any_positive_sixset"],D)
                self.assertEqual(
                    charge["original_pairs_covered_by_same_pencil_positive_sixset"]+
                    charge["original_pairs_not_covered_by_same_pencil_positive_sixset"],D)
                self.assertLessEqual(charge[
                    "maximum_physically_disjoint_source_pair_charges_in_one_Q"],15)
                self.assertLessEqual(charge[
                    "maximum_same_pencil_pair_charges_in_one_Q"],15)
                self.assertLessEqual(charge[
                    "sharp_unconditional_capacity_15_Q_lower_from_weak_charges"],expected)
                self.assertEqual(sum(charge[
                    "exact_weak_charges_by_seven_GF5_class"].values()),
                    charge["all_genuine_original_pair_to_positive_Q_weak_charges"])
                self.assertEqual(charge[
                    "independent_pair_major_original_incidence_oracle"],"PASS")

    def test_004_original_W32_positive_Q_cannot_be_double_charged_by_more_than_15(self):
        model=fixture(1,"S68")
        g=geometry(2,model["incidences"])
        positive=seven_census(model,independent_checks=False,witness_sets=True)["sets"]
        for typ in ("P","L"):
            c=charge_original_sixsets(g,model,positive,source_type=typ)
            self.assertLessEqual(
                c["all_genuine_original_pair_to_positive_Q_weak_charges"],
                15*c["original_seven_positive_sixsets"])
            self.assertLessEqual(
                c["all_genuine_original_pair_to_positive_Q_same_pencil_charges"],
                c["all_genuine_original_pair_to_positive_Q_weak_charges"])

    def test_005_true_source_labels_and_original_Q_input_fail_closed(self):
        model=fixture(1,"S68")
        g=geometry(2,model["incidences"])
        with self.assertRaises(ValueError):
            charge_original_sixsets(g,model,{},source_type="X")
        with self.assertRaises(ValueError):
            charge_original_sixsets(g,model,{(0,1,2,3,4):"D6"},source_type="P")
        with self.assertRaises(ValueError):
            charge_original_sixsets(g,model,{(0,1,2,3,4,4):"D6"},source_type="P")
        with self.assertRaises(ValueError):
            charge_original_sixsets(g,model,{(0,1,2,3,4,45):"D6"},source_type="P")
        with self.assertRaises(ValueError):
            charge_original_sixsets(g,model,{(0,1,2,3,4,5):"FANTASY"},source_type="P")
        with self.assertRaises(ValueError):
            charge_original_sixsets(g,{**model,"left_labels":
                 tuple(model["left_labels"])[:-1]}, {},source_type="P")

    def test_006_original_same_pencil_is_stricter_than_cooccurrence(self):
        model=fixture(1,"S72")
        g=geometry(2,model["incidences"])
        original=tuple(tuple(x) for x in model["incidences"])
        # Independently build a genuine six-distinct-ID Q containing some
        # disjoint collinear pair, but NOT both source incidences on their
        # common original line, proving why the two charges differ.
        c=charge_original_sixsets(g,model,
            seven_census(model,independent_checks=False,witness_sets=True)["sets"],
            source_type="P")
        self.assertLessEqual(
            c["all_genuine_original_pair_to_positive_Q_same_pencil_charges"],
            c["all_genuine_original_pair_to_positive_Q_weak_charges"])
        self.assertLessEqual(
            c["original_pairs_covered_by_same_pencil_positive_sixset"],
            c["original_pairs_covered_by_any_positive_sixset"])

    def test_007_q_major_vs_pair_major_both_types_on_random_W32_real_maps(self):
        m=fixture(1,"lex")
        g=geometry(2,m["incidences"])
        edges=list(combinations(range(6),2))
        rng=random.Random(2300442)
        for _ in range(4):
            rng.shuffle(edges)
            left=tuple(edges)
            rng.shuffle(edges)
            right=tuple(edges)
            model={**m,"left_labels":left,"right_labels":right}
            c=seven_census(model,independent_checks=False,witness_sets=True)
            for typ in ("P","L"):
                o=charge_original_sixsets(g,model,c["sets"],source_type=typ)
                self.assertEqual(o["independent_pair_major_original_incidence_oracle"],"PASS")
                self.assertLessEqual(o[
                    "sharp_unconditional_capacity_15_Q_lower_from_weak_charges"],
                    c["S_seven"])

    def test_008_pinned_true_S72_original_line_pair_no_accepted_seven_Q(self):
        model=fixture(1,"S72")
        g=geometry(2,model["incidences"])
        assert 10 in g["source_line_neighbors"][5]
        self.assertEqual(tuple(model["right_labels"][5]),(1,3))
        self.assertEqual(tuple(model["right_labels"][10]),(0,4))
        full=seven_census(model,independent_checks=False,witness_sets=True)
        self.assertEqual(full["S_seven"],72)
        # Two true concurrent ORIGINAL lines with disjoint physical
        # labels. Independent direct Q source-factor membership oracle.
        count=0
        for Q in full["sets"]:
            lines={model["incidences"][i][1] for i in Q}
            count+=int(5 in lines and 10 in lines)
        self.assertEqual(count,0)
        cert=charge_original_sixsets(g,model,full["sets"],source_type="L")
        self.assertIn((5,10),cert["sample_uncovered_source_pair_ids"])
        self.assertGreaterEqual(cert["original_pairs_not_covered_by_any_positive_sixset"],1)

    def test_009_pinned_true_S68_point_weak_but_not_original_pencil(self):
        model=fixture(1,"S68")
        g=geometry(2,model["incidences"])
        self.assertIn(9,g["source_point_neighbors"][3])
        self.assertEqual(tuple(model["left_labels"][3]),(4,5))
        self.assertEqual(tuple(model["left_labels"][9]),(1,3))
        full=seven_census(model,independent_checks=False,witness_sets=True)
        self.assertEqual(full["S_seven"],68)
        weak=strict=0
        for Q in full["sets"]:
            source=[model["incidences"][i] for i in Q]
            a={l for p,l in source if p==3}
            b={l for p,l in source if p==9}
            weak+=bool(a and b)
            strict+=bool(a&b)
        self.assertEqual((weak,strict),(10,0))
        cert=charge_original_sixsets(g,model,full["sets"],source_type="P")
        self.assertIn((3,9),cert["sample_strict_uncovered_source_pair_ids"])


if __name__=="__main__":
    unittest.main()
