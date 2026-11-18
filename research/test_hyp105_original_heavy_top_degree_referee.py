"""AA4-HEAVY: genuinely independent source-owner, Caro-Wei and top-r tests."""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import unittest

from hyp105_original_heavy_top_degree_referee import (
    SCHEMA,ROOT_STATUS,H_FIXED,K_LOW_FIXED,OLD_R,ERROR_ALLOC,
    ceil_fraction,ceil_root,positive_dyadic_h,source_M,improved_R,
    formal_heavy_low_root,exact_formal_comparison,
    genuine_source,source_j_and_physical,independent_caro_wei,
    derandomize_typed_bits,physical_heavy_top_degree_referee,
    weighted_bipartite_top_r_falsifier,certificate
)


class TestOriginalHeavyTopR(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=certificate()

    def test_01_exact_non_rounded_all_h_source_M_H_and_R_H(self):
        m=source_M(32)
        self.assertGreater(m,1)
        self.assertLess(m,F(10001,10000))
        self.assertEqual(improved_R(32),37441)
        self.assertEqual(ceil_fraction(576*(1+64*m)),37441)
        self.assertEqual(improved_R(32)-1,37440)
        self.assertGreater(576*(1+64*m),37440)
        self.assertLess(576*(1+64*m),37441)
        self.assertEqual(OLD_R,93312)

    def test_02_top_r_graph_average_without_ceil_and_equality_example(self):
        x=weighted_bipartite_top_r_falsifier()
        self.assertEqual(x["abstract_bipartite_graphs_exhausted"],255)
        self.assertTrue(x["exact_equality_witness_2_by_4"])
        self.assertTrue(x["extra_half_from_old_chunk_bound_not_required"])

    def test_03_actual_true_symplectic_W32_W34_and_pair_injected_maps(self):
        for s in (2,4):
            for mode in ("lex","reverse","shift"):
                m=genuine_source(s,mode)
                V=(s+1)*(s*s+1)
                self.assertEqual(m["V"],V)
                self.assertEqual(len(m["flags"]),(s+1)*V)
                self.assertEqual(len(set(m["flags"])),len(m["flags"]))
                self.assertEqual(len(set(m["f"])),V)
                self.assertEqual(len(set(m["g"])),V)
                self.assertLess(comb(m["a"]-1,2),V)
                self.assertGreaterEqual(comb(m["a"],2),V)

    def test_04_true_source_J_equals_original_dual_collinear_overlap(self):
        for s in (2,4):
            m=source_j_and_physical(genuine_source(s,"reverse"))
            self.assertEqual(m["eJ"],m["point_overlaps"]+m["line_overlaps"])
            self.assertEqual(sum(len(v) for v in m["J"]),2*m["eJ"])
            self.assertTrue(all(i not in m["J"][i] for i in range(len(m["J"]))))
            self.assertTrue(all(i in m["J"][j] for j in range(len(m["J"])) for i in m["J"][j]))

    def test_05_true_original_each_named_flag_owns_two_disjoint_diagonals(self):
        for s in (2,4):
            m=source_j_and_physical(genuine_source(s,"lex"))
            self.assertEqual(len(m["physical"]),2*len(m["flags"]))
            self.assertEqual(sum(m["degree"].values()),4*len(m["flags"]))
            for i,edges in m["per_owner"].items():
                self.assertEqual(len(edges),2)
                self.assertEqual(set(edges[0])&set(edges[1]),set())
                self.assertEqual(m["physical"][edges[0]],i)
                self.assertEqual(m["physical"][edges[1]],i)

    def test_06_constructive_original_caro_wei_potential_lower(self):
        for s in (2,4):
            m=source_j_and_physical(genuine_source(s,"shift"))
            selected=independent_caro_wei(m["J"],range(len(m["flags"])))
            self.assertGreaterEqual(len(selected["owners"]),selected["lower"])
            self.assertGreaterEqual(len(selected["owners"]),selected["potential"])
            self.assertEqual(len(selected["potential_steps"]),len(selected["owners"]))
            self.assertTrue(all(F(p)<=1 for p in selected["potential_steps"]))
            self.assertTrue(all(j not in m["J"][i] for i,j in combinations(selected["owners"],2)))

    def test_07_real_source_two_consistent_whole_ID_colorings(self):
        for s in (2,4):
            m=source_j_and_physical(genuine_source(s,"lex"))
            subset=independent_caro_wei(m["J"],range(len(m["flags"])))
            bx,ids=derandomize_typed_bits(subset["owners"],m,"x")
            by,retained=derandomize_typed_bits(ids,m,"y")
            self.assertGreaterEqual(2*len(ids),len(subset["owners"]))
            self.assertGreaterEqual(2*len(retained),len(ids))
            for i in retained:
                p,l=m["flags"][i]
                self.assertNotEqual(bx[m["f"][p][0]],bx[m["f"][p][1]])
                self.assertNotEqual(by[m["g"][l][0]],by[m["g"][l][1]])

    def test_08_all_actual_nonempty_heavy_source_cases_have_unique_F_edges(self):
        for row in self.c["real_original_W32_W34_heavy_true_physical_cases"]:
            self.assertEqual(row["all_original_source_edges"],2*row["original_flag_count"])
            self.assertEqual(row["real_full_J_edges"],
                next(x["original_pencil_J_edges"] for x in row["true_original_heavy_cases"]
                     if x["HEAVY_nonvacuous"]))
            nonzero=[x for x in row["true_original_heavy_cases"] if x["HEAVY_nonvacuous"]]
            self.assertGreater(len(nonzero),0)
            for x in nonzero:
                self.assertTrue(x["all_F_edges_have_unique_original_owner"])
                self.assertTrue(x["all_source_J_independence_verified"])
                self.assertTrue(x["all_selected_source_flags_doubly_bichromatic"])
                self.assertGreater(x["true_no_clone_F_real_edges"],0)
                self.assertGreater(x["true_no_clone_F_real_vertices"],0)
                self.assertLessEqual(x["true_no_clone_F_real_vertices"],
                                     2*x["actual_physical_majority_Q_R"])
                self.assertLessEqual(x["selected_true_top_r_Y"],
                                     x["actual_physical_majority_Q_R"])
                self.assertGreaterEqual(
                    F(x["actual_F_edge_per_vertex_density"]),
                    F(x["physical_top_r_density_lower"]))

    def test_09_true_finite_heavy_selector_retains_real_majority_witnesses(self):
        for row in self.c["real_original_W32_W34_heavy_true_physical_cases"]:
            for x in row["true_original_heavy_cases"]:
                if not x["HEAVY_nonvacuous"]:
                    continue
                self.assertGreaterEqual(2*x["actual_original_heavy_witness_majority"],
                                        x["after_original_y_cut"])
                self.assertGreaterEqual(x["original_true_cross_edges"],
                                        x["actual_original_heavy_witness_majority"])
                self.assertGreaterEqual(
                    F(x["true_no_clone_F_real_edges"]),
                    F(x["sharp_top_r_average_lower"]))

    def test_10_physical_selected_flags_keep_original_both_diagonals(self):
        for row in self.c["real_original_W32_W34_heavy_true_physical_cases"]:
            for x in row["true_original_heavy_cases"]:
                if x["HEAVY_nonvacuous"]:
                    self.assertEqual(x["selected_original_true_two_diagonal_edges"],
                                     2*x["after_original_y_cut"])
                    self.assertGreaterEqual(x["original_independent_owners"],
                                            x["after_original_x_cut"])
                    self.assertGreaterEqual(x["after_original_x_cut"],
                                            x["after_original_y_cut"])

    def test_11_source_original_caro_wei_lower_beats_actual_numerical_case(self):
        for row in self.c["real_original_W32_W34_heavy_true_physical_cases"]:
            for x in row["true_original_heavy_cases"]:
                if x["HEAVY_nonvacuous"]:
                    self.assertGreaterEqual(x["original_independent_owners"],
                                            F(x["original_CaroWei_source_lower"]))
                    self.assertGreaterEqual(x["original_independent_owners"],
                                            F(x["original_CaroWei_source_potential"]))

    def test_12_independent_real_F_C6_to_actual_original_sixset_is_valid(self):
        for row in self.c["real_original_W32_W34_heavy_true_physical_cases"]:
            for x in row["true_original_heavy_cases"]:
                if x["HEAVY_nonvacuous"]:
                    ref=x["direct_C6_all_original_six_ID_inverse_proper"]
                    self.assertEqual(ref["real_F_simple_unoriented_C6"],
                                     ref["corresponding_distinct_original_D6_sixsets"])

    def test_13_full_heavy_at_T0_and_empty_heavy_with_large_diagnostic_T(self):
        for s in (2,4):
            m=source_j_and_physical(genuine_source(s,"lex"))
            x=physical_heavy_top_degree_referee(m,0)
            self.assertTrue(x["HEAVY_nonvacuous"])
            self.assertEqual(x["original_full_heavy_edges"],2*len(m["flags"]))
            no=physical_heavy_top_degree_referee(m,10**6)
            self.assertFalse(no["HEAVY_nonvacuous"])
            self.assertEqual(no["original_full_heavy_edges"],0)

    def test_14_original_edge_j_rejects_noninteger_diagnostic_T(self):
        m=source_j_and_physical(genuine_source(2,"lex"))
        for t in (-1,F(1,2),1.5):
            with self.assertRaises(ValueError):
                physical_heavy_top_degree_referee(m,t)

    def test_15_sharper_density_R_not_accidentally_old_93312(self):
        self.assertEqual(self.c["precise_fixed_H32_R"],37441)
        self.assertEqual(self.c["previous_source_R"],93312)
        gain=F(self.c["new_exact_improvement_in_heavy_delta"])
        self.assertEqual(gain,F(93312,37441)**6)
        self.assertGreater(gain,200)
        self.assertLess(gain,300)

    def test_16_formal_graph_constant_inputs_not_claimed_numerical(self):
        for bad in ((0,F(1)),(F(0),F(1)),(F(1),F(0)),
                    (F(1),F(2)),(F(1),0.2)):
            with self.assertRaises(ValueError):
                formal_heavy_low_root(*bad)
        for h in (0,7,9,33):
            with self.assertRaises(ValueError):
                improved_R(h)

    def test_17_conditional_global_ROOT_delta_increases_even_as_T_decreases(self):
        for C0,c0 in ((F(1),F(1)),(F(2),F(1,5)),(F(7,3),F(1,17))):
            old=formal_heavy_low_root(C0,c0,old=True)
            new=formal_heavy_low_root(C0,c0)
            self.assertLess(new["R"],old["R"])
            self.assertLess(int(new["fixed_T"]),int(old["fixed_T"]))
            self.assertLess(int(new["exact_s0"]),int(old["exact_s0"]))
            self.assertLess(new["exact_h0"],old["exact_h0"])
            self.assertGreater(F(new["actual_heavy_delta"]),F(old["actual_heavy_delta"]))
            self.assertEqual(new["selected_Harris_q2"],1936)
            self.assertEqual(new["selected_Harris_q3"],85184)
            self.assertTrue(new["inherited_original_LOW_and_sixID_gates_still_open"])

    def test_18_exact_lower_CaroWei_H32_sixset_quantifiers(self):
        M=source_M(32)
        alpha=F(1,16*(1+64*M))
        source_after_cuts=alpha/4
        density=source_after_cuts/F(9)
        self.assertEqual(density,F(1,576*(1+64*M)))
        self.assertGreater(density,F(1,improved_R(32)))
        self.assertEqual(improved_R(32),37441)

    def test_19_nonvacuous_TRUE_original_W34_heavy_F_has_source_injective_C6(self):
        cases=[x for row in self.c["real_original_W32_W34_heavy_true_physical_cases"]
               for x in row["true_original_heavy_cases"]
               if x["HEAVY_nonvacuous"] and
                  x["direct_C6_all_original_six_ID_inverse_proper"]
                   ["real_F_simple_unoriented_C6"]>0]
        self.assertGreater(len(cases),0)
        self.assertTrue(any(x["s"]==4 and x["mode"]=="reverse" for x in cases))
        for x in cases:
            c=x["direct_C6_all_original_six_ID_inverse_proper"]
            self.assertEqual(c["real_F_simple_unoriented_C6"],
                             c["corresponding_distinct_original_D6_sixsets"])
            self.assertGreater(c["real_F_simple_unoriented_C6"],0)
            self.assertTrue(x["all_F_edges_have_unique_original_owner"])

    def test_20_no_root_or_ASET_promotion_and_counts(self):
        c=self.c
        self.assertEqual(c["schema"],SCHEMA)
        self.assertEqual(c["status"],ROOT_STATUS)
        self.assertEqual(c["issue"],230)
        self.assertEqual(c["parent_pr"],775)
        self.assertTrue(c["all_h_full_original_HEAVY_owner_and_selected_F_lemma_PROVED_in_manuscript"])
        self.assertFalse(c["full_ROOT_PROVED_A"])
        self.assertFalse(c["ASET_exponent_claimed"])
        self.assertTrue(c["original_BBo_LOW_global_moment_prerequisites_STILL_OPEN"])
        self.assertEqual(len(c["real_original_W32_W34_heavy_true_physical_cases"]),6)
        self.assertEqual(len(c["formal_ROOT_H32_K10_same_low_with_better_heavy_top_r"]),3)


if __name__=="__main__":
    unittest.main()
