"""Independent acceptance evidence regression; not an automatic theorem verifier."""
import csv
import json
import tempfile
import unittest
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

from hyp105_branch_a_final_evidence_review import (
    set_partitions,encode,named_catalog,profile,projection_sizes,forest_components,
    leading_class,joint_case,certificate,write_artifacts,FLOORS,
)
from hyp105_g5e2b3_forests import six_forest_power_report


class TestFinalEvidence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows=named_catalog()
        cls.cert=certificate(cls.rows)

    def test_01_Bell_6_named_partitions(self):
        p=[encode(z) for z in set_partitions(tuple(range(6)))]
        self.assertEqual(len(p),203)
        self.assertEqual(len(set(p)),203)
        for z in p:
            self.assertEqual(z[0],0)
            for i in range(1,6):
                self.assertLessEqual(z[i],1+max(z[:i]))

    def test_02_complete_named_catalog_unique(self):
        self.assertEqual(len(self.rows),11663)
        self.assertEqual(len({z["id"] for z in self.rows}),11663)
        self.assertEqual(self.cert["by_stratum"],
                         {"LEADING":631,"SUBLEADING_NECESSARY_ONLY":11032})

    def test_03_histogram_agrees_historical_independent_power_report(self):
        h=six_forest_power_report()
        self.assertEqual(h["admissible_leafless_factor_forest_shapes"],11663)
        self.assertEqual(h["shape_exponents"],self.cert["by_power"])

    def test_04_no_duplicate_source_or_cyclic_factor_shape(self):
        self.assertIsNone(forest_components((0,0,1,2,3,4),(0,0,1,2,3,4)))
        self.assertIsNone(forest_components((0,0,1,1,2,3),(0,1,0,1,2,3)))
        self.assertEqual(forest_components(tuple(range(6)),tuple(range(6))),6)
        for z in self.rows:
            self.assertEqual(forest_components(z["left_partition"],z["right_partition"]),
                             z["components"])

    def test_05_independent_typed_projection_sizes_and_exponent(self):
        for z in self.rows:
            l=tuple(z["left_profile"]);r=tuple(z["right_profile"])
            self.assertEqual(list(projection_sizes(l)),z["left_leafless_sizes"])
            self.assertEqual(list(projection_sizes(r)),z["right_leafless_sizes"])
            vf,vg=max(z["left_leafless_sizes"]),max(z["right_leafless_sizes"])
            self.assertEqual(Q(z["independent_label_necessary_power"]),Q(3,2)*(vf+vg)-12)
            self.assertFalse(z["all_physical_templates_positive"])

    def test_06_exact_leading_source_partition_categories(self):
        self.assertEqual(self.cert["leading_partition_categories"],{
            "A/A (D6 subset; other physical templates not accepted)":1,
            "B-left/A-right":15,"A-left/B-right":15,"C/A":30,"C/B":360,
            "B/B-overlap":120,"B/B-disjoint":90})

    def test_07_no_subleading_positivity_or_fixed_map_extrapolation(self):
        for z in self.rows:
            if z["stratum"]=="SUBLEADING_NECESSARY_ONLY":
                self.assertIsNone(z["historical_class"])
                self.assertLess(Q(z["independent_label_necessary_power"]),6)
        self.assertTrue(self.cert["subleading_not_GF5_positive_classified"])
        self.assertFalse(self.cert["fixed_label_subleading_upper_claimed"])

    def test_08_same_map_includes_exact_all_seven_and_Q4(self):
        cc=self.cert["same_map_joint_cases"]
        self.assertEqual({x["scheme"] for x in cc},{"lex","reverse","correlated"})
        self.assertEqual(len({x["same_original_map_sha256"] for x in cc}),3)
        for z in cc:
            self.assertEqual(z["s"],2)
            self.assertEqual(z["original_source_flags"],45)
            self.assertEqual(set(z["counts"]),set(FLOORS))
            self.assertTrue(z["independent_source_sets_agree"])
            self.assertTrue(z["independent_Q4_count_agrees"])
            self.assertEqual(z["S_seven"],sum(z["counts"].values()))
            self.assertEqual(z["D6_plus_BBo"],z["counts"]["D6"]+z["counts"]["B/B-overlap"])

    def test_09_historical_W32_lex_and_reverse_baselines_on_identical_map(self):
        for name,d6,counts in (
            ("lex",15,(13,1,8,14)),("reverse",3,(1,1,7,6))):
            z=joint_case(name)["counts"]
            self.assertEqual(z["D6"],d6)
            self.assertEqual(tuple(z[k] for k in ("C/A","C/B","B/B-overlap","B/B-disjoint")),counts)

    def test_10_true_same_map_GF5_floor_not_full_risk(self):
        for z in self.cert["same_map_joint_cases"]:
            self.assertEqual(z["certified_R3_floor_numerator"],
                             sum(z["counts"][k]*w for k,w in FLOORS.items()))
            self.assertEqual(z["certified_R3_floor_denominator"],51**6)
            self.assertEqual(z["certified_Q4_R2_floor_numerator"],531*z["Q4"])
            self.assertEqual(z["certified_Q4_R2_floor_denominator"],51**4)
            self.assertFalse(z["full_weighted_R2_R3_computed"])

    def test_11_complete_JSON_CSV_artifact_roundtrip(self):
        with tempfile.TemporaryDirectory() as d:
            c=write_artifacts(d)
            path=Path(d)
            self.assertEqual(json.loads((path/"certificate.json").read_text()),c)
            raw=json.loads((path/"named_original_partition_index.json").read_text())
            self.assertEqual(raw,list(self.rows))
            with (path/"named_original_partition_index.csv").open(newline="") as f:
                rows=list(csv.DictReader(f))
            self.assertEqual(len(rows),11663)
            self.assertEqual([z["id"] for z in rows],[z["id"] for z in self.rows])

    def test_12_governance_external_review_and_postmerge_unverified(self):
        self.assertEqual(self.cert["issue"],230)
        self.assertEqual(self.cert["parent_pr"],787)
        self.assertEqual(self.cert["repository_status"],"OPEN_WITH_FORMAL_BLOCKER")
        self.assertEqual(self.cert["mathematical_review_verdict"],
                         "NO_FATAL_GAP_FOUND_INTERNAL_REVIEW")
        self.assertFalse(self.cert["independent_external_review_received"])
        self.assertFalse(self.cert["postmerge_main_CI_verified"])
        self.assertFalse(self.cert["new_ASET_exponent"])

if __name__=="__main__":
    unittest.main()
