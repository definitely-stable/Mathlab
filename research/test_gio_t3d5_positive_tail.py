"""G6-D5 independent exact original-source PSD positive-tail tests."""
from fractions import Fraction as Q
import unittest

from gio_t3d5_positive_tail import (
    SCHEMA,PARENT_G6D4,source_adjacency,centered_cutoff_operator,
    exact_positive_tail_psd,wenger_q_eigenspace_witness,
    doubled_gq_sign_witness,witness_for_fixture,tail_mixing_constants,
    integrated_tail_ledger,finite_case,certificate,
    published_Wenger_symbolic_tail,
)
from gio_t3d4_few_outliers import (
    original_source_case, actual_outlier_count,
)
from gio_t3c_intrinsic_defect import (
    source_graph, typed_maps, direct_original_owner_conflicts,
)


def independently_check_majorant(neighbors,W,c):
    """Entrywise independently expand original centered cutoff."""
    n=len(neighbors)
    k=len(neighbors[0])
    D=[]
    for i in range(n):
        row=[]
        for j in range(n):
            val=Q(int(j in neighbors[i])-(c if i==j else 0))
            # Centering independently: 1^T A = k 1^T.
            row.append(val-Q(k-c,n))
        D.append(row)
    assert all(sum(row)==0 for row in D)
    assert all(D[i][j]==D[j][i] for i in range(n) for j in range(n))
    return [[W[i][j]-D[i][j] for j in range(n)] for i in range(n)]


def source_factor_trace(src,maps,which):
    """Independent original symbol-first trace, not production conflict census."""
    labels=maps["f" if which=="point" else "g"]
    nbr=src["neighbors_point" if which=="point" else "neighbors_line"]
    fiber={}
    for i,pair in enumerate(labels):
        for x in pair:
            fiber.setdefault(x,set()).add(i)
    tr=sum(sum(int(j in nbr[i]) for i in group for j in group)
           for group in fiber.values())
    direct=sum(int(bool(set(labels[i])&set(labels[j])))
               for i,nb in enumerate(nbr) for j in nb if i<j)
    assert tr==2*direct
    return direct


