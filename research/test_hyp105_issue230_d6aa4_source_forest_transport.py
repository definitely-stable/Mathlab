"""D6-AA4-A: independent source-girth mask and conditional transport proofs."""
import unittest
from collections import Counter
from itertools import combinations

from hyp105_issue230_d6aa4_source_forest_transport import (
    EXPECTED_PAIR_SUPPORT, positional_graphs, equality_partition,
    graph_source_partition, graph_original_signature, source_forest_info,
    all_130_squared_source_support, source_key, exact_binary_coupling,
    one_sided_candidate_margins, observed_original_seven)
from hyp105_issue230_projection import fixture


class D6AA4SourceForestTests(unittest.TestCase):
    def test_complete_130_squared_exact_girth_support(self):
        x=all_130_squared_source_support()
        self.assertEqual(x["pair_patterns"],16900)
        self.assertEqual(x["admissible_abstract_source_forests"],16270)
        self.assertEqual(x["excluded_by_girth_or_duplicate"],630)
        self.assertEqual(x["allowed_positive_positional_pairs"],11430)
        self.assertEqual(x["allowed_nonseven_AA_pairs"],4840)
        self.assertEqual(x["by_class"],EXPECTED_PAIR_SUPPORT)
        self.assertEqual(sum(x["excluded_reasons"].values()),630)
        self.assertEqual(x["source_path_shapes"]["C/B"],[4,2])
        self.assertEqual(x["source_path_shapes"]["B/B-overlap"],[3,1,1,1])

    def test_source_girth_countermodels_independent_of_physical_coordinates(self):
        self.assertEqual(source_forest_info(
            (0,1,2,3,4,5),(0,1,2,3,4,5))["path_lengths"],
            (1,1,1,1,1,1))
        # B/B repeated source point and source line on identical Q positions
        self.assertEqual(source_forest_info(
            (0,0,1,2,3,4),(0,0,1,2,3,4))["reason"],
            "duplicate_original_incidence")
        # 3 original points and lines each twice, six distinct incidences
        # yield a forbidden source bipartite 6-cycle.
        src=source_forest_info(
            (0,0,1,1,2,2),(0,1,1,2,2,0))
        self.assertFalse(src["valid"])
        self.assertEqual(src["reason"],"source_cycle_shorter_than_girth8")
        # A true ORIGINAL path of 4 edges plus one path of 2.
        src=source_forest_info(
            (0,0,1,1,2,2),(0,1,1,2,3,4))
        self.assertTrue(src["valid"])
        self.assertEqual(src["path_lengths"],(4,2))

    def test_source_partition_invariant_under_typed_factor_relabeling(self):
        E=((1,3),(1,4),(2,4),(5,8),(2,9),(7,8))
        F=tuple((p*17+7,l*19+11) for p,l in E)
        self.assertEqual(source_key(tuple(range(6)),E),
                         source_key(tuple(range(6)),F))
        self.assertEqual(source_key(tuple(range(6)),E)[0],
                         (0,0,1,2,1,3))
        with self.assertRaises(ValueError):
            source_key((0,1,2,3,4,4),E)
        with self.assertRaises(ValueError):
            equality_partition((0,1,2,3,4))

    def test_130_graphs_reconstruct_original_factors_without_GF5_flows(self):
        graphs=positional_graphs()
        self.assertEqual(len(graphs),130)
        counts=Counter()
        for g in graphs:
            sig=graph_original_signature(g)
            self.assertTrue(sig["regular"])
            self.assertEqual(sig["position_graph"],g)
            p=graph_source_partition(g)
            counts[len(set(p))]+=1
        self.assertEqual(counts,Counter({6:70,5:45,3:15}))

    def test_conditional_frechet_is_sharp_by_exhaustive_small_sets(self):
        for n in range(0,6):
            pool=set(range(n))
            subsets=[set(c) for k in range(n+1)
                     for c in combinations(range(n),k)]
            for L in range(n+1):
                for R in range(n+1):
                    best=min(len(a&b) for a in subsets if len(a)==L
                             for b in subsets if len(b)==R)
                    x=exact_binary_coupling(n,L,R)
                    self.assertEqual(x["both"],best)
                    self.assertEqual(x["both"]+x["left_only"],L)
                    self.assertEqual(x["both"]+x["right_only"],R)
                    self.assertEqual(sum(x.values()),n)
        with self.assertRaises(ValueError):
            exact_binary_coupling(2,3,1)
        with self.assertRaises(ValueError):
            exact_binary_coupling(-1,0,0)

    def test_true_original_W32_independent_typed_regular_marginals(self):
        m=fixture(1,"S68")
        L=one_sided_candidate_margins(m,"left")
        R=one_sided_candidate_margins(m,"right")
        self.assertEqual(sum(L.values()),62370)
        self.assertEqual(sum(R.values()),62370)
        self.assertTrue(L)
        self.assertTrue(R)
        actual=observed_original_seven(m)
        self.assertEqual(actual["S"],68)
        self.assertEqual(actual["proxy"],331)
        self.assertEqual(actual["false_positive_types"],{"A/A_nonmatching":263})
        self.assertEqual(actual["GF5_floor_numerator"],3112510)

    def test_scope_rejects_non_W32_and_bad_budget(self):
        from hyp105_issue230_d6aa4_source_forest_transport import original_source_histogram
        with self.assertRaises(ValueError):
            one_sided_candidate_margins(fixture(2,"lex"),"left")
        with self.assertRaises(ValueError):
            one_sided_candidate_margins(fixture(1,"S68"),"invalid")
        with self.assertRaises(ValueError):
            original_source_histogram(tuple(range(45)),set(),budget=1)


if __name__=="__main__":
    unittest.main()
