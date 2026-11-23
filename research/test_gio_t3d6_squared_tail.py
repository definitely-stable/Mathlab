"""Independent G6-D6 source, Schatten-2, PSD and infinite-series tests."""
from fractions import Fraction as Q
from itertools import combinations
import unittest

from gio_t3d6_squared_tail import (
    SCHEMA,PARENT_G6D5,exact_squared_tail_psd,
    original_factor_frobenius,source_quadratic_tail_constants,
    integrated_square_tail_ledger,published_Wenger_squared_tail,
    actual_source_case,certificate,
)
from gio_t3d4_few_outliers import original_source_case
from gio_t3d5_positive_tail import (
    source_adjacency,centered_cutoff_operator,witness_for_fixture,
)
from gio_t3c_intrinsic_defect import (
    source_graph,direct_original_owner_conflicts,
)


def independent_label_overlap(src,labels,side):
    """Brute literal H H^T without fiber-occupancy formula."""
    n=src["points"] if side=="point" else len(src["lines"])
    assert n==len(labels)
    H=[[int(x in labels[p]) for x in range(max(max(z) for z in labels)+1)]
       for p in range(n)]
    G=[[sum(H[i][x]*H[j][x] for x in range(len(H[0])))
        for j in range(n)] for i in range(n)]
    return sum(t*t for row in G for t in row)


def independent_original_trace(src,labels,side):
    nbr=src["neighbors_point" if side=="point" else "neighbors_line"]
    labels=[set(z) for z in labels]
    direct=sum(bool(labels[i]&labels[j])
               for i in range(len(nbr)) for j in nbr[i] if i<j)
    return direct


def independent_witness_factor_trace(src,labels,side,W):
    """Tr(W H H^T) literal source pairs; exact source-independent H."""
    n=len(labels)
    assert len(W)==n
    return sum(W[i][j]*len(set(labels[i])&set(labels[j]))
               for i in range(n) for j in range(n))


