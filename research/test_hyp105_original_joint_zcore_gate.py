"""Independent all-original falsifiers for AA4-JOINTZCORE / #230."""
import unittest
from fractions import Fraction
from math import comb

from hyp105_original_joint_zcore_gate import (
    canonical_joint_original_certificates,
    projection_anchor_exposure,
    prune_genuine_original_source,
    uniform_original_joint_gate,
    verify_at_dyadic_h,
)


class TestActualOriginalJointGate(unittest.TestCase):
    def test_three_formal_exact_allh_thresholds_and_no_promotion(self):
        for C,c in ((Fraction(1),Fraction(1)),
                    (Fraction(2),Fraction(1,5)),
                    (Fraction(7,3),Fraction(1,17))):
            with self.subTest(C=C,c=c):
                z=uniform_original_joint_gate(C,c)
                self.assertFalse(z["root_230_mathematical_acceptance"])
                self.assertEqual(z["lowtail_W3_coefficient"],Fraction(27,16))
                self.assertEqual(z["lowtail_BBo_coefficient"],Fraction(5,32))
                self.assertEqual(z["rho"],Fraction(1,12*z["q3"]**2*z["L6"]))
                self.assertTrue(verify_at_dyadic_h(z,z["h0"])["all_sufficient"])
                self.assertTrue(verify_at_dyadic_h(z,z["h0"]+1)["all_sufficient"])
                self.assertFalse(verify_at_dyadic_h(z,z["h0"]-1)["all_sufficient"])

    def test_actual_old_to_new_mask_radius_gain_only_formal(self):
        z=uniform_original_joint_gate(Fraction(1),Fraction(1))
        gain=z["rho"]/z["old_rho"]
        # Parent used larger T and weaker sigma3, sixth moment and leading mass.
        self.assertGreater(gain,18000)
        self.assertLess(gain,20000)
        self.assertLessEqual(z["rho"],Fraction(1,32))
        self.assertEqual(z["T"],2**64)
        self.assertEqual(z["delta"],Fraction(1,2**120))
        self.assertEqual(12*z["rho"]*z["q3"]**2*z["L6"],1)

    def test_genuine_W32_W34_full_source_heavy_low_core_deletions(self):
        for h in (1,2):
            for scheme in ("lex","reverse-line"):
                with self.subTest(h=h,scheme=scheme):
                    # Exercise a TRUE heavy full-Q source prune (small diagnostic T).
                    z=prune_genuine_original_source(
                        h,scheme,Fraction(1,2),2,[0] if h==1 else list(range(1,425,31)))
                    self.assertTrue(z["verified"])
                    self.assertEqual(z["full_edges"],2*z["source_original_count"])
                    self.assertEqual(z["original_core_budget_exact"],z["original_core_flag_count"])
                    self.assertLessEqual(z["original_heavy_owner_deletion_loss"],
                                         2*z["original_source_deleted_ids"])
                    self.assertEqual(z["core_physical_edge_count"],
                                     2*z["original_core_flag_count"])
                    self.assertLessEqual(z["core_max_original_conflict"],2)
                    self.assertLessEqual(z["core_max_physical_degree"],
                                         Fraction(z["s"],2))

    def test_original_noheavy_lowcore_and_correlated_complete_maps(self):
        for h in (1,2):
            for scheme in ("lex","reverse-line"):
                with self.subTest(h=h,scheme=scheme):
                    Z=[0] if h==1 else list(range(1,425,31))
                    z=prune_genuine_original_source(h,scheme,Fraction(20),64,Z)
                    self.assertEqual(z["full_high_vertices"],0)
                    self.assertEqual(z["full_heavy_physical_edges"],0)
                    self.assertEqual(z["original_full_high_conflict_flags"],0)
                    self.assertEqual(z["original_core_flag_count"],
                                     z["source_original_count"]-len(Z))
                    self.assertGreater(z["original_Qx"],0)
                    self.assertGreater(z["original_Qy"],0)

    def test_true_W34_mixed_heavy_and_nonempty_lowcore(self):
        # Nonvacuous REAL original heavy flags coexist with a REAL retained
        # original paired low core. No theorem-sized T is asserted for s=4.
        observed=[]
        for threshold in (Fraction(4),Fraction(17,4),Fraction(9,2),
                          Fraction(19,4),Fraction(5),Fraction(21,4),
                          Fraction(11,2)):
            x=prune_genuine_original_source(
                2,"lex",threshold,64,range(1,425,31))
            if (0<x["full_heavy_physical_edges"]<x["full_edges"]
                    and 0<x["original_core_flag_count"]<411):
                observed.append(x)
        self.assertTrue(observed,"missing real original mixed fullQ/lowcore witness")
        for x in observed:
            self.assertLessEqual(x["original_heavy_owner_deletion_loss"],
                                 2*x["original_source_deleted_ids"])
            self.assertEqual(x["original_core_budget_exact"],
                             x["original_core_flag_count"])
            self.assertEqual(x["core_physical_edge_count"],
                             2*x["original_core_flag_count"])

    def test_exact_original_gq_three_anchor_role_multiplicity(self):
        for h in (1,2):
            z=projection_anchor_exposure(h)
            self.assertEqual(z["three_roles_each_exact"],z["s"]**2)
            self.assertEqual(z["one_original_deleted_flag_endpoint_cap"],12*z["s"]**2)
            self.assertEqual(z["projection_nonincident_pairs"],
                             (z["s"]+1)*(z["s"]**2+1)*(
                                 (z["s"]+1)*(z["s"]**2+1)-(z["s"]+1)))

    def test_strict_four_case_and_gq_anchor_proof_json(self):
        z=canonical_joint_original_certificates()
        self.assertEqual(z["schema"],"mathlab.hyp105.original-JOINTZCORE.v1")
        self.assertFalse(z["root_A_unconditionally_accepted"])
        self.assertTrue(z["formal_graph_constants_only"])
        self.assertEqual(len(z["genuine_original_source_pruning_cases"]),8)
        self.assertEqual(len(z["conditional_exact_allh_ledgers"]),3)
        self.assertEqual(len(z["exact_original_source_projection_anchor_exposures"]),2)
        self.assertTrue(all(row["verified"]
                            for row in z["genuine_original_source_pruning_cases"]))

    def test_reject_false_numeric_or_invalid_source_parameters(self):
        for C,c in ((1,Fraction(1)),(Fraction(1),1),
                    (Fraction(0),Fraction(1)),(Fraction(1),Fraction(0)),
                    (Fraction(1),Fraction(2))):
            with self.subTest(C=C,c=c),self.assertRaises(ValueError):
                uniform_original_joint_gate(C,c)
        for h,scheme,T,K,Z in ((3,"lex",Fraction(1),2,()),
                                (1,"lex",Fraction(0),2,()),
                                (1,"lex",Fraction(1),-1,()),
                                (1,"lex",Fraction(1),2,(45,))):
            with self.subTest(h=h,scheme=scheme),self.assertRaises(ValueError):
                prune_genuine_original_source(h,scheme,T,K,Z)

    def test_reject_non_dyadic_or_false_integer_h(self):
        z=uniform_original_joint_gate(Fraction(1),Fraction(1))
        for h in (0,-1,2.5,True):
            with self.assertRaises(ValueError):
                verify_at_dyadic_h(z,h)


if __name__=="__main__":
    unittest.main()
