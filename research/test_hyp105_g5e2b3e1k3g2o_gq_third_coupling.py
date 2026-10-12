"""Independent K3-G2-O five-target-orbit and true original GQ tests."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_g5e2b3e1k3g2n_johnson_harmonics import (
    gq_pair_model,exact_target_johnson_decomposition,
    physical_pair_indices, spectral_overlap_certificate,
)
from hyp105_g5e2b3e1c0_weighted_overlap import (
    simple_six_2factor_targets, source_weighted_BA_hypergraph,
)
from hyp105_g5e2b3e1k3g2m_twofamily_falsifier import dual_model
from hyp105_g5e2b3e1k3g2o_gq_third_coupling import (
    physical_triple_shape, target_rank3_orbits,target_H3_on_six,
    gq_line_geometry, gq_sixsource_guard, original_GQ_third_coupling,
    _source_H3_and_energy,
)


class K3G2OThirdCoupling(unittest.TestCase):
    def test_all_a_third_orbits_exact_and_energy_nonnegative(self):
        expected={
            "triangle":Fraction(57,4004),
            "path_P4":Fraction(-25,6006),
            "star_K1_3":Fraction(1,429),
            "path_P3_plus_edge":Fraction(5,4004),
            "matching_3":Fraction(20,3003),
        }
        for a in (6,7,8,9,14,22):
            actual=target_rank3_orbits(a)
            self.assertEqual(sum(actual["orbit_sizes"].values()),
                             comb(comb(a,2),3))
            self.assertGreaterEqual(actual["E3"],0)
            self.assertGreaterEqual(actual["E_ge4"],0)
            if a==6:
                self.assertEqual(actual["h3"],expected)
                self.assertEqual(actual["E3"],Fraction(710,1001))
        with self.assertRaises(ValueError):
            target_rank3_orbits(5)

    def test_independent_actual_three_target_codegrees_and_shapes(self):
        # No reliance on the closed codegree oracle: enumerate all original
        # physical target sixsets, then every contained triple.
        for a in (6,9):
            target=simple_six_2factor_targets(a)
            physical=tuple(combinations(range(a),2))
            d=Counter()
            for S in target:
                for A in combinations(sorted(S),3):
                    d[A]+=1
            exact=target_rank3_orbits(a)
            observed=Counter()
            for A in combinations(physical,3):
                kind=physical_triple_shape(A)
                observed[kind]+=1
                self.assertEqual(d[A],exact["target_triple_codegrees"][kind])
            self.assertEqual(dict(observed),exact["orbit_sizes"])
            self.assertEqual(sum(d.values()),20*len(target))

    def test_complete_5005_rank_three_direct_vs_johnson(self):
        sets,layers,energies=exact_target_johnson_decomposition()
        r=target_rank3_orbits(6)
        edges=tuple(combinations(range(6),2))
        self.assertEqual(energies[3],r["E3"])
        self.assertEqual(sum(energies[4:]),r["E_ge4"])
        self.assertEqual(len(sets),5005)
        for idx,S in enumerate(sets):
            self.assertEqual(target_H3_on_six(S,edges,r["h3"]),layers[3][idx])

    def test_true_original_line_SRG_and_geometric_cherry_bound(self):
        expected={
            2:(15,6,1,3,(80,180,180,15)),
            4:(85,20,3,5,(43520,40800,13600,850)),
        }
        for power in (1,2):
            model=gq_pair_model(power,"lex")
            geom=gq_line_geometry(model)
            V,k,lam,mu,triple=expected[model["s"]]
            self.assertEqual((geom["V"],geom["k"],geom["lambda"],
                              geom["mu"]), (V,k,lam,mu))
            self.assertEqual(geom["triple_populations"],triple)
            observed=Counter(
                sum(b in geom["adjacency"][a] for a,b in
                    combinations(A,2))
                for A in combinations(range(V),3))
            self.assertEqual(tuple(observed[k] for k in range(4)),triple)
            self.assertEqual(sum(observed.values()),comb(V,3))
        W32=gq_pair_model(1,"lex")
        g=gq_line_geometry(W32)
        w=source_weighted_BA_hypergraph(W32)
        guard=gq_sixsource_guard(w,g)
        self.assertEqual(guard["mass"],sum(w.values()))
        self.assertTrue(guard["all_h_sixsource_GQ_cherry_cap_valid"])
        with self.assertRaises(AssertionError):
            gq_sixsource_guard({frozenset(range(6)):10000000},g)
        with self.assertRaises(ValueError):
            gq_sixsource_guard({frozenset(range(5)):1},g)

    def test_original_dual_coupled_tensor_and_rank3_inner_product(self):
        m=gq_pair_model(1,"lex")
        for model in (m,dual_model(m)):
            c=original_GQ_third_coupling(model)
            self.assertEqual(c["tensor_triple_mass"],
                             20*c["original_GQ_sixsource_guard"]["mass"])
            self.assertEqual(c["third_J_harmonic_correlation"],
                             c["independent_triple_projection"])
            self.assertEqual(c["third_J_harmonic_correlation"],
                             c["sixsource_spectrum_third_level"])
            C=Fraction(*c["remaining_four_to_six"])
            b=Fraction(*c["rank_four_to_six_CS_bound_squared"])
            self.assertLessEqual(C*C,b)
            tensor=c["coupled_original_GQ_4x5_tensor"]
            self.assertEqual(len(tensor),4)
            self.assertTrue(all(len(x)==5 for x in tensor.values()))
            w=source_weighted_BA_hypergraph(model)
            h3,E3,E456=_source_H3_and_energy(
                w,model["right_labels"],a=6)
            self.assertEqual(Fraction(*c["source_E3"]),E3)
            self.assertEqual(Fraction(*c["source_E_ge4"]),E456)
            self.assertEqual(len(h3),comb(15,3))

    def test_invalid_triple_physical_labels_fail_closed(self):
        with self.assertRaises(ValueError):
            physical_triple_shape(((0,1),(0,1),(0,2)))
        with self.assertRaises(ValueError):
            physical_triple_shape(((0,1),(2,1),(0,2)))
        with self.assertRaises(ValueError):
            target_H3_on_six((0,1,2,3,4,4),
                tuple(combinations(range(6),2)),
                target_rank3_orbits(6)["h3"])


if __name__=="__main__":
    unittest.main()
