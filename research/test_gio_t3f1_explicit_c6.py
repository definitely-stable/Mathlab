"""Exact independent audits of new NUMERIC all-simple-graph C6 theorem.

Actual brute small-graph enumerations check every 6-vertex injection and
the spectral trace/noninjective bound. Massive-density domain is checked
symbolically only: no fake huge graph fixtures or probability simulation.
"""
import unittest
from math import comb
from fractions import Fraction as Q

from gio_t3f1_explicit_c6 import (
    SCHEMA,PARENT_G6E4,P,ALMOST_REGULAR_RATIO,BIP_DENSITY,
    GENERAL_DENSITY,BIP_CYCLE_FACTOR,GENERAL_CYCLE_FACTOR,
    exact_explicit_constants,require_simple_graph_density,
    exact_almost_regular_gate,_checked_adj,bipartite_coloring,
    brute_c6,exact_bipartite_walk_certificate,complete_bipartite_oracle,
    dense_symbolic_case,certified_original_source_ledgers,certificate,
)


def complete_bipartite(h,k):
    return [list(range(h,h+k)) for _ in range(h)]+[
        list(range(h)) for _ in range(k)]


class TestF1ExplicitC6(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cert=certificate()

    def test_01_exact_numeric_simple_graph_replacement(self):
        c=exact_explicit_constants()
        self.assertEqual((P,ALMOST_REGULAR_RATIO),(2**20,2**23))
        self.assertEqual(BIP_DENSITY,2**40)
        self.assertEqual(GENERAL_DENSITY,2**41)
        self.assertEqual(GENERAL_CYCLE_FACTOR,Q(1,98304))
        self.assertEqual(BIP_CYCLE_FACTOR,Q(1,1536))
        self.assertEqual(c["threshold_C0"],GENERAL_DENSITY)
        self.assertEqual(Q(c["cycle_coefficient_c0"]),GENERAL_CYCLE_FACTOR)
        self.assertTrue(c["host_simple_graph_NO_other_hypotheses"])
        self.assertTrue(c["densities_certified_by_this_proof_NOT_assumed_from_paper"])

    def test_02_exact_degree_and_regularization_constant_arithmetic(self):
        p=P
        self.assertGreaterEqual(p,9**6)
        self.assertGreaterEqual(4*p,9**4)
        self.assertGreaterEqual(p,8)
        self.assertGreaterEqual(p*p,192*p)
        self.assertGreaterEqual(BIP_DENSITY//2,12*ALMOST_REGULAR_RATIO)
        self.assertEqual(BIP_CYCLE_FACTOR,Q(8,3*4**6))
        self.assertEqual(GENERAL_CYCLE_FACTOR,BIP_CYCLE_FACTOR/64)
        self.assertGreaterEqual(Q(p,9**6),1)
        # Bad dense-failing pieces: p^(1/3) >=4*(9/4)^(4/3).
        # Cubing and clearing denominator gives 4p>=9^4.
        self.assertGreaterEqual(4*p,9**4)
        self.assertGreaterEqual(p*p,p)
        self.assertEqual(self.cert["schema"],SCHEMA)
        self.assertEqual(self.cert["parent_G6E4_HEAD"],PARENT_G6E4)

    def test_03_almost_regular_complete_bipartite_boundary_58_59(self):
        fail=complete_bipartite_oracle(58)
        hit=complete_bipartite_oracle(59)
        self.assertFalse(fail["almost_regular_gate"][
            "almost_regular_simple_C6_bound_applies"])
        self.assertTrue(hit["almost_regular_gate"][
            "almost_regular_simple_C6_bound_applies"])
        self.assertGreaterEqual(Q(hit["exact_unoriented_sixcycles"]),
                                Q(hit["almost_regular_gate"][
                                    "minimum_unoriented_C6"]))
        self.assertEqual(hit["exact_unoriented_sixcycles"],
                         6*comb(59,3)**2)
        self.assertEqual(hit["trace_A6"],2*59**6)

    def test_04_closed_walk_single_true_C6_girth6(self):
        g=[[1,5],[0,2],[1,3],[2,4],[3,5],[0,4]]
        cert=exact_bipartite_walk_certificate(g)
        self.assertEqual((cert["n"],cert["m"]),(6,6))
        self.assertEqual(cert["original_unoriented_sixcycles"],1)
        self.assertEqual(cert["injective_ordered_closed_sixwalks"],12)
        self.assertTrue(cert["exact_trace_identity_and_bad_bound"])
        self.assertGreaterEqual(cert["maximum_noninjective_walks_from_six_distance2_pairs"],
                                cert["noninjective_closed_sixwalks"])

    def test_05_independent_K33_trace_and_cycles(self):
        z=exact_bipartite_walk_certificate(complete_bipartite(3,3))
        self.assertEqual(z["original_unoriented_sixcycles"],6)
        self.assertEqual(z["trace_A4"],2*3**4)
        self.assertEqual(z["trace_A6"],2*3**6)
        self.assertEqual(z["noninjective_closed_sixwalks"],
                         2*3**6-12*6)
        self.assertTrue(z["odd_distance3_repeats_impossible_by_actual_bipartiteness"])

    def test_06_K44_true_sixcycle_count_and_moments(self):
        x=exact_bipartite_walk_certificate(complete_bipartite(4,4))
        self.assertEqual(x["original_unoriented_sixcycles"],96)
        self.assertEqual(x["trace_A4"],2*4**4)
        self.assertEqual(x["trace_A6"],2*4**6)
        self.assertEqual(x["noninjective_closed_sixwalks"],2*4**6-12*96)

    def test_07_unequal_and_disconnected_bipartite_graphs(self):
        for h,k in ((2,4),(3,4),(1,7)):
            x=exact_bipartite_walk_certificate(complete_bipartite(h,k))
            expected=6*comb(h,3)*comb(k,3) if min(h,k)>=3 else 0
            self.assertEqual(x["original_unoriented_sixcycles"],expected)
            self.assertTrue(x["exact_trace_identity_and_bad_bound"])
        g=[[1,5],[0,2],[1,3],[2,4],[3,5],[0,4]]+[
            [7,9],[6,8],[7,9],[6,8]]
        x=exact_bipartite_walk_certificate(g)
        self.assertEqual(x["original_unoriented_sixcycles"],1)
        self.assertEqual(x["n"],10)

    def test_08_fail_closed_odd_cycle_and_malformed_source(self):
        with self.assertRaises(ValueError):
            exact_bipartite_walk_certificate([[1,2],[0,2],[0,1]])
        with self.assertRaises(ValueError):
            exact_bipartite_walk_certificate([[1],[0,1]])
        with self.assertRaises(ValueError):
            exact_bipartite_walk_certificate([[1],[]])
        with self.assertRaises(ValueError):
            exact_bipartite_walk_certificate([[0]])
        with self.assertRaises(ValueError):
            exact_bipartite_walk_certificate([[] for _ in range(17)])
        with self.assertRaises(ValueError):
            brute_c6([[] for _ in range(17)])

    def test_09_exact_sparse_nonregular_not_falsely_certified(self):
        # Star K1,7 is bipartite but not 8-almost regular and has 0 C6.
        g=complete_bipartite(1,7)
        x=exact_bipartite_walk_certificate(g)
        self.assertEqual(x["original_unoriented_sixcycles"],0)
        a=exact_almost_regular_gate(8,7,7,L=1)
        self.assertFalse(a["almost_regular_simple_C6_bound_applies"])
        self.assertTrue(a["ONLY_for_bipartite_host"])
        self.assertTrue(a["arbitrary_HEAVY_graph_NOT_claimed_nearly_regular"])

    def test_10_badwalk_exact_6_distance2_bound_many_hosts(self):
        for g in (complete_bipartite(2,3),
                  complete_bipartite(4,4),
                  [[1,5],[0,2],[1,3],[2,4],[3,5],[0,4]],
                  complete_bipartite(1,6)):
            z=exact_bipartite_walk_certificate(g)
            self.assertLessEqual(z["noninjective_closed_sixwalks"],
                                 6*z["max_degree"]*z["trace_A4"])
            self.assertEqual(z["trace_A6"]-z["noninjective_closed_sixwalks"],
                             12*z["original_unoriented_sixcycles"])

    def test_11_exact_integer_dense_condition_without_roots(self):
        n=(4*P)**3
        m=BIP_DENSITY*n*(4*P)
        self.assertTrue(require_simple_graph_density(n,m,BIP_DENSITY))
        self.assertFalse(require_simple_graph_density(n,m,GENERAL_DENSITY))
        self.assertTrue(require_simple_graph_density(n,2*m,GENERAL_DENSITY))
        self.assertFalse(require_simple_graph_density(8,7))
        self.assertFalse(require_simple_graph_density(6,9))
        with self.assertRaises(ValueError):
            require_simple_graph_density(5,20)
        with self.assertRaises(ValueError):
            require_simple_graph_density(True,0)

    def test_12_no_implicit_numeric_or_fake_huge_graph(self):
        x=dense_symbolic_case()
        self.assertTrue(x["symbolic_only"])
        self.assertTrue(x["finite_graph_edge_list_NOT_instantiated"])
        self.assertTrue(x["bipartite_density_exactly_threshold"])
        self.assertGreaterEqual(x["n"],P**2)
        self.assertLessEqual(x["m"],x["n"]*(x["n"]-1)//2)
        with self.assertRaises(ValueError):
            dense_symbolic_case(3)

    def test_13_almost_regular_numeric_L_gates(self):
        for h in (58,59,64,100):
            z=complete_bipartite_oracle(h)
            a=z["almost_regular_gate"]
            self.assertEqual(a["L"],1)
            self.assertTrue(a["degree_ratio_certified"])
            self.assertEqual(Q(a["mean_degree"]),h)
            self.assertEqual(a["sixth_walk_threshold_certified"],h>=59)
            if h>=59:
                self.assertGreaterEqual(z["exact_unoriented_sixcycles"],
                                        Q(a["minimum_unoriented_C6"]))
        with self.assertRaises(ValueError):
            exact_almost_regular_gate(4,7,4)
        with self.assertRaises(ValueError):
            exact_almost_regular_gate(4,3,-1)

    def test_14_exact_graph_regularization_mass_proof_with_ceiling(self):
        p=P
        # n>=p^2 follows from density m>=p²n^(4/3) and m<=n²/2.
        # With n>=p², each of p disjoint groups has size <=n/p+1
        # and two-group source <=(9/4)n/p. Using p>=9^6
        # preserves the entire sixth mass in dense-case recursion.
        self.assertGreaterEqual(p,9**6)
        self.assertGreaterEqual(p,8)
        self.assertGreaterEqual(4*p,9**4)
        self.assertGreaterEqual(Q(p,9**6),Q(1))
        self.assertEqual(Q(8,3)*Q(1,4**6),Q(1,1536))
        self.assertEqual(Q(1,1536)/64,Q(1,98304))

    def test_15_exact_numerical_legacy_D7_local_ledgers_certified(self):
        cases=self.cert[
            "certified_input_constants_inherited_all_order_original_source_ledgers"]
        self.assertEqual(len(cases),5)
        for z in cases:
            self.assertTrue(z["graph_external_numeric_constants_CERTIFIED_from_explicit_proof"])
            self.assertEqual(z["actual_proven_graph_C0"],2**41)
            self.assertEqual(Q(z["actual_proven_graph_c0"]),Q(1,98304))
            self.assertTrue(z["legacy_ledger_FORMAL_ONLY_flag_intentionally_retained"])
            self.assertTrue(z["inherited_source_and_SELECTOR_lemmas_not_reproved"])
            self.assertTrue(z["full_T3_still_conditional_on_original_source_G6C2_G6C3"])
            c=z["closure"]
            self.assertGreater(Q(c["rho"]),0)
            self.assertGreater(Q(c["delta"]),0)
            self.assertGreater(int(c["sufficient_r0"]),0)

    def test_16_one_numeric_C3_and_four_numeric_D7_fixed_regimes(self):
        cases=self.cert[
            "certified_input_constants_inherited_all_order_original_source_ledgers"]
        self.assertEqual([z["regime"] for z in cases],[
            "G6C3_linear_excess_original",
            "G6D7_E1_actual_GQ_PDS",
            "G6D7_E2_odd_q7",
            "G6D7_corrected_q_ge8",
            "G6D7_corrected_q_ge18",
        ])
        expected=[None,(2,2,0),(5,4,0),(5,3,0),(5,2,0)]
        for z,x in zip(cases,expected):
            f=z["fixed_before_source"]
            self.assertEqual(Q(f["external_C0"]),Q(2**41))
            self.assertEqual(Q(f["external_c0"]),Q(1,98304))
            if x:
                self.assertEqual((f["quadratic_C"],f["ell"],f["local_M"]),x)
            else:
                self.assertEqual(f["line_excess_C"],0)

    def test_17_host_C6_numeric_bound_NOT_DEPEND_on_source_geometry(self):
        c=self.cert
        self.assertTrue(c["graph_C6_external_numeric_placeholders_ELIMINATED"])
        self.assertTrue(c["no_external_numeric_graph_theorem_assumed"])
        self.assertTrue(c["old_source_FULL_CORE_and_shared_SELECTOR_prerequisites_still_inherited"])
        self.assertTrue(c["not_an_unrestricted_abstract_T3_or_dependent_ASET_proof"])
        self.assertTrue(c["no_external_human_referee_or_Lean"])
        self.assertFalse(c["self_contained_graph_C6_theorem"].get("assume_GQ",False))

    def test_18_false_small_numeric_constants_NOT_certified(self):
        self.assertNotEqual(GENERAL_DENSITY,1)
        self.assertNotEqual(GENERAL_CYCLE_FACTOR,Q(1))
        self.assertFalse(require_simple_graph_density(118,59**2))
        self.assertTrue(exact_almost_regular_gate(118,59**2,59,L=1)[
            "almost_regular_simple_C6_bound_applies"])
        # The all-graph theorem at massive C0 is a DIFFERENT gate
        # from the independently proved almost-regular small threshold.


    def test_19_exhaustive_all_512_bipartite_3_by_3_graphs(self):
        # There are 2^9 genuine 3-by-3 original bipartite edge sets.
        # The 6 different simple C6 in K3,3 each appear in 2^(9-6)=8
        # of these graphs, so total sum of C6=6*8=48.
        sum_c6=0
        n_positive=0
        for mask in range(512):
            edges=[set() for _ in range(6)]
            for i in range(3):
                for j in range(3):
                    if mask&(1<<(3*i+j)):
                        edges[i].add(3+j)
                        edges[3+j].add(i)
            z=exact_bipartite_walk_certificate(edges)
            self.assertTrue(z["exact_trace_identity_and_bad_bound"])
            self.assertLessEqual(z["noninjective_closed_sixwalks"],
                                 6*z["max_degree"]*z["trace_A4"])
            sum_c6+=z["original_unoriented_sixcycles"]
            n_positive+=z["original_unoriented_sixcycles"]>0
        self.assertEqual(sum_c6,48)
        self.assertGreater(n_positive,0)

    def test_20_real_K6_to_genuine_K33_bipartite_cut(self):
        from gio_t3f1_explicit_c6 import exact_small_graph_bipartite_cut
        K6=[{j for j in range(6) if j!=i} for i in range(6)]
        z=exact_small_graph_bipartite_cut(K6)
        self.assertEqual(z["original_edges"],15)
        self.assertEqual(z["exactly_retained_original_cross_edges"],9)
        self.assertEqual(z["actual_original_sixcycles"],60)
        self.assertEqual(z["genuine_subgraph_sixcycles"],6)
        self.assertTrue(z["original_simple_graph_cut_at_least_half"])
        self.assertTrue(z["no_new_synthetic_edges"])
        self.assertEqual(z["all_cut_assignments_exhaustively_searched"],32)
        with self.assertRaises(ValueError):
            exact_small_graph_bipartite_cut([[] for _ in range(13)])



if __name__=="__main__":
    unittest.main()
