"""Independent K3-G2-N finite and all-alphabet harmonic falsifiers."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_g5e2b3e1c0_weighted_overlap import (
    two_marginal_blind_cube_trade, source_weighted_BA_hypergraph,
    simple_six_2factor_targets,
)
from hyp105_g5e2b3e1k1_kikuchi_c6 import gq_pair_model
from hyp105_g5e2b3e1k3g2m_twofamily_falsifier import dual_model
from hyp105_g5e2b3e1k3g2n_johnson_harmonics import (
    target_low_harmonics, exact_target_johnson_decomposition,
    spectral_overlap_certificate, source_energy_ge3,
    six_image_index, target_H2_value, physical_pair_indices,
)


class K3G2NExactHarmonics(unittest.TestCase):
    def test_all_a_two_orbit_and_exceptional_nine(self):
        for a in (6,7,8,9,10,14,22):
            low=target_low_harmonics(a)
            self.assertEqual(low["K"],comb(a,2))
            self.assertEqual(low["target_count"],70*comb(a,6))
            self.assertEqual(low["E1"],0)
            self.assertGreaterEqual(low["E_ge3"],0)
            self.assertEqual(low["second_level_zero"],a==9)
        r=target_low_harmonics(6)
        self.assertEqual(r["density"],Fraction(2,143))
        self.assertEqual(r["h2_adj"],Fraction(-1,110))
        self.assertEqual(r["h2_dis"],Fraction(2,165))
        self.assertEqual(r["E2"],Fraction(42,11))
        self.assertEqual(r["E_ge3"],Fraction(9324,143))

    def test_complete_target_5005_sixrank_orthogonal_decomposition(self):
        sets,layers,energies=exact_target_johnson_decomposition()
        self.assertEqual(len(sets),5005)
        self.assertEqual(len(layers),7)
        self.assertEqual(sum(energies),70)
        self.assertEqual(energies[0],Fraction(140,143))
        self.assertEqual(energies[1],0)
        self.assertEqual(energies[2],Fraction(42,11))
        indices={e:i for i,e in enumerate(combinations(range(6),2))}
        target={tuple(sorted(indices[e] for e in S))
                for S in simple_six_2factor_targets(6)}
        for i,S in enumerate(sets):
            self.assertEqual(sum((layer[i] for layer in layers),
                                 Fraction(0)),int(S in target))

    def test_cube_trade_proves_rank_at_most_two_is_blind(self):
        trade=two_marginal_blind_cube_trade()
        labels=tuple(combinations(range(6),2))
        even={frozenset(R):1 for R in trade["source_even_sixsets"]}
        odd={frozenset(R):1 for R in trade["source_odd_sixsets"]}
        x=spectral_overlap_certificate(even,labels)
        y=spectral_overlap_certificate(odd,labels)
        self.assertEqual(x["actual_U"],0)
        self.assertEqual(y["actual_U"],1)
        self.assertEqual(x["signed_ranks"][:3],y["signed_ranks"][:3])
        self.assertEqual(x["source_E_ge3"],y["source_E_ge3"])
        self.assertEqual(
            Fraction(*y["higher_order_3_to_6"])-
            Fraction(*x["higher_order_3_to_6"]),1)

    def test_original_GQ_and_dual_true_BA_harmonics(self):
        m=gq_pair_model(1,"lex")
        d=dual_model(m)
        for model in (m,d):
            weights=source_weighted_BA_hypergraph(model)
            proof=spectral_overlap_certificate(weights,model["right_labels"])
            rank=[Fraction(*x) for x in proof["signed_ranks"]]
            self.assertEqual(sum(rank),proof["actual_U"])
            self.assertEqual(rank[0],Fraction(*proof["random_mean"]))
            self.assertEqual(rank[1],0)
            self.assertEqual(rank[2]+sum(rank[3:]),rank[0]*0+
                             proof["actual_U"]-rank[0])
            self.assertTrue(proof["strict_CS_bound_valid"])

    def test_reject_duplicate_and_out_of_range_original_sources(self):
        labels=tuple(combinations(range(6),2))
        weights={frozenset(range(6)):1}
        with self.assertRaises(ValueError):
            spectral_overlap_certificate(weights,labels[:-1])
        with self.assertRaises(ValueError):
            spectral_overlap_certificate({frozenset(range(5)):1},labels)
        with self.assertRaises(ValueError):
            spectral_overlap_certificate({frozenset(range(6)):-1},labels)
        with self.assertRaises(ValueError):
            six_image_index(tuple(range(6)),labels,(physical_pair_indices(6)))
        with self.assertRaises(ValueError):
            source_energy_ge3(weights,labels[:8]+labels[:7])


if __name__=="__main__":
    unittest.main()
