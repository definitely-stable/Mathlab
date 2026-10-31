"""HYP-105 AA4-ROOTREF exact symbolic and genuine ORIGINAL-source falsifiers."""
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_full_physical_degree_tail import genuine_source
from hyp105_branch_a_root_independent_referee import (
    independent_root_threshold, check_root_error_inequality,
    original_root_falsifier, planted_original_sixcycle,
)


def _lex_pairs(V):
    a=2
    while a*(a-1)//2<V:
        a+=1
    return tuple(combinations(range(a),2))[:V]


def _independent_graph_walk_counts(mask):
    # Independent ordinary 3x3 physical graph, all 512 edge masks.
    adj={v:set() for v in range(6)}
    for u in range(3):
        for r in range(3):
            if mask & (1 << (u*3+r)):
                a,b=u,r+3
                adj[a].add(b)
                adj[b].add(a)
    def n_walks(start, length):
        layer={start:1}
        for _ in range(length):
            nextlayer={}
            for v,n in layer.items():
                for w in adj[v]:
                    nextlayer[w]=nextlayer.get(w,0)+n
            layer=nextlayer
        return layer
    tr4=sum(n_walks(v,4).get(v,0) for v in adj)
    tr6=sum(n_walks(v,6).get(v,0) for v in adj)
    walks3=sum(sum(n_walks(v,3).values()) for v in adj)
    # In 3x3 graph, each C6 uses ALL six original physical vertices.
    # For each left order (with smallest left vertex first) count right
    # permutations; divide by two for reverse orientation.
    cycles=0
    left=(0,1,2);right=(3,4,5)
    from itertools import permutations
    for l in ((0,1,2),(0,2,1)):
        for r in permutations(right):
            v=(l[0],r[0],l[1],r[1],l[2],r[2])
            if all(v[(k+1)%6] in adj[v[k]] for k in range(6)):
                cycles+=1
    # Every undirected C6 counted twice by its two orientations.
    assert cycles % 2 == 0
    m=mask.bit_count()
    Delta=max(map(len,adj.values()))
    return tr4,tr6,walks3,cycles//2,m,Delta


class IndependentBranchARootReferee(unittest.TestCase):
    def test_exact_two_pow58_tail_and_h0_new_symbolic_constants(self):
        cases=[
            (Fraction(1), Fraction(1)),
            (Fraction(1,2), Fraction(1,3)),
            (Fraction(7,4), Fraction(19,11)),
            (Fraction(1,100), Fraction(1,10000)),
            (Fraction(100), Fraction(1,10**12)),
        ]
        for C,c in cases:
            with self.subTest(C=C,c=c):
                new=independent_root_threshold(C,c)
                old=independent_root_threshold(C,c,sharpened=False)
                self.assertLessEqual(new["T"],old["T"])
                self.assertLessEqual(new["h0"],old["h0"])
                self.assertEqual(new["delta"],old["delta"])
                self.assertEqual(new["sigma2_inv"],16*65**2)
                self.assertEqual(new["sigma3_inv"],64*65**3)
                self.assertEqual(new["L6"],24+288*new["T"]**2)
                for h in (new["h0"],new["h0"]+1,new["h0"]+30):
                    result=check_root_error_inequality(C,c,h)
                    self.assertTrue(result["three_losses_certified"])
                    self.assertTrue(result["bound_BBo_at_least_s6_over8"])
        # Only mathematical illustration; actual published constants UNKNOWN.
        self.assertEqual(independent_root_threshold(1,1,sharpened=False)["h0"],826)
        self.assertEqual(independent_root_threshold(1,1,sharpened=True)["h0"],816)

    def test_fail_closed_symbolic_constants_and_invalid_h(self):
        for invalid in (0,-1,Fraction(-1,3),0.125,True,"1"):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    independent_root_threshold(invalid,1)
                with self.assertRaises(ValueError):
                    independent_root_threshold(1,invalid)
        for bad in (0,-1,1.5,False):
            with self.assertRaises(ValueError):
                check_root_error_inequality(1,1,bad)

    def test_all_512_three_by_three_bipartite_graphs_proper_c6_trace_six(self):
        positive=0
        for mask in range(512):
            tr4,tr6,walks3,C6,m,delta=_independent_graph_walk_counts(mask)
            if C6:positive+=1
            self.assertLessEqual(tr6,12*C6+6*delta*tr4,mask)
            self.assertLessEqual(tr6,24*C6+72*m*delta**2,mask)
            self.assertLessEqual(tr4**2,2*m*tr6,mask)
            self.assertGreaterEqual(36*walks3,(2*m)**3,mask)
        self.assertGreater(positive,0)
        full=_independent_graph_walk_counts(511)
        self.assertEqual(full[3],6)
        self.assertEqual(full[1],1458)

    def test_original_W32_full_correlated_maps_pencil_and_endpoint_partition(self):
        _,V,flags=genuine_source(1)
        f=_lex_pairs(V)
        for k in (0,1,7):
            g=tuple(f[(i+k)%V] for i in range(V))
            with self.subTest(k=k):
                x=original_root_falsifier(1,f,g)
                self.assertTrue(x["all_checks_passed"])
                self.assertEqual(x["original_flag_count"],len(flags))
                self.assertEqual(x["full_physical_degree_sum"],4*len(flags))
                self.assertEqual(x["full_physical_edges"],2*len(flags))
                self.assertEqual(
                    x["source_books"]["conflict_edges"],
                    x["source_books"]["Mf"]+x["source_books"]["Mg"])
                self.assertTrue(x["source_books"]["endpoint_class_partition_exact"])

    def test_genuine_W34_source_correlated_adversarial_full(self):
        _,V,flags=genuine_source(2)
        f=_lex_pairs(V)
        g=tuple(f[(i*19+17)%V] for i in range(V))
        x=original_root_falsifier(2,f,g)
        self.assertEqual(x["original_flag_count"],len(flags))
        self.assertTrue(x["all_checks_passed"])
        self.assertEqual(x["source_books"]["leftbad"],8*x["source_books"]["Mf"])
        self.assertEqual(x["source_books"]["rightbad"],8*x["source_books"]["Mg"])
        self.assertEqual(
            x["source_books"]["conflict_edges"],
            x["source_books"]["Mf"]+x["source_books"]["Mg"])

    def test_planted_positive_true_original_D6_no_vacuous_cycle_transfer(self):
        for power in (1,2):
            f,g,original_six=planted_original_sixcycle(power)
            r=original_root_falsifier(power,f,g,pinned_original_flags=original_six)
            self.assertGreaterEqual(
                r["accepted_original_D6_from_selected_graph"],1)
            self.assertEqual(r["precut_original_flags"],6)
            self.assertEqual(r["selected_original_flags"],6)
            self.assertTrue(r["all_checks_passed"])
            self.assertTrue(all(len(six)==6 for six in r["cycle_original_sixsets"]))

    def test_illegal_source_relabelings_rejected(self):
        _,V,flags=genuine_source(1)
        f=_lex_pairs(V)
        with self.assertRaises(ValueError):
            original_root_falsifier(3,f,f)
        with self.assertRaises(ValueError):
            original_root_falsifier(1,f[:-1],f)
        with self.assertRaises(ValueError):
            original_root_falsifier(1,(f[0],)*V,f)
        with self.assertRaises(ValueError):
            original_root_falsifier(1,f,f,pinned_original_flags=(0,0))
        with self.assertRaises(ValueError):
            original_root_falsifier(1,f,f,pinned_original_flags=(len(flags),))


if __name__=="__main__":
    unittest.main()
