"""Independent exact G6-D4 tests: real sources and symmetric-inertia oracle."""
from fractions import Fraction as Q
from itertools import combinations
import unittest

from gio_t3d4_few_outliers import (
    SCHEMA,PARENT_G6D1_FIX,exact_symmetric_inertia,
    actual_outlier_count,original_source_case,outlier_mixing_constants,
    integrated_outlier_ledger,source_case,certificate,
)
from gio_t3c_intrinsic_defect import (
    source_graph,typed_maps,direct_original_owner_conflicts,
)


def original_symbol_energy(m,labels,side):
    """Count edges through each literal original factor fiber, independently.

    Each original vertex has EXACTLY two distinct symbols, each symbol
    occurs at most a-1 times because the pair map is injective.
    Each collinear edge co-occurring in a symbol is counted precisely
    twice in the symmetric trace, not four or once.
    """
    nbr=m["neighbors_point" if side=="point" else "neighbors_line"]
    n=len(nbr)
    assert len(labels)==n and len(set(labels))==n
    a=max(x for pair in labels for x in pair)+1
    fib=[set() for _ in range(a)]
    for i,pair in enumerate(labels):
        assert len(pair)==2 and pair[0]!=pair[1]
        for symbol in pair:
            fib[symbol].add(i)
    assert sum(len(z) for z in fib)==2*n
    assert max(len(z) for z in fib)<=a-1
    trace=sum(sum(int(v in nbr[u]) for u in z for v in z)
              for z in fib)
    brute=sum(bool(set(labels[i])&set(labels[j]))
              for i in range(n) for j in nbr[i] if i<j)
    assert trace==2*brute
    return dict(trace=trace,e_col=brute,max_symbol_fiber=max(map(len,fib)),
                sum_symbol_fiber_squares=sum(len(z)**2 for z in fib),
                factor_incidence_row_degree=2)


def independent_double_missing_sign(m):
    """Construct actual ORIGINAL cross-component missing F without matrix code."""
    n=m["points"]
    L=len(m["lines"])
    assert n%2==0 and L%2==0
    p0,l0=n//2,L//2
    missing=set(m["missing"])
    expected={(p,l) for p in range(n) for l in range(L)
              if (p<p0)!=(l<l0)}
    assert missing==expected
    sign=[1 if p<p0 else -1 for p in range(n)]
    assert sum(sign)==0
    ftv=[sum(sign[p] for p in range(n) if (p,l) in missing)
         for l in range(L)]
    num=sum(x*x for x in ftv)
    den=sum(x*x for x in sign)
    assert Q(num,den)==p0*l0
    return dict(source_delta_L=l0,source_delta_P=p0,
                centered_F0_squared_Rayleigh=Q(num,den),
                source_original_missing_pairs=len(missing))


