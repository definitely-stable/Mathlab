"""Independent exact ordinary C6/source D6 census: genuinely distinct oracles."""
from itertools import combinations
from math import comb
import unittest

from hyp105_independent_codegree_c6_source_referee import (
    bipartite_c6_codegree, bipartite_c6_direct_six_vertex_oracle,
    exact_codegree_clique_certificate, selected_original_coherent_provenance,
    original_independently_greedy_cut_ids,
)
from hyp105_full_physical_degree_tail import genuine_source,planted_original_k44


def rows_from_mask(left,right,mask):
    return tuple(sum(1<<y for y in range(right) if (mask>>(x*right+y))&1)
                 for x in range(left))


def dense_rows(left,right):
    return (2**right-1,)*left


def source_labels(power):
    _,V,_=genuine_source(power)
    a=2
    while comb(a,2)<V:a+=1
    pairs=tuple(combinations(range(a),2))
    f=pairs[:V]
    g=tuple(reversed(pairs[:V]))
    lc=tuple(int(i>=a//2) for i in range(a))
    rc=tuple(int(i>=a//2) for i in range(a))
    return f,g,lc,rc


class IndependentSourceCodegreeC6(unittest.TestCase):
    def test_all_4096_labeled_three_by_four_bipartite_graphs(self):
        for mask in range(1<<12):
            rows=rows_from_mask(3,4,mask)
            codegree=bipartite_c6_codegree(rows,4)["ordinary_unoriented_C6"]
            direct=bipartite_c6_direct_six_vertex_oracle(rows,4)
            self.assertEqual(codegree,direct)

    def test_all_65536_labeled_four_by_four_graphs(self):
        # No graph theorem or historical cycle DFS is called: two independent
        # all-injective 6-vertex vs common-neighbor IE definitions.
        for mask in range(1<<16):
            rows=rows_from_mask(4,4,mask)
            codegree=bipartite_c6_codegree(rows,4)["ordinary_unoriented_C6"]
            direct=bipartite_c6_direct_six_vertex_oracle(rows,4)
            self.assertEqual(codegree,direct)

    def test_complete_bipartite_exact_cycle_normalization(self):
        for left,right in ((1,5),(2,5),(3,3),(3,4),(4,4),(4,5),(5,5)):
            rows=dense_rows(left,right)
            expected=6*comb(left,3)*comb(right,3) if left>=3 and right>=3 else 0
            self.assertEqual(
                bipartite_c6_codegree(rows,right)["ordinary_unoriented_C6"],expected)
            self.assertEqual(bipartite_c6_direct_six_vertex_oracle(rows,right),expected)
        self.assertEqual(bipartite_c6_codegree((0,0,0),4)["ordinary_unoriented_C6"],0)

    def test_universal_local_codegree_clique_lower_bound_and_sharp_Ktt(self):
        for t,k in ((3,3),(3,4),(4,3),(4,4),(5,5),(6,6)):
            rows=dense_rows(t,k)
            report=exact_codegree_clique_certificate(rows,k,range(t))
            exact=bipartite_c6_codegree(rows,k)["ordinary_unoriented_C6"]
            self.assertEqual(report["min_codegree"],k)
            self.assertEqual(report["guaranteed_C6"],comb(t,3)*k*(k-1)*(k-2))
            self.assertLessEqual(report["guaranteed_C6"],exact)
            if t==3:
                self.assertEqual(report["guaranteed_C6"],exact)
        # Zero certificate does NOT assert no C6 when pair min-codegree<3.
        rows=(3,3,3)
        self.assertEqual(
            exact_codegree_clique_certificate(rows,2,(0,1,2))["guaranteed_C6"],0)
        self.assertEqual(
            bipartite_c6_codegree(rows,2)["ordinary_unoriented_C6"],0)

    def test_real_original_W34_planted_protected_k44_all_96_D6(self):
        f,g,ids=planted_original_k44()
        a=14
        colors=tuple(0 if i<4 else 1 if i<8 else 0 for i in range(a))
        out=selected_original_coherent_provenance(2,f,g,ids,colors,colors)
        self.assertEqual(out["original_selected_flags"],16)
        self.assertEqual(out["paired_physical_edges"],32)
        self.assertEqual(out["exact_common_neighbor_C6"],96)
        self.assertEqual(out["verified_distinct_original_D6"],96)
        self.assertEqual(out["independent_direct_six_vertex_check"],96)
        self.assertEqual(len(out["source_flag_sets"]),96)

    def test_real_original_W34_coordinate_relabeling_invariance(self):
        f,g,ids=planted_original_k44()
        colors=tuple(0 if i<4 else 1 if i<8 else 0 for i in range(14))
        reverse=lambda pair:tuple(sorted((13-pair[0],13-pair[1])))
        ff=tuple(reverse(pair) for pair in f)
        gg=tuple(reverse(pair) for pair in g)
        color2=tuple(colors[13-i] for i in range(14))
        before=selected_original_coherent_provenance(2,f,g,ids,colors,colors)
        after=selected_original_coherent_provenance(2,ff,gg,ids,color2,color2)
        self.assertEqual(before["source_flag_sets"],after["source_flag_sets"])
        self.assertEqual(after["exact_common_neighbor_C6"],96)

    def test_real_original_W32_W34_adversarial_correlated_greedy_subsets(self):
        for h in (1,2):
            f,g,lc,rc=source_labels(h)
            ids=original_independently_greedy_cut_ids(h,f,g,lc,rc)
            report=selected_original_coherent_provenance(h,f,g,ids,lc,rc)
            self.assertEqual(report["original_selected_flags"],len(ids))
            self.assertEqual(report["paired_physical_edges"],2*len(ids))
            self.assertEqual(report["exact_common_neighbor_C6"],
                             report["verified_distinct_original_D6"])
            self.assertEqual(report["exact_common_neighbor_C6"],
                             report["independent_direct_six_vertex_check"])

    def test_noncoherent_source_flags_and_injections_fail_closed(self):
        f,g,ids=planted_original_k44()
        colors=tuple(0 if i<4 else 1 if i<8 else 0 for i in range(14))
        with self.assertRaises(ValueError):
            selected_original_coherent_provenance(2,f,g,tuple(ids)+(ids[0],),colors,colors)
        with self.assertRaises(ValueError):
            selected_original_coherent_provenance(2,f[:-1],g,ids,colors,colors)
        with self.assertRaises(ValueError):
            selected_original_coherent_provenance(2,(f[0],)*len(f),g,ids,colors,colors)
        with self.assertRaises(ValueError):
            selected_original_coherent_provenance(2,f,g,ids,(0,)*14,colors)
        with self.assertRaises(ValueError):
            selected_original_coherent_provenance(2,f,g,ids,colors,colors[:-1])
        with self.assertRaises(ValueError):
            selected_original_coherent_provenance(2,f,g,(-1,),colors,colors)

    def test_invalid_graph_and_codegree_subset_fail_closed(self):
        for bits,cols in (((-1,0,0),3),((8,0,0),3),((1.0,0,0),3),
                           ((1,0,0),-1),((1,0,0),True)):
            with self.assertRaises(ValueError):
                bipartite_c6_codegree(bits,cols)
            with self.assertRaises(ValueError):
                bipartite_c6_direct_six_vertex_oracle(bits,cols)
        for bad in ((1,1,2),(-1,1,2),(0,1,3),(0,1,2.0)):
            with self.assertRaises(ValueError):
                exact_codegree_clique_certificate((7,7,7),3,bad)


if __name__=="__main__":
    unittest.main()