class TestG6D5(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=certificate()
        cls.cases={(x["kind"],x["scheme"]):x
                   for x in cls.data["exact_actual_source_PSD_witnesses"]}

    def test_01_precise_research_scope(self):
        x=self.data
        self.assertEqual(x["schema"],SCHEMA)
        self.assertEqual(x["parent_G6D4_HEAD"],PARENT_G6D4)
        self.assertEqual(x["claim"],"CONDITIONAL_QUADRATIC_T3_POSITIVE_SPECTRAL_TAIL")
        self.assertTrue(x["strict_finite_Wenger5_separation_from_D4_at_same_parameters"])
        self.assertTrue(x["no_infinite_separation_claim"])
        self.assertTrue(x["no_unrestricted_T3_or_ASET"])
        self.assertTrue(x["no_external_referee_or_Lean"])
        self.assertTrue(x["source_original_six_ID_and_flags_only"])

    def test_02_connected_real_quadratic_Wenger5_strict_finite_separation(self):
        x=self.cases["wenger5","lex"]
        self.assertEqual(x["original_points"],125)
        self.assertEqual(x["original_lines"],125)
        self.assertEqual(x["original_flags"],625)
        self.assertEqual(x["actual_Moore_excess_lines"],40)
        self.assertEqual(x["actual_Moore_excess_points"],40)
        self.assertTrue(x["previous_G6D4_rank_gate_fails_at_same_ell_nu"])
        for side in ("point","line"):
            d=x["exact_psd_tail_witnesses"][side]
            m=x["exact_source_positive_outlier_rank"][side][
                "centered_positive_outliers"]
            self.assertEqual(d["cutoff"],4)
            self.assertEqual(d["trace_W"],"40")
            self.assertEqual(m,40)
            self.assertGreater(m**6,2**6*4**7)
            self.assertLessEqual(Q(d["trace_W"])**2,2**2*4**5)
            self.assertTrue(d["exact_squared_tail_gate"])
            self.assertEqual(d["W_PSD_exact_inertia"]["negative"],0)
            self.assertEqual(d["dominance_PSD_exact_inertia"]["negative"],0)

    def test_03_connected_real_quadratic_Wenger3_both_types(self):
        x=self.cases["wenger3","lex"]
        self.assertEqual(x["original_flags"],81)
        self.assertEqual(x["actual_Moore_excess_lines"],12)
        self.assertTrue(x["previous_G6D4_rank_gate_fails_at_same_ell_nu"])
        for side in ("point","line"):
            d=x["exact_psd_tail_witnesses"][side]
            self.assertEqual(d["trace_W"],"6")
            self.assertEqual(d["cutoff"],2)
            self.assertEqual(x["exact_source_positive_outlier_rank"][side][
                "centered_positive_outliers"],6)

    def test_04_independent_source_factor_traces_universal_lex_correlated(self):
        for key in (("wenger3","lex"),("wenger3","correlated"),
                    ("wenger5","lex"),("doubleQminus24","lex"),
                    ("doubleDualQminus42","lex")):
            src,maps=original_source_case(*key)
            x=self.cases[key]
            p=source_factor_trace(src,maps,"point")
            l=source_factor_trace(src,maps,"line")
            self.assertEqual(p,x["point_collinearity_conflicts"])
            self.assertEqual(l,x["line_collinearity_conflicts"])
            self.assertEqual(p+l,x["original_conflicts_J"])
            self.assertEqual(p+l,direct_original_owner_conflicts(src,maps)["J"])

    def test_05_wenger_projector_is_centered_and_true_q_eigenspace(self):
        for q in (3,5):
            src,_=original_source_case("wenger"+str(q))
            n=q**3
            for side in ("point","line"):
                neighbors=src["neighbors_point" if side=="point"
                              else "neighbors_line"]
                W=wenger_q_eigenspace_witness(neighbors,q,1)
                self.assertEqual(len(W),n)
                self.assertTrue(all(sum(row)==0 for row in W))
                self.assertEqual(sum(W[i][i] for i in range(n)),
                                 Q(q*(q-1)**2,2))
                # Independent actual adjacency multiplication A W=q W,
                # not merely trusting a published eigenvalue list.
                for i in range(n):
                    for j in range(n):
                        self.assertEqual(sum(W[x][j] for x in neighbors[i]),
                                         q*W[i][j])

    def test_06_exact_centered_operator_and_residual_entrywise(self):
        for k in ("wenger3","wenger5","doubleQminus24"):
            src,_=original_source_case(k)
            for side in ("point","line"):
                neighbors=src["neighbors_point" if side=="point"
                              else "neighbors_line"]
                ell=1 if k.startswith("wenger") else 2
                r=min(src["s"],src["t"])
                W=witness_for_fixture(k,src,side,ell)
                D=centered_cutoff_operator(neighbors,ell*r)
                J=independently_check_majorant(neighbors,W,ell*r)
                self.assertEqual(
                    J,[[W[i][j]-D[i][j] for j in range(len(D))]
                       for i in range(len(D))])
                self.assertTrue(all(sum(row)==0 for row in D))

    def test_07_real_asymmetric_double_dual_rank_one_witness(self):
        for k in ("doubleW32","doubleQminus24","doubleDualQminus42"):
            src,_=original_source_case(k)
            r=min(src["s"],src["t"])
            x=self.cases[k,"lex"]
            for side in ("point","line"):
                nbr=src["neighbors_point" if side=="point" else "neighbors_line"]
                W=doubled_gq_sign_witness(nbr,2,r)
                self.assertEqual(sum(W[i][i] for i in range(len(W))),
                                 Q(max(0,len(nbr[0])-2*r)))
                self.assertTrue(all(sum(row)==0 for row in W))
                self.assertEqual(x["exact_psd_tail_witnesses"][side][
                    "W_PSD_exact_inertia"]["negative"],0)
                self.assertEqual(x["exact_source_positive_outlier_rank"][side][
                    "centered_positive_outliers"],1)

    def test_08_refuse_underbudget_even_when_PSD_valid(self):
        src,_=original_source_case("wenger5")
        for side in ("point","line"):
            nbr=src["neighbors_point" if side=="point" else "neighbors_line"]
            W=wenger_q_eigenspace_witness(nbr,5,1)
            # True trace = 40 > r^(5/2)=32, so nu=1 rejects.
            self.assertGreater(Q(40)**2,4**5)
            with self.assertRaises(ValueError):
                exact_positive_tail_psd(nbr,W,1,4,1)

    def test_09_refuse_zero_witness_when_positive_excess_present(self):
        src,_=original_source_case("wenger5")
        neighbors=src["neighbors_point"]
        W=[[Q(0) for _ in neighbors] for _ in neighbors]
        with self.assertRaises(ValueError):
            exact_positive_tail_psd(neighbors,W,1,4,2)

    def test_10_negative_controls_exact_dimension_symmetry_and_cutoff(self):
        src,_=original_source_case("W32")
        nbr=src["neighbors_point"]
        n=len(nbr)
        good=[[Q(0) for _ in range(n)] for _ in range(n)]
        self.assertTrue(exact_positive_tail_psd(nbr,good,2,2,0)[
            "exact_squared_tail_gate"])
        for args in ((-1,2,2),(2,1,2),(2,2,-1),
                     (True,2,2),(2,2,Q(1))):
            with self.assertRaises(ValueError):
                exact_positive_tail_psd(nbr,good,*args)
        with self.assertRaises(ValueError):
            exact_positive_tail_psd(nbr,[[1]],2,2,2)
        bad=[[Q(0) for _ in range(n)] for _ in range(n)]
        bad[0][1]=1
        with self.assertRaises(ValueError):
            exact_positive_tail_psd(nbr,bad,2,2,2)
        with self.assertRaises(ValueError):
            source_adjacency([{1},{0},set()])

    def test_11_real_source_GQ_zero_tail_at_ell_two(self):
        for k in ("W32","Qminus24","dualQminus42"):
            src,_=original_source_case(k)
            for side in ("point","line"):
                nbr=src["neighbors_point" if side=="point" else "neighbors_line"]
                W=witness_for_fixture(k,src,side,2)
                self.assertTrue(all(all(x==0 for x in row) for row in W))
                self.assertEqual(sum(W[i][i] for i in range(len(W))),0)

    def test_12_formal_all_order_gram_error_budget(self):
        for z in self.data["formal_all_order_source_and_four_error_ledgers"]:
            self.assertTrue(z["FORMAL_ONLY"])
            self.assertTrue(z["no_unrestricted_T3"])
            self.assertTrue(z["external_numeric_graph_C6_NOT_verified"])
            a=z["source"];f=z["fixed_before_source"];m=z["moments"];s=z["selector"]
            self.assertEqual(a["each_collinearity_conflict_j0"],
                a["point_degree_k0"]*a["alphabet_a0"]
                +f["centered_cutoff_ell"]*a["source_V0"]
                +a["alphabet_a0"]*f["positive_tail_nu"])
            self.assertTrue(a["no_positive_outlier_rank_gate"])
            self.assertTrue(a["no_global_F0_norm_gate"])
            self.assertIn("(trace W)^2<=nu^2*r^5",
                          m["exact_psd_sufficient_witness"])
            c=z["closure"];r=int(c["sufficient_r0"]);e=Q(c["eps"]);rho=Q(c["rho"])
            self.assertLessEqual(m["improper"],e*r)
            self.assertLessEqual(m["E"]**2,e*e*r)
            self.assertLessEqual(m["blocker_D"]**8,e**8*r)
            self.assertLessEqual(12*f["balance_b"]**2*rho*s["q3"]**2*m["L6"],
                                 e*e)
            self.assertGreater(Q(c["delta"]),0)

    def test_13_fixed_parameters_and_invalid_formal_numbers(self):
        for b,C,ell,nu in ((1,3,1,2),(1,3,2,0),(2,12,2,2),
                           (10,4,9,1)):
            a=tail_mixing_constants(b,C,ell,nu)
            self.assertGreater(a["original_owner_conflict_J0"],0)
            self.assertEqual(a["original_owner_conflict_J0"],
                             2*a["each_collinearity_conflict_j0"])
        for args in ((0,3,1,2),(1,-1,1,2),(1,2,-1,2),
                     (1,2,1,-1),(True,2,1,1),(1,2,1,0.5)):
            with self.assertRaises(ValueError):
                tail_mixing_constants(*args)
        with self.assertRaises(ValueError):
            integrated_tail_ledger(1,3,1,2,Q(0),Q(1))
        with self.assertRaises(ValueError):
            integrated_tail_ledger(1,3,1,2,Q(1),Q(0))

    def test_14_no_false_infinite_conclusion_from_selected_finite_parameters(self):
        for z in self.data["exact_actual_source_PSD_witnesses"]:
            self.assertTrue(z["finite_fixture_constants_selected_AFTER_source"])
            self.assertTrue(z["true_original_source_not_synthetic_F"])
            self.assertTrue(z["no_GQ_projection_completion"])
            r=z["r"];a=z["source_constants"]
            self.assertLessEqual(z["original_conflicts_J"],
                                 a["original_owner_conflict_J0"]*r**4)
            self.assertLessEqual(z["point_original_gram"]**2,
                                 a["original_pencil_Gram_G0"]**2*r**11)
            self.assertLessEqual(z["line_original_gram"]**2,
                                 a["original_pencil_Gram_G0"]**2*r**11)

    def test_15_no_fake_source_shortcycles_or_degree_changes(self):
        src,_=original_source_case("W32")
        lines=[set(z) for z in src["lines"]]
        p,q=sorted(lines[0])[:2]
        ell=next(i for i in range(1,len(lines)) if p in lines[i])
        victim=next(i for i in lines[ell] if i!=p)
        lines[ell].remove(victim)
        lines[ell].add(q)
        with self.assertRaises(ValueError):
            source_graph(lines,src["points"],src["s"],src["t"])

    def test_16_actual_positive_tail_spectral_identity_not_count_only(self):
        # W2(q) has 2q eigenvalue at BBt, hence lambda=q for
        # original point-collinearity A=BBt-qI. For cutoff ell*r:
        # tau_exact=m2*max(q-ell*r,0). W is a witness achieving it.
        for q in (3,5):
            src,_=original_source_case("wenger"+str(q))
            r=q-1;m2=q*(q-1)**2//2
            for ell in (1,2):
                W=wenger_q_eigenspace_witness(src["neighbors_point"],q,ell)
                self.assertEqual(sum(W[i][i] for i in range(q**3)),
                                 m2*max(q-ell*r,0))
                outs=actual_outlier_count(src["neighbors_point"],ell*r)
                self.assertEqual(outs["centered_positive_outliers"],
                                 m2 if q>ell*r else 0)


    def test_17_symbolic_Wenger_tail_fixed_nu_finite_not_infinite(self):
        # W2(q) is a genuine infinite published source family for PRIME
        # POWERS q; these arithmetic rows do not construct q^3 sources.
        out=[published_Wenger_symbolic_tail(q,1,2)
             for q in (3,5,7,11,13,17,19)]
        self.assertTrue(all(x["positive_tail_gate_G6D5"] for x in out[:5]))
        self.assertTrue(all(not x["positive_tail_gate_G6D5"] for x in out[5:]))
        self.assertTrue(all(x["published_Wenger_W2_prime_power_hypothesis_REQUIRED"]
                            for x in out))
        self.assertTrue(all(x["actual_source_NOT_instantiated_for_this_symbolic_formula"]
                            for x in out))
        self.assertEqual(out[1]["positive_outlier_rank"],40)
        self.assertEqual(out[1]["positive_tail_exact"],40)
        self.assertEqual(out[4]["positive_tail_exact"],936)
        self.assertEqual(out[5]["positive_tail_exact"],2176)
        self.assertFalse(out[1]["rank_gate_G6D4"])
        # For ell=1, nu=2, the G6D5 criterion is exactly
        #   (r+1)^2 <=16r; false for every r>=14
        # since r^2-14r+1 is already positive at r=14 and increasing.
        for r in range(14,401):
            self.assertGreater((r+1)**2,16*r)
        for a in ((2,1,2),(5,-1,2),(5,1,-1),(5,1,True)):
            with self.assertRaises(ValueError):
                published_Wenger_symbolic_tail(*a)


if __name__=="__main__":
    unittest.main()
