"""Global q5 11-column decision: certified symmetry and SAT reduction tests."""
from itertools import combinations, product
import unittest

from g2bb2_anchor_sat import (
    ANCHOR, all_actions, anchor_index, build_atleast_cnf,
    canonical_anchor_family, field_action, formula_source_hash,
    verify_11_witness,
)
from lent_exhaustive import is_exact_family
from lent_hypergraph import build_forbidden_hypergraph, independent


class G2BB2AnchorTests(unittest.TestCase):
    def test_support_one_axis_max_two_independent_math(self):
        # 3 distinct singleton columns on same GF5 axis would have
        # 1+3+C(3,2)=7 >5 distinct q5 states: impossible.
        # Independently enumerate each field-value triple.
        for triple in combinations(range(1, 5), 3):
            vectors = [(x, 0, 0) for x in triple]
            self.assertFalse(is_exact_family(vectors, 5, 2))

    def test_support_two_transitive_orbit_and_symmetry_preserves_aset(self):
        graph = build_forbidden_hypergraph(5, 3, 2)
        self.assertEqual(len(tuple(all_actions(5, 3))), 384)
        self.assertEqual(len(graph.columns), 60)
        support_two = [v for v in graph.columns if sum(x != 0 for x in v) == 2]
        self.assertEqual(len(support_two), 48)
        orbit = {
            field_action(ANCHOR, p, scales, 5)
            for p, scales in all_actions(5, 3)
        }
        self.assertEqual(orbit, set(support_two))
        self.assertEqual(anchor_index(graph), graph.columns.index(ANCHOR))

        frozen = ((0, 1, 1), (0, 1, 2), (0, 1, 3), (0, 3, 1),
                  (1, 0, 2), (1, 3, 0), (2, 0, 4), (2, 4, 0),
                  (3, 0, 0), (4, 0, 0))
        self.assertTrue(is_exact_family(frozen, 5, 2))
        for p, scales in all_actions(5, 3):
            t = [field_action(v, p, scales, 5) for v in frozen]
            self.assertTrue(is_exact_family(t, 5, 2))
        normal = canonical_anchor_family(frozen)
        self.assertIn(ANCHOR, normal)
        self.assertTrue(is_exact_family(normal, 5, 2))

    def test_cnf_truth_exact_for_all_small_case_selected_families(self):
        for q,m,w,target in ((3, 2, 2, 1), (3, 2, 2, 2),
                              (5, 2, 1, 2)):
            graph = build_forbidden_hypergraph(q,m,w)
            formula = build_atleast_cnf(graph,target)
            self.assertGreaterEqual(formula.var_count,len(graph.columns))
            for mask in range(1<<len(graph.columns)):
                selected = [i for i in range(len(graph.columns))
                            if mask & (1<<i)]
                expected = (len(selected)>=target
                            and independent(mask,graph.edges))
                truth = formula.satisfied_by(formula.assignment_for(selected))
                self.assertEqual(expected,truth,(q,m,w,target,mask))
                # Independent original ASET oracle must agree with graph.
                actual = is_exact_family([graph.columns[i]
                                          for i in selected],q,2)
                self.assertEqual(independent(mask,graph.edges),actual)

    def test_anchor_is_exactly_one_positive_unit_clause(self):
        g=build_forbidden_hypergraph(5,3,2)
        cnf=build_atleast_cnf(g,11,anchored=True)
        self.assertIn((cnf.anchor+1,),cnf.clauses)
        self.assertEqual(cnf.anchor,g.columns.index((0,1,1)))
        self.assertEqual(len(g.edges),9990)
        self.assertEqual(len(formula_source_hash(g)),64)
        self.assertTrue(cnf.dimacs().startswith("p cnf "))
        # Frozen ten-column witness solves the same CNF with target 10.
        ten=((0,1,1),(0,1,2),(0,1,3),(0,3,1),
             (1,0,2),(1,3,0),(2,0,4),(2,4,0),
             (3,0,0),(4,0,0))
        selected=[g.columns.index(v) for v in ten]
        ten_cnf=build_atleast_cnf(g,10,anchored=True)
        self.assertTrue(ten_cnf.satisfied_by(ten_cnf.assignment_for(selected)))
        self.assertFalse(cnf.satisfied_by(cnf.assignment_for(selected)))

    def test_cannot_promote_unchecked_sat_model_to_witness(self):
        graph=build_forbidden_hypergraph(5,3,2)
        ten=((0,1,1),(0,1,2),(0,1,3),(0,3,1),
             (1,0,2),(1,3,0),(2,0,4),(2,4,0),
             (3,0,0),(4,0,0))
        selected=[graph.columns.index(v) for v in ten]
        with self.assertRaises(ValueError):
            verify_11_witness(selected,graph)
        with self.assertRaises((ValueError, AssertionError)):
            verify_11_witness(list(range(11)),graph)
        # An 11-set containing anchor but invalid ASET must fail.
        chosen=[graph.columns.index(ANCHOR)]
        chosen.extend(i for i in range(len(graph.columns))
                      if i not in chosen)
        with self.assertRaises(AssertionError):
            verify_11_witness(chosen[:11],graph)

    def test_invalid_transformations_rejected(self):
        for p,s in [((0,0,1),(1,1,1)),((0,1,2),(0,1,1)),
                    ((0,1,2),(1,5,1)),((0,1),(1,1))]:
            with self.assertRaises(ValueError):
                field_action((1,1,0),p,s,5)
        with self.assertRaises(ValueError):
            canonical_anchor_family(((1,0,0),(2,0,0)))


if __name__=="__main__":
    unittest.main()
