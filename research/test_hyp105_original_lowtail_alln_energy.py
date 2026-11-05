r"""Independent complete ORIGINAL all-N low-tail spectral path certificate.

Non-duplicate actual W32/W34 GQ source f,g and original source ID Z
are used; actual physical 3-walks, exceptional/low-tail projection
endpoint masks, two dual FULL-allowed / CORE source book B energies
and all six true original positive GF5 BBo source flags.
"""
from fractions import Fraction
import unittest

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_original_lowtail_alln_energy import (
    _source,_endpoint_mask,_original_geometry,
    _physical_trace_and_three_walks,_mixed_original_B,
    _true_physical,full_original_lowtail_source_energy_certificate,
    canonical_original_lowtail_allN,
)


class TestRealOriginalAllNLowTailEnergy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.maps={(h,s):pair_labeled_symplectic(h,s)
                  for h in (1,2) for s in ("lex","reverse-line")}

    def test_true_source_original_W32_W34_complete_proper3_and_dual_blocker(self):
        for h,scheme in ((1,"lex"),(1,"reverse-line"),
                         (2,"lex"),(2,"reverse-line")):
            with self.subTest(h=h,scheme=scheme):
                m=self.maps[h,scheme]
                n=len(m["incidences"])
                Z=tuple(range(0,n,17))
                C=tuple(i for i in range(n) if i not in Z and i%4 in (0,1,3))
                z=full_original_lowtail_source_energy_certificate(
                    h,m["left_labels"],m["right_labels"],C,Z)
                self.assertTrue(z["all_N_complete_original_source_path_partition"])
                self.assertTrue(z["all_N_symmetric_original_masked_four_blocker_bound"])
                self.assertEqual(z["root_230_status"],"OPEN_WITH_FORMAL_BLOCKER")
                self.assertFalse(z["allh_positive_root_Branch_A_proved_here"])
                self.assertEqual(z["physical_real_edge_count"],2*len(C))
                self.assertEqual(
                    z["physical_proper_ordered_3paths"]+
                    z["physical_improper_3walks"],
                    z["physical_full_graph_ordered_3walks"])
                self.assertEqual(
                    z["actual_original_good_unblocked_directed3"],
                    2*z["real_positive_original_BBo_sixsets"])
                self.assertEqual(
                    z["actual_original_good_unblocked_directed3"],
                    z["physical_proper_ordered_3paths"]-
                    z["actual_original_bad_endpoint_path_mass"]-
                    z["physical_internal_original_blocked_path_union"])
                self.assertLessEqual(
                    z["physical_improper_3walks"],
                    z["physical_improper_3walks_max_3DeltaQ"])
                self.assertGreaterEqual(
                    Fraction(z["actual_original_good_unblocked_directed3"]),
                    Fraction(z["all_N_abstract_energy_good3_lower"]))
                self.assertEqual(len(
                    z["real_positive_original_BBo_six_IDs"]),
                    z["real_positive_original_BBo_sixsets"])
                self.assertTrue(all(
                    len(ids)==6 and len(set(ids))==6 and
                    not set(ids)&set(Z)
                    for ids in z["real_positive_original_BBo_six_IDs"]))

    def test_exact_original_coordinate_endpoint_partition_all_offdiagonal(self):
        for h,scheme in ((1,"lex"),(1,"reverse-line"),
                         (2,"lex"),(2,"reverse-line")):
            with self.subTest(h=h,scheme=scheme):
                m=self.maps[h,scheme]
                s,V,a,flags,f,g,C,Z=_source(
                    h,m["left_labels"],m["right_labels"],
                    tuple(range(0,len(m["incidences"]),3)),
                    tuple(range(1,len(m["incidences"]),3)))
                bins,bad,meta=_endpoint_mask(a,flags,f,g,set(Z),V)
                self.assertEqual(sum(map(len,bins.values())),
                                 a*a*(a-1)*(a-1))
                self.assertEqual(len(bad)+len(bins["admissible"]),
                                 a*a*(a-1)*(a-1))
                self.assertEqual(len(meta),len(bins["admissible"]))
                for key,(p,ell,ids) in meta.items():
                    self.assertEqual(len(set(ids)),3)
                    self.assertFalse(set(ids)&set(Z))
                    x,y=key[0];z,w=key[1]
                    self.assertFalse(set(f[p])&{x,z})
                    self.assertFalse(set(g[ell])&{y,w})

    def test_no_deletion_original_full_source_true_projection_and_source_Cauchy(self):
        for h,scheme in ((1,"lex"),(2,"reverse-line")):
            m=self.maps[h,scheme]
            n=len(m["incidences"])
            s,V,a,flags,f,g,C,Z=_source(
                h,m["left_labels"],m["right_labels"],
                tuple(range(n)),())
            graph,owner=_true_physical(flags,f,g,C,a)
            D,T4,W,A2=_physical_trace_and_three_walks(graph)
            self.assertEqual(len(owner),2*n)
            self.assertGreater(W,0)
            self.assertGreater(T4,0)
            self.assertGreaterEqual(D,1)
            source=_mixed_original_B(flags,f,g,C,(),V,a)
            dual=_mixed_original_B(
                tuple((l,p) for p,l in flags),g,f,C,(),V,a)
            self.assertTrue(source["source_mixed_book_Cauchy"])
            self.assertTrue(dual["source_mixed_book_Cauchy"])
            self.assertGreater(source["Theta"],0)
            self.assertGreater(dual["Theta"],0)
            self.assertGreater(source["B"],0)
            self.assertGreater(dual["B"],0)

    def test_independent_existing_true_GQ_original_six_ID_BBo_avoidance_oracle(self):
        # #673 reconstructs original source BBo paths by a different
        # source projection + physically owned flags implementation.
        from hyp105_bbo_resilience import avoidance_certificate
        canonical=canonical_original_lowtail_allN()
        for row in canonical["genuine_true_original_cases"]:
            with self.subTest(s=row["s"],scheme=row["scheme"]):
                power=1 if row["s"]==2 else 2
                scheme=row["scheme"]
                m=self.maps[power,scheme]
                other=avoidance_certificate(
                    power,m["left_labels"],m["right_labels"],
                    row["deleted_original_flag_IDs"],
                    core_ids=row["original_core_source_IDs"])
                self.assertEqual(
                    set(tuple(x) for x in row["real_positive_original_BBo_six_IDs"]),
                    set(tuple(x) for x in other["produced_sixsets"]))
                self.assertEqual(
                    row["actual_original_good_unblocked_directed3"],
                    other["unblocked_paths_avoiding_all_six_forbidden_ids"])

    def test_original_Qx_Qy_are_independently_the_physical_A_squared_row_column_returns(self):
        for h,scheme in ((1,"lex"),(2,"lex"),(2,"reverse-line")):
            m=self.maps[h,scheme]
            n=len(m["incidences"])
            Z=tuple(range(1,n,31))
            C=tuple(i for i in range(n) if i not in Z and i%5 in (0,1,4))
            s,V,a,flags,f,g,C,Z=_source(
                h,m["left_labels"],m["right_labels"],C,Z)
            graph,_=_true_physical(flags,f,g,C,a)
            _,_,_,A2=_physical_trace_and_three_walks(graph)
            xreturns=sum(num for u,row in A2.items()
                         for v,num in row.items() if u[0]==v[0])
            yreturns=sum(num for u,row in A2.items()
                         for v,num in row.items() if u[1]==v[1])
            z=full_original_lowtail_source_energy_certificate(
                h,f,g,C,Z)
            self.assertEqual(xreturns,z["original_source_Qx"])
            self.assertEqual(yreturns,z["original_source_Qy"])

    def test_strict_fail_closed_false_original_IDs_and_maps(self):
        m=self.maps[1,"lex"]
        f,g=m["left_labels"],m["right_labels"]
        bad=list(f);bad[0]=bad[1]
        for C,Z in (((0,1),(1,)),((0,0),()),((45,),()),
                    ((0,),(True,)),((0,),(-1,))):
            with self.assertRaises(ValueError):
                full_original_lowtail_source_energy_certificate(
                    1,f,g,C,Z)
        with self.assertRaises(ValueError):
            full_original_lowtail_source_energy_certificate(
                1,bad,g,(0,1),())
        with self.assertRaises(ValueError):
            full_original_lowtail_source_energy_certificate(
                3,f,g,(0,1),())

    def test_canonical_full_true_original_source_is_not_root_allh_promotion(self):
        z=canonical_original_lowtail_allN()
        self.assertEqual(z["schema"],
                         "mathlab.hyp105.original-LOWTAIL-allN-energy-source.v1")
        self.assertEqual(len(z["genuine_true_original_cases"]),4)
        self.assertFalse(z["allh_unconditional_ROOT_230_claim"])
        self.assertEqual(z["root_230_status"],"OPEN_WITH_FORMAL_BLOCKER")


if __name__=="__main__":
    unittest.main()
