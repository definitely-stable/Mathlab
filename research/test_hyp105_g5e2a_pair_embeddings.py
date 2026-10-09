"""E2-A independent genuine GF2/GF4 pair-injection and factor graph tests."""
import unittest
from math import comb
from itertools import combinations

from hyp105_g5e2a_pair_embeddings import (
    SCHEMES, pair_alphabet_size, pair_labeled_symplectic,
    small_motif_probe, unrank_pair, report,
)
from test_hyp105_g5b_graph_realization import shortest_cycle_bipartite


class E2ASymplecticPairLabelTests(unittest.TestCase):
    def test_complete_unranking_exact_all_pair_alphabet(self):
        for n, expected_a in ((1,2),(15,6),(85,14),(585,35)):
            a=pair_alphabet_size(n)
            self.assertEqual(a,expected_a)
            self.assertGreaterEqual(comb(a,2),n)
            self.assertLess(comb(a-1,2),n)
            got=tuple(unrank_pair(i,a) for i in range(comb(a,2)))
            self.assertEqual(got, tuple(combinations(range(a),2)))
        for rank,a in ((-1,6),(15,6),(0,1)):
            with self.assertRaises(ValueError):
                unrank_pair(rank,a)
        with self.assertRaises(ValueError):
            pair_alphabet_size(0)

    def test_s2_and_s4_bijections_are_true_gq_factor_realizations(self):
        for h,v,e,m in ((1,15,45,12),(2,85,425,28)):
            for mode in SCHEMES:
                model=pair_labeled_symplectic(h,mode)
                self.assertEqual((model["v"],model["N"],model["m"]),
                                 (v,e,m))
                self.assertEqual(len(set(model["left_labels"])),v)
                self.assertEqual(len(set(model["right_labels"])),v)
                self.assertEqual(len(set(model["supports"])),e)
                a=model["a"]
                self.assertEqual({len(set(s)) for s in model["supports"]},{4})
                self.assertEqual(shortest_cycle_bipartite(model["incidences"]),8)
                # Independently reconstruct which original point and line
                # each physical support came from. This is *not* claiming
                # sparse GF5 ASET: the unit weighted family still collides.
                reverse_p={tuple(pair):i for i,pair
                           in enumerate(model["left_labels"])}
                reverse_l={tuple(pair):i for i,pair
                           in enumerate(model["right_labels"])}
                reconstructed=[]
                for support in model["supports"]:
                    l=tuple(c for c in support if c<a)
                    r=tuple(c-a for c in support if c>=a)
                    reconstructed.append((reverse_p[l],reverse_l[r]))
                self.assertEqual(tuple(reconstructed),model["incidences"])
                self.assertEqual({len(s) for s in model["supports"]},{4})
                self.assertFalse(model["all_s_risk_power_proved"])

    def test_candidate_schemes_preserve_graph_but_change_true_coordinates(self):
        for h in (1,2):
            all_models=[pair_labeled_symplectic(h,mode)
                        for mode in SCHEMES]
            self.assertEqual(len({model["supports"] for model in all_models}),3)
            self.assertEqual(
                {model["incidences"] for model in all_models},
                {all_models[0]["incidences"]})
            self.assertEqual(
                {model["N"] for model in all_models},
                {all_models[0]["N"]})
        with self.assertRaises(ValueError):
            pair_labeled_symplectic(1,"invented")
        with self.assertRaises(ValueError):
            pair_labeled_symplectic(3,"lex")

    def test_only_bounded_8_support_motif_probes_at_field_s4(self):
        for h in (1,2):
            m=pair_labeled_symplectic(h,"coordinate-flag")
            probe=small_motif_probe(m)
            self.assertEqual(len(probe["sample_indices"]),8)
            self.assertEqual(len(set(probe["sample_indices"])),8)
            self.assertEqual(probe["k2"]["total_events"],210)
            self.assertEqual(probe["k3"]["total_events"],280)
            self.assertLessEqual(probe["k2"]["possible_events"],210)
            self.assertLessEqual(probe["k3"]["possible_events"],280)
            self.assertTrue(probe["k3"]["necessary_only"])
            with self.assertRaises(ValueError):
                small_motif_probe(m,10)
        x=report()
        self.assertEqual(len(x["cases"]),6)
        self.assertFalse(any(t["new_aset_power_proven"]
                             for t in x["cases"]))
        self.assertTrue(all(t["all_s_nonzero_flow_risk_bound"] is None
                            for t in x["cases"]))


if __name__=="__main__":
    unittest.main()
