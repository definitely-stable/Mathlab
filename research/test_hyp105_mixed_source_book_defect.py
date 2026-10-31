"""Independent source/physical/tensor falsifiers for the all-h Phi=B+Psi GQ law."""
import json
from pathlib import Path
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_full_physical_degree_tail import genuine_source
from hyp105_mixed_source_book_defect import (
    exact_source_book_partition,
    independent_physical_first_blocked_triples,
    independent_original_book_phi_tensor,
)
from hyp105_mixed_srg_referee import exact_mixed_blocker_referee


class TestIndependentAllHSourceBookDefect(unittest.TestCase):
    def referee_three_independent_routes(self,power,f,g,I=None,*,dual=False):
        source=exact_source_book_partition(power,f,g,I,dual=dual)
        physical=independent_physical_first_blocked_triples(
            power,f,g,I,dual=dual)
        tensor=independent_original_book_phi_tensor(
            power,f,g,I,dual=dual)
        old=exact_mixed_blocker_referee(power,f,g,I,dual=dual)
        self.assertEqual(source["source_original_book_phi"],tensor)
        self.assertEqual(
            source["source_original_book_phi"],old["mixed_phi_exact"])
        self.assertEqual(
            source["source_exact_blocked_triple_B"],
            physical["physical_exact_blocked_triple_B"])
        self.assertEqual(
            source["source_exact_blocked_triple_B"],
            old["independent_original_projection_blocked_triples"])
        self.assertEqual(
            source["source_good_triples"],physical["physical_triples"])
        self.assertEqual(
            source["source_original_book_phi"]-
            source["incident_original_book_defect_psi"],
            source["source_exact_blocked_triple_B"])
        self.assertEqual(
            sum(source["good_books_per_core_original_ID"].values()),
            source["source_exact_blocked_triple_B"])
        self.assertEqual(
            sum(source["incident_books_per_core_original_ID"].values()),
            source["incident_original_book_defect_psi"])
        self.assertGreaterEqual(
            source["incident_original_book_defect_psi"],0)
        self.assertTrue(source["anchor_source_flags_are_from_full_original_W3"])
        return source

    def test_true_W32_five_complete_correlated_right_g_maps_and_original_cores(self):
        m=pair_labeled_symplectic(1,"lex")
        n=len(m["incidences"])
        f=tuple(m["left_labels"])
        base=tuple(m["right_labels"])
        cases=(None,(),tuple(range(0,n,2)),
               tuple(i for i in range(n) if i%5))
        positive_incident=False
        for shift in (0,1,3,7,11):
            g=tuple(base[(i+shift)%len(base)] for i in range(len(base)))
            for core in cases:
                for dual in (False,True):
                    with self.subTest(shift=shift,core=core is None or len(core),
                                      dual=dual):
                        x=self.referee_three_independent_routes(
                            1,f,g,core,dual=dual)
                        positive_incident |= (
                            x["incident_original_book_defect_psi"]>0)
                        if core==():
                            self.assertEqual(x["source_original_book_phi"],0)
                            self.assertEqual(
                                x["source_exact_blocked_triple_B"],0)
                            self.assertEqual(
                                x["incident_original_book_defect_psi"],0)
        self.assertTrue(positive_incident)

    def test_true_W34_full_sparse_and_globally_reassigned_right_injections(self):
        cert=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json").read_text())
        f,g=tuple(map(tuple,cert["f"])),tuple(map(tuple,cert["g"]))
        n=len(genuine_source(2)[2])
        cases=[
            ("original-full",g,None),
            ("original-sparse",g,tuple(i for i in range(n) if i%3)),
            ("globally-reassigned-g",tuple(g[(i+17)%len(g)] for i in range(len(g))),
             tuple(i for i in range(n) if i%4)),
        ]
        for label,right,core in cases:
            for dual in (False,True):
                with self.subTest(label=label,dual=dual):
                    self.referee_three_independent_routes(
                        2,f,right,core,dual=dual)

    def test_incident_rejection_is_exact_not_an_optional_heuristic(self):
        m=pair_labeled_symplectic(1,"lex")
        source=exact_source_book_partition(
            1,m["left_labels"],m["right_labels"])
        self.assertGreater(source["source_original_book_phi"],0)
        self.assertGreater(
            source["incident_original_book_defect_psi"],0)
        self.assertGreater(
            source["source_exact_blocked_triple_B"],0)
        self.assertLess(
            source["source_exact_blocked_triple_B"],
            source["source_original_book_phi"])
        self.assertEqual(
            source["source_original_book_phi"],
            source["source_exact_blocked_triple_B"]+
            source["incident_original_book_defect_psi"])

    def test_invalid_original_core_and_typed_injections_fail_closed(self):
        m=pair_labeled_symplectic(1,"lex")
        f,g=m["left_labels"],m["right_labels"]
        for bad_core in ((True,),(-1,),(0,0),(45,)):
            with self.assertRaises(ValueError):
                exact_source_book_partition(1,f,g,bad_core)
            with self.assertRaises(ValueError):
                independent_physical_first_blocked_triples(
                    1,f,g,bad_core)
        with self.assertRaises(ValueError):
            exact_source_book_partition(1,f[:-1],g)
        with self.assertRaises(ValueError):
            independent_original_book_phi_tensor(1,f,g[:-1])
        with self.assertRaises(ValueError):
            exact_source_book_partition(3,f,g)


if __name__=="__main__":
    unittest.main()
