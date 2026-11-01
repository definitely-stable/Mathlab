"""AA4-SS6GATE — exact, independent graph/source/external-hypothesis checks."""
from fractions import Fraction
from itertools import combinations
from math import comb
import unittest

from hyp105_ordinary_c6_ss6_hypothesis_spectral_bridge import (
    exact_c6_gate,independent_closed_six_walk_oracle,
    exact_balanced_chunk_parameter_gate,true_original_selected_graph_ss6_gate,\n    true_original_one_diagonal_per_flag_sector_referee,
)
from hyp105_full_physical_degree_tail import genuine_source,planted_original_k44


def complete_bipartite(a,b):
    L=tuple(range(a))
    R=tuple(range(a,a+b))
    g={i:set(R) for i in L}
    g.update({j:set(L) for j in R})
    return g,L,R


def masked_graph(a,b,mask):
    L=tuple(range(a));R=tuple(range(a,a+b))
    g={i:set() for i in L+R}
    for i in range(a):
        for j in range(b):
            if mask>>(i*b+j)&1:
                g[i].add(a+j);g[a+j].add(i)
    return g,L,R


def independently_selected_original(power,shift):
    s,V,flags=genuine_source(power)
    a=2
    while comb(a,2)<V:a+=1
    f=tuple(combinations(range(a),2))[:V]
    g=tuple(f[(19*i+shift)%V] for i in range(V))
    lc=tuple(i%2 for i in range(a))
    rc=tuple((i//2)%2 for i in range(a))
    chosen=[]
    for i,(p,l) in enumerate(flags):
        if lc[f[p][0]]==lc[f[p][1]] or rc[g[l][0]]==rc[g[l][1]]:
            continue
        if any(
            (p==flags[j][0] and set(g[l])&set(g[flags[j][1]]))
            or (l==flags[j][1] and set(f[p])&set(f[flags[j][0]]))
            for j in chosen):
            continue
        chosen.append(i)
    return f,g,chosen,lc,rc


class OrdinaryC6PublishedInputAndSelfContainedSpectral(unittest.TestCase):
    def test_every_4096_small_three_by_four_bipartite_graphs(self):
        for mask in range(4096):
            g,L,R=masked_graph(3,4,mask)
            result=exact_c6_gate(g,L,R)
            direct=independent_closed_six_walk_oracle(g)
            self.assertEqual(result["trA6"],direct["trA6_direct_walks"])
            self.assertEqual(result["ordinary_unoriented_simple_C6"],direct["C6_direct_12fold"])
            self.assertFalse(result["spectral_direct_condition_met"])

    def test_selected_all_256_four_by_four_graphs_against_walk_dfs(self):
        for mask in range(0,1<<16,257):
            g,L,R=masked_graph(4,4,mask)
            got=exact_c6_gate(g,L,R)
            naive=independent_closed_six_walk_oracle(g)
            self.assertEqual(got["trA6"],naive["trA6_direct_walks"])
            self.assertEqual(got["ordinary_unoriented_simple_C6"],naive["C6_direct_12fold"])

    def test_complete_bipartite_explicit_spectral_selfcontained_success_and_failure(self):
        for a,b in ((3,3),(4,4),(5,5),(12,12),(18,18),(20,20),(18,20),(2,30)):
            g,L,R=complete_bipartite(a,b)
            z=exact_c6_gate(g,L,R,trial_C_graph=Fraction(1,2))
            exact=6*comb(a,3)*comb(b,3) if a>=3 and b>=3 else 0
            self.assertEqual(z["ordinary_unoriented_simple_C6"],exact)
            self.assertTrue(z["published_graph_constants_NUMERICALLY_UNKNOWN"])
            self.assertGreaterEqual(z["trA6"],z["average_degree"]**6)
            if z["spectral_direct_condition_met"]:
                self.assertGreaterEqual(exact,z["spectral_direct_C6_lower"])
        self.assertTrue(exact_c6_gate(*complete_bipartite(18,18))["spectral_direct_condition_met"])
        self.assertFalse(exact_c6_gate(*complete_bipartite(12,12))["spectral_direct_condition_met"])

    def test_density_hypothesis_requires_actual_C_not_hypothetical_one(self):
        g,L,R=complete_bipartite(18,18)
        z1=exact_c6_gate(g,L,R,trial_C_graph=1)
        z2=exact_c6_gate(g,L,R,trial_C_graph=100)
        self.assertTrue(z1["trial_graph_hypothesis"]["trial_density_condition_e_ge_C_v_4_over_3"])
        self.assertFalse(z2["trial_graph_hypothesis"]["trial_density_condition_e_ge_C_v_4_over_3"])
        self.assertTrue(z1["trial_graph_hypothesis"]["NOT_verified_published_C_value"])
        for C in (0,-1,True,1.0,"1"):
            with self.assertRaises(ValueError):
                exact_c6_gate(g,L,R,trial_C_graph=C)
        g,L,R=masked_graph(3,4,0)
        self.assertEqual(exact_c6_gate(g,L,R)["ordinary_unoriented_simple_C6"],0)

    def test_all_h_exact_chunk_bridge_2040_epsilon6_and_hypothetical_constants(self):
        for s in (64,128,1024,2**20):
            for eps in (Fraction(1,8),Fraction(13,32),Fraction(1787,4096)):
                for C in (Fraction(1,3),Fraction(3,2),4):
                    base=exact_balanced_chunk_parameter_gate(eps,C,s,1)
                    T=base["symbolic_sufficient_T"]
                    z=exact_balanced_chunk_parameter_gate(eps,C,s,T)
                    self.assertTrue(z["conditional_theorem_hypothesis_certified_if_all_chunk_bounds_hold"])
                    self.assertEqual(
                        z["symbolic_sufficient_T"],
                        (2**40)*Fraction(C)**3/Fraction(eps)**6)
                    self.assertEqual(
                        z["conditional_C6_floor_as_coefficient_of_s6_for_c_graph_equal_1"],
                        Fraction(eps)**12/Fraction(2**72))
                    half=exact_balanced_chunk_parameter_gate(eps,C,s,T/2)
                    self.assertFalse(half["conditional_theorem_hypothesis_certified_if_all_chunk_bounds_hold"])
                    self.assertTrue(z["published_C_graph_NOT_assigned_a_real_numeric_value"])

    def test_true_original_W34_protected_matching_exact_96_D6_and_bipartition(self):
        f,g,ids=planted_original_k44()
        lc=tuple(0 if i<4 else 1 if i<8 else 0 for i in range(14))
        report=true_original_selected_graph_ss6_gate(2,f,g,ids,lc,lc)
        self.assertEqual(report["actual_ORIGINAL_selected_IDs"],16)
        self.assertEqual(report["actual_original_paired_diagonal_edges"],32)
        self.assertEqual(report["ordinary_graph_audit"]["ordinary_unoriented_simple_C6"],96)
        self.assertEqual(report["injected_distinct_original_D6_sixsets"],96)
        self.assertTrue(report["source_sixID_flag_injection"])

    def test_true_original_W32_W34_greedy_cuts_correlated_maps(self):
        for power in (1,2):
            for shift in (0,1,3):
                with self.subTest(h=power,shift=shift):
                    f,g,ids,lc,rc=independently_selected_original(power,shift)
                    self.assertTrue(ids,"must exercise at least one true selected original flag")
                    z=true_original_selected_graph_ss6_gate(power,f,g,ids,lc,rc)
                    self.assertEqual(z["actual_original_paired_diagonal_edges"],2*len(ids))
                    self.assertEqual(z["injected_distinct_original_D6_sixsets"],
                                     z["ordinary_graph_audit"]["ordinary_unoriented_simple_C6"])
                    self.assertTrue(z["ordinary_graph_audit"]["external_statement_is_ordinary_SIMPLE_graphs_not_homomorphisms"])

    def test_true_original_W34_two_one_diagonal_unpaired_sectors_full_D6_image(self):
        f,g,ids=planted_original_k44()
        lc=tuple(0 if i<4 else 1 if i<8 else 0 for i in range(14))
        z=true_original_one_diagonal_per_flag_sector_referee(2,f,g,ids,lc,lc)
        self.assertEqual(z["both_paired_diagonals_in_parent_G"],32)
        self.assertTrue(z["each_UNPAIRED_sector_exactly_one_original_flag_diagonal"])
        self.assertEqual(z["sum_sector_C6_equals_parent_C6"],96)
        self.assertEqual(z["parent_original_D6_census"],96)
        self.assertTrue(z["all_cycles_still_distinct_ORIGINAL_six_ID_D6"])
        self.assertTrue(z["applicable_to_any_actual_F_subset_of_G"])
        for sector in z["unpaired_sectors"]:
            self.assertEqual(sector["actual_ordinary_physical_edges"],16)
            self.assertEqual(sector["actual_ORIGINAL_ids_present_once"],16)
            self.assertEqual(sector["ordinary_simple_unoriented_C6"],
                             sector["distinct_ORIGINAL_D6_flag_sixsets"])
        self.assertGreater(sum(x["ordinary_simple_unoriented_C6"] for x
                               in z["unpaired_sectors"]),0)

    def test_true_original_W32_W34_one_diagonal_selected_sectors(self):
        for h in (1,2):
            for shift in (0,3):
                with self.subTest(power=h,shift=shift):
                    f,g,ids,lc,rc=independently_selected_original(h,shift)
                    z=true_original_one_diagonal_per_flag_sector_referee(
                        h,f,g,ids,lc,rc)
                    self.assertEqual(z["both_paired_diagonals_in_parent_G"],
                                     2*len(ids))
                    self.assertTrue(z["all_cycles_still_distinct_ORIGINAL_six_ID_D6"])
                    self.assertEqual(
                        z["sum_sector_C6_equals_parent_C6"],
                        z["parent_original_D6_census"])
                    for sector in z["unpaired_sectors"]:
                        self.assertEqual(sector["actual_ORIGINAL_ids_present_once"],len(ids))

    def test_fail_closed_nonbipartite_non_simple_and_source_conflicts(self):
        for g,L,R in (
            ({0:{0}},(0,),()),
            ({0:{1},1:set()},(0,),(1,)),
            ({0:{1,2},1:{0,2},2:{0,1}},(0,1),(2,)),
            ({0:set(),1:set()},(0,),(0,1)),
        ):
            with self.assertRaises(ValueError):
                exact_c6_gate(g,L,R)
        for val in (0,-1,True,1.0,"1"):
            with self.assertRaises(ValueError):
                exact_balanced_chunk_parameter_gate(val,1,64,1)
        with self.assertRaises(ValueError):
            exact_balanced_chunk_parameter_gate(Fraction(1,8),1,63,1)
        f,g,ids=planted_original_k44()
        lc=tuple(0 if i<4 else 1 if i<8 else 0 for i in range(14))
        with self.assertRaises(ValueError):
            true_original_selected_graph_ss6_gate(2,f,g,ids+(ids[0],),lc,lc)
        with self.assertRaises(ValueError):
            true_original_selected_graph_ss6_gate(2,f[:-1],g,ids,lc,lc)
        with self.assertRaises(ValueError):
            true_original_selected_graph_ss6_gate(2,f,g,ids,(0,)*14,lc)
        with self.assertRaises(ValueError):
            true_original_selected_graph_ss6_gate(2,f,g,ids,lc,lc[:-1])


if __name__=="__main__":
    unittest.main()
