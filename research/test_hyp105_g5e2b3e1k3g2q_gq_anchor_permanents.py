"""Independent original GQ anchor-square/permanent and rank56 tests."""
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_g5e2b3e1k1_kikuchi_c6 import labeled_model
from hyp105_g5e2b3e1c0_weighted_overlap import source_weighted_BA_hypergraph
from hyp105_g5e2b3e1k3g2n_johnson_harmonics import gq_pair_model
from hyp105_g5e2b3e1k3g2m_twofamily_falsifier import dual_model
from hyp105_g5e2b3e1k3g2q_gq_anchor_permanents import (
    exhaustive_girth8_permanent_lemma,permanent4,
    original_GQ_tables,physical_squares,
    original_pair_square_permanent_cap,true_original_sixsource_permanents,
    rank56_permanent_split,
)


class K3G2QPermanentTests(unittest.TestCase):
    def test_all_65536_binary_matrices_and_sharp_girth8_cap(self):
        x=exhaustive_girth8_permanent_lemma()
        self.assertEqual(x["all_binary_4x4_matrices"],65536)
        self.assertEqual(x["girth_at_least_eight_matrices"],16217)
        self.assertEqual(x["permanent_histogram"],
                         {"0":11321,"1":4824,"2":72})
        self.assertEqual(x["sharp_permanent_max"],2)
        self.assertEqual(permanent4((12,10,5,3)),2)
        with self.assertRaises(ValueError):
            permanent4((15,15,0,0))  # forbidden 4-cycle
        with self.assertRaises(ValueError):
            permanent4((5,3,6,0))  # forbidden 6-cycle
        with self.assertRaises(ValueError):
            permanent4((1,2,3))

    def test_all_h_original_source_cap_not_confused_with_P2(self):
        W32=original_pair_square_permanent_cap(2,6)
        self.assertEqual(W32["old_per_intersecting_GQ_pair_cap"],81)
        self.assertEqual(W32["new_per_intersecting_GQ_pair_cap"],6)
        self.assertEqual(W32["combined_upper"],6)
        self.assertTrue(W32["new_improves_previous"])
        self.assertFalse(W32["all_h_P2_proved"])
        W34=original_pair_square_permanent_cap(4,14)
        self.assertEqual(W34["new_per_intersecting_GQ_pair_cap"],2970)
        self.assertEqual(W34["old_per_intersecting_GQ_pair_cap"],625)
        self.assertEqual(W34["combined_upper"],625)
        self.assertFalse(W34["new_improves_previous"])
        W38=original_pair_square_permanent_cap(8,35)
        self.assertEqual(W38["V"],585)
        with self.assertRaises(ValueError):
            original_pair_square_permanent_cap(4,6)
        with self.assertRaises(ValueError):
            original_pair_square_permanent_cap(True,6)

    def test_true_GQ_projection_axiom_and_square_label_injections(self):
        for power in (1,2):
            m=gq_pair_model(power,"lex")
            p,l,anchor=original_GQ_tables(m["s"],tuple(m["incidences"]))
            self.assertEqual(len(p),m["v_left"])
            self.assertEqual(len(l),m["v_right"])
            self.assertEqual(len(anchor),m["v_left"]*comb(m["s"]+1,2))
        m=gq_pair_model(1,"lex")
        squares=physical_squares(m)
        self.assertEqual(len(squares),15)
        self.assertEqual({len(x) for x in squares},{3})
        for anchor,sq in enumerate(squares):
            for Q in sq:
                self.assertNotIn(anchor,Q)
                self.assertEqual(len(Q),4)
        # Same true W32 original host, non-surjective K7 pair injections.
        padded=labeled_model(2,7,m["incidences"],m["left_labels"],
                             m["right_labels"],scheme="non-surjective-K7")
        self.assertEqual({len(x) for x in physical_squares(padded)},{3})
        with self.assertRaises(ValueError):
            original_GQ_tables(2,tuple(m["incidences"][:-1]))
        with self.assertRaises(ValueError):
            physical_squares(labeled_model(2,6,m["incidences"],
                m["left_labels"][:-1]+m["left_labels"][:1],
                m["right_labels"],scheme="duplicate-physical-left"))

    def test_complete_original_W32_5005_source_permanents(self):
        m=gq_pair_model(1,"lex")
        independent=true_original_sixsource_permanents(m)
        w=independent["weights"]
        self.assertEqual(w,source_weighted_BA_hypergraph(m))
        self.assertEqual(independent["report"]["W32_original_sixsets_all"],5005)
        self.assertEqual(independent["report"]["original_sixsource_mass"],5000)
        self.assertEqual(
            sum(independent["report"]["all_permanent_zero_one_two_terms"].values()),
            sum(3*e*n for e,n in independent["report"]
                ["sixset_GQ_intersection_count_histogram"].items()
                for e in [int(e)]))
        self.assertEqual(
            sum(independent["permanent_one_counts"].values())+
            2*sum(independent["permanent_two_counts"].values()),5000)
        self.assertTrue(independent["report"]
                        ["previous_81_e_bound_replaced_by_6_e"])

    def test_true_original_signed_fifth_sixth_levels(self):
        m=gq_pair_model(1,"lex")
        ledger=true_original_sixsource_permanents(m)
        s=rank56_permanent_split(m,ledger)
        self.assertEqual(s["actual_physical_BA_overlap"],98)
        self.assertEqual(s["rank56_sum"],[-383,924])
        self.assertEqual(s["independent_full_Johnson_rank56"],[-383,924])
        self.assertEqual(
            s["permanent_one_source_mass"]+s["permanent_two_source_mass"],
            5000)
        self.assertEqual(
            Fraction(*s["rank56_permanent_one_contribution"])+
            Fraction(*s["rank56_permanent_two_contribution"]),
            Fraction(-383,924))
        self.assertFalse(s["rank56_nonnegative_claim"])

    def test_reject_forged_original_sixsource_scope(self):
        m=gq_pair_model(2,"lex")
        with self.assertRaises(ValueError):
            true_original_sixsource_permanents(m)
        m=gq_pair_model(1,"lex")
        bad=dict(m)
        bad["incidences"]=tuple(m["incidences"][:-1])
        with self.assertRaises(ValueError):
            true_original_sixsource_permanents(bad)


if __name__=="__main__":
    unittest.main()
