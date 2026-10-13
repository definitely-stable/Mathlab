"""Independent true ORIGINAL JPKC-006 4/24 seed-charge and U topology gates."""
from collections import Counter
from itertools import combinations
import unittest

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_issue230_jpkc002_path_collision_taxonomy import _path_fibers
from hyp105_issue230_jpkc005_alternate_three_completion import (
    _bad_seed_paths, _physical_seed_counts_by_Q,
)
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_jpkc006_source_topology_sharp_charge import (
    _signature, _local_three_source_paths,
    _other_source_completion, sharp_charge_certificate,
    J18_SHARP_SOURCE_TRIPLE_REALIZATIONS,
    J19_SELECTED_SOURCE_SIXSET_CAP,J19_CLASS_CAPS,
)


class JPKC006ProofGates(unittest.TestCase):
    def test_W32_exact_all_4_original_global_maps_and_oracle(self):
        expected={
            # s, E, S, number covered, positive original (P,Q) hits
            "lex":(786,259,154,214),
            "reverse":(676,169,86,90),
            "S68":(544,68,8,8),
            "S72":(600,72,10,10),
        }
        for scheme,(E,S,covered,hits) in expected.items():
            with self.subTest(scheme=scheme):
                c=sharp_charge_certificate(fixture(1,scheme))
                self.assertTrue(c["complete_endpoint_bad_coverage"])
                self.assertEqual(c["endpoint_bad_physical_seeds_examined"],E)
                self.assertEqual(c["seeds_with_true_original_positive_alternates"],covered)
                self.assertEqual(c["accepted_seed_sixset_pairs"],hits)
                self.assertTrue(c["full_W32_independent_accepted_Q_oracle_compared"])
                self.assertLessEqual(c["max_realized_complete_source_three_seed"],2)
                self.assertLessEqual(c["max_physical_P3_per_accepted_Q_in_sample"],12)
                if scheme=="lex":
                    self.assertEqual(
                        c["max_physical_P3_per_accepted_Q_in_sample"],12,
                        "J19 D6=12 upper is attained on W32 lex real original maps")
                self.assertTrue(c["J18_all_h_2_source_triple_cap_verified"])
                self.assertTrue(c["J19_all_h_12_selected_sixset_cap_verified"])
                self.assertTrue(c["J20_all_h_only_matching_or_wedge_nonGQ_complements"])
                self.assertEqual(sum(c["selected_class_positive_source_hits"].values()),hits)
                self.assertEqual(sum(c["U_source_topology"].values()),hits)
                self.assertEqual(c["U_source_topology"]["GQ_P4"],0)
                self.assertEqual(c["U_source_topology"]["other"],0)
                self.assertEqual(c["selected_class_positive_source_hits"]["B/B-overlap"],0)
                self.assertEqual(c["selected_class_positive_source_hits"]["B/B-disjoint"],0)
                self.assertEqual(c["selected_class_positive_source_hits"]["C/A"],0)
                self.assertEqual(c["selected_class_positive_source_hits"]["C/B"],0)
                self.assertFalse(c["Root_A_proved"])

    def test_all_W32_accepted_sixsets_independent_12_and_8_class_caps(self):
        for scheme in ("S68","S72","lex"):
            with self.subTest(scheme=scheme):
                model=fixture(1,scheme)
                ctx=ProjectionClosure(model)
                source=seven_census(model,independent_checks=False,witness_sets=True)
                # Direct local source-3 diagonal assignment oracle, not
                # global original path-fiber counter or GF5 weighted proxy.
                for Q,tag in source["sets"].items():
                    total=sum(len(_local_three_source_paths(ctx,T))
                              for T in combinations(Q,3))
                    self.assertLessEqual(total,J19_CLASS_CAPS[tag])
                    self.assertLessEqual(total,J19_SELECTED_SOURCE_SIXSET_CAP)
                    if total:
                        # Every proper source P3 has exactly two
                        # orientations of the same physical graph P4.
                        self.assertEqual(total%2,0)
                    self.assertLessEqual(total,12)
                _,fibers,_=_path_fibers(ctx,2_000_000)
                old=_physical_seed_counts_by_Q(ctx,fibers,source["sets"])
                self.assertTrue(all(count<=12 for count in old.values()))

    def test_source_topology_true_GQ_wedge_matching_and_nonGQ(self):
        for scheme in ("S68","S72","lex"):
            ctx=ProjectionClosure(fixture(1,scheme))
            _,fibers,_=_path_fibers(ctx,2_000_000)
            from hyp105_issue230_jpkc005_alternate_three_completion import _other_gq_anchor
            for path,T,(q,r) in _bad_seed_paths(ctx,fibers):
                for Q,tag in _other_source_completion(ctx,path,T,(q,r)).items():
                    U=tuple(sorted(set(Q)-set(T)))
                    source=_signature(ctx,U)
                    expected={"D6":"matching_3K2",
                              "B-left/A-right":"point_wedge_plus_edge",
                              "A-left/B-right":"line_wedge_plus_edge"}[tag]
                    self.assertEqual(source,expected)
                    self.assertIsNone(_other_gq_anchor(ctx,U))
                    self.assertLessEqual(
                        len(_local_three_source_paths(ctx,T)),2)

    def test_targeted_true_original_W34_not_falsely_full_census(self):
        for scheme in ("lex","random"):
            with self.subTest(scheme=scheme):
                c=sharp_charge_certificate(
                    fixture(2,scheme),limit_endpoint_seeds=96,exact_W32=False)
                self.assertEqual(c["endpoint_bad_physical_seeds_examined"],96)
                self.assertFalse(c["complete_endpoint_bad_coverage"])
                self.assertTrue(c["no_full_W34_Q_census"])
                self.assertFalse(c["full_W32_independent_accepted_Q_oracle_compared"])
                self.assertEqual(sum(c["U_source_topology"].values()),
                                 c["accepted_seed_sixset_pairs"])
                self.assertLessEqual(c["max_physical_P3_per_accepted_Q_in_sample"],12)

    def test_true_original_D4_spread_W34_targeted_structural_falsifier(self):
        from hyp105_issue230_jpkc_spread_adversary import spread_adversary_model
        model,proof=spread_adversary_model(2)
        self.assertEqual(proof["M_f_original_exact"],259)
        c=sharp_charge_certificate(model,limit_endpoint_seeds=96,exact_W32=False)
        self.assertEqual(c["endpoint_bad_physical_seeds_examined"],96)
        self.assertFalse(c["complete_endpoint_bad_coverage"])
        self.assertTrue(c["J19_all_h_12_selected_sixset_cap_verified"])
        self.assertFalse(c["Root_B_constructed"])

    def test_fail_closed_limits_and_illegal_physical_maps(self):
        with self.assertRaisesRegex(ValueError,"W32 only"):
            sharp_charge_certificate(fixture(2,"lex"),exact_W32=True)
        with self.assertRaisesRegex(ValueError,"positive selected"):
            sharp_charge_certificate(fixture(1,"lex"),limit_endpoint_seeds=0)
        with self.assertRaisesRegex(ValueError,"path budget"):
            sharp_charge_certificate(fixture(1,"lex"),max_paths=1)
        model=fixture(1,"lex")
        labels=list(model["right_labels"])
        labels[0]=labels[1]
        model["right_labels"]=tuple(labels)
        with self.assertRaises(ValueError):
            sharp_charge_certificate(model)
        ctx=ProjectionClosure(fixture(1,"S68"))
        with self.assertRaisesRegex(ValueError,"three DISTINCT"):
            _signature(ctx,(1,1,2))


if __name__=="__main__":
    unittest.main()
