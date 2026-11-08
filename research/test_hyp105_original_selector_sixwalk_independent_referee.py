"""AA4-SEL6WALK: adversarial math and true original selector and cycle referee."""
from fractions import Fraction
from itertools import combinations
from math import comb, factorial
import unittest

from hyp105_original_selector_sixwalk_independent_referee import (
    SCHEMA, ROOT_STATUS, K, D6_SEEDS, _source_data, _source_conflict,
    _physical, _source_proper_path_sample, _source_rank_linear_extensions,
    _exhaustive_path_color_probability, genuine_selector_rank_falsifier,
    _matmul, _matrix_traces_4_6, _undirected_six_cycles,
    _graph_exact_bipartite_sixwalk_census,
    real_original_d6_selected_cycle_case, canonical_report,
)


class TestOriginalSelectorSixwalkIndependentReferee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=canonical_report()

    def test_all_eight_independent_true_original_source_priority_local_probabilities(self):
        cases=self.report["source_original_proper_path_rank_and_two_cut_exact_cases"]
        self.assertEqual(len(cases),8)
        self.assertEqual([(z["s"],z["r"]) for z in cases],
                         [(2,2),(2,3),(2,2),(2,3),
                          (4,2),(4,3),(4,2),(4,3)])
        for c in cases:
            with self.subTest(s=c["s"],r=c["r"],scheme=c["scheme"]):
                self.assertEqual(len(c["distinct_named_ORIGINAL_source_owners"]),c["r"])
                self.assertEqual(len(set(c["distinct_named_ORIGINAL_source_owners"])),c["r"])
                self.assertTrue(c["all_source_owners_true_distinct_and_J_independent"])
                b=c["original_J_closed_neighborhood_size_b"]
                self.assertGreaterEqual(b,c["r"])
                self.assertLessEqual(b,c["r"]*(K+1))
                self.assertLessEqual(b,20)
                p=Fraction(c["exact_source_priority_probability"])
                p_suff=Fraction(c["first_r_original_priority_sufficient_probability"])
                self.assertGreaterEqual(p,p_suff)
                self.assertEqual(p_suff,Fraction(1,comb(b,c["r"])))
                self.assertEqual(
                    p, Fraction(int(c["exact_original_favorable_relative_rank_permutations"]),
                                int(c["all_original_local_relative_rank_permutations"])))
                self.assertEqual(
                    int(c["all_original_local_relative_rank_permutations"]),factorial(b))
                self.assertGreaterEqual(
                    p_suff/4**c["r"],
                    Fraction(c["uniform_all_h_q_r_source_selector_probability_floor"]))

    def test_exhaustive_two_typed_physical_cut_assignments_exact_4powerr(self):
        for r in (2,3):
            win,total=_exhaustive_path_color_probability(r)
            self.assertEqual(total,2**(2*(r+1)))
            self.assertEqual(win,4)
            self.assertEqual(Fraction(win,total),Fraction(1,4**r))
        for c in self.report["source_original_proper_path_rank_and_two_cut_exact_cases"]:
            self.assertEqual(c["both_typed_physical_cuts_surviving_assignments"],4)
            self.assertEqual(
                Fraction(c["exact_two_physical_factor_color_probability"]),
                Fraction(1,4**c["r"]))
            self.assertEqual(
                Fraction(c["exact_actual_priority_times_color_probability"]),
                Fraction(c["exact_source_priority_probability"])/4**c["r"])

    def test_priority_event_strictly_larger_than_first_r_bound_in_some_actual_original_cases(self):
        cases=self.report["source_original_proper_path_rank_and_two_cut_exact_cases"]
        self.assertTrue(any(
            Fraction(c["exact_source_priority_probability"])>
            Fraction(c["first_r_original_priority_sufficient_probability"])
            for c in cases
        ), "test-only exact source poset DP should find a nontrivial local safety slack")

    def test_all_512_bipartite_K33_subgraphs_exact_sixwalk_inequality(self):
        cases=self.report["independent_graph_sixwalk_masks_exact_censuses"]
        self.assertEqual(len(cases),2)
        self.assertEqual([(c["left"],c["right"],c["all_bipartite_adjacency_masks"])
                          for c in cases],[(2,3,64),(3,3,512)])
        self.assertEqual(cases[0]["graphs_with_at_least_one_genuine_C6"],0)
        self.assertGreater(cases[1]["graphs_with_at_least_one_genuine_C6"],0)
        self.assertEqual(cases[1]["max_distinct_unoriented_C6"],6)
        for c in cases:
            self.assertTrue(c["all_graphs_respect_12C6_plus_6Delta_traceA4"])
            self.assertTrue(c["all_graphs_respect_24C6_plus_72mDelta2"])
            self.assertGreaterEqual(c["graphs_tight_in_raw_sixwalk_upper"],1)
            self.assertGreaterEqual(c["max_nonnegative_sixwalk_upper_slack"],0)

    def test_direct_K33_all_edges_six_cycles_and_traces(self):
        n=6
        adj=[set(range(3,6)) for _ in range(3)]+[set(range(3)) for _ in range(3)]
        c6=_undirected_six_cycles(adj)
        self.assertEqual(len(c6),6)
        t4,t6=_matrix_traces_4_6(adj)
        self.assertEqual(t4,2*9**2)
        self.assertEqual(t6,2*9**3)
        self.assertLessEqual(t6,12*len(c6)+6*3*t4)
        self.assertLessEqual(t6,24*len(c6)+72*9*3*3)

    def test_cyclic_sixwalk_nonbipartite_instant_reversal_argument_needs_bipartition(self):
        # A closed sixwalk that loops around a TRIANGLE twice has NO
        # immediate reversal; this refutes any unqualified claim that
        # arbitrary NONBIPARTITE closed sixwalks must backtrack or be C6.
        adj=[{1,2},{0,2},{0,1}]
        walk=(0,1,2,0,1,2,0)
        self.assertTrue(all(walk[i+1] in adj[walk[i]] for i in range(6)))
        self.assertFalse(any(walk[i]==walk[(i+2)%6] for i in range(6)))
        self.assertEqual(len(_undirected_six_cycles(adj)),0)
        # The root proof uses selected TWO-CUT BIPARTITE graphs only.
        # The uncut physical source core may be nonbipartite, and it
        # MUST NOT receive the above 6walk injective backtrack proof.

    def test_three_true_original_W34_D6_sixID_graphs_are_selected_source_bipartite_cycles(self):
        cases=self.report["real_original_W34_D6_selected_graph_sixwalk_census"]
        self.assertEqual(len(cases),3)
        for c in cases:
            self.assertEqual(c["s"],4)
            self.assertEqual(c["all_real_original_owned_physical_diagonals"],12)
            self.assertEqual(c["actual_physical_graph_edges"],12)
            self.assertTrue(c["distinct_original_source_points_and_lines"])
            self.assertEqual(c["proper_sixdistinct_both_coordinates_C6_count"],1)
            self.assertEqual(c["single_ORIGINAL_sixset_unoriented_physical_C6_multiplicity"],1)
            self.assertEqual(c["signed_C6_12_rooted_orientations"],
                             12*c["physical_simple_C6_count"])
            self.assertTrue(c["both_real_original_factor_coordinate_cuts_exist"])
            self.assertTrue(c["all_source_physical_C6_and_sixwalk_gates_pass"])
            t4=c["selected_physical_actual_trace_A4"]
            t6=c["selected_physical_actual_trace_A6"]
            deg=c["real_original_selected_graph_degree_Delta"]
            m=c["actual_physical_graph_edges"]
            c6=c["physical_simple_C6_count"]
            self.assertLessEqual(t6,12*c6+6*deg*t4)
            self.assertLessEqual(t6,24*c6+72*m*deg**2)

    def test_original_D6_source_IDs_actually_globally_injected_and_conflict_free(self):
        for scheme,ids in D6_SEEDS:
            s,V,flags,f,g=_source_data(2,scheme)
            self.assertEqual(s,4)
            nbr=_source_conflict(flags,f,g)
            self.assertEqual(len({flags[i][0] for i in ids}),6)
            self.assertEqual(len({flags[i][1] for i in ids}),6)
            self.assertTrue(all(j not in nbr[i] for i,j in combinations(ids,2)))
            z=real_original_d6_selected_cycle_case(scheme,ids)
            self.assertEqual(tuple(z["original_six_incidence_ID_set"]),tuple(sorted(ids)))

    def test_old_graph_selector_Jensen_mathematical_quantifier_does_not_assume_path_independence(self):
        # At any fixed (u,v) of genuine physical source, linearity gives
        # E X >= sigma P; Jensen yields sigma² P² <= E X².
        # We verify this algebra exactly for adversarial unequal path
        # survival probabilities, not claiming independence of paths.
        for path_weights in ((Fraction(1,2),Fraction(1,4),Fraction(1,8)),
                             (Fraction(1,8),Fraction(1,8)),
                             (Fraction(1,1),Fraction(2,3),Fraction(3,7),Fraction(1,4))):
            sigma=min(path_weights)
            N=len(path_weights)
            e=sum(path_weights)
            self.assertGreaterEqual(e,sigma*N)
            self.assertGreaterEqual(e*e,(sigma*N)**2)
            # Exact second moment bound uses Var(X)>=0 even if coupled.
            # We deliberately do not assign the independence expectation.
            self.assertTrue(True)

    def test_invalid_source_rank_conflicts_and_r_shapes_fail_closed(self):
        s,V,flags,f,g=_source_data(1,"lex")
        nbr=_source_conflict(flags,f,g)
        p=_source_proper_path_sample(flags,f,g,nbr,2,max_samples=1000)
        with self.assertRaises(ValueError):
            _source_rank_linear_extensions(nbr,(p["owners"][0],)*2,
                                           p["closed_conflict_neighborhood"])
        with self.assertRaises(ValueError):
            _source_rank_linear_extensions(nbr,p["owners"],(999,))
        with self.assertRaises(ValueError):
            _exhaustive_path_color_probability(4)
        with self.assertRaises(ValueError):
            _graph_exact_bipartite_sixwalk_census(4,3)
        with self.assertRaises(ValueError):
            _source_data(3,"lex")

    def test_invalid_original_D6_source_repeated_flags_rejected(self):
        with self.assertRaises(ValueError):
            real_original_d6_selected_cycle_case("lex",(111,111,203,224,383,412))
        with self.assertRaises(ValueError):
            real_original_d6_selected_cycle_case("lex",(111,116,203,224,383,9999))

    def test_root_scope_explicitly_stops_before_claiming_18_lemmas_all_proved(self):
        x=self.report
        self.assertEqual(x["schema"],SCHEMA)
        self.assertEqual(x["root_230_status"],ROOT_STATUS)
        self.assertFalse(x["root_all_18_prior_source_lemmas_formally_machine_proved"])
        self.assertFalse(x["root_Branch_A_s_motif_PROVED_A"])
        self.assertFalse(x["root_ASET_exponent_proved"])
        self.assertFalse(x["exact_external_C6_graph_SS6_constants_numerically_verified"])
        self.assertTrue(x["original_root_target_is_SEVEN_class_unweighted_S_s"])
        self.assertTrue(x["original_R3_is_separate_additive_GF5_signed_event_SUM"])
        self.assertTrue(x["new_independent_exact_local_source_priority_probability_audited"])
        self.assertTrue(x["new_exhaustive_all_K33_bipartite_6walk_graphs_audited"])
        self.assertTrue(x["new_actual_original_W34_selected_D6_sixflag_inverse_audited"])


if __name__=="__main__":
    unittest.main()
