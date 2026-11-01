"""AA4-D6INV independent ORIGINAL six-ID inverse, all f/g permutations and GQ."""
from itertools import combinations,permutations
from math import comb
import unittest

from hyp105_full_physical_degree_tail import genuine_source,planted_original_k44
from hyp105_d6_canonical_source_six_id_inverse_referee import (
    source_sixset_canonical_inverse,
    physical_original_edge_graph,
    independent_original_six_id_inverse_referee,
    true_original_gq_six_id_inverse_referee,
)


def labels(power,reverse=False):
    _,V,_=genuine_source(power)
    a=2
    while comb(a,2)<V:a+=1
    base=tuple(combinations(range(a),2))[:V]
    return base,tuple(reversed(base)) if reverse else base


class OriginalSixIDCanonicalInverse(unittest.TestCase):
    def test_all_720_named_original_six_edge_cycle_permutations_no_fake_source(self):
        # Explicit local abstract original factor matching source, NOT a
        # synthetic GQ. These are all 6! possible right C6 edge-name
        # permutations over the FIXED actual six original source IDs.
        # Exactly 12 dihedral permutations have same named adjacency.
        flags=tuple((i,i) for i in range(6))
        c6=((0,1),(1,2),(2,3),(3,4),(4,5),(0,5))
        successful=0
        for permutation in permutations(range(6)):
            g=tuple(c6[i] for i in permutation)
            inverse=source_sixset_canonical_inverse(flags,c6,g,range(6))
            report=independent_original_six_id_inverse_referee(flags,c6,g)
            if inverse is not None:
                successful+=1
                self.assertEqual(report["rainbow_ordinary_C6"],1)
                self.assertEqual(report["distinct_TRUE_original_D6_sixsets"],1)
                self.assertEqual(
                    report["physical_cycle_to_original_sixset"],
                    (((0,1,2,3,4,5),inverse),))
            else:
                self.assertEqual(report["rainbow_ordinary_C6"],0)
            self.assertEqual(report["rainbow_ordinary_C6"]+
                             report["nonrainbow_ordinary_C6"],
                             report["ordinary_simple_unoriented_C6"])
        self.assertEqual(successful,12)

    def test_true_original_W32_full_lex_reverse_all_sixsets_roundtrip(self):
        for reverse,C6,D6 in ((False,730,15),(True,485,3)):
            with self.subTest(reverse=reverse):
                f,g=labels(1,reverse)
                report=true_original_gq_six_id_inverse_referee(1,f,g)
                self.assertEqual(report["ordinary_simple_unoriented_C6"],C6)
                self.assertEqual(report["rainbow_ordinary_C6"],D6)
                self.assertEqual(report["nonrainbow_ordinary_C6"],C6-D6)
                self.assertEqual(report["distinct_TRUE_original_D6_sixsets"],D6)
                for ids,cycle in report["physical_cycle_to_original_sixset"]:
                    self.assertEqual(len(ids),6)
                    self.assertEqual(len({v[0] for v in cycle}),6)
                    self.assertEqual(len({v[1] for v in cycle}),6)
                    self.assertEqual(
                        source_sixset_canonical_inverse(
                            genuine_source(1)[2],f,g,ids),cycle)

    def test_true_original_W34_protected_K44_both_diagonals_and_parity_sectors(self):
        f,g,ids=planted_original_k44()
        a=14
        colors=tuple(0 if i<4 else 1 if i<8 else 0 for i in range(a))
        full=true_original_gq_six_id_inverse_referee(
            2,f,g,ids,left_colors=colors,right_colors=colors)
        self.assertEqual(full["ordinary_simple_unoriented_C6"],96)
        self.assertEqual(full["rainbow_ordinary_C6"],96)
        self.assertTrue(full["every_ordinary_C6_source_D6_if_coherent"])
        union={}
        for parity in (0,1):
            report=true_original_gq_six_id_inverse_referee(
                2,f,g,ids,left_colors=colors,right_colors=colors,sector=parity)
            self.assertEqual(report["actual_physical_undirected_edges"],16)
            self.assertTrue(report["every_ordinary_C6_source_D6_if_coherent"])
            for source,cycle in report["physical_cycle_to_original_sixset"]:
                self.assertNotIn(source,union)
                union[source]=cycle
        self.assertEqual(len(union),96)
        self.assertEqual(
            set(union),{ids for ids,cycle in full["physical_cycle_to_original_sixset"]})

    def test_actual_W34_unpaired_subgraph_deleting_a_real_diagonal_retains_positive_C6(self):
        f,g,ids=planted_original_k44()
        colors=tuple(0 if i<4 else 1 if i<8 else 0 for i in range(14))
        _,owners=physical_original_edge_graph(
            genuine_source(2)[2],f,g,ids,sector=0,
            left_colors=colors,right_colors=colors)
        self.assertEqual(len(owners),16)
        one=next(iter(owners))
        real_remaining=tuple(e for e in owners if e!=one)
        report=true_original_gq_six_id_inverse_referee(
            2,f,g,ids,left_colors=colors,right_colors=colors,
            sector=0,edge_filter=real_remaining)
        self.assertEqual(report["actual_physical_undirected_edges"],15)
        self.assertEqual(report["ordinary_simple_unoriented_C6"],60)
        self.assertEqual(report["nonrainbow_ordinary_C6"],0)
        self.assertEqual(report["distinct_TRUE_original_D6_sixsets"],60)

    def test_true_original_W32_W34_independent_source_greedy_coherent_two_cuts(self):
        for power in (1,2):
            s,V,flags=genuine_source(power)
            for shift in (0,1,3):
                with self.subTest(power=power,shift=shift):
                    f,base=labels(power)
                    g=tuple(base[(19*i+shift)%V] for i in range(V))
                    a=max(max(x for pair in f+g for x in pair)+1,2)
                    left=tuple(i%2 for i in range(a))
                    right=tuple((i//2)%2 for i in range(a))
                    chosen=[]
                    for i,(p,l) in enumerate(flags):
                        if (left[f[p][0]]==left[f[p][1]] or
                            right[g[l][0]]==right[g[l][1]]):
                            continue
                        if any(
                            (p==flags[j][0] and set(g[l])&set(g[flags[j][1]])) or
                            (l==flags[j][1] and set(f[p])&set(f[flags[j][0]]))
                            for j in chosen):
                            continue
                        chosen.append(i)
                    self.assertGreater(len(chosen),0)
                    report=true_original_gq_six_id_inverse_referee(
                        power,f,g,chosen,left_colors=left,right_colors=right)
                    self.assertEqual(report["actual_physical_undirected_edges"],
                                     2*len(chosen))
                    self.assertEqual(report["nonrainbow_ordinary_C6"],0)
                    self.assertEqual(report["rainbow_ordinary_C6"],
                                     report["distinct_TRUE_original_D6_sixsets"])

    def test_source_inverse_rejects_wrong_original_multiplicities_and_missing_edges(self):
        flags=tuple((i,i) for i in range(6))
        c6=((0,1),(1,2),(2,3),(3,4),(4,5),(0,5))
        self.assertIsNotNone(source_sixset_canonical_inverse(flags,c6,c6,range(6)))
        self.assertIsNone(source_sixset_canonical_inverse(
            ((0,0),(0,1),(2,2),(3,3),(4,4),(5,5)),c6,c6,range(6)))
        self.assertIsNone(source_sixset_canonical_inverse(
            flags,c6,((0,1),(1,2),(2,3),(3,4),(0,4),(0,5)),range(6)))
        for bad_ids in ((0,0,1,2,3,4),(-1,1,2,3,4,5),(0,1,2,3,4,6),(0,1)):
            with self.assertRaises(ValueError):
                source_sixset_canonical_inverse(flags,c6,c6,bad_ids)
        with self.assertRaises(ValueError):
            source_sixset_canonical_inverse(flags,(c6[0],)*6,c6,range(6))
        with self.assertRaises(ValueError):
            source_sixset_canonical_inverse(flags,c6,c6[:-1],range(6))

    def test_real_original_selected_flags_must_not_claim_coherence_without_conflict_gate(self):
        f,g=labels(1)
        flags=genuine_source(1)[2]
        colors=tuple(i%2 for i in range(6))
        # Full source is NOT conflict independent; if both cuts happen
        # to be satisfied on some subset, raw selected graph may contain
        # coordinate cherries. The referee must fail instead of claiming
        # that every ordinary C6 is original D6.
        ids=tuple(i for i,(p,l) in enumerate(flags)
                  if colors[f[p][0]]!=colors[f[p][1]] and
                     colors[g[l][0]]!=colors[g[l][1]])
        if ids:
            with self.assertRaises(ValueError):
                true_original_gq_six_id_inverse_referee(
                    1,f,g,ids,left_colors=colors,right_colors=colors)


if __name__=="__main__":
    unittest.main()
