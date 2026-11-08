"""Independent exact C6 source-normalization, external-theorem quantifier audits."""
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_external_c6_normalization_referee import (
    SCHEMA, ROOT_STATUS, R, _ceil, _complete, _bipartite,
    formal_external_transfer, verify_abstract_graph_budget,
    sixcycles_minroot_dfs, sixcycles_opposite_threepaths,
    oriented_sixcycle_embeddings, canonical_report,
)


class TestExternalOrdinaryC6Normalization(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=canonical_report()

    def test_primary_publication_theorem_exact_k3_r2_and_no_numeric_promotion(self):
        z=self.report
        self.assertEqual(z["schema"],SCHEMA)
        self.assertEqual(z["root_issue"],230)
        self.assertEqual(z["status"],ROOT_STATUS)
        self.assertIn("Theorem 1.1, k=3,r=2",z["external_published_theorem"])
        self.assertEqual(z["external_DOI"],"10.1017/S0963548320000206")
        self.assertFalse(z["original_source_inverse_independently_signed_off"])
        self.assertFalse(z["full_HEAVY_LOW_proof_independently_signed_off"])
        self.assertFalse(z["root_PROVED_A"])
        self.assertFalse(z["new_ASET_exponent"])

    def test_exact_rational_graph_C0_c0_three_formal_cases(self):
        rows=self.report["formal_graph_theorem_normalization"]
        self.assertEqual(len(rows),3)
        self.assertEqual([x["C0_FORMAL"] for x in rows],["1","2","7/3"])
        self.assertEqual([x["c0_FORMAL"] for x in rows],["1","1/5","1/17"])
        for x in rows:
            C,c=Fraction(x["C0_FORMAL"]),Fraction(x["c0_FORMAL"])
            t=x["T"]
            self.assertEqual(x["R"],93313)
            self.assertLess(t-1,Fraction(17,2)*R**3*C**3)
            self.assertGreaterEqual(t,Fraction(17,2)*R**3*C**3)
            self.assertEqual(Fraction(x["C6_unoriented_conditional_sextic_coefficient"]),
                             c/Fraction(R**6))
            self.assertTrue(all(x["exact_all_h_external_quantifier_gates"].values()))
            self.assertFalse(x["external_published_numeric_constants_VERIFIED"])

    def test_actual_integer_budget_exact_cubed_no_float_overflow(self):
        z=self.report["large_abstract_integer_budget_NOT_physical_source_witness"]
        C=Fraction(z["formal_C0"])
        s,v,e=z["s"],z["v"],z["e"]
        T=formal_external_transfer(C,Fraction(1))["T"]
        self.assertEqual(s,1<<60)
        self.assertGreaterEqual(e*R,s*v)
        self.assertLessEqual(2*T*v,17*s**3)
        self.assertGreaterEqual(e**3,C**3*v**4)
        self.assertGreaterEqual(Fraction(z["external_C6_sextic_floor"]),
                                Fraction(z["inherited_C6_sextic_floor"]))
        self.assertTrue(z["external_density_threshold_verified_by_exact_cubes"])

    def test_bad_density_graph_budget_rejected_even_if_many_vertices(self):
        s=1<<60
        with self.assertRaisesRegex(ValueError,"density"):
            verify_abstract_graph_budget(Fraction(1),Fraction(1),s,6,15)

    def test_missing_vertex_cap_rejected_even_when_density_meets(self):
        C,c=Fraction(1),Fraction(1)
        s=1<<60
        T=formal_external_transfer(C,c)["T"]
        v=17*s**3//(2*T)+1
        e=_ceil(Fraction(v*s,R))
        self.assertLessEqual(e,v*(v-1)//2)
        with self.assertRaisesRegex(ValueError,"vertex cap"):
            verify_abstract_graph_budget(C,c,s,v,e)

    def test_all_graph_three_oracles_sixcycle_unoriented_normalization(self):
        rows=self.report["finite_graph_three_oracle_cases"]
        self.assertEqual(len(rows),8)
        for row in rows:
            self.assertEqual(row["unoriented_C6"],row["expected_C6"])
            self.assertEqual(row["opposite_threepath_C6"],row["expected_C6"])
            self.assertEqual(row["oriented_embeddings"],12*row["unoriented_C6"])

    def test_K6_sixty_unoriented_C6_not_720(self):
        E=_complete(6)
        self.assertEqual(sixcycles_minroot_dfs(6,E),60)
        self.assertEqual(sixcycles_opposite_threepaths(6,E),60)
        self.assertEqual(oriented_sixcycle_embeddings(6,E),720)

    def test_K33_six_C6_and_K34_twentyfour_C6(self):
        for a,b,expected in ((3,3,6),(3,4,24),(2,5,0)):
            E=_bipartite(a,b)
            with self.subTest(a=a,b=b):
                self.assertEqual(sixcycles_minroot_dfs(a+b,E),expected)
                self.assertEqual(sixcycles_opposite_threepaths(a+b,E),expected)
                self.assertEqual(oriented_sixcycle_embeddings(a+b,E),12*expected)

    def test_cycles_with_isolated_vertices_same_C6_different_host_v(self):
        edges=[(i,(i+1)%6) for i in range(6)]
        self.assertEqual(sixcycles_minroot_dfs(6,edges),1)
        self.assertEqual(sixcycles_minroot_dfs(8,edges),1)
        self.assertNotEqual(Fraction(len(edges),6),Fraction(len(edges),8))

    def test_non_cycle_sixwalks_not_counted_as_simple_C6(self):
        edges=[(i,(i+1)%5) for i in range(5)]
        self.assertEqual(sixcycles_minroot_dfs(5,edges),0)
        self.assertEqual(sixcycles_opposite_threepaths(5,edges),0)
        self.assertEqual(oriented_sixcycle_embeddings(5,edges),0)

    def test_invalid_loops_parallel_clones_and_noninteger_source_graph_ids_fail_closed(self):
        cases=[(6,[(0,0)]),(6,[(0,1),(1,0)]),
               (6,[(0,6)]),(6,[(0,True)]),
               (6,[(0,1),(0,1)]),(6,[(0,1.0)])]
        for n,E in cases:
            with self.subTest(edges=E),self.assertRaises(ValueError):
                sixcycles_minroot_dfs(n,E)
        for n in (0,True,6.0):
            with self.assertRaises(ValueError):
                sixcycles_minroot_dfs(n,[])

    def test_invalid_external_numeric_inputs_fail_closed(self):
        for C,c in ((1,Fraction(1)),(Fraction(1),1),
                    (Fraction(0),Fraction(1)),(Fraction(1),Fraction(0)),
                    (Fraction(1),Fraction(2)),(Fraction(-1),Fraction(1))):
            with self.subTest(C=C,c=c),self.assertRaises(ValueError):
                formal_external_transfer(C,c)
        with self.assertRaises(ValueError):
            oriented_sixcycle_embeddings(9,[])
        with self.assertRaises(ValueError):
            verify_abstract_graph_budget(Fraction(1),Fraction(1),2,6,16)


if __name__=="__main__":
    unittest.main()
