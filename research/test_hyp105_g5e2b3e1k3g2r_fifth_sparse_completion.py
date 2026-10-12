"""Independent exact HYP-105 K3-G2-R physical H5/H6 and true GQ-dual tests."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_g5e2b3e1c0_weighted_overlap import simple_six_2factor_targets
from hyp105_g5e2b3e1k3g2n_johnson_harmonics import (
    exact_target_johnson_decomposition,gq_pair_model,
    spectral_overlap_certificate,
)
from hyp105_g5e2b3e1k3g2m_twofamily_falsifier import dual_model
from hyp105_g5e2b3e1k3g2q_gq_anchor_permanents import (
    true_original_sixsource_permanents,
    rank56_permanent_split,
)
from hyp105_g5e2b3e1k3g2r_fifth_sparse_completion import PATH_FIVE
from hyp105_g5e2b3e1k3g2r_fifth_sparse_completion import (
    TRIANGLE_PATH,SIX_CYCLE,TWO_TRIANGLES,five_edge_completion,
    target_rank5_and_rank6_energies,rank5_lift_on_six,
    direct_target_rank6_residual,permanent_witness_fifth_sixth_split,
)
from hyp105_g5e2b3e1k3g2n_johnson_harmonics import target_low_harmonics
from hyp105_g5e2b3e1k3g2o_gq_third_coupling import target_rank3_orbits
from hyp105_g5e2b3e1k3g2p_fourth_geometry import target_rank4_orbits


class K3G2RSparseCompletionTests(unittest.TestCase):
    def test_sparse_five_edge_target_unique_completion_and_negatives(self):
        self.assertEqual(five_edge_completion(PATH_FIVE),tuple(sorted(SIX_CYCLE)))
        self.assertEqual(five_edge_completion(TRIANGLE_PATH),
                         tuple(sorted(TWO_TRIANGLES)))
        self.assertFalse(five_edge_completion(
            ((0,1),(0,2),(0,3),(0,4),(0,5))))
        self.assertFalse(five_edge_completion(
            ((0,1),(1,2),(2,3),(3,4),(4,0))))
        with self.assertRaises(ValueError):
            five_edge_completion(((0,1),(0,1),(2,3),(3,4),(4,5)))
        with self.assertRaises(ValueError):
            five_edge_completion(((0,1),(1,0),(2,3),(3,4),(4,5)))

    def test_independent_all_K6_and_K9_five_edge_completion_codegrees(self):
        # Actual target-extension counts, computed from an unrelated full
        # two-factor physical census (not the new shape completion oracle).
        for a in (6,9):
            targets=simple_six_2factor_targets(a)
            counts=Counter()
            for T in targets:
                for F in combinations(sorted(T),5):
                    counts[F]+=1
            self.assertEqual(sum(counts.values()),6*70*comb(a,6))
            self.assertTrue(all(v==1 for v in counts.values()))
            self.assertEqual(len(counts),6*70*comb(a,6))
            if a==6:
                domain=combinations(tuple(combinations(range(a),2)),5)
                for F in domain:
                    extension=five_edge_completion(F)
                    actual=counts[tuple(sorted(F))]
                    self.assertEqual(actual,int(bool(extension)))
                    if extension:
                        self.assertIn(frozenset(extension),targets)
            else:
                # Every target-derived five-edge subset must extend to the
                # same unique full target; no orbit interpolation.
                for F in counts:
                    self.assertEqual(frozenset(five_edge_completion(F)) in targets,
                                     True)

    def test_complete_exact_seven_level_K6_target_and_nonnegative_all_a(self):
        sets,components,energies=exact_target_johnson_decomposition()
        ours=target_rank5_and_rank6_energies(6)
        self.assertEqual(ours["E0_to_E6"],energies)
        self.assertEqual(energies[5],Fraction(1182,77))
        self.assertEqual(energies[6],Fraction(258,7))
        edges=tuple(combinations(range(6),2))
        target=simple_six_2factor_targets(6)
        low=target_low_harmonics(6)
        third=target_rank3_orbits(6)
        fourth=target_rank4_orbits(6)
        for i,S in enumerate(sets):
            t5=rank5_lift_on_six(S,edges,low=low,third=third,fourth=fourth)
            t6=direct_target_rank6_residual(S,edges,low=low,
                        third=third,fourth=fourth,targets=target)
            self.assertEqual(t5,components[5][i])
            self.assertEqual(t6,components[6][i])
        for a in (6,7,8,9,10,14,22):
            x=target_rank5_and_rank6_energies(a)
            self.assertEqual(len(x["E0_to_E6"]),7)
            self.assertEqual(x["E0_to_E6"][1],0)
            self.assertEqual(sum(x["E0_to_E6"]),70*comb(a,6))
            self.assertTrue(all(e>=0 for e in x["E0_to_E6"]))
            self.assertEqual(x["physical_five_nonzero_completion_types"],2)
        with self.assertRaises(ValueError):
            target_rank5_and_rank6_energies(5)

    def test_true_original_and_genuine_dual_rank5_and_rank6_split(self):
        m=gq_pair_model(1,"lex")
        for side in (m,dual_model(m)):
            ledger=true_original_sixsource_permanents(side)
            result=permanent_witness_fifth_sixth_split(side,ledger)
            independent=rank56_permanent_split(side,ledger)
            self.assertEqual(result["signed_C56"],independent["rank56_sum"])
            rows=[[Fraction(*v) for v in row]
                  for row in result["rows_permanent_one_two_columns_rank5_rank6"]]
            self.assertEqual(sum((sum(row) for row in rows),Fraction(0)),
                             Fraction(*result["signed_C56"]))
            self.assertEqual(result["source_mass"],
                             sum(result["permanent_one_two_source_masses"]))
            self.assertEqual(
                sum((row[0] for row in rows),Fraction(0)),
                Fraction(*result["signed_C5"]))
            self.assertEqual(
                sum((row[1] for row in rows),Fraction(0)),
                Fraction(*result["signed_C6"]))
            independent_full=spectral_overlap_certificate(
                ledger["weights"],side["right_labels"])
            self.assertEqual(result["signed_C5"],
                             independent_full["signed_ranks"][5])
            self.assertEqual(result["signed_C6"],
                             independent_full["signed_ranks"][6])

    def test_physical_fifth_harmonic_requires_complete_sixset(self):
        edges=tuple(combinations(range(6),2))
        low=target_low_harmonics(6)
        third=target_rank3_orbits(6)
        fourth=target_rank4_orbits(6)
        with self.assertRaises(ValueError):
            rank5_lift_on_six((0,1,2,3,4,4),edges,
                low=low,third=third,fourth=fourth)
        with self.assertRaises(ValueError):
            rank5_lift_on_six((0,1,2,3,4,15),edges,
                low=low,third=third,fourth=fourth)


if __name__=="__main__":
    unittest.main()