class TestG6D6(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=certificate()
        cls.by={(z["kind"],z["scheme"]):z
                for z in cls.c["actual_original_source_independent_finite_checks"]}

    def test_01_scope_parent_and_honest_prior_art(self):
        x=self.c
        self.assertEqual(x["schema"],SCHEMA)
        self.assertEqual(x["parent_G6D5_HEAD"],PARENT_G6D5)
        self.assertEqual(x["claim"],
             "CONDITIONAL_T3_QUADRATIC_EXCESS_POSITIVE_SQUARED_TAIL")
        self.assertTrue(x["truly_infinite_Wenger_fixed_cutoff_separation_from_D5_nu2"])
        self.assertTrue(x["same_Wenger_family_already_in_D2_by_different_gate"])
        self.assertTrue(x["no_new_infinite_graph_family_or_unrestricted_T3"])
        self.assertTrue(x["standard_Schatten_Holder_and_Wenger_spectra_prior_art"])
        self.assertTrue(x["no_external_referee_or_Lean"])

    def test_02_exact_real_wenger5_two_typed_squared_tails(self):
        x=self.by["wenger5","lex"]
        self.assertEqual((x["actual_source_points"],x["actual_source_lines"],
                          x["actual_original_flags"]),(125,125,625))
        self.assertEqual(x["actual_Moore_excess_L"],40)
        self.assertEqual(x["actual_Moore_excess_P"],40)
        for side in ("point","line"):
            z=x["exact_positive_square_tail_PSD_certificates"][side]
            self.assertEqual(Q(z["witness_trace_W_squared"]),40)
            self.assertEqual(z["cutoff"],4)
            self.assertTrue(z["exact_seventh_power_gate"])
            self.assertEqual(z["exact_symmetric_W_PSD"]["negative"],0)
            self.assertEqual(z["exact_symmetric_dominance_PSD"]["negative"],0)

    def test_03_exact_real_wenger3_correlated_and_lex(self):
        for scheme in ("lex","correlated"):
            x=self.by["wenger3",scheme]
            self.assertEqual(x["actual_original_flags"],81)
            for side in ("point","line"):
                d=x["exact_positive_square_tail_PSD_certificates"][side]
                self.assertEqual(Q(d["witness_trace_W_squared"]),6)
                self.assertEqual(d["cutoff"],2)
                self.assertTrue(d["original_source_centered_projection"])

    def test_04_wenger_all_order_proved_squared_tail_vs_D5_fixed_gate(self):
        # Published q are prime powers; no large q^3 actual graph
        # instantiated by this symbolic oracle.
        for q in (3,4,5,7,8,11,13,16,17,19,23,31,32,64,101):
            w=published_Wenger_squared_tail(q,1,1,2)
            r=q-1
            self.assertEqual(w["positive_tail_squared"],q*r*r//2)
            self.assertEqual(w["positive_tail_first"],q*r*r//2)
            self.assertTrue(w["D6_squared_tail_gate"])
            self.assertLessEqual((r+1)**2,4*r**3)
            if r>=14:
                self.assertFalse(w["D5_first_tail_gate"])
                self.assertGreater((r+1)**2,16*r)
            self.assertTrue(w["published_W2_requires_prime_power_q"])
            self.assertTrue(w["symbolic_only_NOT_original_matrix_instantiation"])
        self.assertEqual(published_Wenger_squared_tail(17)["positive_tail_squared"],
                         2176)
        self.assertEqual(published_Wenger_squared_tail(101)["positive_tail_squared"],
                         505000)

    def test_05_independent_true_two_symbol_factor_Frobenius_identity(self):
        for name in ("W32","Qminus24","dualQminus42",
                     "doubleW32","doubleQminus24",
                     "doubleDualQminus42","wenger3","wenger5"):
            src,maps=original_source_case(name)
            case=self.by[name,"lex"]
            for side in ("point","line"):
                labels=maps["f" if side=="point" else "g"]
                z=case["independently_checked_original_factor_Frobenius"][side]
                brute=independent_label_overlap(src,labels,side)
                self.assertEqual(brute,z["factor_incidence_frob_squared"])
                self.assertEqual(brute,z["direct_pair_overlap_squared"])
                self.assertLessEqual(brute,z["factor_trace_critical_bound"])
                self.assertTrue(z["complete_two_symbol_paired_fiber_identity"])

    def test_06_original_all_pair_label_conflicts_are_exact(self):
        for name,scheme in (("W32","lex"),("Qminus24","lex"),
                            ("dualQminus42","lex"),("wenger3","lex"),
                            ("wenger3","correlated"),("wenger5","lex"),
                            ("wenger5","correlated")):
            src,maps=original_source_case(name,scheme)
            case=self.by[name,scheme]
            pc=independent_original_trace(src,maps["f"],"point")
            lc=independent_original_trace(src,maps["g"],"line")
            self.assertEqual(pc,case["original_source_point_conflicts"])
            self.assertEqual(lc,case["original_source_line_conflicts"])
            self.assertEqual(pc+lc,case["original_source_J"])
            self.assertEqual(pc+lc,direct_original_owner_conflicts(src,maps)["J"])

    def test_07_exact_Schatten_Cauchy_for_original_source_W_and_H(self):
        # All inner products are exact rationals: Tr(W HH^T)^2
        # <= Tr(W^2) * Tr((HH^T)^2), independently computed.
        for name,scheme in (("wenger3","lex"),("wenger5","lex"),
                            ("doubleQminus24","lex"),
                            ("doubleDualQminus42","lex")):
            src,maps=original_source_case(name,scheme)
            ell=1 if name.startswith("wenger") else 2
            for side in ("point","line"):
                nb=src["neighbors_point" if side=="point" else "neighbors_line"]
                labels=maps["f" if side=="point" else "g"]
                W=witness_for_fixture(name,src,side,ell)
                wc=sum(t*t for row in W for t in row)
                hf=independent_label_overlap(src,labels,side)
                trace=independent_witness_factor_trace(src,labels,side,W)
                self.assertGreaterEqual(trace,0)
                self.assertLessEqual(trace*trace,wc*hf)
                self.assertEqual(
                    wc,Q(self.by[name,scheme][
                        "exact_positive_square_tail_PSD_certificates"][side][
                        "witness_trace_W_squared"]))

    def test_08_original_GQ_zero_W_and_double_source_controls(self):
        for name in ("W32","Qminus24","dualQminus42"):
            z=self.by[name,"lex"]
            for side in ("point","line"):
                self.assertEqual(Q(z["exact_positive_square_tail_PSD_certificates"][
                    side]["witness_trace_W_squared"]),0)
        for name in ("doubleW32","doubleQminus24","doubleDualQminus42"):
            z=self.by[name,"lex"]
            r=z["r"]
            for side in ("point","line"):
                x=z["exact_positive_square_tail_PSD_certificates"][side]
                self.assertGreater(Q(x["witness_trace_W_squared"]),0)
                self.assertLessEqual(Q(x["witness_trace_W_squared"])**2,
                                     8*8*r**7)
            self.assertTrue(z["finite_fixture_params_selected_AFTER_source"])

    def test_09_reject_zero_false_PSD_witness_on_actual_Wenger5(self):
        src,_=original_source_case("wenger5")
        for side in ("point","line"):
            nb=src["neighbors_point" if side=="point" else "neighbors_line"]
            zero=[[Q(0)]*len(nb) for _ in nb]
            with self.assertRaises(ValueError):
                exact_squared_tail_psd(nb,zero,1,4,1)

    def test_10_fail_closed_rational_witness_inputs(self):
        src,_=original_source_case("W32")
        nb=src["neighbors_point"];n=len(nb)
        W=[[Q(0) for _ in nb] for _ in nb]
        self.assertEqual(Q(exact_squared_tail_psd(nb,W,2,2,0)[
            "witness_trace_W_squared"]),0)
        for params in ((-1,2,1),(1,1,1),(1,2,-1),(True,2,1),
                       (1,2,Q(1))):
            with self.assertRaises(ValueError):
                exact_squared_tail_psd(nb,W,*params)
        with self.assertRaises(ValueError):
            exact_squared_tail_psd(nb,[[Q(0)]],2,2,0)
        bad=[[Q(0) for _ in nb] for _ in nb]
        bad[0][1]=1
        with self.assertRaises(ValueError):
            exact_squared_tail_psd(nb,bad,2,2,0)
        bad[0][1]=0
        bad[0][0]=-1
        with self.assertRaises(ValueError):
            exact_squared_tail_psd(nb,bad,2,2,4)

    def test_11_reject_underbudget_for_actual_nonzero_square_tail(self):
        src,_=original_source_case("wenger5")
        nb=src["neighbors_point"]
        W=witness_for_fixture("wenger5",src,"point",1)
        with self.assertRaises(ValueError):
            exact_squared_tail_psd(nb,W,1,4,0)
        self.assertEqual(Q(exact_squared_tail_psd(nb,W,1,4,1)[
            "witness_trace_W_squared"]),40)

    def test_12_fixed_source_constants_and_critical_sqrt_envelope(self):
        for p in ((1,3,1,1),(2,12,2,8),(1,3,2,0),(4,7,3,13)):
            a=source_quadratic_tail_constants(*p)
            self.assertEqual(a["original_owner_conflict_J0"],
                             2*a["each_collinearity_conflict_j0"])
            self.assertGreaterEqual(a["weighted_tail_root0"]**2,
                2*a["source_V0"]*a["alphabet_a0"]*p[3])
            self.assertEqual(a["each_collinearity_conflict_j0"],
                a["point_degree_k0"]*a["alphabet_a0"]
                +p[2]*a["source_V0"]+a["weighted_tail_root0"])
        for bad in ((0,1,1,1),(1,-1,1,1),(1,1,-1,1),
                    (1,1,1,-1),(1,1,1,True)):
            with self.assertRaises(ValueError):
                source_quadratic_tail_constants(*bad)

    def test_13_exact_formal_four_LOW_budgets_and_quantifier_stops(self):
        for z in self.c["exact_all_order_four_error_formal_ledgers"]:
            self.assertTrue(z["FORMAL_ONLY"])
            self.assertTrue(z["no_unrestricted_T3"])
            self.assertTrue(z["no_ASET_exponent_improvement"])
            self.assertTrue(z["external_numeric_graph_C6_NOT_verified"])
            self.assertIn("tr(W^2)^2<=M^2*r^7",
                          z["moments"]["exact_PSD_certificate"])
            f=z["fixed_before_source"];m=z["moments"];sel=z["selector"]
            c=z["closure"];r=int(c["sufficient_r0"])
            eps=Q(c["eps"]);rho=Q(c["rho"])
            self.assertLessEqual(m["improper"],eps*r)
            self.assertLessEqual(m["E"]**2,eps*eps*r)
            self.assertLessEqual(m["blocker_D"]**8,eps**8*r)
            self.assertLessEqual(12*f["balance_b"]**2*rho*sel["q3"]**2*m["L6"],
                                 eps*eps)
            self.assertGreater(Q(c["delta"]),0)

    def test_14_literal_geometry_rejects_false_original_C4_C6(self):
        src,_=original_source_case("W32")
        lines=[set(z) for z in src["lines"]]
        p,q=sorted(lines[0])[:2]
        ell=next(i for i in range(1,len(lines)) if p in lines[i])
        victim=next(z for z in lines[ell] if z!=p)
        lines[ell].remove(victim)
        lines[ell].add(q)
        with self.assertRaises(ValueError):
            source_graph(lines,src["points"],src["s"],src["t"])

    def test_15_no_numeric_spectral_guess_or_fake_infinite_GQ(self):
        for z in self.c["actual_original_source_independent_finite_checks"]:
            self.assertTrue(z["fixed_FAMILY_values_NOT_proved_by_fixture"])
            self.assertTrue(z["original_source_not_synthetic_F"])
            self.assertTrue(z["no_GQ_completion"])
            a=z["source_constants"];r=z["r"]
            self.assertLessEqual(z["original_source_J"],
                                 a["original_owner_conflict_J0"]*r**4)
            self.assertLessEqual(z["point_original_Gram"]**2,
                                 a["original_pencil_Gram_G0"]**2*r**11)
            self.assertLessEqual(z["line_original_Gram"]**2,
                                 a["original_pencil_Gram_G0"]**2*r**11)

    def test_16_true_Wenger_prime_power_all_order_asymptotic_separation(self):
        for q in (16,17,19,23,31,32,64,101):
            z=published_Wenger_squared_tail(q,1,1,2)
            self.assertTrue(z["D6_squared_tail_gate"])
            self.assertFalse(z["D5_first_tail_gate"])
            self.assertEqual(z["positive_tail_first"],z["positive_tail_squared"])
            self.assertTrue(z["published_W2_requires_prime_power_q"])
            self.assertTrue(z["symbolic_only_NOT_original_matrix_instantiation"])
        # Not an improvement in *source families* over the optimized D2:
        self.assertTrue(self.c["same_Wenger_family_already_in_D2_by_different_gate"])

    def test_17_source_disambiguation_and_duality(self):
        for left,right in (("Qminus24","dualQminus42"),
                           ("doubleQminus24","doubleDualQminus42")):
            a=self.by[left,"lex"]
            b=self.by[right,"lex"]
            self.assertEqual(a["source_s"],b["source_t"])
            self.assertEqual(a["source_t"],b["source_s"])
            self.assertEqual(a["actual_source_points"],b["actual_source_lines"])
            self.assertEqual(a["actual_source_lines"],b["actual_source_points"])
            self.assertEqual(a["actual_original_flags"],b["actual_original_flags"])

    def test_18_reject_invalid_published_Wenger_symbolic_params(self):
        for params in ((2,1,1,2),(4,-1,1,2),(4,1,-1,2),
                       (4,1,1,-1),(4,1,True,2)):
            with self.assertRaises(ValueError):
                published_Wenger_squared_tail(*params)
        for params in ((1,3,1,1,Q(0),Q(1)),
                       (1,3,1,1,Q(1),Q(0)),
                       (1,3,1,1,1,1)):
            with self.assertRaises(ValueError):
                integrated_square_tail_ledger(*params)


if __name__=="__main__":
    unittest.main()
