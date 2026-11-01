"""AA4-WALKMOBIUS: independent exact six-walk Möbius source referee."""
from itertools import combinations
from math import comb
import unittest

from hyp105_bipartite_sixwalk_mobius_moment_referee import (
    exact_bipartite_sixwalk_mobius,
    independent_direct_rooted_closed_walks,
    source_coherent_actual_physical_bipartite_rows,
)
from hyp105_independent_codegree_c6_source_referee import (
    bipartite_c6_direct_six_vertex_oracle,
    bipartite_c6_codegree,
)
from hyp105_full_physical_degree_tail import genuine_source,planted_original_k44


def real_maps(power,step,shift=0):
    _,V,_=genuine_source(power)
    a=2
    while comb(a,2)<V:a+=1
    labels=tuple(combinations(range(a),2))[:V]
    return labels,tuple(labels[(step*i+shift)%V] for i in range(V))


def greedy_actual_source_cut(power,f,g,left,right):
    _,_,flags=genuine_source(power)
    kept=[]
    for i,(p,l) in enumerate(flags):
        if (left[f[p][0]]==left[f[p][1]] or
            right[g[l][0]]==right[g[l][1]]):
            continue
        if any((p==flags[j][0] and set(g[l])&set(g[flags[j][1]])) or
               (l==flags[j][1] and set(f[p])&set(f[flags[j][0]]))
               for j in kept):
            continue
        kept.append(i)
    return tuple(kept)


