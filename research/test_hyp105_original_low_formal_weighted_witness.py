"""AA4-LOW-FORMAL independent full-original W32/W34 and abstract type refutations."""
import unittest
from collections import Counter
from itertools import combinations, product

from hyp105_original_defect_factor_referee import genuine_symplectic_source
from hyp105_original_low_formal_weighted_witness import (
    SCHEMA, ROOT_STATUS, _edge, _other, minimal_labels, source_model,
    _physical_edges, _neighbors, _physical_moments,
    _book_source_keys, _book_contraction, _source_witness_triples,
    _literal_first_blocks, witness_certificate, true_original_case,
    abstract_adversarial_case, certificate,
)


class TestOriginalLowFormalWeightedWitness(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cert=certificate()

    def test_01_true_W32_W34_original_source_exact_flags(self):
        for s in (2,4):
            flags=genuine_symplectic_source(s)
            V=(s+1)*(s*s+1)
            self.assertEqual(len(flags),(s+1)*V)
            self.assertEqual(len(set(flags)),len(flags))
            p=Counter(a for a,_ in flags)
            l=Counter(b for _,b in flags)
            self.assertEqual(set(p.values()),{s+1})
            self.assertEqual(set(l.values()),{s+1})

    def test_02_source_book_expansion_is_exact_not_just_numerical_cap(self):
        for row in self.cert["true_original_W32_W34_correlated_fixed_map_cases"]:
            self.assertEqual(row["point_source_book_theta"],row["physical_mixed_degree_theta"])
            self.assertEqual(row["line_source_book_theta"],row["physical_mixed_degree_theta"])
            for side in ("x","y"):
                v=row[side]
                self.assertTrue(v["exact_source_book_count_verified"])
                self.assertTrue(v["all_source_triples_have_unique_reversible_witness"])
                self.assertGreaterEqual(v["original_source_book_surplus"],0)
                self.assertEqual(v["original_book_witnesses"]-
                                 v["distinct_reconstructible_source_triples"],
                                 v["original_source_book_surplus"])

    def test_03_exact_point_and_line_charges_are_both_recomputed(self):
        for row in self.cert["true_original_W32_W34_correlated_fixed_map_cases"]:
            for side in ("x","y"):
                v=row[side]
                self.assertTrue(v["physical_path_charging_all_steps_pass"])
                self.assertLessEqual(v["genuine_first_blockers"],
                                     v["direct_source_triple_two_walk_weight"])
                self.assertLessEqual(v["distinct_reconstructible_source_triples"],
                                     v["original_book_witnesses"])
                self.assertLessEqual(
                    v["direct_source_triple_two_walk_weight"]**2,
                    v["distinct_reconstructible_source_triples"]*
                    v["direct_source_triple_two_walk_square"])
                self.assertLessEqual(
                    v["direct_source_triple_two_walk_square"],
                    v["degree_weighted_physical_fourth_trace"])
                self.assertLessEqual(
                    v["degree_weighted_physical_fourth_trace"],
                    v["Delta"]*v["ordinary_physical_fourth_trace"])

    def test_04_nonempty_Z_and_actual_A_differs_from_C(self):
        rows=self.cert["true_original_W32_W34_correlated_fixed_map_cases"]
        self.assertEqual(len(rows),5)
        self.assertEqual({x["mode"] for x in rows},{"lex","reverse","shift"})
        self.assertTrue(any(x["deleted_original_Z"]>0 for x in rows))
        self.assertTrue(any(x["deleted_original_Z"]==0 for x in rows))
        for x in rows:
            self.assertTrue(x["A_not_equal_C"])
            self.assertGreater(x["full_allowed_A"],x["paired_original_CORE_C"])
            self.assertEqual(x["distinct_original_diagonals_full"],
                             2*x["full_allowed_A"])
            self.assertEqual(x["distinct_original_diagonals_core"],
                             2*x["paired_original_CORE_C"])
            self.assertTrue(x["original_first_equals_last_by_reversal"])

    def test_05_positive_genuine_original_blocker_class_not_vacuous(self):
        rows=[x for x in self.cert["true_original_W32_W34_correlated_fixed_map_cases"]
              if x["s"]==4]
        self.assertTrue(any(x["x"]["genuine_first_blockers"]>0 or
                            x["y"]["genuine_first_blockers"]>0 for x in rows))
        self.assertTrue(any(x["x"]["direct_source_triple_two_walk_weight"]>0 or
                            x["y"]["direct_source_triple_two_walk_weight"]>0
                            for x in rows))
        self.assertTrue(any(x["x"]["original_source_book_surplus"]>0 or
                            x["y"]["original_source_book_surplus"]>0 for x in rows))

    def test_06_abstract_nonGQ_partial_projection_generalization(self):
        rows=self.cert["non_GQ_partial_projection_falsifier_cases"]
        self.assertEqual(len(rows),3)
        for r in rows:
            self.assertFalse(r["strict_GQ"])
            self.assertTrue(r["source_projection_is_canonical_single_valued"])
            self.assertTrue(r["A_not_equal_C"])
            for side in ("x","y"):
                self.assertTrue(r[side]["physical_path_charging_all_steps_pass"])
                self.assertLessEqual(r[side]["direct_source_triple_two_walk_weight"]**2,
                    r[side]["original_book_witnesses"]*
                    r[side]["degree_weighted_physical_fourth_trace"])

    def test_07_vertex_weighted_fourth_trace_matches_direct_matrix_wedges(self):
        # Independent closed-fourth-walk identity on a real original W32 graph.
        s=2
        flags=genuine_symplectic_source(s)
        a,pairs=minimal_labels((s+1)*(s*s+1))
        m=source_model(flags,pairs,tuple(reversed(pairs)),require_GQ=True)
        A=set(range(len(flags)))
        C={i for i in A if i%5 not in (0,1)}
        edges=_physical_edges(m,C)
        moment=_physical_moments(m,_physical_edges(m,A),edges)
        adj=_neighbors(edges)
        vertices=list(product(range(a),repeat=2))
        row_sum_fourth=0
        weighted=0
        for v in vertices:
            # Direct four-walk endpoint v with independent middle pairs.
            fours=0
            for u in adj[v]:
                for w in adj[u]:
                    for z in adj[w]:
                        fours+=int(v in adj[z])
            row_sum_fourth+=fours
            weighted+=len(adj[v])*fours
        self.assertEqual(moment["t4"],row_sum_fourth)
        self.assertEqual(moment["weighted4"],weighted)

    def test_08_independent_book_keys_exact_source_multiplicity_on_true_W32(self):
        s=2
        flags=genuine_symplectic_source(s)
        a,pairs=minimal_labels(15)
        m=source_model(flags,pairs,pairs,require_GQ=True)
        A=set(range(len(flags)))
        C={i for i in A if i%3!=0}
        for side in ("x","y"):
            keys=_book_source_keys(m,A,C,side)
            B=_book_contraction(m,A,C,side)
            triples=_source_witness_triples(m,A,C,_physical_edges(m,C),keys,side)
            self.assertEqual(len(keys),B["B"])
            self.assertTrue(set(triples.values())<=keys)
            self.assertLessEqual(len(triples),len(keys))

    def test_09_proper_P3_first_last_blocker_counts_by_true_reversal(self):
        s=4
        flags=genuine_symplectic_source(s)
        a,pairs=minimal_labels(85)
        m=source_model(flags,pairs,tuple(reversed(pairs)),require_GQ=True)
        A=set(range(len(flags)))
        C={i for i in A if i%5 not in (0,1)}
        e=_physical_edges(m,C)
        p3=_literal_first_blocks(m,A,_neighbors(e))
        self.assertGreater(p3["proper"],0)
        self.assertEqual(p3["blocked"]["x1"],p3["blocked"]["x2"])
        self.assertEqual(p3["blocked"]["y1"],p3["blocked"]["y2"])

    def test_10_reject_duplicate_f_or_g_even_when_source_incidence_legal(self):
        flags=((0,0),(1,0),(1,1),(2,1))
        f=((0,1),(0,1),(1,2))
        g=((0,1),(0,2))
        with self.assertRaises(ValueError):
            source_model(flags,f,g)
        with self.assertRaises(ValueError):
            source_model(flags,((0,1),(0,2),(1,2)),((0,1),(0,1)))

    def test_11_reject_duplicate_source_flags_and_noncanonical_pairs(self):
        with self.assertRaises(ValueError):
            source_model(((0,0),(0,0)),((0,1),(0,2)),((0,1),(1,2)))
        with self.assertRaises(ValueError):
            source_model(((0,0),(1,1)),((1,0),(0,2)),((0,1),(1,2)))
        with self.assertRaises(ValueError):
            source_model(((0,0),(1,1)),((0,0),(0,2)),((0,1),(1,2)))

    def test_12_original_projection_is_GQ_unique_not_synthetic(self):
        for s in (2,4):
            flags=genuine_symplectic_source(s)
            V=(s+1)*(s*s+1)
            _,pairs=minimal_labels(V)
            m=source_model(flags,pairs,tuple(reversed(pairs)),require_GQ=True)
            self.assertEqual(len(m["projection"]),
                             V*V-len(flags))
            self.assertEqual(m["competing_abstract_projections"],0)
            for (q,r),(p,ell) in m["projection"].items():
                self.assertNotIn((q,r),m["flagid"])
                self.assertIn((q,ell),m["flagid"])
                self.assertIn((p,ell),m["flagid"])
                self.assertIn((p,r),m["flagid"])

    def test_13_empty_or_invalid_retained_core_fails_closed(self):
        flags=((0,0),(0,1),(1,1))
        f=((0,1),(0,2))
        g=((0,1),(1,2))
        m=source_model(flags,f,g)
        with self.assertRaises((AssertionError,ValueError)):
            witness_certificate(m,coremod=1)
        with self.assertRaises((AssertionError,ValueError)):
            witness_certificate(m,zmod=1)
        with self.assertRaises((AssertionError,ValueError)):
            witness_certificate(m,coremod=0)

    def test_14_scope_guards_do_not_claim_root_theorem_or_B75(self):
        c=self.cert
        self.assertEqual(c["schema"],SCHEMA)
        self.assertEqual(c["status"],ROOT_STATUS)
        self.assertEqual(c["parent_pr"],769)
        self.assertTrue(c["all_h_general_typed_incidence_local_extension_proved_in_manuscript"])
        self.assertTrue(c["all_h_weighted_fourth_trace_bound_proved_in_manuscript"])
        self.assertTrue(c["all_h_GQ_spectral_and_ROOT_dependencies_not_accepted_by_this_code"])
        self.assertFalse(c["root_PROVED_A"])
        self.assertFalse(c["all_h_B75_proved"])
        self.assertFalse(c["general_ASET_exponent_claimed"])


if __name__=="__main__":
    unittest.main()
