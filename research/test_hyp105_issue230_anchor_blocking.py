"""Independent finite falsifiers for full ORIGINAL projection-blocking ledger."""
import unittest

from hyp105_issue230_projection import ProjectionClosure, fixture
from hyp105_issue230_anchor_blocking import (
    _bits, _original_endpoint_pair_census, anchor_ledger,
)


class Issue230AnchorBlockingTests(unittest.TestCase):
    def test_four_bits_are_distinct_and_orientation_invariant(self):
        left=(0,1,2,3)
        right=(4,5,6,7)
        for mask in range(16):
            lf=tuple([0 if mask&1 else 9,1 if mask&2 else 10])
            rg=tuple([4 if mask&4 else 11,5 if mask&8 else 12])
            self.assertEqual(_bits(left,right,lf,rg),mask)
            self.assertEqual(_bits(left[::-1],right[::-1],lf,rg),mask)

    def test_original_dual_endpoint_pair_identities_ALL_W32_states(self):
        for scheme in ("lex","reverse","S68","S72"):
            with self.subTest(scheme=scheme):
                core=ProjectionClosure(fixture(1,scheme))
                summary,left,right=_original_endpoint_pair_census(core)
                self.assertEqual(summary["actual_original_nonincident_endpoint_pairs"],180)
                self.assertEqual(summary["left_endpoint_bad_pair_count"],
                                 summary["left_original_GQ_ordered_pencil_pair_formula"])
                self.assertEqual(summary["right_endpoint_bad_pair_count"],
                                 summary["right_true_dual_GQ_ordered_pencil_pair_formula"])
                self.assertEqual(summary["joint_endpoint_bad_pair_count"],len(left&right))

    def test_lex_W32_full_16atom_and_independent_middle_edge(self):
        row=anchor_ledger(fixture(1,"lex"),verify_middle_edges=True)
        self.assertEqual((row["proper_P3"],row["missing"],row["incident"],
                          row["blocked"],row["unblocked"]),(1346,0,400,942,4))
        self.assertEqual(row["synchronized_BB_overlap_sixsets"],2)
        self.assertTrue(row["independent_original_endpair_middle_edge_oracle"])
        self.assertEqual(sum(row["exact_sixteen_mask_histogram"]),
                         row["blocked"]+row["unblocked"])
        self.assertEqual(row["exact_sixteen_mask_histogram"][0],4)
        self.assertEqual(sum(row["exact_sixteen_mask_histogram"][1:]),942)

    def test_S68_false_P2_P7_but_original_blocking_exact(self):
        row=anchor_ledger(fixture(1,"S68"),verify_middle_edges=True)
        self.assertEqual((row["proper_P3"],row["missing"],row["incident"],
                          row["blocked"],row["unblocked"]),(678,0,72,606,0))
        self.assertEqual(row["synchronized_BB_overlap_sixsets"],0)
        self.assertGreater(row["max_bad_original_endpoint_pair_path_multiplicity"],0)
        self.assertEqual(row["endpoint_bad_pair_weight"],
                         row["endpoint_only_weight"]+row["mixed_endpoint_internal_weight"])
        self.assertFalse(row["universal_S_lower_proved"])
        self.assertFalse(row["all_h_blocking_upper_proved"])

    def test_reverse_and_S72_W32_exact_parent_ledger(self):
        for scheme,tup in (("reverse",(1154,0,256,898,0)),
                           ("S72",(738,0,80,658,0))):
            with self.subTest(scheme=scheme):
                row=anchor_ledger(fixture(1,scheme),verify_middle_edges=True)
                self.assertEqual((row["proper_P3"],row["missing"],
                                  row["incident"],row["blocked"],
                                  row["unblocked"]),tup)

    def test_complete_random_W34_independent_16atom(self):
        row=anchor_ledger(fixture(2,"random"),verify_middle_edges=True)
        self.assertEqual((row["proper_P3"],row["missing"],row["incident"],
                          row["blocked"],row["unblocked"]),
                         (78894,10198,4112,48542,16042))
        self.assertEqual(row["synchronized_BB_overlap_sixsets"],8021)
        self.assertTrue(row["independent_original_endpair_middle_edge_oracle"])
        self.assertEqual(row["nonincident_endpoint_complete"],64584)
        self.assertGreater(row["internal_only_weight"],0)

    def test_complete_lex_W34_independent_16atom(self):
        row=anchor_ledger(fixture(2,"lex"),verify_middle_edges=True)
        self.assertEqual((row["proper_P3"],row["missing"],row["incident"],
                          row["blocked"],row["unblocked"]),
                         (83892,8860,4584,55384,15064))
        self.assertEqual(row["synchronized_BB_overlap_sixsets"],7532)

    def test_fail_closed_budget(self):
        with self.assertRaises(ValueError):
            anchor_ledger(fixture(1,"lex"),max_paths=1)
        with self.assertRaises(ValueError):
            anchor_ledger(fixture(1,"lex"),max_paths=-1)
        with self.assertRaises(ValueError):
            anchor_ledger(fixture(1,"lex"),max_paths=True)

    def test_exact_pair_masks_partition_all_nonincident_paths(self):
        for scheme in ("S68","lex"):
            with self.subTest(scheme=scheme):
                x=anchor_ledger(fixture(1,scheme),verify_middle_edges=True)
                self.assertEqual(x["blocked"],x["endpoint_only_weight"]+
                                 x["internal_only_weight"]+
                                 x["mixed_endpoint_internal_weight"])
                self.assertEqual(x["endpoint_bad_pair_weight"],
                                 x["left_endpoint_bad_pair_weight"]+
                                 x["right_endpoint_bad_pair_weight"]-
                                 (sum(v for mask,v in
                                      enumerate(x["exact_sixteen_mask_histogram"])
                                      if (mask&5)==5)))
                self.assertTrue(all(v%2==0 for v in
                                    x["exact_sixteen_mask_histogram"]))


if __name__=="__main__":
    unittest.main()
