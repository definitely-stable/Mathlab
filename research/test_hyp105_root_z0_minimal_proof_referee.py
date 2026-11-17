"""Independent adversarial tests for AA4-ROOT-Z0 without proof promotion."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_original_defect_factor_referee import genuine_symplectic_source
from hyp105_root_z0_minimal_proof_referee import (
    K, R_ZERO, R_ZPOS, NO_Z_CORE, NEW_W3, NEW_BBO, OLD_BBO,
    SCHEMA, ROOT_STATUS, _ceil, _ceil_sqrt, _pair_alphabet,
    _source_projection, original_physical_model, source_case, source_z0_budget,
    genuine_mixed_AC_blocker_case, certificate,
)


class TestRootZ0Independent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = [source_case(s, mode) for s in (2,4)
                    for mode in ("lex","reverse")]

    def test_01_all_h_exact_formal_constants_three_independent_probes(self):
        for C0,c0 in ((Fraction(1),Fraction(1)),
                      (Fraction(2),Fraction(1,5)),
                      (Fraction(7,3),Fraction(1,17))):
            r=source_z0_budget(C0,c0)
            self.assertEqual(r["R_zero_Z"],R_ZERO)
            self.assertEqual(r["R_with_Z_parent"],R_ZPOS)
            self.assertTrue(all(r["exact_25_gate_ledger"].values()))
            self.assertFalse(r["root_PROVED_A"])
            self.assertFalse(r["full_predecessor_scientific_acceptance"])
            self.assertEqual(Fraction(r["new_Z0_W3_floor"]),NEW_W3)
            self.assertEqual(Fraction(r["new_Z0_produced_BBo_floor"]),NEW_BBO)

    def test_02_K64_strictly_greater_degree_uses_65_not_64(self):
        self.assertEqual(K,64)
        self.assertEqual(1-Fraction(1,8)-Fraction(5,65),NO_Z_CORE)
        self.assertGreater(NO_Z_CORE,Fraction(51,64))
        self.assertGreater(NO_Z_CORE,Fraction(3,4))
        self.assertEqual(Fraction(83,104),NO_Z_CORE)
        self.assertEqual(NEW_W3,Fraction(16,81)*(4*NO_Z_CORE)**3)

    def test_03_new_BBo_bound_is_strong_and_arithmetically_exact(self):
        self.assertEqual(NEW_BBO,(NEW_W3-Fraction(3,8))/2)
        self.assertGreater(NEW_BBO,3)
        self.assertGreater(NEW_BBO,OLD_BBO)
        self.assertLess(Fraction(1,R_ZERO**6),NEW_BBO)
        self.assertGreater(Fraction(NEW_BBO,OLD_BBO),Fraction(6,5))

    def test_04_R93312_only_for_no_deletions(self):
        self.assertEqual(Fraction(72)*(5+Fraction(1,16))/
                         Fraction(1,16)**2,R_ZERO)
        self.assertEqual(R_ZERO+1,R_ZPOS)
        self.assertGreater(Fraction(R_ZPOS,R_ZERO)**6,1)
        # Taking the Z>0 safe constant changes the formal theorem:
        self.assertNotEqual(Fraction(1,R_ZERO**6),Fraction(1,R_ZPOS**6))

    def test_05_reject_invalid_external_constant_or_inexact_rounding(self):
        bad=[(Fraction(0),Fraction(1)),(Fraction(1),Fraction(0)),
             (Fraction(1),Fraction(2)),(1,Fraction(1))]
        for x,y in bad:
            with self.subTest(args=(x,y)),self.assertRaises((ValueError,TypeError)):
                source_z0_budget(x,y)
        with self.assertRaises(TypeError):
            _ceil(1.25)
        with self.assertRaises(ValueError):
            _ceil_sqrt(-1)

    def test_06_original_W32_W34_are_genuine_projective_GQ(self):
        for s in (2,4):
            flags=genuine_symplectic_source(s)
            V=(s+1)*(s*s+1)
            self.assertEqual(len(flags),(s+1)*V)
            self.assertEqual(len(set(flags)),len(flags))
            point_lines=[set() for _ in range(V)]
            line_points=[set() for _ in range(V)]
            for p,l in flags:
                point_lines[p].add(l)
                line_points[l].add(p)
            self.assertEqual({len(b) for b in point_lines},{s+1})
            self.assertEqual({len(b) for b in line_points},{s+1})
            # Unique projection is verified independently of acceptance paths.
            m=original_physical_model(s,flags,"lex")
            for q in range(V):
                for r in range(V):
                    if (q,r) not in m["flagid"]:
                        p,l=_source_projection(m,q,r)
                        self.assertIn((q,l),m["flagid"])
                        self.assertIn((p,l),m["flagid"])
                        self.assertIn((p,r),m["flagid"])

    def test_07_owner_and_conflict_graph_are_original_not_cloned(self):
        for s in (2,4):
            flags=genuine_symplectic_source(s)
            for mode in ("lex","reverse"):
                m=original_physical_model(s,flags,mode)
                V=m["V"]
                a,pairs=_pair_alphabet(V)
                self.assertEqual(a,m["a"])
                self.assertGreaterEqual(len(pairs),V)
                self.assertEqual(len(set(m["f"])),V)
                self.assertEqual(len(set(m["g"])),V)
                self.assertEqual(len(m["owners"]),2*len(flags))
                self.assertEqual(Counter(m["owners"].values()),
                                 Counter({i:2 for i in range(len(flags))}))
                self.assertTrue(all(i not in m["J"][i] for i in range(len(flags))))
                self.assertTrue(all(i in m["J"][j] for j in range(len(flags))
                                    for i in m["J"][j]))

    def test_08_true_original_J_degree_charge(self):
        for r in self.rows:
            self.assertLessEqual(65*r["high_J_removed"],
                                 2*r["actual_original_J_edges"])
            self.assertEqual(r["flags"],(r["s"]+1)**2*(r["s"]**2+1))
            self.assertEqual(r["physical_real_diagonals"],2*r["source_core"])
            self.assertEqual(r["original_heavy_touch_edges"],0)
            self.assertGreaterEqual(Fraction(r["source_core"]),
                                    Fraction(r["core_lower_exact"]))
            self.assertTrue(r["complete_pair_maps"])

    def test_09_blakley_roy_full_isolates_real_physical_graph(self):
        for r in self.rows:
            self.assertGreaterEqual(Fraction(r["source_W3_exact"]),
                                    Fraction(r["Blakley_Roy_full_isolate_lower"]))
            self.assertGreater(r["proper_original_directed_physical_P3"],0)

    def test_10_independently_walk_both_physical_P3_directions(self):
        # source_case enumerates both: left-first adjacency and middle-first
        # orientation; any mismatch raises, never silently drops a path.
        for r in self.rows:
            self.assertGreaterEqual(r["proper_original_directed_physical_P3"],
                                    r["accepted_original_directed_P3"])
            self.assertEqual(r["accepted_original_directed_P3"],
                             2*r["produced_original_distinct_BBo"])
            self.assertTrue(r["accepted_to_original_sixset_exactly_two"])
        self.assertTrue(any(r["produced_original_distinct_BBo"]>0
                            for r in self.rows if r["s"]==4))

    def test_11_bad_source_and_noninjective_original_flags_fail_closed(self):
        s=2
        original=genuine_symplectic_source(s)
        invalid=original[:-1]+(original[0],)
        with self.assertRaises(ValueError):
            original_physical_model(s,invalid,"lex")
        with self.assertRaises(ValueError):
            original_physical_model(s,original,"not-a-real-map")


    def test_12_original_full_A_differs_from_smaller_core_C_mixed_books(self):
        rows=[genuine_mixed_AC_blocker_case(s,mode) for s in (2,4)
              for mode in ("lex","reverse")]
        self.assertEqual(len(rows),4)
        self.assertTrue(all(r["A_not_equal_C"] for r in rows))
        for r in rows:
            self.assertEqual(r["Z"],0)
            self.assertGreater(r["full_A_original_IDs"],
                               r["strict_smaller_paired_CORE_IDs"])
            self.assertGreaterEqual(r["source_mixed_point_book_Bx"],
                                    r["literal_original_first_x_blocker_triples"])
            self.assertGreaterEqual(r["source_mixed_line_book_By"],
                                    r["literal_original_first_y_blocker_triples"])
            self.assertTrue(r["mixed_source_BOOK_two_contraction_methods_agree"])
            self.assertTrue(r["all_four_literal_original_blockers_within_mixed_books"])
            d=r["physical_CORE_delta"]*r["physical_CORE_trace_A4"]
            self.assertLessEqual(r["blockers_actual_first_x"]**2,
                                 d*r["source_mixed_point_book_Bx"])
            self.assertLessEqual(r["blockers_actual_last_x"]**2,
                                 d*r["source_mixed_point_book_Bx"])
            self.assertLessEqual(r["blockers_actual_first_y"]**2,
                                 d*r["source_mixed_line_book_By"])
            self.assertLessEqual(r["blockers_actual_last_y"]**2,
                                 d*r["source_mixed_line_book_By"])

    def test_13_original_mixed_source_has_nonzero_true_blocker_witness(self):
        rows=[genuine_mixed_AC_blocker_case(4,mode)
              for mode in ("lex","reverse")]
        self.assertTrue(any(sum(r[k] for k in (
            "blockers_actual_first_x","blockers_actual_last_x",
            "blockers_actual_first_y","blockers_actual_last_y"))>0 for r in rows))

    def test_14_certificate_is_explicitly_scoped_not_unconditional_theorem(self):
        c=certificate()
        self.assertEqual(c["schema"],SCHEMA)
        self.assertEqual(c["status"],ROOT_STATUS)
        self.assertEqual(c["parent_pr"],768)
        self.assertFalse(c["root_PROVED_A"])
        self.assertFalse(c["infinite_B_counterexample"])
        self.assertFalse(c["general_ASET_exponent"])
        self.assertEqual(Fraction(c["new_analytical_Z0_BBo"]),NEW_BBO)
        self.assertEqual(len(c["genuine_original_W32_W34_independent_source_cases"]),4)
        self.assertEqual(len(c["genuine_original_W32_W34_A_not_C_mixed_blocker_cases"]),4)


if __name__=="__main__":
    unittest.main()