class ExactBipartiteOriginalSixWalkMobius(unittest.TestCase):
    def assert_independent(self,rows,nright,dfs=False):
        a=exact_bipartite_sixwalk_mobius(rows,nright)
        r=bipartite_c6_direct_six_vertex_oracle(rows,nright)
        b=bipartite_c6_codegree(rows,nright)["ordinary_unoriented_C6"]
        self.assertEqual(a["actual_unoriented_simple_C6"],r)
        self.assertEqual(a["actual_unoriented_simple_C6"],b)
        self.assertEqual(a["exact_mobius_injective_sixcycle_numerator"],12*r)
        self.assertEqual(a["trA6_by_two_independent_bipartite_parities"],
                         12*r+a["noninjective_rooted_sixwalks"])
        self.assertLessEqual(a["noninjective_rooted_sixwalks"],
                             a["backtrack_6Delta_trA4_bound"])
        if dfs:
            c=independent_direct_rooted_closed_walks(rows,nright)
            self.assertEqual(a["trA4_by_two_independent_bipartite_parities"],
                             c["trA4_direct_DFS"])
            self.assertEqual(a["trA6_by_two_independent_bipartite_parities"],
                             c["trA6_direct_DFS"])
        return a

    def test_complete_bipartite_Kuv_closed_walks_and_sixcycle_normalization(self):
        for nleft in range(7):
            for nright in range(7):
                rows=tuple(((1<<nright)-1) for _ in range(nleft))
                got=self.assert_independent(rows,nright)
                m=nleft*nright
                self.assertEqual(got["physical_edges"],m)
                self.assertEqual(got["actual_unoriented_simple_C6"],
                                 6*comb(nleft,3)*comb(nright,3) if min(nleft,nright)>=3 else 0)
                self.assertEqual(got["trA6_by_two_independent_bipartite_parities"],
                                 2*m**3)
                self.assertEqual(got["trA4_by_two_independent_bipartite_parities"],
                                 2*m*m)

    def test_named_C6_K33_and_adversarial_graphs(self):
        C6=(0b101,0b011,0b110)
        z=self.assert_independent(C6,3,True)
        self.assertEqual(z["actual_unoriented_simple_C6"],1)
        self.assertEqual(z["trA6_by_two_independent_bipartite_parities"],132)
        self.assertEqual(z["trA4_by_two_independent_bipartite_parities"],36)
        families=[
            ((0b1111111,),7),
            ((0b111111111,0b111111111),9),
            ((0b111,0b111,0b111,0b1000000,0b1000000),7),
            ((0b0101,0b1010,0b0011,0b1100),4),
            ((0b1111,0b1111,0b0001,0b0001,0),5),
            ((),8),
            ((0,0,0),0),
        ]
        for rows,nright in families:
            self.assert_independent(rows,nright,True)

    def test_all_4096_labeled_3_by_4_bipartite_graphs_both_independent_C6_oracles(self):
        for mask in range(1<<12):
            rows=tuple((mask>>(4*i))&15 for i in range(3))
            self.assert_independent(rows,4,dfs=(mask%128==0))

    def test_all_65536_labeled_4_by_4_graphs_mobius_vs_independent_codegree(self):
        for mask in range(1<<16):
            rows=tuple((mask>>(4*i))&15 for i in range(4))
            got=exact_bipartite_sixwalk_mobius(rows,4)
            codeg=bipartite_c6_codegree(rows,4)["ordinary_unoriented_C6"]
            self.assertEqual(got["actual_unoriented_simple_C6"],codeg)
            if mask%257==0:
                self.assert_independent(rows,4,dfs=mask%4096==0)

    def test_known_72_m_delta_squared_moment_certificate_no_unpublished_theorem(self):
        for m in range(1<<12):
            rows=tuple((m>>(4*i))&15 for i in range(3))
            r=exact_bipartite_sixwalk_mobius(rows,4)
            self.assertLessEqual(r["trA6_by_two_independent_bipartite_parities"],
                 24*r["actual_unoriented_simple_C6"]
                 +72*r["physical_edges"]*r["actual_max_degree"]**2)
            self.assertLessEqual(r["trA4_by_two_independent_bipartite_parities"]**2,
                 2*r["physical_edges"]*r["trA6_by_two_independent_bipartite_parities"])
            self.assertTrue(r["no_unproven_graph_C6_supersaturation_claim"])

    def test_true_original_W32_coherent_source_cut_graphs(self):
        for step,shift in ((1,0),(7,1),(11,4)):
            f,g=real_maps(1,step,shift)
            colors=tuple(j%2 for j in range(6))
            other=tuple((j//2)%2 for j in range(6))
            ids=greedy_actual_source_cut(1,f,g,colors,other)
            src=source_coherent_actual_physical_bipartite_rows(
                1,f,g,ids,colors,other)
            self.assertEqual(src["actual_physical_edges"],2*len(ids))
            out=self.assert_independent(src["rows"],src["nright"],True)
            self.assertEqual(out["physical_edges"],src["actual_physical_edges"])

    def test_true_original_W34_correlated_sparse_source_cut_and_protected_K44(self):
        _,V,flags=genuine_source(2)
        f,g=real_maps(2,19,3)
        a=14
        left=tuple(j%2 for j in range(a))
        right=tuple((j//2)%2 for j in range(a))
        ids=greedy_actual_source_cut(2,f,g,left,right)
        src=source_coherent_actual_physical_bipartite_rows(
            2,f,g,ids,left,right)
        self.assertEqual(src["actual_physical_edges"],2*len(ids))
        self.assert_independent(src["rows"],src["nright"])
        f,g,ids=planted_original_k44()
        colors=tuple(0 if j<4 else 1 if j<8 else 0 for j in range(a))
        protected=source_coherent_actual_physical_bipartite_rows(
            2,f,g,ids,colors,colors)
        self.assertEqual(protected["actual_physical_edges"],32)
        out=self.assert_independent(protected["rows"],protected["nright"],True)
        self.assertEqual(out["actual_unoriented_simple_C6"],96)
        self.assertEqual(out["trA6_by_two_independent_bipartite_parities"],2*4**6*2)

    def test_invalid_graph_bitsets_and_original_source_fail_closed(self):
        for rows,nright in (([0b10000],4),([True],4),
                            ([-1],5),((),-1),((),True),([0],1.0),
                            ("bad",2)):
            with self.assertRaises(ValueError):
                exact_bipartite_sixwalk_mobius(rows,nright)
        f,g=real_maps(1,1)
        left=tuple(j%2 for j in range(6))
        right=tuple((j//2)%2 for j in range(6))
        _,_,flags=genuine_source(1)
        for power,ff,gg,ids,lc,rc in (
            (0,f,g,(),left,right),
            (3,f,g,(),left,right),
            (1,f[:-1],g,(),left,right),
            (1,(f[0],)*15,g,(),left,right),
            (1,f,g,(0,0),left,right),
            (1,f,g,(True,),left,right),
            (1,f,g,(len(flags),),left,right),
            (1,f,g,(),left[:-1],right),
            (1,f,g,(0,),left,(0,)*6),
        ):
            with self.assertRaises(ValueError):
                source_coherent_actual_physical_bipartite_rows(
                    power,ff,gg,ids,lc,rc)
        # No fake source cherry-free certificate on full original W32.
        with self.assertRaises(ValueError):
            source_coherent_actual_physical_bipartite_rows(
                1,f,g,range(45),left,right)


if __name__=="__main__":
    unittest.main()
