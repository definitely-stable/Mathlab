"""Independent HYP-105 E1-K3-G2-P fourth harmonic and GQ no-diamond tests."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_g5e2b3e1c0_weighted_overlap import (
    simple_six_2factor_targets,source_weighted_BA_hypergraph,
)
from hyp105_g5e2b3e1k3g2n_johnson_harmonics import (
    gq_pair_model, exact_target_johnson_decomposition,
    physical_pair_indices, spectral_overlap_certificate,
)
from hyp105_g5e2b3e1k3g2m_twofamily_falsifier import dual_model
from hyp105_g5e2b3e1k3g2o_gq_third_coupling import gq_line_geometry
from hyp105_g5e2b3e1k3g2p_fourth_geometry import (
    physical_four_shape,physical_four_templates,target_rank4_orbits,
    _target_rank4_on_six, _original_four_shapes, original_four_type,
    gq_forbidden_diamond_theorem, independent_source_rank4_projection,
    original_GQ_fourth_coupling,
)


class K3G2PFourthGeometryTests(unittest.TestCase):
    def test_all_a_eleven_orbits_and_exact_K6_rank4_energy(self):
        templates=physical_four_templates()
        self.assertEqual(len(templates),11)
        self.assertEqual(len({v[0] for v in templates}),11)
        for a in (6,7,9,14,22):
            x=target_rank4_orbits(a)
            self.assertEqual(len(x["shapes"]),11)
            self.assertEqual(sum(v["orbit_size"] for v in x["shapes"].values()),
                             comb(comb(a,2),4))
            self.assertGreaterEqual(x["E_ge5"],0)
            if a==6:
                self.assertEqual(x["E4"],Fraction(86,7))
                self.assertEqual(x["E_ge5"],Fraction(4020,77))
        self.assertRaises(ValueError,target_rank4_orbits,5)

    def test_independent_K6_K9_physical_four_codegrees(self):
        for a in (6,9):
            palette=tuple(combinations(range(a),2))
            counts=Counter()
            for S in simple_six_2factor_targets(a):
                for B in combinations(sorted(S),4):
                    counts[B]+=1
            r=target_rank4_orbits(a)
            observed=Counter()
            for B in combinations(palette,4):
                shape=str(physical_four_shape(B))
                observed[shape]+=1
                self.assertEqual(counts[B],r["shapes"][shape]["target_codegree"])
            self.assertEqual(
                dict(observed),
                {k:v["orbit_size"] for k,v in r["shapes"].items()
                 if v["orbit_size"]})
            self.assertEqual(sum(counts.values()),
                             15*70*comb(a,6))

    def test_complete_J15_6_independent_rank_four_on_every_sixset(self):
        universe,components,energy=exact_target_johnson_decomposition()
        orbital=target_rank4_orbits(6)
        self.assertEqual(energy[4],orbital["E4"])
        self.assertEqual(sum(energy[5:]),orbital["E_ge5"])
        edges=tuple(combinations(range(6),2))
        for index,S in enumerate(universe):
            self.assertEqual(_target_rank4_on_six(S,edges,orbital),
                             components[4][index])

    def test_original_GQ_no_diamond_and_K4_pencil(self):
        codes=_original_four_shapes()
        self.assertEqual(len(codes),11)
        self.assertEqual(set(codes.values()),set(range(7)))
        m=gq_pair_model(1,"lex")
        geom=gq_line_geometry(m)
        check=gq_forbidden_diamond_theorem(geom)
        self.assertEqual(check["full_original_foursets"],comb(15,4))
        self.assertEqual(sum(check["complete_four_histogram"].values()),
                             comb(15,4))
        self.assertEqual(check["diamond_count"],0)
        self.assertEqual(check["K4_count"],0)
        self.assertEqual(check["all_h_clique_pencil_capacity"],3)
        # W34: independent all-triangle/common-fifth adjacency test
        # rules out EVERY induced diamond without 2m quadruple checks.
        big=gq_pair_model(2,"lex")
        b=gq_line_geometry(big)
        near=b["adjacency"]
        tri=0
        k4=0
        for A in combinations(range(85),3):
            if all(v in near[u] for u,v in combinations(A,2)):
                tri+=1
                for q in range(85):
                    if q in A:
                        continue
                    degree=sum(q in near[u] for u in A)
                    self.assertNotEqual(degree,2)
                    if degree==3:
                        k4+=1
        self.assertEqual(tri,850)
        self.assertEqual(k4//4,85*comb(5,4))
        self.assertNotEqual(b["s"],2)

    def test_genuine_original_dual_source_fourth_orthogonality(self):
        base=gq_pair_model(1,"lex")
        for m in (base,dual_model(base)):
            r=original_GQ_fourth_coupling(m)
            self.assertEqual(r["tensor_mass"],15*r["source_mass"])
            self.assertEqual(r["rank4_contraction"],
                             r["rank4_independent_source_projection"])
            self.assertEqual(r["rank4_contraction"],
                             r["independent_full_spectrum_rank4"])
            v=Fraction(*r["rank5_and_rank6_correlation"])
            self.assertLessEqual(
                v*v,Fraction(*r["rank_ge5_CS_squared_bound"]))
            E=[Fraction(*z) for z in r["source_rank0_to4_energies"]]
            E56=Fraction(*r["source_rank_ge5_energy"])
            self.assertEqual(sum(E)+E56,
                             sum(w*w for w in source_weighted_BA_hypergraph(m).values()))
            self.assertEqual(len(r["coupled_original_GQ_four_by_physical_four"]),11)
            self.assertEqual(r["original_GQ_four_histogram"]["diamond_count"],0)
            for code,row in r["coupled_original_GQ_four_by_physical_four"].items():
                if _original_four_shapes()[int(code)]==5:
                    self.assertEqual(sum(row.values()),0)

    def test_original_weight_and_source_map_fail_closed(self):
        labels=tuple(combinations(range(6),2))
        with self.assertRaises(ValueError):
            physical_four_shape(((0,1),(0,2),(0,3),(0,3)))
        with self.assertRaises(ValueError):
            original_four_type((0,1,1,3),
                tuple(frozenset() for _ in range(15)))
        with self.assertRaises(ValueError):
            independent_source_rank4_projection(
                {frozenset(range(6)):1},labels,a=5)
        with self.assertRaises(ValueError):
            independent_source_rank4_projection(
                {frozenset(range(6)):1},labels[:-1]+labels[:1],a=6)
        with self.assertRaises(ValueError):
            independent_source_rank4_projection(
                {frozenset(range(6)):-1},labels,a=6)
        # Explicit non-surjective V<K: unused coordinate 6 must not shrink a.
        w={frozenset(range(6)):2,frozenset((0,1,2,3,4,6)):3}
        q=independent_source_rank4_projection(w,labels,a=7)
        self.assertEqual(q["rank0_to_4_energies"][0],
                         Fraction(25,comb(21,6)))
        self.assertEqual(sum(q["rank0_to_4_energies"])+q["rank_ge5_energy"],13)


if __name__=="__main__":
    unittest.main()