class TestG6D4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=certificate()
        cls.cases={(x["kind"],x["scheme"]):x
                   for x in cls.c["exact_source_inertia_finite_falsifiers"]}

    def test_01_proof_scope_not_unrestricted(self):
        a=self.c
        self.assertEqual(a["schema"],SCHEMA)
        self.assertEqual(a["parent_G6D1_FIX_HEAD"],PARENT_G6D1_FIX)
        self.assertEqual(a["claim"],
            "CONDITIONAL_T3_QUADRATIC_EXCESS_FEW_POSITIVE_OUTLIERS")
        self.assertTrue(a["novel_in_program_factor_incidence_trace_bound"])
        self.assertTrue(a["eigenvector_delocalization_NOT_required"])
        self.assertTrue(a["unconditional_quadratic_excess_T3_NOT_proved"])
        self.assertTrue(a["new_infinite_bad_gap_family_NOT_constructed"])
        self.assertTrue(a["prior_art_spectral_decomposition_and_inertia"])
        self.assertTrue(a["source_GQ_axiom_NOT_used"])

    def test_02_exact_rational_inertia_all_signs_and_two_by_two(self):
        tests=(
            ([[2]],(1,0,0)),
            ([[-2]],(0,1,0)),
            ([[0]],(0,0,1)),
            ([[0,1],[1,0]],(1,1,0)),
            ([[0,2,0],[2,0,0],[0,0,0]],(1,1,1)),
            ([[2,1],[1,2]],(2,0,0)),
            ([[3,0],[0,-4]],(1,1,0)),
            ([[0,Q(2,3)],[Q(2,3),0]],(1,1,0)),
            ([[0,1,0],[1,0,1],[0,1,0]],(1,1,1)),
            ([[-1,0,0],[0,0,2],[0,2,0]],(1,2,0)),
            ([[0,0,1],[0,0,0],[1,0,0]],(1,1,1)),
        )
        for M,expected in tests:
            z=exact_symmetric_inertia(M)
            self.assertEqual((z["positive"],z["negative"],z["zero"]),
                             expected)
            self.assertTrue(z["exact_rational_congruence"])
        self.assertGreater(
            exact_symmetric_inertia([[0,1],[1,0]])[
                "two_by_two_indefinite_pivots"],0)

    def test_03_inertia_fail_closed_on_malformed(self):
        for bad in ([],[[1,0]],[[1,2],[3,4]]):
            with self.assertRaises(ValueError):
                exact_symmetric_inertia(bad)
        for bad in (-1,Q(3,2),True):
            with self.assertRaises(ValueError):
                actual_outlier_count([{1},{0}],bad)
        with self.assertRaises(ValueError):
            actual_outlier_count([{1},set()],1)
        with self.assertRaises(ValueError):
            actual_outlier_count([{1},{1}],1)

    def test_04_real_GQ_and_Wenger_exceptional_counts(self):
        for k in ("W32","Qminus24","dualQminus42","wenger3","wenger5"):
            x=self.cases[k,"lex"]
            self.assertEqual(x["centered_point_inertia"][
                "centered_positive_outliers"],0)
            self.assertEqual(x["centered_line_inertia"][
                "centered_positive_outliers"],0)
            self.assertTrue(x["true_source_not_synthetic_missing_F"])
            self.assertTrue(x["no_GQ_completion"])

    def test_05_genuine_doubled_asymmetric_nonGQ_one_outlier_each(self):
        for k in ("doubleW32","doubleQminus24","doubleDualQminus42"):
            x=self.cases[k,"lex"]
            self.assertEqual(x["centered_point_inertia"][
                "centered_positive_outliers"],1)
            self.assertEqual(x["centered_line_inertia"][
                "centered_positive_outliers"],1)
            self.assertGreater(x["delta_line"],0)
            self.assertGreater(x["delta_point"],0)
            self.assertLessEqual(1,x["r"])

    def test_06_genuine_double_large_centered_norm_separates_kappa_one(self):
        for k in ("doubleW32","doubleQminus24","doubleDualQminus42"):
            src,maps=original_source_case(k)
            e=independent_double_missing_sign(src)
            self.assertEqual(e["centered_F0_squared_Rayleigh"],
                             src["excess_lines"]*src["excess_points"])
            self.assertGreater(e["centered_F0_squared_Rayleigh"],
                               min(src["s"],src["t"])**3)
            # This exact finite source passes new few-outlier gate even
            # though it fails the *fixed kappa=1* D2 operator gate.
            # The doubled construction has Delta=Theta(r^3) for a
            # variable-order family; NO infinite quadratic claim.
            z=self.cases[k,"lex"]
            self.assertLessEqual(z["centered_point_inertia"][
                "centered_positive_outliers"],z["r"])

    def test_07_independent_original_symbol_trace_for_lex_maps(self):
        for k in ("W32","Qminus24","dualQminus42","doubleW32",
                  "doubleQminus24","doubleDualQminus42","wenger3","wenger5"):
            src,maps=original_source_case(k)
            x=self.cases[k,"lex"]
            point=original_symbol_energy(src,maps["f"],"point")
            line=original_symbol_energy(src,maps["g"],"line")
            self.assertEqual(point["e_col"],x["actual_fixed_map_point_conflicts"])
            self.assertEqual(line["e_col"],x["actual_fixed_map_line_conflicts"])
            self.assertEqual(point["trace"],2*point["e_col"])
            self.assertEqual(line["trace"],2*line["e_col"])
            self.assertEqual(point["factor_incidence_row_degree"],2)
            self.assertEqual(line["factor_incidence_row_degree"],2)

    def test_08_actual_correlated_labels_without_independence(self):
        a=self.cases["wenger3","lex"]
        b=self.cases["wenger3","correlated"]
        self.assertEqual(a["original_source_flags"],b["original_source_flags"])
        self.assertEqual(a["centered_point_inertia"][
            "centered_positive_outliers"],b["centered_point_inertia"][
            "centered_positive_outliers"])
        self.assertEqual(a["centered_line_inertia"][
            "centered_positive_outliers"],b["centered_line_inertia"][
            "centered_positive_outliers"])
        src,maps=original_source_case("wenger3","correlated")
        self.assertEqual(
            direct_original_owner_conflicts(src,maps)["J"],
            b["actual_original_owner_conflicts"])

    def test_09_explicit_all_order_conflict_and_gram_envelopes(self):
        for x in self.c["exact_source_inertia_finite_falsifiers"]:
            r=x["r"];a=x["finite_source_constants"]
            j0=a["each_collinearity_conflict_j0"]
            g0=a["original_pencil_Gram_G0"]
            self.assertLessEqual(x["actual_fixed_map_point_conflicts"],j0*r**4)
            self.assertLessEqual(x["actual_fixed_map_line_conflicts"],j0*r**4)
            self.assertLessEqual(x["actual_original_owner_conflicts"],
                                 a["original_owner_conflict_J0"]*r**4)
            self.assertLessEqual(x["point_gram"]**2,g0*g0*r**11)
            self.assertLessEqual(x["line_gram"]**2,g0*g0*r**11)
            self.assertEqual(a["factor_incidence_norm_square_coefficient"],2)
            self.assertTrue(a["no_eigenvector_delocalization_assumption"])
            self.assertTrue(a["no_global_F0_operator_norm_assumption"])

    def test_10_fixed_before_source_constants_and_exact_cube(self):
        for b,C,ell,nu in ((1,3,2,1),(2,12,2,1),(1,3,2,0),
                           (3,0,2,0),(7,19,5,6)):
            a=outlier_mixing_constants(b,C,ell,nu)
            self.assertGreaterEqual(a["cubic_source_root0"]**3,
                                    4*(b+1)*C*C)
            self.assertEqual(a["each_collinearity_conflict_j0"],
                a["point_degree_k0"]*a["alphabet_a0"]
                +ell*a["source_V0"]
                +a["alphabet_a0"]*nu*a["exceptional_lambda_coefficient"])
            self.assertEqual(a["original_owner_conflict_J0"],
                             2*a["each_collinearity_conflict_j0"])
        for args in ((0,1,2,1),(1,-1,1,1),(1,1,-1,1),
                     (1,1,1,-1),(True,1,1,1),(1,1,1,0.2)):
            with self.assertRaises(ValueError):
                outlier_mixing_constants(*args)

    def test_11_formal_all_four_low_error_closure(self):
        for x in self.c["all_order_formal_ledgers"]:
            self.assertTrue(x["FORMAL_ONLY"])
            self.assertTrue(x["no_unrestricted_T3"])
            f=x["fixed_before_source"]
            self.assertEqual(x["source"]["outlier_count_nu"],
                             f["outlier_multiplicity_nu"])
            c=x["closure"]
            r=int(c["sufficient_r0"])
            eps=Q(c["eps"]);rho=Q(c["rho"])
            m=x["moments"];s=x["selector"]
            self.assertLessEqual(m["improper"],eps*r)
            self.assertLessEqual(m["E"]**2,eps*eps*r)
            self.assertLessEqual(m["blocker_D"]**8,eps**8*r)
            self.assertLessEqual(12*f["balance_b"]**2*rho*s["q3"]**2*m["L6"],
                                 eps*eps)
            self.assertTrue(c["four_LOW_errors_each_below_eps"])
            self.assertGreater(Q(c["delta"]),0)

    def test_12_refuse_to_call_source_parameters_an_existence_proof(self):
        for x in self.c["exact_source_inertia_finite_falsifiers"]:
            self.assertTrue(x["fixed_FAMILY_parameters_NOT_deduced_from_fixture"])
        for a in ((1,3,2,1,1,1),(1,3,2,1,Q(1),1),
                  (1,3,2,1,Q(1,2),Q(1)),(1,3,2,1,Q(1),Q(0))):
            with self.assertRaises(ValueError):
                integrated_outlier_ledger(*a)

    def test_13_real_source_gate_rejects_insufficient_exception_budget(self):
        with self.assertRaises(AssertionError):
            source_case("doubleW32",nu=0)
        # ell=0: ordinary positive q3 Wenger eigenvalue q=3 has
        # positive multiplicity >> 0; claiming NO exceptions is false.
        with self.assertRaises(AssertionError):
            source_case("wenger3",ell=0,nu=0)

    def test_14_independent_girth_fail_closed_not_synthetic_source(self):
        # C4 original incidences are rejected BEFORE any spectral test.
        src,maps=original_source_case("W32")
        lines=[set(line) for line in src["lines"]]
        p,q=next(iter(combinations(sorted(lines[0]),2)))
        shared=next(j for j in range(1,len(lines)) if p in lines[j])
        rem=next(v for v in lines[shared] if v!=p)
        lines[shared].remove(rem)
        lines[shared].add(q)
        with self.assertRaises(ValueError):
            source_graph(lines,src["points"],src["s"],src["t"])


if __name__=="__main__":
    unittest.main()
