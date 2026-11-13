"""Independent true original GQ spectral incidence/physical-vertex referee.

No guessed matrix spectra; independent exact T^2 source polynomial,
physical adjacency, original source-flag rectangular corner oracle
and centered integer spectral inequality crosschecks.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import isqrt,comb
import unittest

from hyp105_original_GQ_spectral_physical_degree_referee import (
    SCHEMA,ROOT_STATUS,CASES,HIGH_ORDER_CAPACITY,
    _independent_original_GQ_integer_polynomial,
    _spectral_degree_cap_integer,_k22_degree_cap_integer,
    _all_h_root_minimal_alphabet_degree_capacity,
    _one_true_original_physical_source_degree_case,
    canonical_report
)
from hyp105_original_full_w34_weighted_risk_referee import _source


class TestTrueOriginalGQRealIncidenceSpectralPhysicalDegree(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cert=canonical_report()
        cls.rows=cls.cert["eight_complete_original_W32_W34_real_physical_source_degree_cases"]

    def test_root_acceptance_nonpromotion_and_known_spectrum_prior_art(self):
        c=self.cert
        self.assertEqual(c["schema"],SCHEMA)
        self.assertEqual(c["status"],ROOT_STATUS)
        self.assertEqual(c["issue"],230)
        for k in (
            "known_prior_art_real_GQ_incidence_spectrum_not_claimed_novel",
            "all_h_original_GQ_incidence_polynomial_T_squared_2sT_plus_s_plus_one_J",
            "all_h_CORRELATED_pair_labels_original_physical_degree_centered_spectral_bound",
            "all_h_root_minimal_alphabet_original_physical_max_degree_O_s_squared",
            "all_h_original_source_rectangle_corner_degree_equals_physical_degree",
            "all_h_original_CORE_degree_not_more_than_full_GQ_degree",
            "all_h_original_physical_degree_square_energy_leq_max_degree_times_4CORE"):
            self.assertTrue(c[k],k)
        for k in ("all_h_root_GLOBAL_original_P3_B75_proved",
                  "all_h_root_six_motif_obstruction_proved",
                  "original_HEAVY_LOW_GF5_full_chain_claimed_complete",
                  "ASET_exponent_claimed","root_PROVED_A"):
            self.assertFalse(c[k],k)

    def test_all_eight_true_original_source_flags_and_physical_degree(self):
        self.assertEqual(len(self.rows),8)
        self.assertEqual(
            [(z["original_s"],z["original_fixed_scheme"],z["original_retained_CORE"])
             for z in self.rows],list(CASES))
        for z in self.rows:
            s=z["original_s"]
            V=(s+1)*(s*s+1)
            self.assertEqual(z["original_V"],V)
            self.assertEqual(z["original_ALL_named_source_flags"],(s+1)*V)
            self.assertEqual(z["actual_original_paired_physical_edges"],
                2*z["original_CORE_retained_named_source_flags"])
            self.assertEqual(z["all_physical_original_vertices_checked"],
                z["original_minimal_pair_alphabet"]**2)
            self.assertTrue(z["exact_original_GQ_incidence_and_physical_graph_cross_oracles_passed"])
            self.assertFalse(z["root_PROVED_A"])

    def test_exact_GQ_spectral_square_polynomial_on_independent_W32_W34(self):
        seen=set()
        for s,scheme,core in CASES:
            if s in seen:continue
            seen.add(s)
            c=_source(s,scheme,core)
            z=_independent_original_GQ_integer_polynomial(s,c["flags"])
            self.assertTrue(z["all_fixture_source_spectral_identities_passed"])
            self.assertEqual(z["exact_integer_T_squared_identity_entries_checked"],
                             c["V"]**2)
            self.assertEqual(z["known_REAL_incidence_singular_square_top"],(s+1)**2)
            self.assertEqual(z["known_REAL_incidence_singular_square_nontrivial"],2*s)
            self.assertEqual(z["known_REAL_incidence_singular_square_zero"],0)
            self.assertEqual(z["known_spectral_multiplicity_top"],1)
            self.assertEqual(z["known_spectral_multiplicity_2s"],s*(s+1)**2//2)
            self.assertEqual(z["known_spectral_multiplicity_zero"],
                             c["V"]-1-s*(s+1)**2//2)
            self.assertEqual(z["exact_original_GQ_point_graph_SRG_lambda"],s-1)
            self.assertEqual(z["exact_original_GQ_point_graph_SRG_mu"],s+1)

    def test_source_incidence_polynomial_strong_regular_via_triple_counts(self):
        # New oracle separately checks original point-graph nontrivial
        # SRG lambda/mu through neighbor intersections, not eigen floats.
        for s in (2,4):
            c=_source(s,"lex","full")
            P=defaultdict(set); L=defaultdict(set)
            for p,l in c["flags"]:
                P[p].add(l)
                L[l].add(p)
            graph=defaultdict(set)
            for points in L.values():
                for a,b in combinations(points,2):
                    graph[a].add(b);graph[b].add(a)
            self.assertTrue(all(len(graph[p])==s*(s+1) for p in range(c["V"])))
            for p in range(c["V"]):
                for q in range(p+1,c["V"]):
                    shared=len(graph[p]&graph[q])
                    self.assertEqual(shared,s-1 if q in graph[p] else s+1)

    def test_minimal_alphabet_all_h_numeric_capacity_exact_integer(self):
        caps=self.cert["independent_all_order_algebraic_minimal_alphabet_spectral_capacity"]
        expected={2:(6,11,15,15),4:(14,41,46,65),
                  8:(35,145,153,306),16:(94,548,559,1581),
                  32:(261,2129,2145,8580),
                  64:(731,8366,8389,47450)}
        self.assertEqual([z["original_s"] for z in caps],list(HIGH_ORDER_CAPACITY))
        for z in caps:
            s=z["original_s"]
            a,cen,unc,naive=expected[s]
            self.assertEqual(z["original_minimal_pair_alphabet_a"],a)
            self.assertEqual(z["uniform_centered_spectral_degree_cap"],cen)
            self.assertEqual(z["uniform_uncentered_spectral_degree_cap"],unc)
            self.assertEqual(z["uniform_original_source_naive_degree_cap"],naive)
            self.assertLess(cen,naive)
            self.assertEqual(z["uniform_best_spectral_K22_degree_cap"],
                             min(cen,z["uniform_independent_K22_degree_cap"],naive))
            self.assertEqual(z["original_F_incidence_flags"],
                             (s+1)*(s+1)*(s*s+1))
            self.assertTrue(z["derived_original_physical_max_degree_O_s_squared_at_minimal_alphabet"])
            self.assertEqual(z["no_GQ_fixture_claimed_for_s_greater_than_four"],s>4)
            self.assertTrue(z["does_NOT_prove_original_weighted_B_over_M_below_three_quarters"])
            self.assertGreaterEqual(comb(a,2),z["original_V"])
            self.assertLess(comb(a-1,2),z["original_V"])

    def test_each_real_original_physical_vertex_degree_vs_true_full_incidence(self):
        for z in self.rows:
            self.assertLessEqual(z["actual_CORE_original_max_physical_vertex_degree"],
                z["actual_full_original_max_physical_vertex_degree"])
            self.assertLessEqual(z["actual_full_original_max_physical_vertex_degree"],
                z["original_max_local_best_spectral_K22_degree_cap"])
            self.assertLessEqual(z["original_max_local_best_spectral_K22_degree_cap"],
                z["root_minimal_alphabet_all_h_uniform_capacity"][
                    "uniform_best_spectral_K22_degree_cap"])
            self.assertLessEqual(z["original_max_local_centered_spectral_degree_cap"],
                z["root_minimal_alphabet_all_h_uniform_capacity"][
                    "uniform_centered_spectral_degree_cap"])
            self.assertGreater(z["actual_full_original_max_physical_vertex_degree"],0)

    def test_all_true_original_GQ_physical_degree_second_moment_cap(self):
        for z in self.rows:
            full=z["original_full_physical_vertex_degree_square_sum"]
            pruned=z["original_retained_physical_vertex_degree_square_sum"]
            self.assertGreater(full,0)
            self.assertGreater(pruned,0)
            self.assertLessEqual(pruned,full)
            self.assertLessEqual(full,
                z["actual_full_original_max_physical_vertex_degree"]*
                4*z["original_ALL_named_source_flags"])
            self.assertLessEqual(pruned,
                z["actual_CORE_original_max_physical_vertex_degree"]*
                4*z["original_CORE_retained_named_source_flags"])

    def test_exact_real_physical_graph_second_moment_from_adjacency_independent(self):
        for s,scheme,core in CASES:
            c=_source(s,scheme,core)
            row=next(q for q in self.rows if
                (q["original_s"],q["original_fixed_scheme"],
                 q["original_retained_CORE"])==(s,scheme,core))
            a=c["a"]
            adj_degrees=[len(c["adj"].get((x,y),()))
                         for x in range(a) for y in range(a)]
            self.assertEqual(sum(adj_degrees),4*len(c["ids"]))
            self.assertEqual(sum(t*t for t in adj_degrees),
                             row["original_retained_physical_vertex_degree_square_sum"])
            self.assertEqual(max(adj_degrees),
                             row["actual_CORE_original_max_physical_vertex_degree"])
            self.assertEqual(len(c["owner"]),2*len(c["ids"]))

    def test_actual_SOURCE_core_pruning_only_reduces_true_physical_degrees(self):
        for s in (2,4):
            cases=[z for z in self.rows if z["original_s"]==s]
            for row in cases:
                self.assertLessEqual(row["actual_CORE_original_max_physical_vertex_degree"],
                                     row["actual_full_original_max_physical_vertex_degree"])
            if s==4:
                e=next(z for z in cases if z["original_retained_CORE"]=="even")
                self.assertLess(e["actual_CORE_original_max_physical_vertex_degree"],
                                e["actual_full_original_max_physical_vertex_degree"])

    def test_centered_spectral_mixing_exact_rational_integer_falsifier(self):
        # Manual direct original GQ submatrix incidence count for every
        # physical vertex; independent from physical graph adjacency.
        for s,scheme,core in CASES:
            c=_source(s,scheme,core)
            V=c["V"];a=c["a"]
            P={x:{p for p in range(V) if x in c["f"][p]} for x in range(a)}
            L={y:{l for l in range(V) if y in c["g"][l]} for y in range(a)}
            for x in range(a):
                for y in range(a):
                    e=sum(1 for p,l in c["flags"] if p in P[x] and l in L[y])
                    r=len(P[x]);t=len(L[y])
                    num=V*e-(s+1)*r*t
                    rad=2*s*r*(V-r)*t*(V-t)
                    self.assertLessEqual(num*num,rad)
                    self.assertLessEqual(e,_spectral_degree_cap_integer(s,V,r,t))
                    self.assertLessEqual(e,_k22_degree_cap_integer(r,t))

    def test_K22_bound_agrees_with_manual_exact_first_second_moment(self):
        for r in range(1,15):
            for c in range(1,15):
                cap=_k22_degree_cap_integer(r,c)
                self.assertGreaterEqual(cap,0)
                self.assertLessEqual(cap,r*c)
                self.assertEqual(cap,_k22_degree_cap_integer(c,r))
                self.assertLessEqual(cap*cap-r*cap,r*c*(c-1))
                self.assertLessEqual(cap*cap-c*cap,c*r*(r-1))
        self.assertEqual(_k22_degree_cap_integer(0,12),0)
        self.assertEqual(_k22_degree_cap_integer(12,0),0)

    def test_original_independent_full_physical_vertex_degree_witness_grounded(self):
        for z in self.rows:
            w=z["real_original_physical_degree_witness"]
            self.assertEqual(len(w["physical_vertex"]),2)
            self.assertEqual(w["actual_full_original_degree"],
                             z["actual_full_original_max_physical_vertex_degree"])
            self.assertLessEqual(w["actual_retained_original_CORE_degree"],
                                 w["actual_full_original_degree"])
            self.assertLessEqual(w["actual_full_original_degree"],
                                 w["local_centered_spectral_degree_cap"])
            self.assertLessEqual(w["actual_full_original_degree"],
                                 w["local_K22_only_degree_cap"])
            self.assertGreaterEqual(w["exact_GQ_centered_mixing_squared_slack"],0)

    def test_spectral_degree_bound_not_an_accepted_global_weighted_B75_proof(self):
        for z in self.rows:
            self.assertFalse(z["root_PROVED_A"])
            self.assertFalse(z["full_all_h_B75_proved"])
        self.assertFalse(self.cert["all_h_root_six_motif_obstruction_proved"])
        self.assertFalse(self.cert["all_h_root_GLOBAL_original_P3_B75_proved"])

    def test_fail_closed_invalid_alphabet_and_dyadic_quantifiers(self):
        for s in (1,3,6,7,0,-2):
            with self.assertRaises(ValueError):
                _all_h_root_minimal_alphabet_degree_capacity(s)
        for s,V,r,c in ((2,15,-1,3),(2,15,2,16),
                        (4,85,86,1),(2,15,3,-2)):
            with self.assertRaises(ValueError):
                _spectral_degree_cap_integer(s,V,r,c)
        for r,c in ((-1,2),(2,-1)):
            with self.assertRaises(ValueError):
                _k22_degree_cap_integer(r,c)
        with self.assertRaises(ValueError):
            _independent_original_GQ_integer_polynomial(8,tuple())

    def test_full_and_pruned_source_physical_degree_sum_true_incidence(self):
        for z in self.rows:
            self.assertEqual(z["original_source_point_and_line_pair_label_total_occupancy"],
                2*z["original_V"])
            self.assertEqual(z["actual_original_paired_physical_edges"],
                2*z["original_CORE_retained_named_source_flags"])
            self.assertGreater(z["original_full_physical_vertex_degree_square_sum"],
                4*z["original_ALL_named_source_flags"])
            self.assertGreaterEqual(z["original_retained_physical_vertex_degree_square_sum"],
                4*z["original_CORE_retained_named_source_flags"])

if __name__=="__main__":
    unittest.main()
