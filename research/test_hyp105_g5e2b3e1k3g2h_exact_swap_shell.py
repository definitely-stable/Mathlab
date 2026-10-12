"""G2-H independent complete-W32 target oracles and fail-closed shell tests."""
import unittest

from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_g5e2b3e1k3g2g_global_adaptive import adaptive_complete_cross_probe
from hyp105_g5e2b3e1k3g2h_exact_swap_shell import (
    swapped_labeling, full_target_hall, transposition_shell,
)


class K3G2HCompleteAdversaryTests(unittest.TestCase):
    def test_pair_label_swaps_are_globally_coherent(self):
        base=gq_pair_model(1,"lex")
        for side,i,j in (("left",0,1),("right",0,14),
                         ("left",5,7),("right",9,14)):
            other=swapped_labeling(base,side,i,j)
            self.assertEqual(other["incidences"],base["incidences"])
            frozen="right" if side=="left" else "left"
            self.assertEqual(other[frozen+"_labels"],base[frozen+"_labels"])
            old=base[side+"_labels"];new=other[side+"_labels"]
            self.assertEqual(new[i],old[j])
            self.assertEqual(new[j],old[i])
            self.assertEqual({k for k in range(15) if old[k]!=new[k]}, {i,j})
        for side,i,j in (("fake",0,1),("right",1,1),
                         ("left",-1,2),("left",1,15),("right",True,2)):
            with self.assertRaises(ValueError):
                swapped_labeling(base,side,i,j)

    def test_complete_B0_baseline_and_GF5_floor(self):
        model=gq_pair_model(1,"lex")
        cert=full_target_hall(model)
        direct=seven_census(model,witness_sets=True,independent_checks=False)
        self.assertEqual(cert["Jcross"],36)
        self.assertEqual(cert["S_seven_exact"],259)
        self.assertEqual(cert["S_seven_exact"],len(direct["sets"]))
        self.assertEqual(cert["GF5_seven_numerator_exact_class_floor"],
                         direct["GF5_seven_lower_numerator"])
        self.assertEqual(cert["matched"]+cert["hall_deficiency"],cert["Jcross"])
        self.assertEqual(cert["matched"],cert["hall_cut_capacity"])
        self.assertTrue(cert["hall_unit_capacity"])
        self.assertEqual(len(cert["assignment_sha256"]),64)
        # Budgeted incomplete G2-G discovery cannot exceed all true B0 targets.
        partial=adaptive_complete_cross_probe(
            model,sample_limit=5,max_nodes_per_seed=2000,
            max_seeds_per_unmatched=2)
        self.assertLessEqual(partial["positive_seven_S_lower"],
                             cert["S_seven_exact"])
        self.assertLessEqual(
            partial["positive_risk_numerator_lower_51_pow_6"],
            cert["GF5_seven_numerator_exact_class_floor"])
        self.assertFalse(partial["full_finite_Jcross_charge_into_true_S_proved"])

    def test_independent_matching_and_hall_cut_for_adversarial_maps(self):
        base=gq_pair_model(1,"lex")
        for side,i,j in (("left",0,1),("left",1,14),
                         ("right",0,14),("right",5,9)):
            model=swapped_labeling(base,side,i,j)
            cert=full_target_hall(model)
            complete=seven_census(model,witness_sets=True,independent_checks=False)
            self.assertEqual(cert["S_seven_exact"],complete["S_seven"])
            self.assertEqual(cert["distinct_sixsets_checked"],complete["S_seven"])
            self.assertEqual(cert["matched"]+cert["hall_deficiency"],cert["Jcross"])
            self.assertEqual(cert["matched"],cert["hall_cut_capacity"])
            if not cert["hall_unit_capacity"]:
                self.assertGreater(cert["hall_cut_witness_subset"],
                                   cert["hall_cut_neighbor_size"])
                self.assertEqual(
                    cert["hall_deficiency"],
                    cert["hall_cut_witness_subset"]-cert["hall_cut_neighbor_size"])
            else:
                self.assertEqual(cert["hall_deficiency"],0)

    def test_incomplete_shell_never_claims_full_or_all_h(self):
        base=gq_pair_model(1,"lex")
        subset=transposition_shell(base,sides=("right",),max_pairs_per_side=2)
        self.assertEqual(subset["tested_coherent_labelings"],2)
        self.assertFalse(subset["exact_complete_lex_W32_single_swap_shell"])
        self.assertTrue(subset["no_all_h_charge_claimed"])
        self.assertTrue(subset["no_global_labeling_exhaustion_claimed"])
        self.assertEqual(subset["unit_hall_successes"]+
                         subset["unit_hall_failures"],2)
        self.assertEqual(len(subset["swap_shell_results_sha256"]),64)
        for sides,limit in (((),None),(("right","right"),None),
                            (("right",),0),(("left",),True),
                            (("left",),106)):
            with self.assertRaises(ValueError):
                transposition_shell(base,sides=sides,max_pairs_per_side=limit)


if __name__=="__main__":
    unittest.main()
