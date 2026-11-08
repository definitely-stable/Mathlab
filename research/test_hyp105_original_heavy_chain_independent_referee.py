"""AA4-HEAVYCHAIN: original symplectic source HEAVY, two cuts and D6 referees."""
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_original_defect_factor_referee import genuine_symplectic_source
from hyp105_original_heavy_chain_independent_referee import (
    SCHEMA,ROOT_STATUS,R,RHO_CAP,_pair_alphabet,heavy_uniform_formal_budget,
    fixed_maps,actual_original_edges,original_conflicts,independent_source,
    source_collinearity_conflict_census,two_exact_original_cuts,
    inverse_D6_by_original_ids,verify_selected_sixcycles,
    true_original_heavy_case,seeded_original_D6_case,canonical_report
)


class TestOriginalHeavyD6Independent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.flags={s:genuine_symplectic_source(s) for s in (2,4)}
        cls.certificate=canonical_report()

    def test_new_original_true_symplectic_W32_W34_source_SRG_first_principles(self):
        for s,flags in self.flags.items():
            V=(s+1)*(s*s+1)
            byp=[set() for _ in range(V)]
            byl=[set() for _ in range(V)]
            for p,l in flags:
                byp[p].add(l);byl[l].add(p)
            self.assertEqual(len(flags),(s+1)*V)
            self.assertTrue(all(len(x)==s+1 for x in byp+byl))
            A=[set() for _ in range(V)]
            for pts in byl:
                for p,q in combinations(sorted(pts),2):
                    A[p].add(q);A[q].add(p)
            self.assertTrue(all(len(x)==s*(s+1) for x in A))
            for p,q in combinations(range(V),2):
                common=len(A[p]&A[q])
                self.assertEqual(common,(s-1) if q in A[p] else (s+1))

    def test_actual_original_two_diagonals_one_flag_one_owner(self):
        for s,flags in self.flags.items():
            a,f,g=fixed_maps(s,flags,"reverse")
            E,per,adj=actual_original_edges(flags,f,g)
            self.assertEqual(len(E),2*len(flags))
            self.assertEqual(len(per),len(flags))
            self.assertEqual(sum(map(len,adj.values())),4*len(flags))
            for i,edges in enumerate(per):
                self.assertEqual(len(edges),2)
                self.assertTrue(all(E[e]==i for e in edges))
                self.assertFalse(set(edges[0])&set(edges[1]))

    def test_typed_collinearity_overlaps_exactly_original_full_J(self):
        for s,flags in self.flags.items():
            for mode in ("lex","reverse","shift"):
                a,f,g=fixed_maps(s,flags,mode)
                q=source_collinearity_conflict_census(s,flags,f,g)
                self.assertEqual(q["actual_original_conflict_J_edges"],
                   q["point_original_collinearity_f_overlap"]+
                   q["line_original_collinearity_g_overlap"])
                self.assertLessEqual(q["point_original_collinearity_f_overlap"],
                                     q["both_typed_C_s_upper"])
                self.assertLessEqual(q["line_original_collinearity_g_overlap"],
                                     q["both_typed_C_s_upper"])

    def test_original_Caro_Wei_min_degree_J_independence_witness(self):
        for s,flags in self.flags.items():
            a,f,g=fixed_maps(s,flags,"shift")
            J=original_conflicts(flags,f,g,range(len(flags)))
            chosen=independent_source(J)
            m=sum(map(len,J.values()))//2
            bound=Fraction(len(J)**2,len(J)+2*m)
            self.assertGreaterEqual(len(chosen),bound)
            self.assertTrue(all(j not in J[i] for i,j in combinations(chosen,2)))

    def test_both_coordinate_cuts_retained_original_flags_and_own_both_diagonals(self):
        for s,flags in self.flags.items():
            a,f,g=fixed_maps(s,flags,"reverse")
            J=original_conflicts(flags,f,g,range(len(flags)))
            I=independent_source(J)
            S,cuts=two_exact_original_cuts(I,flags,f,g,a)
            self.assertGreaterEqual(4*len(S),len(I))
            self.assertEqual(cuts[0]["input"],len(I))
            self.assertEqual(cuts[1]["output"],len(S))
            self.assertTrue(all(cuts[0]["bits"][f[flags[i][0]][0]]!=
                         cuts[0]["bits"][f[flags[i][0]][1]] and
                         cuts[1]["bits"][g[flags[i][1]][0]]!=
                         cuts[1]["bits"][g[flags[i][1]][1]]
                         for i in S))
            E,per,adj=actual_original_edges(flags,f,g)
            self.assertEqual(len({e for i in S for e in per[i]}),2*len(S))

    def test_all_h_uniform_exact_spectral_heavy_R_at_multiple_orders(self):
        z=self.certificate["independent_all_h_FORMAL_arithmetic"]
        self.assertEqual(len(z),5)
        self.assertEqual([x["s"] for x in z],[64,64,128,1024,65536])
        for q in z:
            self.assertEqual(q["R"],R)
            self.assertTrue(all(q["all_h_explicit_rational_and_source_gates"].values()))
            self.assertFalse(q["root_PROVED_A"])
            self.assertFalse(q["external_numerical_C0_c0_assumed"])
        a=heavy_uniform_formal_budget(64,RHO_CAP)
        self.assertEqual(a["R"],93313)
        self.assertLessEqual(Fraction(a["density_R_at_rho"]),R)
        self.assertGreater(Fraction(a["lambda"]),0)

    def test_six_actual_diagnostic_heavy_graphs_have_no_clones_or_imaginary_edges(self):
        rows=self.certificate["true_original_W32_W34_six_heavy_diagnostic_cases"]
        self.assertEqual(len(rows),6)
        self.assertEqual({q["mode"] for q in rows},{"lex","reverse","shift"})
        for q in rows:
            s=q["s"];V=(s+1)*(s*s+1)
            a,_=_pair_alphabet(V)
            self.assertEqual(q["physical_full_edges"],2*q["original_flags"])
            self.assertGreater(q["TRUE_F_edges"],0)
            self.assertLessEqual(q["physical_surviving_heavy_edges"],
                                 q["physical_full_heavy_edges"])
            self.assertGreaterEqual(q["actual_independent_original_owners"],
               Fraction(q["Caro_Wei_necessary_original_independent_lower"]))
            self.assertGreaterEqual(4*q["after_BOTH_source_cuts"],
                                    q["actual_independent_original_owners"])
            self.assertGreaterEqual(Fraction(q["actual_density_F"]),
                                    Fraction(q["source_density_lower_S_over_8a2"]))
            self.assertEqual(q["source_density_lower_S_over_8a2"],
                              str(Fraction(q["after_BOTH_source_cuts"],8*a*a)))
            self.assertEqual(q["unoriented_proper_C6"],
                             q["distinct_original_D6_sixsets"])
            self.assertTrue(q["F_no_clone_and_no_sixset_duplication"])

    def test_construct_true_original_positive_D6_witness_no_finite_vacuity(self):
        seeds=self.certificate["true_original_positive_D6_seed_cases"]
        self.assertEqual(len(seeds),2)
        for q in seeds:
            self.assertEqual(len(q["matching_original_incidence_IDs"]),6)
            self.assertEqual(q["true_TWO_physical_diagonals_per_ID"],12)
            self.assertTrue(q["source_J_independent"])
            self.assertTrue(q["two_explicit_actual_typed_alternating_cuts"])
            self.assertTrue(q["independent_original_sixID_inverse_success"])
            self.assertGreaterEqual(q["unoriented_proper_C6"],1)
            self.assertEqual(q["unoriented_proper_C6"],
                             q["distinct_original_D6_sixsets"])

    def test_source_first_D6_inverse_zero_for_five_or_duplicate_original_IDs(self):
        s=2;flags=self.flags[s];a,f,g=fixed_maps(s,flags,"lex")
        self.assertIsNone(inverse_D6_by_original_ids((0,1,2,3,4),flags,f,g))
        self.assertIsNone(inverse_D6_by_original_ids((0,1,2,3,4,4),flags,f,g))
        self.assertIsNone(inverse_D6_by_original_ids((0,1,2,3,4,5),flags,f,g))

    def test_selected_sixcycle_can_not_multiply_by_twelve(self):
        s=2;flags=self.flags[s]
        seed=seeded_original_D6_case(s)
        self.assertEqual(seed["unoriented_proper_C6"],
                         seed["distinct_original_D6_sixsets"])
        self.assertLessEqual(seed["unoriented_proper_C6"],1)

    def test_original_J_contradiction_coordinate_cherry_on_two_incident_edges(self):
        s=4;flags=self.flags[s];a,f,g=fixed_maps(s,flags,"lex")
        J=original_conflicts(flags,f,g,range(len(flags)))
        E,per,adj=actual_original_edges(flags,f,g)
        candidates=[(i,j) for i in J for j in J[i] if i<j]
        self.assertTrue(candidates)
        found=False
        for i,j in candidates:
            for ei in per[i]:
                for ej in per[j]:
                    shared=set(ei)&set(ej)
                    if shared:
                        v=next(iter(shared))
                        a1=next(vv for vv in ei if vv!=v)
                        a2=next(vv for vv in ej if vv!=v)
                        if a1[0]==a2[0] or a1[1]==a2[1]:
                            found=True;break
                if found:break
            if found:break
        self.assertTrue(found,"true J conflict must witness physical coordinate cherry")

    def test_fail_closed_invalid_original_deletions_and_noninjections(self):
        s=2;flags=self.flags[s];a,f,g=fixed_maps(s,flags,"lex")
        for Z in ((-1,),(len(flags),),(True,)):
            with self.assertRaises(ValueError):
                true_original_heavy_case(s,"lex",Z=Z)
        with self.assertRaises(ValueError):
            true_original_heavy_case(s,"lex",diagnostic_T=0)
        with self.assertRaises(ValueError):
            actual_original_edges(flags,f,tuple([g[0]]*len(g)))
        with self.assertRaises(ValueError):
            original_conflicts(flags,f,g,(0,0))

    def test_formal_non_dyadic_or_bad_original_density_rejected(self):
        for s,rho in ((32,Fraction(0)),(65,Fraction(0)),
                      (64,RHO_CAP+Fraction(1,2**36)),
                      (64,Fraction(-1,17)),(64,0.1)):
            with self.assertRaises(ValueError):
                heavy_uniform_formal_budget(s,rho)

    def test_root_230_unproved_and_external_graph_C0_c0_unknown(self):
        z=self.certificate
        self.assertEqual(z["schema"],SCHEMA)
        self.assertEqual(z["issue"],230)
        self.assertEqual(z["status"],ROOT_STATUS)
        self.assertFalse(z["root_PROVED_A"])
        self.assertFalse(z["new_ASET_exponent"])
        self.assertTrue(z["external_C0_c0_numeric_NOT_claimed"])
        self.assertTrue(z["original_6motif_HEAVY_only"])


if __name__=="__main__":unittest.main()
