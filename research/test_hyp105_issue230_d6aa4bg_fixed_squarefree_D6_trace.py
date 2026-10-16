"""AA4-BG independent nilpotent-matrix trace / fixed W32 historical GF5 falsifiers."""
import unittest
from itertools import permutations

from hyp105_issue230_projection import fixture
from hyp105_issue230_d6aa4ai_triangle_zero_c6_compensation import (
    zero_split_original_W32,
)
from hyp105_issue230_d6aa4aq_colored_original_D_cycle import (
    exact_original_rainbow_D6_cycle_transfer,
    _plain_any_six_cycle,
    original_bicolored_D_flag_graph,
)
from hyp105_g5e2b3e1b0_seven_signature import seven_census
from hyp105_issue230_d6aa4bg_fixed_squarefree_D6_trace import (
    squarefree_trace_six_dp,
    squarefree_trace_six_literal_walks,
    typed_squarefree_coefficient_witnesses,
    abstract_squarefree_six_cycle_polynomial,
)


def independent_historic_D6_from_true_source(model):
    """Historical seven-class classifier, distinct from ANY colored-D graph walk."""
    z=seven_census(model,independent_checks=False,witness_sets=True)
    return sum(label=="D6" for label in z["sets"].values())


class AA4BGFixedOriginalSquarefreeTrace(unittest.TestCase):
    def test_01_all_five_actual_W32_full_fixed_f_g_vs_historical_seven_GF5(self):
        models=[("dual_zero",zero_split_original_W32())]+[
            (scheme,fixture(1,scheme))
            for scheme in ("lex","reverse","S68","S72")]
        expected={"dual_zero":1,"lex":15,"reverse":3,"S68":0,"S72":0}
        for name,model in models:
            z=squarefree_trace_six_dp(model)
            self.assertTrue(z["roots_exhaustive"])
            self.assertEqual(z["accepted_original_six_ID_D6"],expected[name])
            self.assertEqual(z["Tr_A6_squarefree_sum_over_all_typed_degree6_coefficients"],
                             12*expected[name])
            self.assertEqual(z["accepted_original_six_ID_D6"],
                             independent_historic_D6_from_true_source(model))
            self.assertEqual(sum(n for _,_,n in typed_squarefree_coefficient_witnesses(z)),
                             12*expected[name])
            self.assertTrue(z["seven_historical_GF5_classes_total_NOT_PROVED"])

    def test_02_independent_walk_DFS_vs_nilpotent_sparse_matrix_power(self):
        for name in ("dual_zero","lex","reverse","S68","S72"):
            model=(zero_split_original_W32() if name=="dual_zero"
                   else fixture(1,name))
            z=squarefree_trace_six_dp(model)
            brute=squarefree_trace_six_literal_walks(model)
            self.assertEqual(z["sixfold_squarefree_trace_monomials"],brute)
            self.assertTrue(z["rooted_walks_enumerated_without_explicit_source_simplicity_filter"])
            self.assertTrue(z["all_original_point_and_LINE_source_factors_in_rainbow_walk_distinct"])

    def test_03_existing_rainbow_D6_unique_cycle_transfer_crosscheck(self):
        for name in ("lex","S68","S72"):
            model=fixture(1,name)
            z=squarefree_trace_six_dp(model)
            old=exact_original_rainbow_D6_cycle_transfer(model)
            self.assertEqual(z["accepted_original_six_ID_D6"],
                             old["double_rainbow_D6_original_Q_count"])
            if name.startswith("S"):
                g=original_bicolored_D_flag_graph(model)
                self.assertIsNotNone(_plain_any_six_cycle(g))
                self.assertGreater(z["actual_original_D_undirected_edges"],250)
                self.assertEqual(z["Tr_A6_squarefree_sum_over_all_typed_degree6_coefficients"],0)

    def test_04_independent_typed_physical_coordinate_gauge_is_count_preserving(self):
        m=fixture(1,"lex")
        z=squarefree_trace_six_dp(m)
        m2=dict(m,
                left_labels=tuple(tuple(sorted(((v+2)%6 for v in e)))
                                  for e in m["left_labels"]),
                right_labels=tuple(tuple(sorted(((5-v)%6 for v in e)))
                                   for e in m["right_labels"]))
        w=squarefree_trace_six_dp(m2)
        self.assertEqual(z["accepted_original_six_ID_D6"],
                         w["accepted_original_six_ID_D6"])
        self.assertEqual(z["Tr_A6_squarefree_sum_over_all_typed_degree6_coefficients"],
                         w["Tr_A6_squarefree_sum_over_all_typed_degree6_coefficients"])
        self.assertEqual(len(z["sixfold_squarefree_trace_monomials"]),
                         len(w["sixfold_squarefree_trace_monomials"]))

    def test_05_uncolored_6cycle_no_go_even_with_plenty_of_D_edges(self):
        toy=abstract_squarefree_six_cycle_polynomial()
        self.assertTrue(toy["ordinary_uncolored_has_a_simple_C6"])
        self.assertEqual(toy["fully_rainbow_trace"],12)
        self.assertEqual(toy["point_color_collision_trace"],0)
        self.assertTrue(toy["not_a_genuine_original_W3_model"])
        for scheme in ("S68","S72"):
            model=fixture(1,scheme)
            g=original_bicolored_D_flag_graph(model)
            self.assertIsNotNone(_plain_any_six_cycle(g))
            z=squarefree_trace_six_dp(model)
            self.assertEqual(z["accepted_original_six_ID_D6"],0)
            # Not even an ordinary genuine D-sixcycle suffices to force
            # an accepted ORIGINAL GF5 D6 under fully fixed f,g.

    def test_06_W34_partial_original_roots_never_claim_full_trace(self):
        model=fixture(2,"lex")
        dp=squarefree_trace_six_dp(model,roots=(0,1))
        literal=squarefree_trace_six_literal_walks(model,roots=(0,1))
        self.assertEqual(dp["sixfold_squarefree_trace_monomials"],literal)
        self.assertFalse(dp["roots_exhaustive"])
        self.assertIsNone(dp["accepted_original_six_ID_D6"])
        self.assertEqual(dp["s"],4)
        self.assertGreaterEqual(dp["Tr_A6_squarefree_sum_over_all_typed_degree6_coefficients"],0)

    def test_07_invalid_full_global_original_model_and_roots_fail_closed(self):
        m=fixture(1,"lex")
        for bad in (dict(m,left_labels=((0,1),)*15),
                    dict(m,right_labels=((0,1),)*15),
                    dict(m,incidences=m["incidences"][:-1])):
            with self.assertRaises((ValueError,AssertionError)):
                squarefree_trace_six_dp(bad)
        for badroots in ((-1,),(0,0),(999,),(True,)):
            with self.assertRaises(ValueError):
                squarefree_trace_six_dp(m,roots=badroots)
            with self.assertRaises(ValueError):
                squarefree_trace_six_literal_walks(m,roots=badroots)

if __name__=="__main__":
    unittest.main()
