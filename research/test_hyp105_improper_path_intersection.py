"""AA4-B2INT: original source and all-physical-grid proper/improper path audit."""
from fractions import Fraction
from itertools import combinations,product
import json
from pathlib import Path
import unittest

from hyp105_improper_path_intersection import (
    exact_improper_path_grid_certificate,
    genuine_original_improper_path_referee,
    allh_improved_core_path_constants,
)
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_full_physical_degree_tail import genuine_source


def physical_grid_all_pair_different_graph(a,b,mask):
    """Independent generator of ALL permissible physical 2×4-grid graphs."""
    vertices=tuple(product(range(a),range(b)))
    eligible=tuple((u,v) for u,v in combinations(vertices,2)
                   if u[0]!=v[0] and u[1]!=v[1])
    if mask<0 or mask>=1<<len(eligible):
        raise ValueError("mask out of valid physical grid edge range")
    adj={v:set() for v in vertices}
    for k,(u,v) in enumerate(eligible):
        if mask>>k&1:
            adj[u].add(v)
            adj[v].add(u)
    return adj,len(eligible)


class TestImproperSourcePathIntersection(unittest.TestCase):
    def test_all_4096_simple_two_by_four_physical_grid_graphs(self):
        # Every one of 2^12 graphs. All source-FREE physical inclusion/
        # exclusion and 2/3path walk statistics computed by direct DFS.
        for mask in range(1<<12):
            graph,n=physical_grid_all_pair_different_graph(2,4,mask)
            self.assertEqual(n,12)
            row=exact_improper_path_grid_certificate(graph)
            self.assertEqual(
                row["improper_B2_total_exact"],
                row["Qx_direct_two_coordinate_returns"]+
                row["Qy_direct_two_coordinate_returns"]-2*row["edges"])
            self.assertEqual(
                row["trace_A0_fourth_exact"],
                row["proper_P2_frobenius_squared"]+
                row["improper_B2_frobenius_squared"]+
                2*row["cross_P2_B2"])
            self.assertLessEqual(
                row["trace_A0_fourth_exact"],
                row["new_fourth_upper_given_exact_P2"])
            self.assertLessEqual(
                row["direct_improper_threewalks"],
                row["new_improper_three_upper"])
            self.assertLessEqual(
                row["new_improper_three_upper"],
                row["old_improper_three_upper"])
            self.assertLessEqual(
                row["new_fourth_upper_given_exact_P2"],
                row["old_fourth_upper_given_exact_P2"])

    def test_w32_five_legal_right_permutations_original_full_sparse_empty_and_dual(self):
        model=pair_labeled_symplectic(1,"lex")
        f=tuple(model["left_labels"])
        g0=tuple(model["right_labels"])
        _,V,flags=genuine_source(1)
        for shift in (0,1,3,7,11):
            g=tuple(g0[(i+shift)%V] for i in range(V))
            for core in (
                None,(),
                tuple(range(0,len(flags),2)),
                tuple(i for i in range(len(flags)) if i%3),
            ):
                for pointmap,linemap in ((f,g),(g,f)):
                    with self.subTest(shift=shift,core=core is None or len(core),
                                      dual=(pointmap is g)):
                        c=genuine_original_improper_path_referee(
                            1,pointmap,linemap,core)
                        z=c["physical"]
                        self.assertTrue(c["source_and_physical_independent_verification"])
                        self.assertEqual(
                            c["original_source_B2_union_exact"],
                            4*c["original_core_incidence_flag_count_N0"]+
                            4*(c["original_source_Mf"]+c["original_source_Mg"]))
                        self.assertEqual(
                            z["improper_B2_total_exact"],
                            c["original_source_B2_union_exact"])
                        self.assertEqual(
                            z["direct_proper_threewalks"]+
                            z["direct_improper_threewalks"],
                            z["direct_threewalk_total"])

    def test_w34_independent_original_source_dense_sparse_reassigned_duals(self):
        fixture=json.loads(Path(__file__).with_name(
            "hyp105_w34_adversarial_certificate.json").read_text())
        f=tuple(map(tuple,fixture["f"]))
        g=tuple(map(tuple,fixture["g"]))
        _,V,flags=genuine_source(2)
        cases=(
            ("dense",None,g),
            ("sparse",tuple(i for i in range(len(flags)) if i%3),g),
            ("reassigned",tuple(i for i in range(len(flags)) if i%4),
                tuple(g[(i+17)%V] for i in range(V))),
        )
        for name,core,right in cases:
            for a,b in ((f,right),(right,f)):
                with self.subTest(name=name,dual=a is right):
                    row=genuine_original_improper_path_referee(2,a,b,core)
                    x=row["physical"]
                    self.assertEqual(
                        row["original_source_Qx"],
                        x["Qx_direct_two_coordinate_returns"])
                    self.assertEqual(
                        row["original_source_Qy"],
                        x["Qy_direct_two_coordinate_returns"])
                    self.assertLessEqual(
                        x["direct_improper_threewalks"],
                        x["new_improper_three_upper"])
                    self.assertTrue(x["identity_verified_on_given_graph"])

    def test_uniform_all_h_s64_conservative_constants_gain(self):
        for K in (0,1,64,100):
            for T in (1,2,64,2**65):
                with self.subTest(K=K,T=T):
                    c=allh_improved_core_path_constants(K,T)
                    self.assertEqual(c["old_core_L4_nonproper_coefficient"],56*T)
                    self.assertEqual(c["new_core_L4_nonproper_coefficient"],40*T)
                    self.assertEqual(c["old_improper_P3_coefficient"],84*T)
                    self.assertEqual(c["new_improper_P3_coefficient"],68*T)
                    self.assertEqual(c["strict_L4_nonproper_gain"],16*T)
                    self.assertEqual(c["strict_P3_improper_gain"],16*T)
                    self.assertEqual(c["L4_proper_square_constant_gain"],16)
                    self.assertLess(c["new_L6"],c["old_L6"])
                    self.assertFalse(c["full_Branch_A_acceptance"])

    def test_fail_closed_invalid_edges_sources_and_core(self):
        invalid=(
            {(0,0):{(0,1)},(0,1):{(0,0)}},  # same left symbol
            {(0,0):{(1,0)},(1,0):{(0,0)}},  # same right symbol
            {(0,0):{(1,1)},(1,1):set()},   # asymmetric
            {(0,0):{(0,0)}},               # self-loop
            {(0,0):{(1,1)}},               # missing opposite vertex
        )
        for graph in invalid:
            with self.assertRaises(ValueError):
                exact_improper_path_grid_certificate(graph)
        m=pair_labeled_symplectic(1,"lex")
        f,g=m["left_labels"],m["right_labels"]
        for core in ((True,),(-1,),(0,0),(45,)):
            with self.assertRaises(ValueError):
                genuine_original_improper_path_referee(1,f,g,core)
        with self.assertRaises(ValueError):
            genuine_original_improper_path_referee(1,f[:-1],g)
        with self.assertRaises(ValueError):
            genuine_original_improper_path_referee(3,f,g)
        with self.assertRaises(ValueError):
            allh_improved_core_path_constants(64,0)

    def test_exact_machine_readable_certificate(self):
        c=allh_improved_core_path_constants(64,2**65)
        print("HYP105_AA4_B2INT_CERTIFICATE="+json.dumps({
            "all_h_improper_B2":"Qx+Qy-4N0=4N0+4(Mf+Mg)",
            "old_L4_nonproper":str(c["old_core_L4_nonproper_coefficient"]),
            "new_L4_nonproper":str(c["new_core_L4_nonproper_coefficient"]),
            "old_P3_improper":str(c["old_improper_P3_coefficient"]),
            "new_P3_improper":str(c["new_improper_P3_coefficient"]),
            "strict_improvement_fourth_and_proper_three":"16*T each",
            "all_4096_two_by_four_coordinate_grid_graphs":True,
            "original_W32_W34_source_first_and_physical_first":True,
            "no_new_asymptotic_exponent_claim":True,
            "root_Branch_A_external_referee_pending":True,
        },sort_keys=True))


if __name__=="__main__":
    unittest.main()
