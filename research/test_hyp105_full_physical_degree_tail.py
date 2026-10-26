"""Independent exact finite falsifiers for the full-H source-ID selector."""
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_full_physical_degree_tail import (
    min_degree_independent, finite_tail_selector, planted_original_k44,
    exact_bad_endpoint_population,
)
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic


class FullPhysicalTailSelection(unittest.TestCase):
    def test_minimum_degree_caro_wei_on_every_five_vertex_graph(self):
        pairs = tuple(combinations(range(5),2))
        for mask in range(1 << len(pairs)):
            adjacency = {i:set() for i in range(5)}
            for bit,(i,j) in enumerate(pairs):
                if mask >> bit & 1:
                    adjacency[i].add(j); adjacency[j].add(i)
            selected,cw = min_degree_independent(adjacency)
            self.assertGreaterEqual(len(selected),cw)
            self.assertGreaterEqual(len(selected)*(2*mask.bit_count()+5),25)

    def test_true_W32_books_and_all_original_endpoints(self):
        for scheme,expected in (
            ("lex",(26,32,104,128,79,153)),
            ("reverse-line",(26,21,104,84,53,135)),
        ):
            m = pair_labeled_symplectic(1,scheme)
            r = exact_bad_endpoint_population(1,m["left_labels"],m["right_labels"])
            self.assertEqual(tuple(r[k] for k in (
                "M_f","M_g","left_endpoint_bad","right_endpoint_bad",
                "both_endpoint_bad","union_endpoint_bad")),expected)
            self.assertFalse(r["path_weighted_endpoint_mass_bounded"])

    def test_true_W32_and_W34_selected_provenance_and_exact_bounds(self):
        for power in (1,2):
            for scheme in ("lex","reverse-line"):
                m = pair_labeled_symplectic(power,scheme)
                r = finite_tail_selector(power,m["left_labels"],m["right_labels"],Fraction(2))
                self.assertEqual(r["conflict_edges"],r["M_f_restricted"]+r["M_g_restricted"])
                self.assertEqual(r["preserved_heavy_witnesses"],r["retained_original_ids"])
                self.assertEqual(r["retained_physical_edges"],2*r["retained_original_ids"])
                self.assertGreaterEqual(4*r["retained_original_ids"]*(
                    4*r["exact_source_book_bound"]+r["input_original_ids"]),r["input_original_ids"]**2)
                self.assertEqual(r["ordinary_C6"],r["accepted_original_D6"])
                self.assertFalse(r["root_seven_lower_proved"])

    def test_true_W34_protected_positive_C6_source_classifier(self):
        f,g,ids = planted_original_k44()
        r = finite_tail_selector(2,f,g,Fraction(1,4),source_subset=ids)
        self.assertEqual(r["conflict_edges"],0)
        self.assertEqual(r["retained_original_ids"],16)
        self.assertEqual(r["ordinary_C6"],96)
        self.assertEqual(r["accepted_original_D6"],96)
        self.assertTrue(r["all_NB3_coordinate_proper"])

    def test_empty_tail_and_reject_invalid_inputs(self):
        m = pair_labeled_symplectic(1,"lex")
        f,g = m["left_labels"],m["right_labels"]
        r = finite_tail_selector(1,f,g,1000)
        self.assertEqual(r["input_original_ids"],0)
        self.assertEqual(r["retained_original_ids"],0)
        self.assertIsNone(r["balanced_chunk"])
        for threshold in (0,-1):
            with self.assertRaises(ValueError): finite_tail_selector(1,f,g,threshold)
        with self.assertRaises(ValueError): finite_tail_selector(3,f,g)
        with self.assertRaises(ValueError): finite_tail_selector(1,f[:-1],g)
        wrong=list(g);wrong[1]=wrong[0]
        with self.assertRaises(ValueError): finite_tail_selector(1,f,wrong)
        with self.assertRaises(ValueError): finite_tail_selector(1,f,g,1,source_subset=(0,0))


if __name__ == "__main__": unittest.main()
