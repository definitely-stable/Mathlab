"""Exact D2 independent finite endpoint tensor, FALSE universality guards."""
import unittest

from hyp105_issue230_projection import ProjectionClosure,fixture
from hyp105_issue230_anchor_blocking import anchor_ledger
from hyp105_issue230_endpoint_mixedbook_d2 import (
    original_pencil_bad_pairs,_chord_ledger,_typed_degrees,
    _independent_endpoint_threewalks,mixedbook_gate,report,
)


class Issue230EndpointMixedbookD2Tests(unittest.TestCase):
    def test_true_original_GQ_pencil_sets_versus_unique_projection(self):
        for s,scheme in ((2,"S68"),(2,"lex"),(4,"random"),(8,"random")):
            with self.subTest(s=s,scheme=scheme):
                core=ProjectionClosure(fixture({2:1,4:2,8:3}[s],scheme))
                L,R=original_pencil_bad_pairs(core)
                self.assertEqual((L|R)<set(core.projection),True)
                self.assertEqual(len(_typed_degrees(core)),core.a**2)
                led=_chord_ledger(core)
                self.assertEqual(len(led["chords"]),2*len(L|R))
                self.assertEqual(sum(led["Bdeg"]),4*len(L|R))
                self.assertEqual(led["W"],sum(led["pair_energy"].values()))
                self.assertTrue(all(y not in set(v for v,_ in core.adj[x])
                                    for x,y in led["chords"]))

    def test_S68_full_exact_energy_and_two_independent_endpoint_oracles(self):
        state=fixture(1,"S68")
        d2=mixedbook_gate(state,verify_proper=True)
        d1=anchor_ledger(state)
        self.assertEqual(d2["exact_proper_original_endpoint_bad_paths"],544)
        self.assertEqual(d2["exact_proper_original_endpoint_bad_paths"],
                         d1["endpoint_bad_pair_weight"])
        self.assertEqual(d2["bad_original_union_pairs"],166)
        self.assertEqual(d2["actual_bad_physical_antipodal_chords"],332)
        self.assertGreaterEqual(d2["all_oriented_threewalks_bad_endpoint_chords"],544)
        self.assertEqual(d2["independent_sparse_A2_A3_chord_trace"],1644)
        self.assertEqual(d2["independent_sparse_A2_A3_chord_trace"],
                         d2["all_oriented_threewalks_bad_endpoint_chords"])
        self.assertEqual(d2["all_h_weighted_energy_bound_proved"],False)
        self.assertEqual(d2["all_h_internal_only_upper_proved"],False)
        self.assertEqual(d2["issue230_Branch_A"],"OPEN")

    def test_W34_random_complete_but_no_false_theorem(self):
        state=fixture(2,"random")
        z=mixedbook_gate(state,verify_proper=True)
        self.assertEqual(z["bad_original_union_pairs"],3203)
        self.assertEqual(z["actual_bad_physical_antipodal_chords"],6406)
        self.assertEqual(z["exact_proper_original_endpoint_bad_paths"],30194)
        self.assertGreaterEqual(z["all_oriented_threewalks_bad_endpoint_chords"],30194)
        self.assertEqual(z["independent_sparse_A2_A3_chord_trace"],44552)
        self.assertEqual(z["independent_sparse_A2_A3_chord_trace"],
                         z["all_oriented_threewalks_bad_endpoint_chords"])
        self.assertEqual(z["issue230_Branch_B"],"OPEN")

    def test_complete_real_W38_sparse_A3_endpoint_chord_tensor(self):
        x=mixedbook_gate(fixture(3,"random"),verify_proper=False)
        self.assertEqual(x["bad_original_union_pairs"],70174)
        self.assertEqual(x["actual_bad_physical_antipodal_chords"],140348)
        self.assertEqual(x["degree_energy_W"],4927736)
        self.assertTrue(x["independent_sparse_square_trace_computed"])
        self.assertEqual(x["independent_sparse_A2_A3_chord_trace"],1195458)
        self.assertEqual(x["independent_sparse_A2_A3_chord_trace"]-1019228,
                         176230)  # independently sealed D1 full proper endpoint floor
        self.assertFalse(x["all_h_endpoint_mass_o_s6_proved"])

    def test_lex_and_reverse_endpoint_original_weight(self):
        for scheme,expect in (("lex",786),("reverse",676),("S72",600)):
            with self.subTest(scheme=scheme):
                x=mixedbook_gate(fixture(1,scheme),verify_proper=True)
                self.assertEqual(x["exact_proper_original_endpoint_bad_paths"],expect)
                self.assertEqual(x["original_qr_tensor_energy_W"],
                                 x["degree_energy_W"])

    def test_retained_edge_deletion_preserves_tensor_and_mixedbook_bound(self):
        state=fixture(1,"lex")
        core=ProjectionClosure(state)
        adj=[set(v for v,_ in row) for row in core.adj]
        u=next(i for i,row in enumerate(adj) if row)
        v=next(iter(adj[u]))
        adj[u].remove(v)
        adj[v].remove(u)
        original=mixedbook_gate(state,verify_proper=True)
        retained=mixedbook_gate(state,verify_proper=True,
                                retained_adjacency=adj)
        self.assertLessEqual(retained["degree_energy_W"],original["degree_energy_W"])
        self.assertLessEqual(retained["exact_proper_original_endpoint_bad_paths"],
                             original["exact_proper_original_endpoint_bad_paths"])
        self.assertEqual(retained["bad_original_union_pairs"],
                         original["bad_original_union_pairs"])

    def test_empty_retained_graph_exact_zero_without_inventing_paths(self):
        state=fixture(1,"S68")
        core=ProjectionClosure(state)
        zero=[set() for _ in range(core.a**2)]
        z=mixedbook_gate(state,verify_proper=True,retained_adjacency=zero)
        self.assertEqual(z["degree_energy_W"],0)
        self.assertEqual(z["physical_coordinate_neighbor_block_cap"],0)
        self.assertEqual(z["exact_proper_original_endpoint_bad_paths"],0)
        self.assertEqual(z["all_oriented_threewalks_bad_endpoint_chords"],0)
        self.assertFalse(z["mixedbook_certificate_nontrivial"])

    def test_invalid_new_physical_edge_and_asymmetric_graph_fail_closed(self):
        state=fixture(1,"lex")
        core=ProjectionClosure(state)
        adj=[set(v for v,_ in row) for row in core.adj]
        a,b=next(iter(core.projection))
        q,r=a,b
        u,v=core.f[q];x,y=core.g[r]
        adj[u*core.a+x].add(v*core.a+y)
        with self.assertRaises(ValueError):
            mixedbook_gate(state,retained_adjacency=adj)
        adj=[set(v for v,_ in row) for row in core.adj]
        a=next(i for i,row in enumerate(adj) if row)
        b=next(iter(adj[a]))
        adj[a].remove(b)
        with self.assertRaises(ValueError):
            mixedbook_gate(state,retained_adjacency=adj)

    def test_D2_report_compares_independent_full_D1_sixteen_atom(self):
        r=report()
        self.assertEqual(r["slice"],"ISSUE230-PROJECTION-ENDPOINT-MIXEDBOOK-D2")
        self.assertEqual(len(r["records"]),7)
        self.assertFalse(r["all_h_necessary_endpoint_energy_bound_proved"])
        for x in r["records"]:
            self.assertEqual(x["actual_bad_physical_antipodal_chords"],
                             2*x["bad_original_union_pairs"])
            self.assertEqual(x["degree_energy_W"],
                             x["original_qr_tensor_energy_W"])
            self.assertTrue(x["independent_sparse_square_trace_computed"])
            self.assertFalse(x["all_h_endpoint_mass_o_s6_proved"])
            if x["s"]<=4:
                self.assertGreaterEqual(
                    x["all_oriented_threewalks_bad_endpoint_chords"],
                    x["exact_proper_original_endpoint_bad_paths"])


if __name__=="__main__":
    unittest.main()
