"""Adversarial independent ORIGINAL SRG+mixed blocker review of Branch A #672.

Source W(3,2), W(3,4), different legal complete globally injected
correlated right maps and sparse ORIGINAL source cores, BOTH point-line
duals. No use of #672 finite_source_certificate or its original JSON.
"""
from itertools import combinations
from math import comb
import json
from pathlib import Path
import unittest

from hyp105_full_physical_degree_tail import genuine_source
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_mixed_srg_referee import (
    exact_source_star_collinearity_energy,
    exact_mixed_blocker_referee,
)


class MixedSpectralSourceReferee(unittest.TestCase):
    def test_genuine_W32_original_SRG_exact_energy_under_correlated_reassignments(self):
        model=pair_labeled_symplectic(1,"lex")
        s,V,flags=genuine_source(1)
        f=tuple(model["left_labels"])
        g0=tuple(model["right_labels"])
        for shift in (0,1,3,7,11):
            g=tuple(g0[(i+shift)%V] for i in range(V))
            with self.subTest(shift=shift):
                for target in (f,g):
                    x=exact_source_star_collinearity_energy(s,flags,target)
                    self.assertEqual(
                        x["exact_source_star_srg_energy"],
                        x["exact_source_star_srg_closed_form"])
                    self.assertEqual(
                        sum(map(len,x["original_coordinate_stars"])),2*V)
                    self.assertEqual(
                        len(x["original_source_neighbors"]),V)
                    self.assertGreater(
                        x["original_collinear_source_pair_collisions_in_coordinate_stars"],0)
                    self.assertLessEqual(
                        x["exact_source_star_srg_energy"],
                        2*(s*s-1)*V+(s+1)*2*V*(x["a"]-1))
                for dual in (False,True):
                    y=exact_mixed_blocker_referee(
                        1,f,g,dual=dual)
                    self.assertTrue(y["all_checks_passed"])
                    self.assertLessEqual(
                        y["independent_original_projection_blocked_triples"],
                        y["mixed_phi_exact"])
                    self.assertLessEqual(
                        y["mixed_first_square_exact"],
                        2*y["srg_coordinate_star_energy"])
                    self.assertLessEqual(
                        y["blocked_first_internal_coordinate_weighted_2walk_completions"]**2,
                        y["mixed_phi_exact"]*y["max_physical_core_degree"]*
                        y["physical_core_trace4"])
                    self.assertGreater(y["original_core_flags"],0)

    def test_sparse_original_source_core_and_dual_W32(self):
        model=pair_labeled_symplectic(1,"lex")
        f,g=model["left_labels"],model["right_labels"]
        _,_,flags=genuine_source(1)
        for core in (
            (),
            tuple(range(0,len(flags),2)),
            tuple(i for i in range(len(flags)) if i%5),
            tuple(range(len(flags))),
        ):
            for dual in (False,True):
                with self.subTest(n=len(core),dual=dual):
                    x=exact_mixed_blocker_referee(
                        1,f,g,core,dual=dual)
                    self.assertEqual(x["original_core_flags"],len(core))
                    self.assertTrue(x["all_checks_passed"])
                    self.assertGreaterEqual(x["mixed_phi_exact"],0)
                    if not core:
                        self.assertEqual(x["mixed_phi_exact"],0)
                        self.assertEqual(x["independent_original_projection_blocked_triples"],0)
                        self.assertEqual(x["physical_core_trace4"],0)

    def test_true_W34_full_and_sparse_core_mixed_source_referee_primal_dual(self):
        cert=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json").read_text())
        f,g=tuple(map(tuple,cert["f"])),tuple(map(tuple,cert["g"]))
        _,V,flags=genuine_source(2)
        for label,gmap,core in (
            ("adversarial-full",g,None),
            ("adversarial-sparse",g,
             tuple(i for i in range(len(flags)) if i%3)),
            ("reshuffled-g-legal",tuple(g[(i+17)%V] for i in range(V)),
             tuple(i for i in range(len(flags)) if i%4)),
        ):
            for dual in (False,True):
                with self.subTest(label=label,dual=dual):
                    x=exact_mixed_blocker_referee(
                        2,f,gmap,core,dual=dual)
                    self.assertTrue(x["all_checks_passed"])
                    self.assertGreater(x["mixed_phi_exact"],0)
                    self.assertGreater(x["original_core_flags"],0)
                    self.assertLessEqual(
                        x["independent_original_projection_blocked_triples"],
                        x["mixed_phi_exact"])
                    self.assertLessEqual(
                        x["mixed_first_square_exact"],
                        2*x["srg_coordinate_star_energy"])
                    self.assertLessEqual(
                        x["mixed_second_square_exact"],
                        x["source_pointwise_K_cap"]*
                        x["mixed_sumK_equals_full_core_degree_product"])

    def test_srg_source_identity_and_mixed_bounds_fail_closed(self):
        m=pair_labeled_symplectic(1,"lex")
        s,V,flags=genuine_source(1)
        with self.assertRaises(ValueError):
            exact_source_star_collinearity_energy(3,flags,m["left_labels"])
        with self.assertRaises(ValueError):
            exact_source_star_collinearity_energy(2,flags,m["left_labels"][:-1])
        with self.assertRaises(ValueError):
            exact_source_star_collinearity_energy(2,flags,
                (m["left_labels"][0],)*V)
        for bad in ((True,),(-1,),(0,0),(45,)):
            with self.assertRaises(ValueError):
                exact_mixed_blocker_referee(
                    1,m["left_labels"],m["right_labels"],bad)
        with self.assertRaises(ValueError):
            exact_mixed_blocker_referee(
                1,m["left_labels"][:-1],m["right_labels"])

    def test_certificate_has_genuinely_sharpened_collinear_star_correction(self):
        # New exact ALL-h identity:
        # sum_x ||C 1_Sx||²
        #   =2(s²−1)V + (s+1)sum_x |Sx|² −4E_collinear.
        # A previous spectral bound discarded the explicit negative
        # 4E_collinear term. No asymptotic exponent improvement claimed.
        for power in (1,2):
            m=pair_labeled_symplectic(power,"lex")
            s,V,flags=genuine_source(power)
            for f in (m["left_labels"],m["right_labels"]):
                with self.subTest(power=power):
                    a=max(x for edge in f for x in edge)+1
                    x=exact_source_star_collinearity_energy(s,flags,f)
                    E=x["original_collinear_source_pair_collisions_in_coordinate_stars"]
                    self.assertGreater(E,0)
                    self.assertEqual(
                        2*(s*s-1)*V+(s+1)*x["coordinate_star_square_sum"]-
                        x["exact_source_star_srg_energy"],4*E)
                    self.assertLess(
                        x["exact_source_star_srg_energy"],
                        2*(s*s-1)*V+(s+1)*x["coordinate_star_square_sum"])
                    self.assertLessEqual(
                        2*x["exact_source_star_srg_energy"],
                        4*(s+1)**2*(V+s*s*(a-1)))


if __name__=="__main__":
    unittest.main()
