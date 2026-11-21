"""Fail-closed two-class Branch A structural and exact numerical referee."""
import unittest
from fractions import Fraction as Q
from itertools import combinations

from hyp105_aa4_branch_a_integrated_referee import (
    certificate,root_exact_ledger,flow_catalog,gf5_nonzero_flows,
    source_d6,physical_d6,factor_first_d6,source_first_bbo_w32,
    proper_bbo_from_physical,actual_bbo_flow_topology,historical_bbo,
    verify_positive_cycle_cuts,canonical_cycle,
)
from hyp105_low_publication_partition_referee import model


class TestIntegratedBranchA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=certificate()

    def test_01_historical_palette_and_D6_signed_flow(self):
        f=self.c["direct_nonzero_palette_flow"]
        self.assertEqual(f["palette"],51)
        self.assertEqual(f["d6_alternating"],5643)

    def test_02_BBo_full_ten_sign_tree_count(self):
        f=self.c["direct_nonzero_palette_flow"]
        self.assertEqual(len(f["bbo_sign_counts"]),10)
        self.assertEqual(sum(f["bbo_sign_counts"]),53838)
        self.assertGreaterEqual(min(f["bbo_sign_counts"]),5175)
        self.assertGreater(f["bbo_balanced_total"],f["bbo_historical_floor"])

    def test_03_independent_true_W32_censuses(self):
        cases=self.c["genuine_W32_two_independent_source_censuses"]
        self.assertEqual({x["scheme"] for x in cases},
                         {"lex","reverse","correlated"})
        for x in cases:
            self.assertTrue(x["two_independent_D6_censuses_equal"])
            self.assertTrue(x["two_independent_BBo_censuses_equal"])
            self.assertGreaterEqual(x["D6"],0)
            self.assertGreaterEqual(x["produced_BBo"],0)

    def test_04_W32_lex_positive_source_D6_and_BBo(self):
        x=next(x for x in self.c["genuine_W32_two_independent_source_censuses"]
               if x["scheme"]=="lex")
        self.assertGreater(x["D6"],0)
        self.assertGreater(x["produced_BBo"],0)

    def test_05_W32_source_cycle_inverse_and_no_duplicates(self):
        m=model(2,"lex","full")
        c=physical_d6(m)
        self.assertEqual(c,factor_first_d6(m))
        for ids,cy in c.items():
            self.assertEqual(len(set(ids)),6)
            self.assertEqual(source_d6(m,ids),cy)
            self.assertEqual(len(set(x for x,y in cy)),6)
            self.assertEqual(len(set(y for x,y in cy)),6)

    def test_06_W32_BBo_reversal_and_historical_class(self):
        m=model(2,"lex","full")
        a=proper_bbo_from_physical(m)
        self.assertGreater(len(a),0)
        self.assertEqual(dict(a),source_first_bbo_w32(m))
        for ids,paths in a.items():
            self.assertTrue(historical_bbo(m,ids))
            self.assertEqual(len(paths),2)
            self.assertIn(next(iter(paths))[::-1],paths)
            self.assertTrue(actual_bbo_flow_topology(m,ids,next(iter(paths))))
            self.assertIsNone(source_d6(m,ids))

    def test_07_D6_and_BBo_distinct_source_profiles(self):
        m=model(2,"lex","full")
        d=physical_d6(m)
        b=proper_bbo_from_physical(m)
        self.assertTrue(set(d).isdisjoint(b))
        self.assertTrue(all(not historical_bbo(m,ids) for ids in d))

    def test_08_proper_source_cycle_cut_exact_global_probability(self):
        for x in self.c["genuine_W32_two_independent_source_censuses"]:
            if x["nonzero_cycle_cut"] is not None:
                c=x["nonzero_cycle_cut"]
                self.assertEqual(c["cut_assignments"],4096)
                self.assertEqual(c["coherent_global_cut_successes"],4)
                self.assertEqual(Q(c["probability"]),Q(1,1024))

    def test_09_nonvacuous_original_W34_D6(self):
        c=self.c["genuine_W34_positive_cycle"]
        self.assertEqual(len(set(c["original_ids"])),6)
        self.assertEqual(Q(c["probability"]),Q(1,1024))
        m=model(4,"lex","full")
        self.assertIsNotNone(source_d6(m,c["original_ids"]))

    def test_10_actual_W34_source_cycle_injection(self):
        m=model(4,"lex","full")
        ids=tuple(self.c["genuine_W34_positive_cycle"]["original_ids"])
        d=physical_d6(m,ids)
        self.assertEqual(len(d),1)
        self.assertEqual(d[ids],source_d6(m,ids))

    def test_11_exact_uniform_bound_ledger_and_constants(self):
        for z in self.c["formal_root_ledgers"]:
            self.assertEqual(z["R"],33281)
            self.assertEqual(z["K"],10)
            self.assertEqual(z["q2"],1936)
            self.assertEqual(z["q3"],85184)
            self.assertLess(Q(z["endpoint"]),17)
            self.assertLess(Q(z["book"]),46)
            self.assertTrue(z["FORMAL_ONLY"])
            self.assertTrue(z["theorem_constants_numeric_unknown"])

    def test_12_new_expected_source_cycle_bound_is_1024_fold(self):
        for z in self.c["formal_root_ledgers"]:
            self.assertEqual(Q(z["expected_C6_cut_upper"]),Q(1,1024))
            self.assertEqual(Q(z["sixth_D6_coefficient"]),Q(24,1024))

    def test_13_same_frozen_T_delta_and_exact_dyadic_threshold(self):
        for z in self.c["formal_root_ledgers"]:
            self.assertGreaterEqual(int(z["T"]),Q(17,2)*z["R"]**3*Q(z["C0"])**3)
            self.assertEqual(Q(z["delta"]),Q(z["c0"])/z["R"]**6)
            self.assertGreaterEqual(z["sufficient_h0"],32)

    def test_14_fail_closed_on_nonexact_or_invalid_external_constants(self):
        for C,c in [(1,Q(1)),(Q(1),1),(Q(0),Q(1)),(Q(1),Q(2)),(Q(1),Q(0))]:
            with self.assertRaises(ValueError):
                root_exact_ledger(C,c)

    def test_15_bad_source_cycle_six_ids_rejected(self):
        m=model(2,"lex","full")
        self.assertIsNone(source_d6(m,[1]*6))
        self.assertIsNone(source_d6(m,[0,1,2,3,4]))
        self.assertFalse(historical_bbo(m,[1]*6))

    def test_16_tree_oracle_bad_flow_inputs(self):
        with self.assertRaises(ValueError):
            gf5_nonzero_flows([(0,1)]*11,{0,1,2})
        with self.assertRaises(ValueError):
            gf5_nonzero_flows([(0,1)]*12,{0,1,2})
        with self.assertRaises(ValueError):
            gf5_nonzero_flows([(0,1)]*12,{0,1})

    def test_17_governance_not_automatic_ROOT_PROVED_A(self):
        c=self.c
        self.assertEqual(c["schema"],"mathlab.hyp105.branch-a-integrated.v1")
        self.assertEqual(c["parent_pr"],786)
        self.assertEqual(c["issue"],230)
        self.assertEqual(c["status"],"OPEN_WITH_FORMAL_BLOCKER")
        self.assertEqual(c["mathematical_candidate"],
                         "TWO_CLASS_BRANCH_A_COMPLETE_PROOF")
        self.assertFalse(c["repository_PROVED_A"])
        self.assertTrue(c["external_constants_numeric_unknown"])
        self.assertTrue(c["no_new_ASET_exponent"])

if __name__=="__main__":
    unittest.main()
